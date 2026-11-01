# Export Claude Code session transcripts (JSONL) into readable markdown logs.
# Usage:  python -I tools/export_conversation.py <session.jsonl> [more.jsonl ...]
# Writes conversation/<date>-session-<id8>.md and copies the raw file into conversation/raw/ (gitignored).
import json, io, os, sys, shutil, datetime
NL = chr(10)
out_dir = "conversation"
raw_dir = os.path.join(out_dir, "raw")
os.makedirs(raw_dir, exist_ok=True)

def text_of(content):
    parts, tools = [], []
    if isinstance(content, str):
        return content, tools
    if isinstance(content, list):
        for b in content:
            if not isinstance(b, dict):
                continue
            t = b.get("type")
            if t == "text":
                parts.append(b.get("text", ""))
            elif t == "tool_use":
                tools.append(b.get("name", "?"))
    return NL.join(parts), tools

def is_system_noise(txt):
    head = txt[:300]
    return (head.startswith("<system-reminder>") or head.startswith("<task-notification>")
            or "[SYSTEM NOTIFICATION" in head or head.startswith("<local-command-"))

def export(session_file):
    sid = os.path.basename(session_file).replace(".jsonl", "")
    rows, first_ts = [], None
    for line in io.open(session_file, encoding="utf-8"):
        try:
            o = json.loads(line)
        except Exception:
            continue
        t = o.get("type")
        if t not in ("user", "assistant") or o.get("isMeta"):
            continue
        msg = o.get("message") or {}
        txt, tools = text_of(msg.get("content"))
        txt = txt.strip()
        ts = o.get("timestamp") or ""
        if first_ts is None and ts:
            first_ts = ts
        if t == "user":
            if not txt or is_system_noise(txt):
                continue
            rows.append(["Jonathan", ts, txt, []])
        else:
            if not txt and not tools:
                continue
            if not txt and rows and rows[-1][0] == "Claude":
                rows[-1][3].extend(tools)
                continue
            rows.append(["Claude", ts, txt, list(tools)])
    day = (first_ts or "")[:10] or "unknown-date"
    path = os.path.join(out_dir, day + "-session-" + sid[:8] + ".md")
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with io.open(path, "w", encoding="utf-8", newline=NL) as f:
        f.write("# Conversation log " + day + " (session " + sid + ")" + NL + NL)
        f.write("Exported from the Claude Code transcript on " + now + ". Messages between Jonathan and Claude in order. Tool calls are summarised as [tools: ...]; tool outputs are not included. The raw transcript is in conversation/raw/ (kept out of GitHub)." + NL + NL)
        f.write("Resume this exact session in Claude Code with:  claude --resume " + sid + NL + NL + "---" + NL + NL)
        for who, ts, txt, tools in rows:
            stamp = ts[:16].replace("T", " ") + " UTC" if ts else ""
            f.write("## " + who + "  " + stamp + NL + NL)
            if len(txt) > 6000:
                txt = txt[:6000] + NL + NL + "... [truncated here; the full text is in the raw transcript]"
            if txt:
                f.write(txt + NL + NL)
            if tools:
                seen = []
                for x in tools:
                    if not seen or seen[-1] != x:
                        seen.append(x)
                f.write("[tools: " + ", ".join(seen) + "]" + NL + NL)
    shutil.copy2(session_file, os.path.join(raw_dir, os.path.basename(session_file)))
    return path, len(rows)

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        p, n = export(arg)
        print(p, n, "messages")

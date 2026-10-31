# How to use 00 Claude (plain guide)

Read this first. It answers: is it running, how do I start or stop it, do I have to run Claude Code every
time, how do I watch it work in real time, and what to do when something says "log in to continue".

## 1. Is it running? Yes, in the cloud, by itself

The hourly **cloud routine** does the work. It runs in Anthropic's cloud 24 hours a day at 5 minutes past every
hour, even when this PC is off and even when no Claude Code window is open. You do **not** need to run Claude Code
for the system to work.

Claude Code (the terminal) is only for three things:
- watching a run happen in real time (section 4),
- changing what the labels do (section 5),
- continuing setup or tests with Claude (`CONTINUE.md`).

## 2. Start, stop, run now

| I want to | Do this |
|---|---|
| Stop everything | https://claude.ai/code/routines → "00 Claude — Gmail label worker" → turn it off. Or tell any Claude session: "pause the 00 Claude routine". |
| Start again | Same page → turn it on. Or: "resume the 00 Claude routine". |
| Run right now, without waiting for the hour | Same page → **Run now**. Or double-click `run-worker.cmd` in this folder (section 4). Or tell any Claude session: "run the 00 Claude worker now". |
| See what it did | Gmail: label `00 Claude/Review` (drafts waiting for you) and `00 Claude/Done`. Drive: `00 Claude/Outbox/<Client>/<date>/` and `00 Claude/Log/`. Routine page: every run and its summary. |
| Change the schedule | Routine page → schedule. Now: hourly at :05 UTC. Business hours only, for example 9:05 to 19:05 Toronto time Monday to Friday: `5 13-23 * * 1-5`. |

## 3. Daily use (what you actually do)

1. Open the email in Gmail.
2. Optional: reply to yourself in the thread with one line starting `Claude:` (what you want done).
3. Attachments: click **Add to Drive** → folder `00 Claude/Inbox`.
4. Apply a label: `00 Claude/Bank-Statements`, `TMI`, `ITN`, `Payroll`, `Reply`, `Calendar`, or just `00 Claude/Todo`.
5. Within the hour: a draft reply appears in the thread, files land in Drive, and the label becomes `Done` or
   `Review`. Open `Review`, read the draft, send it if you agree, change `Review` to `Done`.

Claude never sends anything. You press Send.

## 4. Watch Claude work in real time (three options)

**Option A: double-click `run-worker.cmd`** (in this folder). A window opens, Claude Code starts here, runs the
worker once on whatever is labelled, prints what it did, and stays open so you can type follow-up questions
("show me the draft", "why did it fail"). Close the window when done. Verified on 2026-10-31.

**Option B: double-click `watch-worker.cmd`.** Same, but it keeps checking every hour while the window stays open.
Close the window to stop. The cloud routine keeps running regardless. If it does not start looping by itself,
type this line into the window: `/loop 1h Follow docs/03-routine-prompt-cloud.md exactly and process the 00 Claude labels now.`

**Option C: claude.ai in the browser.** https://claude.ai/code/routines → the routine → **Run now**, then watch the
run on that page. Works from your phone too.

Options A and B need Claude Code to be logged in once (section 6).

## 5. Change what a label does

Edit `LABELS.md` in this folder (one section per label, plain language). Then double-click `open-claude.cmd` and
type:

```
sync LABELS.md to the Playbook
```

Claude updates the Playbook (`docs/02-playbook.md` and the Google Doc "Playbook" in Drive) and the change is live
at the next hourly run. You can also edit the Google Doc "Playbook" in Drive directly, from any device.

- Add a label: create it in Gmail nested under `00 Claude` (or ask Claude: "create the label 00 Claude/Invoices"),
  add a section for it in `LABELS.md`, sync.
- Pause a label: set its Status to `off` in `LABELS.md`, sync. Emails with that label are left alone.
- One-off instruction for a single email: reply to yourself in the thread with a line starting `Claude:`.

## 6. Logging in ("login to continue")

- **Claude Code (terminal):** if it shows a login prompt, type `/login`, press Enter, and sign in with the
  claude.ai account (jonathan@jonathanlcpa.ca) in the browser window that opens. Once; it stays logged in.
- **Connectors (Gmail, Drive, Calendar):** https://claude.ai/customize/connectors. If a run reports "missing a
  permission" or "insufficient scope", disconnect and reconnect Gmail there and allow every permission.
- **The cloud routine:** needs no login from you after it is created. If it stops working, open the routine page
  and read the last run's error.
- **Claude desktop app (optional, for the Desktop worker):** stays signed in; only matters for jobs labelled
  `Desktop` (Excel, QuickBooks, portals on this PC).

## 7. Where things are

| Thing | Where |
|---|---|
| This folder | `C:\Users\jonat\My Drive\00_Documents\00gmail and claude cowork` (GitHub: jonathanlee310/Test, branch `claude/wonderful-curie-g7sxtq`) |
| What each label does | `LABELS.md` (yours to edit); `docs/02-playbook.md` and the Google Doc "Playbook" (what the worker reads) |
| The worker's full instructions | `docs/03-routine-prompt-cloud.md` (cloud) and `docs/04-routine-prompt-desktop.md` (PC) |
| Setup state, ids, test results | `SETUP-STATUS.md` |
| Continue working with Claude | `CONTINUE.md` |
| Routine (start, stop, run now, history) | https://claude.ai/code/routines |
| Drive folder | https://drive.google.com/drive/folders/1h7kFsxC6Sls7524pK_xN094X7v9-Wfpf |
| Playbook Google Doc | https://docs.google.com/document/d/1xHihLL0E5JzLvfGOrLNPqHaN_jzw-neOXP7m00ecwlQ/edit |

## 8. Cost and safety in one breath

Hourly runs with nothing labelled finish in about 30 seconds and cost almost nothing. A run never sends email,
pays, files or signs; it only creates drafts, Drive files and calendar events. At most 5 emails per run.

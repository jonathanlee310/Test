# 00 Claude — email labels that get work done

Put a label under `00 Claude/…` on an email. Within the hour a scheduled Claude run picks it up, does the job,
puts the files in Google Drive, leaves a **draft** reply in the thread, and relabels the thread so you can see
the state at a glance. Claude never sends, files, pays or signs anything. You read the draft and press Send.

## Start here

- `HOW-TO-USE.md`: is it running, start and stop, run now, watch it in real time, logging in.
- `LABELS.md`: what each label tells Claude to do. Yours to edit; then say: sync LABELS.md to the Playbook.
- `CONTINUE.md`: pick up the setup and the tests with Claude where we left off.
- Double-click `run-worker.cmd` (run once, real time), `watch-worker.cmd` (every hour while the window is open) or `open-claude.cmd` (Claude Code in this folder).

## The big picture

```
            ┌──────────────── YOU: control panel = Gmail labels ─────────────────────────────────────┐
            │ Gmail (web/phone/Chrome)      Google Drive "00 Claude/"        Playbook (Google Doc)     │
            │ • add 00 Claude/Todo or a     • Inbox/  (Add-to-Drive files)   • label → job → output    │
            │   job label (Bank-Statements…)• Outbox/ (results by client)    • edit = change behaviour │
            │ • optional note "Claude: …"   • Log/    (one file per run)     • repo keeps the master   │
            └──────────┬──────────────────────────────┬──────────────────────────┬─────────────────────┘
                       │ labels                       │ files                    │ rules
            ┌──────────▼──────────────────────────────▼──────────────────────────▼─────────────────────┐
 BRAIN      │ CLOUD ROUTINE — claude.ai / Cowork, hourly, runs 24/7 even with the PC off               │
            │ 1 search labels  2 lock (Working)  3 read thread + your note + Playbook  4 pick job/skill  │
            │ 5 do the work in the cloud sandbox (xlsx/docx/pdf + finance skills)                        │
            │ 6 deliver: Outbox files + reply DRAFT in thread + calendar events + Log file               │
            │ 7 relabel: Done | Review | Desktop | Failed   8 notification (only if work happened)      │
            └───────┬───────────────────────────────┬──────────────────────────────┬───────────────────┘
                    │ files only                    │ needs the PC (Desktop label) │ web GUI
 HANDS      ┌───────▼─────────┐          ┌──────────▼───────────────────┐  ┌───────▼───────────────────┐
            │ Cloud sandbox   │          │ WINDOWS PC: Claude desktop   │  │ Claude in Chrome          │
            │ Excel/Word/PDF  │          │ app signed in, Computer use  │  │ your logged-in tabs: CRA, │
            │ generated →     │          │ on; hourly Cowork task       │  │ QBO, banks, Gmail web UI  │
            │ Drive + draft   │          │ drives Excel/Word/Acrobat/   │  │ (download attachments);   │
            │                 │          │ QuickBooks on Drive-synced   │  │ "run my queue now"        │
            │                 │          │ files; relabels Review/Done  │  │                           │
            └─────────────────┘          └──────────────────────────────┘  └───────────────────────────┘

Label state machine (labels are the database; all nested under "00 Claude")
(you) Todo / job label ─▶ Working ─┬─▶ Done
                                   ├─▶ Review  ─(you check the draft, send it, swap Review→Done)
                                   ├─▶ Desktop ─(PC run)─▶ Review / Done
                                   └─▶ Failed  ─(draft explains; fix it, remove Failed → picked up again)
Trigger rule: (Todo or any job label) AND no state label other than Todo.  Redo = remove the state label.
Lock: Working; a Working older than 2 hours is re-taken.
```

## How a job flows

1. **You label** an email with a job label (for example `00 Claude/Bank-Statements`) or with `00 Claude/Todo`.
   If the email has attachments, first click "Add to Drive" on them and choose the folder `00 Claude/Inbox`.
2. **Hourly pickup.** The cloud routine runs once an hour, finds the labelled threads (five at most per run) and
   marks each one `Working` so no second run touches it.
3. **Work.** Claude reads the whole thread, your optional `Claude:` note and the Playbook row for that label,
   then does the job with the account's skills (bank statements, TMI, ITN, payroll, replies, deadlines).
4. **Drive files and a draft.** Results go to `00 Claude/Outbox/<Client>/<date>/`. One draft reply is created
   in the thread (to you or to the client, as the Playbook row says). Deadlines become calendar events.
5. **Relabel.** `Todo` and `Working` come off; exactly one of `Done`, `Review`, `Desktop` or `Failed` goes on.
   The job label stays. A one-paragraph log file lands in `00 Claude/Log/`.
6. **You review.** Open the `Review` label, read the draft, send it if you agree, and change `Review` to `Done`.

## Label legend

| Label (under 00 Claude) | Colour | Meaning | Who sets it |
|---|---|---|---|
| Todo | blue | "Do the default job on this thread": summary, deadlines, draft reply | you |
| Bank-Statements, TMI, ITN, Payroll, Reply, Calendar | teal | Job labels: which Playbook row to run | you (or a Gmail filter) |
| Working | yellow | A run has this thread right now (lock) | Claude |
| Done | green | Finished; nothing for you to do | Claude (or you, after sending a Review draft) |
| Review | orange | Finished, but look before anything leaves the office: a draft is waiting | Claude |
| Desktop | purple | Needs Excel, Word, Acrobat, QuickBooks or a web portal on the PC; the desktop worker takes it next | Claude |
| Failed | red | Could not finish; the draft in the thread says why and what to do | Claude |

## Daily use

1. Open the email.
2. Optional: reply to yourself in the thread with one line that starts with `Claude:` saying what you want
   (for example `Claude: process this into a 2025 CSV with GIFI codes`).
3. Attachments: click **Add to Drive** on each one and choose `00 Claude/Inbox`.
4. Apply a job label (`00 Claude/Bank-Statements`, `TMI`, `ITN`, `Payroll`, `Reply`, `Calendar`) or just
   `00 Claude/Todo`.
5. Later, open `00 Claude/Review`: read the draft, send it, swap `Review` for `Done`.

## Where things live

| Thing | Where |
|---|---|
| Control panel | Gmail labels nested under `00 Claude` |
| Files in | Google Drive `00 Claude/Inbox` (what you add with "Add to Drive") |
| Files out | Google Drive `00 Claude/Outbox/<Client>/<date>/` |
| Run logs | Google Drive `00 Claude/Log/` (one small file per run or thread) |
| Job registry | Google Doc **Playbook** in Drive folder `00 Claude` (the hourly worker reads it); master copy `docs/02-playbook.md` in this repo |
| Worker prompts | `docs/03-routine-prompt-cloud.md` (cloud, hourly) and `docs/04-routine-prompt-desktop.md` (desktop, hourly while the app is open) |
| Scheduled tasks | 1) cloud routine "00 Claude — Gmail label worker" (claude.ai Routines, hourly, runs with the PC off); 2) Cowork task "00 Claude — desktop worker" (runs on this PC while the Claude desktop app is open) |
| This repo | github.com/jonathanlee310/Test, branch `claude/wonderful-curie-g7sxtq`; `SETUP-STATUS.md` says what is live |

## Pause, resume, redo

- **Pause**: disable the cloud routine (and the desktop task). Nothing else is needed.
- **Resume**: enable it again; threads labelled in the meantime are picked up at the next run.
- **Redo a thread**: remove its state label (`Done`, `Review`, `Failed` or `Desktop`); it is picked up again within the hour.

## Changing the work

- Edit the **Playbook** Google Doc: add, change, pause (Status = off) or remove a row. A new job also needs a Gmail label `00 Claude/<Name>`.
- Or ask Claude in any session (claude.ai, desktop app, Chrome side panel, terminal): "add / change / pause / remove the <Name> job in the Playbook" (full prompt in `docs/06-manage-jobs.md`).
- Or, for one email only, put a `Claude:` note in the thread. All three are live at the next hourly run; no prompt or code changes.

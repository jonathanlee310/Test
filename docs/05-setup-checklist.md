# Setup checklist

## A. claude.ai (once)
- [x] Connectors: Gmail, Google Drive, Google Calendar connected at https://claude.ai/customize/connectors.
      Gmail: allow every permission (reading, drafting, labels). Reconnect if "missing a permission" ever appears.
      (2026-10-31: Gmail reconnected with all permissions; create_label works.)
- [x] Cloud routine "00 Claude — Gmail label worker": hourly, connectors on, prompt = docs/03-routine-prompt-cloud.md.
      (2026-10-31: created, id trig_01HU9VtehUJKPE8BxHXrpVdr, hourly at :05 UTC, https://claude.ai/code/routines/trig_01HU9VtehUJKPE8BxHXrpVdr)
      (Claude desktop app → Cowork → /schedule, or claude.ai → Claude Code → Routines.)

## B. Gmail (once)
- [x] 12 labels nested under 00 Claude (Todo, Working, Review, Done, Desktop, Failed, Bank-Statements, TMI, ITN,
      Payroll, Reply, Calendar), coloured as in README.
- [ ] Optional: a Gmail filter that auto-applies 00 Claude/Bank-Statements to statement emails from your banks.

## C. Google Drive (once)
- [x] Folder 00 Claude with Inbox, Outbox, Log, and the Google Doc "Playbook".
- [ ] Google Drive for desktop installed on the PC; 00 Claude syncing; local path written in the Playbook.

## D. Windows PC (once)
- [ ] Claude desktop app installed and signed in; Settings → This computer → Computer use: on; Excel, Word,
      Acrobat, QuickBooks granted when asked.
- [ ] Claude in Chrome installed and signed in.
- [ ] Cowork scheduled task "00 Claude — desktop worker": hourly, prompt = docs/04-routine-prompt-desktop.md.
- [ ] Leave the desktop app running (it is the only thing that needs the PC).

## E. Daily use
1. Open the email. If needed, reply to yourself with one line starting "Claude:" (what you want done).
2. Attachments: click "Add to Drive" → 00 Claude/Inbox.
3. Apply a job label (or 00 Claude/Todo).
4. Within the hour: files in Outbox/<Client>/<date>/, a draft in the thread, label Done or Review.
5. Review: read the draft, send it, change Review → Done.

## F. Control
- Pause everything: disable the routine (and the desktop task). Resume: enable it.
- Run now: ask any Claude session "run the 00 Claude worker now", or in Claude Code: /loop 1h … (see README).
- Redo a thread: remove its state label (Done/Review/Failed/Desktop).
- Change behaviour: edit the Playbook Google Doc (or docs/02-playbook.md, then paste it into the doc).
- Add a job: create label 00 Claude/<Name> + add a Playbook row with Status = on. Live within the hour.
- Pause a job: Status = off. Remove a job: delete the row. Change a job: edit the row or its Job details.
- Or just tell Claude in any session: "add / change / pause / remove the <Name> job in the Playbook".

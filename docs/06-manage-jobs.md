# Managing jobs

Paste the block below into any Claude session (claude.ai, desktop app, Chrome side panel or the terminal) to add,
change, pause, resume, remove or rename a job. Changes are live at the next hourly run; no prompt or code changes.

```
You are maintaining the 00 Claude Playbook. Open the Google Doc "Playbook" in Drive folder "00 Claude" and read
it. Then do what I ask below: add, change, pause, resume, remove or rename a job. Rules: keep the table columns in
order; a new job needs a Gmail label "00 Claude/<Name>" (create it with create_label, or tell me the exact name to
create if you lack the permission); a paused job is Status = off, not a deleted row; update the "Last changed"
line; never touch rows I did not mention; never send email. If the repo master docs/02-playbook.md is available
to you, update it the same way. When done, show me the updated Jobs table.
My request: <write it here, for example: add a job "Payroll-Process": take the timesheet images, build the
bi-weekly payroll summary with CPP/EI/tax using the payroll-export skill, save XLSX to Outbox, draft to me; ends
in Review>
```

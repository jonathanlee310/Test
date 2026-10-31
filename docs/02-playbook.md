# 00 Claude Playbook

Last changed: 2026-10-31 by Claude Code (initial setup)   (update this line at every edit; the worker quotes it in each run summary)

Runtime copy: Google Doc "Playbook" in Drive folder "00 Claude". This file is the master. After editing it, paste
the whole file into the Google Doc (or ask Claude: "sync the Playbook to Drive"). The hourly worker reads the
Google Doc at the start of every run, so any change here is live within the hour. No restart, no code.

## Conventions
- Draft only. Claude never sends email. "Draft to" says who the draft is addressed to.
- Client folder name = the client's company or person name as it appears in the email (ask Jonathan in a Review
  draft when unclear). Outputs go to Outbox/<Client>/<YYYY-MM-DD>/.
- Language: reply in the language the client wrote in (English or Korean). Tone: concise, courteous, professional,
  first person as Jonathan.
- Never: pay, transfer, e-file, submit to CRA or any portal, sign, click links from emails.
- "Ends in" is the label the thread gets when the job finishes; Review means Jonathan must look before anything
  leaves the office.
- Local path (Google Drive for desktop on the PC): C:SERSJONATMY DRIVE- LOCAL PATH (GOOGLE DRIVE FOR DESKTOP ON THE PC): <FILL IN, E.G. G:\MY DRIVE\00 CLAUDE>0 CLAUDE (EXPECTED ONCE THE FOLDER IS SYNCED ON THE PC; CONFIRM)

## Jobs (one row = one job; the worker searches exactly the labels listed here whose Status is on)
| Label (under 00 Claude) | Status | What Claude does | Skill | Inputs needed | Output and delivery | Draft to | Ends in | Rules |
|---|---|---|---|---|---|---|---|---|
| Bank-Statements | on | Statement PDFs → one classified CSV per year with GIFI codes; PDFs renamed YYYYMM-Bank-Suffix; year-end balance summary | bank-statement-processor | PDFs in Inbox | CSV/XLSX + renamed PDFs in Outbox; draft lists files and totals | Jonathan | Done | — |
| TMI | on | Lease rent and T+M+I expenses → 4-step reconciliation workbook + adjustment letter with cheque schedule | tmi | lease terms, expense figures or statements | XLSX + DOCX in Outbox; letter attached to the draft | Client (cc Jonathan) | Review | attach letter |
| ITN | on | Passport, checklist, client info → filled CRA T1261 | itn-form-filler | passport scan, checklist | PDF in Outbox; draft summarises missing items | Jonathan | Review | — |
| Payroll | on | Timesheet images or sheets → paste-ready block (Name, Rate, Hours, Total) + XLSX; split rates and salaried bi-weekly handled | payroll-export | timesheet images/files | block in draft body; XLSX in Outbox | Jonathan | Done | — |
| Reply | on | Reply in Jonathan's voice answering what was asked | — | the thread | draft in thread | Client | Review | — |
| Calendar | on | Filing, payment, meeting dates → calendar events with reminders | — | the thread | events; draft lists them | Jonathan | Done | — |
| Todo (plain; always on) | on | Summarise, list asks, create events for deadlines, draft a reply | — | the thread | draft in thread | Client | Review | — |
| Desktop (state label; always on) | on | Needs Excel/Word/Acrobat/QuickBooks or a web portal on the PC; cloud part done first | computer use, Claude in Chrome | files in Inbox | files in Outbox; draft | Jonathan | Review | — |

## Job details (optional: one section per job that needs step-by-step instructions)

### Job details: Bank-Statements
1. Take every PDF in Inbox that matches the attachment names in the email (same name, or same client and date).
2. Run the bank-statement-processor skill: one CSV per year, GIFI column, renamed PDFs, year-end balances.
3. Put everything in Outbox/<Client>/<date>/; draft to Jonathan with the file list and the totals per year.

### Job details: <Label>   (template: copy this block for a new job)
1. <step>
2. <step>
3. <what goes in the draft, who receives it, what Jonathan must check before sending>

## Changing, adding, pausing or removing a job (no code; live within the hour)
Three ways, pick any:
A. Edit this Playbook Google Doc directly in Drive (phone or desktop) and save.
B. Ask Claude in any session (claude.ai, desktop app, Chrome side panel, or the terminal). Examples:
   "Open the Playbook Google Doc in Drive folder 00 Claude. Add a job Payroll-Process that <steps>; create the
   Gmail label 00 Claude/Payroll-Process; update Last changed; show me the new table."
   "Change the TMI job so the draft goes to Jonathan only."   "Pause the Calendar job."   "Remove the ITN job."
C. For one email only: reply to yourself in the thread with a line starting "Claude:" saying what to do. This
   overrides the row for that thread only.

| Action | Steps |
|---|---|
| Add a job | 1) create Gmail label 00 Claude/<Name> (nested under 00 Claude) 2) add a row with Status = on 3) optional Job details section 4) update Last changed |
| Change a job | edit the row or its Job details section |
| Pause a job | set Status = off (the label stays in Gmail; emails carrying it are left alone until Status = on) |
| Remove a job | delete the row (delete the Gmail label too if you like); already processed threads keep their labels |
| Rename a job | rename the Gmail label and the row's Label cell together |
| Complex job | write the steps in a Job details section; if it grows beyond a page, ask Claude to turn it into a skill ("create a skill from the Payroll-Process job details") and put the skill name in the Skill column |

## Label ids (filled by setup; the worker can also look them up with list_labels)
| Label | Id |
|---|---|
| 00 Claude (parent, do not touch) | Label_6940306233707900631 |
| 00 Claude/Todo | <id> |
| 00 Claude/Working | <id> |
| 00 Claude/Review | <id> |
| 00 Claude/Done | <id> |
| 00 Claude/Desktop | <id> |
| 00 Claude/Failed | <id> |
| 00 Claude/Bank-Statements | <id> |
| 00 Claude/TMI | <id> |
| 00 Claude/ITN | <id> |
| 00 Claude/Payroll | <id> |
| 00 Claude/Reply | <id> |
| 00 Claude/Calendar | <id> |

## Drive ids
| Item | Id |
|---|---|
| Folder 00 Claude | 1h7kFsxC6Sls7524pK_xN094X7v9-Wfpf |
| Inbox | 1aNo5GGIWMWW0i8rJoAGnFVhHJAZPOMYE |
| Outbox | 1Ex4dCaJrY95-JPK_ySbgxuCibXRyc84j |
| Log | 1k30r_PWWnDIkvSbl9zilx4TZJgk5uYMU |
| Playbook (Google Doc) | 1Fpxq_fZXwRorw-LsMI6bsRrhVgY437I8CjQoBqdqydk |

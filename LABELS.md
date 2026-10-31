# LABELS.md — what each label tells Claude to do

This is your file. Write, in plain language, what Claude should do when you put each label on an email. One
section per label. Edit anything, then tell Claude: **"sync LABELS.md to the Playbook"**. Claude copies it into
`docs/02-playbook.md` and the Google Doc "Playbook" that the hourly worker reads, so it is live at the next run.

Last changed: 2026-10-31 by Claude Code (prefilled with the setup defaults; Jonathan to edit)

## How to fill a section
- **Status**: `on` = Claude acts on this label. `off` = emails with this label are left alone (paused).
- **What Claude does**: the job in one or two sentences.
- **Inputs**: what Claude needs: attachments added to Drive Inbox, the email text, a client name...
- **Output**: files to produce and where. Default place: `Outbox/<Client>/<date>/` in Drive folder `00 Claude`.
- **Draft to**: who the draft reply is addressed to: `Jonathan`, or `client` (add "cc Jonathan" if you like).
- **Ends in**: the label when finished: `Done` (nothing to check) or `Review` (look before anything leaves).
- **Rules**: anything extra: "attach the letter", "always in Korean", "ask me first if the year is unclear".
- **Step by step**: optional numbered steps for jobs that need precision.

The state labels (`Working`, `Review`, `Done`, `Desktop`, `Failed`) are not jobs and need no section: Working = Claude
is on it, Review/Done = finished, Desktop = needs this PC, Failed = read the draft in the thread.

---

## Todo (the default job, used when no job label is applied)
- Status: on
- What Claude does: summarise the thread, list what is being asked, create calendar events for any deadline,
  and draft a reply to the client.
- Inputs: the email thread.
- Output: draft in the thread; calendar events.
- Draft to: client
- Ends in: Review
- Rules:
- Step by step:

## Bank-Statements
- Status: on
- What Claude does: turn bank-statement PDFs into one classified transaction CSV per year with GIFI codes, rename
  the PDFs `YYYYMM-Bank-Suffix`, and give a year-end balance summary.
- Inputs: the statement PDFs added to Drive Inbox (Add to Drive).
- Output: CSV/XLSX and renamed PDFs in `Outbox/<Client>/<date>/`.
- Draft to: Jonathan
- Ends in: Done
- Rules:
- Step by step:
  1. Take every PDF in Inbox that matches the attachment names in the email (same name, or same client and date).
  2. Run the bank-statement-processor skill: one CSV per year, GIFI column, renamed PDFs, year-end balances.
  3. Put everything in `Outbox/<Client>/<date>/`; draft to Jonathan with the file list and the totals per year.

## TMI
- Status: on
- What Claude does: from the lease rent and the T+M+I (taxes, maintenance, insurance) expense figures, build the
  4-step TMI reconciliation workbook and the adjustment letter with the cheque schedule.
- Inputs: lease terms, expense figures or statements (in the email or added to Inbox).
- Output: XLSX and DOCX in `Outbox/<Client>/<date>/`; the letter attached to the draft.
- Draft to: client, cc Jonathan
- Ends in: Review
- Rules: attach the letter
- Step by step:

## ITN
- Status: on
- What Claude does: from the passport scan, the checklist and the client information, fill the CRA T1261
  (Individual Tax Number application).
- Inputs: passport scan and checklist in Inbox; client details in the email.
- Output: filled PDF in `Outbox/<Client>/<date>/`; the draft lists anything still missing.
- Draft to: Jonathan
- Ends in: Review
- Rules:
- Step by step:

## Payroll
- Status: on
- What Claude does: from timesheet images or sheets, produce the paste-ready block (Name, Rate, Hours, Total)
  and an XLSX; handle split rates and salaried bi-weekly employees.
- Inputs: timesheet images or files in Inbox (or in the email body).
- Output: the block in the draft body; XLSX in `Outbox/<Client>/<date>/`.
- Draft to: Jonathan
- Ends in: Done
- Rules:
- Step by step:

## Reply
- Status: on
- What Claude does: write a reply in Jonathan's voice that answers what the client asked (concise, courteous,
  professional, same language as the client: English or Korean).
- Inputs: the email thread.
- Output: draft in the thread.
- Draft to: client
- Ends in: Review
- Rules:
- Step by step:

## Calendar
- Status: on
- What Claude does: find filing, payment and meeting dates in the email and create calendar events with reminders.
- Inputs: the email thread.
- Output: calendar events; the draft lists them.
- Draft to: Jonathan
- Ends in: Done
- Rules:
- Step by step:

## Hello (test label created during setup; keep it off, or delete this section and the Gmail label when done)
- Status: off
- What Claude does: reply with a one-line friendly greeting (used only to test that a new label works).
- Inputs: the email thread.
- Output: draft in the thread.
- Draft to: Jonathan
- Ends in: Review
- Rules:
- Step by step:

## <New label name>  (copy this block; also create the Gmail label `00 Claude/<Name>` nested under 00 Claude)
- Status: on
- What Claude does:
- Inputs:
- Output:
- Draft to:
- Ends in:
- Rules:
- Step by step:

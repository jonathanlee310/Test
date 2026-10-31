# SETUP-STATUS — 00 Claude Gmail-label worker

Updated: 2026-10-31 by Claude Code (setup session on Jonathan's PC, repo folder
`C:\Users\jonat\My Drive\00_Documents\00gmail and claude cowork`).

Legend: **done** = finished by this session · **manual** = Jonathan must do it · **waiting** = blocked on a manual step.

## Phase checklist

| Phase | Status | Notes |
|---|---|---|
| 0 Ground rules | done | Repo `jonathanlee310/Test` cloned into the folder above; branch `claude/wonderful-curie-g7sxtq`. |
| 1 Preflight | done | Gmail, Google Drive and Google Calendar connectors all respond. Git remote confirmed; the repo is public. |
| 2 Gmail labels | done | First attempt failed (the Gmail grant lacked the label scope). After Jonathan reconnected Gmail with all permissions, all 12 labels were created and coloured with `create_label` on 2026-10-31; ids below. |
| 3 Drive layout | done (one manual item) | `Inbox`, `Outbox`, `Log` and the Google Doc `Playbook` created under `00 Claude`; the Playbook doc was re-created with the label ids once the labels existed (the Drive connector cannot edit a doc in place); ids below. Manual: make Google Drive for desktop sync `00 Claude` and confirm the local path. |
| 4 Repo documents | done | `README.md`, `docs/01-architecture.md`, `docs/02-playbook.md`, `docs/03-routine-prompt-cloud.md`, `docs/04-routine-prompt-desktop.md`, `docs/05-setup-checklist.md`, `docs/06-manage-jobs.md`. |
| 5.1 Cloud routine | done | Routine **"00 Claude — Gmail label worker"** created: hourly at :05 UTC, fresh cloud session each run, model Opus 5.5, connectors Gmail + Google-Drive + Google-Calendar, prompt = `docs/03-routine-prompt-cloud.md` verbatim. Id `trig_01HU9VtehUJKPE8BxHXrpVdr`. Runs with the PC off. Manage, pause or change the schedule at https://claude.ai/code/routines/trig_01HU9VtehUJKPE8BxHXrpVdr PAUSED (enabled = false) at 18:58 UTC on 2026-10-31 for the Phase 6 tests so the hourly run does not grab the test emails; re-enable when the tests are done. |
| 5.2 Desktop worker | **manual** | Needs the Claude desktop app on this PC; steps below. |
| 5.3 Command-line mode | done | Instructions below and in README. |
| 6.1 Smoke test | done | See "Test results". |
| 6.2 End to end | waiting | Needs the labels plus one bank-statement email from Jonathan. |
| 6.3 Safety | waiting | Needs the labels. |
| 6.4 Flexibility | waiting | Needs the labels. Note: the Drive connector cannot edit a Google Doc's text (`update_file` is metadata only), so the "Status = off" test will be done by creating a replacement Playbook doc and renaming the old one; nothing is deleted. |
| 7 Commit and push | done | Pushed to `origin/claude/wonderful-curie-g7sxtq`. Will be pushed again after the label steps. |

## Ids discovered

| Item | Id |
|---|---|
| Gmail label `00 Claude` (parent, never modified) | `Label_6940306233707900631` |
| Gmail labels under `00 Claude` (12) | Todo = `Label_120`, Working = `Label_121`, Review = `Label_122`, Done = `Label_123`, Desktop = `Label_124`, Failed = `Label_125`, Bank-Statements = `Label_126`, TMI = `Label_127`, ITN = `Label_128`, Payroll = `Label_129`, Reply = `Label_130`, Calendar = `Label_131` |
| Drive folder `00 Claude` | `1h7kFsxC6Sls7524pK_xN094X7v9-Wfpf` |
| Drive folder `00 Claude/Inbox` | `1aNo5GGIWMWW0i8rJoAGnFVhHJAZPOMYE` |
| Drive folder `00 Claude/Outbox` | `1Ex4dCaJrY95-JPK_ySbgxuCibXRyc84j` |
| Drive folder `00 Claude/Log` | `1k30r_PWWnDIkvSbl9zilx4TZJgk5uYMU` |
| Google Doc `Playbook` (current, re-synced 2026-10-31 with label ids) | `1xHihLL0E5JzLvfGOrLNPqHaN_jzw-neOXP7m00ecwlQ` - https://docs.google.com/document/d/1xHihLL0E5JzLvfGOrLNPqHaN_jzw-neOXP7m00ecwlQ/edit |
| First Playbook doc (superseded, renamed `archived-pb-2026-10-31-initial` and moved into Log; safe to delete) | `1Fpxq_fZXwRorw-LsMI6bsRrhVgY437I8CjQoBqdqydk` |
| Cloud routine "00 Claude — Gmail label worker" | `trig_01HU9VtehUJKPE8BxHXrpVdr` — https://claude.ai/code/routines/trig_01HU9VtehUJKPE8BxHXrpVdr |
| Routine environment | `env_01EpkLNdKzLJ3oRf7nUAnpgG` (Default, Anthropic cloud) |

## What Jonathan still has to do

### 1. Gmail labels: DONE
All 12 labels exist (created by Claude after the Gmail reconnect on 2026-10-31). Nothing to do.

### 2. Google Drive for desktop
Google Drive for desktop is already running on this PC, but the Drive folder 00 Claude is not in its local mirror yet. In Drive for desktop (Settings, Google Drive, My Drive) make 00 Claude sync, then write the local path
(expected path: see Findings below) into the Playbook under Local path (Google Doc and docs/02-playbook.md).

### 3. Desktop worker (needs this PC: Excel, Word, Acrobat, QuickBooks, web portals)
1. Claude desktop app → Settings → This computer → **Computer use: on**. Grant Excel, Word, Acrobat, QuickBooks
   when asked. Install **Claude in Chrome** (Chrome Web Store) and sign in.
2. Desktop app → Cowork → `/schedule` → Hourly → paste the prompt from `docs/04-routine-prompt-desktop.md`.
   Because it needs local apps, it runs on this PC while the app is open and signed in. Leave the app running.
3. Google Drive for desktop must be syncing `00 Claude` (step 2).

### 4. Cloud routine notes
- The routine is already enabled and runs 24 times a day. A run with no labelled email answers "No items." and
  costs almost nothing. To limit it to business hours, change the schedule at the routine link above
  (for example `5 13-23 * * 1-5` = 9:05 to 19:05 Toronto time, Monday to Friday, in UTC).
- Push notifications: run results appear in claude.ai under Routines; turn on notifications there if wanted.
- The routine's cloud session clones this repo. Skills placed under `.claude/skills/` in this repo become
  available to the worker; the claude.ai account skills (bank-statement-processor, tmi, itn-form-filler,
  payroll-export, xlsx, docx, pdf) are used when the cloud session exposes them.

### 5. Command-line mode (this terminal)
- Run the worker once right now: paste the prompt from `docs/03-routine-prompt-cloud.md` as a message in a
  Claude Code session that has the Gmail, Drive and Calendar connectors.
- Keep it checking hourly while the terminal is open:
  `/loop 1h Follow docs/03-routine-prompt-cloud.md exactly and process the 00 Claude labels now.`
- Stop with Ctrl+C or by closing the terminal; the cloud routine keeps running regardless.

## Test results

| Test | Result |
|---|---|
| 2.5 label_thread sanity | PASS: applied the parent label id to a thread that already carried it (no-op); the call succeeded, nothing changed. |
| 2.x create_label after reconnect | PASS: 12 labels created and coloured in one go (Label_120 to Label_131); test label 00 Claude/Hello also created for test 6.4. |
| 6.1 Smoke (this session) | PASS: both search syntaxes (hyphenated and quoted) returned zero threads; the worker answers "No items."; nothing changed in Gmail or Drive. |
| 6.1 Smoke (cloud routine, first scheduled fire 2026-10-31 14:05 UTC) | PASS: fired 14:05:39 UTC, session cse_019v5M4UifSLAT9DkN2LdHGy, 32 s, 11 turns; cloned the repo, read the Playbook doc, called list_labels, ran both search syntaxes (zero results), sent a push notification that the sub-labels are missing, answered "No items."; nothing changed in Gmail or Drive. |
| 6.2 End to end | not run yet (needs labels and a bank-statement email) |
| 6.3 Safety | not run yet (needs labels) |
| 6.4 Flexibility | not run yet (needs labels) |

## Known limitations found during setup
- Gmail connector: the original grant had no label-management permission (create_label, update_label failed). Fixed on 2026-10-31 by reconnecting Gmail at claude.ai/customize/connectors with all permissions; all label tools work now.
- Drive connector: `update_file` changes metadata only, so the Playbook Google Doc cannot be edited by Claude in
  place. Re-sync = create a new doc named `Playbook` and rename the old one (never deleted).
- Bash tool on this PC: heredocs containing apostrophes fail; files were written with the Write tool instead.

## Findings from the first cloud run (2026-10-31 14:05 UTC)
- The cloud session sees the connectors as mcp__Gmail__*, mcp__Google-Drive__* and mcp__Google-Calendar__* and loads them with ToolSearch; the routine configuration works as created.
- Drive title search is fuzzy: searching for folder "00 Claude" also returned the Drive mirror of this working folder ("00gmail and claude cowork"), and searching for "Playbook" also returned docs/02-playbook.md. The worker still read the right Playbook (id above) because the Playbook lists the exact Drive ids; keep that table current.
- This working folder sits inside the Google Drive for desktop mirror (Drive: Computers > 2025 Legion > 00_Documents > 00gmail and claude cowork), so the repo clone, including .git, is backed up to Drive. Harmless, but do not move the folder while Drive is syncing.
- Google Drive for desktop is running on this PC (GoogleDriveFS.exe) and mirrors C:\Users\jonat\My Drive, but the Drive folder 00 Claude is not in that mirror yet. Expected local path once synced: C:\Users\jonat\My Drive\00 Claude.

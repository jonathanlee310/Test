# SETUP-STATUS — 00 Claude Gmail-label worker

Updated: 2026-10-31 by Claude Code (setup session on Jonathan's PC, repo folder
`C:\Users\jonat\My Drive\00_Documents\00gmail and claude cowork`).

Legend: **done** = finished by this session · **manual** = Jonathan must do it · **waiting** = blocked on a manual step.

## Phase checklist

| Phase | Status | Notes |
|---|---|---|
| 0 Ground rules | done | Repo `jonathanlee310/Test` cloned into the folder above; branch `claude/wonderful-curie-g7sxtq`. |
| 1 Preflight | done | Gmail, Google Drive and Google Calendar connectors all respond. Git remote confirmed; the repo is public. |
| 2 Gmail labels | **manual** | `create_label` fails for every label with "Insufficient scope" (the Gmail connector grant has no label-management permission). The 12 labels must be created by Jonathan, or the Gmail connector reconnected with all permissions (see "What Jonathan still has to do"). The label-id table and the `label_thread` sanity test wait for that. |
| 3 Drive layout | done (one manual item) | `Inbox`, `Outbox`, `Log` and the Google Doc `Playbook` created under `00 Claude`; ids below. Manual: install Google Drive for desktop, sync `00 Claude`, write the local path into the Playbook. |
| 4 Repo documents | done | `README.md`, `docs/01-architecture.md`, `docs/02-playbook.md`, `docs/03-routine-prompt-cloud.md`, `docs/04-routine-prompt-desktop.md`, `docs/05-setup-checklist.md`, `docs/06-manage-jobs.md`. |
| 5.1 Cloud routine | done | Routine **"00 Claude — Gmail label worker"** created: hourly at :05 UTC, fresh cloud session each run, model Opus 5.5, connectors Gmail + Google-Drive + Google-Calendar, prompt = `docs/03-routine-prompt-cloud.md` verbatim. Id `trig_01HU9VtehUJKPE8BxHXrpVdr`. Runs with the PC off. Manage, pause or change the schedule at https://claude.ai/code/routines/trig_01HU9VtehUJKPE8BxHXrpVdr |
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
| Gmail labels `00 Claude/Todo` … `00 Claude/Calendar` (12) | not created yet (see manual step 1) |
| Drive folder `00 Claude` | `1h7kFsxC6Sls7524pK_xN094X7v9-Wfpf` |
| Drive folder `00 Claude/Inbox` | `1aNo5GGIWMWW0i8rJoAGnFVhHJAZPOMYE` |
| Drive folder `00 Claude/Outbox` | `1Ex4dCaJrY95-JPK_ySbgxuCibXRyc84j` |
| Drive folder `00 Claude/Log` | `1k30r_PWWnDIkvSbl9zilx4TZJgk5uYMU` |
| Google Doc `Playbook` | `1Fpxq_fZXwRorw-LsMI6bsRrhVgY437I8CjQoBqdqydk` — https://docs.google.com/document/d/1Fpxq_fZXwRorw-LsMI6bsRrhVgY437I8CjQoBqdqydk/edit |
| Cloud routine "00 Claude — Gmail label worker" | `trig_01HU9VtehUJKPE8BxHXrpVdr` — https://claude.ai/code/routines/trig_01HU9VtehUJKPE8BxHXrpVdr |
| Routine environment | `env_01EpkLNdKzLJ3oRf7nUAnpgG` (Default, Anthropic cloud) |

## What Jonathan still has to do

### 1. Gmail labels (blocks everything else)
Pick one of the two:

**Option A, quickest:** reconnect Gmail at https://claude.ai/customize/connectors and allow every permission
(including managing labels), restart Claude Code, then tell Claude "retry labels". Claude then creates and
colours all 12 in one go.

**Option B, by hand in Gmail:** Settings → See all settings → Labels → Create new label → name (for example `Todo`)
→ tick "Nest label under" → choose `00 Claude` → Create. Colour each one from the label's ⋮ menu. Create these 12:

| Name (under 00 Claude) | Colour |
|---|---|
| Todo | blue |
| Working | yellow |
| Review | orange |
| Done | green |
| Desktop | purple |
| Failed | red |
| Bank-Statements | teal |
| TMI | teal |
| ITN | teal |
| Payroll | teal |
| Reply | teal |
| Calendar | teal |

Then say **"labels done"**. Claude verifies with `list_labels`, fills the ids into `docs/02-playbook.md` and this
file, re-syncs the Playbook Google Doc, runs the `label_thread` sanity test, and continues with the Phase 6 tests.

### 2. Google Drive for desktop
Install Google Drive for desktop on this PC, make sure `00 Claude` syncs, and write the local path (for example
`G:\My Drive\00 Claude`) into the Playbook under "Local path" (Google Doc and `docs/02-playbook.md`).

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
| 6.1 Smoke (this session) | PASS: both search syntaxes (hyphenated and quoted) returned zero threads; the worker answers "No items."; nothing changed in Gmail or Drive. |
| 6.1 Smoke (cloud routine, first scheduled fire 2026-10-31 14:05 UTC) | PENDING |
| 6.2 End to end | not run yet (needs labels and a bank-statement email) |
| 6.3 Safety | not run yet (needs labels) |
| 6.4 Flexibility | not run yet (needs labels) |

## Known limitations found during setup
- Gmail connector: no label-management permission in the current grant (`create_label`, `update_label` fail).
  Applying existing labels (`label_thread`) uses a different permission and is expected to work; verified once
  the labels exist.
- Drive connector: `update_file` changes metadata only, so the Playbook Google Doc cannot be edited by Claude in
  place. Re-sync = create a new doc named `Playbook` and rename the old one (never deleted).
- Bash tool on this PC: heredocs containing apostrophes fail; files were written with the Write tool instead.

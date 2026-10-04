# Incident Response Runbook: Cloud Credential Compromise Exposing Subscriber Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent B2B SaaS software publisher) |
| Tier / Vertical | Sole Proprietorship / Information |
| Incident type | Cloud credential compromise exposing customer data: a malicious development package on the laptop steals the plaintext `.env` file, and the attacker uses the hosting API token and database connection string to copy the production database and photo storage |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Related risks and POA&M | P01 R-001 (Very High), R-013; P07 POAM-001, POAM-007, POAM-008 |
| Owner and approver | Owner-developer, 2026-09-25 |
| Last tested | Not yet. Walkthrough with the contract security consultant due 2026-10-31 (POAM-008) |

Keep a copy of this runbook, the notification matrix, and the contact sheet **outside the company's own systems** (printed, and in the password manager's secure notes). Assume the laptop and anything it was signed in to are in the attacker's hands: **work from the phone and a clean device.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Contract security consultant | Second pair of hands: evidence capture, log review, persistence check | Hour 0 |
| Breach counsel (privacy and data security attorney; to be identified by 2026-10-15) | Notice decisions, state-by-state analysis, wording of subscriber notices, extortion questions | Hours 0-4 |
| Hosting provider support (security or abuse line) | Help confirm the token's activity, preserve logs, act on attacker infrastructure | Hours 1-4 |
| Cyber insurer | **None today.** If the quoted policy is bought, call its hotline before hiring any outside firm | Hours 0-4 |
| Support contractor | Pause admin console use; route subscriber questions to an approved holding reply | Hour 1 |
| Two negotiated-DPA subscribers (48-hour clock) | Initial notice as soon as the incident is confirmed | Within 48 hours of confirmation |
| FBI (IC3 online report) | Voluntary report; also the law enforcement consultation Florida requires before any "no harm" determination (Fla. Stat. 501.171(4)(c)) | Day 1 |

Contact numbers are kept on the contact sheet only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: an alert or email that a token or key was used from an unknown address or created a new token; the hosting audit log shows a database export, snapshot, or bulk download the owner did not make; a security tool or advisory names a package installed on the laptop as malicious; a subscriber, researcher, or extortion message says the company's data is for sale.

**Write down two times:** discovery (when the owner first knew or had reason to believe) and confirmation (when unauthorized access to subscriber data is confirmed). The DPA clocks (48 and 72 hours) run from confirmation. Florida's 10-day third-party agent clock runs from "the determination of the breach of security or reason to believe the breach occurred" (Fla. Stat. 501.171(6)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Disconnect the laptop from the network. **Do not wipe it**; it is evidence. Switch to the phone and a clean device | Laptop offline |
| 2. From the clean device, revoke the hosting API token and every other token on the hosting account; pause CI deployments | No active tokens except a new break-glass one |
| 3. Rotate the database password and restrict database connections to the platform network; restart the application with the new secret | Old connection string fails |
| 4. Export the hosting audit log (it keeps only 30 days) and the database and storage access logs to a separate location; record a hash | Export saved; hash in the incident log |
| 5. Sign out all sessions and rotate passwords on the hosting console, repository, email, password manager, and registrar | Only the clean device is signed in |
| 6. Start the incident log and the notice clock sheet; call the consultant, then counsel | Log open; both engaged |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What did the token do?** List every action in the exported log: first unknown use, database exports or snapshots, storage listings and downloads, setting changes, new tokens or collaborators. Compare source addresses with the CI service's addresses.
2. **What was copied?** A full database copy holds every subscriber (about 240 current and 31 closed accounts), about 88,000 end-client records with service notes and some home addresses, and about 520 subscriber staff accounts with hashed passwords. Photo downloads show in storage logs only if object logging was on; if not, **assume all photos were taken**.
3. **Other secrets.** Rotate the messaging, model, payment processor, error monitoring, and help desk API keys that were in the `.env` file. Check each provider's console for use from unknown addresses.
4. **Persistence.** With the consultant, look for new accounts, tokens, deploy keys, webhooks, scheduled jobs, or code changes. Compare the deployed code with the repository. Remove only after evidence is captured.
5. **The laptop.** The consultant images the disk and identifies the malicious package and how it ran, with a chain-of-custody note. The repository lock file shows when it was installed.

## 5. Hours 8-24: keep the service running and prepare notices (RS.CO, RC.RP)
- **Service:** the platform can keep running once tokens and the database password are rotated. Put it in maintenance mode only if the code or data may have been changed.
- **Subscriber staff accounts:** force a password reset for every subscriber staff account and end all sessions.
- **Breach analysis with counsel:** which data elements were taken, whose they are (subscriber-owned end-client data versus company-owned staff accounts), and which states the affected people live in. Under the Florida definition a name with a phone number, email, or appointment history alone is not personal information; counsel decides on service notes that describe a physical condition, on home addresses, and on whether hashed passwords are "secured" (Fla. Stat. 501.171(1)(g)).
- **Subscriber notice:** send a short, accurate initial notice to all affected subscribers as soon as the incident is confirmed, and no later than the 48-hour and 72-hour DPA clocks. Do not say "no data was taken" unless the logs prove it. Offer the facts each subscriber needs for its own notices.
- **Extortion demand:** not paid without counsel's advice and an OFAC sanctions check. Paying does not remove any notice duty.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 48 hours of confirmation | DPA notice to the two negotiated-DPA subscribers | Their data affected |
| Within 72 hours of confirmation | DPA notice to all other affected subscribers | Any subscriber data affected |
| No later than 10 days after determination | Florida third-party agent notice to each subscriber, with the information it needs | Florida residents' personal information involved |
| No later than 30 days after determination | Florida individual notice and, if 500 or more Floridians, Department of Legal Affairs notice; or a written "no harm" determination sent to the Department | Company-owned data (subscriber staff accounts) only |
| As each state requires | Other states' rules for service providers and data owners | Affected residents of other states |

**Plan to the shortest clock.** The 48-hour contract notice comes first; send a short notice when the facts are thin, then update at least every 72 hours.

## 7. After day 1 (RC.RP, ID.IM)
Rebuild the laptop from clean media before using it again, with no plaintext secrets (POL-01 7.5). Restore in P05 order if any data was changed. Correct any public statement the incident shows to be untrue (POL-01 4.6). Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-013), P07, and this runbook, and keep all incident records and notices for at least 5 years (POL-01 8.8).

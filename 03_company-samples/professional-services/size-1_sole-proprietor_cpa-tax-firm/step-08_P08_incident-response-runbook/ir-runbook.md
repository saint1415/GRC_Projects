# Incident Response Runbook: Business Email Compromise and Taxpayer Data Theft

| Field | Value |
|---|---|
| Organization | Cris Santos Company (CPA and tax preparation practice) |
| Tier / Vertical | Sole Proprietorship / Professional, Scientific, and Technical Services |
| Incident type | Takeover of the owner's mailbox, theft of client tax documents from email and cloud folders, and fraudulent returns filed with the stolen data. The tax software (MFA enforced by the vendor) is checked but not assumed compromised |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10. A written plan is not required under 16 CFR 314.6, but the IRS, FTC, and Florida clocks cannot be met without one |
| Owner and approver | CPA-owner, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT consultant due 2026-11-30, before the 2027 filing season (POAM-008) |

Keep a printed copy in the home office and one away from it. Assume the attacker can read the mailbox: **use the phone, the printed contacts, and phone calls. Do not discuss the incident by email until the mailbox is clean.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Professional liability carrier's breach hotline | The data breach endorsement ($25,000 sublimit) requires a call before hiring vendors; the hotline refers breach counsel | Hour 0 |
| Breach counsel (through the hotline) | Privilege, breach determination, FTC and state notices | Hours 0-4 |
| On-call IT consultant | Secure the mailbox, check the laptop and printer-scanner, preserve logs | Hour 0 |
| Tax software vendor support | Check sign-ins and bank account changes; hold transmissions; check returns filed under the firm's EFIN | Hours 0-2 |
| Email suite provider support | Help lock out the attacker; confirm what logs exist | Hours 1-2 |
| IRS Stakeholder Liaison (local) | Pub. 1345 security incident report and data theft report; the IRS can block fraudulent returns | No later than the next business day after confirmation |
| State tax agencies (Federation of Tax Administrators list) | Data theft affecting clients' state returns | With the IRS report |
| FBI local field office; local police | Report the crime; police report number for clients | Day 1 |
| Backup CPA (after the continuation agreement exists) | File extensions if the owner is tied up in the response | As needed |

Contact numbers, including the Stakeholder Liaison's, are on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: an e-filed return is rejected because the SSN was already used; a client asks about an email "from the firm" that the owner did not send; a forwarding rule, delegate, or connected app appears that the owner did not create; a sign-in alert from an unknown place; returns filed under the EFIN or PTIN exceed the firm's own count; the owner entered the mailbox password on a page that turned out to be fake.

**Write three dates in the incident log. Each starts a different clock:**
| Date | What it means | Clock |
|---|---|---|
| Discovery | First day the event is known to the firm or its agents (16 CFR 314.4(j)(2)) | FTC notice: no later than 30 days |
| Confirmation | The event is confirmed as one that can lead to unauthorized disclosure or misuse of taxpayer information (Pub. 1345) | IRS report: no later than the next business day |
| Determination | The firm determines a breach occurred or has reason to believe one did (Fla. Stat. 501.171) | Florida notices: no later than 30 days |

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. From the phone, screenshot or export the mailbox's forwarding rules, delegates, connected apps, and sign-in history (only 30 days are kept) **before** changing anything | Evidence saved off the mailbox |
| 2. Change the mailbox password to a new unique passphrase, sign out all sessions, turn MFA on if still off, then remove the attacker's rules, delegates, and apps | Only the owner's devices signed in |
| 3. Change the practice management password (it once shared the email password) and check its sign-ins | Done |
| 4. Call the tax software vendor: confirm no unknown sign-ins, list bank account changes in the last 30 days, and hold transmission of any return with a recent change | Hold list made |
| 5. Call the carrier's hotline, then the IT consultant | Claim number; counsel engaged |
| 6. Start the incident log on paper: times, what was seen, each action, who was called | Log open |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What could the attacker read?** With the consultant, list the client folders and mailbox attachments in reach. If item-level access records are missing, **treat everything in the mailbox and synced folders as accessed**: the FTC rule presumes acquisition from access unless reliable evidence shows otherwise (314.2(m)).
2. **What did the attacker send?** Search sent and deleted items for messages to clients asking for documents, payments, or bank changes. List each recipient for a phone call.
3. **Refund diversion check.** For every bank account change in the tax software in the period, call the client on the number on file (POL-01 8.5). Mark each return as held, filed, or not affected.
4. **Count people.** For each affected person record: individual client or spouse (FTC count), Florida resident or not, and the other state for part-year residents.
5. **Laptop and printer-scanner.** The consultant checks the laptop for malware and the printer-scanner for a stored password. If malware is found, stop using the laptop and image it before reinstalling.

## 5. Hours 8-24: report and keep working (RS.CO, RC.RP)
- **IRS:** report to the local Stakeholder Liaison as soon as the incident is confirmed, and no later than the next business day (Pub. 1345). Ask for guidance on held returns and on clients whose returns were already filed by someone else.
- **States and police:** notify the state tax agencies on the Federation of Tax Administrators list for affected part-year residents; report to the FBI field office and local police.
- **Clients who received attacker messages:** phone them first. Tell them the firm never asks for bank changes by email.
- **Keep working:** the tax software and portal are separate from the mailbox and keep MFA. Work from the laptop once the consultant clears it (or the backup CPA files extensions). Use portal messages instead of email until counsel and the consultant say the mailbox is clean.
- **No payment** of any demand without counsel and an OFAC check (POL-01 10.5).

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Next business day after confirmation | IRS through the Stakeholder Liaison; state tax agencies | Any confirmed incident involving taxpayer information |
| 30 days after discovery | FTC online form | 500 or more consumers |
| 30 days after determination | Florida individuals; Department of Legal Affairs if 500 or more Floridians | Florida residents affected |
| Without unreasonable delay | Consumer reporting agencies | More than 1,000 individuals notified at one time |
| Per each state's law | Residents and regulators of other states | Part-year residents affected |

**The Florida notice cannot be replaced by the FTC notice.** The FTC rule requires notice only to the FTC, so the federal-regulator path in 501.171(4)(g) does not apply.

**Worked example (tabletop script for the walkthrough):**
| Date | Event | Clock effect |
|---|---|---|
| Tue 2027-02-16 | Two e-filed returns are rejected because the SSNs were already used | Logged as possible discovery; the plan uses this date for the FTC clock, so the FTC target is **Thu 2027-03-18** |
| Wed 2027-02-17 | Owner finds a forwarding rule created 2027-02-01 and sign-ins from a hosting network. Incident confirmed and mailbox secured | IRS report due by **Thu 2027-02-18**; made the same afternoon |
| Fri 2027-02-19 | Counsel and the owner determine a breach: about 640 consumers, about 590 of them Florida residents, the rest in other states | Florida notices due by Sun 2027-03-21, so sent by **Fri 2027-03-19**, with the Department notice (500 or more Floridians). Consumer reporting agencies: not required (not more than 1,000) |

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, internet, a clean workstation, tax software, portal and Forms 8879, email and files, accounting, billing. Release held returns only after a phone call confirms the client's bank details. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-013), the POA&M, and this runbook, and keep all incident records for at least 5 years (the period Florida sets for a no-harm determination, 501.171(4)(c)).

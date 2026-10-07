# Incident Response Runbook: Business-System Intrusion with Attempted Pivots to Client Digital Assets

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radiation safety consulting practice) |
| Tier / Vertical | Micro / Nuclear Reactors, Materials, and Waste |
| Incident type | A phished staff account on the practice's business systems (the productivity suite and a laptop), with attempted pivots to clients: malicious documents sent from the trusted mailbox to Part 37 and reactor clients, malware written to USB media headed for a reactor outage, and access to client Part 37 security information |
| Why this incident | Adapted from the registry default ("cyber attack on plant business network with attempted pivot to digital assets"). The practice has no plant; its business network is the suite and its laptops, and its paths into client digital assets are trusted email and removable media. It combines the three High risks in P01 (R-001, R-003, R-013) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Office Manager (Security Officer) |
| Approved | 2026-09-15 by the Principal Health Physicist (owner) |
| Last tested | Not yet. First tabletop with the MSP due 2026-12-15 (POAM-008) |

## 0. Roles and notification chain (Govern)
The practice has 7 people and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics. The Office Manager runs the incident and keeps the log and the clock sheet.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Office Manager | Principal Health Physicist (owner) | Mobile phone (numbers on the printed contact card) |
| Decision maker (money, ransom, client and regulator notices) | Owner | Part 37 services lead | Mobile phone |
| Part 37 client calls | Part 37 services lead with the owner | Owner alone | Client RSO and security contacts on the contact card |
| Reactor plant calls; list of site devices and media | Field services lead | Owner | Plant cyber security contact and outage coordinator on the contact card |
| Technical response | MSP incident line (24x7 emergency number in the MSP contract) | MSP lead technician's mobile | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel firms | n/a | Assigned by the insurer on the first call |
| SYS-02 vendor | Vendor support line | Vendor account manager | If calibration records may have been touched |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** staff member → Office Manager → MSP incident line and owner (at the same time) → insurer breach hotline (owner) → breach counsel and forensics (through the insurer). The **clock sheet starts at the first report**: 4 hours to any plant whose site devices or media are involved, 24 hours to any Part 37 client whose information may have been reached.

**Out-of-band first.** Assume the suite is compromised. Coordinate by phone and text, using the printed contact card. Do not email clients about the incident from the suite until the MSP confirms the mailboxes are clean.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the office and at the owner's and Office Manager's homes: this runbook, contact card with client and plant security contacts, notification matrix, clock sheet, and the list of devices and USB drives used at each plant during the current outage
- [ ] Client approval list current, so the practice knows which staff could reach each client's information (POL-02 B.3)
- [ ] Restricted per-client folders in place with sync off. **Gap until POAM-002 closes**
- [ ] Company encrypted USB drives only, scanned before each trip. **Gap until POAM-010 closes**
- [ ] MFA with number matching on the suite; MFA on the MSP firewall login and all SYS-02 users. **Gap until POAM-005 closes**
- [ ] 90-day immutable suite backups, restore-tested within the last 90 days. **Gap until POAM-007 and POAM-008 close**
- [ ] MSP-managed EDR with after-hours monitoring (R-002). Planned for 2026-12-31
- [ ] Suite alerts for new forwarding rules, mass downloads, and unusual sending (R-019)
- [ ] Insurer hotline and policy number checked at each renewal

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A staff member entered a password on a strange page, or approved an MFA prompt they did not start | Staff report | Office Manager has the MSP reset the password, revoke sessions, and check the sign-in log and forwarding rules |
| A client calls about an odd email or attachment from the practice | Client | Thank them; ask them not to open it and to forward headers to their IT; **start the clock sheet**; declare an incident |
| A plant kiosk quarantines a practice USB drive, or a plant reports malware on practice media | Plant | Field services lead collects the plant's report; **start the 4-hour clock if the practice found it first**; withdraw every drive used at that plant |
| Suite alert for a new forwarding rule, mass download, or sign-in from an unusual location | Suite alert | MSP blocks the session; Office Manager opens an incident |
| Antivirus or EDR alert on a laptop | MSP console | MSP isolates the laptop and calls the Office Manager |
| Someone outside the practice claims to have client security information | Email or call | Do not reply. Save the message. Declare an incident; call the owner |

**Declare an incident** when an unauthorized person is confirmed in any practice account or device, or when malware is found on any practice device or drive.

**Write down the discovery time.** Every clock in `notification-matrix.csv` runs from it:
- reactor plant: 4 hours from discovery (contract);
- Part 37 client: 24 hours from discovery (contract);
- Florida individuals: 30 days from determination of a breach of personal information (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Take affected laptops off the network (unplug or turn off Wi-Fi); leave them on for evidence. Collect every USB drive the affected person used in the last 60 days | Staff, guided by the Office Manager | Devices offline; drives bagged and labeled |
| 2. Call the MSP incident line. MSP resets the account, revokes all sessions and app consents, removes attacker MFA registrations and forwarding rules, and blocks the attacker's sign-in sources | Office Manager; MSP | MSP confirms the account is contained |
| 3. Call the insurer's breach hotline | Owner | Claim number issued; counsel assigned |
| 4. **Start the clock sheet.** Field services lead lists the plants where the person or their media worked in the last 60 days; Part 37 services lead lists the client folders the account could open | Office Manager with both leads | Lists on the clock sheet with discovery time |
| 5. Pause outbound sharing from the client library (MSP sets the library read-only for all but the owner) and stop sending reports by email until step 2 of section 5 is done | MSP; Project Coordinator | Library read-only |
| 6. Open the incident log: timeline, actions, who, when | Office Manager | Log started |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Account activity.** Suite sign-in, mailbox, sharing, and file access logs for the affected account (180 days of history today; export at once). Which Part 37 folders and documents were opened or downloaded? Which outgoing messages did the attacker send, and to whom?
2. **Client exposure list.** For each Part 37 client: documents accessed or downloaded, times, and whether any were shared outward. For each other client: messages or files sent from the compromised mailbox.
3. **Media path to plants.** Forensics examines the affected laptop and every collected USB drive. Did malware write to drives used at a plant? Which drives went through which plant kiosk, and when?
4. **Spread.** Were other staff phished or other laptops infected? Were the MSP's tools or the shared MSP logins used? (P01 R-013)
5. **Calibration records.** If the person had SYS-02 access, ask the vendor for the audit trail and check for changes to readings or certificates since the first suspicious sign-in (R-008).
6. **Personal information.** Did the attacker reach employee records, dose reports with Social Security numbers, or client background pages? **This drives the Florida breach decision.**
7. **Preserve evidence.** Forensics images the affected laptop, keeps the drives, and exports suite logs before they age out. Keep a chain-of-custody record for each item.

## 5. Containment and eradication (RS.MI)
1. Block the attacker's senders, domains, and addresses in the suite; search all mailboxes for the phishing message and remove it.
2. Confirm no attacker-added forwarding rules, app consents, delegated mailbox access, or sharing links remain anywhere in the tenant.
3. Wipe and rebuild affected laptops from the MSP's standard image. Wipe every collected USB drive; destroy any drive that left the practice's control.
4. Confirm with forensics that no persistence remains, including in the MSP's remote management platform, before reconnecting anything.
5. If the MSP's own tools or logins may be the entry point, the owner asks the insurer's forensic firm to lead eradication and requires the MSP to show its own investigation results.
6. Turn on number matching for MFA (if not done) and require re-registration of MFA for the affected account.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every written notice. Phone calls to clients and plants come first; written confirmation follows.

| When | Action | Owner |
|---|---|---|
| Hour 1 | MSP engaged; insurer notified; counsel and forensics assigned | Office Manager; owner |
| **Within 4 hours of discovery** | Call each reactor plant whose site devices or media may be involved: what was found, which drives and laptops, dates on site, what the practice has done. The plant decides its own NRC reporting under 10 CFR 73.77; the practice does not | Field services lead |
| **Within 24 hours of discovery** | Call each Part 37 client whose folder the account could open: what may have been reached, when, and what the practice has done. The client assesses the event under its own procedures and 10 CFR 37.57(b) (law enforcement as appropriate; the Florida Bureau of Radiation Control no later than 4 hours after notifying law enforcement). The practice gives facts and access logs and supports the assessment; it never makes that determination for the client | Part 37 services lead with the owner |
| Within 24 hours | Warning to every client that received messages from the compromised mailbox: do not open the listed messages; how to recognize them; a contact for questions. Sent from a clean account or by phone | Project Coordinator with the owner |
| Day 0 to 2 | Voluntary report to the FBI (IC3) or CISA, as counsel advises. Make it before any ransom decision: full and timely reporting is an OFAC mitigating factor | Owner with counsel |
| Day 0 to 1 | Staff briefing: what happened, what to say (nothing outside the practice), where to send client questions | Office Manager |
| As soon as scope is known | Florida breach determination for any personal information reached; count affected individuals by state | Owner with counsel |
| Within 30 days of determination | Notice to affected Florida individuals (501.171(4)); Department of Legal Affairs if 500 or more (not expected); consumer reporting agencies if more than 1,000 (not expected). For client employees named in background pages, counsel agrees with the client who sends the notice | Owner with counsel |
| Weekly until closed | Status calls to affected clients and plants | Owner |

**The practice's contract clocks are much shorter than the legal ones.** A plant may need to decide within hours whether it has its own NRC reportable event, and a Part 37 client may need to call law enforcement and the State the same day. The practice's job is to give them facts early, even when the facts are incomplete. Say what is known, what is not, and when the next update will come.

**Inbound notices.** If a vendor (accounting and payroll service, MSP, suite vendor) is where the breach happened, it must notify the practice within 10 days of its determination (Fla. Stat. 501.171(6)(a)). The practice still sends its own notices.

**Ransom decision:** only the owner, with breach counsel and the insurer's advice and after an OFAC sanctions check (POL-03 4.7). Paying does not remove any notice duty.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Clean laptop access to the suite for the Office Manager and Project Coordinator; new passwords and MFA re-registration for every account the attacker touched (BP-07)
2. Calibration laboratory: confirm lab workstation 1 is clean and SYS-02 records are intact; resume calibrations (BP-03)
3. Restricted client library: reopen for approved staff only; confirm no stray copies on laptops or in mailboxes (BP-02)
4. Remaining consultant laptops (BP-01)
5. Outage support: issue freshly wiped company drives, scanned on a clean laptop, before staff return to any plant; tell the plant before the next gate entry (BP-06)
6. Lab workstation 2 and gamma spectroscopy (BP-04)
7. Own-license records (BP-09)
8. Accounting and payroll (BP-08)
9. Shielding and survey project files, restored from SYS-06 if needed (BP-05)

**Before reconnecting any device:** antivirus or EDR shows clean, passwords are changed, MFA is re-registered, and patches are current. Tell clients and plants when services are back (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP and counsel. Written summary within 30 days (POL-03 4.11). Offer a copy of the relevant parts to each affected client and plant.
- Update the risk register (P01, especially R-001, R-003, R-013, R-019), the POA&M (P07), the client approval list, and this runbook.
- Keep the incident log, clock sheet, client and plant notices, forensic report, and breach decision for at least 3 years, or longer if a client contract requires (POL-02 A.7).

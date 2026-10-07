# Incident Response Runbook: Ransomware with PMS Downtime and Prescription Diversion

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent community pharmacy) |
| Tier / Vertical | Micro / Healthcare and Public Health |
| Incident type | Ransomware on the store computers (starting from a phishing email) that stops PMS use at the counter, forces prescriptions to be sent to nearby pharmacies, and includes theft of PHI from the shared drive (double extortion) |
| Adapted from | The registry default, "ransomware forcing EHR downtime and ambulance diversion". A pharmacy has no EHR or ambulances; its equivalents are the PMS and sending patients and prescriptions to other pharmacies (`../00_company-facts.md` section 5) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Store Manager (Privacy Officer and Security Officer) |
| Approved | 2026-08-28 by the pharmacist-owner |
| Last tested | Not yet. First tabletop with the MSP and both pharmacists due 2026-11-30 (POAM-008) |

## 0. Roles and notification chain (Govern)
The pharmacy has 7 people and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics. The Store Manager runs the incident and keeps the log; the pharmacist on duty keeps patients safe at the counter.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Store Manager | Pharmacist-owner | Cell phone (numbers on the printed contact card) |
| Decision maker (money, ransom, diversion, closing the counter) | Pharmacist-owner | Staff Pharmacist | Cell phone |
| Counter and patient safety lead | Pharmacist on duty | The other pharmacist | In store |
| Technical response | MSP incident line (24x7 emergency number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel | Insurer panel counsel | n/a | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm | n/a | Engaged by breach counsel |
| PMS vendor | Vendor support line | Vendor security contact (per BAA) | Phone |
| Packaging equipment vendor | Service line | Field technician | Phone |
| Partner pharmacy | Pharmacist in charge | Store phone | Phone (arrangement in the contingency plan) |
| ALF management company | Director of nursing at each ALF | Corporate office | Phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |
| DEA | DEA Diversion field office | n/a | Number in the binder |

**Notification chain in the first hour:** staff member → Store Manager → MSP incident line and pharmacist-owner (at the same time) → insurer breach hotline (pharmacist-owner) → breach counsel and forensics (through the insurer). The PMS vendor is called at once if any PMS session, credential, or the order interface to the packaging workstation may be involved.

**Out-of-band first.** Assume email and the store desktops are compromised. Coordinate by phone and text on personal phones, using the printed contact card. Do not use the store VoIP phones for incident calls if the MSP has not cleared the network.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the pharmacist verification station and at the pharmacist-owner's and Store Manager's homes: this runbook, contact card, notification matrix, downtime card and paper downtime log, four-factor breach assessment form, and paper DEA order forms
- [ ] Printed list of the week's adherence packs and ALF residents' current medications, refreshed each Monday (BP-05)
- [ ] Backups: 90-day immutable versions, restore-tested within the last 90 days (CP-9, CP-4). **Gap until POAM-007 and POAM-008 close**
- [ ] MSP-managed EDR with alert monitoring (SI-3, SI-4). **Gap until POAM-006 closes**
- [ ] Unique local administrator passwords; MFA on the backup console (IA-5, IA-2(1)). **Gap until POAM-015 and POAM-005 close**
- [ ] Packaging workstation on its own network segment (SC-7). **Gap until POAM-014 closes**
- [ ] Partner pharmacy arrangement confirmed in writing; cellular failover router installed (P05)
- [ ] Insurer hotline and policy number checked at each renewal; MSP contract includes incident notice terms

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A staff member clicked a link in an email and typed a password | Staff report | Store Manager has the MSP reset the password and sign out all sessions; check the suite sign-in log and forwarding rules |
| Files will not open, names changed, or a ransom note appears on a counter desktop or the packaging workstation | Staff report | **Unplug the network cable. Do not turn the computer off.** Call the Store Manager; the pharmacist on duty starts the downtime card |
| Shared-drive files changing in bulk; sync errors; backup job failure | Suite alert; MSP alert | MSP pauses sync and the backup job; Store Manager opens an incident |
| Antivirus or EDR alert that is not cleared automatically | MSP console | MSP isolates the device and calls the Store Manager |
| Unusual events in the daily EPCS audit report (alterations or sign-ins nobody recognizes) | Pharmacist on duty | Treat as a possible EPCS security incident (section 6); call the PMS vendor |
| Email or call from someone claiming to have patient data | Extortion message | Do not reply. Save the message. Declare an incident |

**Declare a ransomware incident** when encryption or a ransom note is confirmed on any store computer or in the shared drive, or when someone claims to hold pharmacy data.

**Write down the discovery time.** Under 45 CFR 164.404(a)(2), a breach counts as discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member. The staff member's first report starts that clock. Florida's 30-day clock starts at the pharmacy's determination of a breach, or reason to believe one occurred (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Disconnect affected computers from the network; leave them powered on for evidence. Unplug the packaging workstation's network cable; the packager can finish the current strip offline | Staff, guided by the Store Manager | Devices offline |
| 2. Call the MSP incident line; MSP isolates devices remotely, pauses shared-drive sync, and suspends the backup job so it cannot copy encrypted files over good versions | Store Manager; MSP | MSP confirms isolation and backup protection |
| 3. Call the insurer's breach hotline and give the claim details | Pharmacist-owner | Claim number issued; counsel assigned |
| 4. Call the PMS vendor: report possibly exposed sessions, ask the vendor to sign out all of the pharmacy's sessions and check for unusual sign-ins, alterations, or exports, and confirm whether the PMS itself is affected | Store Manager | Vendor ticket open |
| 5. Reset passwords and sign out all sessions for affected users and all administrators (PMS, suite, fax, delivery app, backup console); confirm MFA is intact | MSP with the Store Manager | Sessions revoked |
| 6. Start the downtime card at the counter (section 3a) | Pharmacist on duty | Patients being served safely |
| 7. If the owner laptop may be affected, treat the CSOS key as compromised: revocation request within 24 hours of substantiation; paper DEA order forms until a new certificate is issued | Pharmacist-owner | Revocation sent or ruled out |
| 8. Open the incident log: timeline, actions, who, when | Store Manager | Log started |

### 3a. Downtime and diversion at the counter (RC.RP)
The PMS is vendor-hosted and usually unaffected. What stops is the store's ability to reach it safely. The pharmacy can reach the PMS web interface from a **clean** device (a laptop the MSP has checked, or a staff phone hotspot) once the vendor confirms the accounts are clean. Until then:

| Situation | Action | Rule |
|---|---|---|
| Refill request, prescriber cannot be reached | One-time emergency refill of up to a 72-hour supply from the labeled bottle; record on the paper downtime log | Fla. Stat. 465.0275(1) |
| Controlled substance prescription and the PDMP cannot be reached because of the outage | Document the reason; dispense no more than a 3-day supply | Fla. Stat. 893.055(8) |
| Paper or oral prescription that says it was sent electronically | Do not fill until the electronic version can be checked, or confirm by phone with the other pharmacy and void one | 21 CFR 1311.200(g)-(h) |
| New prescription that needs the patient's profile (allergies, interactions) | **Divert:** transfer to the partner pharmacy, or ask the prescriber to resend there; tell the patient | Patient safety (P05 BP-01) |
| Electronic controlled substance prescriptions | Cannot be processed outside the PMS. Ask prescribers to send urgent ones to the partner pharmacy; resume only when the vendor confirms the PMS is compliant and clean | 21 CFR 1311.200(c)-(d) |
| Pickup of already-filled bags | Paper pickup log with signatures; the card terminal is standalone and keeps working | P05 BP-04 |
| ALF adherence packs | Hand-filled blister cards checked by a pharmacist; call each ALF's director of nursing | P05 BP-05 |
| Deliveries | Printed route sheet and paper signature slips | P05 BP-06 |

**Diversion decision.** The pharmacist-owner decides to divert all new prescriptions when counter access to the PMS is not back within 4 hours (the BP-01 RTO), or at once if patient safety cannot be assured. Tell the partner pharmacy, post a notice at the door, and change the refill line message. Diversion ends when the PMS is reachable from clean devices and the backlog of downtime entries can be entered.

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Scope.** Which computers, accounts, and cloud services are affected? Sources: MSP antivirus or EDR console, suite sign-in and file activity logs, PMS audit trail (through the vendor), firewall logs.
2. **Initial access.** Find the phishing email, the account used, and the first computer. Search all mailboxes for the same message and remove it. Check whether the packaging vendor's remote connection or the MSP tool was used.
3. **Lateral movement.** The same local administrator password was on every computer until POAM-015 closes; assume every desktop and the packaging workstation may be affected until forensics clears each one.
4. **Preserve evidence.** Forensics images affected computers and exports suite and firewall logs before they age out (suite logs are kept less than one year). Keep a chain-of-custody record.
5. **Data theft.** Did PHI leave? Check suite download and sharing activity, email forwarding rules, large outbound transfers in firewall logs, and the attacker's claims. The shared drive holds delivery log exports since 2021, ALF medication lists, and controlled substance inventory spreadsheets. **This drives the breach decision.**
6. **Controlled substance records.** Ask the PMS vendor whether any controlled substance prescription record was annotated, altered, or deleted, or whether logical access settings changed, during the incident window. The pharmacist on duty reviews the EPCS audit reports for those days.
7. **Backups.** Before any restore, the MSP confirms which backup versions predate the attack and that the backup console was not accessed by the attacker.

## 5. Containment and eradication (RS.MI)
1. Block the attacker's email senders, domains, and IP addresses in the suite and at the firewall (MSP).
2. Disable any compromised accounts; remove attacker-added forwarding rules, app consents, and MFA registrations.
3. Turn off the packaging vendor's remote connection until the vendor and forensics confirm it was not used.
4. Wipe and rebuild affected computers from the MSP's standard image. **Do not decrypt and reuse them.** The equipment vendor rebuilds the packaging workstation from its last clean image.
5. Set unique local administrator passwords on every rebuilt computer.
6. Confirm with forensics that no persistence remains, including in the MSP's remote management platform, before reconnecting anything.
7. If the MSP's own tools may be the entry point, the pharmacist-owner asks the insurer's forensic firm to lead eradication and requires the MSP to show its own investigation results (P01 R-013).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every notice before it goes out. The Store Manager, as Privacy Officer, signs the four-factor breach risk assessment (45 CFR 164.402). Under the 164.402 definition, an impermissible acquisition, access, use, or disclosure of PHI is presumed to be a breach unless the assessment shows a low probability that the PHI has been compromised. Plan on notification unless forensics and counsel support that finding.

**Likely size.** The delivery log exports alone name several thousand patients, so plan for 500 or more affected individuals: HHS notice at the same time as individual notice, media notice if more than 500 Florida residents, the Florida Department of Legal Affairs, and the consumer reporting agencies if more than 1,000.

| When | Action | Owner |
|---|---|---|
| Hour 1 | MSP engaged; insurer notified; counsel and forensics assigned; PMS vendor called | Store Manager; pharmacist-owner |
| Hour 1 to 4 | Partner pharmacy and both ALFs told about possible diversion and pack changes; door notice and refill line message | Pharmacist-owner; Lead Pharmacy Technician |
| Within one business day of deciding that PMS controlled substance records were or could have been compromised | Report to the PMS vendor and DEA (21 CFR 1311.215(c)) | Pharmacist-owner |
| Within 24 hours of substantiating CSOS key compromise | Revocation request to the DEA certification authority (21 CFR 1311.30(e)) | Pharmacist-owner |
| By the close of the next business day after each dispensing | PDMP reports for controlled substances dispensed on paper, through the PDMP web portal from a clean device, or an extension requested from the Department of Health before the deadline (Fla. Stat. 893.055(3)(a)) | Pharmacist on duty |
| Day 0 to 2 | Voluntary report to the FBI (IC3) or CISA, as counsel advises. Make it before any ransom decision: full and timely reporting is an OFAC mitigating factor | Pharmacist-owner with counsel |
| Day 0 to 1 | Staff briefing: what happened, downtime steps, do not discuss outside the pharmacy, send patient and media questions to the pharmacist-owner | Store Manager |
| Day 0 to 3 | Patients at the counter or on the phone: short script (systems down, prescriptions safe, some sent to a nearby pharmacy, more information to follow) | Front-Store Clerk; pharmacists |
| As soon as scope is known | Four-factor breach risk assessment documented; count affected individuals by state | Store Manager with counsel |
| Within 30 days of determination | Florida individual notice, or the HIPAA notice relied on under 501.171(4)(g); copy of the notice to the Department of Legal Affairs if 500 or more Floridians (deemed compliance with 501.171(3)); consumer reporting agencies if more than 1,000 | Store Manager and counsel |
| Within 60 days of discovery | HIPAA individual notices; HHS notice at the same time if 500 or more; media notice if more than 500 Florida residents | Store Manager and counsel |
| Within 60 days after year end | HHS breach log if fewer than 500 | Store Manager |
| Per contract | PBM network notices if claims or PBM data were affected; ALF management company under the supply agreement | Lead Pharmacy Technician; pharmacist-owner |

**Plan to the shorter clock.** For a pharmacy this size, determination and discovery are often days apart at most. Florida's 30-day deadline therefore usually arrives before HIPAA's 60-day outer limit. Counsel should decide in week 1 whether to send one HIPAA-compliant notice by the Florida date.

**Inbound notices.** If the MSP, the backup service, or a SaaS vendor is where the breach happened, it must notify the pharmacy under its BAA (164.410, no later than 60 days) and, as a Florida third-party agent, within 10 days of its determination (501.171(6)(a)). The pharmacy still sends the notices to individuals and regulators.

**Controlled substances.** If the incident is combined with a break-in or the count shows a theft or significant loss, also report to the county sheriff within 24 hours of discovery (Fla. Stat. 893.07(5)(b)) and to the DEA Field Division Office in writing within one business day, with DEA Form 106 within 45 days (21 CFR 1301.76(b)).

**Ransom decision:** only the pharmacist-owner, with breach counsel and the insurer's advice and after an OFAC sanctions check (POL-03 4.12). Paying does not remove notification duties if data was taken.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Internet and store network: firewall checked and credentials changed; cellular failover or a phone hotspot if the line is down
2. Clean intake, verification, and pickup stations: rebuilt desktops with individual accounts; laptops checked by the MSP
3. PMS access: vendor confirms the pharmacy's accounts and sessions are clean and that the PMS remains EPCS-compliant; resume EPCS processing only then
4. Cloud fax: new portal passwords; read queued faxes
5. Phones and email: suite accounts cleaned; forwarding rules removed
6. Delivery phone and app: new passwords; route list rebuilt from the PMS
7. Packaging workstation: rebuilt by the equipment vendor from the last clean image, on its own network segment when available; first strip checked by a pharmacist against the PMS
8. Purchasing: wholesaler portal passwords changed; new CSOS certificate if revoked
9. Shared drive: restored by the MSP from the newest clean version; staff check ALF order sheets and packaging schedules before sync is turned back on

**Back-entry.** Every prescription on the paper downtime log is entered in the PMS, with claims submitted, and every controlled substance dispensing reported to the PDMP. The pharmacist-owner checks that the paper log and the PMS match before the log is shredded.

**Before reconnecting any device:** EDR or antivirus shows clean, passwords are changed, and patches are current. End diversion and tell the partner pharmacy, the ALFs, staff, and patients when services are back (RC.CO). Keep paper downtime until each function meets its RTO in P05.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP and counsel. Written summary within 30 days (POL-03 4.15).
- Update the risk register (P01, especially R-001, R-002, R-005, R-008, R-013, R-023), the POA&M (P07), the downtime card, and this runbook.
- Keep the incident log, breach assessment, notices, DEA reports, and forensic report for 6 years (POL-02 A.7).

# Incident Response Runbook: Front Office Payment and Reservation System Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 38-unit roadside motel) |
| Tier / Vertical | Micro / Accommodation and Food Services |
| Incident type | Registry default "Point-of-sale and reservation system compromise," adapted to a motel with no POS server: an attacker signs in through the lock vendor's remote support tool on the back office PC, moves across the flat office network to the shared front desk PC, and installs a keylogger. It captures card numbers keyed during phone reservations (with security codes), clerks' PMS passwords, and the shared front desk mailbox password, which opens the stored crew card forms. The P2PE terminals are not affected |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Assistant Manager (Security and Privacy Lead) |
| Approved | 2026-08-31 by the Owner-Manager |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (POAM-012) |

## 0. Roles and notification chain (Govern)
The motel has 7 employees and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics. The Assistant Manager runs the incident and keeps the log. The Owner-Manager owns the merchant agreement and makes every money and notice decision.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Assistant Manager | Owner-Manager | Cell phone (numbers on the printed contact card) |
| Decision maker (money, notices, acquirer, ransom) | Owner-Manager | Assistant Manager | Cell phone; lives on site |
| Technical response | MSP emergency line (in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Policy card in the binder |
| Breach counsel | Insurer panel counsel | n/a | Assigned by the insurer on the first call |
| Forensics | Insurer panel forensic firm; a PCI Forensic Investigator (PFI) if Visa requires one | n/a | Engaged through counsel; the PFI list is on the PCI SSC website |
| Acquirer | Acquirer risk line | Gateway support | Number in the binder |
| Vendors | PMS vendor, payment gateway and P2PE provider, lock vendor, productivity suite vendor | n/a | Numbers in the binder; call back on known numbers only |
| Law enforcement | U.S. Secret Service field office | FBI (IC3) | Numbers in the binder |

**Notification chain in the first hour:** staff member → Assistant Manager → MSP emergency line and Owner-Manager (at the same time) → insurer breach hotline (Owner-Manager) → breach counsel and forensics (through the insurer) → acquirer risk line (Owner-Manager, within 24 hours of suspicion).

**Out-of-band first.** Assume the front desk PC, the shared mailbox, and the clerks' PMS passwords are compromised. Coordinate by phone and text on personal phones, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the front desk and in the Owner-Manager's apartment: this runbook, contact card, notification matrix, merchant agreement notice term, paper check-in kit
- [ ] Lock vendor tool set to start only when the motel accepts a session (done 2026-08-05); one-time codes and a remote access log. **Gap until POAM-003 closes**
- [ ] EDR with after-hours alerting on the 3 PCs (SI-4). **Gap until POAM-007 closes**
- [ ] Separate networks for terminals, lock system and CCTV, and office PCs (SC-7). **Gap until POAM-005 closes**
- [ ] No keyed entry on PCs and no stored card forms (POL-04 4.2). **Gap until the 2026-11-30 redesign**
- [ ] Firewall logs kept off the device for 12 months. **Gap: today they roll over in about 7 days, which destroys evidence**
- [ ] Terminal list with serial numbers, for checking that the P2PE devices were not touched (POAM-014)
- [ ] Insurer hotline number and policy number checked each renewal; sealed emergency key cards in the Owner-Manager's safe

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A crew company or guest reports fraud on a card used at the motel | Phone call to the front desk or the Assistant Manager | Log it with the card's last 4 digits and stay dates; if two or more in a month, or any with a keyed or emailed card, declare an incident |
| The acquirer reports the motel as a common point of purchase for fraud | Acquirer call or letter to the Owner-Manager | **Declare the incident. Record the time as the start of the Visa 3-day clock** |
| The lock vendor's tool shows a session nobody started; the front desk PC is slow, shows pop-ups, or the mouse moves by itself | Staff report; EDR alert (when live) | Disconnect the PC's network cable; leave it on; call the Assistant Manager |
| PMS activity report shows full card displays or profile exports by a clerk who was not on shift | Weekly log review (POAM-009) | Disable that PMS account; open an incident |
| Shared mailbox shows a new forwarding rule or sign-ins from unknown places | Suite alert; weekly review | Reset the password; remove the rule; open an incident |

**Declare a card compromise incident** when there is evidence sufficient to raise a reasonable suspicion that card data or a payment system was accessed without authorization. The acquirer's 24-hour term and Visa's 3-day clock start then, not at confirmation.

**Record the date of determination.** Fla. Stat. 501.171(4)(a) counts 30 days from the determination of the breach or reason to believe a breach occurred. Write down when the motel first had reason to believe card numbers or ID numbers were accessed.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Unplug the network cables of the front desk PC and the back office PC. **Do not power off, reboot, scan, or sign in as administrator** (Visa What To Do If Compromised v10.0) | Clerk on duty, guided by the Assistant Manager | Both PCs offline and labeled |
| 2. Switch the front desk to the fallback: card-present payments on the P2PE terminals only; phone bookings taken without card details and paid later by pay-by-link from a clean device; **never write card numbers on paper** | Assistant Manager | Fallback running |
| 3. Check-in continues: Owner-Manager's laptop (encrypted, separate from the incident) for the PMS; printed arrivals list; key cards from the sealed emergency set if the back office PC must stay offline | Assistant Manager; Owner-Manager | Guests checking in |
| 4. Call the MSP emergency line: isolate the PCs remotely, preserve firewall logs before they roll over, disable the lock vendor tool | Assistant Manager; MSP | MSP confirms isolation and log export |
| 5. Call the insurer's breach hotline | Owner-Manager | Claim number issued; counsel assigned |
| 6. From a clean device, reset every clerk's PMS password, the shared mailbox password, and the gateway portal passwords; turn on MFA for every PMS user and the mailbox if not already done; sign out all sessions | Assistant Manager with the PMS vendor and MSP | Sessions revoked |
| 7. Open the incident log: timeline, actions, who, when | Assistant Manager | Log started |
| 8. Call the acquirer's risk line within 24 hours of suspicion and record the case number | Owner-Manager | Acquirer case number recorded |

## 4. Analysis (RS.AN)
Led by the forensic firm (or the PFI) through breach counsel, with the MSP supplying access and logs.
1. **Entry and spread.** Confirm the lock vendor tool as the entry point (tool logs, lock vendor's records), find when the attacker reached the front desk PC, and check the CCTV recorder and terminals for any connection from the attacker.
2. **Window of exposure.** First and last date the keylogger could capture keystrokes. This decides which keyed cards are at risk and is needed for Visa (Section A.4).
3. **Card data at risk:** card numbers, expiration dates, and security codes keyed during phone reservations and no-show charges in the window; **every crew card form in the shared mailbox** if the mailbox was opened (about 640 emails, about 260 with security codes, until the purge is done); OTA virtual cards displayed in the PMS by stolen clerk logins.
4. **Guest data at risk:** PMS exports or ID scans viewed with stolen clerk logins (about 14,000 ID scans until the retention schedule is in force). This drives the Florida and other-state analysis.
5. **P2PE check.** Confirm with the gateway that the 2 terminals were not tampered with or swapped (serial numbers, seals). If they are intact, card-present payments continue.
6. **Preserve evidence.** Forensic images of both PCs, the lock tool's session log, firewall logs, PMS activity exports, and suite sign-in logs, with a chain-of-custody record. If Visa requires a PFI, give it full access.

## 5. Containment and eradication (RS.MI)
1. Remove the lock vendor tool until the vendor provides one-time codes and written terms; the lock vendor resets its own shared credentials.
2. Rebuild both PCs from the MSP's standard image. **Do not clean and reuse them.** Reinstall the lock software from the vendor's media and restore the lock database from the last copy taken before the window of exposure.
3. Rotate every credential the PCs could have captured: PMS users, mailboxes, gateway portal, website-builder account, PMS interfaces (lock and pricing tool), and the staff Wi-Fi passphrase.
4. Purge card data from the shared mailbox and the backup's versions with counsel's agreement (keep a forensic copy for counsel only), and shred the remaining binder forms.
5. Bring forward the network separation (POAM-005) so the terminals, lock system, and office PCs are on separate networks before the PCs return.
6. Confirm with the forensic firm or PFI that no persistence remains, including in the MSP's remote management platform, before reconnecting.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel confirms every legal notice before it goes out. The Owner-Manager owns all acquirer and card brand communication.

| When | Action | Owner |
|---|---|---|
| Hour 0-24 | Acquirer notified (contract term); insurer notified; counsel engaged | Owner-Manager |
| Within 3 calendar days of suspicion | Compromise reported to Visa through the acquirer; other brands per the acquirer's instructions | Owner-Manager |
| Within 3 calendar days of the Visa notice | Incident report to Visa and the acquirer | Assistant Manager and Owner-Manager with forensics |
| Within 3 calendar days of identifying at-risk cards or the window | At-risk account numbers to Visa through the acquirer | Owner-Manager |
| Within 5 business days of a Visa PFI notice | PFI contracted; Visa and the acquirer told its name | Owner-Manager |
| As soon as practical | Voluntary report to the U.S. Secret Service or FBI (IC3) | Assistant Manager |
| Day 0-2 | Staff briefing: what happened, fallback steps, no discussion outside the motel, send guest and media questions to the Owner-Manager | Owner-Manager |
| Day 1-5 | Call each crew company whose card form or card may be affected, so it can watch for fraud; follow with written notice as counsel advises | Owner-Manager |
| Within 30 days of determination | Florida individual notices (15 more days with written good cause to the Department); Department of Legal Affairs notice if 500 or more Florida residents | Owner-Manager and counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at one time | Owner-Manager and counsel |
| Per each state | Notices to non-Florida residents; most transient guests and many crew members live elsewhere | Counsel |

**Is it a Florida breach?** Under 501.171(1)(g), personal information includes a name with a card number **in combination with any required security code**, and a name with a driver license, ID card, or passport number. Keyed phone payments and many crew forms include security codes, and stolen clerk logins could reach ID scans, so this scenario likely qualifies. Paper forms alone are not "data in electronic form" under 501.171(1)(a), but the emailed copies are. Corporate cards issued in an employee's name may still identify an individual; counsel decides and documents the analysis.

**Card brands do not replace legal notice, and legal notice does not replace card brand reporting.** Both run in parallel. The Visa 3-day clock expires long before the 30-day Florida clock.

**Ransom.** This scenario normally has no extortion. If a demand arrives, only the Owner-Manager decides, with counsel and the insurer and after an OFAC sanctions check (POL-03 4.8).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Internet and office network, with the new separate networks if ready; firewall credentials changed and MFA on
2. Front desk PC (rebuilt) and the lock system on the rebuilt back office PC; test key encoding before the evening arrivals
3. PMS access with MFA for every user; check with the PMS vendor that no exports or setting changes remain
4. Terminals and gateway: confirm terminal integrity with the gateway; resume card-present payments (they normally continue throughout)
5. Channel manager and OTA connections (vendor-hosted; confirm with the PMS vendor)
6. Housekeeping tablets and staff Wi-Fi (new passphrase)
7. Email: named mailboxes with MFA replace the shared password; forwarding rules checked
8. Guest Wi-Fi; then accounting and payroll

**Before reconnecting any device:** EDR or antivirus shows clean, passwords are changed, patches are current, and the acquirer agrees the motel may resume card-not-present payments (by pay-by-link only). Tell staff and affected guests and crew companies when services are back (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP and counsel. Written summary within 30 days (POL-03 4.11).
- Update the risk register (P01, especially R-001, R-002, R-003, R-008, R-015), the POA&M (P07), the PCI DSS scope document, and this runbook.
- Expect the acquirer to require a fresh validation, possibly with a QSA, and possible card brand assessments; the insurer's policy may cover some of these.
- Keep the incident log, notices, and forensic report at least 3 years (POL-02 A.7); keep any Florida no-harm determination at least 5 years (501.171(4)(c)).

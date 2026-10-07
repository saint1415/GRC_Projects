# Incident Response Runbook: Customer Device Data Exposure and Point-of-Sale Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent electronics and device repair shop) |
| Tier / Vertical | Micro / Other Services (except Public Administration) |
| Incident type | Exposure of customer data at the shop, through either of two routes: **(A) bench:** a workforce member views, copies, or shares personal data from a customer device in the shop's custody; **(B) counter:** the shared Counter login (or any SYS-01 account) is phished or misused and ticket data (passcodes, account passwords, card numbers written in notes) is exported, or a payment terminal is tampered with |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; POL-04 4.3 to 4.5 |
| Runbook owner | Shop Manager (Security and Privacy Lead) |
| Approved | 2026-08-31 by the Owner |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (POAM-007) |

## 0. Roles and notification chain (Govern)
The shop has 7 people and no IT staff. The MSP does the technical work on the office side; the cyber insurer supplies breach counsel and forensics. The Shop Manager runs the incident and keeps the log. The Senior Technician knows the bench systems but may not lead a route A investigation if a technician's conduct is in question; the Owner then takes the lead and the forensic firm handles the bench evidence.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Shop Manager | Owner | Cell phone (numbers on the printed contact card) |
| Decision maker (money, staff actions, public statements, closing the counter) | Owner | Shop Manager | Cell phone |
| Technical response (office endpoints, network, suite, backups) | MSP emergency line (number in the MSP contract) | MSP lead technician's cell | Phone only |
| Bench systems | Senior Technician (route B only) | Forensic firm (route A) | Cell phone |
| Cyber insurer | Carrier's breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel firms | n/a | Assigned by the insurer on the first call |
| Payment processor | Merchant risk contact | Processor support line | Numbers in the merchant agreement copy in the binder |
| Ticketing and POS vendor | Vendor support (priority line) | Vendor account manager | Phone; vendor security contact |
| Law enforcement | Local police (insider theft); FBI IC3 or U.S. Secret Service (card or account compromise) | n/a | Numbers in the binder |

**Notification chain in the first hour:** staff member → Shop Manager → Owner and MSP emergency line (at the same time) → insurer breach hotline (Owner) → breach counsel and forensics (through the insurer). The processor is called within 24 hours whenever card data or a terminal may be involved, even before the facts are known.

**Out-of-band first for route B.** Assume the Counter login and email may be compromised. Coordinate by phone and text on personal phones, using the printed contact card.
**Quiet first for route A.** Do not confront the workforce member or tell other staff until the Owner and counsel agree on the approach. Preserve evidence first.

## 1. Preparation checks (Identify / Protect)
- [ ] Incident binder behind the counter and a copy at the Owner's home: this runbook, contact card, notification matrix, notice summary (processor 24 h, insurer prompt notice, business accounts 72 h, Florida 30 days), evidence bags, and chain-of-custody labels
- [ ] Named counter accounts with MFA (POAM-001). **Gap until it closes**
- [ ] SYS-01 export alerts on and monthly review in place (POAM-005). **Gap until it closes:** route B exports may go unseen
- [ ] Bench session logging through MSP-managed EDR (POAM-006). **Gap until it closes:** route A cases cannot be confirmed from logs, as the 2026-03-14 complaint showed
- [ ] Terminal list and weekly inspection log (P03 G-127, G-128)
- [ ] Backup immutable and restore-tested (POAM-007, POAM-008)
- [ ] Customer notice templates drafted with counsel (P03 G-111, G-112)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Route | First action |
|---|---|---|---|
| Customer says someone looked at their photos, accounts, or messages while the device was in for repair | Complaint, review, or social post | A | Log it; secure the device's ticket history and the bench PC; call the Shop Manager |
| Staff member reports a colleague browsing or copying customer content | Staff report | A | Call the Shop Manager or Owner privately; protect the reporter's identity |
| USB drive or phone photos of customer content found; customer files on a bench PC that do not match an open transfer job | Shop Manager, Senior Technician | A | Bag the item; do not open files; call the Shop Manager |
| Customer gets an account alert (new sign-in to their email or cloud account) after a repair | Customer | A or B | Treat as possible credential misuse; call the Shop Manager |
| SYS-01 export alert, bulk ticket views, or a sign-in from an unknown place | SYS-01 alert or monthly review | B | Disable the account; open an incident |
| Staff member typed the Counter or email password into a suspicious page | Staff report | B | Change the password; sign out all sessions; check exports |
| Processor notice of possible compromise | Shop Manager | B | Declare; the 24-hour clock may already be running |
| Terminal seal broken, extra device, loose casing, or wrong serial number | Weekly inspection | B | Take the terminal out of use; do not unplug or open it; call the processor |

**Severity:**
- **Severity 1:** a SYS-01 export or card data exposure affecting many customers, or evidence that customer data left the shop.
- **Severity 2:** one or a few customers' device content viewed or copied without a repair need.
- **Severity 3:** a policy breach with no customer content accessed (for example a card number written on paper and shredded the same day).

**Record the time the shop first had reason to believe a breach occurred.** Florida's 30-day clock for individuals and the Department runs from "the determination of the breach or reason to believe a breach occurred" (Fla. Stat. 501.171(3)(a), (4)(a)). The processor's 24-hour clock and the insurer's prompt-notice term run from **suspicion**.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log: time of report, who reported, what was seen, actions taken | Shop Manager | Log open |
| 2A. **Route A:** secure the customer device (bag, label, lock in the parts cabinet), the bench PC (unplug the network cable, leave it on, do not reimage; POL-03 4.4), any USB drives, and the camera footage (save it before the 30-day retention ends) | Shop Manager with the Owner | Items bagged with chain-of-custody labels |
| 3A. **Route A:** suspend the workforce member's accounts quietly; move them to non-customer work or send them home with pay, as the Owner decides | Owner | Accounts suspended |
| 2B. **Route B:** disable the affected SYS-01 account, sign out all sessions, and change the Counter password (or the named account's) with MFA re-registered; MSP resets suite passwords and checks forwarding rules | Shop Manager; MSP | Sessions revoked |
| 3B. **Route B:** take any suspect terminal out of use and switch to the spare; stop taking phone payments until the cause is known | Shop Manager | Terminal isolated |
| 4. Call the cyber insurer's breach hotline; engage counsel and forensics through the insurer | Owner | Claim number issued |
| 5. Start the contract clocks: processor within 24 hours if card data or a terminal may be involved; business accounts within 72 hours of confirmation if their devices or data are involved | Shop Manager | Notices sent or scheduled |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying office-side logs and the ticketing vendor supplying SYS-01 audit exports.
1. **Scope, route A:** which devices did the person handle (SYS-01 ticket assignment history), what was opened (camera footage; bench session logs once deployed; the device's own recent-activity data, examined by forensics only), and were copies made (USB drives, the person's phone, uploads from the bench PC)?
2. **Scope, route B:** which tickets were viewed or exported (SYS-01 audit log; ask the vendor for the detailed export), which of those held passcodes, account passwords, or card numbers (re-run the 2026-07-22 field searches), and where the sign-ins came from.
3. **Personal information test (Fla. Stat. 501.171(1)(g)).** For each affected customer, note whether the exposed data includes an email or user name with a password; a name with a card number and a required code; or a name with medical, biometric, or geolocation information (for example health app data or photo location data on a device). Device passcodes alone are not listed in the statute, but they unlock everything else on the device; counsel decides.
4. **Good-faith test (501.171(1)(a)).** Access during a documented repair test is good faith. Browsing or copying outside the test checklist (POL-04 4.4) is not.
5. **Preserve evidence:** forensics images the bench PC and USB drives; the MSP exports suite and firewall logs, and the Shop Manager exports the SYS-01 audit log, before they roll over; keep chain-of-custody records. **Do not return the customer's device** until forensics releases it; offer a loaner.
6. **Estimate magnitude:** count affected individuals by state. That sets the Florida Department (500 or more) and consumer reporting agency (more than 1,000) thresholds, and which other states' laws apply.

## 5. Containment and eradication (RS.MI)
- **Route A:** end the person's access everywhere the same day (POL-02 B.4), including the keypad code and Wi-Fi password; recover keys and company USB drives; ask counsel whether to demand return or deletion of any copies; review every other ticket the person handled in the last 90 days.
- **Route B:** purge passcode, password, and card-number notes from SYS-01 at once (POAM-011) so the same data cannot be taken twice; enforce MFA on all counter access; block the attacker's sign-in sources; ask the ticketing vendor to check for unusual API or AI assistant access to the shop's tenant.
- **Terminal tampering:** the processor replaces the terminal and takes the suspect device; inspect the other terminals the same day.
- **Customer account protection:** where account passwords were exposed, contact the affected customers promptly to change them, even before formal notice, as counsel advises.
- **If the MSP's tools may be the entry point,** the Owner asks the insurer's forensic firm to lead and requires the MSP to share its own findings (P01 R-013).

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every legal notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Hour 1 | MSP engaged; insurer hotline called; counsel and forensics assigned | Shop Manager; Owner |
| Within 24 hours of suspicion | Processor notice (card data or a terminal involved) | Shop Manager |
| Day 0-2 | Report to law enforcement as counsel advises: local police for insider theft; FBI IC3 or U.S. Secret Service for account or card compromise | Owner |
| Day 0-2 | Staff briefing: what to say to customers who ask; no discussion outside the shop; no replies to online reviews | Owner |
| Within 72 hours of confirmation | Business account notices under their service terms | Shop Manager |
| As soon as known | Breach determination under Fla. Stat. 501.171 and other states' laws, documented with the determination date (POL-03 4.5) | Shop Manager with counsel |
| No later than 30 days after determination | Notice to each affected Florida resident by mail or email; Department of Legal Affairs notice if 500 or more Floridians; consumer reporting agencies if more than 1,000 | Shop Manager and counsel |
| Per each state's law | Notices to residents of other states | Counsel |
| If no notice is required | Written no-notice determination kept 5 years and sent to the Department within 30 days (501.171(4)(c)) | Counsel |

**Plan to the shortest clock.** The processor's 24-hour clock arrives long before the Florida deadline (30 days), and it starts at suspicion. Do not wait for the investigation to finish before calling the processor or the insurer.

**Inbound notices.** If the ticketing vendor, its AI model provider, the backup provider, or the data recovery lab has the breach, it must notify the shop within 10 days of its determination (Fla. Stat. 501.171(6)(a)). The shop still sends the notices to individuals and the Department.

**Extortion:** if anyone demands payment to delete or not publish customer data, follow POL-03 4.7 (Owner, counsel, insurer, and an OFAC sanctions check). Paying does not remove notice duties.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Internet and shop network (after blocking the attacker's access in route B)
2. Payment terminals: spare or replacement terminal from the processor; standalone mode if SYS-01 is not yet trusted
3. Counter PCs with named accounts and MFA; paper intake forms, numbered tags, and the paper release log until then
4. SYS-01 access for intake, payment, and release, after the vendor confirms the tenant is clean
5. Email, the repairs mailbox, and status texts
6. Bench PCs: reimaged from the standard image **only after** forensics releases them
7. Bench storage: restored for open jobs only, with POL-04 4.6 retention applied before anything is restored
8. Other restores from the cloud backup

**Validate before normal service:** no active sessions for suspended or compromised accounts; passcode, password, and card-number notes purged; terminal list reconciled; and each customer device involved returned with the customer told what happened. Tell customers and business accounts when service is normal (RC.CO-03). Public statements come only from the Owner after counsel approves (RC.CO-04).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing, with the MSP and counsel; written summary within 30 days (POL-03 4.9).
- Sanctions decision for route A under POL-02 A.4, documented by the Owner.
- Update the risk register (P01, especially R-001, R-002, R-008, R-009, R-023), the POA&M (P07), training content (POAM-004), and this runbook.
- Keep the incident log, breach determination, notices, any no-notice determination, and the forensic report for at least 5 years (POL-02 A.7).

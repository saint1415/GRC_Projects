# Incident Response Runbook: Customer Device Data Exposure and Point-of-Sale Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electronics and device repair service) |
| Tier / Vertical | Small / Other Services (except Public Administration) |
| Incident type | Exposure of customer data at the repair counter, through either branch: **(A)** a workforce member views, copies, or shares personal data from a customer device in the company's custody; **(B)** a counter login is compromised and ticket data (passcodes, account passwords, card numbers written in notes) is exported, or a payment terminal is tampered with |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; POL-04 4.3 to 4.5 |
| Runbook owner | IT Manager (Information Security Lead) |
| Approved | 2026-09-04 by the General Manager |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-013) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | General Manager | Incident line (cell), then the out-of-band group chat on personal phones |
| Technical response | IT Manager and IT Support Technician | Forensic firm from the cyber insurer's panel | Insurer breach hotline |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer and acquirer | Controller | General Manager | Policy card and merchant agreement contacts in the incident binder |
| Manufacturer A and business accounts | Operations Manager (Manufacturer A); Business Accounts Manager (accounts) | General Manager | Program manager contact in the binder |
| Workforce matters (Branch A) | HR and Payroll Specialist with the Operations Manager | General Manager | Cell |
| Customer and public communications | Customer Experience Manager, after counsel approves | General Manager | Cell |
| Law enforcement | Local police (insider theft); FBI IC3 or U.S. Secret Service (card or account compromise) | n/a | Numbers in the incident binder |

**Out-of-band first for Branch B.** Assume the counter login, email, and chat may be compromised. Coordinate by phone.
**Quiet first for Branch A.** Do not confront the workforce member or tell other staff until HR and counsel agree on the approach. Preserve evidence first.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder at every store and the Depot: this runbook, contacts, the notification matrix, notice term summary (acquirer 24 h, Manufacturer A 24 h, Florida 30 days), and evidence bags and labels
- [ ] Bench session logging and SYS-01 export alerts turned on (POAM-002, POAM-015). **Gap until they close:** Branch A cases cannot be confirmed from logs today, as the April 2026 complaint showed
- [ ] Named accounts with MFA on counter tablets (POAM-007). **Gap until it closes**
- [ ] Payment terminal list and weekly inspection log (POAM-022)
- [ ] Forensic firm available through the insurer panel; retainer confirmed (POAM-013)
- [ ] Customer notice templates drafted with counsel (P03 G-111, G-112)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Branch | Action |
|---|---|---|---|
| Customer says someone accessed their photos, accounts, or messages while the device was in for repair | Complaint, review, or social post | A | Log it; secure the device's ticket history and bench PC; call the incident line |
| Staff member reports a colleague browsing or copying customer content | Staff report or anonymous line | A | Incident line; protect the reporter's identity |
| USB drive or phone photos of customer content found; bench PC with unexpected customer files | Store Manager, IT | A | Bag the item; do not open files; incident line |
| Customer account alert (new sign-in to their email or cloud account) after a repair | Customer | A or B | Treat as possible credential misuse; incident line |
| Unusual SYS-01 export, bulk ticket views, or sign-in from an unknown location | SYS-01 alert or log review | B | Disable the account; open an incident |
| Staff report entering the counter login on a suspicious page | Staff report | B | Reset the password; revoke sessions; review exports |
| Acquirer or processor notice of possible compromise (common point of purchase) | Controller | B | Declare; the acquirer's 24-hour clock may already be running |
| Terminal seal broken, extra device, loose casing, or wrong serial number | Weekly inspection | B | Take the terminal out of use; do not unplug or open it; call the processor |

**Declare an incident when** any trigger above is credible. Severity:
- **Severity 1:** SYS-01 export or card data exposure affecting many customers, or evidence that customer data left the company.
- **Severity 2:** one or a few customers' device content viewed or copied without a repair need.
- **Severity 3:** a policy breach with no customer content accessed (for example card numbers written on paper, then shredded).

**Record the time the company first had reason to believe a breach occurred.** Florida's 30-day clock for individuals and the Department runs from "the determination of a breach or reason to believe a breach occurred" (Fla. Stat. 501.171(3)(a), (4)(a)). The acquirer's and Manufacturer A's 24-hour clocks run from **suspicion**.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log: time of report, who reported, what was seen, actions taken | IT Manager | Log open |
| 2A. **Branch A:** secure the customer device (bag, label, lock in the Depot cabinet), the bench PC (unplug from the network, leave powered on, do not reimage; POL-03 4.4), any USB drives, and the relevant CCTV footage (30-day retention) | Store Manager with the IT Manager on the phone | Items bagged with chain-of-custody labels |
| 3A. **Branch A:** suspend the workforce member's accounts quietly; move them to non-customer work or send them home with pay, as HR decides | HR and Payroll Specialist | Accounts suspended |
| 2B. **Branch B:** disable the compromised account, revoke all SYS-01 and identity provider sessions, and reset the shared counter logins at every store | IT Manager | Sessions revoked |
| 3B. **Branch B:** take any suspect terminal out of use and switch to a spare; stop taking phone payments until the cause is known | Store Manager; Controller | Terminal isolated |
| 4. Call the cyber insurer's breach hotline; engage counsel and forensics through the insurer | Controller | Claim number issued |
| 5. Start the 24-hour contract clocks: acquirer (Branch B with card data) and Manufacturer A (if a Manufacturer A customer or device is involved) | Controller; Operations Manager | Notices sent or scheduled within 24 hours |

## 4. Analysis (RS.AN)
1. **Scope, Branch A:** which devices did the person handle (SYS-01 ticket assignment history), what was accessed (bench session logs once deployed; CCTV; the device's own recent-activity data, examined by forensics only), and were copies made (USB drives, personal phone, cloud uploads from the bench PC)?
2. **Scope, Branch B:** which tickets were viewed or exported (SYS-01 audit log; request the vendor's detailed log export), which contained passcodes, account passwords, or card numbers (the P03 search method), and from where the sign-ins came.
3. **Personal information test (Fla. Stat. 501.171(1)(g)).** For each affected customer, note whether the exposed data includes: an email or user name with a password; a name with a card number and a required code; or a name with medical, biometric, or geolocation information (for example health app data or photo location metadata on a device). Device passcodes alone are not listed in the statute, but they unlock everything else on the device; counsel decides.
4. **Good-faith test (501.171(1)(a)).** Access during a documented repair test is good faith. Browsing or copying outside the test checklist is not.
5. **Preserve evidence:** image the bench PC and USB drives, export SYS-01 and identity provider logs before they roll over, and keep chain-of-custody records. **Do not return the customer's device** until forensics releases it; offer a loaner.
6. **Estimate magnitude:** number of affected individuals by state, which sets the Florida Department (500+) and consumer reporting agency (more than 1,000) thresholds.

## 5. Containment and eradication (RS.MI)
- **Branch A:** end the person's access everywhere, including manufacturer portals (same day, POL-02 4.4); recover company devices and badges; ask counsel whether to request return or deletion of any copies; review every other ticket the person handled in the last 90 days.
- **Branch B:** purge passcode, password, and card-number notes from SYS-01 immediately (POAM-001) so the same data cannot be taken twice; enforce MFA on all counter access; block the attacker's sign-in sources; rotate the chatbot connector's API key.
- **Terminal tampering:** the processor replaces the terminal and handles the device; inspect every other terminal the same day.
- **Customer account protection:** where account passwords were exposed, contact the affected customers promptly to change them, even before formal notice, as counsel advises.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every legal notice before it goes out.

| When | Action | Owner |
|---|---|---|
| Within 24 hours of suspicion | Acquirer notice (card data involved); Manufacturer A notice (program customer or device involved); insurer notified | Controller; Operations Manager |
| Day 0-2 | Report to law enforcement as counsel advises: local police for insider theft; FBI IC3 or U.S. Secret Service for account or card compromise | IT Manager |
| Day 0-5 | Staff briefing script: what to say to customers who ask; no discussion outside the company | General Manager |
| Within 72 hours of confirmation | Business account notices under their contracts | Business Accounts Manager |
| As soon as known | Breach determination under Fla. Stat. 501.171 and other states' laws, documented (POL-03 4.5) | IT Manager with counsel |
| No later than 30 days after determination | Notice to each affected Florida resident by mail or email; Department of Legal Affairs notice if 500 or more Floridians; consumer reporting agencies if more than 1,000 | Controller and counsel |
| Per each state's law | Notices to residents of other states (mail-in customers) | Counsel |
| If no notice is required | Written no-notice determination kept 5 years and sent to the Department within 30 days (501.171(4)(c)) | Counsel |

**Plan to the shortest clock.** The contract clocks (24 hours) arrive long before the Florida deadline (30 days), and they start at suspicion. Do not wait for the investigation to finish before calling the acquirer or Manufacturer A.

**Extortion:** if anyone demands payment to delete or not publish customer data, follow POL-03 4.7 (majority owner, counsel, insurer, and an OFAC sanctions check). Paying does not remove notice duties.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Identity provider and administrator access
2. Store network and internet (Branch B: after blocking the attacker's access)
3. Counter tablets with named accounts and MFA; paper intake forms until then
4. SYS-01 access for intake, payment, and release; spare payment terminals if one was replaced
5. Bench PCs: reimage from the standard image **only after** forensics releases them
6. Manufacturer portals (named accounts)
7. Data recovery lab and delivery storage (check that retention rules are applied before restoring anything)

**Validate before normal service:** no active sessions for the suspended or compromised accounts, passcode notes purged, terminal list reconciled, and the customer devices involved returned with the customer informed of what happened. Tell customers and business accounts when service is normal (RC.CO-03). Public statements come only from the Customer Experience Manager after counsel approves (RC.CO-04).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing (POL-03 4.9 requires documentation within 30 days).
- Sanctions decision for Branch A under POL-01 4.7, documented by HR.
- Update the risk register (P01, especially R-001, R-002, R-003, R-004, R-005), the POA&M (P07), and this runbook.
- Keep incident records and any no-notice determination for at least 5 years (POL-01 4.10).

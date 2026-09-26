# Incident Response Runbook: POS and Reservation System Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 140-room beachfront hotel) |
| Tier / Vertical | Small / Accommodation and Food Services |
| Incident type | Compromise of front office payment and reservation systems: a phishing email leads to a browser form-grabber on reservations and front desk PCs that captures keyed card numbers, and a stolen front desk login is used to sign in to the PMS, display virtual card numbers, and export guest profiles |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager (Information Security Lead) |
| Approved | 2026-08-31 by the General Manager |
| Last tested | Not yet. First tabletop exercise due 2026-11-30 (POAM-011) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | General Manager | Incident line (cell), then the out-of-band group chat on personal phones |
| Technical response | MSP incident team | Forensic firm on the insurer's panel; a PCI Forensic Investigator (PFI) if Visa requires one | MSP 24x7 line |
| Acquirer and card brands | Controller | General Manager | Acquirer risk line (in the incident binder) |
| Breach and notice decisions | General Manager with breach counsel | Controller | Cell; counsel via insurer hotline |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Via insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| Front office operations | Front Office Manager | Night auditor on duty | Cell |
| Restaurant and bars | Food and Beverage Director | Restaurant manager on duty | Cell |
| Lock system and building | Chief Engineer | Engineer on duty | Cell |
| Vendors | PMS vendor, payment gateway, P2PE provider, lock vendor | n/a | Numbers in the incident binder |
| Law enforcement | U.S. Secret Service field office | FBI (IC3) | Numbers in the incident binder |

**Out-of-band first.** Assume email and the PMS are compromised. Coordinate on personal phones and the printed contact list in the incident binder at the front office and in the Controller's office.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder: this runbook, contacts, merchant agreement notice terms, the notification matrix, and downtime forms
- [ ] Current list of all payment devices with serial numbers (POAM-017)
- [ ] EDR on front office PCs with 24x7 alerting (SI-4). **Gap until POAM-009 closes**
- [ ] MFA for all PMS users (POAM-003) and no standing vendor remote access (POAM-004). **Gaps**
- [ ] Central logs retained 12 months (POAM-015). **Gap: today some logs roll over within days, which destroys evidence**
- [ ] Two sealed break-glass identity provider accounts (POL-02 4.9)
- [ ] Forensic firm confirmed through the insurer panel; the PFI list on the PCI SSC website bookmarked
- [ ] Paper arrivals list and emergency key cards ready (P05 BP-01, BP-02)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Acquirer or card brand reports the hotel as a common point of purchase for fraud | Acquirer letter or call to the Controller | Declare the incident. **Record the time as the start of the Visa 3-day clock** |
| Staff report a "group booking" email whose attachment asked to enable content or install something | Staff report | Isolate the PC; reset the user's password; revoke sessions; open an incident |
| PMS shows full card numbers displayed or large profile exports by a front desk user at odd hours | PMS activity report (weekly review, POAM-015) | Disable the account; open an incident |
| Guest complaints of fraud shortly after a stay | Front desk, Controller | Log each; escalate to the IT Manager if two or more in a month |
| Unknown browser extension or process on a front office PC | EDR alert, MSP | Isolate; open an incident |

**Declare a card compromise incident when** there is evidence sufficient to raise a reasonable suspicion that card data or a payment system was accessed without authorization. Visa's clock starts at that point, not at confirmation.
**Record the time of determination** for Florida purposes: 501.171 counts 30 days from determination of the breach or reason to believe a breach occurred.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Disconnect affected front office PCs from the network (cable out, Wi-Fi off). **Do not power off, reboot, or sign in with administrator credentials** (Visa WTDIC 7.1) | Front Office Manager with IT on the phone | PCs offline and labeled |
| 2. Move front desk card payments to the fallback: no keyed entry on PCs; take cards only on chip terminals; phone payments call back later. **Never write card numbers on paper** | Front Office Manager | Fallback running |
| 3. Disable the stolen PMS account and the shared night audit account; force a PMS password reset for all front office users; turn on MFA for all PMS users if not yet done | IT Manager with the PMS vendor | Sessions revoked |
| 4. Call the cyber insurer's breach hotline; engage counsel and a forensic firm through the insurer | General Manager | Claim number issued |
| 5. Call the acquirer's risk line (merchant agreement: within 24 hours of suspicion; fictional) | Controller | Acquirer case number recorded |
| 6. Ask the PMS vendor, gateway, and MSP to preserve logs and images (Visa WTDIC 7.1.6) | IT Manager | Written requests sent |
| 7. Start the incident log: timeline in UTC, actions, who, and when | IT Manager | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** which PCs ran the form-grabber, which PMS accounts were used, and from where? Check EDR (when live), PMS activity reports, identity provider sign-ins, and firewall logs.
2. **Window of exposure:** first and last date card numbers could have been captured. This decides which cards are at risk and is needed for Visa (WTDIC 4.1).
3. **Card data at risk:** keyed card numbers (with expiration and security codes typed during phone payments), virtual card numbers displayed in the PMS, and **card forms in the reservations and sales mailboxes** if the mailbox was reachable (POAM-006).
4. **Guest data at risk:** profile exports, **ID numbers from scanned licenses and passports**, and stay history. This drives the Florida and other-state analysis.
5. **Scope check on MID-2:** confirm the restaurant P2PE devices were not affected (check device inventory and tamper seals). If P2PE is intact, the restaurant keeps trading.
6. **Preserve evidence:** forensic images of affected PCs, PMS activity exports, firewall logs, the phishing email with headers. Maintain chain of custody. If Visa requires a PFI, give the PFI full access (WTDIC 5.1.2).

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure (domains, IPs) at the firewall and in email filtering.
2. Rebuild affected PCs from the standard image. **Do not clean and reuse them.**
3. Rotate all credentials the PCs could have captured: PMS users, identity provider users, gateway portal, and interface credentials (PMS-to-lock, POS-to-PMS).
4. Purge card data from the reservations and sales mailboxes now if not already done (POL-04 4.4).
5. Remove the card-display permission from everyone except the 3 approved users (POAM-002).
6. Confirm with the forensic firm or PFI that no persistence remains before reconnecting.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Legal counsel confirms every legal notice before it goes out. The Controller owns all acquirer and card brand communication.

| When | Action | Owner |
|---|---|---|
| Hour 0-24 | Acquirer notified (contract term); insurer notified; counsel engaged | Controller; General Manager |
| Within 3 calendar days of suspicion | Compromise reported to Visa (through the acquirer); other brands per the acquirer's instructions | Controller |
| Within 3 calendar days of the Visa notice | Incident report to Visa and the acquirer (WTDIC Attachment A) | IT Manager and Controller |
| Within 3 calendar days of identifying at-risk cards or the window of exposure | At-risk account numbers to Visa through the acquirer | Controller |
| Within 5 business days of a Visa PFI notice | PFI contracted; Visa and acquirer told the PFI's name | Controller |
| Day 0-5 | Staff briefing: what happened, fallback steps, do not discuss outside the hotel | General Manager |
| As soon as practical | Voluntary report to the U.S. Secret Service or FBI (IC3) | IT Manager |
| Within 30 days of determination | Florida individual notices; Department of Legal Affairs notice if 500+ Florida residents (15-day extension possible with written good cause) | General Manager and counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified | General Manager and counsel |
| Per each state | Notices to non-Florida residents; most guests live outside Florida | Counsel |

**Is it a Florida breach?** Under 501.171(1)(g), personal information includes a name with a driver license, ID card, or passport number, and a name with a card number **in combination with any required security code**. A card number alone may not qualify, but keyed phone payments include security codes and PMS exports include ID numbers, so this scenario likely does. Counsel decides and documents the analysis.

**Card brands do not replace legal notice, and legal notice does not replace card brand reporting.** Both run in parallel. The Visa 3-day clock will expire long before the 30-day Florida clock.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Staff network and internet (segment the front office PCs if the new payment VLAN is ready)
2. Lock server and encoders (confirm they were not touched; rotate the PMS-to-lock interface credential)
3. Identity provider and administrator access (break-glass if needed)
4. Clean front desk PCs (rebuilt), then PMS access with MFA for every user
5. Front desk terminals and gateway (confirm terminal integrity with the gateway)
6. Distribution: booking engine and channel manager (vendor-hosted; confirm with vendors that their systems were not affected)
7. Restaurant POS (normally unaffected under P2PE)
8. Email, chatbot, and cloud tenant workloads

**Validate before reconnecting:** EDR is clean, credentials are rotated, systems are patched, and the acquirer agrees the hotel may resume keyed card-not-present payments. Tell staff and guests when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update the risk register (P01, especially R-001, R-002, R-004, R-026), the POA&M (P07), the PCI scope document, and this runbook.
- Expect the acquirer to require a new validation (possibly with a QSA) and possible card brand non-compliance assessments; budget for them.
- Retain all incident documentation; keep any Florida no-harm determination for at least 5 years (501.171(4)(c)).

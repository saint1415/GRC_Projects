# Incident Response Runbook: Point-of-Sale Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional electronics and device repair chain) |
| Tier / Vertical | Mid-Market / Other Services (except Public Administration) |
| Incident type | Compromise of the channels where customers pay or where ticket and payment records live, in three variants: **(1) checkout skimming**: a malicious script on the mail-in checkout page captures card data or overlays the gateway's payment fields; **(2) terminal tampering**: a P2PE terminal is opened, swapped, or fitted with a skimmer; **(3) SYS-01 account takeover**: a phished Store Manager, supervisor, or administrator account is used to export ticket data, change settings, or issue fraudulent refunds |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); PCI DSS v4.0.1 12.10.1 |
| Policy basis | POL-03 Incident Response Policy (4.4, 4.7); POL-04 4.5 and 4.6; STD-10; STD-11 |
| Companion documents | `ir-runbook.md` (customer device data exposure); `notification-matrix.csv`; BIA (P05 BP-03, BP-04, BP-05); risk register (P01 R-004, R-009, R-021, R-044) |
| Runbook owner | Security Manager (incident commander) with the Chief Financial Officer (payments lead) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Tabletop with the acquirer contact and the payment gateway scheduled 2027-02-17 (POAM-010) |

## 0. Why this runbook exists
The company keeps card data out of its systems by design: card-present payments run on validated P2PE terminals, and e-commerce card entry happens only inside the gateway's hosted payment fields. That design moves the risk to three places the company still controls: the **checkout page around the payment fields** (which the company builds and hosts), the **physical terminals** at 34 stores, the Depot, and the contact center, and the **SYS-01 accounts** that can export about 1.9 million customer records. A compromise in any of them also threatens the company's SAQ P2PE and SAQ A eligibility, which the CFO must attest to by 2026-12-15.

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Technical response, MSSP, evidence |
| Payments lead | Chief Financial Officer | Controller | Acquirer notice within 24 hours, card brand case, gateway and processor contacts, SAQ impact |
| Application lead (variant 1) | Digital Engineering Manager | Senior developer on call | Page rollback, script removal, deployment freeze |
| Store lead (variant 2) | Director of Retail Operations | Regional Manager | Terminal isolation, store inspections, staff instructions |
| SYS-01 lead (variant 3) | IT Director | Security Manager | Session revocation, vendor escalation, export review |
| CMT chair (severity 1) | Chief Operating Officer | Chief Executive Officer | Business decisions, communications, resources |
| Legal | General Counsel with outside breach counsel (insurer panel) | n/a | Privilege, breach determinations, notices |
| Partner and manufacturer contacts | Director of Partner Programs | Chief Operating Officer | Partner notice within 48 hours if claim data is exposed; Manufacturer A notice within 24 hours if program customers are involved |
| Communications | Director of Customer Experience | n/a | Customer, staff, and media messages through counsel |

**Out-of-band first for variant 3.** Assume the compromised account's email and chat may be watched. Coordinate by phone and the out-of-band group.

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Variant | Action |
|---|---|---|---|
| Change-detection alert on the checkout page, or a new script not in the inventory | Change and tamper detection (POAM-012, live from 2026-11-15) | 1 | MSSP calls the incident commander within 30 minutes; application lead checks the change against the release log |
| Acquirer or processor notice of possible compromise (common point of purchase) | Acquirer; processor | 1 or 2 | Declare severity 1. The acquirer's 24-hour clock may already be running |
| Customers report fraud after a mail-in checkout, or a second "payment" form | Contact center; complaints | 1 | Declare; capture the page from outside the network |
| Terminal seal broken, extra device, loose casing, wrong serial number, or a terminal missing from the list | Weekly inspection; staff | 2 | Take the terminal out of use; do not unplug, open, or clean it; call the processor; declare |
| Sign-in to SYS-01 from an unusual location, a new administrator, or a bulk export | Identity provider alerts; SYS-01 audit events in the SIEM (POAM-003) | 3 | Disable the account; revoke sessions; declare |
| Refund exception report shows unusual refunds | Weekly refund report | 3 | Freeze refunds for the account; declare if unexplained |

**Severity:**
- **Severity 1:** any confirmed or strongly suspected card data capture (variant 1 or 2), a bulk export of customer records, or any exposure of partner claim data. Activate the CMT within 2 hours.
- **Severity 2:** a contained account takeover with no export; a tampered terminal found before use.
- **Severity 3:** an unexplained but benign page change; a failed sign-in campaign.

**Record the time the company first suspected a card data compromise.** The acquirer's 24-hour clock runs from suspicion. Florida's 30-day clocks run from the determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(3)(a), (4)(a)).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Open the incident log; record the time of suspicion | Incident commander | Log open |
| 0-1 h | **Variant 1:** capture the live page and loaded scripts from outside the network (for evidence); then roll the checkout page back to the last signed release, or switch mail-in checkout to "pay by phone" with a banner; freeze deployments | Application lead | Malicious script no longer served |
| 0-1 h | **Variant 2:** take the terminal out of use, bag it with a chain-of-custody form, switch to a spare; inspect every other terminal at that store and its region the same day | Store lead | All terminals in the region inspected |
| 0-1 h | **Variant 3:** disable the account; revoke all identity provider and SYS-01 sessions; reset the credentials and MFA of the user; block the source addresses; ask the SYS-01 vendor for a full audit export | SYS-01 lead | Sessions revoked; export requested |
| 0-2 h | Call the cyber insurer hotline before engaging vendors; counsel engaged; counsel decides on a forensic firm. If the acquirer requires a PCI Forensic Investigator, counsel engages one from the PCI SSC list | Payments lead | Claim number; counsel engaged |
| Within 24 h of suspicion | Notify the acquirer (merchant agreement term), even if facts are incomplete | Payments lead | Notice sent and logged |
| 1-4 h | Severity 1: convene the CMT; first situation report; CEO informs the audit committee chair | CMT chair | CMT meeting held |

## 4. Analysis (RS.AN)
1. **Variant 1: what ran and when.** Compare the captured page with signed releases and the script inventory. Find when the malicious script first appeared (deployment logs, CDN or gateway logs, content security policy reports once live). Identify which customers checked out in that window (portal order records). Determine whether the script captured card data typed into the gateway's frame (it normally cannot read inside the frame) or showed a fake payment form outside the frame (it can capture everything typed into it). The gateway and forensics answer this together.
2. **Variant 1: how it got there.** Check the build pipeline (pipeline secrets, recent changes, dependency updates), the third-party scripts the page loads, and administrator access to the hosting account.
3. **Variant 2: which terminal and how long.** Use the inspection log to bound the window (last clean inspection to discovery). The processor examines the device. P2PE terminals encrypt card data in the device, but a skimming overlay can read the card and PIN before encryption.
4. **Variant 3: what the account did.** Review SYS-01 audit events (exports, bulk views, setting changes, refunds), identity provider sign-ins, and email rules. Determine whether legacy notes with passcodes, passwords, or card numbers were in the exported data (POAM-015 reduces this).
5. **Affected individuals list.** For each variant, build the list by data element and state of residence. Separate checkout customers, store customers, partner claimants, and business account users.
6. **Preserve evidence.** Page captures, deployment and access logs, the terminal (with the processor), SYS-01 exports, and identity provider logs, all with chain of custody.

## 5. Containment and eradication (RS.MI)
- **Variant 1:** remove the malicious script and any unauthorized third-party scripts; rotate pipeline and hosting credentials; enforce the content security policy and subresource integrity; redeploy from a clean, signed build; keep change detection on. Do not reopen online checkout until forensics and the acquirer agree.
- **Variant 2:** the processor replaces the terminal; inspect every terminal at all 34 stores within 48 hours; reconcile the terminal list with the processor (POAM-011).
- **Variant 3:** remove any rules, administrator grants, or settings the attacker created; review refunds and reverse fraudulent ones; enforce separate administrator accounts and security keys for the affected roles; check whether the same password or phishing kit hit other accounts.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice. The Privacy and Compliance Manager keeps the decision log.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| P1 | Is this a suspected card data compromise (acquirer 24-hour clock)? | Chief Financial Officer with counsel | Decision log |
| P2 | Is it a breach of personal information under Fla. Stat. 501.171 (a name with a card number plus any required code, or an email or user name with a password) and each other affected state's law? | Privacy and Compliance Manager with counsel | Decision log |
| P3 | Number of affected individuals by state (Florida thresholds 500 and 1,000) | Privacy and Compliance Manager | Affected individuals list |
| P4 | Partner claim data or Manufacturer A program customers involved? | Director of Partner Programs | Decision log |
| P5 | Can the company still attest to SAQ P2PE and SAQ A eligibility for 2026? What does the acquirer require instead? | Chief Financial Officer | Acquirer correspondence |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-2 | Insurer hotline; counsel engaged | Chief Financial Officer |
| Within 24 hours of suspicion | Acquirer notice | Chief Financial Officer |
| Within 24 hours of suspicion | Manufacturer A notice if program customers are involved (variant 3) | Director of Partner Programs |
| Within 48 hours of discovery | Partner notice if claim data is involved (variant 3) | Director of Partner Programs |
| Day 0-2 | Report to law enforcement as counsel advises (FBI IC3 or U.S. Secret Service for card and account compromise) | Security Manager through counsel |
| Within 3 calendar days of suspicion | Visa compromise report through the acquirer, then the incident report within 3 more days; if Visa requires a PCI Forensic Investigator, retain one within 5 business days (Visa What To Do If Compromised v10.0, A.1, A.2, A.5). Other brands as the acquirer directs | Chief Financial Officer |
| No later than 30 days after determination | Florida individual notices; Department of Legal Affairs notice if 500 or more Floridians | Privacy and Compliance Manager and counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at a single time | General Counsel |
| Per each state's law | Notices to checkout customers and claimants in other states | Outside breach counsel |

**Communications.** Customers who checked out in the window: notice through counsel, with advice to watch card statements; no card replacement promises (issuers decide). Stores: a short script for customers who ask. Media: holding statement approved by counsel; no technical details.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Identity provider and administrator access (variant 3: after credential resets)
2. Store terminals: spares in place; the store keeps taking card-present payments on inspected terminals (BP-03)
3. SYS-01 access for intake, payment, and release
4. Partner integration API, if it was paused as a precaution (BP-05). Tell the partners when it resumes
5. Mail-in checkout page (BP-04): reopen only after forensics and the acquirer agree; until then, bookings by phone with payment on a contact center P2PE terminal

**Validate before normal service:** clean signed build with change detection running; terminal list reconciled; no attacker sessions or settings left; refunds reviewed; acquirer informed of the remediation.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; written report within 30 days (POL-03 4.13).
- Reassess SAQ eligibility with the acquirer before the next attestation.
- Update the risk register (P01 R-004, R-009, R-021, R-044), the POA&M (P07), STD-10, STD-11, and this runbook.
- Keep incident records and the decision log for at least 5 years (POL-01 4.13).

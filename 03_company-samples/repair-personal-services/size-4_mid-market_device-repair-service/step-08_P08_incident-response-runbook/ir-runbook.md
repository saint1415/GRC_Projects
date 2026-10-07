# Incident Response Runbook: Customer Device Data Exposure

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional electronics and device repair chain) |
| Tier / Vertical | Mid-Market / Other Services (except Public Administration) |
| Incident type | Exposure of customer data that the company holds because it repairs or recovers devices, through either branch: **(A) insider**: a workforce member views, copies, or shares personal data from customer devices in the company's custody; **(B) lab or delivery exposure**: recovered data in the Depot lab storage, the delivery storage, or a download link is accessed by someone who should not have it |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy; POL-04 4.4 and 4.7; STD-08 Customer data access and bench standard |
| Companion documents | `ir-runbook-pos-compromise.md` (checkout page, terminal, or SYS-01 account compromise); `notification-matrix.csv`; BIA (P05); risk register (P01 R-001, R-005, R-018, R-024) |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Tabletop with counsel, HR, and the Director of Partner Programs scheduled 2026-11-18 (POAM-010) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers so that technical, business, and legal decisions each have a clear owner. Branch A is also a workforce matter, so HR joins every tier.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, IT Director, Privacy and Compliance Manager, Director of Partner Programs, Director of Customer Experience, HR Director, outside breach counsel | Notices, customer and partner communications, public statements, employment actions in severity 1 cases, resources |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director, security analyst, MSSP, forensic firm (through counsel), Data Recovery Manager (Branch B), Digital Engineering Manager (delivery storage and links) | Evidence, scope, containment, eradication, recovery |
| **Operations lead** | Director of Retail Operations (stores) or Depot Director (Depot and lab), with the Regional Manager and Store Manager involved | Device custody, store staffing, customer handling at the counter |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Incident line; out-of-band group on personal phones |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Breach decisions and decision log | Privacy and Compliance Manager | General Counsel | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel), engaged by the General Counsel | Company's outside employment counsel (Branch A) | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($5M limit, $150K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Workforce matters (Branch A) | HR Director | Director of Retail Operations | Phone |
| Manufacturer A, Partners P1 and P2 | Director of Partner Programs | Chief Operating Officer | Contacts in the incident binder |
| Business accounts | Director of Business Accounts | Director of Partner Programs | Account contacts in SYS-01 |
| Customer and media communications | Director of Customer Experience, after counsel approves | Chief Operating Officer | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair (severity 1) | COO | Phone |
| Law enforcement | Local police (insider theft); FBI IC3 (data theft or extortion) | n/a | Numbers in the binder; contact only through counsel for Branch A |

**Quiet first for Branch A.** Do not confront the workforce member, and do not tell other staff, until HR and counsel agree on the approach. Preserve evidence first. Protect the identity of any colleague who reported the concern.

**Legal privilege protocol.** The General Counsel engages outside counsel, and counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs, chain of custody) separate from legal conclusions. Do not speculate in email or chat.

## 1. Preparation checks (Identify / Protect)
- [x] Customer data access standard with test checklists by repair type (STD-08)
- [x] Confidentiality agreements signed by every technician and data recovery specialist (P07 PS-6 satisfied)
- [ ] Bench session recording and USB and phone-pairing control on every bench PC. **Gap at 14 stores until POAM-002 closes:** Branch A cases there cannot be reconstructed from logs
- [ ] SYS-01 bulk view and export alerts in the SIEM (POAM-003). **Gap until it closes**
- [ ] Lab purge job working with failure alerts; backlog purged (POAM-004). **Gap until it closes:** a Branch B exposure today could include about 27 TB of data that should have been deleted
- [ ] Incident binder with evidence bags, chain-of-custody forms, and this runbook at all 34 stores and the Depot (POAM-010, due 2026-10-31)
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-17
- [x] Anonymous reporting line published to staff (POL-03 4.2)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Branch | Action |
|---|---|---|---|
| Customer says someone accessed their photos, accounts, or messages while the device was in for repair | Complaint, review, social post, or the customer's own account alert | A | Store Manager logs it in the security queue the same day (POL-03 4.2); secure the ticket history and bench PC; call the incident line |
| Colleague reports a technician browsing, photographing, or copying customer content | Staff report or anonymous line | A | Incident line; protect the reporter |
| Bench session flag (content opened outside the checklist), USB drive or phone connected to a bench PC | Bench session records; EDR alert (standard image) | A | Security analyst reviews within 1 business day; declare if unexplained |
| A user views or exports an unusual number of tickets | SYS-01 audit events in the SIEM (once POAM-003 closes) | A | Disable the account pending review; declare if unexplained |
| Recovered-data link accessed from an unexpected location, or a business account says it never requested a download | Delivery storage access logs; customer report | B | Revoke the link; declare |
| Unusual access to the lab storage array or after-hours lab entry | Lab storage logs; badge reports | B | Declare; secure the lab |
| Lab drive or encrypted delivery drive lost in transit or missing from the safe | Courier; Data Recovery Manager | B | Declare; check encryption status |

**Severity:**
- **Severity 1:** customer data from many customers left the company (for example a technician's collection of copied content, a bulk ticket export, or lab data accessed by an outsider), or any exposure of partner claim data. Activate the CMT within 2 hours (POL-03 4.4).
- **Severity 2:** one or a few customers' device content viewed or copied without a repair need, with no evidence it left the company.
- **Severity 3:** a policy breach with no customer content accessed (for example a personal phone plugged into a bench PC with no transfer).

**Record the time the company first had reason to believe a breach occurred** (POL-03 4.3). Florida's 30-day clocks run from "the determination of the breach or reason to believe a breach occurred" (Fla. Stat. 501.171(3)(a), (4)(a)). Manufacturer A's 24-hour clock runs from suspicion; the partners' 48-hour clock runs from discovery.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Open the incident log: time of report, reporter, what was seen, the time the company first had reason to believe a breach occurred | Incident commander | Log open |
| 0-1 h | **Branch A:** secure the customer device (bag, label, Depot cabinet), the bench PC (unplug from the network, leave powered on, do not reimage; POL-03 4.5), any USB drives, and CCTV footage (30-day retention; export now) | Store Manager with the incident commander on the phone | Items bagged with chain-of-custody forms |
| 0-1 h | **Branch B:** revoke the affected links; block the source addresses; snapshot the delivery storage access logs and lab storage logs; secure the lab | Data Recovery Manager; Digital Engineering Manager | Links revoked; logs preserved |
| 0-2 h | **Branch A:** HR suspends the workforce member's accounts quietly (identity provider, SYS-01, manufacturer portals, contact center) and decides on paid leave or non-customer work | HR Director with the IT Director | Accounts suspended |
| 0-2 h | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | Chief Financial Officer | Claim number; counsel engaged |
| 0-4 h | Start the contract clocks: Manufacturer A within 24 hours if a program customer or device is involved; the partner within 48 hours if claim data is involved; business accounts within 72 hours of confirmation | Director of Partner Programs; Director of Business Accounts | Notices scheduled in the decision log |
| 2-4 h | Severity 1: convene the CMT; first situation report (scope, customers affected, decisions needed); CEO informs the audit committee chair | CMT chair | CMT meeting held |

## 4. Analysis (RS.AN)
1. **Scope, Branch A.** Which devices did the person handle (SYS-01 ticket assignment history for the last 90 days)? What was accessed (bench session records where they exist; CCTV; the device's own recent-activity data, examined by forensics only)? Were copies made (USB drives, personal phone pairing, cloud uploads from the bench PC, messaging apps)?
2. **Scope, Branch B.** Which cases and files were reached (delivery storage and lab access logs)? From where? Were any files past retention (POL-04 4.7)? Was the data encrypted with uncompromised keys? Encrypted data is outside Florida's definition of personal information when it is rendered unusable (501.171(1)(g)2).
3. **Personal information test (Fla. Stat. 501.171(1)(g)).** For each affected customer, record whether the exposed data includes a name with medical, biometric, or geolocation information (photo location metadata, health app data), a name with a card number and required code, or an email or user name with a password. Device passcodes alone are not listed, but they unlock everything else on the device; counsel decides.
4. **Good-faith test (501.171(1)(a)).** Access during a documented repair test is good faith. Browsing or copying outside the STD-08 checklist is not.
5. **Whose data is it?** Separate the affected list into walk-in and mail-in customers (company is the covered entity), partner claimants (company is the partners' agent), and business account users (contract notices). Record each person's state of residence.
6. **Preserve evidence.** Forensics images the bench PC and media, exports SYS-01 and identity provider logs before they roll over, and keeps chain of custody. **Do not return the customer's device** until forensics releases it; offer a loaner.
7. **Magnitude.** Count affected individuals by state. Florida thresholds: 500 or more for the Department notice; more than 1,000 at a single time for consumer reporting agencies.

## 5. Containment and eradication (RS.MI)
- **Branch A:** end the person's access everywhere the same day (POL-02 4.4), including manufacturer portals and the contact center platform; recover company devices and badges; counsel decides whether to demand return or deletion of copies and whether to involve police; review every other ticket the person handled in the last 90 days.
- **Branch B:** keep links revoked; apply the 14-day expiry and one-time code to all links (POAM-004); purge data past retention after counsel confirms it is no longer evidence; rotate storage access keys; check that the lab array console is reachable only from the lab management network.
- **Both branches:** if the case shows a control failure (for example a legacy-image bench PC), move that store to the front of the POAM-002 rollout.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice before it goes out. The Privacy and Compliance Manager keeps the **decision log** (POL-03 4.6).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this a breach under Fla. Stat. 501.171 and each other affected state's law? Was the access in good faith for a business purpose? | Privacy and Compliance Manager with counsel | Decision log |
| D2 | When did the company first have reason to believe a breach occurred (Florida clock)? | Privacy and Compliance Manager | Decision log |
| D3 | How many affected individuals, by state, and how many Florida residents (500 and 1,000 thresholds)? | Privacy and Compliance Manager | Affected individuals list |
| D4 | Does the case involve partner claim data (partner 48-hour contract notice; 10-day agent notice under 501.171(6)(a))? Does the partner want to notify individuals itself, or ask the company to do so on its behalf (501.171(6)(b))? | General Counsel with the Director of Partner Programs | Decision log |
| D5 | Has law enforcement asked in writing for a delay (501.171(4)(b))? | Counsel | Written request on file |
| D6 | Is a no-notice determination appropriate (501.171(4)(c))? If yes, write it, keep it 5 years, and send it to the Department within 30 days | Privacy and Compliance Manager with counsel | Written determination |
| D7 | Branch A employment action (suspension, termination) and whether to refer to police | HR Director with employment counsel; COO for severity 1 | HR file |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-2 | Insurer hotline; counsel engaged | Chief Financial Officer |
| Within 24 hours of suspicion | Manufacturer A notice if a program customer or device is involved | Director of Partner Programs |
| Within 48 hours of discovery | Partner notice if claim data is involved | Director of Partner Programs |
| Within 72 hours of confirmation | Business account notices under their contracts | Director of Business Accounts |
| Day 0-5 | Staff briefing script (Branch A: no details about the person); what to say to customers who ask | Director of Customer Experience with HR |
| As soon as scoped | Breach determination (D1 to D4) documented | Privacy and Compliance Manager |
| Within 10 days of determination (statutory outer limit) | Agent notice to the partner with the information it needs (501.171(6)(a)), if not already given under the 48-hour term | General Counsel |
| No later than 30 days after determination | Notice to each affected Florida resident by mail or email; Department of Legal Affairs notice if 500 or more Floridians | Privacy and Compliance Manager and counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at a single time | General Counsel |
| Per each state's law | Notices to residents of other states (mail-in customers and claimants) | Outside breach counsel |
| Within 30 days of a no-notice determination | Written determination to the Department | Privacy and Compliance Manager |

**Plan to the shortest clock.** The contract clocks (24 and 48 hours) arrive long before the Florida deadline (30 days), and they start at suspicion or discovery. Do not wait for forensics to finish before calling Manufacturer A or the partner. Give them what is known and update them.

**Communications.**
- Affected customers: a direct call from a Store Manager or the Data Recovery Manager when counsel agrees, then the written notice; offer to return or securely wipe any company copies.
- Partners and Manufacturer A: a call from the Director of Partner Programs, followed by the written notice.
- Media and social posts: holding statement approved by counsel; no names, no details about the workforce member.
- Staff: a short reminder of the customer data access standard and the reporting line, without case details.

**Extortion.** If anyone demands payment to delete or not publish customer data, follow POL-03 4.10 (CEO, counsel, insurer, an OFAC sanctions check, and a report to law enforcement). Paying does not remove notice duties.

## 7. Recovery (RC.RP, RC.CO)
1. Replace the affected bench PC with a standard-image PC; reimage the original only after forensics releases it.
2. Resume data recovery deliveries only with expiring, code-protected links.
3. Return customer devices released by forensics, with the customer told what happened.
4. Confirm that no active sessions remain for the suspended account and that all its local accounts are closed.

**Validate before normal service:** evidence released by counsel; retention applied to the lab and delivery storage; links reissued with expiry; affected customers and partners told when the matter is closed (RC.CO-03). Public statements come only from the Director of Customer Experience after counsel approves (RC.CO-04).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing; written report within 30 days (POL-03 4.13).
- Sanctions decision under POL-01 4.8, documented by HR.
- Update the risk register (P01 R-001, R-005, R-018, R-024), the POA&M (P07), STD-08 test checklists, training content (POAM-017), and this runbook.
- Keep incident records, the decision log, and any no-notice determination for at least 5 years (POL-01 4.13).

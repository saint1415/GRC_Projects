# Incident Response Runbook: Ransomware Across Stores and the Distribution Center

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional grocery retailer: 5 supermarkets, online ordering, a distribution center) |
| Tier / Vertical | Mid-Market / Retail Trade |
| Incident type | Ransomware (with possible data theft) that encrypts store POS servers, the integration platform, the POS head-office application, support-center systems, and DC systems, threatening checkout, SNAP EBT, replenishment, and refrigeration monitoring |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy (4.1, 4.4, 4.8); STD-07 Contingency and recovery standard |
| Companion documents | `ir-runbook.md` (e-commerce skimming); `notification-matrix.csv`; BIA (P05); risk register (P01 R-001, R-006, R-008, R-015, R-018) |
| Runbook owner | Security Manager (incident commander) with the IT Director (recovery lead) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Ransomware tabletop in 2025 (pre-dates this runbook). Executive ransomware tabletop with outside counsel scheduled 2027-02-24 (POAM-010) |

## 0. Why this runbook exists, and how it fits crisis management
Store checkout survives a network or processor outage for up to 24 hours in offline mode, but offline mode runs on the store POS servers that ransomware would encrypt. The DC holds 1 to 3 days of perishable stock, and refrigeration alarms at Stores 4 and 5 share the corporate network. A ransomware attack is therefore a food safety and customer access crisis first, and a card data question second, because the store servers sit in the CDE (P05 enterprise-wide scenario: about $430,000 in lost sales and $150,000 in product over 72 hours).

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, IT Director, Director of Store Operations, Distribution Center Director, Director of Fresh Departments, Director of E-commerce and Marketing, HR Director, outside breach counsel | Store opening hours, cash-only operation, closing a store, product disposal, customer and supplier communications, ransom recommendation to the CEO |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director (recovery lead), security analysts, MSSP, forensic firm (through counsel), POS vendor, cloud and e-commerce vendor contacts | Containment, investigation, eradication, recovery sequence |
| **Store and DC command** | Director of Store Operations, 5 Store Managers, Distribution Center Director, Director of Fresh Departments | Offline-mode and cash-only procedures, manual temperature checks, paper pick lists, direct-store deliveries |

Contacts are the same as `ir-runbook.md` section 0. **Out-of-band first:** assume email, chat, and VoIP are compromised; use the messaging group on personal phones and the printed call trees kept at every store and the DC.

## 1. Preparation checks (Identify / Protect)
- [x] Immutable cloud backups in the separate backup account, 35-day write-once retention (CP-9; P07 confirmed 30 of 30 days and a successful test restore)
- [x] EDR on PCs, laptops, and store POS servers with 24x7 MSSP (SI-3; P07 test passed)
- [ ] Off-site immutable copies of store POS server images. **Gap until POAM-009 closes (2026-11-30)**
- [ ] Restore tests of the integration platform, POS head-office application, and loyalty and CDP database. **Gap until POAM-008 closes (first test 2026-10-27)**
- [ ] POS vendor access through the access broker with named accounts. **Gap until POAM-002 closes**
- [x] Store offline-mode procedure and cash-only lane procedure (tested March 2026)
- [ ] Refrigeration manual-check drill at all stores (P05 finding 5; due 2026-12-31)
- [x] Incident binder at every store and the DC: this runbook, call tree, downtime forms, notification matrix
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption | EDR alert; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Backup deletion attempts, or disabling of EDR or logging | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| New domain administrator, or vendor account activity outside the change schedule | SIEM; access broker | Disable the account; declare if unexplained |
| Registers at several stores lose contact with store servers at once | Store Managers; POS head-office monitoring | IT triage; declare if malicious |
| Large outbound transfer from the loyalty subnet or file services | Cloud firewall flow logs (egress alerting due 2027-01-31) | Block the destination; declare |
| Extortion email or leak-site post naming the company | Email; threat intelligence; FBI | Declare; preserve the message |

**Severity 1 (declare immediately):** any confirmed ransomware execution, any extortion claim, or encryption of any CDE component. **Record the time of first suspicion:** if card data may be involved (store servers or the POS head-office application), the 24-hour acquirer clock may apply (decision R1 below).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; counsel engages forensics | Chief Financial Officer | Claim number; counsel on the call |
| 0-60 min | Protect backups: confirm write-once retention is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-60 min | **Stores:** Store Managers switch registers to offline mode where store servers are healthy, or to cash-only lanes where they are not; post signs; **SNAP EBT cannot run offline**, so follow the EBT processor's outage procedure and tell EBT customers when service will return | Store and DC command | Every store trading or a closure decision recorded |
| 0-2 h | **Food safety:** start manual temperature checks every 2 hours at all stores and the DC; refrigeration contractor on site at Stores 4 and 5 | Director of Fresh Departments | Paper temperature logs running |
| 0-2 h | Sever site-to-cloud VPN tunnels and hub routes to affected segments; disable POS vendor and refrigeration contractor remote access; block known attacker infrastructure | IT Director | Routes down or filtered |
| 0-2 h | Revoke all sessions in the identity provider; reset privileged credentials with break-glass accounts | Security Manager | Sessions revoked |
| 1-2 h | Convene the CMT; first situation report (stores trading, DC status, food safety, data theft signs) | CMT chair | CMT meeting held |
| 2-4 h | Staff briefing script by text and printed at stores: what to do, do not discuss externally, report anything unusual | HR Director with the Director of Store Operations | Script sent |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner; CFO prepares lender notice (contract term) | CEO; CFO | Notices given |

## 4. Analysis (RS.AN)
1. **Scope.** Which store servers, registers, cloud workloads, PCs, and identities are affected? Use EDR telemetry, identity provider sign-ins, cloud control-plane logs in the locked bucket, and firewall flow logs. The store CDE has limited logging until POAM-005 closes, so rely on EDR on the store servers and the POS vendor's records.
2. **Initial access and dwell time.** Check the POS vendor's shared accounts and remote tool first (P01 R-006), then phishing, exposed edge devices, and vendor-installed connections (R-050).
3. **Card data (decision R1).** Did the attacker reach the store servers or POS head-office application while card data passed through them? In-store card data is encrypted at the PIN pad, but the QSA treats these systems as the CDE. If forensics cannot rule out access to card data, treat it as a suspected card compromise: **notify the acquirer within 24 hours** and follow `ir-runbook.md` section 6 in parallel.
4. **Personal data exfiltration.** Determine whether loyalty, customer, or employee data was taken (archive tools, staging folders, egress volume, leak-site samples). Build the affected individuals list by data element and state of residence. This drives the breach determination.
5. **Operational technology.** Check refrigeration controllers, energy management, and DC cold-room controls for tampering. Product exposed to unsafe temperatures is discarded under food safety rules.
6. **Vendor status.** Confirm the e-commerce platform, processor, ERP, WMS, and identity provider are unaffected. If a vendor is the source, record its notice under Fla. Stat. 501.171(6)(a).

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at store firewalls, SD-WAN, and the cloud firewall.
2. Disable compromised accounts. Rotate service, integration, API, POS vendor, and refrigeration contractor credentials. Re-enable vendor access only through the access broker with named accounts.
3. Rebuild affected store servers from the POS vendor image and restore store data from the last clean backup. **Do not decrypt and reuse compromised systems.**
4. Rebuild cloud workloads from clean images in an isolated recovery network; restore data from backups taken before the attacker's first access.
5. Forensics confirms persistence (scheduled tasks, remote tools, rogue accounts, vendor devices) is removed before reconnection.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Outside counsel confirms every notice. The General Counsel keeps the decision log.

| Decision point | Question | Decider |
|---|---|---|
| R1 | Possible card data access in the CDE? If yes: acquirer within 24 hours of suspicion; card brand instructions; PFI if required | CFO with counsel |
| R2 | Breach of personal information under Fla. Stat. 501.171? Time of determination | General Counsel |
| R3 | Affected individuals by state; Florida thresholds (500 for the Department; more than 1,000 for consumer reporting agencies) | Privacy and Compliance Manager |
| R4 | Contract notices: suppliers (72 hours if supplier data affected), lender (5 business days), sponsor | Counsel and CFO |
| R5 | Ransom decision | CEO, on CMT recommendation |

**Ransom decision (POL-03 4.8).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove notice duties if data was taken and does not guarantee deletion. The default position, approved by the CEO, is not to pay while cloud backups are intact.

**Timeline:** acquirer within 24 hours of suspicion if R1 is yes; insurer at hour 0-1; FBI or CISA voluntary report on day 0-2; Florida individual and Department notices within 30 days of determination; consumer reporting agencies without unreasonable delay; other states per each state's law. CIRCIA reporting is not yet required (no final rule).

**Communications.**
- Customers: store signs and website banner within 2 hours of visible disruption (cash-only lanes, EBT status, online ordering status).
- SNAP EBT customers: clear signs on when EBT will return; no surcharge or substitute tender pressure.
- Suppliers and direct-store-delivery vendors: DC status and delivery changes from the Distribution Center Director.
- Media: holding statement approved by counsel; no technical details, ransom, or attribution comments.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). Validate each step (EDR clean, credentials rotated, patches applied, forensics sign-off) before the next.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Identity provider and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 2 | SD-WAN and store networks, POS VLANs first | 2 h | Clean segments only; IoT rules re-applied |
| 3 | Store POS servers and registers | 2 h (offline mode covers up to 24 h) | Rebuilt from the vendor image; EDR healthy |
| 4 | Refrigeration monitoring | 2 h | Alarms reporting; manual checks continue until confirmed |
| 5 | Processor connectivity (cards, then EBT) | 2 h, 4 h | Test transactions approved |
| 6 | E-commerce checkout | 4 h | Platform unaffected; integrity check per `ir-runbook.md` |
| 7 | Integration platform and loyalty API | 8 h | Restored from pre-compromise backup; price file verified |
| 8 | WMS connectivity, DC network, RF handhelds | 12 h | DC trading on system again; paper pick lists reconciled |
| 9 | SIEM feeds and EDR console | 8 h | Monitoring confirmed before wider reconnection |
| 10 | ERP pricing and purchasing | 12 h, 24 h | Price file reconciled with registers |
| 11 | Reporting portal and data warehouse | 24 h, 72 h | Supplier separation retested before suppliers sign in |
| 12 | Payroll and HR | 48 h | Repeat prior payroll if needed |

Re-enter offline and cash transactions, reconcile settlements (BP-13), and keep paper temperature logs with the food safety records. Tell customers, suppliers, and staff when each service is back (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Update the risk register (P01 R-001, R-006, R-008, R-015, R-018, R-050), the POA&M (P07), STD-07, and this runbook.
- If the CDE was involved, tell the QSA and reflect the incident in the next SAQ D and AOC.
- Keep the decision log for at least 5 years and other incident records for at least 3 years.

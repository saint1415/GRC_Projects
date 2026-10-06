# Incident Response Runbook: Ransomware with Guest Data Theft

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Florida hotel owner and operator: 2 independent resorts and 4 franchised select-service hotels) |
| Tier / Vertical | Mid-Market / Accommodation and Food Services |
| Incident type | Ransomware with data theft (double extortion). The attacker takes over a domain or server administrator account outside the privileged access broker, steals guest and employee data, then encrypts the corporate directory, resort servers (including the lock servers and the on-premises PMS interface connectors for locks, POS, and telephones), PCs, and reachable cloud workloads (P01 R-002, High; R-009, R-015) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy (4.3 to 4.10) |
| Companion documents | `ir-runbook.md` (POS and reservation system compromise; roles, privilege protocol, and communications apply here too); `notification-matrix.csv`; BIA (P05); hotel downtime and hurricane procedures |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | 2025 tabletop under the 2024 plan (lessons not yet built in; P07 IR-4). Ransomware tabletop on this runbook, including REIT owner notice, scheduled 2026-12-15 (POAM-009) |

## 0. Why this is different from the card compromise runbook
- **Guest safety comes first.** If the resort lock servers are encrypted, new arrivals cannot get keys and lost keys cannot be cancelled. The BIA gives room access an RTO of 1 hour and an MTD of 2 hours (BP-02), shorter than any IT system. Guest accounting during an evacuation depends on a current in-house list (BP-10).
- **The whole PMPS can be down at once.** The BIA's 72-hour enterprise scenario costs about $620,000 before response and notification costs.
- **There is an extortion decision,** with OFAC, insurer, and law enforcement steps.

Roles, contacts, the out-of-band channel, and the legal privilege protocol are the same as in `ir-runbook.md` section 0. Two additions: the **Resort Chief Engineers** join hotel operations command for lock servers and building systems, and the **Director of Loss Prevention and Safety** leads guest safety and evacuation accounting.

## 1. Preparation checks (Identify / Protect)
- [x] Immutable backups of the workloads account in the separate backup account, 35-day write-once retention, separate administrator credentials (CP-9; 31 of 31 July backup days confirmed in P07)
- [ ] Lock servers backed up nightly to the cloud backup account. **Gap: weekly to a local disk in the same room; the P07 lab restore of the Resort 2 backup failed (POAM-011, due 2026-12-31)**
- [ ] Quarterly restore tests of the data warehouse, CRM, and lock servers. **Gap: first test 2026-11-10 (POAM-011)**
- [ ] Domain and server administrators only through the broker with phishing-resistant MFA. **Gap until POAM-004 closes (2027-03-31)**
- [x] Two sealed break-glass accounts for the identity provider and cloud consoles (POL-02 4.7)
- [x] EDR with 24x7 MSSP on 470 of 520 PCs; MSSP calls within 30 minutes on high severity
- [x] Emergency key cards and mechanical override keys with an entry log at every hotel; printed arrivals and in-house lists at night audit and every 4 hours at the resorts
- [x] 2 pre-imaged spare laptops per hotel for front desk use
- [ ] Cellular hot spots at Hotels 3 to 6 (POAM-020)
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-15

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file renaming, or encryption on servers or PCs | EDR alert; staff report | MSSP isolates hosts (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Attempts to delete backups, disable EDR, or stop logging | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| New domain administrator, or privileged sign-in outside the broker at night | SIEM (identity logs) | Disable the account; declare if unexplained |
| Large outbound transfer from file servers, the data warehouse, the CRM, or the call recording store | Cloud firewall flow logs; SIEM | Block the destination; declare |
| Lock encoders or PMS interfaces stop working at a resort | Front desk; Chief Engineer | IT triage; declare if malicious |
| Extortion email or leak-site post naming the company | Email; threat intelligence; FBI | Declare; preserve the message |

**Severity 1 (declare immediately):** confirmed ransomware execution, confirmed data theft, or an extortion claim naming company data. **Record the time of discovery** (POL-03 4.3).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | **Guest safety.** At every affected hotel: switch to emergency key cards and escorted entry with an entry log; pull the latest printed in-house list; post security staff at entrances if needed | General Managers; Director of Loss Prevention and Safety | Room access running; in-house list in hand |
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MSSP; security analyst | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel and incident log | Incident commander | Log open |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; counsel engages forensics | CFO | Claim number; counsel on the call |
| 0-60 min | **Protect the backups.** Confirm write-once retention is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Sever site-to-cloud VPN tunnels and cloud hub routes to affected segments; block known attacker infrastructure | IT Director | Routes down or filtered |
| 0-2 h | Revoke all sessions in the identity provider; reset privileged credentials using the break-glass accounts; disable all vendor remote access | Security Manager | Sessions revoked |
| 0-2 h | **Downtime procedures** at affected hotels: paper arrivals and folios, P2PE standalone mode at the resort front desks, brand gateway portal at Hotels 3 to 6, room charge and cash at Resort 2 outlets. Never write card numbers on paper | Hotel operations command | Paper workflows running |
| 1-2 h | Convene the CMT; first situation report (guest safety, hotels affected, data at risk, decisions needed) | CMT chair (COO) | Meeting held |
| 2-4 h | Staff briefing script by text: downtime steps, do not discuss outside the company, report anything unusual | Corporate Communications Manager with HR | Script sent |
| 2-4 h | Scope check of Hotels 3 to 6 and brand systems; notify the franchisor within 24 hours if brand systems or guest data at a franchised hotel may be affected | IT Director; General Counsel | Decision recorded |
| Within 24 h | CEO informs the audit committee chair and the PE sponsor's board representative | CEO | Notice given |

**Hurricane overlap.** If a hurricane watch or warning is in effect, the hurricane plan's guest safety decisions take priority, and the CMT decides whether to stop restoration work at a coastal resort until the storm passes.

## 4. Analysis (RS.AN)
1. **Scope.** Which hosts, servers, cloud accounts, and identities are affected? Use EDR telemetry, identity provider sign-ins, cloud control-plane logs in the locked log bucket, and firewall flow logs. The Resort 2 POS server and the lock servers are not in the SIEM today (R-041), so their own logs must be collected before they roll over.
2. **Initial access and dwell time.** Phishing, an exposed edge device (R-027), a vendor remote tool (R-005), or a stolen administrator account (R-009)? Find the first compromised account and the date the attacker first got in. Backups taken before that date are the restore point.
3. **Preserve evidence** with chain of custody. Evidence is held by the forensic firm under counsel.
4. **Data theft.** Determine what was taken: SYS-01 extracts in the data warehouse (about 410,000 guest profiles, with ID document numbers for about 152,000), the CRM (about 265,000 marketing profiles), call recordings (spoken card numbers and security codes until POAM-013 closes), mailboxes with card forms, HR and payroll files (employee Social Security numbers), and time clock finger templates if the HR vendor is involved. Build the **affected individuals list** by data element and state of residence.
5. **Which data elements trigger notice?** Under Fla. Stat. 501.171(1)(g)1.a., personal information includes a name with a Social Security number, a driver license, ID card, or passport number, a card number with any required security code, or biometric data. Marketing profiles with only names, emails, and stay preferences are not personal information under that definition, but other states' laws and the privacy notice may still matter. Counsel decides each category.
6. **Card data.** If recordings, card forms, or keyed CRO card numbers were reachable, the acquirer and card brand steps in `ir-runbook.md` section 6 also apply.
7. **Vendor status.** Confirm with the SYS-01 vendor, the identity provider, the MSSP, and the franchisor that their platforms are unaffected. SYS-01 is vendor-hosted, so the PMS itself normally keeps running; the problem is the on-premises interfaces and the PCs used to reach it.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at site firewalls, the SD-WAN, and the cloud firewall.
2. Disable compromised accounts. Rotate every service account, interface credential (lock, POS, telephone interfaces to SYS-01), and vendor credential.
3. Rebuild the directory from a known-good state, as forensics directs. Rebuild servers and PCs from standard images. **Do not decrypt and reuse compromised systems.**
4. Rebuild cloud workloads from clean images in an isolated network in the workloads account; restore data from backups taken before the attacker's first access.
5. Lock servers: rebuild with the lock vendor from vendor media and restore the last good database. If no usable backup exists (the P07 test failure), re-encode keys for in-house guests from the SYS-01 in-house list and continue on emergency key cards until the database is rebuilt.
6. Forensics confirms that persistence (scheduled tasks, remote tools, rogue accounts) is removed before reconnection.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel confirms every notice before it goes out. The General Counsel keeps the decision log (POL-03 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Was personal information acquired or accessed? Which elements, for whom, and in which states? Date of determination (Florida 30-day clock) | General Counsel with breach counsel | Decision log |
| D2 | How many individuals in total, in Florida, and by state? (500 for the Department of Legal Affairs; more than 1,000 for consumer reporting agencies) | General Counsel | Affected individuals list |
| D3 | Do card brand and acquirer duties apply (card data reachable)? | CFO with the incident commander | Decision log |
| D4 | Franchisor notice (24 hours) and, from 2027-01-01, REIT owner notice (48 hours; third-party agent notice within 10 days of determination under 501.171(6)(a)) | General Counsel | Decision log |
| D5 | Has law enforcement asked in writing for a delay (501.171(4)(b))? | Breach counsel | Written request filed |
| D6 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | CFO |
| Day 0-1 | Franchisor notice if D4 applies (franchise agreement; fictional) | General Counsel |
| Day 0-2 | REIT owner notice if D4 applies, from 2027-01-01 (management agreement; fictional) | General Counsel |
| Day 0-2 | Voluntary report to the FBI and CISA through counsel. It helps the investigation and is a mitigating factor under the OFAC advisory if a payment is ever considered | Security Manager |
| Day 0-3 | Acquirer and Visa steps if D3 applies (`ir-runbook.md` section 6) | CFO |
| Within 30 days of determination | Florida individual notices (15 more days only with written good cause to the Department); Department of Legal Affairs notice if 500 or more Florida residents (no extension) | General Counsel and breach counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at once | Breach counsel |
| Per each state | Residents of other states: apply each state's law to the affected list | Breach counsel |
| Within 10 days of determination, from 2027-01-01 | Third-party agent notice to the REIT owner if its guests' data was affected (501.171(6)(a)) | General Counsel |
| Watch item | CIRCIA: not yet required. If the final rule is published as proposed, the company would likely be covered and would report within 72 hours (incident) and 24 hours (ransom payment) | Security Manager |

**Ransom decision (POL-03 4.8).**
- Needs CEO approval, counsel's advice, the insurer's involvement, an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties on a strict liability basis), and a report to law enforcement.
- Paying does not remove breach notice duties if data was taken, and does not guarantee deletion.
- The default position, approved by the CEO, is **not to pay** while the cloud backups are intact. The lock server gap (POAM-011) is the main thing that could weaken that position, which is why it is a High POA&M item.

**Communications.**
- Guests in house: front desk talking points within 1 hour of visible disruption: keys and payments are being handled manually; guest safety systems are working.
- Arriving guests and group clients: website banner and a call script through the CRO (or the insurer's call center vendor if the CRO is down).
- Franchisor and (from 2027) the REIT owner: direct calls after the contractual notices.
- Media and online travel agencies: holding statement approved by counsel; no ransom or attribution comments.
- Staff: daily briefings through the out-of-band channel.

## 7. Recovery (RC.RP, RC.CO)
Restore in the BIA recovery order (P05 section 8). Each step is validated before the next: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | SD-WAN and internet, resorts first (cellular failover at the resorts; hot spots at Hotels 3 to 6) | 1 h | Clean segments only |
| 2 | Lock servers and encoders at the resorts; confirm the cloud lock service at Hotels 3 to 6 | 1 h (BP-02) | Restored database or re-encoded keys; vendor confirms integrity |
| 3 | Identity provider and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 4 | Clean front desk PCs (pre-imaged spares first) | 2 h | EDR healthy |
| 5 | SYS-01 access and the interface connectors; brand platform status from the franchisor | 2 h (BP-01) | Vendor integrity statement; interfaces re-enabled last |
| 6 | CCTV recording at the resorts | 2 h (BP-10) | Recording confirmed |
| 7 | Payment devices and gateways | 4 h (BP-03) | Device check against the device list |
| 8 | Booking engine and channel manager; CRO contact center | 4 h (BP-04, BP-05) | Inventory reconciled to avoid overbooking |
| 9 | Outlet POS (Resort 1 cloud, then Resort 2 server) | 4 h (BP-06) | Resort 2 rebuilt from vendor media |
| 10 | SIEM feeds and EDR console | 8 h | Monitoring confirmed before wider reconnection |
| 11 | Email, chatbot, websites | 8 h (BP-12) | Restored and scanned |
| 12 | Data warehouse, CRM, integration services; revenue management | 48 h (BP-11) | Restore from pre-compromise backups; manual rates meanwhile |
| 13 | Payroll and timekeeping | 72 h (BP-13) | Paper time sheets; repeat prior payroll if needed |

Back-enter paper folios and charges within 24 hours of restoration, and reconcile room status and in-house lists before releasing emergency key cards. Tell staff, guests, group clients, the franchisor, and (from 2027) the REIT owner when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12). Unlike after the 2025 tabletop, every lesson becomes a dated POA&M item (P07 IR-4 finding).
- Update the risk register (P01: R-002, R-009, R-015, R-029), the POA&M (P07), the BIA if recovery times were different from the targets, the hotel hurricane plans, and both runbooks.
- File the insurance claim with the cost record kept by the Director of Finance.
- Retain all incident documentation, the decision log, and copies of notices; keep any Florida no-harm determination at least 5 years (501.171(4)(c)).

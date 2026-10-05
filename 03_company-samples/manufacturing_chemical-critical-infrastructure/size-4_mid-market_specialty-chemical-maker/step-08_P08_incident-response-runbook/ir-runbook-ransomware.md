# Incident Response Runbook 2: Ransomware with Data Theft on Corporate IT and the Cloud

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed specialty chemical formulator and packager) |
| Tier / Vertical | Mid-Market / Chemical |
| Incident type | A ransomware group gets in through an adversary-in-the-middle phishing attack on an IT administrator, takes over the on-premises directory, steals file share data (formulations, SSI, employee records), and encrypts corporate endpoints, file services, LIMS, and TTRS virtual machines. SSO is unavailable for about 72 hours. Both plants stay in a safe state but shipping drops to about 60% |
| First runbook | `ir-runbook.md` (intrusion into the Port plant process control systems). If any sign of the attack reaches OT, switch to runbook 1 for the OT part |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; part of the Cyber Incident Response Plan (33 CFR 101.620(b)(6)) |
| Runbook owner | Information Security Manager (CySO), with the IT Director for recovery |
| Approved | 2026-09-22 by the Chief Operating Officer |
| Last tested | Not yet. Ransomware tabletop with the crisis management team, counsel, and the insurer planned for 2027-02 (POAM-011) |

## 0. Roles, crisis management, and legal (Govern)
| Role | Primary | Backup |
|---|---|---|
| Cyber incident manager | Information Security Manager (CySO) | Security Analyst |
| IT recovery lead | IT Director | Infrastructure manager |
| OT protection lead | OT Security Engineer | Controls Engineering Manager |
| Crisis management team chair | Chief Operating Officer | Chief Executive Officer |
| Legal, privilege, breach determinations | General Counsel with outside breach counsel (insurer panel) | Outside counsel |
| Insurer, lenders, PE sponsor, ransom decision support | Chief Financial Officer | Controller |
| Business continuity (orders, shipping, TTRS) | VP Sales and Customer Service; Distribution and Fleet Manager; Director of Customer Solutions | Plant Managers |
| HR and employee communications | HR Director | Corporate communications |
| MTSA reporting | Facility Security Officer | CySO |
| External | MSSP (detection and containment support); insurer panel forensics and ransomware negotiator (only on counsel's instruction) | |

**Crisis management team rhythm.** First call within 1 hour of declaration; then twice daily until shipping is back above 90%. Each call: safety status of both plants, scope, containment, legal and reporting clock check, customer impact, recovery ETA.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable backups in the separate backup account with separate credentials (in place); restore tests for file services and TTRS (gap; POAM-021, POAM-005)
- [ ] Break-glass ERP accounts outside SSO for each site, tested quarterly (due 2026-11-30; P01 R-020)
- [ ] Phishing-resistant MFA for administrators (due 2027-03-31; P01 R-028)
- [ ] Printed order and shipping packs: last ERP extract of open orders, water utility priority list, pre-printed hazmat shipping papers for top products
- [ ] TTRS phone workaround list for the 160 water utility tanks (drill due; P01 R-021)
- [ ] Insurer hotline, counsel, and forensics numbers on printed cards
- [ ] OT isolation step rehearsed: the IT/OT firewall pair can go to deny-all without stopping production

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Impossible-travel or new-device sign-in by an administrator; new MFA method registered | Identity provider alert to the MSSP | MSSP disables the session and calls the Security Analyst within 30 minutes |
| Mass file changes or deletion on file services; backup job deletions attempted | Cloud posture alerts; backup account alerts | Declare; isolate file services |
| Large outbound transfer from the business workloads account | Hub firewall egress alert | Declare; block the destination; preserve flow logs |
| Ransom notes; EDR tampering alerts; domain controllers changing group policy | EDR; MSSP | Declare (severity IT-1) |

**Declare** when ransomware, data theft, or administrator account takeover is confirmed or highly likely. **IT-1** (encryption or theft confirmed) convenes the crisis management team within 1 hour.

**Record the time of discovery** and, separately, the time a breach of personal information is determined. The Florida 30-day clock runs from the determination (Fla. Stat. 501.171).

## 3. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Protect OT first.** Set the IT/OT firewall pair to deny-all at the Port plant; block the Inland plant SCADA from the office VLAN (pull the uplink if needed). Plants keep running on local control; shift supervisors are told to watch for anomalies and use runbook 1 if any appear | OT Security Engineer; Shift Supervisors | OT isolated; plants stable |
| 2. **Report under 6.16-1 if the Port plant is affected or endangered.** The Port plant business network, badge and camera servers, and the ERP shipping interface are "on" the facility. The default is to report to the FBI, CISA, and the Captain of the Port immediately; the General Counsel may decide otherwise only if the Port plant is clearly not involved, and records why | FSO with the CySO and General Counsel | Reports made or decision recorded |
| 3. **Contain.** Disable compromised accounts; reset the directory's privileged accounts and the identity provider administrator roles from clean devices; isolate infected subnets at the hub firewall; suspend VPN | IT Director; MSSP | Spread stopped |
| 4. **Protect backups.** Confirm the backup account's write-once lock and credentials are intact; block all sign-ins to it except the 2 named backup administrators | IT Director | Backups confirmed intact |
| 5. **Preserve evidence.** Snapshot affected cloud volumes; export identity provider, EDR, firewall, and cloud audit logs; do not wipe until forensics agrees | Security Analyst; forensics | Evidence preserved under counsel |
| 6. **Call the insurer; counsel engages forensics** | CFO; General Counsel | Claim number |
| 7. **Start business continuity** (section 6) | COO | Paper ordering and shipping running |

## 4. Analysis (RS.AN)
1. **Initial access and spread:** phishing message, compromised accounts, persistence (scheduled tasks, new federation trust, OAuth grants), lateral movement paths.
2. **Data theft:** which shares and buckets were read or copied (file access logs since 2026-08, flow logs, attacker tooling). Classify what was taken: formulations (trade secrets), SSI (FSP, FSA, plan draft), legacy CVI, employee personal information, TTRS customer data.
3. **Personal information determination:** counsel decides whether a breach of personal information occurred and for which individuals, by state of residence. Record the determination date.
4. **SSI loss:** if SSI was taken, the FSO informs the Coast Guard as part of the 6.16-1 report and follows FSP instructions.
5. **OT check:** confirm through the OT sensor and conduit logs that nothing crossed into OT. If anything did, run runbook 1 in parallel.

## 5. Eradication and recovery (RS.MI, RC.RP)
Restore in BIA order (P05 section 8), starting after OT is confirmed safe:
1. Identity provider with break-glass access, then the directory rebuilt or cleaned under forensics guidance (BP-15 dependency, RTO 8 hours)
2. ERP access (vendor unaffected) and order management (BP-15); loading bays and shipping papers (BP-08)
3. TTRS from the backup account to a clean environment (BP-14, RTO 8 hours); telemetry resumes; replenishment orders checked by hand for the first day
4. LIMS (BP-09); file services from immutable backups, restored only after malware scanning
5. Fleet dispatch (BP-13), finance (BP-17), payroll (BP-18)
6. Endpoints reimaged in priority order (control room support PCs, customer service, logistics, then the rest)

**Do not reconnect OT** until forensics confirms the identity provider, directory, and remote access paths are clean. Restore the historian replica last.

## 6. Business continuity during the outage
- **Orders and shipping:** phone and paper orders from the last ERP extract; water utility and food plant customers first; pre-printed hazmat shipping papers checked by two people against the product (49 CFR Part 172 Subpart C).
- **TTRS:** customer service calls the 160 water utility sites daily for tank readings; dispatch from the last known levels plus a safety margin.
- **Quality:** paper worksheets and typed certificates of analysis for up to 2 days.
- **Payroll:** repeat the prior payroll through the provider if needed.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.**

| When | Action | Owner |
|---|---|---|
| Immediately | 6.16-1 report if the Port plant is affected or endangered (section 3 step 2) | FSO with the CySO |
| Day 0 | Insurer; outside counsel; PE sponsor and lender notice per the agreements | CFO; General Counsel |
| Day 0-1 | Customers: delivery impact and TTRS status. Within 72 hours of confirmation, TTRS customers get the contractual security incident notice | Director of Customer Solutions; VP Sales and Customer Service |
| Day 0-2 | Employees: what happened, what not to do, how to work | HR Director with corporate communications |
| Within 30 days of determination | Florida notices to affected individuals; the Department of Legal Affairs if 500 or more Florida residents; consumer reporting agencies if more than 1,000 individuals (Fla. Stat. 501.171). Residents of other states per each state's law | General Counsel with the HR Director |
| As required | Vendor (third-party agent) notices received are logged and drive the same clocks (501.171(6)) | General Counsel |

**Ransom decision:** CEO decision after advice from counsel, the insurer, and law enforcement, and only after an OFAC sanctions check. Restoring from immutable backups is the plan. Paying would not undo the data theft.

**Not required:** SEC 8-K (privately held); CIRCIA (proposed only); HIPAA (fully insured plan).

## 8. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; report to the audit committee.
- Update P01 (R-003, R-020, R-021, R-025, R-028, R-031, R-049), the POA&M, P04, and this runbook.
- Keep incident and notification records with the breach file for at least 5 years.

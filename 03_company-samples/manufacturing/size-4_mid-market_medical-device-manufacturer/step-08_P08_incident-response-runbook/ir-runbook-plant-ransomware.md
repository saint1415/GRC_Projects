# Incident Response Runbook: Ransomware in the Plant OT That Threatens the Build and Signing Path

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed connected medical device manufacturer) |
| Tier / Vertical | Mid-Market / Manufacturing (NAICS 334510) |
| Incident type | Ransomware reaches the plant OT network (MES, test and calibration stations, provisioning server), stops production, and may threaten device history records, the factory provisioning key, or the build and signing pipeline |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-82 Rev. 3 sections 6.4 and 6.5 (OT response and recovery) |
| Policy basis | POL-03 Incident Response Policy (statements 4.4, 4.8 to 4.10) |
| Regulatory basis | QMSR production and records requirements (21 CFR 820.10, 820.35; ISO 13485 clauses 4.2.5 and 7.5.6); FD&C Act 524B(b)(2) if the signing or provisioning path is touched (N31-33-R05); HIPAA 164.410 only if the CCC is reached (N62-R03); state breach laws for employee data; OFAC ransomware advisory (2021-09-21) |
| Companion documents | `ir-runbook.md`; `notification-matrix.csv`; BIA (P05) plant scenario; plant emergency plan |
| Runbook owner | Security Manager (incident commander), with the Plant Manager for production decisions |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. OT ransomware tabletop scheduled 2027-02-10, after the Line 3 segmentation work (POAM-011) |

## 0. Governance, roles, and contacts (Govern)
| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, VP QA/RA, VP Engineering, Plant Manager, Director of Supply Chain, vCISO, Director of Marketing and Communications, HR Director | Production stop and restart, customer allocation from finished goods, ransom (recommendation to the CEO), external statements |
| **Incident response team** | Incident commander: Security Manager. IT Director (recovery lead), OT Engineering Manager, Product Security Manager, MSSP, forensic firm with OT experience (through counsel), line equipment vendor (through the access broker only) | Containment, investigation, eradication, rebuild |
| **Production and quality command** | Plant Manager, Quality Manager, VP QA/RA | Line shutdown, lot holds, record verification, revalidation before release |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on company phones; printed call tree |
| Production decisions | Plant Manager | OT Engineering Manager | Plant radio and cell |
| Signing and provisioning decisions | Product Security Manager | VP Engineering | Cell |
| Legal lead and privilege | General Counsel | Outside breach counsel (insurer panel) | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the incident binder |
| Forensics | Panel firm with OT capability, engaged by counsel | MSSP incident response team | Through counsel |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the binder |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |

**Safety first on the floor.** OT containment must not create a physical hazard. Controls engineers put line equipment in a safe state (stop conveyors, finish or abort reflow cycles, secure calibration benches) before network isolation where time allows.

## 1. Preparation checks (Identify / Protect)
- [x] Firewall between the office and OT networks
- [ ] Line 1 and Line 3 in separate zones (POAM-011, due 2027-03-31). **Until then, isolating Line 3 isolates Line 1 too**
- [ ] Vendor VPN appliance removed (POAM-005, due 2026-11-30). **Until then, step 1 in section 3 is to unplug it**
- [ ] MES backups isolated from the OT network (POAM-010, due 2026-12-31). **Until then, assume the MES backup is lost if the file server is encrypted**
- [ ] Golden images for all 5 station types (POAM-009, due 2027-02-28)
- [x] Release signing in the HSM in the cloud build and signing account, not on the plant network
- [ ] Provisioning issuing key in the HSM (POAM-008, due 2026-12-15). **Until then, the provisioning server is a key-compromise risk**
- [x] Paper travelers and lot hold procedure
- [x] Insurer panel counsel and forensics confirmed; contact list verified 2026-09-17
- [ ] OT monitoring feeding the SIEM (POAM-012, due 2027-03-31)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note or encrypted files on an MES terminal, station, or plant server | Operator report | Supervisor calls the incident line; do not power off |
| EDR alert on an office endpoint with lateral movement toward the OT firewall | MSSP | MSSP isolates the host and calls the Security Manager within 30 minutes |
| Stations fail to start test programs; MES database unreachable | Plant IT and controls engineers | Treat as possible ransomware until ruled out |
| Unexpected vendor VPN session or new admin account on a plant server | Firewall logs; directory | Disable; declare if unexplained |
| Extortion email naming the company | Email; threat intelligence | Declare; preserve the message |

**SEV-1 (declare immediately):** any confirmed ransomware execution in the plant, or any sign the provisioning server, signing path, or MES records were accessed.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | Put affected lines in a safe state; stop starting new units | Plant Manager; controls engineers | Lines safe |
| 0-30 min | **Unplug the vendor VPN appliance**; block office-to-OT rules at the firewall except the management path | OT Engineering Manager | Paths closed |
| 0-30 min | Declare SEV-1; open the out-of-band channel; start the incident log | Security Manager | Log open |
| 0-1 h | Call the insurer hotline before engaging vendors; General Counsel engages counsel; counsel engages OT-capable forensics | CFO; General Counsel | Claim number; counsel on the call |
| 0-1 h | **Stop certificate issuance at the provisioning server and disconnect it**; freeze all signing requests from any plant-connected system; confirm the build and signing account shows no plant-originated activity | Product Security Manager | Issuance stopped; signing log checked |
| 0-2 h | Place all lots in production on hold; record the last verified device history record per line | Quality Manager | ERP hold in place |
| 1-2 h | Convene the CMT; first situation report (lines down, finished goods cover, customer impact) | COO | CMT meeting held |
| 2-4 h | Revoke sessions and reset privileged credentials that touch the plant, using break-glass accounts | Security Manager; IT Director | Credentials reset |
| 2-4 h | CEO informs the audit committee chair and PE sponsor; staff briefing script to plant shifts | CEO; HR Director | Done |

## 4. Analysis (RS.AN)
1. **Scope.** Which stations, servers, and segments are affected? Did the attacker reach the office network, the cloud landing zone, or the CCC? Use EDR on IT endpoints, firewall logs, and the forensic firm's OT capture.
2. **Entry point and dwell time.** Vendor VPN, phishing on an office endpoint, or infected USB media are the likely paths (P01 R-005, R-020).
3. **Records integrity.** Were MES device history records, test results, or certificate issuance logs altered or lost? Compare with ERP shipment records and the last backup.
4. **Key compromise.** Was the provisioning server accessed? If yes, assume its issuing key is compromised: revoke the intermediate certificate, plan re-issuance for units provisioned since the earliest possible access, and treat it as a product security incident under `ir-runbook.md` (device identity is a 524B related-system issue).
5. **Signing path.** Confirm the HSM signing logs show only approved releases. Any doubt makes this a SEV-1 product incident too.
6. **Data taken.** Plant systems hold no PHI, but the office network holds employee records. If employee personal information was taken, state breach laws apply (each state where affected individuals reside; Florida worked example in the notification matrix).
7. **Preserve evidence** with chain of custody, held by the forensic firm under counsel.

## 5. Containment and eradication (RS.MI)
1. Keep the OT network isolated from the office until forensics clears the path.
2. Rebuild MES servers, stations, and the provisioning server from golden images or vendor media. **Do not decrypt and reuse compromised systems.**
3. Reload PLC programs and station scripts from the controlled copies in the repository, then compare against the last known-good hashes.
4. Rotate all plant service, station, and vendor credentials. Vendor access resumes only through the privileged access broker.
5. Forensics confirms persistence is removed before any reconnection.

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each notice.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| P1 | Can any lot be released? Only if its device history records, firmware hashes, and certificate records are verified complete and untampered | Quality Manager with the VP QA/RA | Lot release record |
| P2 | Were rebuilt stations revalidated before use (ISO 13485 clause 7.5.6)? | VP QA/RA | Validation records |
| P3 | Were devices shipped with firmware or certificates that could have been altered? If yes, run `ir-runbook.md` (possible correction under part 806) | VP QA/RA with the Product Security Manager | PSIRT ticket |
| P4 | Did the attack reach the CCC or PHI? If yes, business associate duties apply (164.410 and BAA terms) | Compliance and Privacy Officer | Decision log |
| P5 | Was employee personal information taken? State breach laws apply per state of residence | General Counsel | Decision log |
| P6 | Customer allocation: which orders ship from finished goods first | COO with the Director of Supply Chain | Allocation plan |
| P7 | Ransom | CEO on CMT recommendation, with counsel, insurer, OFAC sanctions check, and law enforcement report | Decision memo |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | CFO; General Counsel |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA; it helps the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory) | Security Manager through counsel |
| Day 0-2 | Customer notice of possible shipment delays (no technical details) to hospitals and distributors with open orders | Director of Customer Support and Field Service |
| Day 0-3 | Lender and PE sponsor notices per financing terms | CFO |
| As applicable | State breach notices for employees (Florida: individuals no later than 30 days after determination; Department of Legal Affairs if 500 or more Florida residents) | General Counsel |
| As applicable | Product and CCC clocks from `ir-runbook.md` if P3 or P4 is yes | VP QA/RA; Compliance and Privacy Officer |

**Ransom decision (POL-03 4.9).** The default position, approved by the CEO, is not to pay while finished goods cover demand and golden images exist. Paying does not restore trust in device records or keys, which must be rebuilt and verified anyway.

**Proposed rules.** CIRCIA reporting (72 hours for covered incidents, 24 hours after a ransom payment) is **proposed only** and not in effect as of 2026-09-25. The proposed criteria would cover this company as a manufacturer of class II devices, so recheck when a final rule is published.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05), validating each step: forensics sign-off for the segment, credentials rotated, allowlisting on, and hashes checked.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Identity provider and administrator access (break-glass if needed) | 1 h | Sessions revoked; privileged credentials rotated |
| 2 | ERP access for shipping from finished goods (BP-13) | 24 h | Shipments released from lots verified before the incident |
| 3 | MES servers and database (BP-12) | 24 h | Restore from the last clean backup; reconcile with ERP and paper travelers; quarantine lots with gaps |
| 4 | Provisioning service (new build, key in the HSM) | 48 h | New issuing certificate; old one revoked if P3 applies |
| 5 | Line 3 stations and calibration benches (BP-11) | 48 h | Rebuilt from golden images; revalidated before use |
| 6 | Line 2 stations (BP-10) | 48 h | Same |
| 7 | Line 1 SMT and AOI equipment (BP-09) | 48 h | Vendor-supported restore through the access broker; AOI model version verified |
| 8 | Line 4 depot, historian, building management system (BP-15) | 72 h | Rebuilt; monitoring confirmed |

Tell hospitals and distributors when normal shipping resumes (RC.CO). Keep lot holds until each lot's records are verified.

## 8. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; written report within 30 days (POL-03 4.12); CAPA for any production records gap.
- Update the risk register (P01: R-005, R-010, R-020, R-021, R-031), the POA&M (P07), this runbook, and STD-04.
- Retain incident records, lot release decisions, and validation records per the retention schedule (at least 6 years for security records; QMS records per the QMSR).

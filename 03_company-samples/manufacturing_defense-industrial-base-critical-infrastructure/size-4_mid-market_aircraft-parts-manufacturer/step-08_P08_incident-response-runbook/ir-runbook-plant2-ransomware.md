# Incident Response Runbook: Ransomware on the Plant 2 Shop Floor

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed aircraft parts manufacturer, DoD subcontractor) |
| Tier / Vertical | Mid-Market / Defense Industrial Base |
| Incident type | Ransomware enters the Plant 2 corporate segment (for example, through a phishing attachment or the open remote desktop service) and spreads across the flat network to the Plant 2 MES and DNC servers, terminals, and the local backup device, stopping assembly, sheet-metal, and additive production. Data theft before encryption is assumed until ruled out |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-82 Rev. 3 guidance on OT incident handling (safety first, isolate before restore) |
| Policy basis | POL-03 Incident Response Policy (4.4, 4.5, 4.11); STD-04 OT and shop-floor security; STD-07 Contingency and recovery |
| Companion documents | `ir-runbook.md` (CUI exfiltration); `notification-matrix.csv`; BIA (P05 BP-02, BP-03, BP-10); risk register (P01 R-004, R-011, R-012, R-013) |
| Runbook owner | Security Manager (incident commander) with the Plant 2 Manager (production lead) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | 2025-09 ransomware tabletop (corporate network only). Plant 2 shop-floor exercise scheduled 2027-02-24, after the Plant 2 network separation (POAM-013, POAM-019) |

## 0. Why this runbook exists
Plant 2 produces about $392,000 of shipments per production day (P05 BP-02). Its shop floor shares a network with its corporate segment, its MES and DNC run on an operating system past end of support, and its only backup is a weekly copy in the same room (P01 R-004, rated Very High). Until the Plant 2 enclave firewall is in place (2027-01-31), one infected office PC can stop the plant. The MES and DNC hold CUI (travelers, NC programs, build files), so a ransomware event there is also a DFARS cyber incident with a 72-hour report.

## 1. Roles (Govern)
The CMT and IRT from `ir-runbook.md` section 0 apply. This runbook adds a **plant command** tier.

| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Containment, evidence, eradication, recovery sequence |
| Plant command lead | Plant 2 Manager | Vice President of Operations | Safe stop of machines, paper travelers, staff, production priorities |
| OT lead | Manufacturing Systems Manager | Plant 2 manufacturing systems engineer | Isolation of shop-floor systems, controller checks, MES and DNC recovery |
| Quality lead | Director of Quality | Plant 2 quality supervisor | Holds on parts in process; revision checks before restart; inspection records |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Customer and prime communications, ransom recommendation, spending |
| Finance | Chief Financial Officer | Controller | Insurer, cash-flow forecast, sponsor and lender updates |
| DoD reporting | Director of Trade Compliance and Contracts | Security Manager | DIBNet report, prime notices, export decision if data was stolen |
| Legal | General Counsel; outside counsel (insurer panel) | n/a | Privilege, extortion response, employee data decisions |
| HR | HR Director | n/a | Staff communications; employee data assessment if HR files on the Plant 2 corporate segment are affected |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file renaming, or encryption on a Plant 2 PC or server | EDR alert via the MSSP; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the Security Manager within 30 minutes |
| MES terminals or DNC stop responding across Plant 2 | Operators; Plant 2 Manager | OT lead checks; declare if malicious or unexplained |
| Remote desktop sign-ins to the Plant 2 MES server from unknown accounts | EDR telemetry; server event logs (not in the SIEM until 2027-01) | Disable the account; declare |
| Deletion of the local backup or disabling of EDR | EDR tamper alert | Treat as a ransomware precursor; declare |
| Extortion email or leak-site post naming the company | Email; threat intelligence; FBI | Declare; preserve the message |

**Declare severity 1** when encryption or destructive activity reaches any Plant 2 shop-floor system, or more than 5 hosts. Record the time of discovery: it starts the DFARS 72-hour clock because the MES and DNC are covered contractor information systems.

## 3. First hour: safety, isolation, evidence (RS.MA, RS.MI)
Order matters. **People and machines first, then isolation, then evidence, then everything else.**

| Step | Who | Done when |
|---|---|---|
| 1. **Safe state for machines.** Operators finish or pause the current operation under supervisor control; no machine is powered off mid-cut or mid-build without the cell lead's call. Additive builds continue if the printer is running standalone | Plant command lead | All machines in a safe state; additive builds logged |
| 2. **Isolate Plant 2.** Disconnect the Plant 2 SD-WAN appliance and site-to-cloud VPN at the Plant 1 and cloud ends so the infection cannot reach Plant 1 or the landing zone. Disconnect the Plant 2 internet circuit | IT Director | Tunnels down; confirmed from Plant 1 and cloud logs |
| 3. Isolate infected hosts through EDR; disable compromised accounts; block remote desktop at the Plant 2 edge | MSSP with the security analysts | EDR shows hosts isolated |
| 4. **Evidence before rebuild.** Capture memory and disk images of the MES and DNC servers and a sample of infected PCs; photograph ransom notes; export EDR telemetry. Do not power off encrypted servers before imaging unless the OT lead documents a safety reason | Forensic firm through counsel; OT lead | Images hashed; chain of custody started |
| 5. Protect remaining backups: confirm the cloud backup account is untouched (Plant 1 and cloud workloads); remove the Plant 2 local backup device from the network and keep it as evidence | IT Director | Backup account integrity confirmed |
| 6. Call the Director of Trade Compliance and Contracts and the COO; start the 72-hour clock in the incident log | Security Manager | Discovery time agreed |
| 7. CFO calls the insurer hotline; General Counsel engages counsel and, through counsel, the forensic firm | CFO; General Counsel | Claim number issued |
| 8. COO convenes the CMT within 2 hours | COO | First CMT meeting held |

## 4. Analysis (RS.AN)
1. **Scope:** which Plant 2 hosts are encrypted; whether any Plant 1 or cloud system shows the same indicators; whether the attacker used the prior owner's or any other inherited account (P01 R-050).
2. **Review for compromise of covered defense information** (252.204-7012(c)(1)(i)): which travelers, NC programs, build files, and inspection records were on affected systems, and whether any were copied out before encryption (firewall and EDR evidence; Plant 2 edge logs are local only until 2027-01).
3. **Personal information:** whether HR files on the Plant 2 corporate segment (payroll exports, onboarding forms) were affected. If yes, General Counsel starts the Florida breach analysis (`notification-matrix.csv`).
4. **Controllers:** with machine vendors through the access broker, check whether any CNC, CMM, additive, or vision cell controller was changed. Controllers are Specialized Assets and usually run embedded systems that the ransomware cannot reach, but programs loaded from infected PCs or USB drives must be treated as suspect.
5. **Malware:** keep isolated samples for DC3 (252.204-7012(d)).

## 5. Production continuity (RC.RP, with the BIA)
| Time from declaration | Action | Owner |
|---|---|---|
| 0-4 hours | Paper travelers from the quality office's controlled copies for jobs on the floor; machines finish loaded jobs | Plant command lead; quality lead |
| 4-24 hours (BP-02 MTD) | Move urgent machined work to Plant 1 where proven programs exist in Plant 1 DNC; prioritize Prime A and Prime C assemblies with near-term ship dates | Vice President of Operations |
| Day 1-2 | Hand-written packing slips and certificates signed by quality; shipments from Plant 2 only for parts with complete paper records (BP-10) | Director of Quality |
| Day 2 onward | Notify primes and Customer D of expected delays; agree priorities | COO with program managers |
| Each day | Cash-flow forecast and sponsor update while Plant 2 is down | CFO |

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** The rows that apply to this incident type:

| When | Action | Owner |
|---|---|---|
| Hour 0-2 | Insurer notified; counsel engaged; CMT convened | CFO; General Counsel; COO |
| Within 24 hours | Audit committee chair and PE sponsor informed | CEO |
| **Within 72 hours of discovery** | **DIBNet report**: the MES and DNC are covered contractor information systems holding CUI. Report what is known, including whether data theft is suspected | Director of Trade Compliance and Contracts |
| As soon as practicable after the report | DoD incident report number to Prime A, Prime B, and Prime C as affected (252.204-7012(m)(2)(ii)) | Director of Trade Compliance and Contracts |
| When malware is isolated | Submit to DC3 (252.204-7012(d)) | Security Manager |
| At least 90 days from the report | Preserve MES, DNC, and PC images and monitoring data (252.204-7012(e)) | Security Manager |
| Day 1-5 | FBI (IC3) or CISA report | Security Manager |
| If HR data affected | Florida individuals within 30 days after determination; Department of Legal Affairs if 500 or more (Fla. Stat. 501.171(3), (4)) | General Counsel with the HR Director |
| If CUI was copied out | Export decision (22 CFR 127.12; 15 CFR 764.5) as in `ir-runbook.md` section 6 | Director of Trade Compliance and Contracts |
| Daily | Staff briefings at Plant 2 (what to do, what not to say) | Plant 2 Manager |

**Ransom decision.** The CMT gives the CEO a recommendation only after: counsel's advice; the insurer's position; an **OFAC sanctions check** (OFAC advisory, 2021-09-21); a realistic recovery estimate without paying (section 7); and law enforcement contact. Paying never removes the DIBNet report or the preservation duty, and a decryptor's output is treated as untrusted (revision check below).

## 7. Recovery (RC.RP)
Recovery follows the BIA priorities (P05 section 8), adjusted for Plant 2:

1. **Clean identity and network.** Reset all Plant 2 local and domain credentials; remove inherited accounts; close remote desktop and legacy file sharing at the edge; bring the Plant 2 tunnel back only to a quarantine segment monitored by the MSSP.
2. **MES and DNC (RTO 12 hours, unproven).** Today: rebuild on new hardware from vendor media and restore the latest clean backup. With weekly local backups (if the device survived), up to a week of status must be rebuilt from paper (P01 R-011). After 2026-11-30: restore from the nightly encrypted copy in the cloud backup account. After 2027-01-31: deploy the replacement MES image with named sign-in.
3. **Revision check before restart.** Before any NC program or build file goes back to a machine, the quality lead compares its revision and checksum with PLM. Programs from Plant 2 PCs, USB drives, or a decryptor are discarded and re-sent from PLM.
4. **Terminals and PCs.** Reimage from the standard image; EDR confirmed before reconnecting.
5. **Inspection and test records.** Re-enter paper inspection reports; hold shipments of parts whose records cannot be reconstructed.
6. **Reconnect to Plant 1 and the cloud** only after the MSSP confirms 72 hours without indicators on the quarantine segment.

**Validate before closing:** no indicators for 14 days of MSSP review, all credentials reset, evidence set complete, and a restore test of the rebuilt MES passed.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; documented within 30 days (POL-03 4.13).
- Update the risk register (R-004, R-011 to R-013, R-050), the POA&M (POAM-012, POAM-017, POAM-019), the BIA recovery times, and this runbook.
- Recalculate the SPRS score if controls changed, and tell the CEO before the next annual affirmation (32 CFR 170.22).
- Brief the audit committee on cost, delivery impact, and the status of the Plant 2 separation.

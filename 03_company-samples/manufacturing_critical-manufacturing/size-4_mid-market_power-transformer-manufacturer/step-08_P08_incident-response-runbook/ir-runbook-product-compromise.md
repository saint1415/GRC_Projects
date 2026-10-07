# Incident Response Runbook 2: Compromise of Products or Services Supplied to Utilities

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed power and distribution transformer manufacturer, Florida) |
| Tier / Vertical | Mid-Market / Critical Manufacturing |
| Incident type | A compromise or serious vulnerability in something the company supplies to utilities: **(A)** the TMU configuration software or its code signing key, **(B)** supplier TMU firmware loaded at final test, or **(C)** the Fleet Monitoring Service (FMS). The cause may be an attack on the company, on the TMU electronics supplier, or on a utility |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF GV.SC-08, ID.RA-08, RS.CO-02, RS.CO-03 |
| Policy basis | POL-03 Incident Response Policy (4.1, 4.8, 4.9); POL-01 4.8 (product security); STD-10 (secure development and product security) |
| Companion documents | `ir-runbook.md` (ransomware); `notification-matrix.csv`; BIA (P05 BP-10, BP-13, BP-14); risk register (P01 R-007, R-012, R-027, R-028, R-045) |
| Runbook owner | VP Engineering (product lead) with the Security Manager (incident commander) and the Director of Digital Services (FMS lead) |
| Approved | 2026-09-15 by the Chief Operating Officer; effective 2026-10-01 |
| Last tested | Not yet. A 24-hour utility notice drill is scheduled each quarter from 2026-12 (POAM-018); a product compromise tabletop is planned with two addendum utilities in 2027-Q1 |

## 0. Why this runbook exists
The company is now a software and data supplier as well as a transformer maker. Thirty-one utilities have written CIP-013-2 supply chain topics into their contracts, and 14 subscribe to the FMS. A compromise of what the company supplies can reach utility substations or utility decisions, even if no company plant stops. In 2026 the company already missed three customer deadlines (P03 G-129, G-130). This runbook exists so that the 24-hour and 48-hour clocks are met the first time it matters.

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Runs the response; coordinates with the MSSP and forensics |
| Product lead (A, B) | VP Engineering | Product software lead | Technical analysis of software, firmware, and signing; fixes and re-releases |
| FMS lead (C) | Director of Digital Services | FMS engineering lead | FMS containment, data integrity, subscriber communication |
| Utility notices and decision log | General Counsel | Outside counsel | Decision D2 (related to products or services supplied?), notice content, contract positions |
| Utility liaison | VP Sales with the Contracts and Trade Compliance Manager | Director of Field Service | Contact lists, delivery holds, coordination with each utility's security team |
| Quality | Director of Quality | Plant 2 quality lead | Hold shipments; verify firmware at final test; trace affected serial numbers |
| Field actions | Director of Field Service | Field service supervisors | Site visits to re-flash or replace TMUs at utility request; access-revocation notices |
| CMT chair (if escalated) | Chief Operating Officer | CEO | Severity 1 decisions, customer commitments, spending |
| Supplier liaison (B) | Director of Supply Chain | VP Engineering | TMU electronics supplier contact and evidence requests |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Vulnerability report on the TMU configuration software or the FMS | Public security contact (intake live 2026-11-15); utility; researcher; CISA | Log at intake with the date and time: **this starts the 30-day disclosure clock** (addendum sec. 4) |
| Signing key or certificate misuse suspected (unknown signed binary, build server compromise, key file accessed) | EDR on the build server; repository alerts; utility report | Revoke the signing certificate; declare severity 1 |
| Hash mismatch on supplier firmware at receipt or at final test | Receiving inspection; final test | Quarantine the lot; hold every TMU configured since the last good check; declare |
| TMU electronics supplier advisory or breach notice | Supplier (inbound) | Product lead assesses within 1 business day |
| FMS anomaly: unknown administrator, data from an unexpected certificate, mass data access, tampered model or alert | FMS gateway and cloud logs; MSSP (once POAM-019 closes); subscriber report | FMS lead isolates (section 3); declare |
| Utility reports suspicious behavior of a TMU, the configuration software, or FMS advisories | Utility security contact | Treat as a possible incident; open the decision log |

**Severity 1 (declare immediately):** signing key compromise; tampered firmware or software confirmed shipped; confirmed intrusion into the FMS; or a known vulnerability being exploited at a utility.

**Record two times in the decision log:** when the company **learned** of the issue (vulnerability clock, 30 days) and when it **confirmed** an incident related to products or services supplied (incident notice clock, 24 or 48 hours per utility).

## 3. First 24 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-1 h | Open the decision log; convene product lead, FMS lead (if C), General Counsel, and incident commander | Incident commander | Log open; times recorded |
| 0-2 h | **(A) Signing:** revoke the code signing certificate; disable the build pipeline; take the download portal offline except for a notice page; image the build server | VP Engineering; IT Director | Certificate revoked; pipeline stopped; evidence imaged |
| 0-2 h | **(B) Firmware:** quarantine affected lots; hold shipments of power transformers with TMUs configured from them; trace serial numbers and utilities | Director of Quality; Director of Supply Chain | Hold placed; affected unit list started |
| 0-2 h | **(C) FMS:** disable the ingestion interface certificate in question (or all, if unclear); put the portal in read-only maintenance mode; snapshot the FMS account; rotate administrator credentials | Director of Digital Services; Security Manager | Account contained; snapshot taken |
| 0-4 h | Insurer hotline if a compromise is suspected; counsel engages forensics | Chief Financial Officer | Claim number |
| 2-8 h | **Decision D2:** is this an incident related to products or services supplied that poses cyber security risk to the utility? Which utilities are affected (by serial numbers shipped, software versions downloaded, or FMS subscription)? | General Counsel with the product or FMS lead | D2 recorded with the time of confirmation |
| Within 24 h of D2 | **Notice to the 9 utilities with 24-hour terms** among those affected; same template, utility-specific facts | General Counsel | Notices sent and logged |
| Within 48 h of D2 | **Notice to the 22 utilities with 48-hour terms** among those affected | General Counsel | Notices sent and logged |
| 4-24 h | Tell the TMU electronics supplier (B) and request its analysis and hashes; tell the CMT chair if severity 1 | Director of Supply Chain; incident commander | Requests sent |

**Notice content (template in the General Counsel's binder):** what is known and not yet known; affected products, versions, serial numbers, or FMS services; indicators the utility can check; interim mitigations (for example, do not install configuration software versions X to Y; isolate TMU configuration laptops; treat FMS advisories since date Z as unverified); company contacts; next update time. Facts only, reviewed by counsel.

## 4. Analysis (RS.AN)
1. **What was touched?** Repository history, build logs, the signing service log (once hardware-backed), download portal logs, the firmware library, receiving and final test records, FMS gateway, database, and model registry logs.
2. **What left the company?** Which signed builds or firmware images were downloaded or shipped, to which utilities, when. For the FMS: which subscribers' data or advisories could have been read or altered.
3. **Root cause:** stolen credentials, build server compromise, supplier compromise, vulnerable dependency, or a flaw in company code. Use the SBOM (once produced, POAM-017) to check dependencies.
4. **Customer impact:** could the issue change a TMU's behavior, expose utility data, or mislead a utility through a wrong or missing FMS alert (P01 R-028)? A reliability engineer reviews every urgent and missed-alert case in the affected period.
5. **Preserve evidence** with chain of custody (POL-03 4.11).

## 5. Containment, eradication, and fix (RS.MI)
- **(A)** Issue a new signing certificate from the hardware-backed key service with 2-person approval; rebuild every supported release from verified source on a clean build host; publish new hashes and the SBOM; give utilities the integrity information before they install (addendum sec. 5).
- **(B)** Obtain verified firmware and hashes from the supplier; re-verify all lots on hand; re-flash affected TMUs at final test; at utility request, field technicians re-flash installed TMUs through the utility's own remote access or on site (addendum sec. 6).
- **(C)** Rebuild FMS components from templates; restore data from a pre-compromise backup; re-issue client certificates to every subscriber with revocation checking on; revalidate the AI-003 model against the model registry before alerting resumes.
- Disclose the vulnerability and fix to every affected addendum utility **within 30 days of learning of it** (addendum sec. 4), even if the fix is not ready, with interim mitigations. Publish the same information to all TMU and FMS customers.
- Coordinate the response with each affected utility's security team (addendum sec. 2): share indicators, timing of fixes, and field actions.

## 6. Notices and communication (RS.CO)
**Follow `notification-matrix.csv`.** The rows most likely to apply here:
- utility incident notice (24 or 48 hours after D2), coordination, vulnerability disclosure (30 days), and integrity information for replacement releases;
- utility access-revocation notice (1 business day) if a field technician's credentials or a field laptop are involved;
- FMS subscriber notice (72 hours after confirmation) and service status updates (C);
- FAR 52.204-25, -23, or -30 reports if covered equipment or articles are found in the supplier chain;
- voluntary reports to the FBI and CISA. CISA also coordinates vulnerability disclosure for industrial control products; the VP Engineering decides with counsel whether to use it;
- the cyber insurer.

**Not required:** CIRCIA (proposed only), DFARS (no DoD work), SEC (private company). NERC itself imposes no duty on the company; the duties come from the addenda.

**External statements:** none until affected utilities have been told directly. A public advisory on the company website follows the utility notices.

## 7. Recovery (RC.RP, RC.CO)
| Step | Target | Validation |
|---|---|---|
| Download portal back with re-signed releases (A) | 48 h from fix | Hashes published; SBOM attached; 2-person approval recorded |
| Final test resumes with verified firmware (B) | 48 h (BP-10) | Every lot re-verified; shipments released by the Director of Quality |
| FMS alerting back (C) | 8 h RTO (BP-14) | Client certificates re-issued; model version matches the registry; reliability engineers review the gap period and call subscribers about any urgent cases |
| Field re-flash program complete | As agreed with each utility | Per-utility tracker; utility sign-off |

Tell affected utilities and subscribers when each step is complete (RC.CO-03).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; report within 30 days, shared in summary with affected utilities.
- Update P01 (R-007, R-012, R-027, R-028, R-045), the POA&M (POAM-017, POAM-018, POAM-019), STD-10, and this runbook.
- Record the notice times against each utility's deadline and report them in the customer obligations appetite measure (P01 section 1).

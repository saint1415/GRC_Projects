# Security Assessment Plan and Summary: Cris Santos Company | Manufacturing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed connected medical device manufacturer) |
| System assessed | Device Lifecycle Platform (DLP, SYS-01 to SYS-09), per the SSP (P02), plus production units of fielded devices drawn from shipped lots |
| Tier / Vertical | Mid-Market / Manufacturing (NAICS 334510) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, 1 OT specialist), reporting to the board audit committee, with an independent device security lab under subcontract for the device tests. Neither designs nor operates any assessed control. The Security Manager and Product Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-10 to 2026-08-28 (plant walkthrough 2026-08-18; device lab testing 2026-08-19) |
| Also satisfies | HIPAA evaluation for the CCC, 45 CFR 164.308(a)(8); annual internal IT audit; evidence for the section 524B processes review in P03 |
| Results accepted | Chief Operating Officer, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **36 controls, 212 determination statements.** Controls were selected because they:
- address the High risks in the risk register (P01), especially the signing, provisioning, plant, and privileged access paths;
- test the section 524B processes and the HIPAA Security Rule standards with gaps in the gap analysis (P03);
- support inherited-control reliance and the SOC 2 scope expansion (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Access lifecycle; 164.308(a)(3)(ii)(C), (a)(4)(ii)(C); R-028 | Focused | Focused (samples of 25) |
| AC-5, AC-6, AC-6(5) | Privileged and separated duties on signing, production, and stations; R-007, R-009 | Comprehensive | Comprehensive (all 58 privileged accounts) |
| AC-17, MA-4 | Vendor remote access into OT; R-020 | Focused | Comprehensive (90 days of vendor logs) |
| AT-3 | Role training for controls engineers and complaint handlers; R-019 | Basic | Focused |
| AU-6, SI-4 | Activity review and monitoring gaps; 164.308(a)(1)(ii)(D); R-007, R-031 | Focused | Focused |
| CM-3, CM-4, CM-7 | Change control and least functionality, including station software; 524B(b)(2); R-024 | Comprehensive | Focused (20 product and 20 station changes; 15 production devices) |
| CM-8, SA-22 | OT inventory and unsupported components; R-023 | Focused | Focused (passive capture on one segment) |
| CM-14, SI-7 | Signed components and integrity; 524B(b)(2); R-009, R-025 | Focused | Focused (tamper tests on 3 units) |
| CP-4, CP-9, CP-10 | Recovery; 164.308(a)(7); R-006, R-012, R-016, R-021 | Comprehensive | Comprehensive |
| IA-2, IA-2(1), IA-3, IA-5 | Unique identity, MFA, device authentication, authenticators; 164.312(d); R-013, R-022 | Focused | Focused |
| IR-4, IR-6, IR-8 | Incident capability across corporate and PSIRT; 164.308(a)(6); 21 CFR 803 and 806; R-042 | Focused | Basic |
| RA-5, RA-5(11), SI-2 | Vulnerability monitoring, CVD, and flaw remediation; 524B(b)(1)-(2); R-001, R-003 | Comprehensive | Focused (25 matched vulnerabilities) |
| SA-9, SR-3 | Third parties and supply chain; 164.308(b); 524B(b)(3); R-029, R-030 | Focused | Comprehensive (all 18 PHI subcontractors; 22 software suppliers) |
| SA-11 | Developer testing; premarket guidance section V.C | Focused | Focused (4 IP-4 releases) |
| SC-7 | Boundary protection in cloud and plant; R-005 | Focused | Focused |
| SC-12, SC-28 | Keys and encryption at rest; R-010, R-012 | Focused | Comprehensive (key inventory) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control operating many times a year with moderate risk; 5 to 10 for weekly or monthly controls; the whole population where it is small or the risk is High. The assessors chose samples at random from populations extracted in their presence. Device units were pulled from finished goods by lot number chosen by the assessors.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 58 | 25 | AC-2 |
| New accounts (CCC, repositories, landing zone) | 140 | 25 | AC-2 |
| Privileged accounts (all planes) | 58 | All 58 for rights; 25 for MFA test | AC-6, AC-6(5), IA-2(1) |
| Product change records (2026) | 212 | 20 | CM-3, CM-4 |
| Test station change records (2026) | 64 | 20 | CM-3, CM-4, AC-5 |
| IP-4 pumps in finished goods (5 lots) | 410 | 10 | CM-7, IA-5 |
| VM-7 monitors in finished goods | 1,350 | 5 | CM-7 |
| Open matched component vulnerabilities | 612 | 25 | RA-5 |
| Critical cloud patch tickets (Q2 2026) | 10 | 10 | SI-2 |
| IP-4 releases (last 2 years) | 4 | 4 | SA-11, SI-2 |
| Security incidents (2026) | 29 | 8 | IR-4, IR-6 |
| PHI subcontractors | 18 | 18 | SA-9 |
| Critical software suppliers | 22 | 22 | SR-3 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Vendor VPN sessions (90 days) | 41 | 41 | MA-4 |
| Laptops for encryption check | 780 | 30 | SC-28 |
| Staff for reporting-awareness interviews | 850 | 15 | IR-6 |

## 3. Methods and objects
- **Examine:** the 2024 policies and the 2026 drafts; the SSP draft; identity provider, cloud, repository, and MES exports; the SPDF, change, MDR, 806, and PSIRT procedures; SBOM match queue; key inventory and HSM policy; backup, patch, and scan reports; BAAs and vendor files; the incident log and the 2025 tabletop report; the plant network diagram and firewall rules.
- **Interview:** vCISO, IT Director, Security Manager, Product Security Manager, VP Engineering, VP QA/RA, Director of Cloud Operations, Plant Manager, OT Engineering Manager, Compliance and Privacy Officer, the MSSP service lead, and 15 randomly selected staff.
- **Test:**
  - MFA sign-in tests on 25 privileged accounts;
  - device lab tests on 10 IP-4 pumps and 5 VM-7 monitors from shipped lots: port and service scan, service and factory mode access attempts, and install attempts with unsigned and wrongly signed images;
  - a 2-hour passive network capture on the Line 1 and Line 3 segment;
  - a test vulnerability report to security@ (acknowledged in 1 business day);
  - a restore of one CCC table snapshot into the non-production account;
  - a review of 90 days of vendor VPN logs.

## 4. Rules of engagement
- No testing on the production CCC beyond read-only configuration review. No active scanning of plant OT while lines were running; the passive capture used a mirror port approved by the Plant Manager.
- Device tests ran in the independent lab on units pulled from finished goods, which were then quarantined and reworked. No PHI was on the units.
- No PHI left company systems. Screenshots were redacted, and evidence is held in the firm's encrypted workpaper system under a subcontractor BAA.
- **Stop-and-notify rule: used once.** On 2026-08-19 the lab found that all 10 sampled IP-4 pumps had the factory service mode enabled on the wireless interface, reachable with one factory credential. MES records traced it to a 2026-03-02 Line 3 script change and 1,140 pumps shipped since then. The assessors told the Product Security Manager and the VP QA/RA the same day. The company:
  - declared a product security incident (SEV-2) and logged 2026-08-19 as the date it learned of the vulnerability;
  - fixed the Line 3 script and quarantined finished goods on 2026-08-21;
  - added R-049 to P01 on 2026-08-21;
  - followed the P08 runbook (section 9 of `../step-08_P08_incident-response-runbook/ir-runbook.md`).

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 136 |
| Other than satisfied | 76 |
| **Total** | **212** |

Other than satisfied statements by risk: 40 High, 36 Moderate.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 20 | 6 | Moderate | POAM-004 |
| AC-5 | 1 | 1 | Moderate | POAM-002 |
| AC-6 | 0 | 1 | High | POAM-003 |
| AC-6(5) | 0 | 1 | High | POAM-003 |
| AC-17 | 2 | 2 | High | POAM-005 |
| AT-3 | 6 | 3 | Moderate | POAM-017 |
| AU-6 | 2 | 1 | High | POAM-012 |
| CM-3 | 7 | 3 | High | POAM-002 |
| CM-4 | 1 | 1 | High | POAM-002 |
| CM-7 | 3 | 3 | High | POAM-001 |
| CM-8 | 2 | 4 | Moderate | POAM-015 |
| CM-14 | 2 | 0 | n/a | n/a |
| CP-4 | 3 | 2 | High | POAM-009 |
| CP-9 | 4 | 2 | Moderate | POAM-010 |
| CP-10 | 0 | 2 | High | POAM-009 |
| IA-2 | 0 | 2 | Moderate | POAM-006 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-3 | 0 | 1 | Moderate | POAM-019 |
| IA-5 | 6 | 4 | High, Moderate | POAM-001, POAM-006 |
| IR-4 | 9 | 4 | Moderate | POAM-013 |
| IR-6 | 1 | 1 | Moderate | POAM-013 |
| IR-8 | 15 | 2 | Moderate | POAM-013 |
| MA-4 | 1 | 7 | High | POAM-005 |
| PS-4 | 4 | 1 | Moderate | POAM-004 |
| RA-5 | 6 | 3 | High | POAM-007 |
| RA-5(11) | 1 | 0 | n/a | n/a |
| SA-9 | 3 | 3 | High | POAM-014 |
| SA-11 | 7 | 2 | Moderate | POAM-016 |
| SA-22 | 1 | 1 | Moderate | POAM-015 |
| SC-7 | 3 | 3 | High | POAM-011 |
| SC-12 | 0 | 2 | Moderate | POAM-008 |
| SC-28 | 1 | 0 | n/a | n/a |
| SI-2 | 8 | 2 | High | POAM-007 |
| SI-4 | 8 | 4 | High | POAM-012 |
| SI-7 | 6 | 0 | n/a | n/a |
| SR-3 | 2 | 2 | Moderate | POAM-014 |

**Fully satisfied (5 controls):** CM-14 and SI-7 (every unsigned or wrongly signed image was rejected by VM-7 and IP-4 units), IA-2(1) (hardware-key MFA on all 25 sampled privileged accounts), RA-5(11) (the public reporting channel works), and SC-28 (encryption at rest for the CCC and 30 of 30 laptops). These confirm the strengths in the scenario facts: the company's code integrity chain is sound.

**Fully other than satisfied (6 controls):** AC-6, AC-6(5), CP-10, IA-2, IA-3, and SC-12.

**Themes:**
1. **The product is signed well, but the factory is not controlled like the product.** Station software changes, factory modes, and the provisioning key sit outside the SPDF (CM-3, CM-4, CM-7, AC-5, SC-12). R-049 is the result.
2. **Privileged and vendor access** is the largest exposure in the cloud and the plant (AC-6, AC-6(5), AC-17, MA-4).
3. **Recovery is designed but unproven** for the CCC, the keys, and the MES (CP-4, CP-9, CP-10).
4. **Visibility gaps** leave the plant, the build pipeline, and privileged CCC activity outside monitoring (AU-6, SI-4, CM-8).

**POA&M:** 31 controls had at least one Other than satisfied statement. They map to 18 POA&M items (POAM-001 to POAM-017 and POAM-019), because related controls share an item. Three more items come from the gap analysis and the AI assessment (POAM-018 AI governance, POAM-020 806 fallback and MDR training, POAM-021 standards). The total is 21 items: 9 High and 12 Moderate. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-08-03 | Plan and sample requests issued |
| 2026-08-10 to 2026-08-14 | Document examination and interviews |
| 2026-08-17 to 2026-08-21 | Plant walkthrough (2026-08-18), device lab tests (2026-08-19), technical tests |
| 2026-08-24 to 2026-08-28 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (212 rows); `poam.csv` (21 items).

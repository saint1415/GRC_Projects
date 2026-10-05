# Security Assessment Plan and Summary: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed owner and operator of a single-unit nuclear generating station) |
| System assessed | Plant Business Network and Work Management System (PBN-WMS, SYS-01 to SYS-11), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Nuclear Reactors, Materials, and Waste |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 2 IT auditors), reporting to the board audit committee, with 1 Nuclear Oversight assessor for the CSP boundary tests. Neither designs or operates any assessed control. The IT Security Manager coordinated access but did not select samples or rate findings. The CST supported the boundary tests but did not rate them |
| Assessment window | 2026-08-03 to 2026-08-21 (Station and EOF walkthroughs 2026-08-10 to 2026-08-13) |
| Also satisfies | Annual internal IT audit; input to the next 73.55(m) program review |
| Results accepted | Site Vice President, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **33 controls, 245 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- test the business network side of the CSP boundary and the controls behind the High gaps in P03;
- support inherited-control reliance and SOC 2 readiness for the GDSR service (P09).

CDAs at Levels 3 and 4 were **out of scope**. They are assessed by the CST under the CSP and reviewed by Nuclear Oversight under 73.55(m).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Access lifecycle, outage contractor accounts; R-038, R-039 | Focused | Focused (samples of 25) |
| AC-4, SC-7 | Segmentation and the CSP boundary; R-001, R-005; G-012 | Comprehensive | Comprehensive (all paths to the receive server) |
| AC-6, IA-2(1), IA-5 | Privileged access, default credentials; R-004, R-052 | Comprehensive | Comprehensive (all 16 domain administrators) |
| AC-17, MA-4 | Vendor remote access; R-008, R-009; G-077 | Focused | Focused |
| AT-2 | Contractor awareness; G-015 | Basic | Focused |
| AU-2, AU-6, SI-4 | Monitoring of the boundary and applications; R-012; G-020 | Focused | Focused |
| CA-3 | Interconnections (vendor VPN, gateway) | Basic | Focused |
| CM-3, CM-6, CM-8 | Change control and the CST gate, hardening, inventory; R-006, R-043; G-017 | Focused | Focused (25 changes; 10 servers) |
| CP-2, CP-4, CP-9, CP-10 | Recovery and 73.77(b) fallback; R-002 (Very High), R-010, R-011 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Integration with the CSP and 73.77; R-013; G-047, G-049 | Focused | Focused |
| MP-7 | Portable media rules; R-035 | Basic | Focused |
| PE-3 | Site data center and EOF network room | Basic | Focused (2 locations) |
| PS-3 | 73.56 coverage for electronic access; G-064 | Focused | Comprehensive (23 administrators) |
| RA-5, SI-2 | Vulnerability and patch management; R-042 | Focused | Focused |
| SA-9 | Vendor oversight; R-014 | Focused | Focused (24 Tier 1 files) |
| SA-22 | Legacy clearance servers; R-018 | Basic | Comprehensive (2 servers) |
| SC-28, SI-3 | Encryption and EDR | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for controls operating many times a year with moderate risk; 5 to 10 items for weekly or monthly controls; whole populations where small. Samples were chosen at random from populations extracted in the assessors' presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 58 | 25 | AC-2 |
| Outage contractor accounts (2025 outage) | about 1,000 | 25 | AC-2 |
| Domain administrator accounts | 16 | 16 | AC-6 |
| Privileged accounts (all planes) | 41 | 25 (MFA test) | IA-2(1) |
| Network devices and server management interfaces | about 60 | 15 (default credential test) | IA-5 |
| IT change tickets (2024-2026) | 212 | 25 | CM-3 |
| Servers | 90 | 10 (benchmark scan) | CM-6 |
| Backup jobs (July 2026) | 31 | 31 | CP-9 |
| Endpoints | about 1,370 | 30 (encryption); 7 (EDR test) | SC-28, SI-3 |
| Critical vulnerability findings (Q1-Q2 2026) | 40 | 40 | RA-5, SI-2 |
| Incidents (2025-2026) | 31 | 8 | IR-4 |
| Tier 1 vendor files | 24 | 24 | SA-9 |
| Administrators with electronic access near safety, security, or EP | 23 | 23 | PS-3 |
| Staff and contractors for awareness interviews | about 2,150 at peak | 25 (15 staff, 10 contractors) | AT-2, IR-6 |

## 3. Methods and objects
- **Examine:** the 2022 policies and the 2026 drafts; the SSP draft; directory, identity provider, cloud, and VPN exports; firewall rules; backup, patch, scan, and EDR reports; change tickets; vendor files; the 2023 IT incident and DR plans; the CSP incident response procedure (in the SRI room); the defensive architecture drawing (in the SRI room).
- **Interview:** vCISO, IT Director, IT Security Manager and both analysts, Cyber Security Program Manager and 2 CST members, 2 Shift Managers, Regulatory Affairs Manager, Emergency Preparedness Manager, Director of Security, Director of Work Management, HR Director, the MSSP service lead, and 25 staff and contractors.
- **Test:**
  - reachability tests from a work control center workstation and from the cloud workloads account toward the receive server and boundary addresses (2026-08-12, with the CST present);
  - a test connection attempt to a boundary address to check for an alert (2026-08-12);
  - a simulated boundary-probe alert to test MSSP escalation (2026-08-13);
  - default credential tests on 15 network devices and management interfaces;
  - passive discovery on the server VLAN (2026-08-11);
  - MFA sign-in tests on 25 privileged accounts;
  - benchmark scans of 10 servers;
  - EDR test files on 5 endpoints and 2 servers;
  - restore of one file share folder from the recovery account (2026-08-14).

## 4. Rules of engagement
- **No testing at Level 3 or Level 4, and nothing that touches a CDA.** All tests ran on the business network or the cloud. Every boundary test was approved in advance by the Cyber Security Program Manager and the Shift Manager on duty, who were told when it started and ended so that no test could be mistaken for a real event.
- No SGI was handled. CSP documents were reviewed only in the SRI room; no copies left it.
- Personal information (access authorization files) was reviewed in the enclave by the Director of Security's staff, with assessors seeing redacted extracts only.
- **Stop-and-notify rule:** any critical exposure is reported to the IT Director, the vCISO, and the Cyber Security Program Manager the same day. **Used once:** on 2026-08-12 the assessors found the receive server's management interface on the server VLAN with the manufacturer default password. The CST disconnected it on 2026-08-14 and entered it in the CAP. The company logged it as P01 R-052 the same day. The Shift Manager reviewed it against 73.77 and determined that no notification was required because no cyberattack had occurred; the condition itself was recorded in the CAP within 24 hours as a program weakness (73.77(b)(1)).

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 158 |
| Other than satisfied | 87 |
| **Total** | **245** |

Other than satisfied statements by risk: 56 High, 27 Moderate, 4 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 21 | 5 | Moderate | POAM-001 |
| AC-4 | 0 | 1 | High | POAM-018 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | High | POAM-003 |
| AT-2 | 8 | 2 | Low | POAM-004 |
| AU-2 | 1 | 5 | High | POAM-005 |
| AU-6 | 1 | 2 | High | POAM-005 |
| CA-3 | 5 | 3 | Moderate | POAM-006 |
| CM-3 | 6 | 4 | High | POAM-007 |
| CM-6 | 3 | 3 | Moderate | POAM-008 |
| CM-8 | 3 | 3 | High | POAM-009 |
| CP-2 | 12 | 12 | High | POAM-010 |
| CP-4 | 0 | 5 | High | POAM-010 |
| CP-9 | 6 | 0 | n/a | n/a |
| CP-10 | 0 | 2 | High | POAM-010 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 7 | 3 | High | POAM-011 |
| IR-4 | 9 | 4 | High | POAM-012 |
| IR-6 | 1 | 1 | High | POAM-012 |
| IR-8 | 11 | 6 | Moderate | POAM-012 |
| MA-4 | 3 | 5 | High | POAM-003 |
| MP-7 | 2 | 0 | n/a | n/a |
| PE-3 | 10 | 2 | Low | POAM-013 |
| PS-3 | 2 | 1 | Moderate | POAM-014 |
| PS-4 | 4 | 1 | Moderate | POAM-001 |
| RA-5 | 6 | 3 | Moderate | POAM-015 |
| SA-9 | 3 | 3 | Moderate | POAM-016 |
| SA-22 | 1 | 1 | High | POAM-017 |
| SC-7 | 4 | 2 | High | POAM-018 |
| SC-28 | 1 | 0 | n/a | n/a |
| SI-2 | 8 | 2 | Moderate | POAM-015 |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-4 | 9 | 3 | High | POAM-005 |

**Fully satisfied (5 controls):** CP-9 (isolated, write-once backups; 31 of 31 jobs; file share restore worked), IA-2(1) (MFA on all 25 sampled privileged VPN and cloud sign-ins), MP-7 (removable media scanned; kiosk logs complete), SC-28 (30 of 30 endpoints encrypted), and SI-3 (EDR detected every test file within 5 minutes).

**Fully other than satisfied (4 controls):** AC-4, AC-6, CP-4, and CP-10.

**The boundary itself held.** No test from the business network or the cloud reached Level 3. The one-way device did its job. The findings are all on the Level 2 side.

**Themes:**
1. **The seam with the CSP.** Changes, alerts, and incident reports on the business network do not reach the CST or the Shift Manager (CM-3, AU-6, IR-4, IR-6). The simulated boundary probe was escalated to IT in 25 minutes, but nobody called the CST.
2. **Privileged and vendor access** remains the largest attack path (AC-6, AC-17, MA-4, IA-5).
3. **Recovery is unproven** for the systems the BIA ranks highest during an outage (CP-2, CP-4, CP-10).

**POA&M:** 28 controls had at least one Other than satisfied statement. They map to 18 POA&M items (POAM-001 to POAM-018), because related controls share an item. Four more items come from the gap analysis, the SOC 2 readiness work, and the AI assessment (POAM-019 CDA analysis of 3 changes, POAM-020 SRI handling, POAM-021 AI governance, POAM-022 GDSR SOC 2 readiness). The total is 22 items: 11 High, 9 Moderate, and 2 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan, rules of engagement, and sample requests issued; CST and Shift Manager approval of boundary tests |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Walkthroughs and technical tests |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (245 rows); `poam.csv` (22 items).

# Security Assessment Plan and Summary: Cris Santos Company | Information Technology | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (cloud hosting and managed infrastructure provider) |
| System assessed | Hosting Control Plane and Customer Portal (HCP), both partitions, per the SSP (P02) |
| Tier / Vertical | Mid-Market / Information Technology |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 3 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control and is not the FedRAMP independent assessment service. The GRC Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (DC-1 walkthrough 2026-08-11; DC-2 walkthrough 2026-08-13) |
| Relationship to FedRAMP | Not a FedRAMP independent assessment. It is the company's annual internal assessment of both partitions, scoped to the Class C annual assessment list so that the results prepare the 2027 FedRAMP assessment (planned start 2027-02-15) |
| Results accepted | Chief Technology Officer, 2026-09-22; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **40 controls, 185 determination statements.**
- **34 base controls** that FedRAMP requires in each year's independent assessment for Rev5 Class C (IVV-CSF-AIA).
- **6 enhancements** tied to the top risks in P01: AC-2(9), AC-6(5), IA-2(1), and SI-7(1), which are also on the annual list, plus RA-5(5) and CP-9(1).
- Every statement was assessed in **both partitions**, because the company's policy (POL-01 section 4.3) applies one standard to both, and because the 2026 boundary (P02 section 7) brings shared components into scope.

| Control group | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-2(9), AC-3, IA-2, IA-2(1), IA-4, IA-5 | Account lifecycle, shared accounts, MFA, machine credentials; P01 R-003, R-010, R-026; P03 G-092, G-152, G-155 | Comprehensive | Comprehensive (all privileged accounts; samples of 25) |
| AC-6, AC-6(5) | Standing privilege; R-002, R-009 | Comprehensive | Comprehensive (214 privileged accounts) |
| AU-2, AU-3, AU-4, AU-5, AU-6, AU-8, AU-11, AU-12 | Logging gaps and AI triage; R-015, R-016 | Focused | Focused (8 log sources; 50 auto-closed alerts) |
| CM-5, CM-6, CM-7, CM-8 | Change access, drift, boundary inventory; R-017, R-026, R-035 | Focused | Focused (40 hosts; 3 accounts; 2 clusters) |
| CP-4, CP-9(1) | Recovery testing; R-004, R-005, R-018 | Comprehensive | Comprehensive (all tests in 2025-2026) |
| IR-3, IR-4 | Incident capability under the 2026 rules; R-030 | Focused | Focused (10 of 27 incidents) |
| PE-3 | Cage access at DC-1 and DC-2 | Basic | Focused (2 of 3 data centers) |
| RA-5, RA-5(5) | Vulnerability management at scale; R-006 | Focused | Focused (50 findings) |
| SA-9 | External services and third-party resources; R-025 | Focused | Focused (6 services; 14 Tier 1 files) |
| SC-7, SC-8, SC-12, SC-13, SC-21, SC-28 | Boundary, cryptography, encryption at rest; R-003, R-011, R-038 | Focused | Focused |
| SI-3, SI-6, SI-7, SI-7(1), SI-10 | Malware protection, security function checks, template integrity, input validation; R-011 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 74 | 25 | AC-2 |
| Transfers | 41 | 25 | AC-2 |
| New workforce accounts | 118 | 25 | AC-2 |
| Privileged accounts | 214 | 25 for MFA test; all 214 for rights review | IA-2(1), AC-6, AC-6(5) |
| Machine credentials found by secret scanning and cloud APIs | 312 | All 312 matched to the vault inventory | IA-5, CM-5 |
| Hosts for configuration scan | 540 | 40 (20 at DC-1) | CM-6 |
| Commercial volumes | about 24,000 | 30 | SC-28 |
| Auto-closed SIEM alerts (July 2026) | about 18,000 | 50 | AU-6 |
| Incidents (2025-2026) | 27 | 10 | IR-4 |
| Critical and high vulnerability findings (2026-Q1 and Q2) | 50 | 50 | RA-5 |
| Tier 1 vendors | 14 | 14 | SA-9 |
| Restore tests (2025-2026) | 6 | 6 | CP-4, CP-9(1) |
| Data centers for walkthroughs | 3 | 2 (DC-1, DC-2) | PE-3, SC-7 |

## 3. Methods and objects
- **Examine:**
  - POL-01 to POL-05 and the revised standards
  - the SSP draft (P02) and the 2024 FedRAMP SSP
  - identity provider, cloud, PAM, hypervisor manager, and CMDB exports
  - scan, patch, drift, EDR, and backup reports
  - the vault inventory and secret scanning results
  - vendor files and contracts
  - the incident log, the 2026-02 tabletop report, and the contingency test reports
- **Interview:**
  - Director of Security, GRC Manager, Security Operations Manager, Security Engineering Lead
  - VP Platform Engineering, VP Software Engineering, Director of Cloud Operations
  - Director of NOC and Customer Support, Federal Program Director
  - DC-1 and DC-2 data center operations managers
  - the MDR partner's service lead
- **Test:**
  - MFA sign-in tests on 25 sampled privileged accounts, including DC-1 clusters A and B
  - reachability tests from the NOC network to the management networks at DC-1 and DC-2
  - deployment of an unsigned VM template in each partition (non-production clusters)
  - a log forwarder stopped for 35 minutes in non-production (AU-5)
  - PAM session recording stopped on one bastion (SI-6)
  - EICAR test files on 5 bastions and build runners
  - DNSSEC validation with a signed and a deliberately broken test zone
  - 20 malformed API requests against the non-production API
  - benchmark configuration scans of 40 hosts

## 4. Rules of engagement
- No testing that could disrupt customer workloads. Template and API tests ran on non-production clusters and accounts. Reachability tests used read-only probes.
- No customer data left company systems. Evidence was stored in the firm's encrypted workpaper system. Government partition evidence stayed with U.S.-person auditors.
- Stop-and-notify rule: any critical exposure is reported to the Director of Security the same day. **Used once:** on 2026-08-14 the assessors reported a 2024 deploy token with write access to the government partition's deployment repository, no expiry, and no inventory record. The company revoked it on 2026-08-15, logged P01 R-026, and the Federal Program Director evaluated it as not a FedRAMP reportable incident because the token's audit history showed no use since 2024. This is gap 15 in `../00_company-facts.md`.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 143 |
| Other than satisfied | 42 |
| **Total** | **185** |

Other than satisfied statements by risk: 20 High, 19 Moderate, 3 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 20 | 6 | High | POAM-001, POAM-002, POAM-004, POAM-005 |
| AC-3 | 1 | 0 | n/a | n/a |
| AC-6 | 0 | 1 | High | POAM-003 |
| AU-2 | 5 | 1 | High | POAM-005 |
| AU-3 | 6 | 0 | n/a | n/a |
| AU-4 | 1 | 0 | n/a | n/a |
| AU-5 | 2 | 0 | n/a | n/a |
| AU-6 | 2 | 1 | High | POAM-006 |
| AU-8 | 2 | 0 | n/a | n/a |
| AU-11 | 0 | 1 | Moderate | POAM-005 |
| AU-12 | 2 | 1 | Moderate | POAM-005 |
| CM-5 | 5 | 1 | High | POAM-004 |
| CM-6 | 3 | 3 | Moderate | POAM-007 |
| CM-7 | 6 | 0 | n/a | n/a |
| CM-8 | 4 | 2 | High | POAM-008 |
| CP-4 | 3 | 2 | High | POAM-009 |
| IA-2 | 1 | 1 | High | POAM-002 |
| IA-4 | 4 | 0 | n/a | n/a |
| IA-5 | 7 | 3 | High | POAM-002, POAM-004 |
| IR-3 | 0 | 1 | Moderate | POAM-010 |
| IR-4 | 10 | 3 | Moderate | POAM-010 |
| PE-3 | 10 | 2 | Low | POAM-011 |
| RA-5 | 7 | 2 | High | POAM-012 |
| SA-9 | 4 | 2 | High | POAM-008, POAM-013 |
| SC-7 | 5 | 1 | Moderate | POAM-014 |
| SC-8 | 1 | 0 | n/a | n/a |
| SC-12 | 1 | 1 | High | POAM-015 |
| SC-13 | 1 | 1 | Low | POAM-016 |
| SC-21 | 4 | 0 | n/a | n/a |
| SC-28 | 0 | 1 | Moderate | POAM-017 |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-6 | 7 | 0 | n/a | n/a |
| SI-7 | 5 | 1 | High | POAM-015 |
| SI-10 | 1 | 0 | n/a | n/a |
| AC-2(9) | 0 | 1 | High | POAM-002 |
| AC-6(5) | 0 | 1 | Moderate | POAM-003 |
| IA-2(1) | 0 | 1 | High | POAM-002 |
| RA-5(5) | 1 | 0 | n/a | n/a |
| SI-7(1) | 2 | 1 | Moderate | POAM-015 |
| CP-9(1) | 2 | 0 | n/a | n/a |

**Fully satisfied (14 controls):** AC-3, AU-3, AU-4, AU-5, AU-8, CM-7, IA-4, SC-8, SC-21, SI-3, SI-6, SI-10, RA-5(5), and CP-9(1). They confirm the strengths in the scenario facts: role-based access, complete audit content, TLS everywhere, EDR, daily security function checks, and tested, immutable backups.

**Fully other than satisfied (7 controls):** AC-6, AU-11, IR-3, SC-28, AC-2(9), AC-6(5), and IA-2(1).

**Themes:**
1. **Two-speed security is real and testable.** The same test passed at DC-2 and failed at DC-1 (SC-7 reachability), and passed in the government partition and failed in the commercial one (SI-7 unsigned template). About half of the 42 Other than satisfied statements involve DC-1, most of them clusters A and B.
2. **Machine identities are the blind spot (CM-5, IA-5, AC-2).** Human access is well controlled; one forgotten deploy token bypassed it.
3. **Detection depends on what the SIEM sees and what the AI closes (AU-2, AU-6, AU-12).**
4. **The 2026 FedRAMP rules show up as procedure gaps (IR-3, IR-4, RA-5, CM-8, SA-9)**, not as missing technology.

**POA&M:** 26 controls had at least one Other than satisfied statement. They map to 17 POA&M items (POAM-001 to POAM-017), because related controls share an item. Eight more items come from the gap analysis, the risk register, and the AI assessment: POAM-018 FedRAMP 2026 rules transition, POAM-019 bank notice readiness, POAM-020 RMM tool hardening, POAM-021 DFARS incident path, POAM-022 contingency plan and DC-1, POAM-023 customer administrator MFA, POAM-024 FedRAMP emergency messages, and POAM-025 AI governance. The total is 25 items: 15 High, 8 Moderate, and 2 Low. See `poam.csv`.

**Relationship to the legacy FedRAMP POA&M.** The Government Cloud's legacy POA&M (41 open items at 2026-07-31, 3 past due) continues to go to agencies monthly until the VDR and VER rules replace it. Items in both lists are cross-referenced by the GRC Manager.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-14 | Data center walkthroughs and technical tests |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-22 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (185 rows); `poam.csv` (25 items).

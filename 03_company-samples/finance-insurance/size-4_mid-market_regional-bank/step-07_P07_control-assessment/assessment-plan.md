# Security Assessment Plan and Summary: Cris Santos Company | Finance and Insurance | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (regional commercial bank), subsidiary of Cris Santos Company, Inc. |
| System assessed | Core and Online Banking Platform (COBP), per the SSP (P02), plus the program-level controls it inherits from the bank |
| Tier / Vertical | Mid-Market / Finance and Insurance |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced IT audit firm (engagement lead and 2 IT auditors) under the Chief Audit Executive, reporting to the Board Audit Committee. The firm does not design or operate any assessed control. The ISO coordinated access but did not select samples or rate findings. The ISO's team operates vulnerability scanning and MSSP triage, so those controls (RA-5, SI-4) were assessed by the firm alone |
| Assessment window | 2026-08-03 to 2026-08-21 (walkthroughs of the headquarters campus, the Georgia regional office, and branches FL-07 and GA-03 on 2026-08-10 to 2026-08-12) |
| Also satisfies | Testing of key controls under the Interagency Guidelines, 12 CFR 30 App. B III.C.3 (N52-R02), and input to the annual board report (III.F) |
| Results accepted | Chief Operating Officer, 2026-09-18; presented to the Board Audit Committee on 2026-09-17 |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **35 controls, 244 determination statements.** Controls were selected because they:
- address the High risks in the risk register (P01);
- cover Guidelines, Part 53, and Red Flags provisions with High or Moderate gaps in the gap analysis (P03);
- support reliance on inherited controls and the SOC 2 readiness of correspondent services (P09).

| Control | Why selected (risk ID or requirement) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Core role design and deprovisioning; III.C.1.a; R-006, R-039, R-040 | Focused | Focused (samples of 25 and 30) |
| AC-5, CM-3 | Payments hub configuration by one administrator; III.C.1.d, III.C.1.e; R-027, R-047 (High) | Comprehensive | Comprehensive (all 10 limit changes in the quarter) |
| AC-6, AC-6(5) | Privileged access to money-moving applications; R-007 (High) | Comprehensive | Comprehensive (all privileged accounts) |
| AC-17, MA-4 | Vendor standing VPN; R-048 | Focused | Focused (10 vendor sessions) |
| AT-2, AT-3 | Fraud training for contact-change and callback roles; III.C.2; 41.90(e)(3); R-001, R-028 | Focused | Focused |
| AU-6, AU-11, SI-4 | Payments events not monitored; III.C.1.f; R-013 | Focused | Focused |
| CM-6, CM-8 | Configuration and inventory; gap 11 | Basic | Focused (10 servers; 20 components) |
| CP-2, CP-4, CP-9, CP-10 | Payments hub recovery; III.C.1.h; R-004 (High) | Comprehensive | Comprehensive |
| IA-2(1), IA-5 | Administrator MFA and authenticators; R-049 | Focused | Focused (25 of 41 privileged accounts) |
| IA-8, IA-12 | Customer authentication and contact-change verification; II.B.3; 41.90(d)(2); R-001, R-002 (High) | Focused | Focused (40 contact changes) |
| IR-4, IR-6, IR-8 | Notification incident determination and notices; 53.3, 53.4, 225.302; R-008, R-009 | Focused | Basic |
| PM-9, RA-3 | Risk appetite and assessment; III.A.2, III.B; R-012 | Basic | Basic |
| RA-5, SI-2, SA-22 | Vulnerability and legacy servers; R-014, R-015 | Focused | Focused (50 critical findings) |
| SA-9, SR-6 | Third-party oversight; III.D; 53.4; R-010, R-011 | Focused | Focused (34 critical vendors) |
| SC-7, SI-3 | Segmentation and EDR (confirming strengths) | Basic | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; where risk is High and the population is small, the whole population was tested. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 142 | 25 | AC-2, PS-4 |
| Transfers | 88 | 25 | AC-2 |
| Teller and universal banker core users | about 180 | 30 | AC-2, AC-6 |
| New accounts in the identity provider | 160 | 25 | AC-2 |
| Privileged accounts (directory, identity provider, cloud) | 41 | 25 for MFA; all 41 for rights | IA-2(1), AC-6(5) |
| Core security and payments hub administrators | 11 | all 11 | AC-6, AC-6(5) |
| Payments hub limit changes (Q2 2026) | 10 | all 10 | AC-5, CM-3 |
| Infrastructure and application changes | about 400 | 20 | CM-3 |
| Business contact-information changes (Q2 2026) | about 1,100 | 40 | IA-12 |
| Vendor support sessions (July 2026) | 46 | 10 | MA-4 |
| Critical vulnerability findings (H1 2026) | 212 | 50 | RA-5, SI-2 |
| Servers for configuration scan | about 60 on premises | 10 | CM-6 |
| Incidents (last 12 months) | 31 | 10 | IR-4 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6, AT-2 |
| Critical vendors | 34 | all 34 (contracts); 8 Tier 1 SOC reviews | SA-9, SR-6 |

## 3. Methods and objects
- **Examine:**
  - policies (2024 set and the 2026 drafts) and the standards index
  - the SSP draft and the BIA
  - identity provider, core, payments hub, correspondent portal, and cloud exports
  - backup, patch, scan, EDR, and SIEM reports
  - contracts, SOC reports, and 53.4 contact letters
  - the incident register, BSA case extracts (without SAR content), and the 2025 tabletop report
  - the business continuity plan and the 2025 failover test report
  - board and committee minutes and the risk appetite statement
- **Interview:**
  - CRO, COO, CIO, ISO, and the 3 security analysts
  - IT Risk and Compliance Manager, Third-Party Risk Manager
  - Director of Payments Operations, Correspondent Services Director, Treasury Management Director, Retail Banking Director, Contact Center Director
  - HR Director and General Counsel
  - the MSSP service lead
  - 15 randomly selected staff
- **Test:**
  - MFA sign-in tests on sampled privileged accounts
  - self-approval of a wire and a single-administrator limit change in the payments hub test environment
  - a new beneficiary added with a relayed one-time code in the digital banking provider's test environment
  - a test call to the contact center requesting a phone number change using only public information (stopped before completion)
  - comparison of the correspondent portal account list with the access review population
  - a deletion attempt on a test backup by a production administrator
  - reachability test from a branch teller segment to the payments segment
  - EICAR test files on 5 endpoints and 2 servers
  - a simulated impossible-travel sign-in to test MSSP escalation
  - benchmark configuration scans of 10 servers

## 4. Rules of engagement
- No live wires, ACH files, or customer changes were created. Payments and online banking tests used the providers' test environments or bank test customers, with the Director of Payments Operations present.
- The contact center test call was pre-approved by the Contact Center Director and the COO, and stopped before any change was saved.
- No customer information or SAR content left bank systems. Screenshots were redacted; evidence is held in the firm's encrypted workpaper system under its confidentiality agreement.
- Stop-and-notify rule: any critical exposure is reported to the ISO and the CRO the same day. **Used once:** on 2026-08-12 the assessors reported 2 vendor-created generic administrator accounts in the correspondent portal that still used the vendor's default password pattern. The accounts were disabled on 2026-08-14, the risk was added to P01 as R-049, and a review of 18 months of portal logs found no use since 2025-05.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 160 |
| Other than satisfied | 84 |
| **Total** | **244** |

Other than satisfied statements by risk: 27 High, 49 Moderate, 8 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 18 | 8 | Moderate | POAM-001 |
| AC-5 | 1 | 1 | High | POAM-006 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-6(5) | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | Moderate | POAM-003 |
| AT-2 | 8 | 2 | Moderate | POAM-004 |
| AT-3 | 5 | 4 | Moderate | POAM-004 |
| AU-6 | 0 | 3 | High | POAM-005 |
| AU-11 | 0 | 1 | Moderate | POAM-005 |
| CM-3 | 5 | 5 | High | POAM-006 |
| CM-6 | 3 | 3 | Moderate | POAM-007 |
| CM-8 | 6 | 0 | n/a | n/a |
| CP-2 | 16 | 8 | High | POAM-008 |
| CP-4 | 1 | 4 | High | POAM-008 |
| CP-9 | 6 | 0 | n/a | n/a |
| CP-10 | 0 | 2 | High | POAM-008 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 6 | 4 | High | POAM-009 |
| IA-8 | 0 | 1 | High | POAM-010 |
| IA-12 | 3 | 2 | High | POAM-011 |
| IR-4 | 9 | 4 | Moderate | POAM-012 |
| IR-6 | 1 | 1 | High | POAM-012 |
| IR-8 | 10 | 7 | High | POAM-012 |
| MA-4 | 3 | 5 | Moderate | POAM-003 |
| PM-9 | 2 | 2 | Moderate | POAM-013 |
| PS-4 | 4 | 1 | Moderate | POAM-001 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 8 | 1 | Moderate | POAM-014 |
| SA-9 | 3 | 3 | Moderate | POAM-015 |
| SA-22 | 0 | 2 | Moderate | POAM-016 |
| SC-7 | 6 | 0 | n/a | n/a |
| SI-2 | 9 | 1 | Moderate | POAM-014 |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-4 | 8 | 4 | High | POAM-005 |
| SR-6 | 0 | 1 | Moderate | POAM-015 |

**Fully satisfied (6 controls):** CM-8, CP-9 (write-once backups; a production administrator could not delete a test backup), IA-2(1) (hardware-key MFA on all 25 sampled privileged sign-ins), RA-3, SC-7 (the teller segment could not reach the payments segment), and SI-3 (EDR quarantined every test file within 4 minutes). These confirm the strengths in the scenario facts.

**Fully other than satisfied (8 controls):** AC-6, AC-6(5), AU-6, AU-11, CP-10, IA-8, SA-22, and SR-6.

**Themes:**
1. **The money-moving applications sit outside the bank's strongest controls.** PAM, SIEM monitoring, and change control protect the directory and the cloud, but not the payments hub, the correspondent portal, or the core security module (AC-6(5), CM-3, AU-6, SI-4).
2. **Fraud defenses are strong at the wire and weak upstream.** Maker-checker and the callback field work; contact-information changes and relayable customer codes undo them (IA-12, IA-8, AT-3).
3. **Recovery of what the bank runs itself is unproven** (CP-2, CP-4, CP-10).
4. **Notices are incomplete** for the holding company and respondent institutions (IR-6, IR-8).

**New finding.** The 2 generic administrator accounts in the correspondent portal (IA-05e., IA-05i.) were not known before testing. They were disabled during fieldwork and added to P01 as R-049 (High).

**POA&M:** 29 controls had at least one Other than satisfied statement. They map to 16 POA&M items (POAM-001 to POAM-016), because related controls share an item. Five more items come from the gap analysis, the AI assessment, and the policy work (POAM-017 adverse action reasons, POAM-018 Red Flags program, POAM-019 correspondent agreements and SOC 2, POAM-020 AI portfolio, POAM-021 standards). The total is 21 items: 9 High, 11 Moderate, and 1 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-14 | Walkthroughs and technical tests |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the Board Audit Committee |
| 2026-09-18 | Results accepted by the COO |

Deliverables: this plan and summary; `assessment-results.csv` (244 rows); `poam.csv` (21 items).

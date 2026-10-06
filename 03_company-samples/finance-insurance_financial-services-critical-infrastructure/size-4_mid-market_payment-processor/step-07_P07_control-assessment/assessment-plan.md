# Security Assessment Plan and Summary: Cris Santos Company | Financial Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed payment processor serving merchants) |
| System assessed | Payment Processing Platform (PPP), per the SSP (P02): Cloud A, Cloud B, both colocation cages, and the connected-to systems |
| Tier / Vertical | Mid-Market / Financial Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 3 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control and is separate from the QSA firm. The Director of Information Security coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (cage walkthrough and technical tests 2026-08-10 to 2026-08-14) |
| Also satisfies | FTC Safeguards Rule testing of key controls, 16 CFR 314.4(d)(1); annual internal IT audit; readiness input to the combined 2026 PCI DSS ROC (fieldwork from 2026-11-09) |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **32 controls, 207 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01), especially the acquisition and settlement themes;
- cover the High gaps in the gap analysis (P03) that would likely be "not in place" at the ROC;
- test the controls the two P08 scenarios depend on (Cloud B access and monitoring, payment page integrity, settlement recovery);
- support inherited-control reliance and SOC 2 readiness (P09).

This is not a PCI DSS assessment. Only the QSA's ROC can conclude on PCI DSS compliance.

| Control | Why selected (risk ID or gap ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Account lifecycle across both clouds; P03 G-035, G-039; R-011 | Focused | Focused (samples of 25; all 61 Cloud B IAM users) |
| AC-6, AC-17, IA-2(1) | Privileged and remote access; R-001 (Very High), R-012, R-013 | Comprehensive | Comprehensive (all 136 privileged users listed; MFA tested on 35) |
| IA-5, IA-8 | Authenticators, default credentials, portal users; G-009, G-043; R-004, R-050 | Focused | Focused |
| AT-2 | Awareness training; G-080 | Basic | Focused (15 staff interviews) |
| AU-2, AU-5, AU-6, SI-4 | Logging and monitoring across platforms; G-055, G-058, G-068; R-003, R-036 | Focused | Comprehensive (every CDE account and cage) |
| CA-8, SC-7 | Penetration testing and segmentation; G-003, G-064, G-065; R-009 | Focused | Focused |
| CM-3, CM-6, CM-7, CM-8 | Change, configuration, functions, inventory and scope; G-008, G-032, G-077; R-016, R-035, R-050 | Focused | Focused |
| CP-4, CP-9, CP-10 | Recovery; P05 findings; R-006 to R-008 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability and bank notices; G-085, G-109; R-015 | Focused | Basic |
| PE-3 | Cage physical access; G-049 | Basic | Focused (30 visits) |
| RA-3, RA-5 | Risk assessment and vulnerability management; G-029, G-063; R-028 | Focused | Focused |
| SA-9, SA-22 | Service providers and unsupported components; G-082; R-010, R-014 | Focused | Comprehensive for service providers (34 of 34) |
| SC-12, SC-28 | Keys and stored account data; G-013, G-016 to G-018; R-017, R-018 | Focused | Focused |
| SI-7 | Payment page and funding file integrity; G-031, G-069; R-002, R-052 | Focused | Comprehensive (every script on both payment pages) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control that operates many times a year at moderate risk, 5 to 10 items for weekly or monthly controls, and the whole population when it is small or the risk is High. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 142 | 25 | AC-2, PS-4 |
| Transfers | 88 | 25 | AC-2 |
| Cloud B IAM users and access keys | 61 | 61 | AC-2, IA-5 |
| Privileged users (core and Cloud B) | 136 | All listed; MFA test on 25 core and 10 Cloud B | AC-6, IA-2(1) |
| Service accounts | 212 | 40 | AC-6 |
| Production changes (2026-04 to 2026-07) | 410 core, 96 Integrated Payments | 30 core, 15 Integrated Payments | CM-3 |
| Cage servers for configuration scan | 58 | 10 | CM-6 |
| Settlement servers and management interfaces | 12 | 12 | CM-7, IA-5 |
| Critical vulnerability findings on cage servers (Q1-Q2 2026) | 188 | 60 | RA-5 |
| Backup job days (July 2026, all platforms) | 30 | 30 | CP-9 |
| Service providers | 34 | 34 | SA-9 |
| Call recordings (June 2026) | about 41,000 | 60 | SC-28 |
| Pre-2025 support tickets | about 310,000 | 200 | SC-28 |
| Cage visits (2026-01 to 2026-06) | 410 | 30 | PE-3 |
| Incidents (2025-2026) | 46 | 10 | IR-4 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6, AT-2 |
| Payment page scripts (core page and hosted payment fields) | 22 | 22 | SI-7, CM-8 |

## 3. Methods and objects
- **Examine:** policies (the 2024 set and the 2026 set approved 2026-09-15); the SSP draft; identity provider, PAM, Cloud A, and Cloud B exports; posture reports; network rule exports; SIEM use cases and MSSP reports; scan, patch, and penetration test reports; key ceremony logs and the cryptographic architecture document; backup reports and DR test reports; contracts, AOCs, and responsibility matrices; the incident log; cage access logs; call recording and ticket samples.
- **Interview:** vCISO, CTO, Director of Information Security and team, VP Platform Engineering, Director of Integrated Payments Engineering, Director of Settlement and Treasury Operations, Chief Risk and Compliance Officer, HR Director, Contact Center Manager, the MSSP service lead, and 15 randomly selected staff.
- **Test:**
  - MFA sign-in tests on sampled privileged accounts; a test sign-in to a Cloud B console from an unmanaged network
  - a reachability test from the colocation management network to settlement systems
  - a port and credential test of the 12 settlement server management interfaces (vendor-approved, in a maintenance window)
  - a stopped EDR agent on a staging cage server (control failure alerting)
  - DNS queries to an assessor-owned domain from a Cloud A CDE subnet and a Cloud B gateway subnet
  - a simulated suspicious sign-in on a core administrator account (MSSP escalation)
  - an unauthorized change to a staging copy of the hosted payment fields (tamper-detection)
  - a restore of one token vault table into an isolated account
  - benchmark configuration scans of 10 cage servers and 5 Cloud B images

## 4. Rules of engagement
- No testing in production that could affect authorization, clearing, or funding. Payment page and agent tests ran in staging. Management interface tests ran in the 2026-08-12 maintenance window with the VP Platform Engineering present.
- No card data left the company's environments. Recording and ticket results were reported as counts and masked samples (BIN and last four).
- Stop-and-notify rule: any critical exposure is reported the same day to the Director of Information Security and the vCISO. **Used once:** on 2026-08-12 the assessors found vendor default credentials on the baseboard management interfaces of 6 of the 12 settlement servers, reachable from the colocation management network. The credentials were changed on 2026-08-14, and the company logged the finding as P01 R-050 the same day.
- The 3 call recordings containing card verification codes were referred to the Contact Center Manager and the Director of Information Security under POL-03 4.10, not handled by the assessors.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 143 |
| Other than satisfied | 64 |
| **Total** | **207** |

Other than satisfied statements by risk: 1 Very High, 30 High, 28 Moderate, 5 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 20 | 6 | High | POAM-004 |
| AC-6 | 0 | 1 | Very High | POAM-002 |
| AC-17 | 2 | 2 | High | POAM-002 |
| AT-2 | 8 | 2 | Low | POAM-019 |
| AU-2 | 4 | 2 | Moderate | POAM-003 |
| AU-5 | 0 | 2 | Moderate | POAM-003 |
| AU-6 | 2 | 1 | High | POAM-003 |
| CA-8 | 0 | 1 | High | POAM-008 |
| CM-3 | 8 | 2 | Moderate | POAM-010 |
| CM-6 | 3 | 3 | Moderate | POAM-007 |
| CM-7 | 5 | 1 | High | POAM-007 |
| CM-8 | 2 | 4 | High | POAM-009 |
| CP-4 | 3 | 2 | High | POAM-011 |
| CP-9 | 6 | 0 | n/a | n/a |
| CP-10 | 0 | 2 | High | POAM-011 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 6 | 4 | High | POAM-005, POAM-006, POAM-007 |
| IA-8 | 1 | 0 | n/a | n/a |
| IR-4 | 10 | 3 | High | POAM-003, POAM-017 |
| IR-6 | 1 | 1 | Moderate | POAM-017 |
| IR-8 | 13 | 4 | Moderate | POAM-017 |
| PE-3 | 11 | 1 | Low | POAM-018 |
| PS-4 | 3 | 2 | High | POAM-004 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 7 | 2 | Moderate | POAM-014 |
| SA-9 | 3 | 3 | Moderate | POAM-016 |
| SA-22 | 0 | 2 | High | POAM-015 |
| SC-7 | 4 | 2 | High | POAM-008 |
| SC-12 | 1 | 1 | Moderate | POAM-013 |
| SC-28 | 0 | 1 | High | POAM-012 |
| SI-4 | 9 | 3 | High | POAM-003 |
| SI-7 | 2 | 4 | High | POAM-001, POAM-020 |

**Fully satisfied (4 controls):** CP-9 (all 30 backup days succeeded and the isolated restore worked), IA-2(1) (MFA required on every sampled privileged account on both platforms), IA-8, and RA-3. These confirm the strengths listed in the scenario facts.

**Fully other than satisfied (6 controls):** AC-6, AU-5, CA-8, CP-10, SA-22, and SC-28.

**Themes:**
1. **Two platforms, two maturity levels.** On the core platform, monitoring, MFA, change control, and payment page integrity worked in every test (the DNS test alerted in 4 minutes). The same tests failed on the Integrated Payments gateway: the DNS query from Cloud B raised no alert, the staging change to the hosted payment fields went undetected, and the Cloud B console accepted a sign-in from an unmanaged network. Those three results are the attack path in the P08 gateway scenario.
2. **Settlement is protected by design but weak in operation.** Unsupported servers, default credentials on management interfaces, a segmentation route, and slow recovery all sit in the colocation cages (SA-22, CM-7, SC-7, CP-10).
3. **The program has not caught up with the acquisition.** Scope, inventory, access reviews, vendor oversight, and incident response all stop at the core platform (CM-8, AC-2, SA-9, IR-4).

**New finding:** default credentials on settlement server management interfaces (CM-7, IA-5). It was not known before testing. It was added to the risk register as R-050 and to POAM-007.

**POA&M:** 28 controls had at least one Other than satisfied statement. They map to 20 POA&M items (POAM-001 to POAM-020), because related controls share an item and SI-7 and IA-5 each feed more than one. Five more items come from the gap analysis and the AI assessment (POAM-021 AI governance, POAM-022 PAN retention, POAM-023 targeted risk analyses and quarterly reviews, POAM-024 Qualified Individual report, POAM-025 ISV responsibility matrix). The total is 25 items: 1 Very High, 12 High, 10 Moderate, and 2 Low. See `poam.csv`.

**Before the ROC.** Every Very High and High item that maps to a PCI DSS requirement is due by 2026-11-06, or has an interim measure due by then: compensating controls and a targeted risk analysis for the unsupported servers (POAM-015), purge of the affected recordings with daily supervisor checks (POAM-012), and the segmentation route removal (POAM-008). POAM-011 (recovery) and POAM-020 (funding file signing) are availability and integrity items that do not leave a PCI DSS requirement "not in place"; they are due 2027-03-31.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-14 | Cage walkthrough and technical tests (stop-and-notify on 2026-08-12) |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (207 rows); `poam.csv` (25 items). POA&M status is reviewed monthly by the Director of Information Security, in the quarterly reviews required by POL-01 4.7, and by the audit committee each quarter.

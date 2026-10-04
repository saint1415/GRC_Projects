# Security Assessment Plan and Summary: Cris Santos Company | Retail Trade | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional grocery retailer: 5 supermarkets, online ordering, a distribution center) |
| System assessed | E-commerce and Point-of-Sale Platform (EPP: SYS-01 to SYS-04 and SYS-06 to SYS-09), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Retail Trade |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control and is not the QSA firm. The Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (store walkthroughs 2026-08-10 to 2026-08-13; technical tests after store closing, 22:00 to 02:00) |
| Also satisfies | Annual independent evaluation (POL-01 4.11); readiness input for the QSA's PCI DSS assessment in October and November 2026 |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **36 controls, 256 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the PCI DSS requirement groups with the largest gaps in P03 (Requirements 6.4.3, 8, 10, 11.6.1, 12.8) before the QSA arrives;
- support the inherited-control reliance and SOC 2 readiness of the supplier offers service (P09).

| Control | Why selected (risk ID or requirement) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Store account lifecycle; PCI DSS 8.2; R-035 | Focused | Focused (samples of 25) |
| AC-6, AC-6(5), IA-5 | Privileged and shared credentials; R-007, R-009 | Comprehensive | Comprehensive (all 41 privileged accounts) |
| AC-17, MA-4 | Vendor remote access into the CDE; PCI DSS 8.4; R-006 (High) | Comprehensive | Focused (10 vendor sessions) |
| IA-2, IA-2(1) | Unique IDs and MFA; PCI DSS 8.2, 8.4 | Focused | Focused (25 privileged accounts) |
| AT-2 | Store staff awareness; PCI DSS 12.6 | Basic | Focused (30 store staff) |
| AU-2, AU-6, AU-11, AU-12 | CDE logging; PCI DSS 10; R-012 | Focused | Focused |
| CA-3 | Loyalty data exchanges; FTC; R-023, R-024 | Focused | Comprehensive (all 7 external exchanges) |
| CM-3, SI-7 | Checkout page change and integrity; PCI DSS 6.4.3, 11.6.1; R-002 (High) | Comprehensive | Comprehensive (all 23 scripts; 20 of 64 publishes) |
| CM-6, CM-7, CM-8 | Store CDE configuration and inventory; PCI DSS 2.2, 9.5, 12.5 | Focused | Focused (5 of 5 store servers, 10 registers, 65 of 65 PIN pads) |
| CP-2, CP-4, CP-9, CP-10 | Recovery; R-001 (Very High), R-014, R-015 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability; PCI DSS 12.10; R-042 | Focused | Basic |
| MP-6 | Disposal of card data; PCI DSS 9.4; Fla. Stat. 501.171(8) | Basic | Focused (5 of 5 stores) |
| RA-3, RA-5, SI-2 | Risk assessment and vulnerability management; PCI DSS 6.3, 11.3; R-033 | Focused | Focused (12 of 12 critical patches) |
| SA-9, SR-6 | TPSP oversight; PCI DSS 12.8; R-011 | Focused | Comprehensive (14 of 14 TPSPs) |
| SC-7 | Segmentation; PCI DSS 1.3, 1.4; R-008 | Focused | Focused (Stores 2 and 5, DC) |
| SI-3, SI-4 | Anti-malware and monitoring; PCI DSS 5, 10.7; R-003, R-005 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 268 | 25 | AC-2, PS-4 |
| Transfers | 85 | 25 | AC-2 |
| New accounts (identity provider and POS) | 410 | 25 | AC-2 |
| Privileged accounts (all admin planes) | 41 | 25 for MFA test; all 41 for rights review | IA-2(1), AC-6, AC-6(5) |
| Vendor remote sessions (Q2 2026) | 96 | 10 | MA-4 |
| Checkout page publishes (Q2 2026) | 64 | 20 | CM-3 |
| Checkout scripts | 23 | 23 | SI-7 |
| PIN pads | 65 | 65 (reconciliation) | CM-8 |
| Store servers / registers | 5 / 65 | 5 / 10 (benchmark scan) | CM-6, CM-7, AU-12 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| TPSPs | 14 | 14 | SA-9, SR-6 |
| Incidents (2025-2026) | 41 | 12 | IR-4 |
| Critical POS patches (last 12 months) | 12 | 12 | RA-5, SI-2 |
| Store staff training records | 480 | 30 | AT-2 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6, AT-2 |
| Sites for walkthroughs | 6 | 5 stores and the DC | MP-6, SC-7, CM-8 |

## 3. Methods and objects
- **Examine:**
  - policies (the 2024 set and drafts of the 2026 set) and the SSP draft
  - identity provider, POS, e-commerce, merchant portal, directory, and cloud exports
  - backup, patch, scan, ASV, and EDR reports
  - the TPSP list, AOCs, contracts, and the agency and supplier pilot terms
  - the incident queue, the 2024 plan, and the 2025 tabletop report
  - PIN pad lists, inspection logs, and destruction certificates
- **Interview:**
  - vCISO, IT Director, Security Manager, and both analysts
  - Chief Financial Officer, General Counsel, and the Privacy and Compliance Manager
  - Director of E-commerce and Marketing, Director of Store Operations, Distribution Center Director
  - 5 Store Managers and the MSSP service lead
  - 15 randomly selected staff (6 store, 3 customer service, 6 support center)
- **Test:**
  - MFA sign-in tests on sampled privileged accounts
  - benchmark configuration scans of 5 store servers and 10 registers
  - reachability tests from the corporate VLAN at Stores 2 and 5
  - an external scan of store public addresses
  - EICAR test files on 5 endpoints and 1 store server
  - a simulated impossible-travel sign-in to test MSSP escalation
  - a test change to the website checkout page to confirm tamper alerting
  - browser captures of the website and app checkouts
  - a restore of one file-share folder from the backup account

## 4. Rules of engagement
- No testing during store hours. Store tests ran between 22:00 and 02:00 with the Store Manager present. No live card data was used; the test checkout change used a staging copy approved by the Director of E-commerce and Marketing and was reverted within 10 minutes.
- No card data or customer data left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system.
- Stop-and-notify rule: any critical exposure is reported to the IT Director and the vCISO the same day. **Used once:** on 2026-08-12 the external scan found an open remote management port on a public address at Store 4. On 2026-08-13 the walkthrough traced it to a cellular modem the POS vendor had installed in 2024 for failover support, still on its default password. The IT Director disconnected the modem that day. The company logged the finding as P01 R-050 on 2026-08-14 and told the QSA firm.
- The catering forms found with card numbers and security codes were secured by the Director of Fresh Departments, not handled by the assessors, and destroyed under supervision by 2026-09-20 (POAM-019).

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 143 |
| Other than satisfied | 113 |
| **Total** | **256** |

Other than satisfied statements by risk: 62 High, 45 Moderate, 6 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 16 | 10 | High | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-003 |
| AC-6(5) | 0 | 1 | High | POAM-003 |
| AC-17 | 2 | 2 | High | POAM-002 |
| AT-2 | 7 | 3 | Moderate | POAM-004 |
| AU-2 | 1 | 5 | High | POAM-005 |
| AU-6 | 1 | 2 | High | POAM-005 |
| AU-11 | 0 | 1 | Moderate | POAM-005 |
| AU-12 | 1 | 2 | High | POAM-005 |
| CA-3 | 2 | 6 | High | POAM-018 |
| CM-3 | 5 | 5 | High | POAM-013 |
| CM-6 | 2 | 4 | Moderate | POAM-006 |
| CM-7 | 4 | 2 | High | POAM-020 |
| CM-8 | 2 | 4 | High | POAM-007 |
| CP-2 | 15 | 9 | High | POAM-008 |
| CP-4 | 3 | 2 | High | POAM-008 |
| CP-9 | 4 | 2 | High | POAM-009 |
| CP-10 | 0 | 2 | High | POAM-008 |
| IA-2 | 1 | 1 | High | POAM-017 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 5 | 5 | High | POAM-003 |
| IR-4 | 9 | 4 | Moderate | POAM-010 |
| IR-6 | 1 | 1 | Moderate | POAM-010 |
| IR-8 | 11 | 6 | Moderate | POAM-010 |
| MA-4 | 1 | 7 | High | POAM-002 |
| MP-6 | 2 | 2 | High | POAM-019 |
| PS-4 | 2 | 3 | High | POAM-001 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 6 | 3 | High | POAM-011 |
| SA-9 | 1 | 5 | High | POAM-012 |
| SC-7 | 3 | 3 | High | POAM-014; POAM-020 |
| SI-2 | 8 | 2 | Moderate | POAM-011 |
| SI-3 | 7 | 1 | Moderate | POAM-015 |
| SI-4 | 8 | 4 | High | POAM-016 |
| SI-7 | 4 | 2 | High | POAM-013 |
| SR-6 | 0 | 1 | High | POAM-012 |

The Risk column shows the highest risk among the control's Other than satisfied statements.

**Fully satisfied (2 controls):** IA-2(1) (MFA on 25 of 25 sampled privileged identity provider accounts) and RA-3 (the July 2026 SP 800-30 assessment). Strong individual results also confirm the strengths in the scenario facts: cloud backups ran on 30 of 30 days and restored correctly (CP-9a, CP-9d), EDR quarantined every test file within 4 minutes (SI-3), the POS VLANs could not be reached from the corporate VLAN (SC-7), and the MSSP escalated a simulated sign-in within 22 minutes (AU-6).

**Fully other than satisfied (5 controls):** AC-6, AC-6(5), AU-11, CP-10, and SR-6.

**Themes:**
1. **The store CDE is a blind spot.** It is segmented well from the corporate network, but its logs are not collected (AU-2, AU-12), vendor access to it is shared and unmonitored (AC-17, MA-4, IA-2), and an unmanaged vendor modem bypassed the firewall entirely (CM-7, SC-7).
2. **The checkout page belongs to marketing, not to change control** (CM-3, SI-7). The website is monitored, but scripts carry no integrity values and the app checkout is not watched.
3. **Recovery is proven for stores, not for the cloud** (CP-2, CP-4, CP-10). Offline mode works; the cloud workloads behind pricing, loyalty, and the POS head office have never been restored.
4. **Data leaves through partners without terms** (CA-3, SA-9).

**POA&M:** 34 controls had at least one Other than satisfied statement. They map to 20 POA&M items (POAM-001 to POAM-020), because related controls share an item. Four more items come from the gap analysis and the AI assessment (POAM-021 PCI scope document, POAM-022 privacy notice and claims, POAM-023 AI governance, POAM-024 P2PE migration). The total is 24 items: 19 High and 5 Moderate. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Store walkthroughs and technical tests (after store hours) |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee |
| 2026-10-19 | Results shared with the QSA firm at the start of its fieldwork |

Deliverables: this plan and summary; `assessment-results.csv` (256 rows); `poam.csv` (24 items).

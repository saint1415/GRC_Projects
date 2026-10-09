# Security Assessment Plan and Summary: Cris Santos Company | Arts, Entertainment, and Recreation | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (live event venue operator with ticketing; private equity-backed; three Florida venues) |
| System assessed | Ticketing and Venue Operations Platform (TVOP), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Arts, Entertainment, and Recreation |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 2 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control, and it is not the QSA, the ASV, the penetration tester, or the MSSP. The Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (site walkthroughs 2026-08-11 to 2026-08-13; technical tests on dark days and after hours) |
| Also supports | Readiness evidence for the 2026 PCI DSS ROC (N71-R04) and FTC reasonable security (N71-R05); the annual internal IT audit; SOC 2 readiness for the County PAC (P09) |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 238 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the High rows of the gap analysis (P03) that the QSA will test in November;
- underpin the two P08 scenarios (payment page skimming with a patron export, and an event-day outage);
- support inherited-control reliance and SOC 2 readiness (P09).

| Control | Why selected (risk ID or requirement) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Local and agency accounts; PCI 8.2, 7.2; R-002, R-035 | Focused | Focused (samples of 25; all 186 ticketing users) |
| AC-6, AC-6(5) | Privileged access and the API key; PCI 7.2, 8.6; R-003, R-036 | Comprehensive | Comprehensive (all administrator lists) |
| AC-17 | Integrator remote access; PCI 8.4.3; R-038 | Focused | Focused |
| IA-2, IA-2(1), IA-5 | Unique IDs, MFA, authenticators; PCI 8.2 to 8.6; R-002, R-029 | Focused | Focused (25 privileged accounts; 12 integrator devices) |
| AT-2 | Training; PCI 12.6; R-007 | Basic | Focused |
| AU-2, AU-6, AU-11, AU-12 | Log sources and review; PCI 10.2, 10.4, 10.5; R-034 | Focused | Focused |
| CA-8 | Penetration testing; PCI 11.4 | Basic | Basic |
| CM-2, CM-6 | Baselines and defaults; PCI 2.2; R-029 | Focused | Focused |
| CM-3 | Change control for payment settings; PCI 6.5 | Focused | Focused (samples of 25) |
| CM-7, SI-7 | Payment page scripts and tamper detection; PCI 6.4.3, 11.6.1; R-001 (Very High) | Comprehensive | Comprehensive (all 31 scripts; 10 pages) |
| CM-8 | Inventory and P2PE devices; PCI 9.5, 12.5.1; R-041 | Focused | Comprehensive (all 302 P2PE devices) |
| CP-2, CP-4, CP-9 | Event-day continuity and recovery; R-018 (High), R-022 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability; PCI 12.10; R-042 | Focused | Basic |
| MP-6, PE-3 | Media and physical access; PCI 9.2 to 9.4 | Basic | Focused (all 4 sites) |
| RA-5 | Vulnerability scanning; PCI 11.3, 6.3 | Focused | Focused |
| SA-9, SR-6 | Service providers; PCI 12.8; R-037 | Focused | Focused (12 providers) |
| SC-7 | Segmentation; PCI 1.3, 1.4; R-004, R-028 | Focused | Focused |
| SI-3, SI-4 | EDR and monitoring; PCI 5.2, 10.4, 11.5 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items; for small populations, all items. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Ticketing venue users | 186 | 186 (all) | AC-2, IA-2 |
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 51 | 25 | AC-2 |
| New accounts (identity provider) | 143 | 25 | AC-2 |
| Federated privileged accounts | 38 | 25 (MFA test); all 38 for rights review | IA-2(1), AC-6 |
| Integrator-installed devices (CCTV, door access, crowd analytics) | 12 servers and controllers | 12 (default-credential test) | IA-5, CM-6 |
| Scripts on pages that embed the payment form | 31 | 31 (all) | CM-7, SI-7 |
| Ticketing setting changes / infrastructure changes (Jan-Jun 2026) | 214 / 61 | 25 / 25 | CM-3 |
| P2PE devices (POS and box office) | 302 | 302 (reconciliation) | CM-8 |
| Laptops and PCs | 520 | 20 (configuration); 5 (EDR test) | SI-3, CM-6 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Service providers with card or patron data | 12 | 12 | SA-9, SR-6 |
| Incidents (2025-2026) | 41 | 10 | IR-4 |
| Critical vulnerability findings (Jan-Jun 2026) | 18 | 18 | RA-5 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6, AT-2 |
| Sites for walkthroughs | 4 | 4 (HQ, Amphitheater, Music Hall, Club) | PE-3, SC-7, CM-8 |

## 3. Methods and objects
- **Examine:**
  - policies (the 2024 set and drafts of the 2026 set) and the standards index
  - the SSP draft, the BIA, and the 2024 IT continuity plan
  - identity provider, ticketing, tag manager, CMS, cloud, and firewall exports
  - backup, patch, scan, and EDR reports; ASV reports
  - vendor contracts, AOCs, and SOC 2 reports
  - the incident queue and the 2024 incident response plan
- **Interview:**
  - vCISO, Security Manager, IT Director, GRC Analyst, and both security analysts
  - CFO, General Counsel, Controller, and HR Director
  - Vice President of Ticketing, Vice President of Marketing and Digital, Director of Premium Seating and Group Sales
  - Vice President of Venue Operations, Director of Safety and Security, the three venue General Managers
  - the MSSP service lead, the integrator's lead technician, and 15 randomly selected staff
- **Test:**
  - MFA sign-in tests on 25 sampled privileged accounts and on the 2 local ticketing admin accounts
  - default-credential tests on 12 integrator-installed devices (after hours, integrator present)
  - browser capture of 10 event pages on 2026-08-11, compared with the P03 capture of 2026-07-20
  - traffic tests from a virtual terminal laptop and a corporate laptop at HQ and the Music Hall
  - EICAR test files on 5 endpoints
  - a simulated impossible-travel sign-in to test MSSP escalation
  - a restore of one CMS folder from the backup account
  - a query of the ticketing audit log for bulk exports in July 2026

### What each test could show
The 2026 policies and standards (P06) and the P08 runbooks were drafts during fieldwork; they were approved on 2026-09-15 and take effect on 2026-10-01. The 2024 policies, standards, incident response plan and IT continuity plan were in force, so controls built on them were tested for operation. A requirement that only a draft introduces has not operated yet, so the drafts were reviewed for design only. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control was in place before fieldwork and was tested on samples, live systems or the documents in force | 186 |
| Design | The requirement comes from a 2026 draft (the quarterly access review in POL-02; 12-month log retention in POL-03 and STD-02; card compromise, event-day, reportable incident and external sharing coverage in the P08 runbooks); its design was reviewed. Operation is tested at the 2027-03 follow-up | 5 |
| Not implemented | Nothing existed to test | 47 |
| **Total** | | **238** |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-AC-2 and so on). Each sample population in section 2 comes from an intake export or a gap analysis capture: ticketing venue users from the ticketing user export (EV-006), terminations and transfers from the HR report (EV-003), new accounts from the identity provider export (EV-001), privileged accounts from EV-009, integrator-installed devices from the integrator list (EV-017), payment page scripts from the P03 capture (EV-068), ticketing setting changes from the settings history (EV-007) and infrastructure changes from the change records (EV-023), P2PE devices from the device lists (EV-019), laptops and PCs from the endpoint console (EV-013), service providers from the vendor files (EV-043), incidents from the incident queue (EV-033), and critical findings from the scan reports (EV-020).

## 4. Rules of engagement
- No testing during an on-sale or during doors. Network and device tests ran on dark days or after hours, with the Vice President of Venue Operations' approval.
- No card data was entered, copied, or photographed. CRM notes with card numbers were reviewed with numbers masked and reported to the Security Manager under POL-03 4.10.
- Stop-and-notify rule: any critical exposure is reported to the Security Manager and the vCISO the same day. **Used once:** on 2026-08-12 the assessors found the integrator's **default administrator password on the Music Hall crowd analytics server**, reachable from the corporate segment. The password was changed on 2026-08-14 and the company logged the finding as P01 R-029 the same day.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 125 |
| Other than satisfied | 113 |
| **Total** | **238** |

Other than satisfied statements by risk: 58 High, 47 Moderate, 8 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 13 | 13 | High | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-6(5) | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | Moderate | POAM-005 |
| AT-2 | 6 | 4 | Low | POAM-006 |
| AU-2 | 1 | 5 | High | POAM-007 |
| AU-6 | 1 | 2 | High | POAM-008 |
| AU-11 | 0 | 1 | Moderate | POAM-009 |
| AU-12 | 2 | 1 | High | POAM-007 |
| CA-8 | 0 | 1 | Moderate | POAM-020 |
| CM-2 | 2 | 3 | Moderate | POAM-012 |
| CM-3 | 6 | 4 | Moderate | POAM-011 |
| CM-6 | 4 | 2 | Moderate | POAM-012 |
| CM-7 | 3 | 3 | High | POAM-010 |
| CM-8 | 2 | 4 | Moderate | POAM-013 |
| CP-2 | 11 | 13 | High | POAM-014 |
| CP-4 | 0 | 5 | Moderate | POAM-015 |
| CP-9 | 6 | 0 | n/a | n/a |
| IA-2 | 1 | 1 | High | POAM-003 |
| IA-2(1) | 0 | 1 | High | POAM-003 |
| IA-5 | 5 | 5 | High | POAM-004 |
| IR-4 | 8 | 5 | Moderate | POAM-016 |
| IR-6 | 1 | 1 | Moderate | POAM-016 |
| IR-8 | 7 | 10 | Moderate | POAM-016 |
| MP-6 | 3 | 1 | Moderate | POAM-017 |
| PE-3 | 8 | 4 | Low | POAM-018 |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| RA-5 | 7 | 2 | Moderate | POAM-019 |
| SA-9 | 1 | 5 | High | POAM-021 |
| SC-7 | 4 | 2 | High | POAM-022 |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-4 | 8 | 4 | Moderate | POAM-023 |
| SI-7 | 2 | 4 | High | POAM-010 |
| SR-6 | 0 | 1 | High | POAM-021 |

**Fully satisfied (2 controls):** CP-9 (isolated, write-once backups; the test restore succeeded) and SI-3 (EDR quarantined every test file within 4 minutes and alerted the MSSP). These confirm what the intake evidence showed (EV-013, EV-026).

**Fully other than satisfied (7 controls):** AC-6, AC-6(5), AU-11, CA-8, CP-4, IA-2(1), and SR-6.

**Findings that change the picture:**
- **The payment page changed during the assessment.** The capture of 2026-08-11 showed 33 scripts on pages that embed the checkout form, 2 more than on 2026-07-20 (a sponsor campaign tag and a new chat widget loader). Nobody outside the marketing agency knew. This confirms that CM-7 and SI-7 are the controls that would catch the first P08 scenario, and neither works today. The 2 new scripts were removed on 2026-08-14.
- **MFA works where SSO reaches.** All 25 sampled federated administrators were prompted for MFA (IA-2(1) objective tested), but the 2 local ticketing admin accounts and the tag manager publishers signed in with passwords only. The control is rated Other than satisfied because the exceptions are exactly the accounts an attacker would use (P01 R-001, R-002).
- **New finding:** the integrator's default administrator password on the Music Hall crowd analytics server (IA-05e.). Added to the risk register as R-029 and to POAM-004.
- **Event-day continuity depends on one venue's practice.** The Amphitheater's manual entry procedure is solid; the Music Hall and the Club have none (CP-2), and the IT plan has never been tested (CP-4).

**Themes:**
1. The company can **protect and detect at the endpoint** (SI-3, CP-9, EDR escalation), but it **cannot see or control its own edge of the SaaS platforms**: local accounts, scripts, settings changes, and SaaS logs (AC-2, IA-2(1), CM-7, SI-7, AU-2, AU-6).
2. **Third parties are trusted without terms or monitoring** (SA-9, SR-6, AC-17).
3. **Recovery and event-day continuity are unproven** outside the Amphitheater (CP-2, CP-4).

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 23 POA&M items (POAM-001 to POAM-023), because related controls share an item. Four more items come from the gap analysis and the AI assessment (POAM-024 PCI scope and ROC readiness, POAM-025 card data purge, POAM-026 fee display and accessible seating rules, POAM-027 AI governance conditions). The total is 27 items: 13 High, 12 Moderate, and 2 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Site walkthroughs and technical tests |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (238 rows); `poam.csv` (27 items).

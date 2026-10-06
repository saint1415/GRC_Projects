# Security Assessment Plan and Summary: Cris Santos Company | Financial Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (merchant services provider, an ISO) |
| System assessed | Merchant Payments Platform (MPP), per the SSP (P02) |
| Tier / Vertical | Micro / Financial Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant with PCI DSS experience, under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Operations Manager; MSP lead technician on call |
| Assessment window | 2026-08-03 to 2026-08-05 (on site 2026-08-04) |
| Also satisfies | FTC Safeguards Rule testing of key controls, 16 CFR 314.4(d)(1); readiness input to the 2026 SAQ D for Service Providers (due 2026-10-30) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 102 determination statements.** Controls were chosen because they support the four High risks in P01 (console takeover, deposit change fraud, missed notices, PCI DSS validation), cover High gaps in P03, or test what the MSP and the processor partner do on the company's behalf.

This is not a PCI DSS assessment. The SAQ and AOC signed by the Owner are the company's formal PCI DSS validation.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Former agent's accounts active 5 months; excess console privilege (P01 R-006, R-002; P03 G-031, G-034) | Focused | Comprehensive (every account in the console, portal, CRM, suite, and phone system) |
| IA-2(1) | MFA on console and administrator access (P01 R-001; P03 G-039, G-090) | Focused | Comprehensive (every console account; phone and hosting administrators) |
| AT-2 | Phishing and deposit-change pretexting (P01 R-007; P03 G-073) | Basic | Focused (5 of 7 employees and 2 of 6 agents interviewed) |
| AU-6 | No log review (P01 R-001; P03 G-050) | Basic | Basic |
| CM-8 | Inventory, scope, and terminals (P03 G-046, G-070; P01 R-012) | Focused | Comprehensive (every spare terminal; every hosted payment page) |
| CP-9 | Backups never tested (P05 finding 3; P01 R-010) | Basic | Focused |
| IR-6, IR-8 | No incident response plan or contacts (P01 R-008; P03 G-078, G-101) | Focused | Basic |
| RA-5 | Vulnerability scanning (P03 G-057) | Basic | Basic |
| SA-9 | Service providers and the MSP (P01 R-011; P03 G-075) | Focused | Comprehensive (all 7 providers and the agent agreements) |
| SC-28 | Card data and merchant owner data at rest (P01 R-003, R-004, R-005; P03 G-010, G-011) | Focused | Focused (recording list, mailbox search, bucket count, 3 laptops) |
| SI-2 | MSP patching and the website plugin (P01 R-005; P03 G-026) | Focused | Focused (3 laptops including 1 spare; website plugin; firewall) |

## 2. Methods and objects
- **Examine:** user, role, and MFA exports from the console, portal, CRM, suite, and phone system; the employee and agent roster; the agent contract end record; the console audit log; the terminal spreadsheet; the hosted payment page content export for all 120 e-commerce merchants; the 2022 policy template and draft POL-03; the ISO agreement; the processor partner's AOC; vendor and agent agreements; ASV reports; the MSP evidence listed below.
- **Interview:** the Owner, the Operations Manager, the Merchant Support Lead, the Sales and Agent Manager, 5 of 7 employees (training and incident reporting), 2 outside agents, and the MSP lead technician.
- **Test:**
  - user lists compared against the roster in each system
  - sign-in attempts without a second factor to the console (test account), the phone administration page, and the hosting account (with the account holders present)
  - a physical count of spare terminals against the spreadsheet
  - a comparison of each hosted payment page's custom header content against the company's records (there were none, so every script found was a finding)
  - encryption status on 3 laptops and patch status on 3 laptops, including 1 spare
  - a harmless antivirus test file on 1 laptop
  - a search of support mailboxes for card numbers and Social Security numbers (results reported as counts only)

### MSP evidence requested
The MSP operates most laptop and network controls, so evidence came from it. Requested on 2026-07-27 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-07-31 |
| Antivirus console export (all laptops) | SI-3 (context for SI-2) | Yes, 2026-07-31 |
| Laptop encryption report | SC-28 | Yes, 2026-07-31 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-03 |
| Record of any restore test | CP-9 | No record exists (confirmed by the MSP) |
| Firewall rule export and firmware record | SI-2; context for P03 Requirement 1 | Yes, 2026-07-31 |
| Technician list with access to the company, and MFA on the remote management tool | SA-9 | Not received by fieldwork end; follow-up in POAM-011 |

## 3. Rules of engagement
- No testing that could disrupt merchants. Console tests used a test account the processor partner created for the assessment; no merchant setting was changed.
- No card data or merchant owner data left the company. Mailbox and recording results were reported as counts and masked samples (last four digits only).
- The assessor would stop and tell the Operations Manager and Owner at once about any critical exposure. **This rule was used once:** the unapproved scripts on 2 merchants' hosted payment pages were reported on 2026-08-04. The Technician confirmed they were analytics tags the merchants had asked for in 2025, and they were removed with the merchants' agreement on 2026-08-12.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 22 |
| Other than satisfied | 80 |
| **Total** | **102** |

**Fully other than satisfied:** IA-2(1), AU-6, IR-6, SA-9, and SC-28. No process or technology met the objective.
**Strongest:** RA-5 (5 of 9 satisfied: the ASV process works; internal scanning does not exist), then SI-2 (4 of 10: the MSP identifies, reports, and screens patches; time limits, spare laptops, and the website are the gaps) and PS-4 (2 of 5: property is returned; access removal is not timed).
**Weakest by count:** AC-2 (22 of 26 other than satisfied) and IR-8 (15 of 17): there was no account procedure and no incident response plan at fieldwork.

**New findings from testing:**
1. Third-party analytics scripts on 2 merchants' hosted payment pages, in no record and never approved (CM-08a.05). Added to the risk register as R-022 and to POAM-006.
2. The spare terminal count was 41 against 44 on the spreadsheet. The 3 missing units were traced to 2025 swaps shipped without an update (CM-08a.01). POAM-006.
3. The 2 spare laptops had not been patched since March 2026 because they were powered off (SI-02a.[03]). POAM-013.
4. 212 emails in support and onboarding mailboxes carry merchant owner Social Security numbers in attachments (SC-28). POAM-012.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`: 6 High and 7 Moderate. The High items are POAM-001, POAM-002, POAM-005, POAM-009, POAM-011, and POAM-012: console access, monitoring, incident response, service providers, and data at rest, the same themes as the High risks in P01.

## 5. Deliverables
`assessment-results.csv` (102 rows), `poam.csv` (13 items), and this plan and summary. The Owner accepted the results on 2026-08-31. POA&M status is reviewed monthly by the Operations Manager and at the quarterly PCI review (POL-02 A.5).

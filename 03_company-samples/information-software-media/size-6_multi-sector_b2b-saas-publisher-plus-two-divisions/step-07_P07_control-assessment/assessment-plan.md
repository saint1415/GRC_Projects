# Security Assessment Plan and Summary: Cris Santos Company Holdings | Information | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the Workforce Cloud Platform (P02 SSP system), and samples of Technology Consulting and Payments and Payroll controls |
| Tier / Vertical | Multi-Sector / Information (focus division: Cloud Software) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only. The SOC 2 service auditor and the PCI QSA were not involved and did not rely on this work |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also satisfies | Testing of key controls under 16 CFR 314.4(d)(1) for Payments and Payroll; evaluation under 45 CFR 164.308(a)(8) for consulting's business associate work; SOC 2 CC4.1 monitoring evidence for Workforce Cloud |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the termination sample took leavers from all three, including the acquired firm).
2. **The Workforce Cloud Platform's** system-specific and hybrid controls were assessed because it is the SSP system and carries the top group risk (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Technology Consulting was sampled on access, endpoint, and governance controls because of the acquired firm's separate stack (gap 9) and undocumented inheritance (gap 10). Payments and Payroll was sampled on service provider oversight and PCI DSS scope controls (gaps 5 and 6).

## 2. Controls selected
**40 control assessments** (38 distinct controls; AC-2 and SA-9 were assessed in two scopes), **274 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-5 | 42 | Every division's access; GR-01 (static keys) | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-4, IR-6, IR-8, RA-5 | 53 | GR-01, GR-03; scenario gap 7 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-12, SC-28, SC-28(1), CM-6 | 23 | GR-01, GR-02; keys, backups, guardrails | Focused / Focused |
| Workforce Cloud Platform (SSP system) | AC-3, AC-4, AC-6, SC-4, AU-12, SI-12, CM-4, RA-8, SA-11, PT-3, SA-9, CP-4 | 43 | SW-001, SW-002, SW-003, SW-006 (High); gaps 2, 3, 4 | Comprehensive / Comprehensive |
| Division sample: Technology Consulting | AC-2, SI-3, AC-17, MP-6, CA-2 | 53 | IC-001, IC-004, IC-005; gaps 3, 9, 10, 11 | Focused / Focused (20 acquired-firm laptops; 50 partner roles) |
| Division sample: Payments and Payroll | SA-9, CA-8, RA-3, CM-8, CP-2 | 45 | PY-001, PY-002, PY-011; gaps 5 and 6 | Focused / Focused (5 checkout pages) |
| **Total** | **40** | **274** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, cloud key reports, SIEM data sources and rules, landing-zone guardrails, bucket policies and lifecycle rules, logging settings, design review records, privacy impact assessments, contingency plans and test reports, vendor and intercompany files, segmentation test reports, payment page script inventories.
- **Interview:** group identity, SOC, and cloud platform directors; the WCP system owner and integrations director; the Group General Counsel; the consulting security and compliance lead; the Payments and Payroll Qualified Individual and payroll operations director.
- **Test:**
  - a termination sample of 60 leavers across divisions (10 from the acquired firm) and 25 expired contractor accounts;
  - a simulated bulk read of 2,000 synthetic handoff files from the export bucket (with SOC approval) to test detection;
  - creation of a static key and a public bucket in a test account to test guardrails;
  - cross-tenant access attempts in 4 test tenants;
  - a permission test of the workforce assistant in a test tenant seeded with HR case notes;
  - 50 implementation-partner roles checked against project end dates;
  - restores of 2 WCP tenant databases and 1 payroll engine dataset from the provider B vault;
  - a browser capture of all 5 hosted checkout pages to compare loaded scripts with the inventory.

## 4. Rules of engagement
- No testing that could affect customers, payroll runs, or payment authorization. Tests ran in test tenants and test accounts; the bulk-read test used synthetic files.
- No real Social Security numbers, bank details, or cardholder data left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. One item was escalated the same day: 2 toolkit keys found in personal repositories (revoked within 1 hour under POL-03 4.9).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls (four scopes) | 115 | 18 | 133 |
| Workforce Cloud Platform | 26 | 17 | 43 |
| Division sample: Technology Consulting | 40 | 13 | 53 |
| Division sample: Payments and Payroll | 33 | 12 | 45 |
| **Total** | **214** | **60** | **274** |

**Common controls are strong, with one blind spot.** 115 of 133 common statements were satisfied. Privileged access (AC-6(5), IA-2(1)), inactivity disabling (AC-2(3)), training (AT-2), vulnerability management (RA-5), backups (CP-9), boundary protection (SC-7), and key management (SC-12, SC-28) had no findings. The common findings are about **machine credentials** (IA-5, AC-2, and the CM-6 guardrail that is documented but not enforced), **detection at the export bucket** (SI-4), **cross-division incident consistency and notification** (IR-4, IR-6, IR-8; gap 7), the export bucket's provider-managed keys (SC-28(1)), and acquired-firm terminations (PS-4).

**The WCP is where the top risk is.** AC-3, AC-4, and AC-6 were fully other than satisfied (each has one determination statement): the export bucket can be read by principals far beyond the single intended recipient, and 31 of 50 sampled partner roles belonged to consultants whose projects had closed. Tenant isolation (SC-4) passed every cross-tenant test. The AI findings (CM-4, RA-8, SA-11, PT-3) confirm gap 4; the permission test surfaced HR case-note text to a non-HR manager in a test tenant, which the product team fixed in a hotfix design due 2026-11-15.

**Division samples:**
- *Technology Consulting:* partner roles and acquired-firm accounts outside the group lifecycle (AC-2, 6 statements), no central malware alerts or periodic scans on acquired-firm laptops (SI-3), an unauthorized VPN path (AC-17), missing 2025 sanitization certificates (MP-6), and an assessment plan that cannot separate inherited from division controls (CA-2, gap 10).
- *Payments and Payroll:* no oversight of the WCP as a service provider (SA-9, 4 statements), the missed segmentation test (CA-8, fully other than satisfied), a risk assessment that skipped affiliate-held data (RA-3), an incomplete payment page script inventory (CM-8), and a contingency plan that assumes the WCP is up (CP-2).

**Controls fully other than satisfied** (every statement failed): AC-3, AC-4, and AC-6 (WCP) and CA-8 (Payments and Payroll). Each has only one determination statement.

30 of the 40 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **28 items**: 24 from this assessment and 4 from the P03 gap analyses and P10 (POAM-025 to POAM-028). By risk: 8 High (POAM-001 static keys, POAM-003 detection, POAM-006 handoff channel, POAM-007 retention, POAM-015 partner and acquired-firm access, POAM-020 affiliate oversight, POAM-023 checkout scripts, POAM-027 attrition-risk bias testing), 19 Moderate, and 1 Low. Status: 23 In progress, 5 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (274 rows, with an `assessment_scope` column), `poam.csv` (28 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-17. Division presidents accepted their division findings the same week. New findings were added to the risk registers (P01): the HR case-note leakage (SW-028) and the 2025 handoff delay that was never corrected (SW-014).

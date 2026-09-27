# Security Assessment Plan and Summary: Cris Santos Company | Financial Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (payment processor serving merchants) |
| System assessed | Payment Processing Platform (PPP), per the SSP (P02) |
| Tier / Vertical | Small / Financial Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor, separate from the QSA firm. Not involved in operating or designing the controls. Escorted by the IT Manager |
| Assessment window | 2026-08-03 to 2026-08-07 |
| Also satisfies | FTC Safeguards Rule testing of key controls, 16 CFR 314.4(d)(1); readiness input to the 2026 PCI DSS ROC (2026-11-02) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **21 controls, 130 determination statements.** Controls were chosen for three reasons:
- they support the five High risks in P01;
- they cover the High gaps in P03 that would likely be "not in place" at the ROC;
- they test the controls the P08 scenario depends on (repository access, payment page integrity, monitoring, incident response).

This is not a PCI DSS assessment. Only the QSA's ROC can conclude on PCI DSS compliance.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6 | Terminations and reviews (P03 G-031, G-034); R-002, R-010, R-011 | Focused | Focused |
| IA-2, IA-2(1), IA-5, IA-8 | Workforce and merchant user authentication (P03 G-038, G-088); R-004, R-030 | Focused | Focused |
| CM-3, CM-8 | Change control and scope after the migration (P03 G-029, G-070, G-071); R-002, R-014 | Focused | Focused |
| SI-7 | Payment page integrity (P03 G-028, G-063); R-001 | Focused | Comprehensive (every payment page script) |
| SI-4, AU-5, AU-6 | Monitoring, egress detection, and control failures (P03 G-050, G-053, G-062); R-003, R-013 | Focused | Focused |
| CA-8, SC-7 | Segmentation and boundary (P03 G-058, G-059); R-012 | Focused | Focused |
| SC-12, SC-28 | Keys and PAN at rest (P03 G-013, G-014); R-005, R-017 | Focused | Comprehensive (PAN discovery across the warehouse and a ticket sample) |
| RA-5 | Vulnerability management (P03 G-026); R-026 | Basic | Focused |
| IR-6, IR-8 | Incident response and notices (P03 G-078, G-096, G-098, G-099); R-015 | Focused | Basic |
| CP-9 | Backup and recovery (P05 findings); R-008 | Basic | Focused |
| SA-9 | Service providers (P03 G-075); R-016, R-022 | Focused | Focused |

## 2. Methods and objects
- **Examine:**
  - identity provider, cloud IAM, and merchant portal exports
  - pipeline settings and 25 CDE change records
  - network rules and WAF configuration
  - SIEM rules and alert timestamps
  - the 2025 scope document and data-flow diagrams
  - key-management procedures and the key ceremony log
  - scan and penetration test reports
  - the 2023 incident response plan
  - backup configuration
  - service provider contracts and AOCs
- **Interview:** COO, CTO, IT Manager, Platform Engineering Lead, Compliance and Risk Manager, HR Manager, Merchant Support Manager, and 6 randomly selected staff (incident reporting awareness).
- **Test:**
  - sign-ins by workforce users, an administrator with a hardware key, and a merchant test user
  - denied network paths from the office network and a non-CDE subnet
  - a DNS query to an unknown domain from a CDE subnet (egress detection)
  - a stopped log agent in staging (control failure alerting)
  - an unauthorized change to a staging copy of the payment page (tamper-detection)
  - PAN discovery scans of the data warehouse and 200 support tickets

## 3. Rules of engagement
- No testing in production that could affect authorizations. Payment page and log agent tests ran in staging. The DNS test used a domain owned by the assessor, with the Platform Engineering Lead present.
- No card data left the tenant. PAN discovery results were reported as counts and masked samples (BIN and last four).
- The assessor stops and notifies the IT Manager and COO on finding any critical exposure. **This rule was used once**: on 2026-08-05 the PAN discovery scan found about 2.3 million full, unencrypted PANs in a data warehouse training table. Testing of SC-28 paused. The table was purged on 2026-08-07, after the Platform Engineering Lead preserved access logs for the investigation.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 85 |
| Other than satisfied | 45 |
| **Total** | **130** |

- **Fully satisfied:** IA-2, IA-2(1) (hardware keys for all 9 administrators), IA-8, and SC-7 (the denied-path tests confirmed CDE isolation from the office network).
- **Fully other than satisfied:** AC-6, AU-5, CA-8, and SC-28. For these, the weakness affects the whole control.
- **Most other than satisfied statements:** SI-4 (6 of 12), IR-8 (5 of 17), AC-2 (5 of 26), SI-7 (4 of 6), and SA-9 (4 of 6).

**Three findings matter most for the P08 scenario:**
- A test change to the staging payment page went undetected (SI-7).
- A DNS query to an unknown domain from a CDE subnet raised no alert (SI-4).
- Three former contractors still had repository tokens that could deploy to production (AC-2, CM-3).

Together these are the path an attacker would use.

**New finding:** unencrypted PAN in the data warehouse (SC-28). It was not known before testing. It was added to the risk register as R-031 and to POAM-012. P08 section 6 analyzes whether it is reportable.

All 17 controls with weaknesses have POA&M items in `poam.csv`: 10 High and 7 Moderate. The High items are POAM-001 to POAM-005, POAM-007, POAM-009, POAM-010, POAM-012, and POAM-015. Every High item except POAM-003 (full 24x7 managed detection, 2026-12-31) is due before the QSA's fieldwork starts on 2026-11-02, or has an interim measure in place by then (POAM-009).

## 5. Deliverables
`assessment-results.csv` (130 rows), `poam.csv` (17 items), and this plan and summary. The results were accepted by the COO on 2026-08-31. POA&M status is reviewed monthly by the IT Manager and reported in the quarterly reviews required by POL-01 4.7.

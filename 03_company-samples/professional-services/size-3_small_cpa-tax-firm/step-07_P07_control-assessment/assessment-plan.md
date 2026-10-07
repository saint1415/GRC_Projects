# Security Assessment Plan and Summary: Cris Santos Company | Professional, Scientific, and Technical Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| System assessed | Tax Preparation and Client Portal Platform (TPCP), per the SSP (P02) |
| Tier / Vertical | Small / Professional, Scientific, and Technical Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls, and not the MSP. Escorted by the IT Manager |
| Assessment window | 2026-08-03 to 2026-08-07 (walkthrough of both offices 2026-08-05) |
| Also supports | FTC Safeguards Rule: regular testing of the effectiveness of key controls, 16 CFR 314.4(d)(1) (N54-R01). It does **not** replace the annual penetration test and six-month vulnerability assessments in 314.4(d)(2) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 125 determination statements.** Controls were chosen because they support the five High risks in P01 (R-001, R-004, R-010, R-011, R-018), cover the High and Moderate Safeguards Rule gaps in P03, or support the incident reporting duties that the P08 scenario depends on.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6, IA-2, IA-2(1), IA-2(2), IA-5 | Access control and MFA (314.4(c)(1), (c)(5); P03 G-010, G-011, G-015); R-001, R-009, R-010, R-033 | Focused | Focused |
| IA-8 | Client portal MFA (314.4(c)(5)); R-007 | Basic | Focused |
| AC-17 | MSP remote management tool; R-018 (High) | Focused | Focused |
| AT-2 | Training gaps (314.4(e)(1)); R-001, R-002, R-012 | Basic | Focused |
| AU-6, SI-4 | Monitoring of authorized users (314.4(c)(8)); R-001, R-004, R-005 | Focused | Basic |
| RA-5, CA-8 | Testing and monitoring (314.4(d)(2)); R-011 (High) | Focused | Focused |
| SC-8, SC-28 | Encryption (314.4(c)(3)); R-008, R-016 | Basic | Focused |
| SA-9 | Service providers (314.4(f)) and IRC 7216 contractor notice (301.7216-2(d)(2)); R-013, R-018, R-020 | Focused | Focused |
| IR-4, IR-6 | Incident response plan and reporting (314.4(h), (j); IRS Pub. 1345); R-024 | Focused | Basic |
| CP-4 | Recovery testing; R-004, R-028 | Basic | Basic |
| SI-12, MP-6 | Disposal (314.4(c)(6)); R-015, R-017 | Basic | Focused (both offices) |
| RA-3 | Written risk assessment (314.4(b)) | Focused | Basic |

## 2. Methods and objects
- **Examine:** identity provider user, role, and sign-in exports; conditional access and MFA policies; DMS permission export; EDR console; the 2025-03 scan report; contracts for the tax software, portal, cloud, MSP, and practice management vendors; the tax software vendor's SOC 2 Type 2 report; training roster; the 2023 WISP and the 2026 risk register; shredding certificates; the draft incident response runbook; MSP incident tickets from 2025 and 2026.
- **Interview:** Firm Administrator, IT Manager, IT Support Technician, MSP account lead, Tax Partner (e-file Responsible Official), Risk and Quality Partner, Client Services Supervisor, HR and Payroll Specialist, and 10 randomly selected staff (incident reporting awareness).
- **Test:**
  - sign-in tests with a standard account, an administrator account, and a legacy mail protocol against each service mailbox
  - a standard tax staff test user opening client folders of other teams in the DMS
  - an inbox rule and an external forwarding rule created on a test mailbox after hours, to see whether any alert fires
  - local administrator password comparison on 10 endpoints
  - an external scan of the VPN gateway, with the IT Manager's written approval
  - a TLS scan of external services and a sample of 50 outbound emails with attachments (content redacted)
  - encryption spot checks on 5 desktops and 2 printer-scanners

## 3. Rules of engagement
- No testing that could interrupt client work: scans and sign-in tests ran after 18:00, and no test changed a client record or a return in the tax software.
- No tax return information left the firm. Screenshots and email samples were redacted before they entered the workpapers.
- The assessor stops and notifies the IT Manager on finding any critical exposure. One case: the VPN gateway was two firmware releases behind, including a vendor advisory rated high severity. The IT Manager was notified on 2026-08-05 and the MSP updated the firmware on 2026-08-06 (verified). The process weakness stays open under POAM-006.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 46 |
| Other than satisfied | 79 |
| **Total** | **125** |

| Risk level of "Other than satisfied" statements | Count |
|---|---|
| High | 21 |
| Moderate | 51 |
| Low | 7 |

**Fully other than satisfied:** AC-6, IA-2(2), IA-8, AU-6, CA-8, SC-8, SC-28, CP-4, SI-12, and IR-6. No process or technology existed for these, or it did not meet the firm's own policy.
**Fully satisfied:** IA-2(1). Every administrator sign-in required MFA. The method (push without number matching) is weak, and that is recorded under IA-05c. and POAM-002.
**Largely satisfied:** RA-3 (the 2026 risk assessment now exists; only reporting to the Partner Group and the 2023-2026 lapse remain), IA-5 (7 of 10), and SI-4 endpoint detection (EDR works; it is the after-hours and identity and email coverage that fail).

**New finding:** the shared intake mailbox password is known to 6 current staff and 2 former employees, has not changed since 2024, and still works over a legacy mail protocol without MFA (AC-02k.[02], IA-02(02)). This was not known before testing. It was added to the risk register as R-033 on 2026-08-07 and is tracked in POAM-011 and POAM-002, due 2026-09-15.

All 21 controls with weaknesses have POA&M items in `poam.csv` (7 High, 12 Moderate, 2 Low). The High items are POAM-002 to POAM-008, all due by 2027-01-15, before the filing season.

## 5. Deliverables
`assessment-results.csv` (125 rows), `poam.csv` (21 items), and this plan and summary. The results were accepted by the Firm Administrator on 2026-08-31, and the High items by the Managing Partner on the same date.

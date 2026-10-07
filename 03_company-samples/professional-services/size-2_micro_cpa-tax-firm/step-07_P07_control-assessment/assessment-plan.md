# Security Assessment Plan and Summary: Cris Santos Company | Professional, Scientific, and Technical Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| System assessed | Client Tax Platform (CTP), per the SSP (P02) |
| Tier / Vertical | Micro / Professional, Scientific, and Technical Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent IT security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; MSP lead technician on call and present for the sign-in tests |
| Assessment window | 2026-08-03 to 2026-08-05 (on site 2026-08-04) |
| Also satisfies | The regular testing of key controls required by 16 CFR 314.4(d)(1) (N54-R01) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **15 controls, 80 determination statements.** Controls were chosen because they support the three High risks in P01 (BEC, ransomware, MSP compromise), cover High and Moderate gaps in P03, test what the MSP does for the firm, or test an IRC 7216 duty.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Seasonal assistant's accounts active 12 weeks after leaving (P01 R-007; P03 G-010) | Focused | Comprehensive (every user in the suite, tax software, portal, payroll platform, and AI assistant) |
| AC-6 | Everyday global administrator accounts; open client folders (R-008; G-011) | Focused | Comprehensive (all suite roles and top-level folders) |
| IA-2(1), IA-2(2) | MFA gaps behind BEC and MSP compromise (R-001, R-006; G-015) | Focused | Focused (all administrator logins; legacy authentication report) |
| AT-2, IR-6 | No current training; reporting duties unknown (R-001, R-020; G-024, G-052) | Basic | Comprehensive (all 7 employees interviewed) |
| AU-6 | No monitoring of user activity (R-001; G-019) | Basic | Basic |
| CP-9, CP-4 | Backup never fully restored; shared MSP account (R-022) | Focused | Focused |
| RA-3 | First risk assessment (R-021; G-005) | Basic | Basic |
| SA-9 | No provider oversight; AI assistant adopted without review (R-006, R-013, R-019; G-028 to G-030) | Focused | Comprehensive (all 8 vendors that hold client data or administer systems) |
| SC-8, SC-28 | Plain email attachments; unencrypted desktops (R-009, R-011; G-013) | Basic | Focused (15 emails; 3 devices) |
| PS-6 | Written IRC 6713 and 7216 notice to contractors (R-025; G-046) | Basic | Focused |

## 2. Methods and objects
- **Examine:** user lists and role reports from the suite, tax software, portal, payroll platform, and AI assistant; suite authentication, sharing, and alert settings; the MSP contract and SaaS terms; the tax software vendor's SOC 2 report; the P01 register and the 2024 WISP; confidentiality agreements; the MSP evidence listed below.
- **Interview:** Owner CPA, Office Manager, Senior Tax Accountant, all 7 employees (training and incident reporting), and the MSP lead technician.
- **Test:**
  - user lists compared with the staff roster in each system
  - sign-in attempts to the backup console and firewall management page without a second factor (MSP present)
  - legacy authentication sign-in report for the suite, and the MFP's scan-to-email configuration
  - encryption status on 2 desktops and 1 laptop
  - 15 emails with returns sent during the 2026 season, checked for encryption

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-07-27 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) | SI-2 (context) | Yes, 2026-07-31 |
| Antivirus console export | SI-3 (context) | Yes, 2026-07-31 |
| Device encryption report | SC-28 | Yes, 2026-07-31 |
| SYS-08 job report (July 2026) and retention settings | CP-9 | Job report yes, 2026-08-03; immutability setting not shown |
| Record of any full restore test | CP-4 | No record exists (confirmed by the MSP) |
| Technician list with access to the firm, and MFA on the remote management platform | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-012 |
| Subcontractor list and the backup vendor's terms | SA-9 | Not received by fieldwork end; follow-up in POAM-012 |

## 3. Rules of engagement
- No testing that could disrupt client work. On-site tests ran after 4 p.m. on 2026-08-04, outside the extension-season client hours.
- No client data left the office. Screenshots were redacted before they went into the evidence folder, and the assessor signed the written IRC 6713 and 7216 notice before reviewing any system.
- The assessor would stop and tell the Office Manager at once about any critical exposure. The MFP findings were reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 18 |
| Other than satisfied | 62 |
| **Total** | **80** |

**Fully other than satisfied (9 controls):** AC-6, IA-2(1), IA-2(2), AT-2, AU-6, IR-6, CP-4, SC-8, SC-28. No process or technology met the objective. AC-2 comes close: 22 of its 26 statements are other than satisfied.
**Largely satisfied:** RA-3 (the 2026 risk assessment meets every objective except the update cycle, which has never run). CP-9 is half met: the daily backup runs and is encrypted, but its integrity and availability are not protected.

**New findings from testing:**
1. The MFP sends scans through a suite mailbox ("scanner") that signs in with an app password over legacy authentication, which bypasses MFA, and the MFP's administration page still had the default password (IA-02(02); AC-02k.[01]). Added to the risk register as R-024 and to POAM-002. The administration password was changed on 2026-08-05.
2. The portal still listed the seasonal assistant's staff account after the suite and tax software accounts were disabled (AC-02i.01). Its log showed no sign-in after the assistant's last day. Removed on 2026-08-04.
3. The backup console and the firewall management login accept a password alone (IA-02(01)). POAM-003.

All 15 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-002, POAM-005, POAM-008, and POAM-009: email sign-in, monitoring, and backup, the same BEC and ransomware themes as P01.

## 5. Deliverables
`assessment-results.csv` (80 rows), `poam.csv` (15 items), and this plan and summary. The Owner CPA accepted the results on 2026-08-31.

# Security Assessment Plan and Summary: Cris Santos Company | Transportation and Warehousing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (freight forwarding and customs brokerage office) |
| System assessed | Core Brokerage SaaS Stack (CBSS), per the SSP (P02) |
| Tier / Vertical | Micro / Transportation and Warehousing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent information security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office and Compliance Manager; MSP lead technician on call |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11) |
| Also supports | Licensed broker review of the security program (19 CFR 111.28(a)(8)); the CTPAT client questionnaire answers (P09) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **12 controls, 83 determination statements.** Controls were chosen because they support the three High risks in P01 (BEC payment diversion, ransomware with record theft, MSP compromise), cover the High and Moderate customs broker gaps in P03, or test what the MSP does on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Shared accounts and the former Entry Writer's late removal (P01 R-003, R-005; P03 G-024) | Focused | Comprehensive (all 7 users in every SaaS, the bank, and the backup console) |
| IA-2(1), IA-5 | MFA on MSP-held logins; shared and default passwords (R-003, R-009, R-014) | Focused | Focused |
| AT-2, IR-6 | No training; nobody knew the 72-hour CBP notice (R-001, R-004; G-008) | Basic | Focused (5 of 7 employees interviewed) |
| CP-9, CP-4 | Backup copy of records never tested (R-006; G-041, G-043) | Focused | Focused |
| SA-9 | Vendor terms, data location, client authorization (R-011, R-014; G-013, G-015) | Focused | Comprehensive (all 5 vendors that hold client records or administer systems) |
| AU-6 | No review of sign-ins, forwarding rules, or exports (R-001, R-002) | Basic | Basic |
| MP-6 | Disposal records (G-047) | Basic | Focused (12 months of certificates; 2 retired desktops) |
| SI-8 | Look-alike domain and impersonation protection (R-001) | Focused | Focused (one test message) |

## 2. Methods and objects
- **Examine:** user lists for the customs platform, suite, accounting SaaS, bank, and backup console; platform role list; suite security and mail filter settings; contracts and terms; the platform vendor's SOC 2 report; P01 risk register; training records; shredding certificates; the MSP evidence listed below.
- **Interview:** owner, Office and Compliance Manager, Entry Supervisor, Accounting Specialist, 5 of 7 employees (training and incident reporting), and the MSP lead technician.
- **Test:**
  - user lists compared against the staff roster in every system
  - sign-in attempts to the backup console, firewall management page, and entries@ without a second factor (with the MSP present)
  - a review of the printer's web administration page
  - a harmless test message from a look-alike domain registered by the assessor, sent to the Accounting Specialist with the owner's prior approval

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 (context) | Yes, 2026-08-07 |
| Antivirus console export | SI-3 (context) | Yes, 2026-08-07 |
| Device encryption report | SC-28 (context) | Yes, 2026-08-07 |
| Backup job report (July 2026), retention settings, storage region | CP-9 | Job report and retention yes, 2026-08-10; storage region not known to the MSP |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Tickets for the 2 desktops replaced in 2025 | MP-6 | Tickets show pickup only; no wipe record |
| Technician list with access, MFA on the remote management platform, subcontractor list | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-009 |

## 3. Rules of engagement
- No testing that could disrupt filings. On-site tests ran on 2026-08-11 after the day's ISF cutoffs.
- No client data left the office. Screenshots were redacted before they went into the evidence folder.
- The look-alike domain test message contained no link or attachment and was approved in advance by the owner; the Accounting Specialist was told the same day.
- The assessor would stop and tell the Office and Compliance Manager at once about any critical exposure. The printer default password was reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 22 |
| Other than satisfied | 61 |
| **Total** | **83** |

**Fully other than satisfied:** IA-2(1), AT-2, IR-6, CP-4, AU-6. No process or technology met the objective.
**Mostly satisfied:** SI-8 (filtering works; impersonation protection does not). **Half satisfied:** CP-9 and MP-6.

**New findings from testing:**
1. The printer's web administration page still used the manufacturer's default password, and the printer stores the entries@ password for scan-to-email (IA-05e., IA-05g.). Added to the risk register as R-022; the MSP changed the password on 2026-08-14 and the risk is closed. The stored credential stays open under POAM-004.
2. The look-alike domain test message reached the Accounting Specialist with no warning or external tag (SI-08a.[03]). POAM-012 (High), tied to P01 R-001.
3. The backup console, the firewall management page, and entries@ accept a password alone (IA-02(01)). POAM-003.

All 12 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-007, POAM-008, and POAM-012: the backup copy of records and the BEC path, the same themes as P01.

## 5. Deliverables
`assessment-results.csv` (83 rows), `poam.csv` (12 items: 3 High, 8 Moderate, 1 Low), and this plan and summary. The owner accepted the results on 2026-08-31.

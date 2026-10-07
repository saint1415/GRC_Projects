# Security Assessment Plan and Summary: Cris Santos Company | Wholesale Trade | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software reseller) |
| System assessed | Reseller Operations Platform (ROP), per the SSP (P02), including the purchasing and receiving steps that apply the SR controls |
| Tier / Vertical | Micro / Wholesale Trade |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Operations Manager; MSP lead technician on call |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11) |
| Not to be confused with | The CMMC Level 1 self-assessment. That uses the NIST SP 800-171A objectives for the 15 FAR 52.204-21 requirements (32 CFR 170.15(c)(1)) and is planned for 2026-10-31. This assessment tests the SP 800-53 controls in the SSP |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **14 controls, 85 determination statements.** Controls were chosen because they support the Very High and High risks in P01 (unsupported affirmation, counterfeit and covered products, payment fraud, MSP compromise), cover FAR 52.204-21 requirements with gaps in P03, or test what the MSP does on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, IA-2 | Former technician account; shared portal and carrier logins (P01 R-008, R-009; P03 G-001, G-005) | Focused | Comprehensive (all 7 users in the ERP, suite, distributor portal, and carrier service) |
| IA-2(1) | MFA on administrator access, including MSP-held logins (P03 G-006); R-010 | Focused | Focused |
| AT-2, IR-6 | No training; no reporting route for the 1-business-day Section 889 clock (R-003, R-019) | Basic | Focused (5 of 7 staff interviewed) |
| CM-8 | Inventory and Section 889 "use" representation (P03 G-017) | Focused | Comprehensive (walk-down of office, closet, and stockroom) |
| CP-9 | Backup never tested (R-007) | Focused | Focused |
| MP-6, PE-8 | FAR 52.204-21(b)(1)(vii) and (ix) Not met (P03 G-007, G-009); R-014 | Basic | Focused |
| SA-9 | MSP and SaaS vendors that hold FCI; AI subprocessor (R-010, R-021) | Focused | Comprehensive (all 4 providers that hold FCI or administer systems) |
| SI-2 | Patching, including network and camera devices (P03 G-012) | Focused | Focused (3 laptops, the bench, firewall, recorder) |
| SR-5, SR-10, SR-11 | Counterfeit, tampered, and covered products; DFARS 252.246-7008 (R-001, R-002) | Focused | Focused (item master query; 4 receipts observed) |

## 2. Methods and objects
- **Examine:** ERP, suite, distributor portal, and carrier user lists; ERP role list; suite security settings; vendor contracts; the ERP vendor's SOC 2 report; the MSP evidence listed below; the supplier list and spend report; the ERP item master; the P01 register and P03 workbook.
- **Interview:** Owner, Operations Manager, Federal Account Manager, Purchasing and Inventory Coordinator, Setup and Receiving Technician, Bookkeeper, Commercial Account Manager, and the MSP lead technician.
- **Test:**
  - user lists compared with the staff list; sign-in attempts to the carrier account with the old shared password
  - sign-in attempts to the backup console, firewall management page, and distributor portal administrator account without a second factor (with the MSP present)
  - walk-down of every networked device compared with the MSP list, including labels and the recorder's administration page
  - patch and firmware status on 3 laptops, the setup bench, the firewall, and the recorder
  - query of active SKUs with no manufacturer of record
  - observation of 4 inbound receipts and 2 hours of stockroom door traffic

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-07 |
| Endpoint protection console export | SI-3 (P03 G-013 to G-015) | Yes, 2026-08-07 |
| Laptop encryption report | SC-28 | Yes, 2026-08-07 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-07 |
| Record of any restore test | CP-9 | No record exists (confirmed by the MSP) |
| Firewall rule export and firmware record | SC-7, SI-2 | Yes, 2026-08-07 |
| Technician list and MFA on the RMM platform | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-010 |
| Wipe records for retired laptops | MP-6 | None exist |

## 3. Rules of engagement
- No testing that could disrupt shipping. On-site tests ran after the afternoon carrier pickup on 2026-08-11.
- No FCI left the site. Screenshots of user lists and equipment lists were redacted before they went into the evidence folder.
- The assessor would stop and tell the Operations Manager at once about any critical exposure. The covered camera recorder was reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 20 |
| Other than satisfied | 65 |
| **Total** | **85** |

**Fully other than satisfied (6 controls):** IA-2, IA-2(1), IR-6, PE-8, SR-10, SR-11. No process or technology met the objective. AT-2 comes close: only the MSP's phishing warning emails were satisfied.
**Largely satisfied:** CP-9 (backups run and are encrypted; they are not protected from deletion) and SI-2 (computers are patched well; network and camera devices are not).

**New findings from testing:**
1. **Covered equipment in the company's own stockroom (CM-08a.02).** The walk-down found the camera recorder and 4 cameras, bought from a broker in 2019, on no inventory. Their labels and the recorder's administration page show they are white-label units of a manufacturer named in paragraph (2) of the "covered telecommunications equipment or services" definition in FAR 52.204-25. The assessor told the Owner and Operations Manager on 2026-08-11. The devices were disconnected on 2026-08-12 and replaced with equipment from a non-covered manufacturer on 2026-08-20. Whether the company's private stockroom use falls within that paragraph is a legal question; counsel is reviewing the company's 52.204-26 "does not use" representation and whether any report is due. Added to the risk register as R-024, to P03 row G-017, and to POAM-005.
2. **Carrier account still open to a former employee (AC-02i.01).** The carrier account accepted the shared password the former technician knew. The carrier's activity log showed no use after his last day. Changed on 2026-08-12 (POAM-001).
3. **MSP-held administrator logins without MFA (IA-02(01)).** The backup console and firewall management login accept a password alone (POAM-003).

All 14 controls have at least one weakness and a POA&M item in `poam.csv` (6 High, 8 Moderate). The High items are POAM-004, POAM-005, POAM-010, and POAM-012 to POAM-014: training, inventory and Section 889, vendor oversight, and the three supply chain controls, the same "vouch for what you sell and say" theme as P01.

## 5. Deliverables
`assessment-results.csv` (85 rows), `poam.csv` (14 items), and this plan and summary. The Owner accepted the results on 2026-08-31.

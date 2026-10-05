# Security Assessment Plan and Summary: Cris Santos Company | Critical Manufacturing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (transformer repair and remanufacturing shop, Florida) |
| System assessed | ERP and Job Scheduling Platform (EJSP), per the SSP (P02), plus the remote access paths into the shop network |
| Tier / Vertical | Micro / Critical Manufacturing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; the Shop Manager for shop equipment; MSP lead technician on call |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 98 determination statements.** Controls were chosen because they support the High risks in P01 (ransomware over the flat network, the OEM modem, the cooperative exhibit), carry FAR 52.204-21 safeguards with gaps in P03, or test what the MSP and vendors do on the shop's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Former technician's access active 10 weeks; cooperative notice missed (P01 R-005, R-006; P03 G-005, G-039, G-059) | Focused | Comprehensive (all accounts in the ERP, suite, AI portal, and backup service) |
| IA-2(1) | ERP without MFA; MSP-held logins (P01 R-010; P03 G-018) | Focused | Focused |
| AC-17, MA-4 | Remote access by the MSP, the test set vendor, and the oven OEM (P01 R-003; P03 G-028) | Focused | Comprehensive (all 3 remote paths) |
| SC-7 | Flat network; FAR (b)(1)(x)-(xi) (P01 R-001, R-016; P03 G-025, G-048) | Focused | Focused (external port scan; internal reachability test from a laptop) |
| CM-8 | No inventory; FAR 52.204-25 inquiry depends on it (P03 G-011) | Basic | Comprehensive (walkthrough of office and shop) |
| CP-9 | Backups never tested; no ERP export or test PC backup (P01 R-002, R-011; P03 G-023) | Focused | Focused |
| SI-2, SI-3 | Unsupported test PC; FAR (b)(1)(xii)-(xv) (P03 G-050 to G-053) | Focused | Focused (3 computers including the test PC; alert routing test) |
| AT-2, IR-6 | No training; no reporting rules (P01 R-004; P03 G-021, G-033) | Basic | Focused (5 of 7 employees interviewed) |
| SA-9 | No vendor terms or oversight (P01 R-009, R-018; P03 G-009) | Focused | Comprehensive (MSP, ERP vendor, oven OEM, test set vendor, AI vendor) |

## 2. Methods and objects
- **Examine:** ERP, suite, AI portal, and backup service user lists; ERP role list and security settings; suite MFA and sharing reports; firewall rule export; Wi-Fi settings; MSP contract; ERP vendor SOC 2 report; OEM and test set vendor service terms; AI vendor terms; leaver record and cooperative email; the MSP evidence listed below.
- **Interview:** Owner, Office Manager, Shop Manager, Field Service and Test Technician, Lead Winder, 5 of 7 employees on training and reporting, and the MSP lead technician.
- **Test:**
  - user lists compared with the staff list in each system
  - sign-in attempts to the ERP administrator account, the firewall, and the backup service without a second factor (with the MSP present)
  - an external port scan of the shop's internet address, and a reachability test from a laptop on the staff Wi-Fi to the test PC and oven HMI
  - patch status on 2 office computers and the test PC
  - an industry-standard harmless antivirus test file on 1 desktop, and an after-hours test alert to check routing
  - a look at the oven modem's status light and SIM details with the Shop Manager (no change to the oven controls)

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-06 |
| Antivirus console export (all managed computers) | SI-3 | Yes, 2026-08-06 |
| Device list and encryption report | CM-8, SC-28 | Yes, 2026-08-06 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-07 |
| Record of any restore test | CP-9 | No record exists (confirmed by the MSP) |
| Firewall rule export and firmware record | SC-7, SI-2 | Yes, 2026-08-07 |
| Technician list with access to the shop, and MFA on the RMM platform | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-012 |

## 3. Rules of engagement
- No testing that could disrupt production or safety. Nothing on the oven controls, test set, or winding machine was changed. The test PC was examined at the end of the day on 2026-08-11 with no test in progress.
- The external port scan was limited to the shop's own internet address, with the Owner's written approval and the MSP informed.
- No FCI, employee data, or customer data left the shop. Screenshots were redacted before they went into the evidence folder.
- The assessor would stop and tell the Owner at once about any critical exposure. The internet-exposed remote desktop on the test PC was reported within the hour, and the MSP removed the rule the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 15 |
| Other than satisfied | 83 |
| **Total** | **98** |

**Fully other than satisfied:** IA-2(1), AC-17, SC-7, AT-2, IR-6, MA-4. No process or technology met the objective.
**Partly satisfied:** SI-2 (the MSP's process for managed computers works; the test PC, firmware, and time limits do not), CM-8 and CP-9 (what exists is sound but covers too little), PS-4 (property collected; access and notices not), AC-2, SI-3, and SA-9.

**New findings from testing:**
1. A 2024 port-forwarding rule exposed remote desktop on the unsupported test PC to the internet (AC-17b., SC-07a.[02]). Removed by the MSP on 2026-08-11; an offline malware scan on 2026-08-12 found nothing. Added to the risk register as R-024 (High) and to POAM-005.
2. From a laptop on the staff Wi-Fi, the assessor reached the oven HMI status page and the test PC's file share (SC-07a.[04]). POAM-003.
3. The MSP's technicians share one firewall administrator login with no MFA (IA-02(01)). POAM-002.
4. Two disabled 2024 accounts remained in the suite (AC-02f.[05]). Removed on 2026-08-12.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The 7 High items are POAM-002, POAM-003, POAM-005, POAM-006, POAM-007, POAM-008, and POAM-013: the ways in from outside (remote access, MFA, the flat network), recovery (backups, the unsupported test PC), and the cooperative's access notice.

## 5. Deliverables
`assessment-results.csv` (98 rows), `poam.csv` (13 items), and this plan and summary. The Owner accepted the results on 2026-08-31.

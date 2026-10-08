# Security Assessment Plan and Summary: Cris Santos Company | Wholesale Trade | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software wholesale distributor) |
| System assessed | Order-to-Fulfillment Platform (OFP), per the SSP (P02), including the purchasing and receiving processes that apply the SR controls |
| Tier / Vertical | Small / Wholesale Trade |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls. Escorted by the IT Manager |
| Assessment window | 2026-08-03 to 2026-08-07 (walkthrough of the distribution center, dock, and lab cage 2026-08-05) |
| Also supports | SP 800-171 Rev. 2 requirement 3.12.1 (periodic assessment); readiness for the voluntary 2027-02 CMMC Level 2 (C3PAO) assessment |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **25 controls, 130 determination statements.** Controls were chosen because they support the High risks in P01, cover the SP 800-171 requirements that cannot be placed on a CMMC POA&M, or test the supply chain controls behind the P08 incident scenario.

This is an SP 800-53A assessment of the SP 800-53 controls in the SSP. It is **not** a CMMC assessment: a C3PAO will assess the 110 SP 800-171 requirements against SP 800-171A objectives in 2027-02.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-3, IA-2, IA-2(2), SC-7, SC-13, MP-7 | CUI exposure and enclave gaps (P03 3.1.1 to 3.1.3, 3.5.3, 3.13.2, 3.13.11, 3.8.7); R-004 (High) | Focused | Focused (CUI share, lab, WMS) |
| AC-17 | Remote access path for staff and the MSP (3.1.12) | Basic | Basic |
| SA-9 | CUI in a SaaS without FedRAMP equivalency; MSP as an External Service Provider; R-010 (High) | Focused | Focused |
| SR-2, SR-5, SR-6, SR-10, SR-11, SR-11(1) | Counterfeit, tampered, and covered equipment (DFARS 252.246-7008, FAR 52.204-25); R-001, R-002 (High) | Focused | Focused (purchasing, receiving, lab) |
| CP-9 | Backups; R-007 (High), R-008 | Focused | Focused |
| IR-4, IR-6 | No incident capability; DIBNet reporting (3.6.1, 3.6.2) | Focused | Basic |
| AT-2, AT-3 | Training gaps (3.2.1, 3.2.2); R-003 (High), R-025 | Basic | Focused |
| AU-6, AU-11, SI-4 | No log review or monitoring (3.3.1, 3.3.5, 3.14.6) | Basic | Basic |
| RA-5 | No vulnerability scanning (3.11.2) | Basic | Basic |
| CM-8 | Inventory and CMMC asset categories (3.4.1) | Basic | Focused |
| PE-3 | Dock, visitor, and cage controls (3.10.3 to 3.10.5, which cannot be on a CMMC POA&M) | Focused | Focused |

## 2. Methods and objects
- **Examine:** identity provider, ERP, file share, and firewall exports; backup history; vendor contracts and SOC 2 reports; the approved supplier list; the item master extract; purchase history; training roster; draft POL-01 and POL-03; the P08 runbook draft; badge and visitor logs.
- **Interview:** Chief Operating Officer, IT Manager, Systems Administrator, MSP lead technician, Government Contracts Manager, Purchasing and Supplier Manager, Configuration Lab Lead, Warehouse and Logistics Manager, Controller, HR Manager, 2 receiving clerks, 2 buyers, and 8 randomly selected staff (incident reporting awareness).
- **Test:**
  - sign-in to the CUI folder with a warehouse test account, and to the CUI share from the office network (MFA check)
  - sign-in on 3 handhelds (shared accounts)
  - VPN sign-in with a non-member account
  - lab workstation reachability to office subnets and the internet
  - unregistered USB drive on 2 lab workstations and 2 office laptops
  - restore of one file server folder from backup
  - observation of 6 inbound receipts at the dock
  - query of broker-sourced SKUs with a blank manufacturer of record, compared with broker catalogs
  - simulated malicious download to check alert routing

## 3. Rules of engagement
- No testing that could disrupt shipping. Network tests ran after the 5 p.m. carrier cutoff, with the IT Manager present.
- CUI was viewed only in the lab cage by the assessor, who is a U.S. person. No CUI or FCI left the site; screenshots were redacted.
- The assessor stopped and notified the IT Manager on finding any critical exposure. One such finding (the white-label SKUs below) was reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 21 |
| Other than satisfied | 109 |
| **Total** | **130** |

**Fully other than satisfied (16 controls):** AC-3, AT-3, AU-6, AU-11, IA-2(2), IR-4, IR-6, MP-7, RA-5, SC-13, SR-2, SR-5, SR-6, SR-10, SR-11, SR-11(1). No plan, process, or technology existed for these at fieldwork.
**Fully satisfied (1 control):** AC-17 (remote access through the VPN with MFA and approved group membership).
**Partly satisfied:** CP-9 (backups run and are encrypted), SC-7 (internet boundary), PE-3 (badge doors and cage), SA-9 (contract confidentiality terms), IA-2 (named accounts outside the WMS), CM-8, AT-2, SI-4.

**New finding (SR-05[02]).** A query of broker-sourced SKUs with a blank manufacturer of record found 3 IP camera and video recorder SKUs from one broker. The broker's catalog lists them as rebranded units of a manufacturer named in FAR 52.204-25. None had shipped on a DoD order. The assessor told the IT Manager and the Government Contracts Manager on 2026-08-06. The SKUs were blocked and the stock quarantined on 2026-08-07. This was added to the risk register as R-035 and to POAM-012, and the Government Contracts Manager confirmed with counsel that no FAR 52.204-25(d) report was due because no covered equipment was delivered or used under a federal contract. The P08 runbook uses this case as its worked example.

All 24 controls with weaknesses have POA&M items in `poam.csv` (10 High, 14 Moderate). The High items are POAM-001 to POAM-004, POAM-006, POAM-007, and POAM-009 to POAM-012.

## 5. Deliverables
`assessment-results.csv` (130 rows), `poam.csv` (24 items), this plan and summary. The results were accepted by the Chief Operating Officer on 2026-08-31.

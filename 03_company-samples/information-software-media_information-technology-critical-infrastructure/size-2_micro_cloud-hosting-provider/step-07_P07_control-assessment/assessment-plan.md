# Security Assessment Plan and Summary: Cris Santos Company | Information Technology | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (managed cloud hosting provider) |
| System assessed | Hosting Control Plane and Customer Portal (HCP), per the SSP (P02) |
| Tier / Vertical | Micro / Information Technology |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent IT security consultant under a fixed-fee engagement (signed 2026-07-28). Took no part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Lead Systems Engineer; the Operations Manager joined the interviews |
| Assessment window | 2026-08-17 to 2026-08-19 (DC-1 walkthrough and tests 2026-08-18) |
| Also satisfies | The independent testing of key controls both bank contracts expect (Interagency Guidelines III.C.3) |

## 1. Scope and controls selected
Micro tier scope: 10 to 15 controls. **13 controls, 83 determination statements.** Controls were chosen because they:
- carry the Very High and High risks in P01, all about concentrated access to tools that reach every customer;
- cover High gaps in P03 against the bank contracts;
- or test what the MDR provider and the SaaS vendors do for the company.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Shared RMM accounts; former Support Engineer's access (P01 R-001, R-007; P03 G-018) | Focused | Comprehensive (all 7 staff in every system with its own accounts, plus the colocation list) |
| AC-5, AC-6 | One engineer can act on every customer; portal service account and Owner's standing rights (R-001, R-002, R-004, R-017; G-022) | Focused | Focused |
| AC-17, IA-2(1) | Open consoles; no MFA at the hypervisor layer (R-001, R-003; G-018) | Focused | Focused (RMM, cloud, hypervisor manager, BMCs) |
| IA-5 | Shared and default credentials (R-003; G-018) | Focused | Focused (all DC-1 devices checked for default passwords) |
| CP-9, CP-4 | Deletable backups; no restore tests (R-002, R-009; G-025, G-027) | Focused | Focused |
| SI-4, AU-6 | Management plane not monitored; AI auto-close (R-012, R-013; G-023) | Focused | Focused |
| IR-6 | Bank notice duty and contacts (R-014; G-003, G-004, G-034) | Basic | Focused (5 of 7 staff interviewed) |
| SA-9 | Vendors never reviewed (R-019; G-029 to G-031) | Basic | Comprehensive (all 7 vendors that hold customer data or run controls) |

## 2. Methods and objects
- **Examine:** user and role exports from the identity provider, VPN, RMM tool, hypervisor manager, cloud tenant, DNS account, and PSA; the staff roster and the termination record; the colocation authorized-person list; RMM, cloud, and backup settings; the backup job report; the MDR data source list, contract, and July 2026 report; the contract folder; the colocation SOC 2 report; the bank contracts and contact file; the draft POL-02 and POL-03.
- **Interview:** Owner, Operations Manager, Lead Systems Engineer, both Systems Engineers, one Support Engineer.
- **Test (2026-08-18):**
  - user lists compared with the roster in every system, and the colocation list checked at the facility desk;
  - sign-in to the hypervisor manager over the VPN with the shared password only;
  - RMM sign-in from a mobile hotspot using an assessment-only technician account, created for the test and deleted afterwards;
  - a harmless test script scheduled against the company's own lab VMs, to check whether any approval step or MDR alert followed;
  - default-password check of every DC-1 device's management interface;
  - review of cloud account roles to see who can delete the backup copy.

### MDR and vendor evidence requested
The MDR provider runs the company's monitoring, and SaaS vendors run several controls. Evidence was requested on 2026-08-10 with a one-week deadline:

| Item | From | Supports | Received |
|---|---|---|---|
| Data source list and July 2026 monthly report | MDR provider | SI-4, AU-6 | Yes, 2026-08-12 |
| Auto-close statistics and automated-action log for July 2026 | MDR provider | SI-4, AU-6 (P10) | Yes, 2026-08-14 |
| MDR SOC 2 report | MDR provider | SA-9 | Not received by fieldwork end; follow-up in POAM-012 |
| Technician list and audit log export (30 days) | RMM vendor portal (self-service) | AC-2, AC-17 | Yes, 2026-08-17 |
| RMM SOC 2 report and incident notice commitment | RMM vendor | SA-9 | Not received by fieldwork end; follow-up in POAM-012 |
| Authorized-person list and cage access report | Colocation provider | AC-2, PE-2 | Yes, 2026-08-18 at the facility desk |
| Cloud audit trail (90 days) and role export | Public cloud tenant (self-service) | AC-6, CP-9 | Yes, 2026-08-17 |

## 3. Rules of engagement
- **No testing that could affect customers.** Nothing was run on customer VMs or customer servers. The test script ran only on the company's lab VMs, and the RMM test account was deleted the same day.
- **Bank systems were observed, not touched.** Bank A's VMs and both banks' servers were only examined through configuration and role exports.
- **Customer data stayed in place.** No customer data left company systems. Screenshots were redacted before they went into the evidence folder.
- **Critical findings were reported the same day.** The assessor would stop and tell the Lead Systems Engineer at once about any critical exposure. The default backup appliance password and the former employee on the colocation list were both reported on 2026-08-18.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 17 |
| Other than satisfied | 66 |
| **Total** | **83** |

Of the 66 statements other than satisfied, the assessor rated 3 Very High, 25 High, 25 Moderate, and 13 Low.

**Fully other than satisfied (6 controls):** AC-5, AC-6, IA-2(1), CP-4, AU-6, IR-6. No process or setting met the objective.
**Best results:**
- IA-5 (4 of 10): new staff get their credentials properly and use the password manager.
- SI-4 (4 of 12): the MDR's coverage of laptops, firewalls, and sign-ins works.
- CP-9 (2 of 6): backups run every night; protecting them is the gap.

**New findings from testing:**
1. **The backup appliance still accepted the vendor's default administrator password** (IA-05e.). Every VPN user could reach it. Changed on 2026-08-19, added to the risk register as R-024, and tracked in POAM-008.
2. **The former Support Engineer was still on the colocation authorized-person list** five months after leaving (AC-02f.[05]). Removed on 2026-08-18. POAM-013.
3. **The hypervisor manager accepted the shared password alone** once on the VPN (IA-02(01)). POAM-002.
4. **An RMM sign-in from a non-company address and a test script produced no alert and needed no approval** (AC-17a.[02], AC-05b., SI-04a.02[03]). POAM-004, POAM-005, POAM-009.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`:
- **Very High (1):** POAM-001, shared RMM accounts. This is risk R-001, and the Owner's acceptance of continued operation (P02 section 4.2) depends on its 2026-10-15 milestone.
- **High (8):** POAM-002 to POAM-009. Together they cover concentrated access, backups, and blind spots in monitoring.
- **Moderate (4):** POAM-010 to POAM-013.

## 5. Deliverables
`assessment-results.csv` (83 rows), `poam.csv` (13 items: 6 In progress, 7 Open), and this plan and summary. The Owner accepted the results on 2026-09-15. The Lead Systems Engineer tracks the POA&M monthly with the Owner (POL-02 A.10). The next independent assessment is due by 2027-08-31 (POL-02 A.6).

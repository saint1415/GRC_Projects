# Security Assessment Plan and Summary: Cris Santos Company | Energy | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (small intrastate natural gas transmission pipeline operator) |
| System assessed | Pipeline SCADA and Gas Control System (PSGCS), per the SSP (P02) |
| Tier / Vertical | Micro / Energy |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor and independence | Independent OT security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Escorted by the Operations Manager; MSP lead technician on call |
| Criteria | The draft SSP control statements (P02) and draft policies POL-02 to POL-04 (P06), both approved 2026-09-15 |
| Assessment window | 2026-08-17 to 2026-08-19 (field sites visited 2026-08-18) |
| Also supports | The first-year assessment that SD 02G Section III.G would require on TSA designation (readiness only) |

## 1. Scope and controls selected
Micro tier scope: 10 to 15 controls. **13 controls, 108 determination statements.** Controls were chosen for three reasons:
- They address the four High risks in P01 (R-001, R-002, R-003, R-005).
- They address the High CSF benchmark gaps in P03 (G-030, G-032, G-039, G-043).
- They test what the SCADA vendor and the MSP do on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Shared desk login; departed technician's account (R-006; P03 G-031) | Focused | Comprehensive (all 5 active SCADA accounts; suite and accounting users) |
| IA-2(1), IA-5 | Password-only SCADA access; field device passwords (R-002; G-032) | Focused | Focused (SCADA administrator; 3 gateways) |
| AC-17, MA-4 | Remote command rights; vendor support access (R-002, R-003) | Focused | Focused |
| SC-7 | Flat office network; private telemetry network (R-001; G-039) | Focused | Focused (all 7 SIMs examined; 3 gateways tested) |
| CM-8 | No PSGCS inventory (G-026) | Basic | Focused (3 field sites) |
| CP-9, CP-4 | Configuration copies, backups, and exercises (R-009, R-016, R-019) | Focused | Basic |
| IR-8 | No incident response plan (R-005; G-030, G-043) | Basic | Basic |
| AU-6 | No log review (G-042) | Basic | Basic |
| SA-9 | No supplier terms (R-003, R-004; G-024) | Focused | Comprehensive (all 3 key contracts) |
| AT-2 | No awareness training (R-001, R-012; G-034) | Basic | Focused (5 of 7 staff interviewed) |

## 2. Methods and objects
- **Examine:** SCADA user list, role matrix, and access settings; suite and accounting user lists; the SCADA vendor's SOC 2 report (received 2026-08-14); contracts with the SCADA vendor, the MSP, and the carrier; carrier APN settings for all 7 SIMs; the MSP device list, patch report, and backup job report; the O&M manual, emergency plan, and November 2025 drill report; training records; the draft P08 runbook; the P01 risk register.
- **Interview:** the Owner, the Operations Manager, the Office Manager, 5 of 7 staff (training and reporting), and the MSP lead technician.
- **Test (read-only, never on a live control path):**
  - a sign-in to the SCADA web client from an outside network with a controller account, observed by the Operations Manager, stopping at the first display (no command sent);
  - a sign-in to the SCADA administrator account to check for a second factor;
  - a check of saved passwords in the browsers of the 3 controller laptops;
  - a reachability check of 3 gateways from the internet and a login attempt at each with the manufacturer default credentials, done with the gateway vendor's guidance and the on-duty controller informed;
  - a comparison of the field devices at 3 sites against the SCADA point list.

### Provider evidence requested
The SCADA vendor and the MSP operate many controls, so evidence came from them. Requested on 2026-08-07 with a one-week deadline:

| Item | From | Supports | Received |
|---|---|---|---|
| SOC 2 Type 2 report and bridge letter | SCADA vendor | CP-9, MA-4, SA-9 | Report yes, 2026-08-14; bridge letter requested (P09) |
| Tenant audit log export (90 days) and change history | SCADA vendor | AU-6, MA-4 | Yes, 2026-08-14 |
| Monthly patch report and antivirus console export | MSP | Context for SC-7 | Yes, 2026-08-12 |
| Suite backup job report and retention settings | MSP | CP-9 | Yes, 2026-08-12 |
| Firewall rule export | MSP | SC-7 | Yes, 2026-08-12 |
| Technician list and MFA on the RMM tool | MSP | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-011 |

## 3. Rules of engagement
- **No active scanning of field devices or the SCADA service.** SP 800-82 Rev. 3 warns that active scanning can disrupt control systems. Vulnerability information came from configuration exports and vendor documentation.
- Every test near SCADA was approved in advance by the Operations Manager and announced to the controller on duty, who could stop any test.
- No setting on a field device was changed by the assessor. The default-password test stopped at the gateway's status page.
- The assessor would stop and tell the Operations Manager at once about any exposure that could affect pipeline control. One finding met this bar (section 4) and was reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 21 |
| Other than satisfied | 87 |
| **Total** | **108** |

**Fully other than satisfied:** IA-2(1), IR-8, AU-6, and AT-2. No plan, process, or technology existed for these at fieldwork.
**Half satisfied:** CP-9 (the vendor and the MSP back up data; the company's own configuration has no copy) and MA-4 (the vendor's support controls are sound; the company neither approves nor sees the sessions).

**New finding from testing:** the gateway at the municipal gate station answered on a public internet address and accepted the manufacturer default administrator password (SC-07a.[02], SC-07c., IA-05e.). A replacement SIM installed in May 2026 had been provisioned off the carrier private network, and the default password had never been changed. The finding was reported to the Operations Manager on 2026-08-18. The carrier moved the SIM back to the private network and the password was changed on 2026-08-19. It was added to the risk register as R-023 and to POAM-004 and POAM-005.

**Other test observations:**
- A controller account reached the SCADA web client with command rights from an outside network with a password only (AC-17a.[02]).
- Browser-saved SCADA passwords were found on 2 of 3 controller laptops (IA-05g.). They were removed on 2026-08-19.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-002, POAM-003, POAM-004, and POAM-009: SCADA authentication, remote command access, network separation, and incident response, the same theme as the High risks in P01.

## 5. Deliverables
- `assessment-results.csv` (108 rows)
- `poam.csv` (13 items: 4 High, 8 Moderate, 1 Low)
- this plan and summary

The Owner accepted the results on 2026-09-15.

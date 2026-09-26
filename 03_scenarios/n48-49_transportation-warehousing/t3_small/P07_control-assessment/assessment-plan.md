# Security Assessment Plan and Summary: Cris Santos Company | Transportation and Warehousing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (marine cargo terminal operator, NAICS 488320) |
| System assessed | Terminal Operations and Gate Platform (TOGP), per the SSP (P02), plus its interfaces to the crane and yard equipment controllers (OT) |
| Tier / Vertical | Small / Transportation and Warehousing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor with OT experience. Not involved in operating or designing the controls. Escorted by the IT Manager, and by the Maintenance Manager for OT tests |
| Assessment window | 2026-08-10 to 2026-08-14. OT tests on the night of 2026-08-12, with no vessel at berth |
| Also supports | The Cybersecurity Assessment required by 33 CFR 101.650(e)(1) by 2027-07-16 (validation of measures), and the future annual Plan audit by independent auditors (101.630(f)) |

## 1. Scope and controls selected
Small tier scope: 15 to 25 controls. **24 controls, 155 determination statements.** Controls were chosen because they support the 4 High risks in P01, cover the Subpart F measures with High or overdue gaps in P03, or underpin the ransomware scenario in P08.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| IA-2(2), AC-17, MA-4 | MFA and remote access gaps (101.650(a)(4), (e)(3)(v), (f)(3)); R-001, R-003 (High) | Focused | Focused |
| SC-7, AC-4, SI-4 | No IT/OT segmentation or monitoring (101.650(h)); R-001, R-002 (High) | Focused | Focused |
| CP-9, CP-4 | Backups exposed and untested (101.650(g)(4)); R-004 (High) | Focused | Focused |
| IR-4, IR-6 | No Cyber Incident Response Plan; 6.16-1 reporting (101.650(g)(2)); R-005 | Focused | Basic |
| AC-2, AC-6, IA-2, IA-2(1), IA-5 | Account security measures (101.650(a)(1)-(7)); R-008, R-012, R-013, R-014 | Focused | Focused |
| AT-2 | Missed training deadline (101.650(d)); R-007 | Basic | Focused |
| AU-9 | Log protection (101.650(c)(1)); R-021 | Basic | Basic |
| CM-6, CM-7, CM-8, MP-7 | Device security measures and ports (101.650(b), (i)(2)); R-022, R-025 | Focused | Focused (gate complex and 1 STS crane, 2 RTGs) |
| RA-5, SI-2 | Vulnerability and patch management, KEVs (101.650(e)(3)); R-009, R-010 | Basic | Basic |
| SA-9 | Vendor terms and oversight (101.650(f)); R-018 | Focused | Focused |

## 2. Methods and objects
- **Examine:**
  - identity provider, TOS and cloud IAM exports
  - firewall, switch, VPN and wireless controller configurations
  - backup console and snapshot settings
  - patch and antivirus reports
  - contracts with the TOS vendor, MSP, crane vendor, OCR vendor and scheduling vendor
  - the training platform export
  - the FSP reporting section (SSI, read on site)
  - the draft ransomware runbook
- **Interview:**
  - General Manager, IT Manager, Security and Safety Manager (FSO), Operations Manager, Maintenance Manager and HR Specialist
  - the MSP lead technician
  - 2 shift superintendents and 10 randomly selected staff (incident reporting and training awareness)
- **Test:**
  - VPN and TOS sign-in tests with and without MFA
  - gate booth sign-in
  - traceroute from an office PC to an RTG HMI
  - a network discovery scan of the gate and yard segment
  - an external port scan
  - a default-credential test on the OCR camera controllers and RTG HMIs
  - USB mount tests on gate servers, a kiosk and HMIs
  - a local log deletion test on a test gate server
  - a check of the crane vendor appliance link over 3 days

## 3. Rules of engagement
- **No testing that could move equipment or disrupt a vessel.** OT tests were read-only (sign-in pages and network reachability). They ran on the night of 2026-08-12, with no vessel at berth, the Maintenance Manager present, and the crane vendor's written approval.
- The discovery scan used a slow rate and excluded PLC addresses supplied by the crane vendor.
- Every default password found was reported to the Maintenance Manager the same night. No settings were changed by the assessor.
- No SSI or personal information left the site. Screenshots were redacted, and the evidence folder is stored as SSI (POL-04).
- The assessor was to stop and notify the IT Manager and FSO on finding an active compromise or an exposure that could cause a TSI. None was found.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 26 |
| Other than satisfied | 129 |
| **Total** | **155** |

**Fully other than satisfied (14 controls):** AC-4, AC-6, AC-17, AT-2, AU-9, CM-6, CP-4, IA-2, IA-2(1), IA-2(2), IR-6, MA-4, MP-7 and RA-5. Most of these had no process or technology at all.

**Partly satisfied (10 controls):** AC-2 (10 of 26 statements; approvals and roles work, removal and reviews do not), SI-2 (3 of 10), IA-5 (3 of 10), CM-7 (2 of 6), SA-9 (2 of 6), SC-7 (2 of 6), CM-8, CP-9, IR-4 and SI-4 (1 each).

**What works:** MFA for TOS and cloud administrators, role-based access in the TOS, the internet firewall and cloud network rules, TOS release testing, continuous TOS database snapshots, and MSP endpoint isolation.

**New findings:**
- Manufacturer default passwords on 2 RTG HMIs and on the web interfaces of the 3 OCR camera controllers (IA-05e., 2026-08-12). These were not known before testing. They were added to the risk register as R-033 and to POAM-009, with the passwords to be changed by 2026-09-30.
- The discovery scan found 41 devices not in the inventory, including a cellular modem on an RTG (CM-08a.01). This is tracked under R-025 and POAM-019.

**POA&M:** all 24 controls have weaknesses, so there are 24 items in `poam.csv`: 9 High (POAM-001 to POAM-008 and POAM-015) and 15 Moderate. As of 2026-09-04, 10 items are in progress and 14 are open.

## 5. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-08-03 | Plan and rules of engagement approved by the General Manager; crane vendor approval for OT tests |
| 2026-08-10 to 2026-08-14 | Fieldwork (OT tests on the night of 2026-08-12) |
| 2026-08-14 | Exit briefing; R-033 added to the risk register |
| 2026-08-24 | Draft results and POA&M |
| 2026-09-04 | Results and POA&M accepted by the General Manager |

Deliverables: `assessment-results.csv` (155 rows), `poam.csv` (24 items) and this plan and summary. The CySO reviews the POA&M monthly, and the General Manager quarterly (P02 CA-7).

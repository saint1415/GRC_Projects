# Security Assessment Plan and Summary: Cris Santos Company | Defense Industrial Base | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts manufacturer, DoD subcontractor) |
| System assessed | CUI Engineering Enclave (CEE), per the SSP (P02) |
| Tier / Vertical | Small / Defense Industrial Base |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (objective labels and determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls, and not the C3PAO that will perform the certification assessment. Escorted by the IT Manager |
| Assessment window | 2026-08-03 to 2026-08-07 (plant walkthrough 2026-08-05) |
| Purpose | Readiness check before the CMMC Level 2 certification assessment; supports SP 800-171 Rev. 2 requirements 3.12.1 and 3.12.2 |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **20 controls, 131 determination statements.** Controls were chosen because they support the High and Very High risks in P01, cover SP 800-171 requirements worth 5 points in the CMMC score, or cover requirements that cannot be on a CMMC POA&M (32 CFR 170.21(a)(2)(iii)).

| Control | SP 800-171 Rev. 2 requirement(s) | Why selected | Depth | Coverage |
|---|---|---|---|---|
| AC-2 | 3.1.1, 3.5.6, 3.9.2 | Account lifecycle; 5-point requirement; R-032 | Focused | Focused (all 64 accounts) |
| AC-17 | 3.1.12 to 3.1.15 | Only remote path into the enclave | Basic | Focused |
| AC-20 | 3.1.20 | Public AI use with CUI; no POA&M allowed; R-014 | Focused | Focused |
| AT-2 | 3.2.1, 3.2.3 | Generic training; R-031 | Basic | Basic (8 users) |
| AU-6 | 3.3.5 | No log review; 5-point requirement; R-016 | Basic | Basic |
| CM-2, CM-7 | 3.4.1, 3.4.6, 3.4.7, 3.4.8 | Baselines and least functionality; 5-point requirements | Focused | Focused (shop-floor VLAN) |
| IA-2, IA-2(1), IA-2(2) | 3.5.1, 3.5.2, 3.5.3 | Shared MES logins, no MFA on MES; R-006 | Focused | Focused (14 MES terminals) |
| IA-5(1) | 3.5.7 to 3.5.10 | Password rules; plaintext DNC credential | Focused | Focused |
| IR-4, IR-6 | 3.6.1, 3.6.2 | DFARS reporting and preservation; R-008, R-009 | Focused | Basic |
| MP-6, MP-7 | 3.8.3, 3.8.7, 3.8.8 | Printed CUI and USB-loaded CNC machines; R-012, R-020 | Basic | Focused (6 cells, 6 machines) |
| PE-3 | 3.10.1, 3.10.3 to 3.10.5 | Visitor escort; no POA&M allowed; R-005 | Basic | Focused (shop floor and engineering wing) |
| RA-5 | 3.11.2, 3.11.3 | No vulnerability scanning; R-013 | Basic | Basic |
| SC-7 | 3.13.1, 3.13.5 | Enclave boundary | Focused | Focused |
| SC-13 | 3.13.11 | FIPS validation on CUI paths; R-004 | Focused | Focused (all 3 external paths) |
| SI-4 | 3.14.6, 3.14.7 | Detection of exfiltration; R-002 | Focused | Basic |

**How this maps to CMMC assessment objectives.** This assessment uses SP 800-53A objectives because the SSP documents SP 800-53 controls and because the 53A statements are finer grained. A C3PAO assesses each SP 800-171 Rev. 2 requirement against its **SP 800-171A (June 2018)** objectives (32 CFR 170.14(d); 170.11(a)), and a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)). The second column above links each control to the SP 800-171 requirements whose 800-171A objectives it covers. The mapping is the author's, based on the SP 800-53 references NIST lists for each SP 800-171 requirement. A result of "Other than satisfied" on any 800-53A statement in a row means the related 800-171 requirement would be scored NOT MET today. Before the C3PAO assessment, the full self-assessment (2026-12-31) will be performed directly against the 800-171A objectives for all 110 requirements.

## 2. Methods and objects
- **Examine:** identity provider and conditional access exports, MES and DNC account tables and configuration files, firewall and cloud network rules, SSP cryptography table and the provider CRM, training roster and module, badge reports and the July 2026 visitor log, recycling bins in 6 cells, USB drives at the 6 legacy machines, EDR alert queue, P08 runbook.
- **Interview:** Vice President of Operations, IT Manager, both Systems Administrators, Manufacturing Systems Engineer, Contracts Manager, HR Manager, Quality Manager, Facilities and Security Coordinator, 6 engineers (AI tool use), and 8 randomly selected enclave users (incident reporting and training).
- **Test:**
  - remote sign-in from an unmanaged laptop (expected block)
  - administrator sign-in with a hardware key; standard user sign-in with MFA
  - sign-in at 3 MES terminals (shared account observed)
  - web category test from an engineering workstation to 4 public AI and file-sharing sites
  - port scan of the shop-floor VLAN, with the Manufacturing Systems Engineer present and outside production hours
  - external port scan of the SFTP gateway
  - visitor escort observation during the walkthrough

## 3. Rules of engagement
- No testing that could disturb production. The shop-floor port scan ran on 2026-08-07 after the last shift, with machines idle, under the Manufacturing Systems Engineer's supervision. No scan touched CNC controllers.
- No CUI left the enclave. The assessor worked from an enclave virtual desktop and a company-issued laptop, and screenshots with drawings were redacted.
- The assessor is a U.S. person, confirmed by the Contracts Manager before access.
- The assessor stopped and told the IT Manager at once about any critical exposure. One was found: two enabled accounts of departed employees (see section 4). They were disabled the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 55 |
| Other than satisfied | 76 |
| **Total** | **131** |

| Control | Satisfied | Other than satisfied |
|---|---|---|
| AC-2 | 14 | 12 |
| AC-17 | 4 | 0 |
| AC-20 | 1 | 2 |
| AT-2 | 3 | 7 |
| AU-6 | 0 | 3 |
| CM-2 | 0 | 5 |
| CM-7 | 3 | 3 |
| IA-2 | 0 | 2 |
| IA-2(1) | 0 | 1 |
| IA-2(2) | 0 | 1 |
| IA-5(1) | 6 | 2 |
| IR-4 | 2 | 11 |
| IR-6 | 1 | 1 |
| MP-6 | 1 | 3 |
| MP-7 | 0 | 2 |
| PE-3 | 9 | 3 |
| RA-5 | 1 | 8 |
| SC-7 | 6 | 0 |
| SC-13 | 1 | 1 |
| SI-4 | 3 | 9 |

**Fully satisfied (2 controls):** AC-17 (remote access only through the virtual desktop gateway) and SC-7 (enclave boundary). These confirm the cloud enclave design works.
**Fully other than satisfied (7 controls):** AU-6, CM-2, IA-2, IA-2(1), IA-2(2), MP-7, and RA-5. The pattern is clear: the cloud side of the enclave is well built, while the **shop-floor side (MES, DNC, USB loading) and the operating processes (log review, scanning, baselines) are missing**.

**New finding:** two enclave accounts of departed employees were still enabled, 19 and 45 days after departure (AC-02f.[04]). This was not known before testing. The assessor told the IT Manager on 2026-08-05, and both accounts were disabled that day. Sign-in logs showed no use after the departure dates. The finding was added to the risk register as R-032 and to POAM-001.

**CMMC implications.** Two weaknesses (AC-20 and PE-3 visitor escort) involve requirements that cannot be on a POA&M for Conditional status (3.1.20, 3.10.3, 3.10.4). POAM-006 and POAM-007 must be closed and verified before the C3PAO assessment.

## 5. POA&M
`poam.csv` holds **20 items: 19 High and 1 Moderate**.
- **16 items from this assessment**, covering the 18 controls with at least one "Other than satisfied" statement (POAM-003 covers IA-2, IA-2(1), and IA-2(2) together).
- **4 items carried from other deliverables:** POAM-017 (DFARS flowdown, P03 G-119), POAM-018 (SPRS score, P03 G-121), POAM-019 (MES and DNC backups, P05), and POAM-020 (outbound deny-by-default, P03 G-093).

The POA&M was created on 2026-08-07 and is reviewed monthly by the Vice President of Operations. It is the SP 800-171 3.12.2 plan of action. It is not a CMMC POA&M: that is set only at the certification assessment and is limited by 32 CFR 170.21.

## 6. Deliverables
`assessment-results.csv` (131 rows), `poam.csv` (20 items), and this plan and summary. The Vice President of Operations accepted the results on 2026-08-31.

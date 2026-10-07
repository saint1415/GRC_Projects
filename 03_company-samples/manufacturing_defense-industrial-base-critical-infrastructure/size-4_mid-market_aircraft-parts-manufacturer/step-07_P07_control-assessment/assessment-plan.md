# Security Assessment Plan and Summary: Cris Santos Company | Defense Industrial Base | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed aircraft parts manufacturer, DoD subcontractor) |
| System assessed | CUI Engineering Enclave (CEE), per the SSP (P02), at both plants and in the cloud |
| Tier / Vertical | Mid-Market / Defense Industrial Base |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (objective labels and determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, 1 OT specialist), reporting to the board audit committee. The firm does not design or operate any assessed control and is not the C3PAO that will perform the certification assessment. The Security Manager coordinated access but did not select samples or rate findings. All assessors are U.S. persons, confirmed by the Director of Trade Compliance and Contracts |
| Assessment window | 2026-08-03 to 2026-08-21 (plant walkthroughs 2026-08-11 to 2026-08-13) |
| Purpose | Independent-style readiness assessment before the CMMC Level 2 certification assessment; supports SP 800-171 Rev. 2 requirements 3.12.1 and 3.12.2 and the annual internal IT audit |
| Results accepted | Chief Operating Officer, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **36 controls, 240 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover SP 800-171 requirements worth 5 points in the CMMC score, or requirements that cannot be on a CMMC POA&M (32 CFR 170.21(a)(2)(iii));
- test whether controls that work in the cloud and at Plant 1 also work at Plant 2;
- support DFARS reporting duties and the SOC 2 readiness work (P09).

| Control | SP 800-171 Rev. 2 requirement(s) | Why selected (risk or gap ID) | Depth | Coverage |
|---|---|---|---|---|
| AC-2, PS-4 | 3.1.1, 3.5.6, 3.9.2 | Account lifecycle; 5-point requirements; R-018 | Focused | Focused (samples of 25) |
| AC-4, AC-20 | 3.1.3, 3.1.20 | AI-003 and AI-001 flows; no POA&M allowed; R-026, R-027 | Focused | Comprehensive (all external flows) |
| AC-6, IA-2 | 3.1.5, 3.5.1, 3.5.2 | Plant 2 shared logins; R-014 | Focused | Focused (terminals at both plants) |
| AC-17 | 3.1.12 to 3.1.15 | Only remote path into the enclave | Basic | Focused |
| AT-2 | 3.2.1, 3.2.3 | Training after the acquisition; R-017 | Basic | Focused (15 staff) |
| AU-2, AU-6, AU-11, SI-4 | 3.3.1, 3.3.5, 3.14.6, 3.14.7 | Shop-floor monitoring; 5-point requirements; R-005; DFARS 252.204-7012(e) | Focused | Focused |
| CA-2 | 3.12.1 | SPRS score accuracy; R-003 | Focused | Comprehensive (2025 assessment) |
| CM-2, CM-3, CM-6 | 3.4.1 to 3.4.4 | OT baselines and change control; R-020 | Focused | Focused (10 cloud servers; all 6 MES and DNC servers) |
| CM-7 | 3.4.6 to 3.4.8 | Plant 2 exposed services; R-004 | Focused | Comprehensive (Plant 2 network) |
| CM-8 | 3.4.1 | Scope and inventory; P03 G-127 | Focused | Comprehensive (8 cells, additive area) |
| CP-2, CP-4, CP-9 | 3.8.9 | Recovery of High processes; R-011, R-012 | Comprehensive | Comprehensive |
| IA-2(1), IA-5 | 3.5.3, 3.5.7 to 3.5.10 | Privileged access to shop-floor servers; credentials | Focused | Focused (12 OT devices; 2 servers) |
| IR-4, IR-6 | 3.6.1, 3.6.2 | DoD reporting and preservation; R-008, R-009 | Focused | Focused (10 of 14 incidents) |
| MA-4 | 3.7.5 | Vendor remote access; R-016 | Focused | Comprehensive (all vendor paths) |
| MP-6, MP-7 | 3.8.3, 3.8.7, 3.8.8 | Printed CUI and USB loading; R-015, R-019 | Basic | Focused (8 cells, 8 machines) |
| PE-3 | 3.10.1, 3.10.3 to 3.10.5 | Visitors; no POA&M allowed; R-006 | Basic | Focused (both plants) |
| RA-5, SI-2 | 3.11.2, 3.11.3, 3.14.1 | Scanning and patching; R-013 | Focused | Focused (30 findings) |
| SA-9, SR-6 | ESP and supplier duties | MSSP CRM; supplier status; R-010, R-033 | Focused | Comprehensive (22 suppliers) |
| SC-7 | 3.13.1, 3.13.6 | Plant 2 boundary; R-004 | Focused | Focused |
| SC-13, SC-28 | 3.13.11, 3.13.16 | FIPS validation and encryption at rest; R-007 | Focused | Comprehensive (all CUI paths) |

**How this maps to CMMC assessment objectives.** This assessment uses SP 800-53A objectives because the SSP documents SP 800-53 controls and because the 53A statements are finer grained. A C3PAO assesses each SP 800-171 Rev. 2 requirement against its **SP 800-171A (June 2018)** objectives (32 CFR 170.14(d); 170.11(a)), and a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)). The second column above links each control to the SP 800-171 requirements whose 800-171A objectives it covers. The mapping is the author's, based on the SP 800-53 references NIST lists for each SP 800-171 requirement. Before the C3PAO assessment, the full self-assessment (2026-12-31) and the readiness re-check (2027-02) are performed directly against the 800-171A objectives for all 110 requirements.

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year at moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items; small populations were tested in full. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 41 | 25 | AC-2 |
| New hires with enclave accounts | 71 | 25 | AC-2 |
| Privileged accounts | 12 | 12 | AC-2, IA-2(1) |
| Local accounts on Plant 2 servers | 9 | 9 | AC-2 |
| MES and DNC servers (both plants) | 6 | 6 | CM-2, CM-6, IA-2(1), SI-2 |
| Cloud servers for benchmark scans | 38 | 10 | CM-6 |
| Change tickets (2026 Q2) | 164 | 20 | CM-3 |
| OT devices for default-credential test | about 120 | 12 | IA-5 |
| Backup job days (July 2026) | 31 | 31 | CP-9 |
| Incidents (12 months) | 14 | 10 | IR-4 |
| Critical and High vulnerability findings (Q1-Q2 2026) | 74 | 30 | RA-5, SI-2 |
| Suppliers that receive CUI | 22 | 22 | SR-6 |
| Staff for reporting and training interviews | 850 | 15 (8 Plant 1, 7 Plant 2) | IR-6, AT-2 |
| July 2026 visits recorded on gate cameras | 69 (31 Plant 1, 38 Plant 2) | 69 | PE-3 |
| Cells for printed CUI walkthrough | 14 | 8 (3 Plant 1, 5 Plant 2) | MP-6 |

## 3. Methods and objects
- **Examine:** policies (2024 set and drafts of the 2026 set), SSP v3.0 and the v3.9 draft, the 2025 self-assessment and SPRS record, identity provider and MES exports, firewall and cloud network rules, the cryptographic module table and provider CRM, backup and scan reports, change tickets, incident records, supplier files, visitor logs and camera records, training records, the MSSP contract.
- **Interview:** COO, vCISO, IT Director, Security Manager, both security analysts, GRC analyst, Manufacturing Systems Manager and the Plant 2 manufacturing systems engineer, Director of Trade Compliance and Contracts, Director of Supply Chain, HR Director, Director of Quality, Facilities and Security Manager, both plant managers, the MSSP service lead, and 15 randomly selected staff.
- **Test:**
  - remote sign-in from an unmanaged laptop (expected block)
  - sign-in at 4 MES terminals (2 per plant) and as local administrator on 2 MES servers
  - web category tests from 2 engineering workstations to 6 public AI and file-sharing sites
  - traffic capture of the AI-003 gateway (2026-07-22, shared with P03)
  - port scan of the Plant 2 network after the last shift (2026-08-13), with the Manufacturing Systems Manager present
  - default-credential test on 12 OT devices, with the device owner present and machines idle
  - a simulated impossible-travel sign-in to test MSSP escalation
  - visitor escort observation during the walkthroughs

## 4. Rules of engagement
- No testing that could disturb production or safety. Scans of shop-floor networks ran after the last shift with machines idle; no scan touched CNC, additive, or test stand controllers. Credential tests used operator panels only, with the owner present.
- No CUI left the enclave. Assessors worked from enclave virtual desktops and company-issued laptops, and screenshots with drawings were redacted.
- **Stop-and-notify rule: used once.** On 2026-08-12 the assessors found an active local administrator account of the prior owner's IT contractor on the Plant 2 MES server, with remote desktop open. They told the Security Manager and the vCISO the same hour. The account was disabled that day; available logs showed no use after 2025-02, but Plant 2 logs are kept only 30 days locally, so earlier use cannot be ruled out. The company logged it as P01 R-050 on 2026-08-14 and referred it to the incident process, which found no evidence that CUI was accessed and recorded the reasoning in the incident log.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 138 |
| Other than satisfied | 102 |
| **Total** | **240** |

Other than satisfied statements by risk: 95 High, 7 Moderate.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 19 | 7 | High | POAM-001 |
| AC-4 | 0 | 1 | High | POAM-002 |
| AC-6 | 0 | 1 | High | POAM-003 |
| AC-17 | 4 | 0 | n/a | n/a |
| AC-20 | 1 | 2 | High | POAM-002 |
| AT-2 | 8 | 2 | Moderate | POAM-005 |
| AU-2 | 4 | 2 | High | POAM-006 |
| AU-6 | 1 | 2 | High | POAM-006 |
| AU-11 | 1 | 0 | n/a | n/a |
| CA-2 | 8 | 3 | High | POAM-007 |
| CM-2 | 2 | 3 | High | POAM-008 |
| CM-3 | 7 | 3 | High | POAM-008 |
| CM-6 | 3 | 3 | High | POAM-008 |
| CM-7 | 4 | 2 | High | POAM-009 |
| CM-8 | 3 | 3 | Moderate | POAM-010 |
| CP-2 | 7 | 17 | High | POAM-011 |
| CP-4 | 2 | 3 | High | POAM-011 |
| CP-9 | 2 | 4 | High | POAM-012 |
| IA-2 | 1 | 1 | High | POAM-003 |
| IA-2(1) | 0 | 1 | High | POAM-004 |
| IA-5 | 7 | 3 | High | POAM-004 |
| IR-4 | 9 | 4 | High | POAM-013 |
| IR-6 | 1 | 1 | High | POAM-013 |
| MA-4 | 2 | 6 | High | POAM-014 |
| MP-6 | 3 | 1 | High | POAM-015 |
| MP-7 | 0 | 2 | High | POAM-015 |
| PE-3 | 8 | 4 | High | POAM-016 |
| PS-4 | 3 | 2 | High | POAM-001 |
| RA-5 | 6 | 3 | High | POAM-017 |
| SA-9 | 4 | 2 | Moderate | POAM-018 |
| SC-7 | 3 | 3 | High | POAM-019 |
| SC-13 | 1 | 1 | High | POAM-020 |
| SC-28 | 0 | 1 | High | POAM-020 |
| SI-2 | 7 | 3 | High | POAM-017 |
| SI-4 | 7 | 5 | High | POAM-006 |
| SR-6 | 0 | 1 | High | POAM-018 |

**Fully satisfied (2 controls):** AC-17 (remote access only through the gateway; the unmanaged laptop was blocked) and AU-11 (1 year searchable, 6 years archived). Many other controls passed every statement that concerned the cloud or Plant 1: the MSSP escalated the test alert in 18 minutes, backups ran 31 of 31 days, and all 12 public AI and file-sharing tests were blocked.

**Fully other than satisfied (6 controls):** AC-4, AC-6, IA-2(1), MP-7, SC-28, and SR-6.

**Themes:**
1. **The program works where it was built.** The cloud enclave and Plant 1 pass most statements. Plant 2, acquired in 2024, accounts for most other-than-satisfied statements: identity, boundary, backups, visitors, printed CUI, USB media, vendor access, and encryption.
2. **The shop floor is outside the security operations loop at both plants.** MES, DNC, and OT are not logged, scanned, baselined, or under change control (AU-2, AU-6, SI-4, RA-5, CM-2, CM-3, CM-6).
3. **Recovery is unproven** (CP-2, CP-4, CP-9).
4. **Third parties and AI tools created new paths** that nobody reviewed: the AI-003 telemetry flow, the AI-001 pilot, the additive printer vendor's remote tool, and suppliers with unverified status (AC-4, AC-20, MA-4, SR-6).

**CMMC implications.** Weaknesses under AC-20 (3.1.20) and PE-3 (3.10.3, 3.10.4) involve requirements that cannot be on a POA&M for Conditional status. POAM-002 and POAM-016 must be closed and verified before the C3PAO assessment.

## 6. POA&M
`poam.csv` holds **24 items: 21 High and 3 Moderate**.
- **20 items from this assessment** (POAM-001 to POAM-020), covering the 34 controls with at least one Other than satisfied statement. Related controls share an item.
- **4 items carried from other deliverables:** POAM-021 (SPRS score, P03 G-121), POAM-022 (supplier flowdown and DFARS 252.204-7021 templates, P03 G-119 and G-126), POAM-023 (AI conditions, P10), and POAM-024 (SOC 2 readiness gaps, P09).

The POA&M is reviewed monthly by the COO and quarterly by the audit committee. It is the SP 800-171 3.12.2 plan of action. It is not a CMMC POA&M: that is set only at the certification assessment and is limited by 32 CFR 170.21.

## 7. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-14 | Plant walkthroughs (2026-08-11 to 2026-08-13) and technical tests |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the audit committee |
| 2027-02 | Readiness re-check of POA&M items before the C3PAO assessment |

Deliverables: this plan and summary; `assessment-results.csv` (240 rows); `poam.csv` (24 items).

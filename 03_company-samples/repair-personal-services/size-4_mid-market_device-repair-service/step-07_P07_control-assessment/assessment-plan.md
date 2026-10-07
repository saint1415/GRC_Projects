# Security Assessment Plan and Summary: Cris Santos Company | Other Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional electronics and device repair chain) |
| System assessed | Service Ticketing and Point-of-Sale Platform (STPP: SYS-01, SYS-03 to SYS-07, SYS-09 to SYS-11), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Other Services (except Public Administration) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 2 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control. The GRC Analyst coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (site visits 2026-08-10 to 2026-08-13; checkout page capture and store network tests 2026-08-12) |
| Also supports | Evidence for the 2026 SAQ P2PE and SAQ A attestations; the Manufacturer A audit evidence pack; SOC 2 readiness (P09) |
| Results accepted | Chief Operating Officer, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **36 controls, 255 determination statements.** Controls were selected because they:
- address the High risks and most Moderate risks in the risk register (P01);
- cover the High gaps in the gap analysis (P03), including the FTC Act, Fla. Stat. 501.171, and PCI DSS rows;
- support inherited-control reliance, the SAQ attestations, and SOC 2 readiness for the partner claims service (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Leaver and local account gaps; R-014, R-015; G-016, G-145 | Focused | Focused (samples of 25) |
| AC-3, SI-12 | Legacy credential notes and retention; R-002, R-005, R-023; G-037, G-110, G-116 | Comprehensive | Comprehensive (full-population searches and listings) |
| AC-6, AU-12, MP-7 | Technician access to customer devices; R-001; G-057, G-063 | Comprehensive | Focused (30 bench PCs at 8 stores and the Depot; all 11 privileged accounts) |
| AC-17 | Vendor remote access; G-078 | Basic | Focused (6 of 31 sessions) |
| AT-2 | Training, including payment terminals; G-059, G-131 | Basic | Focused (20 interviews) |
| AU-2, AU-6, SI-4 | Visibility of exports, the lab, and the checkout page; R-004, R-018; G-068, G-075, G-077 | Focused | Focused |
| CM-2, CM-3, CM-6 | Configuration and change; R-012, R-040 | Focused | Focused (10 application and 10 infrastructure changes; 8 stores) |
| CM-8 | Inventories, terminals, checkout scripts; R-004, R-009; G-128, G-143 | Focused | Comprehensive for terminals; focused for endpoints |
| CP-2, CP-4, CP-9, CP-10 | Contingency and recovery; R-003, R-006, R-011; G-050, G-064, G-101 | Comprehensive | Comprehensive |
| IA-2, IA-2(1), IA-5 | Identity, MFA, authenticators; G-055 | Focused | Comprehensive for privileged accounts |
| IR-4, IR-6, IR-8 | Incident capability and notice clocks; R-017; G-050, G-112, G-141 | Focused | Focused (10 of 41 incidents) |
| MP-6 | Sanitization; R-008; G-038, G-116 | Focused | Focused (50 devices) |
| PE-3 | Facilities, keys, and terminal inspections; R-009, R-037; G-127, G-129 | Basic | Comprehensive for inspection logs |
| PS-6 | Confidentiality agreements; Manufacturer A terms | Basic | Focused (35 people) |
| RA-3, RA-5, SI-2 | Risk assessment and vulnerability management; R-019, R-041 | Focused | Focused (40 Critical findings) |
| SA-9, SA-11 | Vendors and secure development; R-012, R-025; G-026, G-070 | Focused | Comprehensive for vendors with customer data |
| SC-7, SC-28 | Segmentation and encryption at rest; R-005, R-007; G-061, G-071 | Focused | Focused (3 stores tested) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 286 | 25 | AC-2, PS-4 |
| Transfers | 74 | 25 | AC-2 |
| New SYS-01 accounts | 312 | 25 | AC-2 |
| New hires | 301 | 25 (plus 10 existing technicians) | PS-6 |
| Privileged accounts | 11 | 11 | IA-2(1), AC-6 |
| Bench workstations | 238 | 30 (8 stores and the Depot) | AC-6, AU-12, MP-7, SC-28, SI-2 |
| Office endpoints | 260 | 25 | SC-28, SI-2 |
| Critical vulnerability findings (Q1-Q2 2026) | 162 | 40 | RA-5, SI-2 |
| Application pull requests / infrastructure changes (2026 H1) | 214 / 58 | 10 / 10 | CM-3 |
| Vendor remote sessions (2026 H1) | 31 | 6 | AC-17 |
| Incidents (2025-07 to 2026-06) | 41 | 10 | IR-4, IR-6 |
| Customer complaints alleging device access | 23 | 10 | IR-4, IR-6 |
| Recycling devices (re-performed from P03) | about 1,750 a month | 20 Depot, 30 stores | MP-6 |
| Payment terminal inspection logs | 34 stores x 8 weeks | All | PE-3 |
| Vendors with customer data | 26 | 26 | SA-9 |
| Backup job days (July 2026) | 31 | 31 | CP-9 |
| Staff for reporting-awareness interviews | 600 | 20 | IR-6, AT-2 |
| Stores for walkthroughs | 34 | 8 (2 per region) | PE-3, SC-7, CM-6, CM-8 |

## 3. Methods and objects
- **Examine:**
  - the 2024 policies and the 2026 drafts; the SSP draft; standards drafts;
  - identity provider, SYS-01, manufacturer portal, contact center, and cloud exports;
  - backup, patch, scan, EDR, and SIEM reports;
  - contracts and vendor files; the incident queue and the Store 17 case file;
  - sanitization certificates and recycler certificates; terminal lists and inspection logs;
  - the pipeline definition, pull requests, and the 2026-05 penetration test report.
- **Interview:**
  - vCISO, IT Director, Security Manager, GRC Analyst, Digital Engineering Manager;
  - Privacy and Compliance Manager, Director of Retail Operations, Depot Director, Data Recovery Manager;
  - HR Director, Director of Partner Programs, Director of Customer Experience, the MSSP service lead;
  - 20 randomly selected staff (technicians, advisors, agents).
- **Test:**
  - MFA sign-in tests on all 11 privileged accounts;
  - USB and phone connection tests on 30 bench PCs (with a test phone holding dummy data);
  - SYS-01 test sign-ins for each role to confirm what notes and fields are visible;
  - reachability tests from bench networks at 3 stores (Stores 03, 09, and 21);
  - default-credential checks on CCTV recorders and network devices at 8 stores;
  - a browser capture of the mail-in checkout page with script inventory (2026-08-12);
  - restores of one lab folder and one database snapshot from the backup account into an isolated account;
  - a 2-week review of SYS-01 audit events exported by the vendor.

## 4. Rules of engagement
- No testing on customer devices. USB and pairing tests used the assessors' test phone with dummy data.
- No customer data left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system.
- No changes to the checkout page or terminals. The page capture was read-only, from a browser outside the company network.
- Stop-and-notify rule: any critical exposure is reported to the IT Director and the vCISO the same day. **Used once:** on 2026-08-12 the assessors reported vendor default administrator passwords on CCTV recorders at 5 of 8 visited stores, reachable from the store network. The company logged the finding as P01 R-048 on 2026-08-14 and changed the 5 passwords by 2026-08-21.
- The 3 SYS-01 users with more than 500 ticket views in a day (AU-6 test) were referred to the Security Manager and the Privacy and Compliance Manager under POL-03, not investigated by the assessors.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 138 |
| Other than satisfied | 117 |
| **Total** | **255** |

Other than satisfied statements by risk: 29 High, 64 Moderate, 24 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 19 | 7 | Moderate | POAM-001; POAM-003 |
| AC-3 | 0 | 1 | High | POAM-015 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | Moderate | POAM-018 |
| AT-2 | 8 | 2 | Low | POAM-017 |
| AU-2 | 2 | 4 | High | POAM-003 |
| AU-6 | 1 | 2 | High | POAM-003 |
| AU-12 | 1 | 2 | High | POAM-002 |
| CM-2 | 2 | 3 | Moderate | POAM-016 |
| CM-3 | 6 | 4 | Moderate | POAM-008 |
| CM-6 | 2 | 4 | Moderate | POAM-014; POAM-016 |
| CM-8 | 3 | 3 | High | POAM-011; POAM-012 |
| CP-2 | 1 | 23 | High | POAM-007 |
| CP-4 | 0 | 5 | High | POAM-007 |
| CP-9 | 6 | 0 | n/a | n/a |
| CP-10 | 0 | 2 | High | POAM-007 |
| IA-2 | 2 | 0 | n/a | n/a |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 8 | 2 | Moderate | POAM-008; POAM-014 |
| IR-4 | 6 | 7 | High | POAM-010 |
| IR-6 | 0 | 2 | High | POAM-010 |
| IR-8 | 12 | 5 | Moderate | POAM-010 |
| MP-6 | 1 | 3 | High | POAM-005 |
| MP-7 | 0 | 2 | High | POAM-002 |
| PE-3 | 8 | 4 | Moderate | POAM-011 |
| PS-4 | 2 | 3 | Moderate | POAM-001 |
| PS-6 | 4 | 0 | n/a | n/a |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 7 | 2 | Moderate | POAM-013 |
| SA-9 | 3 | 3 | Moderate | POAM-009 |
| SA-11 | 4 | 5 | Moderate | POAM-008 |
| SC-7 | 4 | 2 | Moderate | POAM-006 |
| SC-28 | 0 | 1 | High | POAM-019 |
| SI-2 | 7 | 3 | Moderate | POAM-013 |
| SI-4 | 8 | 4 | High | POAM-002; POAM-003; POAM-012 |
| SI-12 | 0 | 4 | High | POAM-004; POAM-015 |

The Risk column shows the highest rating among each control's Other than satisfied statements.

**Fully satisfied (5 controls):** CP-9 (encrypted, write-once backups in a separate account and region; both test restores succeeded), IA-2 and IA-2(1) (unique identities; MFA on all 11 privileged accounts), PS-6 (confidentiality agreements signed before access in every sample), and RA-3. These confirm the strengths in the scenario facts.

**Fully other than satisfied (8 controls):** AC-3, AC-6, CP-4, CP-10, IR-6, MP-7, SC-28, and SI-12. CP-2 is close behind (23 of 24).

**Themes:**
1. **The designs are right; the legacy estate is not on them.** Every bench-control finding (AC-6, AU-12, MP-7, SI-4 local connections) sits on the 48 legacy-image PCs at 14 stores. The standard image passed the same tests.
2. **Old data is the largest exposure.** AC-3 and SI-12 failed on data the current process no longer creates: legacy credential notes, recovered data past retention, and records since 2016.
3. **The company protects backups well but has not proven recovery** (CP-9 satisfied; CP-2, CP-4, CP-10 not).
4. **Visibility stops at SaaS and the web page.** SYS-01 exports and the checkout page are blind spots (AU-2, AU-6, SI-4, CM-8).

**POA&M:** 31 controls had at least one Other than satisfied statement. They map to 19 POA&M items (POAM-001 to POAM-019), because related controls share an item. Six more items come from the gap analysis, the SOC 2 readiness assessment, and the AI assessment (POAM-020 intake notice and AI claim, POAM-021 HIPAA screen, POAM-022 AI governance, POAM-023 SOC 2 readiness, POAM-024 partner duties, POAM-025 Manufacturer A audit). The total is 25 items: 13 High, 11 Moderate, and 1 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Site visits and technical tests |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (255 rows); `poam.csv` (25 items).

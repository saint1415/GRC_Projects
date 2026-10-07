# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-10 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for remote and privileged access, no always-on vendor tools, one severity scale, regulated retention periods | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, OT security standard (SP 800-82 Rev. 3 based), Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and operation-specific standards (for example freeze-night operation, food defense cyber scenarios, card data, portal release gate) | Division president, after Group CISO alignment review |
| Division procedures | ROC, plant, and branch runbooks | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Crop Farming | v2026-09 (replaces v2023) | 2026-09-08 | **Re-issued** after the 2026 assessment. The v2023 supplement had no OT remote access, OT change control, or seasonal account rules (section 4) | Train ROC staff, farm technicians, and crew leads before the 2026-27 season (by 2026-11-30) |
| Food Processing | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; adds cyber scenarios to food defense and control changes to management of change in 2026-09 | Confirm alignment with the final policies by 2026-12-30 |
| Farm Supply | v2025, amended 2026-09 | 2025-11; amendment 2026-09-08 | Aligned for card data. The 2026-09 amendment adds the portal release gate that the AI prescription launch skipped | Attest by 2026-12-31 |

## 3. What each supplement adds
### 3.1 Crop Farming supplement (focus division; no binding cybersecurity rule; CSF 2.0 benchmark)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| OT remote access | Integrator and vendor sessions only through group PAM to the ROC jump host, on a ticket, for a set window; remote tools removed from all farm servers | POL-02 4.7 | SP 800-82r3 6.2.10 |
| OT network paths | No connection from the farm data hub or any cloud workload into ROC networks; all flows end in the OT DMZ | POL-02 4.12 | SP 800-82r3 5.2.3 |
| OT change control | Every change to PLC logic, irrigation setpoints, fertigation rates or limits, and freeze triggers, including changes made in the FMIS irrigation module, needs a ticket, ROC lead approval, and a weekly review | POL-01 4.9; POL-05 4.4 | SP 800-82r3 6.2.4 |
| Safe states | Pumps and pivots stop and fertigation valves close on loss of control at every farm; settings verified each season | POL-01 4.9 | SP 800-82r3 Appendix F (CP-12, SC-24) |
| Freeze nights | Written manual start procedure at every ROC-1 farm, drilled each November with ROC and farm crews | POL-03 4.3 | SP 800-82r3 3.3.9 |
| Seasonal accounts | Named crew lead accounts with tablet PINs; FMIS crew accounts disabled on the HR season-end date; stale account report each month in season | POL-02 4.1, 4.5 | 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1) |
| Tally integrity | Tally locked after supervisor approval; edits versioned with reason; weekly reconciliation with payroll exports | POL-04 4.6 | 20 CFR 655.122(j)(1), (k) |
| Farm records | Monthly export of Produce Safety, application, tally, and harvest lot records to the group vault; retention per POL-04 4.5 | POL-04 4.5 | 21 CFR 112.164; 40 CFR 170.311(b)(6); 20 CFR 655.122(j)(4) |
| Harvest lot handoff | Signed lot manifest with every load; buyer notice within 24 hours of an event affecting safety, traceability, or volumes | POL-03 4.4, 4.8 | Buyer agreements |
| Default credentials | Modems, gateways, and controllers re-credentialed before connection; quarterly credential scan | POL-02 4.8 | SP 800-82r3 6.2.1 |
| Drones | Remote pilots hold the FAA certificates their operation requires (Part 107 for imaging; Part 137 for agricultural aircraft operations with spray drones); fleet accounts through SYS-G1 with MFA | POL-02 4.3 | 14 CFR 107.1; 14 CFR 137.1 |
| Acquired farms | OT review before closing; integration to group access, monitoring, and change rules within 180 days | POL-01 4.7 | CSF 2.0 GV.SC-06 (benchmark) |

### 3.2 Food Processing supplement (registered food facilities; N11-R01 applies)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Food defense cyber scenarios | Vulnerability assessments consider an attacker or insider changing setpoints, recipes, dosing, or monitoring records through control systems; reanalysis when new vulnerability information arrives | POL-01 4.3 | N11-R01 (21 CFR 121.130(a)-(b); 121.157(b)(2)) |
| Control changes at actionable process steps | Setpoint and recipe changes logged under named accounts and checked against approved values each shift | POL-05 4.4 | N11-R01 (21 CFR 121.135); 21 CFR 117.126(b) |
| Records integrity | Historian data used as monitoring records locked after the shift; edits versioned | POL-04 4.6 | 21 CFR 117.305; 121.305 |
| Ammonia refrigeration | Contractor sessions approved per session and reviewed weekly; control logic and setpoint changes go through management of change | POL-02 4.7; POL-01 4.9 | 29 CFR 1910.119(l) |
| Release reporting | Incident runbook includes the release reporting decision for ammonia (P08 matrix) | POL-03 4.4 | 40 CFR 302.6; 40 CFR 355.40-355.42 |
| Records under outage | 24-hour records drill each quarter with the traceability system offline; printed food safety and food defense plans at every facility | POL-04 4.5 | 21 CFR 1.361; 117.315(c); 121.315(c) |
| Federal contracts | Requirements of FAR 52.204-21 mapped to group controls; covered telecommunications and Kaspersky reporting steps in the matrix | POL-01 4.6 | N42-R04; N42-R05; 48 CFR 52.204-23 |
| Customer notices | Retail and foodservice 24-hour notice in the matrix | POL-03 4.4 | Customer agreements |

### 3.3 Farm Supply supplement (PCI DSS by contract; portal service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Card data environment | Segmentation tested yearly; point-to-point encryption at all branches by 2027-03-31; payment page script controls on e-commerce | POL-02 4.12 | PCI DSS (contract) |
| Portal release gate | Security review, data-use review, and agronomic validation for every feature that changes how grower data is used or how prescriptions are produced | POL-01 4.13; POL-04 4.7 | N42-R01 (FTC Act Section 5); portal terms |
| Cooperative notices | Incident notice register with each cooperative's contact; notice within 72 hours as the terms commit | POL-03 4.4 | Portal terms |
| Cooperative administrators | MFA required for cooperative administrators | POL-02 4.11 | N42-R01 |
| Grower credit files | Access limited to credit staff; bulk access alerts; Social Security numbers masked in branch views | POL-04 4.2 | Fla. Stat. 501.171(2) (worked example) |
| Blending plants | Recipe changes logged and checked against approved formulas each batch | POL-05 4.4 | SP 800-82r3 6.2.4 |

## 4. Crop Farming: what the v2023 supplement missed
The v2023 supplement was written for division IT before the 2024 farm acquisitions. Group policy already required most of what follows, but staff at ROCs and farms worked from the supplement, so the gaps were real (P01 GR-04; P07 findings).

| Topic | Crop Farming supplement (v2023) | Group policy and the v2026-09 supplement | Effect |
|---|---|---|---|
| Vendor remote access | Not addressed for OT | Only through group PAM; no always-on tools (POL-02 4.7) | Integrator always-on access at 14 farms (CF-001; POAM-001) |
| OT network paths | Not addressed | No direct paths into OT (POL-02 4.12) | Hub to ROC path (CF-004; POAM-002) |
| OT changes | Change tickets for servers only | All logic, setpoint, and limit changes controlled (POL-01 4.9) | Uncontrolled changes at acquired farms (CF-005; POAM-011) |
| Seasonal access | Farm offices remove accounts "when practical" | Disabled on the season-end date (POL-02 4.5) | 1,140 stale accounts (CF-007; POAM-005) |
| Shared logins | Crew logins allowed | Named accounts only (POL-02 4.1) | Unattributable records (CF-006) |
| Common control inheritance | Not addressed | Documented per system including OT (POL-01 4.6) | Scenario gap 2 (POAM-009) |

**Why it happened.** The supplement had an owner but no review trigger tied to acquisitions. **Fix:** POL-01 4.7 now requires a security review before any acquisition and integration within 180 days, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations under the 2026 policies are due 2026-12-31 for all three divisions.

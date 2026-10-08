# Regulatory Gap Analysis: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (precision-agriculture row crop and watermelon farm, NAICS 111998) |
| Tier / Vertical | Micro / Agriculture, Forestry, Fishing and Hunting |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, **as a voluntary benchmark**. NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security (September 2023), applied to the pump station and pivots |
| Binding rules assessed row by row | FDA Produce Safety Rule record requirements, 21 CFR Part 112, Subpart O; H-2A earnings records, 20 CFR 655.122(j); Florida data security, disposal, and breach notice, Fla. Stat. 501.171 (2026 statutes); 21 CFR Part 121 (N11-R01), found not applicable |
| Assessment dates | 2026-07-20 to 2026-07-31 |
| Assessor | Office Manager (Security Coordinator) with the MSP technician, the Irrigation and Equipment Technician, and the Field Supervisor |
| Approved | 2026-08-31 by the Owner and General Manager |
| Workbook | `gap-analysis.csv` (123 rows) |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv). This section restates the result for the rules analyzed here, with the facts behind it: the farm only grows and harvests (EV-024), sells nearly all its food to a packer-shipper and a buying point (EV-028), holds no federal procurement contract (EV-027), and flies a camera drone only (EV-035).

**Step 1 was to find the rule that binds the farm. None of the candidates is a cybersecurity rule that applies to this farm.**

| Candidate | Applies? | Why (citation) |
|---|---|---|
| FSMA intentional adulteration rule, 21 CFR Part 121 (vertical requirement **N11-R01**) | **No** | Part 121 applies to a food facility "required to register under section 415" of the FD&C Act (21 CFR 121.1). Farms do not have to register (21 CFR 1.226(b)). The farm only grows and harvests its own crops; the packer-shipper, buying point, and gin do the packing and handling. Part 121 is also a food defense rule, not an IT security rule |
| Reportable Food Registry, 21 U.S.C. 350f(d) | **No** | The duty falls on a "responsible party," the person who registers a food facility (350f(a)(1)). The farm registers none. It stays in the P08 matrix as a buyer-coordination item |
| CIRCIA, 6 U.S.C. 681-681g; proposed 6 CFR Part 226 | **No (proposed, and would not cover the farm as proposed)** | No final rule as of 2026-09-25. As proposed, food and agriculture entities would be covered only above the SBA size standard; the farm is under the $2.5 million standard for NAICS 111998 (13 CFR 121.201) |
| FAA drone rules, 14 CFR Part 107 and Part 137 | Part 107 yes (not a cybersecurity rule); Part 137 no | The drone is flown by a certificated remote pilot (14 CFR 107.12). Part 137 governs agricultural aircraft operations that dispense substances (14 CFR 137.1, 137.3); the farm's drone only takes pictures |
| SEC cybersecurity disclosure rules | No | Privately held |
| FAR 52.204-21 and 52.204-25 | No | No federal contracts or subcontracts. The NRCS conservation contract is a cost-share agreement, not a procurement contract |
| FTC Act Section 5 | Background only | Applies to any security or privacy promise the farm makes. The farm makes none to the public today. Not decomposed into rows |

**Decision: use NIST CSF 2.0 as the benchmark, with SP 800-82 Rev. 3 for OT.** This follows the vertical profile: primary agricultural production has no binding federal cybersecurity regulation, and CSF 2.0 is the sector-neutral baseline. SP 800-82 Rev. 3 predates CSF 2.0 and was written against CSF 1.1, so its OT guidance is applied here to the matching CSF 2.0 subcategories as an author mapping (column `ot_application_sp800_82r3`). Neither document is binding. Status ratings measure the farm against a voluntary Target Profile, not a legal duty.

**Binding rules that reach the farm's data, assessed row by row:**
- **Produce Safety Rule records (21 CFR 112 Subpart O).** The farm is a covered farm for its watermelons: its average annual produce sales over the prior 3 years exceed the $25,000 threshold, adjusted for inflation (21 CFR 112.4(a)). Peanuts are not covered produce, because they are on the exhaustive "rarely consumed raw" list (112.2(a)(1)). The farm is not eligible for the qualified exemption, because it sells almost all of its food to a packer-shipper and a buying point rather than to qualified end-users (112.5(a)(1)). Subpart O requires records that include specified content and are created at the time of the activity, accurate, legible, and indelible (112.161(a)(1)-(3)), signed or initialed by the person who did the work (112.161(a)(4)), kept at least 2 years (112.164(a)(1)), and produced for FDA within 24 hours when kept off site (112.166(a)). Only the record requirements were assessed; the Rule's growing standards are outside a cybersecurity gap analysis.
- **H-2A earnings records (20 CFR 655.122(j)).** The farm employs 2 H-2A workers from February to July. Daily hours offered and worked and start and end times in SYS-01 are part of the earnings record.
- **Fla. Stat. 501.171.** The farm is a "covered entity" (a commercial entity that maintains personal information). The statute requires reasonable security measures (subsection (2)), breach notices ((3) to (6)), and disposal of customer records (8). Its definition of personal information includes passport numbers and geolocation (501.171(1)(g)1.a.(II) and (VII)), which reach the H-2A files and the operator location history in the telematics portal.

**Also considered, not analyzed row by row:** the FDA Food Traceability Rule (21 CFR Part 1, Subpart S). It exempts produce farms that are not covered farms under Part 112 (21 CFR 1.1305(a)(1)), and this farm is a covered farm. Whether the rule reaches the farm's watermelon harvest records, and its current compliance date, were not verified in this engagement. The question is carried to the July 2027 review.

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcome text come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). Regulation rows cite the eCFR text current as of 2026-09-23 and the 2026 Florida Statutes, with short quotes or paraphrases.
2. **Target Profile.** Each subcategory has a priority for the farm's CSF Target Profile (High 25, Medium 44, Low 37), set by the Office Manager and the Owner and General Manager from the risk register (P01) and BIA (P05).
3. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (CSF 2.0 to SP 800-53 Rev. 5.2.0, SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`. The `sp800_53_controls` column is a key-control subset chosen by the author. Regulation rows use an author mapping (no official NIST mapping exists).
4. **Documentary evidence.** Each status rests on a named document or record from intake (2026-07-06 to 2026-07-17): the payroll roster and H-2A case file (EV-001, EV-002), the SYS-01 user and role lists, settings and terms (EV-003 to EV-006), the productivity suite user export and sharing report (EV-007, EV-008), the MSP's device, policy, encryption, monthly, antivirus, firewall and backup reports and tickets (EV-009 to EV-016), the contract folder, dealer records, telematics portal and AI vendor terms (EV-017 to EV-024), the training records, HR checklists and document request (EV-030 to EV-032), and the Home Farm walk-through (EV-034). Fieldwork added the account comparison of 2026-07-21 and the determination of 2026-07-24 (EV-042, EV-043), interviews with all 5 year-round staff, the MSP technician, and the irrigation dealer (EV-044), a walkthrough of the shop, pump station, and River Tract on 2026-07-22 (EV-045), a SYS-01 access and export test (EV-046), a sample of 20 Produce Safety records and 10 daily hours entries (EV-047), a contract folder review (EV-048), and a personnel file sample and data count (EV-049). The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**. Actions completed since then (for example, the policies approved 2026-08-31) appear in the remediation column but do not change the status. Gap risk uses the P01 scale.

**Current CSF Tier: Tier 1 (Partial).** Security has been informal and reactive. **Target: Tier 2 (Risk Informed) by 2027-08**, meaning practices approved by the Owner and General Manager and driven by the risk register, which is realistic for a 7-person farm with a part-time Security Coordinator and an MSP.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 2 | 10 | 19 | 0 |
| CSF 2.0 Identify (21) | 3 | 4 | 14 | 0 |
| CSF 2.0 Protect (22) | 3 | 13 | 5 | 1 |
| CSF 2.0 Detect (11) | 0 | 1 | 10 | 0 |
| CSF 2.0 Respond (13) | 0 | 3 | 10 | 0 |
| CSF 2.0 Recover (8) | 0 | 1 | 7 | 0 |
| **CSF 2.0 subtotal (106)** | **8** | **32** | **65** | **1** |
| Produce Safety records, 21 CFR 112 Subpart O (7) | 2 | 4 | 1 | 0 |
| H-2A earnings records, 20 CFR 655.122(j) (3) | 0 | 3 | 0 | 0 |
| Fla. Stat. 501.171 (6) | 0 | 2 | 3 | 1 |
| 21 CFR Part 121, N11-R01 (1) | 0 | 0 | 0 | 1 |
| **Total (123)** | **10** | **41** | **69** | **3** |

Of the 110 unmet or partially met rows, 12 are rated High, 51 Moderate, and 47 Low.

**What the numbers say.** Protect scores best, because the SaaS vendors and the MSP supply encryption in transit, sign-in services, and patching for the office computers. Govern is mostly Not met: before this engagement nobody owned security, there were no policies, and no supplier had security terms. The farm **cannot detect, respond to, or recover from** an attack: 27 of the 32 Detect, Respond, and Recover subcategories are Not met. The OT picture is the same: the pump station can be reached from the shop Wi-Fi and through the dealer's gateway, and nobody would see a change.

The three not applicable rows are PR.PS-06 (the farm writes no software; dealer-written controller logic is covered by ID.RA-07 and GV.SC-05), Fla. Stat. 501.171(5) (the farm holds personal information on about 25 people, so a notice to more than 1,000 cannot arise at current scale), and N11-R01.

## 4. Priority gaps
| Gap | Row(s) | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Shared and default credentials (field crew login, gateway, touchscreen PIN); records not signed by the person | G-053, G-108, G-114 | High | Named crew accounts with tablet PINs; named dealer accounts; change defaults | Field Supervisor; Irrigation and Equipment Technician | 2026-11-30 |
| MFA missing on accounts that control irrigation or hold backups | G-055 | High | MFA for every SYS-01 user and mailbox, the backup console, and dealer access | Office Manager | 2026-09-30 |
| Over-shared H-2A files and stale access | G-057, G-117 | High | Restrict the Office folder; last-day checklist; monthly reconciliation; remove standing dealer access | Office Manager | 2026-10-31 |
| Flat network; dealer gateway bypasses the firewall | G-071 | High | Separate segment for the pump station; guest Wi-Fi; gateway on request only | Irrigation and Equipment Technician | 2026-12-31 |
| Backups unproven; no SYS-01 export; controller program held only by the dealer | G-064, G-101 | High | 90-day immutable backup; quarterly restore tests; monthly export; farm-held program copy | Office Manager | 2026-11-30 |
| No incident response or contingency plan | G-052 | High | P08 runbook (approved 2026-08-31); contingency plan with the hand-operation procedure | Owner and General Manager | 2027-01-31 |
| No supplier security terms | G-026 | High | Dealer terms by 2026-10-31; AI vendor terms by 2026-10-31; MSP and equipment dealer amendments | Owner and General Manager | 2026-12-31 |
| No security awareness training; no Spanish material | G-059 | High | Annual training in English and Spanish; tips at crew meetings | Office Manager | 2026-11-30 |
| Hand operation known by one person | G-073 | Moderate | Written procedure; second person trained and drilled | Owner and General Manager | 2027-02-28 |
| Unrecorded dealer changes to the controller | G-045, G-078 | Moderate | Change log; approved and logged dealer sessions | Irrigation and Equipment Technician | 2026-10-31 |
| Irrigation change alerts off; no monitoring | G-075, G-079 | Moderate | SYS-01 alerts to two phones; MSP-managed EDR | Irrigation and Equipment Technician; Office Manager | 2026-09-30; 2026-12-31 |
| No breach procedure | G-095, G-119 | Moderate | P08 notification matrix; notice templates in English and Spanish | Owner and General Manager | 2026-11-30 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person farm: most actions are settings, one-page procedures, or short MSP and dealer jobs, not new systems. The MSP and the irrigation dealer do the technical work under the Office Manager's and the Technician's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Ownership and quick fixes | 2026-09-30 | Security Coordinator designated and policies approved (done 2026-08-31); MFA on every SYS-01 user, mailbox, and the backup console; SYS-01 irrigation change alerts on; first restore test; gateway firmware update and retest; HR checklists with security steps | G-014, G-017, G-016, G-055, G-075 |
| 2. Access, data, and suppliers | 2026-10-31 | Restrict and stop syncing the Office folder; encrypt the desktop; mobile device settings; inventory of devices, OT, and data; dealer security terms and on-request gateway access; AI vendor data terms; breach contacts registered with the payroll service and filing agent; change log; River Tract panel locks | G-032, G-033, G-037, G-045, G-057, G-058, G-061, G-063, G-069, G-078, G-115, G-121, G-122 |
| 3. Records and resilience | 2026-11-30 | Named crew accounts; paper fallback forms; 90-day immutable backup; monthly SYS-01 export; farm-held controller program; training in English and Spanish; tabletop with the MSP and dealer; notice templates | G-053, G-059, G-064, G-086, G-095, G-101, G-107, G-108, G-110, G-113, G-114, G-119 |
| 4. Network and detection | 2026-12-31 | Pump station segment and guest Wi-Fi; MSP-managed EDR with after-hours alerting; quarterly scans; retention schedule; MSP and equipment dealer contract amendments | G-026, G-039, G-071, G-079, G-083, G-111, G-116, G-117 |
| 5. Contingency and annual cycle | 2027-01-31 to 2027-08-31 | Contingency plan with the hand-operation procedure (January); second person trained and drilled before the season (February); risk assessment update (July); independent assessment and policy review (August) | G-052, G-073, G-099, G-050 |

**Progress check.** The Office Manager reports progress to the Owner and General Manager at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending changes (not current obligations)
- **CIRCIA** (6 CFR Part 226, proposed, 89 FR 23644): no final rule as of 2026-09-25. As proposed it would not cover the farm (section 1). Recheck when a final rule publishes, because scope may change.
- **H-2A rules (20 CFR Part 655):** the Department of Labor proposed on 2025-07-02 (FR Doc 2025-12315) to rescind its 2024 farmworker protections final rule, which amended 20 CFR 655.122. No final rescission was found in the Federal Register as of 2026-09-25. Whether the proposal would change the content of the earnings records in 655.122(j)(1) was not verified. The farm follows the current text, which the `pending_rule_change` column flags on the three H-2A rows.
- **Produce Safety Rule:** no pending changes were found for 21 CFR 112 Subpart O. Section 112.161(b) was last amended by the 2024 agricultural water rule (89 FR 37519, 2024-05-06).
- **Fla. Stat. 501.171** was read as the 2026 statute; state bills were not tracked.

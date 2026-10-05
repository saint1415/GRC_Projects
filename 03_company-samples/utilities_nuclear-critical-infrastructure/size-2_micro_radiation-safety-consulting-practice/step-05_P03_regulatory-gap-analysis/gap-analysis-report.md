# Regulatory Gap Analysis: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radiation safety consulting practice, NAICS 541690) |
| Tier / Vertical | Micro / Nuclear Reactors, Materials, and Waste |
| Vertical's primary regulation | 10 CFR 73.54 (with RG 5.71 Rev. 1 controls): **not applicable** (section 1) |
| Regulation analyzed | **10 CFR Part 37 information protection duties** (37.43(d), with 37.31 and the review and reporting provisions the practice supports) as flowed down to the practice by its 6 Part 37 clients' contracts. Text checked on eCFR (version date 2026-09-23) |
| Also analyzed | Reactor client contract terms (4 rows); Fla. Stat. 501.171 (2 rows); NIST CSF 2.0 benchmark for the practice's own program (19 rows) |
| Assessment dates | 2026-08-03 to 2026-08-14 |
| Assessor | Office Manager (Security Officer) with the Senior Health Physicist (Part 37 services lead) and the MSP lead technician |
| Approved | 2026-09-15 by the Principal Health Physicist (owner) |
| Workbook | `gap-analysis.csv` (45 rows: G-001 to G-009 applicability, G-010 to G-020 Part 37, G-021 to G-024 reactor contracts, G-025 to G-026 Florida, G-027 to G-045 CSF 2.0) |

## 1. Applicability

### 1.1 The vertical's primary regulation does not apply
**10 CFR 73.54 does not apply.** It covers each licensee "currently licensed to operate a nuclear power plant under part 50" and Part 52 combined license holders and applicants. The practice holds a limited Florida materials license for a calibration laboratory. For the same reason:
- **10 CFR 73.77** (cyber security event notifications) does not apply. It covers "each licensee subject to the provisions of § 73.54 or § 73.110." The 1-hour, 4-hour, and 8-hour clocks belong to the reactor clients.
- **10 CFR 73.110** (Part 53 plants) does not apply.
- **NERC CIP** does not apply. The practice is not a registered entity.
- **CIRCIA** is not in effect: no final rule was published as of 2026-10-05. As proposed (89 FR 23644, proposed 6 CFR 226.2), it would cover critical infrastructure entities that exceed the SBA size standard or meet a sector criterion. The practice's receipts (about $1.1 million) are far below the $19.0 million standard for NAICS 541690. The nuclear criterion covers owners or operators of a commercial nuclear power reactor or fuel cycle facility.
- **Safeguards Information (10 CFR 73.21)** does not apply today. The section reaches any "person who produces, receives, or acquires" SGI, licensee or not. The practice does none of these, and its reactor contracts say the plants will not share SGI. An accidental receipt would make the section apply at once, so G-023 adds a handling rule.
- **10 CFR 73.56** reactor access authorization does not apply to the practice. Under 73.56(a)(4) "only a licensee shall grant an individual unescorted access," and each plant processes practice staff under its own program.
- **10 CFR Part 810** does not apply. The practice has no foreign clients or foreign national staff and transfers no listed reactor technology.

These results are rows G-001 to G-009. The reactor rules still reach the practice through **contract terms** (rows G-021 to G-024), which the plants write from their own 73.54 and 73.56 programs.

### 1.2 The practice's own license does not bring in Part 37
The practice holds a **limited Florida specific license** (Florida Department of Health, Bureau of Radiation Control, Chapter 64E-5, F.A.C.; Florida has been an NRC Agreement State since 1964). It authorizes one Cs-137 calibrator source of about 0.4 Ci, check sources, and leak test sample analysis. Part 37 Subparts B and C apply to anyone who "possesses or uses at any site, an aggregated category 1 or category 2 quantity" (37.3(a)). The category 2 threshold for Cs-137 is 1 TBq (27.0 Ci) (Part 37, Appendix A), so the practice holds about 1.5% of it (G-007). The license's radiation safety rules (source security, leak tests, dosimetry, records) are binding, but they are not cybersecurity rules and are not decomposed here.

### 1.3 Why Part 37 is still the primary regulation
**The practice holds other licensees' Part 37 secrets.** Six consulting clients possess category 2 quantities. All are Florida licensees, and Florida applies Part 37 to them through a standard license condition (Florida submission to the NRC, ADAMS ML23178A117, as verified in this vertical's Small sample; 37.43 is not among the excluded sections). The practice drafts their security plans and implementing procedures and performs their annual reviews, so it holds copies of exactly the documents 37.43(d) protects:
- the security plan and implementing procedures;
- the list of individuals approved for unescorted access;
- review reports under 37.33 and 37.55, which describe weaknesses in each program.

**How the duty reaches the practice.** The regulation binds the clients, not the practice. Each client's reviewing official must evaluate need to know and complete a trustworthiness and reliability determination before anyone, including a consultant, sees the information (37.43(d)(3)). The determination uses the background investigation elements in 37.25(a)(2) through (a)(7). The clients' contracts then require the practice to:
- use the client's handling procedures;
- give access only to approved staff;
- report departures within 2 working days, so the client can meet its own 7-working-day removal rule (37.43(d)(6));
- return or destroy copies at the end of each engagement;
- report suspected unauthorized access within 24 hours, so the client can meet its 37.57(b) duty to assess suspicious activity.

**Requirement type.** Rows G-010 to G-020 are marked "Contractual (the client's duty under its Florida license condition, flowed down by contract)". A practice failure would be a contract breach for the practice and a possible violation for the client. For a 7-person firm whose Part 37 work is 15% of receipts, the contract breach is the bigger risk.

### 1.4 Other binding rules
- **Fla. Stat. 501.171(2)** requires "reasonable measures to protect and secure data in electronic form containing personal information" (G-025). The practice holds employee records, staff dose reports with Social Security numbers, and background pages photographed at a client.
- **Fla. Stat. 501.171(8)** (disposal of customer records) does **not** apply. "Customer records" are records an individual gives the business to buy a product or obtain a service (501.171(1)(c)). The practice's customers are businesses (G-026).
- **FTC Act Section 5** (15 U.S.C. 45(a)) applies to any security claims the practice makes to clients, including its answers to security questionnaires (P09). It is not decomposed into rows.
- **HIPAA** does not apply. The practice is not a covered entity, and medical clients give it only de-identified patient data.

### 1.5 Why a CSF 2.0 benchmark is added
Neither Part 37 nor the contracts say anything about patching, backups, monitoring, training, or incident response for the practice's own systems. The owner adopted **NIST CSF 2.0**, with the CSF 2.0 Small Business Quick-Start Guide (NIST SP 1300), as the benchmark for those topics (rows G-027 to G-045).

## 2. Method
1. **Requirements.** Part 37 rows follow the regulation's own structure: each paragraph of 37.43(d) that the contracts flow down, plus 37.31, the review report provisions (37.33, 37.55), and the event assessment duty (37.57(b)). Brief quotes come from the public-domain eCFR text. Contract rows paraphrase the client contracts. CSF rows use the subcategory text.
2. **Crosswalk.** No official NIST mapping exists for Part 37 or the contracts, so those CSF 2.0 and SP 800-53 mappings are the author's. For the CSF rows, the SP 800-53 controls are a subset of NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`).
3. **Documentary evidence.** Each status rests on a named document or record: suite permission, sharing, and audit log reports (2026-08-05); the SYS-02 user list; client approval letters and contracts; the 3 client information protection procedures on file; the April 2026 kiosk quarantine email; the MSP device list, patch report, and backup job report; a search of the client library for SGI, background records, and Social Security numbers (2026-08-07); and a check of the 7 USB drives in use (2026-08-07). Interviews covered all 7 staff and the MSP lead technician.
4. **Status.** Met, Partially met, Not met, or Not applicable, **as of the end of fieldwork (2026-08-14)**. Actions completed since then are noted in the remediation column but do not change the status.

## 3. Results summary

| Part | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| A. Applicability (reactor rules, SGI, own license, Part 810) | 0 | 0 | 0 | 9 | 9 |
| B. 10 CFR Part 37 information protection (client flow-down) | 0 | 4 | 7 | 0 | 11 |
| C. Reactor client contract terms | 0 | 3 | 1 | 0 | 4 |
| D. Fla. Stat. 501.171 | 0 | 1 | 0 | 1 | 2 |
| E. NIST CSF 2.0 benchmark | 2 | 8 | 9 | 0 | 19 |
| **Total** | **2** | **16** | **17** | **10** | **45** |

Of the 33 gap rows (Not met or Partially met), 5 are rated High, 25 Moderate, and 3 Low. The High gaps are G-010 and G-013 (Part 37), G-021 (reactor media), G-040 (backups), and G-044 (incident response).

**CSF 2.0 by function:** Govern 1 Met and 3 Not met; Identify 1 Met and 3 Not met; Protect 7 Partially met and 1 Not met; Detect 1 Partially met; Respond 1 Not met; Recover 1 Not met.

**What the numbers say.** No Part 37 row is fully met. The cause is one design choice: a single "Clients" library that every staff member can open and that syncs to every laptop. Seven of the 11 Part 37 rows trace back to it or to the missing procedure that would have prevented it. The Protect function scores best among the CSF rows because the SaaS vendors and the MSP supply encryption, MFA on the main systems, and patching for laptops. The practice's own processes (inventory, training, incident response, recovery) are mostly absent, which is typical for a 7-person firm that has never had a security owner.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Client security information open to all staff and synced to every laptop | 37.43(d)(1); (d)(3)(i) | High | Restricted folder per client, approved staff only, sync off | Part 37 services lead | 2026-10-15 |
| Unapproved staff opened client security information | 37.43(d)(3)(ii) | High | Only approved staff handle Part 37 files; clients decide on the Project Coordinator | Part 37 services lead | 2026-10-15 |
| Personal USB drives carried to reactor plants; malware already found | Reactor contract; MP-7 | High | Company encrypted drives, scanned before each trip | Field services lead | 2026-10-31 |
| Backups untested; no SYS-02 export | PR.DS-11 | High | Restore test; immutable versions; monthly export | Office Manager | 2026-10-31 |
| No incident plan; client clocks not tracked | RS.MA-01; 37.57(b) flow-down; reactor 4-hour notice | High | P08 runbook and notification matrix; tabletop | Office Manager | 2026-12-15 |
| Departures not reported to clients | 37.43(d)(6) | Moderate | Departure checklist with client notice in 2 working days | Office Manager | 2026-10-31 |
| No handling procedure | 37.43(d)(2) | Moderate | SEC-INFO-01 procedure; collect client procedures | Part 37 services lead | 2026-10-31 |
| Background pages photographed at a client | 37.31(a)-(b) | Moderate | Delete and confirm; never copy background records | Part 37 services lead | 2026-09-30 |
| Copies kept after engagements end | 37.43(d)(8); contract | Moderate | Destroy former clients' copies; close-out checklist | Part 37 services lead | 2026-11-30 |
| Late notice to a client after the chatbot event | 37.57(b) flow-down | Moderate | Reporting rule; contact card | Office Manager | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person practice: most actions are settings, one-page procedures, or MSP tasks, not new systems. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Client information | 2026-10-15 | Restricted per-client folders with sync off; client approval list; 2 missing approval letters; only approved staff format Part 37 reports; background photos deleted (by 2026-09-30) | G-010, G-012, G-013, G-014, G-018 |
| 2. Procedures and media | 2026-10-31 | SEC-INFO-01 handling procedure; departure checklist with client and plant notices; encrypted delivery of review reports; personal media banned and company drives issued; SGI accidental-receipt rule; reporting rule and notification matrix; MFA for all SYS-02 users and the MSP firewall login; inventory; first restore test; policies adopted and acknowledged | G-011, G-015, G-016, G-019, G-020, G-021, G-022, G-023, G-024, G-028, G-031, G-032, G-035, G-036, G-040 |
| 3. Hardening | 2026-11-30 | Lab workstation encryption; old dose reports replaced; former clients' copies destroyed; vulnerability scans; separate admin accounts; training starts | G-017, G-025, G-033, G-037, G-038, G-039 |
| 4. Resilience and suppliers | 2026-12-31 | Lab network segment; EDR; P08 tabletop and contingency plan; MSP contract amendment and review; lab workstation plan | G-029, G-030, G-041, G-042, G-043, G-044, G-045 |
| 5. Annual cycle | 2027-08 | Risk assessment update; independent assessment; policy review; client approval list confirmed with each client | All |

**Before the next client review season:** most Part 37 reviews fall between November and February. Phase 1 must be finished first, because a client inspector who asks "who at your consultant can see this plan?" needs a short, true answer.

**Progress check.** The Office Manager reports progress to the owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
- **Part 37.** The NRC proposed "Modernizing Requirements Relating to Physical Protection of Category 1 and Category 2 Quantities of Radioactive Material" (91 FR 17893, 2026-04-09; comments closed 2026-05-11). It was **not final as of 2026-10-05**. Its list of changes covers 37.23, 37.25(b) and (c), 37.43(c)(3) (refresher training every 3 years instead of every 12 months), 37.45(d), 37.49, 37.51, and 37.53(b). **It does not change 37.43(d), 37.31, 37.33, 37.55, or 37.57**, so every Part 37 gap in this analysis stays in force whatever happens. Florida clients would see any final change only when Florida updates its license condition.
- **Other NRC proposals.** "Modernizing Materials Licensing" (91 FR 38124, 2026-06-24) would change the 37.11 exemptions; no effect here. "Modernizing Security Requirements" (91 FR 38928, 2026-06-26) would revise reactor security and fitness-for-duty rules; the plants may change their contract terms later. Neither is final.
- **CIRCIA.** Still proposed. If a final rule narrows or widens coverage, recheck G-005.

The `pending_rule_change` column flags each affected row. None of these proposals is treated as a current obligation.

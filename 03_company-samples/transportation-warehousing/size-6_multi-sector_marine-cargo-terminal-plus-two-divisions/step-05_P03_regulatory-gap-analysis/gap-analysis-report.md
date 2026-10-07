# Regulatory Gap Analysis: Cris Santos Company Holdings | Transportation and Warehousing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Transportation and Warehousing (focus division: Marine Terminals) |
| Primary regulation | USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101, Subpart F (101.600-101.670). Final rule 90 FR 6298 (2025-01-17), effective 2025-07-16. Text checked against eCFR as of 2026-09-23 |
| Division regulations | Freight Trading: FAR 52.204-21, CMMC Level 1 (32 CFR Part 170) and DFARS 252.204-7012 in its DoD contracts. Port Real Estate: no sector cyber rule; the FTC Safeguards Rule (16 CFR Part 314) is used as a voluntary benchmark |
| Group obligations | SEC Reg S-K Item 106 and Form 8-K Item 1.05; Shipping Act, 46 U.S.C. 41106; state breach notification laws; intercompany and customer contracts |
| Gap tables | `gap-analysis.csv` (Marine Terminals, 71 rows); `gap-analysis-freight-trading.csv` (30 rows); `gap-analysis-port-real-estate.csv` (21 rows); `gap-analysis-group.csv` (8 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads, the Division CySO and the Freight Trading federal contracts compliance manager, coordinated by the Group Chief Risk Officer; legal conclusions by the Group General Counsel; reviewed by group internal audit |

## 1. Applicability
### 1.1 Marine Terminals: Subpart F applies at all 9 terminals
Subpart F applies to "the owners and operators of U.S.-flagged vessels, facilities, and OCS facilities required to have a security plan under 33 CFR parts 104, 105, and 106" (101.605(a)). Every terminal is a facility regulated under 33 CFR Part 105 with a Coast Guard-approved FSP, so all 9 are covered. There is **no size threshold or large-operator variant**. Two provisions matter at this size:
- **One CySO for several facilities is allowed** (101.625(b)), if each facility's Plan lists every facility the CySO covers. The Division CySO was designated in writing for all 9 on 2026-03-02.
- **One Plan may cover several facilities of similar operations**, but it must address each facility's specific risks (101.630(d)(2)). The group chose one Plan per terminal because T7 to T9 differ so much from T1 to T6 today.

Subpart F also preempts conflicting state or local law for Part 105 facilities (101.610).

**Compliance dates (verified in the regulation text):**

| What | When | Source |
|---|---|---|
| Rule effective; report reportable cyber incidents to the NRC if not reported under 6.16-1 | 2025-07-16 | 90 FR 6298; 101.620(b)(7), 101.650(g)(1) |
| Training for all personnel and key personnel | 2026-01-12, then annually | 101.650(d)(4) |
| First Cybersecurity Assessment for each facility | No later than 2027-07-16, then annually | 101.650(e)(1) |
| Cybersecurity Plans submitted to the Coast Guard | No later than 2027-07-16 | 101.655 |

The measures in 101.650(a) to (i) must be "in place and documented" in named sections of the Plan. The division treats them as due when the Plans are submitted (target 2027-04-30) and will confirm this reading with each of the four COTP zones in 2027-Q1.

**Secondary rules.** 33 CFR 6.16-1 requires evidence of an actual or threatened cyber incident involving or endangering any vessel, harbor, port or waterfront facility to be reported immediately to the FBI, CISA and the COTP; a 6.16-1 report also satisfies the NRC duty in 101.620(b)(7). The MTSA reporting duties in 101.305 apply through each FSP.

**Shipping Act.** As a marine terminal operator, the division may not "give any undue or unreasonable preference or advantage or impose any undue or unreasonable prejudice or disadvantage with respect to any person" (46 U.S.C. 41106(2)). Whether the reserved appointment slots and the affiliate's data access are "undue or unreasonable" is a fact-specific legal question for the Group General Counsel. This analysis records them as a gap (G-070) because no operational reason is documented.

### 1.2 Freight Trading: DoD contract clauses
| Requirement | Applies? | Basis |
|---|---|---|
| FAR 52.204-21 (N42-R04) | **Yes** | The clause is in the division's DoD supply contracts, and the division's systems process Federal Contract Information (FCI) |
| CMMC Level 1 (N42-R02; 32 CFR Part 170) | **Yes** | Final Level 1 (Self) status was entered in SPRS on 2025-11-03. A Level 1 self-assessment must cover every system that processes, stores or transmits FCI (170.19(b)(1)), must MET all requirements with no POA&Ms (170.15(a)(1)), and is repeated and re-affirmed each year (170.15(a)(1); 170.22) |
| DFARS 252.204-7012 (N42-R03) | **Yes, when covered defense information is present** | The clause is in the contracts. No contract identifies covered defense information to date. CUI-marked drawings received on 2026-06-18 for a quote may be covered defense information if they support performance of a contract; status is being confirmed with the prime contractor. Until then the group treats them as covered |
| CMMC Level 2 | Not yet | Required only where a contract requires it for CUI; Phase 2 of the phase-in starts 2026-11-10 (N42-R02 status) |
| FAR 52.204-25 (N42-R05) | **Yes** | In the contracts; reporting within 1 business day of identifying covered telecommunications equipment or services |
| FTC Act Section 5 (N42-R01) | Yes | General |
| CCPA and CPPA regulations (N42-R08) | No | The 2026 data inventory found no operations, employees or consumers in California |

### 1.3 Port Real Estate: no sector rule; the Safeguards Rule as a benchmark
The FTC Safeguards Rule protects "customer information", meaning nonpublic personal information about consumers who obtain a financial product or service for personal, family or household purposes (16 CFR 314.2). Port Real Estate leases warehouses and yards to about 180 commercial tenants; it provides no consumer financial products and holds no customer information in that sense. The rule's duties therefore have nothing to attach to, and the 314.6 exemption question does not arise. The division uses 314.4's elements as a **voluntary benchmark** because they are concrete and the FTC treats similar measures as reasonable security under Section 5. Every row in `gap-analysis-port-real-estate.csv` from 314.4 is labeled "Benchmark only". Other items: FTC Act Section 5 applies (N53-R02); PCI DSS does not (rent is paid by ACH, and occasional card payments go through the processor's hosted page; N53-R04); CCPA does not (no California business; N53-R03); state breach laws apply to employee and guarantor personal information.

### 1.4 Group-wide and excluded
- **SEC (N48-49-R08):** the group is a registrant. Item 106 disclosure is annual; Form 8-K Item 1.05 is due within four business days after a materiality determination, which must be made without unreasonable delay after discovery (Instruction 1 to Item 1.05).
- **State breach laws:** each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171).
- **CTPAT (N48-49-R05):** voluntary; both Marine Terminals and Freight Trading are partners.
- **Excluded:** TSA rail, public transportation and pipeline Security Directives and aviation security program requirements (N48-49-R02 to R04): the group operates none of those modes. 49 U.S.C. 41712 (N48-49-R06): airlines and ticket agents only. CIRCIA: final rule not published as of 2026-09-25, tracked only (GRP-G08).

## 2. Regulation-by-division matrix
| Requirement | Marine Terminals | Freight Trading | Port Real Estate | Group (corporate) |
|---|---|---|---|---|
| N48-49-R01 Subpart F | **Primary.** All 9 facilities | Not applicable (no Part 105 facility) | Not applicable, except the container freight station inside the T3 secure area, which is covered by the T3 FSP and Plan | Common controls feed all 9 Plans; SYS-G1 to SYS-G4 are critical IT for the terminals |
| 33 CFR 6.16-1; 101.305 | Applies (immediate reporting) | Not applicable | Only through the T3 CFS | SOC supplies the facts |
| 46 U.S.C. 41106 | **Applies** (marine terminal operator) | Not applicable, but its access and appointments are the subject of the gap | Not applicable | Group General Counsel owns the review |
| N48-49-R05 CTPAT | Partner (voluntary) | Partner as importer (voluntary) | Not a partner | Not applicable |
| N42-R04 FAR 52.204-21 | Not applicable | **Applies** (FCI) | Not applicable | Common controls inherited |
| N42-R02 CMMC Level 1 | Not applicable | **Applies** | Not applicable | Common controls inherited |
| N42-R03 DFARS 252.204-7012 | Not applicable | **Applies when CDI is present** | Not applicable | Group IR plan must carry the 72-hour step |
| N42-R05 FAR 52.204-25 | Not applicable | Applies | Not applicable | Group procurement blocks covered brands |
| N53-R01 FTC Safeguards Rule | Not applicable | Not applicable | **Benchmark only** (does not apply) | Not applicable |
| FTC Act Section 5 (N42-R01, N53-R02) | Applies (general) | Applies | Applies | Applies |
| N48-49-R08 SEC Item 106 and 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (registrant) |
| State breach notification laws | Employee, longshore and driver data | Employee and customer contact data | Employee and guarantor data | Coordinates (P08) |
| OSHA marine terminal standards, 29 CFR part 1917 | Applies (safety; relevant to P10) | Not applicable | Not applicable | Not applicable |
| N48-49-R02 to R04 TSA directives; N48-49-R06 | Not applicable | Not applicable | Not applicable | Not applicable |
| CIRCIA | Tracked (not in effect) | Tracked | Tracked | Tracked |

## 3. Method
1. **Requirements.** Subpart F rows follow the regulation's own structure, one row per paragraph that imposes a duty, reused from the group's Small-size analysis of the same rule and re-assessed for 9 facilities. FAR, DFARS and CFR rows were read from eCFR (point in time 2026-09-23). CMMC Level 1 rows use 32 CFR 170.15, 170.19 and 170.22. The Safeguards Rule rows use 16 CFR 314.4. Brief quotes only; all are public-domain federal text.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **These are author mappings.** NIST has published no official mapping for Subpart F, the FAR clause or the Safeguards Rule (the FAR rows follow the CMMC Level 1 to SP 800-171A table in 170.15(c)(1)(ii) for their structure).
3. **Evidence.** Interviews with each division's leadership, the CySO, FSOs, the federal contracts compliance manager and the director of building technology; document review (FSPs, draft Plans, contracts, SPRS record, integrator contracts); configuration exports; the external exposure scan; and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. For Marine Terminals a row is Met only if it is met at all 9 terminals; the `current_state` and `gap_description` columns say which terminals fall short. Gap risk uses the P01 scale.

## 4. Results
### 4.1 Marine Terminals (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 101.620 Owner or operator | 1 | 6 | 0 | 1 |
| 101.625 Cybersecurity Officer | 1 | 2 | 0 | 0 |
| 101.630 Cybersecurity Plan | 0 | 3 | 1 | 2 |
| 101.635 Drills and exercises | 1 | 2 | 0 | 0 |
| 101.640 Records | 0 | 1 | 0 | 0 |
| 101.645 Communications | 2 | 0 | 0 | 0 |
| 101.650 Cybersecurity measures (a) to (i) | 4 | 31 | 2 | 2 |
| 101.655 to 101.665 Dates, documentation, waivers | 0 | 0 | 1 | 2 |
| Secondary: 6.16-1 and 101.305 | 3 | 1 | 0 | 0 |
| Shipping Act 41106(2) and CTPAT | 1 | 0 | 1 | 0 |
| **Total (71)** | **13** | **46** | **5** | **7** |

**Reading the result.** The pattern is the opposite of the Small terminal's: almost every measure is in place at T1 to T6, so most rows are Partially met because of **T7 to T9**, the longshore workforce, or one terminal's exception. Of the 51 Partially met or Not met rows, **9 are overdue or already in force**: 3 Subpart F rows in force since 2025-07-16 (NRC reporting twice and records), 4 training rows past the 2026-01-12 deadline (longshore and OT training), the 6.16-1 reporting procedure, and the Shipping Act row. **The other 42 fall due by 2027-07-16.** The 4 Not met Subpart F rows (Plan submission twice, the Assessment and its FSA entry) are not yet due.

Gap risk for the 51 rows: 13 High, 33 Moderate, 5 Low. The 13 High rows are the Gulf terminals' remote access, segmentation, logging, backups and KEVs (G-010, G-027, G-035, G-046, G-049, G-050, G-054, G-058, G-059, G-060), the overdue longshore and OT training (G-037, G-038) and the Shipping Act gap (G-070).

### 4.2 Freight Trading (`gap-analysis-freight-trading.csv`)
| Regulation | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FAR 52.204-21 (16 rows) | 10 | 6 | 0 | 0 |
| CMMC Level 1, 32 CFR Part 170 (4 rows) | 1 | 1 | 2 | 0 |
| DFARS 252.204-7012 (7 rows) | 0 | 1 | 5 | 1 |
| FAR 52.204-25, FTC Act, CTPAT (3 rows) | 2 | 1 | 0 | 0 |
| **Total (30)** | **13** | **9** | **7** | **1** |

Gap risk for the 16 rows: 7 High, 6 Moderate, 3 Low.

**The Level 1 status does not match reality (scenario gap 4).** The 2025 self-assessment scoped only the federal sales workspace (SYS-F3). FCI also sits on yard shipping documents in SYS-F2, which is open to all yard staff and to the vendor, uses shared logins on some scale PCs, and is outside the group patch cycle. Level 1 allows no POA&Ms, so the division cannot carry these as open items: it must fix the six partially met FAR requirements, re-assess the full scope, and have the Affirming Official enter a corrected affirmation before the annual date of 2026-11-03. Counsel is reviewing the earlier affirmation.

**CUI has no compliant home.** DFARS 252.204-7012 requires NIST SP 800-171 on covered contractor information systems, a cloud service equivalent to the FedRAMP Moderate baseline for any covered defense information in the cloud, and a report to DoD within 72 hours of discovering a cyber incident, filed with a DoD-approved medium assurance certificate. The division has none of these. The drawings received on 2026-06-18 were quarantined on 2026-08-04; the president will decide by 2026-10-31 whether to build a CUI enclave or decline CUI work.

### 4.3 Port Real Estate (`gap-analysis-port-real-estate.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FTC Safeguards Rule 314.4 (benchmark, 18 rows) | 6 | 9 | 2 | 1 |
| FTC Act Section 5, state breach laws, PCI DSS (3 rows) | 0 | 2 | 0 | 1 |
| **Total (21)** | **6** | **11** | **2** | **2** |

Gap risk for the 13 rows: 5 High and 8 Moderate. **Not met:** logging and monitoring of building systems (RE-G11) and oversight of the 5 integrators (RE-G14). Both trace to scenario gap 5. The office side of the division (SYS-R1 and staff endpoints) is sound because it inherits group controls; the building systems were never brought into the group program.

### 4.4 Group obligations (`gap-analysis-group.csv`)
8 rows: 3 Met, 4 Partially met, 1 Not applicable (CIRCIA, not in effect). Gap risk: 1 High (GRP-G06, no affiliate data-sharing rule) and 3 Moderate (Item 106 description of third-party oversight, incident materiality criteria, and the state breach matrix).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Affiliate access to terminal customer data and reserved appointment slots (1) | MT, FT, Group | 46 U.S.C. 41106(2); 101.650(a)(5); terminal services agreements | High | Remove the group logistics role; neutral appointment rules; affiliate data-sharing standard; legal review | Group General Counsel | 2026-11-30 |
| 2 | Gulf terminals: remote access, segmentation, logs, backups, KEVs (2) | MT | 101.650(c)(1), (e)(3)(i), (iv), (v), (f)(3), (g)(4), (h) | High | Disconnect vendor modems 2026-11-30; interim firewalls, log forwarding and vault copies 2026-12-31; migration 2027-06-30 | Gulf terminals general manager | 2027-06-30 |
| 3 | Longshore and OT training overdue (3) | MT | 101.650(d)(1), (d)(3)-(4) | High | Training at the hiring halls; OT course at every terminal; supervision records | Division CySO | 2027-03-31 |
| 4 | Level 1 scope and affirmation; CUI handling; DFARS reporting (4) | FT | 32 CFR 170.15, 170.19, 170.22; 52.204-21; 252.204-7012(b)-(e) | High | Re-scope and re-affirm; CUI decision; DFARS procedure and certificate | Federal contracts compliance manager | 2026-11-30 |
| 5 | Building systems and integrators (5) | RE | 314.4(c)(5), (c)(8), (f) (benchmark); FTC Act Section 5 | High | Jump host, SOC monitoring, integrator contract terms | Director of building technology | 2027-03-31 |
| 6 | Plans and Assessments for 9 facilities; alternates at T7 to T9 (3) | MT | 101.620(b)(3); 101.630; 101.650(e)(1); 101.655 | Moderate | Alternates 2026-10-31; Assessments 2027-03-31; Plans submitted 2027-04-30 | Division CySO | 2027-04-30 |
| 7 | Notification matrix not exercised (7) | All | 6.16-1; 101.620(b)(7); 252.204-7012(c); Form 8-K Item 1.05; state laws | Moderate | Complete the matrix; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 8 | Port Real Estate inheritance and supplement (6) | RE | 314.4(g) (benchmark) | Moderate | Inheritance matrix; supplement realigned | Port Real Estate security and compliance lead | 2026-12-31 |
| 9 | AI governance (8) | MT, FT | 101.650(e)(1) (the Assessment must cover the SYS-T5 to ASC path); 29 CFR part 1917; FTC Act Section 5 | High | Group AI program (P10) | Group Chief Risk Officer | 2027-03-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-024 to POAM-027 come directly from this analysis; most assessment items also trace to rows here (for example POAM-002, POAM-008, POAM-011 to POAM-016, POAM-018, POAM-019 and POAM-023).

## 6. Pending regulatory changes
- **Subpart F:** no change pending for facilities. The final rule asked for comment on delaying implementation for U.S.-flagged vessels only; the Federal Register search on 2026-09-26 found no later rule or proposal, and eCFR shows no version after 2025-07-16.
- **CMMC phase-in:** Phase 2 begins 2026-11-10, when Level 2 (C3PAO) requirements start to appear in applicable solicitations. It matters only if the division accepts CUI work (P01 FT-013).
- **CIRCIA:** final rule not published as of 2026-09-25; not treated as a current obligation (P08 tracks it).
- The `pending_rule_change` column is "None" on every Subpart F row and notes the CMMC phase-in on the CMMC rows.

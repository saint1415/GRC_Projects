# Regulatory Gap Analysis: Cris Santos Company | Transportation and Warehousing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed marine cargo terminal operator, NAICS 488320: Terminal 1, Terminal 2 and an off-dock depot in Florida) |
| Tier / Vertical | Mid-Market / Transportation and Warehousing |
| Primary regulation | USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101, Subpart F (101.600-101.670). Final rule 90 FR 6298 (2025-01-17), effective 2025-07-16. Text checked against eCFR as of 2026-09-23; a Federal Register search on 2026-10-04 found no later rule or proposal amending it |
| Other regulations for the primary business line | Maritime cyber incident reporting (33 CFR 6.16-1, as amended by E.O. 14116, 89 FR 13973) and MTSA reporting (33 CFR 101.305); the cyber-relevant duties in 33 CFR Part 105 (FSO, drills, records, access control, cargo release, FSA, FSP audit); protection of SSI (49 CFR 1520.7, 1520.9); Florida Information Protection Act (Fla. Stat. 501.171(2)-(6), (8)) |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | GRC analyst and the Security Manager (alternate CySO), with the vCISO and both FSOs; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 |
| Requirement IDs | N48-49-R01 (primary). Regulatory driver columns in P01, P02, P04, P06 and P07 cite N48-49-R01 plus the section |
| Handling | Describes security vulnerabilities of MTSA-regulated facilities. Handle as SSI (49 CFR 1520.5(b)(5); POL-04 4.2) |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| 33 CFR Part 101, Subpart F | **Yes, at both terminals** | 101.605(a) covers owners and operators of facilities "required to have a security plan under 33 CFR parts 104, 105, and 106." Both terminals receive foreign cargo vessels greater than 100 gross register tons (33 CFR 105.105(a)(4)) and have Coast Guard-approved FSPs. There is no size threshold or small-business exemption. After the Cybersecurity Assessment the company may seek a waiver or equivalence (101.665) |
| The off-dock depot | **Not separately** | It receives no vessels and has no FSP (company reading of 105.105(a); to be confirmed with the COTP). Its gate connects to the TOS, so its systems appear in the inventory and network map required for the terminals (101.650(b)(3)-(4)) |
| 33 CFR 6.16-1 and 101.305 | **Yes** | Both terminals are waterfront facilities with FSPs |
| 33 CFR Part 105 (cyber-relevant duties) | **Yes** | Each terminal's FSP, FSA, drills, records and audits. Only paragraphs that touch computer systems, networks, electronic records, PACS or cargo release data were analyzed |
| 49 CFR Part 1520 (SSI) | **Yes** | The owner or operator of a maritime facility required to have a security plan is a covered person (1520.7(d)). The Cybersecurity Plan is SSI (101.630(b)) |
| Fla. Stat. 501.171 | **Yes** | The company holds Florida driver and employee personal information (driver license numbers in the TOS gate module; HR records). The Subpart F federalism clause (101.610) does not displace Florida's breach notice duties, which do not conflict with Subpart F |

**How Subpart F applies to two terminals.** The terminals are in different COTP zones. The company will submit **one Cybersecurity Plan** covering both, which 101.630(d)(2) allows for facilities "of similar operations" if the Plan "addresses the specific cybersecurity risks for each" facility, with one CySO for both (101.625(b) allows one person to serve several facilities if each Plan lists them). Each terminal keeps its own FSO, because one FSO may serve several facilities only in the same COTP zone and within 50 miles (105.205(a)(2)).

**Compliance dates (verified in the regulation text and the final rule preamble):**
| What | When | Source |
|---|---|---|
| Rule effective; reporting of reportable cyber incidents to the National Response Center (NRC) if not reported under 6.16-1 | 2025-07-16 | 90 FR 6298 (DATES); 101.620(b)(7), 101.650(g)(1) |
| Training for all personnel and key personnel | 2026-01-12, then annually | 101.650(d)(4) |
| CySO designation in writing | Within the 24-month implementation period. **Done 2026-03-02** | 90 FR 6298 preamble; 101.620(b)(3) |
| First Cybersecurity Assessment | No later than 2027-07-16, then annually | 101.650(e)(1) |
| Cybersecurity Plan submitted to the Coast Guard | No later than 2027-07-16. Company target 2027-05-28 | 101.655 |

**How the cybersecurity measures are dated.** The measures in 101.650(a) to (i) must be "in place and documented" in named sections of the Cybersecurity Plan. The company treats them as due when the Plan is submitted and aims to have them in place by then. This is the company's reading of the text; it will be confirmed with both COTPs at the pre-submission meetings planned for 2027-Q1.

**Other transportation requirements considered and excluded:**
- TSA Security Directives for rail, pipeline and aviation (N48-49-R02 to R04): the company is none of these.
- DOT unfair and deceptive practices authority (N48-49-R06): applies to air carriers and ticket agents.
- CMMC (N48-49-R07): no DoD contracts.
- SEC disclosure (N48-49-R08): privately held.
- CTPAT (N48-49-R05): voluntary; the company is not a partner. The PE sponsor asked for a decision in 2027; its minimum security criteria include cybersecurity and would reuse this analysis.
- Shipping Act, 46 U.S.C. 41106, and OSHA marine terminal standards, 29 CFR part 1917: not cybersecurity rules; they bear on the scheduling optimization service and are handled in P10.

## 2. Method
1. **Requirements.** Subpart F rows follow the regulation's own structure: each paragraph of 101.620 to 101.665 that imposes a duty, at the most granular citation that is separately verifiable. Definitions (101.615), purpose (101.600), applicability (101.605), federalism (101.610) and severability (101.670) set context and have no rows. Part 105, Part 1520 and Florida rows were decomposed from the eCFR text (2026-09-23) and the 2026 Florida Statutes. Brief quotes are used; this is public-domain government text.
2. **Requirement type.** The `requirement_type` column records when each duty takes effect, using the dates in section 1.
3. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. **This is an author mapping.** NIST has not published an official mapping for Subpart F, Part 105, Part 1520 or Fla. Stat. 501.171. The SP 800-53 controls match the TOGP control statements in P02.
4. **Evidence.** Interviews (COO, CySO, alternate CySO, both FSOs, Vice President of Terminal Operations, T1 and T2 General Managers, Director of Maintenance and Engineering, OT network engineer, HR Director, Procurement Manager, General Counsel, 12 supervisors, the MSSP service lead), document review (FSPs, FSAs, drill and exercise records, contracts, training export, the 2024 IR and DR plans), configuration exports, and walkthroughs at T2 (night of 2026-08-12) and T1 (night of 2026-08-13).
5. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were chosen at random from system-generated populations, using the co-sourced internal audit firm's attribute sampling table (25 items for a moderate-risk control operating many times a year; all items for small populations). The same populations were used in P07:
   - terminations: 25 of 74 (2025-07-01 to 2026-06-30);
   - new hires for training timeliness: 25 of 96;
   - training records: all 590 employees with system access;
   - vendors with access, contract terms: 27 of 27;
   - vendors holding personal information: 5 of 5;
   - KEVs: 21 of 21 (2026 H1);
   - backup job days: 30 of 30 (July 2026);
   - security incident tickets: 10 of 31;
   - customs hold overrides: 10 of 46 (2026-04 to 2026-06);
   - drill records: 8 of 8, and both 2025 exercise reports;
   - cyber documents for SSI marking: 15;
   - IT and OT purchases over $25,000: 10 of 31;
   - security equipment maintenance entries: 10 of 64;
   - network devices for default passwords: 40 (P07).
   Each `evidence` cell names the sample and its result.
6. **Status.** Each requirement was rated Met, Partially met, Not met or Not applicable. "Not applicable" is used only for duties that are not yet triggered (after Plan approval, at renewal, or on a change of owner) or are optional. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 101.620 Owner or operator | 1 | 6 | 0 | 1 | 8 |
| 101.625 Cybersecurity Officer | 1 | 2 | 0 | 0 | 3 |
| 101.630 Cybersecurity Plan | 0 | 3 | 1 | 2 | 6 |
| 101.635 Drills and exercises | 0 | 3 | 0 | 0 | 3 |
| 101.640 Records | 0 | 1 | 0 | 0 | 1 |
| 101.645 Communications | 0 | 2 | 0 | 0 | 2 |
| 101.650 Cybersecurity measures (a) to (i) | 0 | 30 | 7 | 2 | 39 |
| 101.655 to 101.665 Dates, documentation, waivers | 0 | 0 | 1 | 2 | 3 |
| **Subpart F subtotal** | **2** | **47** | **9** | **7** | **65** |
| Reporting: 6.16-1 and 101.305 | 1 | 3 | 0 | 0 | 4 |
| 33 CFR Part 105 (cyber-relevant) | 6 | 7 | 0 | 1 | 14 |
| 49 CFR Part 1520 (SSI) | 0 | 2 | 0 | 0 | 2 |
| Fla. Stat. 501.171 | 0 | 4 | 0 | 0 | 4 |
| **Total** | **9** | **63** | **9** | **8** | **89** |

**Gap risk ratings (72 rows Partially met or Not met):** 12 High, 41 Moderate, 19 Low.

**Reading the result.** The company has a defined program with gaps in scale. The MTSA basics are Met (separate FSOs, quarterly drills, annual exercises, PACS records, FSA protection, TSI reporting), and the CySO is designated. Most Subpart F rows are Partially met for the same reason: **the measure works at T1 and in the cloud, but not yet at T2 or in OT.** The 9 Not met rows are the approved software list, default-deny for executables, the network map, the supervision rule for untrained users, the public vulnerability channel, the T2 OEM appliance, the FSA cyber results, and the two Plan submission rows that are not yet due.

**What is overdue or already in force.** Of the 72 gap rows, **25 concern duties already in force or past due**:
- 4 Subpart F duties in force since 2025-07-16: owner responsibility (101.620(a)), NRC reporting (101.620(b)(7) and 101.650(g)(1)) and records (101.640);
- 5 training rows past the 2026-01-12 deadline (101.650(d)(1)-(4));
- the 6.16-1 reporting duty and 2 MTSA reporting rows (101.305(a)-(b));
- 7 Part 105 rows, 2 SSI rows and 4 Florida rows.

**The other 47 fall due by 2027-07-16.** The overdue and in-force items are the priority for 2026 Q4.

**The 12 High gaps:**
- the Cyber Incident Response Plan (101.620(b)(6); 101.650(g)(2));
- KEVs in OT and gate systems (101.625(d)(15); 101.650(e)(3)(i));
- MFA for remote OT and local administrators (101.650(a)(4));
- standing privileged accounts (101.650(a)(5));
- the incomplete OT inventory (101.650(b)(3));
- the T2 OEM appliance (101.650(e)(3)(v));
- unmonitored third-party connections (101.650(f)(3));
- backups and recovery (101.650(g)(4));
- T2 segmentation and IT-OT monitoring (101.650(h)(1)-(2)).

## 4. Priority gaps and program roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| T2 OEM appliance always on, shared account | 101.650(e)(3)(v); (f)(3) | High | Off by default from 2026-10-15; OEM through the privileged remote access service; written justification | Director of Maintenance and Engineering | 2026-12-31 |
| 26 vendors with access outside the remote access service | 101.650(f)(3) | High | Onboard all 27 vendors; monthly session review | Director of Maintenance and Engineering | 2026-12-31 |
| No Cyber Incident Response Plan covering OT and both terminals | 101.620(b)(6); 101.650(g)(2) | High | Full plan built on the P08 runbooks; exercised 2026-11-18 | Director of IT and Cybersecurity (CySO) | 2026-12-31 |
| Recovery not demonstrated; T2 not backed up | 101.650(g)(4) | High | Failover test 2026-11-07; hourly isolated snapshots; T2 image and PLC program backups | Director of IT and Cybersecurity (CySO) | 2026-12-31 |
| KEVs in OT and gate systems | 101.625(d)(15); 101.650(e)(3)(i) | High | KEV matching against the OT inventory; compensating controls for unsupported systems | Security Manager (alternate CySO) | 2026-12-31 |
| MFA and privileged access gaps | 101.650(a)(4)-(5) | High | MFA for all remote OT access; privileged access management for directory, identity provider and TOS administrators | Security Manager (alternate CySO) | 2027-03-31 |
| T2 segmentation, monitoring and inventory | 101.650(b)(3); (h)(1)-(2) | High | T2 OT zone with passive sensors; OT alerts to the MSSP; CySO designates critical systems | Director of IT and Cybersecurity (CySO) | 2027-03-31 |
| Training overdue; no supervision rule | 101.650(d)(1)-(4) | Moderate (overdue) | Longshore rules card and vendor briefing; OT training at T2; key personnel role training | HR Director | 2026-12-31 |
| Reporting never exercised | 6.16-1; 101.620(b)(7); 101.305(a)-(b) | Moderate (in force) | Reporting step in every drill; cyber examples in both FSPs | Security Manager (alternate CySO) | 2026-11-18 |
| Cyber records and T2 records not protected | 101.640; 105.225(b), (c) | Moderate (in force) | Cyber records in the FSO records system; T2 PACS into a security zone | Director of Port Security (T1 FSO) | 2026-12-31 |
| SSI rules not applied to cyber documents | 101.630(b); 1520.9 | Moderate (in force) | SSI handling standard (STD-10); vendor SSI terms | Director of Port Security (T1 FSO) | 2026-12-31 |
| Cybersecurity Assessment, Plan and FSA updates | 101.650(e)(1); 101.630; 101.655; 105.305 | Moderate | Assessment 2027-03-31; Plan draft 2027-04-30; FSAs updated 2027-04-30; submission 2027-05-28 | Director of IT and Cybersecurity (CySO) | 2027-05-28 |

**Program roadmap by quarter:**
| Quarter | Milestones |
|---|---|
| 2026 Q4 | OEM appliance off by default (2026-10-15); default passwords changed (2026-10-31); TOS failover test (2026-11-07); second cyber drill with key personnel role training (2026-11-18); Cyber Incident Response Plan, contingency standard and T2 backups (2026-12-31); all vendors on the remote access service; training catch-up; SSI standard; FTP retired |
| 2027 Q1 | Gate module accounts in the identity provider and logging standard (2027-01-31); T2 network analysis (2027-02-28); pre-submission meetings with both COTPs; T2 OT zone, privileged access management, OT inventory, network map, approved list and allowlisting, T2 server replacement (2027-03-31); Cybersecurity Assessment complete (2027-03-31) |
| 2027 Q2 | Plan draft and FSA updates (2027-04-30); Plan submitted to both COTPs (2027-05-28); 2027 annual exercises with a cyber scenario and the first independent FSP audits (2027-06-30) |
| 2027-07-16 | Regulatory deadline for the Assessment and Plan submission |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
- **No change to Subpart F is pending for facilities.** The final rule asked for comment on a possible delay of the implementation periods for **U.S.-flagged vessels** only (90 FR 6298). A Federal Register search on 2026-10-04 found no later rule or proposal amending Subpart F, and eCFR shows no version after 2025-07-16. The `pending_rule_change` column is "None" on every row.
- **CIRCIA** (6 U.S.C. 681-681g): the final rule had not been published as of 2026-09-25. It is not treated as a current obligation (see P08).
- **CTPAT** is voluntary. A 2027 decision by the PE sponsor could add its cybersecurity criteria; they are not assessed here.

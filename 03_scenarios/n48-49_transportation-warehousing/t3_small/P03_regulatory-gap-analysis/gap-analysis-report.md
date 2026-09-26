# Regulatory Gap Analysis: Cris Santos Company | Transportation and Warehousing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (marine cargo terminal operator, NAICS 488320) |
| Tier / Vertical | Small / Transportation and Warehousing |
| Regulation analyzed | USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101, Subpart F (101.600-101.670). Final rule 90 FR 6298 (2025-01-17), effective 2025-07-16. Text checked against eCFR as of 2026-09-23: no amendments since the effective date |
| Secondary regulation | Maritime cyber incident reporting, 33 CFR 6.16-1 (as amended by E.O. 14116, 89 FR 13973), with the related MTSA reporting duties in 33 CFR 101.305 |
| Assessment dates | 2026-07-20 to 2026-07-31 |
| Assessor | IT Manager (proposed Cybersecurity Officer) with the Security and Safety Manager (FSO) |
| Requirement ID | N48-49-R01 (primary). Regulatory driver columns in P01, P02, P04, P06 and P07 cite N48-49-R01 plus the section |

## 1. Applicability
Subpart F **applies**. Section 101.605(a) covers "the owners and operators of U.S.-flagged vessels, facilities, and OCS facilities required to have a security plan under 33 CFR parts 104, 105, and 106." The terminal must have a Facility Security Plan because it receives foreign cargo vessels greater than 100 gross register tons (33 CFR 105.105(a)(4)), and it has a Coast Guard-approved FSP.

There is **no size threshold or small-business exemption**. After completing the Cybersecurity Assessment, an owner or operator may seek a waiver or an equivalence determination, and must notify the Captain of the Port (COTP) of any temporary deviation (101.665).

**Compliance dates (verified in the regulation text and the final rule preamble):**

| What | When | Source |
|---|---|---|
| Rule effective; reporting of reportable cyber incidents to the National Response Center (NRC) if not reported under 6.16-1 | 2025-07-16 | 90 FR 6298 (DATES); 101.620(b)(7), 101.650(g)(1) |
| Training for all personnel and key personnel | 2026-01-12, then annually | 101.650(d)(4) |
| CySO designation in writing | Within the 24-month implementation period (by 2027-07-16) | Final rule preamble (90 FR 6298), citing 101.620(b)(3) |
| First Cybersecurity Assessment | No later than 2027-07-16, then annually | 101.650(e)(1) |
| Cybersecurity Plan submitted to the Coast Guard | No later than 2027-07-16 | 101.655 |

**How the cybersecurity measures are dated.** The measures in 101.650(a) to (i) must be "in place and documented" in named sections of the Cybersecurity Plan. The company treats them as due when the Plan is submitted, and aims to have them in place by then. This is the company's reading of the text. It will be confirmed with the COTP at the pre-submission meeting planned for 2027-Q1.

**Other transportation requirements considered and excluded:**
- TSA Security Directives for rail, pipeline and aviation (N48-49-R02 to R04): the company is none of these.
- CMMC (N48-49-R07): no DoD contracts.
- SEC disclosure (N48-49-R08): private company.
- CTPAT (N48-49-R05): voluntary; the company is not a partner. Its minimum security criteria are noted for 2027.

**Secondary regulation.** 33 CFR 6.16-1 requires evidence of "an actual or threatened cyber incident involving or endangering any vessel, harbor, port, or waterfront facility" to be reported immediately to the FBI, CISA and the COTP. A report to the Coast Guard under 6.16-1 also satisfies the Subpart F duty to report to the NRC (101.620(b)(7)). The MTSA reporting rules in 101.305 (suspicious activity, breaches of security, transportation security incidents) already apply through the FSP. They were checked for cyber coverage.

## 2. Method
1. **Requirements.** Rows follow the regulation's own structure: each paragraph of 101.620 to 101.665 that imposes a duty, at the most granular citation that is separately verifiable. Definitions (101.615), purpose (101.600), applicability (101.605), federalism (101.610) and severability (101.670) set context and have no rows. Brief quotes are used; this is public-domain federal text.
2. **Requirement type.** The `requirement_type` column records when each duty takes effect, using the dates in section 1.
3. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. **This is an author mapping.** NIST has not published an official mapping for Subpart F.
4. **Evidence.** Current state was established by interviews (General Manager, IT Manager, FSO, Operations Manager, Maintenance Manager, HR Specialist, the MSP), document review (FSP, FSA, contracts, training export), configuration exports, and a walkthrough of the gate complex, the gate server room and an STS crane electrical house on 2026-07-24.
5. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable. "Not applicable" is used only for duties that are not yet triggered (they start after Plan approval or at renewal) or are optional. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 101.620 Owner or operator | 0 | 3 | 4 | 1 |
| 101.625 Cybersecurity Officer | 0 | 1 | 2 | 0 |
| 101.630 Cybersecurity Plan | 0 | 1 | 3 | 2 |
| 101.635 Drills and exercises | 0 | 2 | 1 | 0 |
| 101.640 Records | 0 | 1 | 0 | 0 |
| 101.645 Communications | 0 | 1 | 1 | 0 |
| 101.650 Cybersecurity measures (a) to (i) | 0 | 14 | 23 | 2 |
| 101.655 to 101.665 Dates, documentation, waivers | 0 | 0 | 1 | 2 |
| Secondary: 6.16-1 and 101.305 | 1 | 2 | 1 | 0 |
| **Total (69)** | **1** | **25** | **36** | **7** |

**Reading the result.** Of the 61 Not met or Partially met rows, **12 are overdue or already in force**: 4 in force since 2025-07-16 (owner responsibility, NRC reporting twice, records), 5 training rows past the 2026-01-12 deadline, the 6.16-1 reporting duty, and 2 MTSA reporting rows. **The other 49 fall due by 2027-07-16.** Most "Not met" results reflect a program that started in July 2026, not a refusal to comply. The overdue items are the priority.

Gap risk for the 61 rows: 8 High, 37 Moderate, 16 Low.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Crane vendor remote access always on, no justification | 101.650(e)(3)(v) | High | Off by default; per-session enablement; written justification | Maintenance Manager | 2026-10-31 |
| Third-party remote sessions not monitored | 101.650(f)(3) | High | Session service with recording; monthly review | Maintenance Manager | 2026-10-31 |
| No Cyber Incident Response Plan | 101.620(b)(6); 101.650(g)(2) | High | Full plan built around the P08 runbook; tabletop | IT Manager (proposed CySO) | 2026-10-31 (plan); 2026-11-30 (tabletop) |
| MFA missing on VPN, TOS users and remote OT | 101.650(a)(4) | High | MFA on VPN and all TOS users; MFA-protected vendor sessions | IT Manager (proposed CySO) | 2026-11-30 |
| Backups exposed, incomplete, untested | 101.650(g)(4) | High | Isolated immutable backups; offline gate images and PLC programs; quarterly restore tests | IT Manager (proposed CySO) | 2026-12-31 |
| No IT/OT segmentation or monitoring | 101.650(h)(1)-(2) | High | OT zone behind an internal firewall; log and alert on IT-OT flows | Maintenance Manager; IT Manager | 2027-03-31 |
| Training deadline missed | 101.650(d)(1)-(4) | Moderate (overdue) | All employees, OT and key personnel training; longshore labor briefing; supervision rule | HR Specialist | 2026-11-30 |
| No incident reporting procedure | 6.16-1; 101.620(b)(7) | Moderate (in force) | Reporting checklist and contacts (P08) | Security and Safety Manager | 2026-10-31 |
| No CySO | 101.620(b)(3); 101.625 | Moderate | Written designation of CySO and alternate; 24x7 rota | General Manager | 2026-10-31 |
| No Assessment or Plan | 101.650(e)(1); 101.630; 101.655 | Moderate | Assessment 2027-03-31; Plan draft 2027-04-30; submission 2027-05-31 | General Manager | 2027-05-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
- **No change to Subpart F is pending for facilities.** The final rule asked for comment on a possible 2-to-5-year delay of the implementation periods for **U.S.-flagged vessels** only (90 FR 6298, section VII). A Federal Register search on 2026-09-26 found no later rule or proposal amending Subpart F, and eCFR shows no version after 2025-07-16. The `pending_rule_change` column is therefore "None" on every row.
- **CIRCIA** (6 U.S.C. 681-681g): the final rule had not been published as of 2026-09-25. It is not treated as a current obligation (see P08).
- **CTPAT** minimum security criteria include cybersecurity criteria. The program is voluntary and is not assessed here.

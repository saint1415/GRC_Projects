# Regulatory Gap Analysis: Cris Santos Company | Transportation and Warehousing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-port marine cargo terminal operator, NAICS 488320; 8 terminals in FL, GA, SC and TX) |
| Tier / Vertical | Enterprise / Transportation and Warehousing |
| Primary regulation | USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101, Subpart F (101.600-101.670). Final rule 90 FR 6298 (2025-01-17), effective 2025-07-16. Text checked against eCFR as of 2026-09-23: no amendments since the effective date |
| Also analyzed | Maritime cyber incident reporting (33 CFR 6.16-1); MTSA reporting (33 CFR 101.305); the FSA computer-systems duty (33 CFR 105.305(c)(1)(v)); MARSEC Directives 105-4 and 105-5 (status only; SSI); SEC Form 8-K Item 1.05 and Reg S-K Item 106; state breach and data security laws (Florida worked example); CTPAT (voluntary partner) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the CySO's team; sampling reperformed by Internal Audit for 8 rows |
| Approved | Chief Compliance Officer, CISO and Director of Maritime Cybersecurity (CySO), 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |
| Requirement ID | N48-49-R01 (primary). Regulatory driver columns in P01, P02, P04, P06 and P07 cite N48-49-R01 plus the section |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| 33 CFR Part 101 Subpart F (N48-49-R01) | **Yes, at all 8 facilities** | 101.605(a) covers "the owners and operators of U.S.-flagged vessels, facilities, and OCS facilities required to have a security plan under 33 CFR parts 104, 105, and 106." Each terminal has a Coast Guard-approved FSP because it receives foreign cargo vessels greater than 100 gross register tons (105.105(a)(4)); the container terminals also receive vessels subject to SOLAS chapter XI (105.105(a)(3)). No size threshold or exemption |
| 33 CFR 6.16-1 | **Yes** | The terminals are waterfront facilities in 5 COTP zones |
| 33 CFR 101.305 and 105.305 | **Yes** | MTSA duties already in force through the 8 FSPs and FSAs |
| MARSEC Directives 105-4 and 105-5 | **Yes, at T-03, T-04 and T-07** | Those terminals operate ship-to-shore cranes manufactured by People's Republic of China companies (notices 89 FR 13726 and 89 FR 91413). Directive content is SSI; this analysis records status only |
| SEC Item 1.05 and Item 106 (N48-49-R08) | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| State breach and data security laws | **Yes** | Employee, truck driver and longshore worker personal information; the law of each state where affected individuals reside, with Florida (Fla. Stat. 501.171) as the worked example. The Subpart F federalism clause (101.610) preempts conflicting state or local law for Part 105 facilities, but does not displace state breach notice duties that do not conflict |
| CTPAT (N48-49-R05) | **Voluntary commitment** | Partner since 2019 |
| TSA Security Directives (N48-49-R02 to R04) | **No** | Not a TSA-designated rail, transit, pipeline or aviation operator |
| CMMC and FAR clauses (N48-49-R07) | **No** | No federal or DoD contracts |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25 |
| SOX Section 404 | Separate program | IT general controls over ERP and payroll (SYS-10) are tested by the SOX program and not repeated here |

**Compliance dates (verified in the regulation text and the final rule preamble):**
| What | When | Source |
|---|---|---|
| Rule effective; reporting of reportable cyber incidents to the NRC if not reported under 6.16-1 | 2025-07-16 | 90 FR 6298 (DATES); 101.620(b)(7), 101.650(g)(1) |
| Training for all personnel and key personnel | 2026-01-12, then annually | 101.650(d)(4) |
| First Cybersecurity Assessment | No later than 2027-07-16, then annually, and sooner than annually after a change in ownership | 101.650(e)(1) |
| Cybersecurity Plans submitted to the Coast Guard | No later than 2027-07-16 | 101.655 |

**How the cybersecurity measures are dated.** The measures in 101.650(a) to (i) must be "in place and documented" in named sections of the Cybersecurity Plan. The company treats them as due when the Plans are submitted and aims to have them in place by then. This is the company's reading of the text, discussed with 3 of the 5 COTPs in pre-submission meetings and to be confirmed with the other 2.

**Enterprise features of the rule used here.** One person may be CySO for several facilities if each Plan lists them (101.625(b)); one Plan may cover several facilities of similar operations if it addresses each facility's specific risks (101.630(d)(2)). The company uses both: one CySO for all 8 facilities, one Plan for T-01 to T-07 with facility annexes, and a separate Plan for T-08 until it migrates to ETOP.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Method
1. **Decompose.** Subpart F rows follow the regulation's own structure: each paragraph of 101.620 to 101.665 that imposes a duty, at the most granular citation that is separately verifiable. Definitions (101.615), purpose (101.600), applicability (101.605), federalism (101.610) and severability (101.670) set context and have no rows. Other regulations were broken into citation-level duties from the eCFR text (33 CFR 6.16-1, 101.305, 105.105, 105.225, 105.305 and 17 CFR 229.106, retrieved for 2026-09-23), the Federal Register notices for the MARSEC Directives, the SEC adopting release and the Florida statute. Brief quotes are used; this is public-domain federal text.
2. **Requirement type.** The `requirement_type` column records when each duty takes effect, using the dates in section 1.
3. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. **These are author mappings.** NIST has not published an official mapping for Subpart F or the other rules.
4. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); populations under 250 and lower-risk controls used 25 to 40 items or the whole population; configuration and account data were checked in full with analytics. Selections were random, except OT devices and terminations, which were stratified to cover T-07 and T-08. **37 rows were tested by sampling or full-population analytics; 24 found exceptions.** OT tests followed the P07 rules of engagement (night work, no vessel at berth, OEM present).
5. **Rate.** Met, Partially met, Not met or Not applicable. "Not applicable" is used only for duties that are not yet triggered (they start after Plan approval or at renewal), optional provisions, or rules that do not apply. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| 101.620 Owner or operator | 3 | 4 | 0 | 1 | 8 |
| 101.625 Cybersecurity Officer | 2 | 2 | 0 | 0 | 4 |
| 101.630 Cybersecurity Plan | 0 | 4 | 0 | 2 | 6 |
| 101.635 Drills and exercises | 1 | 2 | 0 | 0 | 3 |
| 101.640 Records | 0 | 1 | 0 | 0 | 1 |
| 101.645 Communications | 2 | 0 | 0 | 0 | 2 |
| 101.650 Cybersecurity measures (a) to (i) | 6 | 31 | 0 | 2 | 39 |
| 101.655 to 101.665 Dates, documentation, waivers | 0 | 1 | 0 | 2 | 3 |
| 33 CFR 6.16-1 cyber incident reporting | 0 | 1 | 0 | 0 | 1 |
| 33 CFR 101.305 MTSA reporting | 3 | 0 | 0 | 0 | 3 |
| 33 CFR 105.305 FSA computer systems | 0 | 1 | 0 | 0 | 1 |
| MARSEC Directives 105-4 and 105-5 | 1 | 1 | 0 | 0 | 2 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| CTPAT (voluntary) | 1 | 1 | 0 | 0 | 2 |
| Other transportation and federal contract rules | 0 | 0 | 0 | 2 | 2 |
| **Total** | **28** | **52** | **0** | **9** | **89** |

**Subpart F alone:** 14 Met, 45 Partially met, 0 Not met, 7 Not applicable (66 rows). No requirement is wholly Not met: the enterprise program already covers every measure somewhere, and the gaps sit at specific terminals (T-07, T-08), in OT, with port partners, or in Plan documents still being written.

**Reading the result.** Of the 52 Partially met rows, **10 are overdue or already in force:** records protection at T-08 (101.640), three training rows past the 2026-01-12 deadline (101.650(d)(1)(v), (d)(3), (d)(4)), the 6.16-1 reporting duty, the FSA update (105.305), one MARSEC Directive 105-5 action, the two SEC Item 1.05 rows, and inherited T-08 vendor contracts under the Florida third-party agent rule. **41 fall due by 2027-07-16**, and 1 is a voluntary CTPAT commitment.

**Gap risk levels across all regulations:** High 12, Moderate 32, Low 8.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-011 | 101.625(d)(15) | 37 OT KEVs open beyond 30 days without documented compensating controls | Compensating control records; OEM patch plan (POAM-006) | Director of OT Engineering | 2026-12-31 |
| G-026 | 101.650(a)(2) | Default passwords on 3 of 60 tested OT devices; compensating controls undocumented | POAM-004 | Director of OT Engineering | 2027-03-31 |
| G-028 | 101.650(a)(4) | No MFA for T-08 legacy TOS users or the 2 OEM tunnels | POAM-001; POAM-002 | Vice President, Integration Management Office | 2027-03-31 |
| G-036 | 101.650(c)(1) | T-07 OT and gate logs and all T-08 logs kept locally for 30 days | SIEM onboarding (POAM-008) | Director of Security Operations | 2027-01-31 |
| G-047 | 101.650(e)(3)(i) | As G-011 | POAM-006 | Director of OT Engineering | 2026-12-31 |
| G-051 | 101.650(e)(3)(v) | Always-on OEM modem at T-08; no justification for 2 OEM tunnels | POAM-002 | Director of OT Engineering | 2026-12-15 |
| G-054 | 101.650(f)(2) | No notice terms with 30 of 96 tier-1 IT and OT vendors, the customs data exchange service or the 6 port community systems | POAM-022 | Director of Third-Party Risk Management | 2027-03-31 |
| G-055 | 101.650(f)(3) | 2 OEM tunnels not monitored or documented | POAM-002 | Director of OT Engineering | 2026-12-15 |
| G-059 | 101.650(g)(4) | ETOP restore 7.5 h against 4 h; failover untested for 8 environments; T-08 backups on the same network and never tested | POAM-005; POAM-020 | Vice President, Terminal Technology | 2027-02-28 |
| G-060 | 101.650(h)(1) | T-07 shared VLAN; T-08 flat network | POAM-003 | Director of Network Engineering | 2027-06-30 |
| G-074 | Form 8-K Item 1.05 | Disclosure process not exercised with current members or for multi-terminal and OT safety events | Playbook update; tabletop 2026-11-18 (POAM-010) | General Counsel | 2026-11-30 |
| G-075 | Form 8-K Item 1.05 (materiality determination) | Escalation timelines never tested end to end with Coast Guard reporting | POAM-010 | General Counsel | 2026-11-30 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Playbook v3 and tabletop with the disclosure committee, CySO and FSOs (POAM-010); OEM gateway onboarding and T-08 modem removal (POAM-002); OT KEV compensating control records (POAM-006); T-08 EDR (POAM-012) and interim backups (POAM-020); contractor and hiring hall training (POAM-016); vendor support accounts into PAM (POAM-015); OCR replacement (POAM-013); T-08 records into the learning system (G-022); second T-08 cyber drill (G-019) | 101.650(e)(3)(i), (v), (f)(3), (d), (g)(4), (a)(5); 101.640; 101.635(b); 6.16-1; Item 1.05 | Tabletop report; gateway records; KEV register; training records |
| 2027 Q1 | Cybersecurity Assessment complete for T-06 to T-08 and FSA annexes (POAM-021); ETOP failover test of all 11 environments (POAM-005); T-07 OT zone (POAM-003); T-08 identity federation with MFA (POAM-001); OT inventory 98% and configuration records (POAM-007); port partner and vendor terms (POAM-022); SL-2 agreement amendments (POAM-011); pre-submission meetings with all 5 COTPs | 101.650(e)(1), (g)(4), (h)(1), (a)(4), (a)(7), (b)(3)-(4), (f)(2); 105.305 | Assessment reports; DR test report; signed addenda |
| 2027 Q2 | Cybersecurity Plans submitted to the COTPs (target 2027-04-30); OT monitoring at T-06 to T-08 (POAM-009); OT approved list and HMI hardening (POAM-023); T-08 migration to ETOP and segmentation (2027-06-30) | 101.630; 101.655; 101.650(b)(1)-(2), (h)(2) | Submission letters; sensor coverage; migration sign-off |
| 2027 Q3 | Deadline 2027-07-16 for the Assessment and Plans; annual risk analysis and gap reassessment; plan the first annual Plan audit by Internal Audit (within 1 year of approval) | All | Updated P01 and P03; audit plan |

## 6. Pending regulatory changes
- **Subpart F:** no amendment or proposal affecting facilities was found. The final rule asked for comment on a possible delay of implementation periods for **U.S.-flagged vessels** only (90 FR 6298). A Federal Register search on 2026-10-04 found no later rule or proposal amending Subpart F, and eCFR shows no version after 2025-07-16. The `pending_rule_change` column says so on every Subpart F row.
- **CIRCIA** (6 U.S.C. 681-681g): the final rule had not been published as of 2026-09-25. It is not treated as a current obligation (see P08).
- **SEC:** no proposal to amend or rescind Item 1.05 or Item 106 was found in the Federal Register as of 2026-10-04.
- **MARSEC Directives** can be issued or revised at any time; the FSOs and the CySO monitor Homeport and Coast Guard notices.

## 7. Regulator-ready package
The GRC team and the CySO keep an evidence binder, indexed by `req_id`, so the company can respond quickly to a COTP inspection or Plan review, a CTPAT validation, or an SEC comment letter. SSI items are kept in the SSI repository and shared only with covered persons with a need to know (49 CFR part 1520):
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk register (input to the Assessment), P02 SSP, P04 architecture, P05 BIA, P06 policy set, P07 assessment and POA&M, and the P08 runbook;
- the CySO designation letters and the 24x7 contact test log;
- training, drill and exercise records kept for at least 2 years (101.640; 105.225);
- the 6.16-1 reporting log with COTP, FBI and CISA reference numbers;
- the MARSEC Directive action tracker (SSI);
- the materiality playbook and disclosure committee minutes.

## 8. Approval
Approved by the Chief Compliance Officer, the CISO and the CySO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, aligned with the first Cybersecurity Assessment.

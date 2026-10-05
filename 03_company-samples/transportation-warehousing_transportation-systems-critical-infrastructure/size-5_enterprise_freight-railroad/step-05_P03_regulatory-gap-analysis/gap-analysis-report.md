# Regulatory Gap Analysis: Cris Santos Company | Transportation Systems | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company of 64 freight railroads: 60 Class III and 4 Class II, in 27 states) |
| Tier / Vertical | Enterprise / Transportation Systems |
| Primary regulation | TSA Security Directive 1580/82-2022-01E, Rail Cybersecurity Mitigation Actions and Testing (effective 2026-05-03 to 2027-05-02), analyzed section by section with SD 1580-21-01E, Enhancing Rail Cybersecurity (effective 2026-01-16 to 2027-01-15) |
| Other regulations analyzed | 49 CFR part 1570 (Security Coordinator, significant security concern reports, training rules); 49 CFR part 1580 subparts B and C; 49 CFR part 1520 (SSI); 49 CFR part 236 subpart I (PTC); 49 CFR part 225; hazmat security plan and training (49 CFR 172.800 to 172.802, 172.704, 174.9); FRA track and freight car inspection (213.233, 215.13) as context for AI; SEC Form 8-K Item 1.05 and Reg S-K Item 106; state breach laws (Florida worked example); state AI employment laws; 33 CFR 6.16-1 |
| Assessment dates | 2026-06-01 to 2026-07-31 (applicability confirmed 2026-06-05; evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Assistant Vice President, Rail Security and the General Counsel's office; sampling reperformed by Internal Audit for 8 rows |
| Approved | CISO and General Counsel, 2026-08-21; roadmap reviewed by the board safety, security, and risk committee, 2026-09-10 |

## 1. Applicability
The brief for this sample asked whether the TSA rail cyber directives apply. They apply only to freight railroads described in 49 CFR 1580.101 or designated by TSA (SD 1580-21-01E Sec. II.A; SD 1580/82-2022-01E Sec. II.A.1). None of the company's railroads is Class I (49 CFR part 1201, General Instructions 1-1), so the test is 1580.101(b) and (c), railroad by railroad.

| Regulation | Applies? | Basis |
|---|---|---|
| SD 1580/82-2022-01E and SD 1580-21-01E (C-TRANSPORTATION-R01) | **Yes, to 10 Covered Railroads** | CR-01 to CR-06 and CR-10 transport RSSM in an HTUA (1580.101(b)); CR-07 to CR-09 host passenger operations described in 1582.101 (1580.101(c)). Florida worked example: CR-01 and CR-02 carry PIH inside the Jacksonville and Tampa HTUAs. TSA has not designated the other 54 railroads |
| 49 CFR 1570.201 and 1570.203 (S01) | **Yes, all 64 railroads** | Each is a freight railroad carrier on the general railroad system (1580.1(a)(1)) |
| 49 CFR part 1580 subpart C (S02) | **Yes, 31 railroads** | They transport RSSM (1580.201). Not Class I, so the 30-minute answer applies (1580.203(d)) |
| 49 CFR part 1580 subpart B training (S09) | **Yes, CR-01 to CR-10** | 1580.101 railroads must have a TSA-approved security training program (1580.113, 1580.115) |
| 49 CFR part 1520 (S03) | **Yes** | Covered persons under 1520.7(n); the CIP, CAP, and results are SSI (SD 1580/82-2022-01E Sec. IV.B) |
| 49 CFR part 236 subpart I (S04) | **Yes, in two ways** | Host duty on CR-07 to CR-09 (236.1005(b)(1)); tenant duty on 22 railroads that run more than 20 miles on Class I PTC lines (236.1006(a), (b)(4)(iii)) |
| 49 CFR part 225 (S05); hazmat rules (S06); 213.233 and 215.13 (S08) | **Yes** | All railroads; PIH carriage triggers the security plan (172.800(b)(5)) |
| SEC Item 1.05 and Item 106 (S10) | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| State breach laws (S07) | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example |
| State AI and automated decision laws (S11) | **Yes, for AI-007** | Colorado SB26-189 from 2027-01-01; Illinois Public Act 103-0804 |
| 33 CFR 6.16-1 (R05) | **Yes, in part** | 2 port switching railroads work inside port facilities; a cyber incident involving or endangering those facilities must be reported immediately |
| SD 1582-21-01E (R01, passenger); pipeline (R02); aviation (R03); USCG subpart F (R04) | **No** | No passenger, pipeline, or aviation operations; no vessel or facility with an MTSA security plan |
| TSA surface cyber NPRM (R06); CIRCIA (R07) | **Not in force** | Proposed rules; tracked in the `pending_rule_change` column and section 6 |
| SOX Section 404 | Separate program | IT general controls over ERP and revenue are tested by the SOX program and not repeated here |

## 2. Method
1. **Decompose.** The two SDs were broken into section-level duties from the TSA-published texts (not marked SSI). Federal rules were broken into citation-level duties from eCFR text (point in time 2026-09-23) for 49 CFR 1570.105, 1570.111, 1570.121, 1570.201, 1570.203, 1580.101, 1580.203, 1580.205, 1520.9, 236.1005, 236.1006, 236.1023, 236.1029, 236.1033, 225.9, 225.11, 172.704, 172.800, 172.802, 174.9, 213.233, 215.13, 17 CFR 229.106, and 33 CFR 6.16-1. Florida rows use the statute text.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. NIST has published no official mapping for these TSA or DOT texts, so every mapping is an **author mapping** and is labeled that way.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls used 25 items; small populations, configurations, and account data were checked in full with analytics. Selections were random. **37 rows were tested by sampling or full-population analytics; 16 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

**CIP-specific rule.** Where the TSA-approved CIP commits to a measure, the gap is measured against the CIP as well as the SD text, because the CIP "sets the security measures and requirements against which TSA inspects for compliance" (SD 1580/82-2022-01E Sec. I).

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| SD 1580/82-2022-01E (R01) | 32 | 16 | 3 | 3 | 54 |
| SD 1580-21-01E (R01) | 12 | 5 | 0 | 0 | 17 |
| 49 CFR part 1570 (S01) | 5 | 1 | 0 | 0 | 6 |
| 49 CFR part 1580 subpart C (S02) | 5 | 1 | 0 | 0 | 6 |
| 49 CFR part 1580 subpart B training (S09) | 3 | 1 | 0 | 0 | 4 |
| 49 CFR part 1520 SSI (S03) | 2 | 1 | 0 | 0 | 3 |
| 49 CFR part 236 subpart I PTC (S04) | 8 | 1 | 0 | 0 | 9 |
| 49 CFR part 225 (S05) | 2 | 0 | 0 | 0 | 2 |
| Hazmat security plan, training, inspection (S06) | 3 | 0 | 0 | 0 | 3 |
| FRA track and freight car inspection (S08) | 2 | 0 | 0 | 0 | 2 |
| SEC Form 8-K Item 1.05 (S10) | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 (S10) | 4 | 0 | 0 | 0 | 4 |
| State breach notification laws (S07) | 2 | 2 | 0 | 0 | 4 |
| State AI and automated decision laws (S11) | 0 | 2 | 0 | 0 | 2 |
| 33 CFR 6.16-1 (R05) | 1 | 0 | 0 | 0 | 1 |
| Not applicable vertical requirements (R01 passenger, R02 to R04) | 0 | 0 | 0 | 4 | 4 |
| **Total** | **82** | **32** | **3** | **7** | **124** |

**Primary regulation (SD 1580/82-2022-01E):** 32 Met, 16 Partially met, 3 Not met, 3 Not applicable (54 rows). The three Not met rows are all access and patching measures in Sec. III: former employees still knowing shared account passwords (III.C.4.b, G-023), no domain trust review schedule (III.C.5, G-024), and no documented mitigations for unpatched PTC servers (III.E.3, G-041).

**Gap risk levels across all regulations:** High 19, Moderate 14, Low 2 (35 gaps).

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-004 | SD-2022 Sec. II.A.3 | Crossing monitor vendor acts on CCS networks without CIP terms | Contract amendment; PAM (POAM-008) | Director of OT Security | 2027-01-31 |
| G-007 | SD-2022 Sec. II.B.2 | 4 CIP measures behind schedule | POAM-003; POAM-004; POAM-005; POAM-007 | CISO | 2027-03-31 |
| G-008 | SD-2022 Sec. III.A | CR-10 Critical Cyber Systems outside the company CIP; vendor modems not identified | POAM-002; POAM-009 | CISO | 2027-02-28 |
| G-013 | SD-2022 Sec. III.B.1.b | 2 external connections missing from the list | POAM-008; POAM-018 | Director of OT Security | 2027-01-31 |
| G-016 | SD-2022 Sec. III.B.2.a | Unauthorized cross-zone paths | POAM-008; POAM-018 | Director of OT Security | 2027-01-31 |
| G-019 | SD-2022 Sec. III.C.1.b | Default credentials; no mitigations for field device classes | POAM-012 | Director of OT Security | 2026-10-31 |
| G-021 | SD-2022 Sec. III.C.3 | Corporate groups hold OT permissions through the directory trust | POAM-005 | Director of OT Security | 2026-12-31 |
| G-022 | SD-2022 Sec. III.C.4 | 3 shared CTC administrator accounts | POAM-004 | Director of OT Security | 2026-11-30 |
| G-023 | SD-2022 Sec. III.C.4.b | Former employees know shared passwords (Not met) | Rotated 2026-09-02; retire (POAM-004) | Director of OT Security | 2026-11-30 |
| G-024 | SD-2022 Sec. III.C.5 | No trust review schedule (Not met) | STD-02.4; POAM-005 | Director of Identity and Access Management | 2026-12-31 |
| G-035 | SD-2022 Sec. III.D.3.a | 39% of OT log sources not collected | POAM-007 | Director of Security Operations | 2027-03-31 |
| G-038 | SD-2022 Sec. III.E.1 | PTC critical patches not current | POAM-003 | PTC Back Office Manager | 2026-12-31 |
| G-041 | SD-2022 Sec. III.E.3 | No mitigations or timeline for unpatched PTC servers (Not met) | POAM-003 | PTC Back Office Manager | 2026-12-31 |
| G-053 | SD-2022 Sec. VI.A, VI.D | CR-10 amendment filed 68 days late | POAM-002 | CISO | 2027-02-28 |
| G-066 | SD-21 Sec. II.D.1.c | Manual CTC operations not proven on 9 signaled railroads | POAM-020 | Vice President, Network Operations | 2027-06-30 |
| G-080 | 49 CFR 1580.203(d) | No tested RSSM answer when the TMS is down | POAM-019 | Assistant Vice President, Rail Security | 2026-11-30 |
| G-097 | 49 CFR 236.1033(f) | PTC restoration plan not achievable as written | POAM-006 | Director of Train Control Systems | 2027-03-31 |
| G-107 | Form 8-K Item 1.05(a) | Disclosure process untested with current members | POAM-010 | General Counsel | 2026-11-30 |
| G-108 | Item 1.05 Instruction 1 | Escalation timelines never tested end to end | POAM-010 | General Counsel | 2026-11-30 |

SD-2022 means SD 1580/82-2022-01E; SD-21 means SD 1580-21-01E.

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Default credentials changed (POAM-012); shared CTC accounts retired (POAM-004); directory trust removed and STD-02.4 trust schedule (POAM-005); PTC compensating measures filed with the CIP (POAM-003); merged TSA/CISA/SEC playbook and tabletop 2026-11-18 (POAM-010); RSSM fallback tested (POAM-019); CR-10 training (POAM-023); AI-007 notices and assessment (POAM-024); AQ-06 VPN blocked (POAM-018 interim) | SD-2022 III.C, III.E.3; SD-21 II.C.4; 1570.203; 1580.203(d); 1580.115; Item 1.05; Colorado SB26-189 | Account inventories; trust removal record; CIP filing; tabletop report; drill records; training records |
| 2027 Q1 | Crossing monitor vendor behind PAM (POAM-008); CR-10 integrated into the company CIP and CIRP (POAM-002); PTC failover automation and retest (POAM-006); OT log forwarding (POAM-007); OT inventory and passive detection (POAM-009; POAM-014); AI-001 and AI-002 local validation (POAM-022) | SD-2022 II.A.3, III.A, III.B, III.D.3, VI.A; 236.1033(f); 213.233 and 215.13 context | Vendor access records; TSA amendment approval; DR retest report; SIEM coverage report |
| 2027 Q2 | Manual CTC operations exercised on all signaled railroads (POAM-020); code line encryption on 3 Class II railroads (POAM-013); AQ-06 CAD migration and SD-WAN (POAM-018 final) | SD-21 II.D.1.c; SD-2022 III.B.2.b | Exercise reports; circuit test results |
| 2027 Q3 | Annual gap reassessment; check SD renewals (SD 1580-21-01E expires 2027-01-15; SD 1580/82-2022-01E expires 2027-05-02) and the status of the NPRM and CIRCIA | All | Updated P01 and P03 |

## 6. Pending regulatory changes
- **SD renewals.** Both SDs are renewed about once a year. SD 1580-21-01E expires 2027-01-15 and SD 1580/82-2022-01E expires 2027-05-02. The GRC team compares each renewal with the prior letter (TSA highlights revisions in bold) and updates this analysis within 30 days.
- **TSA Enhancing Surface Cyber Risk Management NPRM** (89 FR 88488, 2024-11-07) is **still proposed**; no final rule was found in the Federal Register as of 2026-09-25. It would codify cyber risk management requirements for certain rail operators. The SDs remain the operative requirements, and nothing in the NPRM is treated as a current obligation.
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting under the proposed rule is not required; the SD and 1570.203 reports remain the binding ones.
- **Colorado SB26-189** takes effect 2027-01-01; Attorney General rulemaking may add detail.

## 7. Regulator-ready package
The GRC team keeps an evidence binder, indexed by `req_id` and stored in the SSI library where it contains SSI, so the company can respond quickly to a TSA inspection or records request (SD 1580/82-2022-01E Sec. IV.C), an FRA audit, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the CIP, CAP, latest CAP report, architecture design review, CIRP, and exercise records;
- the asset inventory, firewall rule exports, network diagrams, and a procedure to capture up to 24 hours of packet capture on TSA request;
- the P01 risk register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- CISA and TSA report copies, coordinator filings, and RSSM drill records;
- training records (five years, 1570.121) and custody records (60 days minimum, 1580.205(h)).

## 8. Approval
Approved by the CISO and the General Counsel on 2026-08-21. The roadmap was reviewed by the board safety, security, and risk committee on 2026-09-10. Next reassessment: 2027-06 to 2027-07, or within 30 days of an SD renewal with substantive changes.

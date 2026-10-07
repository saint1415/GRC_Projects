# Regulatory Gap Analysis: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded independent crude oil producer, NAICS 211120; Permian, Mid-Continent, and Florida) |
| Tier / Vertical | Enterprise / Mining, Quarrying, and Oil and Gas Extraction |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, all 106 subcategories), applied to OT with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security*. **Voluntary benchmark: no binding federal sector cybersecurity rule applies** (section 1) |
| Binding rules analyzed | SEC Form 8-K Item 1.05 and Reg S-K Item 106; PHMSA gathering line duties (49 CFR 195.11, 195.15, and Subpart B reporting); EPA oil discharge notice (40 CFR 110.6) and the SPCC high-level alarm option (40 CFR 112.9(c)(4)(iv)); state breach and data security laws (Florida worked example). Applicability screens for N21-R01, N21-R02, N21-R03, and PHMSA control room management (49 CFR 195.446) |
| Assessment dates | 2026-06-01 to 2026-07-31 (IOC, BCC, Florida control room, AQ-MC control room, and field site walkthroughs in June and July); evidence sampling completed 2026-08-14 |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Director of OT Security; Pipeline Compliance Manager and Vice President, HSE for the PHMSA and EPA rows; applicability reviewed with outside counsel; sampling reperformed by Internal Audit for 10 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |
| Workbook | `gap-analysis.csv` (133 rows) |
| Regulatory driver label | `N21-BM` in the other deliverables points to this benchmark (see `../00_company-facts.md` section 5) |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| NIST CSF 2.0 with SP 800-82 Rev. 3 (`N21-BM`) | **Voluntary benchmark, adopted enterprise-wide** | No binding federal sector cybersecurity rule reaches an onshore producer without TSA-notified pipelines or MTSA facilities. The board adopted CSF 2.0 as the program structure in 2023 and SP 800-82 Rev. 3 for OT in 2024 |
| SEC Form 8-K Item 1.05 and Reg S-K Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| PHMSA, 49 CFR Part 195 (gathering lines) | **Yes, for the company crude gathering lines** | 44 miles meet the regulated rural gathering line criteria (195.11(a)) and follow the 195.11(b) duties; the other 806 or so miles are reporting-regulated-only (195.15) and carry Subpart B reporting only. Only the reporting and release-estimate duties touch cybersecurity and are analyzed here. Produced water lines carry no hazardous liquid under Part 195. Production facility piping and flow lines are excepted (195.1(b)(8)) |
| PHMSA control room management, 49 CFR 195.446 | **No** | Applies to operators of pipeline facilities controlled through SCADA (195.446(a)), but the duties for regulated rural gathering lines are those listed in 195.11(b), which do not include 195.446. The company follows parts of it voluntarily (P02 section 3) |
| EPA, 40 CFR 110.6 and 112.9(c)(4)(iv) | **Yes** | Onshore oil production facilities. The SCADA high-level alarm is the SPCC overfill measure at 31 tank batteries, which makes that alarm a regulatory control |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside (royalty owners live in all 50 states); Florida (Fla. Stat. 501.171) is the worked example. 501.171(8) (disposal of customer records) does not apply because royalty owners, partners, and SL-2 operators are not consumer customers |
| N21-R01 USCG Marine Transportation System cyber rule (33 CFR 101.605) | **No** | No vessel, MTSA facility, or OCS facility |
| N21-R02 TSA Security Directive Pipeline-2021-02G | **No** | TSA has not notified the company that any of its pipelines is critical |
| N21-R03 CIRCIA (proposed 6 CFR Part 226) | **Not in force** | Final rule not published as of 2026-09-25. As proposed, the size test would cover the company (12,000 employees against the 1,250-employee SBA standard for NAICS 211120), so P08 prepares the reporting path now |
| SOX Section 404 | Separate program | IT general controls over hydrocarbon accounting and ERP are tested by the SOX program and are not repeated here |

**Not otherwise relevant:** BSEE (offshore only), MSHA (no cybersecurity rules), DOE (sector risk management agency; guidance only), federal or tribal lease rules (all leases are fee or state), export controls (no EAR-controlled technology identified), FAR clauses (no federal contracts), and PCI DSS (no payment cards accepted).

## 2. Method
1. **Requirements.** Every CSF 2.0 subcategory (106) is one row. The binding rules were broken into citation-level duties from the eCFR text (2026-09-23 versions of 49 CFR 195.1, 195.2, 195.11, 195.15, 195.50, 195.52, 195.54, and 195.446; 40 CFR 110.6 and 112.9; 17 CFR 229.106), the SEC's adopting release for Item 1.05 (Release 33-11216), and the Florida statute text.
2. **OT guidance.** Each CSF row cites the SP 800-82 Rev. 3 section used to judge the OT side (column `sp800_82r3_reference`). SP 800-82 Rev. 3 organizes its framework guidance by CSF 1.1 categories (section 6), so the link from each CSF 2.0 subcategory to an SP 800-82 section is an **author mapping**.
3. **Crosswalk.** SP 800-53 Rev. 5 controls for CSF rows come from NIST's official CSF 2.0 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), kept in full in column `nist_official_sp800_53r5`; column `sp800_53_controls` is the author's selection of the key controls. Binding-rule rows use an author mapping, labeled as such.
4. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); populations under 250 used 25 to 40 items; configuration and account data were checked in full with analytics. Selections were random, and stratified by operating area where AQ-MC or Florida was a known risk. **43 rows were tested by sampling or full-population analytics; 21 found exceptions.**
5. **Rate.** Met, Partially met, Not met, or Not applicable, for each scope entity (enterprise, operating area, AQ-MC). A row is Partially met when the enterprise meets it but an operating area or AQ-MC does not. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| GOVERN (GV) | 23 | 8 | 0 | 0 | 31 |
| IDENTIFY (ID) | 12 | 9 | 0 | 0 | 21 |
| PROTECT (PR) | 10 | 12 | 0 | 0 | 22 |
| DETECT (DE) | 8 | 3 | 0 | 0 | 11 |
| RESPOND (RS) | 8 | 5 | 0 | 0 | 13 |
| RECOVER (RC) | 6 | 2 | 0 | 0 | 8 |
| **CSF 2.0 subtotal** | **67** | **39** | **0** | **0** | **106** |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 4 | 1 | 0 | 0 | 5 |
| PHMSA hazardous liquid pipeline safety (gathering lines) | 6 | 1 | 0 | 1 | 8 |
| EPA oil pollution prevention and discharge notice | 1 | 1 | 0 | 0 | 2 |
| State breach and data security laws (Florida worked example) | 2 | 3 | 0 | 1 | 6 |
| Applicability screens (N21-R01, N21-R02, N21-R03) | 0 | 0 | 0 | 3 | 3 |
| **Total** | **81** | **47** | **0** | **5** | **133** |

**Gap risk levels (47 partially met or not met rows):** High 16, Moderate 24, Low 7.

**Reading the pattern.** The enterprise program meets most of the benchmark at the IOC, the BCC, and in IT and cloud. Almost every gap sits in one of four places: the acquired AQ-MC assets, the Florida control room, field devices on cellular backhaul, and vendor-operated paths into the field. No CSF subcategory is wholly Not met, because each has a working enterprise control that has not yet reached every operating area. The binding rules are largely met; the gaps there are about how they work during a cyber incident: the SEC materiality step for an OT scenario, a PHMSA release estimate when the historian is down, and the SPCC alarm when SCADA is down.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-005 | CSF 2.0 GV.OC-05 | Single carrier for 88% of field modems with no priority restoration term; Integrator A is a single point of failure (DEP-05, DEP-08) | Second carrier at alarm-critical sites; priority restoration term; second certified integrator (POAM-019) | Vice President, Operations Technology and Automation | 2027-06-30 |
| G-026 | CSF 2.0 GV.SC-05 | ESP vendor service agreement, Integrator B transition services agreement, and one crude purchaser ticket data exchange have no security terms; no priority restoration term with the primary carrier | Amend ESP vendor and Integrator B agreements; carrier amendment (POAM-016; POAM-019) | Director of Third-Party Risk Management | 2027-03-31 |
| G-045 | CSF 2.0 ID.RA-07 | 6 of 40 sampled OT changes (AQ-MC and Florida) had no approval record; no automated program compare outside the Permian | Program repository and compare for all regions; automated download block (POAM-006) | Vice President, Operations Technology and Automation | 2027-03-31 |
| G-050 | CSF 2.0 ID.IM-02 | Failover test findings (9 hours against 4) not yet closed; the materiality playbook has never been exercised for an OT scenario | Repeat failover test (POAM-004); OT tabletop with the disclosure committee (POAM-012) | Vice President, Operations Technology and Automation | 2027-02-28 |
| G-053 | CSF 2.0 PR.AA-01 | OT domain and local SCADA accounts outside quarterly certification; AQ-MC still on the seller directory | OT domain under identity governance; quarterly OT certification (POAM-001) | Director of Identity and Access Management | 2027-01-31 |
| G-055 | CSF 2.0 PR.AA-03 | Default credentials on internet-exposed AQ-MC modems and on 3 LACT flow computers (P07, 2026-08-12); shared HMI logins at Florida and AQ-MC; push MFA still allowed for some non-privileged users | Credential remediation (POAM-008); named HMI accounts (POAM-014); phishing-resistant MFA for all users | Director of OT Security | 2026-12-31 |
| G-057 | CSF 2.0 PR.AA-05 | ESP vendor cloud path outside the gateway with setpoint write on 260 drives; always-on integrator tool at AQ-MC | Disable remote write; bring the vendor path under the gateway; remove the integrator tool (POAM-002) | Director of OT Security | 2026-12-31 |
| G-065 | CSF 2.0 PR.PS-01 | Remote programming mode left enabled on some controllers; Florida and AQ-MC baselines undocumented | Remote programming mode off unless ticketed; baselines (POAM-006) | Vice President, Operations Technology and Automation | 2027-03-31 |
| G-071 | CSF 2.0 PR.IR-01 | Florida has no OT DMZ (corporate-to-SCADA rules on one firewall); the AQ-MC VPN reached enterprise file servers in testing | Florida OT DMZ and AQ-MC VPN restriction (POAM-003) | Director of Network Engineering | 2027-03-31 |
| G-073 | CSF 2.0 PR.IR-03 | 9-hour failover against a 4-hour RTO; no standby for the Florida servers | Failover automation (POAM-004); Florida standby on the enterprise platform (POAM-009) | Vice President, Operations Technology and Automation | 2027-02-28 |
| G-078 | CSF 2.0 DE.CM-06 | ESP vendor activity is not visible to the SOC | Bring the vendor path under the gateway (POAM-002) | Director of OT Security | 2026-12-31 |
| G-089 | CSF 2.0 RS.MA-04 | Escalation to the disclosure committee untested for an OT scenario | OT tabletop with the disclosure committee (POAM-012) | General Counsel | 2026-11-30 |
| G-094 | CSF 2.0 RS.AN-08 | No quick method to estimate deferred production for materiality | Production-loss worksheet (POAM-012) | Vice President, Production and Revenue Accounting | 2026-11-30 |
| G-103 | CSF 2.0 RC.RP-05 | Failover took 9 hours; recovery verification steps manual | Failover automation and repeat test (POAM-004) | Vice President, Operations Technology and Automation | 2027-02-28 |
| G-107 | Form 8-K Item 1.05; SEC Release 33-11216 | Playbook has no OT scenario and has never been exercised with the disclosure committee | Add the OT scenario; tabletop 2026-11-19 (POAM-012) | General Counsel | 2026-11-30 |
| G-108 | Form 8-K Item 1.05 (materiality determination); SEC Release 33-11216 | No agreed method to quantify deferred production quickly; escalation timelines never tested for an OT incident | Production-loss worksheet built from P05 values; tabletop (POAM-012) | General Counsel | 2026-11-30 |

## 5. Compliance roadmap
| Quarter | Milestones | Requirements served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Default credentials removed and AQ-MC modems firewalled (POAM-008, 2026-10-31); ESP remote write disabled and vendor path under the gateway (POAM-002); disclosure committee OT tabletop and production-loss worksheet (POAM-012, 2026-11-19); named HMI accounts (POAM-014); SIEM onboarding for Florida and AQ-MC (POAM-011); PHMSA manual estimate method (POAM-021) | PR.AA-03, PR.AA-05, DE.CM-06, RS.MA-04, RS.AN-08; Form 8-K Item 1.05; 49 CFR 195.52(c) | Credential test results; gateway records; tabletop report; SIEM source list; updated release estimate procedure |
| 2027 Q1 | Florida OT DMZ and AQ-MC VPN restriction (POAM-003); IOC-to-BCC failover retest (POAM-004, 2027-02-28); OT change enforcement and program compare for all regions (POAM-006); Florida off-site backups and restore tests (POAM-005); SPCC alarm end-to-end tests (POAM-022); private APN migration (POAM-013); vendor assessments and contract amendments (POAM-016); OT identity governance (POAM-001); owner data clean-up (POAM-023); Internal Audit test of Item 106 statements | PR.IR-01, PR.IR-03, RC.RP-05, ID.RA-07, PR.PS-01, PR.DS-11, GV.SC-05, GV.SC-07, PR.AA-01; 40 CFR 112.9(c)(4)(iv); Fla. Stat. 501.171(6); 17 CFR 229.106 | Rule reviews; failover test report; change and compare reports; restore test reports; alarm test records; signed amendments |
| 2027 Q2 | AQ-MC migration to the enterprise platform (2027-06-30); Florida server and HMI replacement (POAM-009); field device inventory to 98% (POAM-007); OT monitoring at Florida and AQ-MC (POAM-010); second carrier at alarm-critical sites (POAM-019) | ID.AM-01, ID.AM-08, DE.CM-01, GV.OC-05, PR.IR-03 | Migration acceptance; inventory reconciliation; sensor coverage report; carrier contract |
| 2027 Q3 | Annual risk analysis and gap reassessment; recheck CIRCIA and TSA rulemaking status | All | Updated P01 and P03 |

## 6. Pending regulatory changes
None of these is a current obligation. The `pending_rule_change` column flags the affected rows.
- **CIRCIA (N21-R03).** Final rule not published as of 2026-09-25. As proposed, the company would be covered by the size test and would owe 72-hour covered cyber incident reports and 24-hour ransom payment reports to CISA. P08 includes a draft reporting path so the company can update its procedures within 30 days of a final rule (R-053).
- **TSA surface cyber risk management rule** (NPRM 2024-11-07; not final). Relevant only if TSA designates a company pipeline as critical.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **Business changes that would change applicability:** buying a non-rural gathering line or a transmission pipeline (PHMSA control room management, possibly TSA), acquiring offshore or waterfront assets (USCG Subpart F), or federal leases or contracts.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a PHMSA inspection or information request, an EPA SPCC inspection, a state attorney general inquiry, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook and notification matrix;
- PHMSA segment identification records for the 44 regulated rural miles, annual reports, accident reports, and the release estimate procedure;
- SPCC plans for the 31 tank batteries that use the high-level alarm option, with alarm test records;
- disclosure committee minutes and the Item 106 support file;
- the state law matrix from outside counsel.

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, or within 30 days of a CIRCIA final rule.

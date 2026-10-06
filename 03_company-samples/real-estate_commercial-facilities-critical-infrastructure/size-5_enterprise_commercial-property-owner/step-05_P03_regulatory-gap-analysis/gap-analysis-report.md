# Regulatory Gap Analysis: Cris Santos Company | Commercial Facilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded office and retail REIT; 140 properties in FL, TX, GA, NC, AZ, and CA) |
| Tier / Vertical | Enterprise / Commercial Facilities (NAICS 531120) |
| Primary benchmark | CISA Cross-Sector Cybersecurity Performance Goals, Version 2.0 (CPG 2.0), December 2025 (C-COMMERCIAL-FACILITIES-R05). **Voluntary**; adopted as the company baseline in 2026-02 |
| OT tailoring | NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (final) |
| Other rules analyzed | PCI DSS v4.0.1 SAQ P2PE requirements (R01, binding by contract); SEC Form 8-K Item 1.05 and Reg S-K Item 106 (R04); CCPA and the 2026 CPPA regulations on reasonable security, cybersecurity audits, risk assessments, and ADMT (R03); FTC Act Section 5 (R02); state breach and data security laws (Florida worked example); CIRCIA tracked as a pending rule (R06) |
| Assessment dates | 2026-06-01 to 2026-07-31 (property walkthroughs at 24 sampled properties 2026-06-15 to 2026-07-17; evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Privacy Officer and the Director of OT Security; P07 results incorporated 2026-08-28 |
| Approved | CISO and General Counsel, 2026-09-04; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability

### 1.1 What applies at this size
The vertical overlay names the CISA CPGs, with PCI DSS for payment environments, because **no mandatory sector-specific cybersecurity regulation exists for commercial facilities**. At the enterprise size, more rules apply because the company is publicly traded, does business in California, and is far above the SBA size standard. Each candidate was checked:

| Candidate | Applies? | Basis |
|---|---|---|
| CISA CPG 2.0 (R05) | **Voluntary** | CPG 2.0 states that the goals are not mandated by CISA and that organizations are intended to adopt them voluntarily. No size tiers. The company adopted CPG 2.0 as its IT and OT baseline in 2026-02 |
| PCI DSS v4.0.1 (R01) | **Yes, by contract** | Merchant (about 210,000 card transactions a year at 64 offices). The acquirer requires an annual SAQ P2PE. PCI DSS is an industry standard, not law; validation type is set by the acquirer and the payment brands, not by PCI SSC |
| SEC Item 1.05 and Item 106 (R04) | **Yes** | Exchange Act registrant, not a smaller reporting company |
| CCPA and the CPPA regulations (R03) | **Yes** | The company does business in California (16 properties) and its revenue is far above the CPI-adjusted threshold in Cal. Civ. Code 1798.140(d)(1)(A) ($26,625,000 effective 2025-01-01). The business-to-business exemption ended on 2023-01-01, so tenant employee, visitor, and workforce data are in scope |
| CPPA cybersecurity audit (11 CCR 7120-7124) | **Yes** | 7120(b)(2): revenue threshold met and, in the preceding year, sensitive personal information of 50,000 or more consumers (visitor ID scans at California lobbies: more than 500,000 visits a year; driver license numbers are sensitive personal information under 1798.140(ae)(1)(A)). 2026 revenue over $100 million, so the first audit covers 2027-01-01 to 2028-01-01 and its report is due 2028-04-01 (7121(a)(1)) |
| CPPA risk assessments (11 CCR 7150-7157) | **Yes, for listed processing** | Processing sensitive personal information (7150(b)(2)); systematic observation of employees (7150(b)(4)); permitting a vendor to use video to train identity technology (7150(b)(6)). Existing processing must be assessed by 2027-12-31 (7155(b)); submissions for 2026 and 2027 are due 2028-04-01 (7157(a)(1)) |
| CPPA ADMT rules (11 CCR 7200 et seq.) | **Possibly, for AI-006** | ADMT used for a significant decision, which includes allocation or assignment of work for employees. Businesses already using ADMT must comply by 2027-01-01 (7200(b)). Whether AI-006 substantially replaces human decisionmaking is the open question (G-077) |
| FTC Act Section 5 (R02) | **Yes** | No size threshold |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example |
| Other state comprehensive privacy laws | **Tracked by the privacy program** | For example, the cross-sector file lists the Texas law as applying to businesses that are not SBA-small. These are outside the row-by-row analysis here |
| Florida Digital Bill of Rights | **No** | Revenue is above $1 billion, but the company meets none of the other "controller" conditions in Fla. Stat. 501.702 (online advertising revenue, a smart speaker service, or an app store) |
| CIRCIA (R06) | **Not in force** | Final rule not published as of 2026-09-25. Proposed 6 CFR 226.2(a) would cover any entity in a critical infrastructure sector that exceeds its SBA size standard, so the company would be covered as proposed (G-084) |
| SOX Section 404 | Separate program | IT general controls over SYS-07 and SYS-12 are tested by the SOX program and not repeated here |

**Decision.** The binding rules (CCPA reasonable security, the CPPA audit and assessment duties, state "reasonable measures" laws, FTC Section 5, and SEC disclosure duties) do not say what reasonable security is. The company uses CPG 2.0, the Sector Risk Management Agency's own baseline, tailored for OT with SP 800-82 Rev. 3, to define it, and maps each 11 CCR 7123(c) audit component to the same controls (P02). CPG rows are rated like requirements so the roadmap can show gaps, but **a CPG gap is not by itself a legal violation.**

### 1.2 CPG 2.0 version and structure (verified)
Verified against the CPG 2.0 report (*Cross-Sector Cybersecurity Performance Goals, Version 2.0*, December 2025):
- CPG 2.0 replaces CPG 1.0.1 and adds a GOVERN function to align with NIST CSF 2.0.
- **34 goals** in six functions: 1 Govern (1.A-1.E), 2 Identify (2.A-2.E), 3 Protect (3.A-3.S), 4 Detect (4.A-4.B), 5 Respond (5.A-5.B), 6 Recover (6.A).
- Goals include "OT:" guidance lines, used in this analysis, and list NIST CSF 2.0 references and SP 800-82 Rev. 3 control references, used for the crosswalk.

### 1.3 PCI DSS scope and SAQ
- **Card channels.** Card-present and phone bookings at 64 management offices and conference centers, only through 182 terminals from a validated PCI-listed P2PE solution. Rent is paid by ACH. Parking operators are merchants of record at the 84 garages and are **outside the company's PCI scope** (vendor risk, P01 R-039). Amenity bookings in the tenant app are billed to tenant accounts.
- **SAQ.** The acquirer requires an annual **SAQ P2PE** (*PCI DSS v4.0.1 SAQ P2PE*, October 2024). Its eligibility criteria: all processing through a validated PCI-listed P2PE solution; the only systems that handle account data are the solution's terminals; no electronic receipt, transmission, or storage of account data; any retained data is on paper; and all P2PE Instruction Manual (PIM) controls are implemented. The SAQ covers requirements 3 (paper only), 9.4 (paper only), 9.5, 12.1, 12.6, 12.8, and 12.10.1 (9.5.1.2.1 is "intentionally left blank" in this SAQ).
- **Eligibility finding.** Email data loss prevention found no card numbers in 2026, but PIM inspection logs are missing at 9 of 64 offices, and 2 conference centers wrote phone bookings with security codes on paper. The Chief Accounting Officer will sign the 2026 SAQ P2PE only after G-035, G-037, G-038, G-040, G-042, G-045, and G-046 are closed (POAM-022). An online card channel is not in place; adding one would change the SAQ, and the acquirer must be consulted first.
- PCI DSS v4.0.1 is still the current version. PCI SSC ran a request for comments on v4.0.1 from 2026-06-03 to 2026-07-20 toward a next version.

## 2. Method
1. **Decompose.** CPG rows are the 34 goals at goal level, citing the goal ID; summaries paraphrase the goal and its OT line. PCI DSS rows are the eligibility statement plus the 21 requirements listed in the v4.0.1 SAQ P2PE; PCI DSS is copyrighted, so rows list requirement numbers with short topic labels written for this analysis. SEC rows follow 17 CFR 229.106 (verified on eCFR) and Form 8-K Item 1.05 as described in SEC Release 33-11216. CCPA rows cite the statute text published by the CPPA (version updated 2024) and the CPPA regulation text (Cal. Code Regs. tit. 11, 7120-7124, 7150-7157, 7200-7222). Florida rows cite the statute.
2. **Crosswalk.** CPG rows use the CSF 2.0 references published in CPG 2.0, with an SP 800-53 subset selected from the CPG's SP 800-82 Rev. 3 references. For goal 3.O, CPG 2.0 lists PR.IR-01 and DE.CM-01, which repeat goal 3.I; an author mapping (PR.DS-11; CP-9, CP-4, CP-10) is used instead and labeled. All other rows are author mappings, labeled as such.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); smaller populations used 25 to 40 items; configuration, contract, and site data were checked in full. Selections were random. **27 rows were tested by sampling or full-population review; 24 found exceptions.** P07 reperformed the OT samples (CM-8, IA-5, CM-3, IR-4) independently.
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| CPG 2.0 Govern (1.A-1.E) | 5 | 2 | 3 | 0 | 0 |
| CPG 2.0 Identify (2.A-2.E) | 5 | 2 | 3 | 0 | 0 |
| CPG 2.0 Protect (3.A-3.S) | 19 | 2 | 17 | 0 | 0 |
| CPG 2.0 Detect (4.A-4.B) | 2 | 0 | 2 | 0 | 0 |
| CPG 2.0 Respond (5.A-5.B) | 2 | 1 | 1 | 0 | 0 |
| CPG 2.0 Recover (6.A) | 1 | 0 | 1 | 0 | 0 |
| **CPG 2.0 subtotal** | **34** | **7** | **27** | **0** | **0** |
| PCI DSS v4.0.1 SAQ P2PE (eligibility plus 21 requirements) | 22 | 14 | 7 | 0 | 1 |
| SEC Form 8-K Item 1.05 | 3 | 1 | 2 | 0 | 0 |
| SEC Regulation S-K Item 106 | 5 | 4 | 1 | 0 | 0 |
| CCPA and CPPA regulations | 14 | 0 | 12 | 2 | 0 |
| FTC Act Section 5 | 1 | 0 | 1 | 0 | 0 |
| State breach and data security laws (Florida worked example) | 4 | 2 | 2 | 0 | 0 |
| CIRCIA (pending) | 1 | 0 | 0 | 0 | 1 |
| **Total** | **84** | **28** | **52** | **2** | **2** |

The 54 unmet or partially met rows break down by gap risk as **7 High, 34 Moderate, and 13 Low**.

**The pattern.** A mature enterprise program meets most CPG goals at the 121 integrated properties. **Almost every CPG gap traces to the 19 acquired properties, to OT logging and recovery at scale, or to third parties.** No CPG goal is wholly Not met. The California rules are new: the company is in scope for the cybersecurity audit, risk assessments, and possibly ADMT, and nothing is Met yet because the program for them is still being built. The two Not met rows are the CPPA certification designation (7124) and the ADMT pre-use notice (7220). PCI DSS findings are about paper and inspection logs at a few offices, not systems.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-005 | CPG 1.E | Integrator C outside the OT gateway; 3 integrators never assessed | Move Integrator C to the gateway (POAM-003); integrator assessments (POAM-011) | Director of OT Security | 2026-11-30 |
| G-007 | CPG 2.B | Unsupported OT hosts; firmware backlog | Replace hosts (POAM-007); firmware plan (POAM-015) | Senior Vice President, Engineering | 2027-06-30 |
| G-016 | CPG 3.F | Vendor remote access to Platform C without MFA | Gateway with MFA (POAM-003) | Vice President, Integration Management Office | 2026-11-30 |
| G-019 | CPG 3.I | 19 acquired properties unsegmented; seller VPN reaches the hub | Interim access lists 2026-10-31; OT zones and SD-WAN (POAM-004) | Director of Network Engineering | 2027-03-31 |
| G-025 | CPG 3.O | Platform C without backups; Platform B restore misses RTO | Backups and escrow; restore automation (POAM-008) | Senior Vice President, Engineering | 2027-03-31 |
| G-057 | Form 8-K Item 1.05 | Process not exercised for a building outage; new committee members | Tabletop 2026-11-17 (POAM-012) | General Counsel | 2026-11-30 |
| G-058 | Form 8-K Item 1.05 (materiality determination) | Worksheet lacks building-outage quantification from the BIA | Add P05 values (POAM-012) | General Counsel | 2026-11-30 |

## 5. Compliance roadmap
| Quarter | Milestones | Rules served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Integrator C to the OT gateway (POAM-003); interim access lists at acquired properties (POAM-004); building-outage tabletop and worksheet update (POAM-012); default password remediation (POAM-009); paper card data eliminated and inspection logs at all offices before the 2026 SAQ (POAM-022); CPPA auditor model, 7123 component map, and certifying executive (POAM-020); visitor ID purge (POAM-019); ADMT decision for AI-006 before 2027-01-01 (POAM-023); West tenant training opt-out (POAM-024) | CPG 1.E, 3.F, 3.A, 1.C; Item 1.05; SAQ P2PE; 11 CCR 7122-7124, 7200; 1798.100(a)(3); Fla. Stat. 501.171(8) | Gateway session records; tabletop report; SAQ P2PE; audit plan; purge certificates; ADMT design record |
| 2027 Q1 | OT zones and SD-WAN at the acquired properties (POAM-004); Platform C backups and Platform B restore within RTO (POAM-008); inherited contracts amended (POAM-011); OT inventory to 98% (POAM-006); legacy PACS migration; CPPA risk assessment for visitor ID scanning (POAM-021) | CPG 3.I, 3.O, 1.D, 2.A; 11 CCR 7150; Fla. Stat. 501.171(6) | Firewall exports; restore test reports; amended contracts; risk assessment |
| 2027 Q2 | Platform C replaced (POAM-007); OT log onboarding and passive monitoring at all properties (POAM-005); Internal Audit test of Item 106 statements | CPG 2.B, 3.Q, 4.A, 4.B; Item 106; 11 CCR 7123(c) | Replacement records; SIEM source list; audit memo |
| 2027 Q3 | Annual risk analysis and gap reassessment; CPPA audit fieldwork planning for the 2027 period; review CIRCIA status | All | Updated P01 and P03 |

## 6. Pending regulatory changes (status checked 2026-09-25, after approval)
- **CIRCIA:** the final rule had not been published as of 2026-09-25. As proposed (6 CFR 226.2(a)), the company would be covered because it exceeds the SBA size standard for NAICS 531120. The statute sets 72 hours for a covered cyber incident and 24 hours after a ransom payment; these are not current obligations. CPG 5.B already points reporting toward CISA voluntarily.
- **SEC:** no SEC proposal to amend or rescind Item 1.05 or Item 106 was found as of 2026-09-25, so both remain in force.
- **PCI DSS:** the June-July 2026 request for comments starts work on the next version. No publication date was found. v4.0.1 remains in force.
- **NIST SP 800-82 Rev. 4** is an initial public draft (2026-09-21). It is not used; Rev. 3 remains the final guide.
- **CPG 2.0** states a targeted revision cycle of 24 to 36 months.

None of these is treated as a current obligation.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a CPPA inquiry or audit, a state attorney general request, an SEC comment letter, or an acquirer request:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- the 7123(c) component-to-evidence map and the auditor independence decision (for the 2027 cybersecurity audit);
- CPPA risk assessments as they are completed (P10 links the AI-related ones);
- the signed SAQ P2PE and the acquirer correspondence;
- document retention of at least 7 years for security records (POL-01 4.11).

## 8. Approval
Approved by the CISO and the General Counsel on 2026-09-04. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.

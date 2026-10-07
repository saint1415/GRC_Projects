# Regulatory Gap Analysis: Cris Santos Company | Transportation Systems | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (Class III short line freight railroad, north-central Florida) |
| Tier / Vertical | Small / Transportation Systems |
| Primary regulation named for this vertical | TSA Security Directive 1580/82-2022-01E, Rail Cybersecurity Mitigation Actions and Testing (C-TRANSPORTATION-R01): **not applicable**, kept as a readiness reference together with SD 1580-21-01E |
| Binding rules analyzed | TSA: 49 CFR 1570.105, 1570.201, 1570.203 (C-TRANSPORTATION-S01); 49 CFR part 1580 subpart C (S02); 49 CFR 1520.9 (S03). FRA: 49 CFR part 236 subpart I tenant duties (S04). Text read from eCFR, current through 2026-09-23 |
| Cyber benchmark analyzed | NIST CSF 2.0 outcomes, with NIST SP 800-82 Rev. 3 (Guide to OT Security, September 2023) as the OT implementation guide (C-TRANSPORTATION-BM) |
| Assessment dates | 2026-07-13 to 2026-07-24 (applicability confirmed 2026-07-15) |
| Assessor | IT Manager with the Manager of Safety and Security, Vice President of Operations, Chief Dispatcher, and Signal and Communications Supervisor |

## 1. Applicability

### 1.1 TSA rail cybersecurity directives: do not apply
Both current rail cyber directives were read from the TSA-published text (TSA states that neither is Sensitive Security Information):
- **SD 1580/82-2022-01E** (effective 2026-05-03 through 2027-05-02). Its applicability line reads: "Each freight railroad carrier identified in 49 CFR 1580.101 and other TSA-designated freight and passenger railroads." Section II.A.1.b adds that when TSA identifies additional railroads, "TSA will notify these Owner/Operator(s) and provide specific compliance deadlines."
- **SD 1580-21-01E** (effective 2026-01-16 through 2027-01-15) uses the same test: railroads in 49 CFR 1580.101 and "other TSA-designated freight railroads" notified by TSA.

49 CFR 1580.101 lists three kinds of freight railroad: (a) a Class I railroad; (b) a railroad that "transports one or more of the categories and quantities of RSSM in an HTUA"; and (c) a railroad that "serves as a host railroad" to a railroad in (a) or (b) or to a covered passenger operation.

**Finding.** None of the three criteria is met, and TSA has never designated the company:
- **Class:** Class III under the STB revenue classes. Revenue of $36.4 million is below the Class III ceiling that TSA quoted from STB data in the 2024 NPRM ($42.4 million, 89 FR 88488 footnote 123).
- **RSSM in an HTUA:** the company carries about 600 PIH tank cars a year, which are RSSM (1580.3). But its whole route, the trackage-rights segment, and the interchange yard lie outside the Florida HTUAs in Appendix A to part 1580 (Fort Lauderdale, Jacksonville, Miami, Orlando, and Tampa areas, each with a 10-mile buffer). The Manager of Safety and Security checked this against the route map on 2026-07-15.
- **Host railroad:** the Class I does not operate on company track. The company is the tenant on the Class I's line, not the host.
- **Designation:** the President and General Manager and the Manager of Safety and Security confirmed on 2026-07-15 that no TSA notice has been received, and the correspondence file holds none.

The 19 SD rows in `gap-analysis.csv` (G-069 to G-087) are marked Not applicable. Each carries a readiness note pointing to the benchmark row that would close it if TSA designated the railroad. SD 2022-01E Section III.A.2 is worth noting: it would put PTC systems in scope as Critical Cyber Systems for a railroad "required to install and operate PTC under 49 CFR part 236, subpart I." The company's onboard units would be in scope on designation.

### 1.2 TSA rules that do apply
Part 1580 is broader than the directives. 49 CFR 1580.1(a)(1) covers "each freight railroad carrier that operates rolling equipment on track that is part of the general railroad system of transportation," with no size test. Through that section:
- **49 CFR 1570.201** requires a primary and alternate Security Coordinator at the corporate level, reported to TSA within 37 days of any change and reachable 24/7.
- **49 CFR 1570.203** requires reports to TSA "within 24 hours of initial discovery" of potential threats and significant security concerns. Appendix A to part 1570 lists "Cyber Attack" as a reportable category: "Compromising, or attempting to compromise or disrupt the information/technology infrastructure of an owner/operator subject to this part." TSA's published method is a telephone report to the Transportation Security Operations Center (TSOC). **This is the only binding cyber reporting duty the railroad has today**, and the company was not meeting it (G-007, G-008).
- **Part 1580 subpart C** applies because the company transports RSSM (1580.201(1)): location and shipping information to TSA within 30 minutes of a request (1580.203(d)) and chain of custody (1580.205(b) and (d)).
- **Part 1580 subpart B** (security training programs) does not apply, because it uses the same 1580.101 criteria (row G-020).
- **49 CFR 1520.9** applies because 1520.7(n) makes every surface owner/operator subject to subchapter D a covered person for SSI.

### 1.3 FRA positive train control: tenant duties only
- **Own track: not required.** 49 CFR 236.1005(b)(1) requires PTC from "each Class I railroad and each railroad providing or hosting intercity or commuter passenger service." The company is neither.
- **Trackage-rights segment: required on the locomotives.** The company is a "tenant railroad" (236.1003) on 26 miles of the Class I's PTC-equipped main line. 236.1006(b)(4) lets a Class II or III railroad run unequipped trains on PTC track only where each movement does not exceed 20 miles, or, for longer movements, only until 2023-12-31. The company's run is longer than 20 miles, so every controlling locomotive on that segment must carry an operative onboard PTC apparatus (236.1006(a)). That is why 8 locomotives are equipped and why the company buys a hosted PTC back office service.
- **236.1033** (cryptographic message integrity and authentication; key protection; restoration plan) attaches to the PTC system that the host certifies. The company's units and back office service operate inside it, so the rows are assessed for the company's part only.

### 1.4 NIST CSF 2.0 with SP 800-82 Rev. 3 as the cyber benchmark
The binding rules set roles and reporting, not controls. With no binding cyber control rule, the company chose CSF 2.0 because it is sector-neutral, it is the structure TSA's own vulnerability assessment form uses (SD 1580-21-01E Section II.E), and it is the framework SP 800-61 Rev. 3 and the P08 runbook use. SP 800-82 Rev. 3 supplies OT guidance for each outcome.
- SP 800-82 Rev. 3 Chapter 6 is organized by CSF 1.1 categories. This analysis cites SP 800-82 Rev. 3 **section numbers** only and uses CSF 2.0 IDs for the outcomes.
- The 41 CSF 2.0 subcategories (G-028 to G-068) were chosen for relevance to a dispatch and PTC operation. This is not a full CSF profile.

### 1.5 Other rules that touch this work (used in P08, not decomposed here)
- **FRA accident/incident reporting, 49 CFR part 225** (C-TRANSPORTATION-S05): applies to all railroads on the general system (225.3). A cyber event is reportable only if it leads to a reportable accident/incident; immediate telephone reports to the National Response Center for the events in 225.9, and monthly reports within 30 days after the month ends (225.11).
- **Hazmat security plan, 49 CFR 172.800 and 172.802; car inspection, 174.9** (S06): the plan exists and was reviewed in 2026-02.
- **Fla. Stat. 501.171** (S07): employee personal information.

**Not applicable, with reasons:** pipeline, aviation, and maritime rules (C-TRANSPORTATION-R02 to R05); CIRCIA (R07) and the TSA surface cyber NPRM (R06) are proposed only (section 5).

## 2. Method
1. **Requirements.**
   - TSA and FRA rows follow each regulation's own section and paragraph structure, at the most granular citation that imposes a separate duty. Brief quotes are used; this is public-domain federal text.
   - CSF 2.0 rows use the subcategory text from `00_universal-framework/frameworks/csf2_core.csv`, with the SP 800-82 Rev. 3 section that gives OT guidance.
   - SD rows follow the directives' own section numbers.
2. **Crosswalk.**
   - TSA, FRA, and SD rows use an author mapping to CSF 2.0 and SP 800-53 Rev. 5, labeled as such. No official NIST mapping exists for these rules.
   - CSF rows use the official NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). Where an OT-relevant control was added, the `crosswalk_source` column names it as an author addition.
3. **Evidence.** Interviews (President and General Manager, Vice President of Operations, Chief Dispatcher and 2 dispatchers, Manager of Safety and Security, Signal and Communications Supervisor, Chief Mechanical Officer, Car Management and Customer Service Manager, IT Manager, MSP lead), document review (Security Coordinator designation, TSOC report log, TSA location drill record, interchange agreement, trackage-rights agreement, hazmat security plan, contracts), configuration exports, and walkthroughs of the dispatch center (2026-08-05) and one tower site and detector (2026-08-06).
4. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| **A. TSA regulations (binding)** | | | | |
| 49 CFR 1570.105, 1570.201, 1570.203 | 3 | 5 | 1 | 0 |
| 49 CFR part 1580 subpart C (RSSM) | 6 | 1 | 0 | 0 |
| 49 CFR 1520.9 (SSI) | 0 | 1 | 2 | 0 |
| 49 CFR part 1580 subpart B (applicability) | 0 | 0 | 0 | 1 |
| **Subtotal TSA (20)** | **9** | **7** | **3** | **1** |
| **B. FRA 49 CFR part 236 subpart I (binding, tenant duties) (7)** | **4** | **2** | **0** | **1** |
| **C. NIST CSF 2.0 with SP 800-82 Rev. 3 (benchmark)** | | | | |
| Govern | 0 | 5 | 2 | 0 |
| Identify | 1 | 4 | 4 | 0 |
| Protect | 0 | 12 | 3 | 0 |
| Detect | 0 | 1 | 3 | 0 |
| Respond | 0 | 1 | 2 | 0 |
| Recover | 1 | 1 | 1 | 0 |
| **Subtotal CSF (41)** | **2** | **24** | **15** | **0** |
| **D. TSA SD 1580-21-01E and 1580/82-2022-01E (readiness only) (19)** | 0 | 0 | 0 | 19 |
| **Total (87)** | **15** | **33** | **18** | **21** |

Of the 51 unmet or partially met rows, 13 are rated High, 28 Moderate, and 10 Low.

**The pattern.** The hazmat security side of the TSA rules is in good shape: RSSM car location, chain of custody, the 24/7 contact line, and the Security Coordinators all work, because the Safety department has run them for years. The failures sit where security meets IT:
- **The one binding cyber duty is missed.** 1570.203 makes a cyber attack reportable to TSA within 24 hours, and a 2025 incident was not reported (G-007, G-008).
- **The 30-minute TSA location duty has no fallback** if ransomware takes the workstations or the TMS (G-011).
- **The benchmark shows a dispatch platform built for availability, not security:** vendor access always on, no segmentation, no MFA on remote access, no monitoring, and backups that share the fate of production.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Cyber attacks not reported to TSA; no 24-hour procedure | 1570.203(a)(1), (b); Appendix A | High | Cyber triggers and TSOC reporting in POL-03 and P08; train dispatch and IT | Manager of Safety and Security | 2026-10-15 |
| No fallback for the 30-minute RSSM location duty | 1580.203(d) | Moderate | Clean standby laptop; printed RSSM car list every 4 hours | Car Management and Customer Service Manager | 2026-10-31 |
| Vendor remote access always on, shared account, unlogged | CSF PR.IR-01, DE.CM-06 | High | On-request access through a jump host with MFA and session logging | IT Manager | 2026-11-30 |
| No MFA on remote-access VPN and server administrators | CSF PR.AA-03 | High | MFA everywhere remote or privileged | IT Manager | 2026-11-30 |
| No incident response plan; no response capability | CSF ID.IM-04, RS.MA-01 | High | POL-03, P08 runbook, forensic retainer, tabletop | IT Manager | 2026-11-30 |
| Backups exposed and untested | CSF PR.DS-11 | High | Separate immutable backup account; offline copy; quarterly restore | IT Manager | 2026-12-31 |
| No plan to run and recover dispatch without the CAD system | CSF RC.RP-01 | High | Contingency plan; manual dispatch drill | Vice President of Operations | 2026-12-31 |
| Office LAN routes to dispatch; no way to isolate | CSF PR.IR-01, RS.MI-01 | High | Filtered dispatch zone; documented isolation points | IT Manager | 2027-01-31 |
| No monitoring or EDR | CSF DE.CM-01 | High | MSP-managed EDR with 24x7 triage; log workspace | IT Manager | 2027-01-31 |
| Dispatch servers and radio gateway unpatched | CSF PR.PS-02 | High | Vendor-certified patch cycle; compensating controls | IT Manager | 2027-03-31 |
| SSI open to all office staff; no SSI disclosure notice | 1520.9(a), (c) | Moderate | Restricted SSI library; add TSA SSI notice to P08 | Manager of Safety and Security | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01). Gaps tied to the controls assessed in P07 also appear in the P07 POA&M.

## 5. Pending regulatory changes
- **TSA Enhancing Surface Cyber Risk Management NPRM** (89 FR 88488, 2024-11-07; RIN 1652-AA74; C-TRANSPORTATION-R06). **Still proposed:** a Federal Register search on 2026-09-26 found no final rule. As proposed, it would affect this company in two ways, and in a third way it would not:
  - Proposed 1580.311 would require **every** railroad in 1580.1(a)(1) to designate a Cybersecurity Coordinator.
  - Proposed 1580.325 would require **every** such railroad to report reportable cybersecurity incidents to CISA "no later than 24 hours" after identification.
  - The full Cybersecurity Risk Management program (proposed 1580.301(b)) would reach a Class III railroad only if it serves two or more Class I railroads, carries RSSM in an HTUA, hosts a covered railroad, averages at least 400,000 train miles a year, or is a Defense Connector Railroad. The company meets none of these. The preamble says TSA "is not proposing to apply the CRM program requirements to most short line and regional railroads."
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR part 226, 89 FR 23644; C-TRANSPORTATION-R07). The final rule has not been published (CISA announced further town halls in 2026). The proposed sector criterion 226.2(b)(14)(i) would cover "a freight railroad carrier identified in 49 CFR 1580.1(a)(1), (4), or (5)," so this company would likely be covered if the rule is finalized as proposed (72-hour incident reports and 24-hour ransom payment reports).
- **TSA directives** are renewed each year. SD 1580-21-01E expires 2027-01-15 and SD 1580/82-2022-01E on 2027-05-02. Recheck applicability at each renewal and whenever the business changes (1570.105(b)).
- **Voluntary reporting today.** TSA's Information Circular IC Surface-2025-01 (2025-10-25) recommends voluntary reporting of cybersecurity incidents to TSA by owner/operators not covered by the directives. P08 adopts that recommendation alongside the mandatory 1570.203 report.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row. None of these proposals is treated as a current obligation.

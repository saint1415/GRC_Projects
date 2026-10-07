# Regulatory Gap Analysis: Cris Santos Company | Information Technology | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (cloud hosting and managed infrastructure provider) |
| Tier / Vertical | Mid-Market / Information Technology |
| Regulation analyzed | FedRAMP (44 U.S.C. 3607-3616) as implemented by the **FedRAMP Consolidated Rules for 2026**, Rev5 Class C, agency path. **Transition analysis: the Government Cloud already holds a Rev5 Moderate certification and must move to the 2026 rules to keep it** |
| Also analyzed (primary business line) | Bank service provider notification rule (12 CFR 53.4; 225.303; 304.24); DFARS 252.204-7012 cloud provider duties flowed down by defense customers; FAR 52.204-21, -23, -25, -30 in the GSA Schedule contract; DOJ Data Security Program (28 CFR Part 202); Fla. Stat. 501.171(6) as the worked example of state third-party agent duties |
| Assessment dates | Fieldwork 2026-07-06 to 2026-07-31. Statuses updated 2026-09-22 for the P06 policy approvals and the P07 results |
| Assessor | GRC Manager and GRC analysts, with the Federal Program Director, the Security Operations Manager, the Security Engineering Lead, and the General Counsel. The co-sourced internal audit firm re-performed the evidence samples for 40 controls in P07 |
| Sources checked | fedramp.gov Consolidated Rules for 2026 (ruleset pages, Rev5 control list, important dates, changelog through the 2026-09-22 release), retrieved 2026-10-05; eCFR as of 2026-09-23: 12 CFR 53.2-53.4, 225.301, 225.303, 304.22, 304.24; 48 CFR 252.204-7012, 52.204-21; 32 CFR 170.16 |

## 1. Applicability
### 1.1 FedRAMP: applies, and the rules are changing under the company
The Government Cloud has held a FedRAMP Rev5 **Moderate** agency authorization since 2024-05-20, sponsored by a civilian agency and reused by 6 more agencies. FedRAMP has no size threshold (C-IT-R01); it applies because federal agencies use the service.

**What changed (verified on fedramp.gov, 2026-10-05):**
- The Consolidated Rules for 2026 apply to every certification, including legacy Rev5 ones. Rev5 classes are B, C, and D. The company and its sponsoring agency target **Class C**, whose control list covers the Moderate security objectives (rule FRC-CSF-BSL).
- **Each ruleset has its own dates.** "Maintaining" is when an existing certification must follow the ruleset; after it FedRAMP requests corrective action. "Grace period ends" is when an offering that still does not follow it loses its certification. Grace periods cannot be extended.
- **All grace periods end by 2028-02-01.** Offerings not fully following the 2026 rules by then lose their certification.

**Deadlines that drive this company's plan:**
| Ruleset | Maintaining date | Grace period ends | What it means here |
|---|---|---|---|
| AFC (FedRAMP communication), SCG (secure configuration), MKT (Marketplace) | Already passed (2026-01-05, 2026-03-01, 2026-07-04) | Already passed | In force now. The late Emergency Test action (G-003) is a current gap |
| VDR, VER (vulnerability detection, evaluation, reporting) | **2026-12-07** | 2027-03-07 | Mandated by CISA BOD 26-04. The legacy POA&M model must give way to PAIN-based evaluation in about 2 months |
| FRC, IVV, MAS (certification, assessment, scope) | 2027-01-01 | **The first independent assessment started after 2027-01-01** | The 2027 annual assessment is planned to start 2027-02-15, so these grace periods end then, not in 2028 |
| IEC, SCN, CMU (incidents, changes, cryptography) | 2027-01-01 | 2027-06-01 | 1-hour incident reports for PAIN-3 to PAIN-5 from 2027-01-01 |
| CCM (ongoing certification) | 2027-04-02 | 2027-10-01 | First Ongoing Certification Report and Quarterly Review |
| CPO, SDR, CDS (package, decision record, data sharing) | 2027-07-01 to 2027-08-01 | First assessment after 2027-07-01 or 2027-08-01; 2028-02-01 for CDS | Machine-readable package, Security Decision Record, and trust center |

**Path.** The company keeps its Rev5 agency certification (FRC-CSO-POP: it will not seek both Rev5 and 20x program certifications). New Rev5 applications end 2027-06-11, but that cutoff concerns new certifications, not maintaining this one. A move to 20x is a 2028 option to revisit (section 5).

### 1.2 Other requirements for the primary business line
| ID | Requirement | Applies? | Why |
|---|---|---|---|
| C-IT-R05 | Bank service provider notification rule | **Yes** | 38 banks buy covered services under the Bank Service Company Act; no size exemption |
| C-IT-R03 | DFARS 252.204-7012 | **Yes, by flow-down** | 19 defense contractors store covered defense information in the Government Cloud and require FedRAMP Moderate equivalent security and paragraphs (c) to (g) under (b)(2)(ii)(D) |
| C-IT-R02 | CMMC (32 CFR Part 170) | **No (applies to the customers)** | The company is not a DoD contractor. Its defense customers may use a CSP that is FedRAMP Authorized at Moderate or higher, or equivalent, for Level 2 and must document the customer responsibility matrix (32 CFR 170.16(c)(2)). Keeping the certification protects their CMMC status |
| Contract | FAR 52.204-21, -23, -25, -30 | **Yes** | Clauses in the GSA Multiple Award Schedule contract |
| C-IT-R04 | DOJ Data Security Program (28 CFR Part 202) | **Not triggered today** | No covered transactions; government-related data has no volume threshold, so each new vendor or contractor with access is checked |
| State | Fla. Stat. 501.171(6) and other state laws | **Yes** | Third-party agent duty to notify customers; each state where affected individuals reside applies its own law |
| C-IT-R06 | CIRCIA | Not in force | No final rule as of 2026-09-25 (section 6) |

## 2. Method
1. **Requirements.** Rows follow each regulation's own structure:
   - **90 FedRAMP rules** (G-001 to G-090) from the 15 rulesets that apply to a Rev5 Class C provider maintaining a certification. Each row cites the rule ID and the keyword that applies to Class C (75 MUST, 3 MUST NOT, 11 SHOULD, 1 SHOULD NOT). Where a rule varies by class, the Class C version is used. Summaries are paraphrased; FedRAMP rule text is a U.S. government work. Rules only for initial applicants, agencies, or assessors were left out.
   - **The Rev5 Class C control list** (G-091 to G-270): 180 base controls, one row each, with the Class C enhancements in the citation column. These statements are the same as in the SSP (P02), so the two documents cannot drift apart.
   - **17 rows for the other requirements** (G-271 to G-287): bank rule 5, DFARS 6, FAR 4, DOJ 1, Florida 1, cited to section and paragraph.
2. **Crosswalk.** Control rows use NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 where one exists (134 rows, labeled "Official"). The other 46 control rows and all rule and other rows are author mappings, labeled as such.
3. **Evidence and sampling.** Current state came from interviews, configuration exports (identity provider, cloud accounts, PAM, hypervisor managers, firewalls, SIEM, RMM), document review, the DC-1 and DC-2 walkthroughs, and the legacy FedRAMP package. Samples: 25 of 74 terminations, 25 of 41 transfers, 40 changes from the SOC 2 period, 20 drive destruction records, 30 days of backup reports, 10 bank contacts called, and the 2026-04 FedRAMP Emergency Test record. The co-sourced internal audit firm re-performed the samples for the 40 controls in P07.
4. **Status and risk.** Each row was rated Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Addressing FedRAMP Communication (AFC) | 2 | 1 | 2 | 0 |
| Certification Data Sharing (CDS) | 0 | 5 | 6 | 0 |
| Certification Package Overview (CPO) | 1 | 1 | 1 | 0 |
| Collaborative Continuous Monitoring (CCM) | 0 | 3 | 4 | 0 |
| Cryptographic Module Use (CMU) | 2 | 1 | 0 | 0 |
| FedRAMP Certification (FRC) | 2 | 5 | 1 | 0 |
| Incident Evaluation and Communication (IEC) | 0 | 3 | 4 | 0 |
| Independent Verification and Validation (IVV) | 4 | 3 | 0 | 0 |
| Marketplace Listing (MKT) | 0 | 1 | 0 | 0 |
| Minimum Assessment Scope (MAS) | 0 | 1 | 3 | 0 |
| Secure Configuration Guide (SCG) | 3 | 1 | 0 | 0 |
| Security Decision Record (SDR) | 0 | 1 | 2 | 0 |
| Significant Change Notification (SCN) | 0 | 5 | 3 | 0 |
| Vulnerability Detection and Response (VDR) | 1 | 6 | 3 | 0 |
| Vulnerability Evaluation and Reporting (VER) | 1 | 2 | 6 | 0 |
| **FedRAMP rules subtotal (90)** | **16** | **39** | **35** | **0** |
| Rev5 Class C control list (180 base controls) | 121 | 55 | 1 | 3 |
| Bank service provider notification rule (5) | 2 | 2 | 1 | 0 |
| DFARS 252.204-7012 flow-down (6) | 1 | 3 | 2 | 0 |
| FAR clauses (4) | 1 | 2 | 1 | 0 |
| DOJ Data Security Program (1) | 1 | 0 | 0 | 0 |
| Florida third-party agent duty (1) | 0 | 1 | 0 | 0 |
| **Total (287)** | **142** | **102** | **40** | **3** |

**The pattern is clear: controls are mostly in place, the new rules are mostly not.** 67% of the control list is Met because the 2024 certification built a working Moderate program. Only 18% of the 2026 rules are Met, because they ask for new ways of reporting and sharing (machine-readable package, trust center, PAIN ratings, quarterly reports) that the legacy process never needed.

**Control list by family** (Met / Partially met / Not met / N/A):
- **Strongest:** PE 13/2/0/1 (inherited from colocation providers); PS 8/1/0/0; MP 6/1/0/0; AC 12/4/0/1.
- **Weakest:** CP 4/5/0/0 (commercial recovery and DC-1); IR 4/5/0/0 (2026 reporting and the bank and DFARS paths); SR 3/5/1/0 (vendor reviews, SBOM, hardware inspection); AU 7/4/0/0 and SI 9/3/0/0 (DC-1 and RMM logging, BMC patching).

**Gap risk** (142 rows Partially met or Not met): **42 High, 60 Moderate, 40 Low**. By section: FedRAMP rules 18 High, 32 Moderate, 24 Low; control list 22 High, 23 Moderate, 11 Low; other requirements 2 High, 5 Moderate, 5 Low.

## 4. Priority gaps and roadmap
### 4.1 High gaps
| Gap | Rows | Action | Owner | Target |
|---|---|---|---|---|
| Vulnerability response still on the legacy POA&M model; no PAIN ratings; shared DC-1 components scanned quarterly; late KEVs | G-072, G-073, G-078, G-079, G-084; G-217 (RA-5), G-251 (SI-2) | PAIN-based evaluation in the scanner and ticketing tools; monthly scanning of every in-scope component; automated KEV due dates | Security Engineering Lead; VP Platform Engineering | 2026-12-07 (maintaining date) |
| FedRAMP Emergency Test action completed late | G-003 | On-call routing and a written procedure; quarterly internal test | Director of Security | 2026-11-30 |
| Boundary too narrow; third-party information resources undocumented | G-053, G-055; G-137 (CM-8), G-226 (SA-9) | Expanded boundary (done in P02); CMDB tags; third-party resource records | GRC Manager | 2027-01-31 (before the 2027-02-15 assessment) |
| No reportability evaluation, default PAIN-5, or 1-hour Initial Incident Report | G-038, G-039, G-040; G-166 (IR-6) | P08 runbooks with the IEC steps; on-call federal incident response coordinator; JSON report templates | Security Operations Manager | 2026-12-15 runbooks; 2027-01-01 capability |
| Legacy package; no JSON; no Certification Package Overview or Security Decision Record; no trust center | G-010, G-017, G-031, G-032, G-061 | Convert the package from P02 and this analysis; select a FedRAMP-compatible trust center | GRC Manager | 2027-04-02 trust center and first report; 2027-07-01 package and record |
| No Ongoing Certification Report | G-020 | First report and Quarterly Review | GRC Manager | 2027-04-02 |
| 56 Class C controls not fully in place | G-035 | P07 POA&M, High items first | GRC Manager | 2027-03-31 |
| Commercial and DC-1 control gaps that reach shared components: privileged access, local accounts, deploy tokens, signing key, logging | G-092 (AC-2), G-096 (AC-6), G-152 (IA-2), G-155 (IA-5), G-134 (CM-5), G-238 (SC-12), G-256 (SI-7), G-113 (AU-2), G-117 (AU-6), G-253 (SI-4) | Apply the government patterns to the commercial partition and DC-1 (P01 R-002, R-003, R-011, R-015, R-016, R-026) | Owners in `gap-analysis.csv` | 2026-11-30 to 2027-03-31 |
| Recovery at scale | G-143 (CP-2), G-145 (CP-4), G-147 (CP-7), G-150 (CP-10) | One contingency plan; DC-1 site-loss runbook; commercial restore tests | VP Platform Engineering; VP Software Engineering | 2026-12-31 to 2027-06-30 |
| Continuous monitoring not on the 2026 model; Tier 1 vendor reviews overdue; customer administrator MFA optional | G-127 (CA-7), G-266 (SR-6), G-158 (IA-8) | Ongoing Certification model; complete reviews; require MFA | GRC Manager; VP Software Engineering | 2026-12-31 to 2027-04-02 |
| Bank notice determination never exercised | G-271 | Exercise in both P08 tabletops; affected-bank lookup | Financial Services Account Director | 2026-12-15 |
| No 72-hour DoD reporting path for defense customers' incidents | G-277 | DFARS path in P08; medium assurance certificate (G-278) | Security Operations Manager | 2026-12-15 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, for the 40 assessed controls, the POA&M (P07).

### 4.2 Program roadmap
| Phase | Dates | Work | Exit test |
|---|---|---|---|
| 1. Rules already in force and VDR/VER | 2026-10 to 2026-12-07 | Emergency message procedure; PAIN-based vulnerability workflow; KEV automation; monthly scanning of shared components | VDR and VER rows at Met or Partially met with Low risk by 2026-12-07 |
| 2. Before the 2027 annual assessment | 2026-12 to 2027-02-15 | Expanded boundary and third-party resource records; 2027 assessment scope set to the IVV-CSF-AIA list; IEC steps live from 2027-01-01; SCN change types in the change process; module register | FRC, IVV, and MAS rows ready before the assessment starts, because their grace periods end at that assessment |
| 3. Ongoing certification | 2027-01 to 2027-04-02 | Trust center; migration notice to FedRAMP and 7 agencies; first Ongoing Certification Report and Quarterly Review | First report published by 2027-04-02 |
| 4. Machine-readable package | 2027-04 to 2027-08-01 | Certification Package Overview, Security Decision Record, and public information in human-readable and JSON formats | CPO, SDR, and CDS rows Met by 2027-08-01 |
| 5. Control remediation (runs in parallel) | 2026-10 to 2027-06-30 | P07 POA&M, High items first | All High control gaps closed by 2027-03-31 |

**Decision for the CEO (made 2026-09-22):** treat the maintaining dates, not the grace dates, as deadlines (risk appetite in P01). The Director of Security reports roadmap status to the audit committee each quarter. A FedRAMP advisor supports phases 3 and 4.

## 5. Secondary requirements: key gaps
- **Bank rule (G-271 to G-275).** The rule is simple, but the company has never exercised the 4-hour determination, and 7 of 38 banks lack verified contacts. With 38 banks spread across hosting, managed services, and backup, the first step is a reliable list of which banks each service affects (R-022).
- **DFARS flow-down (G-276 to G-281).** The FedRAMP Moderate certification meets (b)(2)(ii)(D). The incident duties in (c) to (g) have no written path, and the company holds no DoD-approved medium assurance certificate (R-034).
- **FAR clauses (G-282 to G-285).** Safeguarding is met. The reporting clocks are 1 business day for covered telecommunications (52.204-25(d)) and 3 business days for Kaspersky and FASCSA-covered articles (52.204-23(c), 52.204-30), each followed by a 10-business-day report. They are now in the P08 matrix.
- **28 CFR Part 202 (G-286).** Met today; the onboarding check keeps it that way (R-046).
- **State law (G-287).** The MSA's 72-hour notice is stricter than Florida's 10 days for third-party agents. P08 adds a matrix so the right customers get the right notice.

## 6. Pending regulatory changes
- **FedRAMP rule releases.** FedRAMP publishes changes in its changelog (for example, the 2026-09-13 release moved the Rev5 CPO grace default to 2027-07-01). The GRC Manager checks it monthly and updates this analysis.
- **Consolidated Rules for 2027 or 2028.** All 2026 practices expire no later than 2028-12-31, so another transition will follow. A move to 20x should be reconsidered then.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25. If finalized as proposed, covered entities would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours. A cloud provider of this size could be covered, depending on the final criteria. Not treated as a current obligation.
- **CMMC phase-in.** Phase 2 begins 2026-11-10. More defense customers will need Level 2 assessments that rely on the company's FedRAMP status, which raises the stakes of R-023.

# Regulatory Gap Analysis: Cris Santos Company | Information Technology | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded public cloud and managed infrastructure provider) |
| Tier / Vertical | Enterprise / Information Technology |
| Primary regulation | FedRAMP (44 U.S.C. 3607-3616) as implemented by the **FedRAMP Consolidated Rules for 2026** (version 2026.10.05.01): maintaining the two Rev5 Class C certifications (FR-1 for SL-1, FR-2 for SL-2) and upgrading SL-2 to a Rev5 Class D Agency Certification |
| Also analyzed | Bank service provider notification rule (12 CFR 53.4; 225.303; 304.24); SEC Form 8-K Item 1.05 and Reg S-K Item 106; DFARS 252.204-7012 as flowed down by DIB customers; CMMC (32 CFR 170.16(c)(2)); HIPAA as a business associate; DOJ Data Security Program (28 CFR Part 202); state breach laws (Florida worked example); CIRCIA status |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14; statuses updated 2026-08-28 for the P07 results) |
| Assessors | GRC team and the FedRAMP compliance group (second line); sampling reperformed by Internal Audit for 8 rows |
| Approved | CISO and General Counsel, 2026-09-08; roadmap reviewed by the risk and technology committee of the board, 2026-09-10 |
| Sources checked | fedramp.gov Consolidated Rules for 2026 (machine-readable rules file and Important Deadlines page), re-checked 2026-10-05; eCFR (2026-09-23 versions) for 12 CFR 53.4, 17 CFR 229.106, 28 CFR 202.222, 202.302, 202.401, 202.1101, 202.1104, 32 CFR 170.16, 45 CFR 164.302 and 164.314, 48 CFR 252.204-7012 |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| FedRAMP (C-IT-R01) | **Yes** | FR-1 and FR-2 are active FedRAMP certifications used by 59 federal agencies (21 on SL-1, 38 on SL-2). FedRAMP has no size threshold; it applies because federal agencies use the services. Active certifications must follow each 2026 ruleset by its maintain date and lose certification if they still do not when the grace period ends (all grace periods end 2028-02-01) |
| Class D upgrade of SL-2 | **Yes (target)** | A class upgrade needs a new certification with all requirements met in advance (FRC-CCL-UCC), the sponsoring agency's ATO (FRC-APS-ATO), and a fresh assessment within 3 months (FRC-APP-FIA). FedRAMP stops accepting new Rev5 applications on 2027-06-11 |
| Bank service provider notification (C-IT-R05) | **Yes** | The company performs covered services for about 210 banking organizations on SL-1 and SL-3, so it is a bank service provider. No size exemption |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, large accelerated filer |
| DFARS 252.204-7012 (C-IT-R03) | **Yes, by contract** | About 420 DIB customers store covered defense information on SL-2 and flow down (b)(2)(ii)(D) through the DFARS addendum. The company holds no DoD prime contract |
| CMMC (C-IT-R02) | **Indirect** | The company needs no CMMC status. DIB customers may use a cloud offering that is FedRAMP Authorized at Moderate or higher, or Moderate-equivalent (32 CFR 170.16(c)(2)); FR-2 meets this |
| HIPAA | **Yes, as a business associate** | HIPAA-eligible SL-1 services under BAAs with about 1,100 health care customers (45 CFR 164.302; 164.314; 164.410) |
| DOJ Data Security Program (C-IT-R04) | **Yes, as a screening duty** | The company holds government-related data (no volume threshold, 28 CFR 202.222) and bulk sensitive personal data on behalf of customers. It must not enter restricted transactions without the security requirements (202.401). It does no data brokerage, so 202.302 does not apply |
| State breach laws | **Yes** | The law of each state where affected individuals reside. As a service provider, the company usually notifies its customer, the data owner (Florida worked example: Fla. Stat. 501.171(6), third-party agent notice within 10 days) |
| CIRCIA (C-IT-R06) | **Not in force** | No final rule as of 2026-09-25. If adopted as proposed, the size criterion would cover the company |
| SOX Section 404 | Separate program | IT general controls over billing and ERP are tested by the SOX program and not repeated here |

## 2. Method
1. **Decompose.** Rows follow each regulation's own structure:
   - **62 FedRAMP rules** (G-001 to G-062), selected from the 2026 rulesets that bind a Rev5 Class C provider and a Class D applicant. Each row cites the rule ID and its MUST, SHOULD, or MAY keyword; where the rule differs by class, both values are given. Summaries are paraphrased; FedRAMP rule text is a U.S. government work.
   - **87 Class D additions** (G-063 to G-149): every control and enhancement the Class D list adds to the Class C list, one row each, with the same status as the HCP-G SSP (P02 section 6). The 180 base controls of the Class C list are covered by the annual FedRAMP independent assessment (2026-03) and are summarized in one row (G-012), not repeated.
   - **29 rows for the other regulations** (G-150 to G-178), cited to section and paragraph from the eCFR text, the SEC release, and the Florida statute.
2. **Crosswalk.** Class D control rows use NIST's CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 where one exists (labeled "Official"). Rule rows and other regulation rows are author mappings and are labeled that way.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample or the full population and recorded population, sample size, and exceptions. Key populations over 250 used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk items used 25 to 40; populations under 100 were tested in full. Selections were random. **24 rows were tested by sampling or full-population analytics; 13 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| FedRAMP Certification (FRC) | 4 | 5 | 5 | 0 | 14 |
| Minimum Assessment Scope (MAS) | 1 | 3 | 0 | 0 | 4 |
| Security Decision Record (SDR) | 0 | 2 | 1 | 0 | 3 |
| Certification Data Sharing (CDS) | 3 | 2 | 2 | 0 | 7 |
| Certification Package Overview (CPO) | 0 | 2 | 0 | 0 | 2 |
| Collaborative Continuous Monitoring (CCM) | 0 | 0 | 4 | 0 | 4 |
| Incident Evaluation and Communication (IEC) | 3 | 2 | 0 | 0 | 5 |
| Vulnerability Detection and Response (VDR) | 2 | 4 | 0 | 0 | 6 |
| Vulnerability Evaluation and Reporting (VER) | 2 | 2 | 0 | 0 | 4 |
| Significant Change Notification (SCN) | 2 | 1 | 0 | 0 | 3 |
| Cryptographic Module Use (CMU) | 1 | 1 | 0 | 0 | 2 |
| Independent Verification and Validation (IVV) | 2 | 0 | 0 | 0 | 2 |
| Addressing FedRAMP Communication (AFC) | 3 | 0 | 0 | 0 | 3 |
| Secure Configuration Guide (SCG) | 1 | 1 | 1 | 0 | 3 |
| **FedRAMP rules subtotal (62)** | **24** | **25** | **13** | **0** | **62** |
| Rev5 Class D additions (87) | 42 | 35 | 8 | 2 | 87 |
| Bank service provider notification | 3 | 2 | 0 | 0 | 5 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 4 | 0 | 0 | 0 | 4 |
| DFARS 252.204-7012 (customer flow-down) | 3 | 2 | 0 | 0 | 5 |
| CMMC (indirect) | 1 | 0 | 0 | 0 | 1 |
| HIPAA (business associate) | 2 | 2 | 0 | 0 | 4 |
| DOJ Data Security Program | 2 | 0 | 0 | 1 | 3 |
| State breach and data security laws | 3 | 0 | 0 | 0 | 3 |
| CIRCIA (pending) | 0 | 0 | 0 | 1 | 1 |
| **Total** | **85** | **68** | **21** | **4** | **178** |

**Gap risk** (89 rows Partially met or Not met): **17 High, 31 Moderate, 41 Low**.

**What the numbers say:**
- **The certified baseline is sound.** The Class C control list passed the 2026-03 independent assessment with no open High findings, and the established incident, vulnerability scanning, and FedRAMP communication rules are largely met.
- **The 2026 rules are the near-term risk to FR-1 and FR-2.** Continuous monitoring (CCM) is entirely Not met, and the Security Decision Record, trust center, and JSON data are not in place. These have later maintain dates (CCM 2027-04-02; SDR and CDS 2027-08-01) but no extension past the grace periods.
- **Vulnerability timeframes come first.** VDR and VER have the earliest Rev5 maintain date, 2026-12-07, with a grace period ending 2027-03-07. Seven of 60 sampled G1 vulnerabilities and 2 of 14 KEVs missed the targets.
- **The Class D gap is 43 items, and 5 are on the release path.** AU-10, CM-3(1), SI-7(2), and SI-7(5) are the same weakness as P01 R-001 and the P08 scenario; CP-10(4) is the G1 recovery time.

## 4. Priority gaps and roadmap
### 4.1 High gaps
| Gap | Rows | Action | Owner | Target |
|---|---|---|---|---|
| Class D application sequence: no ATO, assessment, or application yet; 2027-06-11 cutoff | G-007, G-009, G-010 (FRC-APP-AFC, FRC-APP-FIA, FRC-APS-ATO) | Assessment 2027-04; agency ATO 2027-05-21; apply by 2027-05-28 | Senior Vice President, Government Cloud | 2027-05-28 |
| 43 Class D additions not fully in place | G-011, G-012 (FRC-CCL-UCC, FRC-CSF-BSL) | Class D program (POAM-021) | Senior Vice President, Government Cloud | 2027-03-31 |
| Release path: guest-agent channel approvals, approver signature, integrity response | G-078 (AU-10), G-083 (CM-3(1)), G-145 (SI-7(2)), G-146 (SI-7(5)) | Two-person approval from separate teams; signature binding; automated halt (POAM-001) | Vice President, Software Supply Chain | 2026-12-15 |
| G1 tenant database recovery 3.4 h against a 2 h RTO | G-101 (CP-10(4)) | Parallel restore; full failover test (POAM-009) | Vice President, Control Plane Engineering | 2027-01-31 |
| Two G1 services without active CMVP validations (a Class D MUST) | G-054 (CMU-CSO-UVM) | Move to a validated module stream (POAM-004) | Director of Key Management and PKI | 2027-02-28 |
| Class D 15-minute Initial Incident Report not operational | G-037 (IEC-CSO-IIR) | Pre-built report from the SOC case; on-call reporter; drills (POAM-010) | Director of Security Operations | 2026-12-31 |
| Vulnerability timeframes and KEV due dates missed | G-041, G-043, G-044 (VDR) | Due-date escalation; Class D timeframes in G1 (POAM-007) | Director of Security Operations | 2026-12-31 |
| Materiality process for a multi-tenant incident | G-155, G-156 (Form 8-K Item 1.05) | Worksheet factors; tabletop 2026-11-18 (POAM-011) | General Counsel | 2026-11-30 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01: R-001, R-006, R-011, R-012, R-013, R-014, R-016, R-018) and, where a control was assessed, the POA&M (P07).

### 4.2 Regulator-ready notes
- **FedRAMP.** Every rule row cites the rule ID, keyword, and class-specific value. The Class D rows match the SSP one for one, so the Security Decision Record can be generated from the same data (POAM-020).
- **Banks.** 22 of 210 banking organizations lack a current designated contact (G-150, G-151). The rule's fallback (CEO and CIO, 53.4(a)(2)) is available for all 210, so no bank would go unnotified, but the designated contact is the required first route (POAM-023, due 2026-11-30).
- **DIB customers.** The joint reporting procedure and the 90-day media preservation step have never been exercised (G-163, G-165; POAM-029).
- **DOJ Data Security Program.** One SaaS contract with offshore support was amended in 2026-09 so that no supplier staff outside the United States can reach customer content (G-172; P01 R-055).

### 4.3 Roadmap
| Phase | Dates | Work |
|---|---|---|
| 1. Release path and vulnerability rules | 2026-10 to 2026-12 | POAM-001 (guest-agent approvals and signatures); VDR and VER timeframes before the 2026-12-07 maintain date (POAM-007); bank contacts (POAM-023); materiality tabletop 2026-11-18 (POAM-011); 15-minute incident reporting (POAM-010) |
| 2. Class D build-out | 2026-11 to 2027-03 | Remaining Class D additions (POAM-021); validated cryptographic modules (POAM-004); G1 recovery (POAM-009); tamper evidence (POAM-005); first Ongoing Certification Reports and Quarterly Reviews before the CCM maintain date 2027-04-02 (POAM-019) |
| 3. Class D assessment and certification | 2027-04 to 2027-05 | FedRAMP independent assessment 2027-04; sponsoring agency ATO 2027-05-21; application by 2027-05-28 (cutoff 2027-06-11) |
| 4. Remaining 2026 rules | 2027-03 to 2027-08 | Security Decision Record in JSON (POAM-020) and trust center (POAM-024) before the SDR and CDS maintain dates of 2027-08-01 |

**Fallback if the Rev5 window is missed.** If the agency ATO slips past early June 2027, the Rev5 Class D path closes. The company would then seek a 20x Class D certification. Most rule work (VDR, VER, IEC, CCM, SDR, CDS) carries over; the Rev5 control list does not. The Senior Vice President, Government Cloud reviews this decision with the sponsoring agency each month from 2027-02.

## 5. Pending regulatory changes
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25. If finalized as proposed, covered entities would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours. Not treated as a current obligation.
- **FedRAMP 2026 rules.** Rev5 maintain dates by ruleset: VDR and VER 2026-12-07 (grace to 2027-03-07); FRC, IVV, MAS, IEC, SCN, CMU 2027-01-01 (IEC, SCN, and CMU grace to 2027-06-01); CCM 2027-04-02; CPO 2027-07-01; SDR and CDS 2027-08-01; all grace periods end 2028-02-01. The 2026 rules expire no later than 2028-12-31, so the 2027 or 2028 rules must be adopted before then. The FedRAMP compliance group checks the rules file monthly; the version used here is 2026.10.05.01.
- **CMMC Phase 2** begins 2026-11-10. It does not bind the company directly but will increase DIB customer requests for FR-2 evidence.
- **HIPAA Security Rule NPRM** (90 FR 898) is proposed only and is not treated as an obligation.

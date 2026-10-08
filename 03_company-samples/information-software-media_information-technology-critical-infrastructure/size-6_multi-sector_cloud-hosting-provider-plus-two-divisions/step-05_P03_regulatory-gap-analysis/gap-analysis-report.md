# Regulatory Gap Analysis: Cris Santos Company Holdings | Information Technology | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Information Technology (focus division: Cloud Hosting) |
| Primary regulation (focus division) | FedRAMP (44 U.S.C. 3607-3616) as implemented by the **FedRAMP Consolidated Rules for 2026**, for **maintaining** the G1 Government Cloud's Rev5 Class C certification |
| Division regulations | Managed IT: DFARS 252.204-7012 and CMMC Level 2 (NIST SP 800-171 Rev. 2), External Service Provider scoping, FAR 52.204-21, HIPAA business associate duties, the bank rule. Payment Processing: FTC Safeguards Rule (16 CFR Part 314) and PCI DSS v4.0.1, plus sponsor bank, card network, and state licensing terms |
| Gap tables | `gap-analysis.csv` (Cloud Hosting, 70 rows); `gap-analysis-managed-it.csv` (41 rows); `gap-analysis-payment-processing.csv` (49 rows) |
| Assessment dates | 2026-08-03 to 2026-08-28, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads, the Government Cloud compliance director, the Managed IT federal contracts compliance officer, and the Payment Processing Qualified Individual, coordinated by the Group Chief Privacy Officer; reviewed by group internal audit and outside counsel (sections 1 and 6) |
| Sources checked | fedramp.gov Consolidated Rules for 2026 (Important Dates; Updating to 2026 Rules; Rev5 Deadlines; Rev5 rulesets), retrieved 2026-10-05; eCFR (current through 2026-09-23): 12 CFR 53.2, 53.4, 225.301, 225.303, 304.22, 304.24; 16 CFR 314.2 and 314.4; 32 CFR 170.3, 170.4, 170.19, 170.21; 48 CFR 252.204-7012 and 252.204-7019 |

## 1. Applicability
At this tier the first question is not "what does the rule say?" but "which subsidiary does it bind, and in what role?"

### 1.1 Role of each division
| Entity | Role | Basis |
|---|---|---|
| Cloud Hosting (G1) | **FedRAMP certified cloud service provider** (Rev5 Class C; legacy FedRAMP Moderate agency authorization, 2023-03-15) | 44 U.S.C. 3607-3616; FedRAMP Consolidated Rules for 2026 |
| Cloud Hosting (G1) | **Cloud provider to DIB contractors** that store covered defense information; bound by a DFARS addendum | 48 CFR 252.204-7012(b)(2)(ii)(D) |
| Cloud Hosting (SL-1) | **Bank service provider** to about 260 banking organizations | 12 CFR 53.2(b)(2), (b)(5); 53.4; 225.303; 304.24 |
| Cloud Hosting (SL-1) | **HIPAA business associate** for the HIPAA-eligible services | 45 CFR 160.103; 164.302 |
| Cloud Hosting | **Affiliate service provider** to Payment Processing (the CDE runs on SL-1) | 16 CFR 314.2 (service provider) and 314.4(f); PCI DSS v4.0.1 Requirement 12.8 |
| Managed IT | **DoD subcontractor** holding covered defense information in SYS-M2 (9 subcontracts) | 48 CFR 252.204-7012; 32 CFR Part 170 |
| Managed IT | **External Service Provider** to about 150 DIB clients (Security Protection Data for all; CUI enclaves for 18) | 32 CFR 170.4 (ESP definition); 170.19(c)(2) |
| Managed IT | **Federal contractor** with federal contract information (11 civilian agency contracts) | 48 CFR 52.204-21 |
| Managed IT | **HIPAA business associate** of about 210 health care clients; **bank service provider** to about 190 banks | 45 CFR 160.103; 12 CFR 53.4 |
| Managed IT | **Affiliate service provider** to Payment Processing (RMM agents on connected-to servers) and to Cloud Hosting (partner operators) | 16 CFR 314.4(f); PCI DSS 12.8 |
| Payment Processing | **Financial institution** under the FTC Safeguards Rule (group legal decision, 2023) | 16 CFR 314.2(h)(1): transferring money is a financial activity; compare example 314.2(h)(2)(vi) ("a business that regularly wires money to and from consumers") |
| Payment Processing | **PCI DSS Level 1 service provider**; **bank service provider** to its sponsor banks; state-licensed money transmitter for bill pay where required | Sponsor bank and card network contracts; 12 CFR 53.4; state laws (generic) |
| Holding company | **SEC registrant** | Reg S-K Item 106; Form 8-K Item 1.05 |

### 1.2 FedRAMP: applies to G1, and the 2026 rules decide whether the certification survives
G1 has 27 federal agency customers, so FedRAMP applies to it. FedRAMP has no size threshold or small-business exemption (C-IT-R01). The question here is not readiness, as it was at the Small size, but **maintenance**. The fedramp.gov pages read on 2026-10-05 say:
- **The 2026 rules apply to every certified provider.** "Cloud service providers that do not adjust to the updated rules will lose their FedRAMP Certification." The term "FedRAMP authorization" is now "FedRAMP Certification," impact levels are now Classes A to D, and "continuous monitoring" by the provider is now "Ongoing Certification."
- **POA&Ms are replaced** by a list of accepted vulnerabilities, and FedRAMP-defined organizational parameters are largely removed.
- **Rev5 is being retired.** No new Rev5 applications are accepted after 2027-06-11. Existing Rev5 certifications remain active until at least 2028-12-31, and providers should plan the move to 20x.
- **Hard deadline.** All grace periods expire by 2028-02-01, and the 2026 rules themselves expire no later than 2028-12-31.

**Rev5 ruleset dates for an existing certification** (fedramp.gov Rev5 Deadlines, retrieved 2026-10-05):

| Ruleset | Maintain by | Grace period ends | Rows |
|---|---|---|---|
| Addressing FedRAMP Communication (AFC) | 2026-01-05 | 2026-07-01 (ended) | G-046, G-047 |
| Secure Configuration Guide (SCG) | 2026-03-01 | 2026-07-01 (ended) | G-048, G-049 |
| Marketplace Listing (MKT) | 2026-07-04 | 2026-07-04 (ended) | G-050 |
| Vulnerability Detection and Response (VDR); Vulnerability Evaluation and Reporting (VER) | **2026-12-07** | 2027-03-07 | G-017 to G-028 |
| Cryptographic Module Use (CMU); Incident Evaluation and Communication (IEC); Significant Change Notification (SCN) | 2027-01-01 | 2027-06-01 | G-011 to G-016, G-029 to G-033 |
| FedRAMP Certification (FRC); Independent Verification and Validation (IVV); Minimum Assessment Scope (MAS) | 2027-01-01 | At the first FedRAMP independent assessment started after 2027-01-01: **for G1, 2027-02-08** | G-001 to G-010, G-043 to G-045 |
| Collaborative Continuous Monitoring (CCM) | 2027-04-02 | 2027-10-01 | G-034 to G-036 |
| Certification Package Overview (CPO) | 2027-07-01 | At the first assessment started after 2027-07-01 | G-037 |
| Certification Data Sharing (CDS) | 2027-08-01 | 2028-02-01 | G-040 to G-042 |
| Security Decision Record (SDR) | 2027-08-01 | At the first assessment started after 2027-08-01 | G-038, G-039 |

"Maintain by" means a provider should follow the ruleset by that date; after it, FedRAMP requests a corrective action plan. "Grace period ends" means a provider that still does not follow it loses its certification, with public notice. The AFC, SCG, and MKT grace periods have already ended, so those rows must be (and are) Met.

### 1.3 Managed IT: DFARS, CMMC, and the ESP role
- **DFARS 252.204-7012 applies** to the 9 DoD subcontracts. Covered contractor information systems must implement NIST SP 800-171 as in effect when the solicitation was issued ((b)(2)(i)). Cyber incidents must be rapidly reported, meaning within 72 hours of discovery, at dibnet.dod.mil, using a DoD-approved medium assurance certificate ((c)(1), (c)(3)), and the subcontractor gives the DoD report number to the prime ((m)(2)(ii)).
- **The enclave sits in G1.** Because the division uses an external cloud provider for covered defense information, that provider must meet security requirements equivalent to the FedRAMP Moderate baseline ((b)(2)(ii)(D)), and under CMMC a cloud provider that processes CUI "shall meet the FedRAMP requirements in 48 CFR 252.204-7012" (32 CFR 170.19(c)(2)). G1's certification therefore carries the enclave. If G1 lost its certification (P01 GR-05), the enclave would fail too.
- **CMMC Phase 2 is suspended.** Phase 1 began on the effective date of the DFARS CMMC acquisition rule (2025-11-10). Phase 2 was to start on 2026-11-10, when DoD intended to require Level 2 (C3PAO) status as a condition of award, or at its discretion at option exercise (32 CFR 170.3(e)(2)). The DoD (Department of War) CIO memorandum of 2026-07-13 suspends CMMC Phase 2. Until 2028-11-09, DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self) (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies. For existing contracts, contracting officers remove CMMC requirements by modification before the next option period or at the next scheduled administrative modification.
- **Conditional status has limits.** A POA&M is allowed only if the score ratio is at least 0.8, no item has a point value above 1 (with one defined exception for 3.13.11), and none of the listed requirements is on it, including 3.12.4 System Security Plan (170.21(a)(2)). A POA&M must be closed within 180 days or the Conditional status expires (170.21(b)).
- **SPRS currency.** An offeror needs a NIST SP 800-171 DoD Assessment not more than 3 years old in SPRS (DFARS 252.204-7019(b)). The division's basic self-assessment is dated 2024-02-12.
- **As an External Service Provider**, the division does not hold a CMMC status for its clients, but its services sit inside each DIB client's assessment scope: as part of the assessment when it processes CUI, and as Security Protection Assets when it processes only Security Protection Data such as logs and configurations (170.19(c)(2)). Clients cannot pass without the division's evidence.

### 1.4 Payment Processing: FTC Safeguards Rule and PCI DSS
- **FTC Safeguards Rule.** A financial institution is any institution significantly engaged in activities that are financial in nature under section 4(k) of the Bank Holding Company Act (16 CFR 314.2(h)(1)). Group legal decided in 2023 that the division's money movement for merchants, billers, and consumers is such an activity and applies Part 314 to all consumer and cardholder information it handles. The 314.6 exceptions do not apply (about 14 million enrolled consumers). The FTC notice in 314.4(j) applies to notification events involving at least 500 consumers, no later than 30 days after discovery.
- **The key finding is about affiliates.** The Cloud Hosting division (SL-1 hosts the CDE) and the Managed IT division (RMM agents on connected-to servers) are service providers to the division. 314.4(f) requires the division to select capable providers, bind them by contract, and assess them periodically. PCI DSS Requirement 12.8 requires the same management of third-party service providers, affiliates included. Neither is in place (scenario gap 6).
- **PCI DSS is contractual,** through sponsor bank A and the card network rules. Rows list requirement numbers with short labels in our own words; the standard's text is not reproduced.
- **Money transmission.** The division holds state money transmitter licenses where its bill-pay service requires them and none in New York. Incident notice duties vary by license and are not yet mapped (PY-G46). This analysis treats state licensing generically.

### 1.5 Group-wide checks
| Requirement | Result |
|---|---|
| SEC Reg S-K Item 106 and Form 8-K Item 1.05 | **Applies** to the holding company (P08 disclosure step) |
| DOJ Data Security Program (28 CFR Part 202) | **Applies to all divisions.** G1 holds government-related data (no volume threshold); SL-1 customers and Payment Processing hold bulk personal financial data (more than 10,000 U.S. persons) and covered personal identifiers (more than 100,000). No covered data transactions are known, but vendor screening misses covered-person status (G-068; scenario gap 10) |
| CIRCIA | **Not in force.** No final rule as of 2026-09-25. If finalized as proposed, the group would likely be covered as an entity above the SBA size standard in a critical infrastructure sector. Tracked only |
| State breach notification laws | Each state where affected individuals reside. Florida worked example: Fla. Stat. 501.171, including the 10-day third-party agent notice (G-067) |
| FTC Act Section 5 | Applies to all divisions' security and AI claims (P10) |
| CCPA | The group is a CCPA business. Payment data covered by GLBA is exempt at the data level (Cal. Civ. Code 1798.145(e)); whether the cybersecurity audit rules (Cal. Code Regs. tit. 11, 7120) reach the group is under counsel review and not asserted here |
| Not applicable | NYDFS Part 500 (no New York license); SEC Reg S-P (no broker-dealer or adviser); CMMC for Cloud Hosting itself (it is a cloud provider whose FedRAMP status DIB customers rely on); HIPAA for Payment Processing (no PHI) |

## 2. Regulation-by-division matrix
| Requirement | Cloud Hosting | Managed IT | Payment Processing | Group (corporate) |
|---|---|---|---|---|
| C-IT-R01 FedRAMP (2026 rules) | **Primary.** G1 Rev5 Class C certification | Relies on G1 for the CUI enclave | Not applicable | SYS-G1 and SYS-G2 are information resources of G1 (MAS) |
| C-IT-R03 DFARS 252.204-7012 | (b)(2)(ii)(D) duties to DIB customers by addendum | **Primary.** 9 DoD subcontracts | Not applicable | Not applicable |
| CMMC (32 CFR Part 170) | Not applicable (cloud provider) | **Applies.** Level 2 for its subcontracts; ESP to about 150 DIB clients | Not applicable | Common controls inherited by the enclave |
| N54-R04 FAR 52.204-21; FAR 52.204-23, -25, -30 | G1 agency contracts | 11 civilian contracts | Not applicable | Not applicable |
| C-IT-R05 Bank service provider rule | **Applies** (about 260 banks) | **Applies** (about 190 banks) | **Applies** (sponsor banks) | One notice register (P08) |
| N54-R06 HIPAA (business associate) | **Applies** (HIPAA-eligible services) | **Applies** (about 210 clients) | Not applicable | Group controls inherited |
| N52-R03 FTC Safeguards Rule | Affiliate service provider | Affiliate service provider | **Primary.** Financial institution | Common controls support the program |
| PCI DSS v4.0.1 (contractual) | Provider of platform controls to the CDE (12.8) | RMM in scope through connected-to servers | **Primary.** Level 1 service provider | Common controls in the responsibility matrix |
| Sponsor bank and card network terms | Not applicable | Not applicable | **Applies** | Matrix rows |
| State money transmitter laws | Not applicable | Not applicable | **Applies** (generic) | Not applicable |
| C-IT-R04 DOJ Data Security Program | **Applies** | **Applies** | **Applies** | Vendor screening |
| N52-R08 SEC Item 106 and Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** |
| State breach laws | Third-party agent duties to customers | Third-party agent duties to clients | Own notices for consumer data | Coordinates |
| C-IT-R06 CIRCIA | Pending | Pending | Pending | Tracked |

## 3. Method
1. **Requirements.**
   - FedRAMP rows follow the rules' own structure: one row per rule or rule pair, cited by rule ID with its MUST, SHOULD, or MAY keyword. Summaries are paraphrased from fedramp.gov (U.S. government works). The Rev5 Class C control list itself is not repeated row by row: the G1 package documents all of it, and the HCP statements are in P02.
   - CFR rows were read from the eCFR and cite section and paragraph. NIST SP 800-171 Rev. 2 rows are one per family, citing the requirement numbers not fully met.
   - PCI DSS rows list requirement numbers with short labels in our own words, as in the industry's other samples.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5 as an **author mapping**. No official NIST mapping exists from the FedRAMP 2026 rules, 16 CFR Part 314, or PCI DSS to CSF 2.0. For SP 800-171 Rev. 2, the mapping is informed by its Appendix D.
3. **Evidence.** Interviews; configuration exports; the G1 package and the 2026-03-20 FedRAMP assessment report; contract registers; the 2026-04-30 PCI DSS Report on Compliance; the 2024 SP 800-171 self-assessment; and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale. The `related_risk_ids` column links each gap to the registers.

## 4. Results
### 4.1 Cloud Hosting (`gap-analysis.csv`)
| Requirement set | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FedRAMP Certification (FRC) | 2 | 3 | 1 | 0 |
| Minimum Assessment Scope (MAS) | 0 | 3 | 1 | 0 |
| Incident Evaluation and Communication (IEC) | 1 | 4 | 1 | 0 |
| Vulnerability Detection and Response (VDR) | 2 | 3 | 2 | 0 |
| Vulnerability Evaluation and Reporting (VER) | 0 | 2 | 3 | 0 |
| Significant Change Notification (SCN) | 0 | 2 | 0 | 0 |
| Cryptographic Module Use (CMU) | 1 | 2 | 0 | 0 |
| Collaborative Continuous Monitoring (CCM) | 0 | 0 | 3 | 0 |
| Certification Package Overview (CPO) | 0 | 0 | 1 | 0 |
| Security Decision Record (SDR) | 0 | 1 | 1 | 0 |
| Certification Data Sharing (CDS) | 0 | 2 | 1 | 0 |
| Independent Verification and Validation (IVV) | 1 | 2 | 0 | 0 |
| AFC, SCG, and MKT (grace periods ended) | 5 | 0 | 0 | 0 |
| **FedRAMP rules subtotal (50)** | **12** | **24** | **14** | **0** |
| Bank service provider rule (5) | 2 | 3 | 0 | 0 |
| DFARS 252.204-7012 cloud provider duties (4) | 1 | 3 | 0 | 0 |
| HIPAA business associate (4) | 3 | 1 | 0 | 0 |
| FAR supply chain reporting (3) | 0 | 3 | 0 | 0 |
| Florida 501.171, DOJ Data Security Program, customer agreement, SOC 2 (4) | 1 | 3 | 0 | 0 |
| **Total (70)** | **19** | **37** | **14** | **0** |

Of the 51 rows that are Partially met or Not met, 5 are rated High, 34 Moderate, and 12 Low.

**The main finding.** The G1 offering is secure by the old measure: its controls passed the 2026 independent assessment, and every ruleset whose grace period has ended (AFC, SCG, MKT) is followed. What it lacks is the **2026 way of proving it**:
- **Vulnerability evaluation by PAIN rating** (G-024), a PAIN-based remediation standard (G-022), and the accepted-vulnerability model (G-026, G-027), all due 2026-12-07.
- **A complete offering scope** that includes the shared group services and the third-party model service that see G1 logs and metadata (G-007, G-009). This must be done before the 2027-02-08 assessment, which ends the MAS grace period.
- **A tested 1-hour incident report** (G-012).
- **Machine-readable package, trust center, and Ongoing Certification Reports** (G-005, G-034 to G-040), with later dates through 2027-08-01.

The 14 Not met rows are all FedRAMP rows with future maintain dates; none is past its grace period yet.

### 4.2 Managed IT (`gap-analysis-managed-it.csv`)
| Requirement set | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| DFARS 252.204-7012 (8) | 4 | 4 | 0 | 0 |
| DFARS 252.204-7019 (1) | 0 | 1 | 0 | 0 |
| CMMC, 32 CFR Part 170 (6) | 1 | 2 | 2 | 1 |
| NIST SP 800-171 Rev. 2, by family (14) | 5 | 9 | 0 | 0 |
| FAR 52.204-21 (2) | 1 | 1 | 0 | 0 |
| HIPAA business associate (6) | 2 | 4 | 0 | 0 |
| Bank service provider rule (2) | 0 | 2 | 0 | 0 |
| Client agreements (2) | 0 | 2 | 0 | 0 |
| **Total (41)** | **13** | **25** | **2** | **1** |

Of the 27 gaps, 8 are High, 15 Moderate, and 4 Low.

**SP 800-171 status: 96 of 110 requirements fully met.** The 14 not fully met are 3.1.5, 3.1.11, 3.1.12, 3.1.15, 3.2.2, 3.3.1, 3.3.5, 3.4.5, 3.5.10, 3.6.3, 3.11.2, 3.12.1, 3.12.4, and 3.13.1. Most trace to one cause: **RMM agents from the shared tenant on the enclave's management servers** (scenario gap 2). Removing them fixes 3.1.12, 3.1.15, 3.4.5, 3.13.1, and part of 3.1.5 at once. 3.12.4 must be fixed regardless, because it may not be on a POA&M.

**Not met:** 32 CFR 170.3(e)(2) (no C3PAO assessment planned for the 2027 option periods; with Phase 2 suspended, this is now a voluntary step) and 170.19(c)(2) as an ESP (no responsibility matrix for DIB clients).

### 4.3 Payment Processing (`gap-analysis-payment-processing.csv`)
| Requirement set | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FTC Safeguards Rule, 16 CFR 314.4 and 314.6 (26) | 14 | 9 | 1 | 2 |
| PCI DSS v4.0.1, service provider (19) | 14 | 4 | 1 | 0 |
| State money transmitter licensing (1) | 0 | 1 | 0 | 0 |
| Sponsor bank, bank rule, and card network terms (3) | 0 | 3 | 0 | 0 |
| **Total (49)** | **28** | **17** | **2** | **2** |

Of the 19 gaps, 5 are High, 11 Moderate, and 3 Low.

**Not met:** 16 CFR 314.4(f)(2) and PCI DSS 12.8, both because the two affiliates are not managed as service providers. **High:** 314.4(c)(1) and PCI DSS Requirement 1 (RMM path into the connected-to segment), and 314.4(f)(1). The division's own controls are strong (its 2026 ROC had no open items); its gaps are about what its sister divisions do inside its scope.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | FedRAMP 2026 transition for G1 (3) | CH | VDR and VER (G-017 to G-028); MAS (G-007 to G-010); IEC (G-011 to G-016); CCM, CPO, SDR, CDS | High | Program by ruleset date; MAS before 2027-02-08 | Government Cloud compliance director | 2026-12-07 to 2027-08-01 |
| 2 | RMM reach into other divisions (2) | MI, PP | PCI DSS 1, 7, 10, 12.5.2.1; 16 CFR 314.4(c)(1); SP 800-171 3.1.12, 3.1.15, 3.13.1; 32 CFR 170.19(c)(1) | High | Remove agents; separate internal tooling; two-person approval | Managed IT chief operating officer | 2027-01-31 |
| 3 | CMMC Level 2 and ESP duties (5) | MI | 32 CFR 170.3(e)(2), 170.19(c)(2), 170.21; DFARS 252.204-7019(b) | High | Close the 14 requirements; fix 3.12.4 first; new SPRS score; voluntary C3PAO; ESP matrix | Managed IT federal contracts compliance officer | 2027-03-31 |
| 4 | Affiliate oversight for Payment Processing (6) | PP, CH, MI | 16 CFR 314.4(f)(1)-(3); PCI DSS 12.8 | High | Intercompany agreements; full responsibility matrix; annual affiliate assessment | Payment Processing chief compliance officer | 2026-12-31 |
| 5 | AI triage data and autonomy (4) | All | MAS-CSO-TPR (G-009); 16 CFR 314.4(c)(8); PCI DSS 10 | High | Redact G1 identifiers; document the model service; human approval in G1 and the CDE (P10) | Group SOC director | 2026-12-31 |
| 6 | Partner-operator path (1) | CH, MI | 45 CFR 164.308(a)(4) and 164.312(d) (BAA customers); customer agreements; SOC 2 description (G-070) | High (P01 GR-01) | SYS-G1 PAM, hardware keys, per-client scope | Group CISO | 2026-12-31 |
| 7 | Multi-regulator notification matrix (7) | All | IEC-CSO-IIR; 12 CFR 53.4; 48 CFR 252.204-7012(c); 45 CFR 164.410; 16 CFR 314.4(j); sponsor bank terms; Form 8-K Item 1.05 | Moderate | Complete the matrix and contact registers; tabletop 2026-12-09 | Group General Counsel | 2026-12-31 |
| 8 | Managed IT supplement drift (8) | MI | 45 CFR 164.316(b)(2)(iii) | Moderate | Re-issue the supplement | Managed IT division security and compliance lead | 2026-11-30 |
| 9 | Managed IT inheritance (9) | MI | 45 CFR 164.308(a)(8); 32 CFR 170.19(c) | Moderate | Inheritance matrix | Managed IT division security and compliance lead | 2026-12-31 |
| 10 | Covered-person screening (10) | All | 28 CFR Part 202 | Moderate | Screening in vendor onboarding and annual review | Group Chief Privacy Officer | 2026-12-31 |

CH = Cloud Hosting, MI = Managed IT, PP = Payment Processing. High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-020 to POAM-022 trace directly to this analysis.

## 6. Pending and watch items
- **FedRAMP 20x.** New Rev5 applications end 2027-06-11, and existing Rev5 certifications remain active until at least 2028-12-31. G1 must plan its move to 20x; the Government Cloud compliance director will bring a recommendation to the division president by 2027-03-31. Most of the ruleset work in this analysis (MAS, VDR, VER, IEC, SCN, CMU, CCM, CDS) is shared with 20x, so it carries over.
- **The Consolidated Rules for 2026 expire no later than 2028-12-31.** Updated rules for 2027 or 2028 are expected; the Government Cloud compliance director checks the fedramp.gov changelog monthly.
- **CMMC phases.** Phase 2 is suspended. Under DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5), DoD includes clause 252.204-7021 until 2028-11-09 only when a program office or requiring activity requires a specific CMMC level, and on or after 2028-11-10 whenever the contractor will process, store, or transmit FCI or CUI on its own systems (except COTS-only buys). Track primes' flow-down of CMMC requirements.
- **FAR CUI proposed rule (2025) and the FAR Overhaul proposed rule (2026-06-23)** are not final. Flagged on MS-G30.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **proposed only**. If finalized as proposed it would affect both business associate divisions (for example, a written technology asset inventory and network map, encryption, MFA, and business associate notice within 24 hours of activating a contingency plan). Not treated as a current obligation.
- **CIRCIA**: no final rule as of 2026-09-25; reporting is voluntary until a final rule takes effect.
- **Colorado SB26-189** (effective 2027-01-01): relevant to Payment Processing's merchant underwriting model if it materially influences a consequential decision in financial or lending services; counsel review in progress (P10).

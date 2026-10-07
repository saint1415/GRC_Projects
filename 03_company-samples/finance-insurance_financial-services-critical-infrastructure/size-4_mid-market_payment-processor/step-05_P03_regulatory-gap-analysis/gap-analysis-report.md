# Regulatory Gap Analysis: Cris Santos Company | Financial Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed payment processor serving merchants) |
| Tier / Vertical | Mid-Market / Financial Services |
| Primary standard | PCI DSS v4.0.1 (PCI SSC, June 2024), assessed as a **service provider** across both platforms |
| Other applicable rules for the primary business line | FTC Safeguards Rule, 16 CFR Part 314; bank service provider notice, 12 CFR 53.4 (Bank A, OCC) and 12 CFR 304.24 (Bank B, FDIC) (C-FINANCIAL-R01); state breach and data security law, with Fla. Stat. 501.171 as the worked example |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | Director of Information Security (Qualified Individual) and the PCI Program Manager, with the Chief Risk and Compliance Officer; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Applicability
Applicability was decided first, one rule at a time, before any gap was rated. Regulatory text comes from the eCFR (point-in-time text for 2026-09-23), the U.S. Code, and the Florida Legislature's statute site; card brand rules come from Visa's public documents. The Small sample's verified citations were reused where they still apply, and each was re-checked for this size: none of these rules has a size threshold that changes the answer between Small and Mid-Market, but the company's second sponsor bank and its board do change two answers (sections 1.4 and 1.2).

### 1.1 PCI DSS v4.0.1: applies, as a service provider (primary)
- **Why it applies.** PCI DSS is not a law. It binds the company by contract: both sponsor agreements and the card brands' rules require every entity that stores, processes, or transmits cardholder data for a brand member to comply. The company does all three for its merchants and ISV partners, so PCI DSS calls it a **service provider**.
- **One assessment for two platforms.** The acquired Integrated Payments gateway (Cloud B) had its own 2025 AOC. From 2026 it is part of the company's CDE, and both sponsor banks agreed (2026-06-12) to accept one combined AOC by 2026-12-15. This analysis therefore rates every row across both platforms. A row is Met only when it is met on both.
- **Service-provider-only requirements** are assessed as their own rows: 3.6.1.1, 8.3.10.1, 11.4.6, 11.5.1.1, 12.4.1, 12.4.2, 12.4.2.1, 12.5.2.1, 12.5.3, 12.9.1, and 12.9.2. Others are Not applicable for the reasons in the CSV: 3.7.9 (no keys shared with customers), 8.2.3 (no remote access to customer premises), 11.4.7 and Appendix A1 (not a multi-tenant hosting provider). 8.3.10 and 10.7.1 are superseded by 8.3.10.1 and 10.7.2.
- **Validation level: set by the card brands, not by PCI SSC.** Under Visa's published service provider levels, a service provider that stores, processes, or transmits more than 300,000 Visa transactions a year is **Level 1**: an annual on-site assessment by a QSA and an AOC. At about 820 million transactions a year the company is Level 1. Other brands publish their own criteria; the sponsor banks confirm which apply.
- **What changes from the Small sample.** The company now controls physical CDE locations (the colocation cages), so requirement 9 and wireless testing (11.2) apply to its own sites, not only through a cloud provider's AOC.
- **Appendices.** A2 does not apply (no SSL or early TLS) and A3 does not apply (not designated).
- **Size.** PCI DSS has no size exemption. Size affects only the validation level.

### 1.2 FTC Safeguards Rule, 16 CFR Part 314: applies
- **Financial institution.** The rule applies to financial institutions under FTC jurisdiction: businesses engaged in an activity that is financial in nature under 12 U.S.C. 1843(k), which incorporates 12 CFR 225.28 (16 CFR 314.1(b); 314.2(h)(1)). Data processing of financial, banking, or economic data is listed in 12 CFR 225.28(b)(14). Card processing is the company's whole business.
- **FTC jurisdiction.** The company is not a bank, a bank subsidiary, a broker-dealer, or an insurer, so no other federal functional regulator enforces GLBA safeguards against it.
- **Customer information of other institutions.** Cardholders are customers of their issuing banks. The rule still covers their data in the company's possession (314.1(b)).
- **Merchant owner data.** Merchants obtain services for business purposes, so merchant owners are not "consumers" under 314.2. Their SSNs and bank details are protected by state law and company policy (POL-04).
- **No small-institution exception.** 314.6 relieves institutions with fewer than 5,000 consumers from some elements. The company holds data on millions of cardholders.
- **Board report.** Unlike the Small sample, the company has a board. 314.4(i) requires the Qualified Individual to report in writing, regularly and at least annually, to the board of directors or equivalent governing body, covering the program's overall status and compliance with Part 314, and material matters such as risk assessment, risk management and control decisions, service provider arrangements, test results, security events, and recommended changes.
- **FTC notice, 314.4(j).** A notification event is the acquisition of unencrypted customer information without the individual's authorization; unauthorized access is presumed to be acquisition unless there is reliable evidence it could not have been (314.2(m)). If it involves the information of at least 500 consumers, notify the FTC as soon as possible and no later than 30 days after discovery. The company counts affected cardholders toward the 500 (conservative reading carried over from the Small sample; counsel confirms the count for any real event).

### 1.3 Bank service provider notice to Bank A, 12 CFR 53.4 (C-FINANCIAL-R01): applies
Part 53 applies to national banks and their bank service providers (53.1(c)). A bank service provider is a person that performs covered services; covered services are services subject to the Bank Service Company Act (53.2(b)(2), (b)(5)). Bank A's sponsor agreement names the company's clearing, settlement, reconciliation, and merchant funding file services as performed for the bank and subject to examination under 12 U.S.C. 1867(c). The company must notify at least one bank-designated point of contact as soon as possible after determining that a computer-security incident has materially disrupted or degraded, or is reasonably likely to, covered services for four or more hours (53.4(a)); without a designated contact, the bank's CEO and CIO or two people of comparable responsibility (53.4(a)(2)). Previously communicated maintenance, testing, and updates are excluded (53.4(b)). There is no size threshold.

### 1.4 Bank service provider notice to Bank B, 12 CFR 304.24 (C-FINANCIAL-R01): applies (new at this size)
Subpart C of Part 304 applies to insured state nonmember banks and to their bank service providers (304.21(c); 304.22(b)(2)). Bank B is an FDIC-supervised insured state nonmember bank, and its sponsor agreement (in effect 2025-10-01) has the same 1867(c) clause, so the same four-hour notice duty applies (304.24(a)-(b), text identical in substance to 53.4). In the Small sample this rule was pending; here it is in force, and Bank B's designated contacts are missing (G-109).

### 1.5 Federal Reserve parallel, 12 CFR 225.303: does not apply
It applies only to services for Board-supervised banking organizations (225.300(c); 225.301(b)(1)). Neither sponsor bank is one.

### 1.6 State law: applies; Florida as the worked example
Breach notification and data security laws apply in each state where affected individuals reside. Three Florida duties were assessed as rows: reasonable measures to protect personal information (501.171(2)), third-party agent notice to merchants within 10 days of determination (501.171(6)(a)), and disposal of customer records (501.171(8)). Other states' laws are applied by counsel during an incident (P08).

### 1.7 Considered and not applicable
| Requirement | Decision |
|---|---|
| Interagency Guidelines (C-FINANCIAL-R02), 12 CFR 30 App. B and 12 CFR 364 App. B | Apply to the sponsor banks, not the company. They reach the company only through the sponsor agreements' service provider oversight terms, which both banks test in annual due diligence (P09) |
| NCUA 12 CFR 748.1(c) (C-FINANCIAL-R03) | Not a credit union and serves none |
| SEC Regulation SCI (C-FINANCIAL-R04) | Not an SCI entity; the company is privately held and not an SEC registrant, so SEC cyber disclosure rules do not apply either |
| NYDFS 23 NYCRR Part 500 (C-FINANCIAL-R05) | Applies only to entities licensed, registered, or chartered under New York banking, insurance, or financial services law. The company holds no New York license, so the 500.19(a) exemption analysis is not reached |
| CIRCIA (C-FINANCIAL-R06) | Proposed rule only (89 FR 23644); no final rule as of 2026-09-25. Tracked in section 6, not applied |
| PCI PIN Security Requirements | The company does not acquire PIN transactions and holds no PIN keys |
| Money transmission licensing | Merchant funds settle through the sponsor banks' accounts; licensing is outside this security library and was not analyzed |

## 2. Method
1. **Requirements.**
   - PCI DSS was decomposed at the requirement-group level (1.1 to 12.10), with every service-provider-only requirement as its own row and with defined requirements broken out where the evidence differed or the gap was High (1.3.2, 2.2.2, 3.2.1, 3.3.1, 6.3.3, 6.4.3, 7.2.4, 7.2.5.1, 10.4.1, 11.3.1.2, 11.6.1, 12.3.1, 12.3.4). A group row that has a broken-out child says so in its summary and rates the rest of the group. PCI DSS is copyrighted, so rows give the requirement number and a short topic label in our own words. Read the full text in the PCI SSC document library.
   - The Safeguards Rule was decomposed to the paragraph level of 16 CFR 314.4, 12 CFR 53.4 and 304.24 to their paragraphs, and Fla. Stat. 501.171 to the three subsections above.
2. **Crosswalk.** Each row is mapped to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. These are **author mappings**: no official NIST mapping from PCI DSS v4.0.1, 16 CFR 314, 12 CFR 53, or Fla. Stat. 501.171 to CSF 2.0 or SP 800-53 exists.
3. **Evidence.** Interviews with the process owners; documents (policies, the 2025 AOCs and ROC, both sponsor agreements, service provider contracts); configuration exports from both clouds, the cages, the identity provider, PAM, and the SIEM; browser captures of both payment pages (2026-07-21); and a walkthrough of the primary cage (2026-07-23).
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested. Samples were chosen at random from system-generated populations, sized with the co-sourced internal audit firm's attribute sampling table (25 items for a control that operates many times a year at moderate risk; all items for small populations):
   - terminations: 25 of 142; transfers: 25 of 88;
   - Cloud B IAM users and access keys: all 61;
   - service accounts: 40 of 212;
   - production changes: 30 core and 15 Integrated Payments;
   - critical vulnerability findings on cage servers: 60 of 188 (Q1-Q2 2026);
   - service provider files: 34 of 34;
   - call recordings: 60 from June 2026; pre-2025 support tickets: 200;
   - cage visits: 30 of 410; key ceremonies: 3 of 3 (2026);
   - Integrated Payments merchant contact records: 50;
   - incidents: 10 of 46 (2025-2026); quarterly reviews: all quarters since 2025-07.
   Each `evidence` cell names the sample and its result.
5. **Status and gap risk.** Each row is Met, Partially met, Not met, or Not applicable. Gaps are rated with the P01 scale. High gaps are the ones that would likely produce a "not in place" finding at the 2026 ROC or leave a High or Very High risk in P01 untreated.

This is a gap analysis, not a PCI DSS assessment. Only the QSA's ROC can conclude on compliance.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI DSS Req. 1 Network security controls | 2 | 4 | 0 | 0 | 6 |
| PCI DSS Req. 2 Secure configurations | 0 | 3 | 0 | 1 | 4 |
| PCI DSS Req. 3 Protect stored account data | 1 | 7 | 0 | 1 | 9 |
| PCI DSS Req. 4 Protect data in transmission | 2 | 0 | 0 | 0 | 2 |
| PCI DSS Req. 5 Anti-malware | 2 | 2 | 0 | 0 | 4 |
| PCI DSS Req. 6 Secure systems and software | 1 | 5 | 1 | 0 | 7 |
| PCI DSS Req. 7 Restrict access by need to know | 2 | 2 | 1 | 0 | 5 |
| PCI DSS Req. 8 Identify and authenticate | 3 | 3 | 1 | 2 | 9 |
| PCI DSS Req. 9 Physical access | 3 | 1 | 0 | 1 | 5 |
| PCI DSS Req. 10 Logging and monitoring | 1 | 6 | 0 | 1 | 8 |
| PCI DSS Req. 11 Security testing | 2 | 6 | 1 | 1 | 10 |
| PCI DSS Req. 12 Policies and programs | 4 | 10 | 2 | 0 | 16 |
| PCI DSS Appendices A1 to A3 | 0 | 0 | 0 | 3 | 3 |
| FTC Safeguards Rule 16 CFR 314.4 | 3 | 14 | 0 | 0 | 17 |
| 12 CFR 53.4, 304.24, and 225.303 | 1 | 3 | 1 | 1 | 6 |
| Fla. Stat. 501.171 (worked example) | 0 | 3 | 0 | 0 | 3 |
| **Total** | **27** | **69** | **7** | **11** | **114** |

**Gap risk ratings (76 rows Partially met or Not met):** 21 High, 40 Moderate, 15 Low. PCI DSS accounts for 55 of the gaps (49 Partially met, 6 Not met), including 18 of the 21 High gaps.

**The 7 Not met rows:** 6.3.3 (critical patches and unsupported servers), 7.2.5.1 (service account reviews), 8.3.10.1 (Integrated Payments portal users), 11.4.6 (segmentation not retested after a change), 12.5.2.1 (scope not confirmed after significant change), 12.5.3 (no review after the acquisition), and 12 CFR 304.24(a)(1)-(2) (no Bank B contacts).

**What the pattern says:**
- **The core platform is close to compliant.** Most core controls that the Small sample lacked (payment page script controls, covert channel detection, merchant MFA for high-risk roles, quarterly reviews, the PCI DSS charter) are in place and were Met or nearly met on the core side.
- **The acquisition is the gap.** 48 of the 76 gaps involve the Integrated Payments gateway or Cloud B, including 15 of the 21 High gaps. The same requirement is met on one platform and not on the other.
- **Legacy settlement is the second cluster.** The unsupported servers (6.3.3), default credentials (2.2.2), the interconnect route (1.3, 11.4.6), and PAN retention (3.2.1) all sit in the colocation cages.
- **Bank notices are designed but untested.** Both 12 CFR duties now have a written decision step, but Bank B's contacts are missing and neither bank has been part of a test.

## 4. Priority gaps
Every High gap must be closed, or have an interim measure the QSA can assess, before ROC fieldwork starts on 2026-11-09.

| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Combined scope not confirmed; inventory missing Cloud B | PCI 12.5, 12.5.2.1, 12.5.3 (G-077 to G-079) | High | Combined scope document, inventory, and data-flow diagrams; report to the COO and audit committee | Director of Information Security | 2026-10-16 |
| Segmentation not retested after the interconnect change; route into the settlement CDE | PCI 1.3, 11.4.6 (G-003, G-065) | High | Remove the route; segmentation test of all CDEs | VP Platform Engineering; Director of Information Security | 2026-10-15 |
| Default credentials on settlement server management interfaces | PCI 2.2.2 (G-009) | High | Credentials changed 2026-08-14; dedicated management network behind PAM; quarterly scan | VP Platform Engineering | 2026-10-15 |
| Gateway hosted payment fields without script controls or tamper-detection | PCI 6.4.3, 11.6.1 (G-031, G-069) | High | Reuse the core script controls and tamper-detection service | Director of Integrated Payments Engineering | 2026-10-30 |
| Integrated Payments portal users with passwords only | PCI 8.3.10.1 (G-043); 314.4(c)(5) (G-095) | High | MFA for partner administrators and refund or funding account roles; dynamic risk analysis for others | Director of Integrated Payments Engineering | 2026-10-30 |
| Cloud B standing administrator roles; departed users' keys | PCI 7.2, 8.2 (G-034, G-039); 314.4(c)(1) (G-091) | High | PAM with security keys; federate Cloud B to the identity provider; remove IAM users | Director of Integrated Payments Engineering | 2026-11-06 |
| Cloud B not monitored; open egress; no covert channel detection | PCI 1.3.2, 10.4.1, 11.5.1.1 (G-004, G-055, G-068); 314.4(c)(8) (G-098) | High | SIEM and MSSP onboarding; egress allow list; DNS analytics | Director of Information Security | 2026-11-06 |
| Cloud B penetration test overdue | PCI 11.4 (G-064) | High | External and internal test of Cloud B and the interconnect | Director of Information Security | 2026-10-31 |
| Card verification codes in call recordings | PCI 3.3.1 (G-013) | High | Automatic pause; purge affected recordings | Director of Merchant Services | 2026-11-30 (interim: purge of the affected recordings and daily supervisor checks by 2026-11-06) |
| PAN kept 7 years in the settlement archive | PCI 3.2.1 (G-012) | High | 18-month limit; purge or truncate older records | Director of Settlement and Treasury Operations | 2026-11-06 |
| Critical patches late; unsupported settlement operating system | PCI 6.3.3 (G-029) | High | Monthly windows; compensating controls and a targeted risk analysis by 2026-11-06; replacement by 2027-06-30 | VP Platform Engineering | 2027-06-30 |
| Incident response plan not tested in 12 months; gateway not covered until 2026-09-15 | PCI 12.10 (G-085) | High | Executive tabletop on the gateway scenario | Director of Information Security | 2026-11-04 |
| Bank B designated contacts missing | 12 CFR 304.24(a)(1)-(2) (G-109) | Moderate | Request and record contacts; quarterly confirmation | Chief Risk and Compliance Officer | 2026-10-15 |
| Service providers without AOC or matrix | PCI 12.8 (G-082); 314.4(f) (G-101) | Moderate | Collect AOCs or include in the ROC; matrices | Chief Risk and Compliance Officer | 2026-10-31 |
| Qualified Individual report did not cover the acquisition | 314.4(i) (G-104) | Moderate | 2026 report to the board covering the acquisition | Director of Information Security | 2026-12-15 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Ready for the ROC** | 2026-09-15 to 2026-11-06 | Combined scope; segmentation retest; Cloud B onboarded to SIEM, MSSP, and PAM; hosted payment field controls; portal MFA; archive purge; Bank B contacts; executive tabletop | PCI 1.3, 1.3.2, 2.2.2, 3.2.1, 6.4.3, 7.2, 8.2, 8.3.10.1, 10.4.1, 11.4, 11.4.6, 11.5.1.1, 11.6.1, 12.5, 12.5.2.1, 12.5.3, 12.10; 304.24(a)(1)-(2) |
| **2. Close the rest** | 2026 Q4 to 2027 Q1 | Service account reviews and secrets vault; TRAs for the gateway; ISV responsibility matrix; recordings fix; Qualified Individual report to the board; settlement ransomware tabletop with both banks | PCI 3.3.1, 7.2.5.1, 8.6, 12.3.1, 12.8, 12.9.2; 314.4(c)(6), (h), (i); 53.4(a); 304.24(a) |
| **3. Retire legacy** | 2027 Q1 to Q2 | Replacement of the unsupported settlement servers; funding file signing; automated failover; standards issued (P06) | PCI 6.3.3, 12.3.4, 2.2; 314.4(c)(2) |
| **4. Converge** | 2027 Q3 | Gateway migrated into the Cloud A landing zone; SOC 2 Type 2 observation period under way (P09) | Most remaining Cloud B rows |

Progress is reported monthly to the COO and quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending regulatory changes
- **PCI DSS.** v4.0.1 is the current version in the PCI SSC document library (library note: re-checked 2026-09-26). Every future-dated v4.0 requirement took effect on 2025-03-31 and is assessed here as a current requirement. No newer version is assumed.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226, 89 FR 23644, 2024-04-04). No final rule had been published as of 2026-09-25. **Not a current obligation.** If finalized as proposed, coverage under proposed 226.2 would include an entity in a critical infrastructure sector that exceeds the SBA size standard for its NAICS code. At $100.0 million in receipts against a $47.0 million standard, the company would likely be covered and would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours. The final scope may change, so the company will re-check when the final rule publishes.
- **Visa What To Do If Compromised** was revised (v10.0, effective 2026-06-25). The P08 clocks use that version.

The `pending_rule_change` column in `gap-analysis.csv` is "None" for every row, because no proposed rule changes a requirement assessed here.

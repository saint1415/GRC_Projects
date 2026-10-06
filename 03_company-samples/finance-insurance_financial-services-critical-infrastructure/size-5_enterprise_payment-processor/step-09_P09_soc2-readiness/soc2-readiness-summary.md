# SOC 2 Readiness Summary: Cris Santos Company | Financial Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded merchant payment processor) |
| Tier / Vertical | Enterprise / Financial Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 Integrated Payments platform (about 2,600 ISV partners; about 50,000 merchants); SL-2 Merchant processing and settlement services (about 360,000 merchants, about 300 enterprise merchants, and sponsor Banks A, B, and C) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new) Processing Integrity. SL-2: Security, Availability, Processing Integrity, and Confidentiality. Privacy is out of scope for both |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Processing Integrity added). SL-2: first Type 2, period 2027-07-01 to 2027-12-31 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-28 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
The company is a service organization for merchants, software partners, and banks, so its customers ask for a CPA's report on its controls. It already has two kinds of assurance; SOC 2 fills the gap between them.
- **PCI DSS ROC and AOC** cover cardholder data protection and are the main assurance the card brands and sponsor banks require. They do not cover availability, processing integrity, or confidentiality of non-card data.
- **SOC 1 Type 2 (since 2019)** covers settlement and merchant funding controls relevant to user entities' financial reporting. It is the right report for the banks' and merchants' auditors but not for their security and resilience reviews.
- **SL-1 Integrated Payments platform** has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2024. The 2025 report had no exceptions. ISV partners that resell payments ask for **Processing Integrity**, because API authorization results and partner settlement reports drive their own customers' money.
- **SL-2 Merchant processing and settlement services** has no SOC 2 report. Two sponsor banks asked for one in their 2026 due diligence (to support their oversight of the company as a service provider under the Interagency Guidelines), and the largest enterprise merchants now require one in their vendor programs.

**Alternatives considered:** extending the SOC 1 (it is scoped to financial reporting and would not answer the banks' resilience questions); relying on the ROC (it does not address availability or processing integrity); the banks' own on-site examinations (they do not replace a report the company can share with merchants).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both SOC 2 reports, the SOC 1, the ROC, and the SOX program. Cloud A, Cloud B, the DC-2 colocation provider, and the MFT software vendor are subservice organizations presented with the carve-out method; their own AOCs and SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 Integrated Payments platform | SL-2 Merchant processing and settlement services |
|---|---|---|
| Services | Partner APIs for authorization and tokenization, hosted payment fields in ISV checkouts, partner portal, partner settlement reports | Authorization (Merchant Acquiring), clearing, settlement, reconciliation, merchant funding files to Banks A, B, and C, chargebacks |
| Infrastructure | Cloud B (6 accounts), second-region warm standby, landing zone controls (P04) | Cloud A CDE accounts (two regions); DC-1 mainframe and midrange servers; DC-2 recovery site; MFT appliances; payment HSMs (P02) |
| Software | Company-built APIs and hosted fields; token vault | Authorization switch and gateways; settlement and funding platform; chargeback system |
| People | Integrated Payments engineering and partner support; Cyber Fusion Center; identity and cloud teams | Core platform engineering; settlement and treasury operations; key custodians; Cyber Fusion Center |
| Data | Card data (tokenized), partner and merchant data, partner settlement data | Card data, clearing and funding files, merchant bank account data, settlement records |
| Procedures | P06 policy hierarchy; P08 runbook; partner support procedures | P06; P08; settlement operating procedures; SOC 1 control descriptions |
| Subservice organizations (carved out) | Cloud B provider; content delivery service | Cloud A provider; DC-2 colocation provider; MFT software vendor (support); card networks are not subservice organizations |

**Why Privacy is out of scope.** The company handles personal information as a service provider for merchants, partners, and banks, which make the privacy commitments to individuals. No user entity asked for the Privacy category. Confidentiality covers card data and merchant data.

## 3. Readiness results
**SL-1 Integrated Payments platform**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 28 | 5 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 Merchant processing and settlement services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 19 | 13 | 1 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1** can continue its annual Type 2 on the existing categories, with five Security items partially ready: phishing-resistant MFA and PAM coverage in Cloud B (CC6.1), the standing pipeline administrator (CC6.3, CC8.1), hosted field tamper-detection (CC6.8), and the enterprise executive exercise (CC7.4). All close by 2027-01-31, so they should be operating for most of the 2027 period; if any is late, the report will describe it. The new Processing Integrity criteria need written processing commitments (PI1.1) and a documented daily reconciliation of partner settlement reports to Bank B funding (PI1.4).

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC6.1 (password-only settlement operators and embedded secrets) and A1.3 (settlement recovery missed its RTO in testing). Partially ready: CC2.3, CC3.1, CC6.2, CC6.6, CC6.7, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, C1.1, PI1.3. These are the same weaknesses Internal Audit found in the CPPP (P07). Closing POAM-002 to POAM-008, POAM-011, POAM-013, and POAM-014 by 2027-03-31, and passing the settlement retest with Bank A in 2027 Q1, makes SL-2 ready to start its period on 2027-07-01. Items that close later (CC6.8 server replacement, CC9.1 joint tests with Banks B and C, both due 2027-06-30) have compensating controls today and would be described in the report if still open.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-2 CC2.3, CC3.1, CC6.1, CC6.2, CC6.6, CC7.4, CC8.1, CC9.2, C1.1; SL-1 CC6.3, CC7.4, CC8.1, PI1.1 | Bank C contacts; SL-2 system description and commitments; operator MFA and secret removal; contractor disablement automation; segmentation fix; executive tabletop; emergency change control; vendor AOCs; data lake PAN blocking; Cloud B pipeline identity; SL-1 PI commitments | Contact register; MFA reports; segmentation retest; tabletop report; change reviews; vendor register |
| 2027 Q1 | SL-2 CC6.7, CC7.1, CC7.2, CC7.5, A1.3, PI1.3; SL-1 CC6.1, CC6.8, PI1.4 | Internal transfer encryption; patch automation; mainframe log forwarding; MFT file-level logging; recovery automation and retest with Bank A; fee table validation; Cloud B keys and PAM; hosted field tamper-detection; partner settlement reconciliation | DR retest report; patch metrics; SIEM source list; coverage reports; reconciliation reports |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-1 period already running since 2027-01-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-2 CC6.8, CC9.1 | Unsupported server replacement; joint tests with Banks B and C | Decommission records; exercise reports |
| 2027 Q3 | SL-2 period starts 2027-07-01 | Evidence collection for all SL-2 criteria | All items in the evidence map |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports (16 of 25). Status: 13 collecting, 5 ready, 7 not started (each tied to a POA&M item or a new SL-1 Processing Integrity control).

**User entity communication:** SL-1 partners receive the 2025 report, a bridge letter, and a note on the Processing Integrity addition. Banks A, B, and C and the enterprise merchants receive this summary, the SOC 1 report, the 2025 AOC, a bridge letter describing the remediation, and the expected SL-2 report date (2028-02).

# Regulatory Gap Analysis: Cris Santos Company | Accommodation and Food Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hotel franchisor, manager, and owner; 750 hotels in 33 states and DC) |
| Tier / Vertical | Enterprise / Accommodation and Food Services |
| Regulations analyzed | PCI DSS v4.0.1 as **merchant and service provider** (primary, contractual, N72-R01); FTC Act Section 5 and the FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (N72-R02); FTC Disposal Rule (N72-R03); state breach notification and data security laws (N72-R04, Florida worked example); Florida guest register and emergency pricing statutes; CCPA cybersecurity audit regulations; SEC Form 8-K Item 1.05 and Reg S-K Item 106; applicability checks for Illinois BIPA (N72-R05), the Florida Digital Bill of Rights, and CIRCIA (N72-R06) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Director of Payments and PCI Compliance and the Chief Privacy Officer; sampling reperformed by Internal Audit for 10 rows |
| Approved | CISO and General Counsel, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability

### 1.1 Merchant, service provider, and franchisor
**PCI DSS applies by contract in two roles.**
- **Merchant.** The 38 owned and leased hotels use the company's merchant accounts, and the company operates every payment system at the 72 managed hotels under the management agreements. The acquirer agreement (fictional term) requires an annual Report on Compliance by a QSA for this program. PCI SSC sets no size tiers; card brands and acquirers set merchant levels and validation methods, and their thresholds were not verified from a card brand primary source, so no level number is stated here.
- **Service provider.** The CRS stores guarantee card data for franchised hotels and SL-2 clients, and the company administers the PMS tenant, the tokenization service, and the managed property network for franchisees. That makes it a third-party service provider to 640 franchisees and 180 distribution clients. The **service-provider-only requirements** therefore apply: 11.4.6 (segmentation tests every six months), 12.4.1 and 12.4.2 (executive responsibility and quarterly reviews), 12.5.2.1 (scope confirmed every six months), and 12.9.1 and 12.9.2 (acknowledgment and support for customers).

**Franchisor.** Each franchisee is its own merchant and validates its own PCI DSS compliance; the company does not validate for them. But *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015) (No. 14-3514, opinion filed 2015-08-24), affirmed that the FTC may treat unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a) in a case about a hotel franchisor. The FTC alleged that the franchisor, which managed its branded hotels' PMS systems, had no firewalls between hotel PMS systems, its corporate network, and the internet; allowed default passwords and unrestricted vendor access; and kept card data in clear text. **The company is measured on the systems it designs, connects, or manages for franchisees**, so the franchise-specific findings sit under the FTC rows (G-076) as well as PCI DSS.

**Current version.** PCI DSS v4.0.1 is current. Its publication added no new requirements; requirements introduced as future-dated in v4.0 have been in force since 2025-03-31 (PCI SSC blog, 2024-06-11). PCI SSC ran a request for comments on v4.0.1 from 2026-06-03 to 2026-07-20 toward the next version.

### 1.2 Other regulations
| Regulation | Applies? | Basis |
|---|---|---|
| FTC Act Section 5 (N72-R02) | **Yes** | For-profit company; no size threshold. Deception (45(a)(1)) for security, privacy, and loyalty statements; unfairness (45(n)) for unreasonable security |
| 16 CFR Part 464 (N72-R02) | **Yes** | Covers "short-term lodging, including temporary sleeping accommodations at a hotel" (464.1). 90 FR 2066 (rule text at 2166), published 2025-01-10, effective 2025-05-12; text checked on eCFR as of 2026-09-23. Any offer, display, or advertisement of a price must show the total price, including mandatory resort and destination fees, more prominently than other pricing (464.2(a)-(b)); government charges may be excluded but must be disclosed with the final amount before the guest pays (464.1, 464.2(c)); fees must not be misrepresented (464.3) |
| FTC Disposal Rule (N72-R03) | **Yes** | The company obtains background-check reports on applicants (16 CFR 682.3) |
| State breach notification laws (N72-R04) | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example |
| Fla. Stat. 509.101(2) | **Yes** | 118 Florida hotels must keep a guest register with dates of occupancy and rates; it may be electronic; registers older than 2 years need not be made available |
| Fla. Stat. 501.160 | **Yes (cautious reading)** | Unconscionable prices during a declared state of emergency. The statute names dwelling units and essential commodities rather than hotels expressly; the company treats room rates as covered. Other states' price gouging laws are handled the same way |
| CCPA and its cybersecurity audit regulations (11 CCR 7120-7124) | **Yes** | California hotels and guests; revenue above $26,625,000. The cybersecurity audit applies to businesses that meet the revenue test and process personal information of 250,000 or more consumers; first report due 2028-04-01 for businesses with 2026 revenue over $100 million. Effective 2026-01-01 |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| Florida Digital Bill of Rights (Fla. Stat. 501.702) | **No** | A "controller" must exceed $1 billion in global gross annual revenue **and** (a) earn 50% or more of revenue from online advertising, (b) operate a consumer smart speaker and voice command service, or (c) operate an app store with at least 250,000 applications. The company exceeds $1 billion but meets none of (a) to (c) |
| Illinois BIPA (N72-R05) | **No, by design** | The company collects no biometric identifiers at its Illinois hotels: time clocks are badge-based and mobile check-in face matching is disabled in Illinois (P10 AI-005). The statute text could not be re-verified (ilga.gov unreachable 2026-10-06), so no BIPA requirement is analyzed |
| CIRCIA (N72-R06) | **Not in force** | Final rule not published as of 2026-09-25. Proposed 226.2(a) would cover the company because it exceeds the SBA size standard for NAICS 721110 |
| SOX Section 404 | Separate program | IT general controls over ERP, payroll, and owner and franchise fee accounting are tested by the SOX program |
| HIPAA; FTC Safeguards and Red Flags Rules | **No** | Not a covered entity; no consumer credit extended (the co-brand card is issued by a bank) |

## 2. Method
1. **Decompose.** PCI DSS was broken down into its requirement groups, with 14 defined requirements taken to their own rows because they are service-provider-only or carry the largest risk (3.3.1, 5.4.1, 6.4.3, 8.4.2, 10.4.1.1, 11.4.6, 11.6.1, 12.3.1, 12.4.1, 12.4.2, 12.5.2.1, 12.9.1, 12.9.2, 12.10.7), plus the appendices. **Labels are short topics written for this analysis, not PCI SSC text**, because PCI DSS is copyrighted; read the requirement text in the company's licensed copy of v4.0.1. Other regulations were broken into citation-level duties from the primary text: eCFR (16 CFR Part 464 and 17 CFR 229.106, versions as of 2026-09-23), the SEC's compliance guide for Item 1.05, the Florida Legislature's 2026 statutes, and the CPPA's approved regulation text.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1 was used.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls and populations under 250 used 25 to 40 items; configuration, account, contract, and mailbox data were checked in full with analytics. Selections were random. **44 rows were tested by sampling or full-population analytics; 29 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 3 | 2 | 0 | 0 | 5 |
| PCI Req 2 Secure configurations | 2 | 1 | 0 | 0 | 3 |
| PCI Req 3 Stored account data | 4 | 3 | 0 | 0 | 7 |
| PCI Req 4 Transmission | 1 | 1 | 0 | 0 | 2 |
| PCI Req 5 Malware and phishing | 3 | 1 | 0 | 0 | 4 |
| PCI Req 6 Secure systems and software | 3 | 3 | 0 | 0 | 6 |
| PCI Req 7 Restrict access | 2 | 1 | 0 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 3 | 4 | 0 | 0 | 7 |
| PCI Req 9 Physical access and devices | 3 | 2 | 0 | 0 | 5 |
| PCI Req 10 Logging | 5 | 3 | 0 | 0 | 8 |
| PCI Req 11 Security testing | 2 | 4 | 1 | 0 | 7 |
| PCI Req 12 Policies and programs | 10 | 5 | 0 | 0 | 15 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **41** | **30** | **1** | **3** | **75** |
| FTC Act Section 5 | 1 | 3 | 0 | 0 | 4 |
| 16 CFR Part 464 (fees) | 2 | 3 | 1 | 0 | 6 |
| FTC Disposal Rule | 1 | 0 | 0 | 0 | 1 |
| State breach and data security laws (generic and Fla. Stat. 501.171) | 3 | 2 | 1 | 0 | 6 |
| Fla. Stat. 509.101(2) guest register | 1 | 0 | 0 | 0 | 1 |
| Fla. Stat. 501.160 emergency pricing | 0 | 1 | 0 | 0 | 1 |
| CCPA cybersecurity audit regulations | 0 | 1 | 0 | 0 | 1 |
| Florida Digital Bill of Rights | 0 | 0 | 0 | 1 | 1 |
| Illinois BIPA | 0 | 0 | 0 | 1 | 1 |
| SEC Form 8-K Item 1.05 | 0 | 3 | 0 | 0 | 3 |
| SEC Reg S-K Item 106 | 4 | 2 | 0 | 0 | 6 |
| CIRCIA | 0 | 0 | 0 | 1 | 1 |
| **Total** | **53** | **45** | **3** | **6** | **107** |

**PCI DSS:** 41 Met, 30 Partially met, 1 Not met (11.4.6, the overdue service provider segmentation test), 3 Not applicable (75 rows). The gaps are concentrated in four places: the legacy POS at 41 hotels, vendor remote access, the resort systems and microsites, and card data in email. None is in the tokenization service or the vault, which the QSA tested without exceptions in the 2026 service provider ROC.

**Gap risk levels across all regulations:** High 16, Moderate 29, Low 3.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-002 | PCI 1.2 | Hub rule let franchised segments reach the CRS integration tier | Verify removal; automated rule checks (POAM-004) | Director of Network Engineering | 2026-10-31 |
| G-003 | PCI 1.3 | Legacy POS shares segments with back office PCs at 9 hotels | Isolate now; replace (POAM-001) | Director of Network Engineering | 2026-12-31 |
| G-007 | PCI 2.2 | Vendor default credentials on legacy POS servers at 3 hotels | Changed; sweep all 41 hotels (POAM-010) | POS Operations Manager | 2026-09-30 |
| G-010 | PCI 3.2 | About 4,800 emails with card numbers | Purge; secure payment links (POAM-006) | Director of Payments and PCI Compliance | 2026-11-30 |
| G-011 | PCI 3.3.1 | 390 emails include card security codes | Purge immediately (POAM-006) | Director of Payments and PCI Compliance | 2026-10-15 |
| G-017 | PCI 4.2 | Clear-text card data inside hotel networks at 41 hotels | Replace legacy POS (POAM-001) | POS Operations Manager | 2027-06-30 |
| G-026 | PCI 6.4.3 | No script controls on 3 resort microsites | Interim monitoring; migrate (POAM-015) | Vice President, Digital and Loyalty | 2026-12-15 |
| G-032 | PCI 8.2 | Late resort terminations; inactive franchisee accounts; always-on vendor accounts | POAM-003; POAM-008; POAM-005 | Director of Identity and Access Management | 2026-12-31 |
| G-034 | PCI 8.4 | 5 vendors use their own remote tools without company MFA | All vendor access through PAM (POAM-005) | Director of Identity and Access Management | 2026-12-31 |
| G-035 | PCI 8.4.2 | Legacy POS vendor sessions into the cardholder data environment without company MFA | POAM-005 | Director of Identity and Access Management | 2026-12-31 |
| G-054 | PCI 11.4 | Segmentation test found the hub rule | POAM-004 | Director of Security Operations | 2026-10-31 |
| G-055 | PCI 11.4.6 | Service provider segmentation test missed in 2025 H2 | Six-month calendar; retest (POAM-004) | Director of Security Operations | 2026-10-31 |
| G-057 | PCI 11.6.1 | Resort microsite payment pages not monitored | POAM-015 | Vice President, Digital and Loyalty | 2026-12-15 |
| G-076 | 15 U.S.C. 45(a)(1); 45(n) | Franchise network, vendor access, and legacy POS gaps match practices alleged in *Wyndham* | POAM-001, POAM-004, POAM-005, POAM-012 | CISO | 2027-06-30 |
| G-098 | Form 8-K Item 1.05 | Playbook not exercised with the current disclosure committee | Tabletop 2026-11-12 (POAM-014) | General Counsel | 2026-11-30 |
| G-099 | Form 8-K Item 1.05 (materiality determination) | Escalation never tested end to end; no guidance for franchise-originated incidents | POAM-014 | General Counsel | 2026-11-30 |

**Before QSA fieldwork for the 2026 merchant ROC (starts 2026-10-19):** close G-007, G-011, and G-055, and have either remediation or documented compensating controls for G-002, G-003, G-010, G-017, G-034, and G-035. Where a requirement cannot be met by the ROC date, the Director of Payments and PCI Compliance agrees the approach with the acquirer and the QSA rather than reporting it "In Place" without evidence.

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Hub rule verification and segmentation retest (POAM-004); credential sweep (POAM-010); security code purge and mailbox cleanup (POAM-006); vendor access into PAM (POAM-005); card display permission cleanup (POAM-007); franchisee account inactivity job (POAM-008); disclosure committee tabletop (POAM-014); chatbot and feed total price fixes (POAM-021); resort microsites migrated (POAM-015); pooled benchmarking opt-out and emergency pricing cap (POAM-020); 2026 merchant ROC | PCI 1.2, 1.3, 2.2, 3.2, 3.3.1, 3.4, 6.4.3, 8.2, 8.4, 11.4.6, 11.6.1; 16 CFR 464.2, 464.3; Fla. Stat. 501.160; Form 8-K Item 1.05 | Segmentation report; ROC and AOC; tabletop report; price display test results |
| 2027 Q1 | Resort migrations and identity federation (POAM-002; POAM-003); SIEM collectors (POAM-011); franchise side letters and technical minimums (POAM-012); guest data retention schedule and first purge (POAM-018); lock server replacements (POAM-009); loyalty MFA for redemptions (POAM-017); Internal Audit test of the Item 106 statements | PCI 8.2, 10.2, 10.4, 12.8, 12.9.1; Fla. Stat. 501.171(8); 45(a)(1); Item 106 | Migration records; contract side letters; purge reports |
| 2027 Q2 | Legacy POS replacement complete (POAM-001); CCPA cybersecurity audit gap assessment (POAM-022); service provider ROC | PCI 1.3, 4.2, 5.3, 6.3, 11.5; 11 CCR 7120-7124 | P2PE deployment records; gap assessment |
| 2027 Q3 | Annual risk analysis and gap reassessment; review PCI DSS version status | All | Updated P01 and P03 |

## 6. Pending regulatory changes
- **PCI DSS.** v4.0.1 remains current. The 2026 request for comments may lead to a new version; the analysis will be updated when one is published.
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect; the proposed size criterion would cover the company.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **CCPA cybersecurity audit:** first audit period 2027-01-01 to 2028-01-01, report due 2028-04-01.
- **FTC AI accuracy policy statement** (proposed, July 2026) is not final (P10).
- None of these is treated as a current obligation.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a QSA, an acquirer or card brand request, an FTC civil investigative demand, a state attorney general inquiry, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the 2025 merchant ROC and 2026 service provider ROC with AOCs, compensating control worksheets, and the franchisee responsibility matrix;
- the P01 risk analysis, P02 SSP, P05 BIA, P06 policy set and brand technology standards, P07 assessment and POA&M, and P08 runbook and notification matrix;
- franchisee AOC tracking reports and brand standard enforcement records;
- price display test results and feed audits for 16 CFR Part 464;
- document retention of at least 7 years for SOX-relevant records and the life of each contract plus 3 years for PCI DSS evidence.

## 8. Approval
Approved by the CISO and the General Counsel on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.

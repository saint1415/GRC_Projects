# Regulatory Gap Analysis: Cris Santos Company Holdings | Financial Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Financial Services (focus division: Payment Processing) |
| Primary standard | PCI DSS v4.0.1 (PCI SSC, June 2024), assessed for the Payment Processing division as a **service provider** |
| Division regulations | Payment Processing: FTC Safeguards Rule (16 CFR Part 314), bank service provider notice rules (12 CFR 53.4, 225.303, 304.24; C-FINANCIAL-R01), card brand rules. Payments Software Platform: SOC 2 commitments and FTC Act Section 5 (its vertical's primary pairing), PCI DSS for the gateway and hosted storefronts, CCPA and DOJ applicability checks. Merchant Consulting: FTC Safeguards Rule applicability (its vertical's primary rule) and contract flow-down as a service provider, PCI DSS for dispute services |
| Gap tables | `gap-analysis.csv` (Payment Processing, 109 rows); `gap-analysis-software.csv` (34 rows); `gap-analysis-consulting.csv` (24 rows) |
| Assessment dates | 2026-05-01 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-31) |
| Assessors | Division security and compliance leads with the Group Chief Compliance Officer's team, coordinated by the Group Chief Risk Officer; reviewed by group internal audit |

## 1. Applicability
Applicability was decided first, rule by rule and division by division, before any gap was rated. Federal text was read from the eCFR (point-in-time text for 2026-09-23) and the U.S. Code; card brand rules from Visa's public site.

### 1.1 Which GLBA safeguards rule applies
No group entity is a bank or is supervised by a federal banking agency, so the FTC Safeguards Rule is the GLBA safeguards rule for any group entity that is a "financial institution": the rule applies to financial institutions "not otherwise subject to the enforcement authority of another regulator" under GLBA section 505 (16 CFR 314.1(b)).

| Entity | Financial institution? | Basis (read from the primary text) | Result |
|---|---|---|---|
| Payment Processing (Cris Santos Payments, LLC) | **Yes** | Data processing and transmission of financial data is listed in 12 CFR 225.28(b)(14), which 314.1(b) incorporates through 12 U.S.C. 1843(k). Card processing is the whole business | Rule applies in full. The rule covers customer information of other institutions' customers that the division holds (314.1(b)): cardholders. The 314.6 exception does not apply |
| Payments Software Platform (Cris Santos Commerce Software, LLC) | **Treated as yes** (conservative) | Its gateway transmits payment transaction data for about 410,000 merchants and 1,900 ISVs (225.28(b)(14)); gateway fees are a material share of revenue | Covered by the group program; division gaps are in `gap-analysis-software.csv` |
| Merchant Consulting (Cris Santos Merchant Advisory, LLC) | **No** | Advisory, integration, PCI readiness, and dispute services are not listed financial activities, so the division is not "significantly engaged" in financial activities (314.2(h)(3)(iv)). Group legal recorded this on 2026-06-12 | Not a financial institution. It is a **service provider** (314.2(r)) to the Payment Processing division for dispute services, so the processor must oversee it and bind it by contract (314.4(f)) |

**The Qualified Individual is employed by an affiliate.** The Group CISO is employed by the holding company and serves as Qualified Individual for both financial-institution divisions. 314.4(a) allows this, but then each division must retain responsibility, designate a senior member of its own personnel to direct and oversee the Qualified Individual, and require the affiliate to maintain a compliant program (314.4(a)(1)-(3)). The division presidents do this in practice; it is not yet written down (G-083, Low).

### 1.2 PCI DSS: who is a service provider for what
| Division | PCI DSS role | Validation |
|---|---|---|
| Payment Processing | Service provider: stores, processes, and transmits cardholder data for merchants. Level 1 under Visa's service provider levels (more than 300,000 transactions a year; levels are set by the card brands) | Annual ROC by a QSA; AOC "Compliant" dated 2026-01-22; next ROC fieldwork 2026-11-02 to 2026-12-11. **Primary standard of this analysis** |
| Payments Software Platform | Service provider: the gateway transmits cardholder data to seven processors, and the division hosts the storefront pages that embed payment fields, a service that can affect the security of merchants' cardholder data | Separate ROC for the gateway (AOC 2026-03-31). Storefront page requirements (6.4.3, 11.6.1) are assessed in `gap-analysis-software.csv` |
| Merchant Consulting | Service provider for dispute services: it receives and handles account data in dispute evidence for about 2,100 merchants | For group merchants, the work happens inside the processor's CDE (SYS-P6) and ROC scope. For the 620 non-group clients there is no validation evidence today (MC-G10) |

Service-provider-only PCI DSS requirements are assessed as their own rows in `gap-analysis.csv`: 3.6.1.1, 8.3.10.1, 11.4.6, 11.5.1.1, 12.4.1, 12.4.2, 12.4.2.1, 12.5.2.1, 12.5.3, 12.9.1, and 12.9.2. 3.7.9, 8.2.3, 11.4.7, and Appendices A1 to A3 are Not applicable to the processor, with reasons in the CSV. PCI DSS has no size exemption; size affects only the validation level. PIN debit is covered by the PCI PIN Security Requirements, assessed separately and outside this analysis.

### 1.3 Bank service provider notice: three rules, four banks
Part 53 applies to national banks and "their bank service providers as defined in 53.2(b)(2)" (53.1(c)). A bank service provider performs covered services, which are services subject to the Bank Service Company Act (53.2(b)(5)). Each sponsor agreement states that clearing, settlement, reconciliation, and merchant funding file services are performed for the bank and are subject to examination under 12 U.S.C. 1867(c). The division is therefore a bank service provider to all four sponsor banks, under the rule of each bank's regulator:

| Sponsor bank | Supervisor | Rule | Designated contact on file? |
|---|---|---|---|
| Bank A (national bank) | OCC | 12 CFR 53.4 | Yes |
| Bank B (national bank) | OCC | 12 CFR 53.4 | **No** (fallback: CEO and CIO, 53.4(a)(2)) |
| Bank C (state member bank) | Federal Reserve | 12 CFR 225.303 (225.300(c); 225.301(b)(1)) | Yes |
| Bank D (state nonmember bank) | FDIC | 12 CFR 304.24 (304.21(c); 304.22(b)(1)) | **No** |

**What the rules require.** Notify at least one bank-designated point of contact as soon as possible after determining that a computer-security incident has materially disrupted or degraded, or is reasonably likely to, covered services to that bank for **four or more hours** (53.4(a)). Previously communicated maintenance, testing, or updates are excluded (53.4(b)). A card data theft that does not disrupt settlement or funding does not trigger the rule by itself; containment that halts covered services can (P08 scenario). The banks' own 36-hour notices to their regulators (53.3 and parallels) are the banks' duties, informed by the division's notice.

The Interagency Guidelines (C-FINANCIAL-R02) apply to the sponsor banks and reach the division only through the sponsor agreements' service provider terms (Guidelines III.D), tested in each bank's annual due diligence.

### 1.4 Considered and not applicable
| Requirement | Decision |
|---|---|
| NCUA 12 CFR 748.1(c) (C-FINANCIAL-R03) | No group entity is a credit union |
| SEC Regulation SCI (C-FINANCIAL-R04) | No group entity is an SCI entity |
| NYDFS 23 NYCRR Part 500 (C-FINANCIAL-R05) | Applies only to entities licensed, registered, or chartered under New York banking, insurance, or financial services law; no group entity holds a New York license, so the 500.19(a) exemption analysis is not reached |
| CIRCIA (C-FINANCIAL-R06; N54-R09) | Proposed rule only (89 FR 23644); no final rule as of 2026-09-25. Tracked in section 6 |
| COPPA, FedRAMP, FCC CPNI, PADFA (N51-R02, R07, R06, R05) | No child-directed services, federal agency customers, carrier operations, or data broker sales |
| IRC 7216, FAR, DFARS and CMMC, HIPAA, ABA and AICPA rules (N54-R02 to R08) | No tax preparation, federal contracts, PHI, legal services, or attestation work |

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Regulation-by-division matrix
| Requirement | Payment Processing | Payments Software Platform | Merchant Consulting | Group (corporate) |
|---|---|---|---|---|
| PCI DSS v4.0.1 | **Primary.** Level 1 service provider | Applies: gateway ROC; storefront pages (6.4.3, 11.6.1) | Applies to dispute services; inside the processor's scope for group merchants | Common controls in both ROCs |
| FTC Safeguards Rule (16 CFR 314) | Applies in full | Applies (conservative) | **Not a financial institution**; service provider to the processor (314.2(r); 314.4(f)) | Qualified Individual and group program |
| C-FINANCIAL-R01 bank service provider notice (53.4; 225.303; 304.24) | **Applies** to all four sponsor banks | Not applicable (no covered services) | Not applicable | Shared services can cause a covered-services disruption |
| C-FINANCIAL-R02 Interagency Guidelines | Through sponsor agreements (III.D) | Not applicable | Not applicable | Due diligence packages |
| Card brand rules (Visa WTDIC and others through the sponsor banks) | Applies | Applies to the gateway | Through the processor | SOC escalation |
| N51-R01 FTC Act Section 5 | Applies | **Primary** (with SOC 2) | Applies | Applies |
| SOC 1 / SOC 2 (contractual) | SOC 1 Type 2; first SOC 2 in preparation (P09) | **SOC 2 Type 2** (P09) | Out of scope (P09) | Group services carved in |
| N51-R03 CCPA and CPPA regulations | Cardholder data exempt at the data level (GLBA, 1798.145(e)) | Applicability under counsel review (SW-G24) | Client contact data; under the same review | Group privacy program |
| N51-R04 DOJ Data Security Program (28 CFR 202) | Applies (bulk financial data) | Applies | Applies | Vendor screening (GR-14) |
| N51-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| Colorado SB26-189 (effective 2027-01-01) | Fraud model: counsel reviewing whether a purchase decline is a consequential decision (P10) | Not applicable to the assistant (no consequential decisions) | Not applicable | Group AI Standard |
| State breach notification laws | Third-party agent of merchants for cardholder data; covered entity for merchant owner data. Each state where affected individuals reside (Fla. Stat. 501.171 worked example) | Third-party agent of merchants | Third-party agent of clients | Coordinates |

## 3. Method
1. **Requirements.**
   - PCI DSS was decomposed at the requirement level (1.1 to 12.10), with every service-provider-only sub-requirement as its own row, plus the appendices. PCI DSS is copyrighted, so rows give the requirement number and a short topic label in our own words. Read the full text in the PCI SSC document library.
   - The Safeguards Rule was decomposed to the paragraphs of 16 CFR 314.4 (with 314.4(a)(1)-(3) for the affiliate Qualified Individual) and 314.6; the bank service provider rules to their paragraphs; SOC 2 rows list criterion IDs with short labels in our own words.
2. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. These are **author mappings**: no official NIST mapping from PCI DSS v4.0.1, 16 CFR 314, or the bank notice rules to CSF 2.0 or SP 800-53 was used.
3. **Evidence.** Interviews with each division's leadership; the 2025 ROCs and AOCs; sponsor agreements and intercompany agreements; configuration exports from SYS-G1, SYS-M1, SYS-P6, and the SIEM; PAN discovery scans; the P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale; a High gap would likely produce a "not in place" ROC finding or leaves a High P01 risk untreated.

This is a gap analysis, not a PCI DSS assessment. Only the QSA's ROC can conclude on compliance.

## 4. Results
### 4.1 Payment Processing (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI DSS Req. 1 Network security controls | 5 | 0 | 0 | 0 | 5 |
| PCI DSS Req. 2 Secure configurations | 2 | 0 | 0 | 1 | 3 |
| PCI DSS Req. 3 Protect stored account data | 5 | 2 | 1 | 1 | 9 |
| PCI DSS Req. 4 Protect data in transmission | 2 | 0 | 0 | 0 | 2 |
| PCI DSS Req. 5 Anti-malware | 4 | 0 | 0 | 0 | 4 |
| PCI DSS Req. 6 Secure systems and software | 6 | 0 | 0 | 0 | 6 |
| PCI DSS Req. 7 Restrict access by need to know | 2 | 1 | 0 | 0 | 3 |
| PCI DSS Req. 8 Identify and authenticate | 4 | 3 | 0 | 2 | 9 |
| PCI DSS Req. 9 Physical access | 4 | 0 | 0 | 1 | 5 |
| PCI DSS Req. 10 Logging and monitoring | 6 | 1 | 0 | 1 | 8 |
| PCI DSS Req. 11 Security testing | 8 | 0 | 0 | 1 | 9 |
| PCI DSS Req. 12 Policies and programs | 9 | 6 | 0 | 0 | 15 |
| PCI DSS Appendices A1 to A3 | 0 | 0 | 0 | 3 | 3 |
| FTC Safeguards Rule 16 CFR 314.4 and 314.6 | 7 | 11 | 0 | 1 | 19 |
| Bank service provider notice (53.4, 225.303, 304.24) | 1 | 3 | 1 | 0 | 5 |
| Bank Service Company Act; Interagency Guidelines III.D | 2 | 0 | 0 | 0 | 2 |
| Card brand rule; sponsor agreement notice | 1 | 1 | 0 | 0 | 2 |
| **Total** | **68** | **28** | **2** | **11** | **109** |

Of the 30 gaps (Partially met or Not met), 6 are rated High, 19 Moderate, and 5 Low. PCI DSS accounts for 14 of them (13 Partially met, 1 Not met).

**What the pattern says:**
- **The processor's own core is in place.** Every row in requirements 1, 2, 4, 5, 6, 9, and 11 is Met or Not applicable, and so are the service-provider governance rows (12.4.1, 12.4.2, 12.4.2.1, 12.9). That is the difference between this division and a smaller processor.
- **Every High gap traces to the acquired consulting firm.** PAN in consulting mailboxes (3.5, Not met), the bulk export permission (7.2), account life cycle and MFA through SYS-M1 (8.2, 8.4, and the matching 314.4(c)(1) and (c)(5) rows). The 2025 acquisition was never reviewed for PCI DSS impact (12.5.3).
- **Notice rules lag the bank portfolio.** The procedure was written when the division had OCC-supervised sponsors only. Bank D's FDIC rule (304.24) is Not met; Bank C's Federal Reserve rule (225.303) and Bank B's contact are Partially met.

### 4.2 Payments Software Platform (`gap-analysis-software.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| SOC 2 commitments (CC and A1, C1 criteria) | 5 | 6 | 2 | 0 | 13 |
| FTC Act Section 5 (N51-R01) | 0 | 2 | 0 | 0 | 2 |
| PCI DSS (gateway and hosted storefronts) | 1 | 5 | 0 | 0 | 6 |
| FTC Safeguards Rule (group program; 314.4(f)) | 1 | 1 | 0 | 0 | 2 |
| CCPA and CPPA regulations; DOJ Data Security Program | 0 | 1 | 1 | 0 | 2 |
| PADFA, COPPA, FedRAMP, CPNI, Colorado SB26-189, bank notice rules | 0 | 0 | 0 | 6 | 6 |
| State breach laws; ISV agreement; SEC | 1 | 2 | 0 | 0 | 3 |
| **Total** | **8** | **17** | **3** | **6** | **34** |

**Not met:** CC2.3 (the merchant insights assistant and its model provider are not in the system description or merchant terms, High); A1.3 (gateway failover testing is more than 12 months old); and the CCPA applicability decision. **High:** storefront page scripts (CC6.6; PCI DSS 6.4.3 and 11.6.1) and the matching FTC unfairness exposure. The immediate issue is the SOC 2 report now being prepared: the period ended 2026-09-30, and the assistant operated for about four and a half months of it (P09).

### 4.3 Merchant Consulting (`gap-analysis-consulting.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| FTC Safeguards Rule: applicability and service provider contract | 0 | 0 | 1 | 1 | 2 |
| Safeguards elements flowed down by contract | 1 | 4 | 1 | 0 | 6 |
| PCI DSS (dispute services) | 1 | 2 | 3 | 0 | 6 |
| FTC Act Section 5; state breach laws; engagement letters | 0 | 3 | 0 | 0 | 3 |
| Group policy (supplement, inheritance) | 0 | 0 | 2 | 0 | 2 |
| Professional services rules not applicable (N54-R02 to R09) | 0 | 0 | 0 | 5 | 5 |
| **Total** | **2** | **9** | **7** | **6** | **24** |

**Not met:** no safeguards clause in the 2025 intercompany agreement (MC-G02); PAN in email (MC-G05, MC-G13); no PCI DSS acknowledgment or responsibility matrix for clients (MC-G10, MC-G11); supplement and inheritance (MC-G16, MC-G17). The division is a year into integration. Its technical gaps sit where the acquired firm's identity provider and email still run; its governance gaps are the documents the group never re-papered.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Consulting identity, MFA bypass, and account life cycle inside the CDE (1) | MC, PP | PCI DSS 8.2, 8.4, 8.5; 314.4(c)(1), (c)(5) | High | Remove the trusted-location rule now; block SMS for CDE access by 2026-12-31; SYS-G1 migration | Group identity director | 2027-03-31 |
| 2 | PAN in consulting mailboxes and dispute files (1) | MC, PP | PCI DSS 3.2, 3.4, 3.5; 314.4(c)(3), (c)(6) | High | Evidence upload portal; masking on upload; purge | Merchant Consulting dispute services director | 2027-01-31 |
| 3 | Bulk case export open to all dispute analysts (1) | PP | PCI DSS 7.2 | High | Supervisors only, with a ticket | Head of settlement operations | 2026-10-31 |
| 4 | Storefront scripts and marketplace apps (3) | SW | PCI DSS 6.4.3, 11.6.1; SOC 2 CC6.6; 15 U.S.C. 45 | High | Inventory and tamper-detection for every theme; app script review | Software division CISO | 2027-03-31 |
| 5 | AI assistant missing from SOC 2 description and terms (6) | SW | SOC 2 CC2.3, CC3.4, CC8.1, CC9.2 | High | Description update for the period ending 2026-09-30; merchant notice | Software division client trust and assurance director | 2026-11-30 |
| 6 | Bank service provider notice: contacts and determination procedure (4) | PP | 53.4(a)(1)-(2); 225.303; 304.24 | Moderate | Contacts for all four banks; procedure covers every incident origin | Head of bank and network relationships | 2026-10-31 |
| 7 | Scope and acquisition review (1, 5) | PP | PCI DSS 12.5, 12.5.2.1, 12.5.3 | Moderate | Reconfirm scope with email paths; documented 12.5.3 review | Payment Processing division CISO | 2026-10-31 |
| 8 | Affiliates not overseen as service providers (2) | PP, SW, MC | PCI DSS 12.8; 314.4(f); 314.4(a)(1)-(3) | Moderate | Intercompany responsibility matrix; safeguards clause; annual review | Group General Counsel | 2026-12-31 |
| 9 | Cross-division incident plan and matrix (7) | All | PCI DSS 12.10; 314.4(h); SOC 2 CC7.4 | Moderate | P08 runbook and matrix; tabletop 2026-12-15 | Group CISO | 2026-12-15 |
| 10 | Consulting supplement and inheritance (2) | MC | POL-01 4.5, 4.6 | Moderate | Re-issue supplement; inheritance matrix | Merchant Consulting security and compliance lead | 2026-12-31 |
| 11 | Gateway recovery testing (8) | SW | SOC 2 A1.3 | Moderate | Failover test | Software division chief technology officer | 2026-12-31 |
| 12 | Applicability decisions (CCPA audits and ADMT; Colorado for the fraud model) | SW, PP | N51-R03; Colorado SB26-189 | Low | Counsel opinions | Group Chief Privacy Officer | 2026-12-15 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-009, POAM-021 to POAM-023, and POAM-025 come from this analysis alone; most of the POA&M items from the P07 assessment cite rows of it as well.

**Before the ROC.** Roadmap items 1 (interim steps), 3, 6, and 7 must be done before QSA fieldwork starts on 2026-11-02. Item 2 cannot finish in time, so the division will bring SYS-M1 into its PCI DSS scope until the mailboxes are purged and agree the treatment with the QSA.

## 6. Pending regulatory changes
- **PCI DSS.** v4.0.1 is the current version in the PCI SSC document library. Every future-dated v4.0 requirement took effect on 2025-03-31 and is assessed here as current. No newer version is assumed.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226, 89 FR 23644, 2024-04-04). No final rule as of 2026-09-25. If finalized as proposed, covered entities would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours. The proposed rule's size criterion is tied to SBA size standards; a group of this size would likely be in scope, but the final criteria are not known. **Not a current obligation.**
- **CPPA regulations.** In effect since 2026-01-01. If the group meets the cybersecurity audit thresholds, the first audit report would be due 2028-04-01 (2026 revenue over $100 million); ADMT duties apply from 2027-01-01 for existing uses. Applicability is the open question (SW-G24).
- **Colorado SB26-189.** Effective 2027-01-01 for consequential decisions made on or after that date. Its application to fraud declines is under counsel review (P10).

The `pending_rule_change` column flags the rows these touch. None is treated as a current obligation beyond its effective date.

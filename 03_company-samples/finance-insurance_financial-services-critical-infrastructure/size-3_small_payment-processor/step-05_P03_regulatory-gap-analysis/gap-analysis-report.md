# Regulatory Gap Analysis: Cris Santos Company | Financial Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (payment processor serving merchants) |
| Tier / Vertical | Small / Financial Services |
| Primary standard | PCI DSS v4.0.1 (PCI SSC, June 2024), assessed as a **service provider** |
| Secondary regulations | FTC Safeguards Rule, 16 CFR Part 314; bank service provider notice, 12 CFR 53.4 (C-FINANCIAL-R01) |
| Assessment dates | 2026-07-13 to 2026-07-24 (R-031 evidence added 2026-08-07) |
| Assessor | IT Manager (Information Security Lead and Qualified Individual) with the Compliance and Risk Manager |
| Approved | COO, 2026-08-31 |

## 1. Applicability
Applicability was decided first, one rule at a time, before any gap was rated. Regulatory text comes from the eCFR and the U.S. Code; card brand rules come from Visa's public site. (Library note: every citation in this section was re-verified against those primary sources on 2026-09-26, using the eCFR point-in-time text for 2026-09-23.)

### 1.1 PCI DSS v4.0.1: applies, as a service provider (primary)
- **Why it applies.** PCI DSS is not a law. It binds the company by contract: the sponsor agreement and the card brands' rules require every entity that stores, processes, or transmits cardholder data for a brand member to comply. The company does all three for its merchants, so PCI DSS calls it a **service provider**. The QSA assessed it that way in 2025.
- **Why "service provider" matters.** PCI DSS has requirements that apply only to service providers. They are assessed here as their own rows: 3.6.1.1, 8.3.10.1, 11.4.6, 11.5.1.1, 12.4.1, 12.4.2, 12.4.2.1, 12.5.2.1, 12.5.3, 12.9.1, and 12.9.2. Other service-provider rows are Not applicable, for the reasons in the CSV: 3.7.9 (no keys shared with merchants), 8.2.3 (no remote access to merchant premises), 11.4.7 and Appendix A1 (not a multi-tenant hosting provider). 8.3.10 and 10.7.1 are superseded by 8.3.10.1 and 10.7.2.
- **Validation level: set by the card brands, not by PCI SSC.** PCI SSC writes the standard; each card brand decides who must validate and how. Under Visa's published service provider levels, a service provider that stores, processes, or transmits more than 300,000 Visa transactions a year is **Level 1**: an annual on-site assessment by a QSA and an AOC signed by the service provider and the QSA. At about 95 million transactions a year the company is Level 1. Other brands publish their own criteria; the sponsor bank confirms which ones apply.
- **Appendices.** A2 (SSL and early TLS for POS POI terminal connections) and A3 (Designated Entities Supplemental Validation) do not apply: early TLS has been disabled since 2023, and no brand or acquirer has designated the company.
- **Size.** PCI DSS has no small-business exemption. Size affects only the validation level.

### 1.2 FTC Safeguards Rule, 16 CFR Part 314: applies (secondary)
- **Financial institution.** The rule applies to "financial institutions" under FTC jurisdiction: businesses engaged in an activity that is financial in nature under 12 U.S.C. 1843(k), which incorporates the activities in 12 CFR 225.28 (16 CFR 314.1(b); 314.2(h)(1)). Data processing and transmission of financial, banking, or economic data is listed in 12 CFR 225.28(b)(14). Card processing is the company's whole business, so it is "significantly engaged" in that activity.
- **FTC jurisdiction.** The company is not a bank, a bank subsidiary, a broker-dealer, or an insurer, so no other federal functional regulator enforces GLBA safeguards against it. That leaves the FTC.
- **Customer information of other institutions.** Cardholders are customers of their issuing banks, not of the processor. The rule still covers their data: it "applies to all customer information in your possession ... [including information that] pertains to the customers of other financial institutions that have provided such information to you" (314.1(b)).
- **Merchant owner data.** Merchants obtain services for business purposes, so merchant owners are not "consumers" under 314.2(b). Their SSNs and bank details are protected by state law and company policy (POL-04), not by Part 314.
- **Small-institution exception does not apply.** 314.6 exempts institutions holding customer information on fewer than 5,000 consumers from 314.4(b)(1), (d)(2), (h), and (i). The token vault holds data on millions of cardholders.
- **FTC notice, 314.4(j) (in effect since 2024-05-13 under 314.5).**
  - **Trigger.** A "notification event" is the acquisition of unencrypted customer information without the individual's authorization. Information counts as unencrypted if the key was accessed. Unauthorized access is presumed to be acquisition unless there is reliable evidence it could not have been (314.2(m)).
  - **Threshold and deadline.** If the event involves the information of at least 500 consumers, notify the FTC through its online form as soon as possible and no later than 30 days after discovery.
  - **Discovery.** An event is discovered on the first day it is known to any employee, officer, or other agent other than the person committing the breach (314.4(j)(2)).
  - **Counting cardholders.** 314.2(b)(2)(v) says an individual is not "your" consumer solely because you process for their bank. However, 314.4(j)(1) counts "the information of at least 500 consumers," not "your consumers," and 314.1(b) brings other institutions' customers' information into scope. The company takes the **conservative reading**: affected cardholders count toward the 500. Counsel confirms the count for any real event (P08).

### 1.3 Bank service provider notice, 12 CFR 53.4 (C-FINANCIAL-R01): applies to the OCC-supervised sponsor bank
- **Scope.** Part 53 applies to national banks and "their bank service providers as defined in 53.2(b)(2)" (53.1(c)). A bank service provider is "a bank service company or other person that performs covered services." Covered services are "services performed, by a person, that are subject to the Bank Service Company Act (12 U.S.C. 1861-1867)" (53.2(b)(5)).
- **BSCA reasoning.** Under 12 U.S.C. 1867(c), when a regularly examined depository institution causes services authorized under the Act to be performed for itself by contract, the performance is subject to examination by its federal banking agency. The sponsor agreement states that the processor's settlement, reconciliation, and merchant funding file services are performed for the national bank and are subject to examination under 1867(c). The company therefore performs covered services and is a bank service provider to that bank.
- **What it requires.** Notify at least one bank-designated point of contact as soon as possible after determining that a computer-security incident has materially disrupted or degraded, or is reasonably likely to, covered services to the bank for **four or more hours** (53.4(a)). If the bank never provided a contact, notify its CEO and CIO or two people of comparable responsibility (53.4(a)(2)). Scheduled maintenance, testing, or updates already communicated are excluded (53.4(b)).
- **What it does not require.** The trigger is disruption of covered services. A card data theft that does not disrupt settlement or funding does not trigger 53.4 by itself. It does trigger the card brand, FTC, and state duties, and the sponsor agreement's own notice clause (P08).
- **Size.** None: no size threshold.

### 1.4 12 CFR 304.24 (FDIC) and 12 CFR 225.303 (Federal Reserve): do not apply today
These sections impose the same bank service provider notice. They apply only if the company performs covered services for an FDIC-supervised institution (304.21(c), 304.22(b)(1)) or a Board-supervised banking organization (225.300(c), 225.301(b)(1)). Today the only bank customer is the OCC-supervised national bank. The FDIC-supervised state nonmember bank has only a letter of intent; no services are performed for it. **304.24 will apply once the company performs covered services under a signed sponsor agreement (target 2027-Q1).** The Compliance and Risk Manager adds its designated contacts to the P08 matrix at signing. 225.303 would apply only if the company served a state member bank, a holding company, or another Board-supervised organization.

### 1.5 Considered and not applicable
| Requirement | Decision |
|---|---|
| Interagency Guidelines (C-FINANCIAL-R02), 12 CFR 30 App. B | Apply to the sponsor bank, not the processor. They reach the company only through the sponsor agreement's service provider oversight terms (Guidelines III.D), which the bank tests in its annual due diligence |
| NCUA 12 CFR 748.1(c) (C-FINANCIAL-R03) | Not a credit union and serves none |
| SEC Regulation SCI (C-FINANCIAL-R04) | Not an SCI entity |
| NYDFS 23 NYCRR Part 500 (C-FINANCIAL-R05) | Applies only to entities licensed, registered, or chartered under New York banking, insurance, or financial services law. The company holds no New York license, so the 500.19(a) exemption analysis is not reached |
| CIRCIA (C-FINANCIAL-R06) | Proposed rule only (89 FR 23644); no final rule as of 2026-09-25. Tracked in section 5, not applied |
| State breach laws | Apply after a breach, in each state where affected individuals reside. Florida (Fla. Stat. 501.171) is the worked example in P08. For cardholder data the company is usually a third-party agent of its merchants and must notify them within 10 days (501.171(6)) |

## 2. Method
1. **Requirements.**
   - PCI DSS was decomposed at the requirement level (1.1 to 12.10), with every service-provider-only sub-requirement as its own row, plus the appendices. PCI DSS is copyrighted, so rows give the requirement number and a short topic label in our own words. Read the full text in the PCI SSC document library.
   - The Safeguards Rule was decomposed to the paragraph level of 16 CFR 314.4, and 12 CFR 53.4 to its paragraphs.
2. **Crosswalk.** Each row is mapped to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. These are **author mappings**: no official NIST mapping from PCI DSS v4.0.1 or 16 CFR 314 to CSF 2.0 or SP 800-53 was used.
3. **Evidence.**
   - Interviews: COO, CTO, IT Manager, Platform Engineering Lead, Compliance and Risk Manager, Settlement Operations Manager, Merchant Support Manager, HR Manager.
   - Documents: policies, the 2025 ROC and AOC, the sponsor agreement, and service provider contracts.
   - Technical: configuration exports from the cloud tenant, identity provider, SIEM, and pipeline, and a browser capture of the hosted payment page (2026-07-22).
4. **Status.** Each row is rated Met, Partially met, Not met, or Not applicable.
5. **Gap risk.** Each gap is rated with the P01 risk scale. High gaps are the ones that would likely produce a "not in place" finding at the 2026 ROC, or that leave a High risk in P01 untreated.

This is a gap analysis, not a PCI DSS assessment. Only the QSA's ROC can conclude on compliance.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI DSS Req. 1 Network security controls | 3 | 2 | 0 | 0 | 5 |
| PCI DSS Req. 2 Secure configurations | 0 | 2 | 0 | 1 | 3 |
| PCI DSS Req. 3 Protect stored account data | 2 | 6 | 0 | 1 | 9 |
| PCI DSS Req. 4 Protect data in transmission | 1 | 1 | 0 | 0 | 2 |
| PCI DSS Req. 5 Anti-malware | 3 | 1 | 0 | 0 | 4 |
| PCI DSS Req. 6 Secure systems and software | 1 | 4 | 1 | 0 | 6 |
| PCI DSS Req. 7 Restrict access by need to know | 2 | 1 | 0 | 0 | 3 |
| PCI DSS Req. 8 Identify and authenticate | 3 | 3 | 1 | 2 | 9 |
| PCI DSS Req. 9 Physical access | 4 | 0 | 0 | 1 | 5 |
| PCI DSS Req. 10 Logging and monitoring | 4 | 2 | 1 | 1 | 8 |
| PCI DSS Req. 11 Security testing | 0 | 4 | 3 | 2 | 9 |
| PCI DSS Req. 12 Policies and programs | 2 | 8 | 5 | 0 | 15 |
| PCI DSS Appendices A1 to A3 | 0 | 0 | 0 | 3 | 3 |
| FTC Safeguards Rule 16 CFR 314.4 | 1 | 14 | 2 | 0 | 17 |
| 12 CFR 53.4 and parallels | 0 | 0 | 2 | 1 | 3 |
| **Total** | **26** | **48** | **15** | **12** | **101** |

Of the 63 gaps (Partially met or Not met), 15 are rated High, 34 Moderate, and 14 Low. PCI DSS accounts for 45 of them: 34 Partially met and 11 Not met.

**What the pattern says:**
- **The technical base is sound.** Network restriction, encryption of stored PAN, transmission security, anti-malware, and physical controls (inherited from the cloud provider) are largely Met.
- **The gaps come from change, not neglect.** The March 2026 migration and April 2026 reorganization were not followed by the scope reconfirmation, segmentation test, penetration test, and responsibility reviews that PCI DSS requires of service providers.
- **Requirement 12 carries the most Not met rows.** Five of the 15 Not met rows are service-provider governance items: executive responsibility (12.4.1), quarterly reviews (12.4.2), six-month scope confirmation (12.5.2.1), organizational change review (12.5.3), and the incident response plan (12.10).

## 4. Priority gaps and roadmap
All 15 High gaps must be closed before the QSA's fieldwork starts on 2026-11-02, except where noted.

| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Scope and data flows not reconfirmed after migration | PCI 12.5, 12.5.2.1 (G-070, G-071) | High | New scope document and data-flow diagrams; six-month confirmation calendar | IT Manager | 2026-09-30 |
| Incident response plan outdated; missing required areas and notice steps | PCI 12.10 (G-078); 314.4(h) (G-096) | High | POL-03 and P08 runbook; 24/7 on-call; tabletop; 12.10.7 procedure | IT Manager | 2026-09-30 (plan); 2026-10-31 (tabletop) |
| Payment page scripts unmanaged; no tamper-detection | PCI 6.4.3, 11.6.1 (G-028, G-063) | High | Remove unneeded scripts; inventory with justification; integrity checks; change- and tamper-detection service | CTO | 2026-10-15 |
| Segmentation not tested every six months or after migration | PCI 11.4.6 (G-059) | High | Segmentation test now, then every six months | IT Manager | 2026-10-15 |
| No penetration test of the new environment | PCI 11.4 (G-058) | High | External and internal test of the cloud CDE | IT Manager | 2026-10-15 |
| Merchant users sign in with passwords only | PCI 8.3.10.1 (G-038); 314.4(c)(5) (G-088) | High | Required MFA for refund, funding account, and virtual terminal roles; risk-based sign-in analysis for all others, approved in writing by the Qualified Individual | CTO | 2026-10-31 |
| Termination misses tokens and local accounts | PCI 8.2 (G-034) | High | Token and local account checklist; 90-day inactivity disable | HR Manager | 2026-10-31 |
| No covert channel detection on egress | PCI 11.5.1.1 (G-062) | High | DNS query logging and tunneling detection; network intrusion detection | Platform Engineering Lead | 2026-10-31 |
| Clear-text PAN in tickets and (until 2026-08-07) the warehouse | PCI 3.5 (G-013) | High | Masking in ticketing and email; purge history; block PAN in warehouse loads | Merchant Support Manager | 2026-10-31 |
| Alerts reviewed in business hours only | PCI 10.4 (G-050); 314.4(c)(8) (G-091) | High | Interim on-call daily review including weekends from 2026-10-15, so 10.4.1 is in place for the ROC; 24x7 managed detection service by 2026-11-30 | IT Manager | 2026-11-30 |

**Moderate gaps due before the ROC (selected):**
- executive charter and quarterly reviews (12.4.1, 12.4.2)
- organizational change review (12.5.3)
- critical control failure alerts (10.7)
- service provider AOCs and responsibility matrices (12.8)
- merchant responsibility matrix (12.9.2)
- targeted risk analyses (12.3)
- key-management procedures (3.6, 3.6.1.1, 3.7)
- 12 CFR 53.4 determination step and sponsor bank contacts (G-099, G-100)
- FTC notice step (G-098)

**After the ROC:** the first written Qualified Individual report to the CEO and COO (314.4(i), 2026-12-15) and the retention schedule for onboarding files and tickets (314.4(c)(6), 2026-12-31).

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
- **PCI DSS.** v4.0.1 is the current version in the PCI SSC document library (library note: re-checked 2026-09-26). Every future-dated v4.0 requirement took effect on 2025-03-31 and is assessed here as a current requirement. No newer version is assumed.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226, 89 FR 23644, 2024-04-04). No final rule had been published as of 2026-09-25, and CISA held further town halls in 2026. If finalized as proposed, covered entities would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours. Whether a processor of this size would be covered depends on the final size and sector criteria. **Not a current obligation.**
- **FDIC 12 CFR 304.24.** Not a rule change, but a scheduled applicability change: it applies once the second sponsor agreement is signed (section 1.4).

The `pending_rule_change` column in `gap-analysis.csv` is "None" for every row, because no proposed rule changes a requirement assessed here.

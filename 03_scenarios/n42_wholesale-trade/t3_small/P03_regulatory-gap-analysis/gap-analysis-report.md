# Regulatory Gap Analysis: Cris Santos Company | Wholesale Trade | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software wholesale distributor) |
| Tier / Vertical | Small / Wholesale Trade |
| Primary regulation | NIST SP 800-171 Rev. 2 (110 requirements), required by DFARS 252.204-7012(b)(2) and assessed under CMMC Level 2 (32 CFR 170.14(c)(3)), scoped to the CUI order stream |
| Secondary | FAR 52.204-21 (15 requirements, CMMC Level 1) for the FCI order stream; supply chain clause check: FAR 52.204-25 (Section 889), DFARS 252.246-7008, and DFARS 252.204-7012, -7019/-7020, and -7021 clause duties |
| Assessment dates | 2026-07-13 to 2026-07-24 (row G-126 updated 2026-08-07 with a P07 finding) |
| Assessor | IT Manager with the Government Contracts Manager and Purchasing and Supplier Manager |
| Workbook | `gap-analysis.csv` (137 rows) |

## 1. Applicability
**DFARS 252.204-7012 and NIST SP 800-171 Rev. 2 apply.** The Prime B subcontract (awarded 2024-06) contains DFARS 252.204-7012, and performance involves covered defense information: CUI-marked network drawings, IP addressing plans, and device configuration templates for DoD installations. Paragraph (m) of the clause requires the prime to flow it down in these cases, and paragraph (b)(2) requires the company to implement SP 800-171 on every covered contractor information system. There is no size exemption.

**CMMC Level 2 (C3PAO) will apply from 2027-04-01.** CMMC applies to subcontractors at all tiers that process, store, or transmit FCI or CUI (32 CFR 170.23(a)). Prime B has notified the company that its option period starting 2027-04-01 requires a CMMC Status of Level 2 (C3PAO), the minimum for a subcontractor handling CUI when the prime contract requires Level 2 (C3PAO) (170.23(a)(3)). Phase 2, when DoD begins to require Level 2 (C3PAO), starts 2026-11-10 (170.3(e)(2)).

**FAR 52.204-21 and CMMC Level 1 (Self) apply to the FCI stream.** Prime A and Prime C purchase orders for custom kitting and asset labeling include FAR 52.204-21 and, since 2026-01, DFARS 252.204-7021 at Level 1 (Self). Orders exclusively for commercially available off-the-shelf items carry neither: 52.204-21 excludes COTS subcontracts and CMMC excludes procurements exclusively for COTS items (32 CFR 170.3(c)). The kitting and labeling work makes these orders more than COTS.

**Supply chain clauses apply as contract terms.** FAR 52.204-25 is in all three DoD subcontracts. DFARS 252.246-7008 is in the Prime B subcontract, and its paragraph (e) requires the company to flow its substance to its own suppliers of electronic parts and assemblies containing them, including commercial products, unless the supplier is the original manufacturer.

**Not applicable, with reasons:**
- SP 800-171 3.13.5 (subnetworks for publicly accessible components): no publicly accessible components are inside the boundary; the website and portal are vendor-hosted (G-092).
- FAR 52.204-21(b)(1)(xi): the same reason (G-121).
- SEC disclosure rules (private company), CCPA/CPRA (no California business), and CTPAT (voluntary; not an importer of record). See `../scenario-facts.md` section 1.

## 2. Method
1. **Requirements.** The 110 requirements, their Basic or Derived type, and their text were taken from NIST's SP 800-171 Rev. 2 requirements dataset. CMMC practice IDs follow 32 CFR 170.14(c). Point values follow the CMMC Scoring Methodology (32 CFR 170.24). The 15 FAR 52.204-21 requirements are quoted from the clause (48 CFR 52.204-21(b)(1)) and linked to their SP 800-171 equivalents per Table 2 to 32 CFR 170.15(c)(1)(ii). Clause rows cite the eCFR text of each clause (current as of 2026-09-23).
2. **Crosswalk.** SP 800-53 controls come from the official SP 800-171 Rev. 2 Appendix D mapping (which uses Rev. 4 control IDs), refined to Rev. 5 by the author (column `nist_official_sp800_53_appendix_d` keeps the official list). CSF 2.0 subcategories are derived from the official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference. Clause rows use an author mapping and are labeled as such.
3. **Evidence.** Interviews (Chief Operating Officer, IT Manager, Systems Administrator, Government Contracts Manager, Purchasing and Supplier Manager, Configuration Lab Lead, Controller, HR Manager, MSP lead technician), document review, configuration exports, an ERP attachment search on 2026-07-17, and an item master extract on 2026-07-17.
4. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable. For CMMC scoring, Partially met counts as NOT MET (170.24), except the partial credit rules for 3.5.3 and 3.13.11.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 3.1 Access Control | 6 | 13 | 3 | 0 | 22 |
| 3.2 Awareness and Training | 0 | 1 | 2 | 0 | 3 |
| 3.3 Audit and Accountability | 3 | 3 | 3 | 0 | 9 |
| 3.4 Configuration Management | 1 | 5 | 3 | 0 | 9 |
| 3.5 Identification and Authentication | 9 | 1 | 1 | 0 | 11 |
| 3.6 Incident Response | 0 | 0 | 3 | 0 | 3 |
| 3.7 Maintenance | 1 | 4 | 1 | 0 | 6 |
| 3.8 Media Protection | 3 | 4 | 2 | 0 | 9 |
| 3.9 Personnel Security | 1 | 1 | 0 | 0 | 2 |
| 3.10 Physical Protection | 2 | 4 | 0 | 0 | 6 |
| 3.11 Risk Assessment | 1 | 0 | 2 | 0 | 3 |
| 3.12 Security Assessment | 3 | 0 | 1 | 0 | 4 |
| 3.13 System and Communications Protection | 8 | 5 | 2 | 1 | 16 |
| 3.14 System and Information Integrity | 3 | 2 | 2 | 0 | 7 |
| **SP 800-171 Rev. 2 subtotal** | **41** | **43** | **25** | **1** | **110** |
| FAR 52.204-21 (CMMC Level 1) | 8 | 6 | 0 | 1 | 15 |
| FAR 52.204-25 (Section 889) | 0 | 1 | 2 | 0 | 3 |
| DFARS 252.246-7008 (sources of electronic parts) | 0 | 2 | 2 | 0 | 4 |
| DFARS 252.204-7012 clause duties (cloud, reporting, preservation) | 0 | 0 | 3 | 0 | 3 |
| DFARS 252.204-7019/-7020 (SPRS) | 0 | 1 | 0 | 0 | 1 |
| DFARS 252.204-7021 (CMMC status) | 0 | 0 | 1 | 0 | 1 |
| **Total (137)** | **49** | **53** | **33** | **2** | **137** |

**SP 800-171 detail.** Of the 68 unmet or partially met requirements, 17 are Basic and 51 are Derived. By gap risk level, 23 are High, 23 Moderate, and 22 Low.

**Score.** Using the CMMC Scoring Methodology (32 CFR 170.24), the 2026 score is **-84 out of 110**. The 2024 SPRS entry of 96 is not supported (G-136).

**What the score means for CMMC.** A Conditional Level 2 status with a POA&M requires a score of at least 88 (0.8 of 110) and allows only 1-point requirements on the POA&M, plus 3.13.11 when encryption is used but not FIPS-validated (32 CFR 170.21(a)(2)). Six requirements can never be on a POA&M (170.21(a)(2)(iii)). Of the 68 unmet requirements:
- **39 cannot be placed on a CMMC POA&M** (point value above 1, or listed in 170.21(a)(2)(iii): 3.1.20, 3.10.3, 3.10.4, 3.10.5). They must be fully met before the 2027-02 assessment.
- **28 are 1-point requirements** that could go on a POA&M, closed within 180 days of the Conditional status date (170.17(c)(3)).
- **1 (3.13.11)** could go on a POA&M if encryption is in place but FIPS validation is not confirmed.

**FAR 52.204-21.** 6 of 15 requirements are only partially met, mainly because of shared WMS accounts on the handhelds (G-111, G-115, G-116). CMMC Level 1 allows no POA&M (170.21(a)(1)), so the January 2026 Level 1 affirmation is not supported (G-137).

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| CUI in the ERP SaaS without FedRAMP Moderate equivalency | 252.204-7012(b)(2)(ii)(D) (G-133) | High | Purge 14 attachments; block attachments on DoD orders | IT Manager | 2026-09-30 |
| Unsupported SPRS score and Level 1 affirmation | 252.204-7019/-7020; 32 CFR 170.15, 170.22 (G-136, G-137) | High | On counsel's advice, post a corrected Basic Assessment and correct the Level 1 entry | Chief Executive Officer | 2026-09-30 and 2026-10-31 |
| Cannot report cyber incidents or covered equipment | 252.204-7012(c); 52.204-25(d); 3.6.2 (G-056, G-127, G-134) | High | Obtain a DoD-approved medium assurance certificate; reporting procedure in P08 | Government Contracts Manager | 2026-10-15 |
| No Section 889 screening; white-label covered video SKUs found | 52.204-25(b)(1) (G-126) | High | Mandatory manufacturer of record; screening list with hard block on federal orders; broker attestations | Government Contracts Manager | 2026-11-30 |
| Sourcing order not documented; brokers unassessed; no notice or authentication procedure | 252.246-7008(b) (G-129, G-130) | High | C-SCRM plan with written sourcing order and broker approval; authorized sources only for DoD jobs now | Purchasing and Supplier Manager | 2026-11-30 |
| CUI share open to all 62 users; CUI flows uncontrolled; no CUI architecture | 3.1.1, 3.1.2, 3.1.3, 3.13.2 | High | CUI enclave project (CUI share for 9 users, lab VLAN, hardened lab workstations) | IT Manager | 2026-12-15 |
| No MFA for network access to the CUI share | 3.5.3 | High | MFA for the CUI share and lab workstation sign-in | Systems Administrator | 2027-01-15 |
| No incident response capability | 3.6.1 | High | POL-03 and P08 runbook (approved 2026-08-31); tabletop | IT Manager | 2026-11-30 |
| No log correlation, monitoring, or scanning | 3.3.5, 3.14.6, 3.11.2 | High | Managed detection and response; monthly authenticated scans | IT Manager | 2027-01-15 |
| No role-based training (CUI, anti-counterfeit) | 3.2.2 | High | Role-based modules for lab, receiving, buyers, administrators | HR Manager | 2026-12-15 |
| No removable media control | 3.8.7, 3.1.21 | High | Block USB storage except issued encrypted drives | Systems Administrator | 2026-12-15 |
| Visitors unescorted at the dock; logs and keys | 3.10.3, 3.10.4, 3.10.5 (no POA&M allowed) | Moderate | Driver waiting area and escort rule; 1-year badge logs; rekey the cage | Warehouse and Logistics Manager | 2026-10-31 |
| External system use not limited | 3.1.20 (no POA&M allowed) | Moderate | Block personal cloud storage; POL-05 rule | IT Manager | 2026-11-30 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

**Sequence.** The 39 requirements that cannot go on a CMMC POA&M, and the clause gaps that carry legal exposure (G-133, G-136, G-137), come first. The 1-point requirements follow. The target is a self-assessed score of at least 88, with only POA&M-eligible items open, by 2027-01-31, ahead of a C3PAO assessment in 2027-02.

## 5. Pending regulatory changes
These are **proposed** and are not treated as current obligations. The `pending_rule_change` column flags the 7 rows affected by the first item.

- **FAR overhaul, parts 1, 2, 4, 33, 39, 40, 52, and 53** (FR Doc. 2026-12559, 91 FR 37550, 2026-06-23; comments closed 2026-07-23). If finalized as proposed:
  - A new FAR 52.240-7 clause for CUI would require **NIST SP 800-171 Rev. 3** with DoD organization-defined parameters. Rev. 3 adds a Supply Chain Risk Management family (03.17), which the C-SCRM plan should anticipate (rows G-081 and G-129).
  - CUI incidents would be reported within **72 hours of discovery** across agencies, not only DoD (G-056, G-134).
  - A new FAR 52.240-3 would consolidate the security prohibitions, including Section 889, and standardize reporting to **72 hours from discovery** with one required report, replacing today's 1-business-day and 10-business-day reports (G-126 to G-128).
- **FAR prohibition on certain semiconductor products and services** (proposed rule, 91 FR 7223, 2026-02-17; comments closed 2026-04-20). It would partially implement a FY2023 NDAA section that bars executive agencies from procuring products that include covered semiconductor products or services, effective 2027-12-23. For a hardware distributor this would add a second screening list alongside Section 889. Not tied to a row yet; the C-SCRM plan (SR-2) will track it.
- **DFARS printed circuit board acquisition restrictions** (advance notice of proposed rulemaking, DFARS Case 2022-D011, 91 FR 40508, 2026-07-02). DoD is gathering information on the prohibition of covered printed circuit boards from a covered nation. No proposed rule text exists yet.
- A Federal Register search on 2026-09-25 found no proposed rule that would change DFARS 252.204-7012 itself or 32 CFR 170. CMMC Phase 2 (2026-11-10) is already scheduled in 32 CFR 170.3(e) and is treated as current.

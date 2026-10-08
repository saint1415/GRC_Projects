# Regulatory Gap Analysis: Cris Santos Company Holdings | Public Administration | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Public Administration (focus division: GovTech Integration) |
| Primary requirement set (focus division) | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline, as selected in NIST SP 800-53B, required by the agency contracts for the ACMP, with the CJISSECPOL v6.1 and IRS Pub. 1075 (Rev. 11-2021) overlays |
| Division requirement sets | IT Consulting: DFARS 252.204-7012, NIST SP 800-171 Rev. 2 and CMMC (32 CFR Part 170), FAR 52.204-21, HIPAA business associate duties. Government Software Products: CJISSECPOL v6.1 for the RMS, FedRAMP, GovRAMP, SOC 2 commitments, FTC Act Section 5 |
| Gap tables | `gap-analysis.csv` (GovTech Integration, 231 rows, including 5 group-wide rows); `gap-analysis-it-consulting.csv` (29 rows); `gap-analysis-govsoftware.csv` (26 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28); statuses as of approval on 2026-09-15 |
| Assessors | Division security and compliance leads, coordinated by the group public sector compliance director; reviewed by group internal audit |

## 1. Applicability
The group is a private contractor, not a government entity. Apart from the Driver's Privacy Protection Act, state data security and breach laws, FTC Act Section 5, and SEC rules, the rules below reach it **through contracts with agencies that are bound by them**, so this analysis starts with the contracts.

### 1.1 GovTech Integration: SP 800-53 Moderate with CJIS and Pub. 1075 overlays
- **SP 800-53 Moderate by contract.** NIST SP 800-53 is a federal standard, not a law for private companies. Almost every agency contract requires the hosted system to meet the Moderate baseline: **177 base controls and 110 enhancements**. Each `G-` row is one base control, with its Moderate enhancements assessed inside the row and named in the `citation` column. CJISSECPOL v6.1 and Pub. 1075 use the same control structure, so one row serves all three sources.
- **CJIS Security Policy through the Security Addendum.** 28 CFR 20.33(a)(7) lets criminal history record information go to private contractors under an agreement with a criminal justice agency that incorporates the Security Addendum. The Addendum requires a security program consistent with the CJIS Security Policy in effect when the contract is executed "and all subsequent versions" (sec. 3.01), and each employee signs the certification page (sec. 2.01). Version checked: **CJISSECPOL v6.1, dated 06/25/2026**. Since 2024-10-01 audits sanction existing and [Priority 1] requirements; [Priority 2] to [Priority 4] requirements are in a zero-cycle that ends **2027-09-30** (section 1.4). The CG-CJ contracts require the whole policy now, so every CJIS row is rated today. Eleven state CSAs audit through the agencies.
- **Pub. 1075 through Exhibit 7.** Under 26 CFR 301.6103(n)-1(a), a state tax agency may disclose returns and return information to a contractor to the extent necessary under a written contract. Pub. 1075 requires the Exhibit 7 contract language and an IRS notification at least 45 days before a contractor or cloud provider receives FTI (sec. 2.E.6; Exhibit 6). Edition checked: Rev. 11-2021, the edition at irs.gov.
- **Why the IEP holds no FTI.** Human services agencies that receive FTI under IRC 6103(l)(7) "may not contract for services that involve the disclosure of FTI to contractors or sub-contractors" (sec. 2.C.11.2). PB-17 tests that the rule holds in practice.
- **HIPAA, as a business associate of 2 Medicaid agencies.** The two agencies' health care components include the eligibility functions on the IEP (45 CFR 164.105), so GovTech signed business associate agreements and is directly subject to the Security Rule for that work (rows HI-01 to HI-04). Corporate shared services operate the IEP's identity, SOC, cloud, and backups, which makes corporate a subcontractor that needs written assurances (164.308(b)(2); 164.314(a)(2)(iii)).
- **Medicaid and SNAP confidentiality by contract** (42 CFR 431.300-431.307; 7 CFR 272.1(c); rows MD-01 to MD-04), and the program rules that keep eligibility decisions with state merit staff (7 CFR 272.4(a)(2); 42 CFR 431.10(b)(3); rows AI-01 to AI-03).
- **Driver's Privacy Protection Act, directly.** 18 U.S.C. 2721(a) says a state motor vehicle department "and any officer, employee, or contractor thereof" shall not knowingly disclose personal information except as 2721(b) permits. The group is that contractor for 3 states (rows DP-01 to DP-03).
- **State law (Florida worked example).** Fla. Stat. 501.171(2) and (6)(a) apply directly to the group as a third-party agent. Fla. Stat. 282.318, 282.3185, and 282.3186 are agency duties the group must support. Rule 60GG-2, F.A.C. reaches the group only through state agency contract terms (Fla. Stat. 282.318(4)(h)), and the SP 800-53 Moderate rows cover it, so it has no separate rows. Other states are handled the same way, "each state where affected individuals reside."

### 1.2 IT Consulting
- **DFARS 252.204-7012** is in 58 DoD contracts and subcontracts: adequate security under NIST SP 800-171, 72-hour incident reporting with a medium assurance certificate, 90-day media preservation, and flowdown.
- **CMMC.** The DFARS CMMC acquisition rule took effect 2025-11-10 (Phase 1). **Phase 2 was to begin 2026-11-10** and add Level 2 (C3PAO) for applicable solicitations (32 CFR 170.3(e)(2)). The DoD (Department of War) CIO memorandum of 2026-07-13 suspends CMMC Phase 2. Until 2028-11-09, DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self). SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). 32 CFR 170.14(c)(3) fixes SP 800-171 **Rev. 2** for Level 2. CMMC does not apply to federal information systems operated on behalf of the Government (170.3(b)), which scopes out the agency-owned systems the division operates under managed services task orders.
- **FAR 52.204-21** applies to about 140 federal civilian contracts with federal contract information.
- **HIPAA business associate** duties apply to 19 engagements with public hospitals and county health departments.
- **The 800-171 rows** list the requirements where the enclave or the acquired estate differ from group controls. The division's full 110-requirement self-assessment is kept with the enclave SSP and is not reproduced here.

### 1.3 Government Software Products
- **CJISSECPOL v6.1** applies to the RMS through the Security Addendum in each RMS agency agreement.
- **FedRAMP** (44 U.S.C. 3607-3616) applies to the Grants Management federal edition, which holds an agency authorization at Moderate. The Civic Suite and RMS are not offered to federal agencies.
- **GovRAMP** is a program, not law, but agency contracts in several states require the Civic Suite's verification.
- **SOC 2 commitments** made in contracts and system descriptions, and **FTC Act Section 5** for security claims.

### 1.4 Excluded or tracked only
| Requirement | Decision | Why |
|---|---|---|
| CIRCIA (N92-R07, N54-R09) | Tracked only | Proposed rule (89 FR 23644). No final rule as of 2026-09-25 |
| SLCGP (N92-R06) | Not applicable | Grant condition on agencies; no SLCGP funds pay for group systems. FY2026+ funding status not verified |
| HIPAA for the ACMP | Not applicable | No ACMP customer has designated the group a business associate |
| FTC Safeguards Rule, IRC 7216, professional conduct rules (N54-R01, R02, R03, R07, R08) | Not applicable | IT Consulting is not a financial institution or tax preparer and gives no legal or attest services |
| COPPA, FCC CPNI, PADFA (N51-R02, R05, R06) | Not applicable | No child-directed service, no telecommunications service, no data brokerage |
| Colorado SB26-189 | Watch item | No IEP or RMS customer in Colorado today; effective 2027-01-01; status unsettled |
| Election systems (EAC VVSG) | Not applicable | The group builds no voting or voter registration systems |

## 2. Regulation-by-division matrix
| Requirement | GovTech Integration | IT Consulting | Government Software Products | Group (corporate) |
|---|---|---|---|---|
| SP 800-53 Moderate (by contract) | **Primary** (ACMP, IEP, MVSP) | Applies to agency-hosted work under task orders (agency rules) | Basis of the FedRAMP and GovRAMP packages | Provides common controls (P02 catalog) |
| N92-R02 CJIS Security Policy v6.1 | Applies (ACMP CJI cluster; 212 agencies, 11 CSAs) | Applies only where consultants work in agency CJI systems (agency-issued accounts) | **Applies** (RMS; about 620 agencies) | Applies to corporate staff with CJI-environment access |
| N92-R01 IRS Pub. 1075 | Applies (7 FTI tenants); FTI prohibited on the IEP | Not applicable (no FTI engagements) | Not applicable | Applies to corporate staff and the provider B vault |
| N92-R03 HIPAA Security Rule | Applies to the IEP (business associate of 2 Medicaid agencies) | Applies (19 business associate engagements, N54-R06) | Not applicable | Subcontractor to GovTech for the IEP (terms missing) |
| N92-R04 Medicaid safeguards; SNAP confidentiality | Applies (IEP, by contract) | Not applicable | Not applicable | Supports GovTech |
| N92-R05 Driver's Privacy Protection Act | **Applies directly** (MVSP, 3 states) | Not applicable | Not applicable | Not applicable |
| N92-R06 SLCGP | Not applicable | Not applicable | Not applicable | Not applicable |
| N92-R07 CIRCIA (proposed) | Tracked only | Tracked only | Tracked only | Tracked only |
| N92-R08 GovRAMP | Requested for the ACMP (P09) | Not applicable | Applies to the Civic Suite (contractual) | Not applicable |
| N54-R04 FAR 52.204-21 | Not applicable (no federal contracts) | **Applies** (about 140 contracts) | Applies to the Grants Management contract terms | Common controls cover the 15 requirements |
| N54-R05 DFARS 252.204-7012; SP 800-171 Rev. 2; CMMC | Not applicable | **Applies** (58 DoD contracts; CMMC Phase 2 suspended) | Not applicable | Common controls inherited by the enclave (undocumented) |
| N51-R07 FedRAMP | Not applicable | Not applicable | **Applies** (Grants Management federal edition) | Not applicable |
| N51-R01 FTC Act Section 5 | Applies (general) | Applies (general) | **Applies** (product security claims) | Applies |
| N51-R04 DOJ Data Security Program, 28 CFR Part 202 | Applies (bulk sensitive data) | Applies | Applies | Group procurement screening |
| N51-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach and data security laws | Third-party agent duties to agencies (Florida: Fla. Stat. 501.171(6)(a)) | Same, for client data | Same, for customer data | The group's own data; coordination |
| State agency incident laws (Florida: Fla. Stat. 282.318, 282.3185, 282.3186) | Support agency 12-hour reports; no ransom payment by agencies | Support agency clients | Support RMS and Civic Suite agencies | Coordination (P08) |
| SOC 2 (contractual) | ACMP Type 2 (P09) | Out of scope (P09) | Civic Suite and RMS Type 2 (P09) | Common controls carved in |

## 3. Method
1. **Requirements.** SP 800-53 rows come from the repository copy of the Release 5.2.0 catalog and its baseline flags. CJIS and Pub. 1075 overlay rows were added only where those documents set a value or duty beyond the base control text; both are U.S. government works and are quoted or summarized. SP 800-171 Rev. 2 rows use the requirement text and CMMC identifiers already verified in the repository's Defense Industrial Base multi-sector sample. DFARS, FAR, 32 CFR Part 170, 42 CFR 431, 7 CFR 272, 45 CFR 164, and 18 U.S.C. 2721-2724 were read from eCFR (2026-09-23) or govinfo.gov. SOC 2 rows name criterion IDs with short labels in our own words.
2. **Crosswalk.** CSF 2.0 subcategories for `G-` rows come from NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). SP 800-171 rows are derived from NIST's official mappings through their Rev. 3 counterparts. All other rows carry an **author mapping**, labeled in the `crosswalk_source` column.
3. **Evidence.** Interviews in each division; configuration exports; screening registers; contracts, BAAs, and agency notifications; CSA audit letters and IRS review letters; SPRS records; FedRAMP and GovRAMP deliverables; and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. A control inherited from a FedRAMP authorized provider is Met when the group's use falls inside the provider's authorization. Gap risk uses the P01 scale.

## 4. Results
### 4.1 GovTech Integration (`gap-analysis.csv`)
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| SP 800-53 Moderate (`G-`) | 177 | 154 | 19 | 0 | 4 |
| CJISSECPOL v6.1 overlay (`CJ-`) | 12 | 7 | 4 | 0 | 1 |
| Pub. 1075 overlay (`PB-`) | 17 | 8 | 8 | 1 | 0 |
| HIPAA business associate, IEP (`HI-`) | 4 | 2 | 1 | 1 | 0 |
| Medicaid and SNAP confidentiality (`MD-`) | 4 | 4 | 0 | 0 | 0 |
| Driver's Privacy Protection Act (`DP-`) | 3 | 1 | 2 | 0 | 0 |
| State law, Florida worked example (`SL-`) | 3 | 1 | 2 | 0 | 0 |
| AI program rules, IEP (`AI-`) | 3 | 0 | 2 | 0 | 1 |
| Other: GovRAMP, SLCGP, CIRCIA (`OT-`) | 3 | 0 | 0 | 0 | 3 |
| Group-wide obligations (`GW-`) | 5 | 3 | 2 | 0 | 0 |
| **Total** | **231** | **180** | **40** | **2** | **9** |

The 19 partially met SP 800-53 rows are in these families: IR (4), PS (3), AC, CM, and CP (2 each), and AT, AU, IA, RA, SA, and SI (1 each). All 16 PE controls are Met by inheritance from the FedRAMP authorized providers.

Of the 42 rows with a gap, 14 are rated High, 25 Moderate, and 3 Low. **Not met:** PB-16 (2 revenue agencies' IRS notifications do not cover the provider B backup vault) and HI-02 (no subcontractor terms between GovTech and corporate for Medicaid ePHI).

The High gaps fall into four themes, all shared with other divisions:
- **People with access to agency data** (G-116, G-119, G-120, CJ-01, CJ-03, PB-01, PB-04): corporate shared-service staff and subcontractor staff outside the screening and certification process (scenario gaps 1 and 10).
- **Notification across divisions** (G-076, G-078, CJ-09, PB-11): agency contacts and clocks are not in the group matrix (gap 5).
- **Recovery at scale** (G-055, G-060): the 8-hour RTO is proven per tenant only (gap 8).
- **AI recommendations in eligibility** (AI-01): caseworkers accept most recommendations without a review-first design (gap 6).

### 4.2 IT Consulting (`gap-analysis-it-consulting.csv`)
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| SP 800-171 Rev. 2 (CMMC Level 2), selected requirements | 14 | 5 | 9 | 0 | 0 |
| DFARS 252.204-7012, 7019, 7020, 7021 and 32 CFR Part 170 | 7 | 1 | 4 | 1 | 1 |
| FAR 52.204-21 | 1 | 0 | 1 | 0 | 0 |
| HIPAA business associate | 3 | 1 | 2 | 0 | 0 |
| Not applicable rules (FTC Safeguards, IRC 7216, conduct rules, CIRCIA) | 4 | 0 | 0 | 0 | 4 |
| **Total** | **29** | **7** | **16** | **1** | **5** |

Of the 17 rows with a gap, 4 are High (IC-G01, IC-G02, IC-G13, IC-G19), 12 Moderate, and 1 Low. **Not met:** IC-G19, no CMMC Level 2 status and no C3PAO assessment scheduled. Phase 2 is suspended, so the C3PAO assessment is now voluntary, but SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies. Almost every gap traces to the **acquired firm**: CUI on its file shares (3.1.3), its VPN with SMS codes (3.1.12), its endpoints without group EDR (3.14.2), and an SPRS score that predates it. The enclave itself, which inherits group controls, is close to ready; what it lacks is documentation of that inheritance (3.12.4; scenario gap 3).

### 4.3 Government Software Products (`gap-analysis-govsoftware.csv`)
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| CJISSECPOL v6.1 (RMS) | 8 | 3 | 3 | 2 | 0 |
| FedRAMP (Grants Management) | 3 | 2 | 0 | 0 | 1 |
| GovRAMP (Civic Suite) | 1 | 0 | 1 | 0 | 0 |
| SOC 2 commitments | 8 | 2 | 6 | 0 | 0 |
| FTC Act Section 5 | 2 | 1 | 1 | 0 | 0 |
| DOJ Data Security Program | 1 | 1 | 0 | 0 | 0 |
| Not applicable (COPPA, CPNI, PADFA) | 3 | 0 | 0 | 0 | 3 |
| **Total** | **26** | **9** | **11** | **2** | **4** |

Of the 13 rows with a gap, 2 are High, 9 Moderate, and 2 Low. **Not met:** SW-G03 (41 RMS connectors on FIPS 140-2 modules; the CJIS deadline of 2026-09-21 falls six days after approval and cannot be met) and SW-G07 (CJI sent to the managed model service in the AI assist beta without a CJIS review). FedRAMP continuous monitoring for Grants Management is fully on track and is the model for the GovRAMP change discipline the Civic Suite lacks.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Shared-service and subcontractor staff screening (1, 10) | Group, GovTech, Software | CJISSECPOL v6.1 PS-3, SA-9, Appendix H; Pub. 1075 sec. 2.C.3, Exhibit 7 I(2), I(8) | High | Suspend unscreened access by 2026-10-31; one group screening register; flowdown checklist (POAM-001, POAM-012) | Group CISO; Group public sector compliance director | 2026-12-31 |
| 2 | Cross-division notification (5) | All | CJISSECPOL v6.1 IR-6; Pub. 1075 sec. 1.8; DFARS 252.204-7012(c); 45 CFR 164.410; Fla. Stat. 501.171(6)(a); Form 8-K Item 1.05 | High | Group notification matrix with every agency, BAA, DoD, and state clock; tabletop (POAM-003, POAM-004) | Group General Counsel | 2026-12-15 |
| 3 | Acquired consulting firm and CMMC (4, 7) | IT Consulting | DFARS 252.204-7012(b); SP 800-171 Rev. 2 3.1.3, 3.1.12, 3.14.2; 32 CFR 170.17 | High | VPN MFA, EDR, CUI into the enclave, then a voluntary C3PAO assessment (POAM-018, POAM-020, POAM-024) | IT Consulting president | 2027-03-31 |
| 4 | RMS connectors and AI assist beta (6, 9) | Software | CJISSECPOL v6.1 SC-13, SA-9 | High | Replace 41 connector modules; stop CJI to the model service until reviewed (POAM-021, POAM-022) | Government Software Products president | 2026-12-31 |
| 5 | IEP AI eligibility recommendations (6) | GovTech | 7 CFR 272.4(a)(2); 272.6(a); 42 CFR 431.10(b)(3) | High | Review-first design, deterministic rules, bias testing, applicant notice (P10; POAM-016) | GovTech Data and AI director | 2026-12-31 |
| 6 | Recovery at scale (8) | GovTech | SP 800-53 CP-4, CP-10; contract RTO | High | Parallel restore automation; full-scale exercise (POAM-011) | ACMP platform director | 2027-03-31 |
| 7 | FTI log retention and IRS notifications (2) | Group, GovTech | Pub. 1075 sec. 4 AU-11; sec. 2.E.6; Exhibit 6 | Moderate | 7-year retention; updated notifications from 2 agencies (POAM-002, POAM-027) | Group cloud platform director; Group public sector compliance director | 2027-03-31 |
| 8 | Enclave inheritance (3) | IT Consulting, Group | SP 800-171 Rev. 2 3.12.4; 32 CFR 170.19 | Moderate | Inheritance matrix (POAM-019) | IT Consulting security and compliance lead | 2026-12-31 |
| 9 | Business associate subcontractor terms | GovTech, Group | 45 CFR 164.308(b)(2); 164.314(a)(2)(iii) | Moderate | Intercompany business associate terms (POAM-026) | Group General Counsel | 2026-12-31 |
| 10 | DPPA bulk requesters | GovTech | 18 U.S.C. 2721(b)-(c) | Moderate | Annual re-verification and sampling (POAM-017) | MVSP program director | 2027-03-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-024 to POAM-027 come directly from this analysis.

## 6. Pending and dated changes
- **CJIS FIPS 140-2 cutoff.** CJISSECPOL v6.1 SC-13 states that FIPS 140-2 certificates "will not be acceptable after September 21, 2026." GovTech's ACMP paths moved in 2026-08 (CJ-10, Met); the RMS connectors will not (SW-G03).
- **CJIS zero-cycle end.** [Priority 2] to [Priority 4] requirements become sanctionable in audits after **2027-09-30**. The contracts already require them. Each new CJISSECPOL version is reviewed within 60 days (CJ-02).
- **CMMC Phase 2** was planned for **2026-11-10** (32 CFR 170.3(e)(2)) and is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13. Under DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5), DoD includes clause 252.204-7021 until 2028-11-09 only when a program office or requiring activity requires a specific CMMC level, and on or after 2028-11-10 whenever the contractor will process, store, or transmit FCI or CUI on its own systems (except COTS-only buys).
- **FAR overhaul.** The "Revolutionary FAR Overhaul" proposed rule (2026-06-23) would move information security clauses into FAR part 40. It is proposed only; FAR 52.204-21 still governs.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is proposed only. If finalized as proposed it would remove the addressable category and require encryption with limited exceptions, which would turn IC-G24 into a mandatory gap.
- **CIRCIA.** Proposed rule only (89 FR 23644). The proposed size-based criterion would likely reach the group (it exceeds the SBA size standard for its NAICS code), so it is tracked for P08 when a final rule is published.
- **Pub. 1075.** Rev. 11-2021 remains the edition at irs.gov. Recheck each July before the SSP review.
- **Colorado SB26-189** (effective 2027-01-01) is a watch item for the AI features; its status is unsettled (litigation and federal preemption efforts).

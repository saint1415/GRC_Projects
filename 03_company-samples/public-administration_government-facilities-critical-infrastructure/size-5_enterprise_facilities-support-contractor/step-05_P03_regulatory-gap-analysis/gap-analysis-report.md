# Regulatory Gap Analysis: Cris Santos Company | Government Services and Facilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded facilities support contractor operating government buildings, NAICS 561210; 8 states and DC) |
| Tier / Vertical | Enterprise / Government Services and Facilities |
| Primary standard | NIST SP 800-53 Rev. 5, Release 5.2.0 (Aug 27, 2025), **Moderate baseline** from SP 800-53B: 177 base controls with 110 enhancements. **Binding by contract** for the IBOP under the 5 state cybersecurity exhibits; **enterprise control standard** for everything else. OT tailoring from NIST SP 800-82 Rev. 3 (September 2023) |
| Other requirements analyzed | FAR 52.204-21, -23, -24/-26 representations, -25, -30, and 52.204-9 with GSAR 552.204-9 (11 GSA contracts); CUI under 32 CFR Part 2002 and GSA Order PBS 3490.3 CHGE 1; GSA BTTRG v3.0 (FISMA through GSA); SEC Form 8-K Item 1.05 and Reg S-K Item 106; FBI CJIS Security Policy v6.1 as applied by public safety customers; FERPA through university contracts; GovRAMP for the FSP; state breach, data security, public records, and customer reporting laws (Florida worked example). Federal text read from eCFR (point-in-time 2026-09-23) and the CJIS Security Policy PDF (v6.1, 06/25/2026) |
| Systems and entities | The IBOP (P02) and enterprise common controls; FCI systems (FSP, collaboration suite, laptops and tablets, ERP); the Federal Facilities, State and Local Government, Education Facilities, and Security Integration segments; AQ-1 and AQ-2 |
| Assessment dates | 2026-06-01 to 2026-07-31 (site sampling visits 2026-06-15 to 2026-07-17; evidence sampling completed 2026-08-14). Statuses reflect 2026-08-28, after the P07 results were in |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Vice President, Government Contracts Compliance; sampling reperformed by Internal Audit for 12 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-31; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability
The vertical profile names SP 800-53 Rev. 5 as the primary control set because FISMA, IRS Pub. 1075, CJIS, and GovRAMP are all built on it. **SP 800-53 is a catalog, not a law. It binds a private contractor only through a contract or a federal system authorization.** At enterprise size the question is therefore not "does this rule apply to the company" but "which contracts and statutes reach which systems and segments".

### 1.1 Requirement by requirement
| ID | Requirement | Applies? | Basis |
|---|---|---|---|
| State exhibits | SP 800-53 Rev. 5 Moderate | **Yes, by contract, for the IBOP** | The 5 state cybersecurity exhibits require Moderate controls for contractor-managed systems that store or process agency data. Florida worked example: Fla. Stat. 282.318(4)(h) requires state agency IT service contracts to meet NIST CSF and to assign security responsibilities |
| C-GOVERNMENT-R01 | FISMA (44 U.S.C. 3551-3558) | **Indirectly, for Federal Facilities only** | 44 U.S.C. 3554(a)(1)(A)(ii) makes each agency responsible for systems "used or operated by an agency or by a contractor of an agency". GSA's building systems hold GSA's authorization; company staff operate them through GSA's virtual desktop and must follow GSA IT policies (BTTRG v3.0 section 1.1). **No company-owned system operates on GSA's behalf**, and under 32 CFR 2002.14(h)(2) a contractor system that receives federal information only incidental to a service is a non-federal system |
| FAR clauses | 52.204-21, -23, -25, -30, -9; GSAR 552.204-9 | **Yes, in all 11 GSA contracts** | Clause text read from eCFR. 52.204-21 applies to company systems that hold FCI (the FSP, collaboration suite, laptops and tablets, ERP). 52.204-25(b)(2) prohibits the company's **own use** of covered equipment anywhere, not only on federal work |
| CUI | 32 CFR Part 2002; GSA Order PBS 3490.3 CHGE 1 | **Yes, by statement of work** | GSA marks sensitive building drawings as CUI (Physical Security). The contracts do not cite NIST SP 800-171, so CUI is handled under the SP 800-53 controls in the CUI enclave. **Watch item:** a GSA CUI clause citing SP 800-171, or the proposed RFO CUI clause, would require a separate assessment |
| SEC | Form 8-K Item 1.05; 17 CFR 229.106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| C-GOVERNMENT-R03 | CJIS Security Policy v6.1 | **Yes, through 27 public safety customers** | The company has no CJI access and performs no criminal justice functions. But the policy requires role-based training for "all individuals with unescorted access to a physically secure location" (AT-3(a)), and its Use Case 2 applies this to custodial staff who clean a police facility after hours. The agencies decide whether personnel security (PS-3 fingerprint-based checks) applies and keep PE-3(b) access logs, which come from the IBOP |
| C-GOVERNMENT-R05 | FERPA (34 CFR Part 99) | **Yes, through 9 university contracts** | The universities designate the company a school official under 99.31(a)(1)(i)(B) for student cardholder records, so the redisclosure limits in 99.33(a) apply. Whether access logs are education records or law enforcement unit records (99.3; 99.8) is decided by each university's counsel |
| C-GOVERNMENT-R08 | GovRAMP | **Yes, for the FSP under two state procurement policies** | GovRAMP is not law; it binds through procurement. It does not apply to the IBOP, which state customers reach under the exhibits instead |
| State laws | Breach, data security, public records, customer reporting | **Yes** | Each state where affected individuals reside or where a customer is located; Florida is the worked example (Fla. Stat. 501.171, 501.702, 119.0701, 119.071(3)(a), 282.318, 282.3185, 282.3186) |
| C-GOVERNMENT-R02 | IRS Pub. 1075 | No | State contracts for revenue and benefits agency buildings exclude restricted FTI areas; staff enter only under escort |
| C-GOVERNMENT-R04 | VVSG 2.0 | No | No election systems |
| C-GOVERNMENT-R07 | SLCGP | No | A grant condition for governments |
| C-GOVERNMENT-R06 | CIRCIA | **Not in force** | Final rule not published as of 2026-09-25. If finalized as proposed, the company would likely be covered as an entity above its SBA size standard in a critical infrastructure sector (counsel to confirm). Tracked in section 6 |
| Other | FedRAMP; DFARS 252.204-7012 and CMMC; Colorado SB26-189; Texas HB 149 | No | No cloud service to federal agencies; no DoD contracts; no business in Colorado or Texas |

**Size check.** None of these requirements has a size exemption that helps the company. Above the SBA standard, it is also inside the proposed CIRCIA size criterion. The enterprise-only additions are the SEC rules and the breadth of customers (federal, state, local, public safety, education).

### 1.2 OT tailoring
Controls were applied to OT components using NIST SP 800-82 Rev. 3: passive discovery instead of active scans of field controllers (RA-5), segmentation to compensate for unencrypted BACnet and legacy reader wiring (SC-8), and vendor hardening guides for PACS and BAS products (CM-6). No control was tailored out. Developer controls (SA-10, SA-11, SA-15) apply to the company's own integration code and the FSP, and to vendors through contracts.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Method
1. **Decompose.** One row per Moderate base control (G-001 to G-177) with its Moderate enhancements in the citation column; FAR clauses to the paragraph (G-178 to G-199); CUI, BTTRG, SEC, CJIS, FERPA, GovRAMP, and state law requirements to the section or paragraph (G-200 to G-233); and four rows recording requirements that do not apply (G-234 to G-237).
2. **Crosswalk.** 134 control rows use NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). The other 43 control rows and all non-NIST rows are author mappings, labeled as such. FAR rows map through the SP 800-171 Rev. 2 lineage of the 15 basic safeguarding requirements.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); populations under 250 and lower-risk controls used 25 to 40 items; configuration and register data were checked in full with analytics. Selections were random or stratified to include AQ-1 and AQ-2. **48 rows were tested by sampling or full-population analytics; 20 found exceptions.** A further 21 control rows rely on the P07 samples (marked "P07 sample").
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High and Very High gaps are in the P01 register and the P07 POA&M.

The SP 800-53 rows use the same statements as the SSP control table (P02), so the two documents do not drift apart.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| NIST SP 800-53 Rev. 5 Moderate baseline (177 base controls) | 138 | 39 | 0 | 0 | 177 |
| FAR 52.204-21 and related FAR clauses | 17 | 5 | 0 | 0 | 22 |
| CUI (32 CFR Part 2002; GSA Order PBS 3490.3) | 2 | 2 | 0 | 1 | 5 |
| FISMA through GSA BTTRG v3.0 (C-GOVERNMENT-R01) | 2 | 1 | 0 | 1 | 4 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 4 | 1 | 0 | 0 | 5 |
| CJIS Security Policy v6.1 (C-GOVERNMENT-R03) | 3 | 1 | 0 | 0 | 4 |
| FERPA (C-GOVERNMENT-R05) | 2 | 0 | 0 | 0 | 2 |
| GovRAMP (C-GOVERNMENT-R08) | 0 | 1 | 0 | 0 | 1 |
| State laws (Florida worked example) | 9 | 1 | 0 | 0 | 10 |
| Not applicable rows (R02, R04, R06, R07) | 0 | 0 | 0 | 4 | 4 |
| **Total** | **178** | **53** | **0** | **6** | **237** |

**SP 800-53 Moderate baseline by family:**
| Family | Met | Partially met |
|---|---|---|
| AC Access Control | 13 | 4 |
| AT Awareness and Training | 3 | 1 |
| AU Audit and Accountability | 8 | 3 |
| CA Assessment, Authorization, and Monitoring | 5 | 2 |
| CM Configuration Management | 9 | 3 |
| CP Contingency Planning | 4 | 5 |
| IA Identification and Authentication | 7 | 3 |
| IR Incident Response | 5 | 3 |
| MA Maintenance | 5 | 1 |
| MP Media Protection | 7 | 0 |
| PE Physical and Environmental Protection | 16 | 0 |
| PL Planning | 6 | 0 |
| PS Personnel Security | 7 | 2 |
| RA Risk Assessment | 5 | 1 |
| SA System and Services Acquisition | 9 | 2 |
| SC System and Communications Protection | 16 | 2 |
| SI System and Information Integrity | 8 | 3 |
| SR Supply Chain Risk Management | 5 | 4 |
| **Total (177)** | **138** | **39** |

No requirement is wholly Not met. The gaps concentrate in four places: the acquired businesses (AQ-1 remote access and identities, AQ-2 legacy instances), the OT edge (monitoring coverage, default credentials, segmentation), supply chain scope (AQ-1 offices and spares, FASCSA checks, subcontract flow-downs), and disclosure readiness for OT incidents.

**Gap risk levels across all regulations (53 Partially met rows):** Very High 2, High 14, Moderate 32, Low 5.

## 4. Priority gaps (Very High and High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-012 | AC-17 | Legacy always-on remote-support tool at 142 AQ-1 sites | Migrate to the OT gateway; remove the tool (POAM-001) | Vice President, Integration Management Office | 2027-01-31 |
| G-082 | MA-4 | Same tool provides unbrokered nonlocal maintenance | POAM-001 | Vice President, Integration Management Office | 2027-01-31 |
| G-002 | AC-2 | AQ-1 legacy directory; 311 inactive and shared customer console accounts | Federation (POAM-002); 90-day disable and attestation (POAM-017) | Director of Identity and Access Management | 2026-12-31 |
| G-062 | IA-2 | AQ-1 and AQ-2 identities without enterprise MFA | POAM-002; POAM-004 | Director of Identity and Access Management | 2026-12-15 |
| G-045 | CM-6 | Vendor default credentials on 5 of 60 sampled field devices | Credential sweep (POAM-003) | Director of OT Security | 2026-12-31 |
| G-065 | IA-5 | Same finding as CM-6 | POAM-003 | Director of OT Security | 2026-12-31 |
| G-038 | CA-7 | OT monitoring at 870 of 1,420 buildings | Sensors, AQ sites first (POAM-005) | Director of OT Security | 2027-06-30 |
| G-161 | SI-4 | Same coverage gap | POAM-005 | Director of OT Security | 2027-06-30 |
| G-126 | RA-5 | OT vulnerability coverage; 37 unsupported workstations | POAM-005; POAM-016 | Director of OT Security | 2027-06-30 |
| G-144 | SC-7 | Flat customer networks at 214 buildings; AQ-1 bypass path | POAM-018; POAM-001 | Director of OT Security | 2027-06-30 |
| G-060 | CP-10 | PACS administration restored in 7.5 h against a 4 h RTO | Automate failover; retest (POAM-007) | IBOP Platform Manager | 2027-01-31 |
| G-078 | IR-8 | No OT or physical-safety factors in the materiality step | Playbook update; tabletop (POAM-013) | General Counsel | 2026-12-15 |
| G-171 | SR-3 | Screening scope excludes AQ-1 offices, spares, and subcontractor-bought equipment | POAM-010 | Vice President, Government Contracts Compliance | 2026-11-30 |
| G-196 | FAR 52.204-25(b)(2) and (d) | 1 recording server model with unconfirmed manufacturer in 2 AQ-1 offices | Confirm by 2026-10-30; report within 1 business day if covered; replace (POAM-010) | Vice President, Government Contracts Compliance | 2026-11-30 |
| G-209 | Form 8-K Item 1.05 | Playbook covers IT and ransomware only; not exercised since AQ-2 | POAM-013 | General Counsel | 2026-12-15 |
| G-210 | Form 8-K Item 1.05 (materiality determination) | Government-customer contract, safety, and eligibility factors missing | POAM-013 | General Counsel | 2026-12-15 |

**Reporting clocks in the supply chain clauses (verified in eCFR):**
- 52.204-25(d): report covered telecommunications or video surveillance equipment within **one business day** of identification, with further information within 10 business days.
- 52.204-23(c): report Kaspersky covered articles within **3 business days** of identification, with further information within 10 business days.
- 52.204-30(c): check SAM.gov for FASCSA orders at least once every three months; report within **3 business days** of identification, with further information within 10 business days.

## 5. Compliance roadmap
| Quarter | Milestones | Requirements served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | AQ-1 equipment screening and any 52.204-25(d) report (POAM-010); enterprise FASCSA check (POAM-011); AQ-1 identity federation (POAM-002); field device credential sweep (POAM-003); notice matrix for AQ contracts (POAM-014); CJIS training holds (POAM-019); materiality playbook update and disclosure committee OT tabletop on 2026-11-19 (POAM-013); CUI moved into the enclave (POAM-015); GSA building recovery exercises (POAM-023); PIV return workflow (POAM-024); customer console clean-up (POAM-017) | FAR 52.204-25, -30, -9; SP 800-53 AC-2, IA-2, IA-5, CM-6, IR-6, AT-3; CJIS AT-3; 32 CFR 2002.14(c); BTTRG 1.6.2; Form 8-K Item 1.05 | Screening records; federation records; sweep reports; tabletop report; enclave audit |
| 2027 Q1 | AQ-1 tool removed from all 142 sites (POAM-001); PACS failover automation and retest (POAM-007); program repository restore test (POAM-008); OT inventory reconciliation (POAM-009); subcontract addendum signed by all suppliers with access (POAM-012); retention jobs per tenant (POAM-020); AI committee reviews and local bias testing (POAM-021); AQ-2 campuses on the IBOP (POAM-004); FY2026 Item 106 draft with the OT program | SP 800-53 AC-17, MA-4, CP-9, CP-10, CM-8, SA-9, SI-12; FAR 52.204-21(c), 52.204-25(e); 17 CFR 229.106(b) | Agent removal records; DR retest report; signed addenda; retention reports |
| 2027 Q2 | OT sensors at 95% of buildings (POAM-005); unsupported workstations replaced or isolated (POAM-016); OT segmentation at the 214 buildings (POAM-018); GovRAMP verification for the FSP (POAM-022); ROC 24-hour absorption and second paging provider (POAM-025) | SP 800-53 CA-7, SI-4, RA-5, SA-22, SC-7, CP-2; GovRAMP | Sensor coverage report; segmentation records; GovRAMP status |
| 2027 Q3 | Annual risk analysis and gap reassessment; review the status of CIRCIA, the RFO, and SP 800-82 Rev. 4 | All | Updated P01 and P03 |

## 6. Pending changes (not current obligations)
- **FAR overhaul (RFO).** The proposed rule (FR Doc. 2026-12559, June 23, 2026) would move information security clauses into FAR part 40, renumber 52.204-21 as 52.240-5, and add CUI clauses requiring NIST SP 800-171 Rev. 3. **Proposed only.** Flagged in the `pending_rule_change` column of the FAR and CUI rows.
- **NIST SP 800-82 Rev. 4.** Initial public draft published 2026-09-21 (comments due 2026-11-30). It lists building automation systems and physical access control systems among its OT examples. **Draft only.** Rev. 3 remains the OT reference here. Flagged on the OT rows (AC-17, CM-6, CM-8, CP-2, MA-4, RA-5, SC-7, SC-8, SI-4).
- **CIRCIA.** No final rule as of 2026-09-25. Reporting to CISA is voluntary and is coordinated with customers.
- **SEC.** A 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.

## 7. Regulator-ready and customer-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a GSA contracting officer, a state customer's annual assessment request, a public safety customer's CJIS audit of its facility, a university's FERPA review, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- FAR screening logs, SAM checks, PIV return logs, and subcontract flow-down records;
- CUI enclave permissions and the 2026-08-20 notices to GSA contracting officers;
- customer notice records and CJIS training rosters;
- record retention of at least 3 years, or longer where a contract or customer records schedule requires (POL-01 4.11).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-31. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.

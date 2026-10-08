# Regulatory Gap Analysis: Cris Santos Company | Government Services and Facilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings, NAICS 561210) |
| Tier / Vertical | Micro / Government Services and Facilities |
| Primary standard | NIST SP 800-53 Rev. 5, Release 5.2.0 (Aug 27, 2025), **Moderate baseline** from SP 800-53B: 177 base controls with 110 enhancements. **Binding by the county security exhibit (CT-C)** for SYS-01, SYS-02, SYS-03 and the accounts that administer them; **benchmark** for the rest of the platform. OT tailoring from NIST SP 800-82 Rev. 3 |
| Overlays | FAR 52.204-21 (NOV 2021), 52.204-23, 52.204-25, 52.204-30, and 52.204-9 as flowed down by the federal subcontract (CT-F), read from eCFR (point-in-time 2026-09-23); Fla. Stat. 501.171, 119.0701, and 119.071(3) (2026 text, read on flsenate.gov) |
| System | Building Systems Operations Platform (BSOP), per the SSP (P02) |
| Assessment dates | Fieldwork 2026-07-13 to 2026-07-24 (site walkthroughs 2026-07-15 to 2026-07-16). Statuses reflect 2026-08-31, after the P06 policies were approved and the P07 results were in |
| Assessor | Office and Compliance Manager (Information Security Officer), with the Lead Controls Technician, the Security Systems Technician, and the MSP lead technician |
| Approved | 2026-08-31 by the owner |

## 1. Applicability
The vertical profile names SP 800-53 Rev. 5 as the primary control set, because FISMA, IRS Pub. 1075, CJIS, and GovRAMP are all built on it. **But SP 800-53 is a catalog, not a law. It binds a private contractor only through a contract or a federal system authorization.** So the first step was to sort out which customer rules reach a 7-person company, and how.

### 1.1 How each customer's rules reach the company
| Contract | Customer | What the company operates | How security terms reach the company |
|---|---|---|---|
| CT-C | Florida county (4 buildings) | Its own access control tenant (SYS-01) for the county; BAS monitoring and remote write (SYS-02, SYS-03) | Security exhibit requiring NIST SP 800-53 Rev. 5 **Moderate** controls for systems the vendor hosts for the county and for privileged vendor accounts. Counties must adopt cybersecurity standards consistent with the NIST Cybersecurity Framework (Fla. Stat. 282.3185(4)(a)); this county chose SP 800-53 Moderate for vendors with that kind of access |
| CT-M | Florida city (3 buildings) | Named administrator accounts on city systems (SYS-10); read-only BAS feed to SYS-02 | City contract terms referring to the city's NIST CSF-based standards (also adopted under 282.3185(4)(a)); named accounts, city MFA, 24-hour notice |
| CT-F | Prime contractor holding a GSA PBS operations and maintenance contract (one federal building) | Nothing of its own. GSA's BAS is reached only on GSA equipment with PIV cards | FAR clauses flowed down; CUI terms (32 CFR Part 2002, GSA Order PBS 3490.3 CHGE 1); GSA Building Technologies Technical Reference Guide v3.0 (BTTRG), including immediate incident reporting (section 1.6.1) |

### 1.2 Decisions, requirement by requirement
| ID | Requirement | Applies to the company? | Reason |
|---|---|---|---|
| C-GOVERNMENT-R01 | FISMA (44 U.S.C. 3551-3558) | **Indirectly, for CT-F only** | FISMA makes each agency responsible for information systems "used or operated by an agency or by a contractor of an agency" (44 U.S.C. 3554(a)(1)(A)(ii)). GSA's BAS is a GSA system under GSA's authorization. The company operates it only on GSA equipment, following GSA policies through the BTTRG. **No company system operates on GSA's behalf**, so the company's own systems are not federal systems |
| C-GOVERNMENT-R02 | IRS Pub. 1075 | No | No federal tax information in any building or system in scope |
| C-GOVERNMENT-R03 | CJIS Security Policy v6.1 | No | Neither contract covers the sheriff's office or the police headquarters. Recheck if the scope changes |
| C-GOVERNMENT-R04 | VVSG 2.0 | No | No election equipment; the supervisor of elections office is outside CT-C |
| C-GOVERNMENT-R05 | FERPA | No | No education facilities |
| C-GOVERNMENT-R06 | CIRCIA | Not in force | Proposed rule only (89 FR 23644). No final rule as of 2026-09-25. Its proposed government facilities criteria target state, local, tribal, and territorial government entities, not their contractors, and the company is far below its SBA size standard |
| C-GOVERNMENT-R07 | SLCGP (6 U.S.C. 665g) | No | A grant condition for governments |
| C-GOVERNMENT-R08 | GovRAMP | Not to the company | No customer requires it of the company. It is a question for the SYS-01 vendor (P09) |

**Size does not change the answer.** None of these rules, and none of the contract terms, has a size exemption. The county exhibit applies to a 7-person vendor exactly as to a large one, and the FAR clauses apply to every subcontractor that receives them. What size changes is **how** the controls are met: most physical and platform controls are inherited from SaaS vendors, and one person holds several roles (SSP section 5).

- **SP 800-53 Rev. 5 Moderate: binding by contract** for SYS-01 (county cardholder data), SYS-02 and SYS-03 (remote write into county buildings), and the accounts that administer them. **Benchmark** for the suite, CMMS, laptops, and the city access paths; one control set is simpler than two.
- **FAR 52.204-21: binding** for company systems that hold federal contract information: the suite (work orders and drawings from the prime), the CMMS (CT-F work orders), and the laptops.
- **CUI.** GSA marks sensitive building drawings as CUI (Physical Security category) under GSA Order PBS 3490.3 CHGE 1, and the CT-F statement of work requires handling under 32 CFR Part 2002. The subcontract does not cite NIST SP 800-171, so CUI is handled under the 800-53 access and media controls (AC-3, AC-21, MP-2 to MP-4, SC-8). **Watch item:** if a CUI clause citing SP 800-171 is added, a separate assessment is needed.
- **Florida statutes.** Three apply directly. **Fla. Stat. 501.171** requires a third-party agent, an entity "contracted to maintain, store, or process personal information on behalf of a covered entity or governmental entity" (501.171(1)(h)), to "take reasonable measures to protect and secure data in electronic form containing personal information" (501.171(2)), to notify within 10 days of determining a breach (501.171(6)(a)), and to dispose of customer records securely (501.171(8)). Two questions are for counsel: whether a county is a "governmental entity" (501.171(1)(f) refers to instrumentalities "of this state"), and which cardholder fields are personal information (badge credential numbers; access history as "geolocation" under 501.171(1)(g)1.a.(VII); face templates as "biometric data as defined in s. 501.702" under (VI)). The company applies the duties to SYS-01 data either way. **Fla. Stat. 119.0701(2)(b)** sets the contractor's public records duties, and **119.071(3)** makes security system plans confidential and exempt and requires recipients of exempt building plans to keep their exempt status.

### 1.3 OT tailoring
Controls were applied to the gateways and the remote paths into customer BAS networks using NIST SP 800-82 Rev. 3. Examples: no active vulnerability scanning of customer BAS networks without the customer's approval (RA-5); no malware agents on gateways, compensated by outbound-only tunnels (SI-3, SC-7); BACnet cannot be encrypted, so segmentation and VPN limits compensate (SC-8, AC-4). Four developer controls (SA-3, SA-10, SA-11, SA-15) are not applicable because the company develops no software; its vendors' practices are reviewed under SA-9.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Method
1. **Requirements.** One row per Moderate base control (G-001 to G-177), with its Moderate enhancements assessed inside the row and named in the citation column; 23 FAR rows (G-178 to G-200) cited to clause paragraph; 5 Florida rows (G-201 to G-205). FAR and Florida text is U.S. and state government text, so short quotes are used.
2. **Crosswalk.**
   - 134 control rows use NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). The other 43 control rows have no NIST reference and show "None".
   - FAR rows are author mappings, through the SP 800-171 Rev. 2 lineage of the 15 basic safeguarding requirements. Florida rows are author mappings. Both are labeled.
3. **Documentary evidence.** Each status rests on a named document or record: SYS-01 and SYS-02 user, role, and audit exports; suite and CMMS user lists and sharing reports; gateway configuration exports and the firmware list; the MSP's July 2026 patch, antivirus, and encryption reports and the SYS-08 job report; contracts and the subcontract; purchase records; background check and PIV records; customer training certificates; the SYS-01 vendor's SOC 2 Type 2 report; and the P07 test results. Interviews covered all 7 staff and the MSP lead technician.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale. The same statements appear in the SSP control table (P02).

## 3. Results summary
### 3.1 SP 800-53 Rev. 5 Moderate baseline (177 base controls)
| Family | Controls | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| AC Access Control | 17 | 5 | 12 | 0 | 0 |
| AT Awareness and Training | 4 | 0 | 3 | 1 | 0 |
| AU Audit and Accountability | 11 | 3 | 7 | 1 | 0 |
| CA Assessment, Authorization, and Monitoring | 7 | 2 | 4 | 1 | 0 |
| CM Configuration Management | 12 | 1 | 6 | 5 | 0 |
| CP Contingency Planning | 9 | 0 | 3 | 6 | 0 |
| IA Identification and Authentication | 10 | 4 | 6 | 0 | 0 |
| IR Incident Response | 8 | 0 | 2 | 6 | 0 |
| MA Maintenance | 6 | 0 | 6 | 0 | 0 |
| MP Media Protection | 7 | 0 | 6 | 1 | 0 |
| PE Physical and Environmental Protection | 16 | 10 | 6 | 0 | 0 |
| PL Planning | 6 | 3 | 3 | 0 | 0 |
| PS Personnel Security | 9 | 1 | 6 | 2 | 0 |
| RA Risk Assessment | 6 | 2 | 3 | 1 | 0 |
| SA System and Services Acquisition | 11 | 0 | 7 | 0 | 4 |
| SC System and Communications Protection | 18 | 14 | 4 | 0 | 0 |
| SI System and Information Integrity | 11 | 5 | 4 | 2 | 0 |
| SR Supply Chain Risk Management | 9 | 0 | 3 | 6 | 0 |
| **Total** | **177** | **50** | **91** | **32** | **4** |

Most "Met" rows are inherited from the SaaS vendors or the office landlord (PE, SC). The weakest families are the ones that matter most for a company whose job is remote access to government buildings: incident response, contingency planning, supply chain, and configuration management.

### 3.2 FAR clauses (23 rows)
| Clause | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 52.204-21(b)(1) (15 requirements) | 9 | 5 | 0 | 1 |
| 52.204-21(c) flow-down | 0 | 0 | 0 | 1 |
| 52.204-23, -25, -30, 52.204-9 (7 rows) | 1 | 5 | 1 | 0 |
| **Total** | **10** | **10** | **1** | **2** |

The basic safeguarding requirements score well because the suite and CMMS have named accounts with MFA and the MSP covers patching and malware. The two N/A rows: 52.204-21(b)(1)(xi) (the company hosts no publicly accessible components) and 52.204-21(c) (the company has no lower-tier subcontractors under CT-F). The supply chain clauses are the weak spot: there is no screening and no SAM.gov search.

### 3.3 Florida statutes (5 rows)
All 5 rows are **Partially met**: 501.171(2), 501.171(6)(a), 501.171(8), 119.0701(2)(b), and 119.071(3)(a)-(b).

### 3.4 Gap risk (Partially met and Not met rows, 139 in total)
| Gap risk | Rows |
|---|---|
| High | 18 |
| Moderate | 53 |
| Low | 59 |
| Very Low | 9 |

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Shared password-only account with write access to county buildings; late account removal | AC-2; IA-2; PS-4 | High | Named SYS-02 accounts with MFA; same-day termination checklist; monthly reconciliation | Lead Controls Technician; Office and Compliance Manager | 2026-10-31 |
| Default and shared gateway passwords | IA-5 | High | Password manager; unique passwords; default check at commissioning | Lead Controls Technician | 2026-10-31 |
| Gateway VPN and MSP RMM without MFA | AC-17; MA-4 | High | Certificate plus MFA on the VPN; MSP evidence of RMM MFA | Lead Controls Technician | 2026-11-30 |
| No log review or monitoring | AU-6; SI-4 | High | Weekly review checklist; alerts for new administrators and off-ticket writes | Office and Compliance Manager | 2026-10-31 to 2027-01-31 |
| Engineering records not backed up; no contingency plan or tests | CP-2; CP-4; CP-9 | High | Engineering repository in the suite; contingency plan with manual lockdown steps; quarterly restore tests | Lead Controls Technician; Office and Compliance Manager | 2026-11-30 |
| Gateway firmware behind; no scanning | SI-2; RA-5 | High | Quarterly firmware review in approved windows; MSP scans of laptops and office network | Lead Controls Technician | 2026-11-30 to 2026-12-31 |
| No incident handling or reporting rule | IR-4; IR-6 | High | P08 runbook, reporting card, tabletop | Office and Compliance Manager | 2026-09-30 to 2026-11-30 |
| No supplier screening for CT-F parts; no FASCSA search | SR-3; 52.204-25(b)(1); 52.204-30(b) | High | Screening checklist; approved suppliers; SAM.gov search before each CT-F order and at least quarterly | Office and Compliance Manager | 2026-09-30 to 2026-10-31 |
| No security terms for the MSP and SYS-02 vendor | SA-9 | High | Security addendum and questionnaire; 24-hour notice | Office and Compliance Manager | 2026-12-31 |
| CUI drawings not controlled | AC-3; AC-21; MP-3; MP-4 | Moderate | Restricted CUI folder; no "anyone" links; marking; CUI training | Office and Compliance Manager | 2026-10-31 |

**Reporting clocks in the supply chain clauses (verified in eCFR, 2026-09-23 point in time):**
- 52.204-25(d): report covered telecommunications or video surveillance equipment within **one business day** of identification, with further information within 10 business days.
- 52.204-23(c): report Kaspersky covered articles within **3 business days** of identification.
- 52.204-30(c)(4): report a covered article or source subject to a FASCSA order within **3 business days** of identification. Paragraph (c)(1) (the quarterly SAM.gov review) is excluded from subcontracts by 52.204-30(e)(1), but (b)(2) still requires a search of SAM.gov for applicable FASCSA orders; the company does both.

As a subcontractor, the company reports to the prime, which reports to the contracting officer. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person company: most actions are one-page procedures, vendor settings, or MSP work, not new systems. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Main gaps closed |
|---|---|---|---|
| 1. Accounts and notices | 2026-09-30 | Termination checklist with PIV return; reporting card; notice matrix briefing; signed policy acknowledgments; SAM.gov FASCSA search; incident log | AC-2, PS-4, IR-6, IR-5, PL-4, PS-6; 52.204-9(b); 52.204-30(b) |
| 2. Access hardening | 2026-10-31 | Named SYS-02 accounts with MFA; password manager; restricted CUI folder; parts screening checklist; weekly log review; SYS-01 operator roles | AC-3, AC-6, AC-21, IA-2, IA-5, MP-3, MP-4, AU-6, SR-3, SR-5, SR-11; 52.204-21(b)(1)(ii); 52.204-25(b)(1) |
| 3. Resilience | 2026-11-30 | Engineering repository; first restore tests; contingency plan with manual lockdown steps; gateway VPN MFA; firmware updates; tabletop with the county and MSP; counsel opinion on 501.171 scope | CP-2, CP-4, CP-9, AC-17, MA-4, SI-2, IR-3, IR-4, CM-8; 501.171(6)(a) |
| 4. Oversight | 2026-12-31 | MSP security addendum; SYS-02 vendor questionnaire; supply chain plan; EDR; vulnerability scanning; records and public records procedure; monitoring metrics | SA-9, SR-2, SR-6, SR-8, RA-5, SI-12, CA-7, PS-7; 119.0701(2)(b) |
| 5. Annual cycle | 2027-07-31 | Risk assessment update; independent assessment; policy review | RA-3, CA-2, PL-1 |

**Progress check.** The Office and Compliance Manager reports progress to the owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending changes (not current obligations)
- **FAR overhaul.** The proposed rule FR Doc. 2026-12559 (91 FR 37550, June 23, 2026; comments closed 2026-07-23) would replace 52.204-21 with a new clause 52.240-5, Covered Federal Information, and consolidate 52.204-23, 52.204-25, and 52.204-30 into a new clause 52.240-3, Security Prohibitions and Exclusion. **Proposed only.** Flagged in the `pending_rule_change` column of the FAR rows.
- **NIST SP 800-82 Rev. 4.** Initial public draft published 2026-09-21 (comments due 2026-11-30). It is restructured around CSF 2.0 and expands coverage to building automation and control systems. **Draft only.** Rev. 3 remains the OT reference here. Flagged on the OT rows.
- **CIRCIA.** No final rule as of 2026-09-25. Reporting to CISA is voluntary.

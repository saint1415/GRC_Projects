# Regulatory Gap Analysis: Cris Santos Company | Public Administration | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed GovTech systems integrator, NAICS 541512) |
| Tier / Vertical | Mid-Market / Public Administration |
| System | Agency Case Management Cloud (ACMC), as bounded in the SSP (P02); managed services rows where an overlay reaches agency-hosted systems |
| Primary requirement set | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline, as selected in NIST SP 800-53B, required by every agency contract |
| Overlays | FBI CJIS Security Policy v6.1 (06/25/2026) for AG-02 and AG-39 (N92-R02); IRS Publication 1075 (Rev. 11-2021) for AG-01 (N92-R01); SNAP and Medicaid confidentiality for AG-03 (N92-R04); Driver's Privacy Protection Act for AG-04 (N92-R05); Fla. Stat. 501.171 (third-party agent duties) |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-28 (the IA-5 row was updated 2026-08-19 from P07 testing, and PB-09 on 2026-09-08 when the export was stopped) |
| Assessor | GRC Manager and the Director of Contracts and Compliance, with the Director of Information Security; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-17 |

## 1. Applicability
**Primary business line:** hosting and operating the ACMC for state and local agencies. The company is a private contractor, not an agency. Apart from Fla. Stat. 501.171, none of the rules below binds it by its own force. Each reaches it **through a contract with an agency that is bound**, so this analysis starts with the contracts and then checks whether anything changes at this size.

| Requirement | Applies? | Basis, and what changes at Mid-Market size |
|---|---|---|
| SP 800-53 Rev. 5 Moderate baseline | **Yes, by contract** | Every agency contract requires it for the ACMC. No size element |
| CJIS Security Policy v6.1 (N92-R02) | **Yes, for AG-02 and AG-39 work** | 28 CFR 20.33(a)(7) lets criminal history record information go "to private contractors pursuant to a specific agreement" that incorporates the CJIS Security Addendum. The Addendum binds the contractor to the policy "in effect when the contract is executed and all subsequent versions" (sec. 3.01). No size threshold. At this size the company also has a second CJIS customer in another state, so the State B CJIS Systems Agency's procedures apply to AG-39 (CJ-02) |
| IRS Publication 1075 (N92-R01) | **Yes, for AG-01 work** | AG-01 receives FTI under IRC 6103(d) and may disclose it to a contractor "to the extent necessary in connection with a written contract" (26 CFR 301.6103(n)-1(a)). The AG-01 contract carries Exhibit 7 language, and AG-01's 45-day notification names the company and its cloud provider (Pub. 1075 sections 2.E.6.1-2.E.6.2; Exhibit 6). Edition checked: Rev. 11-2021, the edition served at irs.gov during fieldwork (rechecked 2026-10-06). No size threshold |
| FTI in the AG-03 tenant | **Prohibited** | Human services agencies that receive FTI under IRC 6103(l)(7) "may not contract for services that involve the disclosure of FTI to contractors or sub-contractors" (section 2.C.11.2). Tested through PR-03 |
| Medicaid and SNAP confidentiality (N92-R04) | **Yes, by contract for AG-03** (and AG-44 from go-live) | 42 CFR 431.300-431.307 and 7 CFR 272.1(c) bind the state agency; the AG-03 contract applies them to the company. Access is limited to persons "subject to standards of confidentiality that are comparable to those of the agency" (431.306(b)) |
| Driver's Privacy Protection Act (N92-R05) | **Yes, for AG-04 work** (new at this size) | A state motor vehicle department "and any officer, employee, or contractor thereof" may not disclose personal information except for permitted uses (18 U.S.C. 2721(a)). The company receives the data as an entity "acting on behalf of" a local agency "in carrying out its functions" (2721(b)(1)). 2722(a) makes it unlawful for any person to obtain or disclose the data for a use not permitted, and 2724 gives individuals a civil action with liquidated damages of $2,500. No size threshold |
| Fla. Stat. 501.171 | **Applies directly** | The company is a "third-party agent" (501.171(1)(h)): reasonable measures (2), notice to the agency no later than 10 days after determining a breach (6)(a), and secure disposal of customer records (8) |
| Florida Rule 60GG-2, F.A.C. | Reaches the company by contract | Binds state agencies (Rule 60GG-2.001(1)(b)), which must make "solicitations, contracts, and service-level agreements" meet or exceed the NIST Cybersecurity Framework (Rule 60GG-2.001(3)(b); Fla. Stat. 282.318(4)(h)). The SP 800-53 Moderate requirement in the state agency contracts is more detailed, so **no separate rows** are needed |
| Fla. Stat. 282.318, 282.3185, 282.3186 | Agency duties the company supports | Florida state agencies and local governments report ransomware within 12 hours and may not pay a ransom. Handled in P08 |
| State B and State C law | Reaches the company by contract | Treated generically: the law of each state where the agency sits or affected individuals reside, confirmed by counsel. State requirements map is an open item (CJ-02; P01 R-051) |
| HIPAA Security Rule (N92-R03) | **Not applicable** | No customer has designated the company a business associate; AG-03 placed its eligibility functions outside its health care component (45 CFR 164.105) |
| GovRAMP (N92-R08) | Voluntary; required by the State B contracts | A verification program, not law. Ready status held; Authorized required by 2027-06-30 (P09) |
| CIRCIA (N92-R07) | **Proposed only** | No final rule as of 2026-09-25 (89 FR 23644). Unlike at Small size, the proposed size-based criterion could reach the company if it is treated as an entity in a critical infrastructure sector, because it exceeds the SBA standard. Recheck when a final rule is published. Not an obligation today |
| SLCGP (N92-R06) | Not applicable | No grant funds pay for company services |
| Colorado SB26-189 | Applies to AI-001 from 2027-01-01 for AG-44 | Analyzed in P10, not in this control analysis |
| FAR 52.204-21, 52.204-25 | Not applicable | No federal contracts or subcontracts |

## 2. Method
1. **Requirements.** One row per Moderate base control (177), from the repository copy of the SP 800-53 Rev. 5.2.0 catalog and its baseline flags. The Moderate-baseline enhancements for each control are assessed inside the row and named in the `citation` and `sp800_53_controls` columns. Overlay rows were added only where a source sets a value or duty beyond the base control text: 15 CJIS rows, 19 Pub. 1075 rows, 5 program confidentiality rows, 5 DPPA rows, and 3 Florida rows. CJIS, Pub. 1075, the CFR, the U.S. Code, and the Florida Statutes are government works, so short quotes are used.
2. **Sources checked.** CJISSECPOL v6.1 (read from the policy PDF in the FBI file repository); Pub. 1075 Rev. 11-2021 (irs.gov PDF); 42 CFR 431.300-431.307, 7 CFR 272.1, 7 CFR 272.4, and 42 CFR 431.10 (eCFR, 2026-09-23 version); 18 U.S.C. 2721-2725 (govinfo, 2023 edition of the U.S. Code); Fla. Stat. 501.171 (Florida Legislature website).
3. **Crosswalk.** CSF 2.0 subcategories for the base controls come from NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), including those of the control's Moderate enhancements. 43 base controls have no informative reference and show none. Overlay rows are mapped by the author, and the `crosswalk_source` column says so. The `regulatory_driver` column shows which overlay also contains the control; Pub. 1075 section 4 does not include 18 of the 177 base controls (CP-6, CP-7, CP-8, PE-9 to PE-15, PL-10, PL-11, RA-2, RA-9, SC-5, SR-5, SR-8, SR-12).
4. **Evidence and sampling.** Interviews (CTO, COO, Director of Information Security, Director of Contracts and Compliance, VP of Engineering, Director of Cloud Operations, Director of Managed Services, Director of Customer Support, HR Director, Director of Data and AI), configuration exports, HR screening files, contracts, the 2026-03 penetration test, and walkthroughs at both offices. Where a requirement operates many times, a random sample was drawn from a system-generated population, sized with the co-sourced internal audit firm's attribute sampling table (25 items for a frequent control at moderate risk; 5 to 10 for weekly or monthly controls; whole populations where small or high risk):
   - terminations: 25 of 142; transfers: 25 of 96;
   - designated staff: all 186 CJI and all 64 FTI staff against screening records (population test);
   - training records: 25 of 600, plus all 64 FTI staff;
   - changes: 25 of about 1,900 standard changes and 9 of 41 emergency changes;
   - backup job days: 30 of 30 (July 2026); restore tests: 4 of 4 plus the 2025-11 full-tenant test;
   - security incidents: 10 of 31 (2025-2026);
   - vulnerability findings: 40 of 212 high and critical (Q1-Q2 2026); AG-02 critical updates: 10;
   - vendors: all 22 with agency data or system access;
   - contract ends since 2025: 5 of 5;
   - AG-01 case notes in the analytics service: 50 (6 contained FTI).
   Each `evidence` cell names the sample and its result.
5. **Status.** Met, Partially met, Not met, or Not applicable. A control inherited from the FedRAMP-authorized cloud provider is rated Met when the company's use of the service falls inside the provider's authorization. Gap risk uses the P01 scale.

## 3. Results summary
| Family | Controls | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| AC Access Control | 17 | 10 | 6 | 0 | 1 |
| AT Awareness and Training | 4 | 2 | 2 | 0 | 0 |
| AU Audit and Accountability | 11 | 7 | 4 | 0 | 0 |
| CA Assessment, Authorization, and Monitoring | 7 | 4 | 3 | 0 | 0 |
| CM Configuration Management | 12 | 8 | 4 | 0 | 0 |
| CP Contingency Planning | 9 | 3 | 6 | 0 | 0 |
| IA Identification and Authentication | 10 | 5 | 5 | 0 | 0 |
| IR Incident Response | 8 | 3 | 5 | 0 | 0 |
| MA Maintenance | 6 | 4 | 1 | 0 | 1 |
| MP Media Protection | 7 | 4 | 2 | 0 | 1 |
| PE Physical and Environmental Protection | 16 | 15 | 1 | 0 | 0 |
| PL Planning | 6 | 4 | 2 | 0 | 0 |
| PS Personnel Security | 9 | 5 | 4 | 0 | 0 |
| RA Risk Assessment | 6 | 5 | 1 | 0 | 0 |
| SA System and Services Acquisition | 11 | 8 | 3 | 0 | 0 |
| SC System and Communications Protection | 18 | 14 | 3 | 0 | 1 |
| SI System and Information Integrity | 11 | 8 | 3 | 0 | 0 |
| SR Supply Chain Risk Management | 9 | 5 | 4 | 0 | 0 |
| **SP 800-53 Moderate subtotal** | **177** | **114** | **59** | **0** | **4** |
| CJIS Security Policy v6.1 overlay | 15 | 2 | 12 | 0 | 1 |
| IRS Pub. 1075 overlay | 19 | 10 | 7 | 2 | 0 |
| SNAP and Medicaid confidentiality | 5 | 3 | 2 | 0 | 0 |
| Driver's Privacy Protection Act | 5 | 4 | 1 | 0 | 0 |
| Fla. Stat. 501.171 | 3 | 0 | 3 | 0 | 0 |
| **Total rows** | **224** | **133** | **84** | **2** | **5** |

**Gap risk ratings (86 rows Partially met or Not met):** 1 Very High, 29 High, 39 Moderate, 17 Low.

**Reading the results.** The company has a defined program: no base control is Not met, and the cloud landing zone, encryption, backups, change control, and inherited physical controls are solid. The gaps are gaps of scale. Controls that worked for the original customers have not kept up with 600 staff, a managed services line, five regulated customers, and a second state:
- the managed services remote access path (IA-5, AC-17, IA-2);
- screening and access to regulated data (PS-3, PS-6, AC-2, AC-6, CJ-01, CJ-03, PB-01);
- detection of misuse inside the application (AU-2, AU-6, SI-4, PB-18);
- FTI flowing out of the enclave to analytics (PB-09, AC-4);
- recovery speed (CP-2, CP-4, CP-6, CP-10);
- FIPS 140-3 on CJI paths (SC-8, SC-13, IA-7, CJ-11).

The two Not met rows are both Pub. 1075 requirements: the FTI spillage into the analytics service (PB-09) and the lack of browsing detection (PB-18).

## 4. Priority gaps and roadmap
Every Very High and High gap (30 rows) falls into one of the themes below. Each theme is carried into the risk register (P01) and the POA&M (P07).

| Theme | Rows | Action | Owner | Target |
|---|---|---|---|---|
| FTI outside the enclave | PB-09, G-004 | Export stopped 2026-09-08; purge copies; disclose to the AG-01 disclosure officer, who decides on reporting; tag note fields as FTI | Director of Contracts and Compliance | 2026-09-30 |
| Cryptography on CJI paths | G-145, G-148, G-067, CJ-11 | FIPS 140-3 certified modules on the AG-02 and AG-39 connectors; module inventory | Director of Cloud Operations | 2026-09-21 |
| Unscreened staff with CJI or FTI access | G-116, G-119, G-083, CJ-01, CJ-03, PB-01 | Remove access for the 18 staff until screened; screening gate (STD-10) | HR Director | 2026-10-31 |
| Managed services remote access | G-065, G-012, G-062 | Revoke and vault the SYS-10 token and agency credentials; remove the jump path; phishing-resistant keys | Director of Managed Services; Director of Information Security | 2027-01-31 |
| Incident handling across business lines | G-074 | Adopt the P08 runbooks, including SYS-10 containment | Security Operations Manager | 2026-10-31 |
| Log retention | G-031, PB-10 | 7-year archive for FTI enclave application audit logs | Director of Cloud Operations | 2026-12-31 |
| Vendors | G-135, G-173 | Tiered reviews for all 22 vendors (STD-03) | Director of Contracts and Compliance | 2026-12-31 |
| Misuse detection and monitoring | G-023, G-027, G-161, PB-18 | Application audit events and SYS-10 logs to the SIEM; weekly access analytics | Security Operations Manager | 2027-01-31 |
| Access reviews and least privilege | G-002, G-006 | Quarterly tenant reviews; removal at project close and transfer; tenant-scoped support | Director of Information Security | 2027-01-31 |
| Recovery | G-053, G-055, G-056, G-060 | Contingency plan rewrite; document storage in the vault; timed restores; rebuild runbook | Director of Cloud Operations | 2027-03-31 |

**Program roadmap (mid-market sequencing):**
| Quarter | Focus | Exit criterion |
|---|---|---|
| 2026 Q3-Q4 (to 2026-10-31) | Stop the bleeding: FTI export, FIPS cutoff, screening, SYS-10 token | No regulated access without screening; no FTI outside the enclave |
| 2026 Q4 (to 2026-12-31) | Logging, vendors, contingency plan, egress, access reviews | All High P03 rows due in 2026 closed and evidenced |
| 2027 Q1 | Managed services privileged access, misuse analytics, recovery tests | R-001 and R-050 at Moderate or lower; first timed restore within 8 hours |
| 2027 Q2 | Region B failover; GovRAMP Authorized assessment; SOC 2 Type 2 period under way | GovRAMP Authorized by 2027-06-30 |

The full list, with evidence, is in `gap-analysis.csv`.

## 5. Pending and dated changes
- **CJIS FIPS 140-2 cutoff.** CJISSECPOL v6.1 SC-13 states that FIPS 140-2 certificates "will not be acceptable after September 21, 2026." This falls four days after approval; the message-switch connectors are scheduled to switch by then (CJ-11).
- **CJIS zero-cycle end.** [Priority 2] to [Priority 4] requirements become sanctionable in audits after **2027-09-30** (section 1.4). The contracts already require them.
- **New CJISSECPOL versions.** The Security Addendum binds the company to "all subsequent versions." CJ-02 adds a 60-day review of each new version.
- **Pub. 1075.** Rev. 11-2021 remains the edition at irs.gov. Recheck each July before the SSP review.
- **CIRCIA.** Proposed rule only. Recheck applicability when a final rule is published (section 1).
- **Colorado SB26-189.** Effective 2027-01-01; AG-44 go-live 2027-04-05 (P10).
- **SP 800-53.** Release 5.2.0 is current. Future releases will be picked up at the annual SSP review.

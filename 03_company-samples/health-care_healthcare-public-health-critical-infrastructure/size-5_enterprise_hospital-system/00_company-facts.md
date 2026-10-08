# Scenario facts: Cris Santos Company | Healthcare and Public Health | Enterprise

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes and of the Health Care (NAICS 62) samples, which describe physician practices. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; parent of a for-profit hospital system) |
| Business | **For-profit acute-care hospital system**, NAICS 622110 General Medical and Surgical Hospitals. 8 general acute-care hospitals (H-01 to H-08) with 1,970 licensed beds, 3 freestanding emergency departments (departments of H-01, H-02, and H-04), 4 outpatient imaging centers, and an employed physician group with 46 clinic locations. H-01 (640 beds) is the tertiary flagship and a state-designated trauma center |
| Location | Headquartered in Florida. Hospitals in Florida (H-01 to H-05), Georgia (H-06, H-07), and Alabama (H-08). **State law is handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees, including about 4,700 registered nurses and 430 employed physicians. About 2,600 practitioners hold medical staff privileges, and about 1,100 agency and contracted staff work in the hospitals on a typical day |
| Patients | About 102,000 inpatient admissions, 560,000 emergency visits (about 1,530 a day, about 310 of them by ambulance), and 1.7 million outpatient encounters a year. The EHR holds records for about 3.6 million individuals |
| Revenue | About $4.8 billion a year (fictional), about $13.2 million per calendar day. Not small under the SBA standard for NAICS 622110 ($47.0 million; 13 CFR 121.201) |
| Payers | Medicare (about 44% of revenue), Medicaid and Medicaid managed care in three states, Medicare Advantage, and commercial plans. Medicare and Medicaid are federal financial assistance, so Section 1557 applies (45 CFR Part 92) |
| HIPAA status | **Covered entity.** The hospitals, the freestanding EDs (as hospital departments), and the physician group are legally separate subsidiaries under common ownership and are designated as a single **affiliated covered entity** (45 CFR 164.105(b); EV-032). Covered entity status is determined in the intake obligations register (C-HPH-R01): the payer and clearinghouse agreements cover standard electronic transactions (EV-047). Also a business associate for the SL-1 affiliate practices (EV-043) |
| Other federal status | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (EV-047, EV-055). Each hospital is Medicare-participating, so the hospital conditions of participation in 42 CFR Part 482 apply, including emergency preparedness (**42 CFR 482.15**) and medical record services (482.24). The system runs a **unified and integrated emergency preparedness program** under 482.15(f). EMTALA (42 CFR 489.24) applies to every dedicated emergency department, including the freestanding EDs. All 8 hospitals take part in the Medicare Promoting Interoperability Program as eligible hospitals (42 CFR 495.24). Each hospital laboratory holds a CLIA certificate (42 CFR Part 493) |
| 42 CFR Part 2 | **H-03 operates a Part 2 program**: a 24-bed inpatient behavioral health unit with an addiction medicine service that holds itself out as providing substance use disorder treatment (an "identified unit within a general medical facility", 42 CFR 2.11), federally assisted through Medicare participation (2.12(b)(2)(i)). Other hospitals hold Part 2 records only as lawful holders. Applicability is in the obligations register (C-HPH-R06; EV-063) |
| Added at this size | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; multi-state operations; growth by acquisition (H-08 acquired 2025-10-01); two service lines sold to other organizations (P09) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (EV-065): **FTC Health Breach Notification Rule** (16 CFR 318.1 excludes HIPAA covered entities and business associates acting as such). **Group health plan** requirements (164.314(b)): the self-insured employee health plan is a separate covered entity run by the benefits program and is outside these deliverables. **Payment cards**: handled through a hosted payment page and point-to-point encrypted terminals; PCI DSS is a contractual program outside these deliverables. **FAR reporting clauses**: the system holds no federal procurement contracts or subcontracts; Medicare and Medicaid participation are provider agreements |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board of directors (audit committee, risk committee, quality and patient safety committee) | Risk committee oversees cybersecurity risk (Item 106 governance); audit committee oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer (CEO); Chief Financial Officer (CFO) | Jointly accept Very High risk; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer (COO) | Business owner of hospital operations; authorizing official equivalent for the ECIS (P02); chairs the system incident command during major outages |
| Chief Information Security Officer (CISO) | Program owner; chairs the policy governance committee; reports to the CEO and to the board risk committee quarterly |
| Director of Security Operations | HIPAA **Security Officer** for the affiliated covered entity (45 CFR 164.308(a)(2)); runs the 24x7 SOC |
| Chief Privacy Officer | HIPAA **Privacy Officer**; breach determinations |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Medical Information Officer | Clinical systems and clinical decision support; chairs the AI governance committee |
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control providers) |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee |
| General Counsel | Chairs the disclosure committee |
| GRC team (10), Security Operations Center (24x7, in-house with managed security service provider overflow), Internal Audit (IT audit team of 5) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Notes |
|---|---|---|
| SYS-01 | Enterprise EHR (commercial EHR, customer-managed). Production in data center DC-1 (Florida), hot standby in DC-2 (Georgia) | Single instance for H-01 to H-07, the freestanding EDs, the physician group, and SL-1 affiliate practices. Includes ED, inpatient, surgery, pharmacy and barcode medication administration, laboratory, radiology, and revenue cycle modules. H-08 migrates to it on 2027-03-01 |
| SYS-02 | Identity platform (directory, SSO with badge tap at clinical workstations, MFA, privileged access management, identity governance) | Covers about 19,500 workforce identities. H-08 still uses its own legacy directory (EV-001, EV-007) |
| SYS-03 | Data centers: DC-1 (system-owned, inland Florida) and DC-2 (colocation, Georgia) | EHR, integration engine, enterprise imaging (PACS), network core |
| SYS-04 | Multi-cloud estate: Cloud provider A and Cloud provider B (vendor-agnostic) | Cloud A: patient portal and FHIR API front end, immutable backup vault, isolated recovery environment (in build; EV-018, EV-024). Cloud B: data and analytics platform, tele-critical care platform (SL-2), AI services |
| SYS-05 | Enterprise network (SD-WAN, hospital campus networks, NAC) | NAC enforced at H-01 to H-05 only (EV-013) |
| SYS-06 | Endpoints and medical devices: about 26,000 endpoints; about 41,000 networked medical devices | Device inventory about 88% complete; about 2,600 devices run unsupported operating systems (EV-012) |
| SYS-07 | Building and clinical operational technology (OT) at 8 hospitals | Building automation, medical gas alarms, nurse call, pneumatic tube, generator monitoring. OT segmented at 6 of 8 hospitals (EV-017) |
| SYS-08 | Enterprise imaging (PACS and vendor-neutral archive) | DC-1 primary, DC-2 replica |
| SYS-09 | ERP, payroll, and supply chain (SaaS) | SOX-relevant; IT general controls tested annually (EV-031) |
| SYS-10 | Third parties: about 1,500 vendors, 430 with PHI | Tiered third-party risk program; one primary clearinghouse carries about 80% of claims (EV-038, EV-041) |
| SYS-11 | AI portfolio (12 use cases) | Governed by the AI governance committee formed in 2025 (EV-076, EV-095) |
| SYS-12 | Unified communications (VoIP, secure clinical messaging, mass notification) | EMS radio and analog lines in each ED are the non-network fallback |
| SYS-13 | H-08 legacy EHR (vendor-hosted) and legacy directory | Until the 2027-03-01 migration |
| SYS-14 | Tele-critical care platform (SL-2) | Cloud B with a vendor tele-ICU application; virtual care center at H-01 |
| SYS-15 | Sepsis prediction model | The EHR vendor's predictive decision support intervention, configured by the system and live at H-01 to H-07 |

**SSP system (P02):** the *Enterprise Clinical Information System (ECIS)*: the system's instance of SYS-01 in DC-1 and DC-2, including its integration engine, clinical device integration, business continuity access (downtime) devices, the patient portal and FHIR API front end on Cloud provider A, and the SYS-15 configuration, categorized High for integrity and availability and inheriting common controls from the enterprise platform; H-08's legacy EHR (SYS-13) is outside the boundary until migration.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. At this size the sources are enterprise systems of record across the hospitals and business units, prior Internal Audit and SOX workpapers, regulator correspondence, and board and committee records.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv), reviewed by the General Counsel's office with outside securities counsel.
- **Gaps against the HIPAA Security Rule and the other applicable rules** are judged in the gap analysis (P03), and **whether controls work** is tested by Internal Audit in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 | The ECIS, categorized High (integrity and availability); High baseline with common control provider inheritance |
| P03 | HIPAA Security Rule (primary) plus every applicable enterprise obligation: Breach Notification Rule, Privacy Rule safeguards, affiliated covered entity designation, SEC Item 1.05 and Item 106, CMS emergency preparedness (482.15, cyber-relevant parts and the unified program), medical record services (482.24), EMTALA (489.24) for diversion and transfers, Promoting Interoperability (495.24), Section 1557 (92.210), CLIA (493.1291), 42 CFR Part 2 (2.16), FTC HBNR (screened out), and state breach laws. The voluntary HHS HPH Cybersecurity Performance Goals are a self-benchmark (extra file `cpg-benchmark.csv`) |
| P08 | Ransomware forcing EHR downtime and ambulance diversion across several hospitals, with an **SEC materiality assessment and Form 8-K Item 1.05** step, EMTALA-compliant diversion, and multi-state breach notification |
| P09 | SOC 2 Type 2 readiness across two service lines sold to other organizations: SL-1 affiliate EHR hosting and SL-2 tele-critical care |
| P10 | Enterprise AI portfolio (12 use cases) with the AI governance committee operating model, and a full assessment of the sepsis prediction model (SYS-15). The registry default fits this business, so it is kept |
| Cloud | Multi-cloud (vendor-agnostic) plus two data centers, with common controls |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-04-06 to 2026-04-30 | Intake: evidence requests, exports from the enterprise systems of record across the hospitals and business units, prior Internal Audit and SOX workpapers, inventories, obligations register (reviewed by counsel) |
| 2026-05-04 to 2026-06-26 | Enterprise BIA interviews and dependency review; enterprise risk analysis and regulatory gap analysis fieldwork (gap analysis evidence sampling completed 2026-07-10) |
| 2026-06-01 to 2026-06-26 | 2026 annual revision of POL-01 to POL-05 drafted from the intake evidence and early risk and gap results |
| 2026-06-22 to 2026-08-07 | Control assessment of the ECIS (Internal Audit): operating tests of controls in force under the existing policy set; design review of the draft 2026 revisions |
| 2026-07-20 to 2026-08-14 | AI portfolio review and sepsis model local validation (P10) |
| 2026-08-24 | Executive risk committee approves the register, POL-02 to POL-05, and treatment plans |
| 2026-09-15 | Results to the board risk committee and audit committee; the board risk committee approves POL-01. The 2026 policy set takes effect 2026-10-01 |
| 2027-03 (planned) | Internal Audit follow-up: operating effectiveness of the controls the 2026 policy revisions and POA&M items introduced, after at least one quarter of operation |

## 7. Facts added for the Phase 5 deliverables
These facts were added while building the deliverables. They do not change sections 1-6. Where a fact describes the state of a control or a record, the evidence ID behind it is given.

**Registry defaults.** All three registry defaults fit a hospital system and are kept: the primary system (hospital EHR and clinical systems, documented as the ECIS), the P08 incident (ransomware forcing EHR downtime and ambulance diversion), and the P10 use case (the sepsis prediction model).

**Sites and beds.** 61 sites plus DC-1, DC-2, and corporate headquarters: 8 hospitals, 3 freestanding EDs, 46 clinics, 4 imaging centers. Licensed beds: H-01 640, H-02 310, H-03 280, H-04 220, H-05 120 (Florida); H-06 190, H-07 110 (Georgia); H-08 100 (Alabama). No hospital has a transplant program (42 CFR 482.15(g) does not apply). The system owns no ambulances; its EDs receive EMS traffic from 9 counties (EV-052, EV-055).

**Volumes.** About 1,600 occupied beds on a typical day, 1,530 ED visits and 310 ambulance arrivals a day, about 290 surgical and interventional cases a day, about 21,000 laboratory results a day, about 6,800 imaging studies a day, about 260 inbound transfers a day through the System Transfer and Command Center, and about 5,200 clinic visits a day. About 1.1 million active patient portal users. Revenue of about $13.2 million per calendar day (EV-053, EV-054).

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Nursing Officer; Chief Medical Officer | Clinical downtime leads; owners of inpatient (BP-02) and emergency (BP-01) processes |
| Chief Compliance Officer; Director of Civil Rights Compliance | Regulatory compliance; the Director is the Section 1557 Coordinator (45 CFR 92.7) |
| Chief Human Resources Officer; Controller | Workforce lifecycle and training; SOX and disclosure committee member |
| Vice President, Emergency Management | Unified emergency preparedness program (482.15(f)); System Transfer and Command Center |
| Hospital presidents (8) | Hospital incident commanders; decide IT-outage diversion with the ED medical director and house supervisor |
| Vice President, Clinical Applications | ECIS system owner |
| EHR Technical Director; Integration Services Manager | ECIS administration and recovery; integration engine |
| Directors of Identity and Access Management, Third-Party Risk Management, Cloud Platform Engineering, Network Engineering, Data Center Operations, Endpoint Engineering, Clinical Engineering, and Facilities Engineering | Common control providers and device and OT owners |
| Vice President, Facilities | Physical security of hospitals |
| Vice Presidents of Revenue Cycle, Laboratory Services, Pharmacy Services, Supply Chain, and Digital Health; President, Physician Group | Process owners in the BIA |
| Vice President, Behavioral Health | Part 2 program director for H-03 |
| Vice President, Integration Management Office | H-08 integration and conversion |
| Vice President, Affiliate Services; Vice President, Virtual Care | SL-1 and SL-2 owners |
| Chief Data and Analytics Officer | Analytics platform and in-house models |
| Director of Health Information Management | Medical records, release of information, downtime back-entry |
| Vice President, Corporate Communications; Vice President, Investor Relations | Media and investor communications |
| Patient safety officer | Patient safety events, including AI-related harm |

**Disclosure committee (P08).** General Counsel (chair), CFO, Controller, COO (joined 2026), CISO, Chief Privacy Officer, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. The materiality playbook was exercised in a 2025 tabletop (EV-033).

**HIPAA designations.** The affiliated covered entity designation and the Security Officer designation were updated to include H-08 on 2025-11-14 (EV-032).

**ECIS details (P02, P07).** About 60 application and presentation servers, a 4-node integration engine cluster per data center with about 640 interfaces, 16 clinical device integration gateways, and about 900 BCA downtime computers (EV-012, EV-059, EV-060). About 19,000 workforce users (EV-009). Failover to DC-2 took 2.6 hours on 2026-03-21; a full restore from the immutable vault took 41 hours on 2026-04-18 (EV-023) against a 24-hour cyber recovery target set in the BIA. A 5-hour network outage at H-06 on 2026-01-22 stopped EHR access there (EV-026). About 1,150 service accounts, about 265 (23%) unvaulted, and 31 integration engine passwords older than 2 years (EV-003). P07 testing found default vendor passwords on 2 of the 16 device integration gateways (EV-IA-5; reported 2026-07-29, changed 2026-08-05). The HL7 MLLP segment inside the data center runs under exception EXC-2026-031 (EV-094).

**H-08.** Acquired 2025-10-01; about 640 workforce and about 1,100 endpoints, about 330 without EDR and about 160 unencrypted (EV-010, EV-011). Joined the unified emergency program in 2026-01. The legacy EHR vendor backs up every 4 hours and its contract states a 24-hour RTO (EV-056).

**Claims routing.** Primary clearinghouse about 80% of claims (about $74 million a week, about $10.5 million a day); secondary clearinghouse about 12%; direct payer connections about 8% (EV-041).

**Service lines (P09).** SL-1: about 70 practices and 1,450 users; contract value about $31 million a year; 99.9% monthly availability and 10-day breach notice in hosting agreements; SOC 2 Type 1 (Security, Availability, Confidentiality) as of 2025-12-31. SL-2: 14 partner hospitals including 6 critical access hospitals, about 210 monitored ICU beds, a virtual care center at H-01 with no alternate site, 15-minute service interruption notice; clinicians at 4 partner hospitals sign in with local application accounts without MFA (EV-043, EV-044, EV-045).

**Program facts used in the gap analysis.** 1,500 vendors (430 with PHI; 41 tier-1 and tier-2 reassessments overdue; EV-038) and 42 staffing agency contracts (EV-006); 388 security incidents and 41 privacy incidents in the first half of 2026 (EV-091); 37 sanctions in 2025 (EV-037); 6 notified breaches from 2024 to 2026 (EV-091); 1,140 Part 2 encounters at H-03 in the first half of 2026 (EV-092); 312 analytics users (71 with identified-data access not recertified; EV-085); outside counsel's state breach matrix updated 2026-03 (Alabama added; EV-066). Exercises: mass-casualty tabletop 2026-02-10 (EV-051), enterprise ransomware tabletop 2026-02-26 (H-01 and H-02; EV-035), community hurricane exercise 2026-05-12 (EV-089); a multi-hospital downtime, diversion, and disclosure committee exercise is planned for 2026-11-18. Current policy exceptions: EXC-2026-027, -029, -031, -034, -036 (EV-094).

**Not applicable, confirmed.** The Florida Digital Bill of Rights does not apply: the system exceeds $1 billion in revenue but does not meet any of the three additional tests in Fla. Stat. 501.702 (obligations register FL-501.702; EV-053, EV-065). Recording consent for the AI scribe uses all-party prior consent in all three states (Florida worked example: Fla. Stat. 934.03(2)(d); obligations register FL-934.03).

**AI portfolio (P10).** 12 use cases (AI-001 to AI-012); 8 reviewed by the AI governance committee (EV-076, EV-095). Sepsis model version 2 went live 2026-04-14 (EV-078). Local validation on 41,200 adult inpatient encounters at H-01 to H-07 (2026-04-14 to 2026-07-31): 2,480 sepsis cases, 71% sensitivity (version 1: 76%), 25% PPV, alert response within 1 hour 64%; flags for adults 18-64 (63%) and Black patients (64%). Universal nurse sepsis screening runs at H-01 to H-05. Treatment funding for 2026 Q4 to 2027 Q2 is about $7.4 million.

# Scenario facts: Cris Santos Company | Healthcare and Public Health | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes and of the Health Care (NAICS 62) samples, which describe physician practices. Where a fact comes from a regulation or standard, the citation is given.

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
| HIPAA status | **Covered entity.** The hospitals, the freestanding EDs (as hospital departments), and the physician group are legally separate subsidiaries under common ownership and are designated as a single **affiliated covered entity** (45 CFR 164.105(b)) |
| Other federal status | Each hospital is Medicare-participating, so the hospital conditions of participation in 42 CFR Part 482 apply, including emergency preparedness (**42 CFR 482.15**) and medical record services (482.24). The system runs a **unified and integrated emergency preparedness program** under 482.15(f). EMTALA (42 CFR 489.24) applies to every dedicated emergency department, including the freestanding EDs. All 8 hospitals take part in the Medicare Promoting Interoperability Program as eligible hospitals (42 CFR 495.24). Each hospital laboratory holds a CLIA certificate (42 CFR Part 493) |
| 42 CFR Part 2 | **H-03 operates a Part 2 program**: a 24-bed inpatient behavioral health unit with an addiction medicine service that holds itself out as providing substance use disorder treatment (an "identified unit within a general medical facility", 42 CFR 2.11), federally assisted through Medicare participation (2.12(b)(2)(i)). Other hospitals hold Part 2 records only as lawful holders |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; multi-state operations; growth by acquisition (H-08 acquired 2025-10-01); two service lines sold to other organizations (P09) |
| Not in scope | **FTC Health Breach Notification Rule** (16 CFR 318.1 excludes HIPAA covered entities and business associates acting as such). **Group health plan** requirements (164.314(b)): the self-insured employee health plan is a separate covered entity run by the benefits program and is outside these deliverables. **Payment cards**: handled through a hosted payment page and point-to-point encrypted terminals; PCI DSS is a contractual program outside these deliverables. **FAR reporting clauses**: the system holds no federal procurement contracts or subcontracts; Medicare and Medicaid participation are provider agreements |

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

| ID | System | Notes |
|---|---|---|
| SYS-01 | Enterprise EHR (commercial EHR, customer-managed). Production in data center DC-1 (Florida), hot standby in DC-2 (Georgia) | Single instance for H-01 to H-07, the freestanding EDs, the physician group, and SL-1 affiliate practices. Includes ED, inpatient, surgery, pharmacy and barcode medication administration, laboratory, radiology, and revenue cycle modules. H-08 migrates to it on 2027-03-01 |
| SYS-02 | Identity platform (directory, SSO with badge tap at clinical workstations, MFA, privileged access management, identity governance) | Covers about 19,500 workforce identities. H-08 still uses its own legacy directory |
| SYS-03 | Data centers: DC-1 (system-owned, inland Florida) and DC-2 (colocation, Georgia) | EHR, integration engine, enterprise imaging (PACS), network core |
| SYS-04 | Multi-cloud estate: Cloud provider A and Cloud provider B (vendor-agnostic) | Cloud A: patient portal and FHIR API front end, immutable backup vault, isolated recovery environment (in build). Cloud B: data and analytics platform, tele-critical care platform (SL-2), AI services |
| SYS-05 | Enterprise network (SD-WAN, hospital campus networks, NAC) | NAC enforced at H-01 to H-05 only |
| SYS-06 | Endpoints and medical devices: about 26,000 endpoints; about 41,000 networked medical devices | Device inventory about 88% complete; about 2,600 devices run unsupported operating systems |
| SYS-07 | Building and clinical operational technology (OT) at 8 hospitals | Building automation, medical gas alarms, nurse call, pneumatic tube, generator monitoring. OT segmented at 6 of 8 hospitals |
| SYS-08 | Enterprise imaging (PACS and vendor-neutral archive) | DC-1 primary, DC-2 replica |
| SYS-09 | ERP, payroll, and supply chain (SaaS) | SOX-relevant; IT general controls tested annually |
| SYS-10 | Third parties: about 1,500 vendors, 430 with PHI | Tiered third-party risk program; one primary clearinghouse carries about 80% of claims |
| SYS-11 | AI portfolio (12 use cases) | Governed by the AI governance committee formed in 2025 |
| SYS-12 | Unified communications (VoIP, secure clinical messaging, mass notification) | EMS radio and analog lines in each ED are the non-network fallback |
| SYS-13 | H-08 legacy EHR (vendor-hosted) and legacy directory | Until the 2027-03-01 migration |
| SYS-14 | Tele-critical care platform (SL-2) | Cloud B with a vendor tele-ICU application; virtual care center at H-01 |
| SYS-15 | Sepsis prediction model | The EHR vendor's predictive decision support intervention, configured by the system and live at H-01 to H-07 |

**SSP system (P02):** the *Enterprise Clinical Information System (ECIS)*: the system's instance of SYS-01 in DC-1 and DC-2, including its integration engine, clinical device integration, business continuity access (downtime) devices, the patient portal and FHIR API front end on Cloud provider A, and the SYS-15 configuration, categorized High for integrity and availability and inheriting common controls from the enterprise platform; H-08's legacy EHR (SYS-13) is outside the boundary until migration.

## 4. Current security posture: mature, with residual gaps

**In place today:**
- A mature security program aligned to CSF 2.0, with an annual risk analysis integrated with ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and an exceptions process
- 24x7 SOC with EDR on 97% of endpoints (excluding H-08), SIEM, and threat intelligence
- Privileged access management and quarterly access certification
- Immutable backups in a separate cloud account with an offline copy at DC-2
- Annual EHR failover test from DC-1 to DC-2
- Business continuity access (BCA) downtime computers on every nursing unit and in every ED
- Tiered vendor reviews
- A unified emergency preparedness program across all 8 hospitals (482.15(f)) with two exercises a year
- SEC Item 106 disclosure in the Form 10-K

**Residual gaps found in the 2026 assessments:**
1. **Acquired hospital H-08.** Still on its legacy EHR and legacy directory with a flat network, EDR on about 70% of its endpoints, and no feeds to the SIEM. EHR migration is due 2027-03-01.
2. **Cyber recovery time.** EHR failover to DC-2 works (2.6 hours in the 2026-03-21 test), but a ransomware event that also reaches DC-2 requires restoring from the immutable vault. The 2026-04-18 full restore test took 41 hours against a 24-hour cyber recovery target, and the isolated recovery environment is not finished.
3. **Ambulance diversion and downtime at scale.** IT-outage diversion criteria exist only at H-01. The unified emergency plan's risk assessment does not score a multi-hospital cyberattack, and no exercise has tested more than one hospital in EHR downtime at once.
4. **Medical devices.** The inventory is about 88% complete, about 2,600 devices run unsupported operating systems, and NAC is enforced at only 5 of 8 hospitals.
5. **Third-party concentration.** One clearinghouse carries about 80% of claims and the manual fallback is untested. Of the 430 vendors with PHI, 41 tier-1 and tier-2 vendors are overdue for reassessment.
6. **AI.** 12 AI use cases, 8 reviewed by the AI governance committee. The sepsis model's vendor version 2 went live on 2026-04-14 without local revalidation, and the Section 1557 inventory of non-automated tools is incomplete.
7. **Disclosure readiness.** The materiality playbook was exercised in 2025, but its quantitative thresholds were not updated after the H-08 acquisition, and the disclosure committee has never rehearsed together with hospital incident command.
8. **Part 2 program at H-03.** Part 2 records are not consistently segmented in the EHR, and the 2.16 security policies were not updated for the 2024 rule (compliance date 2026-02-16).
9. **Service and interface accounts.** About 1,150 service accounts exist; 23% are not vaulted in PAM, including legacy integration engine accounts.

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
| 2026-05-04 to 2026-06-26 | Enterprise risk analysis and regulatory gap analysis fieldwork (evidence sampling completed 2026-07-10) |
| 2026-06-22 to 2026-08-07 | Control assessment of the ECIS (Internal Audit) |
| 2026-07-20 to 2026-08-14 | AI portfolio review and sepsis model local validation (P10) |
| 2026-08-24 | Executive risk committee approves the register, policies, and treatment plans |
| 2026-09-15 | Results to the board risk committee and audit committee |

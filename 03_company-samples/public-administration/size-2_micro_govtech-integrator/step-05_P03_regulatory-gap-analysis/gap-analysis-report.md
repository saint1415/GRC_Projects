# Regulatory Gap Analysis: Cris Santos Company | Public Administration | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator, NAICS 541512) |
| Tier / Vertical | Micro / Public Administration |
| System | Hosted Case Management Service (HCMS), as bounded in the SSP (P02), plus the company's access to the revenue agency's virtual desktop for the Pub. 1075 rows |
| Primary requirement set | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline, as selected in NIST SP 800-53B, required by the AC-02, AC-03, and AC-04 contracts |
| Secondary overlays | FBI CJIS Security Policy v6.1 (06/25/2026) for AC-01 (N92-R02); IRS Publication 1075 (Rev. 11-2021) for the SC-01 subcontract (N92-R01) |
| Assessment dates | 2026-07-27 to 2026-08-07. Statuses reflect the end of fieldwork; actions taken since are noted in the remediation column. CJ-11 was updated 2026-08-19 with a P07 test result |
| Assessor | Operations Manager (Security and Compliance Officer) with the Lead Platform Engineer and the MSP lead technician |
| Approved | 2026-08-31 by the owner |

## 1. Applicability
The company is a private contractor, not an agency. Only two Florida statutes bind it directly (Fla. Stat. 501.171 and 119.0701). Every other rule below reaches it **through a contract with a customer that is bound**. So this analysis starts with the contracts, then checks whether each rule applies at a company of 7 people.

### 1.1 SP 800-53 Rev. 5 Moderate: applies by contract, with no size exemption
SP 800-53 is a federal standard, not a law for private companies. The AC-02 county contract requires the hosted service to meet the Moderate baseline, and the two city contracts (AC-03, AC-04) copy that clause. The contracts have no size threshold, and neither does the baseline. The Moderate baseline has **177 base controls and 110 enhancements**. Each `G-` row below is one base control; its Moderate enhancements are assessed inside the row and named in the `citation` column. Because the company builds on a FedRAMP Moderate authorized platform, many rows are **Met by inheritance**, which is how a 7-person company can carry a Moderate baseline at all.

### 1.2 FBI CJIS Security Policy: applies to AC-01 work through the Security Addendum
- **Legal path.** 28 CFR 20.33(a)(7) allows criminal history record information to go "to private contractors pursuant to a specific agreement" with a criminal justice agency. The agreement "must incorporate a security addendum approved by the Attorney General," whose authority the FBI Director exercises. The AC-01 contract incorporates the CJIS Security Addendum.
- **What the Addendum requires.** The contractor must maintain a security program consistent with the CJIS Security Policy in effect when the contract was executed and all subsequent versions (Addendum sec. 3.01). Each contractor employee with access signs the certification page, which the agency keeps (sec. 2.01; CJISSECPOL v6.1 SA-9).
- **Version.** CJISSECPOL **v6.1, dated 06/25/2026**, approved by the CJIS Advisory Policy Board (supersedes v6.0 of 12/27/2024).
- **No size threshold.** All 177 Moderate base controls appear in CJISSECPOL v6.1, so the `regulatory_driver` column names the CJIS control on every `G-` row. Where CJIS sets a value or duty beyond the base control text, a `CJ-` row was added (12 rows).
- **Scope.** The AC-01 workspace, SYS-02 (which pulls and stores the sheriff's files), the helpdesk where sheriff users send screenshots, the laptops that administer them, and the 5 staff who could reach AC-01 data. AC-01 and the state CJIS Systems Agency audit through the contract.

### 1.3 IRS Publication 1075: applies to the SC-01 subcontract through Exhibit 7
- **Legal path.** The revenue agency receives FTI from the IRS. Exhibit 7 of Pub. 1075 says no work involving FTI may be subcontracted "without the prior written approval of the IRS" (I(8)), that approved subcontracts carry the Exhibit 7 terms unchanged (I(9)), and that the subcontractor takes on the same obligations as the prime (I(10)-(11)). The agency's notification to the IRS Office of Safeguards names the company, and the prime flowed Exhibit 7 down unchanged.
- **Edition.** Rev. 11-2021 is the edition served at irs.gov/pub/irs-pdf/p1075.pdf.
- **Scope at this size.** No company system is authorized to receive, store, or transmit FTI. The Integration Consultant and the Lead Platform Engineer see FTI only inside the agency's virtual desktop, from 2 company laptops the agency CISO approved (Pub. 1075 sec. 4, AC-20 IRS-defined requirement; sec. 3.3.7). So the 10 `PB-` rows cover people, devices, home work sites, spillage, and reporting, not a company FTI system. The Pub. 1075 control catalog in section 4 is **not** applied to the HCMS, because FTI is barred from it.

### 1.4 Florida statutes
| Statute | Decision | Why |
|---|---|---|
| Fla. Stat. 501.171 | **Applies directly** | The company is a "third-party agent", an entity contracted "to maintain, store, or process personal information" for a covered entity or governmental entity (501.171(1)(h)). It must "take reasonable measures to protect and secure data in electronic form containing personal information" (501.171(2)) and must notify the agency of a breach "no later than 10 days following the determination of the breach of security or reason to believe the breach occurred," with all the information the agency needs for its own notices (501.171(6)(a)). Tested through the IR rows and in P08 |
| Fla. Stat. 119.0701 | **Applies directly, through each contract** | Each public agency contract for services must require the contractor to keep and maintain public records, provide them on the custodian's request, keep exempt records confidential, and at contract end transfer all records at no cost or keep them under the retention rules (119.0701(2)(b)). The company has no written procedure for this (P01 R-023; SI-12 row) |
| Fla. Stat. 282.3185 and 282.3186 | Customer duties the company must support | Counties and municipalities must report ransomware incidents within 12 hours of discovery (282.3185(5)(b)) and send an after-action report within 1 week of remediation (282.3185(6)). State agencies, counties, and municipalities may not pay a ransom (282.3186). These bind AC-02, AC-03, AC-04 and the revenue agency, not the company, but the company must give them facts in time (P08). Whether 282.3185 reaches a sheriff's office is for AC-01 and its county to decide |
| Rule 60GG-2, F.A.C. | Not applied | Binds state agencies. The revenue agency applies it to the prime; the company's subcontract carries only the Pub. 1075 terms. The county and city customers are not state agencies |

### 1.5 Other rules considered
| Rule | Decision | Why |
|---|---|---|
| HIPAA Security Rule (N92-R03) | Not applicable | No customer has designated the company a business associate; the county assistance program is not a health plan or provider |
| Medicaid and SNAP confidentiality (N92-R04; 7 CFR 272.1(c)) | Not applicable | The AC-02 program is county-funded; it is not Medicaid, SNAP, or TANF |
| Driver's Privacy Protection Act (N92-R05) | Not applicable | Driver license numbers in city files come from complainants, not from motor vehicle records |
| SLCGP (N92-R06) | Not applicable | No grant funds pay for the company's services |
| CIRCIA (N92-R07) | Proposed only | No final rule as of 2026-09-25. Not treated as an obligation |
| GovRAMP (N92-R08) | Voluntary | A verification program, not law. The platform vendor is listed as verified; the company is not. Considered in P09 |
| FAR 52.204-21 and 52.204-25 | Not applicable | No federal contracts or subcontracts |

## 2. Method
1. **Requirements.** One row per Moderate base control (177), from the repository copy of the SP 800-53 Rev. 5.2.0 catalog and its baseline flags. Overlay rows were added only where CJISSECPOL v6.1 or Pub. 1075 sets a value or duty beyond the base control text. Both are U.S. government works, so short quotes are used.
2. **Crosswalk.** CSF 2.0 subcategories come from NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). 43 base controls have no informative reference and show "None". Overlay rows are mapped by the author, and the `crosswalk_source` column says so.
3. **Documentary evidence.** Each status rests on a named document or record: the platform user, role, and tenant settings exports; the platform vendor's FedRAMP listing, SOC 2 report, service description, and August 2026 letters; the SYS-02 security group, package, log, and crypto policy outputs; the MSP's monthly report, encryption report, and antivirus export; the AC-01 contract, screening confirmations, and training records; the SC-01 subcontract, the agency CISO's device approval, and the agency training certificates; and the 2026-07-29 data inventory notes. Interviews covered all 7 staff and the MSP lead technician; the office was walked through on 2026-08-04.
4. **Status.** Met, Partially met, Not met, or Not applicable, **as of the end of fieldwork (2026-08-07)**. A control inherited from the FedRAMP Moderate authorized platform or IaaS service is rated Met when the company's use falls inside the provider's authorization. Gap risk uses the P01 scale.

## 3. Results summary
| Family | Controls | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| AC Access Control | 17 | 4 | 11 | 2 | 0 |
| AT Awareness and Training | 4 | 0 | 3 | 1 | 0 |
| AU Audit and Accountability | 11 | 4 | 3 | 4 | 0 |
| CA Assessment, Authorization, and Monitoring | 7 | 0 | 2 | 5 | 0 |
| CM Configuration Management | 12 | 0 | 8 | 4 | 0 |
| CP Contingency Planning | 9 | 0 | 5 | 4 | 0 |
| IA Identification and Authentication | 10 | 4 | 5 | 1 | 0 |
| IR Incident Response | 8 | 0 | 2 | 6 | 0 |
| MA Maintenance | 6 | 1 | 3 | 2 | 0 |
| MP Media Protection | 7 | 2 | 4 | 1 | 0 |
| PE Physical and Environmental Protection | 16 | 14 | 1 | 1 | 0 |
| PL Planning | 6 | 1 | 1 | 4 | 0 |
| PS Personnel Security | 9 | 0 | 5 | 4 | 0 |
| RA Risk Assessment | 6 | 1 | 3 | 2 | 0 |
| SA System and Services Acquisition | 11 | 1 | 8 | 2 | 0 |
| SC System and Communications Protection | 18 | 12 | 5 | 1 | 0 |
| SI System and Information Integrity | 11 | 3 | 6 | 2 | 0 |
| SR Supply Chain Risk Management | 9 | 1 | 1 | 6 | 1 |
| **SP 800-53 Moderate subtotal** | **177** | **48** | **76** | **52** | **1** |
| CJIS Security Policy v6.1 overlay (AC-01) | 12 | 1 | 8 | 2 | 1 |
| IRS Pub. 1075 overlay (SC-01) | 10 | 3 | 6 | 1 | 0 |
| **Total rows** | **199** | **52** | **90** | **55** | **2** |

Of the 145 rows with a gap, 21 are rated High, 48 Moderate, and 76 Low. The one Not applicable control row is SR-10 (the company buys no system components except standard laptops, which the MSP sources new).

**What the numbers say.** The inherited rows score best: 14 of 16 physical and environmental controls and 12 of 18 system and communications protection controls are Met because the platform vendor and IaaS provider carry them. The company's own layer scores worst: no policies, plan, or procedures existed (every `-1` control is Not met), incident response and contingency planning are absent, and personnel screening and supplier oversight lag behind the CJI and FTI access the company already has.

## 4. Priority gaps
The 21 High gaps fall into six themes. Each theme is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

| Theme | Rows | Action | Owner | Target |
|---|---|---|---|---|
| Screening and agreements for staff with CJI or FTI access | G-116, CJ-01, CJ-03 | Support role kept out of AC-01 until fingerprint-based checks and Addendum certification are done; screening gate in onboarding | Operations Manager | 2026-10-15 |
| FTI reaching company systems and unapproved devices | PB-05, PB-06 | Spill reported and purged; no-FTI rule; approved-laptop check; Lead Platform Engineer suspended from SC-01 until recertified | Operations Manager | 2026-10-31 |
| Incident reporting to agencies and the prime | G-074, G-076, G-078, CJ-09 | POL-03, P08 runbook and notification matrix; staff briefing on the 1-hour rule; tabletop | Operations Manager | 2026-11-30 |
| Recovery from ransomware or deletion | G-055, G-059 | Write-once exports in a separate account every 4 hours; first restore test; contingency plan | Lead Platform Engineer | 2026-11-30 |
| Logging, monitoring, and the one server | G-031, G-159, G-161, CJ-08 | 1-year write-once log archive; alerts on administrator sign-ins and bulk exports; automatic patching of SYS-02 | Lead Platform Engineer | 2026-10-31 |
| Cryptography, access, and suppliers | G-002, G-006, G-135, G-148, G-173, CJ-10 | FIPS 140-3 mode on SYS-02 before 2026-09-21; separate administrator accounts and quarterly access reviews; supplier reviews of the platform vendor, MSP, helpdesk, and AI add-on | Lead Platform Engineer; Operations Manager | 2026-09-18 (FIPS); 2026-12-31 (others) |

The full list, with evidence, is in `gap-analysis.csv`.

## 5. Remediation plan
The plan fits a 7-person company: most actions are tenant settings, one-page procedures, MSP tasks, or contract terms. The Lead Platform Engineer does the technical work; the Operations Manager does the paperwork and agency contacts. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Stop the bleeding | 2026-09-30 | Support role scoped (done 2026-08-12); Lead Platform Engineer suspended from SC-01 (done 2026-08-12) and recertified; FIPS 140-3 mode on SYS-02 (2026-09-18); MFA for AC-04; CJIS lockout value; platform idle timeout; staff briefing on POL-03; inventory of devices and agency data; CHRI working files deleted after each load; laptops re-encrypted with 256-bit keys | G-007 (AC-7), G-009 (AC-11), G-068 (IA-8), G-148 (SC-13), G-047 (CM-8), G-051 (CM-12), G-072 (IR-2), G-076 (IR-6), G-115 (PS-2), G-156 (SC-28), G-167 (SI-12), G-088 (MP-4), CJ-06, CJ-09, CJ-10, CJ-11, PB-01, PB-02, PB-06 |
| 2. See and keep | 2026-10-31 | 1-year write-once log archive; monthly log review; administrator and bulk-export alerts; separate administrator accounts; change tickets; automatic patching and scanning of SYS-02; helpdesk attachments blocked; first restore test; training with phishing exercises; no-FTI rule and suite scan | G-002 (AC-2), G-006 (AC-6), G-008 (AC-8), G-023 (AU-2), G-026 (AU-5), G-027 (AU-6), G-030 (AU-9), G-031 (AU-11), G-032 (AU-12), G-042 (CM-3), G-044 (CM-5), G-019 (AT-2), G-055 (CP-4), G-126 (RA-5), G-159 (SI-2), G-161 (SI-4), G-116 (PS-3), G-119 (PS-6), CJ-01, CJ-03, CJ-04, CJ-08, PB-05, PB-07 |
| 3. Recover | 2026-11-30 | Write-once exports in a separate account every 4 hours; contingency plan; scripted SYS-02 rebuild; tabletop with the MSP and AC-01 | G-053 (CP-2), G-056 (CP-6), G-059 (CP-9), G-060 (CP-10), G-041 (CM-2), G-073 (IR-3) |
| 4. Contracts and suppliers | 2026-12-31 | MSP contract amendment (incident notice, MFA evidence, named technicians, recovery commitment); supplier reviews; SSH through the MFA-protected session service; outbound allow-list; contract-end and public records checklist | G-004 (AC-4), G-012 (AC-17), G-062 (IA-2), G-144 (SC-7), G-081 (MA-3), G-082 (MA-4), G-083 (MA-5), G-120 (PS-7), G-135 (SA-9), G-173 (SR-6), G-174 (SR-8), CJ-05, PB-09 |
| 5. Annual cycle | 2027-07-31 to 2027-08-31 | Risk assessment update (July); independent assessment and policy review (August); review of any new CJISSECPOL version within 60 days of issue | G-034 (CA-2), G-125 (RA-3), CJ-02 (each new version) |

Items already addressed by approval on 2026-08-31: POL-02, POL-03, POL-04, the SSP, the BIA, the risk register, and the P08 runbook. They remain "Not met" or "Partially met" in the CSV because the status reflects fieldwork.

**Progress check.** The Operations Manager reports progress to the owner at a monthly 30-minute security meeting, using the P07 POA&M as the tracker.

## 6. Pending and dated changes
- **CJIS FIPS 140-2 cutoff.** CJISSECPOL v6.1 SC-13 states that FIPS 140-2 certificates "will not be acceptable after September 21, 2026." The SYS-02 switch is due 2026-09-18 (CJ-10).
- **CJIS zero-cycle.** [Priority 2] to [Priority 4] requirements become sanctionable in audits after **2027-09-30** (CJISSECPOL v6.1 sec. 1.4). The AC-01 contract already requires them, so the company rates them now.
- **New CJISSECPOL versions.** The Addendum binds the company to "all subsequent versions" (sec. 3.01). CJ-02 adds a 60-day review of each new version.
- **Pub. 1075.** Rev. 11-2021 remains the edition at irs.gov. Recheck each July.
- **CIRCIA.** Proposed rule only (89 FR 23644). The proposed size criterion would not reach an SBA-small company; the sector criteria must be rechecked when a final rule is published.
- **SP 800-53.** Release 5.2.0 is current. Future releases are picked up at the annual SSP review.

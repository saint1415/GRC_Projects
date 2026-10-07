# Regulatory Gap Analysis: Cris Santos Company | Public Administration | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent GovTech consultant, NAICS 541512) |
| Tier / Vertical | Sole Proprietorship / Public Administration |
| System | Consulting Delivery Environment (CDE), as bounded in the system profile (P02) |
| Primary requirement set | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline, reached through the county contract (CL-01) |
| Overlays | FBI CJIS Security Policy v6.1 (06/25/2026) for the sheriff work (N92-R02); Fla. Stat. 501.171 (applies directly) |
| Assessment dates | 2026-08-10 to 2026-08-14 (self-assessment). Statuses updated to 2026-09-15, when POL-01 was adopted; CJ-03 to CJ-07 updated from P07 testing on 2026-08-25 to 2026-08-27 |
| Assessor | Owner-consultant, with the on-call IT technician (under NDA since 2026-08-07). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-09-15 |

## 1. Applicability
The owner is a private contractor and hosts no agency system. **No rule in this vertical binds the owner by its own force except Fla. Stat. 501.171.** Every other requirement reaches the owner through a contract with an agency that is bound, so this analysis starts with the contracts.

### 1.1 SP 800-53 Rev. 5 Moderate: applies by contract, scoped to the owner's side
SP 800-53 is a federal standard, not a law for private businesses. The county contract (CL-01) requires contractor devices that store county data to meet the Moderate safeguards, and the owner's laptop, cloud storage, and USB drive held county data. The baseline has **177 base controls and 110 enhancements**. Each row in `gap-analysis.csv` is one base control; the Moderate enhancements are assessed inside the row and named in the `citation` column.

**There is no size exemption**, but the baseline was written for organizations that run systems. The owner runs a laptop and SaaS accounts. Each row therefore records one of three decisions:
- **Applies** to the owner's devices, accounts, or practices (132 rows).
- **Met through inheritance**, when a SaaS provider or the operating system does the work and the owner has nothing to configure (counted as Met, with "Inherited" in the current state).
- **Not applicable** (45 rows), with the reason written in the row: the control assumes a workforce (for example PS-4, PS-5), a facility or data center (11 PE controls), software the owner hosts (for example SC-2, SI-10), or a system the agency runs (for example AC-8, IA-3).

### 1.2 FBI CJIS Security Policy: applies to the sheriff work through the Security Addendum
- **Legal path.** 28 CFR 20.33(a)(7) lets criminal history record information go to private contractors under a specific agreement with a criminal justice agency that incorporates the Security Addendum. The Addendum defines a contractor as "a private business, organization or individual" (sec. 1.02), so a sole proprietor is covered. The sheriff's contract (CL-03) incorporates it.
- **What it requires of the owner.** The contractor "will maintain a security program consistent with ... the CJIS Security Policy in effect when the contract is executed and all subsequent versions" (sec. 3.01). The owner signed the certification page in November 2025, and the sheriff keeps it (sec. 2.01).
- **Version checked.** CJISSECPOL **v6.1, dated 06/25/2026**, read from the policy PDF in the FBI file repository on 2026-10-06.
- **No size threshold; priorities set audit timing only.** Section 1.4: since 2024-10-01, "existing" requirements and [Priority 1] requirements are sanctionable; [Priority 2] to [Priority 4] requirements are in a zero-cycle that ends **2027-09-30**. The contract requires the whole policy now, so every CJIS row is rated today.
- **Scope.** Only the owner's access to the sheriff's virtual desktop and any CJI that reaches the owner's side. Nine overlay rows (CJ-01 to CJ-09) cover the duties that fall on a contractor using an agency's remote access. Controls the sheriff runs on its own system (for example AU-11 one-year log retention and SC-13 encryption of the virtual desktop session) are the sheriff's.

### 1.3 Florida Information Protection Act: applies directly
The owner is a "third-party agent" for the county and the city, because it is contracted to "maintain, store, or process personal information on behalf of a covered entity or governmental entity" (501.171(1)(h)). The county's extracts hold names with driver license numbers, and the city's applications hold names with Social Security numbers, both "personal information" (501.171(1)(g)1.a.). Two duties follow: reasonable measures to protect that data (501.171(2), row FL-01), and notice to the agency of a breach of a system the owner maintains "no later than 10 days" after determining it (501.171(6)(a), row FL-02). The sheriff's CJI fields found in P07 (names, dates of birth, booking numbers, charges) are not personal information under 501.171(1)(g), so that event is handled under CJIS only.

### 1.4 Other rules considered
| Rule | Decision | Why |
|---|---|---|
| IRS Pub. 1075 (N92-R01) | Not applicable | The owner holds no federal tax information. A March 2026 subcontract that needed FTI was declined; it would have required Exhibit 7 contract terms, a 45-day IRS notification by the agency, and a background investigation (26 CFR 301.6103(n)-1) |
| Fla. Stat. 282.3185 and 282.3186 | Agency duties the owner supports | The county and city must report ransomware within 12 hours of discovery and other severe incidents within 48 hours (282.3185(5)(b)), and may not pay a ransom (282.3186). These bind the county and city, not the owner; the owner's contract clocks make sure they hear in time (P08) |
| HIPAA Security Rule (N92-R03) | Not applicable | No client has designated the owner a business associate; no PHI is handled |
| Medicaid safeguards (N92-R04) | Not applicable | The city's utility bill assistance program is city-funded; no Medicaid or SNAP data is handled |
| Driver's Privacy Protection Act (N92-R05) | Not applicable | The county's driver license numbers came from residents' own documents, not from state motor vehicle records (county data inventory) |
| SLCGP (N92-R06) | Not applicable | No grant-funded work |
| CIRCIA (N92-R07) | Proposed only | No final rule as of 2026-09-25. The proposed size-based criterion would not reach an SBA-small business |
| GovRAMP (N92-R08) | Not applicable | Voluntary program for cloud providers; the owner offers no cloud service |
| FAR 52.204-21, 52.204-23, 52.204-25 | Not applicable | No federal contracts or subcontracts |

## 2. Method
1. **Requirements.** One row per Moderate base control (177), from the repository copy of the SP 800-53 Rev. 5.2.0 catalog and its baseline flags, plus 9 CJIS overlay rows and 2 Florida rows. CJIS rows summarize the cited section in plain words; CJISSECPOL is a U.S. government work.
2. **Crosswalk.** CSF 2.0 subcategories for base controls come from NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`); 43 base controls have no reference there and show none. Overlay and Florida rows are an **author mapping**, labeled in `crosswalk_source`. The `regulatory_driver` column shows when CJISSECPOL v6.1 also contains the control.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT technician: device and tenant settings, the router, the signed agreements folder, the county contract, and a home office walkthrough on 2026-08-11.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Family | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| AC Access Control | 17 | 7 | 6 | 0 | 4 |
| AT Awareness and Training | 4 | 2 | 2 | 0 | 0 |
| AU Audit and Accountability | 11 | 7 | 2 | 1 | 1 |
| CA Assessment, Authorization, and Monitoring | 7 | 4 | 2 | 0 | 1 |
| CM Configuration Management | 12 | 2 | 6 | 1 | 3 |
| CP Contingency Planning | 9 | 2 | 5 | 1 | 1 |
| IA Identification and Authentication | 10 | 5 | 2 | 0 | 3 |
| IR Incident Response | 8 | 2 | 5 | 1 | 0 |
| MA Maintenance | 6 | 3 | 2 | 0 | 1 |
| MP Media Protection | 7 | 3 | 2 | 1 | 1 |
| PE Physical and Environmental Protection | 16 | 3 | 2 | 0 | 11 |
| PL Planning | 6 | 5 | 0 | 0 | 1 |
| PS Personnel Security | 9 | 4 | 0 | 0 | 5 |
| RA Risk Assessment | 6 | 5 | 1 | 0 | 0 |
| SA System and Services Acquisition | 11 | 3 | 6 | 0 | 2 |
| SC System and Communications Protection | 18 | 7 | 4 | 0 | 7 |
| SI System and Information Integrity | 11 | 5 | 4 | 0 | 2 |
| SR Supply Chain Risk Management | 9 | 2 | 5 | 0 | 2 |
| **SP 800-53 Moderate subtotal** | **177** | **71** | **56** | **5** | **45** |
| CJIS Security Policy v6.1 overlay | 9 | 4 | 5 | 0 | 0 |
| Fla. Stat. 501.171 | 2 | 1 | 1 | 0 | 0 |
| **Total rows** | **188** | **76** | **62** | **5** | **45** |

Of the 67 rows with a gap, 3 are rated High, 19 Moderate, and 45 Low. Many Met rows are policy rows (the "-1" controls) that became Met only when POL-01 was adopted on 2026-09-15; their first real test is the August 2027 review.

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Standard laptop account for daily work; administrator account only for installs | G-006 (AC-6) | High | 2026-09-30 |
| 2 | Data location log per agency; quarterly search for agency data; no CJI outside the virtual desktop | G-051 (CM-12), CJ-05 | High | 2026-09-30 (search running by 2026-11-30) |
| 3 | Delete county phase 1 extracts everywhere and send the county a deletion certificate | G-090 (MP-6), G-167 (SI-12), FL-01 | Moderate | 2026-09-30 |
| 4 | Encrypt the USB drive (or replace it) and keep it in the locked file box | G-156 (SC-28), G-088 (MP-4) | Moderate | 2026-09-30 |
| 5 | CJIS refresher training within 30 days of the 2026-08-25 incident | CJ-03 | Moderate | 2026-09-24 |
| 6 | Print the agency contact sheet; adopt and walk through the P08 runbook | G-076 (IR-6), G-073 (IR-3), G-055 (CP-4) | Moderate | 2026-09-30 (walkthrough 2026-10-31) |
| 7 | Website builder MFA; ask the city for contractor MFA and removal of the 2024 account | G-062 (IA-2), G-002 (AC-2) | Moderate | 2026-09-30 |
| 8 | Monthly sign-in and sharing review | G-027 (AU-6) | Moderate | 2026-10-31 |
| 9 | Provider list and checklist; no agency data in any service without an agency-approved data agreement | G-135 (SA-9), G-132 (SA-4) | Moderate | 2026-10-31 |
| 10 | Encrypted automatic backup of project folders and scripts; quarterly restore test | G-059 (CP-9) | Moderate | 2026-10-31 |
| 11 | Contact sheet with the attorney, sealed recovery codes, second MFA method, peer backup agreement | G-053 (CP-2) | Moderate | 2026-12-31 |

High and Moderate gaps are carried in the risk register (P01) and the POA&M (P07).

## 5. Pending and dated changes
- **CJIS training date moved up.** CJISSECPOL v6.1 AT-2 a.2 requires training within 30 days of any security incident for the individuals involved. The 2026-08-25 incident makes the owner's refresher due 2026-09-24, not the annual date of 2026-11-18.
- **CJIS zero-cycle end.** [Priority 2] to [Priority 4] requirements become sanctionable in audits after **2027-09-30**. The contract already requires them.
- **CJIS FIPS 140-2 cutoff.** CJISSECPOL v6.1 SC-13 states that FIPS 140-2 certificates "will not be acceptable after September 21, 2026." This matters for the sheriff's virtual desktop gateway (the sheriff's control) and for any CJI the owner might store (none is allowed).
- **New CJIS versions.** The Security Addendum binds the owner to "all subsequent versions." CJ-09 adds a quarterly check.
- **CIRCIA.** Proposed rule only (89 FR 23644). Not an obligation.
- **SP 800-53.** Release 5.2.0 is current. Future releases are picked up at the August review.

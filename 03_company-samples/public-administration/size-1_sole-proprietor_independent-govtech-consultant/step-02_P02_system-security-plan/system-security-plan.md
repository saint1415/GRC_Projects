# System Security Plan (short form): Consulting Delivery Environment

**Organization:** Cris Santos Company (independent GovTech consultant) | **Tier:** Sole Proprietorship | **Vertical:** Public Administration
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Consulting Delivery Environment (**CDE**), identifier CSC-SYS-001.

## 2. System Overview
The CDE is everything the owner uses to deliver agency projects: one laptop, one phone, a business productivity suite (email, calendar, cloud storage), a password manager, a home office network, an accounting and website service, a generative AI assistant, and a USB backup drive (SYS-01 to SYS-04 and SYS-06 to SYS-09 in `../00_company-facts.md` section 3). Through it, the owner signs in to three agency systems (SYS-05): a county's case management SaaS, a city's 311 system, and a sheriff's jail and pretrial system reached only through the sheriff's virtual desktop.

**What the CDE is not.** The registry default for this vertical is a case management system hosted for agencies. This consultancy hosts nothing. The agency systems belong to the agencies, sit outside this boundary, and are protected by the agencies' own plans. The owner's job is to make sure the owner's side never becomes the weak path into them, and that agency data copied to the owner's side is protected and then deleted.

Most infrastructure safeguards are **inherited from SaaS providers**. The owner is responsible for identities, data handling, devices, the home network, and choosing providers (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it reaches the owner |
|---|---|---|---|
| Contract CL-01 | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate safeguards for contractor devices that store county data | SP 800-53B Moderate baseline | County contract clause |
| N92-R02 | FBI CJIS Security Policy | CJISSECPOL v6.1 (06/25/2026); 28 CFR 20.33(a)(7); CJIS Security Addendum | Sheriff's contract (CL-03); the owner signed the certification page |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2) and (6) | Directly, as a third-party agent for the county and city |
| Internal | Information Security Policy | POL-01 (P06) | Owner's own rule set |

Not applicable (reasons in P03 section 1): IRS Pub. 1075 (N92-R01; no FTI), HIPAA (N92-R03), Medicaid safeguards (N92-R04), DPPA (N92-R05), SLCGP (N92-R06), CIRCIA (N92-R07, proposed only), and GovRAMP (N92-R08; no cloud service offered).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-consultant on 2026-09-15.
### 4.2 System Authorization Decision
No formal authorization applies to a private consultancy. Equivalent decision: the owner accepted continued operation on 2026-09-15, on condition that the High risks in P01 (R-001, R-002, R-015) are treated by their due dates. The county may ask for this plan with its annual contractor attestation; the sheriff's LASO received the CJI finding and its fix on 2026-08-27.
### 4.3 System Operational Status
Operational. Planned changes: deletion and certification of county phase 1 extracts and an encrypted backup drive (2026-09-30); a separate standard laptop account (2026-09-30); a separate work network with updated router firmware (2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security officer, privacy contact, incident handler, risk acceptor | Owner-consultant | Every role (POL-01 section 3) |
| Technical support | On-call IT technician (NDA since 2026-08-07) | Laptop, network, and recovery help on request; no standing access |
| Agency counterparts | CL-01 county IT security officer; CL-02 city IT director; CL-03 sheriff's LASO | Grant and remove the owner's agency access; receive incident reports |
| Service providers | Productivity suite, password manager, accounting, website, and AI assistant providers | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (modeled on SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| County constituent and property records (CL-01 extracts) | Moderate | Moderate | Low | Driver license numbers for about 2,100 people make disclosure a notice event under Fla. Stat. 501.171; bad migration data corrupts county cases; agencies can resend extracts (P05 BP-03, MTD 120 h) |
| Criminal justice information (CL-03), seen through the virtual desktop | Moderate | Moderate | Low | Disclosure is restricted by 28 CFR Part 20 and the Security Addendum; wrong report logic could misstate custody data; the sheriff's system runs without the owner |
| City constituent and assistance applicant data (CL-02) | Moderate | Low | Low | Income documents and some Social Security numbers; the city decides eligibility, not the owner |
| Agency communications and incident notices | Low | Moderate | Moderate | A missed 1-hour or 24-hour notice breaks a contract (P05 BP-01, MTD 24 h) |
| Business records (invoices, contracts) | Low | Low | Low | P05 BP-04, MTD 240 h |
| **CDE category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, as the county contract requires for contractor devices that store county data, tailored to **26 controls** that carry the owner's real duties (`control-implementation.csv`). The other Moderate controls are either inherited from SaaS providers or the agencies, or tailored out because they assume staff, servers, or software development. P03 records the decision for all 177 Moderate base controls. Where CJISSECPOL v6.1 sets a stricter value (for example, a 30-minute maximum device lock, 1-hour incident reporting, and FIPS 140-3 encryption for any CJI at rest outside a physically secure location), the stricter value governs.

## 7. Authorization Boundary Description
- **Inside:** the laptop, phone, USB backup drive, home office network, and the owner's accounts and settings in the productivity suite, password manager, accounting and website services, and AI assistant; paper in the locked file box.
- **Outside (external systems):** the agency systems behind SYS-05 (county case management SaaS and secure file transfer, city 311 system, sheriff's virtual desktop and jail system), the SaaS providers' platforms, and the ISP.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| County (CL-01) | Migration extracts in through secure file transfer; load files back | County contract (SP 800-53 Moderate clause, 24-hour notice, 30-day deletion) |
| City (CL-02) | 311 configuration; assistance applications viewed in the city system | City contract (confidentiality, prompt notice) |
| Sheriff (CL-03) | Report designs and test output viewed inside the virtual desktop only | Contract with the CJIS Security Addendum |
| Productivity suite provider | Project files, email | Business plan terms; SOC 2 report reviewed (P09) |
| AI assistant provider | City applicant documents (July 2026 only); code and drafts | **Individual plan terms; no data agreement (gap; P10)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Business laptop (SYS-01) | Endpoint | Owner-consultant |
| Productivity suite tenant (SYS-02) | SaaS | Owner-consultant |
| Mobile phone (SYS-03) | Personal endpoint | Owner-consultant |
| Password manager (SYS-04) | SaaS | Owner-consultant |
| Home office router and Wi-Fi (SYS-06) | Network | Owner-consultant (ISP hardware) |
| Accounting service and website builder (SYS-07) | SaaS | Owner-consultant |
| Generative AI assistant (SYS-08) | SaaS | Owner-consultant |
| USB backup drive (SYS-09) | Removable media | Owner-consultant |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 26 controls:
- Implemented: 7
- Partially implemented: 19
- Planned: 0

Inheritance: 13 hybrid (a provider or agency runs the mechanism and the owner configures or uses it correctly) and 13 the owner's alone. None is fully inherited, because every control here depends on something the owner does.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; access agreements and the Security Addendum (PS-6); provider review (SA-9) |
| Identify | Risk assessment (RA-3); BIA (P05); where agency data lives (SI-12, CM-12 in P03) |
| Protect | MFA (IA-2(2)); full-disk encryption (SC-28); standard daily account (AC-6, gap); deletion of agency data (MP-6, gap) |
| Detect | Built-in antivirus (SI-3); SaaS sign-in alerts reviewed monthly (P03 AU-6) |
| Respond | Agency reporting clocks (IR-6); ransomware runbook (IR-8) |
| Recover | Cloud file versions (CP-9, inherited); encrypted USB backup (CP-9, gap); contact sheet and sealed recovery codes (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-08-24 to 2026-08-26 with the on-call IT technician. See P07.

## 11. Digital Identity Acceptance Statement
The productivity suite, password manager, accounting service, and county single sign-on use a password plus an authenticator app; the sheriff's virtual desktop uses a sheriff-issued hardware token. That fits a Moderate categorization. Exceptions: the city 311 system offers contractors a password only (the city's decision; MFA requested 2026-08-24), and the website builder's MFA is off until the owner turns it on by 2026-09-30 (POAM-002).

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **CDE:** Consulting Delivery Environment
- **CHRI:** criminal history record information
- **CJI:** criminal justice information
- **LASO:** local agency security officer (the sheriff's CJIS security contact)
- **MFA:** multi-factor authentication

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-15 | Initial short-form plan | Owner-consultant |

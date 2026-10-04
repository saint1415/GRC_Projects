# Regulatory Gap Analysis: Cris Santos Company | Defense Industrial Base | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts machine shop, DoD subcontractor) |
| Tier / Vertical | Micro / Defense Industrial Base |
| Regulation analyzed | NIST SP 800-171 Rev. 2 (110 requirements), as required by DFARS 252.204-7012(b)(2) and assessed for CMMC Level 2 (32 CFR 170.14(c)(3)) |
| Secondary requirements | DFARS 252.204-7012 cloud, incident, and flowdown paragraphs; DFARS 252.204-7019, 252.204-7020, 252.204-7021; 32 CFR Part 170 scoping; FAR 52.204-21 |
| Assessment dates | 2026-07-13 to 2026-07-24 (shop walkthrough 2026-07-16) |
| Assessor | Office Manager (Security and Compliance Coordinator) with the CNC Programmer and the MSP lead technician |
| Approved | 2026-08-31 by the President |
| Working file | `gap-analysis.csv` (128 rows: G-001 to G-110 for the 110 requirements, G-111 to G-128 for clause and regulation duties) |

## 1. Applicability
**DFARS 252.204-7012 applies now.** Both current customers' purchase orders (Prime A and Supplier B) include the clause, and the shop receives and creates covered defense information: drawings, models, specifications, and the NC and CMM programs made from them. The clause has no small-business exemption, and the prime must flow it down to any subcontract that involves covered defense information, including for commercial products (252.204-7012(m)(1)). It requires SP 800-171 on every covered contractor information system (252.204-7012(b)(2)(i)). A system becomes covered when it actually holds covered defense information, so the commercial suite, the ERP, and the MSP's backup cloud are covered today even though nobody intended it.

**DFARS 252.204-7019 and 252.204-7020 apply now.** A current SP 800-171 DoD Assessment (not more than 3 years old) must be in SPRS (252.204-7019(b)). The company's 2025 Basic Assessment of 110 is current by date but not accurate (section 3).

**CMMC Level 2 (Self) applies from 2027-04-01.** No current purchase order includes DFARS 252.204-7021. Prime A has said that purchase orders under its new program, issued from 2027-04-01, will flow down Level 2 (Self). A subcontractor that processes CUI needs at least Level 2 (Self) (32 CFR 170.23(a)(2)); if a prime contract later requires Level 2 (C3PAO), the shop will need that instead (170.23(a)(3)). Before award, the shop must hold a Conditional or Final Level 2 (Self) status and the President, as Affirming Official, must enter an affirmation in SPRS (32 CFR 170.16(b); 170.22). There is no size exemption.

**Scope.** The CUI Machining Enclave in the SSP (P02), using the CMMC Level 2 asset categories in 32 CFR 170.19(c). The CNC machines and the CMM are Specialized Assets. The MSP handles Security Protection Data (administrator credentials, RMM, logs), so its services are in scope as Security Protection Assets (170.19(c)(2), Table 4).

**Not applicable, with reasons:**
- **3.13.5 (public-access subnetworks):** no publicly accessible system components in the scope; the website is hosted elsewhere with no connection to the shop network.
- **3.13.7 (split tunneling):** no VPN or other remote connection into the shop network is used. Remote users reach the CUI suite directly as a cloud service.
- **NISPOM (32 CFR Part 117):** no facility clearance and no classified information.
- **CIRCIA:** the final rule is not published; nothing is required yet.

**Considered but not decomposed here:** ITAR and EAR. They shape access (U.S.-person checks), encryption (3.13.11 and the carve-outs in 22 CFR 120.54(a)(5) and 15 CFR 734.18(a)(5)), and visitor control, and they are handled in POL-04 and P08.

## 2. Method
1. **Requirements.** The 110 rows follow the official structure of NIST SP 800-171 Rev. 2 (families 3.1 to 3.14), with the CMMC identifier and the point value from the CMMC Scoring Methodology (32 CFR 170.24(c)(2)). Requirement text is quoted from the public-domain NIST publication. The 18 clause rows cite each clause or section paragraph as checked on eCFR (version date 2026-09-23).
2. **Crosswalk.** CSF 2.0 and SP 800-53 Rev. 5 mappings for the 110 requirements are derived from NIST's official mappings through the SP 800-171 Rev. 3 counterpart of each requirement (the Rev. 2 to Rev. 3 change analysis, the SP 800-171r3 CUI overlay, and the CSF 2.0 to SP 800-171r3 mapping). The route through Rev. 3 is the author's; the `crosswalk_source` column says so. The 18 clause rows use author mappings.
3. **Documentary evidence.** Each status rests on a named record: SYS-01 and SYS-02 user and MFA exports, SYS-01 sharing and audit settings, the MSP's device list, patch report, antivirus export, backup job report, and firewall rules, the ERP attachment report, the commercial mailbox search, the DNC settings file, the visitor log, purchase orders to processors, and the shop walkthrough on 2026-07-16. Interviews covered all 7 employees and the MSP lead technician.
4. **Status.** Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-24)**. Actions completed since (for example, the SSP and policies approved on 2026-08-31) appear in the remediation column but do not change the status. For CMMC scoring, a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)), so every Partially met row counts as NOT MET in the score.

## 3. Results summary

### SP 800-171 Rev. 2 requirements (110)
| Family | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 3.1 Access Control | 4 | 11 | 7 | 0 |
| 3.2 Awareness and Training | 0 | 0 | 3 | 0 |
| 3.3 Audit and Accountability | 1 | 5 | 3 | 0 |
| 3.4 Configuration Management | 0 | 4 | 5 | 0 |
| 3.5 Identification and Authentication | 3 | 6 | 2 | 0 |
| 3.6 Incident Response | 0 | 0 | 3 | 0 |
| 3.7 Maintenance | 0 | 3 | 3 | 0 |
| 3.8 Media Protection | 0 | 4 | 5 | 0 |
| 3.9 Personnel Security | 0 | 2 | 0 | 0 |
| 3.10 Physical Protection | 0 | 5 | 1 | 0 |
| 3.11 Risk Assessment | 0 | 1 | 2 | 0 |
| 3.12 Security Assessment | 0 | 0 | 4 | 0 |
| 3.13 System and Communications Protection | 5 | 6 | 3 | 2 |
| 3.14 System and Information Integrity | 3 | 2 | 2 | 0 |
| **Total (110)** | **16** | **49** | **43** | **2** |

Of the 92 requirements not fully met, 30 are basic and 62 are derived requirements.

**What the numbers say.** The requirements that pass are the ones the cloud provider and the MSP deliver by default: encrypted sessions, antivirus, time sync, masked passwords. Everything the company itself must decide, write down, or check is missing: policies, training, logs, inventory, media rules, visitor control, incident reporting, and assessment. That is typical of a 7-person shop that bought a compliant cloud suite and assumed the job was done.

### Clause and regulation duties (18)
| Source | Met | Partially met | Not met |
|---|---|---|---|
| DFARS 252.204-7012 (cloud, special measures, reporting, malware, preservation, forensics, flowdown) | 0 | 2 | 8 |
| DFARS 252.204-7019 and 252.204-7020 (SPRS, Government access, subcontractor assessments) | 1 | 0 | 2 |
| DFARS 252.204-7021 and 32 CFR Part 170 (status, affirmation, CUI only on assessed systems, flowdown, scoping) | 0 | 0 | 4 |
| FAR 52.204-21 (FCI on the commercial suite and ERP) | 0 | 1 | 0 |
| **Total (18)** | **1** | **3** | **14** |

### Score under 32 CFR 170.24
| Item | Value |
|---|---|
| Maximum score | 110 |
| Points subtracted for the 92 requirements not fully met | 271 (38 at 5 points, 14 at 3 points, 39 at 1 point; 3.12.4 carries no point value) |
| **Recalculated score** | **-161** |
| SPRS score posted 2025-12-15 | 110 (to be replaced; corrected score due 2026-09-30) |
| Minimum for Conditional Level 2 (Self) status | 88 (score / 110 of at least 0.8, 32 CFR 170.21(a)(2)(i)) |

Two scoring choices are worth explaining. **3.13.11** is scored at 3 points because encryption is used but FIPS validation is not confirmed (170.24(c)(2)(i)(B)(4)(ii)). **3.5.3** is scored at the full 5 points: the 3-point credit applies when MFA covers remote and privileged users only, and here the privileged gaps (local administrator, firewall, one RMM login) are exactly what is missing.

Conditional status allows only 1-point requirements on a POA&M (plus 3.13.11 when encryption is used but not FIPS-validated), and never 3.1.20, 3.1.22, 3.12.4, 3.10.3, 3.10.4, or 3.10.5 (32 CFR 170.21(a)(2)(ii) and (iii)). Five of those six were open at fieldwork: 3.1.20, 3.12.4 (the SSP was approved on 2026-08-31 and will be checked at the readiness re-check), 3.10.3, 3.10.4, and 3.10.5. **The plan therefore aims for all 110 requirements Met before the self-assessment**, with a POA&M used only as a fallback for 1-point items.

**The SPRS correction.** Counsel advised on 2026-07-28 that the 110 score must be corrected promptly, because knowingly keeping an inaccurate score could create False Claims Act exposure (31 U.S.C. 3729). The President will post -161 with the SSP date and a target date to reach 110 by 2026-09-30, and post an updated score after each roadmap milestone.

## 4. Priority gaps
109 rows are not fully met: 1 Very High, 45 High, 32 Moderate, 31 Low gap risk. The highest-value items:

| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| G-121 SPRS score of 110 is not accurate | 252.204-7019(b); 252.204-7020(d) | Very High | Post -161 with a date to reach 110; update after each milestone | President | 2026-09-30 |
| G-111, G-125, G-020, G-003 CUI in the commercial suite, ERP, and backup cloud | 252.204-7012(b)(2)(ii)(D); 252.204-7021(d)(2); 3.1.20; 3.1.3 | High | Redirect Supplier B; purge and block; compliant backup then retire the commercial one | President; Office Manager | 2026-09-30 to 2026-10-31 |
| G-114, G-115, G-117, G-056 Cannot report to DoD or preserve evidence | 252.204-7012(c), (e); 3.6.2 | High | Certificates for 2 people; P08 runbook; MSP told not to reimage first; DIBNet drill | President | 2026-10-31 to 2026-11-30 |
| G-087 No SSP | 3.12.4 | High | SSP v1.0 approved 2026-08-31 (P02) | Office Manager | Done 2026-08-31 |
| G-127 Scope, inventory, diagram, and MSP documentation | 32 CFR 170.19(c)(1), (c)(2) | High | Inventory by asset category; diagram; MSP responsibility matrix | Office Manager | 2026-10-31 |
| G-044 to G-046, G-053 Shared logins, MFA gaps, plain-text DNC password | 3.5.1; 3.5.2; 3.5.3; 3.5.10 | High | Named accounts with MFA on SYS-03 and SYS-04; MSP named accounts; protect the DNC credential | Office Manager; CNC Programmer | 2026-10-31 |
| G-077 to G-079, G-063 Visitors and service engineers (3 cannot be on a POA&M) | 3.10.3; 3.10.4; 3.10.5; 3.7.6 | Moderate (ITAR release risk) | Log, escort, key register; cover drawings before a foreign person enters | Lead Machinist; Office Manager | 2026-09-30 |
| G-066, G-070, G-071 Paper in the trash; uncontrolled USB drives | 3.8.3; 3.8.7; 3.8.8 | High | Shred bin and shredder; 2 company-owned encrypted drives | Office Manager; Lead Machinist | 2026-09-30 to 2026-10-31 |
| G-088, G-093 Flat network; outbound traffic open | 3.13.1; 3.13.6 | High | Enclave VLAN with deny-by-default rules | Office Manager (MSP performs) | 2026-11-30 |
| G-023, G-024 No training | 3.2.1; 3.2.2 | High | Annual awareness with phishing simulations; role-based modules | Office Manager | 2026-11-30 to 2026-12-31 |
| G-030, G-026 No log review; short retention | 3.3.5; 3.3.1 | High | Monthly review with the MSP; alerts; monthly export | Office Manager | 2026-10-31 to 2026-12-31 |
| G-082, G-109 No scanning or monitoring | 3.11.2; 3.14.6 | High | Monthly scans; MSP managed detection | Office Manager (MSP performs) | 2026-10-31 to 2026-12-31 |

## 5. Remediation plan
The plan fits a 7-person shop: most actions are MSP settings, one-page procedures, or contract terms, not new systems. The MSP performs the technical work under the Office Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Stop the bleeding | 2026-09-30 | Corrected SPRS score; compliant backup and retirement of the commercial backup; shred bin; visitor log, escort, key register; destroy unowned USB drives; offboarding checklist; Wi-Fi key change; MFA on all RMM logins; incident contacts | G-121, G-072, G-066, G-077 to G-079, G-063, G-071, G-074, G-017, G-062, G-118, G-120 |
| 2. Shrink the boundary | 2026-10-31 | CUI out of the commercial suite and ERP; external sharing limits; external systems list and public AI block; named accounts and MFA on shop PCs; desktop encryption; remove local admin; company USB drives; phone app protection; DoD certificates; inventory and MSP responsibility matrix; processor purchase orders; monthly log review and scanning start | G-003, G-020, G-111, G-125, G-127, G-044 to G-046, G-053, G-103, G-098, G-005, G-070, G-018, G-115, G-119, G-123, G-030, G-082 |
| 3. Separate and harden | 2026-11-30 | Enclave VLAN and outbound rules; phones off the enclave; training; tabletop and DIBNet drill | G-088, G-089, G-093, G-095, G-101, G-023, G-025, G-057, G-114 |
| 4. Prove it | 2026-12-31 to 2027-01-31 | Baselines; role-based training; managed detection; allowlisting; contingency plan; first full self-check against SP 800-171A | G-035, G-036, G-024, G-109, G-042, G-084, G-086 |
| 5. Status | 2027-03-15 | Readiness re-check (January 2027), Level 2 self-assessment, score and affirmation in SPRS | G-124 |

**Progress check.** The Office Manager reports progress to the President at a monthly 30-minute meeting, using the P07 POA&M as the tracker. Every High and Very High gap is carried into the risk register (P01) and, where the control was assessed, into the POA&M (P07).

## 6. Pending regulatory changes
- **FAR CUI rule:** proposed (90 FR 4278, 2025-01-15) and not final. Nothing changes until it is final; DFARS 252.204-7012 remains the governing clause.
- **FAR rewrite (Revolutionary FAR Overhaul):** a proposed rule (91 FR 37550, 2026-06-23) would reorganize FAR parts. FAR 52.204-21 numbering may change (flagged on G-128). Not final.
- **SP 800-171 Rev. 3:** published by NIST, but CMMC Level 2 is fixed to Rev. 2 (32 CFR 170.14(c)(3)). Each requirement row names its Rev. 3 counterpart in `pending_rule_change` for later planning. Rev. 3 is not treated as a current obligation.
- **CIRCIA:** the final rule is not published. Proposed reporting deadlines are not treated as current obligations.

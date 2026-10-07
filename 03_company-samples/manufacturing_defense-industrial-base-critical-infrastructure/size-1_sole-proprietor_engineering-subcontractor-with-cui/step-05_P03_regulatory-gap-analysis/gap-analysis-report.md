# Regulatory Gap Analysis: Cris Santos Company | Defense Industrial Base | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (engineering subcontractor handling CUI drawings) |
| Tier / Vertical | Sole Proprietorship / Defense Industrial Base |
| Regulation analyzed | NIST SP 800-171 Rev. 2 (110 requirements), required by DFARS 252.204-7012(b)(2) and assessed as a CMMC Level 2 self-assessment (32 CFR 170.16; 170.14(c)(3)) |
| Secondary requirements | DFARS 252.204-7012 incident, cloud, and flowdown paragraphs; DFARS 252.204-7019, 252.204-7020, 252.204-7021; 32 CFR Part 170 scoping; FAR 52.204-21; ITAR release and registration |
| Assessment dates | 2026-07-13 to 2026-07-24 (self-assessment); CMMC consultant review 2026-07-22 and 2026-07-23 |
| Assessor | Owner. Evidence is self-attested, checked where possible against settings on screen; the independent CMMC consultant challenged each status from screenshots with no CUI |
| Working file | `gap-analysis.csv` (131 rows: G-001 to G-110 for the 110 requirements, G-111 to G-131 for clause and regulation duties) |
| Adopted | 2026-08-31 |

## 1. Applicability
**The rules reach this one-person business through its contract, not through its size.** None of them has a size exemption.
- **DFARS 252.204-7012 applies now.** The Prime A subcontract includes it, and the owner receives and creates covered defense information (controlled technical information). The clause requires SP 800-171 on every covered contractor information system (252.204-7012(b)(2)(i)) and must be flowed down to any subcontract that involves covered defense information, including for commercial services (252.204-7012(m)(1)). Being a sole proprietor working from home changes how the requirements are met, not whether.
- **DFARS 252.204-7019 and 252.204-7020 apply now.** A current Basic Assessment score (not more than 3 years old) must be in SPRS. The 2025 score of 110 is current by date but not accurate (section 3).
- **CMMC Level 2 (Self) applies from the follow-on subcontract.** The current subcontract predates 2025-11-10 and has no DFARS 252.204-7021. Prime A will flow down Level 2 (Self), the minimum for a subcontractor that handles CUI (32 CFR 170.23(a)(2)); if Prime A's own contract moves to Level 2 (C3PAO), so will the subcontract (170.23(a)(3)). Before award the owner needs a Conditional or Final Level 2 (Self) status and an affirmation in SPRS (32 CFR 170.16(b)). The owner is the Affirming Official (32 CFR 170.22).
- **FAR 52.204-21 applies** to systems with FCI, including the accounting SaaS (SYS-05).
- **ITAR applies to the ITAR-marked drawings** (no release to foreign persons, 22 CFR 120.50(a)(2) and 120.56), but **registration does not**: the business is confined to producing unclassified technical data (22 CFR 122.1(b)(2)) and furnishes no defense services, which by definition involve foreign persons (22 CFR 120.32).

**Scope.** The Engineering Office Systems in the SSP (P02), with the CMMC asset categories in 32 CFR 170.19(c). CUI Assets: the laptop, the USB backup drive, the printer, SYS-01 (until migration), and the phone (until CUI is removed). Security Protection Assets: the router and the phone as MFA device. SYS-05 holds FCI only; its position under 252.204-7021(d)(2) is open (G-125), so it is kept in the boundary.

**Not applicable, with reasons (4 requirements, 4 clause rows):** 3.7.5 (no nonlocal maintenance), 3.13.5 (no public system components in scope), 3.13.7 (no VPN or tunnels), and 3.13.14 (no VoIP) are scored as Met under 32 CFR 170.24(b)(3). Flowdown and subcontractor checks (G-119, G-123, G-126) do not apply because the owner has no subcontractors. DDTC registration (G-131) does not apply for the reason above. NISPOM (32 CFR Part 117) does not apply (no facility clearance). CIRCIA has no final rule.

## 2. Method
1. **Requirements.** The 110 rows follow the official structure of NIST SP 800-171 Rev. 2 (families 3.1 to 3.14), with the CMMC identifier and point value from the CMMC Scoring Methodology (32 CFR 170.24(c)(2)). Requirement text is quoted from the public-domain NIST publication. The 21 clause rows cite each clause or section paragraph as checked on eCFR (version date 2026-09-23).
2. **Crosswalk.** CSF 2.0 and SP 800-53 Rev. 5 mappings reuse the Defense Industrial Base Small sample's derivation from NIST's official mappings through each requirement's SP 800-171 Rev. 3 counterpart; the route through Rev. 3 is the author's, and the `crosswalk_source` column says so. Clause rows are author mappings.
3. **Evidence.** Self-attested: settings viewed on screen, screenshots, the SaaS audit pages, and a walkthrough of the home office on 2026-07-15.
4. **Status.** Met, Partially met, Not met, or Not applicable. For CMMC scoring a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)), so every Partially met row counts as NOT MET in the score.

## 3. Results summary
### SP 800-171 Rev. 2 requirements (110)
| Family | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 3.1 Access Control | 5 | 10 | 7 | 0 |
| 3.2 Awareness and Training | 0 | 1 | 2 | 0 |
| 3.3 Audit and Accountability | 3 | 3 | 3 | 0 |
| 3.4 Configuration Management | 0 | 4 | 5 | 0 |
| 3.5 Identification and Authentication | 6 | 3 | 2 | 0 |
| 3.6 Incident Response | 0 | 0 | 3 | 0 |
| 3.7 Maintenance | 3 | 2 | 0 | 1 |
| 3.8 Media Protection | 1 | 7 | 1 | 0 |
| 3.9 Personnel Security | 1 | 1 | 0 | 0 |
| 3.10 Physical Protection | 0 | 4 | 2 | 0 |
| 3.11 Risk Assessment | 1 | 1 | 1 | 0 |
| 3.12 Security Assessment | 1 | 1 | 2 | 0 |
| 3.13 System and Communications Protection | 4 | 8 | 1 | 3 |
| 3.14 System and Information Integrity | 3 | 1 | 3 | 0 |
| **Total (110)** | **28** | **46** | **32** | **4** |

Of the 78 requirements not fully met, 22 are basic and 56 are derived requirements.

### Clause and regulation duties (21)
| Source | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| DFARS 252.204-7012 (cloud, special measures, review, reporting, certificate, malware, preservation, forensics, flowdown) | 0 | 2 | 7 | 1 |
| DFARS 252.204-7019 and 252.204-7020 (SPRS, Government access, subcontractor assessments) | 1 | 1 | 0 | 1 |
| DFARS 252.204-7021 and 32 CFR Part 170 (status and affirmation, systems used, flowdown, scope, CRM) | 0 | 1 | 3 | 1 |
| FAR 52.204-21 (FCI) | 0 | 1 | 0 | 0 |
| ITAR (release; registration) | 0 | 1 | 0 | 1 |
| **Total (21)** | **1** | **6** | **10** | **4** |

### Score under 32 CFR 170.24
| Item | Value |
|---|---|
| Maximum score | 110 |
| Points subtracted for the 78 requirements not fully met | 221 (32 at 5 points, 6 at 3 points, 37 at 1 point, 3.5.3 and 3.13.11 at 3 points each as partially effective; 3.12.4 carries no point value) |
| **Recalculated score** | **-111** |
| SPRS score posted 2025-05-20 | 110 (to be replaced; corrected score due 2026-09-15) |
| Minimum for Conditional Level 2 (Self) | 88 (score divided by 110 of at least 0.8, 32 CFR 170.21(a)(2)(i)) |

A Conditional status also allows only 1-point requirements on a POA&M (plus 3.13.11 when encryption is used but not FIPS-validated), and never 3.1.20, 3.1.22, 3.12.4, 3.10.3, 3.10.4, or 3.10.5 (32 CFR 170.21(a)(2)(ii) and (iii)). **All six of those are open today.** All of them are cheap for a home office (a list of approved external systems, a posting rule, the new SSP, escort, a visitor log, and the spare key), so they are first on the action list. The plan aims for all 110 Met by 2027-01-15, using a POA&M only for 1-point items.

Gap risk for the 94 rows not fully met (78 requirements and 16 clause duties): 2 Very High, 43 High, 22 Moderate, 27 Low.

## 4. Action list (half page)
In order. Items 1 to 5 cost almost nothing and are within the owner's control this month.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Post the recalculated score (-111) and a date-to-110 in SPRS; tell Prime A in writing | 252.204-7019(b); 252.204-7020(d) (G-121) | Very High | 2026-09-15 |
| 2 | Home office: lock the office, remove the spare key, escort visitors, start a visitor log, locked cabinet for prints | 3.10.1 to 3.10.5; 3.8.1 | High | 2026-09-15 |
| 3 | Password manager; delete the password spreadsheet; MFA on SYS-05; router firmware, UPnP off | 3.5.10; 3.5.7; 3.4.7 | High | 2026-09-15 |
| 4 | Standard user account; remove unused software; encrypted backup drive in the home safe; recovery key to the safe | 3.1.5; 3.1.6; 3.4.6; 3.8.9; 3.13.10 | High | 2026-09-30 |
| 5 | Approved external systems list; no CUI in the AI chatbot; posting rule (POL-01) | 3.1.20; 3.1.22 | High | 2026-08-31 (rules) |
| 6 | Medium assurance certificate; DIBNet registration; P08 runbook; forensics firm on call | 252.204-7012(c) to (e); 3.6.1; 3.6.2 | High | 2026-10-31 |
| 7 | Separate business network; vulnerability scans; CAD and firmware updates; security alerts subscription; training | 3.13.1; 3.11.2; 3.14.1; 3.14.3; 3.2.1 to 3.2.3 | High | 2026-10-31 |
| 8 | Migrate all CUI to SYS-10 with hardware keys; CRM in the SSP; delete CUI from SYS-01 and the phone | 252.204-7012(b)(2)(ii)(D); 32 CFR 170.16(c)(2); 3.1.18; 3.13.11 | High | 2026-11-30 |
| 9 | Monthly log review and monitoring checklist; application allowlisting | 3.3.5; 3.12.3; 3.14.6; 3.4.8 | High | 2026-10-31 to 2026-12-31 |
| 10 | Full self-assessment against SP 800-171A with outside review; post the CMMC Level 2 (Self) result and affirm only with evidence | 252.204-7021(d)(1); 32 CFR 170.16(b); 170.22 (G-124) | Very High | 2027-01-15 |

High and Very High gaps are in the risk register (P01) and the POA&M (P07). **If item 10 cannot be supported by evidence by the solicitation date, the owner tells Prime A instead of affirming.**

## 5. Pending regulatory changes
Status checked on 2026-10-04, after adoption, on the Federal Register and eCFR.
- **FAR CUI rule:** proposed (90 FR 4278, 2025-01-15) and not final. DFARS 252.204-7012 remains the governing clause.
- **Revolutionary FAR Overhaul:** a proposed rule (91 FR 37550, 2026-06-23) covers FAR parts 1, 2, 4, 33, 39, 40, and 53, so the FAR 52.204-21 clause number may change (flagged on G-129). Not final.
- **ITAR:** a proposed rule revising the U.S. Munitions List and related definitions and exemptions (91 FR 62361, 2026-10-01; comments close 2026-11-30) is not final (flagged on G-130).
- **SP 800-171 Rev. 3:** published by NIST, but CMMC Level 2 is fixed to Rev. 2 (32 CFR 170.14(c)(3)). Each row names its Rev. 3 counterpart in `pending_rule_change` for later planning.
- **CIRCIA:** the final rule is not published. Proposed reporting deadlines are not current obligations.

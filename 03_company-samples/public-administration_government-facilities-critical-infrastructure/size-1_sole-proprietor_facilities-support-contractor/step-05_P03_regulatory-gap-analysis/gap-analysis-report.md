# Regulatory Gap Analysis: Cris Santos Company | Government Services and Facilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (facilities support contractor operating government buildings, NAICS 561210) |
| Tier / Vertical | Sole Proprietorship / Government Services and Facilities |
| System | Building Systems Support Environment (BSSE), as bounded in the system profile (P02) |
| Primary requirement set | NIST SP 800-53 Rev. 5 (Release 5.2.0) **Moderate** baseline, reached through the city security exhibit (CT-C) |
| Overlays | FAR 52.204-21, 52.204-23, 52.204-25, 52.204-30, and 52.204-9 flowed down by the federal subcontract (CT-F), with GSA BTTRG v3.0 section 1.6.1 and 32 CFR Part 2002 for CUI; Fla. Stat. 119.0701(2)(b), 119.071(3), and 501.171(2) |
| Assessment dates | 2026-08-10 to 2026-08-14 (self-assessment). Statuses updated to 2026-09-04, when POL-01 was adopted, using the P07 test results of 2026-08-18 to 2026-08-20 |
| Assessor | Owner, with the on-call IT technician (under NDA since 2026-08-03). Evidence is self-attested and checked on screen where possible |
| Adopted | 2026-09-04 |

## 1. Applicability
The owner is a private contractor, not a government entity, and hosts no customer system. **The rules in this vertical reach the owner almost entirely through two contracts.** Only three Florida statutes apply by their own force. So this analysis starts with the contracts.

### 1.1 SP 800-53 Rev. 5 Moderate: binding by contract, scoped to the owner's side
SP 800-53 is a catalog, not a law for private businesses. The city adopted cybersecurity standards consistent with the NIST Cybersecurity Framework, as Fla. Stat. 282.3185(4)(a) requires of every county and municipality, and its contract security exhibit requires contractor devices and accounts that administer city building systems or store city data to meet the **Moderate** baseline "as applicable to the contractor's environment." The owner's laptop, phone, and SaaS accounts do both.

The baseline has **177 base controls and 110 enhancements**. Each row in `gap-analysis.csv` is one base control; the Moderate enhancements are assessed inside the row and named in the `citation` column. **There is no size exemption**, but the baseline was written for organizations that run systems. Each row records one of three decisions:
- **Applies** to the owner's devices, accounts, access paths, or practices (133 rows).
- **Met through inheritance**, when a SaaS provider, the operating system, or the city does the work and the owner has nothing to configure (counted as Met, with "inherited" in the current state).
- **Not applicable** (44 rows), with the reason in the row: the control assumes a workforce (for example PS-4, PS-8), a facility or equipment room (12 PE controls), a system the owner hosts (for example SC-2, SI-10), or software development (SA-3, SA-10, SA-11, SA-15).

The city's BAS controllers, supervisory controller, and access control tenant are the city's systems. Their own controls are the city's. What this analysis covers is everything on the owner's side of the connection, including how the owner's accounts are used inside them.

**OT reference.** For the remote access and maintenance rows (AC-17, MA-4), the owner followed the operational technology guidance in NIST SP 800-82 Rev. 3: remote access to building control networks only through the asset owner's managed path, with MFA, and with the owner's knowledge.

### 1.2 Federal subcontract: FAR clauses, GSA reporting, and CUI
| Item | Applies? | Reason |
|---|---|---|
| FAR 52.204-21 (NOV 2021) | **Yes** | The prime must flow it down to subcontractors that may have federal contract information in their systems (52.204-21(c)). The owner receives work orders and point lists by email. Fifteen requirements in (b)(1) apply to the laptop, phone, and suite (rows FAR-01 to FAR-15). The owner has no subcontractors, so the owner's own flow-down duty does not arise (FAR-16) |
| FAR 52.204-23 (DEC 2023) | **Yes** | Flowed down to all subcontracts (52.204-23(d)). Report a Kaspersky covered article within **3 business days** (FAR-17) |
| FAR 52.204-25 (NOV 2021) | **Yes, without (b)(2)** | Flowed down "excluding paragraph (b)(2)" (52.204-25(e)), so the owner may not provide covered telecommunications equipment to the Government but is not under the (b)(2) use prohibition. Report covered equipment within **1 business day**, with more information within 10 business days (FAR-18) |
| FAR 52.204-30 (DEC 2023) | **Yes, without (c)(1)** | Flowed down "excluding paragraph (c)(1)" (52.204-30(e)(1)), so the quarterly SAM.gov review is not a subcontract duty; the owner does it anyway. The (b) prohibition, the SAM.gov search, and the **3 business day** report apply (FAR-19) |
| FAR 52.204-9 (JAN 2011) | **Yes** | The owner needs routine access to a federally controlled facility and system (52.204-9(d)); PIV card accountability and return (FAR-20) |
| C-GOVERNMENT-R01 FISMA | **Indirectly** | FISMA makes GSA responsible for systems "used or operated by an agency or by a contractor of an agency" (44 U.S.C. 3554(a)(1)(A)(ii)). The GSA BAS is GSA's system, and the owner uses it only on GSA's workstation. Through the prime contract, GSA's BTTRG requires immediate reporting of incidents involving GSA systems, data, or credentials (BTTRG 1.6.1, row GSA-01) |
| CUI (32 CFR Part 2002) | **Yes, by contract** | GSA marks the three drawing sets CUI (Physical Security) under GSA Order PBS 3490.3 CHGE 1. Authorized holders must keep CUI in controlled environments and destroy it so it cannot be recovered (32 CFR 2002.14(c), (f)) (row CUI-01). Under 32 CFR 2002.14(h)(2), the owner's systems receive federal information only incidental to providing a service, so they are non-federal systems. The subcontract does not cite NIST SP 800-171 (**watch item**) |

### 1.3 Florida statutes that apply to the owner directly
- **Fla. Stat. 119.0701(2)(b)** (row FL-01). The owner is a "contractor" acting on behalf of the city (119.0701(1)(a)), and the city contract contains the required clause: keep the records the city needs, provide them on the custodian's request, keep exempt records confidential, and at contract end transfer the records and destroy exempt duplicates.
- **Fla. Stat. 119.071(3)** (row FL-02). Building plans and schematic drawings of city buildings are exempt, and a contractor performing work on the building who receives them "shall maintain the exempt status" (119.071(3)(b)3.b. and 4.). Security system plans, including schematic diagrams of security systems, are confidential and exempt in the city's hands (119.071(3)(a)); the contractor keeps them confidential under 119.0701(2)(b)3.
- **Fla. Stat. 501.171(2)** (row FL-03). A third-party agent must take reasonable measures to protect personal information. Whether the city's cardholder exports hold "personal information" under 501.171(1)(g) (names with credential numbers or access history) and whether the city counts as a covered or governmental entity for this section are **for counsel to confirm**. The owner treats the exports as personal information and itself as a third-party agent. The 10-day notice duty in 501.171(6)(a) is in the P08 matrix.

### 1.4 Other rules considered
| Rule | Decision | Why |
|---|---|---|
| IRS Pub. 1075 (C-GOVERNMENT-R02) | Not applicable | No federal tax information |
| CJIS Security Policy (R03) | Not applicable | The city police station is a separate building outside CT-C; the owner has no access to CJI |
| VVSG 2.0 (R04) | Not applicable | No election equipment is kept in the three city buildings |
| FERPA (R05) | Not applicable | No education facilities |
| CIRCIA (R06) | Proposed only | No final rule as of 2026-09-25 (89 FR 23644 proposal). Its proposed government facilities criteria target government entities, not their contractors |
| SLCGP (R07) | Not applicable | A grant condition for state and local governments |
| GovRAMP (R08) | Not applicable | Voluntary verification for cloud providers; the owner offers no cloud service |
| Fla. Stat. 282.3185(5) and 282.3186 | City duties the owner supports | The city must report ransomware within 12 hours and other severity level 3 to 5 incidents within 48 hours of discovery, and may not pay a ransom. These bind the city; the owner's 24-hour contract notice makes sure the city hears in time (P08) |
| FedRAMP, DFARS 252.204-7012, CMMC | Not applicable | No company system is operated on behalf of GSA; no Department of Defense work |

## 2. Method
1. **Requirements.** One row per Moderate base control (G-001 to G-177), from the repository copy of the SP 800-53 Rev. 5.2.0 catalog and its baseline flags; 20 FAR rows cited to clause paragraph (FAR-01 to FAR-20); one GSA row, one CUI row, and three Florida rows. FAR, CFR, and Florida text was read from eCFR (point in time 2026-09-23) and the 2026 Florida Statutes.
2. **Crosswalk.** CSF 2.0 subcategories for 134 base controls come from NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). The other 43 base controls have no official reference; they and all overlay rows carry an **author mapping**, labeled in `crosswalk_source`.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT technician: device and tenant settings, the router, the signed contracts, purchase records, and a home office and van walkthrough on 2026-08-11.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Family | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| AC Access Control | 17 | 7 | 5 | 2 | 3 |
| AT Awareness and Training | 4 | 1 | 2 | 1 | 0 |
| AU Audit and Accountability | 11 | 6 | 2 | 1 | 2 |
| CA Assessment, Authorization, and Monitoring | 7 | 3 | 3 | 0 | 1 |
| CM Configuration Management | 12 | 3 | 6 | 1 | 2 |
| CP Contingency Planning | 9 | 2 | 4 | 3 | 0 |
| IA Identification and Authentication | 10 | 3 | 2 | 1 | 4 |
| IR Incident Response | 8 | 2 | 5 | 1 | 0 |
| MA Maintenance | 6 | 2 | 3 | 1 | 0 |
| MP Media Protection | 7 | 1 | 5 | 1 | 0 |
| PE Physical and Environmental Protection | 16 | 4 | 0 | 0 | 12 |
| PL Planning | 6 | 5 | 0 | 0 | 1 |
| PS Personnel Security | 9 | 4 | 0 | 0 | 5 |
| RA Risk Assessment | 6 | 5 | 1 | 0 | 0 |
| SA System and Services Acquisition | 11 | 3 | 3 | 0 | 5 |
| SC System and Communications Protection | 18 | 11 | 1 | 0 | 6 |
| SI System and Information Integrity | 11 | 4 | 5 | 0 | 2 |
| SR Supply Chain Risk Management | 9 | 2 | 5 | 1 | 1 |
| **SP 800-53 Moderate subtotal** | **177** | **68** | **52** | **13** | **44** |
| FAR 52.204-21(b)(1) and (c) | 16 | 8 | 6 | 0 | 2 |
| FAR 52.204-23, -25, -30, -9 | 4 | 1 | 2 | 1 | 0 |
| GSA BTTRG 1.6.1 and 32 CFR Part 2002 | 2 | 0 | 2 | 0 | 0 |
| Florida statutes | 3 | 0 | 3 | 0 | 0 |
| **Total rows** | **202** | **77** | **65** | **14** | **46** |

The two N/A FAR rows are 52.204-21(b)(1)(xi) (no publicly accessible components) and 52.204-21(c) (no subcontractors). Of the 79 rows with a gap, 5 are rated High, 27 Moderate, and 47 Low. Many Met rows are policy rows (the "-1" controls) that became Met only when POL-01 was adopted on 2026-09-04, or rows inherited from the SaaS providers; their first real test is the August 2027 review.

**Where the gaps are.** The five High gaps are all about access into the city's BAS or the owner as a single point of failure: AC-17 and MA-4 (the remote-desktop agent), IA-2 and IA-5 (the shared BAS administrator account and its 2023 password), and CP-2 (no backup technician or manual steps). The FAR basic safeguarding rows are mostly met, because MFA, encryption, and antivirus were already on. The weak overlay rows are supply chain screening (FAR-18) and CUI handling (CUI-01).

## 4. Action list (half page)
In order. The first five cost nothing and take under a day each.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Remove the remote-desktop agent and cancel the subscription; city VPN only | G-012 (AC-17), G-082 (MA-4), G-035 (CA-3) | High | 2026-09-30 |
| 2 | Password manager now; city changes the BAS password and issues a named account | G-065 (IA-5), G-062 (IA-2), G-002 (AC-2) | High | 2026-10-31 |
| 3 | Standard laptop account for daily work | G-006 (AC-6), FAR-02 | Moderate | 2026-09-30 |
| 4 | Keep only the two latest cardholder exports; city records folder | G-167 (SI-12), FL-03 | Moderate | 2026-09-30 |
| 5 | Print the P08 contact sheet and walk through the runbook | G-076 (IR-6), G-074 (IR-4), GSA-01 | Moderate | 2026-09-30 |
| 6 | Confirm or replace the federal building switch; parts check and SAM.gov FASCSA search before each purchase | G-171 (SR-3), FAR-18, FAR-19 | Moderate | 2026-09-30 |
| 7 | No customer data in any service not on the approved list (chatbot) | G-015 (AC-20), G-135 (SA-9), FL-02 | Moderate | 2026-09-30 |
| 8 | Restricted CUI folder; marking; CUI training | G-088 (MP-4), G-087 (MP-3), G-020 (AT-3), CUI-01 | Moderate | 2026-11-30 |
| 9 | Cloud and drive backups of controller programs; quarterly comparison test | G-059 (CP-9), G-056 (CP-6), G-163 (SI-7) | Moderate | 2026-10-31 |
| 10 | Monthly review of the access control audit trail, session log, and suite sign-ins | G-027 (AU-6) | Moderate | 2026-10-31 |
| 11 | Backup controls firm approved by the city; manual operation sheets; sealed emergency access | G-053 (CP-2), G-055 (CP-4) | High | 2026-12-31 |

High and Moderate gaps are carried in the risk register (P01) and the POA&M (P07).

## 5. Pending changes (not current obligations)
- **FAR overhaul.** The proposed rule published 2026-06-23 (91 FR 37550, FR Doc. 2026-12559; comments closed 2026-07-23) would replace 52.204-21 with a new clause, FAR 52.240-5, Covered Federal Information, move the supply chain clauses into FAR part 40, and add a CUI notice provision (52.240-6) and a CUI clause (52.240-7) that would require NIST SP 800-171 Rev. 3 where a contract includes it. **Proposed only.** Flagged in the `pending_rule_change` column of the FAR and CUI rows. If a future CT-F modification adds a CUI clause, the owner would need a separate SP 800-171 assessment for the CUI folder and devices.
- **CIRCIA.** No final rule as of 2026-09-25. Reporting to CISA is voluntary.
- **SP 800-53.** Release 5.2.0 is current. Future releases are picked up at the August review.

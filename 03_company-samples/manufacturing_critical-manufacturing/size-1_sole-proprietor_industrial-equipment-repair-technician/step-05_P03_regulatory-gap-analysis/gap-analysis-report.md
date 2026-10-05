# Regulatory Gap Analysis: Cris Santos Company | Critical Manufacturing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated industrial equipment repair service, NAICS 811310, Florida) |
| Tier / Vertical | Sole Proprietorship / Critical Manufacturing (size substitution: the business repairs the machines that build grid equipment; it does not manufacture) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, February 26, 2024) with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (September 2023), as the OT guide. **Voluntary**: no binding sector cyber rule applies |
| Binding obligations (by contract) | Customer A's Contractor Cyber Security Exhibit, terms S1 to S8 (S4, S5, and S6 flow down NERC CIP-013-2 R1.2 topics); the mutual NDAs with Customers B and C |
| Also checked | NERC CIP-013-2 direct applicability; the four vertical requirements C-CRITICAL-MFG-R01 to R04; FAR 52.204-21, -23, -25 |
| Sources read | CIRCIA NPRM regulatory text (89 FR 23644, proposed 6 CFR 226.2); CIP-013-2 and CIP-013-3 standard PDFs from NERC; 13 CFR 121.201 (eCFR version 2026-09-23); the SP 800-82 Rev. 3 PDF |
| Assessment dates | 2026-08-24 to 2026-08-28 (self-assessment) |
| Assessor | Owner-technician, with the on-call IT consultant (under NDA since 2026-08-20). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-09-11 |

## 1. Applicability
The most useful finding for a one-person business is what does **not** bind it, and what binds it anyway through a customer.

### 1.1 No binding sector cyber rule
| ID | Requirement | Applies? | Why |
|---|---|---|---|
| C-CRITICAL-MFG-R01 | CIRCIA, proposed 6 CFR Part 226 | **No** | Proposed only; no final rule as of 2026-09-25. Even as proposed it would not reach this business: it is SBA-small (proposed 226.2(a); the 13 CFR 121.201 standard for NAICS 811310 is $12.5 million and receipts are about $180,000); the critical manufacturing criterion in 226.2(b)(3) covers entities that engage in primary metal, machinery, electrical equipment, or transportation equipment **manufacturing**, and repair is not manufacturing; and it does not report under NERC CIP or Form OE-417 (226.2(b)(6)). Its customers that build transformers and switchgear (subsector 335) would be covered if the rule is finalized as proposed (G-047) |
| C-CRITICAL-MFG-R02 | ICTS connected vehicles rule, 15 CFR Part 791 Subpart D | No | No vehicles or vehicle systems (G-048) |
| C-CRITICAL-MFG-R03 | EAR, 15 CFR Parts 730-774 | No | No exports, reexports, or work abroad, and no release of customer technology to foreign persons. Trigger to recheck: an OEM support desk outside the United States asks for program files (G-049; POL-01 8.6) |
| C-CRITICAL-MFG-R04 | DFARS 252.204-7012 | No | No DoD work; no covered defense information (G-050) |
| FAR | 52.204-21, -23, -25 | No | No federal contracts or subcontracts; Customer A confirmed in writing that the service work involves no FAR clauses or FCI (G-051) |

### 1.2 NERC CIP-013-2 binds the utilities, and reaches the owner through Customer A
CIP-013-2 applies to the Responsible Entities in its section 4.1 (Balancing Authorities, certain Distribution Providers, Generator Operators and Owners, Reliability Coordinators, Transmission Operators and Owners). The owner is none of these and is not NERC-registered (G-046, Not applicable).

Requirement R1 Part 1.2 makes each Responsible Entity's procurement process address six topics, including vendor notification of incidents (1.2.1), coordination of responses (1.2.2), notification when access should no longer be granted (1.2.3), verification of software integrity and authenticity (1.2.5), and coordination of vendor-initiated remote access (1.2.6). Customer A's utility contracts carry those topics, and Customer A flows them down through exhibit terms S4, S5, and S6. **The deadlines (24 hours, 1 business day) are Customer A's contract terms, not NERC requirements.** CIP-013-3 is approved and listed on nerc.com as effective 2028-07-01; its R1.2 keeps the same six topics, so the exhibit is unlikely to change in substance.

### 1.3 Why CSF 2.0 with SP 800-82 Rev. 3 is the benchmark
With no binding rule, the owner needs a yardstick that covers both a SaaS office and the moment a laptop is cabled into a PLC. CSF 2.0 is sector-neutral and is the language customers use in supplier questionnaires; SP 800-82 Rev. 3 adds the OT guidance (removable media, remote access, integrity of programs). SP 800-82 Rev. 3 Section 6 is organized by CSF 1.1 categories, so it is cited by section number only, with CSF 2.0 IDs for the outcomes.

The 35 CSF 2.0 subcategories (G-001 to G-035) were selected for a one-person business that holds customers' machine programs and connects to their equipment. Every CSF Function is covered, but this is not a full profile. **Target:** CSF Tier 2 (Risk Informed) by the end of 2027.

## 2. Method
1. **Requirements.** CSF rows use the subcategory text from `00_universal-framework/frameworks/csf2_core.csv` plus the SP 800-82 Rev. 3 section. Contract rows follow the exhibit term numbers and the NDA clauses, summarized in plain words.
2. **Crosswalk.** CSF rows use the **official** NIST CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`); "subset" means only part of a long mapping is listed. Four controls were added by the author from SP 800-82 Rev. 3 OT guidance (IA-2(1) and MA-4 on PR.AA-03; SI-3 and MP-7 on DE.CM-09) and are labeled. Contract and applicability rows are **author mappings**.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT consultant: SaaS account and sharing settings, laptop and phone settings, the field kit, the router at Customer B (2026-08-27, with its maintenance supervisor present), firmware load records, and the contract file.
4. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork (2026-08-28). Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| **A. CSF 2.0 with SP 800-82 Rev. 3 (benchmark)** | | | | | |
| Govern | 0 | 3 | 3 | 0 | 6 |
| Identify | 1 | 2 | 6 | 0 | 9 |
| Protect | 1 | 6 | 5 | 0 | 12 |
| Detect | 0 | 2 | 2 | 0 | 4 |
| Respond | 0 | 0 | 2 | 0 | 2 |
| Recover | 0 | 0 | 2 | 0 | 2 |
| **Subtotal CSF** | **2** | **13** | **20** | **0** | **35** |
| **B. Customer A exhibit (S1 to S8)** | 2 | 2 | 4 | 0 | 8 |
| **C. Customer B and C NDAs** | 0 | 1 | 1 | 0 | 2 |
| **D. Applicability (CIP-013-2, R01 to R04, FAR)** | 0 | 0 | 0 | 6 | 6 |
| **Total** | **4** | **16** | **25** | **6** | **51** |

Of the 41 unmet or partially met rows, **12 are rated High, 23 Moderate, and 6 Low**:
- CSF: 9 High, 18 Moderate, 6 Low.
- Customer A exhibit: 3 High, 3 Moderate.
- NDAs: 2 Moderate.

**Reading the results.**
- **The office side is in fair shape for one person.** Business-grade SaaS, MFA on the suite, disk encryption, automatic updates, and Customer A's gateway for remote work.
- **The field side is not.** The controls that matter when the laptop meets a PLC (scanning, a clean account, an isolated virtual machine, hash checks, a backup that ransomware cannot reach) are missing or partial.
- **Three of the eight exhibit terms have already been missed in practice:** S1 (AI trial and OEM support disclosures), S3 (scanning skipped on night calls), and S5 (4 firmware loads without a hash check). Customer A has not raised them. The owner will tell Customer A about the S5 loads so it can decide whether to recheck those cabinets.

## 4. Action list (half page)
In order. The first six cost nothing.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Adopt POL-01 with the contract obligations list (Appendix B), incident criteria, and the field rules in section 7 | G-001, G-004, G-031 | High | 2026-09-11 (done) |
| 2 | Never skip Customer A's media scanning station; scan every stick on the laptop before use | G-038, G-030 | High | 2026-09-11 (done) |
| 3 | Hash check before every firmware or software load; tell Customer A about the 4 unverified loads | G-040, G-014 | High | 2026-09-30 |
| 4 | MFA on the accounting SaaS and router portal; router off except Customer B approved sessions | G-017, G-027 | High | 2026-09-30 |
| 5 | Stop Customer A uploads to the AI trial; ask for consent or deletion; OEM file sharing only with consent | G-036, G-005, G-022 | Moderate | 2026-09-30 |
| 6 | Subscribe to CISA ICS advisories and the automation makers' security notices | G-012 | Moderate | 2026-09-30 |
| 7 | Offline encrypted backups on two rotating drives; quarterly test restore | G-023, G-034 | High | 2026-10-31 |
| 8 | Standard daily account; host-only virtual machine; Wi-Fi off when cabled; separate home Wi-Fi | G-018, G-024, G-027 | High | 2026-10-31 |
| 9 | Adopt and rehearse the P08 runbook and Customer A 24-hour notice | G-015, G-039, G-033 | High | 2026-10-31 |
| 10 | Library index with hashes; customer-held copies; router replaced or removed | G-009, G-002, G-027 | High | 2026-12-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). Cyber liability insurance (G-043, exhibit S8) is due before the 2027-09-30 renewal.

## 5. Pending and proposed changes (none treated as current obligations)
- **CIRCIA final rule** (C-CRITICAL-MFG-R01). Not published as of 2026-09-25. Recheck scope on publication; the P08 matrix keeps a voluntary CISA report.
- **NIST SP 800-82 Rev. 4 initial public draft** (2026-09-21; comments due 2026-11-30). Update section references in G-001 to G-035 when Rev. 4 is final.
- **CIP-013-3** (effective 2028-07-01 per nerc.com). Same six R1.2 topics; watch for a revised Customer A exhibit.

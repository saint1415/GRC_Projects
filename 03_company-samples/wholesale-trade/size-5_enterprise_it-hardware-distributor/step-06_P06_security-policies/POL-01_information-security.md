# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, SA-9, SI-12, SR-1, SR-3, SR-5, SR-10, SR-11, SR-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05, GV.SC-07 |
| Key regulatory drivers | DFARS 252.204-7012(b); 32 CFR 170.22; FAR 52.204-25; DFARS 252.246-7008; 17 CFR 229.106(b)-(c) |

## 1. Purpose
Establish the enterprise information security and supply chain security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company, customer, and federal information, and the integrity of the products the company distributes.

## 2. Scope
All Cris Santos Company workforce members (employees, temporary workers supplied by staffing agencies, contractors, and interns) at headquarters, the 6 distribution centers, the 15 sales offices, and remote locations, including AQ-1 and any future acquisition from its closing date. Covers all systems and data, including cloud, colocation, SaaS, distribution-center OT, the FSCE, and systems that vendors, carriers, 3PLs, and drop-ship partners operate for the company, and the services offered to external customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity and product-integrity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Chief Supply Chain Officer | Owns the C-SCRM plan, the approved supplier list, and the Product Authentication Lab |
| President, Federal Solutions | CMMC Affirming Official (32 CFR 170.22) |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0, documented in this policy hierarchy, with system security plans for tier-1 systems and for every system in a CMMC Assessment Scope. (PM-1; PL-2; GV.PO-01)
4.2 The CISO is the program owner. The President, Federal Solutions must be designated in writing as the CMMC Affirming Official, and the Director, CMMC Program Office as the owner of CMMC scope and SSPs. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Product-integrity risks that could affect a federal delivery must not be accepted at High or above without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor, staffing agency, 3PL, or drop-ship partner may receive company data, system access, or FCI until it has been tiered and assessed under STD-01.3 and its contract includes the required security, breach notice, and federal flowdown terms. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems, common control providers, and systems in a CMMC Assessment Scope must be assessed at least annually by an assessor independent of their operation. An assessor may not test a system he or she administered in the previous 24 months. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing and an integration plan that brings identity, network, logging, backup, and endpoint controls to enterprise standards within 18 months of closing. (RA-3; SA-9; GV.OC-01)
4.11 Security and CMMC documentation, including assessments, hashed CMMC artifacts, and incident records, must be retained for at least 6 years. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity and product-integrity risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)
4.13 Products for federal orders must be bought from the original manufacturer or its authorized sources first. Open-market purchases for federal orders need Federal Solutions approval and 100% authentication by the Product Authentication Lab. (SR-5; SR-11; GV.SC-07)
4.14 Every SKU must have a manufacturer of record. Products of covered manufacturers (FAR 52.204-25) and Kaspersky covered articles (FAR 52.204-23) must be blocked on federal orders, and drop-ship substitutions must be screened before they are accepted. (SR-3; SR-4; GV.SC-05)
4.15 Open-market receipts of network and security products, and returns of those products, must be authenticated (OEM serial validation, packaging inspection, and firmware verification) before putaway. (SR-10; SR-11; GV.SC-07)
4.16 Suspect counterfeit, tampered, or covered items must be quarantined, retained until disposition instructions are received, and reported under the P08 notification matrix. (SR-12; SR-8; IR-6; GV.SC-08)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Supply Chain and Product Integrity Standard (C-SCRM plan)
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 Product Authentication Procedure
- PRC-01.5 Section 889 and Kaspersky Screening Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CMMC Program Office's internal assessments for the FSCE. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception may allow CUI outside the FSCE, a shared account in the enterprise FCI scope, or a covered manufacturer's product on a federal order. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 OCFP SSP; FSCE CMMC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.

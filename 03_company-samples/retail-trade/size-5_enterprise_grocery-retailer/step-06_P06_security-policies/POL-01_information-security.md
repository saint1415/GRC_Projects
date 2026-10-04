# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk and technology committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AU-1, AU-2, AU-6, AU-11, CA-1, CA-2, CA-2(1), CA-5, CA-8, CM-1, CM-2, CM-3, CM-4, CM-6, CM-8, IA-5, MA-1, PE-1, PL-1, PL-2, PL-4, PM-1, PM-2, PM-9, PS-1, PS-8, RA-1, RA-3, RA-5, RA-7, SA-1, SA-4, SA-9, SI-2, SI-12, SR-1, SR-6 |
| CSF 2.0 | DE.CM-01, GV.OC-01, GV.OC-03, GV.OV-01, GV.PO-01, GV.PO-02, GV.RM-01, GV.RM-04, GV.RR-02, GV.RR-04, GV.SC-05, ID.AM-01, ID.IM-01, ID.RA-01, PR.PS-01 |
| PCI DSS v4.0.1 (N44-45-R01) | 2.2.1, 2.2.2, 6.3.3, 6.5.1, 6.5.2, 10.2, 10.4, 10.5, 11.3, 11.4, 12.1.1, 12.1.2, 12.1.3, 12.1.4, 12.3.1, 12.5.1, 12.5.2, 12.8.1 to 12.8.5 (requirement numbers only; read the text in the company's licensed copy) |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects payment card data, customer and employee personal information, and the systems that keep stores, distribution centers, and online ordering running, and it supports the company's PCI DSS, FTC Act, SNAP EBT, Tennessee Information Protection Act, state law, and SEC obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at the 112 stores in Florida, Georgia, Alabama, South Carolina, and Tennessee, the 2 distribution centers, and headquarters, including the acquired banner (AB) stores from their acquisition date. Covers all systems and data, including stores, colocation, cloud, SaaS, store operational technology, and systems that third parties operate for the company, and the services the company offers to external business clients (SL-1 retail media and SL-2 supplier collaboration).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk and technology committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations; the CFO signs the PCI DSS AOC |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Vice President, Payments | Chairs the payments security council; owns merchant agreements and the ROC |
| Chief Privacy Officer | Privacy program; Tennessee Act compliance; breach determinations with counsel |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that meets PCI DSS v4.0.1 and other applicable requirements, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO is accountable for the security program, the Chief Privacy Officer for the privacy program, and the CFO is the executive owner of PCI DSS compliance. Security roles and responsibilities must be documented and acknowledged by the people who hold them. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. A targeted risk analysis must exist for every PCI DSS requirement that lets the company set its own frequency. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). A risk outside its enterprise tolerance must not be accepted, and food safety risks at High or above need a dated treatment plan. (PM-9; RA-7; GV.RM-04)
4.5 Policies must be reviewed at least every 12 months; standards and procedures at least every 12 months or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security or privacy policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 PCI DSS scope must be documented, with data flows and an inventory of in-scope components, and confirmed at least every 12 months, after any significant change, and before an acquired business processes cards on company systems. (CM-8; PL-2; ID.AM-01)
4.9 Every third party that can affect card data or customer data must be tiered and assessed under STD-01.3 before engagement. Each TPSP must have a written agreement acknowledging its responsibility for account data, a current AOC checked at least every 12 months, and a documented split of PCI DSS responsibilities. (SA-9; SR-6; GV.SC-05)
4.10 Changes to the CDE, payment pages, and tier-1 systems must go through change management with a security and scope impact analysis, testing, and approval. Emergency changes must be approved within 2 business days after implementation. (CM-3; CM-4; PR.PS-01)
4.11 System components must be built from approved hardening baselines, with vendor default accounts and passwords changed or disabled before they connect to any company network. (CM-2; CM-6; IA-5; PR.PS-01)
4.12 Critical and high-risk vulnerabilities must be fixed within 30 days; internal and external vulnerability scans must run at least quarterly and after significant changes; penetration tests must run at least every 12 months and after significant changes, including new checkout paths. (RA-5; SI-2; CA-8; ID.RA-01)
4.13 Security events on CDE and tier-1 systems must be logged, reviewed daily through automated means, and kept at least 12 months with 3 months immediately available. (AU-2; AU-6; AU-11; DE.CM-01)
4.14 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation (Internal Audit), in addition to the annual PCI DSS assessment by a QSA. (CA-2; CA-2(1); ID.IM-01)
4.15 Security documentation, including risk analyses, assessments, and PCI DSS evidence, must be kept at least 3 years, and breach determinations at least 5 years. (SI-12; GV.PO-02)
4.16 Every acquisition must include security due diligence before signing and an integration plan, funded in the deal approval, that brings payments, identity, network, logging, and endpoint controls to enterprise standards within 18 months of closing. (PM-9; SA-4; GV.OC-01)
4.17 The CISO must report cybersecurity risk to the board risk and technology committee at least quarterly, including Very High and High risks, risks outside tolerance, PCI DSS validation status, and material incidents. (PM-9; GV.OV-01)
4.18 Security, privacy, and savings claims made to customers must be reviewed by Legal and, for security claims, by the CISO before publication. (PL-4; GV.OC-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard (including PCI DSS targeted risk analyses)
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and TPSP Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration, Change, and Vulnerability Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security and POI Device Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 PCI DSS Scope Confirmation Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (monthly PCI DSS control metrics to the payments security council), the annual Internal Audit assessment (P07), the annual ROC by the QSA, and quarterly access certifications. Violations are handled under the sanctions procedure (PRC-01.1, statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method (Tables G-5 and I-2), approved at the authority level for the residual risk (statement 4.4), recorded in the exception register with compensating controls, linked to a P01 risk and a P07 POA&M item, and limited to 12 months. An exception is a time-limited deviation while a dated treatment plan runs; it is not a risk acceptance. A PCI DSS requirement cannot be waived by an internal exception: where a PCI DSS requirement cannot be met as written, the PCI Program Manager documents a compensating control for the QSA under the standard's own process. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-02 to POL-05; `policy-hierarchy.md`; P01 enterprise risk register; P02 OCPP SSP; P03 gap analysis; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI governance.

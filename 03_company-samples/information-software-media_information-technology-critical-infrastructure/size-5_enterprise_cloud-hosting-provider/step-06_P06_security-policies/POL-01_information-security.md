# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk and technology committee of the board (on the recommendation of the executive risk committee, 2026-09-08) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-1, RA-3, CA-2, CA-7, CM-3, SA-9, SR-3, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05, ID.IM-01 |
| Regulatory drivers | FedRAMP (C-IT-R01) program rules FRC, IVV, CCM, SCN; SEC Reg S-K Item 106; bank service provider rule (C-IT-R05); DFARS flow-down (C-IT-R03); HIPAA 45 CFR 164.316 (business associate) |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of customer workloads and data, the company's own systems, and the provider tooling that can reach every customer.

## 2. Scope
All Cris Santos Company workforce members (employees and about 1,400 contractors), including the acquired managed services business (AQ-1) from its acquisition date. Covers all regions (R1 to R6 and G1), edge PoPs, the software supply chain and fleet automation, corporate IT, the external cloud tenancy, SaaS, and systems that suppliers operate for the company. Covers all three service lines (SL-1, SL-2, SL-3).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Risk and technology committee of the board | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer and Chief Financial Officer | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Chief Technology Officer | Owns platform engineering; chairs the AI governance committee |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Director of FedRAMP Compliance | Runs FedRAMP rule compliance for FR-1 and FR-2 and the Class D upgrade |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that meets FedRAMP, SOC 2 commitments, and other applicable requirements, documented in this hierarchy and in system security plans for every FedRAMP offering and tier-1 system. (PM-1; PL-2; GV.PO-01)
4.2 An enterprise risk analysis must be performed at least annually and after major changes, incidents, or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.3 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), Chief Executive Officer and Chief Financial Officer jointly (Very High). Risks to provider tooling or federal certification at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.4 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.5 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.6 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.7 No supplier may access customer content, G1 systems, or production systems until it has been tiered and assessed under STD-01.3 and has signed security, incident notice, and (where relevant) BAA terms. Tier-1 supplier reviews must be completed annually. (SA-9; SR-6; GV.SC-05)
4.8 No supplier or employee located in, or owned by a person of, a country of concern may be given access to customer content or G1 data. (SA-9; PS-3; AC-20; GV.SC-05)
4.9 Hardware for G1 must come from approved suppliers, be shipped in tamper-evident packaging, and be inspected at receiving before installation. (SR-3; SR-9; GV.SC-07)
4.10 Every change to production must go through PRC-01.3. Every release through fleet automation (host or guest-agent channel) must be approved by two people from teams other than the author, and each approval must be bound to the approver by signature (STD-01.9). (CM-3; CM-5; AC-5; AU-10; PR.PS-01)
4.11 Each change to a FedRAMP offering must be evaluated for significant change before it is made, and notified to agencies as the SCN rules require. (CM-4; CA-7; ID.RA-07)
4.12 Security controls for FedRAMP offerings, tier-1 systems, and common control providers must be assessed at least annually by an assessor independent of their operation; FedRAMP offerings also by a FedRAMP Recognized assessment service. (CA-2; CA-2(1); ID.IM-01)
4.13 Every acquisition must include security due diligence before closing and an integration plan that brings identity, privileged access, logging, and remote management tools to enterprise standards within 12 months of closing (PRC-01.5). (RA-3; SA-9; GV.OC-01)
4.14 AI systems may be deployed only after the AI governance committee has tiered and reviewed them; high-tier systems that act without a human must have a documented human oversight design (P10). (PM-9; RA-3; GV.OV-01)
4.15 The CISO must report cybersecurity risk to the risk and technology committee of the board at least quarterly, including Very High and High risks, risks outside tolerance, FedRAMP certification status, and material incidents. (PM-9; GV.OV-01)
4.16 Security documentation, including risk analyses, assessments, decision records, and incident records, must be retained for at least 6 years, or longer where a contract or rule requires. (SI-12; GV.PO-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment, Authorization, and FedRAMP Standard
- STD-01.3 Third-Party and Supply Chain Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration, Change, and Vulnerability Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Landing Zone and G1 Enclave Standard
- STD-01.9 Software Release and Provider Tooling Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 Release Approval Procedure (fleet automation)
- PRC-01.5 Acquisition Security Integration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the FedRAMP independent assessment, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.6), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a provider tooling or federal certification risk at High or above are refused unless a dated treatment plan exists. For FedRAMP offerings, each approved exception is also recorded as a decision in the Security Decision Record (SDR-CSO-FRR). Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 HCP-G SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.

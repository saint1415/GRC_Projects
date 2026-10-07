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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or product launches |
| Implements (SP 800-53 Rev. 5) | PM-1, PL-1, RA-1, CA-1, SA-1, SR-1, PL-2, PM-2, RA-3, PM-9, SA-3, SA-8, SA-11, SA-15, CA-5, PS-8, SA-9, SR-6, CA-2, CA-2(1), SR-3, SR-11, SA-4, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05, PR.PS-06 |
| Regulatory basis | FD&C Act 524B(b)(2) (N31-33-R05); 21 CFR 820.10(c); HIPAA 164.308(a)(1), (a)(1)(ii)(C), (a)(2), (a)(8), (b)(1), 164.316 (business associate services); 17 CFR 229.106 |

## 1. Purpose
Establish the enterprise information and product security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company, customer, patient, and consumer information and the integrity of the company's devices, and supports the company's FDA, HIPAA business associate, FTC, and SEC obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at every site: headquarters, the FL-1, MN-1, and TX-1 plants, the R&D centers, the RCM monitoring centers, and remote work, including the acquired infusion business from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, plant OT, the Device Software Factory, and systems that business associates, contract manufacturers, and other vendors operate for the company, and the products and services the company provides to customers and consumers (fielded devices, the DDC, the RCM service, and the consumer companion app).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk and technology committee | Oversees cybersecurity and product security risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| VP Product Security | Product security program and PSIRT; co-owns STD-01.8 |
| CQRO | Design controls, FDA reporting, and 524B compliance |
| Director of Security Operations | HIPAA security official for the business associate services (45 CFR 164.308(a)(2)); runs the SOC |
| Chief Privacy Officer | HIPAA privacy duties as a business associate; FTC rule duties for the consumer app |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information and product security program aligned to NIST CSF 2.0 that meets FD&C Act section 524B, the HIPAA Security Rule for its business associate services, and other applicable requirements, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The Director of Security Operations must be designated in writing as the HIPAA security official for the business associate services, and the Chief Privacy Officer as the privacy official for those services and the consumer app. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes, acquisitions, or product launches, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Patient-safety and product-integrity risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Every device product must be developed under the Secure Product Development Standard (STD-01.8): threat model including related systems, security requirements, security testing with tester independence, a machine-readable SBOM for every build, signed releases, and a postmarket cybersecurity management plan. (SA-3; SA-8; SA-11; SA-15; PR.PS-06)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security or privacy policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may create, receive, maintain, or transmit PHI for the company until a subcontractor business associate agreement is signed and the vendor has been tiered and assessed under STD-01.3. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. (CA-2; CA-2(1); ID.IM-01)
4.10 Suppliers of software, firmware modules, and programmed subassemblies, including contract manufacturers, must meet STD-01.3 supply chain terms: SBOM delivery, vulnerability notification, and use of the manufacturing PKI for any device programming. (SR-3; SR-11; SA-4; GV.SC-05)
4.11 Security documentation, including risk analyses, assessments, and required actions, must be retained for at least 6 years from creation or last effective date, whichever is later; product security records follow the longer QMS retention where it applies. (SI-12; GV.PO-02)
4.12 The CISO and the VP Product Security must report cybersecurity and product security risk to the board risk and technology committee at least quarterly, including Very High and High risks, risks outside tolerance, field actions, and material incidents. (PM-9; GV.OV-01)
4.13 Every acquisition must include security due diligence before closing and an integration plan that brings identity, network, logging, OT, and product security processes to enterprise standards within 12 months of closing. (RA-3; SA-9; GV.OC-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and Supplier Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard (IT and OT)
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Secure Product Development Standard
- STD-01.9 OT Security Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 Firmware Release and Signing Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a patient-safety or product-integrity risk at High or above are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 DSF-MES SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.

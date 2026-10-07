# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | Chief Operating Officer (executive sponsor); maintained by the Security Manager |
| Approved by | Chief Operating Officer; risk acceptance and appetite sections approved by the Chief Executive Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, incidents, or assessment findings |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-5, CM-2, CM-3, CM-6, CM-8, RA-5, SI-2, SA-4, SA-9, SR-3, SR-6 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.OV-01, GV.OC-03, GV.RM-01, GV.SC-05, GV.SC-06, ID.RA-01 |
| SP 800-171 Rev. 2 and contract clauses | 3.4.1 to 3.4.3, 3.11.1 to 3.11.3, 3.12.1 to 3.12.4, 3.14.1; DFARS 252.204-7012(b), (m); 252.204-7019 and 252.204-7020; 252.204-7021; 32 CFR 170.19, 170.22 |
| Supporting standards | STD-01 Configuration and change; STD-03 Supplier and service provider security; STD-05 AI use; STD-09 Vulnerability and patch management |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy its authority. The program protects CUI entrusted to the company by its defense and commercial customers, keeps both plants running, and keeps the company eligible for defense work.

## 2. Scope
All workforce members (employees, temporary workers, and contractors) at Plant 1, Plant 2, and working remotely, and the service providers who operate systems for the company. Covers all company systems and data, with added rules for the CUI Engineering Enclave (CEE) defined in the SSP (P02), shop-floor systems and operational technology, and printed CUI. It applies to controlled unclassified information (CUI), including controlled technical information and export-controlled technical data, federal contract information (FCI), services customer data, and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Receives quarterly cyber risk and CMMC readiness reports |
| Chief Executive Officer | Approves the security budget and risk appetite; accepts High risks; CMMC Affirming Official (32 CFR 170.22) |
| Chief Operating Officer | Program sponsor and CEE system owner; approves policies; accepts Moderate risks; reviews the POA&M monthly |
| vCISO | Program strategy; board reporting; annual policy review |
| Security Manager | Designated security program lead; maintains the SSP, POA&M, and standards index; incident commander |
| GRC analyst | Risk register, evidence, SPRS score calculation |
| Director of Trade Compliance and Contracts | Contract clauses, SPRS submissions, ITAR Empowered Official |
| Director of Supply Chain | Supplier flowdown and verification |
| Director of Engineering | CUI data owner for engineering data |
| Co-sourced internal audit firm | Independent annual assessment; reports to the audit committee |
| All workforce | Follow these policies; report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program that meets NIST SP 800-171 Rev. 2 for every system that processes, stores, or transmits CUI, as DFARS 252.204-7012(b) requires, and that supports CMMC Level 2 certification. The program is documented in this policy set, the standards index, the SSP, and the POA&M. (PM-1; GV.PO-01)
4.2 The Security Manager is the designated security program lead, and the vCISO advises on strategy. Both designations must be in writing. (PM-2; GV.RR-02)
4.3 CUI may be processed, stored, or transmitted only inside the CUI Engineering Enclave or on printed media handled under POL-04. Any change to the enclave boundary, including a new data flow, AI feature, or vendor connection, must be approved by the Security Manager and reflected in the SSP and asset inventory before use. (PL-2; CM-8; 3.12.4; 32 CFR 170.19(c))
4.4 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Risks must be tracked in the risk register with an owner and a treatment. (RA-3; ID.RA-01; 3.11.1)
4.5 **Risk acceptance authority:** the risk owner may accept Low and Very Low risks; the COO, Moderate; the CEO, High (temporarily, up to 12 months). Very High risks may not be accepted. A known failure to meet a DFARS 252.204-7012 duty, an unauthorized export, or an SPRS affirmation not supported by evidence may never be accepted. (PM-9; GV.RM-01)
4.6 Security policies must be reviewed at least annually and after major changes, incidents, acquisitions, or assessment findings. Standards set measurable minimums under each policy and may not weaken it. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved per 4.5, recorded in the risk register, and limited to 12 months or less. (PL-1)
4.8 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. (PS-8; GV.RR-04)
4.9 **Assessment and SPRS.** The company must assess all 110 SP 800-171 requirements against SP 800-171A objectives at least annually, have the co-sourced internal audit firm assess a sample of controls each year, keep a POA&M for every open deficiency, and review the POA&M monthly. The SPRS score must cover every site and system that handles CUI and must be updated within 30 days of a material change. The CEO affirms compliance only on evidence. (CA-2; CA-5; 3.12.1; 3.12.2; 252.204-7019; 32 CFR 170.22)
4.10 **Service providers.** Before a cloud service provider stores, processes, or transmits CUI, it must meet the FedRAMP Moderate baseline or equivalent (DFARS 252.204-7012(b)(2)(ii)(D)). Every External Service Provider that handles CUI or Security Protection Data must be documented in the SSP with its customer responsibility matrix (32 CFR 170.19(c)(2)), and Tier 1 providers are reviewed each year (STD-03). (SA-9; GV.SC-05)
4.11 **Suppliers.** Before any supplier or outside processor receives CUI, its purchase order must include DFARS 252.204-7012 and, where required, 252.204-7020 and 252.204-7021, and the Director of Supply Chain must confirm its SPRS status and, when required, its CMMC status and affirmation. No flowdown, no CUI. (SR-3; SR-6; SA-4; GV.SC-06; 252.204-7012(m); 32 CFR 170.23)
4.12 **Acquisitions and new sites.** Before an acquired company, plant, or system receives or handles CUI, the Security Manager must complete a security and CMMC scoping review, and the SSP and SPRS score must be updated. Until then, CUI may not be sent to it. (RA-3; PM-9; 32 CFR 170.19(c))
4.13 **AI tools.** No AI tool or AI feature may be used with company data until it is approved through the AI governance process in P10 and listed on the approved-tools list. No AI tool may process CUI unless it is inside the assessed enclave boundary. (SA-9; PM-9)
4.14 **Configuration and change.** Every in-scope system, including MES, DNC, and shop-floor servers, must have a documented baseline, and changes must go through the change process with a security impact review (STD-01). (CM-2; CM-3; CM-6; 3.4.1 to 3.4.4)
4.15 **Vulnerability management.** Every in-scope system must be scanned at least monthly, with passive discovery for controllers that cannot be scanned, and findings remediated within the timelines in STD-09. Unsupported software must be replaced or isolated with documented compensating controls. (RA-5; SI-2; 3.11.2; 3.14.1)
4.16 Security documentation (SSP, POA&M, assessments, policies, incident records) must be retained for at least 6 years. (PL-1)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in 4.8. A suspected unauthorized release of ITAR or EAR technical data is also referred to the Director of Trade Compliance and Contracts (Empowered Official) for a voluntary disclosure decision. Compliance is checked through the annual self-assessment, the co-sourced internal audit (P07), the monthly POA&M review, and the reviews in this policy set.

## 6. Exceptions
Exceptions follow 4.7. They must be written, risk-rated, approved by the authority in 4.5, recorded in the risk register, and expire within 12 months. An exception never removes a DFARS 252.204-7012 duty, permits an unauthorized export, or allows a requirement that cannot be on a CMMC POA&M to remain open at assessment.

## 7. Related documents
POL-02 to POL-05; standards index; System Security Plan (P02); Risk Register (P01); Gap Analysis (P03); POA&M (P07); AI governance assessment (P10); NIST SP 800-171 Rev. 2; DFARS 252.204-7012; 32 CFR Part 170

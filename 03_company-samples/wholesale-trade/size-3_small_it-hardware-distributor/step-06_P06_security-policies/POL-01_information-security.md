# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | Chief Operating Officer |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or changes to DoD contract requirements |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-30, PL-1, PS-8, RA-1, RA-3, CA-2, SA-9, SI-12, SR-1, SR-2, SR-3, SR-5, SR-6, SR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-01, GV.SC-05, GV.SC-06, GV.SC-07 |
| Contract and regulatory basis | DFARS 252.204-7012(b); FAR 52.204-21; 32 CFR 170.22 (Affirming Official); FAR 52.204-25; DFARS 252.246-7008 |

## 1. Purpose
Set up the Cris Santos Company information security and supply chain risk management program, assign who is accountable, and give every other security policy its authority. The program protects the company's own information, including Controlled Unclassified Information (CUI) and Federal Contract Information (FCI), and the integrity of the products the company distributes.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary warehouse staff, and contractors) at the Florida headquarters, distribution center, and configuration lab. Covers all company systems and data, including systems that service providers (the MSP and SaaS and cloud vendors) operate for the company, and the purchasing, receiving, and configuration of products for customers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Executive Officer | Approves the security budget; accepts High and Very High risks; CMMC Affirming Official |
| Chief Operating Officer | Program owner and system owner; approves policies; accepts Moderate risks |
| IT Manager | Runs the program day to day; maintains the SSP, risk register, and POA&M |
| Government Contracts Manager | Flowdown clauses, SPRS entries, Section 889 representations and reports, DIBNet reports |
| Purchasing and Supplier Manager | Supply chain risk lead; owns the C-SCRM plan and the approved supplier list |
| All workforce | Follow these policies; report suspected incidents and suspect products immediately |

## 4. Policy statements
4.1 The company must maintain an information security program that meets NIST SP 800-171 Rev. 2 for systems that handle CUI and FAR 52.204-21 for systems that handle FCI, documented in this policy set, the System Security Plan (P02), and the gap analysis (P03). (PM-1; GV.PO-01; DFARS 252.204-7012(b)(2))
4.2 The IT Manager is the designated security lead. The Chief Executive Officer is the CMMC Affirming Official. Both designations must be in writing. (PM-2; GV.RR-02; 32 CFR 170.22)
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1, and must include supply chain threats. Risks must be tracked in the risk register with an owner and treatment. (RA-3; PM-9; SP 800-171 3.11.1)
4.4 Risk acceptance authority: the IT Manager may accept Low risks; the Chief Operating Officer, Moderate; the Chief Executive Officer, High and Very High. A risk that could put counterfeit, tampered, or covered equipment into a DoD system may not be accepted at High without a dated treatment plan. (PM-9; GV.RM-01)
4.5 Security policies must be reviewed at least annually and updated after major changes, incidents, or changes to DoD contract requirements. (PL-1; GV.PO-02)
4.6 Exceptions to any security policy must be requested in writing, risk-rated, approved per 4.4, recorded in the risk register, and time-limited to 12 months or less. Exceptions may never cover a requirement that cannot be placed on a CMMC POA&M (32 CFR 170.21(a)(2)(iii)). (PL-1)
4.7 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. (PS-8)
4.8 **Honest affirmations.** No SPRS score, CMMC self-assessment result, or affirmation may be posted unless a documented assessment supports it. Assessment artifacts must be kept for 6 years (32 CFR 170.16(c)(4) and 170.17(c)(4)). The Government Contracts Manager posts, and the Chief Executive Officer affirms, only after the IT Manager signs the assessment. (CA-2; GV.OV-01)
4.9 **Service providers.** Before a cloud, SaaS, or managed service provider stores, processes, or transmits CUI, FCI, or Security Protection Data for the company, it must pass a security review. CUI may be placed only with a cloud provider that meets the FedRAMP Moderate baseline or its equivalent (DFARS 252.204-7012(b)(2)(ii)(D)). Each provider's customer responsibility matrix must be referenced in the SSP, and providers are reviewed each year. (SA-9; GV.SC-05)
4.10 Security controls must be evaluated at least annually by someone independent of their operation (P07), and all 110 SP 800-171 requirements must be self-assessed each year. (CA-2; SP 800-171 3.12.1)
4.11 **Supply chain risk management.** The company must keep a C-SCRM plan based on NIST SP 800-161 Rev. 1, owned by the Purchasing and Supplier Manager and reviewed at least annually. It covers sourcing, supplier assessment, receiving inspection, Section 889 screening, and single-source product lines. (SR-1; SR-2; PM-30; GV.SC-01)
4.12 **Sourcing order.** Buyers must buy from the original manufacturer or its authorized sources first. Brokers may be used only when authorized sources cannot supply, only if the broker is approved under the broker assessment, and never for a DoD order without Government Contracts Manager approval and notice to the prime. (SR-5; SR-6; GV.SC-06; DFARS 252.246-7008(b))
4.13 **Section 889 screening.** Every SKU must have a manufacturer of record. SKUs made by a covered manufacturer, including rebranded or white-label units, are blocked on federal orders, and the company must not use such equipment in its own systems. (SR-5; SR-3; FAR 52.204-25(b))
4.14 **Supplier terms.** Purchase orders must require suppliers to notify the company of counterfeit, suspect counterfeit, or tampered items, of a compromise affecting the company's orders, and of covered equipment. They must also flow down the substance of FAR 52.204-25 and DFARS 252.246-7008 where those clauses require it. (SR-8; SR-3; GV.SC-05; FAR 52.204-25(e); DFARS 252.246-7008(e))
4.15 Security policies, procedures, assessments, and required actions must be retained for 6 years from creation or last effective date, whichever is later. (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the annual SP 800-171 self-assessment (P03), and the access and supplier reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the Chief Executive Officer for High risk), and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); Gap Analysis (P03); C-SCRM plan (due 2026-11-30); NIST SP 800-171 Rev. 2; NIST SP 800-161 Rev. 1

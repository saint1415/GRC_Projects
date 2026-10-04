# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, new prime programs, changes to DoD or FAR contract requirements, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-9, PM-30, PL-2, RA-3, RA-3(1), CA-2, CA-5, SA-4, SA-9, SR-1, SR-2, SR-3, SR-5, SR-6, SR-8 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-02, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-01, GV.SC-05, GV.SC-06, GV.SC-07 |
| Contract and regulatory basis | DFARS 252.204-7012(b)(2); 32 CFR 170.21, 170.22; FAR 52.204-21, 52.204-25, 52.204-30; DFARS 252.246-7007, 252.246-7008 |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects company, customer, and federal information, and the integrity of the products the company distributes and configures.

## 2. Scope
All workforce members (employees, temporary warehouse staff, contractors) at headquarters, DC-1, DC-2, the Integration Center, the Federal Integration Lab (FIL), and remote locations. It covers all systems and data, including systems that cloud, SaaS, and managed service providers operate for the company, and the products the company buys, configures, and sells.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, CMMC readiness, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and DOP system owner; approves POL-02 to POL-05; accepts Moderate risks; CMMC Affirming Official |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| Director of Information Technology | Runs the program day to day; owns the SSP and contingency planning |
| Security Manager and security analysts | Security operations, MSSP oversight, vulnerability management, GRC, standards |
| Director of Federal Programs | Flowdowns, SPRS entries, Section 889 and FASCSA screening and reports, DIBNet reports |
| Vice President of Supply Chain | Supply chain risk lead; owns the C-SCRM plan and the approved supplier list |
| Director of Quality and Product Compliance | Owns the counterfeit detection and avoidance system |
| Federal Integration Lab Manager | CUI custodian for the enclave and the FIL |
| General Counsel | Legal review of affirmations, notices, and contract terms |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents and suspect products immediately |

**Role overlaps.** The Director of Information Technology both operates controls and maintains the SSP. This is compensated by the vCISO's review of the SSP and by the co-sourced internal audit firm's independent assessment.

## 4. Policy statements
4.1 The company must maintain an information security program that meets NIST SP 800-171 Rev. 2 for systems that handle CUI and FAR 52.204-21 for systems that handle FCI, documented in this policy set, the supporting standards, the System Security Plan (P02), and the gap analysis (P03). (PL-2; GV.PO-01; DFARS 252.204-7012(b)(2))
4.2 The Director of Information Technology is the designated security lead and the Chief Operating Officer is the CMMC Affirming Official. Both designations must be in writing and reaffirmed each year. (PM-9; GV.RR-02; 32 CFR 170.22)
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1, and must include supply chain threats. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; RA-3(1); GV.RM-01; SP 800-171 3.11.1)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. A risk that could put counterfeit, tampered, or covered equipment into a DoD system may not be accepted above Moderate. (PM-9; GV.RM-01)
4.5 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (GV.PO-02)
4.6 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. Exceptions may never cover a requirement that cannot be placed on a CMMC POA&M (32 CFR 170.21(a)(2)). (GV.PO-01)
4.7 **Honest affirmations.** No SPRS score, CMMC self-assessment result, or affirmation may be posted unless a documented, current assessment supports it. When an assessment finds the posted score or status is no longer accurate, the Director of Federal Programs must, on counsel's advice, correct the entry within 30 days. Assessment artifacts must be kept for 6 years. (CA-2; CA-5; GV.OV-01; 32 CFR 170.22)
4.8 **CUI stays in the enclave.** CUI may be stored, processed, or transmitted only in the Federal Integration Enclave and the FIL. Any CUI found elsewhere is an incident under POL-03 and must be removed. Each new prime program must be onboarded to the enclave before CUI is accepted. (PL-2; GV.OC-03; DFARS 252.204-7012(b)(2))
4.9 **Service providers.** Before a cloud, SaaS, or managed service provider stores, processes, or transmits CUI, FCI, or Security Protection Data for the company, it must pass a security review scaled to its tier. CUI may be placed only with a cloud provider that meets the FedRAMP Moderate baseline or its equivalent (DFARS 252.204-7012(b)(2)(ii)(D)). FCI may be shared only with providers bound by FAR 52.204-21 terms. Each provider's customer responsibility matrix must be referenced in the SSP, and Tier 1 providers are reviewed each year (P09). (SA-9; GV.SC-05)
4.10 Security controls must be evaluated at least annually by someone independent of their operation (P07), and all 110 SP 800-171 requirements and 15 FAR 52.204-21 requirements must be self-assessed each year. (CA-2; GV.OV-01; SP 800-171 3.12.1)
4.11 **Supply chain risk management.** The company must keep an approved C-SCRM plan based on NIST SP 800-161 Rev. 1, owned by the Vice President of Supply Chain and reviewed at least annually. It covers sourcing, supplier and contract manufacturer assessment, receiving inspection, Section 889 and FASCSA screening, private-label imports, and single-source product lines. (SR-1; SR-2; PM-30; GV.SC-01)
4.12 **Sourcing order.** Buyers must buy from the original manufacturer or its authorized sources first. Brokers may be used only when authorized sources cannot supply and only if the broker's approval is current. Broker stock may never be allocated to a DoD job without the approval of the Director of Quality and Product Compliance and notice through the prime as DFARS 252.246-7008(b)(3) requires. (SR-5; SR-6; GV.SC-06)
4.13 **Covered equipment screening.** Every SKU must have a manufacturer of record before it can be sold. SKUs from a covered manufacturer under FAR 52.204-25, including rebranded or white-label units, and articles or sources subject to an applicable FASCSA order under FAR 52.204-30, are blocked on federal orders, including drop-ship orders. The Director of Federal Programs searches SAM.gov for FASCSA orders before each new federal program and at least quarterly, and keeps a log. (SR-3; SR-5; GV.SC-07)
4.14 **Counterfeit detection and avoidance.** The company must keep a counterfeit electronic part detection and avoidance system that meets the 12 criteria in DFARS 252.246-7007(c), owned by the Director of Quality and Product Compliance, including risk-based inspection at every receiving site. (SR-11; SR-10; GV.SC-07)
4.15 **Supplier terms.** Purchase orders must require suppliers to notify the company of counterfeit, suspect counterfeit, or tampered items, of a compromise affecting the company's orders, and of covered equipment, and must flow down the substance of FAR 52.204-25, FAR 52.204-30, DFARS 252.246-7008, and DFARS 252.246-7007 where those clauses require it. (SR-8; SA-4; GV.SC-05)
4.16 AI tools that touch company data or influence purchasing, pricing, customer, or employment decisions must be approved through the AI governance process before use (STD-05; P10). (PM-9; GV.RM-01)
4.17 Security policies, procedures, assessments, and incident records must be retained for 6 years from creation or last effective date, whichever is later. (GV.PO-01)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure in POL-05 section 4.12. Compliance is checked through the annual independent assessment (P07), the annual SP 800-171 and FAR 52.204-21 self-assessment (P03), quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.6. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); Gap Analysis (P03); C-SCRM plan (approval due 2026-11-30); NIST SP 800-171 Rev. 2; NIST SP 800-161 Rev. 1

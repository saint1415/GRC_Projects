# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A., and its parent Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | Information Security Officer (ISO) |
| Approved by | Board Risk Committee, 2026-09-15 (the written program itself goes to the full board on 2026-10-20) |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually by the Board Risk Committee (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, CA-5, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.OV-02, GV.SC-05, GV.SC-07, ID.IM-02 |
| Interagency Guidelines (12 CFR 30 App. B) | II.A, II.B; III.A to III.F; 12 CFR 53.4 (service provider notices, both directions) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Set up the bank's written information security program, as the Interagency Guidelines Establishing Information Security Standards require (12 CFR Part 30, Appendix B, section II.A; N52-R02), assign who is accountable, and give every other security policy and standard its authority. The program protects the security and confidentiality of customer information, protects against anticipated threats to it, and protects against unauthorized access to or use of it that could result in substantial harm or inconvenience to any customer (section II.B). It also protects the bank's own information, the funds that move through its payment systems, and the services it provides to respondent institutions.

## 2. Scope
All workforce members of the bank and the holding company (directors, officers, employees, contractors, and temporary staff) at the 28 branches, the headquarters campus, and the Georgia regional office. Covers all systems and data, including systems that service providers operate for the bank (the core processor, the digital banking provider, the card processor, the cloud provider, and other SaaS providers) and the correspondent services the bank provides to respondent institutions.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board of Directors | Approves the program and the risk appetite, including measurable cyber tolerances; accepts Very High risks (temporary only) (III.A) |
| Board Risk Committee | Approves security policies; receives the annual report (III.F) and quarterly cyber risk reports; receives each High-risk acceptance |
| Board Audit Committee | Oversees internal audit; receives the annual control assessment and quarterly POA&M status |
| President and CEO | Executive owner of the program; accepts High risks with the CRO's concurrence |
| Chief Risk Officer | Second-line oversight; owns the risk appetite and the enterprise roll-up; the ISO reports to the CRO |
| Chief Operating Officer | Owns operations and IT; system owner of the COBP; accepts Moderate risks |
| Information Security Officer | Designated by the board; runs the program day to day; owns this policy, the SSP, and MSSP oversight; accepts Low risks |
| IT Risk and Compliance Manager | Maintains the risk register, policy set, standards, and POA&M |
| Third-Party Risk Manager | Vendor inventory, tiering, due diligence, and SOC report reviews |
| Model Risk Manager | Model and AI inventory; validation program |
| Chief Audit Executive | Independent annual assessment (P07) with the co-sourced IT audit firm |
| All workforce | Follow the policies and standards; report suspected incidents and fraud immediately (POL-03) |

## 4. Policy statements
4.1 The bank must maintain a comprehensive written information security program, appropriate to its size and complexity and the nature and scope of its activities, documented in this policy set, the supporting standards, the System Security Plan, and the risk register. The board must approve the program. (PM-1; GV.PO-01; II.A; III.A.1)
4.2 The board designates the ISO in writing. The ISO reports to the CRO and has a direct line to the Board Risk Committee. Where the ISO's team operates a control (for example, vulnerability scanning or MSSP triage), internal audit tests that control independently. (PM-2; GV.RR-02; III.A.2)
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. It must cover payment fraud through customer and bank channels, service provider failures, the bank's role as a service provider to respondents, and AI and models. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; ID.RA-01; III.B)
4.4 **Risk acceptance authority.** Risk owners and the ISO may accept Low and Very Low risks. The COO may accept Moderate risks. The President and CEO may accept High risks for up to 12 months, with the CRO's concurrence and a dated treatment plan, reporting each acceptance to the Board Risk Committee. Only the board may accept Very High risks, for up to 90 days. Residual risk must be compared each quarter with the board's measurable cyber tolerances. (PM-9; GV.RM-01; III.A.2)
4.5 The ISO must report to the Board Risk Committee each quarter on top risks, tolerance measures, POA&M status, incidents, and roadmap progress, and at least annually on the overall status of the program and compliance with the Guidelines: risk assessment, risk management and control decisions, service provider arrangements, test results, security incidents and management's responses, and recommended changes. (GV.OV-01; CA-5; III.F)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. A standard may not weaken its parent policy. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.8 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. (PS-8; GV.RR-04)
4.9 **Service providers.** Before a service provider receives customer information or performs a critical service, the Third-Party Risk Manager must complete due diligence scaled to the vendor's tier (STD-03). Contracts must require appropriate safeguards (III.D.2), incident notice to the bank within a stated time frame, recovery commitments for critical services, and the right to receive SOC reports and bridge letters. For Tier 1 vendors, the Third-Party Risk Manager and the ISO must review SOC reports each year, map complementary user entity controls (CUECs) to bank controls, and follow up on exceptions (III.D.3). The ISO must give every bank service provider a designated point of contact for incident notices under 12 CFR 53.4. (SA-9; SR-6; GV.SC-05; GV.SC-07)
4.10 **The bank as a service provider.** The Correspondent Services Director must collect a designated point of contact from every respondent institution and keep it current. Respondent agreements must state the bank's security, availability, and incident notice commitments. (CA-3; GV.SC-05; 12 CFR 53.4)
4.11 Key controls must be tested regularly, at a frequency set by the risk assessment, by people independent of those who operate or design them: at least an annual independent assessment (P07), annual external and internal penetration tests, and monthly vulnerability scans. (CA-2; ID.IM-02; III.C.3)
4.12 The program must be adjusted when there are relevant changes in technology, threats, business arrangements, outsourcing, or law. Triggers include a new customer-facing or respondent-facing channel, a new AI system used in decisions about customers, a new or renewed critical service provider, a new regulation, and any notification incident. (GV.OV-02; III.E)
4.13 **Models and AI.** Any model or AI system that makes or supports credit decisions or other decisions about customers must be in the model inventory, independently validated on the bank's own data, and fair lending tested before production use, and monitored while in use (STD-05; P10). (SA-9; GV.RM-01)
4.14 Security policies, risk assessments, test results, incident records, and board reports must be retained for at least five years (bank policy choice). (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (section 4.8). Compliance is checked through the annual independent assessment (P07), quarterly access reviews, callback and contact-change sampling, and the tolerance measures reported to the Board Risk Committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved at the level in section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and risk appetite statements (P01); 12 CFR Part 30, Appendix B; 12 CFR Part 53; 12 CFR 225 Subpart N

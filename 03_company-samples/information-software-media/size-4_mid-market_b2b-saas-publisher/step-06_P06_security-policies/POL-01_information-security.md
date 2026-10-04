# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | Director of Security |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-29 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, CA-5, SA-9, SR-6, SI-12, PT-2 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07 |
| Regulatory drivers | N51-R01 (FTC Act Section 5: reasonable security and truthful statements); HIPAA Security Rule as a business associate, 45 CFR 164.308(a)(1), (a)(2), (a)(8), (b); 164.316 |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of customer data, including the protected health information the company holds as a business associate, and keeps what the company says about its security true.

## 2. Scope
All employees, contractors (including the engineering services contractor), and anyone with access to company systems. It covers the Customer Engagement Platform (CEP), the healthcare cell, corporate systems, and all customer data wherever it is processed, including at sub-processors. It applies to any business the company acquires from the date that business connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, incidents, and SOC 2 status |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Technology Officer | Executive sponsor and CEP system owner; approves POL-02 to POL-05; accepts Moderate risks |
| Director of Security | Owns this policy and the program; designated HIPAA Security Official (45 CFR 164.308(a)(2)); reports to the CTO with direct access to the audit committee chair |
| GRC Manager | Risk register, SOC 2 program, standards, vendor risk, statement-to-practice reviews |
| General Counsel and Associate General Counsel, Privacy | Breach determinations and notices; DPAs, BAAs, and sub-processor terms; approve public security, privacy, and AI statements |
| VP Platform Engineering, VP Engineering, Director of IT | Operate the controls in their areas and own the related standards |
| VP Product | Owns AI features and their compliance with the AI standard (STD-05) |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program that addresses the FTC's expectations of reasonable security and the HIPAA Security Rule for the healthcare cell, documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01; 164.316(a))
4.2 The Director of Security is the designated HIPAA Security Official for the company as a business associate. The designation must be in writing and reaffirmed each year. (PM-2; GV.RR-02; 164.308(a)(2))
4.3 An enterprise risk assessment must be performed at least annually and after major changes (including acquisitions and new data flows of regulated data), using NIST SP 800-30 Rev. 1. It must include a risk analysis of the ePHI held for healthcare customers. Every risk must be recorded with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01; 164.308(a)(1)(ii)(A)-(B))
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The CTO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks of bulk or cross-tenant exposure of customer data may not be accepted above Moderate. (PM-9; GV.RM-01)
4.5 The Director of Security must report to the audit committee each quarter on the top risks, POA&M status, incidents, SOC 2 status, and progress against the roadmap. (GV.OV-01; CA-5)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; 164.316(b)(2)(iii))
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.8 **Sanctions.** Workforce members who fail to comply with security or privacy policies must be sanctioned in proportion to intent and harm, from retraining to termination. The VP People and Legal must document each sanction. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))
4.9 **Sub-processors.** Before any vendor receives customer data, it must sign a DPA, pass a security review scaled to its tier (STD-03), and be added to the public sub-processor list with 30 days' notice to customers. A vendor that will receive healthcare cell data must also sign a subcontractor BAA. Purchasing and engineering must not send customer data to a vendor without that approval. (SA-9; GV.SC-05; 164.308(b)(2); 164.314(a)(2)(iii))
4.10 Tier 1 sub-processors must be reassessed each year, including a review of their SOC 2 report or equivalent and a bridge letter (STD-03; P09). (SR-6; GV.SC-07)
4.11 **Truthful statements.** Every public, contractual, or questionnaire statement about security, privacy, or AI must be approved by the General Counsel and must describe controls that actually operate. The GRC Manager must review each published statement against practice every quarter, and any statement found inaccurate must be corrected within 5 business days. (PT-2; GV.OC-03; N51-R01)
4.12 **Data use.** Customer data may be used only to provide and support the service as described in the DPA and BAAs. It must not be used to train AI models, and copies for internal analytics must be limited to aggregated or de-identified data unless the General Counsel approves otherwise in writing. (PT-2; SI-12)
4.13 Security controls must be independently assessed at least annually (P07) and examined each year for the SOC 2 report. (CA-2; 164.308(a)(8))
4.14 Security policies, procedures, risk assessments, assessments, and incident records, including HIPAA-required documentation, must be retained for 6 years from creation or last effective date, whichever is later. (SI-12; 164.316(b)(2)(i))
4.15 New AI features in the product and new AI tools for staff must be approved through the AI governance process before release or use (STD-05; P10). (PM-9; GV.RM-01)
4.16 Acquisitions must complete a security due diligence checklist before signing and a 90-day integration plan before connecting to company systems. (RA-3; CA-3)

## 5. Compliance and enforcement
Violations are handled under section 4.8. Compliance is checked through the annual independent assessment (P07), the SOC 2 examination (P09), quarterly access reviews, and the quarterly statement review.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); FTC Act Section 5 (15 U.S.C. 45); HIPAA Security Rule, 45 CFR 164 Subpart C; customer DPA and BAA templates

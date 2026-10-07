# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, significant incidents, or FCC rule changes |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, CA-5, SA-9, SR-3, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07 |
| FCC and CALEA rules | 47 U.S.C. 222; 47 CFR 64.2009(b), (e); 64.2010(a); 1.20003; 1.20005; 9.19(b); 9.20(e); 64.6305; 1.50007 |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects customer proprietary network information (CPNI), lawful-intercept information, and the network that carries 911 calls, and it is how the company takes "reasonable measures to discover and protect against attempts to gain unauthorized access to CPNI" (47 CFR 64.2010(a)).

## 2. Scope
All workforce members (employees, contractors, and temporary staff) at the central offices, POPs, retail stores, warehouses, remote cabinets, and remote work locations, and the agents of vendors who access company systems, including the overflow call center. It covers all systems and data, including systems vendors operate for the company, and any business the company acquires from the date it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber and regulatory risk; receives quarterly reports from the vCISO directly |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and OSS/BSS system owner; approves POL-02 to POL-05; accepts Moderate risks |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| Chief Technology Officer | Owns network and IT; 911 reliability certifying official; supervises the Security Manager |
| Security Manager and security team | Security operations, MDR oversight, vulnerability management, standards, GRC |
| Vice President of Regulatory Affairs | CPNI compliance officer; signs the CPNI and RMD certifications; breach determinations with counsel |
| Vice President of Network Operations | CALEA senior officer |
| General Counsel | Legal privilege, breach counsel, contract terms |
| Business unit leaders | Apply policies in their units; approve access; own downtime procedures |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program documented in this policy set, the supporting standards, the System Security Plan (P02), the CPNI operating procedures, the CALEA SSI policies, and the NOC outage and 911 reliability procedures. NIST CSF 2.0 and the CISA Cross-Sector Cybersecurity Performance Goals are the benchmark for reasonable measures. (PM-1; GV.PO-01; 64.2010(a))
4.2 **Designations.** The vCISO leads the program, the Vice President of Regulatory Affairs is the CPNI compliance officer, the Vice President of Network Operations is the CALEA senior officer, and the CTO is the 911 reliability certifying official. Designations must be in writing. The CALEA designation and 24x7 contact appendix must be updated and refiled with the FCC within 30 days of any change, and amended CALEA policies must be filed within 90 days of a merger, divestiture, or amendment. (PM-2; GV.RR-02; 1.20003(a), (b)(4); 1.20005(a))
4.3 An enterprise risk assessment must be performed at least annually and after major changes (including acquisitions and new AI use cases), using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could plausibly stop 911 calls or PSAP notice may not be accepted above Low. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, incidents, regulatory filings, and progress against the roadmap. (GV.OV-01; CA-5)
4.6 **Annual CPNI certification.** By March 1 each year, the Vice President of Regulatory Affairs must sign and file the compliance certificate for the prior calendar year. The accompanying statement must be based on evidence (P07 results, the POA&M, training records, complaint logs, breach records), must say plainly where the company is not yet compliant, and must be reviewed by counsel by December 15. (PM-1; GV.OV-01; 64.2009(e))
4.7 Security policies must be reviewed at least annually and after major changes or incidents. Standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02)
4.8 **Sanctions.** Workforce members who misuse CPNI or violate security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. Accessing or disclosing CPNI without a business need is a serious violation. HR and the Vice President of Regulatory Affairs must document each CPNI-related sanction. Vendor contracts must require equivalent discipline for vendor agents. (PS-8; GV.RR-04; 64.2009(b))
4.9 **Vendors.** No vendor may access CPNI, subscriber personal information, or the network until its contract includes CPNI confidentiality, security, training, no training of AI models on company data, and 24-hour security incident notice terms, and it has passed a security review scaled to its tier (STD-03). Purchasing must not issue a purchase order without that approval. (SA-9; GV.SC-05)
4.10 Tier 1 vendors must be reassessed each year, including a review of their SOC 2 report or equivalent (P09). (SR-6; GV.SC-07)
4.11 **Covered equipment.** Network equipment, including used and refurbished equipment, must be checked against the FCC Covered List before purchase. The CTO must attest each January that the network contains no covered communications equipment, so the 2022 certification under 47 CFR 1.50007(c) stays accurate. (SR-3; GV.SC-05; 1.50007)
4.12 Security controls must be independently evaluated at least annually (P07) by people who do not operate them. (CA-2)
4.13 **Retention.** CPNI approval, notification, and campaign records at least 1 year (64.2007(a)(3); 64.2008(a)(2); 64.2009(c), (d)); CPNI breach records at least 2 years (64.2011(d)); 911 reliability supporting records at least 2 years from each filing (9.20(e)); security policies, assessments, and POA&Ms at least 3 years. (SI-12; GV.PO-02)
4.14 **AI.** AI tools that use CPNI, interact with customers, or can affect network operations must be approved through the AI governance process before use (STD-05; P10). (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under section 4.8. Compliance is checked through the annual independent assessment (P07), quarterly access reviews, the evidence gathered for the annual CPNI certification, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under section 4.4, recorded in the risk register, and time-limited to 12 months or less. No exception may permit a practice the CPNI, CALEA, outage, 911 reliability, or robocall rules prohibit.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); risk register and appetite statements (P01); CPNI operating procedures; CALEA SSI policies; NOC outage and storm plan; P10 AI governance process

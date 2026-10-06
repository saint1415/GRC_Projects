# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, CA-5, CM-3, SA-4, SA-9, SA-11, SA-15, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-01, GV.SC-05, GV.SC-07, ID.RA-07, PR.PS-06 |
| Legal drivers | Fla. Stat. 501.171(2) and (6); 8 CFR 274a.2(e)(1)(iii), (g); E-Verify MOU Art. II.A; Title VII 703(k) (42 U.S.C. 2000e-2(k)) for AI tools |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of associate, candidate, clinician, client, and company information, and keeps associates paid on time.

## 2. Scope
All workforce members (internal staff, contractors, and the integration contractor's developers) at HQ, the 14 branches, and the 6 on-site programs, and temporary associates when they use firm systems. It covers all systems and data, including systems that vendors operate for the firm, and any business the firm acquires from the date it connects to firm systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and APATP system owner; approves POL-02 to POL-05 and the standards; accepts Moderate risks |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| Security Manager (Information Security Officer) | Runs the program day to day; owns the SSP, monitoring, vendor reviews, and the GRC function |
| IT Director | IT operations, identity, cloud, and recovery |
| Director of Compliance and Privacy | Privacy Officer; Form I-9, E-Verify, FCRA, ADA medical files, retention; breach determinations with the General Counsel |
| General Counsel | Legal review of incidents, notices, vendor terms, and AI tools |
| Business unit vice presidents and directors | Apply policies in their units; approve access; own downtime procedures |
| Co-sourced internal audit firm | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The firm must maintain an information security program documented in this policy set, the supporting standards, and the System Security Plan, benchmarked against NIST CSF 2.0. (PM-1; GV.PO-01)
4.2 The Security Manager is the designated Information Security Officer. The designation must be in writing and reaffirmed each year. (PM-2; GV.RR-02)
4.3 An enterprise risk assessment must be performed at least annually and after major changes (including acquisitions and new AI tools that affect hiring or pay), using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01; Fla. Stat. 501.171(2))
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could stop associates being paid on the regular payday may not be accepted above Moderate, and risks to clinician credential verification may not be accepted above Low. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, incidents, and progress against the roadmap. (GV.OV-01; CA-5)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.8 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm, from retraining to termination. Sharing a password or an E-Verify credential is a sanctionable offense. The CHRO documents each sanction. (PS-8; GV.RR-04; E-Verify MOU Art. II.A.15)
4.9 **Vendor gate.** Before any vendor receives Restricted data (POL-04) or system access, it must pass a security review scaled to its tier, sign security terms that include breach notice to the firm within 72 hours (and never later than the 10 days allowed by Fla. Stat. 501.171(6)), data use and deletion terms, and be approved by the Security Manager. Purchasing must not issue a purchase order, and no one may accept click-through terms, for such a vendor without that approval. (SA-4; SA-9; GV.SC-05)
4.10 Tier 1 vendors (those with Restricted data at scale or supporting a High-criticality BIA process) must be reassessed each year, including a review of their SOC 2 report or equivalent and the complementary controls the firm must operate (STD-03; P09). (SR-6; GV.SC-07)
4.11 Security controls must be independently assessed at least annually (P07) by a party that does not design or operate them. (CA-2; ID.IM-01; 8 CFR 274a.2(e)(1)(iii))
4.12 Security policies, risk assessments, assessments, and incident records must be retained for at least 6 years. (SI-12)
4.13 AI tools that screen, rank, score, or communicate with candidates or associates, or that affect pay, must be approved through the AI governance process before use (STD-05; P10). Any AI that makes, or is a substantial factor in, an employment decision is High tier. (PM-9; GV.RM-01; Title VII 703(k))
4.14 **Firm-written code** (including the integration platform) must follow the secure development requirements in STD-01: code review, dependency and secret scanning, and no credentials in code or images. Contractors must meet the same requirements under their statements of work. (SA-11; SA-15; PR.PS-06)
4.15 **Configuration changes** to systems that affect pay, Forms I-9, credential verification, or AI tool behavior must be logged, risk-assessed, and approved by the business owner and the IT Director before they take effect (STD-01). (CM-3; ID.RA-07)

## 5. Compliance and enforcement
Violations are handled under statement 4.8. Compliance is checked through the annual independent assessment (P07), quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow statement 4.7. They must be written, risk-rated, approved by the right authority under statement 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); Gap Analysis (P03); AI governance assessment (P10)

# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-2, PM-9, PL-2, RA-3, RA-9, CA-2, CA-5, CM-3, CM-4, SA-4, SA-9, SR-6, PS-7 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-02, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.RA-07, ID.IM-01 |
| Rules and contracts | 9 CFR 417.4(a)(3); 9 CFR 416.14; 29 CFR 1910.119(l); 40 CFR 68.75; Fla. Stat. 501.171(2); customer contracts |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program for both IT and operational technology (OT), assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of company information and control systems so the company can make safe food, protect its workers and neighbors, and keep its commitments to customers.

## 2. Scope
All workforce members (employees, agency temporaries, contractors, and vendors with access) at Plant 1, Plant 2, and the corporate offices. It covers all IT and OT systems and data, including the Plant Production and Cold-Chain Monitoring System (PPCM), systems vendors operate for the company, and any site the company acquires from the date it is acquired.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and PPCM system owner; approves POL-02 to POL-05; accepts Moderate risks |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| Security Manager | Designated security lead for IT and OT; incident commander; MSSP liaison |
| IT Director | IT infrastructure, identity, landing zone, and the IT/OT boundary |
| Controls Engineering Manager | OT system owner at both plants; OT change control |
| Vice President of Food Safety and Quality Assurance | Food safety and food defense decisions; integrity of food safety records |
| Director of Engineering and Maintenance | Refrigeration controls and the PSM and RMP programs |
| GRC Analyst | Policies and standards, risk register, vendor reviews |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents or tampering immediately |

## 4. Policy statements
4.1 The company must maintain an information security program covering IT and OT, documented in this policy set, the supporting standards, and the System Security Plan for the PPCM. (PL-2; GV.PO-01)
4.2 The Security Manager is the designated security lead for IT and OT. The designation must be in writing and reaffirmed each year. (PM-2; GV.RR-02)
4.3 An enterprise risk assessment must be performed at least annually, after each acquisition, and after major changes, using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could plausibly let adulterated or misbranded product reach consumers, or affect ammonia safety, may not be accepted above Low. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, incidents, and progress against the program roadmap. (CA-5; GV.OV-01)
4.6 **One change process for OT.** Every change to PLC logic, HMI screens or setpoints, recipe or blend definitions, SCADA, historians, the MES, refrigeration controllers, OT networks, or OT remote access must go through OT change control (STD-03). The change record must state whether a HACCP reassessment (9 CFR 417.4(a)(3)), a Sanitation SOP revision (416.14), or a PSM and RMP management of change review (29 CFR 1910.119(l); 40 CFR 68.75) is needed, and must carry the FSQA or PSM sign-off when it is. Emergency changes are allowed to protect people or product and must be documented within 1 business day. (CM-3; CM-4; ID.RA-07)
4.7 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-2; GV.PO-02)
4.8 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PM-9)
4.9 **Vendors.** No vendor may receive company data or access to company systems, IT or OT, without a security review scaled to its tier and a contract with security, change notice, and incident notice terms (STD-07). OT vendors must use the company's remote access gateway (POL-02). Purchasing must not issue a purchase order for such a vendor without the GRC Analyst's approval. (SA-4; SA-9; PS-7; GV.SC-05)
4.10 Tier 1 vendors (OT support, cold-chain monitoring, cloud and SaaS hosting PPCM data, the MSSP) must be reassessed each year, including a review of their SOC 2 report or equivalent (P09). (SR-6; GV.SC-07)
4.11 Security controls must be independently assessed at least annually (P07) and after major changes. (CA-2; ID.IM-01)
4.12 **Acquisitions.** An acquired site must not connect to company networks until it passes the integration standard: inventory, remote access review, credential reset, segmentation, and monitoring. Until then it connects only through a filtered interconnection approved by the IT Director. (CA-3; RA-3; GV.SC-06)
4.13 Security policies, risk assessments, assessments, and incident records must be retained for at least 3 years, or longer where a rule requires (for example CCP records under 9 CFR 417.5(e) and PSM incident reports under 1910.119(m)(7)). (SI-12; GV.PO-02)
4.14 AI systems that affect food safety, process control, people decisions, or restricted data must be approved through the AI governance process before use (STD-09; P10). (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under the HR disciplinary procedure, in proportion to intent and harm, from retraining to termination; vendors are handled under their contracts. Compliance is checked through the annual independent assessment (P07), quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.8. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); risk register and appetite statements (P01); gap analysis (P03); HACCP plans and Sanitation SOPs; PSM and RMP program documents

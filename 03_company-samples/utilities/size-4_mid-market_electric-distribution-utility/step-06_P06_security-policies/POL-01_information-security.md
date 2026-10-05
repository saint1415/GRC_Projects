# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | President and CEO (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2025 policy) |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, new client utilities, CIP scope changes, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-2, RA-3, CA-2, CA-5, SA-9, SR-2, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-01, GV.SC-05, GV.SC-07 |
| NERC and other | CIP-002-5.1a R1-R2; CIP-003-9 R1, R3, R4; 16 CFR 681.1(d)-(e); Fla. Stat. 501.171(2) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-11) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of company, customer, and client utility information, and the safe and reliable operation of the distribution grid. When a security action could affect the grid, the safety of the public and line crews comes first.

## 2. Scope
All workforce members (employees, contractors, and temporary staff) at headquarters, the DCC and backup DCC, the 4 operations centers, crew yards, and all 74 substations. It covers all systems and data: corporate IT, the Distribution Operations Platform (DOP), the low impact BES Cyber Systems at Substations N, E, L, and H, the cloud landing zone, the customer and Utility Services SaaS systems, and systems that vendors operate for the company. It covers any asset, substation, or client the company takes on from the date it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board of directors and audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, CIP compliance, and incidents; approves the Identity Theft Prevention Program |
| President and CEO | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | CIP Senior Manager (CIP-003-9 R3); DOP system owner; executive sponsor; approves POL-02 to POL-05 and the CIP low impact policy; accepts Moderate risks |
| General Counsel | Breach determinations with outside counsel; regulator correspondence; the NERC Compliance Manager reports here |
| vCISO | Owns this policy and the program strategy; reports to the board |
| Information Security Manager, 3 security analysts, and the GRC analyst | Runs the program day to day for IT and OT; security operations, vulnerability management, MSSP oversight, standards, GRC |
| Director of Information Technology | IT operations, identity provider, cloud landing zone, corporate network |
| OT Engineering Manager | SCADA, OT network, OT DMZ, OT accounts and backups |
| Director of System Operations | DCC operation; operational incident commander for OT incidents |
| Director of Engineering and Protection | Relays, substation physical access, CIP-002 identifications (delegate under CIP-003-9 R4) |
| NERC Compliance Manager | CIP, EOP-004, and DOE-417 evidence; compliance calendar; SERC submissions and self-reports |
| Vice President of Customer Operations | Customer data owner; Identity Theft Prevention Program administrator |
| Director of Utility Services | Client utility data and service commitments; SOC 2 system description owner |
| Procurement Manager | Vendor security terms and the vendor register |
| Co-sourced internal audit firm | Independent annual assessment (P07); reports to the audit committee |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program documented in this policy set, the supporting standards, the System Security Plan, and the CIP low impact cyber security policy and plan. The program covers IT and OT equally. (PM-1; GV.PO-01)

4.2 The Chief Operating Officer is the CIP Senior Manager. The designation must be documented by name, and any change recorded within 30 calendar days. Delegations of CIP Senior Manager authority must be documented with the delegate, the actions delegated, and the date, and updated within 30 days of a change. The Information Security Manager is accountable for the day-to-day program. (PM-2; GV.RR-02; CIP-003-9 R3, R4)

4.3 An enterprise risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The Chief Operating Officer may accept Moderate risks. The President and CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could plausibly endanger the public or crews may not be accepted above Low. A known or potential noncompliance with a NERC Reliability Standard may never be accepted; it must be mitigated and reported to SERC. (PM-9; GV.RM-01)

4.5 **CIP categorization.** Every BES asset must be considered under CIP-002-5.1a at least every 15 calendar months, and the CIP Senior Manager or delegate must approve the result. Every OT project, acquisition, or transfer of a substation or protection system must pass a CIP-002 review at its design gate and before it goes live. (RA-2; ID.AM-05; CIP-002-5.1a R1, R2)

4.6 **New low impact assets.** When a substation becomes an asset containing a low impact BES Cyber System, every CIP-003-9 Attachment 1 section must be in place on the day it does: keys and locks, access lists, contractor laptop reviews, and vendor access paths. (PL-2; CIP-003-9 R2)

4.7 The vCISO must report to the board each quarter on top risks, POA&M status, CIP compliance and self-reports, incidents, and progress against the roadmap. (GV.OV-01; CA-5)

4.8 Security policies must be reviewed at least annually and after major changes or incidents. The CIP low impact policy must be reviewed and approved by the CIP Senior Manager at least once every 15 calendar months. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; CIP-003-9 R1)

4.9 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months or less. Statements that carry a NERC requirement cannot be excepted. (PL-1)

4.10 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm, from retraining to termination. HR must document each sanction. (PS-8; GV.RR-04)

4.11 **Third parties.** Before a vendor gets system access, OT remote access, or customer data, it must pass a security review scaled to its tier and sign security terms (STD-03). Vendors with OT remote access or customer data are Tier 1 and must be reassessed each year, including a review of their SOC 2 report or equivalent (P09). Purchasing must not issue a purchase order to such a vendor without that approval. Vendors may not install remote access equipment at any substation. (SA-9; SR-6; GV.SC-05; GV.SC-07)

4.12 **OT supply chain.** OT purchases (field devices, radios, relays, SCADA and ADMS software) must meet the OT procurement requirements in STD-03, including approved suppliers and firmware integrity checks. (SR-2; SA-4; GV.SC-01)

4.13 **Customer identity data.** The company must protect personal information with reasonable measures, keep only the identity data it needs, and run a written Identity Theft Prevention Program that is updated at least annually, approved by the board or a board committee, supported by staff training, and applied to service providers. (SI-12; PM-9; 16 CFR 681.1(d)-(e); Fla. Stat. 501.171(2))

4.14 Security controls must be independently evaluated at least annually (P07) and after major changes. (CA-2)

4.15 Security policies, risk assessments, assessments, CIP evidence, and incident records must be kept for at least 3 years, or longer where a regulation, audit cycle, or contract requires. (SI-12; CIP-003-9 Compliance 1.2)

4.16 AI tools that use customer data, operational data, or CEII, or that support operational or customer decisions, must be approved through the AI governance process before use (STD-05; P10). (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under statement 4.10. Compliance is checked through the annual independent assessment (P07), quarterly access reviews, the NERC Compliance Manager's internal CIP checks, and the metrics reported to the board.

## 6. Exceptions
Exceptions follow statement 4.9. They must be written, risk-rated, approved by the right authority under 4.4, and expire within 12 months. Statements 4.2, 4.5, 4.6, and 4.8 carry NERC requirements and cannot be excepted.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; CIP low impact cyber security policy (2026-02-26) and plan; Identity Theft Prevention Program (rewrite due 2026-12-10); System Security Plan (P02); risk register and appetite statements (P01); gap analysis (P03); NERC CIP-002-5.1a and CIP-003-9; 16 CFR 681.1; Fla. Stat. 501.171

# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy, which was written mainly for IT) |
| Review cycle | Annually (next review by 2027-09-30); CIP-003-9 R1 topics within 15 calendar months; and after major changes or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PL-2, PM-2, RA-3, PM-9, RA-2, RA-9, CA-5, PM-4, PL-1, CM-3, CM-4, CA-3, SA-9, SR-6, PS-7, CA-2, RA-5, SI-12, PS-8 |
| CSF 2.0 | GV.PO-01, GV.RR-02, ID.RA-01, GV.RM-01, ID.AM-05, GV.OV-01, GV.PO-02, PR.PS-01, GV.SC-05, ID.IM-01, GV.RR-04 |
| Regulatory drivers | C-DAMS-R01 (FERC Security Program Rev. 3A); C-DAMS-R02 (18 CFR 12.10); C-DAMS-R03 (NERC CIP-003-9, CIP-012-2, EOP-004-4) where cited below |
| Supporting standards | See `standards-index.md` |

## 1. Purpose
Establish the Cris Santos Company information security program for corporate IT, the Hydro Control and Dam Monitoring System (HCDMS), and the services the company provides to RMOS clients; assign accountability; and give every other security policy and standard its authority. The program exists first to keep the dams safe for the people who live downstream, then to keep generation, client services, and company information available and protected.

## 2. Scope
All employees, contractors, OEM and service vendors, and RMOS client users, at headquarters, the Remote Operations Center (ROC), the backup ROC, and all 4 projects. It covers all systems and data, OT and IT, including systems operated for the company by vendors, and client sites connected to the ROC.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports from the vCISO on top risks, POA&M status, incidents, and regulatory matters |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks temporarily |
| Chief Operating Officer | Executive sponsor; CIP Senior Manager (CIP-003-9 R3); authorizing official equivalent for the HCDMS; approves POL-02 to POL-05 and the CIP-003 plan; accepts Moderate risks |
| General Counsel | Regulatory reporting decisions, self-reports, breach decisions; the NERC Compliance Manager reports here |
| vCISO | Owns this policy and the program strategy; reports directly to the audit committee |
| Vice President of Generation Operations | HCDMS system owner |
| OT Security Manager | OT cyber lead: Section 9 measures, CIP-003 implementation, OT monitoring and vulnerability management |
| IT Director | IT security lead: identity, corporate network, cloud landing zone |
| Corporate Security Manager | FERC primary security contact; Security Plans, VA, SAs; physical security |
| Chief Dam Safety Engineer | EAPs, 18 CFR 12.10 reports, annual certification letter; AI-001 business owner |
| NERC Compliance Manager | CIP-002, CIP-003, CIP-012, and EOP-004 compliance and evidence |
| GRC Manager | Policies and standards, gap analysis, POA&M, vendor and client risk, SOC 2 readiness |
| Co-sourced internal audit firm | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
Each statement ends with the SP 800-53 controls, CSF 2.0 subcategory, and regulatory driver it implements.

4.1 The company must maintain an information security program that covers OT and IT, meets the FERC Security Program for Hydropower Projects for each dam according to its Security Group, and meets NERC CIP-003-9 for the low impact BES assets. It is documented in this policy set, the supporting standards, the System Security Plan (the Cyber/SCADA Security Plan), and the CIP-003 plan. (PM-1; PL-2; GV.PO-01; C-DAMS-R01 (Rev. 3A 3.2; 3.3.1; 3.3.2); C-DAMS-R03 (CIP-003-9 R1 Part 1.2, R2))
4.2 The Chief Operating Officer is the CIP Senior Manager. The designation must name the person and be updated within 30 calendar days of a change; any delegation must be documented with the delegate, the actions, and the date. (PM-2; GV.RR-02; C-DAMS-R03 (CIP-003-9 R3, R4))
4.3 A risk assessment covering OT and IT must be performed at least annually and after major changes (new project, new RMOS client, change in BES status), using NIST SP 800-30 Rev. 1. Every risk must be recorded with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01; C-DAMS-R01 (Form 3 Q23a, Q29-31))
4.4 Risk acceptance authority: risk owners may accept Low and Very Low risks; the COO may accept Moderate risks; the CEO may accept High risks for up to 12 months with a dated plan. Very High risks may not be accepted except by a CEO exception of up to 90 days after notice to the audit committee chair. A risk that could plausibly cause an uncontrolled release, a missed warning, or loss of a public water supply may not be accepted above Low. A known noncompliance with a FERC or NERC requirement is never accepted as a risk. (PM-9; GV.RM-01; C-DAMS-R01 (Form 3 Q29))
4.5 The FERC Section 9 cycle must run every June: Form 3 Questions 1-4 for every Group 1 and 2 dam, the consequence determination against Table 9.1c, criticality review of the cyber asset inventory, and Form 3 Questions 5-33 with a plan and schedule for each negative answer. Interconnected facilities, including the Group 3 dam and RMOS client sites, are included. (RA-2; RA-9; CA-5; ID.AM-05; C-DAMS-R01 (Rev. 3A 9.1.1; 9.1.1.3; 9.2; Table 9.3a general))
4.6 The Annual Security Compliance Certification Letter must be accurate. Before signature, the Chief Dam Safety Engineer must receive written confirmation from the Corporate Security Manager (VA, SAs, Security Plans, exercise status) and the OT Security Manager (Section 9 status). (CA-5; PM-4; GV.OV-01; C-DAMS-R01 (Rev. 3A 8.0))
4.7 The vCISO must report to the audit committee each quarter on top risks, POA&M status, incidents, regulatory findings, and progress against the program roadmap. (PM-9; CA-5; GV.OV-01; C-DAMS-R01 (Form 3 Q31 (results reported to management)))
4.8 Security policies must be reviewed at least annually and after major changes or incidents. Policies that address CIP-003-9 R1 Part 1.2 topics must be reviewed and approved by the CIP Senior Manager at least once every 15 calendar months. (PL-1; GV.PO-02; C-DAMS-R01 (Table 9.3a general (review procedures annually)); C-DAMS-R03 (CIP-003-9 R1))
4.9 Security impact review: any change to the HCDMS, any new remote or third-party connection to OT, and any new RMOS client must be reviewed by the OT Security Manager before approval by the change board. No connection from the cloud or the corporate network into OT may be created except through the OT DMZ jump hosts. (CM-3; CM-4; CA-3; PR.PS-01; C-DAMS-R01 (Table 9.3a system lifecycle (secure design); Table 9.3a access control))
4.10 Vendor and client security: no OEM, vendor, or RMOS client may connect to OT, or receive CEII or Confidential data, without a contract security schedule (responsibilities, incident notice within 24 hours, remote access rules, return of data) approved by the GRC Manager. Tier 1 vendors and all RMOS client connections are reviewed each year (STD-03). (SA-9; SR-6; PS-7; GV.SC-05; C-DAMS-R01 (Table 9.3a coordination (outsourcers, partners); Form 3 Q32a))
4.11 Security controls must be independently assessed at least annually (P07), and OT vulnerability assessments must be done for every Critical cyber system at least every 12 months. (CA-2; RA-5; ID.IM-01; C-DAMS-R01 (Table 9.3b vulnerability assessment; Form 3 Q24b, Q31))
4.12 Records: Security Program documents, risk assessments, assessments, and incident records are kept at least 6 years; NERC compliance evidence at least 3 calendar years, or longer if the Regional Entity directs; 12.10 reports as permanent project records under 18 CFR 12.12. (SI-12; GV.PO-01; C-DAMS-R03 (evidence retention); C-DAMS-R02 (related Part 12 duty: 12.12))
4.13 AI systems that analyze dam safety data, support operating decisions, monitor security, or process CEII or Confidential data must be approved through the AI governance process before use (STD-11; P10). No AI output may command a gate or unit or replace a manual dam safety check. (PM-9; SA-9; GV.RM-01; C-DAMS-R01 (Rev. 3A 3.2 (trigger points defined by people)))
4.14 Sanctions: workforce members who violate security policies are subject to discipline in proportion to intent and harm, documented by HR. (PS-8; GV.RR-04; Company policy)

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), quarterly OT access reviews, NERC compliance evidence reviews by the NERC Compliance Manager, and metrics reported to the audit committee. Violations are handled under POL-01 4.14.

## 6. Exceptions
Exceptions must be requested in writing, risk-rated, approved under POL-01 4.4, recorded in the risk register, and limited to 12 months. No exception may waive a FERC or NERC requirement.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); risk register and appetite (P01); FERC Security Program Rev. 3A; CIP-003-9 low impact plan; Owner's Dam Safety Program; EAPs

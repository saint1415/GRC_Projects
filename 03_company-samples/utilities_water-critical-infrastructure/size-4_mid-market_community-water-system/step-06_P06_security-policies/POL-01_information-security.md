# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after any acquisition, new interconnection, or significant incident |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-3, CA-5, SA-4, SA-9, SR-6, SC-24, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.RA-05, PR.IR-03 |
| Regulatory drivers | SDWA section 1433, 42 U.S.C. 300i-2(a)-(d) (C-WATER-R01); Fla. Stat. 501.171(2) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program for business IT and operational technology (OT), assign accountability, and give every other security policy and standard its authority. The program exists so that the company can keep delivering safe drinking water to the people it serves, protect customer and client data, and keep its SDWA section 1433 risk and resilience assessments (RRAs) and emergency response plans (ERPs) accurate.

## 2. Scope
All workforce members (employees, contractors, and integrator and vendor staff working under company direction) at headquarters, the Regional Operations Center (ROC), all plants, field operations centers, and remote sites. It covers all systems and data: the Integrated Water Operations SCADA (IWOS), business IT, cloud and SaaS services, Utility Services systems used for municipal clients, and every water system the company acquires, from the date the acquisition agreement is signed.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber and resilience risk; receives quarterly reports on top risks, POA&M status, incidents, and SDWA certification status |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor; IWOS system owner; approves POL-02 to POL-05; accepts Moderate risks; signs EPA RRA and ERP certifications |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| IT Director (security officer) | Runs the program day to day; owns the IT/OT boundary, remote access, and identity |
| Director of Water Operations | Operations owner for all OT; decides operating mode during incidents |
| SCADA and Controls Engineering Manager | OT configuration, backups, change control, and integrator oversight |
| Security Manager and security analysts | Security operations, OT monitoring, vulnerability management, MSSP oversight, GRC, and standards |
| Emergency Management and Resilience Manager | RRA and ERP program lead for the 3 covered systems; LEPC coordination |
| Water Quality and Compliance Manager | Public notice and state reporting decisions; AI program lead (P10) |
| General Counsel | Legal decisions on notices, contracts, and privilege |
| Co-sourced internal audit firm | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain one information security program that covers business IT and OT, documented in this policy set, the supporting standards, and the System Security Plan for the IWOS. (PM-1; GV.PO-01)
4.2 The IT Director is the designated security officer, and the Director of Water Operations is the designated operations owner for OT. Both designations must be in writing and reaffirmed each year. (PM-2; GV.RR-02)
4.3 An enterprise risk assessment must be performed at least annually and after any acquisition, new interconnection, or major OT change, using NIST SP 800-30 Rev. 1. Its system-level views for each covered water system are the cybersecurity addendum to that system's RRA. (RA-3; PM-9; ID.RA-05; 42 U.S.C. 300i-2(a)(1)(A)(i)-(ii))
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. No risk that could plausibly lead to unsafe water reaching customers may be accepted above Low. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, incidents, and SDWA certification status. (CA-5; GV.OV-01)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months or less. (PL-1)
4.8 **Sanctions.** Workforce members who violate security policies are subject to discipline in proportion to intent and harm. Contractors who violate them may lose access and be removed from company work. HR documents each sanction. (PS-8; GV.RR-04)
4.9 **SDWA section 1433.** For each covered system, the Emergency Management and Resilience Manager must keep the RRA and ERP current, track the certification dates, incorporate RRA findings (including the cybersecurity addendum) into the ERP within 6 months of each RRA certification, coordinate with the local emergency planning committee, and keep both documents for at least 5 years after each certification. (PL-2; CP-2; GV.OV-01; 42 U.S.C. 300i-2(a)(3)(B), (b), (c), (d))
4.10 **Vendors and integrators.** No vendor may receive remote access to OT, or access to customer or client data, until its contract contains the security terms in STD-08 and it has passed a review scaled to its tier. Tier 1 vendors, including every SCADA integrator, must be reviewed each year. (SA-9; SR-6; GV.SC-05; GV.SC-07)
4.11 **Engineered safeguards.** No change may weaken the hardwired chemical feed limits, hardwired analyzer alarms, SCADA alarms, or the ability to operate any plant in manual mode. No path from the cloud, an AI tool, or any external system may write to SCADA or a controller without a risk assessment and the COO's written approval. (SC-24; CM-3; PR.IR-03)
4.12 **Acquisitions.** Before an acquired water system is connected to the ROC or any company network, it must have an OT security assessment, an entry in the risk register, and the minimum controls in STD-07. Until then it stays isolated, and remote access to it goes only through the company gateway. (CA-3; SA-4; RA-3; GV.RM-01)
4.13 Security controls must be independently assessed at least annually (P07) and after major changes. (CA-2; GV.OV-01)
4.14 Security policies, risk assessments, assessment results, incident records, and decision logs must be kept for at least 5 years. RRAs and ERPs must be kept for at least 5 years after each certification. (SI-12; GV.PO-02; 42 U.S.C. 300i-2(d))
4.15 AI tools that use company data, interact with customers, or inform operational decisions must be approved through the AI governance process before use (STD-10; P10). (PM-9; RA-3; GV.RM-01)

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), quarterly access reviews, the SDWA certification calendar, and the metrics reported to the audit committee. Violations are handled under statement 4.8.

## 6. Exceptions
Exceptions follow statement 4.7. They must be written, risk-rated, approved by the right authority under statement 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); Gap Analysis and roadmap (P03); RRAs and ERPs for the Regional, Lakes, and Ridge Systems; 42 U.S.C. 300i-2.

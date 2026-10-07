# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | VP Operations |
| Approved by | VP Operations; security budget and High-risk acceptance rules confirmed by the CEO |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes, incidents, or a change in CFATS or CIRCIA status |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-3, PS-8, RA-1, RA-3, CA-2, CM-3, SA-9 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, ID.IM-02 |
| Benchmarks and rules | C-CHEMICAL-R01 (6 CFR 27.230(a)(8), (a)(12), (a)(17), voluntary benchmark); 40 CFR 68.15, 68.50 (EPA RMP); NIST CSF 2.0 with SP 800-82 Rev. 3 |

## 1. Purpose
Set up the Cris Santos Company security program for both office IT and the plant's operational technology (OT), assign who is accountable, and give the other security policies their authority. At this plant, security protects people and the community as well as information. A compromised control system can cause a toxic release.

## 2. Scope
All workforce members (employees, temporary staff, and contractors, including the DCS integrator and the data science contractor), all company systems and data, and all OT: the DCS, batch management system, SIS, PLCs, historian, OT network, and the loading rack. Includes systems that vendors operate for the company (ERP, cloud tenant, HR and payroll).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| CEO | Approves the security budget; accepts High and Very High risks |
| VP Operations | Program owner; approves policies; accepts Moderate risks |
| Plant Manager | Owner of the process control system; RMP qualified person; confirms that treatments for toxic release risks are adequate |
| IT Manager (security officer for IT and OT) | Runs the program day to day; maintains the risk register, SSP, and POA&M; chairs the monthly OT security meeting |
| Controls Engineer | Accountable for implementing OT security; approves DCS, SIS, and OT network changes |
| EHS Manager | Physical security, CVI custody, release reporting, and the link to the RMP |
| All workforce | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain a security program that covers IT and OT, documented in this policy set, the System Security Plan for the PCBMS (P02), and the POA&M (P07). The program uses NIST CSF 2.0 with SP 800-82 Rev. 3 as its OT benchmark and CFATS RBPS 8 as a voluntary benchmark. (PM-1; GV.PO-01)
4.2 The IT Manager is the security officer for IT and OT. The Controls Engineer is accountable for OT implementation. Both designations must be in writing. (PM-2; GV.RR-02; 27.230(a)(17))
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Risks must be tracked in the risk register with an owner and a treatment. (RA-3; PM-9)
4.4 **Risk acceptance.** The IT Manager may accept Low and Very Low risks (with the Controls Engineer for OT). The VP Operations may accept Moderate. Only the CEO may accept High or Very High, temporarily and with a dated treatment plan. **A risk that could cause a toxic release reaching the public may not be accepted at High.** It must be treated, and the Plant Manager must agree that the treatment is adequate. (PM-9; GV.RM-01)
4.5 Security policies must be reviewed at least annually, and after major changes or incidents. (PL-1; GV.PO-02)
4.6 Exceptions to any security policy must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months. (PL-1)
4.7 **Sanctions.** Workforce members who break security policies are subject to discipline in proportion to intent and harm: retraining, written warning, suspension, or termination. Contractors may be removed from site. HR documents each sanction. (PS-8; GV.RR-04)
4.8 **Third parties.** Before a vendor gets access to OT, formulations, or employee data, it must sign an agreement with security clauses: named accounts, MFA, screening attestations for staff with process access, incident notice within 24 hours, and return or destruction of data. The Controller must review key vendors' SOC 2 reports every year. (SA-9; GV.SC-05; 27.230(a)(12))
4.9 Security controls must be assessed at least annually (P07) and after major changes. (CA-2; ID.IM-02)
4.10 Cyber risks to the process must be included in RMP hazard reviews. The EHS Manager must invite the Controls Engineer and IT Manager to each hazard review and revalidation. (RA-3; 40 CFR 68.50(a)(2))
4.11 **Management of change for control systems and regulatory limits.** Changes to DCS logic, setpoints, alarms, SIS logic, PLC programs, master recipes, and the IT/OT firewall must go through MOC. The Controls Engineer must approve them, and a second person must approve recipe changes. MOC must also block two changes without a new regulatory review by the EHS Manager: buying hydrogen peroxide at 52% or higher, and holding more than 4 totes of isopropyl alcohol. Either change would bring the plant under OSHA PSM and move the ammonia process to RMP Program 3. (CM-3; PR.PS-01; 40 CFR 68.48(c), 68.50(d), 68.52(c))
4.12 Background checks are required at hire for all employees, and screening attestations are required for contractors with access to restricted areas or OT. (PS-3; 27.230(a)(12))
4.13 The EHS Manager must track regulatory status at least quarterly (CFATS reauthorization, CIRCIA final rule, RMP amendments, SP 800-82 revisions) and report changes to the VP Operations. (GV.OC-03)

## 5. Compliance and enforcement
Violations are handled under section 4.7. Compliance is checked through the annual control assessment (P07), the monthly OT security meeting, and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow section 4.6. They must be written, risk-rated, and approved by the policy owner (or by the CEO for High risk), and they expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); Gap Analysis (P03); MOC procedure; RMP management system document; 6 CFR 27.230 (voluntary benchmark); 40 CFR Part 68

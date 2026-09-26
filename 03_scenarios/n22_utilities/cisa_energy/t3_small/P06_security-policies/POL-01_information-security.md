# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | President |
| Approved by | President |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, incidents, or a TSA designation |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-9, RA-3, CA-2, SA-4, SA-9, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.SC-05, GV.OC-03, ID.RA-05 |
| Pipeline safety link | 49 CFR 192.631(f) (change management); 49 CFR 192.605 and 192.615 |

## 1. Purpose
Set up the Cris Santos Company cybersecurity program for both business IT and the Pipeline SCADA and Gas Control System (OT), assign who is accountable, and give every other security policy its authority. The program protects the safe and reliable operation of the pipeline first, then the confidentiality, integrity, and availability of company information.

## 2. Scope
All Cris Santos Company employees, contractors, and suppliers with access to company systems, at HQ and the Gas Control Center, Compressor Station 1, the field offices, and all field sites. It covers business IT, OT (SCADA, field devices, telecommunications, and the IT/OT DMZ), the cloud tenant, and SaaS services, including systems that suppliers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Majority owner | Approves the security budget; accepts High and Very High risks |
| President | Program owner; approves policies; accepts Moderate risks; approves any precautionary pipeline shutdown for cyber reasons |
| IT Manager | Security program lead; maintains the risk register, SSP, and policy set; business IT security |
| SCADA Engineer | OT security: accounts, remote access, backups, patching, and monitoring for the PSGCS |
| Gas Control Manager | Makes sure security changes to SCADA follow control room management procedures (192.631) |
| VP Operations | System owner of the PSGCS; integrates cyber events into the O&M manual and emergency plan |
| All personnel | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain a cybersecurity program covering business IT and OT, documented in this policy set and the System Security Plan. (PM-1; GV.PO-01)
4.2 The IT Manager is the security program lead and the SCADA Engineer is responsible for OT security. Both designations must be in writing and in their position descriptions. (PM-2; PS-9; GV.RR-02)
4.3 A risk assessment covering business IT and OT must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Risks must be tracked in the risk register with an owner and treatment. (RA-3; PM-9; ID.RA-05)
4.4 Risk acceptance authority: the IT Manager (business IT) or Gas Control Manager (OT) may accept Low risks; the President, Moderate; the majority owner, High and Very High. A risk that could cause loss of pipeline control or public harm may not be accepted at High without a dated treatment plan. (PM-9; GV.RM-01)
4.5 Security policies must be reviewed at least annually and updated after major changes, incidents, or a change in regulatory status. (PL-1; GV.PO-02)
4.6 Exceptions to any security policy must be requested in writing, risk-rated, approved per 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.7 **Pipeline safety comes first.** No security control may be installed, changed, or tested on OT in a way that could affect control room operations unless it has gone through the management of change process with Gas Control sign-off, as 49 CFR 192.631(f) requires. (CM-3; GV.OC-03)
4.8 Suppliers with access to OT or to Restricted information must have written security requirements in their contract before access is granted. The requirements must cover remote access rules, incident notice within 24 hours, and return or destruction of company data at the end of the contract. (SA-4; SA-9; GV.SC-05)
4.9 Security controls must be assessed at least annually (P07), with at least one-third of the controls in the SSP assessed each year and all of them over three years. (CA-2; ID.IM-02)
4.10 **TSA designation.** If TSA notifies the company that its pipeline is critical, the Pipeline Safety and Compliance Manager must tell the President the same day. The IT Manager must then confirm receipt to TSA as the directive requires and start a compliance project against the directive's deadlines, using the P03 readiness rows. (PM-1; GV.OC-03)
4.11 Security documentation (policies, risk assessments, assessment results, incident records) must be kept for at least 3 years. Records that PHMSA or the FPSC requires, including 192.631(j) records, must be kept for the period those rules require. (SI-12; GV.PO-02)

## 5. Compliance and enforcement
Violations may lead to retraining, written warning, loss of access, or termination, depending on intent and impact. For contractors, violations may lead to removal of access and contract action. Compliance is checked through the annual control assessment (P07) and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); control room management manual; O&M manual (49 CFR 192.605); emergency plan (49 CFR 192.615)

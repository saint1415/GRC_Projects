# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, exercises, or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, AU-6 |
| CSF 2.0 | ID.IM-02, ID.IM-04, RS.MA-01, RS.MA-02, RS.MA-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01 |
| Regulatory basis | TSA SD Pipeline-2021-02G Sections III.D.4 and III.F; SD Pipeline-2021-01G Section II.C; 49 CFR 191.5; 49 CFR 192.615; 49 CFR 192.631(b)(3), (g) |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from cybersecurity incidents while keeping the pipeline and the operated laterals safe, and meets every notice deadline. This policy is the policy basis for the TSA-approved Cybersecurity Incident Response Plan and the P08 runbooks.

## 2. Scope
All employees, contractors, authorized representatives, and managed service providers, at all sites. It covers business IT, OT, the cloud landing zone, SaaS services, and incidents at suppliers that affect company systems or data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for cyber incidents; Cybersecurity Coordinator; owns the TSA incident response plan |
| Director of Gas Control | Operations lead in any cyber incident; authority to isolate OT from IT at any time |
| Controller and shift supervisor on duty | Safety actions without waiting for IT; vendor session decisions; first notices to lateral owners |
| SCADA and OT Engineering Manager | OT technical lead: isolation, evidence, rebuild |
| Chief Operating Officer | Chairs the crisis management team; approves any precautionary shutdown for cyber reasons |
| Chief Executive Officer | Ransom decisions with the board chair; external statements; board notice |
| General Counsel | Privilege, breach determinations, contract notices, law enforcement contact |
| Director of Pipeline Safety and Compliance | Decides on and makes Part 191 notices |
| VP Commercial and Director of Regulatory Affairs | Shipper, interconnect, and lateral owner notices; FERC postings |
| MSSP and incident response retainer | 24x7 detection and business IT containment; forensics under counsel |
| All personnel | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain the TSA-approved Cybersecurity Incident Response Plan and runbooks for its most likely and most severe incidents, starting with (1) ransomware on business IT that could lead to a precautionary shutdown and (2) suspected OT compromise through a vendor path (P08). The plan must name the position responsible for each measure and the resources needed, and must be integrated with the emergency plan required by 49 CFR 192.615. (IR-8; CP-2; ID.IM-04; SD 02G III.F)
4.2 Anyone who suspects an incident must report it **immediately**, and within 1 hour at most, to the security incident line. Anything that affects SCADA, HMIs, station controls, field devices, or what a controller sees must be reported to the controller on duty at once. Good-faith reporting is never punished. (IR-6; RS.MA-02)
4.3 Every incident must be logged with the time of identification, given a severity (1 Critical: OT affected or suspected; 2 High: business IT disruption, data theft, or a supplier incident affecting company systems; 3 Moderate: contained single system; 4 Low: attempt blocked), and tracked to closure. (IR-5; RS.MA-03)
4.4 **Safety first.** A controller never waits for IT to take a safety action. Controllers follow the control room management and emergency procedures for any abnormal or emergency condition, whatever its cause. (IR-4; 192.631(b)(3))
4.5 **Isolation authority.** The Director of Gas Control, or the shift supervisor on duty if the Director cannot be reached at once, may close the IT/OT DMZ connections at any time when a business IT incident could spread to OT. Isolation must not wait for proof of compromise. The isolation capability must be performed live at least once a year. (IR-4; SC-7; RS.MI-01; SD 02G III.D.4, III.F.1.d)
4.6 **Shutdown decision.** A precautionary shutdown or curtailment for cyber reasons must follow the operate-or-shut-down criteria in the P08 runbooks, which are tied to the BIA, and be approved by the COO. This does not limit a controller or field supervisor who must act at once for safety under 192.615. (IR-4; CP-2; SD 02G III.F.1.d)
4.7 **Containment and evidence.** Infected devices must be contained promptly and segregated, with volatile memory captured before powering off where it is safe and vendor-approved, and affected equipment labeled. Backups must be checked for integrity and malicious code before any restore. (IR-4; CP-9; SD 02G III.F.1.a-c)
4.8 **Reporting to CISA.** The Cybersecurity Coordinator must report every cybersecurity incident covered by SD 01G to CISA as soon as practicable and no later than 72 hours after identification, with supplemental information within 24 hours of it becoming available. The shift supervisor may make the report if no Coordinator can be reached. (IR-6; RS.CO-02; SD 01G II.C)
4.9 Other notices to the National Response Center, PHMSA, shippers, interconnecting operators, lateral owners, state officials, the insurer, and affected individuals must meet the deadlines in the P08 notification matrix. The Director of Pipeline Safety and Compliance decides on Part 191 notices. The General Counsel confirms any breach notice. (IR-6; RS.CO-03)
4.10 No ransom may be paid without an OFAC sanctions check, General Counsel and insurer review, and approval by the CEO and the board chair. (IR-4)
4.11 The plan must be exercised at least annually, testing at least two of its objectives (containment, segregation, backup integrity, IT/OT isolation), with the positions named in the plan as active participants, including controllers, shift supervisors, the MSSP, and from 2027 the compressor station technicians. (IR-3; ID.IM-02; SD 02G III.F.1.e)
4.12 Lessons learned must be documented within 30 days of closing a Severity 1 or 2 incident or an exercise. They must be added to the risk register and the POA&M and, where control room actions were involved, to the controller training program (192.631(g)). (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations may lead to retraining, written warning, loss of access, or termination, depending on intent and impact. For contractors, violations may lead to removal of access and contract action. Compliance is checked through the annual exercise, the control assessment (P07), and TSA inspections.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may remove the controller's safety authority in 4.4 or delay a CISA report beyond 72 hours.

## 7. Related documents
P08 runbooks and notification matrix; TSA Cybersecurity Incident Response Plan (SSI); emergency plan (49 CFR 192.615); manual operation plan (192.631(c)(3)); STD-02; STD-07; POL-01

# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | President |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | ID.IM-04, RS.MA-01, RS.MA-02, RS.MA-03, RS.CO-02, RS.MI-01, RC.RP-01 |
| Pipeline safety link | 49 CFR 192.615 (emergency plans); 49 CFR 191.5; Rule 25-12.084, F.A.C. |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from cybersecurity incidents while keeping the pipeline safe, and meets every notice deadline.

## 2. Scope
All Cris Santos Company employees, contractors, and suppliers with access to company systems, at HQ and the Gas Control Center, Compressor Station 1, the field offices, and all field sites. It covers business IT, OT (SCADA, field devices, telecommunications, and the IT/OT DMZ), the cloud tenant, and SaaS services, including systems that suppliers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for cyber incidents; coordinates the MSP, the IR retainer, and the insurer |
| Gas Control Manager | Operations lead during a cyber incident; has authority to isolate OT from IT at any time |
| SCADA Engineer | OT technical lead: isolation, evidence, rebuild |
| President | Approves any precautionary pipeline shutdown for cyber reasons, ransom decisions, and external statements |
| Pipeline Safety and Compliance Manager | Decides on and makes pipeline incident notices (NRC, PHMSA, FPSC) |
| Commercial Manager | Notifies customers and the upstream pipeline |
| All personnel | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain a cybersecurity incident response plan and runbooks for its most likely incidents, starting with ransomware on business IT (P08). The plan must be integrated with the emergency plan required by 49 CFR 192.615. (IR-8; CP-2; ID.IM-04)
4.2 Anyone who suspects an incident must report it **immediately**, and within 1 hour at most, to the IT Manager's incident line. Anything that affects SCADA, HMIs, field devices, or what a controller sees must be reported to the controller on duty at once. Good-faith reporting is never punished. (IR-6; RS.MA-02)
4.3 Every incident must be logged, given a severity level (1 Critical: OT affected or suspected; 2 High: business IT disruption or data theft; 3 Moderate: contained single system; 4 Low: attempt blocked), and tracked to closure. (IR-5; RS.MA-03)
4.4 **Safety first.** A controller must never wait for IT to take a safety action. Controllers follow the control room management and emergency procedures for any abnormal or emergency condition, whatever the cause. (IR-4; 192.631(b)(3))
4.5 **Isolation authority.** The Gas Control Manager, or the controller on duty if the manager cannot be reached, may close the IT/OT DMZ connections at any time when a business IT incident could spread to OT. Isolation must not wait for proof of compromise. (IR-4; SC-7; RS.MI-01)
4.6 **Shutdown decision.** A precautionary shutdown or curtailment for cyber reasons must follow the decision criteria in the P08 runbook and be approved by the President, except where a controller or field supervisor must act at once for safety under 192.615(a)(6). (IR-4; CP-2)
4.7 Notices to the National Response Center, PHMSA, the FPSC, CISA, law enforcement, customers, the insurer, and affected individuals must meet the deadlines in the P08 notification matrix. The Pipeline Safety and Compliance Manager decides on pipeline incident notices. Legal counsel confirms any breach notice. (IR-6; RS.CO-02)
4.8 No ransom may be paid without approval from the majority owner, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.9 The plan must be exercised at least annually by a tabletop that tests at least two of these objectives: containment, IT/OT isolation, backup integrity, and recovery. The exercise must include the controllers, the SCADA Engineer, the IT Manager, and the MSP. (IR-3; ID.IM-02)
4.10 Lessons learned must be documented within 30 days of closing an incident. They must be added to the risk register and, where control room actions were involved, to the controller training program (192.631(g)). (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations may lead to retraining, written warning, loss of access, or termination, depending on intent and impact. For contractors, violations may lead to removal of access and contract action. Compliance is checked through the annual control assessment (P07) and the annual exercise.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; emergency plan (192.615); manual operation plan (192.631(c)(3)); POL-01

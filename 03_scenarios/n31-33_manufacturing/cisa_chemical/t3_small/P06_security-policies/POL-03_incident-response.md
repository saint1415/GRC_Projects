# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | VP Operations |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Benchmarks and rules | C-CHEMICAL-R01 (6 CFR 27.230(a)(8), (a)(15), (a)(16), voluntary benchmark); 40 CFR 302.6; 40 CFR 355.40-355.43; 40 CFR 68.60, 68.90(b), 68.96(a); Fla. Stat. 501.171 (employee personal information) |

## 1. Purpose
Make sure the company detects, responds to, reports, and recovers from security incidents in a way that **keeps the process safe first** and meets its reporting duties.

## 2. Scope
All workforce members and contractors, all systems, and all OT. Covers cyber incidents and suspicious events that could affect process safety, product quality, chemical security, or personal information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Plant Manager | Incident commander when the process is affected; decides on safe state and restart |
| IT Manager | Cyber incident lead; runs the runbook; coordinates forensics and the insurer |
| Controls Engineer | OT technical lead; isolates and restores the DCS and SIS |
| EHS Manager | Release reporting (NRC, SERC, LEPC), coordination with county fire rescue, RMP incident investigation |
| Shift Supervisors | First responders; put the process in a safe state and call the incident line |
| Controller | Insurer notice; approves emergency spending |
| Customer Service Manager | Customer communication, approved by the VP Operations |

## 4. Policy statements
4.1 The company must maintain an incident response plan that covers IT and OT, plus a runbook for its highest-risk incident type (P08: intrusion into process control systems). (IR-8; RS.MA-01)
4.2 Workforce members must report suspected incidents **immediately** to their Shift Supervisor or the incident line. That includes unexplained setpoint or alarm changes, unexpected HMI behavior, ransom notes, or phishing. If a cyber cause is suspected, operators must treat the event as a process upset and follow the operating procedure for loss or compromise of the DCS. (IR-6; RS.MA-02)
4.3 **Safety first.** When an incident may affect the process, the first objective is a safe state. The process must not be restarted on a DCS that has not been verified against the configuration baseline. (IR-4; RC.RP-01; 40 CFR 68.52(b)(4))
4.4 Incidents must be triaged, categorized, logged in the ticketing system under the security category, and tracked to closure. (IR-4; IR-5; 27.230(a)(16))
4.5 **Release reporting comes first.** If a release of ammonia or another hazardous substance reaches or may exceed its reportable quantity, the notices to the National Response Center, SERC, and LEPC must go out immediately, whatever the cause (40 CFR 302.6; 355.43). All other notices follow the notification matrix (P08). (IR-6; RS.CO-02)
4.6 The emergency notification path must work without the business network: cellular phones and printed call lists in the control room and gatehouse. (CP-8; 40 CFR 68.90(b)(3))
4.7 **Ransom payments** need approval from the CEO, legal counsel, and the insurer, and an OFAC sanctions check first. (IR-4)
4.8 Evidence must be preserved: DCS event journals, SIS event logs, firewall logs, and images of affected workstations, with chain of custody. Any RMP incident investigation must ask whether a control system was tampered with. (IR-4; 40 CFR 68.60)
4.9 The plan must be tested at least annually with an OT tabletop exercise. The yearly RMP notification exercise must include a case where the business network is down. (IR-3; ID.IM-02; 40 CFR 68.96(a))
4.10 Operators, I&E technicians, and integrator staff must be trained to recognize when a process anomaly may have a cyber cause. (IR-2)
4.11 Lessons learned must be documented within 30 days of closing a significant incident and fed into the risk register (P01) and the POA&M (P07). (ID.IM-02)
4.12 An OT contingency plan, based on the BIA (P05), must define safe-state, recovery, and restart steps for the PCBMS. (CP-1; CP-2)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Compliance is checked through the annual control assessment (P07) and the yearly exercises.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. No exception may delay a release notification.

## 7. Related documents
P08 OT incident runbook and notification matrix; RMP emergency action plan; incident investigation procedure; P05 BIA; POL-01; CISA and FBI voluntary reporting guidance

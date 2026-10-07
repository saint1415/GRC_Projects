# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), after every significant incident, and after each exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AU-2, AU-6, AU-11, SI-4 |
| CSF 2.0 | RS.MA-01, RS.AN-03, RS.AN-06, RS.AN-07, RS.CO-02, RS.CO-03, DE.CM-01, ID.IM-03 |
| SP 800-171 Rev. 2 and contract clauses | 3.3.1, 3.3.5, 3.6.1 to 3.6.3, 3.14.6; DFARS 252.204-7012(c) to (g), (m)(2)(ii) |
| Supporting standards | STD-02 Logging and monitoring; STD-07 Contingency and recovery |

## 1. Purpose
Make sure the company detects, contains, and recovers from security incidents quickly, meets its DoD reporting and evidence duties, and protects CUI, production, and its contracts while doing so.

## 2. Scope
All suspected or confirmed incidents affecting company systems, CUI, shop-floor systems, services customer data, or data held for the company by suppliers and service providers, at both plants and in the cloud.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Crisis management team (chair: COO) | Business decisions, external statements, ransom recommendation to the CEO |
| Security Manager | Incident commander; maintains the plan and runbooks |
| MSSP | 24x7 detection, triage, and containment actions approved in the playbooks |
| Director of Trade Compliance and Contracts | DIBNet reports, prime notices, export control decisions |
| General Counsel | Privilege, outside counsel, employee data breach decisions |
| IT Director and Manufacturing Systems Manager | Recovery of cloud, network, and shop-floor systems |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must keep an incident response plan and runbooks for its main incident types (P08), with a crisis management team, an incident response team, and plant command roles. (IR-8; RS.MA-01; 3.6.1)
4.2 Every workforce member must report suspected incidents, phishing, lost devices, and unusual shop-floor behavior to the security team at once, by phone if systems are down. (IR-6; 3.6.2)
4.3 The MSSP must call the Security Manager within 30 minutes of a high-severity alert. The Security Manager declares incidents and records the time of discovery. (IR-4; SI-4)
4.4 **DoD reporting.** A cyber incident that affects a covered contractor information system or the covered defense information in it must be reported to DoD at https://dibnet.dod.mil within 72 hours of discovery (DFARS 252.204-7012(c)). At least two named people must hold current DoD-approved medium assurance certificates and be able to report from a clean endpoint. The DoD-assigned incident report number must go to the affected prime as soon as practicable (252.204-7012(m)(2)(ii)). The report is never delayed for internal review. (IR-6; RS.CO-02)
4.5 **Evidence preservation.** Images of all known affected systems and relevant monitoring and packet capture data must be preserved for at least 90 days from submission of the DoD report (252.204-7012(e)). No affected system, including MES, DNC, or shop-floor servers, may be wiped or rebuilt before it is imaged, unless the incident commander documents that safety or production requires it and captures what can be captured. (IR-4; AU-11; RS.AN-07)
4.6 Malicious software isolated in connection with a reported incident must be submitted to the DoD Cyber Crime Center (DC3) as instructed, never to the Contracting Officer (252.204-7012(d)). (IR-4)
4.7 For any incident in which CUI or export-controlled data may have reached an unauthorized person, the Director of Trade Compliance and Contracts must decide, with export counsel, whether a voluntary disclosure is warranted, and record the reasoning. (IR-6)
4.8 General Counsel decides when outside counsel directs the investigation. Analysis prepared at counsel's direction is labeled privileged. (IR-4)
4.9 **Testing.** The plan must be exercised at least annually. Over each 2-year cycle, exercises must cover CUI exfiltration with a DIBNet reporting drill, ransomware on shop-floor systems, and a supplier incident. (IR-3; ID.IM-03; 3.6.3)
4.10 **Logging and monitoring.** All in-scope systems, including MES, DNC, OT gateways, and plant firewalls, must send security logs to the SIEM. Logs are kept 1 year searchable and 6 years in the write-once archive (STD-02). (AU-2; AU-6; AU-11; 3.3.1; 3.3.5; 3.14.6)
4.11 **Extortion and ransom.** No payment may be made without the CEO's decision after advice from counsel, the insurer, and an OFAC sanctions check. Paying never removes a reporting duty. (IR-4)
4.12 **Supplier incidents.** Suppliers that hold company CUI must report incidents to DoD under their own flowed-down clause and tell the company promptly; the company coordinates with the affected prime. (IR-6; RS.CO-03)
4.13 A lessons-learned review must be held within 14 days of containment and documented within 30 days, with updates to the risk register, POA&M, and runbooks. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.8. Compliance is checked through exercise reports, the incident log, and the co-sourced internal audit (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may remove a DFARS 252.204-7012 reporting or preservation duty.

## 7. Related documents
POL-01; POL-02; STD-02; STD-07; P08 runbooks and notification matrix; BIA (P05)

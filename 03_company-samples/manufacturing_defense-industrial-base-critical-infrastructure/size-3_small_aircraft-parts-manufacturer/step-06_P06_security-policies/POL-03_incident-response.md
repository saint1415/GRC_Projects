# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | Vice President of Operations (2026-08-31) |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or assessment findings |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AU-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| SP 800-171 Rev. 2 and contract clauses | 3.6.1 to 3.6.3; DFARS 252.204-7012(c) to (g), (m)(2)(ii); FAR 52.204-25(d) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from cyber incidents quickly and lawfully, and meets its DFARS reporting and evidence preservation duties.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary workers, and contractors) at the Florida plant and working remotely. Covers all company systems and data, with added rules for the CUI Engineering Enclave (CEE) defined in the SSP (P02), printed CUI on the shop floor, and systems that service providers operate for the company. It applies to controlled unclassified information (CUI), including controlled technical information and export-controlled technical data, federal contract information (FCI), and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander; coordinates the forensic retainer and the cloud provider |
| Contracts Manager | DoD reporting through DIBNet; prime notifications; DoD liaison; export control assessment |
| Vice President of Operations | Engages counsel and the cyber insurer; approves external communications |
| Director of Engineering | Identifies which CUI and programs were affected |
| Controller | Cyber insurance notice |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with exfiltration of CUI (P08). (IR-8; RS.MA-01; 3.6.1)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the IT help line or their supervisor. Examples: phishing clicks, lost devices, CUI sent to the wrong place, CUI pasted into an unapproved tool, unusual system behavior. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category. (IR-5; 3.6.1)
4.4 When a cyber incident affects a covered contractor information system or the CUI in it, the company must review for evidence of compromise of covered defense information and **report to DoD at https://dibnet.dod.mil within 72 hours of discovery**, using a DoD-approved medium assurance certificate. The Contracts Manager must give the DoD-assigned incident report number to Prime A or Prime B as soon as practicable. (IR-6; RS.CO-02; 252.204-7012(c); (m)(2)(ii))
4.5 The company must keep at least two people able to report to DIBNet (the Contracts Manager and the IT Manager), each with a current medium assurance certificate. (IR-6; 252.204-7012(c)(3))
4.6 Malicious software isolated in connection with a reported incident must be submitted to the DoD Cyber Crime Center (DC3) as DC3 or the Contracting Officer instructs, never to the Contracting Officer. (IR-4; 252.204-7012(d))
4.7 Images of all known affected systems and relevant monitoring and packet capture data must be preserved for at least 90 days from submission of the report. Affected systems must not be wiped or rebuilt until images are captured. Logs are retained for 1 year. (IR-4; AU-11; 252.204-7012(e))
4.8 The company must give DoD access to additional information or equipment for forensic analysis on request, and provide damage assessment information if the Contracting Officer asks. (IR-7; 252.204-7012(f), (g))
4.9 The incident response plan must be tested at least annually by a tabletop that includes a DIBNet reporting drill, and after any major incident. (IR-3; ID.IM-02; 3.6.3)
4.10 Lessons learned must be documented within 30 days of closing an incident and added to the risk register and training. (IR-4; ID.IM-03)
4.11 No ransom or extortion payment may be made without approval from the President, legal counsel, and the cyber insurer, and an OFAC sanctions check. Paying never removes a reporting duty. (IR-4)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. A suspected unauthorized release of ITAR or EAR technical data is also referred to the Contracts Manager (Empowered Official) for a voluntary disclosure decision. Compliance is checked through the annual self-assessment against SP 800-171A objectives, the control assessment (P07), and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), recorded in the risk register, and expire within 12 months. An exception never removes a DFARS 252.204-7012 duty or permits an unauthorized export.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; POL-04; DFARS 252.204-7012; Fla. Stat. 501.171 (employee personal information only)

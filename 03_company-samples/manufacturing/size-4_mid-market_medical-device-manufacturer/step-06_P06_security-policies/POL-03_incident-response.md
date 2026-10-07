# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager, with the Product Security Manager for product security incidents |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy and the 2025 PSIRT procedure's governance sections) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-02, RC.RP-01, ID.IM-02 |
| Regulatory basis | FD&C Act 524B(b)(1)-(2) (N31-33-R05); 21 CFR 803.50, 803.53, 806.10, 806.20, 820.35(a); FDA postmarket cybersecurity guidance (2016, nonbinding); HIPAA 164.308(a)(6) and 164.410 (N62-R01, N62-R03); state third-party agent notice laws (Florida example: Fla. Stat. 501.171(6)) |
| Supporting standards | STD-02 Logging and monitoring; STD-07 Contingency and recovery; STD-09 Vulnerability and patch management |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents, including incidents that affect its devices in the field, quickly enough to protect patients and to meet every FDA, HIPAA, state, and contract deadline.

## 2. Scope
All security incidents and suspected incidents affecting company systems or data, the CCC, the plant, and the company's fielded devices, and all vulnerabilities in company products that could cause uncontrolled risk.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for corporate and plant incidents; MSSP coordination |
| Product Security Manager | Incident commander for product security incidents; PSIRT lead |
| Chief Operating Officer | Chairs the crisis management team; approves customer advisories and external statements |
| General Counsel | Legal lead; engages outside counsel; privilege; law enforcement contact |
| VP QA/RA | Complaint, MDR, and correction and removal decisions |
| Compliance and Privacy Officer | Breach decisions and notices to hospitals; decision log |
| Plant Manager | Line shutdown and lot hold decisions |
| Chief Medical Officer | Patient safety assessment for product incidents |
| Director of Customer Support and Field Service | Hospital communications and field actions |
| Director of Marketing and Communications | Media and public statements through counsel |
| MSSP | 24x7 detection and first containment for IT and cloud; call within 30 minutes on high severity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely and most harmful incidents. At minimum these are an exploited vulnerability in a fielded device and ransomware in the plant OT (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the service desk security line. This includes hospital reports of unusual device behavior received by support or field service. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; 164.308(a)(6)(ii))
4.3 Every incident must be logged and tracked to closure. The log must record the date and time of discovery and, for product incidents, the date the company learned of the vulnerability, because different legal and guidance clocks start from each. (IR-5; IR-4)
4.4 Corporate and product incidents use one severity scale. A SEV-1 incident (exploitation with possible patient harm, tampering with the update or signing path, ransomware, or confirmed PHI exfiltration) must activate the crisis management team, chaired by the COO, within 2 hours. (IR-4; RC.RP-01)
4.5 Every product security incident must be screened as a possible complaint (21 CFR 820.35(a)) and evaluated by the VP QA/RA for MDR reporting (803.50, 803.53) and for correction or removal reporting (806.10). Each decision must be documented in the eQMS with its date. (IR-6; RS.CO-02; 21 CFR 803; 806)
4.6 **Uncontrolled risk.** For a vulnerability assessed as an uncontrolled risk, the company must communicate with customers within 30 days of learning of it, distribute a validated fix within 60 days, and share the communication with its ISAO, as FDA's postmarket guidance describes. A day-50 checkpoint confirms the fix date. If any condition cannot be met, the VP QA/RA must file an 806.10 report within 10 working days of initiating the correction. (IR-4; IR-6; RS.MI-02; 524B(b)(2)(B))
4.7 The Compliance and Privacy Officer must decide whether an incident is a breach of unsecured PHI under 45 CFR 164.402, document the assessment in the decision log, and notify each affected hospital by the shortest applicable clock: the BAA term, the state third-party agent law, or 164.410 (no later than 60 days after discovery). (IR-6; RS.CO-03; 164.410)
4.8 The cyber insurer must be notified through its hotline before incident response vendors are engaged. The General Counsel engages outside counsel, who directs forensic work under privilege where appropriate. (IR-7)
4.9 No ransom may be paid without approval from the CEO, the General Counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. (IR-4)
4.10 During a plant incident, the Plant Manager decides on line shutdown and lot holds. No lot may be released until its device history records and the firmware and certificate records for each unit are verified as complete and untampered. (CP-2; IR-4; 21 CFR 820.35)
4.11 Incident response must be exercised at least annually for each runbook, including one exercise a year that combines a product vulnerability, FDA decisions, and business associate notice, with outside counsel. (IR-3; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a major incident. Product incidents must also open a CAPA in the eQMS. Results feed the risk register (P01) and the POA&M (P07). (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), exercise reports, and the quarterly reconciliation of PSIRT tickets with complaint records. Violations are handled under POL-01 section 4.11.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal, regulatory, or contractual notification deadline.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-plant-ransomware.md`, and `notification-matrix.csv`; POL-01; STD-02; STD-07; STD-09; MDR, complaint handling, and correction and removal procedures (eQMS)

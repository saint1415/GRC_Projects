# Incident Response and Product Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations (enterprise incidents) and VP Product Security (product security incidents) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or product launches |
| Implements (SP 800-53 Rev. 5) | IR-1, CP-1, IR-8, IR-6, IR-5, IR-4, RA-5(11), PM-15, SI-2, CP-2, CP-4, CP-10, IR-3 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.RA-08, ID.IM-02 |
| Regulatory basis | FD&C Act 524B(b)(1)-(2) (N31-33-R05); 21 CFR 803, 806, 820.35; HIPAA 164.308(a)(6), (a)(7), 164.410 (N62-R01, N62-R03); 16 CFR 318 (N62-R06); SEC Form 8-K Item 1.05; state breach laws |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully, including incidents that affect fielded devices, and that vulnerability handling connects to complaint handling, FDA reporting, customer advisories, business associate and FTC notices, and SEC disclosure.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at every site: headquarters, the FL-1, MN-1, and TX-1 plants, the R&D centers, the RCM monitoring centers, and remote work, including the acquired infusion business from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, plant OT, the Device Software Factory, and systems that business associates, contract manufacturers, and other vendors operate for the company, and the products and services the company provides to customers and consumers (fielded devices, the DDC, the RCM service, and the consumer companion app).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for enterprise incidents; runs the SOC |
| VP Product Security | Incident commander for product security incidents; CVD coordinator |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| CQRO | Complaint, MDR, and correction and removal decisions; FDA communications |
| Chief Privacy Officer | Breach risk assessments; notices to customers under BAAs; FTC rule notices |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| CIO and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with an exploited vulnerability in a fielded device (P08) and ransomware. (IR-8; RS.MA-01)
4.2 Workforce, contract manufacturers, and vendors must report suspected incidents and vulnerability reports to the SOC or PSIRT within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure. Product security incidents must also be recorded in the eQMS and screened as possible complaints. (IR-5; IR-4; RS.MA-02)
4.4 The company must publish a coordinated vulnerability disclosure policy, acknowledge each report within 3 business days, keep reporters informed, coordinate public disclosure, and participate in an ISAO (STD-03.4). (RA-5(11); PM-15; ID.RA-08)
4.5 Every vulnerability affecting a device or related system must be assessed as controlled or uncontrolled risk to essential performance, and the CQRO must decide and document whether an MDR (21 CFR 803) or a correction or removal report (21 CFR 806.10) is required, or record the 806.20 justification. (IR-4; IR-6; RS.AN-03)
4.6 Critical vulnerabilities that could cause uncontrolled risks must be fixed out of cycle as soon as possible; customers must be told, with compensating controls, within 30 days of the company learning of an uncontrolled risk, and a fix distributed within 60 days. (SI-2; IR-4; RS.MI-02)
4.7 For a severity-1 incident, including a PSIRT severity-1, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). If the committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; IR-8; RS.CO-02)
4.8 The Chief Privacy Officer must document a four-factor breach risk assessment (45 CFR 164.402) for every incident involving PHI held for customers, and notices to customers must meet the BAA term and no later than 60 calendar days after discovery (164.410), and any shorter state agent deadline (Florida worked example: 10 days under Fla. Stat. 501.171(6)). (IR-6; RS.CO-03)
4.9 For the consumer app, the Chief Privacy Officer must determine whether an incident is a breach of security under 16 CFR 318.2, including an unauthorized disclosure, and notices to individuals, the FTC, and media must meet 16 CFR 318.4 (no later than 60 calendar days after discovery). (IR-6; RS.CO-03)
4.10 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.11 Tier-1 systems and business associate services must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually. (CP-2; CP-4; CP-10; RC.RP-01)
4.12 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee using a scenario that rotates between enterprise and fielded-device incidents. (IR-3; IR-8; ID.IM-02)
4.13 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register, the product risk management file, and the POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach and Regulatory Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- STD-03.4 Coordinated Vulnerability Disclosure Standard
- PRC-03.1 Fielded-Device Vulnerability Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Breach and Regulatory Notification Procedure
- PRC-03.4 Ransomware Runbook

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 DSF-MES SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.

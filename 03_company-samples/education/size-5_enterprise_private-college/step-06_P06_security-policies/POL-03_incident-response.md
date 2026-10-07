# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after material changes, incidents, or new service lines |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, ID.IM-03 |
| Key regulatory requirements | 16 CFR 314.4(h)(1)-(7), (j); SAIG Enrollment Agreement; 34 CFR 99.32(a); Form 8-K Item 1.05 |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully; meets the FSA, FTC, state, and SEC deadlines; and keeps instruction and student services running during outages. Together with its standards and the P08 runbook, this policy is the written incident response plan required by 16 CFR 314.4(h).

## 2. Scope
All Cris Santos Company workforce members (employees, including full-time and adjunct faculty, contractors, student workers, and volunteers) at headquarters, the 23 campuses, and the 4 student support centers, and all remote workers in any state. Covers all systems and data, including cloud, colocation, SaaS, and systems that vendors and the Title IV third-party servicer operate for the company, and the services the company offers to other organizations (SL-1 Workforce Education Services and SL-2 Online Program Services).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| CISO (Qualified Individual) | Executive incident lead; escalates to the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Privacy Officer | Notification event and breach determinations; FERPA disclosure records with the University Registrar |
| Vice President, Financial Aid | Reports to FSA |
| CIO and system owners | Recovery in BIA priority order |
| Vice President, Campus Operations | Campus emergency notification |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain a written incident response plan and runbooks that address the goals, internal processes, roles and decision authority, communications, remediation, documentation, and post-incident revision elements of 16 CFR 314.4(h), starting with ransomware with data exfiltration (P08). (IR-8; RS.MA-01)
4.2 Workforce members and vendors must report suspected incidents to the SOC within 1 hour of noticing them; vendor contracts must require notice within 72 hours. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in SOC case management; incidents that start at a vendor must use the vendor incident template, including the vendor notice timeline and containment confirmation. (IR-5; IR-4; RS.MA-02)
4.4 For an actual or suspected breach of student information or of the company's Department system access, the Vice President, Financial Aid must report to FSA immediately through the Cybersecurity Breach Intake, without waiting for forensic confirmation. (IR-6; RS.CO-02)
4.5 The Qualified Individual and counsel must document whether a notification event occurred and its discovery date; if 500 or more consumers are involved, the FTC must be notified as soon as possible and no later than 30 days after discovery. (IR-6; RS.CO-02)
4.6 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2), including Title IV and accreditation consequences. (IR-6; IR-8; RS.CO-02)
4.7 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.8 Notices to affected individuals, state regulators, and consumer reporting agencies must meet the deadlines in the P08 notification matrix for each state where affected individuals reside, and every unauthorized disclosure of education records must be entered in the affected students' FERPA disclosure records. (IR-6; RS.CO-03)
4.9 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.10 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually; a failed objective must be retested within 6 months. (CP-2; CP-4; CP-10; RC.RP-01)
4.11 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee and the FSA and FTC notification steps, and after major organizational changes. (IR-3; IR-8; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Ransomware Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Refund Fraud Response Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the Qualified Individual's annual report to the board. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 SRLP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.

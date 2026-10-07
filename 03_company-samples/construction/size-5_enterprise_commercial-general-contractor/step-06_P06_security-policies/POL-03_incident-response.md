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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-8, IR-6, IR-5, IR-4, CP-2, CP-4, CP-10, IR-3 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MI-01, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | N23-R03 (252.204-7012(c)-(g); SP 800-171 R2 3.6.1-3.6.3); SEC Form 8-K Item 1.05; 17 CFR 229.106(a); state breach laws (Fla. Stat. 501.171 worked example); FAR 52.232-33; OFAC advisory (2021-09-21) |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents and payment fraud quickly and lawfully; meets DoD, SEC, state, and contract deadlines; and keeps jobsites, billing, and payments running during outages.

## 2. Scope
All Cris Santos Company workforce members (employees, craft workers, contractors, and interns) at headquarters (HQ-1), the nine regional offices, about 140 jobsites, the two yards, and the two colocation data centers in eight states, including acquired businesses (AQ-1 and AQ-2) from their acquisition date. Covers all company systems and data, including cloud, colocation, SaaS, the Federal Programs CUI Enclave (FPCE), jobsite technology, client building systems that BTS administers, systems that vendors and subcontractors operate for the company, and the services the company offers to external clients (SL-1 and SL-2). Subcontractor and design-team users of company systems are bound by the security terms in their subcontracts and access agreements.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| CISO | Executive incident lead; briefs the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; personal information determinations; engages outside counsel |
| Vice President, Treasury | Payment response lead: bank recalls, payment holds, and payee freezes |
| Director of Government Contracts and Director, CMMC Program Office | CUI determination and DIBNet reporting; contracting officer notices |
| CIO and system owners | Recovery in BIA priority order (P05) |
| Chief Operating Officer | Activates the crisis management team for jobsite and project disruption |

Role overlaps are limited by design: Internal Audit (third line) never operates the controls it tests, and the people who maintain payees never release payments (POL-02 4.3).

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in the 2026 PDPP assessment (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with business email compromise that redirects payments (P08) and ransomware. (IR-8; RS.MA-01)
4.2 Workforce, acquired businesses, and vendors must report suspected incidents and suspicious payment requests to the SOC within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in SOC case management. (IR-5; IR-4; RS.MA-02)
4.4 When a payment may have been diverted, Treasury must request a bank recall within 1 hour of suspicion and the SOC must file an IC3 complaint the same day. (IR-4; RS.MI-01)
4.5 For a severity-1 incident or any payment fraud event, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours. The committee must assess related occurrences together. (IR-6; IR-8; RS.CO-02)
4.6 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.7 Every incident must include a CUI determination. A cyber incident affecting CUI must be reported through DIBNet within 72 hours of discovery, and images and monitoring data preserved for at least 90 days. (IR-6; RS.CO-02)
4.8 The General Counsel must document a personal information determination for every incident involving personal information, and notices must meet the deadlines in the P08 notification matrix for each state where affected individuals reside. (IR-6; RS.CO-03)
4.9 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.10 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually, including restore of SaaS data exports. (CP-2; CP-4; CP-10; RC.RP-01)
4.11 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee and a DIBNet reporting drill; lessons learned must be documented within 30 days. (IR-3; IR-8; ID.IM-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot weaken it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Business Email Compromise and Payment Fraud Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 DoD Cyber Incident Reporting (DIBNet) Procedure
- PRC-03.5 Ransomware Runbook

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certifications, monthly payment-control exception reports, the annual Internal Audit assessment (P07), and the CMMC self-assessments (P03). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Subcontractor and vendor violations are handled under their contracts and can lead to removal of access or the subcontract.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception can change how a CMMC requirement is scored.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 enterprise risk register; P02 PDPP SSP; P03 regulatory gap analysis (including the FPCE readiness check); P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI governance; FPCE SSP (separate, CMMC Level 2).

# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (and Cris Santos Payouts, LLC, under 23 NYCRR 500.2(d)) |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, new sponsor banks, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IR-8, IR-6, IR-5, IR-4, CP-2, CP-4, CP-10, IR-3 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, ID.IM-03 |
| Regulatory drivers | See `policy-control-map.csv` (one driver per statement) |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports security incidents quickly and lawfully; meets card brand, sponsor bank, FTC, NYDFS, state, and SEC deadlines; and keeps authorization and merchant funding running during outages.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) in every location, and Cris Santos Payouts, LLC, which adopted this program under 23 NYCRR 500.2(d). Covers all systems and data, including Cloud A, Cloud B, DC-1, DC-2, SaaS, and systems that service providers operate for the company, and the services the company provides to merchants, ISV partners, and sponsor Banks A, B, and C.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the Cyber Fusion Center |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Compliance Officer | Sponsor bank, card brand, FTC, NYDFS, and state notices |
| Senior Vice President, Settlement and Treasury Operations | Settlement recovery and the 4-hour bank notice determination with the incident commander |
| CTO, CIO, and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with compromise of the payment processing environment (P08) and ransomware, covering card brand, sponsor bank, FTC, NYDFS, state, and SEC duties. (IR-8; RS.MA-01)
4.2 Workforce members and service providers must report suspected incidents to the Cyber Fusion Center within 1 hour, including any card number found where it should not be. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in case management. (IR-5; IR-4; RS.MA-02)
4.4 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.CO-02)
4.5 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.6 When an incident affects authorization, clearing, settlement, reconciliation, or funding services, the incident commander and the Senior Vice President, Settlement and Treasury Operations must decide by the second hour whether the disruption has lasted or is reasonably likely to last 4 hours or more, and if so notify each affected bank's designated contacts as soon as possible (PRC-03.3). (IR-6; RS.CO-03)
4.7 All other notices must meet the deadlines in the P08 notification matrix, including card brand reports, the FTC notice, the NYDFS 72-hour notice, and third-party agent notices to merchants. (IR-6; RS.CO-03)
4.8 No ransom or extortion payment may be made without approval from the CEO, the General Counsel, and the cyber insurer, and an OFAC sanctions check. Any payment must be reported to NYDFS within 24 hours, with an explanation within 30 days. (IR-4; RS.MI-01)
4.9 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05), must pass a recovery test at least annually, including restoring from backups, and the sponsor banks must be invited to settlement recovery tests. (CP-2; CP-4; CP-10; RC.RP-01)
4.10 The incident response plan must be exercised at least annually with all staff and management critical to the response, including the disclosure committee and the President of Cris Santos Payouts, LLC, and after major organizational changes. (IR-3; IR-8; ID.IM-02)
4.11 A root cause analysis and lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Regulatory and Contractual Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Payment Environment Compromise Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Bank Service Provider Notice Procedure
- PRC-03.4 NYDFS Notice and Annual Filing Procedure
- PRC-03.5 Ransomware Response Runbook

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the PCI DSS quarterly reviews (PCI DSS 12.4.2), access certifications, and the annual Internal Audit assessment (P07). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 Core Payment Processing Platform SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.

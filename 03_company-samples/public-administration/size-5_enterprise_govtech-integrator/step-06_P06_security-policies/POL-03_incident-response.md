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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or new CJISSECPOL versions |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2, CP-4, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, ID.IM-03 |
| Key requirements | CJISSECPOL v6.1 IR-6; Pub. 1075 sec. 1.8; 45 CFR 164.410 (AG-04); Fla. Stat. 501.171(6); DFARS 252.204-7012(c); Form 8-K Item 1.05 |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports incidents quickly and lawfully, gives agencies what they need to meet their own reporting clocks, meets its own notice and SEC disclosure deadlines, and keeps agency services running.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and subcontractor staff) in every state and delivery center, including AQ-1 staff from the acquisition date. Covers all company systems, the hosted agency environments (ACMC, IES, legacy hosting, AQ-1), the CUI enclave, and all agency data the company receives, wherever it is stored or processed.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| Director of Regulated Data Compliance | Agency notices for CJI, FTI, ePHI, and DPPA data |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Privacy Officer | Breach determinations; business associate notice to AG-04 |
| Segment presidents and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks for its most likely severe incidents, starting with ransomware with data theft (P08). (IR-8; RS.MA-01)
4.2 Workforce members and subcontractors must report suspected incidents immediately and no more than 1 hour after discovery. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Incident records, tickets, email, and chat must not contain FTI, CJI, or ePHI; evidence is kept in the restricted evidence store. (IR-4; IR-5; PR.DS-01)
4.4 The Director of Regulated Data Compliance must notify each affected agency's security contact within 1 hour of discovering a suspected incident involving CJI or FTI, and within the contract term for other agency data, followed by a written fact sheet within 4 hours. (IR-6; RS.CO-02)
4.5 Statutory and contract notices must meet their deadlines in the P08 notification matrix, including the 10-day third-party agent notice (Fla. Stat. 501.171(6)(a)) and similar laws in other states, the business associate notice to AG-04 (45 CFR 164.410), and DoD reporting within 72 hours (DFARS 252.204-7012(c)). (IR-6; RS.CO-03)
4.6 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours and the disclosure committee must convene within 48 hours; if the committee determines the incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; IR-8; RS.CO-02)
4.7 No ransom may be paid without approval from the CEO, the General Counsel, and the cyber insurer, consultation with every affected agency, and an OFAC sanctions check. Florida agencies may not pay or comply with a ransom demand (Fla. Stat. 282.3186), and the company will not pay over the objection of any agency. (IR-4; RS.MI-01)
4.8 Tier-1 systems must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually. (CP-2; CP-4; CP-10; RC.RP-01)
4.9 The incident response plan must be exercised at least annually, including one exercise a year with the disclosure committee and at least two agency security contacts, and after each acquisition. (IR-3; IR-8; ID.IM-02)
4.10 Lessons learned must be documented within 30 days of closing a severity-1 or severity-2 incident and fed into the risk register and POA&M; staff involved in an incident affecting CJI must complete refresher training within 30 days. (IR-4; AT-2; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Agency and Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Ransomware Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-Agency and Multi-State Notification Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and agency audits (CJIS audits, IRS safeguard reviews). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception may be granted against a CJIS Security Addendum, Pub. 1075 Exhibit 7, or business associate agreement term, or a statute.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ACMC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; agency contracts; CJIS Security Policy v6.1; IRS Publication 1075.

# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Security Operations (with the General Counsel for notification and disclosure) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-9, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-04 |
| Regulations | 16 CFR 314.4(h)(1)-(7), (j); IRS Pub. 1345 (Reporting of Security Incidents); 45 CFR 164.308(a)(6), (a)(7); 164.410; Fla. Stat. 501.171(3)-(6) |

## 1. Purpose
Make sure the firm detects, responds to, reports, and recovers from security events promptly and in the right order, and meets every notification deadline to regulators, taxing authorities, clients, and individuals. With the runbooks below it, this policy is the written incident response plan required by 16 CFR 314.4(h).

## 2. Scope
All Cris Santos Company partners, employees, seasonal staff, contractors, and interns in all 64 offices and the 12 processing hubs, and staff of acquired firms from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, the offshore provider workspace, and systems that service providers operate for the firm, and the services the firm offers to clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; owns this policy and the runbooks |
| CISO | Executive incident lead; briefs the General Counsel and the CEO |
| General Counsel | Chairs the Incident Disclosure Committee; engages outside counsel; owns notification decisions |
| Chief Privacy Officer | Breach determinations and the affected-individual population |
| Director of e-file Operations | IRS Stakeholder Liaison reporting and state tax agency notices |
| Chief Operating Officer | Business continuity and crisis management team |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The incident response plan must state its goals, internal processes, roles and decision authority, communications, remediation, documentation, and post-incident revision, as 16 CFR 314.4(h)(1)-(7) requires. (IR-8; RS.MA-01)
4.2 Every workforce member must report a suspected incident (including an MFA prompt they did not start or a request to change a client's bank details) to the security hotline or the report-phish button immediately. (IR-6; RS.MA-02)
4.3 Incidents must be classified and escalated under STD-03.1; every severity-1 incident must be briefed to the General Counsel within 24 hours of declaration. (IR-4; IR-8; RS.MA-02)
4.4 The incident log must record three dates separately: discovery (FTC clock, 314.4(j)(2)), confirmation (IRS clock, Pub. 1345), and determination of a breach (state clocks, for example Fla. Stat. 501.171). (IR-5; IR-6; RS.MA-02)
4.5 Security incidents affecting taxpayer information must be reported to the IRS as soon as possible and no later than the next business day after confirmation, through the local Stakeholder Liaison. (IR-6; RS.CO-02)
4.6 Notification decisions (FTC, states, individuals, health care clients, contracting officers, and clients) must be made by the Incident Disclosure Committee following `notification-matrix.csv`, planned to the shortest applicable deadline, and confirmed by counsel. (IR-6; IR-8; RS.CO-02)
4.7 Clients whose data is affected, including SEC-registrant clients that must assess incidents on third-party systems they use, must be notified within their contract terms; the General Counsel keeps a central register of those terms. (IR-6(3); SA-4; RS.CO-03)
4.8 No ransom or extortion payment may be made without the approval of the CEO and Managing Partner and the General Counsel, an OFAC sanctions check, and notice to law enforcement. (IR-4; RS.MI-01)
4.9 The incident response plan and each runbook must be exercised at least annually, including the Incident Disclosure Committee, and before each filing season for the business email compromise runbook. (IR-3; ID.IM-02)
4.10 Recovery must follow the BIA priority order (P05). Tier-1 systems must be restore-tested at least annually and must meet their RTO in the test, or a dated corrective action must be opened. (CP-4; CP-10; RC.RP-01)
4.11 Lessons learned must be documented within 30 days after an incident is closed, and the resulting weaknesses added to the POA&M. (IR-4; CA-5; ID.IM-04)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Business Email Compromise and Taxpayer Data Theft Runbook (P08)
- PRC-03.2 Incident Disclosure Committee and Client-Impact Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Ransomware Runbook

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment, partnership, or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 Tax Engagement Platform SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.

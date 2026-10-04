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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions or Cybersecurity Plan amendments |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10, SR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, ID.IM-03 |
| 33 CFR Part 101 Subpart F | 101.620(b)(6)-(7); 101.635; 101.650(g); 33 CFR 6.16-1 |

## 1. Purpose
Make sure the company detects, contains, recovers from and reports cyber incidents quickly, safely and lawfully across its terminals; meets Coast Guard, SEC and state deadlines; supports the SL-2 client terminals' own reporting; and keeps vessel and gate work going during outages. This policy is the policy basis of the Cyber Incident Response Plan required by 33 CFR 101.650(g)(2).

## 2. Scope
All Cris Santos Company employees, contractors, temporary staff and interns at headquarters, the enterprise planning center and the 8 terminals (T-01 to T-08) in Florida, Georgia, South Carolina and Texas, including acquired terminals from their acquisition date. Longshore workers ordered through the hiring halls and OEM and vendor technicians are covered when they use company IT or OT, through the hiring hall arrangements and their contracts. Covers all IT and OT systems and data, including cloud, colocation, SaaS, cranes and automation, gate systems, and the services the company provides to outside customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander for security incidents; runs the SOC |
| Director of Maritime Cybersecurity (CySO) | Coast Guard reporting under 6.16-1; Subpart F incident records |
| CISO | Executive incident lead; escalates to the General Counsel and CEO |
| Chief Operating Officer | Chairs the crisis management team; terminal continuity |
| General Counsel | Chairs the disclosure committee; engages outside counsel; personal information breach decisions |
| Vice President, Maritime Security and the FSOs | MTSA reports; FSP measures during incidents |
| Vice President, Terminal Technology | SL-2 client notification and ETOP recovery |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain a Cyber Incident Response Plan and runbooks for its most likely severe incidents, starting with ransomware on ETOP (P08), and must keep them consistent with each facility's Cybersecurity Plan. (IR-8; RS.MA-01)
4.2 Workers, longshore workers, contractors and vendors must report suspected cyber incidents to the SOC or the CySO line within 1 hour. Good-faith reports are never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, classified by severity under STD-03.1, and tracked to closure in SOC case management, including incidents at acquired terminals. (IR-5; IR-4; RS.MA-02)
4.4 Evidence of an actual or threatened cyber incident involving a terminal must be reported immediately by the CySO or an alternate to the COTP of every affected zone, the FBI and CISA, without waiting for forensics or legal review. The NRC is notified only if no 6.16-1 report was made. (IR-6; RS.CO-02)
4.5 For a severity-1 incident, the CISO must brief the General Counsel within 24 hours, and the disclosure committee must convene within 48 hours to begin the materiality assessment (PRC-03.2). (IR-6; IR-8; RS.CO-02)
4.6 If the disclosure committee determines an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination, unless the U.S. Attorney General has authorized a delay. (IR-6; RS.CO-02)
4.7 For every incident involving personal information, the General Counsel must document whether a breach occurred, and notices must meet the deadlines in the P08 notification matrix for each state where affected individuals reside. (IR-6; RS.CO-03)
4.8 SL-2 client terminals must be notified without delay, with a 1-hour target, of any incident that affects or may affect their environment, so that they can make their own Coast Guard reports. (IR-6; SR-8; RS.CO-03)
4.9 A ransom must not be paid without approval from the CEO, the General Counsel and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.10 If the integrity of crane, automation or equipment control data is in doubt, the equipment must be stopped in a safe state, and it must not return to TOS-directed work until OT Engineering signs off. (IR-4; RS.MI-01)
4.11 Tier-1 systems and every ETOP environment must have contingency plans with RTO and RPO from the BIA (P05) and must pass a recovery test at least annually. (CP-2; CP-4; CP-10; RC.RP-01)
4.12 Each facility must hold cyber drills at least twice each calendar year and the company must hold an exercise at least once each calendar year, no more than 18 months apart, with the active participation of the CySO and, once a year, the disclosure committee. (IR-3; IR-8; ID.IM-02)
4.13 Lessons learned and exercise corrective actions must be documented within 30 days and fed into the risk register, the POA&M and, where needed, a Cybersecurity Plan amendment. (IR-4; CA-5; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Ransomware Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Coast Guard and MTSA Reporting Procedure
- PRC-03.5 Manual Terminal Operations Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications and, once the Cybersecurity Plans are approved, the annual Plan audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ETOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the Cybersecurity Plans and FSPs (SSI).

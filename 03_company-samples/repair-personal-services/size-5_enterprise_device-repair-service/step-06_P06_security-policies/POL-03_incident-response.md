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
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-6, IR-8, CP-2, CP-4 |
| CSF 2.0 | ID.IM-04, RS.MA-01 to RS.MA-04, RS.AN-07, RS.CO-02, RC.RP-01 |
| Other requirements | PCI DSS v4.0.1 12.10; HIPAA 164.308(a)(6), (a)(7) and 164.410 for SL-2; SEC Form 8-K Item 1.05 |

## 1. Purpose
Detect, respond to, and recover from security incidents, including exposure of customer device data and payment card compromise, and meet every notice and disclosure duty on time.

## 2. Scope
All incidents affecting company systems, customer devices in custody, customer, card, or client data, or services provided to clients, including incidents at vendors and in the acquired chain.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Policy owner; incident commander |
| CISO | Executive incident lead; briefs the General Counsel |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Privacy Officer | Breach determinations with counsel |
| Store and depot managers | Preserve evidence and report immediately |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an incident response plan and runbooks (P08) and test them at least annually, including at least one exercise a year with the disclosure committee. (IR-8; IR-3; ID.IM-04)
4.2 Every workforce member must report a suspected incident immediately, including any customer complaint that someone accessed their device content, through the store manager, the SOC hotline, or the anonymous line. (IR-6; RS.MA-02)
4.3 Incidents must be classified and escalated under STD-03.1; a severity-1 incident must reach the CISO within 1 hour of declaration. (IR-4; RS.MA-03)
4.4 The CISO must brief the General Counsel within 24 hours of declaring a severity-1 incident. The disclosure committee must convene within 48 hours and record each materiality determination with its date, time, and reasoning. (IR-8; RS.MA-04)
4.5 Evidence must be preserved: affected bench workstations, POS PCs, and customer devices must not be reimaged, wiped, or returned until forensics releases them, and chain of custody must be kept. (IR-4; RS.AN-07)
4.6 Each breach determination must be documented with counsel for every state where affected individuals reside, and the notification matrix (P08) must be followed. (IR-6; RS.CO-02)
4.7 No ransom or extortion payment may be made without approval of the CEO, the General Counsel, and the insurer, and an OFAC sanctions check. (IR-4; RS.MA-01)
4.8 Contractual notices must be sent on time: the acquirer within 24 hours of suspecting a card data compromise; Manufacturers A, B, and C within 24 hours of a suspected customer data incident under their programs; SL-1 clients within 48 hours of confirmation; SL-2 health care clients under their BAAs. (IR-6; RS.CO-02)
4.9 Contingency and disaster recovery plans for tier-1 systems must follow the BIA recovery order and be tested at least annually. (CP-2; CP-4; RC.RP-01)
4.10 A lessons-learned review must be held within 14 days of closing a severity-1 or severity-2 incident and documented within 30 days. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach and Contract Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Customer Device Data Exposure and POS Compromise Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Card Compromise Procedure (acquirer, card brands, forensic investigator)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, access certifications, the annual Internal Audit assessment (P07), and the annual PCI DSS ROC. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions to this policy follow the process in POL-01 section 7 and `policy-hierarchy.md` section 5: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, limited to 12 months, and recorded in the exception register with compensating controls.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 STPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.

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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or CMMC scope changes |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-4(14), IR-5, IR-6, IR-7, IR-8, CP-1, CP-2, CP-4, CP-9, AU-11, RA-10 |
| CSF 2.0 | RS.MA-01, RS.CO-02, RS.AN-03, RC.RP-01, DE.CM-01 |
| SP 800-171, CMMC, and other drivers | SP 800-171 Rev. 2 3.6.1 to 3.6.3; DFARS 252.204-7012(c) to (g), (m)(2); 32 CFR 117.8(f); Form 8-K Item 1.05; state breach laws |

## 1. Purpose
Detect, respond to, report, and recover from security incidents so that the company meets its DoD, NISPOM, export control, SEC, and state reporting duties and restores operations in the order the BIA sets.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, temporary workers, and interns) at all 8 sites in Florida, Georgia, Alabama, Texas, Kansas, and Arizona and at the 2 data centers, including acquired operations from their acquisition date. Covers all company systems and data, including the government-community and commercial clouds, SaaS, plant OT, and systems that suppliers and service providers operate for the company, with added rules for the CUI Engineering Enclave (CEE) and the Manufacturing Operations Zone (MOZ). The classified information system at FL-1 also follows NISPOM and DCSA requirements, which prevail where stricter.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander; runs the 24x7 SOC |
| CISO | Executive incident lead; briefs the General Counsel |
| Vice President, Contracts | DFARS reportability decisions, DIBNet reports, prime notices |
| Vice President, Trade Compliance | Export control decisions and voluntary disclosures |
| Corporate Facility Security Officer and ISSM | NISPOM reports to DCSA |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Operating Officer | Crisis management team chair; plant recovery |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must keep a 24x7 security operations center and an incident response team that can deploy to any site within 24 hours. (IR-4; IR-4(14); RS.MA-01)
4.2 Every workforce member must report suspected incidents, lost devices, and possible CUI exposure to the SOC at once. (IR-6; RS.MA-01)
4.3 Every incident case must record the discovery time and a documented DFARS reportability decision by the Vice President, Contracts. A reportable cyber incident must be reported on DIBNet within 72 hours of discovery, and the incident number given to the higher-tier contractor. (IR-6; IR-4; RS.CO-02)
4.4 The CISO must brief the General Counsel on every severity-1 incident within 24 hours, and the disclosure committee must convene within 48 hours to start the materiality assessment (PRC-03.2). (IR-8; GV.OV-01)
4.5 Images of affected systems and relevant monitoring data must be preserved for at least 90 days from the DIBNet report, and malicious software sent to DC3 when instructed. (AU-11; IR-4; RS.AN-03)
4.6 Cyber incidents on the classified information system must be reported immediately to the DoD cognizant security office by the ISSM. (IR-6; RS.CO-02)
4.7 No ransom or extortion payment may be made without approval of the CEO, the General Counsel, and the insurer, after an OFAC sanctions check and a report to law enforcement. (IR-4; RS.MA-01)
4.8 The incident response plan and the materiality playbook must be tested at least annually, with a scenario the previous test did not cover. (IR-3; IR-8; ID.IM-02)
4.9 Threat hunts must be scheduled, documented with scope and findings, and run at least quarterly and when intelligence warrants. (RA-10; DE.CM-01)
4.10 Recovery must follow the BIA priority order, and restored engineering data, NC programs, and build files must be revision-checked against PLM before release. (CP-2; CP-10; RC.RP-01)
4.11 A lessons-learned review must be held within 14 days of closing a major incident and documented within 30 days. (IR-4; ID.IM-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach and Government Reporting Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 CUI Exfiltration Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Threat Hunting Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the CMMC readiness checks before each affirmation. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. A suspected unauthorized release of ITAR or EAR technical data is also referred to the Vice President, Trade Compliance for a voluntary disclosure decision.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 CEE SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.

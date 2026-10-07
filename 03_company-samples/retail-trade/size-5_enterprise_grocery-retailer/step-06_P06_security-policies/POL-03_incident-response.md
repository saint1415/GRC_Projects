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
| Implements (SP 800-53 Rev. 5) | CP-1, CP-2, CP-4, CP-9, IR-1, IR-3, IR-4, IR-6, IR-8, SA-9, SR-8 |
| CSF 2.0 | DE.AE-02, GV.OV-01, GV.SC-08, ID.IM-03, ID.IM-04, PR.DS-11, RC.RP-01, RS.AN-03, RS.CO-02, RS.CO-03, RS.MA-01, RS.MI-01 |
| PCI DSS v4.0.1 (N44-45-R01) | 9.5.1.3, 12.8.2, 12.10.1, 12.10.2, 12.10.3, 12.10.6 (requirement numbers only; read the text in the company's licensed copy) |

## 1. Purpose
Detect, respond to, and recover from security incidents and disruptions in a way that protects customers, cardholders, SNAP households, and food safety, meets card brand, legal, and SEC deadlines, and keeps stores trading.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at the 112 stores in Florida, Georgia, Alabama, South Carolina, and Tennessee, the 2 distribution centers, and headquarters, including the acquired banner (AB) stores from their acquisition date. Covers all systems and data, including stores, colocation, cloud, SaaS, store operational technology, and systems that third parties operate for the company, and the services the company offers to external business clients (SL-1 retail media and SL-2 supplier collaboration).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Security Operations | Incident commander; runs the SOC and the runbooks |
| CISO | Executive incident lead; briefs the General Counsel and the CEO |
| General Counsel | Chairs the disclosure committee; engages outside counsel and forensics |
| Vice President, Payments | Acquirer, processor, and card brand liaison |
| Chief Privacy Officer | Breach determinations and notifications with counsel |
| Chief Operating Officer | Chairs the crisis management team; store and DC continuity |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must keep an incident response plan that meets PCI DSS 12.10.1 and follows NIST SP 800-61 Rev. 3, with runbooks for card data compromise, ransomware, and store outages, and a SOC that can respond 24x7. (IR-8; RS.MA-01)
4.2 Every workforce member must report a suspected incident immediately to the service desk or the SOC. Cashiers and store leads must report a suspicious or tampered PIN pad at once and stop using it. (IR-6; DE.AE-02)
4.3 A suspected compromise of card data must be reported to the acquirer within 24 hours of suspicion, as the merchant agreement requires, and the acquirer's and card brands' instructions must be followed, including engaging a PCI Forensic Investigator when required. (IR-6; RS.CO-02)
4.4 The CISO must brief the General Counsel within 24 hours of declaring a severity-1 incident, and the disclosure committee must convene within 48 hours to start the materiality assessment. (IR-8; GV.OV-01)
4.5 The incident response plan must be tested at least every 12 months, alternating scenarios so that a card data compromise with the disclosure committee is exercised at least every 2 years. (IR-3; ID.IM-04)
4.6 Breach notifications must be decided by the Chief Privacy Officer with counsel under the law of each state where affected individuals reside, planning to the shortest deadline. (IR-6; RS.CO-03)
4.7 No ransom or extortion payment may be made without approval by the CEO, the General Counsel, and the insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)
4.8 Tier-1 processes must have contingency plans with RTO and RPO from the BIA (P05), tested at least every 12 months, including SNAP EBT routing and manual voucher procedures. (CP-2; CP-4; RC.RP-01)
4.9 Backups of tier-1 data and configurations must be immutable, kept in separate accounts, and restore-tested at least quarterly. (CP-9; PR.DS-11)
4.10 A lessons-learned review must be held within 14 days of closing a severity-1 or severity-2 incident and documented within 30 days. (IR-4; ID.IM-03)
4.11 Forensic investigations must be run through counsel, with chain of custody for every artifact. (IR-4; RS.AN-03)
4.12 Contracts with TPSPs and with vendors that hold customer personal information must require notice to the company of any security incident affecting company data within 24 hours of discovery for TPSPs and no later than state law allows for other vendors (Florida worked example: 10 days). (SR-8; SA-9; GV.SC-08)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Breach Notification Standard
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 E-commerce Skimming Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure
- PRC-03.4 Store Downtime and Manual EBT Voucher Procedures

## 6. Compliance and enforcement
Compliance is measured through incident metrics (time to declare, time to contain, time to brief the General Counsel), annual exercises, and the annual Internal Audit assessment (P07). Failure to report a suspected incident or a tampered PIN pad is a policy violation under PRC-01.1.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2. A deviation from a PCI DSS requirement also needs the PCI Program Manager's review, because internal exceptions do not change what the QSA must validate.

## 8. Related documents
POL-01; STD-03.1 to STD-03.3; PRC-03.1 (P08 runbook) and `notification-matrix.csv`; P05 BIA recovery objectives; P07 IR and CP results; POAM-010, POAM-011, POAM-016, POAM-024.

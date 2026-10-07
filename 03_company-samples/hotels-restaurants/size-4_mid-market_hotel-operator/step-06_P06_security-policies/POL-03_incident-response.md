# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after every severity 1 incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-6(3), IR-8, AU-2, AU-6, SI-4, CP-2, CP-4 |
| CSF 2.0 | RS.MA-01, RS.CO-02, RS.AN-03, DE.AE-02, RC.RP-01, ID.IM-04 |
| PCI DSS v4.0.1 | 10.2, 10.4, 12.10 |
| Other drivers | Fla. Stat. 501.171(3)-(6); state breach notification laws (N72-R04); merchant agreement; franchise agreements; REIT management agreement |
| Supporting standards | STD-02 Logging and monitoring; STD-07 Contingency and recovery; P08 runbooks |

## 1. Purpose
Make sure suspected incidents are reported, contained, investigated, and communicated fast enough to protect guests, meet the acquirer's, card brands', franchisor's, and owners' clocks, and meet state breach laws.

## 2. Scope
All suspected or confirmed security incidents affecting company systems, card data, guest or employee data, lock systems, or data the company holds for the franchisor or (from 2027) for hotel owners, including incidents at vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander; owns this policy and the P08 runbooks |
| Chief Operating Officer | Chairs the crisis management team |
| Chief Financial Officer | Acquirer and card brand communication |
| General Counsel | Breach determinations, legal notices, decision log; franchisor and owner notices |
| IT Director | Containment and recovery |
| MSSP | 24x7 detection and first response |
| All workforce | Report anything suspicious at once |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident immediately to the service desk or the incident line. Reporting in good faith is never punished. (IR-6; RS.MA-01)
4.2 The company must keep incident response runbooks for its most likely and most damaging incidents (P08), covering roles, containment, communication, legal and contractual notice, recovery, and business continuity. The runbooks must be tested at least annually, including one card compromise exercise. (IR-8; IR-3; PCI DSS 12.10.1, 12.10.2)
4.3 The incident log must record the time of discovery, the time of each decision, and the time the company determined a breach occurred, because notice clocks run from these times. (IR-5; IR-4)
4.4 **Suspected card compromise.** The CFO must notify the acquirer within 24 hours of suspicion, as the merchant agreement requires, and follow the card brand rules in the P08 notification matrix (for Visa, report within 3 calendar days). (IR-6; PCI DSS 12.10.1)
4.5 The General Counsel keeps a decision log for each potential breach: what data, whose data, which states, which notices, and why. No notice and no decision not to notify is made without it. (IR-4; IR-6; RS.CO-02)
4.6 The General Counsel must notify the franchisor within 24 hours of a suspected compromise affecting brand systems or guest data at a franchised hotel, and (from 2027-01-01) the hotel owner within 48 hours of a suspected incident affecting a managed hotel, and in any case within the 10 days Fla. Stat. 501.171(6)(a) allows a third-party agent after determining a breach. (IR-6(3))
4.7 Evidence must be preserved. Affected systems are isolated, not powered off or rebuilt, until the forensic firm agrees. Forensic firms are engaged through the cyber insurer and counsel. (IR-4)
4.8 No ransom may be paid without CEO approval, counsel's advice, the insurer's involvement, an OFAC sanctions check on the recipient, and a report to law enforcement. (IR-4)
4.9 Logs required by STD-02 must be collected centrally, kept at least 12 months, and security events from card data systems reviewed at least daily. (AU-2; AU-6; SI-4; PCI DSS 10.2, 10.4.1, 10.5.1)
4.10 Recovery objectives come from the BIA (P05). Recovery procedures for every High-criticality process must be written and tested at least annually; restores of company-managed workloads are tested each quarter. (CP-2; CP-4; RC.RP-01)
4.11 Card numbers found stored where they should not be (email, files, chat, recordings) are treated as an incident: secured, deleted, and the cause fixed. (IR-4; PCI DSS 12.10.7)
4.12 A lessons-learned review must be held within 14 days of closing a severity 1 or 2 incident, and a written report produced within 30 days. (IR-4; ID.IM-04)

## 5. Compliance and enforcement
P07 tests incident handling and reporting. The Security Manager reports incident metrics quarterly. Failure to report a known incident is a violation under POL-01 4.15.

## 6. Exceptions
None for statements 4.1, 4.3, 4.4, 4.5, and 4.8. Others under POL-01 4.7.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-ransomware.md`, and `notification-matrix.csv`; BIA (P05); STD-02; STD-07; POL-04

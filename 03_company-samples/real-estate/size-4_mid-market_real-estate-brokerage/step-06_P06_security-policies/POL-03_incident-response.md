# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC |
| Policy ID | POL-03 |
| Owner | Security Manager (Qualified Individual) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-29 |
| Effective date | 2026-10-15 (replaces the 2024 incident response plan) |
| Review cycle | Annually (next review 2027-09-30), and after every significant incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AU-1, AU-2, AU-6, AU-11, SI-4, CP-1, CP-2, CP-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-04, DE.CM-01, DE.AE-02 |
| FTC Safeguards Rule (N53-R01) | 16 CFR 314.4(c)(8), (h)(1)-(7), (j) |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |
| Runbooks | P08 `ir-runbook.md` (business email compromise targeting closing funds); P08 `ir-runbook-ransomware.md` (ransomware with data theft) |

## 1. Purpose and goals (314.4(h)(1))
Respond to and recover from security events that affect customer, client, tenant, or company information or client funds. In order of priority, the goals are to:
1. recover or freeze diverted funds and stop further payments;
2. contain the threat and preserve evidence;
3. keep closings, rent collection, and owner payouts running safely;
4. meet every legal, contractual, and insurance notice deadline;
5. fix the weakness that allowed the event.

## 2. Scope
All security events affecting either entity, its contractor agents, or its service providers, including email account takeover, spoofed or altered payment instructions, ransomware, data theft, lost devices, and service provider breaches.

## 3. Roles and decision authority (314.4(h)(3))
| Role | Authority |
|---|---|
| Crisis management team (chair: COO; CEO, CFO, President of Title and Closing, General Counsel, Broker of Record, vCISO, Director of Marketing) | Business decisions, external statements, ransom decision recommendation to the CEO, funding of any trust or escrow shortfall |
| Incident commander (Security Manager; backup IT Director) | Declares incidents and severity; directs containment and investigation |
| Funds response lead (President of Title and Closing for trust accounts; Controller for sales and property management escrow; CFO for operating accounts) | Bank recall requests, payment holds, and re-verification |
| General Counsel | Notification decisions and the decision log; engages panel counsel through the insurer |
| Broker of Record | Escrow dispute notices to the Florida Real Estate Commission |

## 4. Policy statements
4.1 **Report immediately.** Every employee and contractor agent must report a suspected incident, a suspicious payment instruction, or a suspected account compromise to the incident line at once, and in any case the same day. Reporting duties for contractor agents are part of the agent agreement. (IR-6; RS.MA-01; 314.4(j)(2))

4.2 The incident commander declares an incident and assigns severity. Any event in which client funds may have been sent to a wrong account, or customer information may have been acquired without authorization, is Severity 1. (IR-4; RS.MA-02)

4.3 **Record discovery.** The incident log must record the date and time the event was first known to any employee, officer, or agent of the company, because that starts the FTC 30-day clock (314.4(j)(2)), and the date of determination, which starts the Florida 30-day clock (Fla. Stat. 501.171(4)(a)). (IR-5; RS.MA-02; 314.4(h)(6))

4.4 **Funds first.** When funds may have been diverted, the funds response lead must contact the sending bank's wire or fraud desk within 1 hour of the report to request a recall, and must hold every other pending payment to the affected payee or from the affected file until it is re-verified under STD-05. (IR-4; RS.MI-01; 314.4(h)(2))

4.5 **Decision log.** General Counsel must keep a decision log for every Severity 1 incident: whether customer information was acquired (with the presumption in 16 CFR 314.2(m)), the number of affected consumers, the states of residence of affected people, law enforcement requests, and each notice decision with its date. (IR-6; RS.CO-02)

4.6 **Notices.** Notices to the FTC, individuals, state agencies, consumer reporting agencies, the title insurance underwriter, the cyber insurer, lender and builder clients, and the Florida Real Estate Commission must follow the P08 notification matrix and be approved by General Counsel. (IR-6; RS.CO-02; RS.CO-03; 314.4(h)(4), (j))

4.7 **Out-of-band communication.** During a suspected email compromise or ransomware incident, responders must use the pre-arranged messaging group on personal phones and printed contact lists, not company email. (IR-4; RS.CO-03)

4.8 **Ransom.** No ransom or extortion payment may be made without CEO approval, outside counsel advice, insurer involvement, and an OFAC sanctions check. The default position is not to pay while backups are intact. (IR-4)

4.9 **Monitoring.** The MSSP and the security team must monitor identity, email, cloud, endpoint, and SaaS application events defined in STD-02, including new forwarding rules, payee and bank account changes, and bulk exports. (SI-4; AU-6; DE.CM-01; 314.4(c)(8))

4.10 **Testing.** Each P08 runbook must be exercised at least annually in a tabletop with the crisis management team, and bank and insurer contact lists must be verified each quarter. (IR-3; ID.IM-04; 314.4(h)(7))

4.11 **Lessons learned.** A lessons-learned review must be held within 14 days after each Severity 1 or 2 incident and documented within 30 days. Weaknesses go to the risk register and the POA&M. (IR-4; ID.IM-04; 314.4(h)(5), (h)(7))

4.12 **Recovery.** Systems are restored in the BIA priority order (P05) and validated before reconnection, under STD-07. (CP-2; CP-4; RC.RP-01)

## 5. Compliance and enforcement
Compliance is checked through tabletop exercises, the annual independent assessment (P07), and review of the incident log by the Qualified Individual each month.

## 6. Exceptions
None. Deviations during an incident must be recorded in the incident log with the reason and approver.

## 7. Related documents
POL-01; POL-04; STD-02; STD-05; STD-07; P08 runbooks and notification matrix; BIA (P05)

# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | COO |
| Effective date | 2026-09-21 |
| Review cycle | Annually (next review 2027-09-21), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, AT-3 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-04 |
| FTC Safeguards Rule (16 CFR 314) | 314.4(h)(1)-(7); 314.4(j) |

## 1. Purpose
This policy and the runbooks under it (starting with P08, business email compromise targeting closing funds) are the company's written incident response plan under 16 CFR 314.4(h). The plan's goals are to:
- stop the loss of client and escrowed funds, and recover them where possible;
- contain unauthorized access to customer information quickly;
- keep closings and escrow duties running, or reschedule them safely;
- meet every notification deadline (FTC, Florida, other states, the title underwriter, and the Florida Real Estate Commission where escrow is disputed);
- learn from each event and fix the weaknesses it exposed.

## 2. Scope
All Cris Santos Company workforce members: owners, employees, and the affiliated sales associates who work under the Broker of Record's license as independent contractors. Covers any event that affects customer information, client or escrowed funds, or company systems, including events at service providers.

## 3. Roles and responsibilities
| Role | Responsibility and decision authority |
|---|---|
| IT Manager (Qualified Individual) | Incident commander; declares incidents; directs containment, the MSP, and forensic support |
| Closing Services Manager | Leads the funds response for closing and trust account wires: bank recall, payee holds, rescheduling closings |
| Controller | Leads the funds response for sales and property management escrow wires; records the escrow impact in the reconciliation |
| COO | Engages counsel and the cyber insurer; approves external communications and client notices; backup incident commander |
| Majority owner and Broker of Record | Decides on escrow disputes and notice to the Florida Real Estate Commission; approves any payment decision above the COO's authority |
| Outside counsel | Confirms whether an event is a notification event or a breach, and approves each regulatory and individual notice |
| All workforce members | Report suspected incidents immediately (4.2) |

## 4. Policy statements
4.1 The company must keep an incident response plan made up of this policy and a runbook for each of its most likely incident types. BEC targeting closing funds (P08) is first; ransomware and lost or stolen devices follow by 2027-03-31. (IR-8; RS.MA-01; 314.4(h))
4.2 **Report immediately.** Every workforce member, **including contractor sales associates**, must report any suspected incident **immediately, and within 1 hour at most**, by calling the incident line (not by email). Examples: a client asking about wire instructions they did not expect, a changed payee or bank account, a password entered on a suspicious page, a lost phone, unexpected mailbox rules or sent messages, or a misdirected closing package. Good-faith reporting is never sanctioned. Because the knowledge of any employee, officer, or other agent can start the FTC's 30-day clock (314.4(j)(2)), a late report is itself a policy violation. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category. (IR-5; 314.4(h)(6))
4.4 When client or escrowed funds may have been misdirected, the funds response comes first: call the sending bank's fraud or wire desk to request a recall, then file a complaint with the FBI's Internet Crime Complaint Center (IC3), as set out in P08. (IR-4)
4.5 Outside counsel, with the Qualified Individual, must decide whether an event is a **notification event** under 16 CFR 314.2(m) and a breach of security under Fla. Stat. 501.171(1)(a), and must document the decision and the count of affected consumers. (IR-6)
4.6 Notifications to the FTC, affected individuals, the Florida Department of Legal Affairs, consumer reporting agencies, other states, the title insurance underwriter, and law enforcement must meet the deadlines in the P08 notification matrix. Counsel must confirm each notice. (IR-6; RS.CO-02; RS.CO-03; 314.4(j))
4.7 The plan must be tested at least annually by a tabletop exercise, and after any major incident. Closing Services staff, the Controller, and transaction coordinators must be trained on their runbook roles each year. (IR-2; IR-3)
4.8 **Lessons learned** must be documented within 30 days of closing an incident. The IT Manager must add the weaknesses found to the risk register and the POA&M and revise the plan. (IR-4; ID.IM-04; 314.4(h)(5), (h)(7))
4.9 **Funds-transfer verification (prevention).** No payee, bank account, or wire instruction may be created or changed on the strength of an email, text, or voicemail alone. Every payoff, every seller proceeds wire, every change of instructions, and every change to a property owner's payout account must be verified by a phone call to a number obtained independently (the lender's published number, the number collected at listing, or the owner portal record), never the number in the message. The Closing Services Manager samples verification records monthly. (AT-3; IA-8; Fla. Stat. 626.8473(4))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 4.7. Compliance is checked through the annual control assessment (P07), the tabletop exercise, and the monthly verification sample in 4.9.

## 6. Exceptions
Exceptions follow POL-01 4.6. No exception may be granted to 4.2 or 4.9.

## 7. Related documents
P08 incident response runbook and notification matrix; POL-01; FTC Safeguards Rule 16 CFR 314.4(h) and (j); Fla. Stat. 501.171; Fla. Stat. 475.25(1)(d)1. and Fla. Admin. Code r. 61J2-10.032 (escrow disputes)

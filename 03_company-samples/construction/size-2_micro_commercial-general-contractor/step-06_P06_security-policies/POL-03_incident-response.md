# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Owner and President, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required outside help or notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, AU-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.MI-01, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Federal contract and state requirements | FAR 52.204-25(d) (N23-R02); DFARS 252.204-7012(c)-(e) only if covered defense information is ever held (N23-R03); FAR 52.232-33 and 52.232-27 for diverted federal payments; Fla. Stat. 501.171 |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents quickly, recovers diverted money where it can, and meets every contract and breach notification deadline.

## 2. Scope
All Cris Santos Company workforce members and every company system and copy of company information, including systems the MSP and SaaS vendors run for the company. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, or interference with a system. It also includes a false payment instruction (sent or received), a lost or stolen device, and covered Section 889 equipment found in a system.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Incident lead; keeps the incident log; calls the bank and the MSP; prepares the personal information determination with counsel |
| Owner and President | Backup incident lead; calls the cyber insurer; approves outside communications, spending, and every notice to the Government |
| Project Manager and Estimator | Calls owners and subcontractors on numbers from the contract file |
| MSP | Technical response: secure accounts, collect logs, check devices, restore |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely costly incident, business email compromise that redirects payments (P08), with a printed copy and the contact card in the office binder and in the Owner's truck. (IR-8; RS.MA-01)

4.2 Workforce members must report any suspected incident to the Office Manager **at once, and within 1 hour at most**, by phone or in person, not by email. If the Office Manager cannot be reached, report to the Owner. Examples: a bank-change request, an owner asking about a payment the company did not expect, an MFA prompt you did not start, a login page after clicking a link, a lost phone or tablet, or a document marked CUI. (IR-6; RS.MA-02)

4.3 The Office Manager must log every incident, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5)

4.4 **Suspected payment diversion.** The first action is a recall request to the company's bank, or a call to the paying owner asking it to contact its bank, within the hour. All bank-detail changes in SYS-02 are frozen until the incident lead lifts the freeze. A complaint is filed with the FBI's Internet Crime Complaint Center (IC3) the same or next day. (IR-4; RS.MI-01)

4.5 For any incident that may involve personal information (for example, certified payrolls with Social Security numbers, or an email address with its password), the Office Manager and breach counsel must record the date the company determined, or had reason to believe, that a breach occurred, and decide in writing whether Florida or other state notice is required. Notices must meet the deadlines in the P08 notification matrix, and counsel must review each notice before it is sent. (IR-6; RS.CO-02; RS.CO-03; Fla. Stat. 501.171)

4.6 For any suspected account takeover, payment diversion, or ransomware, the Owner must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its contract. The call-back log (POL-02 A.6) must be preserved for the insurer. (IR-4; RS.MA-02)

4.7 **Section 889.** If covered telecommunications or video surveillance equipment is found in a system during a federal contract, the Owner must report it to the Contracting Officer (DoD: dibnet.dod.mil) within 1 business day of identification, and send the mitigation details within 10 business days (FAR 52.204-25(d)). (IR-6; RS.CO-02)

4.8 At the start of any incident, the MSP must export and keep the relevant logs (suite sign-ins, mailbox audit records, inbox rules, SYS-01 activity, SYS-02 change log) before they roll off. Every incident must include a check for covered defense information; if any were involved, DFARS 252.204-7012 reporting within 72 hours and 90-day image preservation would apply. (IR-4; AU-11; RS.AN-03)

4.9 No ransom or extortion payment may be made without the Owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.10 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. Lessons learned must be written up within 30 days of closing any incident that required outside help or notification, and fed into the risk register and training. (IR-3; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.10. No exception may delay a bank recall request, a contract report, or a legally required notification.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; call-back log; cyber insurance policy; FAR 52.204-25; Fla. Stat. 501.171

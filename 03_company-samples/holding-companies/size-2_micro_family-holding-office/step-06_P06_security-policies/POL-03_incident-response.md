# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Family Office Director (Qualified Individual) |
| Approved by | Principal, 2026-09-18 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required notification or outside help |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, DE.AE-08, RC.RP-01, ID.IM-02 |
| Regulation | 16 CFR 314.4(h) (adopted voluntarily; excepted by 314.6) and 314.4(j); Fla. Stat. 501.171(3)-(6) |

## 1. Purpose
Make sure the office spots, contains, reports, and recovers from security incidents quickly and lawfully, stops fraudulent payments before money is lost, and meets every notice deadline. This policy covers the seven areas a written incident response plan addresses under 16 CFR 314.4(h): goals, internal processes, roles and decision authority, communications, remediation of weaknesses, documentation, and post-incident review. The office is not required to have such a plan at its size (314.6) but adopts one because email compromise is its top risk.

## 2. Scope
All workforce members and every system and copy of office information, including systems the MSP and vendors run for the office. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, or interference with a system, and also:
- a suspicious payment request or bank-detail change, even if nobody acted on it;
- a lost or stolen laptop, phone, security key, or bank token;
- family or subsidiary information sent to the wrong person;
- a report from a subsidiary, vendor, custodian, or family member that their account or email may be compromised.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Family Office Director | Incident lead; decides whether an incident is a breach that requires notice; keeps the incident log |
| Controller | Backup incident lead; leads payment recall with the banks |
| Principal | Calls the cyber insurer; approves outside communications, spending, and any ransom question; informs the Board of Managers |
| MSP | Technical response: isolate, investigate, reset, rebuild, restore; preserves logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The office must keep an incident response runbook for its most likely serious incident, compromise of the shared productivity and identity tenant with payment fraud (P08), and a printed copy and contact card in the office safe and at the Family Office Director's, Controller's, and Principal's homes. (IR-8; RS.MA-01)

4.2 Workforce members must report any suspected incident to the Family Office Director **at once, and within 1 hour at most**, by phone or in person. If the Family Office Director cannot be reached, report to the Controller. Examples: entering a password on a page reached from an email link, an MFA prompt you did not start, a payment request that seems unusual, a lost phone or token, or a message sent to the wrong family member. (IR-6; RS.MA-02)

4.3 **Suspected payment fraud is handled first.** If money may have been sent to a fraudster, the Controller must call the sending bank's fraud line at once to request a recall, before any other step, and then file a complaint with the FBI's Internet Crime Complaint Center (IC3). (IR-4; RS.MI-01)

4.4 The Family Office Director must log every incident and near miss, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5; DE.AE-08)

4.5 For any incident that may involve personal information, the Family Office Director must decide, with breach counsel, whether there was a breach of security under Fla. Stat. 501.171 (and the law of any other state where affected individuals live), and whether a notification event under 16 CFR 314.2(m) occurred. The date of determination or discovery must be written down, because the notice clocks start there. (IR-6; RS.AN-03)

4.6 Notices to individuals, regulators, subsidiaries, custodians, and others must meet the deadlines in the P08 notification matrix. Breach counsel must review each notice before it is sent. If, after investigation and consultation with law enforcement, the office decides under 501.171(4)(c) that notice to individuals is not required, that decision must be written, kept for at least 5 years, and sent to the Florida Department of Legal Affairs within 30 days. (IR-6; RS.CO-02; RS.CO-03)

4.7 For any suspected account takeover, data theft, or ransomware, the Principal must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its contract. (IR-4; RS.MA-02)

4.8 No ransom may be paid without the Principal's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.9 Subsidiaries, the MSP, and vendors must report incidents that may affect the office as their contracts require (target: within 24 hours). The Family Office Director must log each report and handle it under this policy. If an incident at the office affects a subsidiary's information, the office must tell that subsidiary within 24 hours, and in any case within the 10 days that 501.171(6)(a) allows a third-party agent. (IR-6; SA-9; GV.SC-08)

4.10 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. (IR-3; ID.IM-02)

4.11 Lessons learned must be written up within 30 days of closing any incident that required notification or outside help, fed into the risk register, the POA&M, and training, and summarized in the annual report to the Board of Managers. Weaknesses found must get an owner and a date (16 CFR 314.4(h)(5), (h)(7)). (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a legally required notification or a payment recall.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02 (B.10 payment verification); POL-04; Fla. Stat. 501.171; 16 CFR 314.4(j)

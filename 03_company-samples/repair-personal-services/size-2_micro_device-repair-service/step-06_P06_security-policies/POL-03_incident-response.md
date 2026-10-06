# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Shop Manager (Security and Privacy Lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.AN-07, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02, ID.IM-03 |
| Regulatory drivers | N81-R02 (Fla. Stat. 501.171(3)-(6)); N81-R03 (PCI DSS v4.0.1 12.10.1; merchant agreement notice term) |

## 1. Purpose
Make sure the shop spots, contains, reports, and recovers from security incidents quickly and lawfully, and meets every notice deadline in law and in its contracts.

## 2. Scope
All workforce members and every shop system, customer device in custody, and copy of shop or customer information, including systems the MSP and SaaS vendors run for the shop. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information; any viewing or copying of customer device content outside POL-04 4.4; a lost or stolen device; a card number found outside the payment terminals; and a tampered payment terminal.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Shop Manager | Incident lead; keeps the incident log; makes the breach determination with counsel; calls the processor |
| Owner | Backup incident lead; calls the cyber insurer's hotline; decides on staff actions, spending, and public statements |
| MSP | Technical response for office endpoints, network, suite, and backups: isolate, investigate, rebuild, restore; preserves logs |
| Cyber insurer and its panel | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once; do not investigate on their own |

## 4. Policy statements
4.1 The shop must keep an incident response runbook for its most likely serious incident, exposure of customer data at the counter or bench (P08), with a printed copy, contact card, and evidence bags in the incident binder behind the counter and a copy at the Owner's home. (IR-8; RS.MA-01; PCI DSS 12.10.1)

4.2 Workforce members must report any suspected incident to the Shop Manager **at once, and within 1 hour at most**, in person or by phone. If the Shop Manager cannot be reached, report to the Owner. Examples: a colleague browsing a customer's photos, a customer saying their account was accessed after a repair, a card number written down, a strange sign-in prompt, a terminal that looks different, a lost USB drive. (IR-6; RS.MA-02)

4.3 The Shop Manager must log every incident, including those that turn out to be harmless, with the time reported, what happened, what was done, and the outcome. (IR-5)

4.4 Evidence must be preserved before anything is fixed: bench PCs, USB drives, and customer devices involved are bagged, labeled, and locked away, not reimaged or returned, until the Owner and counsel release them. Camera footage must be saved before its 30-day retention ends. (IR-4; RS.AN-07)

4.5 For any incident that may involve personal information, the Shop Manager must decide with counsel whether it is a breach under Fla. Stat. 501.171 and each other affected state's law, and record the decision with its reasons. The record must note the date of the determination or reason to believe a breach occurred, because Florida's 30-day clock runs from it. (IR-6; RS.AN-03)

4.6 Notices to individuals, the Florida Department of Legal Affairs, consumer reporting agencies, other states, the processor, and the insurer must meet the deadlines in the P08 notification matrix. Contract notices that run from **suspicion** (the processor's 24-hour term and the insurer's prompt-notice term) must not wait for the investigation. Breach counsel reviews every legal notice before it is sent. (IR-6; RS.CO-02; RS.CO-03)

4.7 For any suspected account takeover, data theft, card data exposure, or insider misuse, the Owner must call the cyber insurer's breach hotline before hiring any outside firm. No ransom or extortion payment may be made without the Owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.8 Vendors must report incidents to the Shop Manager as their terms require (POL-02 A.5). The Shop Manager logs each report and handles it under this policy. Under Fla. Stat. 501.171(6), a vendor that maintains personal information for the shop must give notice within 10 days of its determination; the shop still sends the notices to individuals and the Department. (IR-6; SA-9)

4.9 Lessons learned must be written up within 30 days of closing any incident that required notification or outside help, or that involved a workforce member, and fed into the risk register, training, and this policy. (IR-4; ID.IM-03)

4.10 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. (IR-3; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a legally required or contractually required notice.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; merchant agreement; cyber insurance policy; Fla. Stat. 501.171

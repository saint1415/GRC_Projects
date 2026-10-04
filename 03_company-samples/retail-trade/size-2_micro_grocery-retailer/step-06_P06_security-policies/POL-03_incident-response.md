# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Store Manager (Security and PCI Lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Yearly (next review 2027-08-31), and after any incident that required outside notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| PCI DSS v4.0.1 (N44-45-R01) | 12.10 (12.10.1 is in SAQ P2PE) |
| State law | Fla. Stat. 501.171(3)-(6) |

## 1. Purpose
Make sure the store spots, contains, reports, and recovers from security incidents quickly, meets the merchant agreement's notice term, and meets every breach notice deadline.

## 2. Scope
All workforce members of Cris Santos Company and every system and copy of store information, including systems that the provider, the MSP, and other vendors run for the store. A "security incident" includes any attempted or successful unauthorized access to, use, disclosure, change, or destruction of information, interference with a system, a tampered or missing card terminal, a lost store phone, and card or customer data sent to the wrong place.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Store Manager | Incident lead; keeps the incident log; works with the MSP and the provider |
| Owner | Decision maker: calls the cyber insurer, approves spending and outside communications, and decides on any notice |
| Bookkeeper | Notifies the payment provider; backup contact when the Store Manager is away |
| MSP | Technical help on the office PC, laptop, firewall, Wi-Fi, and mailboxes; preserves logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The store must keep an incident response runbook for its most likely serious incident, e-commerce skimming (P08), with a printed copy and contact list in the back office binder and at the Owner's home. (IR-8; RS.MA-01; PCI DSS 12.10.1)

4.2 Staff must report any suspected incident to the Store Manager **at once, and within 1 hour at most**, in person or by phone. If the Store Manager cannot be reached, report to the Owner. Examples: a terminal that looks different or has something attached, a customer saying their card was misused after shopping here, a strange change on the online store, a suspicious email or text that was clicked, a lost store phone, or a payment request that seems wrong. (IR-6; RS.MA-02)

4.3 The Store Manager must log every incident, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5)

4.4 **24-hour provider notice.** When a card data compromise is suspected, the Bookkeeper (or the Owner) must notify the payment provider **no later than 24 hours after the suspicion**, as the merchant agreement requires, and follow the provider's instructions, including any requirement to use a PCI Forensic Investigator. The clock starts at suspicion, not confirmation. (IR-6; RS.CO-02; PCI DSS 12.10.1)

4.5 For any suspected card compromise, data theft, account takeover, or extortion, the Owner must call the cyber insurer's breach hotline before hiring any outside firm. The MSP is engaged under its service contract. (IR-4; RS.MA-02)

4.6 The Owner, with breach counsel, must decide whether an incident is a breach of personal information under Fla. Stat. 501.171 and the laws of any other state where affected customers live, and record the date of that determination. Notices to individuals, the Florida Department of Legal Affairs, and consumer reporting agencies must meet the deadlines in the P08 notification matrix. A decision not to notify must be documented, kept for 5 years, and sent to the Department within 30 days (501.171(4)(c)). (IR-6; RS.AN-03; RS.CO-02)

4.7 Evidence comes first: before changing the online store, capture the page and export the activity log; before wiping a device, ask the MSP or forensic firm. (IR-4; RS.AN-03)

4.8 No ransom or extortion payment may be made without the Owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.9 Vendors must report incidents that affect store data. The Store Manager must log each report and handle it under this policy. Contracts must require notice no later than 10 days after the vendor's determination of a breach (Fla. Stat. 501.171(6)(a)). (IR-6; SA-9; GV.SC-08)

4.10 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. (IR-3; ID.IM-02)

4.11 Lessons learned must be written up within 30 days of closing any incident that required outside notice or outside help, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Failing to report an incident breaks this policy and is handled under POL-02 section 5. Reporting a mistake in good faith is never punished. Compliance is checked in the yearly assessment (P07) and the yearly tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay the 24-hour provider notice or a legally required notice.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; merchant agreement; cyber insurance policy; Fla. Stat. 501.171

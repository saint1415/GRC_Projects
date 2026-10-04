# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Operations Manager (security and compliance lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required a report or notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, SR-8, SR-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, GV.SC-08, ID.IM-02 |
| Contract and regulatory basis | FAR 52.204-25(d); FAR 52.204-23(c); DFARS 252.246-7008(b)(3); Fla. Stat. 501.171 |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents and supply chain incidents quickly, and meets every contract and legal reporting deadline.

## 2. Scope
All workforce members and every company system and copy of company information, including systems the MSP and SaaS vendors run for the company. An "incident" here includes any attempted or successful unauthorized access to company systems or information, account takeover, payment fraud, lost or stolen devices, and any **product incident**: suspected counterfeit, tampered, or covered (Section 889) items in stock, in transit, or delivered.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Incident lead; decides on reports to the Government, customer notices, and spending; calls the cyber insurer |
| Operations Manager | Incident coordinator and backup lead; keeps the incident log; directs the MSP |
| Federal Account Manager | Prepares DoD reports and notices; backup for DIBNet reporting |
| Purchasing and Inventory Coordinator | Product side: stop-ship, quarantine, supplier contact, OEM validation |
| MSP | Technical response: isolate, investigate, rebuild, restore; preserves logs |
| Cyber insurer and panel vendors | Breach counsel and forensics, engaged through the insurer's hotline |
| Government contracts counsel | Advises on DoD reports, SPRS and SAM entries, and notices to contracting officers |
| All workforce | Report suspected incidents and suspect products at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most serious likely incident, a supplier compromise that introduces tampered, counterfeit, or covered products (P08), with a printed copy, contact list, and contracting officer contacts in the incident binder in the Owner's office. (IR-8; RS.MA-01)

4.2 Workforce members must report any suspected incident or suspect product to the Operations Manager **at once, and within 1 hour at most**, in person or by phone. If the Operations Manager cannot be reached, report to the Owner. Examples: a supplier asking to change bank details, a resealed box or mismatched serial label, a product from a manufacturer on the screening list, a suspicious link clicked, an unexpected MFA prompt, or a lost laptop. (IR-6; RS.MA-02)

4.3 The Operations Manager must log every incident, including those that turn out to be harmless, with the time of discovery, the time of identification of any covered item, what happened, what was done, and the outcome. (IR-5)

4.4 Suspect items must be put on hold in the ERP and quarantined in the marked stockroom area. They must not be returned, sold, or scrapped until the Owner releases them, or, for items bought for DoD orders, until the contracting officer or the Federal Prime gives disposition instructions. (IR-4; SR-11; RS.MI-01)

4.5 **Government reports.** The Owner, with the Federal Account Manager, must make these reports on time, with counsel's review where time allows (counsel's review never delays a deadline):
- Covered telecommunications or video surveillance equipment identified during DoD contract performance: report at https://dibnet.dod.mil within **1 business day** of identification, then further information within 10 business days (FAR 52.204-25(d)).
- A Kaspersky covered article provided to the Government, where the order includes FAR 52.204-23: report within **3 business days**, then within 10 business days (FAR 52.204-23(c)).
- An electronic part for a DoD order obtained from outside the sourcing order, or that cannot be confirmed as new: prompt written notice to the contracting officer (DFARS 252.246-7008(b)(3)(ii)(A)).
(IR-6; RS.CO-02)

4.6 For any suspected cyber incident, payment fraud, or supplier compromise involving company systems, the Owner must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its contract. (IR-4; RS.MA-02)

4.7 No ransom or extortion payment may be made without the Owner's approval, advice from counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.8 If personal information may have been accessed, the Owner and counsel decide on notices to individuals and the Florida Department of Legal Affairs under Fla. Stat. 501.171, and under the law of each other state where affected individuals live, using the P08 notification matrix. (IR-6; RS.CO-03)

4.9 Supplier, MSP, and SaaS vendor notices of incidents or suspect items must be logged and handled under this policy. (SR-8; IR-6; GV.SC-08)

4.10 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. (IR-3; ID.IM-02)

4.11 Lessons learned must be written up within 30 days of closing any incident that required a report, a notice, or outside help, and fed into the risk register, the C-SCRM plan, and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.13. No exception may delay a contract or legal reporting deadline.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02 (Part A supplier rules); POL-04; C-SCRM plan (due 2026-11-30)

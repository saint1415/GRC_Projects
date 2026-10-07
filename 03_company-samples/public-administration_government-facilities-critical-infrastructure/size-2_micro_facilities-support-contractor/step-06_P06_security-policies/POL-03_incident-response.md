# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office and Compliance Manager (Information Security Officer) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required a customer or legal notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02 |
| Customer and legal drivers | County and city 24-hour incident notice; CT-F immediate notice to the prime (BTTRG 1.6.1); Fla. Stat. 501.171(6)(a); FAR 52.204-23(c), 52.204-25(d), 52.204-30(c); Fla. Stat. 282.3185(5) and 282.3186 (customer duties the company supports) |

## 1. Purpose
Make sure the company keeps building occupants safe, contains intrusions into the customers' building systems quickly, and meets every customer and legal notice deadline.

## 2. Scope
All workforce members of Cris Santos Company, and the MSP and vendors when they handle company systems. It covers the Building Systems Operations Platform, the company's access into customer systems, and every copy of customer data and CUI. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information or of a building system setting; door, schedule, or setpoint changes nobody can tie to a work order; lost or stolen devices, badges, or PIV cards; and mis-shared drawings or CUI.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office and Compliance Manager | Incident lead; keeps the incident log; sends customer and FAR notices; decides with counsel whether personal information was breached |
| Owner | Backup incident lead; calls the cyber insurer; approves outside communications, spending, and any decision on a ransom |
| Lead Controls Technician | Technical lead for SYS-02, the gateways, and BAS changes |
| Security Systems Technician | Technical lead for SYS-01 (doors, cardholders, video) |
| MSP | Laptops, office network, suite: isolate, investigate, rebuild, restore; preserves logs |
| Cyber insurer and its panel | Breach counsel and forensics, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most serious likely incident, an intrusion into building access control and automation systems (P08), with a printed copy and contact card in the office, the on-call bag, and the owner's home. (IR-8; RS.MA-01)

4.2 Workforce members must report any suspected incident to the Office and Compliance Manager **at once, and within 1 hour at most**, by phone. If the Office and Compliance Manager cannot be reached, report to the owner. A door, lock, or HVAC condition that puts people at risk is reported to the customer's security staff or facilities contact **first**, then to the company. (IR-6; RS.MA-02)

4.3 **Safety first.** Before preserving evidence, the incident lead must agree with the customer's security staff on how doors and building systems will be held safe (for example, doors locked to schedule, guards posted, BAS equipment in local or manual mode). (IR-4; RS.MI-01)

4.4 The Office and Compliance Manager must log every incident, including those that turn out to be harmless, with the time found, what happened, what was done, and the outcome. (IR-5; RS.MA-02)

4.5 Notices to customers must meet the clocks in the P08 notification matrix: the county and the city within 24 hours of discovery; the prime **immediately** when GSA systems, GSA data, CUI, or a PIV card or GSA credential may be involved. The company's notice must give a county or city enough facts in time for its own state report (Fla. Stat. 282.3185(5)). (IR-6; RS.CO-02)

4.6 For any incident that may involve personal information in SYS-01 or company HR data, the Office and Compliance Manager, with counsel, must decide whether a breach occurred and record the date of that determination. Third-party agent notice to the customer is due no later than 10 days after the determination (Fla. Stat. 501.171(6)(a)), and the 24-hour contract notice comes first. (IR-6; RS.AN-03; RS.CO-03)

4.7 For any suspected intrusion, ransomware, or data theft, the owner must call the cyber insurer's hotline before hiring any outside firm, and the MSP must be engaged under its contract. (IR-4; IR-7; RS.MA-02)

4.8 **FAR reports (CT-F).** If covered telecommunications or video surveillance equipment is found in anything supplied to or used at the federal building, the Office and Compliance Manager reports to the prime within one business day of identification (52.204-25(d)); a Kaspersky covered article or a FASCSA-order article within 3 business days (52.204-23(c); 52.204-30(c)). (IR-6; GV.SC-05)

4.9 No ransom may be paid on behalf of a county or city (Fla. Stat. 282.3186 bars them from paying). Any payment for the company's own systems needs the owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)

4.10 Vendors and the MSP must report incidents to the Office and Compliance Manager as their contracts require (POL-02 A.5). Each report is logged and handled under this policy. (IR-6; SA-9; GV.SC-08)

4.11 The runbook must be tested every year with a tabletop exercise that includes the county and the MSP, and after any real incident that used it. All staff walk through the runbook once a year. (IR-2; IR-3; ID.IM-02)

4.12 Lessons learned must be written up within 30 days of closing any incident that required a customer or legal notice, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a safety action or a required notice.

## 7. Related documents
P08 incident response runbook and notification matrix; POL-02; POL-04; county and city contract security terms; CT-F subcontract; Fla. Stat. 501.171

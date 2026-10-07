# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | C-COMMUNICATIONS-R01: 47 CFR 64.2011. C-COMMUNICATIONS-R02: 47 CFR 4.9, 4.18. C-COMMUNICATIONS-R03: 47 CFR 1.20003(c). Fla. Stat. 501.171 |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents and outages quickly and lawfully, and meets every CPNI, outage, CALEA, and state breach notification deadline.

## 2. Scope
All workforce members of Cris Santos Company and every system and copy of company information, including systems that the MSP, the consultant, and SaaS vendors run for the company.
- A **security incident** is any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, or interference with a system or the network. It includes lost or stolen devices and a caller who obtains call detail without proper authentication.
- A **CPNI breach** occurs when a person, without authorization or exceeding authorization, intentionally gains access to, uses, or discloses CPNI (47 CFR 64.2011(e)).
- An **outage** is a significant degradation in customers' ability to make and keep a connection because of a failure in the company's network (47 CFR 4.5(a)).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Incident lead for security incidents; decides, with counsel, whether a CPNI breach has been reasonably determined; files the law enforcement notice; keeps the incident register |
| Owner and General Manager | Backup incident lead; calls the cyber insurer; approves outside communications and spending; CALEA compromise reports |
| Network Operations Lead | Incident lead for outages and network containment; NORS, 911 outage contact notices, and DIRS reports |
| Network engineering consultant | Network investigation and rebuild under the Network Operations Lead |
| MSP | Office IT response: isolate, investigate, rebuild, restore |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely serious incident, a network intrusion exposing CPNI (P08), with an outage checklist and contact list. Printed copies are kept at the office, in the hut, and at the homes of the Office Manager, the Network Operations Lead, and the Owner and General Manager. (IR-8; RS.MA-01)

4.2 Workforce members must report any suspected incident to the Office Manager **at once, and within 1 hour at most**, in person or by phone; outages go to the on-call technician at once. If the Office Manager cannot be reached, report to the Owner and General Manager. Examples: a strange login prompt or pop-up, a configuration change nobody made, a caller pressing for call detail without a PIN, a lost tablet, or a law enforcement call. (IR-6; RS.MA-02)

4.3 The Office Manager must log every incident in the incident register, including those that turn out to be harmless. For a CPNI breach, the record must include, where available, the dates of discovery and of each notification, a detailed description of the CPNI involved, and the circumstances, and must be kept at least 2 years. (IR-5; 64.2011(d))

4.4 For any incident that may involve CPNI, the Office Manager, with counsel, must decide whether a breach has been reasonably determined and record the date and basis. The decision must not wait for forensics to finish: evidence that an unauthorized person read or exported CPNI is enough. (IR-6; RS.AN-03; 64.2011(b), (e))

4.5 CPNI breach notices follow the P08 notification matrix:
- The Office Manager must notify the USSS and FBI through the FCC's central reporting facility as soon as practicable and **no later than 7 business days** after reasonable determination (internal target: 2 business days).
- No customer or public notice may be given until 7 full business days after that notice, unless the company has flagged an extraordinarily urgent need and consulted the investigating agency, or the agency directs otherwise.
- Customers whose CPNI was breached are notified after the hold ends.
- Florida and other state notices for personal information follow the matrix, with counsel coordinating the timing with the federal hold.

Counsel reviews every notice before it goes out. At the start of every incident, the Office Manager must check whether the FCC has made the 2023 amendments to 64.2011 effective. (IR-6; RS.CO-02; RS.CO-03)

4.6 **CALEA.** The Owner and General Manager must report to the affected law enforcement agencies, within a reasonable time after discovery, any compromise of a lawful intercept or of call-identifying information, and any unlawful electronic surveillance on company premises. Only the General Manager and the Network Operations Lead may handle intercept information during an incident. (IR-6; 1.20003(c))

4.7 **Outages.** The Network Operations Lead must measure every outage against the thresholds in the outage checklist and: notify the county 911 center's designated contacts within 30 minutes when the 47 CFR 4.5(e) test is met; file NORS notifications within 120 minutes (wireline) or the 4.9(g) times (VoIP); and file daily DIRS reports whenever the FCC activates DIRS for the county. The 911 contacts must be confirmed every year. (IR-6; CP-2; 4.9(f)-(h); 4.18)

4.8 For any suspected intrusion, data theft, or account takeover, the Owner and General Manager must call the cyber insurer's breach hotline before hiring any outside firm. The MSP (office IT) and the consultant (network) are engaged under their contracts. (IR-4; RS.MA-02)

4.9 No ransom or extortion payment may be made without the Owner and General Manager's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.10 Vendors must report incidents to the Office Manager as their contracts require, and a vendor that maintains personal information for the company must do so within 10 days under Fla. Stat. 501.171(6)(a). The Office Manager must log each report and handle it under this policy. (IR-6; SA-9; GV.SC-08)

4.11 The runbook must be tested every year with a tabletop exercise that includes the MSP and the consultant, and after any real incident that used it. (IR-3; ID.IM-02)

4.12 Lessons learned must be written up within 30 days of closing any incident that required notification or outside help, and fed into the risk register, CPNI training, and the next CPNI certification evidence file (POL-02 A.7). (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.10. No exception may delay a legally required notification.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; outage checklist; CALEA SSI policies; POL-02; POL-04; 47 CFR 64.2011; 47 CFR Part 4; Fla. Stat. 501.171

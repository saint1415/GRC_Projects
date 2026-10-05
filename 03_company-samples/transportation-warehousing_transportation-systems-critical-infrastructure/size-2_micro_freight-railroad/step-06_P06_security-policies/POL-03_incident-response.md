# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office Manager (Security Lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident reported to TSA or that needed outside help |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | C-TRANSPORTATION-S01 (49 CFR 1570.203; Appendix A to part 1570); C-TRANSPORTATION-S03 (1520.9(c)); C-TRANSPORTATION-S05 (part 225); C-TRANSPORTATION-S07 (Fla. Stat. 501.171) |

## 1. Purpose
Make sure the railroad keeps trains safe, then spots, contains, reports, and recovers from security incidents quickly and lawfully, and meets every reporting deadline, starting with the TSA 24-hour report.

## 2. Scope
All employees of Cris Santos Company and every system and copy of company information, including the operations system, the radio system, crew tablets, and systems the MSP and SaaS vendors run for the company. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, interference with a system, lost or stolen devices, and suspicious emails that were acted on.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Incident lead (cyber); keeps the incident log; directs the MSP |
| Owner and General Manager | Operations lead (train safety) and primary Security Coordinator: makes the TSA report; calls the cyber insurer; approves outside communications and spending |
| Roadmaster | Alternate Security Coordinator and relief dispatcher; takes over either role when the General Manager is unavailable |
| MSP | Technical response: isolate, investigate, rebuild, restore; preserves logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All employees | Report suspected incidents at once |

## 4. Policy statements
4.1 The railroad must keep an incident response runbook for its most likely serious incident, ransomware on the dispatch and office systems (P08). A printed copy, the contact card, and the TSA report form must be kept in the incident binder at the dispatch desk and in the General Manager's and Roadmaster's vehicles. (IR-8; RS.MA-01)

4.2 Employees must report any suspected incident to the Office Manager **at once, and within 1 hour at most**, in person or by phone. Anything that affects dispatch, radio, or the crew tablets must also be told to the dispatcher immediately. If the Office Manager cannot be reached, report to the General Manager. Examples: clicking a suspicious link, a ransom note or locked files, an unexpected MFA prompt, an authority or switch list that looks wrong, a lost tablet or phone, or someone asking for security information. (IR-6; RS.MA-02)

4.3 **Safety first.** If the dispatcher has any doubt about the integrity or availability of the operations system or the dispatch desktop, the dispatcher must switch to paper dispatch under the contingency plan: radio roll call of every train and work group, then paper authorities only. Trains without radio contact stop until contact is restored. (CP-2; RC.RP-01)

4.4 **TSA report.** Any cyber attack on company systems, meaning any compromise of, or attempt to compromise or disrupt, the company's information or technology infrastructure (Appendix A to 49 CFR part 1570, "Cyber Attack"), must be reported to TSA by a Security Coordinator as soon as possible and **within 24 hours of initial discovery** (49 CFR 1570.203). The company target is 12 hours. Do not wait for the investigation to finish. When in doubt, report. The Office Manager records the discovery time when the incident is opened. (IR-6; RS.CO-02)

4.5 If SSI may have been released to anyone without a need to know, including through data theft, a Security Coordinator must promptly inform TSA (49 CFR 1520.9(c)). (IR-6; RS.CO-02)

4.6 Other notifications (FRA, the National Response Center, Florida breach notices, the connecting Class I, customers) must meet the deadlines in the P08 notification matrix. Breach counsel reviews breach notices to individuals before they are sent; the TSA report is never held for that review. (IR-6; RS.CO-02; RS.CO-03)

4.7 For any suspected ransomware, data theft, or account takeover, the General Manager must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its contract. (IR-4; RS.MA-02)

4.8 No ransom may be paid without the Owner and General Manager's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.9 The Office Manager must log every incident, including those that turn out to be harmless, with the discovery time, what happened, what was done, who was notified, and the outcome. (IR-5)

4.10 Vendors must report incidents that affect company data or systems as their contracts require (POL-02 A.5). The Office Manager logs each report and handles it under this policy. (IR-6; SA-9)

4.11 The runbook must be tested every year with a tabletop exercise that includes the MSP, and paper dispatch must be drilled twice a year. Both are also required after any real incident that used them. (IR-3; ID.IM-02)

4.12 Lessons learned must be written up within 30 days of closing any incident reported to TSA or that needed outside help, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07), the annual tabletop, and the paper dispatch drills.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay the TSA report, a safety step, or any other legally required notice.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; contingency plan (due 2026-11-30); POL-02; POL-04; hazmat security plan

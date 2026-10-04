# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office and Compliance Manager (Security Coordinator) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Legal duties | 19 CFR 111.21(b) (72-hour notice to the CBP Security Operations Center); Fla. Stat. 501.171(3)-(6) |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents quickly and lawfully, recovers diverted payments where it can, and meets every notice deadline, starting with the 72-hour CBP notice.

## 2. Scope
All employees and every system and copy of company information, including systems the MSP and SaaS vendors run for the company. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, a payment sent on false instructions, interference with a system, a lost or stolen device, and client records sent to the wrong person.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office and Compliance Manager | Incident lead; keeps the incident log; prepares the CBP notice and the importer number list |
| Owner | Backup incident lead; decides on breach status with counsel; calls the cyber insurer; approves outside communications, spending, and the CBP notice |
| Accounting Specialist | Calls the bank fraud line at once for any suspect wire |
| MSP | Technical response: lock accounts, investigate, rebuild, restore; preserves logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All employees | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely serious incident, business email compromise with payment diversion and client record exposure (P08), with a printed copy and contact card in the office and at the owner's and the Security Coordinator's homes. (IR-8; RS.MA-01)

4.2 Employees must report any suspected incident to the Office and Compliance Manager **at once, and within 1 hour at most**, in person or by phone. If she cannot be reached, report to the owner. Examples: clicking a suspicious link or entering a password on a strange page, a request to change bank details, an unexpected MFA prompt, a mailbox rule you did not create, a lost phone or laptop, or client documents sent to the wrong person. (IR-6; RS.MA-02)

4.3 **Suspect wire: call the bank first.** If a wire may have gone to a fraudulent account, the Accounting Specialist or the owner must call the bank's fraud line immediately, before anything else, and ask for a recall. The owner files a complaint with the FBI's Internet Crime Complaint Center (IC3) the same day. (IR-4; RS.MI-01)

4.4 The Security Coordinator must log every incident, including harmless ones and near-misses, with the date found, what happened, what was done, and the outcome. (IR-5)

4.5 **CBP notice within 72 hours.** For any known breach of electronic or physical records relating to customs business, the owner must make sure the CBP Security Operations Center is notified electronically within 72 hours of discovery, including any known compromised importer identification numbers; an updated list is sent within 10 business days, and any later information within 72 hours of finding it (19 CFR 111.21(b)). The clock starts when the company knows of the breach; do not wait for the forensic report. (IR-6; RS.CO-02)

4.6 For any incident that may involve personal information, the Security Coordinator, with breach counsel, must document whether a breach under Fla. Stat. 501.171 occurred and the date of that determination. Notices to individuals, the Department of Legal Affairs, consumer reporting agencies, and clients must meet the deadlines in the P08 notification matrix, and counsel reviews each notice before it is sent. (IR-6; RS.AN-03; RS.CO-03)

4.7 For any suspected account takeover, payment fraud, ransomware, or data theft, the owner must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its contract. (IR-4; RS.MA-02)

4.8 No ransom or extortion payment may be made without the owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.9 Vendors that hold company or client data must report incidents to the Security Coordinator; for vendors that hold personal information, within 10 days of their determination (Fla. Stat. 501.171(6)(a)). The Security Coordinator logs each report and handles it under this policy. (IR-6; SA-9)

4.10 The runbook must be tested every year with a tabletop exercise that includes the MSP and the bank's fraud process, and after any real incident that used it. (IR-3; ID.IM-02)

4.11 Lessons learned must be written up within 30 days of closing any incident that required notification or outside help, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a legally required notice.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02 (B.10 payments); POL-04 (importer number data map); 19 CFR 111.21(b); Fla. Stat. 501.171

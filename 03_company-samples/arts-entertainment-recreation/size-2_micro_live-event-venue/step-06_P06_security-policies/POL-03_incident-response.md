# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Venue Manager (Security and Privacy Lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, AU-6, AU-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, DE.CM-01, ID.IM-02 |
| PCI DSS v4.0.1 (N71-R04) | 10.4, 10.5, 12.10 |
| Law | Fla. Stat. 501.171; each state where affected individuals reside; FTC Act Section 5 (N71-R05) |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents quickly, meets every acquirer, card brand, and breach notification deadline, and keeps shows running safely while it does.

## 2. Scope
All employees, owners, and contractors (including the MSP, the web designer, and event-night workers), and every system and copy of company information, including systems that the ticketing vendor, payment partner, POS vendor, MSP, and other SaaS providers run for the company. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, or interference with a system, as well as a missing or tampered card reader, a card number received by email, and an unexplained change to the website or ticketing settings.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Venue Manager | Incident lead; keeps the incident log; runs the weekly log check |
| Owner and General Manager | Backup incident lead; calls the cyber insurer; contacts the acquirer; approves outside communications and spending |
| Box Office and Ticketing Manager and Marketing Coordinator | Contain the ticketing platform and the website; preserve their evidence |
| MSP | Technical response on office computers, network, and suite; preserves logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All workforce and contractors | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely serious incident, a ticketing channel breach exposing customer and card data (P08), with a printed copy and contact card in the back office and at the Owner's home. (IR-8; RS.MA-01; PCI 12.10.1)

4.2 Everyone, including contractor door staff and bartenders, must report a suspected incident to the Venue Manager **at once, and within 1 hour at most**, in person, by radio, or by phone. If the Venue Manager cannot be reached, report to the Owner. Examples: a card reader that looks different, is missing, or has extra parts; a strange pop-up or payment form on the website; a card number received by email; an MFA prompt or password reset you did not start; a patron reporting card fraud after buying tickets. (IR-6; RS.MA-02; PCI 12.10)

4.3 The Venue Manager must log every incident, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5)

4.4 **Log checks.** The Venue Manager must check the ticketing audit log (exports, refunds, new users and roles, setting and API token changes), suite sign-in alerts, and website change alerts every week, record the check, and export the ticketing audit log every month to a restricted suite folder so that 12 months are kept. (AU-6; AU-11; DE.CM-01; PCI 10.4; 10.5)

4.5 **Acquirer and card brands.** For any suspected compromise of card data, the Owner must notify the acquirer **within 24 hours of suspicion** (merchant agreement term) and follow the card brand instructions the acquirer gives. The clock starts at suspicion, not confirmation. (IR-6; RS.CO-02; PCI 12.10.1)

4.6 For any suspected compromise, the Owner must call the cyber insurer's breach hotline before hiring any outside firm. The MSP is engaged under its contract for office computers, network, and suite. (IR-4; RS.MA-02)

4.7 **Breach decisions and notices.** The Venue Manager must record the time of suspicion and the time the company determined that a breach occurred or had reason to believe one occurred. With breach counsel, the company decides which notices are due and sends them by the deadlines in the P08 notification matrix: individuals and the Department of Legal Affairs under Fla. Stat. 501.171, consumer reporting agencies when required, and the law of each state where affected individuals reside. Counsel reviews every notice before it is sent. (IR-6; RS.AN-03; RS.CO-02; RS.CO-03)

4.8 **Preserve evidence.** No one may delete a suspicious script, account, API token, or email before it has been captured (screenshot or export with the time) and the capture saved in the incident folder, unless the Venue Manager decides that leaving it running causes more harm. (IR-4; RS.AN-03)

4.9 No ransom or extortion payment may be made without the Owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.10 **Vendor incidents.** Incident reports from the ticketing vendor, payment partner, POS vendor, MSP, or web designer must be logged and handled under this policy. Contracts renewed after 2026-09-01 must require notice to the company within 72 hours of the vendor confirming an incident that affects company data. (IR-6; SA-9; GV.SC-08)

4.11 The runbook must be tested every year with a tabletop exercise that includes the MSP and a call to the insurer's hotline, and after any real incident that used it. (IR-3; ID.IM-02; PCI 12.10.2)

4.12 Lessons learned must be written up within 30 days of closing any incident that required notification or outside help, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.12. No exception may delay a contractual or legally required notification.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; merchant agreements; cyber insurance policy; Fla. Stat. 501.171

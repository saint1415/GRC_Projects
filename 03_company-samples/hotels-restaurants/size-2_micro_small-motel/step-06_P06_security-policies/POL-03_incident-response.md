# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Assistant Manager (Security and Privacy Lead) |
| Approved by | Owner-Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Yearly (next review 2027-08-31), and after any incident that required notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Requirements | PCI DSS v4.0.1 requirement group 12.10 (N72-R01); merchant agreement notice terms; Fla. Stat. 501.171 and other states' breach laws (N72-R04) |

## 1. Purpose
Make sure the motel spots, contains, reports, and recovers from security incidents quickly, meets the acquirer's and card brands' deadlines, and meets every breach notification deadline.

## 2. Scope
All workforce members and every system and copy of motel information, including systems the MSP, the PMS vendor, the payment gateway, and the lock vendor run for the motel. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, interference with a system, a suspected tampered terminal, a lost or stolen device, and guest or card information sent or handed to the wrong person.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Assistant Manager | Incident lead; keeps the incident log; prepares the breach analysis with counsel |
| Owner-Manager | Backup incident lead; calls the cyber insurer and the acquirer; approves outside communications and any spending; decides on notices with counsel |
| MSP | Technical response: isolate, preserve, rebuild, restore |
| Cyber insurer and its panel vendors | Breach counsel and a forensic firm, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The motel must keep an incident response runbook for its most likely serious incident, a compromise of front office payment and reservation systems (P08), with a printed copy and contact card in the front desk binder and in the Owner-Manager's apartment. (IR-8; RS.MA-01; PCI DSS 12.10)

4.2 Workforce members must report any suspected incident to the Assistant Manager **at once, and within 1 hour at most**, in person or by phone. If the Assistant Manager cannot be reached, report to the Owner-Manager, who lives on site. Examples: a strange pop-up or slow front desk PC, a call or email asking for card or guest details, a crew company or guest reporting card fraud after a stay, a terminal that looks different or has loose parts, a lost key card list, or a remote support session nobody asked for. (IR-6; RS.MA-02; PCI DSS 12.10)

4.3 The Assistant Manager must log every incident, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5)

4.4 For a suspected card compromise, staff must not turn off, wipe, or "clean" an affected PC or terminal. They disconnect it from the network, leave it on, stop keyed card entry on PCs, and wait for the MSP or the forensic firm. (IR-4; RS.MI-01)

4.5 The Owner-Manager must notify the acquirer within 24 hours of suspecting a card compromise (merchant agreement term; fictional), and follow the acquirer's instructions for the card brands, including Visa's 3-calendar-day notice. These clocks start at suspicion, not confirmation. (IR-6; RS.CO-02; PCI DSS 12.10)

4.6 For any incident that may involve personal information, the Assistant Manager, with breach counsel, must record the date of determination of the breach or reason to believe a breach occurred, count affected individuals by state, and decide which notices are due under the P08 notification matrix. Notices to Florida residents are due no later than 30 days after that date (Fla. Stat. 501.171(4)(a)); other states' laws apply to their residents. A decision not to notify under 501.171(4)(c) must be made in writing after consultation with law enforcement, kept at least 5 years, and sent to the Department of Legal Affairs within 30 days. (IR-6; RS.AN-03; RS.CO-03)

4.7 For any suspected compromise, ransomware, or account takeover, the Owner-Manager must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its contract. (IR-4; RS.MA-02)

4.8 No ransom may be paid without the Owner-Manager's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.9 Vendors that maintain personal information for the motel must report breaches to the Assistant Manager; Florida requires a third-party agent to do so no later than 10 days after its determination (Fla. Stat. 501.171(6)(a)). The Assistant Manager logs each report and handles it under this policy. (IR-6; SA-9)

4.10 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. (IR-3; ID.IM-02; PCI DSS 12.10)

4.11 Lessons learned must be written up within 30 days of closing any incident that required notification or outside help, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the yearly assessment (P07) and the yearly tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a contractual or legally required notification.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; merchant agreement; Fla. Stat. 501.171

# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office Manager (Qualified Individual) |
| Approved by | Owner CPA, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02, GV.SC-08 |
| Rules | FTC Safeguards Rule 16 CFR 314.4(j) (N54-R01); IRS Pub. 1345 Reporting of Security Incidents (N54-R03); IRC 7216 (N54-R02); Fla. Stat. 501.171 |

**Why the firm has a written plan when the rule does not require one.** The Safeguards Rule's written incident response plan (314.4(h)) does not apply to a firm with fewer than 5,000 consumers (314.6). The firm adopts one anyway, because the IRS requires an e-file provider to report a security incident by the next business day after confirmation (Pub. 1345), the FTC notice clock starts when any employee knows of an event (314.4(j)(2)), and business email compromise is the firm's top risk (P01 R-001).

## 1. Purpose
Make sure the firm spots, contains, reports, and recovers from security incidents quickly and lawfully, protects clients from refund and payroll fraud, and meets every IRS, FTC, and state notification deadline.

## 2. Scope
All workforce members and every system and copy of client and firm information, including systems the MSP and SaaS vendors run for the firm. A "security incident" includes any attempted or successful unauthorized access to, or use, disclosure, change, or destruction of, information; account takeover; a lost or stolen device; misdirected client documents; and a disclosure of tax return information without a permission or consent under IRC 7216 (for example, to an unapproved AI tool).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Incident lead; keeps the incident log; coordinates the MSP and counsel |
| Owner CPA | Backup incident lead; calls the cyber insurer; IRS e-file Responsible Official (IRS and state tax agency reports); decides breach status and notices with counsel; approves spending and outside statements |
| MSP | Technical response: contain, investigate, rebuild, restore; preserves logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The firm must keep an incident response runbook for its most likely serious incident, business email compromise with data theft (P08), with a printed copy and contact card at the front desk and at the Owner CPA's and Office Manager's homes. (IR-8; RS.MA-01)

4.2 Workforce members must report any suspected incident to the Office Manager **at once, and within 1 hour at most**, in person or by phone. If the Office Manager cannot be reached, report to the Owner CPA. Examples: an MFA prompt you did not start, a client asking about an email "from the firm," a request to change bank details, a strange inbox rule, a lost phone or laptop, a return sent to the wrong client, or client information pasted into an unapproved tool. (IR-6; RS.MA-02)

4.3 The Office Manager must log every incident, including those that turn out to be harmless, with what happened, what was done, and the outcome. (IR-5; RS.MA-02)

4.4 The incident log must record three dates, because each starts a different clock: **discovery** (first day any employee, other than a person committing the breach, knows of the event; 314.4(j)(2)), **confirmation** (the event is confirmed as one that can result in unauthorized disclosure, misuse, modification, or destruction of taxpayer information; Pub. 1345), and **determination** (the firm determines a breach occurred or has reason to believe one did; Fla. Stat. 501.171). (IR-6; RS.AN-03)

4.5 For an incident involving taxpayer information, the Owner CPA must report to the IRS through the local Stakeholder Liaison **as soon as possible and no later than the next business day after confirmation**, and notify the tax agencies of the states where affected clients file. (IR-6; RS.CO-02; Pub. 1345)

4.6 If unencrypted customer information of **500 or more consumers** may have been acquired without authorization, the Owner CPA must make sure the FTC is notified on its online form as soon as possible and no later than 30 days after discovery (314.4(j)). (IR-6; RS.CO-02)

4.7 Notices to individuals, the Florida Department of Legal Affairs, consumer reporting agencies, and other states must meet the deadlines in the P08 notification matrix. Breach counsel reviews each notice before it is sent. (IR-6; RS.CO-02; RS.CO-03)

4.8 For any suspected account takeover, data theft, or ransomware, the Owner CPA must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its contract. (IR-4; RS.MA-02)

4.9 When an incident could lead to refund or payroll diversion, the firm must at once freeze bank account changes made in the period of exposure, hold affected returns and payroll runs, and confirm each change with the client by phone on the number on file before release. (IR-4; RS.MI-01)

4.10 No extortion payment may be made without the Owner CPA's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.11 Vendors must report incidents affecting firm data as their contracts require, and in any case as Florida law requires of third-party agents. The Office Manager logs each report and handles it under this policy. (IR-6; SA-9; GV.SC-08)

4.12 The runbook must be tested every year with a tabletop exercise before the filing season that includes the MSP and covers the IRS and FTC steps, and after any real incident that used it. (IR-3; ID.IM-02)

4.13 Lessons learned must be written up within 30 days of closing any incident that required notification or outside help, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.5. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.11. No exception may delay a legally required report or notice.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; IRS Pub. 1345; IRS Data Theft Information for Tax Professionals; 16 CFR 314.4(j); Fla. Stat. 501.171

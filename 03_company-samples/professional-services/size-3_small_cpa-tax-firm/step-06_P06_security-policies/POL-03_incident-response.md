# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | Firm Administrator |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any security event |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-04 |
| FTC Safeguards Rule | 16 CFR 314.4(h), (j) |
| Other | IRS Pub. 1345 (Reporting of Security Incidents); Fla. Stat. 501.171 |

## 1. Purpose
Make sure the firm detects, contains, reports, and recovers from security events quickly and lawfully. This policy and the runbooks under it (starting with P08) are the firm's written incident response plan under 16 CFR 314.4(h). **Goals:** stop the harm to clients (especially fraudulent returns and refund theft), preserve evidence, meet every notification deadline, and restore filing capability within the BIA recovery times.

## 2. Scope
All Cris Santos Company workforce members (partners, employees, seasonal preparers, interns, and contractors) and all security events affecting customer information, tax return information, or firm systems, including events at service providers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager (Qualified Individual) | Incident commander; coordinates the MSP and forensic firm; can isolate systems and disable accounts without further approval |
| Risk and Quality Partner | Breach determinations with outside counsel; approves notifications to clients, the FTC, and states |
| Tax Partner (e-file Responsible Official) | Reports to the IRS Stakeholder Liaison; coordinates with state tax agencies; decides filing holds and extensions |
| Managing Partner | Engages counsel and the cyber insurer; approves external statements; decides any ransom question |
| Firm Administrator | Staff communications; service provider contacts |
| All workforce | Report suspected incidents immediately |

Decision levels: the IT Manager decides technical containment. The Risk and Quality Partner decides whether an event is a notification event or breach. The Managing Partner decides public statements and any payment.

## 4. Policy statements
4.1 The firm must maintain an incident response plan made up of this policy and runbooks for its most likely events, starting with business email compromise and data theft (P08). Together they must address the seven areas in 16 CFR 314.4(h)(1)-(7). (IR-8; RS.MA-01; 314.4(h))
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, by calling the IT incident line or telling their team manager in person. Examples: a phishing click, an unexpected MFA prompt, a client saying the firm emailed a strange request, an IRS reject for a duplicate SSN, a lost device, or a misdirected return. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category, with a timeline of actions. (IR-5; 314.4(h)(6))
4.4 **Discovery date.** The date an event becomes known to any employee or agent (other than the attacker) is the discovery date for FTC purposes (16 CFR 314.4(j)(2)). The incident commander must record it at once.
4.5 The Risk and Quality Partner must decide, with counsel, whether the event is an FTC notification event (unencrypted customer information acquired without authorization; unauthorized access is presumed to be acquisition unless reliable evidence shows otherwise, 16 CFR 314.2(m)) and a breach under each applicable state law, and must document the decision. (IR-6)
4.6 Notifications must meet the deadlines in the P08 notification matrix. In particular: the IRS Stakeholder Liaison no later than the next business day after an incident is confirmed (IRS Pub. 1345); the FTC within 30 days of discovery when 500 or more consumers are involved (16 CFR 314.4(j)); and Florida residents and the Florida Department of Legal Affairs within 30 days of determination (Fla. Stat. 501.171). Counsel must confirm each notice. (IR-6; RS.CO-02; RS.CO-03)
4.7 Changes to a client's refund bank account, mailing address, or email that arrive during or after a suspected compromise must be frozen until verified by a call to the phone number on file. (IR-4)
4.8 No ransom or extortion payment may be made without approval from the Managing Partner, counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.9 Weaknesses found during an incident must be added to the POA&M with an owner and date. (IR-4; 314.4(h)(5))
4.10 The plan must be tested at least annually by tabletop exercise before the filing season, and after any major incident. Lessons learned must be documented within 30 days of closing an incident, and the plan revised. (IR-3; ID.IM-04; 314.4(h)(7))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.11. Compliance is checked through the annual control assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the Managing Partner for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; 16 CFR 314.4(h) and (j); IRS Pub. 1345; IRS Data Theft Information for Tax Professionals; Fla. Stat. 501.171

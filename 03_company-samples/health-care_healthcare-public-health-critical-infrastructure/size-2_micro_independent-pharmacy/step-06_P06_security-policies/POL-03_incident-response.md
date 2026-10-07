# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent community pharmacy) |
| Policy ID | POL-03 |
| Owner | Store Manager (Privacy Officer and Security Officer) |
| Approved by | Pharmacist-owner, 2026-08-28 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, AU-6 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, DE.AE-02, RC.RP-01, ID.IM-02, GV.SC-08 |
| HIPAA | Security Rule 164.308(a)(6); Breach Notification Rule 164.400-414 |
| DEA and Florida | 21 CFR 1311.200(c)-(d), 1311.215(b)-(c), 1311.30(e), 1301.76(b); Fla. Stat. 501.171, 893.055(3)(a), 893.07(5)(b) |

## 1. Purpose
Make sure the pharmacy spots, contains, reports, and recovers from security incidents quickly and lawfully, keeps dispensing safely while systems are down, and meets every breach, DEA, and Florida reporting deadline.

## 2. Scope
All workforce members of Cris Santos Company and every system and copy of pharmacy information, including systems the MSP and SaaS vendors run for the pharmacy. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, or interference with a system, as well as lost or stolen devices, misdirected PHI, misuse of the CSOS certificate, and any event in the daily EPCS audit report that could have compromised controlled substance prescription records.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Store Manager | Incident lead; decides whether an incident is a reportable breach (as Privacy Officer); keeps the incident log |
| Pharmacist-owner | Backup incident lead; DEA registrant contact; calls the cyber insurer; decides on diversion of prescriptions to other pharmacies; approves outside communications and any spending |
| Pharmacist on duty (pharmacist-owner or Staff Pharmacist) | Reviews the daily EPCS audit report; decides whether an event is an EPCS security incident and makes the one-business-day report; runs the downtime procedure at the counter |
| MSP | Technical response: isolate, investigate, rebuild, restore; preserves logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's breach hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The pharmacy must keep an incident response runbook for its most likely serious incident, ransomware on the store computers with PMS downtime at the counter and data theft (P08), with a printed copy, the contact card, and the downtime card at the pharmacist verification station and in the pharmacist-owner's and Store Manager's homes. (IR-8; RS.MA-01)

4.2 Workforce members must report any suspected incident to the Store Manager **at once, and within 1 hour at most**, in person or by phone. If the Store Manager cannot be reached, report to the pharmacist on duty. Examples: clicking a suspicious link, a strange pop-up or locked files, a lost phone or laptop, a fax or email sent to the wrong place, someone using another person's PMS session or the CSOS certificate, or a caller asking for patient information without a reason. (IR-6; RS.MA-02; 164.308(a)(6)(ii))

4.3 The Store Manager must log every incident, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5; 164.308(a)(6)(ii))

4.4 For any incident that may involve PHI, the Store Manager (Privacy Officer) must complete and sign the four-factor breach risk assessment in 45 CFR 164.402 and decide whether the incident is a breach of unsecured PHI. The date of discovery is the first day the incident was known, or by reasonable diligence would have been known, to any workforce member (164.404(a)(2)). (IR-6; RS.AN-03)

4.5 Notifications to individuals, HHS, the media, the Florida Department of Legal Affairs, and consumer reporting agencies must meet the deadlines in the P08 notification matrix. Breach counsel must review each notice before it is sent. (IR-6; RS.CO-02; RS.CO-03; 164.404-164.408; Fla. Stat. 501.171)

4.6 **Daily EPCS audit report.** Each business day the pharmacist on duty must open the PMS EPCS audit report, decide whether any listed event is a security incident that compromised or could have compromised the integrity of controlled substance prescription records, and initial the review log. Any such incident must be reported to the PMS vendor and to DEA within one business day of that decision, and logged under 4.3. (AU-6; IR-6; DE.AE-02; 21 CFR 1311.215(b)-(c))

4.7 **EPCS stop and resume.** If the PMS vendor says the PMS no longer meets the EPCS rule, or a security incident makes its controlled substance records untrustworthy, the pharmacist on duty must stop processing electronic controlled substance prescriptions at once, and resume only when the vendor confirms compliance and the updates are installed. Prescribers are asked to send urgent prescriptions to the partner pharmacy in the meantime. (IR-4; 21 CFR 1311.200(c)-(d))

4.8 **CSOS certificate compromise.** If the CSOS private key or its password may have been lost, stolen, used by someone else, or exposed on a compromised computer, the certificate holder must send a revocation request to the DEA certification authority within 24 hours of substantiation and apply for a new certificate. Schedule II orders use paper DEA order forms until then. (IR-6; SC-12; 21 CFR 1311.30(e))

4.9 **Controlled substance theft or significant loss.** If an incident includes the theft or significant loss of controlled substances, the pharmacist-owner must report it to the county sheriff within 24 hours of discovery (Fla. Stat. 893.07(5)(b)), notify the DEA Field Division Office in writing within one business day of discovery, and file DEA Form 106 within 45 days (21 CFR 1301.76(b)). (IR-6; RS.CO-02)

4.10 **PDMP during downtime.** Controlled substances dispensed on paper during an outage must still be reported to the PDMP by the close of the next business day, through the PDMP web portal from a clean device if the PMS cannot send its file, or the pharmacist-owner must ask the Department of Health for an extension before the deadline (Fla. Stat. 893.055(3)(a)). (IR-4; RC.RP-01)

4.11 For any suspected ransomware, data theft, or account takeover, the pharmacist-owner must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its BAA and contract. (IR-4; RS.MA-02)

4.12 No ransom may be paid without the pharmacist-owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4; RS.MI-01)

4.13 Business associates must report incidents to the Store Manager as their BAA requires. The Store Manager must log each report and handle it under this policy. (IR-6; SA-9; GV.SC-08; 164.314(a)(2)(i))

4.14 The runbook must be tested every year with a tabletop exercise that includes the MSP and both pharmacists, and after any real incident that used it. (IR-3; ID.IM-02)

4.15 Lessons learned must be written up within 30 days of closing any incident that required notification or outside help, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. The pharmacist-owner checks the EPCS review log each month. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a legally required notification or report.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; downtime card (contingency plan, due 2026-11-30); POL-02; POL-04; HIPAA Breach Notification Rule; 21 CFR Part 1311; Fla. Stat. 501.171, 893.055, and 893.07

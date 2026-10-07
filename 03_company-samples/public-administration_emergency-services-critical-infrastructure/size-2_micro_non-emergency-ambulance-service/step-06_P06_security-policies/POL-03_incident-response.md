# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office Manager (Privacy Officer and Security Officer) |
| Approved by | Owner, 2026-09-04 |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required notification or manual dispatch |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| HIPAA (C-EMERGENCY-R04) | Security Rule 164.308(a)(6); Breach Notification Rule 164.400-414 |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents quickly and lawfully, keeps patients moving while it does, and meets every breach notification deadline.

## 2. Scope
All workforce members of Cris Santos Company and every system and copy of company information, including systems the MSP and SaaS vendors run for the company and the devices in the ambulances. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, or interference with a system, as well as lost or stolen devices, misdirected faxes or emails, and an outage of the dispatch board caused by a security event.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Incident lead; decides whether an incident is a reportable breach (as Privacy Officer); keeps the incident log |
| Owner | Backup incident lead; calls the cyber insurer; approves outside communications and spending; decides on manual dispatch beyond one day |
| Scheduler-Dispatcher | Starts manual dispatch; keeps crews and facilities informed |
| MSP | Technical response for office computers, network, and backup: isolate, investigate, rebuild, restore; preserves logs |
| Operations platform vendor | Checks the company's tenant for misuse; suspends sessions; supplies logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely serious incident, ransomware with a dispatch outage and data theft (P08), with printed copies and the contact card at the dispatch desk, in the on-call bag, in each ambulance, and at the Owner's home. (IR-8; RS.MA-01)

4.2 Workforce members must report any suspected incident to the Office Manager **at once, and within 1 hour at most**, by phone or in person. If the Office Manager cannot be reached, report to the Owner. Crews on a trip report as soon as the patient is handed over. Examples: clicking a suspicious link, an unexpected MFA prompt, a strange pop-up or locked files, a dispatch board that will not load or shows changes nobody made, a lost tablet or phone, a face sheet sent to the wrong place, or someone asking for patient information without a reason. (IR-6; RS.MA-02; 164.308(a)(6)(ii))

4.3 The Office Manager must log every incident, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5; 164.308(a)(6)(ii))

4.4 For any incident that may involve PHI, the Office Manager (Privacy Officer) must complete and sign the four-factor breach risk assessment in 45 CFR 164.402 and decide whether the incident is a breach of unsecured PHI. The date of discovery is the first day the incident was known, or by reasonable diligence would have been known, to any workforce member (164.404(a)(2)). (IR-6; RS.AN-03)

4.5 Notifications to individuals, HHS, the media, the Florida Department of Legal Affairs, and consumer reporting agencies must meet the deadlines in the P08 notification matrix. Breach counsel must review each notice before it is sent. (IR-6; RS.CO-02; RS.CO-03; 164.404-164.408)

4.6 **Patients first.** When the dispatch board or the office computers are unavailable, the Scheduler-Dispatcher must switch to manual dispatch from the printed run sheet at once and call the dialysis centers about the day's runs. Any caller who describes an emergency must be told to dial 911, whatever the state of the systems. (IR-4; RC.RP-01)

4.7 For any suspected ransomware, data theft, or account takeover, the Owner must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its BAA and contract. Outside MSP hours, the insurer's 24x7 hotline is the first technical call. (IR-4; RS.MA-02)

4.8 No ransom may be paid without the Owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.9 Business associates must report incidents to the Office Manager as their BAA requires. The Office Manager must log each report and handle it under this policy. (IR-6; SA-9; 164.314(a)(2)(i))

4.10 The runbook must be tested every year with a tabletop exercise that includes the MSP and a manual dispatch drill, and after any real incident that used it. (IR-3; ID.IM-02)

4.11 Lessons learned must be written up within 30 days of closing any incident that required notification, manual dispatch, or outside help, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07), the annual tabletop, and the quarterly manual dispatch drill.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a legally required notification or a 911 redirect.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; contingency plan (due 2026-11-30); HIPAA Breach Notification Rule; Fla. Stat. 501.171

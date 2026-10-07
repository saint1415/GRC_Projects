# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Operations Manager (Security and Compliance Officer) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), after any incident that required an agency notice, and within 60 days of a new CJIS Security Policy version |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, SR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Contract and legal drivers | CJISSECPOL v6.1 IR-6 and AT-2 (AC-01); Pub. 1075 sec. 1.8.2-1.8.4 and Exhibit 7 (SC-01); Fla. Stat. 501.171(6); SP 800-53 Moderate (AC-02, AC-03, AC-04) |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents quickly, and tells every agency and the prime fast enough for them to meet their own reporting duties.

## 2. Scope
All staff and every company system, laptop, and account, including systems the MSP and vendors run for the company, and the company's access to agency systems. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, interference with a system, a lost or stolen laptop or phone, agency data sent to the wrong place, and any FTI found outside the agency's virtual desktop.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager | Incident lead; sends every notice to agencies and the prime; keeps the incident log; decides with counsel whether a breach occurred |
| Lead Platform Engineer | Technical lead for the platform tenant and SYS-02; backup incident lead |
| Owner | Decision maker for money, ransom, and customer communication; calls the cyber insurer |
| MSP | Laptop and suite response: isolate, investigate, reimage; preserves laptop and suite logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the hotline |
| All staff | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely serious incident, ransomware that reaches agency data (P08), with a notification matrix and a printed contact card held by the owner, the Operations Manager, and the Lead Platform Engineer. (IR-8; RS.MA-01)

4.2 Staff must report any suspected incident to the Operations Manager **at once, and no more than 1 hour after discovery**, by phone. If the Operations Manager cannot be reached, call the Lead Platform Engineer, then the owner. This 1-hour rule comes from the CJIS Security Policy (IR-6) and applies to every incident, not only CJI. Examples: a suspicious link clicked, an unexpected MFA prompt, a ransom note, files that will not open, a lost laptop, agency data emailed to the wrong person, or FTI noticed in any company file. (IR-6; RS.MA-02)

4.3 The Operations Manager must log every incident, including those that turn out to be harmless, with the discovery time, what happened, what was done, and who was told. **Never put CJI or FTI in the incident log, email, chat, or tickets.** Describe it by record key and count. (IR-5; RS.MA-01)

4.4 **Notice to customers and the prime.** The Operations Manager must give these notices by phone, then in writing through the agreed channel:
- **AC-01 (CJI):** to the AC-01 LASO within 1 hour of discovery of any suspected incident that may involve the AC-01 workspace, SYS-02, the sheriff's file drop, or support tickets from sheriff users, without waiting for the company's investigation.
- **SC-01 (FTI):** to the prime's security officer and the revenue agency's disclosure officer at once, with a company target of 1 hour, for any possible improper inspection or disclosure of FTI, including a spill into a company system, a compromised approved laptop, or an unapproved connection. The agency must contact TIGTA and the IRS Office of Safeguards within 24 hours and may not wait for an investigation (Pub. 1075 sec. 1.8.2-1.8.4). If the company cannot confirm within 24 hours that the agency has reported, it reports to TIGTA itself (sec. 1.8.2 places the duty on any person who discovers a possible improper disclosure).
- **AC-02, AC-03, AC-04:** to each agency's security contact within 4 hours of discovery of any suspected incident affecting its data, and within 1 hour for suspected ransomware, so a county or city can file its report within 12 hours of discovery (Fla. Stat. 282.3185(5)(b)).
(IR-6; RS.CO-02; RS.CO-03)

4.5 **Breach determination and the 10-day notice.** For any incident that may involve personal information, the Operations Manager, with breach counsel, decides whether a breach of security occurred. The company must give each affected agency written notice as expeditiously as practicable and no later than 10 days after determining the breach or having reason to believe it occurred, with all the information the agency needs for its own notices (Fla. Stat. 501.171(6)(a)). The company sends notices to individuals only if an agency asks it to in writing (501.171(6)(b)). (IR-6; RS.AN-03)

4.6 For suspected ransomware, data theft, or account takeover, the owner must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its contract. (IR-4; IR-7; RS.MA-02)

4.7 **Ransom.** No ransom may be paid without the owner's approval, advice from breach counsel and the insurer, consultation with every affected agency, and an OFAC sanctions check. Florida state agencies, counties, and municipalities may not pay or otherwise comply with a ransom demand (Fla. Stat. 282.3186); the company will not pay over agency data that any agency objects to. (IR-4)

4.8 Vendors and the MSP must report security incidents affecting company or agency data within 24 hours (contract term added at each renewal under POL-02 A.5). The Operations Manager logs each report and handles it under this policy. (SR-8; IR-6)

4.9 All staff must be briefed on this policy at hire and every year. The runbook must be tested every year with a tabletop exercise that includes the MSP and at least one agency security contact, and after any real incident that used it. (IR-2; IR-3; ID.IM-02)

4.10 Lessons learned must be written up within 30 days of closing any incident that required an agency notice or outside help, and fed into the risk register and training. Staff involved in an incident affecting CJI must complete refresher security awareness training within 30 days (CJISSECPOL v6.1 AT-2). (IR-4; ID.IM-02)

4.11 Incident records, evidence, and notices must be kept at least 3 years, or longer if an agency or the insurer requires (POL-02 A.7). (IR-5)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a notice to an agency or the prime.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; CJIS Security Addendum; SC-01 subcontract (Exhibit 7); Fla. Stat. 501.171; cyber insurance policy

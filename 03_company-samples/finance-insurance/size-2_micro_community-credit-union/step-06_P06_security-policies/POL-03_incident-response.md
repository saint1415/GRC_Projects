# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Community Federal Credit Union |
| Policy ID | POL-03 |
| Owner | Operations Manager (Information Security Officer and Privacy Officer) |
| Approved by | Board of Directors, 2026-08-25 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required a regulator or member notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02 |
| NCUA Part 748 | 748.0(b)(3), (b)(4); 748.1(c) (C-FINANCIAL-R03); 748.1(d); Appendix A III.C.1.g; Appendix B |

## 1. Purpose
Make sure the credit union spots, contains, reports, and recovers from security incidents quickly and lawfully, including the 72-hour report to NCUA, the response program and member notice described in Appendix B, SAR filing, and state breach notices.

## 2. Scope
All workforce members and every member information system, including systems the core processor, the digital banking provider, the corporate credit union, the MSP, and SaaS vendors run for the credit union. A "security incident" includes any attempted or successful unauthorized access to, use, disclosure, change, or destruction of member information or systems; any fraudulent payment instruction, sent or stopped; lost or stolen devices or tokens; and misdirected member information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager (ISO) | Incident lead; keeps the incident log; recommends the reportable-incident and member notice decisions |
| President and CEO | Decides on NCUA reports and member notices with the ISO; calls the insurers; approves outside communications and spending |
| Accounting and Compliance Officer (BSA Officer) | SAR decision and filing; law enforcement contact for fraud; backup incident lead |
| MSP | Technical response: isolate, investigate, rebuild, restore; preserves logs |
| Cyber insurer, fidelity bond carrier, and panel vendors | Breach counsel and forensics through the cyber insurer's hotline; loss notice under the bond |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The credit union must keep an incident response runbook for its most likely serious incident, business email compromise with a fraudulent wire (P08), with a printed copy and contact card in the vault binder and at the ISO's and the President and CEO's homes. (IR-8; RS.MA-01)

4.2 Workforce members must report a suspected fraudulent wire or payment to the ISO **within 15 minutes**, and any other suspected incident **at once, and within 1 hour at most**, in person or by phone. If the ISO cannot be reached, report to the President and CEO, then the Accounting and Compliance Officer. Examples: a member says they did not ask for a wire; an email with changed payment instructions; a link or attachment that asked for a password; a lost phone, laptop, or wire token; member information sent to the wrong person. (IR-6; RS.MA-02)

4.3 The ISO must log every incident, including those that turn out to be harmless, with the time found, what happened, what was done, and the outcome. (IR-5; 748.0(b)(4))

4.4 **NCUA 72-hour report.** As soon as the facts allow, the ISO and the President and CEO must decide whether the credit union reasonably believes it has experienced a reportable cyber incident as defined in 748.1(c)(1), and record the decision with the date and time. If yes, NCUA's designated point of contact must receive notice as soon as possible and no later than 72 hours after that belief is formed. If a vendor or other third party tells the credit union of an incident at a credit union service organization, cloud service provider, or other third-party data host, or a supply chain compromise, the 72 hours run from that notice. The decision is recorded either way. (IR-6; RS.CO-02; 748.1(c))

4.5 **Sensitive member information.** When the credit union becomes aware of unauthorized access to or use of sensitive member information (a member's name, address, or phone with a Social Security number, driver's license number, account number, card number, or a password or PIN that permits account access; or any combination that would let someone log in to the account), the President and CEO must notify the NCUA Regional Director as soon as possible, and the ISO must lead a reasonable investigation into whether misuse has occurred or is reasonably possible. (IR-4; RS.AN-03; App. B II.A.1.b, III.A)

4.6 **Member notice.** If misuse has occurred or is reasonably possible, affected members must be notified as soon as possible with the content in Appendix B III.B, unless law enforcement asks in writing for a delay. Florida and other state notices follow the P08 notification matrix. Counsel reviews each notice before it is sent. (IR-6; RS.CO-03; App. B II.A.1.e, III; Fla. Stat. 501.171)

4.7 **SAR and law enforcement.** The BSA Officer decides whether a SAR is required under 748.1(d) and files it within 30 calendar days of initial detection (up to 60 if no suspect is identified). For a violation that needs immediate attention, such as an ongoing fraud, the BSA Officer notifies law enforcement and NCUA by telephone at once. SARs and the fact of filing are confidential. (IR-6; 748.1(d); App. B II.A.1.c)

4.8 For any suspected fraudulent wire, account takeover, data theft, or ransomware, the President and CEO must notify the cyber insurer's breach hotline and the fidelity bond carrier as their terms require, before hiring any outside firm. The MSP is engaged under its contract. (IR-4; RS.MA-02)

4.9 No ransom or extortion payment may be made without board approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.10 **Vendor incidents.** Vendors must report incidents to the ISO as their contracts require. When an incident involves a vendor's systems, the credit union is still responsible for notifying NCUA and members, unless it has contracted the vendor to send notices for it. (IR-6; SA-9; GV.SC-08; App. B II.A.2)

4.11 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. (IR-3; ID.IM-02)

4.12 Lessons learned must be written up within 30 days of closing any incident that required notice or outside help, fed into the risk register and training, and summarized in the annual board report. (IR-4; ID.IM-02; App. A III.F)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.10. No exception may delay a legally required notice or report.

## 7. Related documents
P08 incident response runbook and notification matrix; POL-02 (B.10 wire security procedure); POL-04; BSA program; Identity Theft Prevention Program; 12 CFR 748.1(c) and (d); 12 CFR Part 748 Appendix B; Fla. Stat. 501.171

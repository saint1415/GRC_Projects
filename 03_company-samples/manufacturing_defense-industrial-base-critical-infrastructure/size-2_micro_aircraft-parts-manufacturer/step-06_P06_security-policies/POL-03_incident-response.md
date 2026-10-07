# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | President |
| Approved by | President, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after every incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-4, IR-5, IR-6, IR-8, IR-3, AU-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, ID.IM-02 |
| SP 800-171 Rev. 2 | 3.6.1, 3.6.2, 3.6.3 |
| Contract basis | DFARS 252.204-7012(c) to (g) and (m)(2)(ii) |

## 1. Purpose
Make sure the company can detect, contain, recover from, and report a cyber incident, and meet its DoD reporting duties even though it has no IT staff.

## 2. Scope
Every system in the SSP boundary, every system that holds CUI even by mistake (for example, the commercial suite), printed CUI, and incidents at the MSP, the cloud provider, or a customer that affect company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| President | Decision maker: declares incidents, approves DoD reports, export control decisions, and any spending; files the DIBNet report |
| Office Manager | Incident coordinator: keeps the incident log and evidence custody; backup DIBNet filer |
| MSP | Technical response: isolates devices, revokes sessions, collects logs; does not reimage before evidence is taken |
| Cyber insurer and panel vendors | Breach counsel and forensics, engaged through the insurer's hotline |
| All workforce | Report at once (4.2) |

## 4. Policy statements
4.1 **What counts.** A cyber incident is any action that compromises, or may have compromised, a company system or the information in it, including possible copying of CUI to unauthorized media or disclosure to unauthorized people (DFARS 252.204-7012(a)). Suspected is enough to start the process.

4.2 **Report at once.** Anyone who sees a suspected incident, a lost laptop, phone, USB drive, or drawing, an unescorted visitor near drawings, or a strange sign-in prompt must tell the Office Manager or the President immediately, by phone if email may be affected. (IR-6; 3.6.2)

4.3 **Plan and contacts.** The company keeps the P08 runbook, a printed contact list (MSP 24x7 line, insurer hotline, counsel, Prime A and Supplier B security contacts), and the DIBNet field list in a binder in the office and at the President's home. (IR-8; 3.6.1)

4.4 **DoD report within 72 hours.** For any cyber incident that affects a covered system or CUI, the President (or the Office Manager as backup) reports to DoD through DIBNet within 72 hours of discovery, using a DoD-approved medium assurance certificate, with whatever is known, and updates the report later. The company keeps two certificates current. (252.204-7012(c)(1)(ii), (c)(3))

4.5 **Prime notice.** After the DIBNet report, the President gives the DoD-assigned incident report number to Prime A or Supplier B, whichever owns the affected CUI, as soon as practicable. (252.204-7012(m)(2)(ii))

4.6 **Review and preserve.** The company reviews for evidence of compromise of CUI (computers, accounts, files) and preserves images of affected systems and relevant logs for at least 90 days from the DIBNet report. Nobody may wipe, reimage, or rebuild an affected device until its image is taken. Audit logs are kept at least 1 year. (252.204-7012(c)(1)(i), (e); IR-4; AU-11)

4.7 **Malware.** Malware found in connection with a reported incident is quarantined, not deleted, and submitted to the DoD Cyber Crime Center (DC3) as DC3 or the Contracting Officer instructs, never to the Contracting Officer. DoD requests for information, equipment, or damage assessment data are answered through the President. (252.204-7012(d), (f), (g))

4.8 **Extortion.** No payment to an extortionist may be made without the President, counsel, the insurer, and an OFAC sanctions check. Paying never changes a reporting duty.

4.9 **Export control.** If CUI that is ITAR or EAR controlled may have reached a foreign person, the President, as Empowered Official, decides with export counsel whether to file a voluntary disclosure (22 CFR 127.12; 15 CFR 764.5) and records the reasoning either way.

4.10 **Personal information.** If employee personal information is involved, counsel decides on notice under Florida law (Fla. Stat. 501.171) and the law of any other state where affected people live.

4.11 **Lessons learned.** Within 14 days after an incident closes, the President and Office Manager hold a review with the MSP; a written summary follows within 30 days, and the risk register, POA&M, SSP, and runbook are updated. (IR-4; ID.IM-02)

4.12 **Testing.** The runbook is tested at least once a year with the MSP by a tabletop exercise that includes a DIBNet login check. The first test is due 2026-11-30. (IR-3; 3.6.3)

4.13 **Records.** The incident log, evidence custody forms, reports, and decisions are kept for at least 6 years (POL-02 A.8). (IR-5)

## 5. Compliance and enforcement
The Office Manager checks yearly that the certificates are current, the contact list is right, and the tabletop happened. Failure to report under 4.2 is handled under POL-02 A.9; good-faith reports are never sanctioned.

## 6. Exceptions
None. The 72-hour reporting duty cannot be waived.

## 7. Related documents
P08 runbook and notification matrix, POL-02, POL-04, the SSP (P02), the MSP contract and responsibility matrix, the cyber insurance policy.

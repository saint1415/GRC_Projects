# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office Manager (Security Coordinator) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that needed outside help or notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-04, RS.MI-01, RS.AN-07, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02, ID.IM-04 |
| Benchmark and law (N21-BM) | SP 800-82 Rev. 3 sections 3.3.8 (incident response capability), 6.4 (Respond), 6.5 (Recover); Fla. Stat. 501.171(4), (6); 40 CFR 110.6 |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents quickly, safely, and lawfully, including incidents that reach the SCADA system and the field.

## 2. Scope
All workforce members, both offices, the tank battery, the SWD facility, every well site, and every system and copy of company information, including systems the MSP and vendors run for the company. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, interference with a system or field equipment, a lost or stolen device, and misdirected owner or employee data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Incident lead; keeps the incident log; calls the MSP; runs breach notice steps with counsel |
| Owner | Backup incident lead; calls the cyber insurer; approves outside communications, spending, and any ransom decision |
| Field Superintendent | OT lead; decides isolation of the SCADA host, manual operations, and shut-ins under the emergency response plan |
| Field Technician | Isolates and checks the SCADA host and controllers; works with the integrator |
| MSP | Technical response on office systems: isolate, investigate, rebuild, restore; preserves logs |
| SCADA integrator | Technical response on the SCADA host and controller programs |
| Cyber insurer and its panel vendors | Breach counsel and forensics, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely serious incident, ransomware spreading from business IT toward SCADA (P08), linked to the manual-operations and shut-in steps in the emergency response plan. A printed copy, the contact card, and the isolation decision table must be kept at both offices and in each field truck. (IR-8; RS.MA-01; ID.IM-04)

4.2 Workforce members must report any suspected incident to the Office Manager **at once, and within 1 hour at most**, by phone; field staff may report to the Field Superintendent, who passes it on. Examples: clicking a suspicious link, locked or renamed files, a ransom note, a lost phone, owner data sent to the wrong person, a caller asking to change bank details, or HMI behavior nobody can explain (setpoints changing, wells starting or stopping without a command). Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)

4.3 The Office Manager must log every incident, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5; RS.AN-06)

4.4 **Authority to isolate.** The Field Superintendent may disconnect the SCADA host from the field office network and the internet at any time to contain an incident. If the Field Superintendent cannot be reached within 15 minutes and ransomware is spreading, the Field Technician or the on-call Lease Operator may do so. Field controllers keep running on their own logic; shut-in decisions stay with the Field Superintendent under the emergency response plan. **No one may disable, bypass, or reset a hardwired safety shutdown as part of incident response.** (IR-4; RS.MI-01)

4.5 Evidence must be preserved before systems are rebuilt, where this does not delay a safety action: logs, disk images, HMI screen photos, and copies of controller programs. (IR-4; RS.AN-07)

4.6 For any suspected ransomware, data theft, or account takeover, the Owner must call the cyber insurer's breach hotline before hiring any outside firm. The MSP and the SCADA integrator must be engaged under their agreements. (IR-4; RS.MA-04)

4.7 Notifications to individuals, other states' regulators, the National Response Center, law enforcement, the insurer, partners, and the purchaser must meet the deadlines in the P08 notification matrix. Counsel must review each legal notice before it is sent. Any documented no-harm determination under Fla. Stat. 501.171(4)(c) must be made with counsel, kept for 5 years, and sent to the Department of Legal Affairs within 30 days. (IR-6; RS.CO-02; RS.CO-03)

4.8 No ransom may be paid without the Owner's approval, advice from counsel and the insurer, and an OFAC sanctions check. A decryptor must never be run on the SCADA host; it is rebuilt from a clean image. (IR-4)

4.9 Vendors that hold company data (production accounting, payroll, the MSP) must report breaches to the Office Manager as their contracts and Fla. Stat. 501.171(6) require. The Office Manager logs each report and handles it under this policy. (IR-6; SA-9)

4.10 The runbook must be tested every year with a tabletop exercise that includes the MSP, the SCADA integrator, and the field staff, and after any real incident that used it. (IR-3; ID.IM-02)

4.11 Lessons learned must be written up within 30 days of closing any incident that needed outside help or notification, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a legally required notification or a safety action.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; emergency response plan; POL-02; POL-04; Fla. Stat. 501.171; 40 CFR 110.6

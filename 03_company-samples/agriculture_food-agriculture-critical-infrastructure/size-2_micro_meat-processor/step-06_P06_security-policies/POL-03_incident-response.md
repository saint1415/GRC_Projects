# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that affected product or required notification |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, SI-7 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.MI-01, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| FSIS rules supported | 9 CFR 417.3(b); 417.5(c); 418.2; 416.15 |

## 1. Purpose
Make sure the company spots, contains, and recovers from security incidents quickly, keeps unsafe or misbranded product out of commerce, and meets every notification deadline.

## 2. Scope
Everyone working for the company, and every system, machine, and copy of company information, including systems run by the MSP, SaaS vendors, and equipment vendors. A "security incident" includes any attempted or successful unauthorized access, change, or destruction of information or of machine settings, ransomware or other malware, loss of monitoring or records caused by a cyber event, lost or stolen devices, and suspicious vendor or remote activity.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Incident lead; keeps the incident log; calls the MSP; decides with counsel whether personal information was breached |
| Owner and General Manager | Backup incident lead; calls the cyber insurer; approves spending, outside communications, and any decision to stop production |
| Production Supervisor | **Food safety lead:** puts product on hold, decides product acceptability, decides whether FSIS must be notified; backup is the owner |
| Maintenance and Sanitation Technician | Puts machines in a safe state; disconnects vendor connections; works with equipment vendors |
| MSP | Technical response on PCs and the network: isolate, investigate, rebuild, restore; preserves logs |
| Cyber insurer and its panel vendors | Breach counsel and forensics, engaged through the insurer's hotline |
| Everyone | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely serious incident, ransomware that stops the lines and cold-chain monitoring (P08). Printed copies and the contact card must be kept in the production office, the office, and at the owner's home. (IR-8; RS.MA-01)

4.2 Anyone who suspects an incident must tell the Office Manager **at once, and within 1 hour at most**, in person or by phone. If the Office Manager cannot be reached, tell the owner. For anything that may affect product (a strange cook cycle, a label that looks wrong, a machine screen behaving oddly, temperature monitoring gone quiet), also tell the Production Supervisor at once. (IR-6; RS.MA-02)

4.3 The Office Manager must log every incident, including those that turn out to be harmless: when it was found, what happened, what was done, and the outcome. (IR-5)

4.4 **Product first.** When an incident may have affected a cook cycle, formulation, chilling, cold storage, label, or the records that prove them, the Production Supervisor must put the affected product on hold, review its acceptability, and decide its disposition as for an unforeseen deviation (9 CFR 417.3(b)). Product may not ship until its records are complete and reviewed (417.5(c)). (IR-4; RS.MI-01)

4.5 **FSIS notice.** If the Production Supervisor or owner learns or determines that adulterated or misbranded product has entered commerce, the local FSIS District Office must be notified within 24 hours, with the type, amount, origin, and destination of the product, and the recall procedure followed (9 CFR 418.2, 418.3). (IR-6; RS.CO-02)

4.6 **Unexplained changes are possible tampering.** Any cook cycle, formulation, or label template that does not match the approved version, and that nobody can explain, must be treated as possible deliberate tampering: the step is stopped, the approved version is restored, and the incident is escalated under this policy. (SI-7; IR-4)

4.7 For ransomware, data theft, account takeover, or any incident needing outside help, the owner must call the cyber insurer's breach hotline before hiring any outside firm. (IR-4; RS.MA-02)

4.8 No ransom may be paid without the owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. Paying never makes held product safe. (IR-4)

4.9 Personal information notices (Fla. Stat. 501.171) and other notices must meet the deadlines in the P08 notification matrix. Breach counsel reviews each notice before it is sent. (IR-6; RS.CO-03)

4.10 Vendors (MSP, SaaS, equipment vendors) must report incidents that affect company systems or data as their contracts require; the Office Manager logs each report and handles it under this policy. (IR-6; SA-9)

4.11 **Restart only after checks.** After an incident, each line restarts only when its machine settings have been compared with the approved copies, the Production Supervisor has signed a restart check, and monitoring and records are working or the paper fallback is in place. (IR-4; RC.RP-01)

4.12 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. Lessons learned must be written up within 30 days and fed into the risk register, training, and, where needed, a HACCP reassessment. (IR-3; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a product hold or a required notification.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; HACCP plans and recall procedure; Fla. Stat. 501.171

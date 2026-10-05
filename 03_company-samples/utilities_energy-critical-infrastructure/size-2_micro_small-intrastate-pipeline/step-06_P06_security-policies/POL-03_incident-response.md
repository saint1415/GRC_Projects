# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office Manager (security program coordinator), with the Operations Manager for operations |
| Approved by | Owner, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-15), and after any incident that needed outside help or a notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | ID.IM-02, ID.IM-04, RS.MA-01, RS.MA-02, RS.MI-01, RS.CO-02, GV.SC-08 |
| Pipeline safety link | 49 CFR 192.615 (emergency plans); 192.605(c) (abnormal operation); 191.5 (immediate notice); Rule 25-12.084, F.A.C. |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from cybersecurity incidents while keeping the pipeline safe, and meets every notice deadline.

## 2. Scope
All employees, contractors, and vendors, and every company system: the hosted SCADA tenant, the gas control desk, controller laptops, field devices and gateways, office IT, and business SaaS, including systems the SCADA vendor and the MSP run for the company. A cybersecurity incident includes any suspected unauthorized access to or change of a system, ransomware or other malware, SCADA data that cannot be trusted, an unexplained SCADA command, a lost or stolen device, and information sent to the wrong person.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Cyber incident lead: opens the incident, keeps the log, coordinates the MSP, the insurer, and counsel |
| Operations Manager | Operations lead: pipeline safety, isolation of the gas control desk, manual operation, pipeline notices; backup cyber lead |
| On-call controller | Acts under the emergency plan first; may isolate and move to manual operation at any time (4.4) |
| Owner | Decision maker: precautionary shut-in, spending, ransom, outside statements |
| MSP | Office IT response: isolate, investigate, rebuild, restore |
| Hosted SCADA vendor | Tenant investigation, audit log export, platform containment |
| Cyber insurer and its panel | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All staff | Report suspected incidents at once |

## 4. Policy statements
4.1 **Runbook.** The company must keep the P08 runbook with its operate-or-shut-in decision table, contacts, and notification matrix. Printed copies must be kept at the office, in each field truck, and at the Owner's and Operations Manager's homes. (IR-8; RS.MA-01)

4.2 **Reporting.** Anyone who notices anything unusual on the gas control desk, a controller laptop, SCADA, or a field device must tell the Operations Manager or the on-call controller **at once, and within 15 minutes at most**. Anything else (a suspicious email, a locked file, a lost phone) must be reported to the Office Manager at once, and within 1 hour at most. (IR-6; RS.MA-02)

4.3 **Safety first.** The controller on duty follows the emergency plan (192.615) and the abnormal operation procedures (192.605(c)) before any cyber step. No cyber response step may delay a safety action. (IR-4; CP-2; RS.MA-01)

4.4 **Isolation authority.** The Operations Manager or the on-call controller may, at any time and without approval: disconnect the gas control desk from the office network, switch to the clean spare laptop, disable a SCADA account, or move to manual operation. They tell the Office Manager and the Owner right after. (IR-4; RS.MI-01)

4.5 **Precautionary shut-in.** Only the Owner (backup: the Operations Manager) may order a precautionary shut-in or curtailment for cyber reasons, using the P08 decision table and after warning the municipal gas system. This does not limit immediate safety actions under 192.615(a)(6), which any controller takes when needed. (IR-4; RS.MI-01)

4.6 **Incident log.** The Office Manager must log every incident, including those that turn out harmless, with the time found, what happened, what was done, who was told, and the outcome. (IR-5)

4.7 **Notices.** The Operations Manager decides on and makes the NRC telephonic notice (no later than one hour after confirmed discovery of an incident under 191.3 and 191.5) and the FPSC notice. The Office Manager, with breach counsel, handles employee breach notices under Fla. Stat. 501.171. All deadlines are in the P08 notification matrix. (IR-6; RS.CO-02)

4.8 **Outside help.** For suspected ransomware, data theft, or unauthorized SCADA activity, the Owner must call the cyber insurer's hotline before hiring any outside firm. The MSP and the SCADA vendor are engaged under their contracts. (IR-4; RS.MA-02)

4.9 **Ransom.** No ransom may be paid without the Owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.10 **Vendor incidents.** The SCADA vendor, the MSP, and the carrier must report security incidents that affect the company within their contract times. The Office Manager logs each report and handles it under this policy. (IR-6; SA-9; GV.SC-08)

4.11 **Exercises.** The runbook must be tested every year with a tabletop that includes the MSP and the SCADA vendor and, where possible, the municipal gas system, and after any real incident that used it. (IR-3; ID.IM-02)

4.12 **Lessons learned.** Lessons learned must be written within 30 days of closing any incident that needed outside help or a notice, and fed into the risk register, the emergency plan, and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.10. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a safety action or a legally required notice.

## 7. Related documents
P08 incident response runbook and notification matrix; emergency plan and its cyber annex; O&M manual (abnormal operation); POL-02; POL-04

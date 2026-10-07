# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Property Manager (security and privacy lead) |
| Approved by | Managing Member, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required notification or outside help |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Benchmark and obligations | CISA CPG 2.0 goals 1.C, 4.B, 5.A, 5.B, 6.A (voluntary); PCI DSS v4.0.1 12.10.1; Fla. Stat. 501.171(3) to (6) |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents quickly and lawfully, keeps the buildings safe and usable while it does, and meets every notice deadline.

## 2. Scope
All employees and contractors, both properties, and every company system: the building systems (BAS, access control, video, networks), the business SaaS, devices, paper records, and the card terminal. A "security incident" includes any attempted or successful unauthorized access to, change to, or disruption of a system; unexpected changes to HVAC setpoints, schedules, or door states; lost or stolen devices or fobs; suspected terminal tampering; and personal information sent or shown to the wrong person.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Property Manager | Incident lead; keeps the incident log; decides with counsel whether personal information was breached; sends tenant notices |
| Managing Member | Backup incident lead; calls the cyber insurer; approves outside communications, spending, building closures, and any ransom decision |
| Building Engineer | Building safety during the incident: manual HVAC operation, door checks, contact with the controls contractor |
| MSP | Technical response for office computers, the Property A network, and backups; preserves logs |
| Controls contractor | BAS investigation and rebuild, under the Building Engineer's direction |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most likely serious incident, ransomware on the building automation system (P08), with a printed copy, contact card, and tenant contact list in the management office binder and at the Property Manager's and Managing Member's homes. (IR-8; RS.MA-01; CPG 1.C)

4.2 Staff must report any suspected incident to the Property Manager **at once, and within 1 hour at most**, in person or by phone. If the Property Manager cannot be reached, report to the Managing Member. Examples: a strange pop-up or locked files, a ransom note, HVAC or door settings changing on their own, a contractor session nobody scheduled, a lost phone, tablet, laptop, or master fob, an email asking to change bank details, or a damaged or unfamiliar card terminal. (IR-6; RS.MA-02; CPG 4.B)

4.3 The Property Manager must log every incident, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5)

4.4 **Safety first.** In any incident affecting building systems, the Building Engineer must first confirm that entrances, egress, and cooling are safe, and switch to manual operation under the contingency procedures if the BAS or the access control platform cannot be trusted. Life-safety systems must never be switched off as a containment step. (IR-4; CP-2; RC.RP-01; CPG 6.A)

4.5 For any incident that may involve personal information, the Property Manager must record the date the company determined a breach occurred or had reason to believe one occurred (the start of Florida's 30-day clock), and decide with breach counsel whether notice is required. Any decision that notice is not required must follow Fla. Stat. 501.171(4)(c), be documented in writing, and be kept for at least 5 years. (IR-6; RS.AN-03)

4.6 Notices to individuals, the Florida Department of Legal Affairs, consumer reporting agencies, tenants under their leases, and the acquirer must meet the deadlines in the P08 notification matrix. Breach counsel reviews each notice before it is sent. (IR-6; RS.CO-02; RS.CO-03; CPG 5.A, 5.B)

4.7 For any suspected ransomware, data theft, or account takeover, the Managing Member must call the cyber insurer's breach hotline before hiring any outside firm. The MSP and the controls contractor are engaged under their contracts. (IR-4; RS.MA-02)

4.8 No ransom may be paid without the Managing Member's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.9 The company should report ransomware and other significant cyber incidents voluntarily to CISA or the FBI, as breach counsel advises, and before any ransom decision. (IR-6; CPG 5.B)

4.10 Vendors and contractors must report incidents affecting company systems or data to the Property Manager as their agreements require (24 hours under the security addendum; 10 days at the latest for a third-party agent under Fla. Stat. 501.171(6)(a)). The Property Manager logs each report and handles it under this policy. (IR-6; SA-9)

4.11 For a suspected card data compromise or terminal tampering, the Bookkeeper must stop using the terminal, keep it as it is, and notify the payment processor and acquirer as the merchant agreement and the P2PE Instruction Manual require. (IR-4; PCI DSS 12.10.1)

4.12 The runbook must be tested every year with a tabletop exercise that includes the MSP and the controls contractor, and after any real incident that used it. (IR-3; ID.IM-02; CPG 1.C)

4.13 Lessons learned must be written up within 30 days of closing any incident that required notification or outside help, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.10. No exception may delay a legally required notice or a safety step.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; P05 BIA recovery order; POL-02; POL-04; contingency plan (due 2026-12-31); Fla. Stat. 501.171

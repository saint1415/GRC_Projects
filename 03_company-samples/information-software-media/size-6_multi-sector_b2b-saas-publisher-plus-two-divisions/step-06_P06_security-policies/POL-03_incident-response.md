# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO; notifications owned by the Group General Counsel |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after every Severity 1 incident |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, CP-4, AU-6 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-04 |
| Regulatory anchors | 16 CFR 314.4(h), (j) (N52-R03); 45 CFR 164.410 (N54-R06); 12 CFR 53.4, 225.303, 304.24; Form 8-K Item 1.05 (N51-R08); state breach laws (Florida worked example, Fla. Stat. 501.171); FAR 52.204-25; PCI DSS 12.10; customer DPAs and sponsor bank agreements |
| Division supplements | Cloud Software: DPA clocks and bank customer contacts. Technology Consulting: hospital BAA clocks and federal contracting officer contacts. Payments and Payroll: FTC notice, sponsor bank notice, and card network procedures |

## 1. Purpose
Detect, contain, and recover from security incidents quickly, and meet every notice duty on time, including when one incident touches several divisions.

## 2. Scope
All security events and incidents affecting group systems or data, including data held for a division by another division, a sub-processor, or a vendor.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Incident commander for Severity 1 and 2 incidents |
| Group CISO | Executive lead; escalates to the disclosure committee |
| Group General Counsel | Owns the notification matrix and approves every external notice |
| Division incident liaisons | Bring division facts, contacts, and contract clocks to the bridge |
| Payments and Payroll Qualified Individual | Decides FTC Safeguards notification events for the division |
| Disclosure committee | Materiality determination for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 The group must maintain one written incident response plan and one notification matrix covering all divisions. Each division supplement adds its own contacts and contract clocks to that matrix; divisions must not keep separate matrices. (IR-8; RS.MA-01; 16 CFR 314.4(h))

4.2 **One severity scale** applies across the group. Severity 1: confirmed exfiltration or destruction of Restricted data (POL-04), an incident in a shared service, or an incident touching more than one division. Severity 2: confirmed compromise of one division's system without Restricted data. Severity 3: contained events. (IR-4)

4.3 Workforce members must report suspected incidents immediately to the SOC. Divisions must report any event that may involve another division's data to the SOC within 1 hour. (IR-6; RS.MA-02)

4.4 **Discovery date.** For each notice duty, the discovery date is recorded as the earliest date any group workforce member knew or should have known, unless counsel documents a later date. Clocks are never planned from a later date. (IR-6; 16 CFR 314.4(j)(2); 45 CFR 164.410(a)(2))

4.5 **Notices.** Every notice in the matrix must be sent by its deadline, including: customer notices under DPAs (72 hours, or 48 hours where negotiated); bank service provider notices to bank-designated contacts when covered services are disrupted for 4 or more hours; sponsor bank notices within 24 hours; the FTC notice within 30 days for notification events involving 500 or more consumers; hospital client notices under BAAs; third-party agent notices under state law (Florida: within 10 days); and individual and regulator notices under state law. (IR-6; RS.CO-02)

4.6 The Group CISO must brief the disclosure committee within 24 hours of declaring a Severity 1 incident. The committee must decide materiality without unreasonable delay; if material, the Form 8-K Item 1.05 filing is due within 4 business days of that determination. (IR-6; RS.CO-03)

4.7 **Ransom.** Any ransom payment requires board risk committee approval, counsel and insurer review, and an OFAC sanctions check. Paying never removes a notice duty. (IR-4)

4.8 The plan must be tested at least annually with a cross-division tabletop that exercises the full notification matrix, and technical playbooks must be tested each quarter. (IR-3; ID.IM-04)

4.9 Leaked credentials found anywhere (including personal repositories and public paste sites) must be revoked within 1 hour of discovery, before any investigation of their use. (IR-4; IA-5)

4.10 Lessons learned must be held within 14 days of recovery and documented within 30 days; resulting actions go to the risk registers and POA&M. (IR-4; ID.IM-04)

## 5. Compliance and enforcement
Compliance is checked through exercises, after-action reviews, and the P07 assessment of IR controls.

## 6. Exceptions
None. Notice deadlines cannot be waived by exception.

## 7. Related documents
P08 incident response runbook and notification matrix; POL-01; POL-04; division supplements; P05 BIA (recovery order).

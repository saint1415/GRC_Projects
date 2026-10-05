# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Electric Cooperative, Inc. |
| Policy ID | POL-03 |
| Owner | Office and Finance Manager (Security Coordinator); Line Superintendent for operational response |
| Approved by | General Manager, 2026-08-31; adopted by the Board of Trustees, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Yearly (next review 2027-08-31), and after any incident reported to DOE or to members |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02 |
| Drivers | Form DOE-417 (Pub. L. 93-275 sec. 13(b)); 7 CFR 1730.28(c)(1), (c)(2), (c)(6), (f); Fla. Stat. 501.171(3)-(6) |

## 1. Purpose
Make sure the cooperative keeps people safe, regains control of its grid, reports on time, and recovers from security incidents, including attacks on SCADA and field devices.

## 2. Scope
All staff and every system and copy of cooperative information, including systems vendors and the MSP run for the cooperative. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information; any unexplained or unauthorized operation or setting change of a field device; interference with SCADA, AMI, or the business suite; lost or stolen devices or keys; and suspicious contact asking for passwords, settings, or payment changes.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Line Superintendent | Operational incident commander: safety of crews and the public, switching, local control, coordination with the G&T control center; DOE-417 filer |
| General Manager | Decision maker: outside notices, spending, insurer, law enforcement, any payment; backup incident commander |
| Office and Finance Manager (Security Coordinator) | Incident log, evidence, vendor and MSP coordination, member and Florida breach notices |
| MSP | Office computers and the backup vault: isolate, investigate, rebuild, restore |
| Hosted SCADA vendor and AMI vendor | Service logs, account lockouts, and restoration of their services |
| Cyber insurer and its panel | Breach counsel and forensic firms (including an OT-capable firm), engaged through the insurer's hotline |
| All staff | Report suspected incidents at once |

## 4. Policy statements
4.1 The cooperative must keep an incident response runbook for its most serious likely incident, an intrusion into SCADA and field devices (P08). The runbook is the cyber annex to the ERP (7 CFR 1730.28(c)(6)). Printed copies with the contact sheet must be kept in the ERP binder, in every truck, and at the homes of the General Manager and Line Superintendent. (IR-8; RS.MA-01)

4.2 Staff must report any suspected incident **at once, and within 15 minutes at most**, by phone to the Line Superintendent for anything touching SCADA, field devices, or AMI, and to the Security Coordinator for everything else. If neither answers, call the General Manager. Examples: a recloser or regulator operating with no fault or no one switching, a SCADA alarm or setting change no one made, a strange sign-in alert, clicking a suspicious link, a request to change bank details, a lost tablet or key. (IR-6; RS.MA-02)

4.3 **Safety first.** If SCADA or a field device may be under someone else's control, the Line Superintendent must move affected devices to local control, block remote operation (disable remote control at the device or ask the SCADA vendor to lock all accounts), and restore service by local switching. Restoring power safely comes before preserving evidence, but staff must photograph device screens and note times before changing settings where safe. (IR-4; RS.MI-01)

4.4 **DOE-417.** For a cyber event that interrupts electrical system operations, or a complete shut-down of the distribution system, the Line Superintendent must make sure Form DOE-417 is filed **within 1 hour** (by phone to the DOE Operations Center if the online form cannot be reached), either by the cooperative or by the G&T or Balancing Authority under the written filing arrangement. A cyber event that could affect reliability but did not interrupt service must be reported within 6 hours. The final report is due within 72 hours. (IR-6; RS.CO-02)

4.5 The Security Coordinator must log every incident, including those that turn out to be harmless, with the date and time found, what happened, what was done, and the outcome. (IR-5; RS.MA-02)

4.6 For any incident that may involve member personal information, the Security Coordinator must work with breach counsel to decide whether a breach of security occurred under Fla. Stat. 501.171 and record the date of that determination. Notices to members, the Florida Department of Legal Affairs, and consumer reporting agencies must meet the deadlines in the P08 notification matrix (no later than 30 days after the determination for individuals). (IR-6; RS.AN-03; RS.CO-03)

4.7 For any suspected attack on SCADA or field devices, ransomware, data theft, or account takeover, the General Manager must call the cyber insurer's hotline before hiring any outside firm, and must tell the G&T control center of any event that affects load at the delivery point. (IR-4; RS.MA-02)

4.8 No ransom or extortion payment may be made without approval by the General Manager and the Board chair, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.9 Vendors and the MSP must report incidents to the cooperative as their contracts require (POL-02 A.5) and as Fla. Stat. 501.171(6) requires. The Security Coordinator must log each report and handle it under this policy. (IR-6; SA-9)

4.10 The runbook must be exercised every year, as part of the ERP exercise (7 CFR 1730.28(f)), with the MSP and the SCADA vendor invited, and after any real incident that used it. (IR-3; ID.IM-02)

4.11 Lessons learned must be written up within 30 days of closing any incident reported to DOE or to members, or that needed outside help, and fed into the risk register, the VRA, and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the yearly assessment (P07) and the yearly exercise.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a safety action or a required report.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; the ERP and its contact list; POL-02; POL-04; Form DOE-417 instructions; Fla. Stat. 501.171

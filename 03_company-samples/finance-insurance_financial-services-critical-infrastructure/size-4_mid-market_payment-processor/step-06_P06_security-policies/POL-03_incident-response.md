# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Director of Information Security |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2025 plan) |
| Review cycle | Annually (next review 2027-09-30), after every tabletop, and after any major incident |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-04 |
| PCI DSS v4.0.1 | 10.4.1, 12.10 (including 12.10.7) |
| FTC Safeguards Rule | 16 CFR 314.4(h), (j) |
| Bank service provider notice | C-FINANCIAL-R01 (12 CFR 53.4; 12 CFR 304.24) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly on every platform, and that every notice owed to card brands, both sponsor banks, the FTC, merchants, ISV partners, and affected individuals goes out on time.

## 2. Scope
All workforce members and all company systems, data, and service providers, including the Integrated Payments gateway and the settlement environment. It covers any event affecting the confidentiality, integrity, or availability of account data, customer information, or the processing, settlement, and funding services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Information Security | Incident commander for security incidents; owns this policy and the runbooks |
| Crisis management team (CMT) | Chaired by the COO; includes the CEO, CFO, CTO, General Counsel, Chief Risk and Compliance Officer, vCISO, and the Director of Corporate Communications. Decides business continuity, external statements, and resources for severity 1 incidents |
| General Counsel | Legal privilege, engagement of outside counsel and forensics through the insurer, final review of every legal notice |
| Chief Risk and Compliance Officer | Owns the notification matrix and the sponsor bank and card brand notices |
| VP Platform Engineering, Director of Integrated Payments Engineering, Director of Settlement and Treasury Operations | Technical containment and recovery leads for their platforms |
| MSSP | 24x7 detection and first response for platforms it monitors |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must keep a written incident response plan, made of this policy and the P08 runbooks, covering the seven elements in 16 CFR 314.4(h) and the PCI DSS 12.10.1 elements: roles, communication and contact strategies including card brand and sponsor bank notice, incident procedures, business recovery and continuity, data backup, legal reporting, coverage of all critical components, and the payment brands' incident procedures. There must be at least one runbook for a card data compromise and one for a disruption of settlement and funding. (IR-8; RS.MA-01; PCI DSS 12.10.1; 16 CFR 314.4(h))

4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, through the security on-call number or the incident channel. Good-faith reports are never sanctioned. The incident response team must be available 24 hours a day, 7 days a week. (IR-6; RS.MA-02; PCI DSS 12.10.3)

4.3 Security alerts from the SIEM, intrusion detection, change- and tamper-detection, and file integrity monitoring on **every** platform must be monitored and answered 24x7. (IR-4; SI-4; DE.AE-02; PCI DSS 10.4.1, 12.10.5)

4.4 **Severity and escalation.** Severity 1 incidents (confirmed or suspected card data compromise, ransomware, or a disruption of covered services expected to reach 4 hours) must be escalated to the COO within 1 hour, and the COO must convene the CMT. Outside counsel directs forensic work so that analysis can be privileged. (IR-4; RS.MA-01)

4.5 Every incident must be logged, categorized, and tracked to closure, with the times of discovery, reasonable suspicion, and determination recorded, because notice clocks start from them. (IR-5; RS.MA-02)

4.6 **Suspected account data compromise.** The team must preserve evidence (no wiping, rebooting, or logging in to compromised systems with administrator credentials), notify the affected sponsor bank immediately and in any case within the 24 hours its agreement allows, make sure the compromise is reported to Visa within three calendar days of reasonable suspicion or confirmation, meet each other card brand's rules through the sponsor banks, and engage a PCI Forensic Investigator when a brand requires one. (IR-4; IR-6; RS.AN-03; RS.CO-02; PCI DSS 12.10.1)

4.7 **Bank service provider notice.** For every incident, the incident commander and the Chief Risk and Compliance Officer must decide, and record, whether it has materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, covered services (clearing, settlement, reconciliation, or merchant funding files) for either sponsor bank for four or more hours. If so, each affected bank's designated point of contact must be notified as soon as possible (12 CFR 53.4 for Bank A; 12 CFR 304.24 for Bank B). If a bank has not provided a contact, notify its CEO and CIO. Designated contacts for both banks must be kept on file and confirmed every quarter. Planned maintenance and recovery tests that could affect covered services must be announced to both banks in advance. (IR-6; RS.CO-02; C-FINANCIAL-R01 (12 CFR 53.4; 12 CFR 304.24))

4.8 **FTC notice.** The General Counsel and the Chief Risk and Compliance Officer must decide whether an event is a notification event under 16 CFR 314.2: acquisition of unencrypted customer information without authorization. If it involves the information of at least 500 consumers, the FTC must be notified through its online form as soon as possible and no later than 30 days after discovery. The company counts affected cardholders toward the 500. (IR-6; RS.CO-02; 16 CFR 314.4(j))

4.9 **Merchant, ISV, and state notices.** When account data or merchant information is affected, the company must notify affected merchants (directly, or through their ISV where the ISV holds the merchant relationship) quickly enough for them to meet their own duties, and in any case within the shortest period state law sets for a third-party agent (10 days under Fla. Stat. 501.171(6)(a)). For data it owns, such as merchant owner data, the company must meet the breach laws of each state where affected individuals reside. Counsel must confirm each notice. (IR-6; RS.CO-03)

4.10 **Card data found where it should not be.** When PAN or sensitive authentication data is found outside a CDE (tickets, chat, call recordings, email, the data warehouse, logs), the finder must report it under 4.2. The team must determine how it got there, securely delete it or move it into the CDE, decide whether it was exposed and handle it as an incident if so, and fix the cause. (IR-4; SI-12; RS.AN-03; PCI DSS 12.10.7)

4.11 No ransom or extortion payment may be made without approval from the CEO after consulting the audit committee chair, the General Counsel, and the cyber insurer, and without an OFAC sanctions check and a report to law enforcement. The default position is not to pay while clean backups exist. (IR-4)

4.12 The plan must be tested at least annually by an executive tabletop and a technical exercise, and after any major incident. At least every two years, one exercise must cover a settlement disruption with both sponsor banks taking part. (IR-3; ID.IM-02; PCI DSS 12.10.2)

4.13 Incident response staff, including Integrated Payments engineers and CMT members, must be trained on their duties at least annually. (IR-2; PR.AT-02; PCI DSS 12.10.4)

4.14 Lessons learned must be documented within 30 days of closing a severity 1 or 2 incident. The plan must be updated, and new risks added to the risk register. (IR-4; ID.IM-04; PCI DSS 12.10.6; 16 CFR 314.4(h)(7))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Compliance is checked through the annual exercises (4.12), the quarterly reviews in POL-01 4.7, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.13. No exception may delay a notice required by law, a card brand, or a sponsor agreement.

## 7. Related documents
P08 `ir-runbook.md` (compromise of the payment processing environment), `ir-runbook-settlement-ransomware.md` (settlement and funding disruption), and `notification-matrix.csv`; POL-01; POL-04; Visa What To Do If Compromised (v10.0); 12 CFR 53.4 and 304.24; 16 CFR 314.4(h), (j); Fla. Stat. 501.171

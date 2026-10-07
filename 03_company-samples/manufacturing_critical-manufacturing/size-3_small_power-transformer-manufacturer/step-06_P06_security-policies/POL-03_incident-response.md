# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | VP Operations, 2026-09-04 |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review by 2027-09-08), and after major changes or incidents |
| Replaces | IT handbook (2021), for the topics covered here |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, DE.AE-08, ID.IM-02, ID.IM-03 |
| Contract and regulatory drivers | Utility addenda secs. 1 and 2 (CIP-013-2 R1.2.1, R1.2.2 flow-down); FAR 52.204-23(c) and 52.204-25(d) reports; Fla. Stat. 501.171 (employee personal information); OFAC ransomware advisory; CIRCIA (proposed, voluntary reporting only) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly and safely, protects the people on the plant floor, and meets every notice duty it owes to customers, the government, and employees.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary workers, and contractors) on the Florida campus and in the field. Covers office IT, plant control systems (OT), the high-voltage test bay, cloud and SaaS services, and systems that service providers operate for the company. It applies to all company information, customer information shared under NDA, and federal contract information (FCI).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for IT and cloud incidents; overall coordinator; engages the MSP |
| Controls Engineer | Incident lead for plant control systems; verifies OT integrity before restart |
| Plant Manager | Decides on safe state, manual operations, or shutdown of plant equipment |
| Contracts and Compliance Manager | Sends notices to utilities, the contracting officer, and regulators on the deadlines in the P08 notification matrix |
| Controller | Engages the cyber insurer, breach coach, and incident response retainer |
| President | Approves any ransom decision and external statements |
| Shift supervisors | Receive reports from the plant floor and call the Controls Engineer |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must keep an incident response plan and runbooks for its most likely incidents, starting with ransomware that disrupts production (P08). Runbooks must cover both IT and OT. (IR-8; RS.MA-01)

4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the IT incident line or their supervisor. Plant-floor examples: an HMI or controller acting on its own, unexpected setpoint or recipe changes, an unknown device or cable. Office examples: phishing clicks, lost devices, ransom notes. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)

4.3 The IT Manager (IT) or the Controls Engineer (OT) must decide within 2 hours of a report whether an event is an incident, using the declaration criteria in P08, and record the decision and the time. That time starts the contract notice clocks. (IR-4; DE.AE-08)

4.4 **Safety first.** When an incident may affect plant control systems, the Plant Manager decides whether to hold equipment in a safe state, run manually, or shut down. No OT equipment may be restarted until the Controls Engineer has verified its programs and settings. (IR-4; RS.MI-01)

4.5 The IT Manager or Controls Engineer may disconnect the IT/OT firewall, the cloud VPN, the MES office interface, or any OEM or MSP remote access path at once, without further approval, to contain an incident. (IR-4; RS.MI-01)

4.6 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category. (IR-5)

4.7 Notices must meet the deadlines in the P08 notification matrix. The Contracts and Compliance Manager sends them after counsel review. They include: each addendum utility within 48 hours after an incident related to the products or services supplied is confirmed; the contracting officer when a FAR 52.204-23 or 52.204-25 report is due; employees and the Florida Department of Legal Affairs under Fla. Stat. 501.171; and the cyber insurer. (IR-6; RS.CO-02; Utility addendum sec. 1)

4.8 The company must coordinate its response with any affected utility, including sharing indicators and planned recovery steps for supplied products. (IR-4; RS.CO-03; Utility addendum sec. 2)

4.9 No ransom may be paid without approval from the President, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)

4.10 Evidence must be preserved before systems are wiped or rebuilt, when it is safe to do so. This includes OT evidence: controller programs, HMI images, and firewall and remote access logs. (IR-4; RS.AN-03)

4.11 The plan must be tested at least annually by a tabletop exercise that includes the Plant Manager, the Controls Engineer, and the MSP, and after any major incident. (IR-3; ID.IM-02)

4.12 Lessons learned must be documented within 30 days of closing an incident and added to the risk register. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 statement 4.12. Consequences range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), access reviews, and the quarterly obligations register review.

## 6. Exceptions
Exceptions follow POL-01 statement 4.11. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months. Exceptions for plant equipment that cannot technically meet a statement (for example, an HMI without individual accounts) must name the compensating controls.

## 7. Related documents
P08 Ransomware Runbook and notification matrix; POL-01; POL-02; utility Supplier Cyber Security Addenda; FAR 52.204-23 and 52.204-25; Fla. Stat. 501.171; cyber insurance policy

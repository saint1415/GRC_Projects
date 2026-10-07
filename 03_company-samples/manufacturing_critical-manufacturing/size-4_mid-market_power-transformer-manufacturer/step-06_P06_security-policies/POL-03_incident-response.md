# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AU-6, CP-10, SR-8, AU-9 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-04, RS.CO-02, RS.CO-03, RS.MI-01, RS.AN-06, RS.AN-07, DE.AE-08, RC.RP-05, ID.IM-02, GV.SC-08 |
| Drivers | Utility addenda secs. 1, 2, and 4; FAR 52.204-23(c), 52.204-25(d), 52.204-30(c); Fla. Stat. 501.171; FMS subscription agreements; CSF 2.0 benchmark |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard; P08 runbooks |

## 1. Purpose
Make sure the company detects, contains, and recovers from cyber incidents in IT, on the plant floor, and in the products and services it supplies, keeps people safe, and meets every notice deadline.

## 2. Scope
All incidents affecting company systems, plant control and test systems, the FMS, software and firmware supplied to utilities, and company data held by suppliers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Crisis management team (chair: COO; CEO, CFO, General Counsel, vCISO, Security Manager, IT Director, Director of Manufacturing Engineering, Director of Digital Services, Director of Marketing and Communications, HR Director) | Business decisions, external statements, ransom recommendation to the CEO |
| Security Manager | Owns this policy; incident commander for cyber incidents |
| OT Security Engineer and Director of Manufacturing Engineering | OT incident leads |
| Plant Managers | Safe-state and shutdown decisions |
| VP Engineering | Product incidents and vulnerability disclosure |
| General Counsel | Notice decisions, decision log, privilege |
| MSSP and insurer panel | Monitoring, forensics, OT-capable response |

## 4. Policy statements
4.1 The company must keep an incident response plan made up of this policy and runbooks for its most likely incidents: ransomware disrupting production, and compromise of products or services supplied to utilities (P08). Runbooks must cover IT, OT, and products. (IR-8; ID.IM-04)

4.2 Workforce members must report any suspected incident immediately, and within 1 hour at most, to the incident line or their supervisor. Plant-floor examples: an HMI or controller acting on its own, unexpected setpoint or recipe changes, an unknown device. Office examples: phishing clicks, lost devices, ransom notes. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)

4.3 The Security Manager (IT and products) or the OT Security Engineer (OT) must decide within 2 hours of a report whether an event is an incident, using the declaration criteria in the P08 runbooks, and record the decision and the time. That time can start contract notice clocks. (IR-4; DE.AE-08)

4.4 **Safety first.** When an incident may affect plant control or test systems, the Plant Manager decides whether to hold equipment in a safe state, run manually, or shut down. No OT equipment may restart until the plant Controls Lead has verified its programs and settings against verified copies. (IR-4; CP-10; RS.MI-01; RC.RP-05)

4.5 The Security Manager, IT Director, or OT Security Engineer may disconnect the IT/OT firewalls, the SD-WAN, the Plant 2 MES office interface, the FMS ingestion interface, or any vendor remote access path at once, without further approval, to contain an incident. (IR-4; RS.MI-01)

4.6 Every incident must be logged, categorized (IT, OT, product, FMS, privacy), and tracked to closure. Major incidents must keep a decision log maintained by the General Counsel. (IR-5; IR-4; RS.AN-06)

4.7 The crisis management team must convene for any severity 1 incident (P08). The CEO informs the audit committee chair and the private equity sponsor. (IR-4; IR-8; RS.MA-04)

4.8 Notices must meet the deadlines in the P08 notification matrix, after counsel review: each affected addendum utility within its contract deadline (24 or 48 hours after an incident related to the products or services supplied is confirmed); the contracting officer when a FAR 52.204-23, 52.204-25, or 52.204-30 report is due; affected individuals and the Florida Department of Legal Affairs under Fla. Stat. 501.171; FMS subscribers under their agreements; and the cyber insurer. (IR-6; SR-8; RS.CO-02)

4.9 The company must coordinate its response with any affected utility, including sharing indicators and recovery steps for supplied products and services. (IR-4; IR-7; RS.CO-03)

4.10 No ransom may be paid without approval from the CEO, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4; RS.MA-04)

4.11 Evidence must be preserved before systems are wiped or rebuilt when it is safe to do so, including OT evidence (controller programs, HMI images, firewall and remote access logs), with chain of custody. (IR-4; AU-9; RS.AN-07)

4.12 The plan must be tested at least annually by a crisis management tabletop and an OT tabletop at each plant, and after any major incident. The 24-hour utility notice must be drilled each quarter. (IR-3; ID.IM-02)

4.13 Lessons learned must be documented within 30 days of closing a major incident and added to the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.13. Compliance is verified through exercises, the incident register, notice timeliness metrics, and the annual control assessment (P07: IR-4, IR-6, IR-8).

## 6. Exceptions
Exceptions follow POL-01 section 4.12. Notice deadlines set by contract or law cannot be excepted.

## 7. Related documents
POL-01; P08 `ir-runbook.md` (ransomware disrupting production), `ir-runbook-product-compromise.md` (compromise of products or services supplied to utilities), and `notification-matrix.csv`; P05 BIA recovery order; STD-02; STD-07; OFAC ransomware advisory (2021-09-21)

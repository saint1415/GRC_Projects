# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after every severity 1 incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, AU-2, AU-6, SI-4, CP-2, CP-4, CP-9, CP-10 |
| CSF 2.0 | RS.MA-01, RS.CO-02, RS.CO-03, DE.AE-02, DE.CM-01, RC.RP-01, ID.IM-02 |
| Regulatory drivers | SDWA section 1433, 42 U.S.C. 300i-2(b)(2)-(4) (C-WATER-R01); 40 CFR 141.202, 141.31, 141.405(a)(1); 42 U.S.C. 300i-1; Fla. Stat. 501.171(3)-(6); CIRCIA (C-WATER-R02, proposed, tracked only) |
| Supporting standards | STD-02 Logging and monitoring; STD-06 Contingency and recovery |

## 1. Purpose
Make sure the company detects, contains, and recovers from security incidents in a way that keeps the water safe first, meets every notice clock, and preserves evidence.

## 2. Scope
All suspected or confirmed security incidents affecting company or client systems, OT, data, or facilities, including incidents at vendors that affect company data or services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Operator or ROC operator on duty | Process safety lead for the first hour of any OT incident |
| Security Manager | Incident commander |
| Director of Water Operations | Decides the operating mode (islanded or manual) for affected plants |
| Water Quality and Compliance Manager | Tier 1 public notice decision with the COO; state reporting |
| General Counsel | Notice decisions, privilege, law enforcement and regulator contact |
| Chief Operating Officer | Chairs the crisis management team |
| MSSP | 24x7 monitoring, triage, and IT containment; escalates OT alerts to the ROC |

## 4. Policy statements
4.1 **Water safety comes first.** Any operator may place any process in local or manual control, or take any other process safety action, at any time without waiting for IT, management, or forensics. (IR-4; CP-2; RS.MA-01; 42 U.S.C. 300i-2(b)(2))
4.2 All workforce members must report suspected incidents, including unexpected HMI changes or remote activity, to the ROC or the Security Manager within 1 hour. The MSSP must escalate high-severity OT alerts to the ROC within 15 minutes. (IR-6; DE.AE-02)
4.3 The incident commander must record the time the company learned of the situation, and the General Counsel must record the date a data breach was determined. These start the Tier 1 notice clock (40 CFR 141.202(b)) and the Florida clock (Fla. Stat. 501.171(3)-(4)). (IR-5; IR-4; RS.CO-02)
4.4 The incident response plan consists of this policy and the P08 runbooks. Runbook 1 (OT remote-access compromise) is the cybersecurity annex of the ERP for each covered system and must be kept consistent with it. (IR-8; CP-2; RS.MA-01; 42 U.S.C. 300i-2(b)(2))
4.5 The General Counsel must keep a decision log for every incident that may require notice: Tier 1 decision, state reports, breach determination, affected individuals by state, law enforcement requests, and client and contract notices. (IR-6; RS.CO-02)
4.6 The Water Quality and Compliance Manager, with the COO, decides whether an incident is a Tier 1 situation. If it is, the notice must be delivered and primacy agency consultation started within 24 hours of learning of it, using offline contact lists if business systems are down. (IR-6; RS.CO-02; 40 CFR 141.202)
4.7 Any evidence of tampering or attempted tampering with a water system must be reported to the FBI as soon as the incident is declared (42 U.S.C. 300i-1). Significant cyber incidents must be reported to CISA within 24 hours of declaration (voluntary, company rule). (IR-6; RS.CO-03)
4.8 **Ransom.** Only the CEO may decide on a ransom payment, after advice from counsel and the insurer, an OFAC sanctions check, and a report to law enforcement. The default position is not to pay while backups and manual operation are available. (IR-4; RS.MA-01)
4.9 Each covered system must hold an OT cyber tabletop exercise at least once a year and a functional exercise at least every 2 years, involving the relevant integrator. The first tabletop is 2026-11-17. (IR-3; CP-4; ID.IM-02; 42 U.S.C. 300i-2(b)(2))
4.10 Contingency and recovery must follow STD-06: recovery objectives from the BIA (P05), offline known-good backups for every OT site, and an annual rebuild test for each covered system's SCADA. (CP-2; CP-4; CP-9; CP-10; RC.RP-01)
4.11 Logging and monitoring must follow STD-02, including logs from every covered system's SCADA, remote access, and firewalls. (AU-2; AU-6; SI-4; DE.CM-01)
4.12 Municipal clients must be notified within 24 hours of any incident affecting their data or their plant monitoring, as their contracts require. (IR-6; RS.CO-02)
4.13 A lessons-learned review must be held within 14 days of recovery and documented within 30 days. The risk register, POA&M, runbooks, RRA addenda, and ERPs must be updated from it. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Checked through exercises, incident reviews, the MSSP escalation report, and the annual assessment (P07).

## 6. Exceptions
None for statements 4.1, 4.3, 4.6, and 4.7. Others under POL-01 statement 4.7.

## 7. Related documents
POL-01; STD-02; STD-06; P08 `ir-runbook.md`, `ir-runbook-ransomware.md`, and `notification-matrix.csv`; ERPs for the Regional, Lakes, and Ridge Systems; BIA (P05)

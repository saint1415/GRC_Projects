# Incident Response and Downtime Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Information Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after every severity 1 incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2, CP-4, CP-8, CP-10, AU-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02, ID.IM-04 |
| HIPAA Security Rule and Breach Notification Rule | 164.308(a)(6), (a)(6)(ii), (a)(7), (a)(7)(ii)(B)-(D); 164.402-164.414 |
| Other rules | 42 CFR 482.15(a)(2), (b)(5), (c)(3), (d)(2); 42 CFR 489.24(b); 21 CFR 803.30; Fla. Stat. 501.171 |
| Supporting standards | STD-02 (logging and monitoring), STD-07 (contingency, recovery, and downtime) |

## 1. Purpose
Make sure the hospital detects, contains, and recovers from security incidents while patients keep receiving safe care, and that every notice to patients, regulators, practices, and partners is made on time.

## 2. Scope
All security and privacy incidents and IT outages affecting hospital systems, medical devices, OT, communications, vendors that hold hospital PHI, and the EHR services provided to affiliated practices.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Information Security Manager | Incident commander for cyber incidents; owns this policy and the P08 runbooks |
| Chief Operating Officer | Chairs the cyber crisis management team |
| Chief Executive Officer | Hospital incident commander when the Hospital Incident Command System is activated; ransom decision |
| CNO, ED Medical Director, administrator on call | Diversion decision |
| Compliance and Privacy Officer | Breach determinations and the decision log |
| IT Director | Recovery lead |
| Director of Emergency Management | Activates the emergency operations plan and the IT outage annex |
| MSSP | 24x7 detection, triage, and endpoint containment |
| All workforce | Report suspected incidents immediately to the service desk or privacy hotline |

## 4. Policy statements
4.1 The hospital must keep an incident response plan with runbooks for at least ransomware with EHR downtime and insider unauthorized access (P08), approved by the COO and reviewed annually. (IR-8; 164.308(a)(6))

4.2 Every workforce member must report a suspected incident immediately. No one may be disciplined for a good-faith report. (IR-6; 164.308(a)(6)(ii))

4.3 **Discovery time.** The incident register must record the date and time an incident was first known, or by reasonable diligence would have been known, to any workforce member or agent, and the date a breach was determined. (IR-5; 164.404(a)(2); Fla. Stat. 501.171)

4.4 Severity 1 incidents (ransomware execution, confirmed PHI exfiltration, extortion, or loss of a High-criticality BIA process) must be declared within 30 minutes of confirmation, and the crisis management team convened within 2 hours. (IR-4; RS.MA-01)

4.5 **Decision log.** For every privacy or security incident involving PHI, the Compliance and Privacy Officer must document the four-factor risk assessment, the decision, and every notice, and keep them for 6 years. (IR-5; RS.AN-03; 164.402; 164.414(b))

4.6 **Integration with emergency preparedness.** A cyber incident that affects patient care activates the Hospital Incident Command System and the IT outage annex of the emergency operations plan. Clinical decisions (downtime, cancellations, diversion) belong to clinical command; technical decisions to the incident commander. (CP-2; 482.15(a)(2))

4.7 **Downtime.** Departments must keep downtime procedures that sustain care for at least 72 hours, with paper forms, downtime workstation printouts, and back-entry rules, and must drill them at least quarterly (STD-07). (CP-2; 164.308(a)(7)(ii)(C); 482.15(b)(5))

4.8 **Diversion.** Ambulance diversion during an IT outage follows the criteria in the IT outage annex, is decided by the CNO, the ED Medical Director, and the administrator on call, and is logged with times. Patients who arrive on hospital property are always screened. (CP-2; 489.24(b))

4.9 **Communications.** The hospital must keep an out-of-band contact tree and alternate means (analog or cellular lines, radios) on every clinical unit that do not depend on the campus network or email. (CP-8; 482.15(c)(3))

4.10 **Ransom.** The hospital does not pay ransom while backups are intact. Any payment decision needs the CEO, counsel, the insurer, a sanctions check under the OFAC advisory, and a report to law enforcement. (IR-4; RS.MA-02)

4.11 **Notices.** Notices to individuals, HHS, the media, state regulators, affiliated practices, partners, and insurers follow the P08 notification matrix and are approved by counsel. (IR-6; RS.CO-02; 164.404-164.410)

4.12 **Medical devices.** If information reasonably suggests a device (including a compromised or malfunctioning networked device or AI software) caused or contributed to a death or serious injury, biomedical engineering and risk management must report it within 10 work days under 21 CFR 803.30. (IR-6; RS.CO-03)

4.13 **Recovery.** Systems are restored in BIA priority order (P05) only after the incident commander confirms they are clean; compromised systems are rebuilt, not decrypted and reused. (CP-10; RC.RP-01; 164.308(a)(7)(ii)(B))

4.14 **Testing.** The plan must be exercised at least yearly with clinical, executive, and legal participants. The ransomware exercise may serve as the 482.15(d)(2)(ii) additional exercise when it uses a clinically relevant scenario. (IR-3; CP-4; 482.15(d)(2))

4.15 Lessons-learned review within 14 days of recovery, with a written report within 30 days and updates to the risk register and POA&M. (IR-4; ID.IM-04; 482.15(d)(2)(iii))

## 5. Compliance and enforcement
Checked by exercises, after-action reports, the P07 assessment, and audit committee reporting. Late reporting or bypassing the decision log is handled under POL-01 4.8.

## 6. Exceptions
None for statements 4.3, 4.5, 4.8, 4.10, and 4.12. Others under POL-01 4.7.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-insider-access.md`, and `notification-matrix.csv`; P05 BIA; emergency operations plan and IT outage annex; STD-02; STD-07

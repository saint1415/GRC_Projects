# Incident Response, Logging, and Contingency Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Operations Manager (incident response and logging), with the VP Platform Engineering (contingency) |
| Approved by | Chief Technology Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 incident response plan as the governing policy) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, IR-9, AU-1, AU-2, AU-6, AU-11, SI-4, CP-1, CP-2, CP-4, CP-9, CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, DE.CM-01, DE.AE-02, RC.RP-01, PR.DS-11 |
| Regulatory drivers | C-IT-R01 (IEC rules; Rev5 Class C IR, AU, CP controls); C-IT-R03 (252.204-7012(c)-(g)); C-IT-R05 (12 CFR 53.4); FAR 52.204-23, -25, -30; Fla. Stat. 501.171(6) |
| Supporting standards | STD-04 Logging and monitoring; STD-07 Contingency and recovery |
| Runbooks | P08 `ir-runbook.md` (provider tooling compromise); P08 `ir-runbook-dc1-site-loss.md`; P08 `notification-matrix.csv` |

## 1. Purpose
Detect, contain, and recover from incidents quickly, and meet every notice clock owed to agencies, FedRAMP, defense customers, banks, other customers, and regulators.

## 2. Scope
All security incidents and service disruptions affecting either partition, the data centers, managed services, backup and DR, DNS and edge, corporate IT, or vendors that hold customer data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Operations Manager | Incident commander for security incidents; federal incident response coordinator for FedRAMP reports |
| Director of NOC and Customer Support | First responder; incident commander for outages; status page and customer notices |
| General Counsel | Legal lead; decides notices with outside counsel; privilege; law enforcement contact |
| Federal Program Director | Agency and defense customer communications |
| Financial Services Account Director | Bank notices to designated contacts |
| Chief Technology Officer | Crisis management lead for major incidents; approves service shutdowns |
| Chief Executive Officer | Crisis management decisions with business impact; ransom payment decisions |
| Director of Communications | Public statements and media |
| MDR partner | 24x7 tier-1 triage; escalation to the SOC on call |

## 4. Policy statements
4.1 **Plan and runbooks.** The company must keep an incident response plan made up of this policy and the P08 runbooks, approved by the CTO and tested each year. (IR-8; RS.MA-01; C-IT-R01)
4.2 **Reporting by staff.** Anyone who suspects an incident must report it to the NOC or the SOC at once. Reports are never punished. (IR-6; RS.MA-01; C-IT-R01)
4.3 **Severity and command.** Every incident must be given a severity and an incident commander within 30 minutes of declaration. Severity 1 incidents activate crisis management with the CTO, General Counsel, and the Director of Communications. (IR-4; RS.MA-02; C-IT-R01)
4.4 **FedRAMP reportability.** For every incident, the federal incident response coordinator must promptly decide whether it affects, or is likely to affect, the confidentiality or integrity of federal customer data. If it does, it is treated as PAIN-5 unless a PAIN rating is estimated, and the Initial Incident Report goes to FedRAMP, the affected agencies, and all necessary parties within 1 hour for PAIN-3 to PAIN-5 (Class C), with ongoing and final reports on the Class C timeframes. (IR-6; IR-4; RS.CO-02; C-IT-R01 (IEC-CSO-EFR, IEC-CSO-DPR, IEC-CSO-IIR))
4.5 **Notice clocks.** Each incident must be checked against the notification matrix (P08) within 1 hour of declaration, and every clock that starts must be logged with its start time. This includes the bank rule (as soon as possible after determining a 4-hour material disruption is likely), DFARS 252.204-7012 (72 hours from discovery), FAR clause reports, the MSA (72 hours from confirmation), and state third-party agent duties (Florida: 10 days). (IR-6; RS.CO-02; C-IT-R05 (12 CFR 53.4(a)); C-IT-R03 (252.204-7012(c)); Fla. Stat. 501.171(6))
4.6 **Evidence preservation.** Images of affected systems and relevant monitoring data must be preserved with chain of custody, and kept at least 90 days after any DFARS report. (IR-4; AU-11; RS.AN-07; C-IT-R03 (252.204-7012(e)))
4.7 **Tooling compromise.** If the RMM tool, the control plane, the pipeline, or a signing key may be compromised, it must be isolated first and validated before it is used again, even if this extends the outage (P08). (IR-4; RS.MI-01; C-IT-R01)
4.8 **Insurance and payments.** The cyber insurer's hotline must be notified before incident vendors are engaged. No ransom may be paid without CEO approval, General Counsel review, and a sanctions check consistent with the OFAC ransomware advisory. (IR-4; RS.MA-01; C-IT-R01)
4.9 **Spillage.** CUI or federal data found in the commercial partition or a managed services server must be handled under the spillage procedure, including the DFARS path when covered defense information is involved. (IR-9; RS.MA-02; C-IT-R01; C-IT-R03)
4.10 **Exercises and training.** Both P08 runbooks must be exercised at least once a year, including their notice steps. Incident response training is required at hire and yearly for SOC, NOC, platform, and managed services staff. (IR-2; IR-3; PR.AT-02; C-IT-R01)
4.11 **Logging.** The event types in STD-04 must be logged from every system in both partitions and the RMM tool, sent to the SIEM, kept at least 1 year online and 3 years in the write-once archive, and reviewed as STD-04 requires. (AU-2; AU-6; AU-11; SI-4; DE.CM-01; C-IT-R01)
4.12 **AI-assisted triage.** AI triage must not close alerts on privileged access, the RMM tool, the pipeline, or signing keys without human review, and a weekly sample of auto-closed alerts must be checked (P10). (AU-6; SI-4; DE.AE-02; C-IT-R01)
4.13 **Contingency plans.** One contingency plan must cover both partitions, all three data centers, and the BIA recovery objectives (P05), including the loss of a data center. (CP-2; RC.RP-01; C-IT-R01; C-IT-R05 (12 CFR 53.4(a)))
4.14 **Recovery testing.** Control plane restores must be tested quarterly in both partitions. Data center failover must be exercised at least yearly. A failed test must be repeated within 90 days. (CP-4; CP-10; PR.DS-11; C-IT-R01)
4.15 **Backups.** Control plane backups must be immutable, held in a separate account and region, and deletable only with two-person approval. (CP-9; CP-6; PR.DS-11; C-IT-R01)

## 5. Compliance and enforcement
P07 tests these statements each year. Exercise results and notice timings are reported to the audit committee.

## 6. Exceptions
Through POL-01 section 4.8. No exception may remove a legal or contractual notice duty.

## 7. Related documents
POL-01; STD-04; STD-07; P08 runbooks and notification matrix; BIA (P05); risk register (P01 R-001, R-005, R-015, R-016, R-018, R-022, R-030, R-034)

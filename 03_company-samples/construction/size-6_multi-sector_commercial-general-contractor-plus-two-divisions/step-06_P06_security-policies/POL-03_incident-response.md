# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO, with the Group General Counsel for notifications |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 (approved 2026-09-15) |
| Review cycle | Annually (next review 2027-09-30), after every Severity 1 incident, and after each cross-division exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory drivers | N23-R03 DFARS 252.204-7012(c)-(g), (m); N23-R02 FAR 52.204-25(d); N23-R04 DFARS 252.204-7021 (status currency); N53-R05 Form 8-K Item 1.05; state breach notification laws (Fla. Stat. 501.171 worked example); N53-R04 PCI DSS Requirement 12.10 (parking) |
| Division supplements | Construction: owner and surety notices; TSSI client notices. Property: tenant notices; parking provider and acquirer. A&E: subcontractor reporting to Construction on design-build; digital twin client notices |

## 1. Purpose
Make sure the group detects, contains, and recovers from incidents consistently across divisions, and that each contracting entity and the public company meets its own reporting duties on time.

## 2. Scope
All security incidents affecting any group system or data, including payment fraud, incidents at subcontractors, subconsultants, and cloud providers that affect group data, and incidents in client systems the TSSI unit manages.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Runs detection and incident handling 24x7; incident commander for Severity 1 and 2 incidents in shared services |
| Group CISO | Declares Severity 1; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; approves every external notice |
| Director of Federal Contracts Compliance | Holds the DoD medium assurance certificate; files DoD cyber incident reports at DIBNet for both contracting entities |
| Group Treasurer | Leads payment recall and payment-fraud response |
| Division incident liaisons | Bring division facts, operational impact, and division customer and regulator contacts |
| Disclosure committee | Decides materiality for Form 8-K Item 1.05 |

## 4. Policy statements
4.1 Every workforce member must report a suspected incident to the group SOC within 1 hour of noticing it. A suspected false payment instruction must be reported at once, and the Group Treasurer called. (IR-6; RS.MA-02)

4.2 The group SOC must handle incidents using one group severity scale and the group playbooks, including the P08 runbook. Division scales are not permitted. (IR-4; IR-8; RS.MA-01)

4.3 The incident log must record the time the incident was discovered and, separately, the time each notice clock started (for example, the determination that personal information was involved under state law, or the materiality determination). (IR-5; RS.AN-03)

4.4 **DoD reporting.** When a cyber incident affects a covered contractor information system or covered defense information (including CUI found outside the enclave), the Director of Federal Contracts Compliance must report it at dibnet.dod.mil within 72 hours of discovery, submit any malicious software to the DoD Cyber Crime Center, and preserve images of affected systems for at least 90 days from the report (DFARS 252.204-7012(c)-(e)). When A&E is the subcontractor on a design-build project, it reports to DoD and gives the DoD incident report number to Construction as the prime as soon as practicable (252.204-7012(m)(2)(ii)). (IR-6; RS.CO-02)

4.5 The Group General Counsel must maintain the multi-regulator notification matrix (P08) and review it every quarter. Every external notice must be approved by counsel before it is sent. (IR-6; IR-8; RS.CO-02)

4.6 **SEC materiality.** Severity 1 incidents, and any payment fraud loss above $5 million, must be escalated to the disclosure committee within 24 hours of declaration. The committee must decide materiality without unreasonable delay. If material, the Form 8-K Item 1.05 filing must be made within 4 business days after the determination. (IR-6; RS.CO-03)

4.7 **Covered equipment.** If covered telecommunications equipment or services are found in use during performance of a federal contract, the Director of Federal Contracts Compliance must report to the Contracting Officer (DoD contracts: dibnet.dod.mil) within 1 business day of identification, with mitigation details within 10 business days (FAR 52.204-25(d)). (IR-6; SR-5)

4.8 **CMMC status after an incident.** If an incident shows that a CMMC requirement is no longer met in an assessed scope, the Director of Federal Contracts Compliance must tell the Affirming Official and counsel, and the requirement must be restored and re-assessed before the status is relied on for a new award or a new affirmation. (CA-2; IR-4)

4.9 **Ransom payments** require board risk committee approval, counsel, the cyber insurer, and an OFAC sanctions check before any payment. (IR-4)

4.10 **Payment fraud.** The Group Treasurer must request a recall of any payment that may have been diverted as soon as it is suspected, and file a complaint with the FBI Internet Crime Complaint Center. Bank-detail changes must be frozen for the affected division until every change in the last 90 days is re-verified. (IR-4; RS.MI-01)

4.11 The group must run at least one cross-division exercise each year that includes the notification matrix, the DoD reporting path, and a materiality decision. (IR-3; ID.IM-02)

4.12 Evidence must be preserved with chain of custody. Logs relevant to an incident must be placed on legal hold. (IR-4; RS.AN-03)

4.13 A lessons-learned review must be completed within 30 days of recovery, and the risk registers, POA&M, and this policy updated. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR-3, IR-4, IR-6, IR-8) and exercise reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may extend a legal or contractual reporting deadline.

## 7. Related documents
P08 runbook and notification matrix; POL-01; `division-supplements.md`; BIA recovery priorities (P05); DFARS 252.204-7012; FAR 52.204-25.

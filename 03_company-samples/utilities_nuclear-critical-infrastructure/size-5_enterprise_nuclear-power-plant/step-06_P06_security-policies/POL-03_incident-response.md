# Incident Response and Resilience Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director, Security Operations |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-10, within the 15 calendar months CIP-003-9 R1 allows), and after major changes, incidents, acquisitions, or a final NRC rule |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10, CA-5 |
| CSF 2.0 | RS.MA-01, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, RC.RP-03, ID.IM-02 |
| Regulatory basis | 10 CFR 73.77; 50.72; 73.1200; CIP-008-6; Form 8-K Item 1.05; state breach laws (Fla. Stat. 501.171 worked example) |

## 1. Purpose
Make sure the company detects, contains, recovers from, and reports cyber incidents quickly and lawfully. A business network incident can start NRC clocks measured in hours (10 CFR 73.77), a NERC CIP report, an SEC filing, and state breach notices at the same time, so this policy fixes who decides each one and how they stay coordinated.

## 2. Scope
All Cris Santos Company workforce members (about 12,000 employees, the supplemental contractors who support refueling outages, and other contractors and vendors with company accounts) at the corporate campus in Florida, the four stations (Florida, Georgia, South Carolina, and Alabama), the Generation Dispatch Center, and the data centers DC-1 and DC-2. Covers all business systems and data, including the two public clouds, SaaS, the plant business networks, Station 4 legacy systems from the 2025-07-01 acquisition date, and the services sold to outside companies (SL-1 monitoring and diagnostics; SL-2 dosimetry processing). **Critical digital assets (CDAs) are governed by each station's NRC-approved cyber security plan (CSP) under 10 CFR 73.54.** This policy supports the CSPs and never overrides them; where a CSP or a NERC CIP requirement is stricter, the stricter rule applies.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director, Security Operations | Incident commander for business IT incidents; runs the SOC |
| CISO | Executive incident lead; briefs the General Counsel and the CEO |
| Station shift manager | Decides NRC notifications for the station (73.77, 50.72, 73.1200), advised by the Site Cyber Security Program Manager |
| Director, Nuclear Cyber Security | Fleet coordination of station cyber teams and the CDA side of any incident |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Compliance Officer | Breach determinations for personal information |
| Director, NERC Compliance | CIP-008 determinations and reports for the Generation Dispatch Center |
| CIO and system owners | Recovery in BIA priority order |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every suspected incident must be reported to the SOC immediately. Anything involving a station business network, portable media, or a device near plant equipment must also be reported to the Site Cyber Security Program Manager. (IR-6; RS.MA-01)

4.2 The station shift manager, advised by the Site Cyber Security Program Manager, decides NRC notifications under 73.77, 50.72, and 73.1200. The SOC must not report to any outside agency without first notifying every affected station. (IR-6; RS.CO-02)

4.3 Vulnerabilities, weaknesses, failures, and deficiencies in the cyber security program must be entered in the station corrective action program within 24 hours of discovery, whoever discovers them. (IR-5; CA-5; ID.IM-02)

4.4 The CISO must brief the General Counsel within 24 hours of declaring any severity-1 incident, and the disclosure committee must convene within 48 hours to begin the materiality assessment under PRC-03.2. If the committee determines that an incident is material, the Form 8-K Item 1.05 must be filed within 4 business days of that determination. (IR-8; RS.CO-03)

4.5 The Chief Compliance Officer makes breach determinations for personal information; notices follow PRC-03.3 and the law of each state where affected individuals reside. (IR-6; RS.CO-03)

4.6 A ransom payment requires approval by the CEO and the General Counsel, the insurer's involvement, and an OFAC sanctions check, and does not remove any notification duty. (IR-4; RS.MI-01)

4.7 The incident response plan must be exercised at least annually, including a disclosure committee exercise; the GDC plan must be tested at least every 15 calendar months. (IR-3; IR-8; RS.MA-01)

4.8 Tier-1 business systems must have contingency and disaster recovery plans tested at least annually against the BIA RTOs, including the outage-mode RTO where one exists. (CP-2; CP-4; RC.RP-01)

4.9 Recovery must follow the BIA priority order, and restored systems must be validated before they reconnect. (CP-10; RC.RP-03)

4.10 A lessons-learned review must be held within 14 days after recovery and a written report issued within 30 days. (IR-4; ID.IM-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it, the CSPs, or a NERC CIP requirement.
- STD-03.1 Incident Classification and Escalation Standard
- STD-03.2 Regulatory Notification Standard (NRC, NERC, SEC, and state)
- STD-03.3 Contingency and Disaster Recovery Standard
- PRC-03.1 Plant Business Network Cyber Attack Runbook (P08)
- PRC-03.2 SEC Materiality Assessment Procedure
- PRC-03.3 Multi-State Breach Notification Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certification, the annual Internal Audit assessment (P07), Nuclear Oversight reviews of the security program (73.55(m)), NRC cyber security inspections, and NERC Regional Entity audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract. A violation by a person with unescorted access is also reported to the access authorization program, which decides whether it affects trustworthiness and reliability under 10 CFR 73.56.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception may waive a regulatory requirement, a CSP commitment, an SGI requirement, or a NERC CIP requirement.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 WMS-PBN SSP; P03 gap analysis; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI governance; station cyber security plans and implementing procedures (controlled documents, not attached).

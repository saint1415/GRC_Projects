# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager (corporate and device cloud incidents); Product Security Lead (product security incidents) |
| Approved by | COO |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, RA-5(11), PM-15 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.RA-08, ID.IM-02 |
| Regulatory basis | FD&C Act 524B(b)(1)-(2) (N31-33-R05); 21 CFR 803, 806, 820.35; HIPAA 164.308(a)(6) and 164.410 for the device cloud (N62-R01, N62-R03); Fla. Stat. 501.171(6) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly and lawfully. This includes incidents that affect fielded devices, so that vulnerability handling connects to complaint handling, FDA reporting, customer advisories, and business associate notice to hospitals.

## 2. Scope
All workforce members. Covers:
- **corporate incidents** (email, endpoints, SaaS, the factory floor);
- **device cloud incidents**, including any breach of PHI held for hospitals;
- **product security incidents:** a vulnerability or exploit affecting fielded PM-2 or PM-1 monitors, the device cloud acting as a related system, or the build and signing pipeline.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for corporate and device cloud incidents |
| Product Security Lead | Incident commander for product security incidents; CVD coordinator |
| VP QA/RA | Complaint, MDR, and correction and removal decisions; FDA communications |
| Compliance Manager (Privacy Officer) | Breach risk assessments; notices to hospitals under BAAs |
| COO | Engages counsel and the cyber insurer; approves external communications and customer advisories |
| Customer Support Manager | Hospital communications and complaint intake |
| All workforce | Report suspected incidents and vulnerability reports immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with an exploited vulnerability in a fielded device (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately, and within 1 hour at most**, to the incident line. Examples: a phishing click, a lost laptop, PHI sent to the wrong party, unusual device behavior reported by a hospital, or a message from a security researcher. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; 164.308(a)(6)(ii))
4.3 Every incident must be logged, categorized, and tracked to closure. Product security incidents must also be recorded in the eQMS, where they are evaluated as possible complaints (21 CFR 820.35). (IR-5)
4.4 **Coordinated vulnerability disclosure.** The company must publish a CVD policy that tells researchers how to report vulnerabilities, acknowledge each report within 3 business days, keep the reporter informed, and coordinate public disclosure. The company must participate in an ISAO that shares medical device vulnerabilities. (RA-5(11); PM-15; ID.RA-08; FD&C Act 524B(b)(1))
4.5 Every vulnerability affecting a device or the device cloud must be assessed for its risk to patient safety and essential performance, as controlled or uncontrolled risk, using FDA's postmarket cybersecurity guidance. The VP QA/RA must decide and document whether an MDR (21 CFR 803) or a correction or removal report (21 CFR 806.10) is required. (RS.AN-03; IR-6)
4.6 Critical vulnerabilities that could cause uncontrolled risks must be fixed out of cycle as soon as possible. Customers must be told, with compensating controls, within 30 days of the company learning of an uncontrolled risk. (SI-2; FD&C Act 524B(b)(2)(B))
4.7 The Privacy Officer must decide whether a device cloud incident is a breach of unsecured PHI under 45 CFR 164.402, and document the decision. Notice to each affected hospital must be made without unreasonable delay and no later than 60 calendar days after discovery (164.410), or sooner if the BAA requires it. Under Florida law, a third-party agent must notify the covered entity no later than 10 days after determining the breach or having reason to believe it occurred (Fla. Stat. 501.171(6)). (IR-6; RS.CO-02)
4.8 No ransom may be paid without approval from the CEO, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.9 The incident response plan must be tested at least annually by a tabletop exercise, and after any major incident. (IR-3; ID.IM-02)
4.10 Lessons learned must be documented within 30 days of closing an incident and added to the risk register, the design risk management file, and the POA&M. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the annual tabletop exercise.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved at the level set in POL-01 4.4, and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; published CVD policy; QMS complaint handling, MDR, and correction and removal procedures; BAA terms register; POL-01

# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 incident response plan's policy section) |
| Review cycle | Annually (next review 2027-09-30), and after major incidents or exercises |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, AU-11, SR-11, SR-12 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Contract and regulatory basis | DFARS 252.204-7012(c)-(e); FAR 52.204-25(d); FAR 52.204-23(c); FAR 52.204-30(c); DFARS 252.246-7007(c)(6); DFARS 252.246-7008(b)(3); state breach notification laws |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Ensure Cris Santos Company detects, responds to, reports, and recovers from security incidents and product integrity incidents in a consistent and lawful way, and meets every contract and legal reporting clock.

## 2. Scope
All workforce members, systems, and data, including systems operated by service providers, and every product incident: counterfeit, suspect counterfeit, tampered, or covered products, and CUI found outside the enclave.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Operating Officer | Chairs the crisis management team; declares major incidents |
| Security Manager | Incident commander for cyber incidents; owns this policy and the P08 runbooks |
| Director of Quality and Product Compliance | Incident lead for product incidents; quarantine and authentication decisions |
| Director of Federal Programs | All reports to DoD, primes, and contracting officers (DIBNet, Section 889, FASCSA, sourcing notices) |
| General Counsel | Privilege, breach determinations, notices, regulator and law enforcement contact |
| MSSP | 24x7 detection, containment, and escalation to the Security Manager within 30 minutes for high severity |
| All workforce | Report suspected incidents and suspect products immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incident types: supplier compromise and counterfeit or tampered products, and ransomware (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report suspected incidents, suspect products, and CUI found outside the enclave within 1 hour to the security hotline or the service desk, and must not investigate on their own. (IR-6; RS.MA-02)
4.3 Incidents must be triaged, categorized, and tracked to closure in the incident register, with the time of discovery and the time of identification recorded, because reporting clocks run from them. (IR-4; IR-5; RS.MA-02)
4.4 **Product incidents.** Suspect counterfeit, tampered, or covered items must be quarantined at once, kept, and never returned to the seller or the supply chain until they are determined to be authentic or disposition instructions are received. (SR-11; SR-12; RS.MA-01; DFARS 252.246-7007(c)(6))
4.5 **Reporting clocks.** Notifications must meet the deadlines in the notification matrix (P08), including: DIBNet report within 72 hours of discovery of a cyber incident affecting covered defense information; FAR 52.204-25(d) report within 1 business day of identifying covered telecommunications equipment; FAR 52.204-23(c) and FAR 52.204-30(c) reports within 3 business days of identification; and state breach notices on each state's timeline. File what is known on time and follow up. (IR-6; RS.CO-02; RS.CO-03)
4.6 At least two employees must hold current DoD-approved medium assurance certificates for DIBNet at all times. (IR-6; RS.CO-02)
4.7 When a cyber incident affecting covered defense information is discovered, images of affected systems and relevant monitoring and packet capture data must be preserved for at least 90 days from the DIBNet report, and malicious software must be submitted to the DoD Cyber Crime Center as instructed, never to the contracting officer. (AU-11; IR-4; RS.AN-03)
4.8 The cyber insurer's hotline must be called before any incident response vendor is engaged, and counsel directs forensic work. (IR-4; RS.MA-01)
4.9 No ransom or extortion payment may be made without a sanctions check, counsel's advice, and the Chief Executive Officer's approval. (IR-4; RS.MA-03)
4.10 The plan must be tested at least annually with a tabletop exercise for each runbook, including a DIBNet reporting drill. Incident roles receive training at least annually. (IR-3; IR-2; ID.IM-02)
4.11 Lessons learned must be documented within 30 days of closing a significant incident and fed into the risk register (P01) and the POA&M (P07). (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Compliance is checked through tabletop results, the incident register, and the annual assessment (P07). Failure to report a known incident or suspect product is a sanctionable violation under POL-05 section 4.12.

## 6. Exceptions
None. Reporting deadlines are set by contract and law and cannot be waived internally.

## 7. Related documents
POL-01; P08 `ir-runbook.md`, `ir-runbook-ransomware.md`, and `notification-matrix.csv`; BIA (P05); STD-02; STD-07

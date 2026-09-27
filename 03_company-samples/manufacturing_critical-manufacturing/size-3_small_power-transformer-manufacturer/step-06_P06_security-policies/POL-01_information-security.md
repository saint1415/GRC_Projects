# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | VP Operations |
| Approved by | VP Operations, 2026-09-04 |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review by 2027-09-08), and after major changes or incidents |
| Replaces | IT handbook (2021), for the topics covered here |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, CA-2, CP-1, CP-2, PS-8, RA-3, SA-4, SA-9, SR-2, SR-3, SR-6, SR-11, SI-7 |
| CSF 2.0 | GV.OC-01, GV.OC-03, GV.RM-02, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.SC-05, GV.SC-07, ID.RA-08, ID.RA-09, RC.RP-01 |
| Contract and regulatory drivers | NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary benchmark); FAR 52.204-21, 52.204-23, 52.204-25 (federal contract); Utility Supplier Cyber Security Addenda (CIP-013-2 R1.2 flow-down); 15 CFR 762.6 (C-CRITICAL-MFG-R03) |

## 1. Purpose
Set up the Cris Santos Company information security program for both office IT and the plant floor, assign who is accountable, and give every other security policy its authority.

**Mission and critical services.** The company designs, builds, and tests transformers that electric utilities need to run the grid and to restore it after storms. Its critical services are on-time production (especially reserved storm-restoration slots), the integrity of every transformer and its certified test report, the integrity of the monitoring firmware shipped into utility substations, and the security duties it has accepted in customer contracts. Security decisions are made to protect these services and the safety of the people who work in the plant (see the BIA, P05).

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary workers, and contractors) on the Florida campus and in the field. Covers office IT, plant control systems (OT), the high-voltage test bay, cloud and SaaS services, and systems that service providers operate for the company. It applies to all company information, customer information shared under NDA, and federal contract information (FCI).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| President | Approves the security budget; accepts High and Very High risks; decides on ransom and precautionary plant shutdown with the VP Operations |
| VP Operations | Program owner; approves policies; accepts Moderate risks; chairs the quarterly security review |
| IT Manager | Security program lead for IT, cloud, and identity; maintains the risk register and SSP; manages the MSP |
| Controls Engineer | OT security lead: plant network, PLCs, HMIs, OEM remote access, OT backups and inventory |
| Plant Manager | Authority to isolate the plant network, move to manual operations, or order a safe shutdown; approves OT changes |
| Contracts and Compliance Manager | Keeps the obligations register; reviews security terms before contracts are signed; sends contractual and regulatory notices |
| VP Engineering | Product security: vulnerability intake and disclosure for supplied firmware and software |
| Quality Manager | Integrity of test data, certified test reports, and firmware loaded at final test |
| Supply Chain Manager | Supplier tiering, security terms, and annual supplier reviews |
| All workforce | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain an information security program covering office IT, plant control systems, and cloud and SaaS services, documented in this policy set and the System Security Plan (P02). NIST CSF 2.0, with NIST SP 800-82 Rev. 3 for OT, is the benchmark. (PM-1; GV.PO-01)

4.2 The IT Manager is the security program lead and the Controls Engineer is the OT security lead. Both designations must be in writing and in their job descriptions. (PM-2; GV.RR-02)

4.3 The Plant Manager may order the plant network isolated, a move to manual operations, or a safe shutdown at any time for a security reason. The IT Manager and the Controls Engineer may disconnect the IT/OT firewall, the cloud VPN, or any OEM remote access path without further approval (see POL-03 4.5). (GV.RR-02; IR-4)

4.4 A cybersecurity risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Risks must be tracked in the risk register with an owner and a treatment. (RA-3; PM-9)

4.5 Risk acceptance authority: the IT Manager may accept Low risks; the VP Operations, Moderate; the President, High and Very High, only temporarily and with a dated treatment plan. Risks to worker safety or to the integrity of products delivered to utilities may not be accepted at High or above. (PM-9; GV.RM-02)

4.6 The Contracts and Compliance Manager must keep an obligations register of every legal, regulatory, and contractual cybersecurity duty, with an owner and trigger for each: the utility security addenda, FAR 52.204-21, 52.204-23, and 52.204-25, 15 CFR 762.6, and Fla. Stat. 501.171. The register must be reviewed quarterly. Any contract with security terms must be reviewed by the Contracts and Compliance Manager and the IT Manager before signature. (SA-4; GV.OC-03)

4.7 Suppliers must be tiered by their access to company systems and their effect on products. Tier 1 suppliers (the MSP, cloud, identity, ERP, MES, and EDI providers, OEMs with remote access, the TMU electronics supplier, and AI service vendors) must accept security terms covering incident notice, vulnerability disclosure, remote access rules, and software integrity, and must be reviewed annually (SOC 2 report or questionnaire). (SR-2; SR-6; SA-9; GV.SC-05; GV.SC-07)

4.8 Product security: the VP Engineering must run intake for vulnerabilities in the firmware and software the company supplies with its products, and disclose known vulnerabilities to the addendum utilities within the contract deadline (30 days). The Quality Manager must verify the hash or signature of every firmware image on receipt and before loading at final test, and give utilities the hashes. (SI-7; SR-11; ID.RA-08; ID.RA-09)

4.9 The company must not buy or use covered telecommunications or video surveillance equipment or services (FAR 52.204-25) or Kaspersky covered articles (FAR 52.204-23). Purchasing must check new IT, OT, and security equipment against these definitions. Any covered item found must be reported to the Contracts and Compliance Manager the same day, for the contracting officer report. (SR-3; CM-8)

4.10 Security policies must be reviewed at least annually and updated after major changes or incidents. Security controls must be assessed at least annually (P07). (PL-1; CA-2; GV.PO-02)

4.11 Exceptions to any security policy must be requested in writing, risk-rated, approved per 4.5, recorded in the risk register, and limited to 12 months or less. (PL-1)

4.12 **Sanctions.** Workforce members and contractors who break security policies must face consequences in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each case. Good-faith incident reports are never sanctioned. (PS-8; GV.RR-04)

4.13 The company must keep a business impact analysis and a contingency plan that includes manual production procedures (paper travelers and a printed schedule) and OT recovery steps, and must test them at least annually. (CP-1; CP-2; RC.RP-01)

## 5. Compliance and enforcement
Violations are handled under POL-01 statement 4.12. Consequences range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), access reviews, and the quarterly obligations register review.

## 6. Exceptions
Exceptions follow POL-01 statement 4.11. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months. Exceptions for plant equipment that cannot technically meet a statement (for example, an HMI without individual accounts) must name the compensating controls.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); BIA (P05); obligations register; NIST CSF 2.0; NIST SP 800-82 Rev. 3; FAR 52.204-21, 52.204-23, 52.204-25; utility Supplier Cyber Security Addenda

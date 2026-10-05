# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2022 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, CM-3, CM-4, RA-3, PM-9, CA-5, IR-5, PL-1, SA-9, SR-6, CA-2, SI-12, AU-11, PS-8 |
| CSF 2.0 | GV.OV-01, GV.PO-01, GV.PO-02, GV.RM-01, GV.RM-03, GV.RR-04, GV.SC-05, GV.SC-07, ID.IM-01, ID.IM-02, ID.RA-05, ID.RA-07, PR.DS-11 |
| Regulatory drivers | C-NUCLEAR-S06, C-NUCLEAR-R01, C-NUCLEAR-S03, C-NUCLEAR-R03, C-NUCLEAR-S04, C-NUCLEAR-S01, C-NUCLEAR-S02 |
| Supporting standards | STD-01 Configuration; STD-03 Vendor risk management; STD-04 CSP interface and change screening; STD-05 AI use (see `standards-index.md`) |

## 1. Purpose
Establish the Cris Santos Company information security program for the business network, the cloud, and business data; assign accountability; define how the program works with the NRC-approved cyber security plan (CSP); and give every other security policy and standard its authority.

## 2. Scope
All employees, long-term contractors, outage contractors, and vendors at the Station and the EOF, and all business systems and data (the PBN-WMS and the AI tools). Critical digital assets (CDAs) at Levels 3 and 4 are governed by the CSP and its implementing procedures. Where this policy and the CSP overlap, the CSP controls for anything in 73.54 scope.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Site Vice President | Executive sponsor and PBN-WMS system owner; approves POL-02 to POL-05; accepts Moderate risks; NERC CIP Senior Manager |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| Cyber Security Program Manager | Owns the CSP; decides whether a change or system is in 73.54 scope; co-owns boundary risks |
| IT Director and IT Security Manager | Run the business network program day to day; the IT Security Manager is the information system security officer |
| Compliance and GRC Lead | Risk register, policy management, NERC CIP evidence |
| Director of Security | SGI program, access authorization program, Security-Related Information rules |
| Nuclear Oversight and the co-sourced internal audit firm | Independent assessment (P07) and the 73.55(m) review |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program for the business network and business data, documented in this policy set, the supporting standards, and the SSP, and coordinated with the CSP. (PM-1; GV.PO-01; C-NUCLEAR-S06)
4.2 **CSP boundary rule.** No business system, cloud service, vendor connection, or AI tool may connect to, receive data from, or support a function of a CDA or an EP system unless the Cyber Security Program Manager has first evaluated it under 10 CFR 73.54(b)(1) and (d)(3). Every IT change ticket and IT purchase request must answer the CSP scope question. (CM-3; CM-4; ID.RA-07; C-NUCLEAR-R01 (73.54(b)(1), (d)(3)))
4.3 Every IT change and purchase that could affect the emergency plan or plant security must also pass the 10 CFR 73.58 safety/security interface screening. (CM-4; GV.RM-03; C-NUCLEAR-S03 (73.58(b)-(d)))
4.4 An enterprise risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Every risk must be recorded with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-05; C-NUCLEAR-R01 (73.54(d)(2)))
4.5 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks; the Site Vice President, Moderate; the CEO, High for up to 12 months with a dated plan. Very High risks may not be accepted except by a 90-day CEO exception after notice to the audit committee chair. A known regulatory noncompliance may never be accepted; it must be corrected through the corrective action program. (PM-9; GV.RM-01; C-NUCLEAR-S06)
4.6 Cyber security program deficiencies found by IT, the MSSP, or assessors must be entered in the corrective action program within 24 hours of discovery when they concern the 73.54 program. (CA-5; IR-5; ID.IM-02; C-NUCLEAR-R03 (73.77(b)(1)))
4.7 The vCISO must report to the audit committee each quarter on top risks, POA&M status, incidents, and roadmap progress. (CA-5; GV.OV-01; C-NUCLEAR-S06)
4.8 Security policies must be reviewed at least annually and after major changes or incidents; standards annually by their owners. Exceptions must be written, risk-rated, approved under 4.5, recorded in the risk register, and limited to 12 months. (PL-1; GV.PO-02; C-NUCLEAR-S06)
4.9 **Vendors.** No vendor may connect to the business network or receive Restricted or Confidential data without a security review scaled to its tier, contract security terms (named accounts, MFA, incident notice within 72 hours, and personal information breach notice within 10 days), and approval by the Compliance and GRC Lead. Tier 1 vendors must be reassessed each year (STD-03; P09). (SA-9; SR-6; GV.SC-05; GV.SC-07; C-NUCLEAR-S04 (501.171(6)); C-NUCLEAR-S06)
4.10 Security controls must be independently assessed at least annually (P07). The cyber security program must also be reviewed at least every 24 months under 10 CFR 73.55(m) by individuals independent of program management. (CA-2; ID.IM-01; C-NUCLEAR-R01 (73.54(g)); C-NUCLEAR-S03 (73.55(m)))
4.11 Records that support CSP decisions (evaluations, tickets, logs used as evidence) must be retained until license termination, with superseded versions kept at least 3 years; other security records 6 years. (SI-12; AU-11; PR.DS-11; C-NUCLEAR-R01 (73.54(h)))
4.12 AI tools must be approved through the AI governance process before use (STD-05; P10). No AI tool may connect to a CDA, take any automatic action on plant equipment, or receive SGI or SRI. (PM-9; SA-9; GV.RM-01; C-NUCLEAR-S01; C-NUCLEAR-S06)
4.13 Workforce members who violate security policies are subject to sanctions under the HR disciplinary policy; behavior of concern is also reported to the access authorization program. (PS-8; GV.RR-04; C-NUCLEAR-S02 (73.56))

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), quarterly access reviews, the metrics reported to the audit committee, and, for anything in 73.54 scope, the 73.55(m) program review. Violations are handled under POL-01 4.13.

## 6. Exceptions
Exceptions follow POL-01 4.8: written, risk-rated, approved by the right authority under POL-01 4.5, recorded in the risk register, and limited to 12 months. No exception may permit a known regulatory noncompliance.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; SSP (P02); risk register and appetite (P01); the CSP and its implementing procedures (SRI); 10 CFR 73.54, 73.55(m), 73.58, 73.77; NERC CIP-003-9

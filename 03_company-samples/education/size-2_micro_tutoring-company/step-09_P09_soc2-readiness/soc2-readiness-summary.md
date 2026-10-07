# SOC 2 Readiness Summary: Cris Santos Company | Educational Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (K-12 tutoring and learning center) |
| Tier / Vertical | Micro / Educational Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the school district's vendor security questionnaire |
| Part B | Tutoring platform vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-18 by the Center Director with the independent consultant; approved by the Owner 2026-08-28 |

## 1. Why SOC 2 for this organization
A 7-person tutoring company could, in principle, be a service organization: it delivers a service to the district. But no customer has asked for a SOC 2 report, and the company will not seek one. The Trust Services Criteria are used here for two practical reasons.

**A. Answering the district's questionnaire.** The district sends every vendor that handles student data an annual security questionnaire. Its questions follow the Trust Services Criteria for security and confidentiality. The company will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-09-30, three weeks after the program restarts.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. An audit would also cost more than the district contract's margin. The district's questionnaire accepts a self-assessment from vendors of this size.

**B. Relying on the tutoring platform vendor.** The platform vendor carries most of the company's inherited controls (P02 section 10.2) and holds the system of record for children's information. Its SOC 2 Type 2 report is the evidence for those controls. Reviewing it each year is part of the due diligence that 16 CFR 312.8(c) requires before letting a service provider maintain children's information.

**Why Confidentiality and not another category.** The district's data privacy agreement is about keeping program students' data confidential and deleting it on time, and the questionnaire asks exactly that. Families care most about who can see evaluation reports and recordings. Availability matters less to the district: missed sessions can be made up (P05 MTD 72 hours for the program). Processing Integrity was not requested. The Privacy criteria were not requested either; the company's children's privacy duties are tracked against the COPPA Rule itself in P03, which is the stricter and binding standard.

## 2. System description (scope)
- **Services:** K-12 tutoring in person and online; the district after-school program for about 90 students.
- **Infrastructure and software:** the Tutoring Operations Platform (SSP, P02): tutoring platform, scheduling platform, productivity suite, suite backup, 18 company devices, center network, website.
- **People:** 7 employees, 14 contractor tutors, and the MSP.
- **Data:** children's personal information, district roster data, parent contact and billing data, staff and contractor files.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 18 | 9 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Information Security Coordinator designated; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access (locked center with alarm; vendor data centers under SOC 2)

**Not ready:**
- CC2.1: no inventory of systems or of where children's information lives
- CC3.3: fraud risk not assessed
- CC6.2 and CC6.3: access granted without approval and not removed (former contractor tutors; trial child accounts)
- CC6.5 and C1.2: nothing has ever been deleted, and disposal is unrecorded
- CC7.2, CC7.3, CC7.5: no monitoring, no incident records, recovery unproven (the same gap as risk R-010)
- CC8.1: vendors and the MSP change things without the company's approval (the AI module)

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments and new contractor agreements (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Platform vendor SOC 2 review | CC9.2 | Yes | Bridge letter (2026-10); signed data processing addendum (2026-10) |
| Background screening and child-safety training records | CC1.4 | Yes | Security and privacy training records (from 2026-10) |
| MSP monthly report (patching, antivirus, encryption) | CC5.2, CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Contractor tutor device attestations | CC6.7, C1.1 | No | 2026-09 |
| Restore test records | CC7.5 | No | Quarterly from 2026-09 |
| Retention purge and deletion record | CC6.5, C1.2 | No | Yearly from 2026-11 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the platform vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-04-30. One exception (a late quarterly access review of vendor engineers), remediated.
- **Confidentiality:** in scope; encryption at rest and in transit, including recordings, meets POL-04 4.2.
- **Availability:** the vendor's RPO of 1 hour meets the BIA. Its RTO of 8 hours does **not** meet the 4-hour RTO for online sessions (BP-03); the downtime steps cover the gap (P01 R-011).
- **The AI module is not covered.** The AI progress insights module was released in May 2026, after the report period. It is untested by the auditor, and the vendor's terms allow de-identified data for product improvement. P10 sets the conditions; the module stays off until then.
- **Controls the company must run.** The report lists complementary user entity controls: user provisioning and removal, role assignment, enabling MFA, setting data retention, and reviewing customer audit logs. Four are open gaps at the company: removal (POAM-001, POAM-012), MFA (POAM-002), retention (POAM-010), and log review. **The vendor's controls protect the company only once those gaps are closed.**
- **Follow-ups:** request a bridge letter to 2026-09-30; sign a data processing addendum with no model training, deletion on request, and 72-hour incident notice; ask whether the next report will cover the AI module.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC1.5, CC6.2, CC6.7, CC7.3 | Acknowledgments and contractor agreements (POAM-009); questionnaire response; onboarding checklist and consent before accounts (POAM-001); platform-only rosters and attestations (POAM-008); incident log |
| 2026 Q4 | CC1.2, CC1.4, CC2.1, CC2.2, CC2.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.3, CC6.5, CC6.6, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, C1.1, C1.2 | Monthly oversight notes; training (POAM-003); inventory (POAM-006); new notices; checklists; MFA (POAM-002); offboarding (POAM-012); disposal records; segmentation (POAM-011); EDR and alerts; restore tests and backup upgrade (POAM-004, POAM-005); tabletop (POAM-013); change notes; contingency plan; addendum and MSP amendment (POAM-007); retention purge (POAM-010) |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk assessment |

**Response to the district:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Center Director as security contact, confirm the 48-hour notice procedure in P08, and commit to an updated self-assessment before the 2027-2028 school year.

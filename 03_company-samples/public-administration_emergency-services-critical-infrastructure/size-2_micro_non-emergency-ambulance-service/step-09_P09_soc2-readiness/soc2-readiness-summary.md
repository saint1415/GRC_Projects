# SOC 2 Readiness Summary: Cris Santos Company | Emergency Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed BLS ambulance service, non-emergency transport only) |
| Tier / Vertical | Micro / Emergency Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the regional hospital's transport vendor questionnaire |
| Part B | Operations platform vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-26 by the Office Manager with the independent consultant; approved by the Owner 2026-09-04 |

## 1. Why SOC 2 for this organization
A non-emergency ambulance company is **not** a SOC 2 service organization. It transports patients; it does not run systems for other businesses. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a questionnaire.** The regional hospital renews its transport agreement each year. In July 2026 it sent its transport vendor security questionnaire, which follows the Trust Services Criteria and asks about security and availability. The company will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-09-30.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in September 2026. An audit would also cost more than a year of the company's whole security budget. The hospital's instructions accept a self-assessment from vendors of this size.

**B. Relying on the platform vendor.** The operations platform holds every trip and patient care record and carries most of the company's inherited controls (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls, and reviewing it each year is part of vendor oversight under 45 CFR 164.308(b) and SA-9.

**Why Availability and not another category.** The hospital needs to know its discharges will be picked up when booked, and dialysis centers need the same for their patients. The company cannot dispatch from the board without the platform, the phones, and the internet (P05). Confidentiality of patient information is covered under the Security criteria and the HIPAA Privacy Rule. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** non-emergency BLS transport, about 3,000 trips a year, for hospitals, dialysis centers, nursing facilities, and families.
- **Infrastructure and software:** the Transport Operations Platform (SSP, P02): operations platform, productivity suite, hosted phone system, suite backup, 10 devices, office network, vehicle hotspots.
- **People:** 7 workforce members, the contracted Medical Director, the MSP, and the billing company.
- **Data:** trip requests, certification statements, patient care reports, call recordings, claims, workforce data.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 18 | 10 | 0 |
| Availability (A1, 3) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security and Privacy Officer designated; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk analysis done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked

**Not ready:**
- CC2.1: no inventory of devices or ePHI
- CC3.3: fraud risk not assessed
- CC6.1, CC6.2, CC6.3: no MFA on the platform, a shared dispatch account, and access granted and removed without a process (the former EMT and facility portal accounts)
- CC7.1, CC7.2, CC7.3: no vulnerability scanning, monitoring, or incident records
- CC7.5, A1.2, A1.3: recovery unproven (the same gap as risks R-005 and R-008)
- CC8.1: changes to company devices are not approved (the remote desktop tool)

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Platform vendor SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| BAA list | CC9.2 | Yes | AI feature confirmation (2026-10); MSP subcontractor confirmation (2026-10) |
| MSP monthly report (patching, antivirus, encryption, MDM) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Platform MFA report | CC6.1 | No | From 2026-10 |
| Account reconciliation, export check, and log review records | CC6.2, CC6.3, CC7.2 | No | Weekly and monthly from 2026-09 |
| Restore test records and manual dispatch drill reports | CC7.5, A1.3 | No | Quarterly from 2026-09 |
| Training and phishing simulation records | CC1.4, CC2.2 | New-hire video only | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the platform vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-05-31. One exception (a missing change approval for 1 of 25 sampled changes), remediated.
- **Availability:** the vendor's stated RPO of 15 minutes meets the BIA. **Its stated RTO of 4 hours does not meet the 2-hour RTO for dispatch (BP-02).** The company covers the gap with the nightly printed run sheet and manual dispatch, which is why the drill matters (POAM-009).
- **The AI intake feature is not covered.** It was released after the report period. The company needs the vendor's description of its controls and subprocessor before relying on it (P10).
- **Controls the company must run.** The report lists complementary user entity controls: user provisioning and removal, enabling MFA, role assignment, review of access and export reports, and protecting devices that run the mobile apps. Three are open gaps at the company: MFA (POAM-003), removal (POAM-001, POAM-004), and review (POAM-007). **The vendor's controls protect the company only once those gaps are closed.**
- **Follow-ups:** request a bridge letter to 2026-09-30; ask for 24-hour incident notice and Florida third-party agent notice within 10 days at renewal; ask when the AI feature will be in scope.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC2.3, CC5.3 | Acknowledgments; staff briefing and reporting card; checklists; questionnaire response |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC3.4, CC5.1, CC5.2, CC6.1-CC6.8, CC7.1-CC7.5, CC8.1, CC9.1, CC9.2, A1.1-A1.3 | Monthly oversight notes; training (POAM-006); inventory (POAM-008); platform MFA and named accounts (POAM-002, POAM-003); account process (POAM-001, POAM-004); network cabinet; disposal records; Wi-Fi separation; encryption (POAM-012); EDR and software list (POAM-013, POAM-014); scanning; log review (POAM-007); incident log; tabletop; restore tests and backup upgrade (POAM-009, POAM-010); change approval; contingency plan; vendor reviews (POAM-011); failover router |
| 2027 Q3 | CC3.3 | Fraud scenarios in the August 2027 risk analysis |

**Response to the hospital:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Office Manager as security contact, and commit to an updated self-assessment with the 2027 agreement renewal.

# SOC 2 Readiness Summary: Cris Santos Company | Healthcare and Public Health | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent community pharmacy) |
| Tier / Vertical | Micro / Healthcare and Public Health |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Target report | None. Readiness self-assessment only (no Type 1 or Type 2 audit planned) |
| Part A | Pharmacy readiness self-assessment (`soc2-readiness.csv`), used to answer the ALF management company's vendor questionnaire |
| Part B | PMS vendor SOC 2 Type 2 report (EV-023) and EPCS third-party audit report (EV-065) review (`vendor-soc2-review.csv`) |
| Prepared | Part B reviewed 2026-08-12; Part A completed 2026-08-21 by the Store Manager with the independent consultant; approved by the pharmacist-owner 2026-08-28 |

## 1. Why SOC 2 for this organization
An independent pharmacy is **not** a SOC 2 service organization in the usual sense. It dispenses to patients; it does not run systems for other businesses. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a questionnaire.** The pharmacy supplies weekly adherence packs to about 40 residents of two assisted living facilities run by one management company, its largest single relationship (P05 BP-05). In July 2026 the management company sent its pharmacy vendors a security questionnaire organized by the Trust Services Criteria, asking about security and the ability to keep packs and deliveries coming. The response is due 2026-09-30 (EV-033). The pharmacy will answer with this self-assessment, the POA&M (P07), and a named security contact.

**The pharmacy will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the pharmacy's controls were defined in August 2026. An audit would also cost far more than the management company asked for; its questionnaire instructions accept a self-assessment from small vendors.

**B. Relying on the PMS vendor.** The PMS vendor carries most of the pharmacy's inherited controls (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls, and its EPCS third-party audit report is the evidence the DEA rule requires before the pharmacy relies on the PMS for controlled substance prescriptions (21 CFR 1311.200(a)). Reviewing both each year is part of vendor oversight under 45 CFR 164.308(b) and SA-9.

**Why Availability and not another category.** The ALF management company needs to know that residents' packs and deliveries will arrive on time. The pharmacy cannot dispense safely without the PMS and the internet (P05). Confidentiality of patient information is covered under the Security criteria and the HIPAA Privacy Rule. Processing Integrity and Privacy were not requested. The 25 criteria in those three categories are marked N/A.

## 2. System description (scope)
- **Services:** retail prescriptions, controlled substance dispensing, weekly adherence packaging for about 70 patients (about 40 ALF residents), and about 25 deliveries a day.
- **Infrastructure and software:** the Pharmacy Core SaaS Stack (SSP, P02): PMS, productivity suite, store computers and delivery phone, store network, adherence packaging system, cloud fax, cloud backup, and the proof-of-delivery app.
- **People:** 7 workforce members, the MSP, and the PMS and packaging equipment vendors.
- **Data:** ePHI (profiles, prescriptions, ALF medication lists, delivery records), controlled substance records, claims, workforce data.
- **Procedures:** POL-02, POL-03, POL-04, and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 18 | 9 | 0 |
| Availability (A1, 3) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security and Privacy Officer designated; roles defined, including pharmacist EPCS duties
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk analysis done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access (keyed entry, alarm, cameras, locked Schedule II safe; vendor data centers under SOC 2)

**Not ready:**
- CC2.1: no inventory of devices or ePHI
- CC3.3: fraud and diversion scenarios not in the risk analysis
- CC6.2 and CC6.3: access granted and removed without a process (the former technician's accounts)
- CC7.1, CC7.2, CC7.3: no vulnerability scanning, the EPCS report not reviewed consistently, no incident records
- CC7.5, A1.2, A1.3: recovery unproven (the same gap as risk R-005)
- CC8.1: changes reach the pharmacy without its approval (the packaging patch exclusion and the vendor's risk score release)

## 4. Evidence inventory
The questionnaire asks for evidence. What the pharmacy can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| PMS vendor SOC 2 and EPCS audit report review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| BAA list | CC9.2 | Yes (4 vendors) | Delivery app and packaging vendor BAAs; MSP subcontractor confirmation (2026-10) |
| MSP monthly report (patching, antivirus, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Daily EPCS audit review log | CC7.2 | No | Daily from 2026-09-01 |
| Account reconciliation and access review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-09 |
| Restore test records | CC7.5, A1.3 | No | Quarterly from 2026-09 |
| Training and phishing simulation records | CC1.4, CC2.2 | Privacy video only | From 2026-10 |
| Contingency plan and downtime card; tabletop report | CC7.4, CC9.1 | No | 2026-11 |

## 5. Findings from the PMS vendor reports (Part B)
- **SOC 2 opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception (2 of 40 sampled production releases deployed without a documented approval), remediated in 2026-02. The pharmacy has asked whether the May 2026 release that switched on the controlled substance risk score went through the approval process (P10).
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 30 minutes **meet the pharmacy's BIA** (RTO 4 h for BP-01 and BP-04; RPO 1 h for BP-01 to BP-03).
- **EPCS audit report:** a third-party audit dated 2025-10-15 finds the PMS meets the pharmacy application requirements, with no limitation on additional prescription information. The pharmacist-owner recorded the determination required by 21 CFR 1311.200(a) on 2026-08-12, about 7 years after the pharmacy started using the hosted PMS. The pharmacy asked the vendor in writing whether the May 2026 release changed EPCS functionality and so needs a new audit (1311.300(a)(2)).
- **Controls the pharmacy must run.** The SOC 2 report lists complementary user entity controls: user provisioning and removal, role assignment (including controlled substance permissions), MFA configuration, review of access reports and the daily EPCS audit report, and reporting security incidents to the vendor. Three are open gaps at the pharmacy: removal (POAM-001, POAM-002), review (POAM-004), and in-store MFA (POAM-005). **The vendor's controls protect the pharmacy only once those gaps are closed.**
- **Follow-ups:** request a bridge letter to 2026-09-30; ask how the vendor monitors the carved-out claims switch and e-prescribing network; ask for 24-hour incident notice at BAA renewal.

## 6. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC2.3, CC6.2, CC7.3 | Acknowledgments; questionnaire response; daily EPCS review log (POAM-004); onboarding checklist (POAM-001); reporting cards (POAM-012); assessment of the March 2026 fax |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.3, CC6.5, CC6.6, CC6.7, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, A1.1, A1.2, A1.3 | Monthly oversight notes; training (POAM-009); inventory; termination process (POAM-002); EDR (POAM-006); restore tests and backup upgrade (POAM-007, POAM-008); encryption (POAM-011); packaging workstation segment (POAM-014); contingency plan and failover router; BAAs and MSP review (POAM-010); release review rule |
| 2027 Q3 | CC3.3 | Fraud and diversion scenarios in the July 2027 risk analysis |

**Response to the ALF management company:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Store Manager as security contact, and commit to an updated self-assessment in April 2027.

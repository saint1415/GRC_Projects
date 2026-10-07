# SOC 2 Readiness Summary: Cris Santos Company | Chemical | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical maker) |
| Tier / Vertical | Micro / Chemical |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Target report | None. This is a self-assessment, not a CPA examination. No Type 1 or Type 2 report is planned |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the private-label distributor's questionnaire |
| Part B | Accounting and inventory vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-19 by the Office Manager (Security Coordinator) with the independent consultant; updated for the policies and approved by the Owner and President on 2026-08-31 |

## 1. Why SOC 2 for this organization
**The company is not a SOC 2 service organization.** It blends, packages, and ships chemical products. Customers receive pails, drums, and totes, not an IT service, so a SOC 2 report on the company's own system is not the right product. The vertical registry lists no chemical-sector assurance alternative.

The Trust Services Criteria are still useful for two reasons.

**A. Answering a questionnaire.** In June 2026 the company's largest customer, a regional distributor that buys private-label products (about 22% of revenue), sent a supplier security and continuity questionnaire. It asks how the company protects its systems and how quickly it could ship again after a cyber incident. Its questions follow the Trust Services Criteria. The company will answer with this self-assessment, a POA&M extract (P07), and a named security contact. The response is due 2026-09-30.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. An audit would also cost more than the company's whole 2026 security budget (P01 section 4). The distributor's instructions accept a self-assessment.

**B. Relying on the accounting and inventory vendor.** Orders, lots, invoices, and the hazmat bills of lading run on this service (SYS-07). It carries the company's inherited controls for that data (P02 section 10.2), and its SOC 2 Type 2 report is the evidence. Reviewing it each year is part of vendor oversight (POL-02 A.5; SA-9).

**Why Availability and not another category.** The distributor's main concern is continuity of supply, and the BIA (P05) shows that shipping stops within a day without the accounting service and the internet. The confidentiality of formulation summaries shared with the distributor is covered under the Security criteria (CC6.1, CC6.7) and the supply agreement. Processing Integrity and Privacy were not requested, and the company holds no consumer personal information.

## 2. System description (scope)
- **Services:** blending, packaging, and shipping of about 180 specialty cleaning, degreasing, and water-treatment products, including private-label products, for about 140 business customers.
- **Infrastructure and software:** the Blending and Business Platform (SSP, P02): the batch control PLC, the HMI and recipe PC, the integrator's remote access gateway, the office network, 7 endpoints, the productivity suite, the accounting and inventory service, the SDS and label service, and the cloud backup.
- **People:** 7 employees, the MSP, and the control system integrator.
- **Data:** 85 formulations and recipes (Restricted), customer orders and lots, bills of lading, certificates of analysis, and employee personal information.
- **Procedures:** POL-02, POL-03, POL-04, the emergency action plan, and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 17 | 11 | 0 |
| Availability (A1, 3) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready (5):**
- CC3.1 and CC3.2: risk tolerance set and the 2026 risk assessment done
- CC3.3: fraud scenarios assessed (payment redirection, hydrogen peroxide theft)
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked in the POA&M

**Not ready (13):**
- CC2.1: no inventory or network diagram
- CC6.1, CC6.2, CC6.3: shared logins on the portal and HMI; no approval or removal process
- CC6.6: always-on integrator gateway; flat network; guest Wi-Fi reached the HMI
- CC6.8, CC7.1: HMI PC with no malware protection, unpatched since 2023
- CC7.2, CC7.3: no monitoring and no incident records
- CC7.5, A1.2, A1.3: no tested way to restore the batch control system (the same gap as risk R-005)
- CC8.1: recipe and alarm limit changes were never approved or logged

**The pattern matches P03 and P07.** The SaaS services and office computers are in fair shape because vendors and the MSP run them. The gaps sit in the batch control system, which nobody managed for security before 2026. **What this means for the distributor:** finished goods cover about 3 days, and shipping can continue on paper (P05). If the HMI PC were lost today, blending would take 1 to 2 weeks to restore. After POAM-004 and POAM-005 close, the target is 24 hours.

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC3.3, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| BIA summary (P05) | CC9.1, A1.1 | Yes | Updated after the first restore test |
| Accounting vendor SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| MSP monthly report (patching, antivirus, backup) | CC6.8, CC7.1, A1.2 | Yes (July 2026) | Monthly |
| Integrator session log with approvals | CC6.6, CC7.2 | No (log exists; no approvals) | From 2026-09 |
| Batch tickets with the Owner's change approval | CC8.1 | No | From 2026-09 |
| Account reconciliation records | CC6.2, CC6.3 | No | Monthly from 2026-10 |
| Restore test records | CC7.5, A1.3 | No | First shared-drive test 2026-09; HMI and PLC test 2026-12 |
| Training and phishing simulation records | CC1.4, CC2.2 | DOT training only | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the accounting vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-05-31. One exception (a missing quarterly restore test record), remediated.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 1 hour **meet the BIA** (BP-04 RTO 8 h; BP-03 RPO 1 h).
- **Controls the company must run (CUECs).** The report assumes the customer provisions and removes users, enforces MFA for all users, and reviews access. All three were open gaps at the company during fieldwork: MFA (POAM-002), removal (POAM-003, POAM-011), and review (POAM-003). **The vendor's controls protect the company only once those gaps are closed.**
- **Retention:** bills of lading must be retrievable for 2 years (49 CFR 172.201(e)). Data is kept only for the life of the subscription, so the company will export a yearly archive.
- **Follow-ups:** request a bridge letter to 2026-09-30; confirm how the vendor monitors its carved-out hosting provider; ask for 24-hour incident notice at renewal.

## 6. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC2.3, CC6.2, CC6.4, CC6.7, CC7.3 | Acknowledgments; questionnaire response; onboarding checklist (POAM-003); door code changed (POAM-011); open link removed; incident log and reporting cards (POAM-012) |
| 2026 Q4 | CC1.2, CC1.3, CC1.4, CC1.5, CC2.1, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.3, CC6.5, CC6.6, CC6.8, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, A1.2, A1.3 | Monthly oversight notes; inventory and network diagram; named portal accounts with MFA (POAM-001, POAM-002); named HMI logins and audit trail (POAM-003, POAM-009); HMI segment (POAM-006); allowlisting (POAM-008); training (POAM-010); tabletop (POAM-012); offline backup and restore test (POAM-004, POAM-005); contingency plan; vendor terms (POAM-013) |
| 2027 | CC7.1, A1.1 | Supported HMI PC at the 2027 year-end shutdown (POAM-007); internet failover reconsidered at the July 2027 review |

**Response to the distributor:** send this summary, the readiness checklist, and a POA&M extract limited to items that affect supply continuity and shared formulation data by 2026-09-30, name the Office Manager as security contact, and commit to an updated self-assessment in April 2027.

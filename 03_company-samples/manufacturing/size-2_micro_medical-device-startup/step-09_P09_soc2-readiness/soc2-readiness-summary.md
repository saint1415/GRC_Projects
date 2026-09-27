# SOC 2 Readiness Summary: Cris Santos Company | Manufacturing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (medical device startup) |
| Tier / Vertical | Micro / Manufacturing (NAICS 334510) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Part A | Readiness self-assessment (`soc2-readiness.csv`), used to answer the partner hospital system's vendor security review |
| Part B | Cloud provider SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 by the Operations Manager and the Cloud Software Engineer with the independent consultant; approved by the CEO 2026-08-31 |

## 1. Why SOC 2 for this organization
The company is not yet a service organization in practice: it has no customers using the WM-1 cloud service and no patient data. But hospitals will buy WM-1 together with a cloud service that holds their patients' data and sends alerts to their clinicians. Hospital vendor risk teams ask cloud-connected device makers for SOC 2 evidence, and the partner hospital system has already started.

**A. Answering the partner hospital's vendor security review.** The partner hospital system plans a clinical pilot after clearance. Its vendor security questionnaire is due back on 2026-10-30 and follows the Trust Services Criteria. The company will answer with this self-assessment, the POA&M (P07), and the P03 premarket roadmap, and will name the Head of Engineering as security contact.

**The company will not get a SOC 2 audit now.** A Type 2 report needs controls that operate over a period, usually 6 to 12 months. Most of the company's controls were defined in August 2026, and the service is not in production. The realistic path is a Type 1 report on the production cloud service near commercial launch and a Type 2 after the first observation period. The partner hospital accepted a self-assessment for the pre-clearance review.

**B. Relying on the cloud provider.** The cloud provider runs the platform under the WM-1 cloud service and is the main source of inherited controls (P02 section 10.2). Its SOC 2 Type 2 report is the evidence, and reviewing it each year is part of vendor oversight (SA-9) and of the purchasing controls the QMSR expects (ISO 13485 cl. 7.4, incorporated by reference).

**Why Availability and not another category.** The hospital needs to know that remote viewing and secondary alerts will be there when clinicians rely on them, and that firmware fixes can be delivered (P05 BP-05, BP-01). Confidentiality of design data is covered by the Security criteria and NDAs. Processing Integrity and Privacy become relevant when patient data flows and will be reconsidered before the clinical pilot.

## 2. System description (scope)
- **Services:** the WM-1 cloud service (ingestion, clinician dashboard, secondary alerts, firmware update distribution), in pre-production.
- **Infrastructure and software:** the Product Development and Release Platform (SSP, P02): cloud tenant, repository and CI, eQMS, productivity suite, laptops, lab, signing key.
- **People:** 7 employees, the MSP, and the contract manufacturer (for provisioning).
- **Data:** test and simulator data today; hospital patient data after clearance.
- **Procedures:** POL-02, POL-03, POL-04, and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 20 | 7 | 0 |
| Availability (A1, 3) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles designated in writing
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access (building, suite, safe; provider data centers under SOC 2)

**Not ready:**
- CC2.1: no inventory or SBOM
- CC2.3: no published security contact or CVD policy
- CC6.2 and CC6.3: access granted and removed without a process (the former contractor)
- CC7.1 and CC7.2: no vulnerability monitoring of device components and no log review
- CC7.5, A1.2, A1.3: recovery unproven and no clinical recovery targets (P01 R-015)

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation memo; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01), assessment summary (P07), P03 roadmap | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Cloud provider SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| MSP monthly report (patching, EDR, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Incident response runbook and tabletop notes | CC7.3, CC7.4 | Yes | Next tabletop before commercial distribution |
| CVD policy and ISAO membership | CC2.3, CC7.1 | No | 2026-10 |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| SBOM and vulnerability monitoring records | CC2.1, CC7.1 | No | Weekly from 2026-12 |
| Restore test records | CC7.5, A1.3 | No | From 2026-10, then twice a year |
| Penetration test report | CC4.1, CC7.1 | No | 2027-01 |
| Training records | CC1.4, CC2.2 | Onboarding video only | From 2026-10 |

## 5. Findings from the cloud provider report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. Two exceptions (a late removal of an operator's access; one change without a recorded approval), both remediated.
- **Scope:** all six services the company uses are in scope, including the HSM-backed key tier the company should be using for its signing key.
- **Controls the company must run.** The report lists complementary user entity controls. Four are open gaps at the company: the shared owner account (POAM-002), restore testing (POAM-009), key management (POAM-003), and log review (SSP AU-6). **The provider's controls protect the company only once those gaps are closed.**
- **Follow-ups:** request a bridge letter to 2026-09-30; set the account security contact to a monitored shared mailbox; choose regions whose facilities are covered before clinical launch.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC6.2 | Acknowledgments; policy briefing; onboarding checklist (POAM-001) |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.3, CC3.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.3, CC6.5, CC6.6, CC6.7, CC6.8, CC7.1-CC7.5, CC8.1, CC9.1, CC9.2, A1.1-A1.3 | Oversight notes; training; inventory and SBOM (POAM-005); CVD and monitoring (POAM-006); call-back rule; design-freeze risk update; release pipeline and key service (POAM-003); per-device credentials (POAM-004); offboarding (POAM-012); lab workstations (POAM-010); contractor security terms (POAM-011); log review; restore tests (POAM-009); contingency plan; clinical capacity and recovery targets |

**Response to the partner hospital:** send this summary, the readiness checklist, the POA&M, and the P03 roadmap by 2026-10-30; name the Head of Engineering as security contact; commit to an updated self-assessment at design freeze and a SOC 2 Type 1 report on the production service before the clinical pilot.

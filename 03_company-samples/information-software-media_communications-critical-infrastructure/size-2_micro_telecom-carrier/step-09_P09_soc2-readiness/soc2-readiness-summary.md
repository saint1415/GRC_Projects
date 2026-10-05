# SOC 2 Readiness Summary: Cris Santos Company | Communications | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural fiber broadband and voice carrier) |
| Tier / Vertical | Micro / Communications |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the community bank branch's vendor questionnaire |
| Part B | BSS vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-25 by the Office Manager with the independent consultant; approved by the Owner and General Manager 2026-08-31 |

## 1. Why SOC 2 for this organization
A micro carrier is **not** a SOC 2 service organization in the usual sense. It carries traffic; it does not process data that its customers rely on for their own controls. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a questionnaire.** The community bank branch in town buys one of the company's 6 dedicated internet circuits. Under its own vendor management program, the bank sent a security and availability questionnaire in July 2026 organized around the Trust Services Criteria. The company will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-09-30, and the town hall has said it will ask the same questions at its contract renewal.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. The bank's questionnaire instructions accept a self-assessment from a vendor of this size.

**B. Relying on the BSS vendor.** The BSS vendor carries most of the company's inherited controls for customer data (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls. Reviewing it each year is part of vendor oversight (SA-9) and part of the "reasonable measures" the CPNI rules require (47 CFR 64.2010(a)).

**Why Availability and not another category.** The bank buys a circuit with a 99.9% monthly commitment, and its questions are about whether the circuit stays up and whether the company can recover. The BIA (P05) shows that availability is where the company's structural weakness lies (one middle-mile circuit). Confidentiality of customer data is covered under the Security criteria and the CPNI rules. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** fiber broadband for about 1,385 subscribers, interconnected VoIP for about 440 numbers, and 6 dedicated internet circuits.
- **Infrastructure and software:** the Network Operations and Customer Billing Platform (SSP, P02): the BSS and portal, the hosted voice platform account, the OLTs and edge router, the hut servers, the monitoring service, office IT, and the cloud backup.
- **People:** 7 employees, the MSP, and the network engineering consultant.
- **Data:** CPNI and the customer account record, network configurations, billing data.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 18 | 9 | 0 |
| Availability (A1, 3) | 0 | 2 | 1 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: security and compliance lead designated in writing; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access to the hut and the office network closet

**Not ready:**
- CC1.4: no security or CPNI training
- CC3.4: the AI assistant went live with no review
- CC6.1, CC6.2, CC6.3: shared network logins; no MFA on the voice platform and VPN; no access approval or removal process
- CC7.1, CC7.2: no vulnerability monitoring or security monitoring
- CC7.5 and A1.3: recovery unproven; configuration backups only in the hut
- CC8.1: router and OLT changes have no written approval or record

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| BSS vendor SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| BIA summary and capacity graphs for the middle-mile and OLTs | CC9.1, A1.1 | Yes | Monthly capacity snapshot |
| MSP monthly report (patching, antivirus, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Router and OLT firmware records and advisory review log | CC7.1 | No | Monthly from 2026-09 |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Network change log | CC8.1 | No | From 2026-10 |
| Restore test records | CC7.5, A1.3 | One (P07) | Twice a year |
| Training records (security and CPNI) | CC1.4, CC2.2 | No | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the BSS vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception (a missed quarterly access review for vendor support staff), remediated.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 1 hour **meet the BIA** for customer service and billing (BP-04 RTO 8 h, RPO 1 h).
- **Controls the company must run.** The report lists complementary user entity controls, including API credential protection and the choice of customer authentication options. Four are open gaps at the company: API key scope and storage (POAM-004), customer authentication options (POAM-005), audit report review (POAM-007), and staff removal (POAM-001). **The vendor's controls protect the company only once those gaps are closed.**
- **The AI assistant is not covered.** It launched after the report period. The company relies on the P10 conditions until the next report.
- **Follow-ups:** request a bridge letter to 2026-09-30; ask for the assistant's subservice organizations and data-use terms; ask for 24-hour incident notice and CPNI confidentiality terms at renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC6.2, CC6.6 | Acknowledgments; questionnaire response; onboarding checklist (POAM-001); router upgrade (POAM-012); named consultant login (POAM-002) |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.3, CC6.5, CC6.7, CC6.8, CC7.1-CC7.5, CC8.1, CC9.1, CC9.2, A1.1-A1.3 | Monthly oversight notes; CPNI and security training (POAM-006); inventory; change checklist and change log; MFA and named accounts (POAM-001, POAM-003); segmentation and alerts (POAM-013); advisory review (POAM-010); log review (POAM-007); off-site backup and restore tests (POAM-008); contingency plan; vendor reviews (POAM-011); diverse circuit decision |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk assessment |

**Response to the bank:** send this summary, the readiness checklist, the BIA summary, and the POA&M by 2026-09-30, name the Office Manager as security contact, and commit to an updated self-assessment in April 2027. Be plain about the single middle-mile circuit: it is the honest answer to the bank's availability questions, and the diverse-path decision is due with the 2027 budget.

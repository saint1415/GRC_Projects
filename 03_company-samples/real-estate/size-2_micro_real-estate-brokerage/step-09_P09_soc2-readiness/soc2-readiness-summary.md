# SOC 2 Readiness Summary: Cris Santos Company | Real Estate | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management) |
| Tier / Vertical | Micro / Real Estate and Rental and Leasing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Brokerage readiness self-assessment (`soc2-readiness.csv`), used to answer a relocation management company's broker network questionnaire |
| Part B | Transaction platform vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-19 by the Office Manager with the independent consultant; updated with policy approvals and approved by the Broker-owner 2026-09-14 |

## 1. Why SOC 2 for this organization
A 7-person brokerage is **not** a SOC 2 service organization. It represents buyers, sellers, and owners; it does not run a system that other businesses rely on for their own controls. The Trust Services Criteria are used for two practical reasons.

**A. Answering a questionnaire.** In July 2026 a relocation management company invited the brokerage to join its broker network, which refers employees who are moving for work. The network sends the brokerage transferees' names, contact details, and relocation budgets, and its questionnaire follows the Trust Services Criteria for security and confidentiality. The brokerage will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-10-15.

**The brokerage will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the brokerage's controls were defined in September 2026. An audit would also cost more than a year of the referral fees in question. The questionnaire accepts a self-assessment with a remediation plan.

**B. Relying on the transaction platform vendor.** The vendor carries most of the inherited controls for the TMCC (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for them, and reviewing it each year is part of vendor oversight (POL-02 A.5; SA-9).

**Why Confidentiality and not another category.** The relocation company's concern is what happens to its transferees' information, which is confidentiality. Availability is covered internally by the BIA (P05) and was not asked about. Processing Integrity does not fit: the brokerage processes no transactions for others. Privacy was not requested; personal information duties come from Fla. Stat. 501.171 and the FCRA, handled in P03.

## 2. System description (scope)
- **Services:** residential buyer and seller representation; property management for about 85 homes; relocation referrals once accepted into the network.
- **Infrastructure and software:** the TMCC (SSP, P02): transaction platform, productivity suite, e-signature, 9 company devices, office network, and the email backup; online banking and the property management platform as interconnected systems.
- **People:** 7 employees, about 22 contractor agents, and the MSP.
- **Data:** client identity documents, proof of funds, contracts, deposit and payout instructions, screening reports, and referral data.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 16 | 11 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: security lead designated in writing; roles defined
- CC3.1, CC3.2, CC3.3: risk criteria set; 2026 risk assessment done; **fraud risk is the center of it** (diverted wires and payout changes)
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked and reviewed monthly

**Not ready:**
- CC1.4: no security training after hire; agents untrained
- CC2.1: no inventory of systems and where confidential data lives
- CC6.1, CC6.2, CC6.3: agents without MFA, a shared administrator, no access approvals, late removal of departing agents
- CC6.5 and C1.2: confidential information is never disposed of
- CC6.7: wire instructions and ID copies sent as email attachments
- CC7.1, CC7.2, CC7.3: no scanning, monitoring, or event triage before September 2026
- CC7.5: recovery unproven (backup never restored)

## 4. Evidence inventory
The questionnaire asks for evidence. What the brokerage can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3, C1.1 | Yes | Signed acknowledgments (2026-10 to 2026-12) |
| Risk register summary (P01) and assessment summary (P07) | CC3.1-CC3.3, CC4.1, CC4.2 | Yes | Monthly POA&M review notes (from 2026-09) |
| Transaction platform vendor SOC 2 review | CC9.2 | Yes | Bridge letter (2026-10) |
| MFA report showing every account enrolled | CC6.1 | No | After POAM-003 (2026-10-31) |
| Offboarding checklists and monthly user reconciliations | CC6.2, CC6.3 | No | From 2026-10 |
| Alert review checklist | CC7.2 | No | Weekly from 2026-10 |
| Restore test records | CC7.5 | No | Quarterly from 2026-09 |
| Training and phishing simulation records | CC1.4, CC2.2 | New-hire video only | From 2026-11 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |
| Purge record | CC6.5, C1.2 | No | January 2027 |

## 5. Findings from the transaction platform vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-05-31. One exception (2 of 40 sampled changes lacked documented approval), remediated.
- **Availability and confidentiality:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the BIA** for BP-03 (RTO 8 h, RPO 4 h). Customer data is encrypted and deleted on request after contract end.
- **Controls the brokerage must run.** The report lists complementary user entity controls: user provisioning and timely removal, MFA for all users, restricting file visibility, reviewing activity, and protecting credentials on user devices. **Four are open gaps at the brokerage** (POAM-001, POAM-003, POAM-005). The vendor's controls protect client files only once those gaps are closed.
- **Follow-ups:** request a bridge letter to 2026-09-30; ask whether client document sharing links expire and can be revoked.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q4 (by 2026-12-31) | CC1.1, CC1.5, CC2.1, CC2.2, CC2.3, CC5.1, CC5.2, CC5.3, CC6.1, CC6.2, CC6.3, CC6.4, CC6.6, CC6.7, CC7.1, CC7.2, CC7.3, CC7.4, CC7.5, CC8.1, CC9.1, C1.1 | Questionnaire response (2026-10-15); acknowledgments and agent addendum; inventory; MFA and named administrators (POAM-002, POAM-003); offboarding (POAM-001); forwarding block and alerts (POAM-004, POAM-005); scan; tabletop; backup scope and restore tests (POAM-006, POAM-007); contingency plan; closet lock |
| 2027 Q1 | CC1.4, CC6.5, CC6.8, CC9.2, C1.2 | Office Manager security course; January purge; device rules and detection at MSP renewal; vendor reviews (POAM-009) |
| 2027 Q3 | CC1.2, CC3.4 | First annual report to the Broker-owner; July 2027 risk reassessment |

**Response to the relocation company:** send this summary, the readiness checklist, and the POA&M by 2026-10-15, name the Office Manager as security contact, and commit to an updated self-assessment in April 2027.

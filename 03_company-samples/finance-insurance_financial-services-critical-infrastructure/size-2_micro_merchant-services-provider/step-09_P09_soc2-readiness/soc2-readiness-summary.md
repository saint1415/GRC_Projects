# SOC 2 Readiness Summary: Cris Santos Company | Financial Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (merchant services provider, an ISO) |
| Tier / Vertical | Micro / Financial Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer two questionnaires |
| Part B | CRM vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-21 by the Operations Manager; approved by the Owner 2026-08-31 |

## 1. Why SOC 2 for this organization
The company **is a small service organization**: it provides sales, support, gateway administration, and onboarding services to merchants and to its processor partner. But **PCI DSS, not SOC 2, is the assurance its customers rely on** for card data. The processor partner, the sponsor bank, and the card brands require the annual SAQ D for Service Providers and AOC, and SOC 2 does not replace it (the vertical's assurance alternatives are PCI DSS validation and, for financial reporting controls, SOC 1).

The Trust Services Criteria are used here for two practical reasons:

**A. Answering two questionnaires.**
- The processor partner's annual ISO risk review asks how the company protects merchant owner information and runs its security program, beyond card data.
- A regional restaurant association that refers members to the company sent a vendor security questionnaire in July 2026, due 2026-09-30. Its questions follow the Trust Services Criteria.

The company will answer both with this self-assessment, the POA&M (P07), the 2026 AOC when signed, and a named security contact.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. An audit would also cost far more than either requester asked for. Both accepted a self-assessment.

**B. Relying on the CRM vendor.** The CRM holds every merchant owner's Social Security number and bank details. Its SOC 2 Type 2 report is the evidence for the controls the company inherits there, and reviewing it each year is part of vendor oversight under 16 CFR 314.4(f) and SA-9. (The processor partner offers a PCI DSS AOC rather than a SOC 2 report; that AOC is reviewed under PCI DSS 12.8, P03 G-075.)

**Why Confidentiality and not another category.** The requesters asked how merchant owner information and merchant business details are protected and disposed of. Availability was not requested, and merchants can keep trading when the company is down because the processor partner runs authorization (P05). Processing Integrity does not fit: the company does not process transactions. Privacy notices and consent are given by the processor partner and merchants.

## 2. System description (scope)
- **Services:** merchant sales and onboarding, help desk, backup keyed entry (until 2026-10-15), gateway administration, terminal swaps, chargeback support.
- **Infrastructure and software:** the Merchant Payments Platform (SSP, P02): gateway console, partner portal, CRM, productivity suite, phone system, laptops, office network, website, spare terminals, suite backup.
- **People:** 7 employees, 6 outside agents, and the MSP.
- **Data:** merchant owner information, merchant business information, card data in transit during keyed entry.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.
- **Subservice organizations:** the processor partner, the CRM vendor (Part B), the phone vendor, the suite vendor, the web hosting provider, and the MSP.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 19 | 8 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |
| **Total (61)** | **6** | **20** | **9** | **26** |

**Ready:**
- CC1.3: Qualified Individual and PCI DSS lead designated in writing
- CC3.1 and CC3.2: objectives, risk tolerance, and a written risk assessment (P01)
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked in the POA&M
- CC6.4: physical access (locked office and terminal cabinet; vendor data centers covered by their reports)

**Not ready:**
- CC2.1: no single inventory of systems, data stores, and payment page content
- CC3.4: the 2025 phone system go-live was never assessed (it brought card data into recordings)
- CC6.2 and CC6.3: access granted and removed without a process; every staff console account can log in as any merchant
- CC6.7: applications with Social Security numbers arrive by plain email
- CC7.2 and CC7.3: no log review, alerting, or incident log
- CC8.1: payment page and fraud filter changes made with no approval or record
- C1.2: no retention schedule for merchant files

These are the same weaknesses as the High risks in P01 and the High POA&M items in P07. Fixing them for the 2026 SAQ also fixes them for these questionnaires.

## 4. Evidence inventory
What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments from staff and agents (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| 2025 AOC and ASV scan reports | CC4.1, CC7.1 | Yes (2025 AOC to be replaced by the accurate 2026 AOC by 2026-10-30) | Quarterly |
| CRM vendor SOC 2 review | CC9.2, C1.1 | Yes | Bridge letter (2026-10) |
| Console MFA report | CC6.1 | Shows the gap today | After 2026-09-15 |
| Account reconciliation and access review records | CC6.2, CC6.3 | No | Monthly from 2026-10; six-monthly from 2027-03 |
| Console alert digests and weekly log review checklists | CC7.2 | No | From 2026-10 |
| Payment page script inventory and change log | CC8.1, CC6.8 | No | From 2026-09 |
| Quarterly PCI review checklists | CC1.2, CC4.1 | No | From 2026-10 |
| Restore test records | CC7.5 | No | Quarterly from 2026-10 |
| Retention purge records | C1.2 | No | Quarterly from 2026-12 |
| Training and phishing simulation records | CC1.4, CC2.2 | Video list only | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the CRM vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception (a late quarterly access review for vendor support staff), remediated.
- **Confidentiality and availability:** Confidentiality is in the report's scope. The stated RTO of 8 hours and RPO of 1 hour **meet the BIA** for onboarding (BP-04: RTO 48 h, RPO 24 h).
- **Controls the company must run.** The report lists complementary user entity controls: user provisioning and removal, MFA enforcement, role and sharing settings, and customer-side retention. Two are open gaps at the company: removal (POAM-001, POAM-003) and retention (P03 G-091). **The vendor's controls protect the company only once those gaps are closed.**
- **Follow-ups:** request a bridge letter to 2026-09-30; ask for 24-hour incident notice at renewal; confirm that the secure upload link the company will use for applications is inside the report's scope (it is listed as the "upload portal").

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.1, CC3.3, CC6.1, CC6.2, CC6.3, CC7.3, CC8.1 | Acknowledgments; inventory; call-back rule; console MFA and roles (POAM-001, POAM-002); offboarding checklist (POAM-003); incident log; change log; questionnaire response to the association |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.2, CC2.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.5, CC6.6, CC6.7, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC9.1, CC9.2, C1.1, C1.2 | Quarterly PCI review; training (POAM-004); merchant responsibility summary; scope confirmation; keyed entry stopped; CRM upload link (POAM-012); EDR; internal scans (POAM-010); log review (POAM-005); tabletop (POAM-009); restore test (POAM-007); contingency plan; service provider list and contracts (POAM-011); retention purge |

**Response to the restaurant association:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Operations Manager as security contact, and send the 2026 AOC when signed. **Response to the processor partner's ISO risk review:** the same package with the accurate 2026 SAQ and AOC by 2026-10-30.

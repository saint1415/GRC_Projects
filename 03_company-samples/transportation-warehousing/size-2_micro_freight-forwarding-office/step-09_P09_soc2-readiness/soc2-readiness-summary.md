# SOC 2 Readiness Summary: Cris Santos Company | Transportation and Warehousing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (freight forwarding and customs brokerage office) |
| Tier / Vertical | Micro / Transportation and Warehousing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer CTPAT importer clients' business partner security questionnaires |
| Part B | Customs platform vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-27 by the Office and Compliance Manager with the independent consultant; approved by the owner 2026-08-31 |

## 1. Why SOC 2 for this organization
A 7-person forwarding and brokerage office does provide services to other businesses, but none of its clients has asked for a SOC 2 report, and no customs or FMC rule requires one. The Trust Services Criteria are used here for two practical reasons.

**A. Answering CTPAT client questionnaires.** Six importer clients are CTPAT partners. CTPAT is voluntary (N48-49-R05), but its minimum security criteria include cybersecurity and business partner criteria, so partners send their service providers yearly security questionnaires. The largest (about 12% of revenue) is due 2026-10-31. Its questions on access, incident notice, data protection, and confidentiality of shipment and client data line up with the Security and Confidentiality criteria. The company will answer with this self-assessment, the POA&M (P07), and a named security contact.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most controls were defined in August 2026. An audit would cost a large share of a year's profit and no client has asked for one.

**B. Relying on the customs platform vendor.** The platform holds every entry, POA, and shipment file and carries most inherited controls (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls, and reviewing it each year is part of vendor oversight (SA-9) and of showing that client records stay confidential and in the United States (19 CFR 111.23(a), 111.24).

**Why Confidentiality and not Availability.** Client records are confidential by regulation (111.24), and the CTPAT questionnaires ask how shipment and client information is protected. Availability matters to clients too, but it is managed through the BIA (P05) and the standby broker arrangement, and clients did not ask about it. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** import entries and ISFs, export EEI filings, ocean forwarding for about 180 clients.
- **Infrastructure and software:** the Core Brokerage SaaS Stack (SSP, P02): customs platform, productivity suite, accounting SaaS, bank portal, suite backup, 9 computers and a printer, office network.
- **People:** 7 employees and the MSP.
- **Data:** client customs records (including importer identification numbers), payment details, employee data.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 7 | 18 | 8 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security Coordinator and CBP recordkeeping contact designated; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access (locked suite and cabinets; vendor data centers under SOC 2)
- CC6.6: firewall, separated guest Wi-Fi, MFA on SaaS

**Not ready:**
- CC2.1: no inventory or importer number data map
- CC6.2 and CC6.3: access granted and removed without a process (the former Entry Writer; shared logins)
- CC7.1, CC7.2, CC7.3: no vulnerability scanning, monitoring, or incident records
- CC7.5: recovery unproven (the same gap as risk R-006)
- CC8.1: vendors and the MSP change settings and features without the company's approval (the AI feature)

## 4. Evidence inventory
CTPAT clients ask for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Customs platform vendor SOC 2 review | CC9.2, C1.1 | Yes | Bridge letter (2027-01) |
| Incident notice commitment to clients (72 hours) and the CBP notice step | CC2.3, CC7.4 | Yes (P08) | Template finished (2026-10) |
| MSP monthly report (patching, antivirus, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Restore and records retrieval test records | CC7.5, C1.1 | No | Quarterly from 2026-09; retrieval yearly from 2026-10 |
| Training and phishing simulation records | CC1.4, CC2.2 | No | From 2026-10 |
| Shredding and wipe certificates | CC6.5, C1.2 | Shredding yes; wipe no | Every disposal |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the customs platform vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-06-30. One exception (a late quarterly access review of vendor support staff), remediated.
- **Data location:** production and backup data in U.S. regions, matching the contract and 111.23(a).
- **Availability:** the vendor's RPO of 1 hour meets the BIA; its **RTO of 8 hours does not meet the 4-hour target** for entries and ISFs (P05 finding 1; P01 R-007).
- **Controls the company must run.** The report lists complementary user entity controls: user provisioning and removal, role assignment, keeping MFA enabled, review of user access and export reports, and control of exported data. Two are open gaps at the company: removal (POAM-001, POAM-002) and review (POAM-010). **The vendor's controls protect the company only once those gaps are closed.**
- **The AI feature is outside the report.** The document capture and classification feature released in 2026-04 is not described, and no AI model provider is listed as a subservice organization. That is a key input to P10.
- **Follow-ups:** bridge letter by 2027-01-31; AI feature and model provider details; incident notice within 24 hours (to protect the company's 72-hour CBP clock); opt-in for new features that process client data.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC6.1, CC6.2, CC6.5, CC7.3, CC7.5, C1.2 | Acknowledgments; entries@ conversion and MFA on MSP-held logins (POAM-001, POAM-003); onboarding checklist; wipe confirmation (POAM-011); incident log; first restore test (POAM-008); 163.5 notice to CBP |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.2, CC2.3, CC3.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.3, CC6.7, CC6.8, CC7.1, CC7.2, CC7.4, CC8.1, CC9.1, CC9.2, C1.1 | Questionnaire response by 2026-10-31; monthly oversight notes; training (POAM-005); inventory and data map; client terms clause; vendor change review; termination process (POAM-002); encryption rule; EDR and impersonation protection (POAM-012); scans; log review (POAM-010); tabletop; contingency plan and standby broker; MSP review (POAM-009); suite retention policy |

**Response to the CTPAT client:** send this summary, the readiness checklist, and the POA&M by 2026-10-31, name the Office and Compliance Manager as security contact, commit to notify the client within 72 hours of any incident affecting its records, and offer an updated self-assessment in April 2027.

# SOC 2 Readiness Summary: Cris Santos Company | Accommodation and Food Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 38-unit roadside motel) |
| Tier / Vertical | Micro / Accommodation and Food Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Target report | None. No SOC 2 examination is planned |
| Part A | Readiness self-assessment (`soc2-readiness.csv`), used to answer the largest crew client's vendor security questionnaire |
| Part B | PMS vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 to 2026-08-21 by the Assistant Manager with the independent consultant; approved by the Owner-Manager 2026-08-31 |

## 1. Why SOC 2 (or an alternative) for this organization
**The motel is not a SOC 2 service organization.** It rents rooms to travelers and work crews. It does not run systems or services for other businesses whose own controls depend on it.

**Its payment assurance is PCI DSS validation.** The vertical overlay names PCI DSS validation for card payments as the alternative to SOC 2, and that is what the acquirer requires: SAQ P2PE plus SAQ A for 2026 after the redesign (P03). A crew company that asks whether its card is safe should get the motel's attestation of compliance once it is signed.

The Trust Services Criteria still appear here for two practical reasons:

**A. Answering a questionnaire.** In July 2026 the motel's largest crew client, a regional utility line contractor (about 18% of room-nights), sent a vendor security questionnaire. It asks how the motel protects the company's corporate card data and its crew rosters (names, phone numbers, and the employee ID numbers the company sends for room assignments), who can see them, and how they are disposed of. Its questions follow the Trust Services Criteria. The response is due 2026-09-30. The client's procurement team accepts a self-assessment with a remediation plan from small lodging vendors; it does not require a SOC 2 report.

**B. Relying on the PMS vendor.** The PMS vendor carries most of the motel's inherited controls (P02 section 10.2). Its SOC 2 Type 2 report, together with its PCI DSS AOC, is the evidence for those controls. Reviewing it each year is part of service provider management (PCI DSS requirement group 12.8; SA-9).

**Why Confidentiality and not another category.** The client's questions are about keeping its card data and rosters confidential and disposing of them. Availability matters to the motel but is covered by the BIA (P05), and the client did not ask about it. Processing Integrity has no client commitment. Guest privacy duties come from the FTC Act and Florida law, not a SOC 2 commitment.

## 2. System description (scope)
- **Services:** lodging for transient guests and work crews, with crew billing by card or invoice.
- **Infrastructure and software:** the Motel Property Management and Point-of-Sale System (SSP, P02): cloud PMS, payment gateway and P2PE terminals, productivity suite, cloud backup, 5 company devices, the motel network, the lock system, and CCTV.
- **People:** 7 employees, the MSP, and key vendors.
- **Data:** card data (on the front desk PC and in email until the redesign), crew rosters, guest profiles and ID scans, stay history, workforce data.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 14 | 13 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: the Security and Privacy Lead is designated in writing; roles are defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access (24-hour front desk, locked back office, vendor data centers under SOC 2)

**Not ready:**
- CC1.4: no security training
- CC2.1 and CC2.3: no inventory or scope document; a false statement about card storage on the website
- CC3.3: fraud risk only partly assessed
- CC6.1, CC6.2, CC6.3, CC6.7: shared logins, no MFA for front office users, no access approvals or reviews, card forms and rosters received by ordinary email
- CC7.1, CC7.2, CC7.3: no vulnerability scanning, monitoring, or incident records
- CC7.5: recovery of the lock system unproven
- CC8.1: no change management
- C1.2: no retention schedule, so crew card forms and rosters are never disposed of

## 4. Evidence inventory
The questionnaire asks for evidence. What the motel can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3, C1.1 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| PMS vendor SOC 2 review and AOCs (PMS vendor, gateway) | CC9.2 | Yes | Bridge letter (2026-10) |
| P2PE solution listing and terminal inspection log | CC6.7, CC6.8 | Listing yes; log no | Weekly from 2026-09 |
| MSP monthly report (patching, antivirus, backup) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Account reconciliation and weekly log review checklists | CC6.2, CC6.3, CC7.2 | No | From 2026-09 |
| Purge and shredding records for card forms | C1.2, CC6.5 | No | From 2026-09 |
| Restore test records, including the lock database | CC7.5 | No | Quarterly from 2026-10 |
| Training records | CC1.4, CC2.2 | No | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |
| 2026 attestation of compliance (SAQ P2PE plus SAQ A) | CC6.7, CC9.2 | No | By 2026-12-31 |

## 5. Findings from the PMS vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception (a missed quarterly access review for vendor support staff), remediated.
- **Scope:** Security and Availability. Confidentiality is not in the report, so the motel relies on the Security criteria and the contract's deletion terms for the client's confidentiality questions. The card vault is covered by the vendor's **PCI DSS AOC (2026-02)**, and card processing by the gateway's AOC (2026-01). The motel keeps and checks all three.
- **Availability:** the stated RTO of 4 hours and RPO of 15 minutes meet the BIA for reservations and payments (BP-02, BP-03) but **not the 2-hour RTO for check-in (BP-01)**. The paper check-in kit and offline key encoding cover the difference.
- **Controls the motel must run.** The report lists five complementary user entity controls: timely removal of users, least-privilege roles, MFA for all users, review of user activity reports, and protection of workstations that access the PMS. **Every one of them is an open gap at the motel** (POAM-001, POAM-006, POAM-004, POAM-009, POAM-007). The vendor's controls protect guest data only once those gaps are closed.
- **Follow-ups:** request a bridge letter to 2026-09-30; turn on the purge settings to match POL-04 4.8; ask for 24-hour notice of suspected incidents at renewal (Florida's 10-day third-party agent duty applies in any case).

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC2.3, CC6.2 | Acknowledgments; corrected privacy statement; questionnaire response naming the Assistant Manager as security contact; onboarding checklist (POAM-001) |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.3, CC6.5, CC6.6, CC6.7, CC6.8, CC7.1-CC7.5, CC8.1, CC9.1, CC9.2, C1.1, C1.2 | Monthly oversight notes; training (POAM-011); inventory (POAM-014); redesign and purge of card data (POAM-002); named accounts and MFA (POAM-001, POAM-004); display permission (POAM-006); lock vendor terms (POAM-003); EDR (POAM-007); scans (POAM-008); log review (POAM-009); restore tests (POAM-010); tabletop (POAM-012); MSP review (POAM-013); retention schedule; contingency plan; failover router |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk assessment |

**Response to the crew client:** send this summary, the readiness checklist, and the POA&M by 2026-09-30; state plainly that card forms are being retired and replaced by pay-by-link by 2026-11-30, and that rosters will be deleted 30 days after each crew's last checkout; send the 2026 attestation of compliance once signed; commit to an updated self-assessment in April 2027.

# SOC 2 Readiness Summary: Cris Santos Company | Accommodation and Food Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 140-room beachfront hotel) |
| Tier / Vertical | Small / Accommodation and Food Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only, as an internal benchmark |
| Target report | None. No SOC 2 examination is planned |
| Part A | Security-only self-benchmark (`soc2-readiness.csv`) |
| Part B | PMS vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager with the Controller |

## 1. Why SOC 2 (or an alternative) for this organization
**The hotel is not a SOC 2 service organization.** It sells rooms, food, and events to guests. It does not run systems or services for other businesses whose controls would depend on it. No customer, group client, or partner has asked the hotel for a SOC 2 report, and none is expected.

**Its assurance mechanism is PCI DSS validation.** The vertical overlay names PCI DSS validation for card payments as the typical alternative, and that is what the acquirer requires: SAQ D for MID-1 and SAQ P2PE for MID-2 for 2026 (P03). Corporate clients that book group stays sometimes ask for a PCI attestation of compliance, not a SOC 2 report.

SOC 2 still appears here for two reasons:

**A. Security-only self-benchmark.** The Trust Services Criteria cover governance topics that PCI DSS touches only lightly: board oversight (CC1.2), fraud risk (CC3.3), change management across all systems (CC8.1), and business disruption (CC9.1). The General Manager asked for a benchmark against the Security category to show where the program stands beyond card data. The other categories are marked N/A: availability is handled in the BIA (P05), confidentiality in POL-04 and PCI DSS, processing integrity has no customer commitment, and privacy duties come from the FTC Act and Florida law, not a SOC 2 commitment.

**B. Third-party risk management.** The hotel depends on its PMS vendor for most controls over guest data and for the availability of check-in. The vendor's SOC 2 Type 2 report is reviewed every year alongside its PCI DSS attestation (POL-01 4.10; PCI DSS 12.8.4).

## 2. System description (scope)
- **Services:** lodging, food and beverage, and events for guests, with payments under two merchant accounts.
- **Infrastructure and software:** the Property Management and Point-of-Sale Platform (SSP, P02).
- **People:** 60 employees, contracted staff supplied by the staffing company, the MSP, and key vendors.
- **Data:** card data (in vendor services and on front office PCs today), guest profiles and ID scans, stay history, and workforce data.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 18 | 11 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles are designated in writing
- CC3.1 and CC3.2: objectives, tolerance, and risk assessment are done
- CC4.2: deficiencies are tracked in the POA&M

**Not ready:**
- CC2.1: no reliable inventory or PCI scope
- CC2.3: the published privacy policy is inaccurate about card storage
- CC3.3: fraud risk not assessed (refund abuse, folio adjustments, insider card theft)
- CC6.1, CC6.3, CC6.6, CC6.7: MFA gaps, excess card-display rights, vendor remote access, card data in email and chat
- CC7.1, CC7.2: no vulnerability scanning or security monitoring
- CC7.5: recovery of the lock server is unproven
- CC8.1: no change management

## 4. Findings from the PMS vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months to 2026-03-31. One exception (a missed quarterly access review for vendor support staff), remediated.
- **Scope:** Security and Availability. The card vault is covered by the vendor's **PCI DSS AOC (2026-03)**, not by the SOC 2 report. The hotel keeps and checks both.
- **Availability:** the stated RTO of 4 hours and RPO of 15 minutes meet the BIA for payments and reservations (BP-03, BP-04) but **not the 2-hour RTO for check-in (BP-01)**. Paper arrivals and emergency key cards cover the difference.
- **Controls the hotel must run.** The report lists controls the customer must operate for the vendor's controls to work (complementary user entity controls): timely removal of users, least-privilege roles, MFA or single sign-on, review of user activity reports, and protection of workstations that access the PMS. **Every one of them is an open gap at the hotel** (POAM-001, POAM-002, POAM-003, POAM-015, POAM-009). The vendor's controls protect guest data only once those gaps are closed.
- **Follow-ups:**
  - Obtain a bridge letter through 2026-06-30.
  - Put RTO and RPO commitments in the contract.
  - Negotiate incident notice fast enough for the Visa 3-day clock, and in any case within the 10 days that Fla. Stat. 501.171(6)(a) allows a third-party agent.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.3, CC6.6, CC6.7, CC2.3, CC7.1, CC7.3-7.4 | Account removals, vendor session approvals, mailbox purge record, revised privacy policy, ASV and internal scan reports, tabletop report |
| 2027 Q1 | CC6.1, CC6.8, CC7.2, CC8.1, CC2.1 | MFA enrollment report, EDR alerts and tickets, segmentation test, change log, PCI scope document |
| 2027 Q2 | CC7.5, CC9.1, CC3.3, CC1.2 | Lock server restore test, IT hurricane plan, updated risk assessment with fraud scenarios, owner review minutes |

**Use of this benchmark:** internal only. It is reported to the majority owner with the POA&M (P07) and repeated in 2027 Q2. It is not a SOC 2 report and must not be described to guests or partners as one.

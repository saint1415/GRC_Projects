# SOC 2 Readiness Summary: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer) |
| Tier / Vertical | Small / Mining, Quarrying, and Oil and Gas Extraction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only, as a self-benchmark |
| Target report | None. The company is not a service organization and does not plan a SOC 2 examination |
| Part A | Security-only self-benchmark (`soc2-readiness.csv`) |
| Part B | Review of the production accounting vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager; approved by the CFO, 2026-08-31 |

## 1. Why SOC 2 for this organization
**The company is not a SOC 2 service organization.** SOC 2 reports on controls at an organization that provides services to other businesses. Cris Santos Company produces and sells crude oil and associated gas. Its customers (the crude purchaser and the gas gathering company) buy a commodity at the lease; they do not rely on the company's systems to deliver a service to them. The vertical overlay names no sector assurance alternative to SOC 2, and no customer or regulator has asked for one.

**Two relationships come closest, and neither calls for a SOC 2 report:**
- As operator, the company does joint interest billing and revenue distribution for 9 non-operating working interest owners. That work affects the partners' financial reporting, which is the subject of SOC 1 reports, not SOC 2. The joint operating agreements already give partners audit rights over the company's accounts.
- The company pays about 2,300 royalty owners. They are individuals, not business customers relying on a system description.

**So P09 is built in two parts:**

**A. Security-only self-benchmark.** The reserve-based lender and two non-operating partners sent security questionnaires in 2026 after sector ransomware news. Their questions follow the Security (common criteria) themes of the Trust Services Criteria. The company answers with this self-benchmark and its remediation dates, alongside the P03 CSF 2.0 gap analysis. The other four categories are marked N/A with a reason in `soc2-readiness.csv`:
- **Availability:** the company makes no availability commitments to customers. Field availability is handled by the BIA (P05) and covered under CC7.5 and CC9.1.
- **Confidentiality:** covered for owner and reservoir data by POL-04 and P03, not by customer commitments.
- **Processing Integrity:** the company processes no transactions for customers. Allocation and payment integrity sit with the production accounting vendor and are checked in Part B.
- **Privacy:** no consumer customers. Personal information duties come from Fla. Stat. 501.171 (P03).

**B. Third-party risk management.** The company relies on the production accounting vendor for royalty owner data, allocations, and payments, and inherits several controls from it (P02, P04). The vendor's SOC 2 Type 2 report is the evidence for those controls. The company reviews it every year (SA-9; POL-01 4.9).

## 2. System description (scope)
- **Services:** oil and gas production and sale; production accounting, royalty distribution, and joint interest billing.
- **Infrastructure and software:** the Field SCADA and Production Accounting System (SSP, P02), the corporate network, and the SaaS applications.
- **People:** 250 employees, the SCADA integrator, and the production accounting vendor.
- **Data:** production volumes and run tickets, royalty owner and employee personal information, reservoir data (trade secret), and SCADA configurations.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 20 | 8 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

In scope: 33 criteria (5 Ready, 20 Partially ready, 8 Not ready). Out of scope: 28 criteria.

**Ready:**
- CC1.3: security roles designated in writing, including the OT security lead
- CC3.1 and CC3.2: objectives, risk tolerance, and the 2026 risk assessment
- CC3.3: fraud risks (payment redirection and run ticket falsification) are in the register
- CC4.2: deficiencies tracked in the POA&M with owners and dates

**Not ready:**
- CC6.1 and CC6.3: integrator access without MFA, shared SCADA accounts, late access removal
- CC6.6: internet-exposed modems and the cloud VPN path into SCADA
- CC7.1 and CC7.2: no OT vulnerability management and no 24x7 or OT monitoring
- CC7.5: no isolated backups or restore tests (the same gap as risk R-003)
- CC8.1: no change control for SCADA or controller logic
- CC9.2: no supplier security terms or process

## 4. Findings from the production accounting vendor report (Part B)
- **Opinion:** Type 2, unqualified, covering Security, Availability, Confidentiality, and Processing Integrity. One exception (a late quarterly access review of vendor support staff), remediated.
- **Availability:** the vendor's stated RTO of 24 hours and RPO of 1 hour **meet the BIA** for production accounting (BP-06: RTO 72 h, RPO 24 h).
- **Controls the company must run.** The report lists complementary user entity controls. Two are open gaps at the company: user removal (POAM-014) and verification of owner bank detail changes (P01 R-007). **The vendor's controls protect owner data and payments only once those gaps are closed.**
- **Incident notice:** the vendor commits to 72 hours after confirming an incident. Florida law separately requires a third-party agent to notify the company within 10 days of determining a breach (Fla. Stat. 501.171(6)). The contract should add the 72-hour commitment and breach cooperation at renewal (POAM-020).
- **Follow-ups:** obtain a bridge letter through 2026-06-30; get the assurance summary for the carved-out check and ACH provider.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1, CC6.2, CC6.3, CC6.6, CC7.3, CC7.4, CC2.3 | Jump host session records, termination tickets, access reviews, modem configuration records, tabletop report |
| 2027 Q1 | CC7.1, CC7.2, CC7.5, CC8.1, CC9.2, CC5.2 | OT sensor alerts, MDR tickets, restore test records, OT change records, amended integrator contract, OS upgrade records |
| 2027 Q2 | CC1.2, CC1.5, CC3.4, CC4.1 | Owner security reports, job descriptions, quarterly metrics |

**Response to the lender and partners:** send this summary, the readiness checklist, and the POA&M (P07). Commit to an updated self-benchmark in April 2027.

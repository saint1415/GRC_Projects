# SOC 2 Readiness Summary: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer, one field) |
| Tier / Vertical | Micro / Mining, Quarrying, and Oil and Gas Extraction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1), as a self-assessment |
| Target report | None. The company is not a service organization and does not plan a SOC 2 examination |
| Part A | Readiness self-assessment (`soc2-readiness.csv`), used to answer the larger non-operating partner's questionnaire and the seismic data license renewal |
| Part B | Production accounting vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Office Manager with the independent consultant; approved by the Owner 2026-08-31 |

## 1. Why SOC 2 for this organization
**The company is not a SOC 2 service organization.** SOC 2 reports on controls at an organization that provides services to other businesses. Cris Santos Company produces crude oil and sells it at the lease; the purchaser buys a commodity and does not rely on the company's systems. The vertical overlay names no sector assurance alternative to SOC 2. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a partner and a licensor.** In June 2026 the larger of the two non-operating working interest owners sent a security questionnaire before a joint drilling program. The partners share well data, reservoir maps, and interpretations of the licensed 3D seismic survey with the company as operator, and the questionnaire follows the Security and Confidentiality criteria. The response is due 2026-09-30. Separately, the seismic data license renews on 2026-12-31 and asks the licensee to state how it limits access to the licensed data. Both will receive this self-assessment, the POA&M (P07), and a named security contact.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. The partner's instructions accept a self-assessment, and an audit would cost more than the company's whole 2026 security budget.

**Why Confidentiality and not another category.** What the partner and the licensor care about is that shared well data and licensed seismic data stay with the people allowed to see them. Availability commitments are not made to anyone (field availability is handled by the BIA and covered under CC7.5 and CC9.1). The company processes no transactions for customers (Processing Integrity), and personal information duties come from Fla. Stat. 501.171 (P03), not privacy commitments to customers.

**B. Relying on the production accounting vendor.** The vendor holds royalty owner personal information and runs the allocations behind every royalty payment, and the company inherits several controls from it (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls. Reviewing it each year is part of vendor oversight (SA-9; POL-02 A.5).

## 2. System description (scope)
- **Services:** operation of one oil field for the company and its 2 partners; production accounting and royalty distribution; sharing of well and seismic data with the partners.
- **Infrastructure and software:** the Field SCADA and Production Accounting System (SSP, P02): SCADA host and field controllers, production accounting, the productivity suite, cloud backup, the SCADA vendor's cloud service, 7 computers and 5 phones.
- **People:** 7 employees, the MSP, the SCADA integrator.
- **Data:** licensed seismic data and reservoir interpretations, partner well data, royalty owner and employee personal information, controller programs.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 16 | 12 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

In scope: 35 criteria (5 Ready, 17 Partially ready, 13 Not ready). Out of scope: 26 criteria.

**Ready:**
- CC1.3: Security Coordinator and OT lead designated in writing
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk analysis done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked in the POA&M

**Not ready:**
- C1.1: the Geology folder with licensed seismic data is open to all 7 staff, which the license does not allow; partner data is emailed without encryption
- CC6.1, CC6.2, CC6.3: shared HMI and integrator accounts, no MFA on vendor access, no account procedure, late removal
- CC6.6: the flat field office network and the remote desktop exposure found in testing
- CC7.1, CC7.2, CC7.5: no vulnerability scanning or monitoring; no isolated or tested SCADA backup
- CC8.1: no change control for SCADA, and a vendor changed field settings without approval
- CC1.4, CC2.1, CC6.5, CC9.2: no training, no inventories, no disposal records, no vendor terms

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation memo; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Production accounting vendor SOC 2 review | CC9.2 | Yes | Bridge letter (2026-10) |
| Geology folder permission report limited to licensed users | C1.1 | No | After restriction (2026-09) |
| Account review and last-day checklists | CC6.2, CC6.3 | No | Quarterly from 2026-10 |
| MSP monthly report (patching, antivirus, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| External scan reports | CC6.6, CC7.1 | Yes (2026-08-12 rescan) | Quarterly from 2026-12 |
| Restore test records | CC7.5 | No | Quarterly from 2026-09 |
| OT change log | CC8.1 | No | From 2026-10 |
| Training and phishing exercise records | CC1.4, CC2.2 | No | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the production accounting vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31, covering Security, Availability, Confidentiality, and Processing Integrity. One exception (a late quarterly access review of vendor support staff), remediated.
- **Availability:** the vendor's stated RTO of 24 hours and RPO of 1 hour **meet the BIA** for production accounting (BP-05: RTO 120 h, RPO 24 h).
- **Controls the company must run.** The report lists complementary user entity controls. Three are open gaps at the company: user removal (POAM-005, POAM-006), verification of owner bank detail changes (P01 R-004), and protection of export files (P01 R-005). **The vendor's controls protect owner data and payments only once those gaps are closed.**
- **Incident notice:** the vendor commits to 72 hours after confirming an incident. Florida law separately requires a third-party agent to tell the company within 10 days of determining a breach (Fla. Stat. 501.171(6)). The contract should add the 72-hour commitment and breach cooperation at renewal.
- **Other critical vendors have no report.** The SCADA vendor offers only a security whitepaper, and the MSP and integrator have none. Each gets a short questionnaire by 2026-12-31 (POAM-013).

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC2.3, CC3.3, CC6.2, CC6.3, CC6.4, C1.1 | Acknowledgments; partner questionnaire response; account procedure and last-day checklist (POAM-005, POAM-006); call-back rule; gate code; Geology folder restricted |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.5 to CC6.8, CC7.1 to CC7.5, CC8.1, CC9.1, C1.2 | Monthly oversight notes; training (POAM-011); OT inventory (POAM-010); vendor sessions with MFA (POAM-001); firewall (POAM-002); backups and restore tests (POAM-003, POAM-004); replacement host and EDR (POAM-008, POAM-009); tabletop (POAM-012); OT change log; disposal records |
| 2027 Q1 | CC9.2 | Vendor security terms at renewal (POAM-013) |

**Response to the partner and the licensor:** send this summary, the readiness checklist, and the POA&M by 2026-09-30 (the licensor by 2026-12-31), name the Office Manager as security contact, and commit to an updated self-assessment in April 2027.

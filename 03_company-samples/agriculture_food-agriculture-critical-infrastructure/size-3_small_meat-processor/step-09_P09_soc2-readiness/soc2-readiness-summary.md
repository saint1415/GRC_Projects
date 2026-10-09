# SOC 2 Readiness Summary: Cris Santos Company | Food and Agriculture | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (meat processing plant with a smoked seafood room) |
| Tier / Vertical | Small / Food and Agriculture |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only, as a self-benchmark |
| Target report | None. The company does not plan a SOC 2 examination |
| Part A | Security self-benchmark against the Common Criteria (`soc2-readiness.csv`) |
| Part B | Cold-chain monitoring vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-21 by the IT Manager |

## 1. Why SOC 2 (or an alternative) for this organization
**The company is not a service organization.** SOC 2 reports on controls at an organization that provides services to other businesses, where those controls affect the customers' own systems or data. Cris Santos Company sells food. Its grocery-chain and distributor customers rely on it for safe product and on-time delivery, not for processing their data. No customer has asked for a SOC 2 report, and a SOC 2 examination would not be the right assurance tool.

**What customers do ask for.** Food safety assurance is covered by FSIS inspection, the HACCP plans, and customer supplier-approval programs. The vertical overlay names no SOC 2 alternative for this sector. Two grocery-chain customers have started sending **cybersecurity questionnaires** (EV-036) as part of supplier approval, after publicized ransomware incidents at food companies. So SOC 2 is used here in two limited ways:

**A. Security self-benchmark.** The Common Criteria (CC1-CC9) are a well-known, organized yardstick. The IT Manager rated the company against them so it can answer customer questionnaires consistently, reusing evidence from P02, P06, and P07. Availability, Confidentiality, Processing Integrity, and Privacy are out of scope: they describe commitments a service organization makes to its customers, and the company makes none of that kind. Its own availability and integrity needs are covered by the BIA (P05) and the SSP (P02).

**B. Third-party risk management.** The company does rely on service organizations. The most critical one for food safety is the **cold-chain monitoring vendor**, whose alerting is how the company learns that cold storage (a CCP) has gone out of limits. Its SOC 2 Type 2 report, obtained at intake (EV-033), is the best available evidence for the controls the company inherits (P04). The company reviews it every year (SA-9, POL-01 4.10).

## 2. System description (scope)
- **Services:** further processing of meat and seafood for grocery chains, distributors, and the outlet and online store.
- **Infrastructure and software:** the Plant Production and Cold-Chain Monitoring System (SSP, P02), plus the ERP, WMS, identity provider, and productivity suite.
- **People:** 250 workforce members, the controls integrator, and the refrigeration contractor.
- **Data:** formulations, food safety records, the food defense plan, employee data, and online customer accounts.
- **Procedures:** POL-01 to POL-05, the HACCP plans, the food defense plan, and the P08 runbook.

## 3. Readiness results
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 7 | 19 | 7 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.1: code of conduct and sanctions
- CC1.3: roles designated, including OT owner and Food Defense Coordinator
- CC2.3: external communication channels to customers, FSIS, and FDA
- CC3.1 and CC3.2: objectives and risk assessment
- CC4.2: deficiencies tracked in the POA&M
- CC5.1: controls selected against risks

**Not ready:**
- CC3.4 and CC8.1: no change management in OT (the same gap as the overdue food defense reanalysis)
- CC6.3: shared OT accounts and excess privileges
- CC6.6: weak OT boundary and always-on remote access
- CC7.1 and CC7.2: no OT inventory, vulnerability identification, or monitoring
- CC7.5: OT recovery unproven

**What a customer questionnaire answer should say.** Business systems are in reasonable shape (MFA, EDR, encryption, SaaS with SOC 2 reports). Plant control systems are not, and the company has a funded plan with dates (P01 section 4, P07 POA&M).

## 4. Findings from the cold-chain vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability. One exception on alert delivery latency, remediated with a second messaging route.
- **Availability:** alert dispatch within 5 minutes and 24-hour local gateway buffering **meet the BIA** for BP-01 (MTD 2 h, RTO 1 h, RPO 15 min), but only if the company's own side works.
- **Controls the company must run.** The report lists complementary user entity controls: configure and test alert recipients, keep the gateway connected, manage users and MFA, and review alert acknowledgments. Two are open gaps at the company: a single SMS recipient with no escalation (P01 R-005) and the gateway on corporate Wi-Fi (P01 R-029). **The vendor's controls only protect the cold chain once those gaps are closed.**
- **Follow-ups:**
  - Ask how the vendor monitors failures at its carved-out messaging provider.
  - Export sensor data monthly into the records application so HACCP retention does not depend on the vendor (9 CFR 417.5(e)).
  - Negotiate 24-hour notice for incidents affecting alert delivery or data integrity.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.4, CC2.2, CC6.1, CC6.2, CC6.4, CC6.7, CC7.4, CC9.2 | Training records (including temporary workers), named OT account lists, remote access session logs, tabletop report, vendor contract terms |
| 2027 Q1 | CC3.4, CC8.1, CC6.3, CC6.6, CC6.8, CC7.1, CC7.2, CC7.5 | OT change tickets with FSQA sign-off, firewall rule reviews, OT monitoring alerts, restore test records, PLC checksum reports |
| 2027 Q2 | CC1.2, CC3.3, CC4.1, CC5.3 | Owner review minutes, fraud scenarios in the risk assessment, monthly POA&M reviews, written procedures |

**Response to grocery-chain questionnaires:** answer from this self-benchmark, attach the POA&M summary, and commit to an updated self-benchmark in April 2027. The General Manager approves each response.

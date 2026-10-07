# SOC 2 Readiness Summary: Cris Santos Company Holdings | Finance and Insurance | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Finance and Insurance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the AICPA text is not reproduced |
| Scoping | Per division (section 1). One readiness report: Financial Software and Data Services (`soc2-readiness.csv`). The bank and Commercial Real Estate are out of scope for SOC 2, with reasons. The bank's review of the division's SOC reports as a user entity is in `affiliate-soc-report-review.csv` |
| Prepared | 2026-09-10 by the client risk and assurance director with the Head of Technology and Cyber Risk; affiliate review completed 2026-09-04 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations build their own controls on.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Financial Software | Digital banking platform (SYS-S1) for 310 client institutions and the bank | **Yes, a true service organization.** Client institutions rely on the platform's controls as part of their own programs (12 CFR 30 App. B III.D.3 for bank clients) | **In scope.** Existing annual Type 2 | Security, Availability, Confidentiality; Processing Integrity planned for the 2027 period | Type 2, 12 months ending September 30; SOC 1 Type 2 as well |
| Financial Software | Cash-flow data service (SYS-S2) for 64 client banks | **Yes.** Client banks use its outputs in credit decisions | **To be added** to the 2026 description, or excluded with a statement (scenario gap 4) | Same, plus Processing Integrity in 2027 | Same report |
| Banking | Deposits, lending, payments, treasury management | **No** for SOC 2. The bank's customers buy banking products; they do not build their controls on the bank's systems | **Out of scope** (reasons below) | n/a | n/a |
| Commercial Real Estate | CRE lending; loan servicing for the bank and third-party investors; group premises | **Partly.** Loan servicing for third-party investors is a service whose controls affect investors' financial reporting | **Out of scope for SOC 2.** A SOC 1 on loan servicing is to be evaluated in 2027 if investors ask | n/a | n/a |

**Why the bank is out of scope:**
1. **No user entities for SOC 2.** Consumers and businesses buy accounts and loans. They do not rely on the bank's controls as part of their own control environment, which is what a SOC 2 report is for.
2. **Assurance comes from supervision instead.** The bank is examined by the OCC against the Interagency Guidelines using the FFIEC IT Examination Handbook, and the holding company by the Federal Reserve. This matches the vertical overlay's named alternatives: federal and state bank examinations, and SOC 1 reports from service providers.
3. **Treasury management clients** sometimes ask for assurance. They receive the group security program description and the bank's controls summary, not a SOC report.
4. **Revisit trigger:** if the bank starts offering processing to other institutions (for example, correspondent payment processing), assess whether a SOC 1 or SOC 2 is needed.

**Why Commercial Real Estate is out of scope for SOC 2 now:** its only external service is loan servicing for third-party investors, whose concern is financial reporting (SOC 1 territory, or the servicing attestations investors specify in their agreements). Group Property Management serves only the group. The division benefits from this work anyway: the common controls it inherits are the same ones the platform report covers, once its inheritance is documented (POAM-018).

**Other assurance options considered.** Some client institutions ask about ISO/IEC 27001. The group decided SOC 1 and SOC 2 remain the primary reports because client contracts require them and client banks use them in their third-party oversight (the 2023 interagency third-party guidance mentions SOC reports as something a bank may consider reviewing). Credit union clients, which the Bank Service Company Act does not cover, rely even more on the SOC reports, because their regulator cannot examine the division.

## 2. System description (scope)
- **Services:** online and mobile banking, business wire and ACH initiation, and tenant administration for 310 client institutions and the bank; the cash-flow data service for 64 client banks (**not yet in the description**).
- **Infrastructure and software:** SYS-S1 and SYS-S2 on cloud provider A (primary and warm standby regions); backups in provider B; group identity (SYS-G1), SOC (SYS-G2), and infrastructure (SYS-G3) included as part of the system.
- **Subservice organizations (carve-out):** cloud providers A and B; source hosting and status page vendors.
- **People:** about 5,500 division employees plus the group SOC and identity teams.
- **Data:** client institutions' customer data for about 19 million end users.
- **Complementary user entity controls:** approve and remove tenant administrators; set business entitlements and limits; review tenant audit reports; reconcile payment files; require MFA for business payment users; give the division a bank-designated contact for incident notices (12 CFR 53.4(a)(1)).

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5; planned for 2027) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |

**Not ready:** CC2.3. The cash-flow data service is not in the system description, and 61 client banks have not given a designated notice contact.
**Partially ready:** CC3.4 and CC8.1 (data service changes), CC6.1 (replayable 12-hour sessions), CC6.3 (support console reach), CC7.2 (token replay and console activity not detected), CC7.4 (client notice process), A1.3 (region failover not tested in the period), C1.2 (conversion files in mailboxes), PI1.1 and PI1.4 (no processing objectives or stability testing for the score).

**The immediate issue is the report now being prepared** for the period ending 2026-09-30. The data service operated for the whole period and was sold as part of client agreements. Management must either describe it (with its controls and any exceptions) or state clearly that it is excluded, so client banks do not assume coverage. Expect the service auditor to evaluate CC2.3, CC3.4, and CC8.1 for exceptions, and the support console finding under CC6.3.

**Processing Integrity** is planned for the 2027 period because client banks now ask whether payment processing and the cash-flow score are complete and accurate. Payment processing is ready (PI1.2, PI1.3, PI1.5); the score is not (PI1.1, PI1.4).

## 4. The bank as a user entity of its affiliate (`affiliate-soc-report-review.csv`)
Until 2026 the bank never reviewed the division's SOC reports, because the division is an affiliate (P03 G-026; scenario gap 3). The first review, completed 2026-09-04 on the reports for the period ending 2025-09-30 plus a bridge letter to 2026-06-30, found:
- unmodified opinions; one SOC 2 exception (CC6.2, late removal of 2 support leavers) with a fix in place;
- the data service the bank's AI credit model uses is **not covered** by either report;
- 4 of 6 CUECs mapped to bank controls that operate; the bank never gave the division a designated notice contact, and tenant administrator removal is not tied to bank HR events;
- neither the reports nor the 2021 intercompany agreement state incident notice terms (POAM-012).

## 5. Remediation plan and evidence calendar
| Quarter | Scope | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | Platform | CC2.3, CC7.4 | Designated contacts for all client banks; 4-hour timer; notice register with contract terms |
| 2026 Q4 | Data service | CC2.3, CC3.4, CC8.1 | Updated system description (or exclusion statement); change gate records; developer documentation sent to 64 client banks |
| 2026 Q4 | Platform | CC6.1, CC6.3, CC7.2 | Device-bound session policy; tenant-scoped support roles; console review and token-replay use cases |
| 2027 Q1 | Platform | A1.3, C1.2 | Region and gateway failover test reports; mailbox purge evidence |
| 2027 Q1 | Data service | PI1.1, PI1.4 | Processing objectives; stability and fairness test results approved by model risk management |
| 2027 Q2 to Q3 | All in scope | All in-scope criteria, including PI1 | Operating evidence for the 2027 period (2026-10-01 to 2027-09-30) |

**Communication:** the division president briefs the 20 largest client banks on the support console and data service changes before the 2026 report is issued. The bank records its affiliate review in its vendor file and repeats it each year (POL-01 4.8).

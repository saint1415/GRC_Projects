# SOC 2 Readiness Summary: Cris Santos Company Holdings | Information | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Information |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the AICPA text is not reproduced |
| Scoping | Per division (section 1). Two readiness reports: Workforce Cloud (`soc2-readiness.csv`) and the Payments and Payroll platform (`soc2-readiness-payments-and-payroll.csv`). Technology Consulting is out of scope |
| Prepared | 2026-09-11 by the Group Chief Risk Officer's assurance team with the Cloud Software division CISO and the Payments and Payroll division CISO; presented to the board risk committee 2026-09-17 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service whose controls other organizations rely on.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Cloud Software | Workforce Cloud (SYS-D1, the WCP) for about 38,000 customers | **Yes.** Customers rely on it for their workers' data and their payroll inputs | **In scope (full).** Existing annual Type 2; ISO/IEC 27001 certified | Security, Availability, Confidentiality | Type 2, 12 months ending September 30 |
| Payments and Payroll | Embedded payroll (SYS-D3) for about 11,500 employers and payment acceptance (SYS-D4) for about 26,000 merchants | **Yes.** Employers rely on it for pay, tax deposits, and worker data. Today they receive a SOC 1 Type 2 (financial reporting) for payroll and a PCI DSS Attestation of Compliance for payments; enterprise employers now ask for SOC 2 | **In scope (new).** First readiness assessment | Security, Availability, Confidentiality, Processing Integrity | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| Technology Consulting | Implementation and integration projects | **No, for project work.** Clients receive deliverables, not an ongoing service whose controls they build on | **Out of scope** (reasons below) | n/a | n/a |
| Technology Consulting | Managed application services (about 160 clients) | **Possibly.** Clients rely on consultants operating their applications | **Deferred to 2027 review** | n/a | n/a |

**Why Technology Consulting is out of scope for now:**
1. **Project work has no user entities in the SOC 2 sense.** Implementation clients own and operate the systems after go-live; consultants work under each client's controls and contract.
2. **Assurance comes from other sources.** Federal clients rely on FAR 52.204-21 (P03 consulting table); hospital clients rely on BAAs and the HIPAA Security Rule; commercial clients rely on contract terms and security questionnaires answered with the group program description and P07 results.
3. **The division is not ready to be described.** Its common control inheritance is undocumented (gap 10) and the acquired firm runs a separate stack until 2027-03-31 (gap 9). A system description written today would have to carve out half the division.
4. **Revisit trigger:** after the acquired-firm migration, assess whether managed application services should get a SOC 2 Type 1, starting with the clients that have asked for one.

**Other assurance options considered.** ISO/IEC 27001 certification already covers Workforce Cloud and is accepted by some international customers. The vertical profile lists ISO/IEC 27001 and FedRAMP as alternatives; FedRAMP does not apply (no government edition). SOC 2 remains the primary report because customer and employer contracts require it.

## 2. System descriptions (scope)
### 2.1 Workforce Cloud
- **Services:** scheduling, time and attendance, HR records, employee self-service app; optional AI features (workforce assistant for 6,200 opt-in customers; attrition-risk insights for about 9,800).
- **Infrastructure and software:** the WCP on cloud provider A (primary and warm standby regions); group identity (SYS-G1), SOC (SYS-G2), and CI/CD (SYS-G3) as internal shared services.
- **Subservice organizations (carve-out):** cloud provider A; the third-party model provider; SMS and email delivery providers; the support SaaS.
- **People:** about 14,000 Cloud Software employees plus group SOC, identity, and platform teams. **Consultants from Technology Consulting** who hold implementation-partner roles in customer tenants must be described as part of the system's people, with their access controls (gap 3).
- **Data:** customer worker data (about 21 million profiles), and payroll handoff files held for the Payments and Payroll division.
- **Complementary user entity controls:** customer SSO and MFA for administrators, user provisioning and removal, review of export destinations and API tokens.

### 2.2 Payments and Payroll platform
- **Services:** gross-to-net payroll, tax deposits and filings, direct deposit through sponsor bank A; card and ACH acceptance and settlement through sponsor bank B.
- **Infrastructure and software:** payroll engine and payments CDE on cloud provider B; group common controls carved in.
- **Affiliate service:** the WCP supplies hours and bank details through the handoff. The description must state whether the WCP is included or carved out; the group's preference is to **include** the new handoff channel (which will sit in division accounts after POAM-006) and carve out the rest of the WCP, relying on the Workforce Cloud SOC 2 report.
- **Subservice organizations (carve-out):** cloud provider B; sponsor banks; tax filing networks.
- **Complementary user entity controls:** employers approve pay runs, review payroll registers, and protect their administrator accounts.

## 3. Readiness results
### 3.1 Workforce Cloud (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 23 | 9 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3 (three public or contractual statements are not true today) and C1.2 (exports and handoff files kept far longer than the 30 days in the system description).
**Partially ready:** CC3.4 and CC8.1 (AI changes without impact analysis or adversarial testing), CC6.1, CC6.2, CC6.3, and CC6.7 (static keys, partner roles, and the shared handoff bucket), CC7.2 (no read logging or bulk-read alerts), CC7.4 (notification matrix), CC9.2 (model provider and consultant arrangements), A1.3 (joint recovery with payroll), and C1.1 (pre-2023 DPAs and AI tuning).

**The immediate issue is the report now being prepared.** The observation period ended 2026-09-30, and the export retention deviation, the partner roles, and the AI changes existed throughout it. Management must tell the service auditor now (POAM-007 milestone 2026-10-31). Expect the auditor to evaluate CC2.3, CC6.2, CC6.3, CC8.1, and C1.2 for exceptions. The goal is to correct the statements and fix retention before the report is issued, so the report can describe the remediation, and to have the 2027 period start clean.

**Processing Integrity** is out of scope today because the service makes no processing integrity commitments. It is under evaluation for 2027, because customers now ask whether AI outputs are complete and accurate (P10).

### 3.2 Payments and Payroll platform (`soc2-readiness-payments-and-payroll.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 24 | 7 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first report:** the PCI DSS program, the SOC 1 control set, and group common controls already evidenced for the Workforce Cloud report cover most of the Security criteria.
**Not ready:** CC2.3 (no SOC 2 system description or written service commitments) and CC9.2 (the WCP holds division customer information with no agreement, assessment, or monitoring, gap 5).
**Partially ready:** CC3.2 (risk assessment omitted the affiliate flow), CC4.1 (missed segmentation test), CC6.1 and CC7.2 (handoff data readable and unlogged in the WCP), CC6.6 and CC8.1 (checkout page scripts), CC7.4 (notification matrix), A1.3 (joint recovery), C1.2 (handoff retention), PI1.1 (processing commitments not yet written), and PI1.5 (inputs stored outside the division).

## 4. Remediation plan and evidence calendar
| Quarter | Division | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | Cloud Software | CC2.3, C1.2 | Corrected trust center and product pages; lifecycle rules and deletion records; letter to the service auditor |
| 2026 Q4 | Cloud Software | CC6.1, CC6.2, CC6.3, CC6.7, CC7.2 | Key retirement report; partner role expiry configuration; new handoff channel; read logs and detection rules |
| 2026 Q4 | Payments and Payroll | CC9.2, CC3.2, CC4.1, CC6.6, CC8.1, C1.2, PI1.5 | Intercompany agreement and first WCP assessment; updated risk assessment; segmentation test; script inventory and tamper detection; handoff retention |
| 2026 Q4 | Both | CC7.4 | Completed matrix; tabletop report (2026-12-08) |
| 2027 Q1 | Cloud Software | CC3.4, CC8.1, CC9.2, A1.3 | Retroactive PIAs; AI test results; internal service agreement; joint failover test |
| 2027 Q1 | Payments and Payroll | CC2.3, PI1.1, A1.3 | System description; processing integrity commitments; joint failover test. Type 1 as of 2027-03-31 |
| 2027 Q2 to Q3 | Both | All in-scope criteria | Operating evidence for the Workforce Cloud 2027 period and the platform's first Type 2 period (2027-04-01 to 2027-09-30) |
| 2027 Q2 | Cloud Software | C1.1 | DPA amendments at renewal |

**Communication:** the Cloud Software division president briefs the top 200 customers on the export retention deviation and remediation before the 2026 report is issued. Payments and Payroll sends its 300 largest employers a readiness letter with the 2027 timeline and offers the SOC 1 report and PCI DSS Attestation of Compliance in the meantime.

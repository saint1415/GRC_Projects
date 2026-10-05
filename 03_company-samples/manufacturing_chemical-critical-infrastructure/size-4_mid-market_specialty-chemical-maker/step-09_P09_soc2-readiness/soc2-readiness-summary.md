# SOC 2 Readiness Summary: Cris Santos Company | Chemical | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed specialty chemical formulator and packager) |
| Tier / Vertical | Mid-Market / Chemical |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1) |
| Service in scope | Tank Telemetry and Replenishment Service (TTRS, SYS-12) |
| Target report | SOC 2 **Type 1** as of 2027-03-31 (interim), then **Type 2** for the observation period 2027-04-01 to 2027-09-30, report expected by 2027-11-30 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-04 by the GRC Analyst and the Director of Customer Solutions, with the Information Security Manager, using P02, P04, P05, and P07 evidence; approved by the COO 2026-09-22 |

## 1. Why SOC 2 for this organization
A chemical maker is usually not a SOC 2 service organization: it sells products, and its customers' assurance needs are product quality and supply. **TTRS changes that.** The company operates a managed service: it monitors 420 customer tanks, decides when to deliver, and creates orders automatically. Customers rely on it to keep treatment chemicals in stock, so TTRS affects their operations the way an outsourced service does.
- Two large water utilities and a pulp and paper group require a SOC 2 Type 2 report on TTRS from 2027 (P01 R-024: about $2 million to $6 million of annual revenue at risk).
- They asked for **Security and Availability**. The company added **Processing Integrity**, because the core promise is correct, timely replenishment orders, and **Confidentiality**, because tank levels and delivery data reveal customers' operations.
- **Privacy is excluded:** TTRS holds business contacts and tank data, not consumer personal information.

**Why Type 1 first.** P07 and this assessment found gaps in change management, recovery testing, vendor oversight, and gateway security. A Type 2 period started now would produce exceptions. The customers accepted a Type 1 report as of 2027-03-31 with quarterly status updates, followed by a 6-month Type 2 period.

**Alternatives considered:** a questionnaire-only response (not accepted by the utilities' auditors); an ISO/IEC 27001 certificate (customers asked specifically for SOC 2); the vertical overlay names no sector-specific assurance alternative.

**Auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the P07 work does not raise an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | TTRS: telemetry collection, customer portal, replenishment decisions and orders, AI-004 demand forecasting |
| Infrastructure | TTRS account in the cloud landing zone, the backup account, shared services and security accounts (P04); 420 company-owned cellular gateways at customer tanks |
| Software | Telemetry ingestion, replenishment engine, customer portal, TTRS database, AI-004 model service, the ERP order interface |
| People | Director of Customer Solutions, 5 TTRS engineers, customer service and dispatch staff, IT and security teams, MSSP |
| Data | Tank levels, delivery addresses, customer contacts, replenishment orders |
| Procedures | POL-01 to POL-05, the standards index, runbook 2 (P08), the TTRS change process (being built) |
| Subservice organizations (carve-out) | Cloud provider, ERP vendor, identity provider, MSSP, gateway maker's device management service, cellular carrier. Their controls are covered by their own reports or alternative assurance and by the complementary subservice organization controls in the system description |
| Not in scope | Plant production and the PCBMS (P02); the company's products themselves |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 15 | 15 | 3 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **18** | **21** | **4** | **18** |

**Ready (18):** governance and oversight (CC1.1, CC1.2, CC1.5, CC2.2), risk assessment (CC3.1, CC3.2), monitoring (CC4.1, CC4.2), control design (CC5.1), access and boundary protection (CC6.2, CC6.4, CC6.6, CC6.7), detection and triage (CC7.2, CC7.3), capacity (A1.1), and processing objectives and stored data (PI1.1, PI1.5). The corporate program built since 2023 (audit committee reporting, P01, P07, MSSP) carries most of these.

**Not ready (4):**
- **CC8.1** change management: replenishment rules and code change with no peer review, test evidence, or release approval (gap 11; P01 R-023).
- **CC7.5 and A1.3** recovery: TTRS runs in one region, and no restore or failover has been tested (P01 R-021).
- **CC9.2** vendor management: only 3 of 11 key cloud and SaaS vendor reports have been reviewed (gap 7).

Each maps to POA&M items POAM-012 and POAM-021 (P07). The 21 Partially ready criteria mostly depend on standards being issued (P06), gateway hardening (CC6.1, CC6.8, CC7.1), and documenting checks that exist informally (PI1.2 to PI1.4).

**Mapping to other work.** Evidence is reused from P02 (control statements), P04 (cloud controls), P05 (availability commitments: BP-14 RTO 8 hours, RPO 1 hour), P06 (policies), P07 (test results), and P08 (runbook 2). The `related_sp800_53` column links each criterion to SP 800-53 controls; AICPA publishes a TSC-to-SP 800-53 mapping (SRC-TSC).

## 4. Vendor SOC 2 review program (Part B)
`vendor-soc2-review.csv` covers the 11 key cloud and SaaS vendors and the 3 OT service providers (13 rows; the SIS and tank gauging vendors share one row).
- **Reviewed (3):** cloud provider, ERP vendor, identity provider. All unqualified. The ERP vendor's stated RTO 8 hours and RPO 1 hour meet the BIA. The cloud provider's report is sound, but TTRS's single-region design is the company's own gap.
- **Requested, review due by 2026-12-31 (6):** MSSP, productivity suite, HR and payroll, fleet management, community notification service, AI-005 vendor.
- **No SOC 2 available (2):** the gateway maker (questionnaire and certificate review) and the cellular carrier (availability commitments).
- **OT service providers (2 rows):** no SOC 2 exists for this kind of service. Assurance is an annual questionnaire, an on-site review of remote support practices, and contract clauses for vulnerability and incident notice, which the USCG rule requires (33 CFR 101.650(f)(2)).

Four contracts lack incident notice terms (fleet, gateway maker, community notification, AI-005) and are on the renewal list.

## 5. Remediation plan and evidence calendar
| Window | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.3, CC1.4, CC2.1, CC3.3, CC3.4, CC5.2, CC6.3, CC6.5, CC8.1, CC9.1, CC9.2, C1.1, C1.2, PI1.2 to PI1.4 | Approved RACI; training records; data flow diagram; change tickets with peer review and approval; quarterly access review; gateway wipe log; phone workaround drill record; vendor review records; reconciliation logs |
| 2027 Q1 | CC2.3, CC5.3, CC6.1, CC6.8, CC7.1, CC7.4, CC7.5, A1.2, A1.3 | Status page; issued standards; gateway firmware and credential reports; tabletop report; restore and failover test records; monthly availability reports |
| 2027-03-31 | Type 1 (design) report | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence (quarterly reviews, monthly availability, change tickets, vendor reviews, restore tests) |

**Status reporting.** The Director of Customer Solutions reports readiness monthly to the COO, and quarterly to the audit committee and the three requesting customers.

# SOC 2 Readiness Summary: Cris Santos Company | Real Estate and Rental and Leasing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management and an in-house Closing Services division) |
| Tier / Vertical | Small / Real Estate and Rental and Leasing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Self-benchmark for the title insurance underwriter; no CPA report is planned |
| Part A | Company self-benchmark against the Security criteria (`soc2-readiness.csv`) |
| Part B | Transaction platform vendor's SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-15 by the IT Manager; accepted by the COO 2026-09-21 |

## 1. Why SOC 2 for this organization
**The company is not a service organization.** A SOC 2 report describes controls at a company that provides services to other businesses, where those controls affect the customers' own security. Cris Santos Company serves consumers (buyers, sellers, tenants, and property owners). No business customer relies on its systems as part of that customer's own control environment, and none has asked for a SOC 2 report. A CPA-issued SOC 2 report would cost far more than it would return.

SOC 2 criteria still appear here for two reasons:

**A. The title insurance underwriter's agent review.** The underwriter that appoints the Closing Services division as its agent reviews each agent's escrow and security practices. For 2026 it asked the company to benchmark its security controls against the Trust Services Criteria, **Security category only**. The company answers with this self-benchmark, the POA&M (P07), and the gap analysis (P03). This is a readiness self-assessment, not an attestation.

Why not other categories:
- **Availability and Confidentiality:** the underwriter did not ask. The BIA (P05) and POL-04 already cover recovery and confidential data.
- **Processing Integrity:** the company makes no processing commitments to business customers.
- **Privacy:** consumer privacy is governed by the GLBA privacy provisions and the FTC Act, and was not requested.

**B. Third-party risk management.** The company relies on its transaction platform vendor for many inherited controls (P02, P04). The vendor's SOC 2 Type 2 report is the evidence for those controls, and the Safeguards Rule requires periodic assessment of service providers (16 CFR 314.4(f)(3)). This is the company's first such review (P03 G-031).

The vertical overlay names no industry-specific assurance alternative. The underwriter's own agent review questionnaire is the most common mechanism in this business, and this self-benchmark feeds it.

## 2. System description (scope)
- **Services:** residential sales brokerage and closing and settlement services (Closing Services division).
- **Infrastructure and software:** the Transaction Management and Closing Communications System (SSP, P02), with online banking and the e-signature service as interconnected external services.
- **People:** 60 employees, about 140 contractor sales associates, and the MSP.
- **Data:** customer information in closing files, wire instructions, transaction records, and escrow records.
- **Procedures:** POL-01 to POL-05 and the P08 BEC runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 20 | 9 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC3.1 and CC3.2: objectives and a written risk assessment exist (P01).
- CC3.3: fraud risk is at the center of the risk assessment (diverted wires, seller impersonation, insider payee changes).
- CC4.2: deficiencies are tracked in the POA&M with owners and dates.

**Not ready:**
- CC6.1: contractor agents have no MFA.
- CC6.3: late contractor removal, office-wide visibility, single approver on two escrow accounts.
- CC6.5: no retention or disposal schedule.
- CC6.7: closing packages emailed unencrypted; external auto-forwarding allowed.
- CC7.1 and CC7.2: no vulnerability scanning and no security monitoring.
- CC7.5: backups not isolated or restore-tested (the same gap as risk R-006).
- CC8.1: no change management for the portal.
- CC9.2: no service provider program.

The pattern matches P07: the company has strong manual money controls (dual approval on the trust account, positive pay, monthly reconciliations) but weak identity, monitoring, and recovery controls around the email channel that criminals use to get around them.

## 4. Findings from the transaction platform vendor's report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-06-30. One exception (2 of 40 changes lacked documented approval), remediated by the vendor.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the company's BIA** for contract-to-close (P05 BP-03: RTO 8 h, RPO 4 h).
- **Controls the company must run.** The report lists complementary user entity controls: timely user removal, MFA or single sign-on for all users, least-privilege roles, activity report review, and API credential protection. **All five are open gaps at the company:** no contractor MFA (POAM-001), late removal (POAM-009, POAM-010), office-wide visibility (POAM-011), no activity review (POAM-007), and API keys stored in a configuration file on the integration VM (P04 finding 4). **The vendor's controls only protect the company once these gaps close.**
- **Follow-ups:**
  - Obtain the bridge letter through 2026-09-30 by 2026-10-31.
  - Add the e-signature vendor, outside the report's scope, to the service provider inventory (POAM-013).
  - Review the closing software vendor's report next; its recovery commitments are not documented (P05).

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1, CC6.3, CC6.7, CC7.1, CC7.2, CC1.2, CC1.3, CC2.2 | MFA enrollment reports, dual approval settings, access review records, scan reports, alert tickets, designation letter, first annual report, training records |
| 2027 Q1 | CC7.5, CC8.1, CC9.2, CC6.5, CC7.4 | Restore test records, change tickets, provider inventory and contract addenda, retention schedule and purge log, tabletop report |
| 2027 Q2 | CC9.1, CC3.4, CC4.1 | Hurricane and contingency plan, change-triggered risk reviews, monthly verification samples |

**Response to the underwriter:** send this summary, the readiness checklist, and the POA&M (P07), with a commitment to an updated self-benchmark in June 2027.

# SOC 2 Readiness Summary: Cris Santos Company | Water and Wastewater Systems | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (investor-owned community water system) |
| Tier / Vertical | Small / Water and Wastewater Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Part A is an internal self-benchmark, not preparation for a CPA-issued report |
| Part A | Security-only self-benchmark (`soc2-readiness.csv`) |
| Part B | Review of the customer information system (CIS) vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager |

## 1. Why SOC 2 for this organization
**The company is not a service organization.** SOC 2 reports on controls at a service organization whose services affect its customers' own systems or data. Cris Santos Company sells drinking water to households and businesses. Its customers do not rely on its controls for their own security or financial reporting, and no customer, lender, or regulator has asked for a SOC 2 report. The vertical profile names no sector-specific assurance alternative. The binding assurance for this business is the SDWA section 1433 certification to EPA (P03), which is a self-certification with no third-party audit.

SOC 2 still appears here for two useful reasons:

**A. A Security-only self-benchmark.** The Common Criteria (CC1-CC9) are a well-known, auditor-oriented yardstick. Rating the company against them gives the majority owner and the cyber insurer's underwriter a second view of the program, in terms they recognize, alongside the CSF 2.0 view in P03. Only Security is in scope:
- **Availability:** assessed against SDWA section 1433 and the BIA (P03, P05) instead. Nobody has asked for commitments in TSC form.
- **Confidentiality and Privacy:** customer data duties come from Fla. Stat. 501.171. The company makes no TSC-style commitments to customers.
- **Processing Integrity:** not relevant to a water utility's customers.

**B. Third-party risk management.** The CIS vendor holds all customer personal information and runs the call campaigns the company would use for a Tier 1 public notice. Its SOC 2 Type 2 report is the evidence for the controls the company inherits (P02, P04). The company reviews it every year (SA-9, POL-01 4.8).

The SCADA integrator is the company's most important OT vendor, but it has no SOC 2 report. Its security is being handled through contract terms instead (P03 G-021).

## 2. System description (scope)
- **Services:** drinking water supply to 46,200 people; customer service and billing for 18,400 accounts.
- **Infrastructure and software:** the Water Treatment SCADA System (SSP, P02), the cloud tenant and SaaS services (P04), and the business network.
- **People:** 60 employees and the SCADA integrator.
- **Data:** process control data, RRA and ERP contents, customer personal information, water quality data.
- **Procedures:** POL-01 to POL-05, the ERP, and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 19 | 8 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles and risk acceptance authority are designated
- CC2.3: external communication (public notice SOP, primacy agency contacts)
- CC3.1 and CC3.2: objectives and the risk assessment are done
- CC4.2: deficiencies are tracked in the POA&M
- CC6.4: physical access

**Not ready:**
- CC2.1: no reliable OT inventory, diagram, or logs
- CC3.4: significant changes (the AI pilot, the CIS move) were not risk-assessed
- CC6.1, CC6.3, and CC6.6: OT logical access, least privilege, and boundary protection (the same gaps as P01 R-001 to R-003)
- CC7.1 and CC7.2: no vulnerability scanning or security monitoring
- CC8.1: no change management for OT or the AI model

The pattern matches P03: governance and physical controls are in reasonable shape, while OT technical controls are not.

## 4. Findings from the CIS vendor report (Part B)
- **Opinion:** Type 2, unqualified. One exception (a missed quarterly access review for vendor support staff), remediated.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 1 hour **meet the BIA** for customer service (BP-06: RTO 24 h, RPO 4 h) and billing (BP-07: RTO 72 h).
- **Controls the company must run.** The report lists complementary user entity controls: user provisioning and removal, single sign-on with MFA, customer-portal security settings, and protection of exported files. The company meets the first two for staff. **Customer-portal MFA is not enabled** (P01 R-013).
- **Public notice dependency.** The CIS call-campaign module is the fastest way to reach every account for a Tier 1 notice, but its telephony provider is carved out of the report. The company will test a 500-call campaign and keep broadcast media and posting as the backup the rule already allows (40 CFR 141.202(c)).
- **Breach notice.** The contract gives 72 hours after confirmation. Florida law separately requires a third-party agent to notify the company no later than 10 days after determining a breach (Fla. Stat. 501.171(6)(a)). The company will ask for 24-hour security incident notice at renewal.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.1, CC1.2, CC1.5, CC2.2, CC3.3, CC3.4, CC5.3, CC6.1, CC6.2, CC6.3, CC6.5, CC6.7, CC7.1, CC7.4, CC7.5, CC8.1, CC9.1 | Policy acknowledgments, owner briefing minutes, gateway session records, MFA reports, termination checklists, scan reports, change tickets, offline backup log, tabletop report, certified ERP |
| 2027 Q1 | CC1.4, CC2.1, CC4.1, CC6.6, CC6.8, CC7.2, CC7.3, CC9.2 | Training records, OT inventory, firewall change records, allowlisting reports, monitoring alerts and weekly reviews, integrator contract amendment |
| 2027 Q2 | CC5.1, CC5.2 | POA&M closure evidence for the remaining OT controls (SCADA upgrade) |

**Next step:** repeat this self-benchmark in August 2027 with the annual control assessment (P07) and report both to the majority owner.

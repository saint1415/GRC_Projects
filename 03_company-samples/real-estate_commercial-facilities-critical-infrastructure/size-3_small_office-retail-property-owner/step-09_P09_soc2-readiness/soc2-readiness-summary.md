# SOC 2 Readiness Summary: Cris Santos Company | Commercial Facilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| Tier / Vertical | Small / Commercial Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Part A is an internal self-benchmark, not preparation for a CPA-issued report |
| Part A | Security-only self-benchmark (`soc2-readiness.csv`) |
| Part B | Review of the access control and video platform vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager with the Security Manager |

## 1. Why SOC 2 for this organization
**The company is not a service organization.** SOC 2 reports on controls at a service organization whose services affect its customers' own systems or data. Cris Santos Company leases space and runs the buildings. Tenants rely on it for cooling, doors, and building security, but they do not rely on its information systems to process their own data or financial reporting. No tenant, lender, or insurer has asked for a SOC 2 report, and the vertical profile names no sector-specific assurance alternative. The binding assurance the company does give is contractual: the annual PCI DSS SAQ P2PE to its acquirer (P03).

SOC 2 still appears here for two useful reasons:

**A. A Security-only self-benchmark.** The Common Criteria (CC1-CC9) are a well-known, auditor-oriented yardstick. Rating the company against them gives the majority owner, the cyber insurer's underwriter, and the larger office tenants (whose own vendor reviews increasingly ask landlords about building system security) a second view of the program in terms they recognize, alongside the CPG 2.0 view in P03. Only Security is in scope:
- **Availability:** assessed against CPG 2.0 goals 3.O and 6.A and the BIA (P03, P05). Nobody has asked for commitments in TSC form.
- **Confidentiality and Privacy:** personal information duties come from Fla. Stat. 501.171 and lease clauses. The company makes no TSC-style commitments.
- **Processing Integrity:** not relevant to a landlord's tenants.

**B. Third-party risk management.** The access control and video platform vendor runs the cloud service behind every door, badge, and camera, and holds tenant employee names, badge photos, and access history. Its SOC 2 Type 2 report is the evidence for the controls the company inherits (P02, P04). The company reviews it every year (SA-9, POL-01 4.8).

The BAS integrator and the MSP are the company's most important remote-access vendors, but neither has a SOC 2 report. Their security is being handled through the security addendum and an annual questionnaire instead (POAM-018).

## 2. System description (scope)
- **Services:** leasing and operation of three Florida properties for 101 tenants: building environmental control, physical access control, video surveillance, tenant services, and billing.
- **Infrastructure and software:** the Building Automation and Access Control System (SSP, P02), the cloud tenant and SaaS services (P04), and the corporate network.
- **People:** 60 employees, the MSP, both integrators, and the guard contractor.
- **Data:** tenant employee credential and access data, video, visitor ID scans, employee HR data, tenant bank details, BAS programs and building drawings.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 19 | 9 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles and risk acceptance authority are designated
- CC3.1 and CC3.2: objectives (CPG 2.0 baseline) and the risk assessment are done
- CC4.2: deficiencies are tracked in the POA&M
- CC6.4: physical access to the server room and engineering rooms

**Not ready:**
- CC2.1: no OT inventory, diagrams, or central logs
- CC3.4: significant changes (the vendor-enabled video analytics) were not risk-assessed
- CC6.1, CC6.3, and CC6.6: BAS logical access, late removal and excess privileges, and the integrator's always-on tool (the same gaps as P01 R-001 and R-003)
- CC7.1 and CC7.2: no OT vulnerability or event monitoring
- CC7.5: BAS recovery not possible with confidence (P01 R-002)
- CC8.1: no change management for BAS programs or vendor features

The pattern matches P03 and P07: governance and physical security are in reasonable shape, while OT technical controls are not.

## 4. Findings from the platform vendor report (Part B)
- **Opinion:** Type 2, unqualified, period ending 2026-03-31. One exception (a production change without documented approval), remediated.
- **The analytics features are outside the report.** Tailgating detection and face verification were released in 2026, after the report period. The report gives no assurance about them. This supports the P10 conditions on AI-001 and the rejection of AI-002.
- **Availability:** the vendor's RPO of 1 hour meets the BIA. Its RTO of 4 hours does not meet the 2-hour target for badge administration (BP-01). The company accepts this because door controllers keep working on cached credentials for up to 72 hours and guards cover entrances (P01 R-017, accepted by the COO).
- **Controls the company must run.** The report lists complementary user entity controls: administrator account management, SSO with MFA, administrator log review, and security of the on-site devices and networks. The company meets MFA. **It does not yet meet least privilege (9 full administrators, POAM-012), log review (POAM-015), or device security (POAM-006, POAM-016).** The vendor's controls only protect the company once those gaps close.
- **Breach notice.** The terms of service give 72 hours after confirmation. Florida law separately requires a third-party agent to notify the company no later than 10 days after determining a breach (Fla. Stat. 501.171(6)(a)). The company will ask for 24-hour notice at renewal.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.1, CC1.2, CC1.4, CC1.5, CC2.2, CC2.3, CC3.3, CC3.4, CC4.1, CC5.3, CC6.1, CC6.2, CC6.3, CC6.5, CC6.7, CC7.4, CC8.1, CC9.1, CC9.2 | Policy acknowledgments, owner briefing minutes, gateway session records, MFA reports, termination and badge review records, destruction certificates, change tickets, quarterly POA&M reviews, tabletop report, contingency plan, signed security addenda |
| 2027 Q1 | CC2.1, CC5.1, CC5.2, CC6.6, CC6.8, CC7.1, CC7.2, CC7.3, CC7.5 | OT inventory and diagrams, firewall change records, scan reports, log reviews and alerts, restore test records, BAS upgrade records |

**Next step:** repeat this self-benchmark in August 2027 with the annual control assessment (P07), and report both to the majority owner.

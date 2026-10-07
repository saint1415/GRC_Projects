# SOC 2 Readiness Summary: Cris Santos Company | Dams | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensee of the fictional Cypress Fork Hydroelectric Project) |
| Tier / Vertical | Small / Dams |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is AICPA's |
| Categories in scope | Security (CC1-CC9) only, as a self-benchmark |
| Part A | Security-only self-benchmark of the company (`soc2-readiness.csv`) |
| Part B | Review of the instrumentation data platform vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Target report | None. No SOC 2 examination is planned |
| Prepared | 2026-08-20 by the IT Manager with the Controls Engineer and Chief Dam Safety Engineer |

## 1. Why SOC 2 (or an alternative) for this organization
**The company is not a service organization for its customers, so a SOC 2 report is not the right assurance product.**
- Its main customer, the offtaker, buys electricity. The offtaker's control center receives telemetry from the plant's RTU; the company does not host, process, or operate anything for the offtaker.
- Its field services customers (other dam owners) receive on-site mechanical work on gates and hoists. Crews do not connect to or operate customer control systems and do not hold customer data.
- Recreation customers pay through the reservation vendor's hosted page.

No customer has asked for a SOC 2 report, and the vertical overlay lists no sector alternative to SOC 2. The assurance that matters for this company is **regulatory**: the FERC Security Program (inspections, the Annual Security Compliance Certification Letter, and Form 3), analyzed in P03.

The Trust Services Criteria are still useful here for two reasons:

**A. Security-only self-benchmark.** The Common Criteria give the Vice President of Operations a familiar, outside yardstick to cross-check the FERC-driven program. It shows gaps FERC's documents do not ask about directly, such as fraud risk (CC3.3), communication of policies (CC2.2), and board-level oversight (CC1.2). Availability, Confidentiality, Processing Integrity, and Privacy were left out: plant availability and CEII protection are already assessed against FERC and Part 12 requirements in P03 and P05, and there are no customer commitments to measure against.

**B. Third-party risk management.** The instrumentation data platform (SaaS) holds the company's dam safety readings and runs the AI anomaly module assessed in P10. Its SOC 2 Type 2 report is the main evidence for the controls the company relies on there (SA-9). The company reviews it every year.

## 2. System description (scope)
- **Services:** hydroelectric generation and dam operation at the Cypress Fork project; hydro field services; recreation.
- **Infrastructure and software:** the PCDMS (P02) plus the corporate network, identity provider, productivity suite, cloud tenant, and business SaaS (P04).
- **People:** 187 employees, the MSP (corporate only), the SCADA integrator, and the governor and excitation vendor.
- **Data:** CEII and security-sensitive documents, instrumentation and historian data, employee personal information, business records.
- **Procedures:** POL-01 to POL-05, the P08 runbook, the EAP, and the FERC Security Plan.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 18 | 10 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:** CC1.3 (roles designated), CC3.1 and CC3.2 (objectives and risk assessment), CC4.1 (independent assessment), CC4.2 (deficiencies tracked).

**Not ready:**
- CC2.1: no OT asset inventory
- CC3.4: the 2024 remote-operation change was never risk-assessed
- CC6.1, CC6.2, CC6.3, and CC6.6: OT access and boundary (shared accounts, password-only VPN, CEII open to all, bypassed firewall)
- CC7.1, CC7.2, and CC7.3: no OT vulnerability management, monitoring, or event triage
- CC7.5: OT recovery never tested

The results match P03 and P07: the weak area is the control system, not the corporate side.

## 4. Findings from the instrumentation vendor report (Part B)
- **Opinion:** Type 2, unqualified, period ending 2026-03-31. One exception (a late quarterly access review for vendor support staff), remediated.
- **Scope gap:** the AI anomaly module was released after the report period, so **no SOC 2 evidence covers it yet**. P10 relies on the company's own acceptance tests until the next report.
- **Availability:** the stated RTO of 8 hours is longer than the BIA's 4 hours for BP-02. That is acceptable only because raw readings stay in the data loggers and the OT historian, and technicians can read instruments by hand (P05). The dependency is recorded, not ignored.
- **Controls the company must run** (complementary user entity controls): user management through SSO (in place), a quarterly review of platform user activity (first due 2026-10-31), validation of data sent to the platform (planned at the DMZ replica), and the company's own dam safety decision process. The last one matters most: **the vendor's report says the customer, not the vendor, is responsible for dam safety decisions made from platform outputs.** That is the basis for the human-review rules in P10.
- **Follow-ups:** a contract clause against using company data to train other customers' models; 24-hour incident notice at renewal; an updated bridge letter before 2026-12-31.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1-6.3, CC6.6, CC6.7, CC2.2, CC3.4, CC8.1, CC7.3, CC7.4 | Jump host and MFA configuration, named-account list, firewall rule set, policy acknowledgments, change log, tabletop report |
| 2027 Q1 | CC2.1, CC7.1, CC7.2, CC7.5, CC9.1, CC9.2 | OT inventory, vulnerability assessment report, monitoring alerts and reviews, restore test record, OT vendor reviews |
| 2027 Q2 | CC5.2, CC1.2, CC3.3 | SCADA upgrade records, quarterly oversight minutes, updated risk register |

Progress is reported through the POA&M (P07), which also serves as the FERC Section 9 plan and schedule. The self-benchmark will be repeated in July 2027 with the annual risk assessment.

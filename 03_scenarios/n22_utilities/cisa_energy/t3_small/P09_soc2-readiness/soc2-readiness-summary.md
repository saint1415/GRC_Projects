# SOC 2 Readiness Summary: Cris Santos Company | Energy | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (intrastate natural gas transmission pipeline operator) |
| Tier / Vertical | Small / Energy |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only, as a self-benchmark |
| Target report | None. The company is not a service organization and does not plan a SOC 2 examination |
| Part A | Security-only self-benchmark (`soc2-readiness.csv`) |
| Part B | Review of the managed service provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-10 by the IT Manager |

## 1. Why SOC 2 (or an alternative) for this organization
**The company is not a SOC 2 service organization.** SOC 2 reports on controls at a company that provides services to other businesses in a way that affects those businesses' own information systems. Cris Santos Company transports natural gas. Its customers (two LDCs, a power plant, and six industrial plants) depend on the gas, not on company systems that process their data. No customer has asked for a SOC 2 report, and none would expect one from a pipeline operator.

**The assurance alternative named for this vertical does not apply either.** The overlay names TSA pipeline security directive compliance reviews, but those are only for TSA-designated pipelines, and this pipeline is not designated (P03). Oversight of the control room comes from FPSC pipeline safety inspections under 49 CFR 192.631, which are not cybersecurity assurance.

**So the company uses SOC 2 in two narrower ways:**
- **A. Security-only self-benchmark.** The Security criteria (CC1-CC9) are a widely understood yardstick. Scoring against them gives the President and the LDC customers, who have begun sending supplier security questionnaires, a short, familiar summary of where the company stands. Availability, Confidentiality, Processing Integrity, and Privacy are marked not applicable. Those categories describe commitments a service organization makes to its customers, and the company makes none.
- **B. Supplier assurance.** The MSP has administrator access to every business endpoint through its remote monitoring and management (RMM) tool. A compromise of that tool is P01 risk R-016. The MSP's SOC 2 Type 2 report is the best available evidence for the MSP's controls, and reviewing it each year is part of SA-9 (P03 G-039).

Why not other options:
- **ISA/IEC 62443 or a third-party OT assessment:** more useful than SOC 2 for the pipeline itself. Planned as the architecture review that SD 02G Section III.G would require every two years if TSA designated the pipeline (readiness only).
- **A formal SOC 2 examination:** no customer need, and the controls have not operated long enough for a Type 2 period.

## 2. System description (scope)
- **Services:** intrastate natural gas transportation, gas control, scheduling, measurement, and billing.
- **Infrastructure and software:** the Pipeline SCADA and Gas Control System (P02), business IT, the cloud tenant, and SaaS services (P04).
- **People:** 60 employees, the MSP, and the SCADA integrator.
- **Data:** SCADA and measurement data, customer contracts and nominations, and employee personal information.
- **Procedures:** POL-01 to POL-05, the P08 runbook, and the control room management manual.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 20 | 8 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles are designated
- CC3.1 and CC3.2: objectives are set and risks analyzed
- CC4.2: deficiencies are tracked
- CC5.1: controls are selected from risk

**Not ready:**
- CC2.1: no security information collected
- CC6.3: late removal and no access reviews
- CC6.5: no certified disposal
- CC7.1 and CC7.2: no OT change detection, vulnerability monitoring, or anomaly monitoring
- CC7.5: SCADA recovery unproven (the same gap as P01 R-004)
- CC8.1: SCADA changes outside change control
- CC9.2: no supplier security terms

The pattern matches P03 and P07. Governance and risk work done in 2026 is ready. Operational security for OT is not.

## 4. Findings from the MSP report (Part B)
- **Opinion:** Type 2, unqualified, covering 12 months ending 2026-05-31. A bridge letter covers through 2026-08-31.
- **One exception matters to this company.** For 3 weeks, MFA was not enforced on 2 of 40 sampled technician accounts on the RMM tool. That tool can push software to every company endpoint. The exception was remediated, but the company will ask for evidence that MFA is enforced for its own tenant.
- **Controls the company must run.** The report lists controls the customer must operate for the MSP's controls to work (complementary user entity controls): approving technician access, telling the MSP about departures, restricting which systems get RMM agents, and reviewing monthly reports. Two of these link to company gaps:
  - Departure notice is part of POAM-001.
  - The rule that **no RMM agent may be installed in OT** (P04 finding 5) is what keeps an MSP compromise out of the pipeline.
- **Carve-outs.** The EDR platform and the RMM tool are subservice organizations excluded from the report. The company will ask for their assurance summaries.
- **Follow-ups:**
  - Negotiate 24-hour incident notice (the report states 72 hours) in the security addendum (POAM-018).
  - Confirm the MSP has no administrator access to the cloud backup account.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1, CC6.2, CC6.3, CC6.6, CC9.2, CC2.2, CC1.1 | Named integrator accounts with MFA, OT access approvals, departure tickets, signed supplier addendums, policy acknowledgments |
| 2027 Q1 | CC2.1, CC7.1, CC7.2, CC7.3, CC7.5, CC6.8, CC7.4 | OT sensor alerts and reviews, KEV reviews, restore test record, HMI allowlisting report, tabletop report |
| 2027 Q2 | CC8.1, CC6.5, CC6.7, CC3.4 | SCADA change records with P2P verification, destruction certificates, SCADA upgrade risk review |

**Answer to customer questionnaires:** send this summary, the Security readiness table, and the P07 POA&M. Commit to an updated self-benchmark in September 2027.

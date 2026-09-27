# SOC 2 Readiness Summary: Cris Santos Company | Utilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electric distribution utility, NERC-registered Distribution Provider) |
| Tier / Vertical | Small / Utilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Internal benchmark; no CPA-issued SOC 2 report is planned |
| Part A | Security-only readiness benchmark (`soc2-readiness.csv`) |
| Part B | Review of the AMI vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-28 by the IT Manager, with the Customer Service Manager for Part B |
| Approved | President and CEO, 2026-09-04 |

## 1. Why SOC 2 (or an alternative) for this organization
**SOC 2 is not the company's assurance mechanism.** SOC 2 reports on controls at a *service organization*, a company that provides services to other businesses whose own controls depend on it. This company sells electricity to homes and businesses. No customer, lender, wholesale supplier, or transmission owner has asked it for a SOC 2 report.

**The assurance that regulators rely on is NERC CIP compliance monitoring.** For the low impact relays at Substation N and Substation E, SERC's audits and the company's own self-report (P03) are the mechanism. The vertical overlay names this as the sector's alternative to SOC 2. That scope is 8 relays, so it says little about the SCADA, OMS, AMI, or corporate systems.

SOC 2 appears here for two practical reasons:

**A. Security-only internal benchmark.** The Security criteria (CC1-CC9) give the board one broad yardstick for the whole program, IT and OT, using work already done in P01, P02, P06, and P07. It complements the voluntary NIST CSF 2.0 and SP 800-82 Rev. 3 benchmark in P02.

Other options considered:
- **A formal SOC 2 audit:** no one requires it, and it would cost more than the security fixes it would measure.
- **Relying on CIP alone:** CIP reaches only the two BES substations.
- **The DOE Cybersecurity Capability Maturity Model (C2M2):** a strong, free fit for utilities. It is planned for 2027 once the High POA&M items are closed, and it would replace this benchmark.

**B. Third-party risk management.** The AMI vendor runs the head-end that can remotely connect and disconnect 72,000 meters. A compromise there could cut power to thousands of customers at once (P01 R-010). Its SOC 2 Type 2 report is the evidence for the controls the company inherits (P04). The CIS vendor's report was reviewed in 2026-05 and is on file.

## 2. System description (scope)
- **Services:** electric distribution operations and restoration, metering, customer service, and billing.
- **Infrastructure and software:** the Distribution Operations Platform (SSP, P02), the cloud tenant (P04), and the corporate network, identity provider, and SaaS services around it.
- **People:** 250 employees, the SCADA vendor, the relay testing contractor, and the SaaS vendors.
- **Data:** grid control data, relay settings, outage records, customer personal information, and usage data.
- **Procedures:** POL-01 to POL-05, the P08 OT runbook, the CIP low impact plan, and the storm restoration plan.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 22 | 7 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: the Information Security Lead, CIP Senior Manager, and delegate are designated
- CC3.1 and CC3.2: objectives are set and the risk assessment covers IT and OT
- CC4.2: deficiencies are tracked in the POA&M and CIP issues were self-reported

**Not ready:**
- CC6.1 and CC6.6: shared OT accounts, no MFA on the jump host, and standing vendor access (the same gap as P01 R-001)
- CC7.1 and CC7.2: no OT vulnerability monitoring or security monitoring
- CC7.5: SCADA recovery unproven (R-006)
- CC8.1: no change control for relay settings or gateway access lists
- CC3.4: Substation E went live without a security review (the P07 new finding)

The weakest area is **CC6.6, CC7.2, and CC8.1 together**: nobody controls, watches, or records what enters the OT network. The same findings drive the CIP-003-9 self-report (P03).

## 4. Findings from the AMI vendor report (Part B)
- **Opinion:** Type 2 (Security and Availability), unqualified, for 12 months to 2026-03-31. One remediated change-approval exception.
- **Availability:** the stated 8-hour recovery time and 1-hour recovery point **meet the BIA** (P05 BP-05 RTO 48 h, RPO 24 h).
- **Bulk disconnect is the customer's job.** The report shows that bulk-command limits and two-person approval are optional features the customer must turn on. The company has not turned them on, and 9 users can issue remote disconnects.
- **Controls the company must run (CUECs):**
  - user and role management
  - MFA through the identity provider (in place)
  - approval of bulk connect and disconnect commands (**open gap**, P01 R-010)
  - review of user activity reports (**open gap**)

  **The vendor's controls only protect the company once these gaps are closed.**
- **Follow-ups:**
  - Obtain a bridge letter to 2026-09-30.
  - Ask how meter and collector firmware is signed.
  - Negotiate 24-hour incident notice at the 2027-03 renewal. Fla. Stat. 501.171(6) sets 10 days as the outer limit for a third-party agent.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1, CC6.2, CC6.6, CC3.4, CC7.3, CC7.4, CC2.2 | Named OT and vendor account records, session approvals, MFA configuration, commissioning checklists, tabletop report, policy acknowledgments |
| 2027 Q1 | CC7.1, CC7.2, CC6.8, CC8.1, CC5.2 | OT monitoring alerts and weekly reviews, vulnerability review records, kiosk scan logs, change records for relays and gateways |
| 2027 Q2 | CC7.5, CC9.1, CC9.2, CC1.2, CC2.3 | Restore test and failover records, SCADA cyber recovery procedure, vendor security addenda, board minutes |

**Next benchmark:** replace this self-assessment with a DOE C2M2 self-evaluation in 2027 Q3, after the High POA&M items are closed.

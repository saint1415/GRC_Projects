# SOC 2 Readiness Summary: Cris Santos Company | Transportation Systems | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (Class III short line freight railroad) |
| Tier / Vertical | Small / Transportation Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (Common Criteria CC1-CC9) only, as a self-benchmark |
| Target report | None. No SOC 2 examination is planned (see section 1) |
| Part A | Security-only readiness self-benchmark (`soc2-readiness.csv`) |
| Part B | Review of the PTC back office vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager with the Vice President of Operations |

## 1. Why SOC 2 for this organization
**The railroad is not a SOC 2 service organization.** SOC 2 reports on controls at a company whose services affect its customers' own systems and internal controls. The railroad moves freight for 45 shippers under tariffs and contracts. No shipper relies on the railroad's IT controls for its own financial reporting or system security. No shipper or the Class I has asked for a SOC 2 report, and the vertical overlay names no SOC 2 alternative for rail. Assurance in this sector comes from regulators instead: TSA (Security Coordinator, reporting, RSSM rules) and FRA (safety rules, including PTC).

SOC 2 still earns a place here for two reasons:

**A. Security-only self-benchmark.** The Common Criteria are a well-understood yardstick that insurers, lenders, and larger shippers recognize. Rating the railroad against them:
- gives the cyber insurer's renewal questionnaire a structured answer;
- cross-checks the CSF 2.0 benchmark in P03 from a second angle;
- uses evidence already collected in P02, P06, and P07.

Availability, Confidentiality, Processing Integrity, and Privacy are out of scope because the railroad makes no such commitments to user entities. Its availability goals are set in the BIA (P05), not in customer contracts.

**B. Third-party risk management.** The railroad depends on the PTC back office vendor to keep interchange running (P05 BP-03; P02 SA-9). That vendor **is** a service organization for the railroad, so its SOC 2 Type 2 report is the right evidence. Reviewing it every year is part of POL-01 4.7 and CC9.2.

## 2. System description (scope)
- **Services:** freight rail service on 186 route miles plus the trackage-rights run to interchange.
- **Infrastructure and software:** the Train Dispatch and PTC Operations Platform (SSP, P02), with the TMS, the cloud tenant, and office systems (P04).
- **People:** 250 employees, the MSP, and the dispatch system vendor.
- **Data:** movement authority, PTC operational data, RSSM car location data, SSI, and employee personal information.
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
- CC1.5: owners named for every policy and POA&M item
- CC3.1 and CC3.2: objectives set and risk assessment done (P01, P05)
- CC4.2: deficiencies tracked in the POA&M
- CC5.1: control selection documented in the SSP

**Not ready:**
- CC3.3: fraud risk not assessed (the 2025 payment redirection attempt)
- CC6.1 and CC6.3: no MFA on VPN and server administrators; late account removal; SSI open to all office staff
- CC6.5: no media disposal process
- CC7.1, CC7.2, and CC7.3: no vulnerability scanning, monitoring, or event triage
- CC7.5: no tested recovery (the same gap as risks R-003 and R-005)
- CC8.1: no change management for operations systems

The Not ready criteria line up with the High POA&M items in P07. Closing POAM-002 to POAM-012 would move most of them to Partially ready or Ready.

## 4. Findings from the PTC back office vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, 12 months ending 2026-03-31. One change-approval exception, remediated with an automated gate.
- **Availability:** the system description shows separate processing sites and an annual disaster recovery test, which **likely meets** the BIA for interchange (RTO 24 h). But nothing is contractual, and the railroad has no copy of the vendor's prioritized service restoration plan that 49 CFR 236.1033(f) expects the railroad "or its vendor or supplier" to have.
- **Controls the railroad must run.** The report lists complementary user entity controls: named portal users with MFA, prompt removal of departed users, accurate locomotive, crew, and consist data, secure customer workstations, and telling the vendor about suspected compromise. Three are open gaps at the railroad: user removal (POAM-001), consist accuracy (P01 R-015), and the PTC workstation used for email and browsing (POAM-019). **The vendor's controls only protect the railroad once those gaps close.**
- **Follow-ups:**
  - Obtain the bridge letter through 2026-09-30.
  - Obtain the restoration plan and add restoration targets to the contract (POAM-005, POAM-018).
  - Negotiate security incident notice within 24 hours, so the railroad can meet its own 24-hour TSA reporting duty.
  - Ask how the vendor oversees its carved-out hosting and messaging network providers.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.3, CC2.2, CC3.3, CC6.1, CC6.3, CC6.6, CC7.3, CC7.4, CC9.2 | Designation letter, briefing records, MFA enforcement reports, termination tickets, jump host session logs, tabletop report, signed vendor addenda |
| 2027 Q1 | CC1.4, CC6.5, CC6.8, CC7.1, CC7.2, CC7.5, CC8.1 | Destruction records, EDR alerts and tickets, scan reports, restore test and manual dispatch drill records, change log, role-based training records |
| 2027 Q2 | CC6.4, CC6.7, CC9.1 | Rekey records, APN configuration, North Yard standby site test |

**Next self-benchmark:** April 2027, shared with the cyber insurer at renewal.

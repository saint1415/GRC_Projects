# SOC 2 Readiness Summary: Cris Santos Company | Government Services and Facilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings) |
| Tier / Vertical | Small / Government Services and Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Target report | Readiness self-assessment now; SOC 2 Type 1 targeted for 2027-06-30, then a Type 2 with a 6-month period |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`) |
| Part B | Access control and video platform vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager; statuses updated 2026-08-31 |

## 1. Why SOC 2 for this organization
**The company is a service organization for its county and state customers.** It operates their building automation and access control systems on its own platform and holds their cardholder data and security system layouts. The customers' own security depends on the company's controls. That is the situation SOC 2 is designed to report on.

Two customer requests make it concrete:
- **County IT audit.** The county's security addendum asks for a SOC 2 report or an equivalent readiness assessment. This checklist and the POA&M (P07) are the equivalent for 2026.
- **State annual independent assessment.** The state exhibit already requires an annual independent assessment against SP 800-53 Moderate. The P07 assessment meets it for 2026. A future SOC 2 report could be mapped to the same controls using the AICPA TSC-to-SP 800-53 mapping, so one audit serves both customers.

**Why not an audited SOC 2 now.** A Type 2 report needs controls that have operated for a period, typically 6 to 12 months. Most of the company's controls were defined in August 2026, and several (remote access, backups, monitoring) are still being built.

**Alternatives considered:**
- **GovRAMP:** for cloud service providers selling to state and local governments. The company is not a cloud provider. Its access control SaaS vendor is the party GovRAMP would apply to (Part B).
- **FedRAMP:** not applicable. The company operates no system for GSA; GSA's building systems run under GSA's own ATO.
- **CMMC:** a DoD program. The company has no DoD contracts.

**Why Availability and Confidentiality.** The customers rely on the ROC and access control administration staying available (BIA BP-01 and BP-02) and on security plans, cardholder data, and GSA CUI staying confidential. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** remote monitoring and operation of building automation and access control for the state and county; badge administration; video support.
- **Infrastructure and software:** the Facility Operations Technology Platform (SSP, P02): BAS supervisory platform, access control and video tenants, jump host, cloud tenant, site edge firewalls, ROC workstations.
- **People:** 60 employees, including 4 ROC operators, 6 controls and security systems technicians, and the integrator (subcontractor).
- **Data:** cardholder records for about 5,000 people, 140 face templates (pilot), building drawings and security system layouts, GSA CUI drawings (federal contract).
- **Procedures:** POL-01 to POL-05 and the P08 runbook.
- **Excluded:** GSA's building systems (GSA-owned and authorized).

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 21 | 8 | 0 |
| Availability (A1, 3) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles and authority are designated
- CC3.1 and CC3.2: objectives and risk assessment are done
- CC4.2: deficiencies are tracked in the POA&M

**Not ready:**
- CC6.1 and CC6.6: remote access to OT bypasses controls; edge firmware is behind (the same gap as risk R-001)
- CC6.3: late removal and excess privilege
- CC7.1 and CC7.2: no vulnerability scanning or monitoring
- CC7.5, A1.2, and A1.3: recovery is not planned or tested (R-006, R-008)
- CC8.1: no change management for BAS programs and door schedules
- CC9.2: subcontractors are not bound or reviewed

## 4. Findings from the access control vendor report (Part B)
- **Opinion:** Type 2, unqualified. One change management exception at the vendor, remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 15 minutes **meet the BIA** for access control administration (RTO 8 h, RPO 1 h).
- **The face verification module is not covered.** It launched after the report period. The company needs written assurance on template encryption, no vendor training on the templates, and per-person deletion before the pilot can continue (P10 condition).
- **Controls the company must run** (complementary user entity controls): prompt removal of administrators, MFA for administrators, review of administrator activity, and a secure local network for door controllers. Three of the four are open gaps at the company: removal (POAM-011), activity review (POAM-015), and segmentation at the county service centers (POAM-004). **The vendor's controls only protect the customers once those gaps close.**
- **GovRAMP:** the vendor says its GovRAMP verification is in progress. Not verified; check the GovRAMP list before renewal.
- **Follow-ups:** negotiate 24-hour incident notice (the vendor offers 72 hours, but the company owes its customers 24 hours).

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1, CC6.3, CC6.6, CC2.2, CC7.3-7.4, CC9.2, C1.1 | Jump host session logs, termination tickets, firmware records, policy acknowledgments, tabletop report, signed subcontractor addenda |
| 2027 Q1 | CC7.1-7.2, CC7.5, CC8.1, A1.2-A1.3, CC6.8 | Scan reports, log review records, restore test records, change tickets, manual-mode exercise report |
| 2027 Q2 | CC1.2, CC3.3, CC4.1, C1.2 | Owner review minutes, updated risk assessment, monthly metrics, retention schedule |

**Response to the county:** send this summary, the readiness checklist, and the POA&M (P07) by 2026-10-31. Commit to a SOC 2 Type 1 by 2027-06-30 if the Q4 and Q1 items close on schedule.

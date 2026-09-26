# SOC 2 Readiness Summary: Cris Santos Company | Agriculture | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (diversified precision-agriculture crop farm) |
| Tier / Vertical | Small / Agriculture, Forestry, Fishing and Hunting |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only, as a self-benchmark |
| Target report | None. The farm is not a service organization and will not seek a SOC 2 report |
| Part A | Security-only self-benchmark against the Trust Services Criteria (`soc2-readiness.csv`) |
| Part B | Review of the farm management and irrigation software (FMIS) vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Operations and Technology Manager |

## 1. Why SOC 2 for this organization
A crop farm is **not** a SOC 2 service organization. It sells produce and peanuts; it does not operate systems or process data for other businesses, and no customer has asked it for a SOC 2 report. The assurance its buyers ask for is about food safety: the distributor requires an annual third-party food safety (GAP) audit, which the farm passed in March 2026. That audit does not cover cybersecurity. The vertical overlay lists no assurance alternative to SOC 2 for agriculture.

The Trust Services Criteria still matter to the farm in two ways:

**A. Security self-benchmark.** The Security criteria give an outside yardstick for the same program that P03 measured against CSF 2.0. Where both find the same gap (for example, account removal, monitoring, or recovery), the finding is stronger. No CPA opinion is sought, and none is implied.

**B. Supplier oversight.** The farm's most important system, SYS-01, is a vendor SaaS. The vendor's SOC 2 Type 2 report is the main evidence for the controls the farm inherits (P02, P04), and supplier assessment (GV.SC-07) is a High priority in the farm's CSF 2.0 Target Profile. The report had been on file since 2025 but was never read (P03 G-028, POAM-016).

## 2. System description (scope)
- **Services:** growing, harvesting, packing, and selling produce and peanuts; the internal services that support them (irrigation control, harvest tally, food safety records, payroll).
- **Infrastructure and software:** the Farm Management and Irrigation Control Platform (SSP, P02), the cloud tenant (P04), and the pump-house and field OT.
- **People:** 15 employees, the MSP, and the irrigation integrator.
- **Data:** Produce Safety records, H-2A earnings records, worker and employee personal information, operator location history, yield and buyer data.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 16 | 12 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

Availability and Confidentiality are outside this benchmark by decision. They are covered by the BIA (P05) and the CSF 2.0 and Fla. Stat. 501.171 rows of the gap analysis (P03). Processing Integrity and Privacy do not apply, because the farm processes nothing for others.

**Ready (5):**
- CC3.1 and CC3.2: objectives and risk tolerance set; 2026 risk assessment done
- CC3.3: fraud risk considered (payment diversion, misuse of tally records)
- CC4.2: deficiencies tracked on the POA&M
- CC6.6: the firewall blocks unsolicited inbound traffic

**Not ready (12):**
- CC2.1: no inventory of OT, IoT, or data
- CC3.4 and CC8.1: no change assessment or change control, including the integrator's PLC changes
- CC5.2: no general IT controls over the OT
- CC6.3: departed accounts left active; over-shared personnel files
- CC6.5: no disposal control
- CC6.8, CC7.1, CC7.2, CC7.3: no malware alert handling, scanning, monitoring, or event evaluation
- CC7.5: recovery unproven (the same gap as P01 R-003)
- CC9.2: supplier risk not managed

The pattern matches P03 and P07: the farm has started to govern and assess risk, but **controls over the OT, over suppliers, and over detection and recovery are not operating**.

## 4. Findings from the FMIS vendor report (Part B)
- **Opinion:** Type 2, unmodified, for the 12 months ending 2026-03-31, covering Security and Availability. One change-approval exception at the vendor, remediated with a deployment approval gate.
- **Carve-out that matters:** the device connectivity service that carries commands to the pivot panels is run by a subservice organization and is **carved out**. That is the path an attacker would use to start or stop pivots through SYS-01. The farm will ask for the vendor's review of that provider.
- **Availability:** the stated RPO of 1 hour meets the BIA. The stated RTO of 8 hours does **not** meet the 6-hour RTO for irrigation (BP-01). The written manual irrigation procedure (POAM-004) carries the difference. A stated RTO goes into the contract at renewal (R-009).
- **Controls the farm must run (CUECs):** six were mapped. Five are open gaps at the farm: user removal (POAM-001), MFA on the mobile app (R-006), review of audit and change reports (POAM-010), protection of the tablets that run the app, and security of the field devices and network (POAM-006). **The vendor's controls only protect the farm's records and pivots once the farm closes these gaps.**
- **Incident notice:** "without undue delay," with no time frame. Seek a 72-hour term at renewal.
- **Follow-ups:** bridge letter received (to 2026-06-30); request the connectivity provider review; confirm the change-approval gate in the next report.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.3, CC2.2, CC2.3, CC6.2, CC6.3, CC7.3, CC7.4, CC8.1 | Security lead designation, signed acknowledgments (English and Spanish), breach contacts registered with agents, departure checklists, season-end access review, PLC change log, tabletop report |
| 2027 Q1 | CC2.1, CC5.2, CC6.1, CC6.5, CC6.7, CC6.8, CC7.1, CC7.2, CC7.5, CC9.2 | Inventory, OT baselines, segmentation change record, wipe records, EDR alerts and tickets, scan reports, restore test records, supplier terms |
| 2027 Q2 | CC1.2, CC1.5, CC3.4, CC4.1, CC5.1, CC5.3, CC9.1 | Quarterly owner review minutes, supplier checklists for new purchases, contingency plan and drill records |

**Use of this summary:** attach it, the readiness checklist, and the POA&M (P07) to the quarterly owner review. Update the self-benchmark in August 2027. If a buyer or lender ever asks for security assurance, send this summary with the CSF 2.0 gap analysis (P03) rather than commissioning a SOC 2 report.

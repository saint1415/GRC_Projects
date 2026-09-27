# SOC 2 Readiness Summary: Cris Santos Company Holdings | Manufacturing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Manufacturing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). Two readiness reports: the Medical Devices Device Connectivity Cloud (`soc2-readiness.csv`) and the Testing client portal and LIMS (`soc2-readiness-testing.csv`). Distribution is out of scope |
| Prepared | 2026-09-01 by the Group Chief Risk Officer's assurance team with the Medical Devices and Testing security and compliance leads; reviewed by the board risk committee 2026-09-15 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations build into their own control environment.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Medical Devices | Device Connectivity Cloud (SYS-D2) for about 1,300 hospitals | **Yes.** Hospitals are covered entities that rely on the DCC as their business associate and as part of their clinical systems | **In scope.** Existing annual Type 2 | Security, Availability; **Confidentiality added** from the current period | Type 2, 12 months ending 2027-06-30; report by 2027-09-30 |
| Medical Devices | Devices sold to hospitals (IX-4, IX-3, PM-7, US-2) | No. Products are regulated by FDA; hospitals rely on FDA clearance, labeling, and the customer security guide, not on a SOC report | Out of scope | n/a | n/a |
| Engineering and Product Testing Services | Client portal and LIMS holding client designs, test data, and unpublished vulnerability findings | **Yes, for this service line.** About 950 device makers entrust confidential data to it, and 41 clients asked for a SOC 2 report in 2026 | **In scope.** First readiness assessment | Security, Confidentiality | Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| Engineering and Product Testing Services | Test execution and reports | No. Validity of results is assured by laboratory accreditation | Out of scope | n/a | n/a |
| Distribution | Medical supply distribution, ordering portal, EDI | **No.** Customers buy products; they do not rely on Distribution's systems as part of their own control environment | **Out of scope** (reasons below) | n/a | n/a |

**Why Distribution is out of scope:**
1. **No user entities.** Hospitals and clinics buy supplies. Their reliance is on delivery and product quality under supply contracts, not on Distribution's controls over their data.
2. **Federal customers use a different assurance route.** VA and DoD rely on FAR 52.204-21 and, for DoD, a CMMC Level 1 status with an SPRS affirmation (P03). A SOC 2 report would not satisfy those clauses.
3. **EDI partners** rely on connection agreements and the EDI network provider's own SOC report.
4. **Customer questionnaires** are answered with the group security program description and the P03 and P07 results.
5. **Revisit trigger:** if Distribution starts hosting inventory or ordering systems for customers (for example, managed inventory inside hospitals with data held for them), assess whether a SOC 1 or SOC 2 report is needed.

**Other assurance options considered.** The vertical overlay names no standard alternative for manufacturing. For the DCC, hospitals also ask for HITRUST certification; the group decided SOC 2 remains the primary report because hospital contracts already require it. For Testing, laboratory accreditation covers technical competence and impartiality but not security controls over client data, so it does not replace SOC 2.

## 2. System descriptions (scope)
### 2.1 Device Connectivity Cloud (Medical Devices)
- **Services:** device telemetry ingestion, remote viewing and secondary alarm notifications, drug library and firmware distribution, and EHR interfaces for about 1,300 hospitals.
- **Infrastructure and software:** DCC on cloud provider A with warm standby on provider B; group identity (SYS-G1) and SOC (SYS-G2) carved in as internal shared services; the DEMS release repository is the only source of distributed firmware.
- **Subservice organizations (carve-out):** cloud providers A and B; the support ticketing and log analytics vendors (both under subcontractor BAAs).
- **Data:** PHI of about 9 million patients (24-month rolling retention) and device data.
- **Complementary user entity controls:** hospital SSO and MFA (including, from this period, MFA for administrators who publish drug libraries), user provisioning and removal, network isolation of devices per the customer security guide.

### 2.2 Testing client portal and LIMS (Testing)
- **Services:** client submission of test data and files, project tracking, report delivery, and access to findings.
- **Infrastructure and software:** client portal and findings vault on cloud provider A (separate account and keys); LIMS (SaaS); isolated test range (on premises, outside the system boundary except for exports to the vault).
- **Subservice organizations (carve-out):** cloud provider A; LIMS vendor.
- **Data:** client designs, test data, and unpublished vulnerability findings for about 950 clients.
- **Complementary user entity controls:** clients provision and remove their users, use MFA, and do not submit personal information.

## 3. Readiness results
### 3.1 Device Connectivity Cloud (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 30 | 3 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Partially ready:** CC2.3 (the complementary user entity controls do not yet require MFA for hospital administrators who publish drug libraries), CC6.3 (standing support access to all tenants' PHI), CC7.4 (no device-to-breach decision step in the PSIRT procedure; BAA terms register at 81%), and C1.2 (3 of 11 offboarded hospitals without destruction certificates).

**Adding Confidentiality mid-cycle.** Health systems asked for it in their 2026 renewals. The service auditor agreed it can be included for the period that began 2026-07-01, because encryption, classification, and tenant tagging have operated since before then. Expect the auditor to test C1.2 for exceptions in the first half of the period; automated deletion with certificates is due 2027-03-31.

**Processing Integrity** stays out of scope: the accuracy of device data is a design control under the QMSR, evidenced through FDA submissions, not a DCC service commitment.

### 3.2 Testing client portal and LIMS (`soc2-readiness-testing.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 20 | 11 | 2 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first-time report:** control environment, risk, monitoring, and most IT criteria are met by group common controls already evidenced for the DCC report.
**Not ready:** CC2.3 (no system description or written security commitments to clients) and CC6.3 (the information barrier: client material in a collaboration space open to 212 Medical Devices engineers; P07 AC-4 other than satisfied).
**Partially ready:** CC2.1, CC3.4, CC4.1, CC5.3, CC6.1, CC6.2, CC6.7, CC7.2, CC7.4, CC8.1, CC9.2, and C1.1. They cluster on the acquired laboratories (gap 3), the barrier (gap 5), PHI at intake (gap 6), and the AI drafting tool (gap 8).

**Why this matters beyond SOC 2.** For a testing laboratory whose clients are its parent's competitors, CC6.3 and C1.1 are the report. A Type 1 opinion with a barrier exception would undermine client trust more than having no report, so the Type 1 date is set after the barrier work (POAM-010) and a full division assessment are complete.

## 4. Remediation plan and evidence calendar
| Quarter | Division | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | DCC | CC2.3, CC7.4 | Updated system description and customer security guide; hospital notice; PSIRT 164.402 step; complete BAA terms register; tabletop record |
| 2026 Q4 | Testing | CC6.3, C1.1, CC3.4, CC8.1, CC9.2, CC5.3 | Collaboration space closure; barrier groups and attestations; AI tool change record and client consent clause; re-issued supplement |
| 2026 Q4 | Testing | CC2.1, CC6.7, CC7.2, CC7.4 | Intake scanning reports; data loss prevention rules; SOC barrier alerts; NDA terms in the matrix |
| 2027 Q1 | DCC | CC6.3, C1.2 | Just-in-time support access records; automated deletion certificates |
| 2027 Q1 | Testing | CC6.1, CC6.2, CC2.3 | Federation of acquired laboratories; system description and client security overview |
| 2027 Q2 | Testing | CC4.1; all in-scope criteria | Division assessment; Type 1 as of 2027-06-30 |
| 2027 Q3 | Both | All in-scope criteria | DCC report for the period ending 2027-06-30 (by 2027-09-30); Testing Type 2 period begins 2027-07-01 |

**Communication:** Medical Devices tells hospitals about the new Confidentiality category and the administrator MFA requirement with the 2026 Q4 customer notice. Testing sends the 41 requesting clients a readiness letter with the 2027 timeline and a description of the information barrier program.

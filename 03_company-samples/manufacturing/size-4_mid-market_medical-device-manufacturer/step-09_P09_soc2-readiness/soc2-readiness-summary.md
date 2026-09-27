# SOC 2 Readiness Summary: Cris Santos Company | Manufacturing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed connected medical device manufacturer) |
| Tier / Vertical | Mid-Market / Manufacturing (NAICS 334510) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| System | Connected Care Cloud (CCC) service, as provided to hospital customers |
| Categories in scope | Security (CC1-CC9), already reported; **Availability (A1) and Confidentiality (C1), to be added** |
| Target report | SOC 2 **Type 2** for 2027-04-01 to 2028-03-31 covering Security, Availability, and Confidentiality, report by 2028-05-31; interim Type 1 for all three categories as of 2027-03-31 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-04 by the vCISO and the Security Manager, using P02, P05, and P07 evidence; approved by the COO 2026-09-17 |

## 1. Why SOC 2 for this organization
The CCC is a service the company provides to about 290 hospitals, so for the CCC the company is a service organization and SOC 2 is the right assurance tool.

- **Today:** a SOC 2 Type 2 report on the Security category for 2025-04-01 to 2026-03-31 (unqualified, with 3 exceptions: access review timeliness, transfer role removal, and one late subcontractor review). The 2026-04-01 to 2027-03-31 period is under way with the same scope.
- **The request:** a group purchasing organization contract covering about 60 of the company's hospitals requires Availability and Confidentiality from contract year 2028. Several health system CISOs ask the same in security questionnaires, because hospitals rely on the CCC for remote monitoring and pump programming (P05 BP-01 and BP-02) and it holds their patients' PHI.
- **Why not add them now:** P07 found gaps in recovery testing (the CCC failover missed its 2-hour RTO), access reviews, privileged activity monitoring, and subcontractor BAAs. Adding Availability before failover is proven would produce an exception on A1.3 and likely CC7.5. The plan is to remediate through 2027 Q1, issue a Type 1 as of 2027-03-31, and start the expanded Type 2 period on 2027-04-01.

**What SOC 2 does not cover.** SOC 2 does not assess compliance with section 524B, the QMSR, or HIPAA. Hospitals also receive the customer security guide, disclosure statements, and SBOMs (P03 G-043). The plant and the device firmware are outside the SOC 2 system boundary, though the update service and the build and signing pipeline that deploy CCC code are inside it.

**Alternatives considered:**
- **Security only, as today:** does not meet the contract.
- **HITRUST certification:** some health systems accept it, but the contract names SOC 2.
- **Bridge letters and questionnaires only:** not acceptable to the purchasing organization's audit committee.

**Service auditor independence.** The examination is performed by an independent CPA firm that is not the co-sourced internal audit firm, so the P07 work does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Remote monitoring and secondary notifications, pump drug library and programming, AI-001 image analysis, HL7 and FHIR interfaces, firmware distribution |
| Infrastructure | The 7-account landing zone (P04), with the CCC production, shared network, security, build and signing, and backup accounts |
| Software | CCC services, the update service, the CI/CD pipeline and signing service that deploy CCC code |
| People | Cloud operations (12 site reliability engineers), CCC engineering, support, product security, IT and security, the MSSP |
| Data | PHI held for hospitals (about 2.4 million patients), device telemetry, drug libraries, firmware |
| Procedures | POL-01 to POL-05, the standards index, and the P08 runbooks |
| Subservice organizations (carve-out) | Cloud provider, identity provider, MSSP, repository SaaS. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls in the system description |
| Excluded | Plant OT and MES, device firmware, ERP, PLM, eQMS (the eQMS and PLM are reviewed as vendors in Part B) |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 18 | 12 | 3 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **20** | **14** | **4** | **23** |

**Ready (20):**
- governance and risk: CC1.1, CC1.2, CC1.3, CC1.5, CC2.1, CC2.2, CC3.1, CC3.2;
- monitoring and control design: CC4.1, CC4.2, CC5.1, CC5.2;
- access, boundary, and transmission: CC6.2, CC6.4, CC6.5, CC6.6, CC6.7, CC6.8;
- capacity and backups: A1.1, A1.2.

**Not ready (4):**
- CC6.3: annual reviews, transfers keeping roles, and standing all-tenant production access;
- CC7.2: no review of privileged activity or bulk exports; build and signing logs not in the SIEM;
- CC9.2: 2 subcontractors receive PHI without a BAA;
- A1.3: failover tested once and missed the 2-hour RTO.

Each maps to a P07 POA&M item. The Partially ready criteria depend mostly on standards being issued (P06), the change control fix (POAM-002), and incident process maturity (POAM-013).

**Why Security is mostly Ready but three criteria are Not ready.** The current Security report tested the controls against the 2024 commitments (annual reviews). The 2026 policies commit to quarterly reviews and just-in-time access, and the expanded report will be tested against those. Until they operate, the auditor would report exceptions.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.3, CC3.3, CC3.4, CC6.1, CC6.3, CC7.1, CC7.3, CC8.1, CC9.2, C1.1, C1.2 | System description draft with A and C commitments; transfer tickets; first quarterly access review; just-in-time logs; KEV automation reports; decision log; change forms; signed subcontractor BAAs; purge job verification |
| 2027 Q1 | CC1.4, CC5.3, CC7.2, CC7.4, CC7.5, CC9.1, A1.3 | Training records; STD-01 and STD-02; weekly privileged review records; tabletop report; automated failover test at 2 hours or less |
| 2027-03-31 | Type 1 (design) report for Security, Availability, and Confidentiality | Management's system description and assertion |
| 2027-04-01 to 2028-03-31 | Type 2 observation period | All recurring control evidence (quarterly reviews and failover tests, monthly scans, weekly privileged reviews, vendor reviews) |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee. The Director of Customer Support and Field Service gives the purchasing organization a quarterly status letter.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for 9 Common/Inherited and 33 Hybrid controls in the SSP (P02). This program makes that reliance evidence-based and is the core of the supplier standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | PHI at scale, privileged access to company systems (including plant OT), support for a High BIA process, or control over code that reaches devices | SOC 2 Type 2 (or equivalent independent assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited PHI or limited system access; supports Moderate or Low processes | Security questionnaire; SOC 2 if available; subcontractor BAA if any PHI | Every 2 years |
| **Tier 3** | No PHI and no system access | Contract terms only | At contract renewal |

Of 38 suppliers with system or data access, 11 are Tier 1 and 19 are Tier 2 under this approach. The CSV holds 7 Tier 1 reviews and 1 Tier 2 example. The remaining 4 Tier 1 reviews (support ticketing, ERP, payroll, and a critical software component supplier) are due by 2027-03-31 (POAM-014).

**Key findings:**
1. **Cloud provider:** unqualified Type 2 for all three categories. Its availability supports the CCC's 2-hour RTO **by design, but the company has not demonstrated it**. Failover and just-in-time access are company CUECs with open gaps (POAM-009, POAM-003).
2. **eQMS vendor:** **qualified opinion** on change management because it released an AI feature without documented testing. That is the AI-005 feature the company switched on without its own validation (P03 G-014; P10). The company must validate the feature or turn it off.
3. **MSSP:** unqualified Type 2 (Security only), with one missed 30-minute escalation. Log source coverage is the company's CUEC and is incomplete (OT, MES, build, PLM).
4. **Call-recording service:** no SOC 2 report and **no subcontractor BAA** although recordings can contain patient identifiers (POAM-014).
5. **Line equipment vendor:** no independent assessment and a persistent VPN into plant OT (POAM-005). Security terms and an assessment requirement are due at the 2027 renewal.

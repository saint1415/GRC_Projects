# SOC 2 Readiness Summary: Cris Santos Company | Manufacturing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (connected medical device manufacturer) |
| Tier / Vertical | Small / Manufacturing (NAICS 334510) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Target report | SOC 2 Type 2 for the Device Cloud Service; observation period 2027-01-01 to 2027-06-30; report expected by 2027-09-30 |
| Current report | SOC 2 Type 1 (Security only) as of 2026-03-31 |
| Part A | Device cloud readiness self-assessment (`soc2-readiness.csv`) |
| Part B | Cloud provider SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 by the IT Manager with the Cloud Operations Lead; statuses updated for the policy approvals of 2026-09-04 |

## 1. Why SOC 2 for this organization
The company is a **service organization** for its device cloud. Forty hospitals rely on it for remote monitoring, secondary alarms, EHR results, and firmware updates, and it holds PHI for them as a business associate. SOC 2 is the assurance these customers ask for:

**A. Customer demand.** Hospital security and procurement teams now ask for a **Type 2** report with **Availability** and **Confidentiality**, not the current Type 1 (Security only). A Type 1 shows controls are designed at one date. A Type 2 shows they operated over a period. Renewals are at risk without it (P01 R-011).

Other options considered:
- **Security questionnaires only:** hospitals already send them, and a Type 2 report would replace most of them.
- **HITRUST certification:** common in health care, but the hospitals asked for SOC 2, and HITRUST would add cost without meeting that request.
- **FDA 524B documentation:** it covers device cybersecurity for FDA. It does not give hospitals independent assurance over the device cloud's operations, so it complements SOC 2 rather than replacing it.

**B. Third-party risk management.** The device cloud inherits physical, hypervisor, and managed-service controls from its cloud provider (P02, P04). The provider's SOC 2 Type 2 report is the evidence for those controls, and the company reviews it every year (HIPAA 164.308(b), SA-9). The provider will appear in the company's own report as a **carved-out subservice organization**.

## 2. System description (scope)
- **Services:** remote patient monitoring and secondary alarm notification, results delivery to hospital EHRs, and signed firmware distribution for PM-2 monitors.
- **Infrastructure:** the Device Cloud Service on a public cloud tenant (SSP, P02; architecture, P04), the identity provider tenant, and the log analytics service.
- **Software:** the ingestion, processing, portal, HL7 interface, and update services, built through the company's CI/CD pipeline.
- **People:** the COO (system owner), Cloud Operations Lead, 14 cloud and DevOps engineers, the IT Manager, the Product Security Lead, and the support team.
- **Data:** PHI for about 380,000 patients (24-month retention), device certificates, and firmware images.
- **Procedures:** POL-01 to POL-05, the P08 runbook, and the device cloud procedures listed in the POA&M.
- **Not in the system:** the factory floor, the fielded monitors themselves (hospital-operated), and the build and signing server (an interconnected system outside the SSP boundary). Hospitals' own controls appear as complementary user entity controls: clinician account management, federation, and network protection for their monitors.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 17 | 6 | 0 |
| Availability (A1, 3) | 0 | 2 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |
| **Total (61)** | **11** | **20** | **7** | **23** |

**Ready (11):** CC1.1, CC1.3, CC1.5, CC3.1, CC3.2, CC4.2, CC5.1, CC6.2, CC6.4, CC6.6, and C1.2. The Type 1 work shows here: governance, risk assessment, provisioning, and boundary protection are designed and working.

**Not ready (7):**
- CC2.3: no public channel for vulnerability reports; BAA notice terms scattered
- CC6.3: standing all-tenant production access, no access reviews
- CC6.7: PHI flows to a log analytics vendor with no BAA
- CC7.2: no log review or security monitoring
- CC7.5 and A1.3: recovery never tested (the same gap as P01 R-016 and R-017)
- CC9.2: vendor oversight (the same log analytics vendor)

**Processing Integrity** was considered, because the device cloud processes vital signs and alarms. Hospitals did not ask for it in the first report. It is a candidate for the 2028 period. **Privacy** is excluded because the hospitals, as covered entities, administer privacy duties under HIPAA, and the BAAs set the company's obligations.

## 4. Findings from the cloud provider report (Part B)
- **Opinion:** Type 2, unqualified, for 2025-04-01 to 2026-03-31, covering Security, Availability, and Confidentiality. One change-approval exception at the provider, remediated.
- **Scope:** every managed service the device cloud uses, in both company regions, is in scope.
- **Availability:** the provider commits to service levels per managed service. It does not commit to recovering the company's workloads. **Meeting the BIA's 2-hour RTO and 15-minute RPO for BP-01 depends on the company's own restore and regional recovery design**, which has never been tested (POAM-012).
- **Controls the company must run (CUECs).** The report lists controls the customer must operate for the provider's controls to work: identity and access, MFA, key policies, backup configuration, network rules, and logging. Three are open gaps: production access (POAM-001), backup separation (POAM-013), and log review (POAM-008). **The provider's controls only protect the device cloud once those gaps close.**
- **Follow-ups:**
  - Request an updated bridge letter before 2027-01-01.
  - Record the provider's incident notice terms in the BAA terms register.
  - Consider customer-managed keys for the clinical data store.

## 5. Remediation plan and evidence calendar
A Type 2 auditor will test controls across the whole observation period, so each control must be operating **before 2027-01-01**. Evidence starts on that date.

| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.2, CC2.3, CC6.3, CC6.7, CC9.2, C1.1, CC7.3-7.4 | Policy acknowledgments, published CVD policy, just-in-time access tickets, first quarterly access review, log analytics BAA or migration record, tabletop report |
| 2026 Q4 to 2027 Q1 | CC7.1, CC7.2, CC7.5, A1.2, A1.3, CC5.2, CC6.8 | Weekly log review records, alert tickets, SBOM matching reports, restore test records, immutable backup configuration, image signing records |
| 2027 Q1 | CC1.2, CC1.4, CC3.3, CC3.4, CC4.1, CC8.1, A1.1 | Quarterly oversight minutes, role-based training records, updated risk assessment, change records with security impact, monthly metrics, capacity reviews |

**Decision point:** the COO will confirm on 2026-12-15 that every Not ready criterion is at least Partially ready with its control operating. If A1.3 (recovery testing) is not operating by then, the observation period moves to 2027-04-01, and the report date moves to 2027-12-31.

**Response to hospitals:** send the current Type 1 report, this summary, and the target report date. Hospitals that need more assurance before the Type 2 report can receive the POA&M (P07) under NDA.

# SOC 2 Readiness Summary: Cris Santos Company | Information Technology | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (cloud hosting and managed infrastructure provider) |
| Tier / Vertical | Small / Information Technology |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Examination target | SOC 2 Type 1 as of 2027-03-31, then a Type 2 period from 2027-04-01 to 2027-09-30 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Review of the DC-1 colocation provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 to 2026-09-04 by the IT Manager with the Controller; approved by the COO 2026-09-25 |

## 1. Why SOC 2 for this organization
The company **is a service organization.** It hosts customer workloads, runs managed services on customer servers, and serves customer DNS. Its controls are part of its customers' own control environments. A SOC 2 report is the normal way to give those customers assurance, so this is a real readiness assessment for a CPA examination, not a self-benchmark.

**Who asked:**
- **The 14 community banks.** The banks' vendor-management programs ask their critical technology service providers for an annual SOC 2 Type 2 report. Today the banks accept questionnaires with a commitment to a report in 2027.
- **Two enterprise prospects** made a SOC 2 Type 2 report a condition of signing.
- **The prospective agency sponsor** does not need SOC 2; it needs FedRAMP (P03). The two efforts share most controls.

**Why these categories:**
- **Security** is required in every SOC 2 examination.
- **Availability** matters because the MSA commits to 99.95% and 99.9% availability.
- **Confidentiality** matters because the MSA's confidentiality clause is a customer commitment.
- **Processing Integrity** is out of scope: customers run their own processing, and the company makes no processing commitments.
- **Privacy** is out of scope: the company processes personal information only as a service provider for its customers, who own the privacy commitments. The company's breach duties as a third-party agent are covered in P08.

**Why Type 1 first.** Most controls were defined or approved in September 2026, and a Type 2 needs controls operating over a period. A Type 1 as of 2027-03-31 gives the banks a report in the first half of 2027. The Type 2 period starts the next day.

## 2. System description (scope)
- **Services:** managed private cloud, managed services through the RMM tool, and authoritative DNS and edge services.
- **Infrastructure:**
  - the Hosting Control Plane and Customer Portal (SSP, P02)
  - the hypervisor clusters and storage at DC-1 and DC-2
  - the edge network
- **People:** 60 employees, including the 24x7 NOC.
- **Data:** customer VM contents, customer DNS zones, tenant metadata and credentials, and customer contact and billing data.
- **Procedures:** POL-01 to POL-05, the P08 runbook, and the control owners' procedures (in progress).
- **Carved-out subservice organizations:**
  - the DC-1 and DC-2 colocation providers
  - the public cloud provider
  - the RMM, identity, and SIEM SaaS vendors

  Their controls will be listed as complementary subservice organization controls.
- **Complementary user entity controls for the company's customers**, from the MSA shared responsibility schedule (P04 section 5):
  - customers secure and patch their own guest operating systems unless they buy managed services;
  - customers back up their own VMs unless they buy replication;
  - customers enroll their users in MFA and manage their own portal users.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 19 | 9 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |
| **Total in scope (38)** | **6** | **22** | **10** | |

**Ready:**
- CC1.3: roles and authority are designated
- CC3.1: service commitments are defined in the MSA
- CC3.2: the first risk assessment is done (P01)
- CC4.2: deficiencies are tracked and reviewed monthly
- CC6.7: data in transit is encrypted
- A1.1: capacity is managed

**Not ready:**
- CC3.3: no misuse or fraud risk assessment
- CC3.4: significant changes are not assessed
- CC6.1 and CC6.3: shared administrator accounts, no MFA at the hypervisor layer, and excess privilege (the P07 findings behind R-001 to R-003)
- CC7.1 and CC7.2: no authenticated scanning or management-plane monitoring
- CC7.5 and A1.3: recovery never tested (R-005)
- CC8.1: no change management for the data centers
- CC9.2: critical vendors not reviewed

**An auditor would likely report exceptions today in the areas that matter most to customers:** administrative access to the tools that reach them (CC6.1, CC6.3), and whether the company would notice misuse (CC7.2). These are the same weaknesses as the FedRAMP High gaps (P03), so one remediation plan serves both.

## 4. Findings from the DC-1 colocation report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-06-30. One exception at the provider: a missed monthly visitor log review, since remediated.
- **Availability:** redundant power, 48 hours of generator fuel, and N+1 cooling support the BIA's 4-hour hosting MTD for facility failures. They do not address a regional disaster. A hurricane that takes DC-1 offline for days remains risk R-018, handled through the contingency plan and replication offer.
- **Controls the company must run.** The report lists complementary user entity controls. Two are open gaps: reviewing the authorized access list, and reviewing cage access reports. **The provider's physical controls only fully protect the company once those reviews happen** (CC6.4, due 2026-12-31).
- **Follow-ups:**
  - Obtain the bridge letter through 2026-09-30.
  - Review the DC-2 provider's report, last reviewed in 2024, by 2026-11-30.
  - Ask for a 24-hour incident notice term at renewal.
  - Obtain and review the RMM and SIEM vendors' reports (POAM-020).

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1, CC6.2, CC6.3, CC6.6, CC8.1, CC9.2, CC7.4, CC1.1 | Named RMM accounts and IP restriction, hypervisor MFA, termination tickets, change tickets, vendor reviews, tabletop report, policy acknowledgments |
| 2027 Q1 | CC7.1, CC7.2, CC7.3, CC7.5, A1.2, A1.3, CC3.3, CC3.4, CC1.4 | Monthly scan reports, SIEM alerts from management-plane logs, AI triage sampling records, restore test records, updated risk assessment, role-based training records |
| 2027-03-31 | Type 1 as of this date | Auditor walkthroughs of control design |
| 2027-04-01 to 2027-09-30 | Type 2 period | Operating evidence for every control, collected monthly by control owners |

**Budget:** the Type 1 audit is in the funded 2026 Q4 to 2027 Q2 plan (P01 section 4). Engage the CPA firm by 2026-12-31 so its independence checks and planning are done before the Type 1 date.

**Response to the banks:** send this summary and the POA&M (P07) with the questionnaire responses, and commit to the Type 1 report in the second quarter of 2027.

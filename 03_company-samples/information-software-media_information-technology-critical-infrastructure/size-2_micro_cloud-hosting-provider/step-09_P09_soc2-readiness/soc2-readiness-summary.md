# SOC 2 Readiness Summary: Cris Santos Company | Information Technology | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (managed cloud hosting provider) |
| Tier / Vertical | Micro / Information Technology |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Target report | None in 2026. Readiness self-assessment now; decision on a SOC 2 Type 1 examination in 2027 (section 6) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer both banks' 2026 vendor due diligence questionnaires |
| Part B | Review of the DC-1 colocation provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 to 2026-08-28 by the Operations Manager and the Lead Systems Engineer (colocation report reviewed 2026-08-26); statuses updated for the policy approvals; approved by the Owner 2026-09-15 |

## 1. Why SOC 2 for this organization
**The company is a service organization.** It hosts about 260 customer VMs, patches about 310 customer servers, and serves about 190 customer DNS zones. Its controls are part of its customers' own control environments, which is exactly what a SOC 2 report is meant to describe.

**Who is asking:**
- **Bank A and Bank B.** Each bank's vendor management program sent a 2026 due diligence questionnaire, due **2026-10-30**. The questions follow the Trust Services Criteria and the Interagency Guidelines. Both banks will accept a self-assessment with a dated remediation plan this year. Bank A's questionnaire says it expects an independent report "within a reasonable period."
- **Larger prospects.** Two prospects in 2026 asked for a SOC 2 report; neither made it a condition yet.

**Why not an examination now.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months. Most of the company's controls were defined in September 2026, and the main access-control weaknesses close by 2026-12-31. A Type 1 now would report exceptions in the areas customers care about most. The self-assessment gives the banks an honest picture now at almost no cost.

**Alternatives considered.**
- **A bank-specific questionnaire only.** Cheaper, but every new customer asks again.
- **Sharing the colocation provider's SOC 2 report.** Not enough on its own: it covers the facility, not the company's own controls.
- **ISO/IEC 27001 certification.** More effort than a SOC 2 Type 1 at this size, and the banks did not ask for it.

**Why Availability and not another category.**
- **Availability:** the MSA commits to 99.9% monthly availability with service credits, and the bank rule's 4-hour test is about disruption of covered services.
- **Confidentiality:** customer data confidentiality is covered under the Security criteria and the MSA. Neither bank asked for C1 separately.
- **Processing Integrity:** out of scope; the company makes no processing commitments.
- **Privacy:** out of scope; the company processes personal information only as a service provider for its customers. Its third-party agent duties are in P03 and P08.

## 2. System description (scope)
- **Services:** managed private cloud hosting, managed server services through the RMM tool, managed DNS, and the VM backup add-on.
- **Infrastructure and software:**
  - the Hosting Control Plane and Customer Portal (SSP, P02), with SYS-01 to SYS-11;
  - the hypervisor cluster, storage array, network, and backup appliance in two racks at DC-1;
  - the public cloud tenant.
- **People:** 7 employees and the MDR provider.
- **Data:** customer VM contents (including Bank A's loan documents), customer DNS zones, credentials for customer servers, and customer contact and billing data.
- **Procedures:** POL-02, POL-03, POL-04, and the P08 runbook.
- **Subservice organizations (carved out):**
  - the colocation provider;
  - the public cloud provider;
  - the RMM, PSA, DNS, identity, and MDR vendors.
- **Complementary user entity controls for customers** (MSA shared responsibility):
  - customers patch and protect their own guest operating systems unless they buy managed services;
  - customers back up their own VMs unless they buy the backup add-on;
  - customers manage their own portal users and enroll them in MFA.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 18 | 9 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |
| **Total in scope (36)** | **7** | **19** | **10** | |

**Ready:**
- CC1.3: roles and authority designated in writing
- CC3.1: service commitments defined in the MSA and the BIA
- CC3.2: first risk assessment done (P01)
- CC4.1: independent assessment done (P07)
- CC6.7: data in transit encrypted
- CC6.8: EDR with 24x7 MDR response
- A1.1: capacity checked monthly against the one-host-down rule

**Not ready:**
- CC2.1: no inventory of systems or of where bank customer information sits
- CC3.4 and CC8.1: no change management
- CC6.1, CC6.2, CC6.3: shared administrator accounts, no MFA at the hypervisor layer, no account approvals, and late removal of a former employee (the P07 findings behind R-001, R-003, R-007)
- CC7.1: no vulnerability scanning
- CC7.2: management plane not monitored
- CC7.5 and A1.3: recovery never tested

**What an auditor would say today.** Exceptions would be likely in the controls customers rely on most: who can use the tools that reach every customer (CC6.1 to CC6.3), and whether the company would notice misuse (CC7.2). These are the same weaknesses as the High gaps against the bank contracts (P03), so one remediation plan serves the banks and a future SOC 2.

## 4. Evidence inventory
What the company can send the banks now, and what it starts collecting for a future examination:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04; SSP | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-10) |
| Risk register summary (P01), assessment summary and POA&M (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-10) |
| Colocation SOC 2 review | CC6.4, CC9.2, A1.2 | Yes | Bridge letter (2026-10); RMM and MDR reports (2026-10 to 2026-12) |
| MDR monthly report | CC6.8, CC7.2, CC7.3 | Yes (July and August 2026) | Monthly; auto-close sample review (P10) from 2026-10 |
| Backup job reports | A1.2 | Yes | Monthly |
| Account reconciliation and termination checklists | CC6.2, CC6.3 | No | Monthly from 2026-10 |
| Change log | CC3.4, CC8.1 | No | From 2026-11 |
| Vulnerability scan reports | CC7.1 | No | Monthly from 2026-11 |
| Restore test records | CC7.5, A1.3 | No | Quarterly from 2026-11 |
| Tabletop exercise report | CC7.4 | No | 2026-10-28 |
| Training and phishing simulation records | CC1.4, CC2.2 | Yearly module only | From 2026-11 |

## 5. Findings from the colocation report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-06-30. One exception at the provider (a quarterly customer access list confirmation not sent once), since remediated.
- **Availability:** redundant power, generators, and cooling support the BIA's 4-hour hosting MTD for facility failures. They do not cover loss of the facility. A hurricane that takes DC-1 offline for days remains risk R-009, handled through the degraded-mode recovery plan.
- **Controls the company must run.** The report lists complementary user entity controls. Two were not being run:
  - keeping the authorized-person list current, which let a former employee stay on it until 2026-08-18;
  - reviewing cage access reports.

  **The provider's physical controls fully protect the company only once those reviews happen** (CC6.4, from 2026-10).
- **Follow-ups:** bridge letter through 2026-09-30; 24-hour incident notice term at renewal; the same review for the RMM and MDR providers' reports (POAM-012).

## 6. Remediation plan and decision on an examination
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q4 (by 2026-10-31) | CC1.1, CC2.2, CC2.3, CC4.2, CC6.2, CC7.4 | Acknowledgments; bank questionnaire answers (due 2026-10-30); bank contacts and tabletop (POAM-011); onboarding checklist and shared RMM accounts removed (POAM-001) |
| 2026 Q4 (by 2026-12-31) | CC1.2, CC1.4, CC1.5, CC3.4, CC5.2, CC5.3, CC6.1, CC6.3 to CC6.6, CC7.3, CC8.1, CC9.2, A1.2 | Owner meetings; role-based training; change log; MFA and named accounts everywhere (POAM-002 to POAM-005); termination checklist (POAM-013); disposal records; AI triage conditions (P10); vendor reviews (POAM-012); immutable backups (POAM-006) |
| 2027 Q1 | CC2.1, CC5.1, CC7.1, CC7.2, CC7.5 | Inventory; monthly scans; management-plane logs at the MDR (POAM-009, POAM-010); contingency plan (POAM-007) |
| 2027 Q2 | CC9.1, A1.3 | Degraded-mode recovery exercise before hurricane season (R-009; POAM-007) |
| 2027 Q3 | CC3.3 | Misuse and fraud scenarios in the July 2027 risk assessment |

**Decision point.** At the 2027-03-31 monthly meeting, the Owner decides whether to engage a CPA firm for a **SOC 2 Type 1 (Security and Availability)**, with an as-of date in the third quarter of 2027. The test: all High POA&M items closed, and at least one quarter of evidence for access reviews, change records, scans, and restore tests. Cost is not yet budgeted and would be added to the 2027 plan.

**Response to the banks (due 2026-10-30):** send this summary, the readiness checklist, the P07 POA&M, and the SSP summary. Name the Lead Systems Engineer as security contact, and commit to an updated self-assessment by 2027-04-30 and to telling the banks the Type 1 decision.

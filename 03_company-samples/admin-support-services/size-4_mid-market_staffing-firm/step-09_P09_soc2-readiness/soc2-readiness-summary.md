# SOC 2 Readiness Summary: Cris Santos Company | Administrative and Support and Waste Management | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed staffing and temporary help firm) |
| Tier / Vertical | Mid-Market / Administrative and Support and Waste Management and Remediation Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| System | Managed Workforce Solutions system: the MSP program services run on the VMS tenant (SYS-11) and the APATP components that payroll MSP workers and produce consolidated invoices |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30; Type 1 (design) as of 2027-03-31 as an interim deliverable |
| Part A | Firm readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-18 by the vCISO and the Security Manager with the VP Managed Workforce Solutions, using P02, P05, P06, and P07 evidence; approved by the COO 2026-09-22 |

## 1. Why SOC 2 for this organization
A staffing firm that only supplies labor is usually **not** a SOC 2 service organization: its associates work under the client's supervision on the client's systems, and the data the firm most needs to protect is its own workforce data. The Small sample reached that conclusion. **This firm's Managed Workforce Solutions unit is different:**
- it operates the VMS tenant through which 2 clients (a Florida hospital system and a regional logistics company) run their whole contingent workforce programs, with about 1,100 workers from 65 supplier firms;
- it processes the clients' supplier timesheets and issues one consolidated invoice of client spend each week (about $2.6 million a week across the 2 clients);
- it holds client cost centers, rates, and supplier data on the clients' behalf.

For those services the firm is a service organization, and both MSP contracts require a SOC 2 Type 2 report by their renewals (hospital system 2027-12-31; logistics company 2028-03-31). Losing either program would remove about $2 million a year of fee and payrolling revenue (P01 R-032).

**Categories.** The clients asked for Security, Availability (the VMS and weekly invoicing are commitments in the contracts), Confidentiality (client rates and cost centers), and **Processing Integrity**, because the consolidated invoice is the clients' input to their own accounts payable. **Privacy** is out of scope: the clients did not request it, and the firm's privacy duties to workers and candidates come from law (FCRA, 8 CFR 274a.2, the ADA, Fla. Stat. 501.171) and are covered in P03.

**Why Type 2, and why not now.** P07 found gaps in access reviews, SaaS monitoring, change control, recovery, and vendor oversight. Starting the observation period before those close would produce exceptions. The plan is to remediate through 2027 Q1, issue a Type 1 as of 2027-03-31, then observe for 6 months from 2027-04-01. Both clients accepted this plan with quarterly status updates.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm that performed P07.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | MSP program management: requisitions, supplier management, timesheet processing, consolidated invoicing; payrolling of client-sourced workers |
| Infrastructure | VMS tenant (SYS-11); identity provider (SYS-03); the landing zone integration platform and backups (SYS-04); payroll and billing platform (SYS-02); HQ network and endpoints used by program staff |
| People | 6 Managed Workforce Solutions staff; payroll and billing staff; IT and security team; MSSP; vCISO |
| Data | Client requisitions, cost centers, rates; supplier submissions, timesheets, invoices; payrolled worker data |
| Procedures | POL-01 to POL-05, the standards index, and the P08 runbooks (including the 48-hour MSP client notice) |
| Subservice organizations (carve-out) | VMS vendor, payroll vendor, identity provider, cloud provider, MSSP. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls in the firm's system description (Part B) |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 16 | 8 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 1 | 4 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **11** | **23** | **9** | **18** |

In scope: 43 criteria (11 Ready, 23 Partially ready, 9 Not ready). Out of scope: the 18 Privacy criteria.

**Ready (11):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC3.1, CC3.2;
- monitoring and control design: CC4.1, CC4.2, CC5.1;
- malware protection: CC6.8;
- capacity: A1.1;
- stored data: PI1.5.

**Not ready (9):**
- CC2.1 and CC7.2: VMS, payroll, and ATS activity is not in the SIEM;
- CC3.4 and CC8.1: SaaS, VMS, and integration code changes are not under change control;
- CC6.3: departed users in the VMS and no quarterly reviews;
- CC7.1: container scanning and remediation timeliness;
- CC7.5 and A1.3: no approved contingency plan or recovery test for the MSP system;
- CC9.2: vendor management.

Each maps to a P07 POA&M item. Most Partially ready criteria depend on standards being issued (P06) and on monitoring coverage.

**Processing Integrity.** The consolidated invoice is built from VMS timesheets by the integration platform and billed through the payroll and billing platform. The key gaps are a missing duplicate check on VMS time imports and no documented weekly reconciliation of billed hours to approved hours (PI1.2 to PI1.4; P01 R-027).

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments for BP-07), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.2, CC3.3, CC3.4, CC6.2, CC6.3, CC6.5, CC6.7, CC7.1, CC7.3, CC9.1, A1.2, C1.1, PI1.2 to PI1.4 | VMS on SSO and access tickets; quarterly review sign-offs; SaaS change log; scan reports; supplier bank change call-backs; invoice reconciliation sign-offs; contingency plan approval |
| 2027 Q1 | CC1.2, CC1.4, CC2.1, CC2.3, CC5.2, CC5.3, CC6.1, CC6.4, CC6.6, CC7.2, CC7.4, CC7.5, CC8.1, CC9.2, A1.3, C1.2, PI1.1 | SIEM source list and alert tickets; tabletop reports; restore test records; standards; Tier 1 vendor reviews; system description |
| 2027-03-31 | Type 1 (design) report to both MSP clients | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence (quarterly reviews, monthly scans, restore tests, weekly invoice reconciliations, vendor reviews) |

**Status reporting.** The VP Managed Workforce Solutions and the vCISO report readiness monthly to the COO and quarterly to the audit committee and both MSP clients.

## 5. Vendor SOC 2 review program (Part B)
The APATP relies on vendor controls for many inherited controls (P02: 12 Common/Inherited and 33 Hybrid), and the MSP system will carve out 5 subservice organizations. The program in `vendor-soc2-review.csv` makes that reliance evidence-based and is the core of the vendor risk standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Restricted data at scale (more than 10,000 people), privileged access to firm systems, a High-criticality BIA process, or a subservice organization in the MSP system | SOC 2 Type 2 (or equivalent) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to firm controls, availability against the BIA, and incident terms | Annually |
| **Tier 2** | Limited personal information, no privileged access, Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No personal information and no system access | Contract terms only | At contract renewal |

Of the 64 vendors that receive personal information, 9 are Tier 1 and about 30 are Tier 2 under this approach. The CSV holds the 9 Tier 1 entries: 8 completed reviews (7 SOC 2 reports and the credentialing vendor's questionnaire) and 1 pending (the screening provider's report, requested 2026-08-12, review due 2026-12-31).

**Key findings:**
1. **Payroll vendor:** unqualified Type 2 with Processing Integrity; RTO 8 hours meets the BIA. Its CUECs (bank-change and export report review, register approval) are partly open on the firm's side (POAM-006, POAM-021). **The vendor's controls only protect the firm once those close.**
2. **ATS vendor:** unqualified, but its RTO of 12 hours does not meet dispatch (P05 finding 1), and its report **excludes marketplace add-ons**, including the AI tools (P10). The AI vendors need their own assurance.
3. **VMS vendor:** unqualified Type 2 with all four requested categories; its CUECs become complementary subservice organization controls in the firm's own system description, so the firm's VMS access and supplier bank change controls must work for the firm's report to be clean.
4. **Timekeeping vendor:** an exception for unlogged remote support sessions to customer devices, the same weakness the firm found for the fingerprint clocks (P01 R-008).
5. **Credentialing vendor:** no SOC 2 report, no stated recovery objective, no MFA for client users. It supports the process with the shortest MTD (BP-05, 12 hours). A SOC 2 commitment or replacement is a renewal condition (POAM-017).
6. **MSSP:** 2 of 40 escalations late in the report period; tracked as a monthly metric.

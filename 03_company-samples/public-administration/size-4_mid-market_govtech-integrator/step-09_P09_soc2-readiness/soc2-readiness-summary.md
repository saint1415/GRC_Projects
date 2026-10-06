# SOC 2 Readiness Summary: Cris Santos Company | Public Administration | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Mid-Market / Public Administration |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| System | Agency Case Management Cloud (ACMC), as bounded in the SSP (P02) |
| Prior report | SOC 2 Type 1 (Security and Availability) as of 2025-12-31 |
| Target report | First SOC 2 Type 2 covering 2027-04-01 to 2027-09-30, adding Confidentiality |
| Prepared | 2026-09-10 by the GRC Manager with the Director of Contracts and Compliance; reviewed by the Chief Operating Officer 2026-09-17 and presented to the audit committee the same day |
| Files | `soc2-readiness.csv` (61 criteria); `vendor-soc2-review.csv` (8 vendor reviews) |

## 1. Why SOC 2 for this organization
**The company is a service organization.** It hosts and operates a case management service for 43 agencies, and those agencies rely on its controls over their data: FTI for AG-01, CJI for AG-02 and AG-39, benefits data for AG-03, and motor vehicle records for AG-04. A SOC 2 report is how a service organization shows its customers that those controls are designed and operating over time.

**Demand:**
- **AG-03** (about $14 million a year) amended its contract in 2026 to require a SOC 2 Type 2 report covering a period in 2027, or an equivalent independent report.
- **AG-01** (about $9.5 million a year) renews in 2027 and has asked for a Type 2 report rather than the 2025 Type 1 (P01 R-021).
- **Florida state agencies** must require suppliers, by contract where necessary, to implement appropriate security measures and must assess them routinely (Rule 60GG-2.002(6)). One independent report saves each agency its own assessment.
- **State B** customers require GovRAMP Authorized status by 2027-06-30 (P01 R-020). GovRAMP is pursued in parallel, from the same SP 800-53 evidence.

**Why a Type 2 period starting 2027-04-01.** A Type 2 report tests how controls operated over a period. The High POA&M items for access, monitoring, and managed services close between 2026-10-31 and 2027-01-31, and the first timed restore within 8 hours is due 2027-01-29 (P07). Starting the period on 2027-04-01 gives each fix at least 2 months of operation before the period, so the report shows the fixed controls rather than the gaps. Recovery items due later (region B failover, 2027-06-30) will be inside the period; their design must be in place by 2027-04-01.

**Assurance alternatives (not replacements):**
| Option | What it is | Role for this company |
|---|---|---|
| GovRAMP (formerly StateRAMP) | Nonprofit membership program, not law. SP 800-53-based verification for cloud providers serving state and local governments, with tiers (Core, Ready, Provisional or Authorized) and Snapshot programs (N92-R08) | Ready status held since 2025; Authorized required by State B by 2027-06-30. The SSP (P02) and gap analysis (P03) are built on SP 800-53, so the evidence carries over |
| CJIS audits by the Florida and State B CJIS Systems Agencies | Audits of AG-02 and AG-39 and their contractors against CJISSECPOL | Required regardless of SOC 2. Results are not shareable with other customers |
| IRS Office of Safeguards review | Review of AG-01, which can include contractor facilities (Pub. 1075 Exhibit 7 III) | Required regardless of SOC 2. Not a report for other customers |
| FedRAMP | Federal authorization program | Not pursued: no federal customers. The cloud provider's FedRAMP Moderate authorization is used as subservice evidence |

## 2. System description (scope)
- **Services:** hosting, operation, and support of the ACMC for state and local agencies, including integration with agency systems and the AI eligibility assistant. Delivery services and **managed services for agency-hosted systems are out of the report scope**; they are described as separate services so readers do not assume coverage. Managed services customers (AG-02, AG-08 to AG-14) are told this in writing.
- **Infrastructure:** the 8 landing zone accounts (SYS-01 to SYS-03, SYS-05, SYS-06, SYS-08, SYS-09, SYS-14).
- **Software:** the ACMC application, the pipeline that builds it (SYS-07), the identity provider and privileged access management (SYS-04), and the SIEM with the MDR provider (SYS-12).
- **People:** 600 staff; about 300 in engineering, cloud operations, support, security, data and AI, and IT are closest to the system.
- **Data:** FTI, CJI including CHRI, benefits applicant data, motor vehicle records, and constituent data (about 3.1 million individuals).
- **Procedures:** POL-01 to POL-05, the standards (STD-01 to STD-10), and the P08 runbooks.

**Subservice organizations (carve-out).** The cloud provider (data centers, managed services, and the managed model service), the identity provider, the repository and pipeline vendor, and the MDR provider. The report will use the carve-out method and list the controls the company expects each to run. The company reviews their SOC 2 reports each year (`vendor-soc2-review.csv`, criterion CC9.2).

**Complementary user entity controls (what each agency must do).** Listed in the report and in each contract:
- agencies with federated sign-in enforce MFA and remove leavers in their own identity providers;
- every agency approves its users' access and reviews it at least yearly;
- municipal administrators manage their local accounts and use MFA once enabled (R-040);
- agency users do not attach FTI or CJI to support tickets, and AG-03 caseworkers do not enter IRS income data in case notes;
- AG-03 caseworkers make every eligibility decision and review AI suggestions under the agreed design (P10);
- agencies tell the company promptly about suspected incidents on their side.

## 3. Readiness results
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 14 | 16 | 3 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

Processing Integrity and Privacy are out of scope for the first Type 2 report; the reasons are in each row of `soc2-readiness.csv`.

**Ready (15):** governance and oversight (CC1.2, CC1.3, CC1.5), risk assessment (CC3.1 to CC3.3), monitoring and deficiency tracking (CC4.1, CC4.2), control selection and technology controls (CC5.1, CC5.2), user registration (CC6.2), physical access (CC6.4), malware and integrity (CC6.8), event evaluation (CC7.3), and capacity (A1.1). Most of these were tested in the 2025 Type 1 examination and again in P07.

**Not ready (4):**
- CC1.4: staff reached CJI or FTI before screening was complete (POAM-005, POAM-013)
- CC6.3: standing support access to regulated tenants and slow removal (POAM-001, POAM-002)
- CC7.2: no monitoring of regulated-record access or of SYS-10 (POAM-006, POAM-018)
- A1.3: recovery testing does not meet the 8-hour RTO (POAM-009)

The Partially ready rows mostly have the control designed but not yet operating everywhere it needs to, which is what a mid-market company should expect before its first Type 2 period. A Type 2 auditor would report each of them as an exception if the period started today.

## 4. Vendor and subservice SOC 2 reviews
`vendor-soc2-review.csv` records 8 reviews refreshed for this readiness work: 6 of the 9 Tier 1 vendors and 2 Tier 2 vendors. The remaining 3 Tier 1 vendors (the productivity suite, the endpoint protection and device management vendor, and the staffing firm that supplies contract developers) are due by 2026-12-31 under POAM-011.

| Result | Vendors |
|---|---|
| Unqualified opinion, no follow-up beyond routine | VEN-05, VEN-06, VEN-08 |
| Unqualified, with follow-up actions | VEN-01 (FedRAMP listing check), VEN-02 (bridge letter), VEN-03 (escalation SLA; no FTI in logs), VEN-07 (signed data-use terms) |
| **No report on file** | **VEN-04, the remote management platform (SYS-10)**. Its report is due by 2026-10-31; this is the most important vendor gap because of P01 R-001 and R-013 |

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 (by 2026-11-30) | CC1.1, CC1.4, CC2.2, CC6.5, C1.2, CC7.1, CC8.1 | Policy acknowledgments; screening gate records and recertifications; managed services training roster; scan and remediation reports; deletion certificates; enclave change records with second approver |
| 2026 Q4 (by 2026-12-31) | CC2.1, CC2.3, CC5.3, CC6.6, CC6.7, CC7.4, CC9.1, CC9.2, C1.1 | Data inventory confirmations; AG-39 agreement; issued standards; egress rules; FIPS module inventory; agency tabletop report (2026-12-15); contingency plan; vendor reviews |
| 2027 Q1 | CC6.1, CC6.3, CC7.2, CC7.5, CC3.4, A1.3 | Security key enrollment; quarterly access review; weekly access analytics; SYS-10 vault and session logs; first timed restore (2027-01-29) and rebuild exercise (2027-03-31) |
| 2027-03-31 | All in-scope criteria | Readiness re-check by the GRC Manager; go or no-go for the period start |
| 2027-04-01 to 2027-09-30 | All in-scope criteria | **Type 2 period.** Monthly evidence folders per criterion; region B failover exercise inside the period (A1.2, A1.3) |
| 2027-11-30 | | Report issued to AG-01, AG-03, and other customers on request |

**Owner and follow-up.** The GRC Manager runs the program; the Chief Operating Officer reviews progress monthly against this plan and the POA&M (POAM-023); the vCISO reports it to the audit committee each quarter. The CPA firm and the GovRAMP assessor are to be engaged by 2026-11-30 within the $310,000 budget (P01 section 4). Send AG-01 and AG-03 this summary and the POA&M with their renewal discussions.

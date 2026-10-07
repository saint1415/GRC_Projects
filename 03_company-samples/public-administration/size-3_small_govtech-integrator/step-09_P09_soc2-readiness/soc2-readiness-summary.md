# SOC 2 Readiness Summary: Cris Santos Company | Public Administration | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Small / Public Administration |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| System | Agency Case Management Platform (ACMP), as bounded in the SSP (P02) |
| Target report | SOC 2 Type 1 as of 2027-03-31, then a Type 2 covering 2027-04-01 to 2027-09-30 |
| Prepared | 2026-08-26 by the IT Manager with the Contracts and Compliance Manager; reviewed by the Chief Operating Officer 2026-08-31 |

## 1. Why SOC 2 for this organization
**The company is a service organization.** It hosts and operates a case management service for 11 agencies, and those agencies rely on its controls over their data: FTI for AC-01, CJI for AC-02, and SNAP, TANF, and Medicaid applicant data for AC-03. A SOC 2 report is how a service organization shows its customers that those controls are designed and operating. This is the situation SOC 2 was built for, unlike a business that only buys services.

**Demand:**
- **AC-01 (revenue agency)** requires an independent SOC 2 Type 2 report, or an equivalent, at its 2027 contract renewal. AC-01 is about 20% of receipts (P05 BP-03). Losing it is risk R-031 in P01.
- **Two prospective out-of-state agencies** ask for GovRAMP verification.
- **Florida state agencies** must require suppliers, by contract where necessary, to implement appropriate security measures and must assess them routinely (Rule 60GG-2.002(6); P03 section 1.4). An independent report saves each agency from running its own assessment.

**Why readiness first, not an audit now.** The company's policies were approved on 2026-08-31, and the High gaps in backups, logging, monitoring, and privileged access close between 2026-10 and 2027-03 (P07 POA&M). A Type 2 report tests how controls operated over a period, usually 6 to 12 months, so an audit now would report the gaps as exceptions. The plan is a **Type 1 report as of 2027-03-31** (design at a point in time, budgeted at $48,000 in the FY2027 security budget, P01 section 4), then a **6-month Type 2 period from 2027-04-01**. The company will ask AC-01 to accept the Type 1 report, the P07 assessment, and the POA&M as the equivalent at renewal, with a contract commitment to deliver the Type 2 report.

**Assurance alternatives (not replacements):**
| Option | What it is | Role for this company |
|---|---|---|
| GovRAMP (formerly StateRAMP) | Nonprofit membership program, not law. NIST SP 800-53-based verification for cloud providers serving state and local governments, with tiers (Core, Ready, Provisional or Authorized) and Snapshot programs for vendors still progressing. stateramp.org now redirects to govramp.org (N92-R08, checked 2026-09-25) | Answers the two prospective agencies. The SSP (P02) and gap analysis (P03) are already built on SP 800-53, so the evidence carries over. Plan a Snapshot in 2027 Q1 and a Ready verification after the High POA&M items close |
| CJIS audit by the state CJIS Systems Agency | Audit of AC-02 and its contractors against CJISSECPOL | Required for AC-02 regardless of SOC 2. Its results are not shareable with other customers |
| IRS Office of Safeguards review | Review of AC-01, which can include contractor facilities (Pub. 1075 Exhibit 7 III) | Required for AC-01 regardless of SOC 2. Not a report for other customers |
| FedRAMP | Federal authorization program | Not pursued: the company has no federal customers. Its cloud provider's FedRAMP Moderate authorization is used as subservice evidence |

## 2. System description (scope)
- **Services:** hosting, operation, and support of the ACMP for 11 Florida agencies; integration with AC-01, AC-02, and AC-03 systems. Implementation and data migration services are out of the report scope.
- **Infrastructure:** the company's production and non-production cloud accounts (managed containers, managed relational databases, object storage, message queue, integration gateway), backups, and logging (SYS-01, SYS-02, SYS-04, SYS-10 to SYS-13).
- **Software:** the ACMP application, the AI eligibility assistant pilot (SYS-11), the pipeline that builds them (SYS-06), and the workforce identity provider (SYS-03).
- **People:** 60 staff; the 32 in engineering, cloud operations, and support are closest to the system.
- **Data:** FTI, CJI including CHRI, benefits applicant data, and constituent data (about 455,000 individuals).
- **Procedures:** POL-01 to POL-05 (P06), the P08 runbook, and the procedures still to be written (CC5.3).

**Subservice organization (carve-out).** The cloud provider supplies the data centers, physical security, and managed services. The report will use the carve-out method: the provider's controls are excluded, and the report lists the controls the company expects the provider to run. The company must collect and review the provider's own SOC 2 report each year (CC9.2 gap).

**Controls the agencies must run (complementary user entity controls).** The company's controls only work if each agency does its part. These will be listed in the report and in each contract:
- AC-01, AC-02, and AC-03 enforce MFA and remove leavers in their own identity providers
- every agency approves its users' access and reviews it at least yearly
- municipal administrators manage their local accounts (and use MFA once enabled, P01 R-014)
- agency users do not attach FTI or CJI to support tickets, and AC-03 caseworkers do not enter IRS income data in case notes (P01 R-005, R-030)
- agencies tell the company promptly about suspected incidents on their side

## 3. Readiness results
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 21 | 6 | 0 |
| Availability (A1, 3) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

Processing Integrity and Privacy are out of scope for the first report; the reasons are in each row of `soc2-readiness.csv`.

**Ready:**
- CC1.3: the Information Security Officer is designated and roles are set
- CC3.1 and CC3.2: objectives are set from the contracts, and the risk assessment is done (P01)
- CC4.2: deficiencies are tracked in the POA&M (P07)
- CC5.1: controls are selected from the Moderate baseline (P02)
- CC6.4: physical security is inherited from the FedRAMP Moderate cloud provider

**Not ready:**
- CC6.3: standing administrator rights and support access to every tenant (POAM-012, POAM-001)
- CC6.5 and C1.2: no disposal at contract end; a former customer's data is still held (P01 R-022)
- CC6.7: TLS modules not FIPS-validated; FTI and CJI leave in ticket screenshots (POAM-008 to POAM-010)
- CC7.2: no security monitoring (POAM-007)
- CC7.5, A1.2, and A1.3: backups are exposed and recovery is untested (POAM-003, POAM-004; the same gap as R-001)
- CC9.2: vendors other than the cloud provider are not reviewed (POAM-010)

Most Partially ready rows have the control designed in the August 2026 policies but not yet operating long enough to produce evidence. That is normal for a first readiness review. For a Type 2 report it means the evidence clock should start as soon as each control is live.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 (by 2026-11-30) | CC1.1, CC1.4, CC2.2, CC3.4, CC6.5, C1.2, CC7.1, CC7.4, CC8.1 | Policy acknowledgments; screening and training records before access; reporting-rule briefing roster; weekly scan reports; tabletop report; emergency change tickets; deletion certificate for the former customer |
| 2026 Q4 (by 2026-12-31) | CC1.2, CC2.1, CC2.3, CC4.1, CC5.3, CC6.2, CC6.7, CC7.2, CC7.3, CC9.1, CC9.2, A1.1, A1.2, C1.1 | Quarterly oversight minutes; weekly log review records; managed detection tickets; quarterly access reviews; FIPS module inventory; vendor register and reviews (including the cloud provider's SOC 2 report); contingency plan; backup account settings |
| 2027 Q1 | CC1.5, CC3.3, CC5.2, CC6.1, CC6.3, CC6.6, CC6.8, CC7.5, A1.3 | Just-in-time elevation logs; egress rules; image signing records; secrets rotation logs; first timed restore test (2027-01-29) and first exercise (2027-03-31) |
| 2027-03-31 | All in-scope criteria | **Type 1 examination date.** Select the CPA firm by 2026-12-31 |
| 2027-04-01 to 2027-09-30 | All in-scope criteria | **Type 2 period.** Keep monthly evidence folders per criterion |

**Owner and follow-up.** The IT Manager runs the program; the Chief Operating Officer reviews progress monthly against this plan and the POA&M. The readiness self-assessment is repeated in 2027-01 to confirm the Type 1 date. Send AC-01 this summary, the checklist, and the POA&M with its renewal discussion.

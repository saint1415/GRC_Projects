# SOC 2 Readiness Summary: Cris Santos Company Holdings | Educational Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Educational Services (focus division: Higher Education) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness assessment: Education Software, both platforms (`soc2-readiness.csv`). Higher Education and Student Health are out of scope. The college's review of its key vendors' SOC 2 reports is in `vendor-soc2-review.csv` |
| Target report | Education Software: Type 2 for 2026-07-01 to 2027-06-30 (Security, Availability, Confidentiality), the period after the report issued 2026-08-14 |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the Education Software CISO and the College CISO. Presented to the board risk committee 2026-09-15 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. So the question for each division is whether other organizations rely on its controls as part of their own.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Education Software | Campus Platform (SYS-E1) for about 900 colleges and District Platform (SYS-E2) for about 5,400 districts | **Yes, a true service organization.** Schools rely on it as a school official under FERPA and, for Title IV colleges, as a service provider under 16 CFR 314.4(f) | **In scope (full).** Existing annual Type 2 | Security, Availability, Confidentiality | Type 2, 12 months ending June 30 |
| Higher Education | Instruction, enrollment, and aid for about 410,000 students | **No.** Students are not user entities | **Out of scope** (reasons below) | n/a | n/a |
| Student Health | Clinical care at 96 sites, including 58 clinics run for 37 unaffiliated colleges | **Partly.** The contracting colleges rely on Student Health to keep their students' records | **Out of scope for now** (reasons and revisit trigger below) | n/a | n/a |

**Why Higher Education is out of scope:**
1. **No user entities.** The college serves students. No organization builds its own control environment on the college's systems.
2. **Its assurance comes from regulators.** The annual Title IV compliance audit tests the FTC Safeguards Rule, as FSA requires (GENERAL-23-09), and the fiscal 2025 audit had no GLBA finding. The P03 gap analysis against 16 CFR 314 is the college's main compliance yardstick.
3. **SOC 2 still matters to the college as a customer.** Most of its controls come from vendors, and the largest of them is its own sister division. Section 4 summarizes the vendor report reviews required by 16 CFR 314.4(f)(3).

**Why Student Health is out of scope for now:**
1. **The service is clinical care, not a system.** The 37 contracting colleges buy clinic operations under management contracts. Their students' records stay in Student Health's EHR, and the colleges do not use that system themselves.
2. **The contracts already give the colleges their assurance.** The management contracts carry FERPA school-official and redisclosure terms (being added where missing, P03 SH-G27), and each college can review clinic operations on site. No contracting college has asked for a SOC 2 report.
3. **Other assurance applies.** Student Health is a HIPAA covered entity assessed under 45 CFR 164.308(a)(8) (P07 division sample). Group internal audit covers its controls in the annual cycle.
4. **Revisit trigger:** if 3 or more contracting colleges ask for a SOC report, or if Student Health starts giving colleges direct access to the EHR or any hosted service, assess a SOC 2 Type 1 for the clinic management service line.

**Other assurance options considered.** The vertical overlay for information and software names ISO/IEC 27001 certification and FedRAMP as alternatives. FedRAMP does not apply because Education Software has no federal agency customers. ISO/IEC 27001 was considered, but school and district contracts ask for SOC 2, so SOC 2 stays the primary report.

## 2. System description (Education Software)
- **Services:** the Campus Platform (SIS, LMS, and student financials for about 900 colleges, including Cris Santos College) and the District Platform (K-12 SIS, LMS, family app, and the AI tutoring pilot for about 5,400 districts).
- **Infrastructure and software:**
  - SYS-E1 and SYS-E2 on cloud provider B (container platform, managed databases, warm standby region);
  - the support console and release pipeline (SYS-E3);
  - group identity (SYS-G1), SOC (SYS-G2), and the backup vault (SYS-G3) carved in as internal shared services.
- **Subservice organizations (carve-out):**
  - cloud provider B;
  - **the third-party model provider for the AI tutor.** It was missing from the 2026 description and must be added for the current period (scenario gap 6).
- **People:** about 8,500 Education Software employees, plus the group SOC and identity teams.
- **Data:** about 6.5 million college student records on the Campus Platform and about 22 million K-12 student users on the District Platform (about 8 million under 13). This covers education records, customer information of Title IV colleges, and children's personal information.
- **Complementary user entity controls:** customer SSO and MFA, provisioning and removal of customer users, approval of support access requests (new, POAM-001), review of audit and support access reports, and protection of integration credentials.

## 3. Readiness results (Education Software, `soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 25 | 6 | 2 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 0 | 1 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many criteria are Ready.** Group common controls cover the control environment, risk assessment, monitoring, workforce identity, network, SOC, and backup criteria. Those controls were evidenced in the 2026 report and confirmed by group internal audit (P07: 121 of 134 common control statements satisfied).

**Not ready (3):**
- **CC2.3 (communication with external parties).** The 2026 description left out the AI tutor and its model provider, although the tutor ran from 2026-01. The 140 pilot districts got no subprocessor notice. The trust page says staff access customer data only with permission, which standing support access contradicts (P03 ES-G16 to ES-G18).
- **CC6.3 (least privilege).** 61 support accounts have standing read access to every customer tenant. In the P07 sample, 19 of 30 reads had no customer approval (POAM-001). This is the group's top risk (GR-01).
- **C1.2 (disposal).** Data from 212 former districts is still held, some of it more than 3 years after contract end. That breaks the 90-day deletion commitment and 16 CFR 312.10 (POAM-015).

**Partially ready (6):**
- CC3.4 and CC8.1: the AI tutor launched without a significant-change assessment, privacy impact analysis, or safety testing.
- CC5.3: the division supplement lacks the change gate and the support access rule.
- CC7.2: no detection of support console reads outside a ticket.
- CC7.4: no register of the state-specific notice terms in about 1,300 district contracts.
- CC9.2: the model provider is not monitored, and 23 integration partners have no written assurances.

**The 2026 report and its users.** The report issued 2026-08-14 covered a period in which the AI tutor ran for about six months, but it did not describe the tutor or the model provider. The 2026 opinion was unqualified, and its testing of support access covered role approvals only. Management has asked the service auditor whether the omission needs any communication to report users before the next report. In the meantime, Education Software is sending subprocessor notices to the pilot districts by 2026-10-31 (POAM-014). For the current period, expect the service auditor to evaluate CC2.3, CC3.4, CC6.3, CC8.1, and C1.2 for exceptions. Remediation dated after 2026-07-01 will reduce exceptions in the later part of the period but will not remove them.

**Processing Integrity and Privacy** are out of scope. Education Software makes no processing integrity commitments, and its privacy duties (COPPA operator notice, consent, and retention; FERPA contract terms) are assessed against the regulations in P03. Processing Integrity is under evaluation for the period starting 2027-07-01, because districts now ask whether the AI tutor's answers are accurate (P10 AI-004).

## 4. The college's review of key vendors' SOC 2 reports (`vendor-soc2-review.csv`)
The Safeguards Rule requires the college to oversee its service providers and assess them periodically (16 CFR 314.4(f)). The College CISO reviewed 4 reports in August 2026:

| Ref | Vendor | Opinion | Recovery vs BIA | Complementary user entity controls not met at the college |
|---|---|---|---|---|
| VR-01 | Campus Platform (sister division) | Unqualified, no exceptions | Meets | Support access approval and support access report review (POAM-001); integration credentials (POAM-002) |
| VR-02 | Financial aid management system vendor | Unqualified, no exceptions | Meets | Review of user and vendor support account activity (POAM-012) |
| VR-03 | Admissions CRM vendor | Unqualified, 1 remediated exception | Meets | None; but the report does not cover the scoring model (P10 AI-001) |
| VR-04 | Online proctoring vendor | Unqualified, 1 remediated exception | Meets | Consistent flag review (HE-029); verified deletion each term (HE-013) |

**What the reviews show:**
1. **The college had never read its most important vendor's report.** The Campus Platform report was first reviewed by the college on 2026-08-21, although the college has relied on the platform since 2021 (P03 G-032; scenario gap 3).
2. **A clean report does not mean the college is protected.** A vendor's controls only work if the customer runs the complementary user entity controls. The college does not yet run 4 of them: support access approval, support access report review, integration credentials, and FAMS activity review.
3. **SOC 2 does not answer the AI questions.** The CRM and proctoring reports cover security, not whether models are accurate or fair, or whether the vendor trains on college data. Those questions are handled in contracts and P10.
4. **Incident notice terms are uneven.** The intercompany agreement has none (the revised agreement sets 24 hours, POAM-009), and the proctoring contract says "without undue delay" (the target is 72 hours at the 2027 renewal).

The Qualified Individual's written report to the college board of trustees on 2026-10-20 will cover these service provider arrangements (16 CFR 314.4(i)(2)).

## 5. Remediation plan and evidence calendar
| Quarter | Division | Criteria or item | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | Education Software | CC2.3 | Subprocessor notices (2026-10-31); corrected trust page (2026-10-31); district authorizations (2026-11-30); draft description section on the tutor and the model provider |
| 2026 Q4 | Education Software | CC3.4, CC5.3, CC8.1 | Re-issued supplement with the change gate (2026-11-30); privacy impact analysis; AI tutor test plan and red-team results (2026-12-31) |
| 2026 Q4 | Education Software | CC6.3, CC7.2 | PAM workflow records (college tenant 2026-11-30, all tenants 2026-12-31); console detection rules |
| 2026 Q4 | Education Software | C1.2, CC7.4 | Deletion certificates for 212 districts (2026-11-30); automated deletion records; contract term register (2026-12-15) |
| 2026 Q4 | Higher Education | VR-01 to VR-04 | Revised intercompany agreement (2026-12-31); FAMS bridge letter (2026-10-31); CRM contract amendment; first FAMS activity review |
| 2027 Q1 | Education Software | CC9.2 | Model provider attestation; integration partner assurances (2027-03-31) |
| 2027 Q1 | Higher Education | VR-01 | Campus Platform bridge letter (2027-01-31); first annual service provider assessment (2027-02-28) |
| 2027 Q1 to Q2 | Education Software | All in-scope criteria | Operating evidence through 2027-06-30 for the Type 2 period |

**Communication:**
- The Education Software chief product officer briefs the 140 pilot districts on the tutor, the model provider, and the remediation before further rollout.
- The division president sends all customers a letter on the support access redesign once standing access is removed.
- The college registrar receives the same monthly support access summary as external customers, starting 2026-11-30.

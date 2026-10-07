# SOC 2 Readiness Summary: Cris Santos Company | Educational Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private career college) |
| Tier / Vertical | Small / Educational Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (Common Criteria CC1-CC9) only |
| Target report | None. This is a self-benchmark, not a CPA engagement. No Type 1 or Type 2 report is planned |
| Part A | Security readiness self-benchmark requested by the Board of Managers (`soc2-readiness.csv`) |
| Part B | Review of the SIS and LMS vendors' SOC 2 Type 2 reports (`vendor-soc2-review.csv`) |
| Prepared | Vendor reviews completed 2026-08-14 by the IT Director; readiness status as of 2026-08-21, after the policy set was approved |

## 1. Why SOC 2 for this organization
**The college is not a service organization.** A SOC 2 report describes controls at a company that provides services to other businesses. The college serves students, not user entities, and no customer has asked it for a SOC 2 report. Its external assurance comes from somewhere else: the annual Title IV compliance audit, in which the auditor tests compliance with the FTC Safeguards Rule (16 CFR Part 314) as FSA requires (GENERAL-23-09). The vertical overlay names no SOC 2 alternative for colleges, so the Safeguards Rule gap analysis (P03) is the primary compliance yardstick.

SOC 2 still has two legitimate uses here:

**A. A Board self-benchmark (Part A).** After the risk assessment, the Board of Managers asked how the college's security compares with a recognized outside standard. The Security category of the Trust Services Criteria was chosen because it is widely understood and maps to the SP 800-53 controls in the SSP. The result is a readiness self-assessment, not an audit opinion.
- **Only Security** is in scope. The college makes no availability, confidentiality, processing integrity, or privacy commitments to user entities. Student privacy is governed by FERPA and assessed in P03.
- The benchmark goes to the Board with the Qualified Individual's first written report on 2026-10-15 (16 CFR 314.4(i)).

**B. Vendor oversight (Part B).** The SIS and LMS vendors operate most of the controls the college inherits (P02, P04). Their SOC 2 Type 2 reports are the evidence for those controls, and reviewing them is part of the periodic service provider assessment the Safeguards Rule requires (314.4(f)(3), P03 G-032). This was the first time the reports were requested.

## 2. System description (scope)
- **Services:** enrollment, academic records, online instruction, Title IV aid processing, and student accounts for about 900 students.
- **Infrastructure and software:**
  - the Student Information and Financial Aid Platform (SSP, P02);
  - the LMS;
  - the campus network and 70 staff endpoints.
- **People:** 60 staff and faculty, plus the financial aid servicer.
- **Data:** customer information (about 6,400 consumers), education records, and workforce data.
- **Procedures:** POL-01 to POL-05 (P06) and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 20 | 8 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready (5):**
- CC1.3: the Qualified Individual and reporting lines are designated in writing.
- CC3.1 and CC3.2: objectives, risk tolerance, and the 2026 risk assessment.
- CC3.3: fraud risks (refund redirection, fraudulent awards, identity fraud in online enrollment) are in the risk register.
- CC5.1: controls are selected from a recognized baseline in the SSP.

**Not ready (8):**
- CC1.2: the Board has never overseen security. Its first written report is on 2026-10-15.
- CC6.1: servicer access without MFA and unencrypted aid exports. These are the same gaps as High risks R-004 and R-002.
- CC6.3: excess SIS access and stale adjunct accounts.
- CC6.7: aid spreadsheets sent by unencrypted email.
- CC7.1 and CC7.2: no vulnerability management or monitoring.
- CC7.5: recovery is unproven (R-019).
- CC8.1: no change management.

The remaining 20 Security criteria are partially ready. Most have an approved policy but no operating evidence yet.

## 4. Findings from the vendor reports (Part B)
| Item | SIS vendor | LMS vendor |
|---|---|---|
| Opinion | Type 2, unqualified; 1 change-approval exception, remediated | Type 2, unqualified; no exceptions |
| Recovery objectives vs the BIA | RTO 4 h, RPO 1 h. **Meets** BP-01 (RTO 8 h, RPO 1 h) | RTO 8 h, RPO 4 h. **Meets** BP-02 (RTO 8 h, RPO 4 h) |
| Incident notice | 72 hours after confirmation | "Without undue delay". Negotiate 72 hours at renewal |

**Controls the college must run.** Each report lists complementary user entity controls: controls the customer must operate for the vendor's controls to work.
- **SIS:** role assignment, prompt account removal, MFA through SSO, audit report review, and protection of API credentials.
- **LMS:** management of local accounts, SSO configuration, course permissions, and administrator activity review.

Five of these are open gaps at the college:
- SIS roles (POAM-009);
- account removal (POAM-008);
- audit review (POAM-010);
- the integration secret (POAM-012);
- the adjunct LMS accounts (POAM-008, POAM-022).

**The vendors' controls only protect the college once these gaps are closed.**

**Follow-ups:**
- Obtain the SIS bridge letter through 2026-06-30 by 2026-10-31.
- The SIS report covers the analytics module that runs the early-alert model (AI-001), but a SOC 2 report does not say whether the vendor may use college data to train its models. That is handled by the contract amendment in P03 G-052 and the P10 conditions.
- Review the FAMS vendor's report and the servicer's security questionnaire by 2026-11-30 (POAM-002).

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.2, CC2.2, CC4.2, CC6.1 (servicer MFA), CC6.7, CC7.1, CC7.3-7.4, CC8.1, CC9.2 | Board report and minutes, policy acknowledgments, servicer amendment, scan and penetration test reports, tabletop report, change log, FAMS SOC 2 review |
| 2027 Q1 | CC6.1, CC6.2-6.3, CC6.8, CC7.2, CC7.5, CC9.1 | Role redesign and access reviews, EDR alerts and tickets, restore test records, contingency plan |
| 2027 Q2 | CC1.4, CC4.1, CC5.2-5.3, CC6.4-6.5 | Training records, monthly POA&M reviews, procedures, key log, disposal certificates |

**Next benchmark:** repeat this self-assessment in July 2027 with the annual risk assessment, and report the change to the Board in October 2027.

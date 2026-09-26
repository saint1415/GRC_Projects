# SOC 2 Readiness Summary: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm) |
| Tier / Vertical | Small / Administrative and Support and Waste Management and Remediation Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only, as a self-benchmark |
| Target report | None. The firm is not a SOC 2 service organization for its clients and does not plan a SOC 2 examination |
| Part A | Security-only self-benchmark (`soc2-readiness.csv`) |
| Part B | Review of the payroll platform vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager; approved by the COO, 2026-08-31 |

## 1. Why SOC 2 for this organization
**Two warehouse clients asked, in their 2026 vendor questionnaires, whether the firm has a SOC 2 report.** That question is common in staffing, so the first step was to decide whether a SOC 2 report is the right answer.

**The firm is not a SOC 2 service organization in the sense that matters.** A SOC 2 report describes a system that a service organization operates for its customers and the controls over that system. What the firm sells is labor: associates who work under the client's supervision, on the client's premises and the client's systems. The client information the firm holds is limited to contact names, job orders, bill rates, invoices, and the timesheets client supervisors approve in the portal. The firm does not store, process, or transmit client business data on the clients' behalf, and it does not operate any system the clients rely on for their own security or processing. The data that most needs protecting is the firm's own workforce data (associate SSNs, I-9 records, consumer reports), and the legal duties for it run to the associates and regulators, not to the clients. The vertical overlay names no sector alternative to SOC 2.

A CPA could still examine the firm under SOC 2; nothing forbids it. It is not proportionate now: a Type 2 needs controls that have operated for a period (typically 6 to 12 months), most of the firm's controls were defined in August 2026, and the clients' actual questions are about how the firm protects associate data and screens associates. **Revisit** if the firm starts offering a managed payroll or vendor management service that processes client data, or if a client makes a SOC 2 report a contract condition.

**So P09 is built in two parts:**

**A. Security-only self-benchmark.** The firm answers the client questionnaires with this self-benchmark against the Security (common criteria) of the Trust Services Criteria, its remediation dates, and the P03 CSF 2.0 gap analysis summary. The other four categories are marked N/A with a reason in `soc2-readiness.csv`:
- **Availability:** the firm makes no system availability commitments to clients. Dispatch and payroll continuity is handled by the BIA (P05) and covered under CC7.5 and CC9.1.
- **Confidentiality:** client confidential data held is limited; worker data confidentiality is covered by POL-04 and P03.
- **Processing Integrity:** the firm processes no transactions for clients. Payroll calculation integrity sits with the payroll vendor and is checked in Part B.
- **Privacy:** no privacy commitments to clients. Worker and candidate privacy duties come from the FCRA, 8 CFR 274a.2, and Fla. Stat. 501.171 (P03).

**B. Third-party risk management.** The payroll platform vendor holds every associate's SSN and bank account and moves about $270,000 each week. The firm inherits several controls from it (P02, P04). Its SOC 2 Type 2 report is the evidence for those controls, and the firm reviews it every year (SA-9; POL-01 4.8). The ATS vendor's report has been requested and will be reviewed the same way by 2026-12-31 (POAM-010).

## 2. System description (scope)
- **Services:** temporary staffing (Light Industrial, Office and Administrative) and direct-hire referrals in Florida.
- **Infrastructure and software:** the Associate Payroll and Applicant Tracking Platform (SSP, P02), office networks, and the SaaS applications.
- **People:** 60 internal staff, the managed IT provider, and about 450 associates on assignment weekly (as users of self-service and timekeeping).
- **Data:** associate and candidate personal information (SSNs, I-9 records, consumer reports, bank accounts, geolocation), client contacts, job orders, rates, and timesheets.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 19 | 9 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

In scope: 33 criteria (5 Ready, 19 Partially ready, 9 Not ready). Out of scope: 28 criteria.

**Ready:**
- CC1.3: security and compliance roles designated in writing
- CC3.1 and CC3.2: objectives, risk tolerance, and the 2026 risk assessment
- CC3.3: fraud risks (payroll diversion, bank-change fraud, invoice fraud, identity fraud in remote I-9 exams) are in the register
- CC4.2: deficiencies tracked in the POA&M with owners and dates

**Not ready:**
- CC2.1: no data inventory; no logs for the I-9 archive and reporting database
- CC3.4 and CC8.1: no change assessment or change control (the AI tool's mode changed without review)
- CC6.1 and CC6.3: phishable payroll sign-in, SSNs open to recruiters, over-broad ATS roles, and late removals
- CC7.1 and CC7.2: no vulnerability or activity monitoring beyond laptops
- CC7.5: no contingency plan or tested restore (the same gap as risk R-004)
- CC9.2: vendor risk not managed beyond the payroll vendor

## 4. Findings from the payroll vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception: some bank changes were processed without the vendor's optional confirmation email **because customers had turned it off. The firm has it turned off.** Turning it on is part of POAM-022.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 1 hour **meet the BIA** for weekly payroll (BP-01: RTO 24 h, RPO 24 h).
- **Controls the firm must run** (complementary user entity controls): user access and MFA, review of change and export reports, verification of bank changes the firm enters, and payroll register approval. Three are open gaps at the firm: MFA strength (POAM-002), report review (POAM-008), and bank-change verification (POAM-022). **The vendor's controls do not protect the firm until those close.** The scenario in P08 is exactly this failure.
- **Follow-ups:** obtain the bridge letter by 2026-10-31; ask how the vendor monitors its carved-out banking partners; register the Information Security Lead as the security contact.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1, CC6.2, CC6.3, CC2.2, CC7.3-7.4, CC3.4, CC8.1 | SSO enforcement report for payroll, access review sign-offs, termination tickets, policy acknowledgments, change log, tabletop report |
| 2027 Q1 | CC7.1-7.2, CC7.5, CC2.1, CC9.2, CC6.5-6.6 | Scan reports, alert tickets, restore test records, data inventory, vendor reviews, destruction certificates, kiosk network diagram |
| 2027 Q2 | CC1.2, CC4.1, CC5.1-5.3, CC9.1 | Quarterly oversight minutes, I-9 quality check results, procedures |

**Response to the two clients:** send this summary, the Security criteria checklist, and a one-page POA&M summary (P07). Commit to an updated self-benchmark in April 2027.

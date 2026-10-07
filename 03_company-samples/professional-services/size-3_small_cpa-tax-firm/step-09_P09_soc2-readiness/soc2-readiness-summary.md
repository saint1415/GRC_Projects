# SOC 2 Readiness Summary: Cris Santos Company | Professional, Scientific, and Technical Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| Tier / Vertical | Small / Professional, Scientific, and Technical Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. This is a self-benchmark, not a CPA-issued SOC 2 report |
| Part A | Security-only readiness self-benchmark (`soc2-readiness.csv`) |
| Part B | Tax software vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager (Qualified Individual), with the Tax Partner for Part B |

## 1. Why SOC 2 for this organization
**The firm is not a SOC 2 service organization.** A SOC 2 report describes a system that a service organization runs for its customers, where the customers rely on that system's controls. The firm delivers professional services: tax returns, audits, reviews, compilations, and advice. Clients do not operate their business on a firm system. The client portal is a delivery channel run by a vendor, not a service the firm offers to others. The firm's assurance practice also does not perform SOC examinations (scenario facts section 1). A formal SOC 2 audit of the firm would therefore answer a question no client is asking and would cost far more than the requests below justify.

SOC 2 is still useful here, in two ways:

**A. A Security-only self-benchmark for client questionnaires.** Business clients, especially those with lenders or private equity owners, send security questionnaires before sharing payroll, financial statements, and owner data. The Trust Services Criteria are the vocabulary those questionnaires use. The firm answers with this self-benchmark and its remediation plan. Security (the common criteria) is the only category included, because the firm makes no availability, processing integrity, or privacy commitments to clients through a system they rely on. Confidentiality of client data is already covered by CC6 and by the FTC Safeguards Rule program.

Assurance alternatives considered:
- **Engagement letters** (the vertical's usual client assurance): they set confidentiality duties and IRC 7216 consent terms, but say little about controls. The self-benchmark fills that gap.
- **A client-specific questionnaire:** still answered case by case, now drawing on this checklist.
- **The FTC Safeguards Rule program itself** (P03): binding, and the stronger answer for individual clients. The Qualified Individual's annual report to the Partner Group (from 2026-10-20) can be summarized for clients who ask.

**B. Vendor review (third-party risk).** The tax software vendor runs the system of record for returns and transmits them to the IRS. Many TPCP controls are inherited from it (P02, P04). Its SOC 2 Type 2 report is the evidence for those controls, and reviewing it each year supports 16 CFR 314.4(f)(3) (periodic assessment of service providers) and SA-9.

## 2. System description (scope of the self-benchmark)
- **Services:** individual and business tax preparation and e-file, assurance engagements, and client advisory work.
- **Infrastructure and software:** the Tax Preparation and Client Portal Platform (SSP, P02), plus practice management (SYS-07).
- **People:** 60 employees, about 6 seasonal preparers from January to April, and the MSP.
- **Data:** tax return information and customer information on about 21,000 consumers, business client financial data, and firm data.
- **Procedures:** POL-01 to POL-05 (P06), the incident response runbook (P08), and the POA&M (P07).

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 7 | 18 | 8 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: the Qualified Individual and reporting lines are designated in writing
- CC3.1, CC3.2, and CC3.3: objectives, the written risk assessment, and fraud risks (refund diversion, fraudulent returns, payment fraud) are documented in P01
- CC4.2: deficiencies are tracked in the POA&M and reviewed monthly
- CC6.4: physical access at both offices
- CC6.8: EDR and software installation controls

**Not ready:**
- CC1.2: the Partner Group has never received a written security report (314.4(i))
- CC3.4 and CC8.1: no change management or pre-adoption review (the AI extraction feature was turned on without one)
- CC6.3: standing admin rights and no need-to-know limits in the DMS
- CC6.5: no retention schedule; client files kept since 2009
- CC7.1 and CC7.2: no vulnerability scanning cadence and no after-hours or identity and email monitoring
- CC9.2: vendor management

The Not ready items overlap with the P01 High risks and the P07 High POA&M items. A client reviewer will see the same story in all three documents.

## 4. Findings from the tax software vendor report (Part B)
- **Opinion:** Type 2, unmodified, for the 12 months ending 2026-03-31. One exception (3 of 40 changes without documented approval), remediated by the vendor.
- **Availability:** the stated RTO of 4 hours and RPO of 1 hour **meet the firm's BIA** for return preparation and e-file (RTO 8 h, RPO 1 h). The report has no deadline-week capacity commitment, which matters for P01 R-019.
- **Controls the firm must run (complementary user entity controls).** The report expects customers to manage user access, enforce MFA through SSO, assign roles by least privilege, review user activity, and report suspected compromise. Three of these are High gaps at the firm today (POAM-002, POAM-003, POAM-004). **The vendor's controls protect the firm's clients only once those gaps are closed.**
- **The AI feature is outside the report.** The document extraction and return-drafting feature was released after the report period and sends documents to a sub-processor that the report does not list. The firm cannot yet show where that processing happens, which matters under 26 CFR 301.7216-2(d)(1) and 301.7216-3(b)(4). This is the main input to P10.
- **Follow-ups:**
  - Obtain a bridge letter through 2026-09-30 by 2026-10-31.
  - Obtain the AI sub-processor's identity, location, and assurance, and a U.S.-only processing clause (POAM-010).
  - Add a 72-hour incident notice term to the contract.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.1, CC1.2, CC1.5, CC2.1, CC2.2, CC2.3, CC4.1, CC6.1, CC6.3, CC7.1, CC7.4 | Signed acknowledgments, Partner Group report and minutes, MFA policy exports, admin role reports, monthly scan reports, penetration test report, tabletop report |
| 2027 Q1 | CC1.4, CC3.4, CC5.1, CC5.2, CC5.3, CC6.2, CC6.6, CC6.7, CC7.2, CC7.3, CC8.1, CC9.2 | Client MFA enrollment report, MSP contract amendment, 24x7 monitoring tickets, change log, vendor review records |
| 2027 Q2 | CC6.5, CC7.5, CC9.1 | Retention schedule and first disposal record, restore test records, approved contingency plan |

**Response to clients who ask:** send this summary, the readiness checklist, and a one-page extract of the POA&M status. Update the self-benchmark in July 2027 with the annual risk assessment.

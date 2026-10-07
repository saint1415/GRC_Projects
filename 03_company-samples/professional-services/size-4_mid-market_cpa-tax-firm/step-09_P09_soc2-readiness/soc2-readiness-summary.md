# SOC 2 Readiness Summary: Cris Santos Company | Professional, Scientific, and Technical Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed CPA, tax, and advisory firm, with its attest affiliate) |
| Tier / Vertical | Mid-Market / Professional, Scientific, and Technical Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| System in scope | The client accounting services (CAS) service: outsourced bookkeeping, bill pay, and payroll for business clients |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30; a Type 1 report as of 2027-03-31 as an interim deliverable |
| Service auditor | An unaffiliated CPA firm, selected by the audit committee. **Not** the Attest Firm and **not** the co-sourced internal audit firm |
| Part A | CAS readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-18 by the GRC Manager and the CAS Practice Leader, using P02, P05, P06, and P07 evidence; approved by the Chief Operating Officer on 2026-09-22 |

## 1. Why SOC 2 for this organization
A tax practice is usually **not** a SOC 2 service organization: clients rely on its professional judgment, not on a system it runs for them. The CAS service is different:
- The Company runs payroll for about 210 business clients and bookkeeping and bill pay for about 340. Those clients' employees get paid, and their vendors get paid, through processes the Company operates.
- Several CAS clients have lenders, boards, or private equity owners who ask how the Company protects their data and money. Their auditors ask whether the Company's controls over payroll and payments can be relied on.
- For the CAS service, the Company is a service organization, and a SOC 2 Type 2 report is the right way to answer the security, availability, processing accuracy, and confidentiality questions.

**SOC 1 as well.** Auditors of CAS clients mainly need a **SOC 1 Type 2** report on controls relevant to their clients' financial reporting (payroll and payments). The Company will commission a SOC 1 Type 2 report on the same observation period. Its control objectives overlap heavily with the Processing Integrity and Security rows here. This readiness assessment covers SOC 2 only.

**Who can examine the Company.** The Company sells SOC examinations through the Attest Firm, but the Attest Firm cannot examine the Company's own CAS system. The two entities share staff, systems, and economics under the administrative services agreement, so the Attest Firm would not be independent of the Company. AICPA independence rules govern this; their text was not verified for this sample, but the conclusion does not depend on the detail. The audit committee will engage an unaffiliated CPA firm. The co-sourced internal audit firm is excluded as well: it works for management and the audit committee inside the program, and the audit committee wants the external examination kept separate from internal audit.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in exactly the controls a CAS client cares about: accounts outside SSO, single-approver bank changes, no monitoring of CAS activity, and an untested payroll fallback. Starting the observation period before those are fixed would produce exceptions or a qualified opinion. The plan is to remediate through 2027 Q1, issue a Type 1 as of 2027-03-31, and run the Type 2 period from 2027-04-01. The observation period also avoids the busiest weeks of the filing season for the shared IT and security team.

**Alternatives considered:**
- **Engagement letters and CAS agreements only** (the vertical's usual client assurance): they set confidentiality duties but say little about controls. Not enough for clients whose auditors rely on payroll controls.
- **A security questionnaire for each client:** what the Company does today; it does not scale to several hundred CAS clients and gives auditors nothing to rely on.
- **ISO/IEC 27001 certification:** recognized, but it does not report on operating effectiveness over a period, and CAS clients' auditors asked for SOC reports.
- **The FTC Safeguards Rule program (P03):** binding and the base for everything here, but it is not an independent attestation.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Payroll processing, bookkeeping, and bill pay for business clients |
| Infrastructure | Company endpoints and office networks used by CAS staff, the identity provider, the productivity suite, and the client portal (common controls documented in the SSP, P02) |
| Software | The CAS platform (SYS-08): cloud accounting, bill-pay, and payroll services, run by vendors |
| People | CAS staff (70), IT and security team, MSSP |
| Data | Client ledgers, vendor and employee bank details, payroll data |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks, and the CAS procedures to be written (CC5.3) |
| Subservice organizations (carve-out) | Payroll processing service, cloud accounting and bill-pay services, identity provider, productivity suite vendor, cloud provider, MSSP. Their controls are covered by their own SOC reports and the complementary subservice organization controls listed in the system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 17 | 6 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **13** | **22** | **8** | **18** |

43 criteria are in scope. Privacy is out of scope because CAS processes personal information on behalf of business clients, which make the privacy commitments to their own employees and payees. The confidentiality of that data is covered by C1 and CC6.

**Ready (13):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC3.1, CC3.2, CC3.3;
- monitoring of controls: CC4.1, CC4.2;
- physical access and malware: CC6.4, CC6.8;
- capacity: A1.1;
- outputs and stored data: PI1.4, PI1.5.

**Not ready (8):**
- CC3.4: SaaS feature changes and acquisitions are not assessed for control impact;
- CC6.2 and CC6.3: local accounts outside SSO (3 former staff active) and single-approver bank changes;
- CC7.2: no monitoring of CAS activity;
- CC7.5 and A1.3: the CAS payroll fallback has never been exercised;
- CC9.2: payroll and bill-pay vendors not reviewed since onboarding;
- C1.2: no return or deletion of client data when a CAS client leaves.

Each maps to a P07 POA&M item. The Partially ready criteria mostly depend on standards being issued (P06), SIEM onboarding, and the CAS procedures.

**Mapping to other work.** Evidence is reused from P02 (common control statements), P05 (availability commitments for BP-10 and BP-11), P06 (policies), P07 (test results), and P08 (CAS payment holds and notices to CAS clients). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.2, CC6.1, CC6.2, CC6.3, CC6.7, CC7.1, CC7.3, CC7.4, CC9.1, PI1.2, PI1.3 | SSO federation records; monthly local-account reconciliations; dual-approval settings; call-back logs; payroll second-review sign-offs; tabletop report; patch metrics |
| 2027 Q1 | CC1.2, CC1.4, CC2.1, CC2.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.6, CC7.2, CC7.5, CC8.1, CC9.2, A1.2, A1.3, C1.1, PI1.1 | Audit committee minutes; CAS training records; SIEM source list and CAS alerts; system description; CAS procedures; security key enrollment; payroll fallback exercise report; change tickets for SaaS settings; Tier 1 vendor reviews and bridge letters; client service specification sheets |
| 2027-03-31 | Type 1 (design) report, issued by the unaffiliated service auditor | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence (quarterly access reviews, monthly reconciliations, payroll reviews, vendor reviews, monitoring tickets) |
| 2027 Q2 | CC6.5, C1.2 | First disposal run; CAS client offboarding records |

**Budget.** $210,000 across 2027 for readiness support, the Type 1 report, and the Type 2 examination, approved in the FY2027 security plan (P01). The SOC 1 Type 2 report is budgeted separately by the CAS practice.

**Status reporting.** The CAS Practice Leader and the GRC Manager report readiness monthly to the Chief Operating Officer and quarterly to the audit committee.

## 5. Vendor SOC 2 review program (Part B)
The Company relies on vendor controls for many inherited controls (P02: 14 Common/Inherited and 37 Hybrid). For the CAS SOC 2, the payroll and accounting vendors are subservice organizations, so their reports must be reviewed before the Company's own system description can be written. The program in `vendor-soc2-review.csv` is the core of STD-03 and supports 16 CFR 314.4(f)(3).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Restricted data at scale, privileged access to Company systems, money movement, or support for a High-criticality BIA process | SOC 2 Type 2 (or SOC 1 Type 2 where financial reporting controls matter, or an equivalent Company assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, complementary user entity controls mapped to Company controls, availability against the BIA, and incident terms | Annually |
| **Tier 2** | Limited Restricted data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No client data and no system access | Contract terms only | At contract renewal |

Of about 85 service providers, 14 are Tier 1 and about 40 are Tier 2 under this approach. The CSV holds 9 Tier 1 reviews and 1 Tier 2 example. The remaining 5 Tier 1 reviews are due by 2027-03-31 (POAM-017).

**Key findings:**
1. **Payroll service:** unmodified SOC 1 and SOC 2 reports. Its complementary user entity controls (approving changes, verifying bank changes, reviewing users) are exactly the controls that are Not ready at the Company (CC6.2, CC6.3). **The vendor's controls protect CAS clients only once the Company closes those gaps.**
2. **Tax software vendor:** unmodified Type 2; RTO 8 hours meets the BIA with no margin; the AI extraction sub-processor is outside the report (P10).
3. **Bill-pay service:** its bridge letter is overdue, and its report noted an exception on bank change verification by its own support staff, which raises the importance of the Company's own call-back control.
4. **MSSP:** unmodified Security-only report with 2 missed escalations in 40 samples; no BAA even though its logs can contain PHI.
5. **Offshore preparation vendor:** no SOC 2. Its ISO/IEC 27001 certificate does not cover the Company desktops its staff use. The Company will perform its own assessment with a site review by 2027-03-31.

# SOC 2 Readiness Summary: Cris Santos Company | Real Estate and Rental and Leasing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC (PE-backed residential real estate brokerage with property management and title and closing services) |
| Tier / Vertical | Mid-Market / Real Estate and Rental and Leasing |
| Service organization | Cris Santos Title and Closing, LLC, with the parent company as the provider of its IT, security, HR, and finance services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30; Type 1 report as of 2027-03-31 as an interim deliverable |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-22 by the vCISO and the Security Manager (Qualified Individual), using P02, P05, P06, and P07 evidence; approved by the President of Title and Closing and the Chief Operating Officer, 2026-09-29 |

## 1. Why SOC 2 for this organization
A residential brokerage is usually **not** a SOC 2 service organization: it serves consumers, and its clients do not rely on its controls for their own financial reporting or compliance. Title and Closing is different:
- About 38% of its 8,400 closings a year come from other brokerages, 2 regional mortgage lenders, and a national homebuilder (about 900 new-home closings a year in 2 Florida communities).
- It holds and disburses those clients' money (about $3.6 billion a year from its trust accounts), so the lenders and the homebuilder depend on its controls over disbursement accuracy, wire fraud, and borrower data.
- The 2 lenders and the homebuilder require a SOC 2 Type 2 report from Title and Closing by 2027 (`../00_company-facts.md` section 7).

For those closing and escrow disbursement services, Title and Closing is a service organization, and a SOC 2 Type 2 report is the right assurance tool. The clients asked for Security, Availability, and Confidentiality; **Processing Integrity** was added because the question they care about most is whether money goes only where the closing instructions say (Fla. Stat. 626.8473(4)).

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated over a period. P07 found gaps in payee verification, access, monitoring of SaaS activity, recovery, and portal change control. An observation period started before those are fixed would produce exceptions. The plan is to remediate through 2027 Q1, issue a Type 1 report as of 2027-03-31, and run a 6-month Type 2 period from 2027-04-01.

**Alternatives considered:**
- **Type 1 only:** accepted by the homebuilder as an interim step, but both lenders require a Type 2.
- **Lender security questionnaires and on-site audits:** what happens today; each lender spends about 2 weeks a year auditing Title and Closing, and the answers do not reach the homebuilder.
- **ISO/IEC 27001 certification:** not requested by any client and covers no processing integrity criteria.
- **Industry best-practice attestations for title agents:** useful for the underwriter relationship but not accepted by the lenders' vendor management teams in place of SOC 2.

**Service auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the internal audit work in P07 does not create an independence question.

**Link to the Safeguards Rule.** SOC 2 is not required by 16 CFR Part 314, but the observation-period evidence (quarterly reviews, payee change tests, restore tests, vendor reviews) also supports the regular testing in 314.4(d)(1) and the Qualified Individual's annual report (314.4(i)).

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Title and Closing's closing, settlement, and escrow disbursement services for buyers, sellers, lenders, other brokerages, and the homebuilder: title orders, settlement statements, payoff verification, wire instruction delivery, disbursement, and trust account reconciliation |
| Infrastructure | TMCC components used by Title and Closing (P02): the cloud landing zone with the Closing Communications Portal (P04), the headquarters network and title operations center, the 8 sales offices with closing rooms, company endpoints used by Title and Closing staff, and the SIEM |
| Software | SYS-02 title production and closing software; the Closing Communications Portal; the identity provider (SYS-03); the productivity suite (SYS-04) for Title and Closing staff; e-signature (SYS-12); bank platforms for the title trust accounts (SYS-09) as interfaces |
| People | 112 Title and Closing staff, the Title Escrow Accounting Manager's team, the parent's IT and security team, the vCISO, and the MSSP |
| Data | Title and Closing customer information (about 98,000 consumers since 2012), closing packages from lenders, payee and disbursement data |
| Procedures | POL-01 to POL-05, the standards index (STD-05 payment verification above all), the P08 runbooks, and closing procedures |
| Subservice organizations (carve-out) | Title production vendor, identity provider, productivity suite provider, cloud provider, MSSP, and e-signature service. Their controls are covered by their own SOC 2 reports (Part B), and the system description will list the complementary subservice organization controls the company relies on |
| Not in scope | The brokerage's sales and property management operations, contractor agents, SYS-10, SYS-11, and SYS-13. The identity and email tenant is shared with contractor agents, so agent MFA still matters to CC6.1 |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 12 | 17 | 4 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **15** | **22** | **6** | **18** |

**Ready (15):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2, CC3.3 (fraud risk sits at the center of the risk assessment);
- monitoring and control design: CC4.2, CC5.1;
- access and protection: CC6.2, CC6.6, CC6.8;
- capacity: A1.1;
- processing: PI1.3 (dual approval, positive pay, daily three-way reconciliation) and PI1.5.

**Not ready (6):**
- CC6.3: unneeded export rights, standing administrators, and late removal of prior-role and bank platform access;
- CC7.2: payee changes and exports inside SYS-02 are not monitored;
- CC7.5 and A1.3: recovery is documented and tested only for the portal;
- CC8.1: the portal that delivers wire instructions has no secure change control;
- C1.2: no retention schedule, so confidential information is never disposed of.

Each Not ready criterion maps to a P07 POA&M item (POAM-003 to POAM-005, POAM-008, POAM-010, POAM-013). The Partially ready criteria mostly depend on standards being issued (P06), on payee verification for edits to existing payees (PI1.2, POAM-002), and on documenting service commitments to clients (CC2.3, PI1.1). The readiness work itself is tracked as POAM-019.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies), P07 (test results and samples), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. The mapping is the author's; AICPA publishes its own mapping of the TSC to SP 800-53, which the service auditor may use.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.2, CC1.4, CC3.4, CC6.1 (agent MFA, secrets), CC6.3, CC6.7, CC7.3, PI1.2 | Board of managers minutes and the 314.4(i) report; payee change approvals and callback logs; quarterly access review sign-offs; MFA reports; encryption rule logs; single incident log |
| 2027 Q1 | CC2.1, CC2.3, CC4.1, CC5.2, CC5.3, CC6.5, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, A1.2, A1.3, C1.1, C1.2, PI1.1, PI1.4 | SIEM alerts on SaaS events; restore test records and the 2027-01-21 drill report; pipeline approvals and scan results; issued standards; vendor reviews; first retention purge certificates; quarterly STD-05 sample test; tabletop reports |
| 2027-03-31 | Type 1 (design) report | Management's system description, service commitments, and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence (quarterly reviews, payee change tests, restore tests, vendor reviews, monitoring reports) |
| 2027 Q1-Q2 | CC6.4 (badge readers: offices with closing rooms by 2027-03-31, the rest by 2027-06-30) | Badge system reports |

**Status reporting.** The vCISO reports readiness monthly to the COO and the President of Title and Closing, and quarterly to the audit committee and Title and Closing's board of managers. The lenders and the homebuilder receive a quarterly status letter until the Type 1 report is issued.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 13 Common/Inherited and 36 Hybrid). Under the Safeguards Rule it must also periodically assess its service providers (16 CFR 314.4(f)(3)). The program in `vendor-soc2-review.csv` makes that reliance evidence-based and is the core of STD-03.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Customer or consumer information at scale, privileged access to company systems, or support for a High-criticality BIA process | SOC 2 Type 2 (or an equivalent independent assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, complementary user entity controls (CUECs) mapped to company controls, availability against the BIA, and incident notice terms | Annually |
| **Tier 2** | Limited customer or consumer information, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No customer or consumer information and no system access | Contract terms only | At contract renewal |

Of the 42 service providers with customer or consumer information, 11 are Tier 1. The CSV holds the 7 completed Tier 1 reviews (VEN-01 to VEN-07), the 4 Tier 1 reviews still pending (VEN-08 to VEN-11, due 2027-01-31, POAM-015), and 1 Tier 2 example (VEN-12).

**Key findings:**
1. **Title production vendor (VEN-02):** unqualified Type 2 covering all four requested categories. Its stated RTO of 24 hours and RPO of 1 hour **do not meet the BIA** (RTO 4 hours and RPO 15 minutes for BP-01). Its most important CUEC, configuring payee approval rules, is a company gap: the two-person rule covers only new payees (POAM-002). **The vendor's controls protect client money only once that gap closes.**
2. **Transaction platform and property management platform (VEN-01, VEN-07):** both rely on the company to remove users and review audit logs, which are open gaps (POAM-003, POAM-005). The property management platform's RTO of 12 hours does not meet the 8-hour need for maintenance dispatch.
3. **MSSP (VEN-06):** unqualified Type 2 (Security only) with an exception for missed 30-minute escalations in 2 of 40 samples. The SIEM platform is carved out, and its own SOC 2 must be obtained. Log source coverage is the company's CUEC and is incomplete.
4. **Contract development firm (VEN-09):** has no SOC 2 report and no breach notice term, yet it can deploy the code that shows wire instructions. Secure development and notice terms are due 2026-12-15 (POAM-010).
5. **Tenant screening provider (VEN-10):** no security terms in its contract; its review is also a condition of the P10 decision on AI-001.

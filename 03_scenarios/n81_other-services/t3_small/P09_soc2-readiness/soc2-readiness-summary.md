# SOC 2 Readiness Summary: Cris Santos Company | Other Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electronics and device repair service) |
| Tier / Vertical | Small / Other Services (except Public Administration) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Internal benchmark; no CPA-issued SOC 2 report is planned |
| Part A | Security-only readiness benchmark (`soc2-readiness.csv`) |
| Part B | Review of the ticketing and POS vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-21 by the IT Manager, with the Controller for Part B (fieldwork 2026-08-17 to 2026-08-21) |
| Approved | General Manager, 2026-09-04 |

## 1. Why SOC 2 (or an alternative) for this organization
**The company is not a SOC 2 service organization.** SOC 2 reports on the controls of a company that operates systems or processes data *as a service for other businesses*, where those controls affect the customers' own security. A repair shop fixes hardware and hands it back. It does not run systems for its customers. Most of its customers are consumers, who do not ask for SOC 2 reports. The vertical overlay names no SOC 2 alternative, and none of the company's assurance obligations is a SOC 2 report:
- **PCI DSS validation** (SAQ P2PE, due 2026-11-30) is the assurance the acquirer relies on (P03).
- **The Manufacturer A program audit** (2026-10) is the assurance Manufacturer A relies on.

SOC 2 appears here for two practical reasons:

**A. A common yardstick for business account questionnaires.** About 140 business accounts (small businesses, 2 private schools, a property manager) send their devices, with their data, to the company. Four of them sent security questionnaires in 2026, each in a different format. The Security criteria (CC1-CC9) give one structured self-assessment that the Business Accounts Manager can use to answer them, and that also covers what the Manufacturer A audit asks about (access, training, incident notice, vendor control). It reuses work already done in P01, P02, P06, and P07.

Other options considered:
- **A formal SOC 2 audit:** no customer requires one, and a Type 2 audit needs controls that have operated for months. Most of the company's controls were defined in September 2026.
- **Answering each questionnaire separately:** more work and less consistent.
- **Adding the Confidentiality category:** it fits the business (customer device data, disposal), but those duties are already assessed against the law in P03 (Fla. Stat. 501.171(8) and FTC Act rows). It can be added in 2027 if business accounts ask for it.

**B. Third-party risk management.** The company depends on its ticketing and POS vendor for most of the controls it inherits (P02, P04). The vendor's SOC 2 Type 2 report is the evidence for those controls, and the company reviews it every year (POL-01 4.8).

## 2. System description (scope)
- **Services:** walk-in, mail-in, and business account repair; data recovery and transfer; recycling drop-off.
- **Infrastructure and software:** the Service Ticketing and Point-of-Sale Platform (SSP, P02) and its cloud tenant (P04).
- **People:** 60 workforce members, including 30 technicians who handle customer devices.
- **Data:** customer records and tickets, device content in custody, recovered data, business account data. Card data stays in the P2PE terminals.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 18 | 10 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: the Information Security Lead and reporting lines are designated
- CC3.1 and CC3.2: objectives are set and the risk assessment is done
- CC4.2: deficiencies are tracked in the POA&M
- CC6.6: site firewalls, no inbound services, MFA on remote access

**Not ready:**
- CC6.1 and CC6.3: every user can read passcodes; technicians have unlimited access to device content; former employees still active
- CC6.5: a recycling phone still held its owner's data; recovered data kept indefinitely
- CC2.3: the intake notice promises something the company does not do
- CC7.1, CC7.2: no scanning, and nobody reviews logs
- CC7.5: lab backups unproven
- CC3.4 and CC8.1: no change or new-service review (the AI tools went live without one)
- CC9.2: AI vendors, recycler, and courier have no terms

**What a business account would notice first:** CC6.1, CC6.3, and CC6.5 together. The question business customers ask is "who can see our data on the devices we send you, and what happens to it afterwards?" Today the honest answer is "any technician, and we keep it." The POA&M items POAM-001 to POAM-003 and POAM-012 change that answer, and should close before the next questionnaire response.

## 4. Findings from the vendor report (Part B)
- **Opinion:** SOC 2 Type 2 (Security and Availability), unqualified, 12 months to 2026-03-31. One change-approval exception at the vendor, remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the BIA** for intake and release (P05 BP-01 and BP-03).
- **Controls the company must run (CUECs).** The report says the customer must manage users, assign roles by least privilege, enable MFA, review audit logs and exports, and **not store payment card data or credentials in free-text fields**. The company breaks the last one today (passcodes, account passwords, and 37 card numbers in notes) and has open gaps on roles, MFA for counter logins, user removal, and log review (POAM-001, POAM-007, POAM-008, POAM-015). **The vendor's controls protect the company only once these gaps are closed.**
- **Useful features not in use:** role-based field permissions and a restricted credential field with automatic purge. Turning them on is the core of POAM-001 and costs nothing extra.
- **Follow-ups:** confirm the vendor reviews its carved-out subservice providers (hosting and text messaging); request an updated bridge letter before the Manufacturer A audit; ask for 24-hour incident notice at renewal to match the company's own contract clocks. The vendor's stated 72 hours is already inside the 10-day outer limit for third-party agents in Fla. Stat. 501.171(6)(a).

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1, CC6.2, CC6.3, CC6.5, CC2.2, CC2.3, CC1.1, CC7.3, CC7.4 | SYS-01 role report and purge record, named-account list, access reviews, sanitization certificates, signed confidentiality agreements, revised intake notice, tabletop report |
| 2027 Q1 | CC6.7, CC6.8, CC7.1, CC7.2, CC7.5, CC9.1, CC9.2 | USB block settings, EDR coverage, scan reports, weekly log review checklists, restore test records, contingency plan, signed vendor addenda |
| 2027 Q2 | CC1.2, CC3.3, CC3.4, CC4.1, CC8.1 | Owner review minutes, updated risk assessment, change log, quarterly POA&M reviews |

**Next benchmark:** repeat this self-assessment in August 2027. Send the Section 3 summary and the POA&M status (not the full POA&M) to business accounts that ask.

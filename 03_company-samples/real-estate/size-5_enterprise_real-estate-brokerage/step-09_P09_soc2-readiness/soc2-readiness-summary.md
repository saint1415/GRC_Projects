# SOC 2 Readiness Summary: Cris Santos Company | Real Estate and Rental and Leasing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded residential real estate brokerage) with Cris Santos Title and Escrow, LLC and Cris Santos Relocation, LLC |
| Tier / Vertical | Enterprise / Real Estate and Rental and Leasing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Service lines | SL-1 title and settlement services (Title and Escrow, for lenders, other brokerages, and homebuilders); SL-2 corporate relocation services (Relocation, for about 280 corporate clients) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new) Processing Integrity. SL-2: Security, Availability, Confidentiality, and Privacy |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Processing Integrity added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-09-04 by the GRC team with the President of Title and Escrow and the President of Relocation, after the Internal Audit fieldwork (P07); reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is brokerage for consumers, which SOC 2 does not cover. Two service lines are different: the company **provides services to other businesses**, so it is a service organization for them, and those businesses ask for a CPA's SOC 2 report.
- **SL-1 title and settlement services.** About 45% of Title and Escrow's 88,000 closings a year come from lenders, other brokerages, and homebuilders. Lenders' vendor programs require a SOC 2 Type 2 report before they send closing funds and borrower data. SL-1 has issued a Type 2 report (Security, Availability, Confidentiality) every year since 2024. After the 2026 H1 diverted-wire incidents, the largest lenders now ask for **Processing Integrity**, because accurate and authorized disbursement is the core commitment.
- **SL-2 corporate relocation services.** Corporate clients send their relocating employees' personal and household data and fund home-sale and move programs. Their procurement teams increasingly require a SOC 2 Type 2 report, and several ask for **Privacy** because Relocation collects data directly from employees and their families.

**Alternatives considered:** the lenders' own vendor questionnaires (they accept a SOC 2 report in place of most questions, which saves time on about 1,900 business clients); ISO/IEC 27001 certification (some multinational relocation clients accept it, but U.S. lenders ask for SOC 2); industry best-practice frameworks for title and settlement agents (useful as a checklist, but they are not an independent attestation and do not replace SOC 2 for lenders). The CPPA cybersecurity audit (P03 G-073) is a separate legal requirement; the evidence below will be reused for it where the scopes overlap.

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports, the Safeguards Rule program, and SOX. The cloud providers, the title production platform vendor (SYS-02), and the relocation platform vendor (SYS-13) are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 title and settlement services | SL-2 corporate relocation services |
|---|---|---|
| Services | Title search and policy issuance support, settlement statements, closing, disbursement of closing funds, payoff verification | Move management, home-sale program administration, expense processing and payment for relocating employees |
| Infrastructure | Cloud provider A TMCC workload accounts, landing zone controls, second-region standby (P02, P04) | Relocation platform (vendor SaaS, SYS-13); enterprise identity, network, and endpoints |
| Software | Company-built Closing Communications Hub and Disbursement Hub; SYS-02 tenant configuration; bank connectors | SYS-13 tenant configuration; expense payment integration with SYS-12 |
| People | Title and Escrow closers, payoff specialists, escrow accounting; closing platform engineering; SOC | Relocation client managers and expense team (700 staff); SOC; identity team |
| Data | Borrower, buyer, and seller customer information; payee bank details; settlement statements | Relocating employees' personal, household, and immigration data; expense and payment data |
| Procedures | P06 policy hierarchy; PRC-04.3 payee verification; P08 BEC runbook | P06; relocation program procedures; P08 notification steps |
| Subservice organizations (carved out) | Cloud provider A; title production platform vendor; bank account ownership verification provider; e-signature service | Relocation platform vendor; moving and household goods partners (complementary controls named in client agreements) |
| Excluded | AQ-09 (acquired Texas title agency) until its migration into SYS-02 and the Disbursement Hub (POAM-005, due 2027-02-28); it will be added to the system description for the 2028 period | None |

## 3. Readiness results
**SL-1 title and settlement services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 28 | 5 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 corporate relocation services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 25 | 7 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | 11 | 7 | 0 | 0 |

Totals across both lines: 75 Ready, 23 Partially ready, 1 Not ready, 23 N/A (122 rows).

**SL-1** is ready for its next Type 2 on the existing categories once 7 partially ready items close: CC6.1 (bank API secrets, POAM-010), CC6.2 and CC6.3 (external Hub accounts, POAM-017), CC8.1 (emergency changes, POAM-009), CC9.2 (e-signature vendor review, POAM-012), A1.3 (Disbursement Hub DR retest, POAM-011), and PI1.3 (payee verification coverage, POAM-006). All but PI1.3 close before the period starts on 2027-01-01. PI1.3 closes on 2027-03-31; until then the report would describe the compensating control (a second escrow officer's callback for disbursements without electronic verification), and the service auditor may report an exception for the first quarter.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: CC6.3 (no access review of SYS-13; a test of 120 accounts found 31 departed employees still active). Partially ready: CC1.3, CC2.3, CC3.1, CC6.2, CC7.2, CC7.5, CC9.2, A1.3, C1.2, P3.2, P4.2, P4.3, P6.2, P6.4, P6.5, P6.7. The gaps are first-report gaps: a written system description, a named system owner, access reviews and logging for a SaaS platform that was never onboarded to the enterprise controls, partner contract terms, and privacy records that live in email and paper. All are due by 2027-03-31, so the period can start on 2027-04-01.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC6.1, CC6.2, CC6.3, CC8.1, CC9.2; SL-2 CC1.3 | Vault bank secrets; external account cleanup and attestation; pipeline enforcement of two approvals; e-signature review; name the SL-2 system owner | Vault inventory; inactivity job reports; attestations; change records; vendor review |
| 2027 Q1 | SL-1 A1.3, PI1.3; SL-2 CC2.3, CC3.1, CC6.2, CC6.3, CC7.2, CC7.5, CC9.2, A1.3, C1.2, P3.2, P4.2, P4.3, P6.2, P6.4, P6.5, P6.7 | Disbursement Hub DR retest; payee verification to 98%; SL-2 system description; SYS-13 access reviews and SIEM connector; partner terms; electronic consent, retention, and disclosure log | DR retest report; verification coverage reports; SYS-13 certifications; partner contracts; consent and disclosure logs |
| 2027 Q1 (March) | Readiness check by Internal Audit (both lines); SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q3 and Q4 | SL-1 period continues; SL-2 period ends 2027-09-30 | Fieldwork for both reports | Type 2 samples per the evidence map |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 13 collecting, 5 ready, 7 not started (each tied to a POA&M item or a 2027 Q1 action). The 12 items marked Both also feed the Qualified Individual's annual report and the first CPPA cybersecurity audit.

**Client communication:** SL-1 clients receive the 2025 report (issued 2026-02), a bridge letter covering 2026, and a letter describing the Processing Integrity addition and the payee verification program. SL-2 clients receive this summary, the remediation timeline, and the expected first report date (2027-11).

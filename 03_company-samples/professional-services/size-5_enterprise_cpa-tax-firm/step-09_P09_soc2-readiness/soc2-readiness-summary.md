# SOC 2 Readiness Summary: Cris Santos Company | Professional, Scientific, and Technical Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP (national CPA and tax firm; privately owned by its partners) |
| Tier / Vertical | Enterprise / Professional, Scientific, and Technical Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Service lines | SL-1 client accounting and payroll services (about 3,100 client businesses, about 410,000 client employees); SL-2 tax compliance outsourcing with the corporate client tax portal (about 380 corporate clients, about 38,000 global mobility assignees) |
| Categories in scope | SL-1: Security, Availability, Confidentiality, and (new for 2027) Processing Integrity. SL-2: Security, Availability, and Confidentiality |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Service auditor | An unaffiliated CPA firm. The firm's own SOC examination practice may not examine the firm (scenario facts section 1) |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (26 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the two service line leaders; reviewed by the CISO and the Chief Audit Executive. Updated 2026-09-04 for the Internal Audit results (P07) |

## 1. Why SOC 2 for this organization
Most of the firm's work is professional services: tax returns, audits, and advice. SOC 2 does not fit those, because clients do not run their business on a firm system. Two service lines are different. In each, the firm runs a system that clients rely on to operate, so the firm is a **service organization** for them:
- **SL-1 client accounting and payroll.** The firm runs bookkeeping, close, bill pay, and payroll for about 3,100 client businesses on per-client accounting SaaS instances and a firm-built payroll engine. Clients and their auditors rely on it. SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2024, plus a SOC 1 Type 2 for payroll (out of scope here). The 2025 SOC 2 report had one exception, late access removal, since remediated (P01 R-046). Clients now ask for **Processing Integrity**, because pay-date accuracy is the core commitment (P01 R-057).
- **SL-2 tax compliance outsourcing.** About 380 corporate clients outsource their entity and global mobility tax compliance to the firm and exchange data through the corporate client tax portal. Their vendor risk programs now require a SOC 2 Type 2 report. SL-2 has never had one, and losing clients over it is P01 risk R-047.

**Alternatives considered:**
- **SOC 1 only for SL-2.** SL-2 affects clients' tax provisions, so a few clients' auditors may also ask for a SOC 1. Corporate clients' security and procurement teams ask for SOC 2, so it comes first.
- **A Type 1 report for SL-2 first.** Rejected: the largest clients' vendor programs accept only Type 2, and a Type 1 would delay the Type 2 by a full cycle.
- **Engagement letters and questionnaires** (the vertical's usual client assurance). They remain the answer for the firm's professional services, but they cannot replace an independent report for outsourced operations at this scale.

**Relationship to other assurance.** Both service lines inherit the enterprise common controls (P02 section 10.3; P04 section 5), so one set of evidence serves both reports, the Safeguards Rule program (P03), and the Internal Audit plan (P07). Cloud providers, the accounting SaaS provider, the tax software vendor and transmitter, the DMS vendor, the ACH originating bank, the payroll tax filing service, and the offshore tax outsourcing provider are subservice organizations presented with the **carve-out method**. Their SOC reports are reviewed under CC9.2, and the complementary subservice organization controls the firm relies on are listed in each system description.

**Independence.** Engagement acceptance (SYS-11) checks independence before SL-1 or SL-2 work is accepted for any attest client. The readiness work was done by the GRC team and Internal Audit, not by the SOC examination practice that sells these services to clients.

## 2. System description (scope)
| Element | SL-1 client accounting and payroll | SL-2 tax compliance outsourcing |
|---|---|---|
| Services | Bookkeeping, monthly close, bill pay, payroll processing, payroll tax deposits and filings | Entity income tax returns, state and local filings, tax provision support, global mobility returns and assignee support |
| Infrastructure | Cloud provider B (payroll engine, landing zone controls, standby region); identity platform; SOC | Cloud provider A (Tax Engagement Platform, P02); identity platform; SOC; colocation offline backups |
| Software | Per-client accounting SaaS instances; firm-built payroll engine; ACH file creation | Licensed tax software and e-file; tax workflow; corporate client tax portal (part of SYS-02); DMS; assignee assistant (AI-003, P10) |
| People | About 1,300 client accounting staff; identity, cloud platform, and SOC teams | About 1,700 SL-2 staff plus seasonal staff for the global mobility peak; offshore provider staff under consent |
| Data | Client ledgers, vendor and bank details, client employees' payroll and tax data | Corporate tax data, assignee tax return information, tax provision workpapers |
| Procedures | P06 policy hierarchy; P08 runbook; SL-1 payroll procedures | P06 (including STD-04.4 and PRC-04.1); P08; SL-2 delivery procedures |
| Subservice organizations (carve-out) | Accounting SaaS provider; Cloud provider B; ACH originating bank; payroll tax filing service | Cloud provider A; tax software vendor and transmitter; DMS vendor; offshore tax outsourcing provider |

**Categories excluded and why.** Privacy is out of scope for both lines: SL-1 processes client employees' data on the clients' instructions and does not collect it from them directly, and Privacy for SL-2 is deferred to its second period, after the assignee portal and AI-003 privacy notice are aligned (decision 2026-08-21). Processing Integrity is out of scope for SL-2 because return accuracy is a professional judgment governed by the firm's quality management system, not a system processing commitment.

## 3. Readiness results
**SL-1 client accounting and payroll**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 30 | 3 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-2 tax compliance outsourcing**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 21 | 11 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**SL-1 is ready** for its 2027 period on the existing categories. Three Security criteria and one Confidentiality criterion are partially ready: CC2.3 (client notice terms not in the central register, POAM-023), CC6.2 (the monthly access removal check that fixes the 2025 exception has not yet run for a full quarter), CC7.2 (session token replay detection, POAM-004), and C1.2 (37 former clients' data past the contract deletion date). For the new Processing Integrity category, PI1.1 (processing objectives not yet in the system description) and PI1.3 (manual, not per-client, variance thresholds) are partially ready. All close by 2027-03-31; the CC items close before the period starts.

**SL-2 is not yet ready** for its period to start. Not ready: CC6.3 (SL-2 repositories open to whole office tax teams in the DMS). Partially ready: CC2.3, CC4.1, CC6.1, CC6.2, CC6.7, CC7.1, CC7.2, CC7.5, CC8.1, CC9.1, CC9.2, A1.3, C1.1, and C1.2. These are the same gaps Internal Audit found in the Tax Engagement Platform (P07): client account MFA, seasonal terminations, DMS need-to-know, the legacy file transfer endpoint, patch timeliness, token replay detection, the recovery time shortfall, change test evidence, transmitter concentration, vendor reviews, and the offshore consent and masking exceptions. Closing POAM-002, POAM-003, POAM-004, POAM-006, POAM-008, POAM-009, POAM-011, POAM-013, POAM-015, POAM-016, and POAM-023, together with the SL-2 system description (2027-01-31), the transmitter scenario, drill, and contract amendment (POAM-019 milestones through 2027-03-31), and Internal Audit's readiness test (2027-03-15), makes SL-2 ready to start its period on 2027-04-01. Two items close later and would be described in the report if still open: the second e-file transmission path (POAM-019, decision 2027-09-01; the early-extension plan is the compensating control) and the first electronic disposal run (POAM-007, 2027-09-30).

**Common controls cut both ways.** CC2.3 and CC7.2 are enterprise gaps, so they appear in both lines. A fix there helps both reports at once, and an exception there would appear in both.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | Both CC2.3, CC7.2; SL-1 CC6.2, C1.2, PI1.1; SL-2 CC7.1, CC8.1, C1.1 | Client notice register (POAM-023); token replay detections (POAM-004); monthly SL-1 access removal check; former SL-1 client deletion run; SL-1 processing objectives; portal patch backlog (POAM-013); change test evidence rule (POAM-009); offshore consent gate and K-1 masking (POAM-008) | Register extract; detection test results; monthly check records; deletion attestations; change records with test evidence; consent gate logs |
| 2027 Q1 | SL-1 PI1.3; SL-2 CC2.3, CC4.1, CC6.1, CC6.2, CC6.3, CC6.7, CC7.5, CC9.1, CC9.2, A1.3 | SL-1 per-client variance thresholds (R-057); SL-2 system description (2027-01-31); client MFA enforcement (POAM-002); seasonal end dates (POAM-006); SL-2 repositories on engagement permissions (POAM-003, SL-2 first by 2027-02-28); retire the legacy endpoint (POAM-016); DR retest (POAM-011); transmitter scenario and drill (POAM-019); overdue vendor reviews (POAM-015) | MFA reports; permission exports; DR retest report; drill records; vendor reviews |
| 2027 Q1 (March) | Readiness check of SL-2 by Internal Audit (CC4.1), including AI-003 and client onboarding; mock walkthrough with the service auditor | Internal Audit test; walkthrough | Test results; walkthrough notes |
| 2027 Q2 and Q3 | SL-2 CC9.1 and C1.2 items still open | Second transmission path decision (POAM-019); first disposal run (POAM-007) | Decision record; disposal log |

**Evidence map.** `soc2-evidence-map.csv` lists 26 evidence items with their source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. 13 items are enterprise common controls marked "Both", collected once and used for both reports; 6 are specific to SL-1 and 7 to SL-2. Status: 16 collecting, 2 ready, 8 not started (each tied to a POA&M item or a dated action above).

**Client communication.** SL-1 clients receive the 2026 report when issued, a bridge letter, and a note that Processing Integrity is added for 2027. SL-2 clients receive this summary, a letter describing the remediation, and the expected first report date (2027-11).

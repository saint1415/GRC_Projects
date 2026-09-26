# SOC 2 Readiness Summary: Cris Santos Company | Finance and Insurance | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (community commercial bank) |
| Tier / Vertical | Small / Finance and Insurance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only, as a self-benchmark |
| Target report | None. The bank is not a service organization and will not seek a SOC 2 report |
| Part A | Security-only self-benchmark against the Trust Services Criteria (`soc2-readiness.csv`) |
| Part B | Review of the core processor's SOC 1 Type 2 and SOC 2 Type 2 reports (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Information Security Officer with the Chief Operating Officer |

## 1. Why SOC 2 for this organization
A community bank is **not** a SOC 2 service organization. It serves depositors and borrowers, not other businesses' systems, and no customer has asked it for a SOC 2 report. Its assurance comes from elsewhere: OCC examinations against the Interagency Guidelines using the FFIEC IT Examination Handbook, the annual independent IT audit, and its external financial statement audit. The vertical overlay lists the alternatives: federal bank examinations and SOC 1 reports from service providers.

SOC reports still matter to the bank in two ways:

**A. Security self-benchmark.** The Trust Services Criteria give a second, outside yardstick for the same program that P03 measured against the Guidelines. The bank used the Security criteria as a cross-check before the next OCC examination. Where both analyses find the same gap (for example, access reviews or monitoring), the finding is stronger. No CPA opinion is sought, and none is implied.

**B. Service provider oversight.** The Guidelines require the bank to oversee its service providers and, where the risk assessment indicates, to monitor them, including by reviewing audits or summaries of test results (12 CFR 30 App. B III.D.3; P03 G-026). The core processor hosts the bank's system of record, so its SOC reports are the main evidence for controls the bank inherits (P02, P04). Until 2026 the reports were collected but never read (gap 4 in the scenario facts).
- The **SOC 1 Type 2** report covers controls relevant to the bank's financial reporting. The bank's external auditor relies on it, and the bank must operate the complementary user entity controls it lists (such as daily balancing).
- The **SOC 2 Type 2** report covers Security, Availability, and Confidentiality. It is the evidence for the bank's III.D.3 oversight and for the availability commitments in the BIA.

The June 2023 interagency third-party guidance says a bank may consider SOC reports in due diligence, and the agencies' September 2026 joint statement calls core providers community banks' highest-risk third parties (P03 section 5). The **proposed** September 2026 replacement guidance is not yet final and is not treated as an obligation here.

## 2. System description (scope)
- **Services:** deposit, lending, payments (wires, ACH, cards), and online and mobile banking for about 16,000 deposit customers.
- **Infrastructure and software:** the Wire and Digital Banking Platform (SSP, P02), the core banking system at the core processor, the cloud tenant (P04), and six branch networks.
- **People:** 120 workforce members, the MSSP, and the outsourced internal audit firm.
- **Data:** customer nonpublic personal information, account and card data, wire instructions, loan files, and SAR information.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 7 | 21 | 5 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

Availability and Confidentiality are outside this benchmark by decision. They are covered by the BIA (P05) and by the Guidelines gap analysis (P03).

**Ready (7):**
- CC1.1: code of ethics acknowledged each year
- CC3.2 and CC3.3: risk analysis done, including fraud risk (BEC, account takeover, insider wire fraud)
- CC4.2: deficiencies tracked and reported to the Audit and Risk Committee
- CC6.4: physical access to the wire room and operations center
- CC6.6: boundary protection
- CC6.8: EDR with 24x7 monitoring

**Not ready (5):**
- CC6.1: customer MFA optional (R-002)
- CC6.3: no quarterly core access reviews, stale accounts, approvers can edit templates
- CC7.1: no vulnerability or configuration monitoring
- CC7.2: payment-system anomalies (beneficiary and limit changes) not monitored
- CC7.5: recovery of bank-managed components unproven (the same gaps as R-004 and R-010)

The pattern matches P03 and P07: governance and preventive controls are mostly in place, but **monitoring and access review are not operating**.

## 4. Findings from the core processor reports (Part B)
- **Opinions:** both Type 2 reports are unmodified, for the 12 months ending 2026-03-31. One exception each (a late access removal at the processor; two changes without documented approval). Both were remediated by the processor.
- **Availability:** the stated RTO of 4 hours and RPO of 15 minutes **meet the BIA** (RTO 4 h and RPO 1 h for branch services and loan servicing). The commitment is in the system description, not the contract, so it goes into the 2027 renewal (R-003).
- **Controls the bank must run (CUECs):** six were mapped. Four are open gaps at the bank: core user reviews (POAM-001), review of user activity and exception reports (POAM-004), keeping authorized contacts current, including the 12 CFR 53.4 contacts (POAM-009), and approval of parameter changes (POAM-014). **The processor's access controls only protect the bank once the bank's own core user reviews operate.**
- **Incident notice:** the processor promises notice "without undue delay" with no time frame. 12 CFR 53.4 requires the processor to notify the bank as soon as possible of incidents that disrupt covered services for four or more hours. The bank will send designated contacts by 2026-09-30 and seek a stated notice time.
- **Follow-ups:** the bridge letter to 2026-06-30 was received; ask for the processor's review of the carved-out colocation provider; review the digital banking provider and payments service provider reports by 2026-11-30.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.2, CC3.1, CC2.2, CC2.3, CC6.2, CC6.3, CC7.1, CC7.2 | Board-approved risk appetite, policy acknowledgments, 53.4 contact letters, termination tickets, quarterly access reviews, scan reports, daily beneficiary change reports |
| 2027 Q1 | CC6.1, CC7.3, CC7.4, CC7.5, CC8.1, CC9.2 | Customer MFA enrollment reports, MSSP after-hours tickets, tabletop report, restore test records, change records, provider SOC reviews |
| 2027 Q2 | CC1.3, CC5.2, CC6.7, CC9.1 | ISO reporting line change, configuration baselines, secure portal logs, Branch 4 relocation exercise |

**Use of this summary:** attach it, the readiness checklist, and the POA&M (P07) to the annual information security report to the board (III.F) and to the examination request package for the next OCC examination. Update the self-benchmark in August 2027.

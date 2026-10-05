# SOC 2 Readiness Self-Check: Cris Santos Company | Transportation Systems | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight broker arranging truck and rail shipments) |
| Tier / Vertical | Sole Proprietorship / Transportation Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the TMS vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-17 (Part B) and 2026-08-19 (Part A) by the owner with the IT consultant; adopted 2026-09-08 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person brokerage would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for customers who rely on its systems. Shippers rely on the broker to move freight, not to run their systems, and the cost of a CPA examination would be out of proportion to about $180,000 of annual margin. What the business does face is a **yearly security questionnaire** from its largest shipper under the master broker-shipper agreement (P03 G-032). This checklist is the evidence behind those answers.

The Security criteria are useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Some criteria assume a board, staff, or a development team, so they are marked N/A or are met by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the TMS vendor's SOC 2 report.** The TMS vendor operates most of the inherited controls (P02, P04). The owner uses the same CC criteria as a checklist when reading the vendor's report every year (POL-01 6.1).

## 2. Scope
- **Services:** truck brokerage and rail carload coordination for 14 shippers.
- **System:** the Freight Brokerage SaaS Stack (P02).
- **People:** the owner; the bookkeeper and IT consultant under their engagement terms.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 16 | 3 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; the vendor's change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**A strength for a broker:** CC3.3 (fraud risk) is Ready. Payment diversion, carrier impersonation, and fake invoices are in the risk register, which is where a broker's losses actually come from.
**Not ready:** CC6.1 (MFA off on the TMS, accounting, and load board; a forgotten contractor admin account), CC7.2 (no monitoring of TMS, email, or bank activity), and CC9.2 (no vendor list; carrier vetting without an identity check). All three map to open POA&M items in P07 or to POL-01 rules adopted on 2026-09-08.

## 4. TMS vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, period ending 2026-03-31. One exception (late quarterly access reviews at the vendor), remediated.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 24 hours **do not meet the BIA for in-transit tracking** (BP-02: RTO 4 h, RPO 4 h). The owner compensates with a twice-daily in-transit list and a quarterly export (POAM-004).
- **Controls the business must run (CUECs):** turn on MFA, review users, review audit logs, protect credentials, and report suspected compromise. MFA was off (POAM-002) and logs had never been reviewed, so **the vendor's controls protect the business only once the owner runs these.**
- **Not covered:** the document capture feature (AI-001) was released after the report period. P10 assesses it directly.
- **Follow-ups:** bridge letter by 2026-10-31; ask for breach notice within 10 days (Fla. Stat. 501.171(6)); confirm the training opt-out made on 2026-08-18.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC5.2, CC6.1, CC6.2 | MFA screenshots for every service; account list |
| By 2026-10-31 | CC2.1, CC3.4, CC6.3, CC6.7, CC7.2, CC7.3, CC7.4 | Monthly review log; individual railroad user ID; sharing default; walkthrough notes |
| By 2026-11-30 | CC1.4, CC2.3 | Course certificate; 2026 shipper questionnaire answers |
| By 2026-12-31 | CC6.5, CC6.6, CC7.5, CC9.1, CC9.2 | Disposal record; network change; export log; backup broker agreement; vendor list |
| By 2027-08-31 | CC4.1, CC7.1 | Outside review; settings review with the 2027 assessment |

**Answer to the shipper:** the owner answers the 2026 questionnaire from this checklist and the POA&M, stating plainly which items are open and their dates, and updates the answers each August.

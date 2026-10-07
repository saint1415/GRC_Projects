# SOC 2 Readiness Self-Check: Cris Santos Company | Retail Trade | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (corner grocery with online and phone ordering) |
| Tier / Vertical | Sole Proprietorship / Retail Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the website builder's SOC 2 Type 2 report and the processor's PCI DSS attestation of compliance (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-12 (Part B) and 2026-08-14 (Part A) by the owner with the outside IT helper; adopted 2026-09-04 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A corner grocery would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for its business customers. This store sells groceries to neighbors, has no business customers relying on its systems, and could not justify a CPA examination. **Its assurance mechanism is PCI DSS validation**: the two SAQs the processor's portal asks for each year (P03).

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions that covers ground the SAQs do not, such as risk assessment, fraud, and business disruption. Many criteria assume a board, staff, or a development team, so they are marked N/A or are satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the providers' reports.** The website builder runs the online store platform and the processor runs card processing. The owner uses the CC criteria and the PCI customer responsibilities as a checklist when reading the website builder's SOC 2 report and the processor's AOC every August (POL-01 6.3).

## 2. Scope
- **Services:** retail grocery sales in store, online, and by phone; no services to other businesses.
- **System:** the Store Sales Platform (P02).
- **People:** the owner and the family member at the register; providers under their terms.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 17 | 5 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC8.1 (no software development or infrastructure; the owner's setting changes go in the change log).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year. CC3.1, CC3.2, CC5.1, CC5.3, and CC6.8 are ready on the evidence of P01, P02, POL-01, and the P07 antivirus test.
**Not ready:** CC6.1 (no MFA on the online store and email; flat network), CC6.5 (paper card data in the trash), CC6.7 (card data on paper and customer data in a consumer AI chatbot), CC7.2 (no activity review), and CC9.2 (no provider list or ongoing check). All five map to open POA&M items in P07.

## 4. Provider reports (Part B)
- **Website builder SOC 2 Type 2:** Security and Availability, 12 months ending 2026-03-31, unqualified opinion, no exceptions. Recovery objectives meet the BIA for online orders (BP-02). **Customer responsibilities** include turning on MFA, reviewing administrator access, and controlling third-party apps and custom code. Those are exactly the store's gaps (POAM-001, POL-01 7.4 and 7.7): **the platform is secure, but the store's account on it is not yet.**
- **Processor PCI DSS AOC:** dated 2026-02, compliant, covering card-present processing and the hosted payment page. It covers the processor, not the store. The store still owns terminal inspection, no stored card data, a separated network, and its own SAQs.
- **Gaps in provider assurance:** the POS app vendor's security documentation has never been requested (POAM-007); the website builder bridge letter is due 2026-10-31.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1 (MFA part), CC6.2, CC6.4, CC6.5, CC7.1, CC2.3, CC7.3, CC7.4 | MFA screenshots; POS user list; terminal record and inspection log; shredder in use; walkthrough notes |
| By 2026-10-31 | CC1.4, CC2.1, CC2.2, CC6.7, CC7.2, CC9.2 | Course certificate; signed acknowledgment; monthly check log; provider list; P10 decision |
| By 2026-11-30 | CC4.1 | Both SAQs with evidence |
| By 2026-12-31 | CC3.4, CC5.2, CC6.1 (network part), CC6.3, CC6.6, CC7.5, CC9.1 | Terminal network retest; quarterly review record; file plan; sealed envelope and open-and-close sheet |
| By 2027-08-31 | CC3.3 | Updated risk register with fraud scenarios |

**What customers and the processor see:** the completed SAQs, not this checklist. This self-check is kept with the SAQ evidence and updated each August.

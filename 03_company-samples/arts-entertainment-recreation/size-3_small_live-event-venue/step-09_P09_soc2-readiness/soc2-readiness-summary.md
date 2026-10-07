# SOC 2 Readiness Summary: Cris Santos Company | Arts, Entertainment, and Recreation | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing) |
| Tier / Vertical | Small / Arts, Entertainment, and Recreation |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only, as an internal benchmark |
| Part A | Security-only readiness self-assessment (`soc2-readiness.csv`) |
| Part B | Review of the ticketing vendor's SOC 2 Type 2 report and PCI DSS service provider AOC (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-21 by the IT Manager with the Controller |

## 1. Why SOC 2, and why only as a benchmark
**The company is not a SOC 2 service organization.** It sells tickets and experiences to the public. It does not run systems that other businesses rely on for their own control objectives, and no customer, artist, or promoter has asked for a SOC 2 report. Touring promoters rely on the company's settlement sheets, but they check those against their own ticket counts; nobody has asked for an assurance report on them.

**Its real assurance mechanism is PCI DSS validation** (the vertical's assurance alternative): an annual SAQ and AOC for each merchant account, plus ASV scans, submitted to the acquirer (P03). A CPA-issued SOC 2 report would cost more than the company's whole 2026 security budget and answer a question nobody is asking.

SOC 2 still earns its place here in two ways:

**A. Internal benchmark.** The Security category (the Common Criteria) is a well-known yardstick that covers governance and operations PCI DSS does not stress, such as board oversight, fraud risk, and change risk. The company scored itself against the 33 Security criteria to show the owner where the program stands. The other categories are marked not in scope: availability is covered by the BIA (P05) and patron privacy by the FTC Act analysis (P03).

**B. Third-party risk management.** The ticketing vendor holds the company's most sensitive data and hosts its checkout. Its SOC 2 Type 2 report and PCI DSS AOC are the evidence for the controls the company inherits (P02, P04). The company reviews both every year (PCI DSS 12.8; SA-9).

## 2. System description (scope)
- **Services:** ticket sales (online, box office, phone), event entry, show settlement, and patron communications.
- **Infrastructure and software:** the Ticketing and Venue Operations Platform (SSP, P02).
- **People:** 60 employees, the marketing agency, the network and security integrator, and event-day workers.
- **Data:** patron records, card data in the box office channel, settlement data.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 18 | 11 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles and owners are designated
- CC3.1 and CC3.2: objectives are stated and the risk assessment is done
- CC4.2: deficiencies are tracked in the POA&M

**Not ready:**
- CC2.1 and CC7.2: no security information is collected or monitored
- CC2.3: the privacy notice contradicts practice, and vendors have no breach notice terms
- CC3.4: dynamic pricing went live with no change risk review
- CC6.1, CC6.3, and CC6.8: no MFA on the ticketing platform, excess and stale access, and unmanaged checkout scripts
- CC7.1, CC7.3, CC7.5, and CC8.1: no scanning, no event triage, unproven recovery, no change control

The Not ready criteria map almost one to one to the High risks in P01 and the High POA&M items in P07. **The benchmark tells the same story as the PCI DSS analysis from a different angle: the company's weak point is how it runs its own accounts and changes on the vendor platform.**

## 4. Findings from the ticketing vendor's reports (Part B)
- **Opinion and period:** SOC 2 Type 2, unqualified, 12 months ending 2026-03-31. PCI DSS service provider AOC dated 2026-02-20, Compliant.
- **One exception:** 2 of 40 sampled production changes lacked documented approval. The vendor has since blocked unapproved changes in its tooling. Accepted, to be watched in the next report.
- **Availability:** RTO 4 hours and RPO 15 minutes meet the BIA for box office and online sales (P05 BP-04, BP-05). Event entry (BP-01) cannot wait 4 hours, so the manual entry procedure remains the real control.
- **Controls the company must run.** The report lists six controls the customer must operate for the vendor's controls to work. **Four are open gaps at the company:** MFA for its users (POAM-003), protecting API credentials (POAM-005), reviewing its audit log (POAM-011), and approving content added through marketing settings (POAM-007). This is the single most important finding of Part B: the vendor's clean report does not protect the company until those four close.
- **Carve-outs:** the payment partner is carved out. The company holds only the partner's 2024 AOC. A current AOC is needed before the 2026 SAQs (POAM-019).
- **Follow-ups:**
  - Bridge letter to 2026-09-30.
  - Written statement on checkout script protection for SAQ A eligibility (PCI SSC FAQ 1588).
  - Alerts to the company on any marketing or checkout setting change.
  - A 72-hour incident notice term in the contract at renewal. Florida law already requires a third-party agent to notify within 10 days of determining a breach (Fla. Stat. 501.171(6)(a)).

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC6.1, CC6.3, CC6.8 | MFA enforcement report, account cleanup record, checkout captures showing no company-added scripts |
| 2026 Q4 | CC2.1, CC2.2, CC2.3, CC7.1, CC7.2, CC7.3, CC7.4, CC8.1, CC9.2 | Log alerts and weekly reviews, ASV reports, change log, tabletop report, provider list and AOCs, policy acknowledgments |
| 2027 Q1 | CC3.3, CC3.4, CC7.5, CC1.2 | Fraud risk review, P10 reviews for new features, restore tests, owner review minutes |

**Next step:** repeat this benchmark in August 2027 alongside the annual risk assessment. Revisit a formal SOC 2 only if a customer (for example a promoter that outsources its ticketing to the company) asks for one.

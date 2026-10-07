# SOC 2 Readiness Summary: Cris Santos Company | Arts, Entertainment, and Recreation | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing; one music club) |
| Tier / Vertical | Micro / Arts, Entertainment, and Recreation |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Readiness self-assessment (`soc2-readiness.csv`), used to answer a corporate rental client's security questionnaire |
| Part B | Review of the ticketing vendor's SOC 2 Type 2 report and PCI DSS service provider AOC (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-21 by the Venue Manager with the Box Office and Ticketing Manager; approved by the Owner and General Manager 2026-08-31 |

## 1. Why SOC 2 for this organization
**The company is not a SOC 2 service organization.** It sells tickets and nights out to the public. No artist, promoter, or client relies on its systems for their own control objectives in a way that calls for a CPA's report. **Its real assurance mechanism is PCI DSS validation** (the vertical's assurance alternative): an SAQ and AOC for each merchant account, plus ASV scans of the website, submitted to the acquirer by 2026-12-15 (P03).

The Trust Services Criteria are still useful here for two practical reasons.

**A. Answering a client questionnaire.** A regional employer has booked the room for its annual employee event and a product reveal in November 2026. It will send an attendee list (about 550 names, work emails, and dietary and accessibility notes) for check-in and wristbands, and the event details are confidential until the reveal. On 2026-07-28 its procurement team sent a vendor security questionnaire organized by the Trust Services Criteria, asking about **Security and Confidentiality**. The response is due 2026-09-30. The client accepts a self-assessment with a named security contact; it did not ask for a SOC 2 report.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. The cost would also exceed the company's whole 2026 security budget.

**B. Relying on the ticketing vendor.** The ticketing vendor holds the company's patron data and serves the checkout widget. Its SOC 2 Type 2 report and PCI DSS AOC are the evidence for the controls the company inherits (P02, P04). Reviewing both every year is part of service provider oversight (PCI DSS 12.8; SA-9).

**Why Confidentiality and not another category.** The client's question is whether its attendee list and event details stay confidential. Availability of the club is covered by the BIA (P05), and patron privacy by the FTC Act analysis (P03). Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** ticketed shows and private and corporate room rentals, including guest lists and check-in for corporate events.
- **Infrastructure and software:** the Ticketing and Venue Operations Platform (SSP, P02): ticketing platform, door tablets and readers, productivity suite, website, venue network, office computers, and the suite backup.
- **People:** 7 employees, the MSP, the web designer, and contractor door staff who check guests in.
- **Data:** patron records, client attendee lists and event details, settlement data. Card data stays in the vendor's widget and the P2PE readers once the P03 Option B changes are complete.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 15 | 13 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security and Privacy Lead designated; roles defined
- CC3.1 and CC3.2: objectives set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked

**Not ready:**
- CC1.4: no training; contractor leads never briefed on card readers
- CC2.1: no inventory and no log information used
- CC2.3: the privacy notice contradicts practice; vendors have no breach notice terms
- CC3.4: the demand tools and website scripts went live with no change review
- CC6.1, CC6.2, and CC6.3: no MFA on ticketing or the website, shared logins, and a stale account
- CC6.7: card numbers by phone and email; exports to laptops; an old integration sending patron records
- CC7.1, CC7.2, CC7.3, CC7.5, and CC8.1: no scanning, monitoring, triage, tested recovery, or change control
- C1.2: client lists are never deleted after events

**For the client's question specifically:** client attendee lists arrive today in the shared info mailbox, which has a shared password and no MFA (C1.1), and 2025 client lists are still there (C1.2). Both are fixed before the November event: lists go to a restricted folder reached only by named accounts with MFA, and are deleted 30 days after the event.

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3, C1.1 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Ticketing vendor SOC 2 and AOC review | CC9.2 | Yes | Bridge letter (2026-10) |
| Suite MFA report; ticketing MFA enforcement screenshot | CC6.1 | Suite only | Ticketing and website MFA (2026-09) |
| Monthly account check records | CC6.2, CC6.3 | No | Monthly from 2026-10 |
| Weekly log check records | CC7.2 | No | Weekly from 2026-10 |
| Restore test record | CC7.5 | No | Quarterly from 2026-09 |
| Client list deletion record | C1.2 | No | After each corporate event, from 2026-11 |
| Training and briefing records | CC1.4, CC2.2 | No | From 2026-09 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the ticketing vendor's reports (Part B)
- **Opinion and period:** SOC 2 Type 2, unqualified, 12 months ending 2026-03-31 (Security, Availability, Confidentiality). PCI DSS service provider AOC dated 2026-03-12, Compliant.
- **One exception:** 3 of 40 sampled access removals for vendor staff were late. Remediated with automation. Accepted, to be watched in the next report.
- **Availability:** RTO 4 hours and RPO 15 minutes meet the BIA for online and door sales (P05 BP-04, BP-05). Event entry (BP-01) cannot wait 4 hours, so the manual door procedure remains the real control.
- **Controls the company must run.** The report lists six complementary user entity controls. **Five are open gaps at the company:** MFA (POAM-003), user management (POAM-001), API credentials (POAM-012), audit log review (POAM-006), and protecting the pages where it embeds the widget (POAM-008). This is the most important finding of Part B: the vendor's clean report does not protect the company until those five close.
- **Carve-outs:** the payment partner is carved out, and the company has never held its AOC. A current AOC is needed before the 2026 SAQs (POAM-012).
- **Follow-ups:** a bridge letter to 2026-09-30; a written statement on widget script protection for SAQ A and the vendor's guidance for pages that embed it (PCI SSC FAQ 1588); a 72-hour incident notice term at renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC6.1, CC6.2, CC6.7, CC7.3, C1.1 | Acknowledgments; MFA and named logins (POAM-001, POAM-003); Option B (P03); incident log; client list folder; questionnaire response |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.2, CC2.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.3, CC6.4, CC6.5, CC6.6, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, C1.2 | Monthly oversight notes; training (POAM-005); inventory (POAM-007); log checks (POAM-006); privacy notice; change control; key list; disposal rules (POAM-013); crew Wi-Fi (POAM-009); EDR; ASV scans; tabletop; restore tests (POAM-010); door drill; provider list and contract terms (POAM-012); client list deletion |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk assessment |

**Response to the client:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Venue Manager as security contact, and confirm in writing how the attendee list will be received, stored, and deleted. Repeat the self-assessment in August 2027 with the annual risk assessment.

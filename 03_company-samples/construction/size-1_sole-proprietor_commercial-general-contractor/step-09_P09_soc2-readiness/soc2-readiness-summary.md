# SOC 2 Readiness Self-Check: Cris Santos Company | Construction | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (commercial and institutional building general contractor) |
| Tier / Vertical | Sole Proprietorship / Construction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the project management SaaS vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-16 (Part B) and 2026-07-22 (Part A) by the owner with the IT technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person general contractor would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. The company builds and renovates buildings; clients do not rely on its IT systems to run their own operations, and a CPA examination would cost more than a year of the owner's profit.

**What clients and agencies actually ask for instead:**
- **Federal work:** compliance with FAR 52.204-21 and 52.204-25, already in FC-1, and for the DoD subcontract a current CMMC Level 1 (Self) status with an affirmation in SPRS (32 CFR 170.15(b)). **CMMC is the assurance that matters for this company** (P03).
- **Private clients and prime contractors:** occasional questionnaires about how the company protects drawings and, more and more, how it prevents payment fraud. A one-page self-attestation built from this check answers them.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a complete list of questions. Many criteria assume a board, staff, or a development team, so they are marked N/A or are met by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the project management vendor's SOC 2 report.** That vendor runs most of the inherited controls around FCI and drawings (P02, P04). The owner uses the same CC criteria as a checklist when reading its report each year (POL-01 6.3).

## 2. Scope
- **Services:** small commercial renovations and build-outs, billing, and subcontractor payment.
- **System:** the Project Management and Payment Application System (P02).
- **People:** the owner; the outside bookkeeper and IT technician under their engagement letters.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 15 | 5 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; the vendor's change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside reader before each CMMC self-assessment.
**Not ready:**
- CC2.3: clients and subcontractors have no reliable way to confirm a payment change
- CC6.1: passwords only on the project management and accounting SaaS; shared accounting password
- CC6.5: no device wipe or disposal records
- CC6.7: FCI on external systems; bank details accepted by email
- CC7.2: no monitoring of sign-ins or mailbox rules

Four of the five are the same weaknesses behind business email compromise (P01 R-001, R-002). Most also match FAR 52.204-21 gaps in P03, so one plan (the P07 POA&M) serves SOC 2, FAR, and CMMC.

## 4. Vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, 12 months ending 2026-03-31. No exceptions. Bridge letter through 2026-06-30.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the BIA** for project document control (BP-03: RTO 8 h, RPO 4 h).
- **Controls the company must run (CUECs):** turn on MFA, remove users, set permissions, review activity, and keep exports. **Most are open gaps today** (POAM-001, POAM-002, POAM-006, stale users, broad default role). The vendor's controls protect the company's drawings only once the owner runs these.
- **No FedRAMP claim:** irrelevant while the company accepts no CUI.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC2.3, CC6.2, CC6.3, CC6.5, CC6.6, CC6.7, CC7.1, CC7.3, CC7.4 | Contract and pay app notice; user lists; disposal log; router settings; walkthrough notes |
| By 2026-10-31 | CC2.1, CC5.2, CC6.1, CC6.4, CC7.2, CC7.5, CC9.2 | MFA screenshots; monthly check log; backup settings; signed subcontract riders |
| By 2026-12-31 | CC1.4 (training by 2026-11-30), CC3.4 and CC4.1 (by 2026-11-30, with the CMMC self-assessment), CC9.1 | Course certificate; self-assessment and outside reader notes; standby agreement |

**Self-attestation for clients and prime contractors:** a one-page letter from the owner that summarizes this check, the CMMC status once achieved, and the call-back rule for payments, updated each July.

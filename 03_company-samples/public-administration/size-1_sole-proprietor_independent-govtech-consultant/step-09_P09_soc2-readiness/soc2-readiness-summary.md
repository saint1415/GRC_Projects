# SOC 2 Readiness Self-Check: Cris Santos Company | Public Administration | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent GovTech consultant) |
| Tier / Vertical | Sole Proprietorship / Public Administration |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the productivity suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`), because that service holds agency files |
| Prepared | 2026-08-13 (Part B) and 2026-08-26 (Part A) by the owner-consultant with the IT technician; adopted 2026-09-15 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**The owner is a service provider, but runs no system for clients.** SOC 2 reports on a service organization's controls over a system its customers rely on. The agencies rely on their own case management systems, not on a system the owner operates, so none of the three asks for a SOC 2 report, and a CPA examination would cost a large share of a year's receipts. What the agencies ask for instead:
- **County:** an annual contractor security attestation under the contract's SP 800-53 Moderate clause, which P02, P03, and P07 now answer.
- **Sheriff:** the CJIS Security Addendum certification, fingerprint-based checks, CJIS training, and cooperation with CJIS audits.
- **City:** confidentiality terms and prompt notice.
- **Prime contractors:** a short security questionnaire with each subcontract.

GovRAMP (formerly StateRAMP) is not relevant: it verifies cloud service providers, and the owner offers no cloud service (P03 section 1.4).

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Some criteria assume a board or staff, so they are marked N/A or are met through the owner's direct oversight, with the reason written in the checklist. The answers feed the county attestation and the prime contractor questionnaires.
- **B. Reading the productivity suite provider's SOC 2 report.** That provider holds agency files in the sync folder. The owner uses the same CC criteria as a checklist when reading its report every year (POL-01 6.3).

## 2. Scope
- **Services:** configuration, reporting, and data migration for three Florida agencies, plus documentation subcontracts.
- **System:** the Consulting Delivery Environment (P02).
- **People:** the owner-consultant; the on-call IT technician under NDA.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 16 | 5 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC2.2 (no internal workforce). The non-Security categories are out of scope at this tier; each row in the checklist says why.
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies; the agencies' contracts add outside accountability. The limit is independence, which POL-01 4.5 addresses with an outside review every second year.
**Not ready:**
- CC6.1: daily administrator account, password-only sign-ins on the laptop administrator account and the website builder, unencrypted USB drive (POAM-001, POAM-002, POAM-004, POAM-010)
- CC6.5: county extracts kept past the contract deletion date (POAM-005)
- CC6.7: CJI left the sheriff's virtual desktop, and city applications went to an AI assistant (POAM-003, POAM-008)
- CC7.2: no review of sign-ins, sharing, or alerts (P03 G-027)
- CC9.2: no provider other than the productivity suite was reviewed (POAM-008)

## 4. Productivity suite provider report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, period ending 2026-03-31. No exceptions reported.
- **Recovery:** version history and the recycle bin meet the BIA for synced files (P05 BP-02: RTO 24 h, RPO 8 h). They do not cover the scripts repository, which needs its own backup (POAM-006).
- **Controls the owner must run (CUECs):** turn on MFA, manage users and sharing, review audit logs, and protect the endpoints that sync data. MFA is on and the laptop is encrypted; log review and sharing link expiry are open gaps, so **the provider's logging protects agency files only once the owner reviews it.**
- **Follow-ups:** bridge letter by 2026-10-31; ask which U.S. regions hold the tenant's data.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC5.2, CC6.3, CC6.4, CC6.5 | Standard account screenshot; encrypted drive status; county deletion certificate |
| By 2026-10-31 | CC2.1, CC2.3, CC3.4, CC6.1, CC6.2, CC6.6, CC7.1, CC7.2, CC7.3, CC7.4, CC7.5, CC8.1, CC9.2 | MFA screenshots; city confirmation; monthly review log; walkthrough notes; restore test record; provider list |
| By 2026-11-30 | CC1.4, CC6.7 | CJIS refresher certificate (due 2026-09-24) and course certificate; first quarterly data location search |
| By 2026-12-31 | CC9.1 | Contact sheet with the attorney; peer backup agreement |
| By 2027-08-31 | CC4.1 | Outside review of the 2027 self-assessment |

**Self-attestation for agencies and primes:** a one-page letter from the owner that summarizes this check, the P07 results, and the POA&M, attached to the county's annual attestation and to prime contractor questionnaires, updated each August.

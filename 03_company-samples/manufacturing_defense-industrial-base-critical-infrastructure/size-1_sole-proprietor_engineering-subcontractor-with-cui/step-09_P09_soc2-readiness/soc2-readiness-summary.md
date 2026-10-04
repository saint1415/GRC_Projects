# SOC 2 Readiness Self-Check: Cris Santos Company | Defense Industrial Base | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (engineering subcontractor handling CUI drawings) |
| Tier / Vertical | Sole Proprietorship / Defense Industrial Base |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the planned government-community cloud suite's assurance evidence (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 (Part B) and 2026-08-26 (Part A) by the owner, with the CMMC consultant's comments; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person engineering firm would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. The owner's customers rely on engineering work, not on the owner's systems, and a CPA examination would cost more than a month of revenue. For defense work the assurance that counts is **CMMC**: a Level 2 (Self) assessment posted in SPRS with an affirmation (P03). A commercial customer sent a security questionnaire in July 2026, and the owner answers it with a short self-attestation that this checklist supports.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions that cross-checks the SP 800-171 work. Criteria that assume a board, staff, or software development are marked N/A or are satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Choosing the CUI cloud.** The owner uses the CC series, plus the FedRAMP and DFARS items, as a checklist for the planned SYS-10 provider's evidence before moving CUI there (POL-01 6.1).

## 2. Scope
- **Services:** engineering design and analysis; no services that customers run on the owner's systems.
- **System:** the Engineering Office Systems (P02).
- **People:** the owner; IT and CMMC consultants as outside help.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 13 | 7 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with the CMMC consultant's outside review.
**Not ready:** CC2.3 (cannot report to DoD), CC6.1 (passwords in a spreadsheet; CUI in a non-FedRAMP cloud), CC6.3 (daily administrator use), CC6.4 (home office access and visitors), CC6.7 (CUI by email to a commercial suite; unencrypted backup), CC7.2 (no monitoring), and CC9.2 (non-compliant provider holds CUI). All seven map to open POA&M items in P07.

**Crosswalk to CMMC.** Every Not ready criterion matches an SP 800-171 requirement that is Not met or Partially met in P03, so one remediation plan (the P07 POA&M) serves both. The self-attestation to the commercial customer will state the recalculated SPRS score and the POA&M dates, not a claim of compliance (POL-01 4.7).

## 4. Planned CUI cloud evidence (Part B)
- **Authorization:** the SYS-10 offering is listed on the FedRAMP Marketplace as authorized at the High baseline, which satisfies the Moderate-or-higher test in 32 CFR 170.16(c)(2)(i) and the DFARS cloud requirement.
- **Incident duties:** the provider's service terms commit to DFARS 252.204-7012(c) to (g).
- **CRM:** a summary was provided; the full matrix comes at onboarding and will be referenced in the SSP.
- **SOC 2 Type 2:** Security and Availability, period ending 2026-06-30, unqualified. Its availability commitments meet the BIA.
- **Controls the owner must run (CUECs):** MFA and access policies, user management, log review, and reporting suspected compromise. Log review is an open gap (POAM-008), so **the provider's logging protects the owner only once the owner reviews it.**
- **Follow-ups:** confirm FIPS module certificate numbers for the SSP; keep any generative AI add-on turned off until P10 conditions are met.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.2, CC6.3, CC6.4 | Account check record; standard account screenshot; visitor log; cabinet and key record |
| By 2026-10-31 | CC1.4, CC2.3, CC6.5, CC6.6, CC7.1 | Training certificates; certificate and DIBNet access; sanitization records; business network diagram; first scan report |
| By 2026-11-30 | CC2.1, CC3.4, CC5.2, CC6.1, CC6.7, CC7.2, CC7.3, CC7.4, CC9.2 | SYS-10 go-live record and CRM reference; monthly review log; tabletop notes |
| By 2027-01-15 | CC4.1, CC7.5, CC9.1 | Full self-assessment with consultant review; restore test record; continuity arrangement with Prime A |

**Self-attestation for commercial customers:** a one-page letter from the owner that summarizes this check, the SPRS score, and the POA&M, updated after each self-assessment.

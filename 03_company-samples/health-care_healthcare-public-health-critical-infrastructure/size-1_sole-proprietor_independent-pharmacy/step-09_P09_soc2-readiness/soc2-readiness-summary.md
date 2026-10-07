# SOC 2 Readiness Self-Check: Cris Santos Company | Healthcare and Public Health | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent community pharmacy) |
| Tier / Vertical | Sole Proprietorship / Healthcare and Public Health |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs and short topic labels only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the PMS vendor's SOC 2 Type 2 report and EPCS certification report (`vendor-soc2-review.csv`, an extra file added for this tier) |
| Prepared | 2026-08-05 (Part B) and 2026-08-07 (Part A) by the pharmacist-owner with the IT consultant; adopted 2026-09-04 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person pharmacy would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for its business customers. This pharmacy dispenses to patients, has no business customers relying on its systems, and could not justify the cost of a CPA examination. PBMs that audit network pharmacies and prescriber offices that ask about security accept a **self-attestation**, which this checklist supports.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Some criteria assume a board or a development team, so they are marked N/A or are met by the owner's direct oversight, with the reason written in the checklist. Unlike a solo practice with no staff, this pharmacy has one workforce member (the relief pharmacist), so the communication and accountability criteria do apply.
- **B. Reading the PMS vendor's reports.** The PMS vendor operates most of the pharmacy's inherited controls (P02, P04). The owner uses the CC criteria as a checklist when reading the vendor's SOC 2 report every year (POL-01 6.3; 45 CFR 164.308(b)). For this vendor the SOC 2 report is not enough: the DEA EPCS rule also requires a third-party audit or certification of the pharmacy application (21 CFR 1311.300), and the pharmacy must check its finding (1311.200(a)). Part B covers both.

## 2. Scope
- **Services:** community pharmacy dispensing and non-sterile compounding for about 650 active patients; no services to other businesses.
- **System:** the Pharmacy Core SaaS Stack (P02).
- **People:** the pharmacist-owner and the relief pharmacist; contracted services under BAAs.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 19 | 3 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC8.1 (no software development or infrastructure; the vendor's change management and the EPCS recertification rule cover application changes).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, and CC4.2. One person sets the tone, holds every role, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (shared account, no MFA for the administrator in the store, unencrypted desktop with the CSOS key), CC6.2 (the relief pharmacist was never registered as a user), and CC7.2 (no monitoring; the daily EPCS audit report was never read). All three map to open POA&M items in P07 (POAM-001, POAM-002, POAM-003, POAM-005).

## 4. PMS vendor reports (Part B)
- **SOC 2 opinion:** Type 2, unqualified, Security and Availability, period 2025-04-01 to 2026-03-31. One exception (late removal of departed vendor staff access), remediated.
- **Availability:** the vendor's stated RPO of 1 hour **meets** the BIA; its RTO of 12 hours **does not meet** the BIA's 4 hours for dispensing (BP-01). The pharmacy bridges the gap with the paper downtime kit (P05, P08).
- **EPCS certification:** issued 2025-11-14 by a DEA-approved certification organization; finds the application compliant with no limitation. It satisfies the pharmacy's check under 21 CFR 1311.200(a), although the check was made five years after first use. Next report due by 2027-11-14.
- **Controls the pharmacy must run (CUECs):** assign roles and remove users, never share credentials, protect MFA devices, review audit and EPCS reports, control remote-support sessions, report suspected compromise. Four of these were not done (POAM-002, POAM-003, POAM-004, POAM-005), so **the vendor's audit trail and role controls protect the pharmacy only once the pharmacy uses them.**
- **Follow-ups:** bridge letter by 2026-10-31; ask how the vendor monitors the carved-out e-prescribing network and claims switch; ask for same-day notice of any outage-causing security incident.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC1.5, CC2.1, CC2.2, CC2.3, CC5.2, CC6.1, CC6.2, CC6.7, CC7.2, CC7.3, CC7.4, CC9.2 | Own accounts and MFA screenshots; encryption status; accepted BAA; review log; printed contacts; walkthrough notes; signed contract clause |
| By 2026-10-31 | CC3.4, CC6.6, CC7.5 | Network scan after the split; downtime kit checklist; transfer arrangement |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC6.3, CC6.5, CC9.1 | Course certificates; quarterly user review; disposal certificate; sealed envelope receipt |
| By 2027-08-31 | CC3.3, CC4.1, CC7.1 | Updated risk register; outside review notes; settings review |

**Self-attestation for PBMs and prescriber offices:** a one-page letter from the owner that summarizes this check and the POA&M, updated each August.

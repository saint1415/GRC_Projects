# SOC 2 Readiness Self-Check: Cris Santos Company | Manufacturing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated CNC machine shop) |
| Tier / Vertical | Sole Proprietorship / Manufacturing (NAICS 332710) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the productivity suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-13 (Part B) and 2026-08-14 (Part A) by the owner-machinist with the IT technician; adopted 2026-09-04 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person machine shop would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls over systems its customers rely on. The shop's customers buy parts, not access to the shop's systems, and the cost of a CPA examination would be a large share of a year's receipts. The manufacturing vertical has no sector assurance alternative. What customers actually ask for is:
- **OEM supplier security questionnaires** (during supplier audits and re-approval), which this checklist answers;
- **CMMC Level 1 (Self) status in SPRS** for the aerospace work, which is the only assurance that customer is contractually required to collect (P03).

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. A few criteria assume a board or staff and are marked N/A or met by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the productivity suite provider's SOC 2 report.** That service holds the drawings and programs, including FCI. The owner uses the CC criteria as a checklist when reading the report every year (POL-01 6.4).

## 2. Scope
- **Services:** machined parts to customer drawings for about 12 business customers.
- **System:** the Shop Business Systems (P02).
- **People:** the owner-machinist; contracted services under NDA or contract.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 16 | 5 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC2.2 (no internal workforce).
**Not N/A, on purpose:** CC8.1 (change management). The shop writes no software, but released CNC programs are the shop's production "software", and a changed program can ship a bad OEM part. It is Partially ready (POAM-003).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, signs the CMMC affirmation, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (flat network and open VMC share; accounting without MFA), CC6.5 (no media sanitization), CC6.7 (drawings moving through open links, email to a processor, and an AI assistant), CC7.2 (no monitoring), and CC7.5 (no backup the laptop cannot overwrite; no program verification). All five map to open POA&M items in P07.

## 4. Productivity suite provider report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, period ending 2026-03-31. No exceptions.
- **Retention vs the BIA:** 30-day versions meet the BIA for failures on the provider's side, **but not for ransomware on the laptop**, which would sync encrypted files into the service. The shop's own backup is still required (POAM-002).
- **Controls the shop must run (CUECs):** manage users and MFA, set sharing, keep own backups where needed, review logs, and report compromise. Three are open gaps (MFA method, sharing defaults, log review), so **the provider's controls protect the drawings only once the owner runs these.**
- **Fit for FCI:** FAR 52.204-21 sets no cloud authorization requirement for FCI, so the report is enough to approve the suite as the place FCI is kept (POL-01 8.2). If CUI ever arrived, DFARS 252.204-7012 would set a higher bar.
- **Follow-ups:** bridge letter by 2026-10-31.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.4, CC6.6 | Visitor log; remote-support settings and the technician's MFA confirmation |
| By 2026-10-31 | CC2.1, CC2.3, CC3.4, CC5.2, CC6.1, CC6.2, CC6.3, CC6.5, CC6.7, CC7.1, CC7.2, CC7.3, CC7.4, CC9.2 | Router and share settings; MFA screenshots; disposal record; supplier list; review log; walkthrough notes |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC7.5, CC8.1, CC9.1 | Course certificate; test restore record; released-program hashes; emergency access sheet |
| By 2027-08-31 | CC4.1 | Outside reviewer's notes |

**Answer for customer questionnaires:** a one-page letter from the owner that summarizes this check, the CMMC Level 1 status once affirmed, and the open POA&M items, updated each August.

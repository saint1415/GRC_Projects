# SOC 2 Readiness Self-Check: Cris Santos Company | Utilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent utility engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Utilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Part A is the owner's self-check (`soc2-readiness.csv`); Part B is a review of the email and file suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-23 (Part B) and 2026-07-24 (Part A) by the owner-engineer with the IT technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person engineering consultancy would not obtain a SOC 2 report.** A SOC 2 report describes a service organization whose systems its customers rely on. The clients rely on the owner's engineering judgment, not on a hosted system, and none has asked for a report. What the clients do ask for is evidence that their security terms are kept: **Client A sends an annual security questionnaire** under SSA-A, and Client B checks the laptop and USB drives at each visit under VAA-B. The utilities vertical's usual assurance route is the NERC CIP compliance audit of the registered entity (the client), which reaches the vendor only through the client's supply chain and access terms.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions, and its answers become the evidence behind Client A's questionnaire. Criteria that assume a board, staff, or software development are marked N/A with the reason, or are met through the owner's direct oversight.
- **B. Reading the email and file suite provider's SOC 2 report.** The suite holds most client files and every client notice runs through it. The owner uses the CC criteria as a checklist when reading the provider's report every year (POL-01 6.5).

## 2. System description (scope)
- **Services:** protection and control engineering, field support for commissioning and event analysis, and planning and interconnection studies for four utility clients.
- **System:** the Core Business Systems (P02): the email and file suite, laptop, phone, USB drives, accounting SaaS, home network, AI tools, and the owner's accounts on the Client A portal and the Client B gateway.
- **People:** the owner-engineer; the drafting subcontractor and IT technician under contract.
- **Data:** client security information (Client A BCSI, Client B settings and event records, CEII), client load data, and business records.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 16 | 4 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; the relay settings the business delivers go through each client's own change control).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (SMS codes, saved and reused passwords, daily administrator account), CC6.7 (client data outside approved locations: BCSI in email, site photos in a personal cloud, Client C data in an AI SaaS), CC7.2 (no log review), and CC9.2 (no vendor list or drafter access agreement). All four map to open POA&M items in P07 or High and Moderate gaps in P03.

**Confidentiality is out of scope here only because of the tier.** For this business, confidentiality of client information matters more than any other category. It is covered through the CC6 rows and POL-01 section 8. If a client ever asks for a SOC 2 report, C1 would be the first category to add.

## 4. Email and file suite provider report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, period ending 2026-03-31. One exception (departing provider staff kept access for 3 days), remediated.
- **Availability:** 99.9% monthly uptime with cross-region replication **meets the BIA** for client communications (BP-02: RTO 8 h, RPO 24 h). It does not cover the laptop's local settings databases (P01 R-011).
- **Controls the owner must run (CUECs):** choose MFA strength, manage users and sharing, review sign-in logs, protect credentials, and report compromise. Both exposures found in P04 came from the owner's sharing settings, and SMS delivery is carved out of the report. **The provider's controls protect client data only once the owner runs these.**
- **Follow-ups:** bridge letter by 2026-10-31; turn on sign-in and forwarding alerts; quote the provider's deletion periods in SSA-A (7) certifications.

## 5. Remediation plan and evidence calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1, CC6.2, CC6.7, CC6.8, CC5.2, CC2.3, CC7.3, CC7.4, CC9.2 | Password manager and MFA screenshots; deletion records; drafter agreement; printed contact sheet; walkthrough notes |
| By 2026-10-31 | CC1.4 (Client A module by 2026-10-20), CC2.1, CC6.3 (first quarterly review 2026-10-01), CC6.5, CC6.6, CC7.1, CC7.2, CC7.5 | Training certificates; monthly review log; certifications to Client A; router settings; backup and restore record |
| By 2026-12-31 and later | CC3.4, CC9.1 (2026-12-31); CC4.1 (2027-07-31) | Change review for the field laptop; standby engineer agreement; outside review notes |

**Answer to Client A's questionnaire:** each July the owner answers it from this checklist, the P07 results, and the POA&M, and attaches the sharing report (POL-01 7.8).

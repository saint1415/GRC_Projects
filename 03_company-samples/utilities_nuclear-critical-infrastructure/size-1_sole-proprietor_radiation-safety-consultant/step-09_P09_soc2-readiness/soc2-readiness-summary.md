# SOC 2 Readiness Self-Check: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent radiation safety consultant) |
| Tier / Vertical | Sole Proprietorship / Nuclear Reactors, Materials, and Waste |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the email and file suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-23 (Part B) and 2026-07-24 (Part A) by the owner-consultant with the IT technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person consultancy would not obtain a SOC 2 report.** SOC 2 reports on a service organization's system for its business customers. The business sells professional services, not a system its clients rely on, and could not justify a CPA examination. What Client A actually asks for is its **annual supplier security questionnaire**, and Client B relies on CSIA-B. This self-check is the evidence behind the questionnaire answers.

The Security criteria are useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Several criteria assume a board, staff, or a development team, so they are marked N/A or are met by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the suite provider's SOC 2 report.** The suite holds the business's email and report drafts. The owner reads the provider's report every year (POL-01 6.3) and runs the customer controls it lists.

## 2. Scope
- **Services:** radiation protection consulting for Client A, Client B, and small clients.
- **System:** the Core Business SaaS Stack (P02).
- **People:** the owner-consultant; the per-diem technician and IT technician under agreements.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 15 | 6 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure of its own).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (MFA gaps, daily administrator account, unencrypted field laptop and drive), CC6.3 (open link to Client B security information), CC6.5 (Client A packages not returned or destroyed), CC6.7 (one drive across clients; AI paste), CC7.2 (no log review), and CC9.2 (no vendor list; AI terms unreviewed). All six map to open POA&M items in P07.

**If an attestation is ever needed,** Confidentiality (C1) is the category to add first, because protecting client information is this business's main risk. Until then, CC6.1, CC6.5, and CC6.7 carry it.

## 4. Suite provider report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, period ending 2026-03-31. No exceptions.
- **The main finding is the owner's, not the provider's.** The open link to Client B's report (P07 AC-03) is a failure of a complementary user entity control: the provider offers named-person sharing and a sharing report, and the owner did not use them.
- **Controls the business must run (CUECs):** choose and enforce MFA, control sharing, review sign-in and sharing activity, remove users, protect devices. Sharing review and the stronger MFA method are open items (POAM-001, POAM-002).
- **Follow-ups:** bridge letter by 2026-10-31; add the provider's incident notice channel to the P08 contact list.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1 (MFA and standard account part), CC6.2, CC6.3, CC6.5, CC7.2, CC2.1, CC3.3, CC3.4 | MFA screenshots; empty browser password store; sharing report review log; Client A destruction certificate; register of client information |
| By 2026-10-31 | CC6.7, CC9.2, CC2.3, CC7.3, CC7.4, CC6.6, CC7.5 | Encrypted Client A drive; vendor list; walkthrough notes; printed contacts; restore test record |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC5.2, CC6.8, CC7.1, CC9.1, and the rest of CC6.1 | Course certificate; field laptop replacement; peer coverage agreement |
| July 2027 | CC4.1 | Outside reviewer's notes |

**Answering Client A's questionnaire:** answers come from this check and the POA&M dates, updated each July and before each outage. Where a criterion is not ready, the answer says so and gives the date.

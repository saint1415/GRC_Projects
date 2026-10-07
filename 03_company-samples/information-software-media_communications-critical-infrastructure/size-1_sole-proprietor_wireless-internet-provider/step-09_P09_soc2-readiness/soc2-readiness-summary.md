# SOC 2 Readiness Self-Check: Cris Santos Company | Communications | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated wireless internet service provider) |
| Tier / Vertical | Sole Proprietorship / Communications |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Self-check only; no SOC 2 examination planned |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the billing platform vendor's SOC 2 Type 2 report, plus the wholesale VoIP provider's security questionnaire (`vendor-soc2-review.csv`, added at this tier) |
| Prepared | 2026-07-23 (Part B, billing vendor), 2026-07-24 (Part A), and 2026-08-12 (VoIP questionnaire) by the owner-operator with the network consultant; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person ISP would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on them for their own control objectives. The company sells internet access and phone service to households, farms, and small businesses. Its customers rely on the connection, not on the company's controls over their data processing, and none has asked for a SOC 2 report. The Communications vertical lists no sector assurance alternative. A CPA examination would also cost more than a month of revenue.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Criteria that assume a board or a workforce are marked N/A or satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading key vendors' assurance.** The billing vendor and the wholesale VoIP provider operate most of the controls around CPNI (P02, P04). The owner uses the CC criteria as a checklist when reading the billing vendor's report and the VoIP provider's questionnaire every year (POL-01 6.3).

The checklist also feeds the statement the owner must file with the annual CPNI certification (47 CFR 64.2009(e)), which must explain how the company's procedures ensure compliance.

## 2. Scope
- **Services:** fixed wireless internet for about 310 accounts and the home phone add-on (58 VoIP lines).
- **System:** the ISP Operations Systems Profile (P02).
- **People:** the owner-operator; contractors under written terms.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 16 | 5 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC2.2 (no internal workforce). Unlike a business that only uses SaaS, CC8.1 (change management) stays in scope, because the owner changes the configuration of the core network devices that carry every customer's traffic.
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, signs the CPNI certification, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (no MFA on the VoIP portal; router management reachable from subscriber networks), CC6.6 (router firmware behind a critical advisory), CC7.1 (no vulnerability or change detection), CC7.2 (no monitoring), and CC8.1 (no change record for core network devices). All five map to open POA&M items in P07.

## 4. Vendor assurance (Part B)
- **Billing vendor:** Type 2, unqualified, Security and Availability, period ending 2026-04-30. One access removal exception, remediated. Stated RTO 8 hours and RPO 1 hour **meet the BIA** (BP-03 RTO 8 h; BP-04 RTO 72 h, RPO 24 h). Customer incident notice within 72 hours under the service terms.
- **The AI support assistant add-on is outside the report.** It was launched after the period ended. The owner treats it as unassured until the vendor brings it into scope (P10).
- **Controls the company must run (CUECs):** MFA for admins (in place), prompt user removal, correct customer authentication and notification settings (open, POAM-004), audit log review (open, POAM-007), and reporting suspected compromise (POAM-008).
- **Wholesale VoIP provider:** no SOC 2 report. Its questionnaire (2026-08-12) confirms MFA is available for reseller accounts, which makes the company's failure to turn it on (POAM-003) entirely the company's gap. No contractual breach notice period; requested at renewal.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.5, CC7.3, CC7.4 | Export deletion note; printed contacts; walkthrough notes |
| By 2026-10-31 | CC6.1, CC6.2, CC6.3, CC6.6, CC7.1, CC8.1, CC9.2, CC3.4 | MFA and filter screenshots; firmware versions; change log; vendor list |
| By 2026-12-31 | CC1.4 (courses by 2026-11-30), CC2.1, CC5.1, CC5.2, CC6.7, CC7.2, CC7.5 | Course certificates; log server; encrypted ATA settings; restore test record |
| By 2027-03-01 | CC2.3 | Filed CPNI certification and CALEA policies |
| Later | CC4.1 (outside review by 2027-07-31), CC9.1 (generator transfer and upstream study by 2027-06-30) | Reviewer report; quotes and decision |

**Self-attestation on request:** if a business customer asks about security, the owner sends a one-page letter that summarizes this check and the POA&M, updated each July.

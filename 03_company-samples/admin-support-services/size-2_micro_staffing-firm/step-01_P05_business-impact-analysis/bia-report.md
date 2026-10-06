# Business Impact Analysis: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Micro

**Organization:** Cris Santos Company, LLC (temporary staffing firm) | **Tier:** Micro (7 internal staff) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Operations Manager (Security and Privacy Lead) with the Account Manager, the Onboarding and Payroll Coordinator, the Senior Recruiter, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** Owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the firm, how long each can be down, and how much data each can lose. No law requires a staffing firm to have a contingency plan. The firm did this BIA because its two core duties are time-bound: associates must be at client sites the next morning, and they must be paid every Friday. The BIA feeds:
- the availability rating and contingency controls in the SSP (P02);
- impact ratings in the risk register (P01);
- the CSF 2.0 Recover rows of the gap analysis (P03);
- the recovery order in the incident response runbook (P08).

## 2. System and business description
One Central Florida office suite, 7 internal staff, about 22 temporary associates on assignment in an average week, and about 30 client accounts. The firm owns almost no infrastructure. Its work runs in vendor SaaS: the staffing ATS (SYS-01), the payroll and timekeeping service (SYS-02), the productivity suite (SYS-03), the background screening portal (SYS-06), E-Verify (SYS-07), and the accounting SaaS (SYS-10). On site are 8 laptops, an applicant tablet, and a scanner (SYS-04) and the office network (SYS-05). The MSP runs IT and the suite backup (SYS-08). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual receipts: about $19,400 billed a week (about $3,900 a business day) and a weekly associate payroll of about $13,500.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $15,000 (about 4 business days of billings, or a missed payroll) | $4,000 to $15,000 | Less than $4,000 |
| Operations | Associates are not paid, or client orders cannot be filled | One function stops; others slowed | Staff slowed but working |
| Regulatory | Reportable breach, or a Form I-9 or E-Verify violation | A deadline missed but curable (for example a late E-Verify case documented as an outage) | Internal policy deviation |
| Safety | Associate harm traceable to the outage (for example an associate sent to the wrong site without safety instructions) | Delayed site safety contact | None |
| Reputation | Loss of a major client, or associates quitting in numbers | Client complaints; poor online reviews from associates | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Client orders, assignments, and associate call-outs | High | 8 h | 4 h | 4 h |
| BP-02 Weekly associate and staff payroll | High | 24 h | 8 h | 24 h |
| BP-03 Onboarding: Form I-9, E-Verify, and background checks | High | 24 h | 8 h | 24 h |
| BP-04 Time capture and client approval | High | 48 h | 24 h | 24 h |
| BP-05 Recruiting and applicant screening | Moderate | 72 h | 24 h | 24 h |
| BP-06 Client invoicing and collections | Moderate | 120 h | 72 h | 24 h |
| BP-07 HR, compliance, and office records | Low | 120 h | 72 h | 24 h |
| BP-08 Direct-hire placement | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **BP-01 has the shortest MTD (one business day).** Clients order today for tomorrow morning. Past one day, shifts go unfilled and clients call another agency. The RPO is 4 hours because job orders and confirmations entered that morning cannot be rebuilt from memory.
- **BP-02 is the most visible failure.** Payroll is due in the payroll service by Wednesday 5 p.m. for Friday direct deposit. If the payroll service or the firm's access to it fails on a Wednesday, the firm has one day before associates go unpaid. The real risk to payroll is not an outage but fraud: diverted direct deposits (P01 R-001, R-002; P08).
- **BP-03 is set by legal clocks.** Form I-9 Section 2 is due within 3 business days of hire (8 CFR 274a.2(b)(1)(ii)), and E-Verify cases within 3 employer business days of hire, extended while E-Verify is down (MOU Art. II.A.9). Florida requires the employer to document any E-Verify outage, for example with a daily screenshot (Fla. Stat. 448.095(2)(c)). Paper Forms I-9 keep working when systems do not.
- **Safety is mostly N/A.** Associates work under client supervision, and site safety is the client's and the firm's field process, not a system function. The one link is BP-01: associates must be told where to report and whom to call.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Staffing ATS (SaaS) | Applicants, job orders, onboarding packets, screening orders | ATS vendor's platform backups. The vendor's stated recovery figures were not obtained (SOC 2 report requested 2026-08-03, not received) | BP-01, BP-03, BP-05, BP-08 |
| SYS-02 Payroll and timekeeping service (SaaS) | Payroll, tax filing, direct deposit, time capture, approvals | Payroll vendor's backups and replication. Its SOC 2 report states an RPO of 1 hour and an RTO of 8 hours (P09 review) | BP-02, BP-04, BP-06 |
| SYS-03 Productivity suite (SaaS) | Email, calendar, shared drive (Onboarding folder) | Vendor service resilience; daily copy to SYS-08 | BP-01, BP-03, BP-07, BP-08 |
| SYS-08 Suite backup (SaaS, MSP-operated) | Daily copy of email and the shared drive, 30 days | **Never restore-tested** | BP-07 |
| SYS-06 Screening provider portal | Background check orders and FCRA letters | Provider-hosted; usable directly if the ATS integration fails | BP-03 |
| SYS-07 E-Verify | Case creation | Federal system; outages documented under Fla. Stat. 448.095(2)(c) | BP-03 |
| SYS-10 Accounting SaaS | Invoices and receivables | Vendor backups | BP-06 |
| SYS-04 Endpoints | 8 laptops, applicant tablet, scanner, 7 personal phones | No business data kept locally by design; laptops reimaged by the MSP | All |
| SYS-05 Office network and internet | Firewall, Wi-Fi, one internet line | Firewall configuration backed up by the MSP; staff can work from home on laptops | All on-site work |
| People | 7 staff | Cross-training: the Operations Manager can run payroll and onboarding; the Owner can approve payroll | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Security and recovery evidence |
|---|---|---|
| Payroll service vendor | BP-02, BP-04, BP-06 | SOC 2 Type 2 report received 2026-08-14 and reviewed (P09); RTO 8 h and RPO 1 h meet this BIA |
| ATS vendor (and its AI subprocessor) | BP-01, BP-03, BP-05, BP-08 | Trust page claims a SOC 2 Type 2 report; requested 2026-08-03, not received by 2026-08-31 |
| Productivity suite vendor | BP-01, BP-07, email for everything | Vendor service commitments (standard terms) |
| MSP | Recovery of every laptop and the network; operates the suite backup | No written recovery commitment; the contract has a 4-business-hour response time only |
| Background screening provider | BP-03 | Not reviewed |
| DHS E-Verify | BP-03 | Federal system; the MOU extends the case deadline during outages |
| Internet provider and phone carrier | Every SaaS function at the office; BP-01 calls | None; single line. Laptops can work from home and phones forward to cell phones |

**Key findings:**
1. **The payroll vendor meets the BIA.** Its stated RTO (8 h) and RPO (1 h) meet BP-02 and BP-04. The firm's own access to payroll (SMS codes, no call-back on bank changes) is the weak point, not the vendor's platform.
2. **The ATS vendor is unverified.** BP-01, the function with the shortest MTD, depends on a vendor whose recovery capability the firm has never seen (P01 R-017).
3. **The shared-drive backup is unproven.** SYS-08 has never been restore-tested, so the BP-07 RTO and RPO are assumptions (R-005). The paper Forms I-9 limit the damage: they, not the scans, are the record of retention.
4. **No one has a manual payroll procedure written down.** The off-cycle workaround above was described in interviews but has never been tried (R-011).
5. **The MSP contract has no recovery commitment.** A 4-business-hour response is not a recovery time. The contract amendment in P01 (R-013) adds one.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Phones and the ATS from a clean device (BP-01) | 4 h | Office line forwarded to cell phones; printed assignment roster; laptops at home if the office is down |
| 2 | Payroll service access for the Operations Manager and the Coordinator (BP-02) | 8 h | Owner approves from a clean laptop; payroll vendor's off-cycle run or printed checks |
| 3 | Onboarding: screening portal and E-Verify (BP-03) | 8 h | Paper Form I-9; provider portal; E-Verify outage screenshots |
| 4 | Time approvals (BP-04) | 24 h | Signed paper timesheets |
| 5 | ATS recruiting functions and the AI feature (BP-05) | 24 h | Job board inboxes; recruiter review without scores |
| 6 | Accounting SaaS (BP-06) | 72 h | Spreadsheet invoices from the payroll billing report |
| 7 | Shared drive restore from SYS-08 (BP-07) | 72 h | Paper Forms I-9; re-download reports |
| 8 | Direct-hire work (BP-08) | 72 h | Any clean device |

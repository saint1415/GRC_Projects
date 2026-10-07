# Business Impact Analysis: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Micro

**Organization:** Cris Santos Company, LLC (radiation safety consulting practice) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (Security Officer) with the Principal Health Physicist, the Calibration Laboratory Technician, the Project Coordinator, and the MSP lead technician, 2026-08-03 to 2026-08-14 | **Approved:** Principal Health Physicist (owner), 2026-09-15

## 1. Overview and purpose
This BIA lists every business function of the practice, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the client notification steps, because two client contract clocks (4 hours for reactor clients, 24 hours for Part 37 clients) depend on the practice being able to reach its clients.

No regulation requires this practice to have a contingency plan or a BIA. The power reactor cyber rule (10 CFR 73.54) and the Part 37 rules bind the practice's clients, not the practice (P03 section 1). The BIA is done because a 7-person business can lose its two most sensitive service lines, calibration and Part 37 work, through one bad week.

## 2. System and business description
One Florida office suite with an attached calibration laboratory. 7 employees serve about 140 consulting clients, about 300 calibration and leak test customers, and 2 power reactor operators during refueling outages. Almost everything runs in SaaS: the productivity suite (SYS-01), the calibration and leak test system (SYS-02), and the accounting and payroll service (SYS-03). On site are 7 laptops and 2 lab workstations (SYS-04), the office network (SYS-05), and the lab instruments (SYS-07). The MSP runs IT and the suite backup (SYS-06). See `../00_company-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual receipts, about $4,400 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $13,000 (about 3 business days) | $4,000 to $13,000 | Less than $4,000 |
| Operations | The practice cannot serve clients at all, or a whole service line stops | One function stops; work is slowed | Staff slowed but working |
| Regulatory and contractual | A client's security information is disclosed, or a client misses a regulatory duty because of the practice | A client deadline or contract term is missed | Internal deviation only |
| Safety | A client uses an out-of-calibration survey instrument, or a leaking source goes undetected | Delayed calibration or leak test, covered by loaners or retesting | None |
| Reputation | Loss of a Part 37 or reactor client relationship; word spreads among licensees and the State | Client complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Consulting RSO services and program audits | Moderate | 72 h | 24 h | 24 h |
| BP-02 Part 37 security program services | High | 72 h | 24 h | 24 h |
| BP-03 Instrument calibration and certificates | High | 48 h | 24 h | 8 h |
| BP-04 Leak test sample analysis | Moderate | 120 h | 48 h | 24 h |
| BP-05 Shielding design and radiation surveys | Low | 120 h | 72 h | 24 h |
| BP-06 Reactor outage support | High | 24 h | 8 h | 24 h |
| BP-07 Client communications and report delivery | High | 24 h | 8 h | 24 h |
| BP-08 Billing, payroll, and office administration | Low | 120 h | 72 h | 24 h |
| BP-09 Radiation safety program for the practice's own license | Moderate | 72 h | 48 h | 24 h |

**What drives the values:**
- **BP-07** carries every other function. Without email, the client library, and the contact list, the practice cannot deliver reports or meet a contract notice clock, so its MTD is one business day.
- **BP-03** is the only function with a direct safety link. Clients' survey instruments must be calibrated (10 CFR 20.1501(c); for medical licensees, before first use, annually, and after repairs under 10 CFR 35.61). The practice promises a 5-business-day turnaround and keeps 12 loaner meters, which sets the MTD at 48 hours. Its RPO is 8 hours because readings are typed into SYS-02 the same day.
- **BP-02** is rated High for confidentiality, not for downtime. Part 37 work tolerates 72 hours of outage, but disclosure of one client's security plan would likely end the service line. Section 5 treats the restricted library as a recovery item in its own right.
- **BP-06** is High only during the 4 to 6 weeks of outages a year. Staff then work on plant systems, so the practice's IT matters mainly for scheduling and for the clean-media rule.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Productivity suite (SaaS) | Email, calendar, client library, chat | Vendor service resilience; nightly SaaS-to-SaaS backup (SYS-06) with 30 days of versions | BP-01, BP-02, BP-05, BP-06, BP-07, BP-08, BP-09 |
| SYS-02 Calibration and leak test system (vendor SaaS) | Instrument records, readings, certificates, leak test results, own source inventory | Vendor backups and replication (vendor SOC 2 report states RTO 8 h and RPO 1 h; see P09). **The practice has never exported its records** | BP-03, BP-04, BP-09 |
| SYS-03 Accounting and payroll (SaaS) | Invoices, receivables, payroll | Vendor service resilience | BP-08 |
| SYS-04 Endpoints | 7 laptops; lab workstation 1 (calibrator controller, electrometer); lab workstation 2 (gamma spectroscopy) | Laptops hold synced copies only. **Lab workstation 2 is a single, unsupported, unbacked-up computer; reinstalling the spectroscopy software needs the vendor and its license key** | All |
| SYS-05 Office network | Firewall, staff Wi-Fi, guest Wi-Fi, one internet line | Firewall configuration backed up by the MSP | BP-03, BP-04, BP-07 |
| SYS-06 Suite backup (SaaS, MSP-operated) | Nightly copy of mail and files, 30 days of versions | **Never restore-tested** | BP-07 and every function that uses SYS-01 |
| SYS-07 Lab instruments | Beam calibrator controller, reference electrometer, gamma spectroscopy system | Manufacturer service; paper data sheets | BP-03, BP-04 |
| People | 7 staff | Cross-training: the Principal Health Physicist can run calibrations; nobody backs up the gamma spectroscopy analysis except the Calibration Laboratory Technician | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Security or confidentiality terms | Evidence of recovery capability |
|---|---|---|---|
| Productivity suite vendor | BP-01, BP-02, BP-05, BP-06, BP-07, BP-08, BP-09 | Standard business terms | Vendor service commitments (standard terms) |
| Calibration and leak test system vendor | BP-03, BP-04, BP-09 | Confidentiality clause; data-use terms allow use of pooled customer data for "product improvement" (see P10) | SOC 2 Type 2 report reviewed (P09); RTO 8 h and RPO 1 h meet this BIA |
| MSP | Recovery of every on-site system; operates the backup | None beyond a general confidentiality clause | No written recovery commitment; the contract has only a 4-business-hour response time |
| Suite backup service (MSP subcontractor) | Restore of mail and files | Through the MSP (not reviewed) | None until the first restore test |
| Gamma spectroscopy software vendor | BP-04 | None | Reinstallation on request; no time commitment |
| Accounting and payroll service | BP-08 | Standard terms | Vendor service commitments |
| Internet provider and phone carrier | BP-07 and every SaaS function | Not applicable | None; single line; mobile phones as fallback |

**Key findings:**
1. **The suite is a single point for 7 of 9 functions, and its backup is unproven.** The vendor's own resilience is good, but deleted or encrypted files can only come back from SYS-06, which has never been restored (risk R-010).
2. **The calibration vendor meets the BIA, but holds the only copy.** Its stated RTO (8 h) and RPO (1 h) meet BP-03. The practice has never exported its own records, so a vendor failure or account lockout would leave it with nothing (R-015).
3. **Lab workstation 2 is the weak link for leak tests.** It is unsupported, unencrypted, unpatched, and not backed up, and rebuilding it depends on the software vendor. The 48-hour RTO for BP-04 is an assumption until a rebuild is rehearsed (R-009).
4. **The MSP contract has no recovery commitment.** A 4-business-hour response time is not a recovery time (R-013).
5. **Contract clocks need out-of-band contacts.** The 4-hour reactor notice and the 24-hour Part 37 client notice cannot depend on the suite being up. P08 adds a printed contact card.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Clean laptop access to the suite (SYS-01, SYS-04) for the Office Manager and Project Coordinator | 8 h | Mobile phones for calls; owner's laptop if clean; MSP reimages the others |
| 2 | Calibration laboratory: lab workstation 1 and SYS-02 access (SYS-07, SYS-05) | 24 h | Paper data sheets; loaner meters to clients with overdue instruments |
| 3 | Restricted client library for Part 37 work (SYS-01) | 24 h | Work from client on-site copies under client procedures |
| 4 | Remaining laptops for consultants (SYS-04) | 24 h | Paper checklists for site visits |
| 5 | Outage support coordination (SYS-01 calendar and email) | 8 h during an outage | Phone; staff work on plant systems |
| 6 | Lab workstation 2 and gamma spectroscopy (SYS-07) | 48 h | Hold samples; phone urgent results |
| 7 | Own-license records (SYS-02, SYS-01) | 48 h | Paper source log |
| 8 | Accounting and payroll (SYS-03) | 72 h | Payroll service repeats the prior payroll |
| 9 | Shielding and survey project files (SYS-01 restore from SYS-06) | 72 h | Rebuild from client drawings |

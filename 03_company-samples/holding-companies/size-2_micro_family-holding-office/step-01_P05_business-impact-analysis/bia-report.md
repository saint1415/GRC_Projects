# Business Impact Analysis: Cris Santos Company | Management of Companies and Enterprises | Micro

**Organization:** Cris Santos Company, LLC (family holding company and single-family office) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Family Office Director with the Controller, Investment Director, Senior Accountant, Office Manager, and the MSP lead technician, 2026-08-03 to 2026-08-14 | **Approved:** Principal, 2026-09-18

## 1. Overview and purpose
This BIA lists every business function of the office, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the Safeguards Rule element on identifying and managing the data, systems, and personnel that support the business "in accordance with their relative importance to business objectives" (16 CFR 314.4(c)(2)).

No federal rule requires this office to keep a contingency plan. The BIA is done because the office moves family and subsidiary money every day, and an outage or a fraudulent payment would hurt the family and the subsidiaries more than the office itself.

## 2. System and business description
One Florida office suite with 7 employees. The office oversees three operating subsidiaries (Hospitality, Marine Supply, Properties), manages about $310 million (fictional) of family assets held at two custodians, and runs bill pay, household payroll, accounting, and records for 11 family members and 10 family entities.

Nearly everything runs in vendor SaaS: the accounting system (SYS-01), the productivity suite with identity (SYS-02), bill pay (SYS-03), payroll (SYS-04), the investment platform (SYS-06), and the document vault (SYS-07). Banks and custodians host their own portals (SYS-05). On site are 8 laptops, 1 conference-room PC, and a printer (SYS-08) and the office network (SYS-09). The one cloud workload is the legacy partnership accounting server (SYS-11), run by the MSP. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to the family's exposure, not only the office's $1.1 million of fees: one misdirected wire can exceed the office's monthly revenue.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $50,000 (one fraudulent wire, a private fund default, or tax penalties) | $10,000 to $50,000 | Less than $10,000 |
| Operations | Payments, payroll, or approvals stop | One function stops; others slowed | Staff slowed but working |
| Regulatory | Safeguards Rule or state breach notice; loss of the Advisers Act family office exclusion | Missed tax, payroll, or lender deadline | Internal policy deviation |
| Personal safety and privacy | Family members' home addresses, travel plans, or minors' details exposed in a way that creates physical risk | Urgent personal need delayed (for example, a health care directive) | None |
| Reputation | Loss of a custodian or bank relationship, or a subsidiary lender's confidence | Complaints from family members or subsidiaries | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Treasury and payment approvals | High | 24 h | 8 h | 4 h |
| BP-02 Family bill pay and household payroll | High | 48 h | 24 h | 24 h |
| BP-03 Investment management and custodian instructions | High | 48 h | 24 h | 24 h |
| BP-04 Subsidiary oversight and consolidated reporting | Moderate | 120 h | 72 h | 24 h |
| BP-05 Family entity accounting and tax coordination | Moderate | 168 h | 72 h | 24 h |
| BP-06 Family records and emergency document access | Moderate | 24 h | 8 h | 24 h |
| BP-07 Investment reporting to the family | Low | 336 h | 168 h | 24 h |
| BP-08 Office communications and administration | High | 24 h | 8 h | 4 h |

**What drives the values:**
- **Money movement drives BP-01.** Subsidiaries cannot release large payments without the office's second approval, and capital calls and tax payments have fixed dates. One business day is the limit.
- **Email drives BP-08 and, through it, BP-01.** Payment requests, approvals, family requests, and subsidiary packages all arrive by email. That makes email both the most critical channel and the main attack path (risk R-001).
- **BP-05 tightens near deadlines.** A week of slack most of the year falls to about 2 days in the two weeks before a K-1 or tax deadline.
- **BP-06 is about people, not money.** A hospital may need a health care directive within hours. Counsel holds the originals, which is why the MTD is 24 hours and not shorter.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-02 Productivity suite and identity (SaaS) | Email, files, chat, sign-in for every other SaaS system | Vendor service resilience and the vendor's deleted-item retention. **No independent backup** | BP-01, BP-04, BP-08, and sign-in for all |
| SYS-05 Bank and custodian portals | Payments, approvals, trading instructions | Bank- and custodian-hosted; the banks keep the payment record. Hardware tokens per approver | BP-01, BP-02, BP-03 |
| SYS-01 Accounting system (SaaS) | Ledgers, consolidation, payee bank details | Vendor backups (SOC 2 report on file, not yet reviewed) | BP-04, BP-05 |
| SYS-03 Bill pay platform (SaaS) | Family bills | Vendor backups; payment history also at the banks | BP-02 |
| SYS-04 Payroll service (SaaS) | Office and household payroll | Vendor backups; prior payroll can be repeated by phone | BP-02 |
| SYS-06 Investment platform (SaaS) | Positions and reports | Custodian data can be pulled again | BP-03, BP-07 |
| SYS-07 Document vault (SaaS) | Family records | Vendor backups; counsel holds originals | BP-05, BP-06 |
| SYS-11 Legacy partnership accounting server (IaaS) | Capital accounts and K-1 allocations | Daily snapshots in the same cloud account, 14 days kept. **Never restore-tested** | BP-05 |
| SYS-08 and SYS-09 Laptops and office network | 8 laptops, 1 conference-room PC, firewall, one internet line | Laptops hold little data by design; staff can work from home | All |
| People | 7 staff; the Principal as backup bank approver | Cross-coverage: Controller and Family Office Director cover each other; Senior Accountant and Controller cover bill pay | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Productivity suite vendor | BP-08 and every SaaS sign-in (single sign-on) | Vendor service commitments (standard terms); no independent backup |
| Banks and custodians | BP-01, BP-02, BP-03 | Bank-grade resilience; phone instruction procedures with callback |
| Accounting system vendor | BP-04, BP-05 | SOC 2 Type 2 report on file, not reviewed (P09 follow-up) |
| Bill pay vendor and payroll service | BP-02 | Vendor service commitments |
| Investment platform vendor | BP-03, BP-07 | SOC 2 Type 2 report reviewed in P09 |
| Document vault vendor | BP-06 | Vendor service commitments |
| MSP | Recovery of laptops, network, and SYS-11 | Contract has a 4-business-hour response time and no recovery time commitment |
| Cloud provider (SYS-11) | K-1 allocations (BP-05) | Provider infrastructure; snapshots are the office's responsibility (P04) |
| Internet provider | Every SaaS function from the office | None; single line. Staff can work from home |
| Outside CPA firm | Tax returns (BP-05) | Not a technology dependency; extensions available |

**Key findings:**
1. **Email is a single point of failure and the main way in.** Every High function relies on SYS-02, and SYS-02 has no independent backup (risk R-006). A mailbox takeover can redirect payments without touching the banks (R-001).
2. **Bank-side controls are strong; the office side is weak.** The banks enforce dual approval, but two approvers who both trust a spoofed email will approve a fraudulent payment. The callback rule must be written down and recorded (R-002).
3. **SYS-11 recovery is unproven.** Its snapshots share the cloud account, so the same compromise could delete both, and nobody has tried a restore (R-007).
4. **The MSP contract has no recovery commitment.** Its 4-business-hour response time is not a recovery time (R-010).
5. **The internet line is not critical.** All systems are SaaS or hosted, and staff can work from home on managed laptops, so a single line is acceptable (R-019 accepted).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Clean laptops for the Controller and Family Office Director, and bank tokens (SYS-08, SYS-05) | 4 h | Principal as backup approver; spare laptop reimaged by the MSP |
| 2 | Identity and email (SYS-02) | 8 h | Phones and the printed contact card; vendor web portal from a clean device |
| 3 | Document vault (SYS-07) | 8 h | Counsel's originals; family members' own copies |
| 4 | Bill pay and payroll (SYS-03, SYS-04) | 24 h | Pay in bank portals; repeat prior payroll |
| 5 | Investment platform and custodian access (SYS-06, SYS-05) | 24 h | Custodian phone lines and websites |
| 6 | Accounting and consolidation (SYS-01) | 72 h | Spreadsheet consolidation |
| 7 | Legacy partnership accounting server (SYS-11) | 72 h | Rebuild K-1 allocations from the prior year file |
| 8 | Investment reporting (SYS-06 reports) | 168 h | Custodian statements |

# Business Impact Analysis: Cris Santos Company | Management of Companies and Enterprises | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded holding company with four operating subsidiaries and a shared services organization) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners in every subsidiary, 2026-05-04 to 2026-07-10 | **Approved:** CFO and Chief Risk Officer, 2026-07-24 | **Reported to:** risk committee of the board, 2026-09-17

## 1. Overview and purpose
This group-wide BIA identifies the business processes the holding company and its subsidiaries depend on, how long each can be down, how much data each can lose, and what each depends on, including the shared services that every subsidiary relies on, third parties, and the two acquired businesses. It feeds:
- the contingency plan and recovery objectives in the Shared Corporate Services Platform (SCSP) System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the shared-services compromise runbook (P08), and the business impact facts the disclosure committee uses for materiality;
- Finance's incident response plan and business continuity duties under its information security program (16 CFR 314.4(h));
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 7 are High criticality, 9 Moderate, and 1 Low. 3 processes need recovery within 4 hours and 9 within 8 hours. The dependency map (`dependency-map.csv`) lists 24 dependencies, 15 of them single points of failure and 6 never tested.

## 2. System and business description
Cris Santos Company is a public holding company headquartered in Florida with operations in six states. It owns four subsidiaries: Building Products (building materials distribution, 72 branches and 4 distribution centers), Home Services (residential HVAC and plumbing, 48 branches), Manufacturing (HVAC equipment, 3 plants), and Finance (consumer installment lending, about 210,000 loans). Global Business Services (GBS) runs accounting, treasury, payroll, procurement, and IT for all of them. The group has 12,000 employees and about $4.8 billion in annual receipts.

The technology estate is in `../00_company-facts.md` section 3. The center of it is the **Shared Corporate Services Platform** (P02): the group ERP (SYS-01), consolidation (SYS-02), treasury management and the payment hub (SYS-03), and the group identity platform (SYS-04). Around it sit the subsidiary systems (SYS-10), plant OT (SYS-11), two clouds and two data centers (SYS-07), and about 2,300 vendors (SYS-14). AQ-01 (acquired 2025-10) and AQ-02 (acquired 2026-03) still run their own directories and ERPs (SYS-15).

**What is different about a holding company.** Most processes belong to a subsidiary, but almost all of them depend on the same shared services. A single outage of the identity platform, the payment hub, or the shared virtualization layer stops every subsidiary at once. The BIA therefore rates each subsidiary process and then traces its dependency on shared services.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of receipts per calendar day and to the group's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | A tier-1 process stops group-wide, or a whole subsidiary or plant stops | One region, branch network segment, or service line stops | Staff slowed but working |
| Regulatory | Missed SEC filing; ICFR deficiency; consumer harm at Finance requiring remediation; breach notice to regulators | Missed contractual or internal deadline; breach notice to fewer than 500 people | Internal policy deviation |
| Safety | Plausible injury (plant machine safety; no-heat or no-cooling emergencies for vulnerable customers) | Delayed but safe service | None |
| Reputation | National media, analyst or rating agency action, loss of dealer or customer contracts | Regional media; customer or dealer complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-03 Home Services dispatch and field service | High | 12 h | 4 h | 15 min | $2.60M |
| BP-06 Finance loan origination and dealer financing platform (SL-1) | High | 8 h | 4 h | 15 min | $1.40M |
| BP-14 Customer contact centers | Moderate | 12 h | 4 h | 24 h | $1.10M |
| BP-08 Treasury and payments | High | 24 h | 8 h | 15 min | $0.50M |
| BP-04 Manufacturing production | High | 24 h | 8 h | 4 h | $4.90M |
| BP-07 Finance loan servicing, payments, and collections | High | 24 h | 8 h | 15 min | $0.60M |
| BP-01 Building Products order-to-cash | High | 24 h | 8 h | 1 h | $5.70M |
| BP-13 Connected equipment monitoring service (SL-2) | Moderate | 24 h | 8 h | 1 h | $0.20M |
| BP-17 Email, collaboration, and the AI assistant | Moderate | 24 h | 8 h | 1 h | $0.60M |
| BP-02 Building Products e-commerce and contractor portal | Moderate | 48 h | 12 h | 1 h | $0.90M |
| BP-09 Payroll and timekeeping | High | 48 h | 24 h | 24 h | $0.40M |
| BP-05 Manufacturing shipping and supply chain | Moderate | 48 h | 24 h | 4 h | $1.20M |
| BP-16 AQ-01 and AQ-02 operations on legacy systems | Moderate | 24 h | 24 h | 24 h | $1.10M |
| BP-10 Procure-to-pay | Moderate | 72 h | 48 h | 4 h | $0.30M |
| BP-11 Financial close, consolidation, and SEC reporting | Moderate | 120 h | 72 h | 4 h | $0.15M |
| BP-12 HR, benefits, and group health plan administration | Moderate | 120 h | 72 h | 24 h | $0.05M |
| BP-15 Board, investor relations, and M&A | Low | 72 h | 48 h | 24 h | $0.02M |

Rows are in recovery priority order (the `recovery_priority` column).

**What drives the values:**
- **Customers who leave the same day** set the shortest MTDs: dealers switch lenders at the kitchen table (BP-06), and Home Services customers with no heat or cooling call a competitor (BP-03).
- **Safety** raises BP-03 (vulnerable customers in extreme heat or cold) and BP-04 (an OT event can create unsafe machine states; the hardwired safety systems are independent of the control network).
- **Money movement** sets BP-08 and BP-09: missed payroll, tax, or debt service payments create legal and covenant exposure even though the dollar cost per day is modest.
- **Regulation** sets BP-11: SEC filing deadlines cut the close MTD to 48 hours in the quarter-end window. BP-07 is High because misapplied or late loan payments harm borrowers.
- **Contracts** set the objectives for the two service lines offered to outside customers: 99.9% monthly availability for SL-1 and 99.5% for SL-2 (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **The outsourced service desk (DEP-06) is a hidden single point of failure.** It performs about 61% of all password and MFA resets, including for administrators, after knowledge-based verification only. It is both an availability dependency and the most likely path to a full identity compromise. The internal fallback has never been tested. This is P01 risks R-002 and R-013 and POA&M items POAM-001 and POAM-012.
2. **Shared virtualization and the directory (DEP-01, DEP-04).** About 420 virtual machines from every subsidiary run on the shared virtualization layer at DC-1 and DC-2, and one directory serves every entity. The tier-1 DR test on 2026-04-25 met the identity RTO, but a ransomware event in this layer would stop all subsidiaries together (R-001, R-046).
3. **ERP recovery (DEP-02).** The ERP recovered in 9.5 hours against its 8-hour RTO in the 2026-04-25 DR test; the database restore took 3.1 hours of that and the rest was manual reconfiguration of integrations. This is R-019 and POAM-010.
4. **Acquired businesses (DEP-20, DEP-21).** AQ-01 and AQ-02 keep nightly backups only, so their real RPO is 24 hours against a 1-hour target, and the AQ-02 hosted ERP contract states a 48-hour RTO against the 24-hour BIA RTO. Neither restore has been tested (R-020).
5. **Vendor recovery times shorter than the BIA (DEP-11).** The field-service SaaS contract states an 8-hour RTO against the 4-hour BIA RTO for BP-03 (R-022). The consolidation fallback (DEP-09) and the EDI network (DEP-24) have never been tested (R-023, R-059).
6. **Plants (DEP-14, DEP-15).** Only Plant 1 has exercised its MES fallback; integrators reach Plants 2 and 3 through unmanaged remote tools (R-014, POAM-016).
7. **Bank concentration (DEP-07).** The primary bank carries 64% of payment value; the reroute to the secondary bank was tested on 2026-02-19 and the residual risk is accepted (R-021).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-04 Group identity platform | Directory, single sign-on, MFA, PAM, identity governance | All |
| SYS-01 Group ERP and integration platform (Cloud provider A) | Ledgers, payables, receivables, intercompany; interfaces to subsidiaries and banks | BP-01, BP-05, BP-08, BP-10, BP-11 |
| SYS-03 Treasury management and payment hub | Cash, wires, ACH, positive pay | BP-07, BP-08, BP-09 |
| SYS-02 Consolidation | Close and SEC reporting | BP-11 |
| SYS-10 Subsidiary systems | Distribution and e-commerce, field service, MES, loan origination and servicing | BP-01 to BP-07, BP-13 |
| SYS-11 Plant OT | Controllers, operator panels, robots | BP-04 |
| SYS-07 Clouds A and B; DC-1 and DC-2 | Hosting, standby regions, shared virtualization, backup copies | All |
| SYS-08 SD-WAN | Site connectivity with cellular failover | All site-based processes |
| SYS-05 HRIS and payroll | Workforce records, payroll, benefits enrollment | BP-09, BP-12 |
| SYS-06 Productivity suite and SYS-13 AI assistant | Email, files, chat, meetings | BP-17 and incident coordination |
| Immutable backups | Separate backup accounts with write-once retention; offline copy at DC-2 | RPO for all cloud workloads |
| People | Branch staff, technicians, plant workers, GBS accounting and treasury, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-04 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; isolated recovery forest |
| 2 | Network core, SD-WAN, DNS, and data center connectivity | 2 h | Cellular failover at branches |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | Managed security service provider tooling |
| 4 | Field-service system and contact center routing (BP-03, BP-14) | 4 h (8 h vendor contract) | Branch phone dispatch from printed schedules |
| 5 | Loan platform and SL-1 dealer portal (BP-06, BP-07) | 4 h | Phone applications for urgent deals; payments to suspense |
| 6 | Payment hub and treasury management (BP-08) | 8 h | Bank portals with dual approval for priority payments |
| 7 | MES and plant OT (BP-04), plant by plant | 8 h | Local controller programs and paper travelers for one shift |
| 8 | Distribution system (BP-01) | 8 h | Paper tickets; standalone card terminals |
| 9 | Productivity suite and SL-2 platform (BP-17, BP-13) | 8 h | Out-of-band phones; units run on local controls |
| 10 | Group ERP and integration platform | 8 h target (9.5 h demonstrated) | Bank portals; queued journals |
| 11 | E-commerce portal (BP-02) | 12 h | Branch ordering |
| 12 | HRIS and payroll (BP-09) | 24 h | Repeat the prior pay file |
| 13 | AQ-01 and AQ-02 legacy systems (BP-16) | 24 h target (48 h AQ-02 contract) | Paper tickets and dispatch |
| 14 | Consolidation and close (BP-11) | 72 h (48 h at quarter-end) | Controlled spreadsheets from ERP trial balances |
| 15 | Board portal and data rooms (BP-15) | 48 h | Encrypted documents through secure file transfer |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Outsourced service desk: single provider, weak verification, untested fallback | P01 R-002, R-013; POAM-001; POAM-012 |
| ERP recovery 9.5 h against an 8 h RTO | P01 R-019; P02 CP-10; POAM-010 |
| AQ-01 and AQ-02: RPO 24 h and AQ-02 contract RTO 48 h against BIA targets; no tested restore | P01 R-020; P03 G-021 (ICFR changes) |
| Field-service SaaS contract RTO 8 h against 4 h | P01 R-022 |
| Consolidation fallback and EDI never tested | P01 R-023, R-059 |
| Plants 2 and 3: MES fallback not exercised; unmanaged vendor remote access | P01 R-011, R-014; POAM-014; POAM-016 |
| Shared virtualization serves every subsidiary | P01 R-001, R-046; P08 recovery order |

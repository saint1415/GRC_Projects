# Business Impact Analysis: Cris Santos Company | Construction | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed commercial and institutional building general contractor) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and GRC analyst with the vCISO, the IT Director, and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: construction operations at 22 jobsites, the FC-4 design-build project, preconstruction, the prefabrication shop, finance, HR and payroll, contracts and compliance, virtual design and construction (VDC), the Technology and Security Systems group, the Managed Building Systems Services (MBSS) line, and equipment and fleet. It rates 17 business processes and quantifies what an outage costs in money, operations, contract and regulatory exposure, and safety.

The results feed:
- the IT contingency plan and the availability rating of the Project Delivery and Payment Platform (PDPP) in the SSP (P02);
- impact ratings and dollar exposure in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria for the MBSS SOC 2 readiness assessment (P09).

For a general contractor, **integrity of payment data matters as much as availability**. A two-day ERP outage costs overtime and some interest. One altered bank record can divert a whole progress payment (P01 R-001, R-002). For the FC-4 project, **confidentiality drives the design**: when the CUI Project Enclave is slow or unavailable, staff fall back to the commercial project platform, which is how CUI ended up outside the enclave (gap 1 in `../00_company-facts.md`). The BIA therefore records integrity and confidentiality workarounds alongside the usual downtime values.

## 2. System and business description
The company builds offices, health care buildings, schools, university buildings, and federal facilities from a Florida headquarters, a regional office, an equipment yard with a prefabrication shop, and 22 active jobsites, with 600 employees and about $100 million in revenue. Work runs on the PDPP described in the SSP (P02): the SaaS project management platform, the SaaS ERP, the identity provider, the productivity suite, the 5-account corporate cloud landing zone, the CUI Project Enclave (CPE) in a government-community cloud, office, yard, and jobsite networks, about 960 endpoints, and the MSSP-operated SIEM. The MBSS platform (SYS-13) runs in its own cloud account. See `../00_company-facts.md` sections 1 to 4.

## 3. Impact categories and values
Dollar values are scaled to about $94 million of construction revenue over about 250 business days (about $376,000 a day), about $6 million of MBSS revenue (about $16,400 a day), about $7.8 million billed a month, and about $5.2 million paid to subcontractors and suppliers a month.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $100,000 over the MTD, a missed bid, or any diverted payment | $20,000 to $100,000 | Less than $20,000 |
| Operations | Two or more jobsites stop or slow by more than 20%, a bid is missed, or client security systems go unmonitored | One jobsite, the shop, or one department stops | Staff slowed but working |
| Regulatory and contractual | Missed federal reporting, payment, or payroll duty (DFARS 252.204-7012(c), FAR 52.204-25(d), FAR 52.232-27, FAR 52.222-8), CUI handled outside authorized systems, or a reportable breach | Missed contract deliverable or response time | Internal policy deviation |
| Safety | Crews could start high-risk work without permits, or build from wrong structural or life-safety details | Delayed inspections | None |
| Reputation | An owner, surety, MBSS client, or the Army Corps of Engineers loses confidence; subcontractors stop bidding to the company | Owner or subcontractor complaints | Internal only |

**How criticality was set.** A process is **High** when two or more categories are Severe, **Moderate** when one is Severe or two or more are Moderate, and **Low** otherwise. The rule is applied in `bia.csv` and reviewed with each owner.

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered, extra labor, penalties, SLA credits, and interest over the MTD. For billing (BP-01), the loss is interest on the delayed cash at the credit line rate plus overtime; the delayed cash itself is shown separately. For estimating (BP-05), the loss is the expected margin on one missed bid.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-11 MBSS monitoring and client support | MBSS | High | 4 | 2 | 1 | $50,000 |
| 2 | BP-05 Estimating and bid submission (bid week) | Preconstruction | High | 8 | 4 | 24 | $300,000 |
| 3 | BP-03 Project document control | Construction operations | High | 24 | 8 | 1 | $90,000 |
| 4 | BP-04 CUI document control and distribution (FC-4) | FC-4 project | High | 24 | 8 | 4 | $15,000 |
| 5 | BP-13 Contract administration and federal compliance reporting | Contracts and compliance | Moderate | 24 | 8 | 24 | $5,000 |
| 6 | BP-07 Jobsite operations | Construction operations | Moderate | 24 | 8 | 8 | $10,000 |
| 7 | BP-08 Safety program and incident reporting | Safety | Moderate | 24 | 8 | 8 | $5,000 |
| 8 | BP-01 Progress billing and collections (billing week) | Finance | High | 48 | 8 | 4 | $60,000 (plus up to $7.8 million cash delayed one cycle) |
| 9 | BP-06 Craft payroll and certified payroll | HR and payroll | High | 48 | 24 | 24 | $20,000 |
| 10 | BP-16 VDC and BIM coordination | VDC | Moderate | 48 | 24 | 24 | $15,000 |
| 11 | BP-09 Prefabrication shop production | Construction operations | Moderate | 72 | 24 | 24 | $30,000 |
| 12 | BP-10 Security systems installation and commissioning | Technology and Security Systems | Moderate | 72 | 24 | 24 | $20,000 |
| 13 | BP-14 Subcontractor prequalification, onboarding, and vendor master setup | Contracts and compliance | Moderate | 72 | 24 | 4 | $10,000 |
| 14 | BP-02 Subcontractor and supplier payments | Finance | High | 120 | 48 | 4 | $25,000 |
| 15 | BP-15 Hiring, onboarding, and training | HR and payroll | Low | 120 | 72 | 24 | $5,000 |
| 16 | BP-12 Equipment and fleet management | Equipment and fleet | Low | 168 | 72 | 24 | $5,000 |
| 17 | BP-17 Financial close and reporting | Finance | Low | 168 | 120 | 24 | $5,000 |

**Summary:** 7 High, 7 Moderate, and 3 Low processes (17 in total). The sum of estimated losses at each process's MTD is $670,000.

**Enterprise-wide scenario.** If the corporate identity provider, productivity suite, and cloud workloads were down for 72 hours (for example, ransomware), the estimated cost is about $626,000: field productivity loss of about $226,000 (20% of $376,000 a day for 3 days), one missed bid ($300,000 expected margin), MBSS SLA credits ($50,000), and payroll and billing overtime (about $50,000). If the outage fell in billing week, about $7.8 million of cash would also be delayed by a month. Incident response, legal, and notification costs come on top (P01 R-005, R-006). The SaaS project platform and ERP would keep running, but staff could not sign in to them through single sign-on, so the break-glass and vendor-direct access paths in section 7 matter.

**What drives the values:**
- **Bid deadlines drive BP-05.** A late bid is rejected, so in bid week the tolerable outage is one working day. Outside bid weeks the MTD relaxes to 72 hours.
- **Client safety and SLAs drive BP-11.** The MBSS agreements require a response to critical alerts within 1 hour. After about 4 hours, a failed door controller or camera at a hospital or school can go unnoticed.
- **Drawings drive BP-03.** Crews can work about a day from offline tablet sets and printed sheets. After that, the risk of building from superseded sheets rises and RFIs stall.
- **Federal rules drive BP-02, BP-06, and BP-13.** Subcontractors on federal jobs must be paid within 7 days of the company's receipt of payment (FAR 52.232-27(c)(1)). Certified payrolls are due weekly (FAR 52.222-8(b)(1)). Section 889 reports are due within 1 business day (FAR 52.204-25(d)(2)(i)) and DFARS cyber incident reports within 72 hours (252.204-7012(c)(1)(ii)).
- **Cash and integrity drive BP-01 and BP-02.** A federal payment sent to incorrect EFT information that the contractor supplied is treated as paid, and the contractor must recover it (FAR 52.232-33(e)(2)).

## 5. Key findings
1. **The ERP vendor's recovery commitment does not meet billing week.** The ERP vendor's SOC 2 system description states RTO 24 hours and RPO 4 hours. In the last 5 business days of the month, 15 of 22 pay apps are due, so BP-01 needs RTO 8 hours. Action: contract amendment for billing-week priority support, and a daily export of the schedule of values and job cost to the backup account (P01 R-018; P09 vendor review).
2. **The CPE has no independent backup.** BP-04 depends on the government-community cloud provider's retention and versioning only. A compromised enclave account or synchronized deletion could destroy CUI design packages that cannot be recreated quickly (gap 9; P01 R-017).
3. **No company-controlled copy of project records.** SYS-01 meets the BP-03 targets on paper (vendor SOC 2: RTO 4 hours, RPO 1 hour), but the company has no export of its own if the vendor tenant or a project administrator account is compromised (gap 9; P01 R-019).
4. **MBSS recovery is untested.** The MBSS servers and remote-access gateway run in one cloud region. Backups exist, but a full rebuild has never been tested against the 2-hour RTO (P01 R-020; P09 A1.3).
5. **The offline workaround for drawings created the CUI spill on tablets.** Offline drawing sets on rugged tablets keep BP-03 going during outages. On FC-4 they also put CUI on 26 tablets outside the enclave. The workaround must be split: offline sets for non-CUI projects; printed CUI sets in a locked cabinet for FC-4 (P03 G-003 and G-019; P01 R-003).
6. **Payment workarounds must be integrity-safe.** The manual workarounds for BP-01, BP-02, and BP-14 rely on call-back to numbers already on file. Two of 25 sampled bank changes had no call-back record (gap 4). A workaround that accepts new bank details during an outage would recreate the business email compromise risk.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-04 Identity provider | Single sign-on, MFA, and conditional access for about 610 workforce accounts | All except BP-04 (enclave sign-in is separate) |
| SYS-05 Productivity suite | Email, files, chat; pay app, bid, and payment correspondence | BP-01, BP-02, BP-05, BP-06, BP-08, BP-10, BP-13, BP-14, BP-15, BP-17 |
| SYS-01 Project management platform | Drawings, RFIs, submittals, daily logs, safety module, pay app workflow | BP-01, BP-03, BP-07, BP-08, BP-09, BP-10, BP-14 |
| SYS-02 ERP and accounting | Billing, accounts payable, vendor master, ACH files, equipment costs | BP-01, BP-02, BP-12, BP-14, BP-17 |
| SYS-03 Payroll and HR | Payroll, certified payroll, applicant tracking | BP-06, BP-15 |
| SYS-06 Corporate landing zone | Estimating database, BIM/CAD servers and GPU virtual desktops, file-transfer portal, backup account | BP-05, BP-09, BP-16 (and recovery of all company-managed workloads) |
| SYS-07 CUI Project Enclave | CUI email and files, virtual desktops, 18 enclave laptops | BP-04 |
| SYS-08 Networks | SD-WAN (headquarters, regional office, yard); 22 jobsite cellular routers | All |
| SYS-09 Endpoints | 420 laptops and desktops, 380 smartphones, 150 rugged tablets, 12 commissioning laptops | All |
| SYS-10 Bank portal | ACH and wire release, positive pay | BP-02 |
| SYS-11 Jobsite technology | Time clocks, telematics | BP-06, BP-07, BP-12 |
| SYS-12 SIEM and MDR (MSSP) | Detection and investigation | Recovery validation |
| SYS-13 MBSS platform | Monitoring servers, remote-access gateway, ticketing, client credential vault | BP-10, BP-11 |
| SYS-14 Federal portals | SAM, SPRS, invoicing, DIBNet | BP-01, BP-05, BP-13 |
| Third parties | Project platform vendor, ERP vendor, payroll vendor, cloud provider, government-community cloud provider, MSSP, bank, cellular carriers, A&E subcontractor | As listed in `bia.csv` |
| People and facilities | Project Managers, superintendents, Controller and accounts payable staff, estimators, MBSS technicians, IT and security team, FC-4 project team; headquarters, regional office, yard, 22 trailers | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-04 identity provider and break-glass accounts | 1 h | Two break-glass accounts per critical SaaS with security keys in the headquarters safe; vendor-direct sign-in for SYS-01 and SYS-02 administrators |
| 2 | Out-of-band communications | 1 h | Company phones; printed contact list with verified numbers for owners, banks, subcontractors, the MSSP, and the insurer hotline |
| 3 | SYS-13 MBSS gateway and monitoring servers | 2 h | Rebuild from templates and backups in a second region (to be tested); technicians call clients and dispatch |
| 4 | SYS-08 SD-WAN and jobsite routers | 4 h | Cellular hotspots for trailers; second internet circuit at headquarters |
| 5 | SYS-05 productivity suite and SYS-09 clean endpoints | 4 h | Vendor-hosted; pre-imaged spare laptops (10 at headquarters, 4 at the regional office) |
| 6 | SYS-06 estimating database (bid week) | 4 h | Prior-day export on an encrypted laptop |
| 7 | SYS-01 project management platform access | 8 h | Offline tablet sets (non-CUI projects); printed sets |
| 8 | SYS-07 CUI Project Enclave | 8 h | Printed CUI sets in the locked FC-4 plan cabinet; never the commercial platform |
| 9 | SYS-14 federal portals (reporting) | 8 h | Any managed device with a valid medium assurance certificate; telephone the Contracting Officer |
| 10 | SYS-02 ERP and SYS-10 bank portal | 8 h in billing week; 24 h otherwise | Manual pay apps from the last export; manual ACH from the last approved batch, with call-back on any change |
| 11 | SYS-12 SIEM and EDR console | 8 h | MSSP runs from its own platform; needed to confirm clean recovery |
| 12 | SYS-03 payroll and certified payroll | 24 h | Repeat prior payroll through the vendor |
| 13 | SYS-06 BIM/CAD servers and GPU virtual desktops | 24 h | Restore from the backup account (10 hours in the 2026-03 test); design team model copies |
| 14 | SYS-06 file-transfer portal | 24 h | Design teams send through the project platform |
| 15 | SYS-11 telematics and time clocks | 72 h | Paper hour logs and time sheets |

**After any suspected business email compromise, "recovered" means "verified".** No payment instruction received or changed during the incident window may be used until it is confirmed by phone to a number already on file (P08 `ir-runbook.md`).

**After any suspected CUI incident, "recovered" means "preserved first".** Images of affected CPE systems and endpoints must be preserved for at least 90 days before rebuild (DFARS 252.204-7012(e); P08 `ir-runbook-cui-incident.md`).

## 8. Contract and regulatory linkage
| Source | What it asks of recovery | Where the BIA answers it |
|---|---|---|
| FAR 52.232-27(c)(1) | Pay subcontractors on federal jobs within 7 days of receiving payment | BP-02 MTD 120 hours, manual ACH workaround |
| FAR 52.222-8(a), (b)(1) | Weekly certified payrolls; payroll records kept 3 years after the work | BP-06 MTD 48 hours; payroll vendor retention |
| FAR 52.232-33(e)(2) | A payment to incorrect contractor-supplied EFT data is the contractor's loss | BP-01 integrity workaround; SAM changes need two approvers (P06 POL-01) |
| FAR 52.204-25(d) | Report covered equipment within 1 business day | BP-13 MTD 24 hours |
| DFARS 252.204-7012(c), (e) | Report cyber incidents within 72 hours; preserve images for 90 days | BP-13 MTD 24 hours; preservation before rebuild (section 7) |
| MBSS agreements | 1-hour response to critical alerts | BP-11 MTD 4 hours, RTO 2 hours |
| 29 CFR 1904.39(a) | Report fatalities within 8 hours, and in-patient hospitalization, amputation, or loss of an eye within 24 hours | BP-08: telephone or OSHA website; does not depend on company systems |

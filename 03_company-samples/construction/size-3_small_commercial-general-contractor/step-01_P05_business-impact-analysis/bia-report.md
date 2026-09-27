# Business Impact Analysis: Cris Santos Company | Construction | Small

**Organization:** Cris Santos Company, LLC (commercial and institutional building general contractor) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the Accounting Manager, VP Operations, and Director of Preconstruction | **Approved:** CFO, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the IT contingency plan due 2026-12-31 (P02 control CP-2);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

For this company, **integrity of payment data matters more than availability**. A two-day ERP outage is an inconvenience. One altered bank record can cost more than $1 million (P01 R-001, R-002). The BIA therefore records integrity-driven workarounds (phone verification of bank details) alongside the usual downtime values.

## 2. System and business description
The company builds commercial, institutional, and federal facilities from one Florida main office and 8 active jobsites, with 60 employees. Work runs on the Project Delivery and Payment Platform (PDPP):
- a SaaS project management platform
- a SaaS ERP
- an identity provider and a productivity suite
- a cloud tenant (BIM/CAD file server, estimating database, file-transfer portal, backups)
- the main office network, jobsite cellular routers, and endpoints

See `../00_company-facts.md` sections 3-4.

## 3. Impact categories and values
Dollar values are scaled to $27.0 million in annual revenue, about $108,000 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $250,000 (a lost bid, a diverted payment, or more than 2 days of revenue) | $50,000 to $250,000 | Less than $50,000 |
| Operations | Two or more jobsites stop work, or a bid is missed | One jobsite or one department stops | Staff slowed but working |
| Regulatory and contractual | Missed federal payment or payroll obligation (FAR 52.232-27, 52.222-8), or a reportable breach | Missed contract deliverable date | Internal policy deviation |
| Safety | Crews work from wrong drawings or without safety records | Delayed inspections | None |
| Reputation | Owner or surety loses confidence; subcontractors stop bidding to the company | Owner or subcontractor complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Progress billing and collections | High | 72 h | 24 h | 24 h |
| BP-02 Subcontractor and supplier payments | High | 120 h | 48 h | 24 h |
| BP-03 Project document control | High | 24 h | 8 h | 4 h |
| BP-04 Estimating and bid submission (bid weeks) | High | 8 h | 4 h | 24 h |
| BP-05 Payroll and certified payroll | High | 48 h | 24 h | 24 h |
| BP-06 Jobsite operations | Moderate | 24 h | 8 h | 8 h |
| BP-07 Security systems installation and commissioning | Moderate | 72 h | 24 h | 24 h |
| BP-08 Equipment and fleet management | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Bid deadlines drive BP-04.** A late bid is rejected, so during bid weeks the tolerable outage is one working day or less. Outside bid weeks the MTD relaxes to 72 hours.
- **Drawings drive BP-03.** Crews can work from printed sets for about a day. After that, the risk of building from superseded sheets rises and RFIs stall.
- **Federal rules drive BP-02 and BP-05.** On federal jobs, subcontractors must be paid within 7 days of the company's receipt of payment (FAR 52.232-27(c)(1)). Certified payrolls are due weekly (FAR 52.222-8(b)(1)).
- **Cash drives BP-01.** Billing is monthly, so a 3-day outage is survivable if it is not pay app week. Integrity is the real exposure. The FAR places the loss on the contractor when a federal payment goes to incorrect EFT information in SAM that the contractor supplied (FAR 52.232-33(e)(2)).

**Key finding.** The project management platform vendor's contracted recovery commitments must meet the 8-hour RTO and 4-hour RPO for BP-03. Its SOC 2 report (reviewed in P09) states an RTO of 4 hours and an RPO of 1 hour, which meets the BIA. The company-managed backups for the estimating database and file server have **never been restore-tested**, so the 4-hour RTO for BP-04 in bid weeks is unproven (P01 R-006).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-04 Identity provider | Single sign-on and MFA for all SaaS and the cloud tenant | All |
| SYS-05 Productivity suite | Email and files; pay app and bid correspondence | BP-01, BP-02, BP-04, BP-05, BP-07 |
| SYS-01 Project management platform | Drawings, RFIs, submittals, daily logs, pay app workflow | BP-01, BP-03, BP-06 |
| SYS-02 ERP and accounting | Billing, AP, vendor master, ACH file | BP-01, BP-02 |
| SYS-06 Estimating database and file server | Historical costs, bid files, BIM/CAD models | BP-04, BP-03, BP-07 |
| SYS-09 Bank portal | ACH and wire release | BP-02 |
| SYS-03 Payroll SaaS | Payroll and certified payroll | BP-05 |
| SYS-07 and SYS-08 | Main office network, jobsite routers, endpoints | All |
| People | Accounting Manager and AP clerk, Project Managers, estimators, superintendents, IT Manager, MSP | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-04 Identity provider and break-glass accounts | 1 h | Two break-glass administrator accounts with security keys stored in the CFO's safe (to be created; POL-02 4.7) |
| 2 | Out-of-band communications (company phones) | 1 h | Printed contact list with verified phone numbers for owners, banks, and subcontractors |
| 3 | SYS-05 Productivity suite | 4 h | Vendor-hosted; phones and text messages meanwhile |
| 4 | SYS-06 Estimating database (bid weeks) | 4 h | Prior-day export on an encrypted laptop |
| 5 | SYS-01 Project management platform | 8 h | Printed drawing sets in each trailer |
| 6 | SYS-07 Main office network and jobsite routers | 8 h | Cellular hotspots |
| 7 | SYS-03 Payroll | 24 h | Repeat prior payroll through the vendor |
| 8 | SYS-02 ERP and SYS-09 bank portal | 24 h | Manual pay app preparation; manual ACH from the last approved batch |
| 9 | SYS-06 File server and virtual desktops | 24 h | Design teams hold model copies |
| 10 | SYS-10 Telematics | 72 h | Paper hour logs |

**After any suspected business email compromise, "recovered" means "verified".** No payment instruction received or changed during the incident window may be used until it is confirmed by phone to a number already on file (P08).

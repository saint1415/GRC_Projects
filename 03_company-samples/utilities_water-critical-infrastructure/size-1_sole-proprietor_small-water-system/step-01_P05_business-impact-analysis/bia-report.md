# Business Impact Analysis: Cris Santos Company | Water and Wastewater Systems | Sole Proprietorship

**Organization:** Cris Santos Company (small community water system, 138 connections, 330 persons served) | **Tier:** Sole Proprietorship (owner-operator only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-operator, 2026-07-21, with the on-call IT technician (under a confidentiality agreement) | **Adopted:** Owner-operator, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five functions the water system depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the voluntary risk and resilience review in the gap analysis (P03), which follows the elements of SDWA section 1433 even though the law does not reach a system this small.

## 2. Business description
One licensed owner-operator runs a groundwater system for a rural subdivision in Florida: two wells, hypochlorite disinfection, a 50,000-gallon ground tank, two high-service pumps, and a pressure tank. A PLC panel in the well house (SYS-01) runs the plant and is reached from the owner's phone through a cloud remote access portal (SYS-02). Billing, email, and files are SaaS (SYS-03, SYS-04). There are no employees: a licensed relief operator covers days off, and a controls integrator supports the panel. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $15,000 a month.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (emergency repairs, bottled water, integrator call-out) | $1,000 to $5,000 | Less than $1,000 |
| Operations | Homes without safe water or pressure | Plant runs only by hand with extra site visits | Administrative delay only |
| Regulatory | Treatment technique violation or a missed Tier 1 notice | Late monthly report or a monitoring gap | Internal policy deviation |
| Safety | Plausible illness from under-disinfected water, or a chlorine overfeed | Precautionary boil water notice with no illness | None |
| Reputation | Primacy agency enforcement or local news coverage | Customer complaints | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Disinfection and treatment | High | 4 h | 2 h | 24 h |
| BP-02 Water supply and pressure | High | 8 h | 4 h | 720 h |
| BP-03 Remote monitoring and alarms | Moderate | 24 h | 8 h | 24 h |
| BP-04 Customer notices and communications | High | 24 h | 8 h | 720 h |
| BP-05 Billing, payments, and compliance reporting | Moderate | 240 h | 72 h | 24 h |

**What drives the values:** BP-01's 4-hour MTD comes straight from the Ground Water Rule. A failure to maintain 4-log virus treatment that is not corrected within 4 hours is a treatment technique violation (40 CFR 141.404(c)) and must be reported to the state by the end of the next business day (141.405(a)(1)). BP-04's 24 hours is the Tier 1 public notice clock (141.202(b)). BP-05's 10 days is the monthly reporting deadline (141.31(a)).

**The plant does not need the PLC to make safe water.** Every pump has a hand-off-auto switch, and the daily compliance grab sample uses a field test kit. What the plant needs is **the owner, on site, with the right settings written down**. The written dose table and manual-operation steps do not exist yet (missing item 13).

**Two RPO targets are not supported today.** BP-02's RPO is the last approved PLC program, and the only current copy is at the integrator (P01 R-004). BP-04's RPO assumes a monthly offline export of the customer contact list, which does not exist yet (P01 R-009).

**Single-person dependency (the key finding).** The owner is the only person who holds the portal, billing, and email credentials, knows the manual settings, and can issue a public notice. The relief operator covers planned days off but has no account of its own and has never run the plant by hand during an alarm. If the owner is ill or injured, BP-01 can exceed its 4-hour MTD before anyone else knows what to do. Actions (P01 R-005, due 2026-12-31):
1. Write a one-page manual-operation sheet (dose table by well flow, pump settings, how to isolate the cellular router) and keep it in the well house.
2. Extend the relief agreement to cover emergencies, give the relief operator a named portal account with MFA, and walk through the sheet together.
3. Store recovery codes and a one-page access sheet in a sealed envelope held by the owner's attorney.
4. Keep the primacy agency's after-hours number and the boil water notice template in the well house binder.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Treatment control panel | PLC, HMI, analyzer, flow meter, hand-off-auto switches, alarm dialer | BP-01, BP-02, BP-03 |
| SYS-02 Cellular router and remote access portal | Remote view and setpoint changes | BP-03 |
| SYS-06 Mobile phone | Portal app, alarm calls, MFA codes, customer calls | BP-03, BP-04 |
| SYS-03 Billing SaaS | Customer contacts, automated notices, billing | BP-04, BP-05 |
| SYS-04 Email and file storage; SYS-05 Laptop | Reports, records, drawings, residual spreadsheet | BP-04, BP-05 |
| Contracted services | Relief operator; controls integrator; certified laboratory; hypochlorite supplier | BP-01, BP-02, BP-05 |
| People | Owner-operator only; relief operator on days off | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner (or relief operator) on site at the well house | 1 h | Relief operator called by the dialer if the owner does not answer |
| 2 | Disinfection running by hand at a known dose | 2 h | Dose table on the manual-operation sheet; grab samples every 4 hours |
| 3 | Wells and pressure by hand; generator if power is out | 4 h | Portable generator on the transfer switch |
| 4 | Ability to issue a Tier 1 notice | 8 h | Paper template, offline contact list, hand delivery and posting |
| 5 | Clean remote access (portal and router) | 8 h | Two site visits a day; dialer alarms continue without the portal |
| 6 | PLC program verified against a known-good copy | 72 h | Integrator restores from its copy; plant stays in hand mode meanwhile |
| 7 | Billing and compliance reporting | 72 h | Paper log and lab portal for the monthly report |

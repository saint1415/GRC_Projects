# Business Impact Analysis: Cris Santos Company | Defense Industrial Base | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed aircraft parts manufacturer holding DoD subcontracts with CUI) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and the GRC analyst with the vCISO, the process owners named in `bia.csv`, and the IT Director | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: Plant 1 (machining, engineering center, test lab), Plant 2 (assembly, sheet metal, additive production), the additive and engineering services line, and enterprise functions (contracts and trade compliance, supply chain, finance, HR, IT). It rates 16 business processes and quantifies what an outage costs in money, operations, contract and regulatory exposure, and product safety.

The results feed:
- the contingency plan for the CUI Engineering Enclave (SP 800-53 CP-2, CP-4, CP-10 in the SSP, P02), due 2026-12-31;
- the availability rating in the SSP (P02 section 6);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria in the SOC 2 readiness assessment for the services line (P09).

NIST SP 800-171 Rev. 2 has no contingency planning requirement, so most of this BIA is a business need, not a CMMC requirement. Three contract duties depend on it: the 72-hour cyber incident report (DFARS 252.204-7012(c)) must be made even while systems are down; images of affected systems must be preserved for at least 90 days from the report (252.204-7012(e)) before they are rebuilt; and backups of CUI must be protected (SP 800-171 3.8.9).

## 2. System and business description
The company machines, assembles, and prints aircraft parts at two Florida plants for three defense primes and two commercial aerospace customers. Engineering data lives in the CUI Engineering Enclave (CEE): an identity provider, a collaboration suite, and a 4-account landing zone in a government-community cloud; CAD/PLM; 230 enclave endpoints; MES and DNC at both plants; operational technology (90 CNC machines, 12 CMMs, 6 additive printers, 6 test stands); and the plant networks. Orders, purchasing, and shipping run on a commercial ERP outside the enclave. See `../00_company-facts.md` sections 3 and 4 and the SSP (P02).

## 3. Impact categories and values
Dollar values are scaled to about $240 million in annual revenue over about 250 production days: about $528,000 of shipments per day from Plant 1, $392,000 from Plant 2, and $40,000 from the services line (about $960,000 in total).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $500,000 of shipments deferred, or more than $100,000 of unrecovered loss | $100,000 to $500,000 deferred, or $20,000 to $100,000 unrecovered | Less than $100,000 deferred and less than $20,000 unrecovered |
| Operations | A plant cannot produce or nothing can ship | One department, line, or work cell stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory and contract | Missed DFARS 72-hour report, unauthorized ITAR release, or loss of CMMC eligibility | Missed prime quality or delivery notice; services agreement breach | Internal policy deviation |
| Product safety | A nonconforming flight part could reach an aircraft, or a wrong NC program could injure an operator | Defect caught at inspection; rework or scrap | None |
| Reputation | Prime supplier rating downgrade, loss of source approval, or loss of a services customer | Corrective action request from a prime | Internal only |

**How loss at MTD was estimated.** Deferred shipments are mostly recovered with overtime within about 3 weeks. The estimated loss is the part that is not recovered: overtime and expedite premiums (about 10% of the deferred value for the plants), late delivery penalties, service credits, and scrap of interrupted additive builds. Process owners supplied the recovery assumptions. Deferred revenue and delayed cash are shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-12 Contracts, trade compliance, and DoD incident reporting | Enterprise | High | 24 | 8 | 24 | $0 direct (contract eligibility at risk) |
| 2 | BP-01 Machining and production release | Plant 1 | High | 24 | 12 | 4 | $70,000 |
| 3 | BP-02 Assembly, sheet-metal, and additive production | Plant 2 | High | 24 | 12 | 4 | $55,000 |
| 4 | BP-03 Quality inspection and product acceptance | Both plants | High | 24 | 12 | 4 | $30,000 |
| 5 | BP-10 Shipping, receiving, and customer delivery | Both plants | High | 48 | 24 | 4 | $120,000 (plus $1.92 million of shipments deferred) |
| 6 | BP-09 Order management, planning, and purchasing | Enterprise | Moderate | 48 | 24 | 4 | $40,000 |
| 7 | BP-06 NC programming and manufacturing engineering | Engineering | Moderate | 48 | 24 | 24 | $30,000 |
| 8 | BP-08 Additive and engineering services | Services line | Moderate | 48 | 24 | 4 | $35,000 |
| 9 | BP-05 Engineering design and change control | Engineering | Moderate | 72 | 24 | 24 | $25,000 |
| 10 | BP-07 CUI exchange with primes, customers, and suppliers | Enterprise | Moderate | 72 | 24 | 24 | $15,000 |
| 11 | BP-04 Hydraulic and functional testing | Plant 1 | Moderate | 72 | 24 | 24 | $20,000 |
| 12 | BP-11 Supplier management and outside processing | Enterprise | Moderate | 72 | 48 | 24 | $25,000 |
| 13 | BP-13 Program management and customer quality reporting | Enterprise | Moderate | 72 | 48 | 24 | $10,000 |
| 14 | BP-16 Corporate email, collaboration, and office work | Enterprise | Low | 48 | 24 | 24 | $10,000 |
| 15 | BP-14 Finance: invoicing, collections, and cost accounting | Enterprise | Moderate | 120 | 72 | 24 | $20,000 (plus about $4.8 million of invoicing delayed) |
| 16 | BP-15 Payroll, HR, and timekeeping | Enterprise | Low | 120 | 72 | 24 | $15,000 |

**Summary:** 5 High, 9 Moderate, and 2 Low processes (16 in total). The sum of estimated losses at each process's MTD is $520,000.

**Enterprise scenarios.**
- **Plant 2 shop floor down for 5 production days** (the P08 ransomware scenario): about $1.96 million of Plant 2 shipments deferred, about $235,000 not recovered (overtime, expedite freight, interrupted additive builds, late delivery penalties), plus response costs. Plant 1 can absorb only machined work whose programs are already proven there.
- **Enclave-wide outage for 72 hours** (cloud services and both plants' MES): about $2.88 million of shipments deferred and about $350,000 not recovered. Incident response and legal costs come on top (P01 R-004, R-012).

**What drives the values:**
- **Revenue and prime delivery ratings** drive BP-01, BP-02, and BP-10. Machines keep running loaded jobs for about one shift, so the MTD for production release is one production day.
- **Integrity drives BP-01 to BP-06 as much as availability.** A restored NC program, build file, inspection record, or test result that is one revision old can produce a nonconforming flight part. Recovery includes a revision check against PLM before release.
- **Contract duties** drive BP-12. Its RTO is short because the DoD reporting clock does not stop during an outage, and the report must come from a clean endpoint, not from the enclave.
- **Customer commitments** drive BP-08. The services agreements make availability and confidentiality part of what the customers buy (P09).

## 5. Key findings
1. **Plant 2 cannot meet its RPO.** The BIA needs a 4-hour RPO for BP-02, but the Plant 2 MES and DNC back up weekly to a storage device in the same room (gap 7). A ransomware event on the flat Plant 2 network could destroy the servers and the backup together and lose up to a week of traveler, inspection, and build status (P01 R-011). Plant 1 MES and DNC back up nightly to the cloud backup account, which meets a 24-hour RPO but not 4 hours; journal shipping every 4 hours is planned.
2. **Shop-floor recovery is unproven.** No MES restore has been tested at either plant. The 12-hour RTOs for BP-01 to BP-03 are targets, not demonstrated capabilities (P01 R-012; P07 CP-4).
3. **PLM recovery was proven once.** The 2025-04 restore test recovered PLM in 9 hours, within the 24-hour RTO for BP-05 and BP-06. It has not been repeated since the landing zone was rebuilt in 2025, so the result needs refreshing (P07 CP-4).
4. **The reporting capability exists but is untested.** Two medium assurance certificates are held, but there has been no DIBNet drill since 2024 and no clean reporting laptop is set aside (gap 12). BP-12 is first in the recovery order for that reason.
5. **Evidence preservation adds time to recovery.** Images of affected systems must be captured before servers are wiped (252.204-7012(e)). The procedure covers cloud systems only; for the Plant 2 MES and OT, imaging steps and storage are not defined (P08 runbook 2).
6. **The services line has no recovery commitments in writing.** Customer agreements promise turnaround times, but the company has not stated recovery objectives to the customers. The SOC 2 Availability criteria will require it (P09 A1.2, A1.3).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Enclave identity provider | Single sign-on and MFA for enclave services; 4 break-glass accounts | BP-03 to BP-08, BP-12, BP-13 |
| SYS-02 Enclave collaboration suite | CUI email, file storage, chat | BP-05, BP-07, BP-12, BP-13 |
| SYS-03 Landing zone: workloads account | PLM, CAD license servers, build preparation server, test data repository | BP-04 to BP-08 |
| SYS-03 Landing zone: shared services account | Network hub, VPN gateways, virtual desktop pool, MFT gateway | BP-05 to BP-08, BP-11 |
| SYS-03 Landing zone: backup account | Write-once backups (35 days) of cloud workloads and Plant 1 MES and DNC | Recovery of SYS-03, SYS-04, Plant 1 SYS-06 |
| SYS-04 CAD/PLM | System of record for about 165,000 controlled documents | BP-01 to BP-06, BP-08 |
| SYS-05 Enclave endpoints | 120 CAD workstations, 110 enclave laptops | BP-03 to BP-08 |
| SYS-06 MES and DNC | Plant 1 (40 terminals), Plant 2 (20 terminals) | BP-01, BP-02, BP-03, BP-10 |
| SYS-07 Operational technology | 90 CNC machines, 12 CMMs, 6 additive printers, 6 test stands, vision cell | BP-01 to BP-04, BP-08 |
| SYS-08 Plant networks and SD-WAN | Enclave firewalls, VLANs, SD-WAN, site-to-cloud VPN | BP-01 to BP-08 |
| SYS-09 Corporate network and suite | Commercial email, time clocks, clean reporting laptop | BP-09, BP-10, BP-12, BP-14 to BP-16 |
| SYS-10 ERP (SaaS) | Orders, purchasing, inventory, shipping documents, invoicing | BP-09, BP-10, BP-11, BP-14 |
| SYS-11 Payroll and HR SaaS | Payroll, onboarding, terminations | BP-15 |
| SYS-13 SIEM and MDR (MSSP) | Detection and investigation; validation of clean recovery | All (recovery validation) |
| DoD reporting capability | Medium assurance certificates, DIBNet access, prime security contacts | BP-12 |
| People and facilities | Operators, inspectors, engineers, manufacturing systems team, IT and security staff, MSSP; shop floors, inspection rooms, test lab, engineering center | All |

**Dependency note:** MES and DNC run on premises, so the shop floors keep working through an internet or cloud outage. Engineering, NC programming, the services line, and CUI exchange stop when the site-to-cloud VPN or the cloud services are down, although enclave laptops can reach enclave services from any internet connection. Plant 2 has a single internet circuit; Plant 1 has two.

## 7. Contract and DFARS duties that continue during an outage
| Duty | What this BIA supplies | Status |
|---|---|---|
| Report a cyber incident within 72 hours of discovery (252.204-7012(c)) | BP-12 first in recovery order; clean corporate laptop with certificates; prime contact list on paper | Certificates held; no drill since 2024 (drill set for 2026-11-18) |
| Preserve images and monitoring data for at least 90 days from the report (252.204-7012(e)) | Imaging step before rebuild in both P08 runbooks; storage in the backup account | Cloud procedure exists; OT and MES procedure due 2026-11-30 |
| Give the DoD incident report number to the prime (252.204-7012(m)(2)(ii)) | Prime security contacts in the incident binder | In place |
| Protect the confidentiality of backup CUI (SP 800-171 3.8.9) | Backups encrypted in the backup account | Met for cloud; Plant 2 local backups are not encrypted (P03) |
| Keep CUI only on systems with the required CMMC status once DFARS 252.204-7021 applies (252.204-7021(d)(2)) | Recovery uses only in-scope systems; no emergency use of corporate systems for CUI | Rule written into the P08 runbooks |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | DoD reporting capability (clean laptop, certificates, contact list) | 8 h | Report from a clean corporate laptop; phone primes' security contacts |
| 2 | SYS-01 identity provider and break-glass accounts | 1 h | Provider-hosted; break-glass accounts with hardware keys in the safes at both plants |
| 3 | SYS-08 plant networks, enclave firewalls, SD-WAN | 4 h | Restore firewall configurations from backup to spare hardware; cellular backup at Plant 2 |
| 4 | SYS-06 MES and DNC (Plant 1, then Plant 2) | 12 h | Paper travelers from controlled job packets; machines finish loaded jobs |
| 5 | SYS-07 CNC, CMM, and additive connectivity | 12 h | Load proven programs from DNC after a revision check; hand gauges for simple inspections |
| 6 | SYS-10 ERP | 24 h | Vendor-hosted; printed open-order and shipping reports |
| 7 | SYS-03 and SYS-04: PLM, virtual desktops, MFT, build preparation server | 24 h | Restore from the backup account; local CAD work checked in later |
| 8 | SYS-05 enclave endpoints | 24 h | Virtual desktops for engineers whose workstations are being reimaged |
| 9 | SYS-02 collaboration suite | 24 h | Provider-hosted; partners re-send files |
| 10 | SYS-13 SIEM and MDR views | 8 h (in parallel) | MSSP runs from its own platform; needed to validate a clean recovery |
| 11 | SYS-09 corporate network and email | 24 h | Mobile phones; paper time sheets |
| 12 | SYS-11 payroll and HR SaaS | 72 h | Repeat prior payroll |

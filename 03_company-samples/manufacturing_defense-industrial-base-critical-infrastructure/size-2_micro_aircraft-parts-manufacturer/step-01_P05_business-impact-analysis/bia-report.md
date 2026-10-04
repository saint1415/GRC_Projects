# Business Impact Analysis: Cris Santos Company | Defense Industrial Base | Micro

**Organization:** Cris Santos Company, LLC (aircraft parts machine shop holding DoD subcontracts with CUI) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (Security and Compliance Coordinator) with the President, CNC Programmer, Quality Inspector, Lead Machinist, and the MSP lead technician | **Fieldwork:** 2026-07-13 to 2026-07-24 | **Approved:** President, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the shop, how long each can be down, and how much data each can lose. It feeds:
- a short contingency plan for the CUI Machining Enclave, due 2026-12-31 (SP 800-53 CP-2, planned in the SSP);
- the availability rating in the SSP (P02 section 6);
- impact ratings in the risk register (P01);
- the recovery order and the reporting duties that must continue during an incident (P08).

NIST SP 800-171 Rev. 2 has no contingency planning requirement, so this BIA is a business need, not a CMMC requirement. Two DFARS duties still depend on it: the 72-hour cyber incident report (DFARS 252.204-7012(c)) must be possible while systems are down, and images of affected systems must be preserved for at least 90 days (252.204-7012(e)) before they are rebuilt.

## 2. System and business description
One leased Florida unit, 7 employees, 5 CNC machines and 1 CMM. CUI drawings and models live in the CUI suite (SYS-01, a government-community cloud SaaS) and sync to the CAM workstation (SYS-03), the quality PC (SYS-04), and two laptops (SYS-05). Programs go to 3 machines over the shop network and to 2 older machines by USB (SYS-06). Orders, purchasing, and invoicing run in a job-shop ERP SaaS (SYS-09); business email is in a commercial suite (SYS-02). The MSP runs IT. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue over about 250 production days, or about $4,400 of shipments per production day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $13,000 (about 3 production days) | $4,000 to $13,000 | Less than $4,000 |
| Operations | Nothing can be machined, inspected, or shipped | One function stops; deliveries slip | Staff slowed but working |
| Regulatory | Missed 72-hour DoD report, unauthorized ITAR release, or loss of CMMC eligibility | Missed prime notice or contract deliverable | Internal policy deviation |
| Safety | A nonconforming flight part could reach an aircraft, or a wrong program could injure an operator | Defect caught at inspection; rework or scrap | None |
| Reputation | Prime supplier rating downgrade or removal from the approved supplier list | Corrective action request from a customer | Internal only |

## 4. Process criticality and downtime
From `bia.csv` (7 processes: 3 High, 3 Moderate, 1 Low).

| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 CNC machining production | High | 48 h | 24 h | 4 h |
| BP-02 CNC programming and job setup (CAD/CAM) | Moderate | 72 h | 24 h | 4 h |
| BP-03 Quality inspection and product acceptance | High | 48 h | 24 h | 24 h |
| BP-04 Customer CUI exchange and quoting | Moderate | 72 h | 24 h | 24 h |
| BP-05 Orders, scheduling, purchasing, shipping, and invoicing | Moderate | 48 h | 24 h | 24 h |
| BP-06 DoD incident reporting and contract compliance | High | 24 h | 8 h | 24 h |
| BP-07 Payroll and bookkeeping | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- Revenue and prime delivery ratings drive BP-01 and BP-03. Machines keep running programs already loaded for about one shift, and nothing ships without inspection records, so both tolerate about two production days.
- Integrity matters as much as availability for BP-01 to BP-03. A restored NC program or CMM program one revision old can produce a nonconforming flight part. Every restored program is checked against the current drawing revision in the job folder before release.
- BP-06 has the shortest RTO because the DoD reporting clock keeps running during an outage. The capability does not exist yet: the company has no DoD-approved medium assurance certificate (P03 G-115).
- BP-02 depends on one person. Only the CNC Programmer can program complex parts. Losing that person for a week would stop new work even with every system running.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 CUI suite | Email, controlled job folders, identity and MFA | Provider-run service; file versions kept by the suite; backup inside the government-community offering planned by 2026-09-15 | BP-01 to BP-04, BP-06 |
| SYS-03 CAM workstation | CAM software, synced job folders, program transfer to 3 machines | Job folders re-sync from SYS-01. Until 2026-09-15 also a nightly image in the MSP's commercial cloud backup, which must stop because that cloud is not FedRAMP authorized (P04 finding 1). CAM post-processors and tool libraries to be kept in a SYS-01 folder | BP-01, BP-02 |
| SYS-04 Quality PC and CMM | CMM software and inspection programs | Inspection programs re-sync from SYS-01; same backup change as SYS-03 | BP-03 |
| SYS-05 Laptops (2) | President and Office Manager | Rebuilt by the MSP; data in SYS-01 and SYS-02 | BP-04 to BP-07 |
| SYS-06 CNC machines (5) | 3 networked, 2 USB-loaded | Programs in controller memory; released programs in SYS-01 | BP-01 |
| SYS-07 Shop network | Firewall, switch, Wi-Fi, printer, phones; one internet line | Firewall configuration backed up by the MSP | All |
| SYS-09 ERP (SaaS) | Orders, travelers, purchasing, invoicing | Vendor-hosted; vendor backups | BP-05 |
| SYS-02 Commercial suite | Business email | Vendor-hosted | BP-05 |
| SYS-11 Payroll and accounting SaaS | Payroll, bookkeeping | Vendor-hosted | BP-07 |
| People | 7 employees | Cross-training: Office Manager covers shipping; Lead Machinist covers simple programs at the control | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Government-community cloud provider | BP-02 to BP-04 (new work), BP-06 contact lists | FedRAMP authorization at Moderate or higher; provider service commitments. Customer responsibility matrix not yet on file (P02) |
| MSP | Recovery of every on-site computer, firewall, and backup | No written recovery commitment; the contract has only a 4-business-hour response time |
| Commercial backup service (MSP subcontractor) | Image restore of SYS-03 and SYS-04 | One file restore in 2025; no full restore test. Being retired because it holds CUI outside a FedRAMP-authorized cloud |
| ERP vendor | BP-05 | Vendor service terms |
| Machine tool and CMM service vendors | BP-01, BP-03 (hardware faults) | Service agreements with next-day response |
| Internet provider | BP-02 to BP-06 (cloud access); machines keep running | None; single line |

**Key findings:**
1. **DoD reporting cannot be done today.** BP-06 has an 8-hour RTO but no medium assurance certificate exists. This is the top recovery gap (P01 R-006).
2. **The CAM workstation's backup is in the wrong place.** The only full backup of SYS-03 and SYS-04 sits in a commercial cloud that is not FedRAMP authorized. Removing it without a replacement would leave the 24-hour RTO for BP-02 unproven. The approved sequence is: compliant SYS-01 backup first, settings folder second, then stop the commercial backup (P01 R-003).
3. **One programmer.** BP-02 has a key-person dependency that no system fixes. Treatment: a written programming procedure for the 10 highest-volume parts and an arrangement with a contract programmer who is a U.S. person (P01 R-019).
4. **The MSP contract has no recovery commitment.** The 4-business-hour response is not a recovery time (P01 R-010).
5. **Internet is a single point of failure for cloud work, not for machining.** Machines and the CMM keep running offline. A cellular backup router is planned (P01 R-015).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | DoD reporting capability (clean laptop, certificate, printed contacts) | 8 h | Certificate on two people's credentials (due 2026-10-31); borrowed clean device |
| 2 | Shop network and firewall (SYS-07) | 4 h | MSP restores configuration to a spare firewall; cellular router once installed |
| 3 | CNC machines (SYS-06) | 8 h | Finish loaded jobs; hand-load proven programs after a revision check |
| 4 | Quality PC and CMM (SYS-04) | 24 h | Manual inspection for simple parts; re-sync inspection programs from SYS-01 |
| 5 | CAM workstation (SYS-03) | 24 h | MSP rebuilds from the standard image; re-sync job folders; reactivate CAM license |
| 6 | CUI suite access (SYS-01) | 24 h | Provider-hosted; any enrolled laptop with MFA |
| 7 | ERP and commercial email (SYS-09, SYS-02) | 24 h | Printed open-order and traveler reports |
| 8 | Payroll and accounting (SYS-11) | 72 h | Payroll service repeats prior payroll |

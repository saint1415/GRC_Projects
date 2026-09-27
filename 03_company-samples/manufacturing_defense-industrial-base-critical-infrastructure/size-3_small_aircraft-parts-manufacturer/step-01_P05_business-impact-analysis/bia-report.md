# Business Impact Analysis: Cris Santos Company | Defense Industrial Base | Small

**Organization:** Cris Santos Company, LLC (aircraft parts manufacturer holding DoD subcontracts with CUI) | **Tier:** Small (250 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the Plant Manager, Quality Manager, Director of Engineering, Contracts Manager, and Controller | **Fieldwork:** 2026-07-13 to 2026-07-24 | **Approved:** Vice President of Operations, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the plant depends on, how long each can be down, and how much data each can lose. It feeds:
- the contingency plan for the CUI Engineering Enclave, due 2026-12-31 (SP 800-53 CP-2, planned in the SSP);
- the availability rating in the SSP (P02 section 6: Moderate);
- impact ratings in the risk register (P01);
- the recovery order and the reporting duties that must continue during an incident in the runbook (P08).

SP 800-171 Rev. 2 has no contingency planning requirement, so this BIA is a business need, not a CMMC requirement. Two DFARS duties still depend on it: the 72-hour cyber incident report (252.204-7012(c)) must be made while systems may be down, and images of affected systems must be preserved for at least 90 days (252.204-7012(e)) before they are rebuilt.

## 2. System and business description
The company machines structural fittings, brackets, and hydraulic manifolds on 38 CNC machines in one Florida plant. Engineering data lives in the CUI Engineering Enclave (CEE): an identity provider, a collaboration suite, and a cloud subscription in a government-community cloud; CAD/PLM; 40 enclave endpoints; MES and DNC servers on the shop-floor VLAN; and the plant enclave network. Orders, purchasing, and shipping run on a commercial ERP SaaS outside the enclave. See `../00_company-facts.md` sections 3 and 4 and the SSP (P02).

## 3. Impact categories and values
Dollar values are scaled to $68 million in annual revenue over about 250 production days, or about $272,000 of shipments per production day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $500,000 (about 2 production days) | $100,000 to $500,000 | Less than $100,000 |
| Operations | Shop floor stops or nothing can ship | One department or work cell stops | Staff slowed but working |
| Regulatory | Missed DFARS 72-hour report, unauthorized ITAR release, or loss of CMMC eligibility | Missed contract quality or delivery notice to a prime | Internal policy deviation |
| Safety | A nonconforming flight part could reach an aircraft, or a wrong NC program could injure an operator | Defect caught at inspection; rework or scrap | None |
| Reputation | Prime supplier rating downgrade or loss of source approval | Corrective action request from a prime | Internal only |

## 4. Process criticality and downtime
From `bia.csv` (10 processes: 4 High, 5 Moderate, 1 Low).

| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Shop-floor release and production | High | 24 h | 12 h | 4 h |
| BP-02 Quality inspection and product acceptance | High | 48 h | 24 h | 4 h |
| BP-03 Engineering design and change control | Moderate | 72 h | 24 h | 24 h |
| BP-04 NC programming and manufacturing engineering | Moderate | 48 h | 24 h | 24 h |
| BP-05 CUI exchange with primes and outside processors | Moderate | 72 h | 24 h | 24 h |
| BP-06 Order management, purchasing, and inventory | Moderate | 48 h | 24 h | 4 h |
| BP-07 Shipping, receiving, and customer delivery | High | 48 h | 24 h | 4 h |
| BP-08 Contracts, export compliance, and DoD incident reporting | High | 24 h | 8 h | 24 h |
| BP-09 Corporate communications and office work | Moderate | 48 h | 24 h | 24 h |
| BP-10 Payroll and human resources | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- Revenue and prime delivery ratings drive BP-01 and BP-07. Machines keep running jobs already loaded for about one shift, so the MTD for shop-floor release is one production day.
- Integrity drives BP-01, BP-02, and BP-04 as much as availability does. A restored NC program or inspection record that is one revision old can produce a nonconforming flight part. Recovery must include a check of program and drawing revisions against PLM before release.
- BP-08 has a short RTO because the DoD reporting clock does not stop during an outage. It must not depend on the enclave: the report is made from a clean endpoint with a DoD-approved medium assurance certificate, which the company does not yet have (P03 G-115).
- Engineering (BP-03) tolerates a longer outage because released jobs keep running and customer change deadlines are usually measured in days.

**Key findings:**
1. **MES and DNC backups do not meet the 4-hour RPO for BP-01.** They are weekly, to a local disk in the same server room (SSP CP-9). A ransomware event on the shop-floor VLAN could destroy both the servers and the backup and lose up to a week of traveler status. NC programs can be re-sent from PLM, but traveler and inspection status would be rebuilt from paper (P01 R-011).
2. **PLM daily backups meet the 24-hour RPO for BP-03 and BP-04**, but no restore has ever been tested, so the 24-hour RTO is unproven. A restore test is planned with the contingency plan (2026-12-31).
3. **No contingency plan exists.** Recovery steps are in people's heads. The contingency plan is due 2026-12-31 (SSP CP-2 and CP-10).
4. **Evidence preservation comes before rebuild.** For a cyber incident affecting CUI, images of affected systems must be captured before servers are wiped (DFARS 252.204-7012(e)). This adds time to recovery and is built into the P08 runbook.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Enclave identity provider | Single sign-on and MFA for enclave services; 2 break-glass accounts | BP-02 to BP-05, BP-08 |
| SYS-02 Enclave collaboration suite | CUI email, file storage, chat | BP-03, BP-04, BP-05, BP-08 |
| SYS-03 Enclave cloud subscription | PLM VMs, virtual desktops, SFTP gateway, backup vault | BP-03, BP-04, BP-05 |
| SYS-04 CAD/PLM | System of record for about 41,000 controlled documents | BP-02, BP-03, BP-04 |
| SYS-05 Enclave endpoints | 24 CAD workstations, 16 enclave laptops | BP-02 to BP-05 |
| SYS-06 MES and DNC servers, 14 terminals | Travelers, work instructions, NC program distribution | BP-01, BP-02, BP-04, BP-07 |
| SYS-07 CNC machines and CMMs | 38 CNC machines (32 DNC, 6 USB-loaded), 4 CMMs | BP-01, BP-02 |
| SYS-08 Plant enclave network | Enclave firewall, VLANs, site-to-site VPN to SYS-03 | BP-01 to BP-05 |
| SYS-09 Corporate network and productivity suite | Commercial email, time clocks, 170 corporate endpoints | BP-06, BP-07, BP-08, BP-09, BP-10 |
| SYS-10 ERP (SaaS) | Orders, purchasing, inventory, shipping documents | BP-06, BP-07 |
| SYS-11 Payroll and HR SaaS | Payroll, onboarding, terminations | BP-10 |
| DoD reporting capability | Medium assurance certificate, DIBNet access, prime security contacts (not yet in place) | BP-08 |
| People and facilities | Machine operators, inspectors, engineers, Manufacturing Systems Engineer, IT staff; shop floor, inspection room, engineering wing | All |

**Dependency note:** MES and DNC run on premises, so the shop floor keeps working through an internet or cloud outage. Engineering, NC programming, and CUI exchange stop when the site-to-site VPN or the cloud services are down, although enclave laptops can reach enclave services from any internet connection.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | DoD reporting capability (clean endpoint, certificate, contact list) | 8 h | Report from a clean corporate laptop; phone Prime A and Prime B security contacts |
| 2 | SYS-01 Identity provider and break-glass accounts | 1 h | Provider-hosted; 2 break-glass accounts with hardware keys in the safe |
| 3 | SYS-08 Plant enclave network and firewall | 4 h | Restore firewall configuration from backup to replacement hardware |
| 4 | SYS-06 MES and DNC servers | 12 h | Paper travelers from controlled job packets; machines finish loaded jobs |
| 5 | SYS-07 CNC and CMM connectivity | 12 h | Load proven programs from DNC after revision check; hand gauges for simple inspections |
| 6 | SYS-10 ERP | 24 h | Vendor-hosted; printed open-order and shipping reports |
| 7 | SYS-03 and SYS-04 PLM, virtual desktops, SFTP gateway | 24 h | Restore PLM from the backup vault; local CAD work checked in later |
| 8 | SYS-05 Enclave endpoints | 24 h | Virtual desktops for engineers whose workstations are being reimaged |
| 9 | SYS-02 Collaboration suite | 24 h | Provider-hosted; partners re-send files |
| 10 | SYS-09 Corporate network and email | 24 h | Mobile phones; paper time sheets |
| 11 | SYS-11 Payroll and HR SaaS | 72 h | Repeat prior payroll |

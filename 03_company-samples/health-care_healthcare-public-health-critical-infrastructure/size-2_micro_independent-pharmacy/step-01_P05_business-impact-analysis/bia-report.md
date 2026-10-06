# Business Impact Analysis: Cris Santos Company | Healthcare and Public Health | Micro

**Organization:** Cris Santos Company, LLC (independent community pharmacy) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Store Manager (Privacy and Security Officer) with the pharmacist-owner, the Staff Pharmacist, the Lead Pharmacy Technician, and the MSP lead technician, 2026-07-13 to 2026-07-24 | **Approved:** pharmacist-owner, 2026-08-28

## 1. Overview and purpose
This BIA lists every business function of the pharmacy, how long each can be down, and how much data each can lose. It supports:
- the contingency plan required by the HIPAA Security Rule (45 CFR 164.308(a)(7)), including the Applications and Data Criticality Analysis (164.308(a)(7)(ii)(E));
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order and diversion decision in the incident response runbook (P08).

The CMS emergency preparedness conditions (C-HPH-R07, 42 CFR 482.15 and the parallel rules) do not apply: pharmacies are not among the covered provider types. The drivers here are the HIPAA contingency plan standard, the DEA rules for electronic controlled substance prescriptions (21 CFR Part 1311), and the Florida pharmacy duties in `../00_company-facts.md` section 1.

## 2. System and business description
One Florida storefront, 7 employees, about 3,100 active patients, about 55 prescriptions a business day, and about 25 deliveries a day. About 70 patients, including about 40 residents of two assisted living facilities (ALFs), receive weekly adherence packs. Nearly everything runs in vendor SaaS: the pharmacy management system (PMS, SYS-01), the productivity suite (SYS-02), cloud fax (SYS-06), the MSP-operated cloud backup (SYS-07), and the proof-of-delivery app (SYS-08). On site are 5 desktops, 2 laptops, and a delivery phone (SYS-03), the store network (SYS-04), and the adherence packaging system (SYS-05). The MSP runs IT. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual sales, about $3,600 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $11,000 (about 3 business days) | $3,500 to $11,000 | Less than $3,500 |
| Operations | The pharmacy cannot dispense | One function stops; dispensing slowed | Staff slowed but working |
| Regulatory | Reportable breach, or a missed DEA or PDMP duty | Missed documentation or timeliness requirement | Internal policy deviation |
| Safety | Plausible patient harm (missed doses, a missed interaction or allergy, wrong patient or drug) | Delayed but safe care | None |
| Reputation | Loss of the ALF business or local media coverage | Patient complaints, transfers to other pharmacies, online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Prescription intake, verification, and dispensing | High | 8 h | 4 h | 1 h |
| BP-02 Controlled substance dispensing and DEA and Florida duties | High | 24 h | 8 h | 1 h |
| BP-03 Claims adjudication and PBM billing | Moderate | 24 h | 8 h | 1 h |
| BP-04 Patient pickup, counseling, and payment | High | 8 h | 4 h | 4 h |
| BP-05 Adherence packaging for ALF residents and home patients | High | 48 h | 24 h | 24 h |
| BP-06 Delivery | Moderate | 24 h | 8 h | 24 h |
| BP-07 Refill requests and communications | Moderate | 24 h | 8 h | 24 h |
| BP-08 Purchasing and inventory | Moderate | 48 h | 24 h | 24 h |
| BP-09 Office administration, payroll, and records | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- Patient safety drives BP-01 and BP-04. Allergies, drug interaction checks, and the medication history live only in the PMS. An MTD of 8 hours is one business day; past that, about 55 prescriptions a day go unfilled and patients transfer to other pharmacies, often for good.
- BP-02 has an RPO of 1 hour because EPCS records must be kept electronically for 2 years (21 CFR 1311.305) and the PMS backs them up daily (1311.205(b)(17), a duty of the application). If the PDMP cannot be reached because of a technical failure, Florida lets the pharmacist dispense up to a 3-day supply after documenting the reason (Fla. Stat. 893.055(8)), which sets a hard limit on how long controlled substance dispensing can run on workarounds.
- BP-05 tolerates 48 hours because packs are built 2 days before the Wednesday delivery. A longer outage means hand-filled cards for about 70 patients.
- BP-08 tolerates 48 hours because the wholesaler delivers next day and fast movers are stocked for about 2 days.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 PMS (SaaS) | Profiles, e-prescriptions including EPCS, DUR, labels, claims, PDMP file, refill line, signature capture, packaging interface | PMS vendor's backups and replication (vendor SOC 2 report states RPO 30 minutes and RTO 4 hours; see P09) | BP-01 to BP-05, BP-07 |
| SYS-02 Productivity suite (SaaS) | Email and the shared drive | Vendor service resilience; shared drive copied nightly to SYS-07 | BP-07, BP-09 |
| SYS-03 Endpoints | 5 desktops, 2 laptops, delivery phone | No data stored locally by design; downloaded faxes and reports in practice. The owner laptop holds the CSOS certificate | All |
| SYS-04 Store network and internet | Firewall, Wi-Fi, VoIP phones, one internet line | Firewall configuration backed up by the MSP | All |
| SYS-05 Adherence packaging system | Strip packager and controller workstation with local pack history | Nightly image in SYS-07; **never restore-tested** | BP-05 |
| SYS-06 Cloud fax (SaaS) | Prescriptions, refill authorizations, ALF orders | Faxes queue at the vendor | BP-01, BP-07 |
| SYS-07 Cloud backup (SaaS, MSP-operated) | Shared drive copy; images of the back-office desktop and SYS-05 workstation; 30 days of versions | **Never restore-tested** | BP-05, BP-09 |
| SYS-08 Proof-of-delivery app (SaaS) | Route list and signatures on the delivery phone | Vendor-held; no backup agreement | BP-06 |
| People | 2 pharmacists, Store Manager, 2 technicians, clerk, driver | Cross-training: the Store Manager covers intake and claims; the Staff Pharmacist covers the owner | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | BAA | Evidence of recovery capability |
|---|---|---|---|
| PMS vendor (with the e-prescribing network, claims switch, and PDMP connection) | BP-01 to BP-05, BP-07 | Yes | SOC 2 Type 2 report reviewed (P09); RTO 4 h and RPO 30 min meet this BIA |
| MSP | Recovery of every on-site system; operates the backup | Yes | No written recovery commitment; the contract has a 4-business-hour response time only |
| Backup service (MSP subcontractor) | Restore of the shared drive and the SYS-05 workstation | Through the MSP (flow-down not verified) | None until the first restore test |
| Packaging equipment vendor | BP-05 | **No** | Service contract with next-business-day on-site support; no recovery commitment for the workstation software |
| Productivity suite vendor | BP-07, BP-09 | Yes | Vendor service commitments (standard terms) |
| Cloud fax vendor | BP-01, BP-07 | Yes | Vendor service commitments |
| Proof-of-delivery app vendor | BP-06 | **No** | None (free tier) |
| Drug wholesaler | BP-08 | Not a business associate | Next-day delivery; sales representative takes phone orders |
| Internet provider | Every SaaS function | Not a business associate (conduit) | None; single line |

**Key findings:**
1. **The PMS vendor meets the BIA.** Its stated RTO (4 h) and RPO (30 min) meet the targets for BP-01 to BP-04.
2. **The internet line is a single point of failure for every High function** (risk R-010). The PMS is reachable only over the internet.
3. **On-site recovery is unproven.** SYS-07 has never been restore-tested, so the 24-hour RPO for BP-05 and BP-09 and the rebuild of the packaging workstation are assumptions (risk R-005).
4. **The MSP contract has no recovery commitment.** Its 4-business-hour response time is not a recovery time. The contract amendment in P01 (R-013) adds one.
5. **There is no downtime procedure.** The workarounds in `bia.csv` were described by the pharmacists in interviews; none is written down or practiced. The contingency plan due 2026-11-30 (P03) turns them into a one-page downtime card.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Internet and store network (SYS-04) | 2 h | Cellular failover router (to be installed by 2026-11-30); a phone hotspot until then |
| 2 | Clean intake, verification, and pickup stations (SYS-03) | 4 h | Laptops if clean; MSP reimages desktops from its standard image |
| 3 | PMS access (SYS-01) | 4 h | Vendor-hosted; paper downtime log, emergency refills, and transfers to the partner pharmacy until restored |
| 4 | Cloud fax (SYS-06) | 8 h | Vendor web portal from any clean device |
| 5 | Phones and email (SYS-04 VoIP, SYS-02) | 8 h | Main line forwarded to the store cell phone |
| 6 | Delivery phone and app (SYS-08) | 8 h | Printed route sheet and paper signature slips |
| 7 | Packaging workstation (SYS-05) | 24 h | Hand-filled blister cards; equipment vendor rebuilds from the SYS-07 image |
| 8 | Purchasing (wholesaler portal, CSOS on the owner laptop) | 24 h | Phone orders; paper DEA order forms for Schedule II |
| 9 | Shared drive restore (SYS-07 to SYS-02) | 48 h | ALFs re-send order sheets; payroll service repeats the prior payroll |

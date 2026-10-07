# Business Impact Analysis: Cris Santos Company Holdings | Manufacturing | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and network, finance, procurement, HR).
- **Division BIAs:** Medical Devices (focus), Medical Supply Distribution, and Engineering and Product Testing Services. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the Medical Devices division's ability to ship out-of-cycle patches "as soon as possible" for critical vulnerabilities (FD&C Act 524B(b)(2)(B)) and to meet FDA reporting clocks (21 CFR 803 and 806);
- the device cloud's contingency plan as a HIPAA business associate (45 CFR 164.308(a)(7));
- Distribution's recall and hold duties and its federal delivery commitments;
- the availability commitments in the DCC SOC 2 report (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud, network, and colocation data center, and SYS-G4 ERP and HR services. Division systems are SYS-D1 (DEMS: PLM, build and signing, MES and test stations; the P02 SSP system), SYS-D2 (the Device Connectivity Cloud), SYS-D3 (the device eQMS), SYS-D4 and SYS-D5 (Distribution's order-to-cash platform and distribution center automation), SYS-D6 (Testing LIMS, client portal, and test networks), and SYS-D7 (devices in the field). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Medical Devices about $29.6 million per day, Distribution about $17.3 million per day, and Testing about $2.5 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core output (devices, supplies, tests) or fielded devices lose connected functions | One plant, distribution center, laboratory, or service stops | Staff slowed but working |
| Regulatory | Missed FDA reporting clock, breach notice, federal contract duty, or SEC disclosure | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Plausible patient harm (infusion error, lost remote alarm path, delayed supplies for procedures) | Delayed but safe care | None |
| Reputation | National media, FDA or customer action, loss of hospital or testing clients | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 25 processes: 7 group shared services, 9 Medical Devices, 5 Distribution, and 4 Testing. 14 are High, 10 Moderate, and 1 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-G04 Wide-area network and site connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-MD01 Device connectivity and remote monitoring (DCC) | Medical Devices | High | 4 h | 2 h | 15 min |
| BP-MD05 Product security incident response and CVD intake | Medical Devices | High | 8 h | 4 h | 1 h |
| BP-DS01 Order-to-cash for hospitals and clinics | Distribution | High | 24 h | 8 h | 1 h |
| BP-DS02 Warehouse fulfillment and distribution center automation | Distribution | High | 24 h | 8 h | 1 h |
| BP-DS04 Recall, hold, and complaint handling as distributor and importer | Distribution | High | 24 h | 8 h | 4 h |
| BP-MD02 Firmware and drug library distribution | Medical Devices | High | 24 h | 8 h | 1 h |
| BP-DS03 Federal customer orders (VA and DoD) | Distribution | High | 48 h | 24 h | 4 h |
| BP-MD04 Build, sign, and release device software | Medical Devices | High | 72 h | 24 h | 4 h |
| BP-MD06 Complaint handling, MDR, and corrections and removals | Medical Devices | High | 72 h | 24 h | 4 h |
| BP-MD03 Production and final test | Medical Devices | High | 72 h | 24 h | 4 h |
| BP-MD09 Technical support to hospitals | Medical Devices | Moderate | 24 h | 8 h | 4 h |
| BP-TS02 Client portal and report delivery | Testing | Moderate | 48 h | 24 h | 4 h |
| BP-TS03 Cybersecurity testing practice | Testing | Moderate | 72 h | 24 h | 4 h |
| BP-DS05 Supplier EDI and procurement | Distribution | Moderate | 72 h | 24 h | 4 h |
| BP-MD08 Field service and depot repair | Medical Devices | Moderate | 72 h | 48 h | 24 h |
| BP-TS01 Client test execution in laboratories | Testing | Moderate | 72 h | 48 h | 24 h |
| BP-G05 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-MD07 Design and development | Medical Devices | Moderate | 120 h | 72 h | 4 h |
| BP-G07 Group procurement and supplier management | Group | Moderate | 120 h | 72 h | 24 h |
| BP-G06 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-TS04 Intercompany testing for Medical Devices submissions | Testing | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Patient safety and hospital commitments** drive the DCC (BP-MD01). Primary alarms stay at the bedside, but clinicians rely on remote views and secondary notifications, and about 1,300 hospitals hold BAAs and service commitments. The RPO of 15 minutes matches the point-in-time recovery of the DCC database.
- **The ability to fix fielded devices** drives BP-MD04 and BP-MD02. Their MTDs are longer than the DCC's, but an outage during a device incident would stop an out-of-cycle patch that 524B(b)(2)(B) expects "as soon as possible". The signing key's integrity matters more than its availability (P02 rates DEMS integrity High).
- **Regulatory clocks** drive BP-MD05, BP-MD06, and BP-DS04. They are rated High even though their MTDs are measured in hours to days, because the FDA and HIPAA clocks keep running during an outage.
- **Hospital supply** drives Distribution. Most hospitals keep 1 to 3 days of par stock, so a 24-hour MTD protects scheduled procedures.
- **Contracts more than time** drive Testing. Clients can reschedule tests, but a loss of confidentiality in the client portal or the findings vault would be Severe for reputation. That is why P02 and P01 treat Testing as a confidentiality risk, not an availability risk.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process except MES local operator accounts and the 4 acquired laboratories | A group identity outage stops all three divisions at once. Break-glass accounts per critical system are the fallback |
| WAN and colocation data center | Group | Distribution centers (ERP), plants (PLM, release repository), laboratories | Distribution's ERP is only as available as the link to the colocation data center |
| SOC facts | Group | PSIRT, Distribution recalls, SEC filing | Every notice clock in P08 depends on the SOC and the PSIRT establishing what happened |
| Build and signing (BP-MD04) | Medical Devices | DCC update service (BP-MD02); field service (BP-MD08) | No signed fix, no patch. IX-3 depends on the Plant D build server (gap 1) |
| Medical Devices products and corrections | Medical Devices | Distribution recall and hold (BP-DS04) | Distribution holds IX-3 and IX-4 stock and customer lot data needed for corrections |
| Distribution complaints | Distribution | Medical Devices eQMS (BP-MD06) | Device complaints Distribution receives on Medical Devices products must reach the manufacturer's complaint file |
| Testing of Medical Devices products | Testing | Medical Devices submissions and fixes | Testing verifies fixes and runs premarket penetration tests; independence must be documented (gap 5) |
| Supplier EDI | Medical Devices as supplier | Distribution replenishment | Same EDI gateway; an EDI outage delays Medical Devices disposables to hospitals |
| Financial close (BP-G05) | Group | Disclosure committee | A Form 8-K Item 1.05 filing needs facts from every division |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts, tested quarterly); the Plant D build server for IX-3 firmware (gap 1; no backup HSM path; P01 MD-003); one colocation data center for the distribution ERP (P01 DS-006, disaster recovery replica in provider B planned for 2027).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs, backup vault | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SYS-D2 DCC | BP-MD01, BP-MD02 | Database point-in-time recovery (15 minutes); warm standby in provider B |
| SYS-D1 build pipeline and HSMs | BP-MD04 | Pipeline defined as code; primary HSM at Plant A, backup HSM at Plant B; key ceremonies documented. Plant D software key has no backup (gap 1) |
| SYS-D1 PLM and repositories | BP-MD07 | SaaS vendor replication; nightly export to the group vault |
| SYS-D1 MES | BP-MD03 | Nightly backups at each plant; Plants D and E copies stay on site (P07 CP-9 finding) |
| SYS-D3 eQMS | BP-MD06, BP-DS04 | SaaS vendor replication; weekly export |
| SYS-D4 distribution ERP and warehouse management | BP-DS01 to BP-DS05 | Nightly backups to disk and the provider B vault; hourly log shipping |
| SYS-D6 LIMS, portal, findings vault | BP-TS01 to BP-TS04 | Daily backups; findings vault backups encrypted with a separate key |
| People | All | Cross-trained teams; PSIRT follow-the-sun rota; field engineers in every state |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and hub network
3. WAN and site connectivity
4. SOC visibility (SIEM and EDR)
5. DCC remote monitoring (warm standby in provider B)
6. PSIRT intake and triage
7. to 9. Distribution order-to-cash, warehouse fulfillment, and recall and hold
10. to 14. Device update distribution, federal orders, build and signing, complaint and MDR handling, and production
15. to 25. Hospital technical support, Testing client portal and cybersecurity practice, supplier EDI, field service, laboratory testing, financial close, design and development, procurement, payroll, and intercompany testing.

## 8. Key findings
1. **Shared services must recover first and fastest.** The group identity RTO of 1 hour was met in two tests in 2026. Every division process depends on it.
2. **The Plant D build server is a single point of failure for IX-3 fixes.** If it failed during an IX-3 incident, no signed fix could be produced until a new key is generated and trusted by fielded pumps, which IX-3 may not support without a field visit (P01 MD-003; POAM-003).
3. **Distribution is the fastest path to hospitals during a device incident.** Its lot trace data and customer lists are needed within hours for holds and customer notices, so BP-DS04 is High even though it is not a revenue process.
4. **Testing is a confidentiality business.** Its availability MTDs are long, but P01 and P02 treat the findings vault and client data as the main exposure.
5. **Notification capacity is itself a process** (BP-G02, BP-MD05, BP-MD06, BP-DS04, BP-G05). If these stop during an incident, notice clocks keep running. P08 uses out-of-band channels for this reason.

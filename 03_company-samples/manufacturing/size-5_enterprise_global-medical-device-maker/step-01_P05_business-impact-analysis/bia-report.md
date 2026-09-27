# Business Impact Analysis: Cris Santos Company | Manufacturing | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded connected medical device manufacturer, NAICS 334510) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners (interviews 2026-05-18 to 2026-06-26) | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk and technology committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, contract manufacturers, and the acquired infusion business. It feeds:
- the contingency plans for the Device Data Cloud (DDC) and the Remote Cardiac Monitoring (RCM) platform, including the HIPAA contingency plan standard for the business associate services (45 CFR 164.308(a)(7)) and its applications and data criticality analysis (164.308(a)(7)(ii)(E));
- the availability rating and recovery objectives in the DSF-MES System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the fielded-device incident runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 6 are High criticality, 9 Moderate, and 2 Low. 2 processes need recovery within 2 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 13 of them single points of failure and 2 never tested.

## 2. System and business description
Cris Santos Company designs, builds, and services connected medical devices for about 2,300 hospitals, about 5,200 physician practices, and about 900,000 consumers. It has 12,000 employees, three plants (FL-1 Florida, MN-1 Minnesota, TX-1 Texas), two R&D centers, two RCM monitoring centers, two colocation data centers (DC-1 and DC-2), and about $4.8 billion in annual revenue. The technology estate is described in `../00_company-facts.md` section 3: the DDC (SYS-01), the RCM platform (SYS-02), the Consumer Health Platform (SYS-03), the Device Software Factory (SYS-04), PLM and eQMS (SYS-05), MES and plant OT (SYS-06), ERP (SYS-07), the identity platform (SYS-08), the enterprise estate (SYS-09), about 2,400 suppliers (SYS-10), and the fielded device fleet (SYS-11). The infusion pump business and plant MN-1 were acquired in 2024 and are still being integrated.

**Design facts that bound safety impact:**
- Primary alarms always sound at the bedside monitor or pump. A DDC outage removes remote visibility and secondary notifications. It does not silence a device.
- Infusion pumps keep running on their current drug library if the update service is down.
- The CR-100 phone gateway app buffers about 24 hours of ECG, but urgent findings reach a physician only after a technician reviews them, so an RCM outage is a direct patient safety event.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day ($19.2 million per business day) and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | A tier-1 service stops for all customers, or two plants stop | One service line, one plant, or one region stops | Staff slowed but working |
| Regulatory | Missed FDA reporting deadline (21 CFR 803 or 806); missed business associate breach notice (164.410) or FTC rule deadline (16 CFR 318.4); missed SEC filing; loss of a 524B element needed for a submission | Missed contractual or documentation deadline; late internal record | Internal procedure deviation |
| Safety | Plausible patient harm (for example, an urgent arrhythmia not reported, or a compromised device update) | Clinicians lose remote visibility but bedside alarms work | None |
| Reputation | National media, analyst or ratings action, public vulnerability disclosure naming the company, or loss of health system contracts | Regional coverage; complaints from several customers | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-02 Remote cardiac monitoring (RCM) | High | 4 h | 2 h | 15 min | $2.50M |
| BP-01 Remote patient monitoring and secondary alarms (DDC) | High | 4 h | 2 h | 15 min | $0.90M |
| BP-05 Product security intake, CVD, and advisories (PSIRT) | High | 24 h | 8 h | 24 h | $0.05M |
| BP-11 Field service and technical support | Moderate | 24 h | 8 h | 4 h | $0.40M |
| BP-13 Ultrasound image archive and US-20 app services | Moderate | 24 h | 12 h | 1 h | $0.20M |
| BP-10 Order fulfillment, distribution, and UDI traceability | High | 48 h | 24 h | 1 h | $12.00M |
| BP-04 Device software build, code signing, and release | High | 72 h | 24 h | 1 h | $1.10M |
| BP-06 Complaint handling, MDR, and correction and removal reporting | High | 48 h | 24 h | 4 h | $0.10M |
| BP-03 Drug library and firmware update distribution | Moderate | 48 h | 24 h | 24 h | $0.20M |
| BP-12 Consumer companion app and HB-40 support | Low | 72 h | 24 h | 4 h | $0.15M |
| BP-07 Patient monitor and gateway production (FL-1) | Moderate | 72 h | 48 h | 24 h | $0.90M |
| BP-08 Infusion pump production (MN-1) | Moderate | 72 h | 48 h | 24 h | $0.80M |
| BP-09 ECG patch and HB-40 production (TX-1) | Moderate | 96 h | 48 h | 24 h | $0.70M |
| BP-16 Payroll, timekeeping, and HR | Moderate | 72 h | 48 h | 24 h | $0.25M |
| BP-15 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-17 Supplier management and contract manufacturing | Moderate | 120 h | 72 h | 24 h | $0.30M |
| BP-14 Design controls and regulatory submissions | Low | 168 h | 72 h | 24 h | $0.10M |

The table is in recovery priority order (`recovery_priority` in `bia.csv`).

**What drives the values:**
- **Patient safety** sets the shortest MTDs: RCM urgent-finding review (BP-02) and DDC remote monitoring (BP-01).
- **Regulatory clocks, not revenue,** make PSIRT intake (BP-05), complaint and FDA reporting (BP-06), and the build and signing pipeline (BP-04) High. An out-of-cycle fix for a critical vulnerability must be made available as soon as possible under 524B(b)(2)(B), and FDA reports are due in 5 work days (803.53), 10 working days (806.10), or 30 calendar days (803.50).
- **Cash** drives distribution (BP-10): each business day of ERP or distribution outage defers about $12 million of shipments.
- **Finished-goods buffers** keep plant outages (BP-07 to BP-09) at Moderate: about two weeks for monitors, 10 days for pumps and patches.
- **Regulation** tightens financial close (BP-15) in the quarter-end window, when its MTD drops to 48 hours.
- **Contracts** set SL-1 and SL-2 availability commitments (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **One legacy key blocks every IV-300 1.x fix (DEP-05).** The first-generation pump firmware is signed on a standalone offline workstation with one copy of the key and no backup share. If that workstation fails, no security fix can reach the 62,000 first-generation pumps until the line moves to the HSM service. This is P01 risk R-010 and POA&M item POAM-001.
2. **RCM recovery is slower than its RTO (DEP-01).** The RCM platform recovered in 3.5 hours against a 2-hour RTO in the 2026-04-18 DR test, because the technician workstation service and the call-routing integration were restored by hand. This is R-004 and POAM-026.
3. **MN-1 production has no tested restore (DEP-12).** The MN-1 MES server is a single instance on an unsupported operating system with no restore test, inside a flat network (R-020, POAM-006, POAM-009).
4. **Signing and build recovery (DEP-04, DEP-07).** Secondary HSM failover has not been tested in the last 12 months, and the build farm rebuild took 30 hours against a 24-hour RTO in the 2026-05 test (R-014, POAM-012).
5. **Single-source components and contract manufacturers (DEP-21 to DEP-23).** CMO-2 is the only source of HB-40 main boards and programs firmware outside the manufacturing PKI (R-033, POAM-013). The IV-300 wireless module and the CR-100 ECG sensor are single-source, covered by 8 and 10 weeks of safety stock.
6. **Industry-wide platforms (DEP-15).** The CR-100 phone gateway app depends on mobile operating system platforms and app stores that the company cannot replace; the workaround is company-provided phones.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Device Data Cloud | Ingestion, remote viewing, secondary alarms, EHR interfaces, update service, image archive | BP-01, BP-03, BP-13 |
| SYS-02 RCM platform | ECG ingestion, arrhythmia algorithm, technician workstations, report delivery | BP-02 |
| SYS-03 Consumer Health Platform | Companion app back end | BP-12 |
| SYS-04 Device Software Factory | Repositories, build farm, HSM signing service, artifact repository, SBOM service; legacy IV-300 signing workstation | BP-03, BP-04, BP-07 to BP-09 |
| SYS-05 PLM and eQMS | Design history and release records; complaints, MDR, and 806 records | BP-04 to BP-06, BP-11, BP-14 |
| SYS-06 MES and plant OT | MES servers and about 420 test and programming stations at FL-1, MN-1, TX-1 | BP-07 to BP-09 |
| SYS-07 ERP | Orders, shipping, UDI traceability, finance | BP-07 to BP-10, BP-15 to BP-17 |
| SYS-08 Identity platform | SSO, MFA, PAM, identity governance | All |
| SYS-09 Enterprise estate | Endpoints, SD-WAN, DC-1 and DC-2, productivity suite, ticketing, telephony | All |
| Backup and replication | DDC and RCM databases: point-in-time recovery with a 5-minute log interval and immutable daily copies in separate backup accounts; source mirror nightly to DC-1; artifact repository replicated to DC-2; HSM key backup shares with 3 custodians (not for the legacy workstation); MES configuration backups nightly at FL-1 and TX-1 (none tested at MN-1) | RPO for BP-01 to BP-04, BP-07 to BP-09 |
| Third parties | Cloud providers A and B, SaaS vendors, colocation providers, carriers, CMO-1 and CMO-2, single-source suppliers, ISAO, MSSP | As listed in `dependency-map.csv` |
| People and facilities | Plants, R&D centers, monitoring centers, data centers; RCM technicians, PSIRT, SOC, site reliability teams | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-08 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 2 | SD-WAN, DNS, and data center connectivity | 2 h | Cellular failover at plants and monitoring centers |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | MSSP tooling |
| 4 | SYS-02 RCM platform and telephony routing | 2 h target (3.5 h demonstrated) | Other monitoring center; patient and practice instructions |
| 5 | SYS-01 DDC ingestion, remote viewing, secondary alarms | 2 h | Hospital downtime procedures; device buffers backfill |
| 6 | PSIRT intake channels and eQMS | 8 h | Phone intake; controlled paper log |
| 7 | Field service ticketing and telephony | 8 h | Forwarded lines; paper log |
| 8 | DDC image archive | 12 h | Tablet queue |
| 9 | SYS-07 ERP and distribution | 24 h | Paper log for urgent orders |
| 10 | SYS-04 HSM signing service, build farm, artifact repository | 24 h (build farm 30 h demonstrated) | Secondary HSM at DC-2; plants run from cached images |
| 11 | DDC update service | 24 h | USB installs by field service |
| 12 | Consumer Health Platform | 24 h | Readings stay on the device |
| 13 | SYS-06 MES at FL-1 and TX-1, then MN-1 | 48 h (MN-1 not demonstrated) | Ship from finished goods; hold lots |
| 14 | Payroll and HR systems | 48 h | Repeat prior payroll |
| 15 | PLM, supplier portal, financial close tools | 72 h | Exported documents; filing agent |

The recovery order in `bia.csv` (`recovery_priority`) ranks the processes. This table ranks the resources those processes need.

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Legacy IV-300 signing workstation with a single key copy | P01 R-010; P02 SC-12; POAM-001 |
| RCM recovery 3.5 h against a 2 h RTO | P01 R-004; P03 G-060 and G-062; POAM-026 |
| MN-1 MES without a tested restore; flat network | P01 R-020; P02 CP-9, SC-7; POAM-006, POAM-009 |
| HSM failover untested; build farm rebuild 30 h against 24 h | P01 R-014; P02 CP-4, CP-10; POAM-012 |
| CMO-2 outside the manufacturing PKI; single-source components | P01 R-033; POAM-013 |

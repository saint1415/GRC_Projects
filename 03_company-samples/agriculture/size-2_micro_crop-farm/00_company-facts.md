# Scenario facts: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (a precision-agriculture row crop and watermelon farm) |
| Business | Combination crop farm (NAICS 111998, All Other Miscellaneous Crop Farming): watermelons, peanuts, and cotton grown in a three-year rotation, so that no single crop is a majority of crop value. Uses connected center pivots, a drip and fertigation system for watermelons, GNSS-guided tractors, one camera drone, and farm management software |
| Location | North Florida. About 420 farmed acres (owned and leased) in two parcels. **Home Farm** (about 300 acres: the shop and farm office, the pump station on the main well, about 90 acres of watermelons on drip under plastic mulch, and 3 center pivots). **River Tract** (about 120 leased acres, 9 miles away, 2 center pivots, no buildings) |
| Workforce | 7 employees: the Owner and General Manager, an Office Manager, an Irrigation and Equipment Technician, a Field Supervisor, a year-round Equipment Operator, and 2 seasonal farm workers employed under the H-2A temporary agricultural worker program (February to July) |
| Revenue | About $1.1 million a year in receipts (fictional): watermelons about 40%, peanuts about 35%, cotton about 25%. Watermelon receipts arrive in an 8-week harvest from late May to mid-July (about $9,000 per harvest day); peanut and cotton receipts arrive from September to December. Under the SBA standard of $2.5 million in average annual receipts for NAICS 111998 (13 CFR 121.201), so SBA-small |
| Sales channels | Watermelons to a regional packer-shipper under a seasonal grower agreement; peanuts to a peanut buying point; cotton ginned at a cooperative gin and marketed through a cotton marketing cooperative. The grower agreement requires notice within 24 hours of any event that could affect product safety, lot traceability, or committed loads. No direct-to-consumer sales and no card payments |
| USDA programs | Federal crop insurance on peanuts and cotton through a private crop insurance agent; Farm Service Agency farm records and acreage reports; a 2025 Natural Resources Conservation Service (NRCS) conservation contract that cost-shared soil moisture probes and variable-rate irrigation on 2 pivots. The farm keeps its own copies of these program documents |
| Food safety status | A **covered farm** under the FDA Produce Safety Rule (21 CFR Part 112) for its watermelons, because its average annual produce sales over the previous 3 years are well above the $25,000 threshold, adjusted for inflation (21 CFR 112.4(a)). Peanuts are not covered produce (rarely consumed raw, 21 CFR 112.2(a)(1)), and cotton is not food. The farm is not eligible for the qualified exemption, because nearly all of its food is sold to a packer-shipper and a buying point, not to qualified end-users (21 CFR 112.5(a)(1)). Produce Safety records (worker training, agricultural water, equipment and harvest bin cleaning, harvest log) are kept in the farm management software (SYS-01). The packer-shipper requires an annual third-party food safety audit, passed in April 2026 |
| Water use | Groundwater from the Home Farm main well and 4 pivot wells under a water use permit from the regional water management district. Flow meter records in SYS-01 support the annual water use report |
| Drones | One camera drone (RGB and multispectral) flown for crop scouting and yield imagery by the Irrigation and Equipment Technician, who holds an FAA remote pilot certificate with a small UAS rating (14 CFR 107.12). The farm does no aerial application. Crop protection is applied by ground sprayer; any aerial application is contracted to an aerial applicator that operates under its own 14 CFR Part 137 certificate, so Part 137 does not apply to the farm |
| Cybersecurity regulation | **No binding federal cybersecurity rule applies** (see P03 section 1). The farm uses **NIST CSF 2.0** as its benchmark, with **NIST SP 800-82 Rev. 3** guidance for the irrigation operational technology (OT) |
| Binding rules that reach farm data | Produce Safety Rule record requirements (21 CFR 112 Subpart O); H-2A earnings records (20 CFR 655.122(j)); Florida's data security, disposal, and breach notice duties (Fla. Stat. 501.171) |
| Not in scope | **21 CFR Part 121 (N11-R01, FSMA intentional adulteration):** Part 121 applies only to facilities required to register under FD&C Act section 415 (21 CFR 121.1), and farms do not have to register (21 CFR 1.226(b)). The farm only grows and harvests its own crops; it does no packing, manufacturing, or processing. **Reportable Food Registry (21 U.S.C. 350f):** the duty falls on a "responsible party," the person who registers a food facility (350f(a)(1)); the farm registers none. **SEC disclosure rules:** privately held. **FAR 52.204-21 and 52.204-25:** no federal contracts or subcontracts (the NRCS contract is a conservation cost-share agreement, not a procurement contract). **HIPAA:** not a covered entity. **PCI DSS:** the farm does not accept cards. **State comprehensive privacy laws:** not analyzed; the farm holds personal information only about its own workers |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (data security, disposal, and breach notification, Fla. Stat. 501.171). The samples otherwise stay federal |
| Regulatory driver labels | The vertical requirement N11-R01 does not apply (above). `regulatory_driver` columns therefore cite the benchmark as "CSF 2.0 <subcategory> (benchmark)", the OT guide as "SP 800-82r3", and binding rules by their own citation: "21 CFR 112.<section>", "20 CFR 655.122(j)", and "Fla. Stat. 501.171(<subsection>)". N11-R01 is cited only where its food defense approach is used as a voluntary checklist for the fertigation risk |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Owner and General Manager | Runs the farm and owns the LLC. Approves policies and spending; accepts Moderate, High, and Very High risks; decision maker in an incident; holds the cyber insurance policy; business owner of the yield prediction pilot (P10) |
| Office Manager | Bookkeeping, payroll, onboarding and terminations, H-2A paperwork and earnings records, USDA program documents. Designated **Security Coordinator** in writing on 2026-08-31 (part-time, about 3 hours a week). Manages the MSP; keeps the risk register, incident log, and inventory; accepts Low risks |
| Irrigation and Equipment Technician | Operates the pivots, pump station, fertigation, soil probes, tractors, GNSS guidance, and the telematics portal; administers the irrigation module of SYS-01; FAA Part 107 remote pilot. The only person who has run every pump and pivot by hand (procedure not written down) |
| Field Supervisor | Bilingual (English and Spanish). Supervises the crew; enters daily hours and Produce Safety records (harvest log, cleaning logs) on the field tablet; delivers food safety training to workers |
| Equipment Operator | Year-round tractor and sprayer operator; GNSS guidance user |
| Seasonal farm workers (2, H-2A) | Field work February to July; no system accounts |
| Managed service provider (MSP) | Part-time IT support under a block-hours contract (about 6 hours a month): help desk, patching and antivirus on the office computers, the shop firewall and Wi-Fi, productivity suite administration, and the cloud backup. 4-business-hour response time; no recovery time commitment |
| Irrigation dealer | Sold and services the pivot panels and the pump station controller; supports the pump station remotely through a cellular remote-access gateway in the pump panel |
| Equipment dealer | Tractor and sprayer service, telematics portal, remote diagnostics |
| Outside parties | Cyber insurance carrier (breach hotline, panel counsel and forensics), CPA firm, crop insurance agent, payroll service, H-2A filing agent |

## 3. Systems
| ID | System | Hosting | Holds personal or regulated data? | Notes |
|---|---|---|---|---|
| SYS-01 | Farm management software (FMIS): field records, crop plans, chemical application records, labor and daily hours module, food safety records module, yield maps, and the **irrigation control module** (remote start, stop, speed, and schedules for the 5 pivots through the pivot manufacturer's connectivity service; alarms) | Vendor SaaS, web and mobile app | Yes: Produce Safety records; daily hours records for the crew, including the H-2A workers (names, hours offered and worked, start and end times) | System of record for farm operations. MFA available but enforced only on the Owner and General Manager's account. The vendor offers a SOC 2 Type 2 report on request (first requested in August 2026, reviewed in P09) |
| SYS-02 | Productivity suite (email, files, chat), business plan | SaaS | Yes: the shared "Office" folder holds payroll exports, H-2A documents (passport and visa copies), and USDA program documents | MFA enforced for the Owner and General Manager, Office Manager, and Irrigation and Equipment Technician; the Field Supervisor's mailbox has no MFA. The Office folder is synced to the office desktop |
| SYS-03 | Endpoints | On-premises and field | Yes (cached) | 1 office desktop (Office Manager), 2 laptops (Owner and General Manager; Irrigation and Equipment Technician), 2 rugged tablets (shared field tablet; drone ground station), 3 company smartphones. The MSP patches and runs antivirus on the desktop and laptops; laptops encrypted, desktop not; tablets and phones unmanaged |
| SYS-04 | Shop network | On-premises | In transit | MSP-managed small-business firewall, one shop Wi-Fi network (password shared with dealer technicians and contractors, unchanged since 2022), and an outdoor wireless bridge to the pump station. One fixed-wireless internet line with no failover. **Flat network**: the office desktop, the Wi-Fi, and the pump station share one network |
| SYS-05 | Irrigation OT | On-premises and field | No | Pump station controller (small PLC with touchscreen) driving the main well's variable-frequency drive (VFD) pump, sand filters, 6 drip zone valves, and a fertigation injection pump; a cellular remote-access gateway in the pump panel for the irrigation dealer; 5 center-pivot control panels with cellular modems (each starts its own well pump); 12 soil moisture probes and 2 flow meters with cellular telemetry; 1 weather station. About 30 OT and IoT devices |
| SYS-06 | Equipment telematics and GNSS guidance | Equipment dealer SaaS portal and on-machine displays | Yes: operator sign-in with machine location history (geolocation) | 2 tractors with auto-steer and a sprayer with section control; RTK corrections by cellular subscription; as-applied data syncs to SYS-01. Dealer technicians have standing remote diagnostic access |
| SYS-07 | Drone and imagery | On-premises devices; imagery to SYS-09 | Incidental (people in fields may appear in images) | 1 camera drone and the ground station tablet |
| SYS-08 | Cloud backup of the productivity suite | SaaS backup service, operated by the MSP | Yes (copies of SYS-02) | Nightly copy of mailboxes and the Office folder; 30 days of versions; one MSP administrator account with a password only; **never restore-tested**. The SYS-08 subscription is resold by the MSP |
| SYS-09 | Agronomy analytics SaaS (computer-vision yield prediction) | Vendor SaaS | Farm operational and yield data | Pilot for the 2026 watermelon season; cotton boll counts planned for fall 2026 (see P10) |
| SYS-10 | Accounting and payroll | Accounting SaaS; payroll service SaaS; H-2A filing agent's portal | Yes: Social Security numbers, bank accounts, H-2A passport and visa numbers, home-country addresses, earnings records | The payroll service and the H-2A filing agent are third-party agents under Fla. Stat. 501.171(1)(h) |

**SSP system (P02):** the *Farm Management and Irrigation Control Platform (FMICP)*: SYS-01 (the farm's configuration of the FMIS and its irrigation module), SYS-02 to SYS-05, and SYS-08, with interfaces to SYS-06, SYS-07, and SYS-09.

## 4. Current security posture: early to partial
**In place today:**
- MFA on the productivity suite for the 3 office users, and on the Owner and General Manager's SYS-01 account
- MSP patching and antivirus on the office desktop and both laptops
- Laptop encryption
- Shop firewall with no inbound services exposed
- Nightly cloud backup of the productivity suite (SYS-08)
- SYS-01 vendor-managed backups
- The bank calls the Owner and General Manager back before adding any new payee
- Every pump and pivot can be run by hand at its panel (Hand-Off-Auto switches)
- Locked farm office and a locked pump station panel
- A cyber insurance policy (2025) with a breach hotline
- Produce Safety training for workers at hire, in English and Spanish

**Missing or weak, found in the 2026 assessments:**
1. No documented cybersecurity risk assessment, and nobody designated in writing to own security.
2. No written security policies.
3. The irrigation dealer has always-on remote access to the pump station controller through the cellular gateway, using one shared dealer login with no MFA. The dealer agreement has no security terms. The controller's touchscreen still uses the default PIN.
4. The crew enters daily hours and Produce Safety records in SYS-01 under one shared "field crew" login on the field tablet, so entries cannot be tied to a person.
5. MFA is not enforced in SYS-01 for the Irrigation and Equipment Technician's account (which can start and stop pivots) or for the shared field login, and SYS-01 irrigation change alerts are switched off.
6. Flat shop network: the office desktop, the Wi-Fi shared with dealer technicians and contractors, and the pump station are on one network.
7. The cloud backup has never been restore-tested, keeps only 30 days, and is administered with one password-only MSP account. SYS-01 records have never been exported. The pump station controller program exists only on the irrigation dealer's laptop.
8. No incident response plan, and no written manual irrigation procedure.
9. A former part-time bookkeeper who left in January 2026 still had an active productivity suite account with an automatic forwarding rule to a personal address.
10. Nobody reviews SYS-01, productivity suite, or firewall logs.
11. No security awareness training, and no Spanish-language security guidance.
12. No inventory of devices, OT, or where personal data lives (including operator geolocation in SYS-06, which is personal information under Fla. Stat. 501.171(1)(g)1.a.(VII)). Dealer technicians have standing access to the telematics account.
13. The office desktop is not encrypted, and it holds a synced copy of the H-2A files.
14. The yield prediction pilot (SYS-09) started under click-through terms that let the vendor use farm imagery and yield data to improve its models. There is no approved-tools list for AI.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 benchmark | NIST CSF 2.0 (all 106 subcategories), with SP 800-82 Rev. 3 applied to the OT subcategories. Also assessed row by row: the Produce Safety Rule record requirements (21 CFR 112 Subpart O), H-2A earnings records (20 CFR 655.122(j)), and Fla. Stat. 501.171. N11-R01 documented as not applicable |
| P08 incident | Ransomware on farm-management and irrigation control systems: a phishing email to the Office Manager during watermelon harvest leads to ransomware on the office computers and the synced Office folder, theft of payroll and H-2A files, and misuse of a stolen SYS-01 password to reach the irrigation module. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Availability, as a self-assessment used to answer the packer-shipper's 2026 grower security and continuity questionnaire; plus a review of the SYS-01 vendor's SOC 2 Type 2 report. The farm is not a service organization |
| P10 AI | Computer-vision crop yield prediction (AI-001) from drone imagery, piloted on watermelons in the 2026 season |
| Cloud | SaaS plus one cloud workload: the MSP-operated cloud backup (SYS-08). Vendor-agnostic |

**Why the registry defaults fit this size.** The registry's primary system, incident, and AI use case were kept. At this size the "irrigation control system" is the SYS-01 irrigation module plus a single pump station controller, not a SCADA system, so the P08 ransomware lands on the office computers and reaches irrigation through a stolen SYS-01 password and the dealer's remote gateway. The yield model is a vendor SaaS pilot on one crop.

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis with the MSP (end of watermelon harvest; H-2A workers on site until 2026-07-31) |
| 2026-08-10 to 2026-08-13 | Control assessment by an independent consultant (OT tests on 2026-08-12, outside irrigation run times) |
| 2026-08-31 | Deliverables approved by the Owner and General Manager |

## 7. Facts added while building the deliverables
| Topic | Added fact | Used in |
|---|---|---|
| Former bookkeeper account | Found active on 2026-07-21 during the risk assessment, with an automatic forwarding rule to a personal address. Disabled that day. The 41 messages forwarded after her departure were reviewed: none contained personal information as defined in Fla. Stat. 501.171(1)(g). The Office Manager documented that determination on 2026-07-24 | P01, P03, P07 |
| Pump station gateway | P07 testing on 2026-08-12 found the cellular gateway's web administration page reachable from the internet with the manufacturer's default password. The irrigation dealer changed the password and turned off internet-facing administration on 2026-08-14 | P01, P04, P07 |
| Cyber insurance | The policy has a 24x7 breach hotline and panel vendors (breach counsel, forensics). It requires prompt notice and use of panel vendors | P08 |
| MSP contract | Block of about 6 hours a month; covers the desktop, 2 laptops, firewall, Wi-Fi, productivity suite administration, and SYS-08. 4-business-hour response time; no recovery commitment; no incident notice term | P02, P04, P05, P07 |
| Finances and payroll | An operating line of credit and cash cover about 60 days of expenses. Payroll runs weekly through the payroll service | P01, P05 |
| Grower questionnaire | The packer-shipper added a grower security and continuity questionnaire to its 2026 grower agreement renewal. Response due 2026-10-15 | P09 |
| People affected by a records breach | The farm holds personal information on about 25 people (current staff, former staff, and H-2A workers from the last 3 seasons). No customer personal data | P01, P08 |
| Past events | In 2025 a phishing email led to a reset of the Owner and General Manager's email password (MFA was enabled afterwards), and the field tablet was lost in a field for 2 days. Neither was recorded | P01, P03 |
| Assessor | The P07 assessor is an independent consultant with OT experience, not involved in the risk assessment or the gap analysis and operating no control | P07 |
| FMIS vendor SOC 2 report | Requested 2026-08-03, received 2026-08-18, reviewed 2026-08-20. Type 2, unmodified opinion, 12 months ending 2026-03-31, Security and Availability. Stated RTO 8 hours and RPO 1 hour. Cloud hosting and the pivot manufacturer's connectivity service are carved-out subservice organizations. One exception (a skipped quarterly access review for vendor database administrators). Incident notice "without undue delay," no time frame; no bridge letter provided | P02, P04, P05, P09 |
| Yield prediction pilot | Signed up in April 2026 under click-through terms. 11 weekly flights from 2026-05-04 to 2026-07-13 over 4 watermelon fields (an established seedless variety on 60 acres and a new seedless variety on 30 acres). The vendor account uses a password only. Estimates are copied into the harvest plan by hand; no connection to SYS-01 or irrigation | P10 |
| Public AI chatbots | Staff interviews found no AI tool in use other than SYS-09, apart from occasional use of free public chatbots by the Office Manager to draft letters, with no personal information entered (per interview). Listed as AI-002 | P10 |

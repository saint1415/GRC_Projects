# Scenario facts: Cris Santos Company | Chemical | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a statute, regulation, or NIST publication, the citation is given. Regulatory text was read from eCFR (point-in-time 2026-09-23), the Federal Register, uscode.house.gov, and cisa.gov on 2026-09-26.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (specialty chemical formulator and packager) |
| Business | Blends and packages specialty chemical products (water treatment formulations, cleaning and process chemicals) for industrial customers and distributors, including toll blending and private-label packaging. Primary industry NAICS 325998, All Other Miscellaneous Chemical Product and Preparation Manufacturing |
| Location | Florida. One inland plant on a 14-acre industrial site: bulk tank farm, **Blend Hall A** (eight jacketed blend tanks run by the DCS), **Blend Hall B** (small manual batches), a packaging hall (drum, tote, and pail lines), a truck loading and unloading rack, a rail siding, a quality control laboratory, a warehouse, and offices. Raw materials arrive by rail and truck. There is no marine transfer, dock, or waterfront |
| Workforce | 162 employees: 64 production (blend operators on three shifts), 22 packaging, 18 warehouse and shipping, 12 maintenance and instrumentation (including 2 instrument and electrical technicians), 10 quality and laboratory, 8 engineering and EHS, 10 sales and customer service, 18 general and administrative (finance, HR, purchasing, and a 3-person IT team) |
| Revenue | $74 million a year (fictional). The SBA size standard for NAICS 325998 is 650 employees (13 CFR 121.201), so the company is SBA-small |
| Operations | Blending runs 24 hours a day, Monday to Friday, with weekend packaging overtime. About 420 active formulations and 1,150 packaged SKUs. About 35 batches and 25 outbound truckloads a day |
| Customers | About 600 business customers in the Southeast. The largest private-label customer (about 18% of revenue) sent a supplier security questionnaire in 2026 (see P09) |
| Regulated inventory | See the table below. Maximum intended inventories are the limits written into the RMP safety information (40 CFR 68.48(a)(2)) and the tank level alarms |
| CFATS status | The plant holds 50% hydrogen peroxide, a CFATS chemical of interest. The company filed a Top-Screen in 2008, was assigned a risk tier, and operated under an approved CFATS Site Security Plan until the statutory authority expired on **July 28, 2023** (CISA CFATS page, read 2026-09-26; 6 U.S.C. 621-629 shown as omitted at uscode.house.gov). CFATS has **not been reauthorized** as of 2026-09-26. CISA states it cannot enforce CFATS or require facilities to implement their Site Security Plans. The company kept most physical measures and treats RBPS 8 as a **voluntary benchmark** (P03) |
| EPA RMP status | **Covered.** The aqueous ammonia process holds more than the threshold quantity (math below). **Program 2** (40 CFR 68.10(k)): Program 1 is not available because the 2024 worst-case release analysis reaches public receptors (68.10(j)(2)), and Program 3 does not apply because NAICS 325998 is not in the 68.10(l)(1) list and the process is not covered by OSHA PSM (68.10(l)(2)). **Non-responding stationary source** (68.90(b)): employees evacuate and the county fire rescue hazardous materials team responds. RMP five-year update submitted 2024-03-18. Compliance audit completed 2025-06-12 |
| OSHA PSM status | **Not covered** (29 CFR 1910.119(a)(1)). No chemical is at a listed concentration and threshold (math below) |
| Not in scope | USCG MTSA cybersecurity rule (33 CFR Part 101 Subpart F): applies only to facilities required to have a security plan under 33 CFR Part 105 (101.605(a)); the plant has no marine transfer. CIRCIA: proposed rule only, not in effect; as proposed, the company would be below the SBA size criterion and the CFATS sector criterion is moot while CFATS is lapsed. EAR: the company ships only to U.S. customers and holds no controlled technology. Federal contracts: none. SEC rules: privately held |
| Regulatory driver IDs | **C-CHEMICAL-R01** (CFATS RBPS 8, voluntary benchmark), **C-CHEMICAL-R02** (USCG MTSA rule, not applicable), **C-CHEMICAL-R03** (CIRCIA, proposed). EPA RMP (40 CFR Part 68), CERCLA and EPCRA release reporting (40 CFR 302.6, 355.40-355.43), and the OT benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) are cited directly because the vertical registry has no ID for them |
| State law approach | Florida law is cited only where unavoidable: breach notice for employee personal information (Fla. Stat. 501.171). The samples otherwise stay federal |

### Regulated inventory and threshold math

| Chemical | Storage | Maximum intended inventory | EPA RMP (40 CFR 68.130) | OSHA PSM (29 CFR 1910.119 App. A) | CFATS App. A (legacy) |
|---|---|---|---|---|---|
| Aqueous ammonia, 29% | One 12,000-gal tank (level limit 11,000 gal), piped to four Blend Hall A tanks | 11,000 gal x 7.50 lb/gal = 82,500 lb of solution; 82,500 x 0.29 = **23,925 lb of ammonia** | Listed as "Ammonia (conc 20% or greater)", TQ 20,000 lb. 23,925 lb is above the TQ, so the process is covered. The partial-pressure exclusion in 68.115(b)(1) is not available because the supplier SDS vapor pressure is far above 10 mm Hg. The whole solution weight (82,500 lb) would also exceed the TQ, so the conclusion does not depend on the counting method | Listed only as "Ammonia solutions (>44% ammonia by weight)", TQ 15,000 lb. 29% is below 44%: **not covered** | Not the basis of the legacy tiering |
| Hydrogen peroxide, 50% | Two 4,000-gal tanks (combined level limit 7,000 gal) | 7,000 gal x 10.0 lb/gal = 70,000 lb of solution; 35,000 lb of hydrogen peroxide | Not listed | Listed only at "52% by weight or greater", TQ 7,500 lb. 50% is below 52%: **not covered** | Listed for theft and diversion (explosives precursor) at a minimum concentration of 35%, STQ 400 lb (72 FR 65396, Nov. 20, 2007). Far above the STQ: this is why a Top-Screen was filed |
| Hydrochloric acid, 31.5% | One 10,000-gal tank | About 97,000 lb of solution | Listed only at "conc 37% or greater": **not covered** | Listed only as anhydrous: **not covered** | Not relevant |
| Sulfuric acid, 93% | One 6,000-gal tank | About 91,000 lb | Only oleum is listed: **not covered** | Only oleum 65-80% is listed: **not covered** | Not relevant |
| Sodium hypochlorite, 12.5% | Two 8,000-gal tanks | About 160,000 lb | Not listed | Not listed | Not relevant |
| Isopropyl alcohol, 99% (flash point below 100 F) | Totes in the flammables room, inventory cap of 4 totes | 4 x 275 gal x 6.55 lb/gal = **7,205 lb** | Not listed | Flammable liquid rule (a)(1)(ii) needs 10,000 lb or more in one location: **not covered** while the 4-tote cap holds | Not relevant |

**Two limits the company must keep** (both enforced by management of change, POL-01 4.11): hydrogen peroxide must not be bought at 52% or higher, and isopropyl alcohol must stay at or under 4 totes. Either change would bring OSHA PSM and RMP Program 3 into play.

## 2. People (role titles only)

| Role | Security, process safety, and compliance duties |
|---|---|
| Majority owner and President (CEO) | Approves the security budget; accepts High and Very High risks |
| Vice President of Operations (VP Operations) | Executive owner of the security program; accepts Moderate risks; approves policies |
| Plant Manager | RMP qualified person with overall responsibility for the risk management program (40 CFR 68.15(b)); owner of the process control system; incident commander for process emergencies |
| EHS Manager | RMP compliance (hazard review, audits, emergency response coordination under 68.93, notification exercises under 68.96(a)); CERCLA and EPCRA release reporting; former CFATS facility security officer; owns physical security |
| IT Manager | Security officer for IT and OT (part-time security and compliance duties); runs the identity provider, endpoints, networks, cloud tenant, and backups; leads a systems administrator and a help desk technician |
| Controls Engineer | The only OT engineer: DCS, batch management system, SIS, PLCs, and the OT network. Approves DCS and SIS configuration changes |
| Instrument and Electrical Technicians (2) | Field instruments, SIS proof tests, PLC maintenance |
| Process Engineer | Formulations and master recipes; management of change coordinator; business owner of the AI-001 process-optimization model (P10) |
| Quality Manager | Laboratory and LIMS; certificates of analysis; batch release |
| Shift Supervisors (3) | Run blending on each shift; first responders to alarms; authorize manual operations |
| HR Manager | Onboarding, transfers, terminations, background checks |
| Controller | Finance, insurance, and the ERP business owner |
| Customer Service Manager | Customer communications, including the P09 questionnaire |
| DCS integrator (contracted) | Remote and on-site support of the DCS and batch management system |
| Data science contractor | Built AI-001 with the Process Engineer |

## 3. Systems

| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Distributed control system (DCS) | On premises, control room and Blend Hall A | Setpoints, alarm limits, process data | Redundant controllers and server pair; 3 operator stations; 1 engineering workstation (EWS). Controls the tank farm, the aqueous ammonia process, and Blend Hall A. Two major releases behind the vendor's current release |
| SYS-02 | Batch management system | On premises (DCS server pair) | About 420 master recipes (trade secrets) | Recipe management and batch execution. Receives production orders from SYS-08 through the order interface in SYS-10 |
| SYS-03 | Safety instrumented system (SIS) | On premises, separate safety controller | Safety logic | Independent logic solver: aqueous ammonia tank high level and high pressure trips, remote isolation valve, ammonia gas detection, hydrogen peroxide tank high-temperature trip. Proof-tested yearly |
| SYS-04 | Packaging line PLCs (4) and the truck loading rack automation | On premises | Load records | Loading rack PLC with meters, ground verification, and a driver card reader |
| SYS-05 | Process historian | On premises, **dual-homed** on the business and control networks | 3 years of process data | Feeds operator reports and the replica used by AI-001 |
| SYS-06 | OT network and IT/OT firewall | On premises | n/a | Control network and supervisory network behind one firewall. Rules include "any" rules for the integrator and the historian |
| SYS-07 | Remote access | On premises and SaaS | n/a | Employees: VPN with MFA. DCS integrator: a **remote desktop tool installed on the EWS**, always on, one shared account, no MFA |
| SYS-08 | Enterprise resource planning (ERP) | Vendor SaaS | Orders, inventory (including hydrogen peroxide), bills of materials, customer data | A critical business system in RBPS 8 terms. The vendor has a SOC 2 Type 2 report (reviewed in P09) |
| SYS-09 | Laboratory information management system (LIMS) | Cloud tenant (SYS-10) | QC results, certificates of analysis | |
| SYS-10 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Formulation data, historian replica | Hosts the LIMS, the order interface service, the historian replica and analytics store, the AI-001 model service, the file shares, the backup vault, and the log workspace |
| SYS-11 | Identity provider (single sign-on and MFA) and the on-premises directory | SaaS and on premises | Identities | Covers the SaaS apps, the cloud console, and the VPN. The OT systems use **separate local accounts** |
| SYS-12 | Productivity suite (email, files, chat) | SaaS | Incidental | |
| SYS-13 | Endpoints | On premises | Incidental | 118 office laptops and desktops with EDR; 16 OT workstations (HMIs, EWS, historian clients) **without EDR** |
| SYS-14 | Physical security systems | On premises | Video, badge records | Badge access, 42 networked cameras, and a video recorder on the business network. Legacy CFATS measures |
| SYS-15 | HR and payroll | Vendor SaaS | Employee PII | Background check results and payroll data for 162 employees |
| SYS-16 | AI-001 process-optimization model | Cloud tenant (SYS-10) | Historian replica | Pilot on 2 Blend Hall A tanks since May 2026 (see P10) |

**SSP system (P02):** the *Process Control and Batch Management System (PCBMS)*: SYS-01, SYS-02, SYS-03, SYS-05, the OT network and IT/OT firewall (SYS-06), the integrator and employee remote access paths into OT (SYS-07), and the 16 OT workstations in SYS-13, with interfaces to the ERP order interface and historian replica in SYS-10.

## 4. Current security posture: partially compliant

**In place today:**
- An IT/OT firewall between the business and control networks (rules too broad; see gap 2)
- Redundant DCS controllers and servers; UPS on the DCS, SIS, and control room
- An independent SIS for the aqueous ammonia and hydrogen peroxide tanks, proof-tested yearly (last test 2025-10-21)
- MFA through the identity provider for email, the ERP, the cloud console, and employee VPN
- EDR on office endpoints
- Nightly DCS configuration exports (stored on the EWS; see gap 8)
- Perimeter fence, badge access, cameras, and a day-shift gate guard (kept from the CFATS Site Security Plan)
- Background checks at hire (kept from CFATS RBPS 12 practice; terrorist-ties vetting through CISA stopped with the lapse)
- Annual security awareness training for office staff
- RMP Program 2 elements: hazard review (2024), operating procedures, training, maintenance, 2025 compliance audit, annual coordination with county fire rescue, and a 2025-11-06 notification exercise
- A written management of change (MOC) procedure for process chemistry and equipment
- Legacy CVI kept in a locked cabinet and a restricted folder
- Daily cloud backups of the LIMS and file shares, copied to a second region

**Missing or weak, found in the 2026 assessments:**
1. No OT asset inventory. The newest OT network diagram is from the 2019 CFATS Site Security Plan.
2. The historian is dual-homed on the business and control networks, and the IT/OT firewall has "any" rules for the DCS integrator and the historian.
3. The DCS integrator has always-on remote access through a remote desktop tool on the EWS, with one shared account, no MFA, no session approval, and no session logging.
4. Operators share one account per HMI, and engineers share one DCS engineering account. There are no unique IDs in the DCS.
5. DCS, SIS, PLC, and recipe changes are outside the MOC procedure. There is no configuration baseline or change log, and the Process Engineer can release recipe changes without a second approval.
6. OT patches are applied only at the annual turnaround, the DCS is two major releases behind, and nobody monitors OT vulnerabilities or CISA's Known Exploited Vulnerabilities (KEV) catalog.
7. No security monitoring of the OT network. DCS, SIS, and firewall logs are not collected.
8. DCS backups sit on the EWS and one USB drive in the control room. They have never been restore-tested, there is no offline copy, and the SIS program copy has never been compared with the running logic.
9. The incident response plan covers office IT only. Cyber causes are not in the RMP hazard review or the emergency action plan, and there has never been an OT tabletop exercise.
10. Removable media are used freely on HMIs for recipe files and vendor updates. There is no scanning station.
11. Operators, maintenance staff, and contractors get no cybersecurity training.
12. DCS local accounts and the loading rack driver cards are not part of terminations or access reviews. Two active DCS accounts and one driver card belong to people who have left.
13. Legacy CVI, the old Site Security Plan, and formulation files sit in a shared folder open to 40 users. There is no data classification policy.
14. Third parties: the DCS integrator and data science contractor agreements have no security clauses, the ERP vendor's SOC 2 report has never been reviewed, and the AI-001 pilot started without a risk assessment or an approved-tools list.
15. The SIS keyswitch was found in the remote program position, and SIS engineering software is installed on the DCS EWS (found during P07 testing on 2026-08-12).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P02 SSP | Process Control and Batch Management System (PCBMS), categorized High (integrity) under FIPS 199 |
| P03 regulation | Primary: CFATS RBPS 8, 6 CFR 27.230(a)(8), as a **voluntary benchmark** (authority lapsed). OT benchmark: NIST CSF 2.0 with SP 800-82 Rev. 3. Secondary (binding): EPA RMP Program 2, 40 CFR Part 68, for the elements that touch the control system |
| P04 cloud | The cloud tenant (SYS-10) and the SaaS services, plus the one-way data path from OT. Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| P05 BIA | 11 business processes (BP-01 to BP-11). BP-01 controlled blending: MTD 24 h, RTO 12 h, RPO 24 h for DCS configuration |
| P07 assessment | 22 controls on the PCBMS; testing on 2026-08-12 during a planned Blend Hall A maintenance day |
| P08 incident | Intrusion into the DCS through the integrator's remote access path: setpoint and alarm changes on the aqueous ammonia process, then ransomware on the historian and HMIs |
| P09 SOC 2 | The company is not a service organization. (a) Security-only (CC1-CC9) self-benchmark to answer the largest private-label customer's questionnaire; (b) review of the ERP vendor's SOC 2 Type 2 report |
| P10 AI | AI-001 process-optimization model (advisory setpoint recommendations, 2-tank pilot). AI-002 enterprise generative AI assistant (proposed). AI-003 public chatbots (prohibited for formulations) |
| Cloud | Vendor-agnostic. Services are described by category |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork (plant walkthrough 2026-07-15) |
| 2026-08-10 to 2026-08-14 | Control assessment fieldwork (OT testing 2026-08-12 during a planned Blend Hall A maintenance day) |
| 2026-08-24 | SOC 2 security self-benchmark completed |
| 2026-08-26 | AI risk assessment completed |
| 2026-09-04 | Deliverables approved by the VP Operations (Moderate and below) and the CEO (High) |

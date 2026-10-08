# Business Impact Analysis: Cris Santos Company | Healthcare and Public Health | Mid-Market

**Organization:** Cris Santos Company, Inc. (112-bed community acute-care hospital with an off-campus outpatient center) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Information Security Manager with the vCISO, the Director of Emergency Management, and the process owners named in `bia.csv` | **Fieldwork:** 2026-06-22 to 2026-07-17 | **Approved:** Chief Operating Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit of the hospital: the emergency department (ED), the inpatient and critical care units, women's services, surgical services, pharmacy, laboratory, imaging and cardiology, patient access, revenue cycle, health information management (HIM), facilities, the outpatient center, the affiliated practice program, and enterprise support functions. It rates 20 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and patient safety.

The results feed:
- the HIPAA contingency plan and its applications and data criticality analysis (45 CFR 164.308(a)(7), including (7)(ii)(E));
- the hospital emergency preparedness program required by 42 CFR 482.15 (section 7 below);
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria in the SOC 2 readiness assessment for the affiliated practice program (P09).

## 2. System and business description
The hospital has 112 licensed beds, a 32-bed ED with about 115 visits a day, 6 operating rooms and 2 endoscopy suites, a catheterization lab, a laboratory with a blood bank, imaging at the main campus and the outpatient center 9 miles away, and a pharmacy with 36 automated dispensing cabinets. It is a primary stroke center and receives STEMI patients. Clinical and business work runs on the Hospital EHR and Clinical Systems (HECS) described in the SSP (P02): the vendor-hosted EHR, the identity provider, the PACS and RIS, the 5-account cloud landing zone, the on-premises data center (LIS, dispensing cabinet, pump, monitoring, fetal surveillance, and cardiology servers), the networks, 960 workstations and laptops, about 1,650 networked medical devices, and MSSP-monitored security operations. Building OT (SYS-09) and clinical communications (SYS-11) share the campus network. The two nearest hospitals that can receive diverted patients are 11 and 14 miles away. See `../00_company-facts.md` sections 1, 3, and 7.

## 3. Impact categories and values
Dollar values are scaled to $100.0 million in annual revenue, about $274,000 a day: inpatient care about $142,000 a day, ED about $38,000, imaging and laboratory about $38,000 (of which the outpatient center about $25,000), and outpatient surgery about $48,000 per operating day. About $1.9 million in expected collections moves through the clearinghouse each week (about $380,000 per business day).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $150,000 in lost revenue or extra cost, or more than $1 million of cash delayed | $30,000 to $150,000 | Less than $30,000 |
| Operations | The ED must go on diversion, or a care unit cannot continue safely | One department or site stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory | EMTALA exposure, reportable breach, or a condition-of-participation finding (for example 482.15 or 482.24) | Missed reporting, documentation, or contractual deadline | Internal policy deviation |
| Patient safety | Plausible serious harm (missed allergy, wrong dose, missed alarm, delayed stroke or STEMI care, transfusion error) | Delayed but safe care | None |
| Reputation | Regional media coverage, loss of community or EMS confidence, or loss of affiliated practices | Patient complaints or online reviews | Internal only |

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered plus extra labor (overtime, agency staff, runners, back-entry) over the MTD. Recovery assumptions came from the process owners: about 40% of diverted ambulance patients would have been admitted and do not return, about 50% of cancelled elective cases are rescheduled, and about 60% of deferred outpatient studies are rebooked. For claims (BP-13), the loss is overtime, denials, and interest on the credit line; the delayed cash is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-10 Clinical communications | Enterprise | High | 1 | 0.5 | 24 | $2,000 |
| 2 | BP-03 Critical care and continuous patient monitoring | Critical care and telemetry | High | 2 | 1 | 24 | $6,000 |
| 3 | BP-01 Emergency department care | ED | High | 4 | 2 | 0.25 | $30,000 |
| 4 | BP-02 Inpatient nursing care and medication administration | Nursing | High | 4 | 2 | 0.25 | $25,000 |
| 5 | BP-06 Pharmacy order verification and dispensing | Pharmacy | High | 4 | 2 | 0.25 | $12,000 |
| 6 | BP-07 Laboratory testing and blood bank | Laboratory | High | 4 | 2 | 0.25 | $10,000 |
| 7 | BP-05 Labor, delivery, and newborn care | Women's services | High | 4 | 2 | 0.25 | $8,000 |
| 8 | BP-04 Surgical services and anesthesia | Surgical services | High | 4 | 2 | 0.25 | $15,000 |
| 9 | BP-08 Diagnostic imaging and catheterization lab | Imaging and cardiology | High | 4 | 2 | 1 | $20,000 |
| 10 | BP-11 Building and clinical OT monitoring | Facilities | High | 4 | 2 | 168 | $25,000 |
| 11 | BP-09 Registration, bed management, and transfer center | Patient access | High | 8 | 4 | 1 | $30,000 |
| 12 | BP-20 Outpatient center services | Outpatient center | Moderate | 24 | 8 | 1 | $15,000 |
| 13 | BP-15 Supply chain and sterile processing | Materials management | Moderate | 24 | 12 | 24 | $20,000 |
| 14 | BP-17 Affiliated practice EHR services | Physician services | Moderate | 24 | 8 | 0.25 | $10,000 |
| 15 | BP-12 Health information management and release of information | HIM | Moderate | 72 | 48 | 24 | $15,000 |
| 16 | BP-13 Claims submission and clearinghouse connectivity | Revenue cycle | Moderate | 72 | 48 | 24 | $60,000 (plus $1.14 million cash delayed) |
| 17 | BP-16 Public health and regulatory reporting | Quality and infection prevention | Moderate | 72 | 48 | 24 | $2,000 |
| 18 | BP-14 Patient billing and payment posting | Revenue cycle | Low | 120 | 72 | 24 | $15,000 |
| 19 | BP-18 Payroll, HR, credentialing, and privileging | Enterprise | Low | 120 | 72 | 24 | $25,000 |
| 20 | BP-19 Quality reporting and analytics | Enterprise | Low | 168 | 120 | 24 | $5,000 |

**Summary:** 11 High, 6 Moderate, and 3 Low processes (20 in total). The sum of estimated losses at each process's MTD is $350,000.

**Enterprise-wide scenario.** If the EHR, the campus network, and the on-premises data center were all down for 72 hours with 48 hours of ambulance diversion (for example, ransomware), unrecovered revenue would be about $370,000: about $241,000 from diverted ambulance patients (about 80 diverted, about 32 of whom would have been admitted), $73,000 from cancelled elective surgery, $46,000 from deferred outpatient imaging and laboratory work, and about $9,000 of affiliated practice service credits. Extra labor (agency nurses, overtime, runners, back-entry) adds about $280,000, and about $1.14 million of cash would be delayed. Incident response and breach notification costs come on top (see P01 R-001 and R-002). The larger cost is not money: a hospital on diversion for 2 days sends stroke and STEMI patients 11 more miles.

**What drives the values:**
- **Patient safety and EMTALA drive BP-01 to BP-08.** The ED must screen and stabilize anyone who comes to it, whatever the state of IT (42 CFR 489.24). The 4-hour MTD is the point where the CNO, the ED Medical Director, and the administrator on call decide whether to ask county EMS to divert ambulances. EMTALA allows a hospital in "diversionary status" (one that does not have the staff or facilities to accept more emergency patients) to direct an ambulance elsewhere, but an ambulance that disregards the instruction and arrives on hospital property has brought the patient to the ED (489.24(b)).
- **BP-10 and BP-03 come first.** Codes, rapid responses, alarms, and diversion calls all depend on phones and the monitoring network, which ride on the campus network. Without them, the bedside becomes the only place an alarm is heard.
- **The hourly extract sets the RPO for BP-01, BP-02, BP-04 to BP-07.** The downtime workstations print from an hourly extract, but the BIA asks for 15 minutes because medication and blood product decisions change minute to minute. The EHR vendor's RPO of 15 minutes meets that need; its RTO of 12 hours does not (finding 1).
- **Cash flow, not time, drives BP-13.** Payers accept late claims within their filing limits, but about $380,000 of collections is delayed each business day.
- **BP-11's RPO of 168 hours** reflects that OT configurations change rarely; a weekly configuration export is enough. No export is taken today (finding 4).

## 5. Key findings
1. **EHR vendor recovery objectives do not meet the BIA.** The EHR vendor's SOC 2 system description states RTO 12 hours and RPO 15 minutes. The BIA needs RTO 2 hours for BP-01, BP-02, and BP-04 to BP-08. The downtime workstations make the 4-hour MTD survivable in read-only mode, but beyond 4 hours the ED decision turns to diversion. Action: negotiate recovery terms at renewal and extend the downtime procedures to cover a 72-hour outage (P01 R-005; P09 vendor review).
2. **Hospital-managed recovery is unproven.** The LIS, dispensing cabinet server, pump server, monitoring gateway, fetal surveillance server, and cardiology system run in the on-premises data center and have never been restore-tested; there is no IT disaster recovery plan (EV-021, EV-028). Their 1- to 2-hour RTOs are targets, not demonstrated capabilities (P01 R-003; P07 CP-4, CP-10).
3. **One campus network carries clinical care, phones, alarms, and building systems.** A single attack on the network hits BP-01, BP-03, BP-05, BP-10, and BP-11 at once (EV-014, EV-016; P01 R-001, R-007, R-016).
4. **No OT configuration backups.** The building automation and nurse call vendors have not confirmed that they keep configuration backups, so the BP-11 RPO is unsupported today.
5. **The emergency plan has no cyber hazard.** The 482.15 hazard vulnerability analysis ranks "IT outage" as short and low, and there are no diversion criteria for an IT outage (EV-030; section 7).
6. **The affiliated practices depend on the hospital's recovery.** 18 practices lose their EHR whenever the hospital does. The service agreement promises practice access within 8 hours of EHR availability, which has never been tested (P09).

## 6. Resource requirements
| Resource | Description | Supports | Recovery method today |
|---|---|---|---|
| SYS-01 EHR (vendor-hosted) | System of record, eMAR, order entry, pharmacy, surgery, labor and delivery, patient accounting, portal, ambulatory module for the practices | BP-01 to BP-09, BP-12 to BP-15, BP-17, BP-20 | Vendor replication (RPO 15 min, RTO 12 h per SOC 2); downtime workstations |
| SYS-02 Identity provider | Single sign-on and MFA; directory synchronization | All | SaaS; break-glass accounts exist for the cloud only |
| SYS-03 PACS and RIS (workloads account) | Image storage, reading, AI triage (AI-002) | BP-08, BP-20 | Daily backups to the backup account; never restore-tested |
| SYS-04 Landing zone | Interface engine, data warehouse, file services, backup vault | BP-07, BP-08, BP-12, BP-13, BP-16, BP-17, BP-19 | Daily write-once backups (35 days); interface engine never restore-tested |
| SYS-05 On-premises data center | LIS, dispensing cabinet server, pump server, monitoring gateway, fetal surveillance server, cardiology system, nurse call server, directory, file and print, downtime extract server | BP-02, BP-03, BP-05 to BP-08, BP-11 | Nightly backup to the appliance, replicated to the backup account; never restore-tested |
| SYS-06 Networks | Campus core and Wi-Fi; outpatient center SD-WAN with two carriers; two internet carriers at the campus | All | Redundant carriers; no documented network rebuild procedure |
| SYS-07 Endpoints | 960 workstations and laptops, 380 clinical smartphones, 120 barcode scanners, 12 downtime workstations | All | Standard images; 20 pre-imaged spare laptops |
| SYS-08 Medical devices | About 1,650 networked devices | BP-01 to BP-08, BP-20 | Standalone operation; manufacturer support |
| SYS-09 Building and clinical OT | Building automation, nurse call, infant protection, medical gas alarms, pneumatic tube, generator monitoring | BP-05, BP-11 | Local controllers; no configuration export |
| SYS-10 Security operations | SIEM (MSSP), EDR, email security | Recovery validation | MSSP platform |
| SYS-11 Clinical communications | VoIP, smartphones, paging, mass notification, analog lines, EMS radio | BP-01, BP-03, BP-10 | Analog lines and radios only in the ED and house supervisor office |
| SYS-12 External connections | Clearinghouse, HIE, reference laboratory, teleradiology, telestroke, public health | BP-07, BP-08, BP-13, BP-16 | Vendor-operated |
| People and facilities | Nurses, contracted physicians, ancillary staff, IT and security team (20), MSSP, facilities engineers; main campus and outpatient center | All | Call-in list; agency staff; Hospital Incident Command System |

## 7. Emergency preparedness linkage (42 CFR 482.15)
The hospital is a Medicare-participating hospital, so the emergency preparedness condition of participation applies (42 CFR 482.15, text verified on eCFR, 2026-09-23 version). The rule is all-hazards and does not use the word "cyber," but its risk assessment, strategies, medical documentation, and communication elements are exactly where a prolonged EHR or network outage belongs. The BIA supplies the content the program is missing today:

| 482.15 requirement (verified text, summarized) | What this BIA supplies | Status |
|---|---|---|
| (a)(1) Plan based on a documented facility-based and community-based risk assessment using an all-hazards approach | Cyber hazards (ransomware, EHR vendor outage, network loss, medical device compromise, OT compromise) added with the P01 risks R-001, R-003, R-005, R-007, and R-016 | Hazards added in this BIA; hazard vulnerability analysis update due 2026-12-15 |
| (a)(2) Strategies for addressing the events identified by the risk assessment | Workarounds for all 20 processes in `bia.csv`; diversion decision at the 4-hour ED MTD | Written here; IT outage annex due 2026-12-15 |
| (a)(3) Patient population, services the hospital can provide in an emergency, and continuity of operations with delegations of authority and succession | Which services continue on paper (ED screening, inpatient care, births, emergency surgery) and which stop (elective surgery, outpatient imaging); diversion decided by the CNO, ED Medical Director, and administrator on call, with the CEO as successor | To be added to the plan |
| (b)(5) A system of medical documentation that preserves patient information, protects confidentiality, and secures and maintains the availability of records | RTO 2 hours and RPO 15 minutes for clinical documentation; downtime workstations; paper record custody and back-entry | Gap: vendor RTO 12 hours (finding 1); downtime never exercised beyond 4 hours |
| (b)(7) Arrangements with other hospitals and providers to receive patients if operations are limited or stop | Transfer and diversion arrangements with the regional medical center and the 180-bed hospital, including stroke and STEMI patients | Existing hurricane arrangements; cyber scenario to be confirmed with both hospitals |
| (c)(3) Primary and alternate means of communicating with staff and emergency management agencies | Analog lines, EMS radio, handheld radios, out-of-band messaging (P08) | Gap: alternate means exist only in the ED and house supervisor office |
| (c)(4) Method for sharing information and medical documentation with other providers | Paper transfer packet from the downtime extract | Written here; procedure due 2026-12-15 |
| (c)(7) Information on occupancy, needs, and ability to assist to the authority having jurisdiction or the incident command center | Diversion status and bed availability reported to county EMS and the healthcare coalition | Existing for hurricanes; add IT outage trigger |
| (d)(1) Training at least every 2 years, documented, with demonstrated staff knowledge | Downtime training for nursing, ED, pharmacy, laboratory, and imaging | To be added |
| (d)(2) Exercises at least twice a year, including the annual community full-scale exercise and an additional exercise (which may be a facilitated tabletop) | Ransomware and 72-hour EHR downtime tabletop scheduled 2026-11-10 as the additional exercise | Planned |
| Plan, policies, communication plan, and training and testing program reviewed and updated at least every 2 years | Next plan revision incorporates this BIA | Due 2026-12-15 |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Clinical communications: analog lines, EMS radio, handheld radios, then VoIP and smartphones | 0.5 h | Printed contact lists; runners; personal cell phones |
| 2 | SYS-02 identity provider and break-glass accounts | 1 h | Two sealed break-glass accounts per critical system (cloud only today) |
| 3 | SYS-06 campus core network, then medical device and monitoring segments | 1 h | Isolate segments; restore monitoring network first |
| 4 | Monitoring gateway and central stations (SYS-05, SYS-08) | 1 h | Bedside monitors with assigned observers |
| 5 | SYS-07 clean endpoints for the ED, ICU, pharmacy, laboratory, and nursing stations | 2 h | 20 pre-imaged spare laptops; downtime workstations |
| 6 | SYS-01 EHR access through the vendor connection | 2 h target (vendor commits to 12 h) | Downtime workstations and paper procedures |
| 7 | LIS and blood bank module; dispensing cabinet server; pump server (SYS-05) | 2 h | Standalone analyzers; cabinet overrides with double-check; pumps on last library |
| 8 | Fetal surveillance server and cardiology system (SYS-05) | 2 h | Bedside strips; cath lab standalone with paper log |
| 9 | SYS-03 PACS and RIS | 2 h | Modality local storage; reads at consoles; teleradiology by image transfer |
| 10 | SYS-09 OT on its own segment | 2 h | Hourly manual rounds |
| 11 | SYS-10 SIEM feeds and EDR console | 4 h | MSSP runs from its own platform; needed to validate clean recovery |
| 12 | SYS-04 interface engine | 8 h | Phone and fax results; queue public health messages |
| 13 | Affiliated practice access (after hospital units) | 8 h after EHR availability | Practice downtime procedures |
| 14 | File services and HIM scanning | 24 h | Printed downtime binders |
| 15 | Clearinghouse connectivity and claims backlog | 48 h | Payer portals for high-dollar claims; credit line |
| 16 | Payroll, HR, and credentialing SaaS | 72 h | Repeat prior payroll; Medical Staff Office binder |
| 17 | SYS-04 data warehouse | 120 h | EHR standard reports |

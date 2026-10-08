# Business Impact Analysis: Cris Santos Company | Healthcare and Public Health | Small

**Organization:** Cris Santos Company, LLC (rural critical access hospital) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Security Officer) with the Director of Nursing, Facilities Manager, and department managers | **Approved:** CEO, 2026-08-31
**Sources:** process owner interviews 2026-07-13 to 2026-07-15 (EV-057), FY2025 revenue report (EV-025), patient volume report (EV-026), backup job reports (EV-017), the EHR vendor's SOC 2 report (EV-018), downtime PC print logs (EV-033), and the phone inventory and communication plan (EV-046, EV-030). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owners' statements, reviewed and approved by the CEO.

## 1. Overview and purpose
This BIA identifies the processes the hospital depends on, how long each can be down, and how much data it can lose. It supports:
- the HIPAA contingency plan (45 CFR 164.308(a)(7)), including the applications and data criticality analysis (164.308(a)(7)(ii)(E));
- the emergency preparedness plan: the services the hospital can provide during an emergency and continuity of operations (42 CFR 485.625(a)(3)), and the medical documentation system (485.625(b)(5));
- the availability rating in the SSP (P02), impact ratings in the risk register (P01), and the recovery order in the incident response runbook (P08).

## 2. System and business description
The hospital has 12 inpatient beds used for acute or swing-bed care, a 24-hour emergency department with about 20 visits a day, a laboratory, CT and X-ray, and a small pharmacy. Clinical work runs on the Hospital Clinical Information System (HCIS): a vendor-hosted EHR, an identity provider, a cloud tenant (imaging archive, interface engine, backup vault), the hospital network and server room, endpoints, and medical devices. Building and clinical OT shares the same network. The nearest hospital that can take diverted patients is about 45 miles away. Systems and suppliers are listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv).

## 3. Impact categories and values
Dollar values are scaled to $28.2 million in FY2025 revenue, about $77,000 a day (EV-025).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $230,000 (about 3 days of revenue) | $50,000 to $230,000 | Less than $50,000 |
| Operations | The ED must go on diversion, or inpatient care cannot continue safely | One department stops or slows sharply | Staff slowed but working |
| Regulatory | EMTALA exposure, reportable breach, or a condition-of-participation finding | Missed reporting or documentation deadline | Internal policy deviation |
| Safety | Plausible serious harm (missed allergy, wrong dose, delayed stroke, sepsis, or trauma care) | Delayed but safe care | None |
| Reputation | Regional media coverage or loss of community trust in the only local hospital | Complaints or online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-12 Internal and external communications | High | 2 h | 1 h | 24 h |
| BP-01 Emergency department care | High | 4 h | 2 h | 15 min |
| BP-02 Inpatient and swing-bed nursing and medication administration | High | 4 h | 2 h | 15 min |
| BP-03 Pharmacy order verification and dispensing | High | 4 h | 2 h | 15 min |
| BP-04 Laboratory testing and result reporting | High | 4 h | 2 h | 1 h |
| BP-09 Building and clinical OT monitoring | High | 4 h | 2 h | 168 h |
| BP-05 Diagnostic imaging and teleradiology | High | 8 h | 4 h | 1 h |
| BP-06 Registration, bed management, and transfers | High | 8 h | 4 h | 1 h |
| BP-07 Revenue cycle and claims | Moderate | 72 h | 48 h | 24 h |
| BP-08 Public health and regulatory reporting | Moderate | 72 h | 48 h | 24 h |
| BP-10 Health information management | Low | 120 h | 72 h | 24 h |
| BP-11 Payroll and HR | Low | 120 h | 72 h | 24 h |

The table is in recovery priority order. Eight processes are High, two Moderate, and two Low.

**What drives the values:**
- **Patient safety and EMTALA drive BP-01 to BP-04.** The ED must screen and stabilize anyone who arrives, whatever the state of IT (42 CFR 489.24). The 4-hour MTD is the point where leaders, with the ED physician, decide whether to ask county EMS to divert ambulances. EMTALA allows a hospital to divert ambulances that are not yet on its property when it lacks the staff or facilities to accept more emergency patients (489.24(b)); walk-in patients and ambulances that arrive anyway are still screened.
- **Diversion is costly here.** A diverted ambulance travels about 45 more miles. That is why the MTD for ED support systems is short, and why downtime procedures, not only system recovery, have to carry the first hours.
- **The 2-hour MAR print cycle sets the practical limit for BP-02.** The downtime PC prints the MAR every 2 hours, so the 2-hour RTO keeps nurses within one print cycle of current data.
- **BP-12 is first.** Diversion, transfers, and staff call-in all depend on phones. The VoIP system rides on the hospital network, so a network-wide attack takes it down unless the analog lines and radio work.
- **Revenue drives BP-07 more than time.** Payers accept late claims within their filing limits, and Medicare interim payments cushion a delay.
- **BP-09 RPO of 168 hours** reflects that OT configurations change rarely; a weekly configuration export is enough. Today no export is taken (gap below).

## 5. Key findings
1. **The EHR vendor's recovery commitment does not meet the BIA.** The vendor's SOC 2 system description states an RTO of 8 hours and an RPO of 15 minutes (EV-018; P09). The RPO meets the 15-minute need of BP-01 to BP-03. The RTO does not meet their 2-hour need. Until the contract says otherwise, downtime procedures must carry up to 8 hours of EHR outage, and those procedures are from 2019 and untested (P01 R-004).
2. **Hospital-managed recovery is unproven.** Backups of the servers, interface engine, and imaging archive have never been restore-tested, and the backup appliance is reachable from the directory (P01 R-003). The 2-hour RTO for the dispensing cabinet server and analyzer middleware (BP-03, BP-04) and the 4-hour RTO for the imaging archive (BP-05) are therefore targets, not capabilities.
3. **One network carries everything.** Phones, OT, medical devices, and workstations share one flat network and one fiber circuit. A single attack or fiber cut hits BP-01, BP-04, BP-05, BP-09, and BP-12 at once (P01 R-001, R-014, R-033).
4. **No OT configuration backups.** The building automation and nurse call vendors have not confirmed they keep configuration backups (BP-09 RPO unsupported today).

## 6. Resource requirements
| Resource | Description | Supports | Recovery method today |
|---|---|---|---|
| SYS-01 EHR (vendor-hosted) | System of record, eMAR, orders, laboratory module, patient accounting, portal | BP-01 to BP-07, BP-10 | Vendor replication (RPO 15 min, RTO 8 h per SOC 2) |
| SYS-02 Identity provider | Single sign-on and MFA; directory synchronization | All | SaaS; break-glass accounts planned |
| SYS-05 Network, phones, and server room | Firewall, core switch, Wi-Fi, fiber and cellular backup, VoIP phones, virtualization host (directory, file, print, middleware, dispensing cabinet, pump drug-library servers) | All | Nightly backup to local appliance with cloud copy (not isolated) |
| SYS-06 Endpoints | 88 desktops and workstations on wheels, 12 laptops, 16 barcode scanners, 2 downtime PCs | BP-01 to BP-06 | Standard image; 6 pre-imaged spare laptops planned |
| SYS-07 Medical devices | CT, X-ray, infusion pumps, monitors, analyzers, dispensing cabinets | BP-01 to BP-05 | Standalone operation; vendor support |
| SYS-04 Imaging archive | CT and X-ray storage and viewer | BP-05 | Daily snapshots, same account (not isolated) |
| SYS-04 Interface engine | Reference laboratory, HIE, and public health feeds | BP-04, BP-08 | Daily snapshots, same account |
| SYS-08 Building and clinical OT | Nurse call, HVAC, medical gas alarms, generator monitoring | BP-09 | Local controllers; no configuration export |
| SYS-09 to SYS-12, SYS-14 | Clearinghouse, teleradiology, telepharmacy, reference lab, HIE, public health, cloud fax | BP-03 to BP-08, BP-10 | Vendor-operated |
| People and facilities | Nurses, contracted ED physicians, laboratory and imaging staff, IT Manager, IT Support Specialist, MSP, Facilities staff; one campus | All | Call-in list; agency staff |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Phones: analog lines, EMS radio, cellular phones | 1 h | Printed contact list; personal cell phones |
| 2 | SYS-02 identity provider and break-glass accounts | 1 h | Two sealed break-glass accounts (to be created) |
| 3 | SYS-05 firewall, core network, and internet | 2 h | Cellular backup on the firewall for EHR traffic only |
| 4 | SYS-06 clean endpoints for the ED, nursing station, pharmacy, and laboratory | 2 h | 6 pre-imaged spare laptops (to be purchased) |
| 5 | SYS-01 EHR access through the vendor tunnel | 2 h target (vendor commits to 8 h) | Downtime PCs and paper downtime procedures |
| 6 | Dispensing cabinet server and analyzer middleware | 2 h | Cabinet override with double-check; standalone analyzers |
| 7 | SYS-08 OT monitoring on its own segment | 2 h | Manual rounds every 2 hours |
| 8 | SYS-04 imaging archive and the route to teleradiology | 4 h | CT local storage; transfer patients who need emergent reads |
| 9 | SYS-04 interface engine | 12 h | Phone and fax results and reportable conditions |
| 10 | File and print servers | 24 h | Local printers on downtime PCs |
| 11 | SYS-09 clearinghouse connectivity | 48 h | Queue claims |
| 12 | Payroll SaaS | 72 h | Repeat prior payroll |

# Business Impact Analysis: Cris Santos Company | Healthcare and Public Health | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded for-profit hospital system: 8 hospitals, 1,970 beds; FL, GA, AL) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners and hospital presidents, 2026-05-04 to 2026-06-26 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-24 | **Reported to:** risk committee of the board, 2026-09-15
**Sources:** process owner and hospital president interviews 2026-05-04 to 2026-06-12 (EV-079, EV-080), dependency and contract review (EV-081), the tele-critical care failover test (EV-082), site and license register (EV-055), FY2025 revenue report (EV-053), operational volume report (EV-054), claims routing report (EV-041), DR test, backup and contingency records (EV-023, EV-019, EV-024), the H-08 legacy EHR contract (EV-056), service line agreements (EV-043, EV-044) and the H-01 diversion protocol (EV-052). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owners' statements, reviewed and approved by the Chief Operating Officer and the Chief Risk Officer.

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the hospital system depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, the acquired hospital H-08, and the two service lines sold to other organizations. It feeds:
- the HIPAA contingency plan, including the applications and data criticality analysis (45 CFR 164.308(a)(7)(ii)(E));
- the unified emergency preparedness program for all 8 hospitals (42 CFR 482.15(a)(1)-(3) and 482.15(f)): the services each hospital can provide during an IT outage, and the IT-outage diversion criteria;
- the integrity and availability ratings and recovery objectives in the ECIS System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order and the diversion decision rule in the ransomware runbook (P08);
- the Availability criteria for the SL-1 and SL-2 SOC 2 readiness work (P09).

**Results in one line:** 21 processes were analyzed; 14 are High criticality and 7 Moderate. 11 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 28 dependencies, 9 of them single points of failure and 4 never tested.

## 2. System and business description
Cris Santos Company operates 8 acute-care hospitals with 1,970 licensed beds in Florida, Georgia, and Alabama, 3 freestanding emergency departments, 4 outpatient imaging centers, and 46 physician group clinics. It has 12,000 employees, about 102,000 admissions and 560,000 emergency visits a year, and about $4.8 billion in annual revenue. The technology estate is listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv): a customer-managed enterprise EHR in two data centers (SYS-01, SYS-03), an identity platform (SYS-02), two public clouds (SYS-04), an SD-WAN (SYS-05), about 26,000 endpoints and 41,000 networked medical devices (SYS-06), building and clinical OT (SYS-07), enterprise imaging (SYS-08), ERP and payroll (SYS-09), about 1,500 vendors (SYS-10), and unified communications (SYS-12). H-08, acquired on 2025-10-01, still runs its own EHR (SYS-13) until 2027-03-01.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day ($4.8 billion in FY2025 revenue, EV-053) and to the materiality worksheet in P08 section 7. Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Any hospital must divert ambulances, or a tier-1 service stops at more than one hospital | One department, one hospital, or one service line degraded | Staff slowed but working |
| Regulatory | Reportable breach of 500 or more; CMS condition-level or EMTALA finding; CLIA finding; missed SEC filing | Missed contractual or documentation deadline; breach under 500 | Internal policy deviation |
| Safety | Plausible patient harm (delayed emergency care, medication error, missed critical result) | Delayed but safe care | None |
| Reputation | National media, analyst or ratings action, loss of partner or affiliate contracts | Regional media; partner complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
Ordered by RTO, then MTD.

| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-08 Clinical communications | High | 2 h | 1 h | 24 h | $0.30M |
| BP-09 Building and clinical operational technology | High | 4 h | 2 h | 24 h | $0.80M |
| BP-15 Tele-critical care and telestroke (SL-2) | High | 4 h | 2 h | 1 h | $0.15M |
| BP-01 Emergency care and ambulance intake | High | 8 h | 4 h | 15 min | $3.10M |
| BP-02 Inpatient care, nursing documentation, and medication administration | High | 8 h | 4 h | 15 min | $5.60M |
| BP-04 Laboratory testing and critical result reporting | High | 8 h | 4 h | 15 min | $1.20M |
| BP-05 Diagnostic imaging and radiology reads | High | 8 h | 4 h | 1 h | $1.40M |
| BP-06 Pharmacy order verification and dispensing | High | 8 h | 4 h | 15 min | $0.60M |
| BP-07 Patient access, bed management, and transfer center | High | 8 h | 4 h | 15 min | $0.90M |
| BP-03 Surgical and procedural services | High | 12 h | 4 h | 15 min | $3.40M |
| BP-14 Affiliate EHR hosting (SL-1) | High | 24 h | 4 h | 15 min | $0.25M |
| BP-20 H-08 clinical operations on the legacy EHR | High | 8 h | 8 h | 15 min | $0.90M |
| BP-12 Physician group clinic care | High | 24 h | 8 h | 15 min | $1.60M |
| BP-13 Patient portal, telehealth, and FHIR API | Moderate | 24 h | 8 h | 1 h | $0.20M |
| BP-21 Behavioral health and Part 2 program (H-03) | Moderate | 24 h | 8 h | 15 min | $0.10M |
| BP-17 Supply chain and materials management | Moderate | 48 h | 24 h | 24 h | $0.40M |
| BP-19 Health information management, release of information, and public health reporting | Moderate | 48 h | 24 h | 4 h | $0.10M |
| BP-16 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-10 Claims submission and remittance | High | 120 h | 72 h | 24 h | $10.50M |
| BP-18 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-11 Patient billing, payment posting, and collections | Moderate | 168 h | 72 h | 24 h | $0.50M |

**What drives the values:**
- **Patient safety and EMTALA** set the shortest MTDs. Emergency care (BP-01), inpatient medication administration (BP-02), laboratory critical results (BP-04, 42 CFR 493.1291(g)), imaging for stroke and trauma (BP-05), and pharmacy (BP-06) cannot wait more than one medication pass or one stroke window. EMTALA duties to screen and stabilize anyone who comes to the emergency department do not pause during an outage (42 CFR 489.24(a)).
- **Communications and building systems** have the shortest MTDs of all (BP-08, 2 hours; BP-09, 4 hours), because they are the workarounds for everything else. Operating room pressure and medical gas alarms run on SYS-07.
- **Cash, not time,** drives claims (BP-10). Payers accept late claims within filing limits, so the MTD is 5 days, but each day defers about $10.5 million of expected payments through the primary clearinghouse.
- **Contracts** set the SL-1 (BP-14) and SL-2 (BP-15) objectives. SL-2 partner hospitals' ICU patients depend on remote monitoring overnight, so its MTD is 4 hours.
- **Regulation** tightens financial close (BP-18) during the quarter-end window, when the MTD drops to 48 hours because of SEC filing deadlines.

**Two recovery objectives for the ECIS.** The 4-hour RTO for BP-01 to BP-07 is met by failover to DC-2 (2.6 hours in the 2026-03-21 test, EV-023). Ransomware that also reaches DC-2 (both data centers share one directory) needs a restore from the immutable vault. For that case the business set a **24-hour cyber recovery target**, the longest the hospitals can run on BCA downtime computers and paper before patient safety, diversion, and record integrity become unmanageable. The 2026-04-18 full restore test took **41 hours** (EV-023; R-004; POAM-003).

## 5. Diversion thresholds by process (for the emergency plan and P08)
EMTALA allows a hospital to direct an ambulance that is not yet on its property to another facility only when the hospital "does not have the staff or facilities to accept any additional emergency patients" (42 CFR 489.24(b), definition of "comes to the emergency department"). Anyone who arrives must still be screened and stabilized. The BIA gives the emergency plan these IT-outage triggers, to be applied hospital by hospital:

| Trigger (not expected to recover within the MTD) | Process | Diversion scope |
|---|---|---|
| CT cannot be read, or images cannot reach a radiologist | BP-05 | CT-dependent ambulance traffic (stroke, major trauma) |
| Laboratory cannot produce or report results, including critical values | BP-04 | All ambulance traffic needing stat laboratory work |
| ED cannot document, order, or give medications safely on paper | BP-01; BP-02; BP-06 | Full diversion |
| Phones, secure messaging, and radio fallback all unavailable | BP-08 | Full diversion |
| Operating room air handling or medical gas alarms unavailable | BP-09 | Trauma and surgical traffic |

No more than one hospital in a county may go on full IT-outage diversion without the System Transfer and Command Center coordinating with county EMS and the receiving hospitals. Today these criteria are agreed only for H-01 (EV-052; DEP-10; R-009; POAM-018).

## 6. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Cyber recovery, not failover (DEP-01 to DEP-05).** Failover between data centers is fast and tested. The gap is the case where both data centers are compromised. The immutable vault keeps clean copies, but a full restore takes 41 hours, and the isolated recovery environment where restored systems are rebuilt and checked is not finished (EV-023, EV-024).
2. **Clearinghouse concentration (DEP-08).** One clearinghouse carries about 80% of claims. The secondary clearinghouse has no contracted surge capacity, and the payer-portal fallback has never been tested (EV-041, EV-080). A 30-day outage would defer about $315 million of expected payments (R-005; POAM-019).
3. **Acquired hospital H-08 (DEP-21, DEP-22).** Its legacy EHR vendor's contract states a 24-hour RTO against an 8-hour BIA RTO, the restore has never been tested by the system, and H-08 reaches the enterprise integration engine over a legacy site VPN (EV-056, EV-014).
4. **EMS and diversion (DEP-10).** EMS agencies in 9 counties depend on the system's EDs. Only H-01 has agreed IT-outage diversion criteria (EV-052).
5. **Medical devices and OT (DEP-12 to DEP-14).** About 2,600 networked devices run unsupported operating systems, three analyzer platforms use vendor remote tools outside PAM, and OT is not segmented at H-07 and H-08 (EV-012, EV-016, EV-017).
6. **Tele-critical care (DEP-17, DEP-18).** SL-2 has no alternate virtual care center; its cloud platform failover met the 2-hour RTO in 2026-06 (EV-082).

## 7. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 ECIS (EHR, integration engine, BCA devices) | System of record for clinical care, laboratory, pharmacy, radiology, revenue cycle | BP-01 to BP-07; BP-10; BP-12; BP-14; BP-19; BP-21 |
| SYS-02 Identity platform | SSO, badge-tap access, MFA, privileged access, identity governance | All |
| SYS-03 Data centers DC-1 and DC-2 | EHR production and standby, PACS, network core, offline backup copy | All clinical processes |
| SYS-04 Cloud provider A | Portal and FHIR API front end; immutable backup vault; isolated recovery environment | BP-13; recovery of all |
| SYS-04 Cloud provider B and SYS-14 | Tele-critical care platform; data and analytics; AI services | BP-15; BP-18 |
| SYS-05 Network | SD-WAN, hospital campus networks, NAC | All site-based processes |
| SYS-06 Endpoints and medical devices | Workstations, BCA computers, analyzers, pumps, monitors, ADCs | BP-01 to BP-06 |
| SYS-07 Building and clinical OT | Air handling, medical gas alarms, generator monitoring, nurse call | BP-03; BP-09 |
| SYS-08 Enterprise imaging | PACS and archive | BP-05 |
| SYS-09 ERP and payroll | Finance, payroll, supply chain | BP-11; BP-16 to BP-18 |
| SYS-12 Unified communications | VoIP, secure messaging, mass notification; analog lines and EMS radio | BP-07; BP-08 |
| People | Clinicians, laboratory and pharmacy staff, SOC, data center operations, transfer center | All |

## 8. Recovery priorities
Restore order for a system-wide event. Each item restores in a clean environment first.

| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Clinical communications (analog lines, radio, cellular; then VoIP and secure messaging) | 1 h | Runners; overhead paging; EMS radio |
| 2 | Identity platform and break-glass accounts | 1 h | Sealed break-glass accounts |
| 3 | Network core, SD-WAN, DNS, data center links | 2 h | Cellular failover at sites |
| 4 | Building OT monitoring | 2 h | Manual building operation |
| 5 | Security tooling (EDR console, SIEM) for validation | 2 h | Managed security service provider tooling |
| 6 | Tele-critical care platform (SL-2) | 2 h | Partner hospitals' local coverage |
| 7 | ECIS: EHR database, application, integration engine (failover 4 h; vault restore 24 h target) | 4 h (failover) or 24 h (cyber restore) | BCA downtime computers; paper |
| 8 | Laboratory analyzer middleware and pharmacy ADC servers | 4 h | Manual result entry; ADC override |
| 9 | PACS and radiology reading path | 4 h | Read at modality; telephone reads |
| 10 | Patient portal, telehealth, and FHIR API | 8 h | Contact center; phone visits |
| 11 | H-08 legacy EHR | 8 h target (24 h per vendor contract) | Paper downtime; transfers |
| 12 | HIE, public health reporting, release of information | 24 h | Fax or phone reports |
| 13 | ERP, payroll, supply chain | 24 to 48 h | Repeat prior payroll; manual orders |
| 14 | Clearinghouse connectivity and claims pipeline | 72 h | Secondary clearinghouse; payer portals |

## 9. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Cyber restore 41 h against a 24 h target; isolated recovery environment not finished | P01 R-004; P02 CP-10; POAM-003 |
| IT-outage diversion criteria only at H-01; no multi-hospital downtime exercise | P01 R-009; P03 (42 CFR 482.15(a)(1)-(2)); POAM-018; P08 section 4 |
| Clearinghouse concentration and untested fallback | P01 R-005; P03 164.308(a)(7)(ii)(B); POAM-019 |
| H-08 legacy EHR RTO 24 h against 8 h | P01 R-061 (closed by the 2027-03-01 conversion); interim vendor recovery commitment |
| Medical devices on unsupported operating systems; vendor remote tools outside PAM | P01 R-006, R-011; POAM-009; POAM-011 |
| Communications fallback not tested at several hospitals at once | P01 R-018; P08 section 1 |

# Business Impact Analysis: Cris Santos Company | Health Care and Social Assistance | Mid-Market

**Organization:** Cris Santos Company, Inc. (multi-specialty physician group with an ASC and an imaging center) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager with the vCISO, the process owners named in `bia.csv`, and the ASC Administrator | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the 8 clinics, the ambulatory surgery center (ASC), the imaging center, the central business office (CBO), and enterprise support functions. It rates 17 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and patient safety.

The results feed:
- the HIPAA contingency plan and its Applications and Data Criticality Analysis (45 CFR 164.308(a)(7), including (7)(ii)(E));
- the ASC emergency preparedness program required by 42 CFR 416.54 (section 7 below);
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The company runs 8 clinics, a Medicare-certified ASC with 4 operating rooms, and an imaging center (MRI, CT, X-ray) in Florida, with about 110,000 active patients. Clinical and business work runs on the Enterprise Clinical Platform (ECP) described in the SSP (P02): the SaaS EHR/PM, the identity provider, the PACS and radiology information system, the 4-account cloud landing zone (interface engine, data warehouse, file services, backups), the 10 site networks on SD-WAN, 870 endpoints, about 400 networked medical devices, and the MSSP-operated SIEM. About 140 vendors handle PHI (see `../scenario-facts.md` sections 3, 4, and 7).

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual revenue over about 250 operating days: about $240,000 per day for the clinics, $88,000 for the ASC, and $48,000 for the imaging center. About $1.9 million in expected collections moves through the clearinghouse each week (about $380,000 per business day).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $200,000 in lost revenue, or more than $1 million of cash delayed | $40,000 to $200,000 | Less than $40,000 |
| Operations | A business unit (all clinics, the ASC, or the imaging center) cannot deliver its core service | One site or one service line stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory | Reportable breach, CMS condition-for-coverage deficiency, or federal program issue | Missed documentation, timeliness, or payer requirement | Internal policy deviation |
| Patient safety | Plausible patient harm (missed allergy, wrong dose, delayed critical result, intraoperative information loss) | Delayed but safe care | None |
| Reputation | Regional media coverage, loss of the hospital joint venture partner, or referral loss | Patient complaints or online reviews | Internal only |

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered plus extra labor, over the MTD. Recovery assumptions came from the process owners: about 35% of cancelled clinic visits, 50% of cancelled ASC cases, and 40% of deferred imaging studies are not recovered. For claims (BP-10), the loss is overtime, denials, and interest on the credit line; the delayed cash is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-04 Surgical services | ASC | High | 4 | 2 | 0.25 | $30,000 |
| 2 | BP-01 Clinical documentation and care delivery | Clinics | High | 8 | 4 | 1 | $94,000 |
| 3 | BP-03 E-prescribing | Clinics | High | 8 | 4 | 1 | $10,000 |
| 4 | BP-02 Scheduling, registration, and eligibility | Clinics | High | 8 | 4 | 1 | $40,000 |
| 5 | BP-07 Imaging acquisition and reading | Imaging center | High | 12 | 6 | 1 | $30,000 |
| 6 | BP-05 Medication administration and infusion | ASC | High | 24 | 8 | 24 | $20,000 |
| 7 | BP-09 Laboratory orders and results | Clinics and ASC | Moderate | 24 | 8 | 1 | $5,000 |
| 8 | BP-06 ASC case scheduling and pre-admission | ASC | Moderate | 24 | 8 | 1 | $30,000 |
| 9 | BP-08 Imaging results distribution | Imaging center | Moderate | 24 | 12 | 4 | $5,000 |
| 10 | BP-13 Patient communications | Enterprise | Moderate | 24 | 8 | 24 | $10,000 |
| 11 | BP-12 Prior authorization | CBO | Moderate | 48 | 24 | 24 | $60,000 |
| 12 | BP-14 Referral management | Enterprise | Moderate | 48 | 24 | 24 | $15,000 |
| 13 | BP-10 Claims and clearinghouse connectivity | CBO | Moderate | 72 | 48 | 24 | $60,000 (plus $1.14 million cash delayed) |
| 14 | BP-17 ASC supplies and implant tracking | ASC | Moderate | 72 | 24 | 24 | $10,000 |
| 15 | BP-11 Payment posting and patient billing | CBO | Low | 120 | 72 | 24 | $15,000 |
| 16 | BP-16 Payroll, HR, and credentialing | Enterprise | Low | 120 | 72 | 24 | $20,000 |
| 17 | BP-15 Quality reporting and analytics | Enterprise | Low | 168 | 120 | 24 | $5,000 |

**Summary:** 6 High, 8 Moderate, and 3 Low processes (17 in total). The sum of estimated losses at each process's MTD is $459,000.

**Enterprise-wide scenario.** If the whole ECP were down for 72 hours (for example, ransomware), unrecovered revenue would be about $440,000 (clinics $252,000, ASC $132,000, imaging $58,000). About $1.14 million of cash would also be delayed. Incident response and breach notification costs come on top (see P01 R-001 and R-002).

**What drives the values:**
- **Patient safety** drives BP-01, BP-03, BP-04, BP-05, and BP-07. The ASC has the shortest MTD (4 hours) because cases cannot start safely without the history and physical, consent, allergy, and anesthesia records.
- **Cash flow**, not time, drives BP-10. Payers accept late claims within their filing limits, but about $380,000 of collections is delayed each business day.
- **Regulatory** duties drive the ASC rows (42 CFR 416.54) and BP-08 (critical result communication).

## 5. Key findings
1. **EHR vendor recovery objectives do not meet the BIA.** The EHR vendor's SOC 2 system description states RTO 12 hours and RPO 1 hour. The BIA needs RTO 2 hours for the ASC (BP-04) and 4 hours for clinics (BP-01 to BP-03). The downtime report workstations (hourly read-only extract) make the MTD achievable in read-only mode, but the ASC RPO of 15 minutes is not met. Action: negotiate contract recovery terms and add an ASC-specific extract every 15 minutes (P01 R-013; P09 vendor review).
2. **Practice-managed recovery is unproven.** The interface engine (BP-08, BP-09, BP-10), PACS (BP-07), and data warehouse (BP-15) have never been restore-tested (gap 4). Their RTOs of 6 to 120 hours are targets, not demonstrated capabilities (P01 R-014 to R-016; P07 CP-4).
3. **The clearinghouse is a single point of failure.** One clearinghouse carries all claims and eligibility. A multi-week outage would delay about $1.9 million of collections per week (P01 R-012; P08 `ir-runbook-vendor-outage.md`).
4. **The ASC emergency plan does not address cyber events** such as loss of the EHR or of the infusion pump network (gap 6; section 7).
5. **Medical devices keep working without the network**, but monitoring, drug library updates, and results flow stop. Manual workarounds exist but are not written into the downtime procedures for BP-05 and BP-07.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 EHR/PM (SaaS) | System of record, portal, e-prescribing, ASC perioperative module | BP-01 to BP-06, BP-09 to BP-14, BP-17 |
| SYS-02 Identity provider | SSO and MFA for all users; conditional access | All |
| SYS-03 PACS and RIS (vendor-managed, in the workloads account) | Image storage, reading, AI triage worklist (AI-003) | BP-07, BP-08 |
| SYS-04 Landing zone: interface engine | HL7 and X12 interfaces to labs, clearinghouse, HIE, PACS | BP-08, BP-09, BP-10, BP-14 |
| SYS-04 Landing zone: data warehouse | Analytics and reporting | BP-15 |
| SYS-04 Landing zone: file services | Department shares (downtime forms, procedures) | All (downtime) |
| SYS-04 Landing zone: backup account | Daily immutable backups, 35-day retention | Recovery of SYS-03 and SYS-04 workloads |
| SYS-05 Site networks and SD-WAN | 10 sites; dual ISP at the ASC and imaging center, single ISP at clinics | All |
| SYS-06 Endpoints | 750 workstations and laptops, 120 tablets; downtime report workstation at each site | All |
| SYS-07 Medical devices | About 400 networked devices, including ASC infusion pumps and pump server, and imaging modalities | BP-04, BP-05, BP-07 |
| SYS-08 SIEM (MSSP) | Detection and investigation | Recovery validation |
| Third parties | EHR vendor, PACS vendor, clearinghouse, MSSP, cloud provider, reference labs, teleradiology group, prior-authorization vendor | As listed in `bia.csv` |
| People and facilities | 90 providers, ASC and imaging staff, CBO staff, IT and security team, MSSP | All |

## 7. ASC emergency preparedness linkage (42 CFR 416.54)
The ASC is a Medicare-certified ambulatory surgical center, so the CMS emergency preparedness condition for coverage applies to it (42 CFR 416.54, text verified on eCFR, 2026-09-23 version). The clinics and imaging center are not covered by that section. The BIA supplies the cyber content the ASC program is missing today:

| 416.54 requirement (verified text, summarized) | What this BIA supplies | Status |
|---|---|---|
| (a)(1) Plan based on a documented facility-based and community-based risk assessment using an all-hazards approach | Cyber events (ransomware, EHR vendor outage, pump network loss, clearinghouse outage) added as hazards, with the P01 risks R-001, R-013, and R-017 | Hazards added in this BIA; the ASC plan update is due 2026-12-15 |
| (a)(2) Strategies for events identified by the risk assessment | Workarounds for BP-04, BP-05, BP-06, and BP-17 | Written here; procedures due 2026-12-15 |
| (a)(3) Continuity of operations, including delegations of authority and succession | ASC MTD 4 hours; decision to cancel cases rests with the ASC Medical Director, with the Chief Medical Officer as successor | To be added to the ASC plan |
| (b)(4) A system of medical documentation that preserves patient information, protects confidentiality, and secures and maintains availability of records | BP-04 RTO 2 hours and RPO 15 minutes; paper perioperative packet; ASC downtime extract | Gap: vendor RPO is 1 hour (finding 1) |
| (c) Communication plan with primary and alternate means of communication | Out-of-band contact tree in the P08 runbooks | To be added to the ASC plan |
| (d)(1) Training at least every 2 years, and (d)(2) exercises at least annually, including an option for a facilitated tabletop | Cyber downtime tabletop for the ASC scheduled for 2026-11-18 | Planned |
| Plan, policies, and communication plan reviewed and updated at least every 2 years | Next ASC plan revision incorporates this BIA | Due 2026-12-15 |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-02 identity provider and break-glass accounts | 1 h | Two break-glass accounts per critical system, stored offline |
| 2 | SYS-05 SD-WAN and site networks (ASC first, then clinics and imaging) | 2 h | Cellular failover kits at every site (ASC and imaging center have dual ISP) |
| 3 | SYS-06 clean endpoints for the ASC and clinic front desks | 2 h (ASC), 4 h (clinics) | Pre-imaged spare laptops: 6 at the ASC, 4 per clinic |
| 4 | SYS-01 EHR/PM access (vendor-hosted) | 2 h (ASC read access), 4 h (full) | Downtime report workstations; paper packets |
| 5 | SYS-07 ASC infusion pump server and device VLAN | 8 h | Pumps run on last library; manual programming with double-check |
| 6 | SYS-03 PACS and RIS | 6 h | Modality local storage; urgent reads at consoles; teleradiology group |
| 7 | SYS-04 interface engine | 8 h | Lab portals, fax, phone for critical results |
| 8 | SYS-08 SIEM and EDR console | 8 h | MSSP runs from its own platform; needed to validate clean recovery |
| 9 | Clearinghouse connectivity (vendor) and claims backlog | 48 h | Payer portals for high-dollar claims; credit line |
| 10 | Prior-authorization automation (AI-004) | 24 h | Manual payer portal submissions |
| 11 | SYS-04 file services | 24 h | Printed downtime binders |
| 12 | Payroll and HR SaaS | 72 h | Repeat prior payroll |
| 13 | SYS-04 data warehouse | 120 h | EHR standard reports |

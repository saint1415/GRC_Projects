# Scenario facts: Cris Santos Company | Healthcare and Public Health | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the Health Care (NAICS 62) samples, which describe physician practices. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (licensed operator of one rural hospital; the hospital's trade name is not used in this sample) |
| Business | **Critical access hospital (CAH)**, NAICS 622110 General Medical and Surgical Hospitals. 12 inpatient beds used for acute or swing-bed care (the CAH limit is 25; 42 CFR 485.620(a)), a 24-hour emergency department (42 CFR 485.618(a)), laboratory, radiology (digital X-ray and one CT scanner), respiratory therapy, outpatient infusion, and a small inpatient pharmacy |
| Why a CAH | A general acute-care hospital with 60 employees is only plausible as a very small rural facility. The CAH designation fits that facility: a rural location more than a 35-mile drive on primary roads from the nearest hospital (42 CFR 485.610(b)-(c)), no more than 25 beds, and an annual average acute length of stay of 96 hours or less (485.620(b)). Seriously ill patients are stabilized and transferred to a regional hospital about 45 miles away |
| Location | Florida. One campus in a rural North Florida county: the hospital building, an attached outpatient wing, and a server room. No other sites |
| Workforce | 60 employees: 8 leadership and administration, 2 IT, 26 nursing (registered nurses, licensed practical nurses, nursing assistants), 11 ancillary (laboratory, imaging, respiratory therapy, pharmacy technician), 7 patient access, health information management (HIM), and business office, and 6 facilities, environmental services, and dietary |
| Contracted clinicians (not employees) | An emergency physician group staffs the ED 24x7 and covers inpatients by day; a telehospitalist service covers nights; a consultant pharmacist (on site 20 hours a week) plus a telepharmacy service for after-hours order verification; a teleradiology group reads all imaging; agency nurses fill about 4 shifts a week; 6 local physicians hold medical staff privileges |
| Patients | About 7,300 ED visits a year (about 20 a day), an average daily inpatient and swing-bed census of 7, and about 24,000 outpatient laboratory and imaging encounters a year. The EHR holds records for about 38,000 individuals |
| Revenue | $28.2 million a year (fictional), about $77,000 a day. Under the SBA standard of $47.0 million for NAICS 622110 (13 CFR 121.201), so SBA-small. Revenue per employee is high because Medicare pays CAHs on a reasonable-cost basis and much of the clinical labor is contracted rather than employed |
| Payers | Medicare (about 55% of revenue), Florida Medicaid, commercial plans. Medicare Part A and Medicaid are federal financial assistance, so Section 1557 of the Affordable Care Act applies (45 CFR Part 92) |
| HIPAA status | **Covered entity.** A health care provider that transmits claims electronically through a clearinghouse (45 CFR 160.103) |
| Other federal status | Medicare-participating CAH: the CAH conditions of participation apply, including emergency preparedness (**42 CFR 485.625**, the CAH counterpart of the hospital rule at 482.15). EMTALA applies because 42 CFR 489.24(b) defines "hospital" to include a CAH. The hospital uses certified EHR technology and takes part in the Medicare Promoting Interoperability Program for CAHs (42 CFR 495.24) |
| Not in scope | **42 CFR Part 2** (excluded by scoping decision, and screened as not applicable): the hospital has no unit or staff that holds itself out as providing substance use disorder diagnosis, treatment, or referral, so it is not a Part 2 program. ED care for overdoses is general medical care. If Part 2 records are ever received from an outside program, HIM flags them and the Privacy Officer handles them case by case; that path is outside this sample. **FTC Health Breach Notification Rule**: does not apply to HIPAA covered entities (16 CFR 318.1). **Group health plan** requirements (164.314(b)): the employee health plan is fully insured, and the hospital as plan sponsor receives only summary health information and enrollment information, which 164.314(b)(1) excludes. **Payment cards**: patient payments use a vendor-hosted, point-to-point encrypted terminal service outside the ePHI systems |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Governing body (chaired by the majority owner, Cris Santos) | Accepts High and Very High risks; approves the security budget; receives quarterly security and emergency preparedness reports |
| Chief Executive Officer (CEO) | Executive owner of the security program; accepts risk up to Moderate; signs policies; with the Director of Nursing and the ED physician on duty, decides ambulance diversion |
| Chief Financial Officer (CFO) | Vendor contracts and BAAs; cyber insurance; revenue cycle oversight |
| Director of Nursing | Clinical downtime lead for nursing units and the ED; co-owner of the downtime procedures |
| Quality and Compliance Manager | HIPAA **Privacy Officer**; Section 1557 Coordinator (45 CFR 92.7); breach determinations |
| IT Manager | HIPAA **Security Officer** (45 CFR 164.308(a)(2)); runs IT with one IT Support Specialist and a contracted managed service provider |
| IT Support Specialist | Help desk, account changes, endpoint builds, backup checks |
| Facilities Manager | Building and clinical operational technology (OT); generator; **Emergency Preparedness Coordinator** for the 485.625 program |
| HIM Manager | Medical records, release of information, downtime record reconciliation |
| Business Office Manager | Revenue cycle; clearinghouse relationship |
| HR Manager | Onboarding, terminations, and workforce clearance for employees; tracks agency staff start and end dates |
| Laboratory Manager and Imaging Manager | Laboratory information and analyzer workflows; CT, X-ray, and imaging archive workflows |
| Chief of Medical Staff (contracted emergency physician) | Clinical lead for the sepsis prediction model (P10) and for clinical decision support; chairs the medical staff quality committee |
| Managed service provider (MSP) | Network and server administration, patching, EDR console, business-hours alert monitoring. A business associate |

## 3. Systems

| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Hospital EHR (ED, inpatient and nursing documentation, order entry, eMAR with barcode medication administration, pharmacy, laboratory information module, patient accounting, patient portal) | EHR vendor-hosted (SaaS) | Yes | System of record. Certified health IT. The vendor is a business associate with a SOC 2 Type 2 report. Includes the vendor's sepsis prediction model (SYS-13) |
| SYS-02 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Also runs the on-premises directory synchronization. Protects email, remote access, and the cloud console. **On-site EHR sign-in uses a password only** |
| SYS-03 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | |
| SYS-04 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts three hospital-managed workloads: the imaging archive (PACS) and viewer, the interface engine, and the cloud backup vault |
| SYS-05 | Hospital network and server room | On-premises | Yes (in transit and on servers) | Firewall, core switch, Wi-Fi; one fiber internet circuit with a cellular backup on the firewall; site-to-site VPN to SYS-04 and to the EHR vendor. A virtualization host runs the directory server, file server, print server, analyzer middleware, dispensing cabinet server, and infusion pump drug-library server. One flat network for users, servers, medical devices, and building OT |
| SYS-06 | Endpoints | On-premises | Yes (cached) | 88 desktops and workstations on wheels, 12 laptops, 16 handheld barcode scanners. Two EHR downtime (read-only) PCs with local printers, one in the ED and one at the nursing station |
| SYS-07 | Medical devices | On-premises | Yes | CT scanner and acquisition workstation, digital X-ray, 14 wireless infusion pumps, patient monitors with a central station (ED and inpatient), chemistry and hematology analyzers, 2 automated dispensing cabinets, point-of-care glucose meters |
| SYS-08 | Building and clinical OT | On-premises | Limited (nurse call shows patient names and rooms) | Nurse call, building automation (HVAC, including the negative-pressure room and pharmacy and lab temperatures), medical gas alarms, generator monitoring. Owned by the Facilities Manager |
| SYS-09 | Clearinghouse | Vendor SaaS | Yes | Business associate; claims and remittance |
| SYS-10 | Teleradiology group | Vendor | Yes | Business associate; images routed from the imaging archive. Vendor support uses a **shared VPN account without MFA** (see gaps) |
| SYS-11 | Telepharmacy service | Vendor | Yes | Business associate; remote pharmacists verify after-hours orders inside SYS-01 |
| SYS-12 | Reference laboratory, health information exchange (HIE), and public health interfaces | Vendors and the state health department | Yes | Send-out lab orders and results; HIE document exchange; electronic laboratory reporting, immunization, and syndromic surveillance feeds through the interface engine. The reference lab and HIE are business associates; public health reporting is a permitted disclosure |
| SYS-13 | Sepsis prediction model | Feature of SYS-01 (EHR vendor) | Yes | Predictive decision support that scores adult ED and inpatient encounters and alerts nurses. **Live since 2026-03-02** without local validation (see P10) |
| SYS-14 | Cloud fax service (HIM) | Vendor SaaS | Yes | Records requests and transfers. **No BAA on file** |

**SSP system (P02):** the *Hospital Clinical Information System (HCIS)*: the hospital's configuration and use of SYS-01 (including SYS-13), SYS-02, SYS-04, SYS-05, SYS-06, SYS-07, and their interfaces to SYS-09 through SYS-12. SYS-08 building OT shares the network and is covered in P01 and P04, but it is a separate system owned by the Facilities Manager.

## 4. Current security posture: partially compliant

**In place today:**
- MFA for email, remote access for employees, the identity provider, and the cloud console
- Unique EHR accounts for employees and contracted clinicians, with role-based access from the vendor role catalog
- BAAs with the EHR vendor, cloud provider, clearinghouse, MSP, teleradiology group, telepharmacy service, reference lab, and HIE
- EDR on servers and workstations (deployed in 2025), with alerts monitored by the MSP during business hours only
- Monthly OS patching of workstations and servers by the MSP
- Nightly backups of on-premises servers to a local backup appliance, copied to the cloud backup vault; daily snapshots of the cloud workloads
- The EHR vendor's own backups and disaster recovery
- An emergency preparedness program under 42 CFR 485.625, focused on hurricanes: plan reviewed in 2025, a community-based full-scale exercise with the county each year, and a second exercise (a mass-casualty tabletop)
- Generator inspection and testing by the Facilities Manager
- Annual HIPAA training for employees
- Full-disk encryption on laptops
- Badge access to the server room, pharmacy, and ED entrance
- A 2023 security risk analysis by a consultant, used for the Promoting Interoperability attestation

**Missing or weak, found in the 2026 assessments:**
1. The security risk analysis was last updated in 2023. It does not cover medical devices, building OT, or the cloud tenant (Required, 164.308(a)(1)(ii)(A)).
2. The emergency preparedness risk assessment and plan do not address a cyberattack or a prolonged EHR outage. There are no diversion criteria for an IT outage, and the medical documentation system required during emergencies (485.625(b)(5)) has never been exercised without the EHR.
3. Downtime procedures date from 2019. The two downtime PCs have never been tested, and staff have not practiced paper workflows.
4. Backups are exposed: the local backup appliance is joined to the hospital directory, the cloud vault sits in the production account and region without immutable retention, and the imaging archive has never been restore-tested.
5. The network is flat. Medical devices, building OT, servers, and user workstations share one network.
6. Medical device security is unmanaged: the CT acquisition workstation runs an unsupported operating system, the infusion pump drug-library server is unpatched, and no manufacturer disclosure statements (MDS2) or device network inventory exist.
7. EDR alerts are watched only during business hours. There is no central log collection, and EHR access reports are reviewed only after a complaint.
8. Shared generic accounts exist: the ED tracking board, the analyzer middleware workstation, and a nursing station "unit" login.
9. Access for contracted clinicians and agency nurses is not removed on time. The agencies do not report end dates reliably; 11 accounts of people no longer working at the hospital were active in July 2026.
10. Vendor remote access is weak: the teleradiology support connection uses a shared VPN account without MFA, and on-site EHR sign-in uses a password only.
11. Desktops and workstations on wheels are not encrypted.
12. There is no incident response plan or ransomware runbook, only a generic "IT outage" page in the emergency plan. No cyber tabletop has been held.
13. BAAs are missing for the biomedical equipment service contractor (which services devices that store ePHI) and the cloud fax service. Vendors get no security review.
14. The sepsis prediction model went live without local validation, a Section 1557 input-variable review (45 CFR 92.210(b)), or a named governance owner.
15. Contracted clinicians and agency nurses do not complete the hospital's security training, and there are no phishing exercises for anyone.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 secondary regulation | CMS emergency preparedness condition of participation for CAHs, 42 CFR 485.625, analyzed at paragraph level for its cyber-relevant parts. The voluntary HHS Healthcare and Public Health Cybersecurity Performance Goals (CPGs) are used as a self-benchmark (extra file `cpg-benchmark.csv`) |
| P08 incident | Ransomware forcing EHR downtime and ambulance diversion. Initial access through the teleradiology vendor's shared VPN account |
| P09 SOC 2 | The hospital is not a service organization, so there is no SOC 2 readiness in the usual sense. Instead: (a) a Security-only (CC1-CC9) self-benchmark against the Trust Services Criteria, and (b) a review of the EHR vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| P10 AI | The EHR vendor's sepsis prediction model (SYS-13) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Security risk analysis and gap analysis fieldwork |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (after-hours device testing 2026-08-05) |
| 2026-08-17 to 2026-08-21 | Sepsis model review (P10) and vendor SOC 2 report review (P09) |
| 2026-08-31 | Deliverables approved by the CEO; High risks accepted with treatment plans by the governing body |

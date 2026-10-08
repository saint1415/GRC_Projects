# Scenario facts: Cris Santos Company | Healthcare and Public Health | Small

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the Health Care (NAICS 62) samples, which describe physician practices. Where a fact comes from a regulation or standard, the citation is given.

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
| HIPAA status | **Covered entity**, determined in the intake obligations register (C-HPH-R01): the clearinghouse agreement covers standard electronic transactions (EV-023) |
| Other federal status | Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) from the license, certification and payer records (EV-023, EV-024, EV-034). Medicare-participating CAH: the CAH conditions of participation apply, including emergency preparedness (**42 CFR 485.625**, the CAH counterpart of the hospital rule at 482.15). EMTALA applies because 42 CFR 489.24(b) defines "hospital" to include a CAH. The hospital uses certified EHR technology and takes part in the Medicare Promoting Interoperability Program for CAHs (42 CFR 495.24) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): **42 CFR Part 2** (excluded by scoping decision, and screened as not applicable: the hospital is not a Part 2 program), the **FTC Health Breach Notification Rule** (16 CFR 318.1 excludes covered entities), and **group health plan** requirements (164.314(b)(1) exception) do not apply. **Payment cards**: patient payments use a vendor-hosted, point-to-point encrypted terminal service outside the ePHI systems |
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
| Managed service provider (MSP) | Network and server administration, patching, EDR console, business-hours alert monitoring (EV-012). A business associate |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Hospital EHR (ED, inpatient and nursing documentation, order entry, eMAR with barcode medication administration, pharmacy, laboratory information module, patient accounting, patient portal) | EHR vendor-hosted (SaaS) | Yes | System of record. Certified health IT. The vendor is a business associate with a SOC 2 Type 2 report. Includes the vendor's sepsis prediction model (SYS-13) |
| SYS-02 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Also runs the on-premises directory synchronization. Protects email, remote access, and the cloud console. On-site EHR sign-in is excluded from the MFA rule (EV-002) |
| SYS-03 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | |
| SYS-04 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Hosts three hospital-managed workloads: the imaging archive (PACS) and viewer, the interface engine, and the cloud backup vault |
| SYS-05 | Hospital network and server room | On-premises | Yes (in transit and on servers) | Firewall, core switch, Wi-Fi; one fiber internet circuit with a cellular backup on the firewall; site-to-site VPN to SYS-04 and to the EHR vendor. A virtualization host runs the directory server, file server, print server, analyzer middleware, dispensing cabinet server, and infusion pump drug-library server. One internal network carries users, servers, medical devices, and building OT (EV-014). The VoIP phone system also runs on this network; analog lines in the ED and at the nursing station and the county EMS radio in the ED are the only non-network voice paths |
| SYS-06 | Endpoints | On-premises | Yes (cached) | 88 desktops and workstations on wheels, 12 laptops, 16 handheld barcode scanners. Two EHR downtime (read-only) PCs with local printers, one in the ED and one at the nursing station |
| SYS-07 | Medical devices | On-premises | Yes | CT scanner and acquisition workstation, digital X-ray, 14 wireless infusion pumps, patient monitors with a central station (ED and inpatient), chemistry and hematology analyzers, 2 automated dispensing cabinets, point-of-care glucose meters |
| SYS-08 | Building and clinical OT | On-premises | Limited (nurse call shows patient names and rooms) | Nurse call, building automation (HVAC, including the negative-pressure room and pharmacy and lab temperatures), medical gas alarms, generator monitoring. Owned by the Facilities Manager |
| SYS-09 | Clearinghouse | Vendor SaaS | Yes | Business associate; claims and remittance |
| SYS-10 | Teleradiology group | Vendor | Yes | Business associate; images routed from the imaging archive. Vendor support uses a shared VPN account with a password only (EV-015) |
| SYS-11 | Telepharmacy service | Vendor | Yes | Business associate; remote pharmacists verify after-hours orders inside SYS-01 |
| SYS-12 | Reference laboratory, health information exchange (HIE), and public health interfaces | Vendors and the state health department | Yes | Send-out lab orders and results; HIE document exchange; electronic laboratory reporting, immunization, and syndromic surveillance feeds through the interface engine. The reference lab and HIE are business associates; public health reporting is a permitted disclosure |
| SYS-13 | Sepsis prediction model | Feature of SYS-01 (EHR vendor) | Yes | Predictive decision support that scores adult ED and inpatient encounters and alerts nurses. Enabled 2026-03-02 (EV-049; see P10) |
| SYS-14 | Cloud fax service (HIM) | Vendor SaaS | Yes | Records requests and transfers. No BAA located at intake (EV-022) |

Other business SaaS without ePHI (not given system IDs): payroll and time capture (used by the HR Manager, BP-11 in P05).

**SSP system (P02):** the *Hospital Clinical Information System (HCIS)*: the hospital's configuration and use of SYS-01 (including SYS-13), SYS-02, SYS-04, SYS-05, SYS-06, SYS-07, and their interfaces to SYS-09 through SYS-12. SYS-08 building OT shares the network and is covered in P01 and P04, but it is a separate system owned by the Facilities Manager.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the HIPAA Security Rule and 42 CFR 485.625** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports, walk-throughs, inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, security risk analysis and gap analysis fieldwork |
| 2026-07-27 to 2026-07-31 | Policies and the incident response runbook drafted from the gaps |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (after-hours device testing 2026-08-05): operating tests of controls already in place; design review of the draft policies and runbook |
| 2026-08-17 to 2026-08-21 | Sepsis model review (P10) and vendor SOC 2 report review (P09) |
| 2026-08-31 | Deliverables and policies approved by the CEO; High risks accepted with treatment plans by the governing body |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |

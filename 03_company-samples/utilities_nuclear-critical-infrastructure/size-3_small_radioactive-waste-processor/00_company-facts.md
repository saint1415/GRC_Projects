# Scenario facts: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given. This scenario is independent of the other sizes.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; Cris Santos is majority owner and President) |
| Business | Radioactive and hazardous waste processor (NAICS 562211). Receives low-level radioactive waste (LLRW), hazardous waste, and mixed waste from generators; surveys, sorts, volume-reduces (supercompaction and shredding), repackages, and ships it to licensed treatment and disposal facilities outside Florida. Also runs a disused sealed source recovery service: collects sealed sources that customers no longer use, consolidates them in a vault, and ships them to licensed recyclers or disposal sites |
| Location | Florida. One site (**the Plant**): processing building, sealed source vault, permitted hazardous waste container storage area, truck yard, and an administration building. Field service crews also work at customer sites |
| Workforce | 60 employees: 7 managers, 5 radiation safety staff (Radiation Safety Officer and 4 health physics technicians), 24 plant operators and waste technicians (including 2 shift leads), 4 maintenance and controls staff, 8 field services staff, 6 transportation staff (5 drivers and a dispatcher), 4 customer service and billing staff, 2 IT staff |
| Customers | About 450 active generator accounts: hospitals, universities, research laboratories, industrial gauge and radiography users, and 2 nuclear power plant operators (dry active waste volume reduction and on-site packaging support) |
| Revenue | $28.2 million a year (fictional). Under the SBA standard of $47.0 million for NAICS 562211 (13 CFR 121.201), so SBA-small |
| Radioactive materials license | **Specific license issued by the Florida Department of Health, Bureau of Radiation Control.** Florida is an NRC Agreement State (agreement effective 1964), so the State, not the NRC, licenses and inspects the company. The license authorizes receipt, possession, processing, storage, and transfer of LLRW and disused sealed sources under Chapter 64E-5, F.A.C. It authorizes an aggregated **category 2** quantity in the sealed source vault (10 CFR Part 37, Appendix A), and no category 1 quantity |
| Part 37 status | **Applies through a license condition.** Florida implements Part 37 by a standard license condition requiring compliance with 10 CFR Part 37, with listed exclusions (37.1, 37.3, 37.7, 37.9, 37.11(a)-(b), 37.13, 37.77(f), 37.105, 37.107, 37.109) and with "NRC" read as the Florida Department of Health for most purposes (Florida DOH letter to NRC, 2023-06-23, ADAMS ML23178A117). The vault holds disused **discrete sources**, so the radioactive waste exemption in 37.11(c) does not apply to it. The company has run a Part 37 program since its April 2023 license amendment. Vault inventory is typically 0.4 to 1.6 on the category 2 sum-of-fractions scale and reaches category 2 several times a year before quarterly outbound shipments |
| Hazardous waste status | Permitted hazardous waste storage facility (container storage and consolidation) under Florida's EPA-authorized RCRA program (base authorization effective 1985-02-12, 50 FR 3908; latest revisions 91 FR 14648, effective 2026-05-26; Chapter 62-730, F.A.C.). Uses the EPA e-Manifest system. Recordkeeping under 40 CFR Part 264 Subpart E (operating record, 264.73; records retention, 264.74) |
| Transportation | DOT hazmat shipper and carrier. Company trucks collect waste from customers (always below category 2 per shipment). Outbound category 2 shipments from the vault use an exclusive-use carrier with package tracking (10 CFR 37.79(a)(3)). Because it offers category 2 shipments, the company must have a DOT hazmat security plan (49 CFR 172.800(b)(15)) |
| Not in scope | **10 CFR 73.54 and 73.77** (the company is not a power reactor licensee under Part 50 or 52); **10 CFR 73.110** (not a Part 53 licensee); **NERC CIP** (not a NERC-registered entity); **Safeguards Information** (10 CFR 73.21: the company does not produce, receive, or acquire SGI; reactor customers do not share it); **10 CFR Part 110 and Part 810** (no import or export); **CIRCIA** (proposed only; as proposed, the company is below the SBA size standard and meets no sector criterion); **HIPAA** (customer contracts require generators to remove patient identifiers from waste; the company performs no function involving PHI) |
| Contract flow-down | The 2 power reactor customers' contracts require company field staff to follow the reactor site's access authorization and its cyber security program rules for portable media and devices, and forbid connecting company devices to plant networks. These are contract terms that flow from the customers' own 10 CFR 73.54 programs; they do not make the company a 73.54 licensee |
| State law approach | Florida is cited where it is the licensing authority (Chapter 64E-5, F.A.C., and the Part 37 license condition) and for breach notification (Fla. Stat. 501.171). The samples otherwise stay federal |

### Regulatory driver IDs used in this sample
The vertical's `requirements.csv` lists power reactor and grid rules (C-NUCLEAR-R01 to R05). None of them applies directly to this business (P03 section 1). To keep traceability, this sample adds **scenario-level driver IDs (C-NUCLEAR-S01 to S06)** for the rules that do apply. They are defined here and nowhere else.

| ID | Requirement | Citation | Status for this company |
|---|---|---|---|
| C-NUCLEAR-R01 | NRC cyber rule for power reactors | 10 CFR 73.54 | Not applicable (cited only in P03 applicability rows) |
| C-NUCLEAR-R02 | Part 53 cyber rule | 10 CFR 73.110 | Not applicable |
| C-NUCLEAR-R03 | NRC cyber security event notifications | 10 CFR 73.77 | Not applicable |
| C-NUCLEAR-R04 | NERC CIP | 16 U.S.C. 824o; 18 CFR Part 40 | Not applicable |
| C-NUCLEAR-R05 | CIRCIA (proposed) | Proposed 6 CFR Part 226 | Not in effect; not covered as proposed |
| **C-NUCLEAR-S01** | Physical protection of category 1 and 2 quantities, including protection of security-related information | 10 CFR Part 37, imposed by the Florida license condition | **Applies (primary regulation in P03)** |
| C-NUCLEAR-S02 | Florida radiation control rules | Chapter 64E-5, F.A.C. (for example 64E-5.320 security of stored sources; 64E-5.332 transfer for disposal and manifests; 64E-5.343 reports of stolen, lost, or missing sources; 64E-5.344 notification of incidents) | Applies |
| C-NUCLEAR-S03 | DOT hazmat transportation security plan | 49 CFR 172.800-172.804 | Applies (category 2 shipments) |
| C-NUCLEAR-S04 | RCRA permitted facility manifest system and records | 40 CFR Part 264 Subpart E, through Chapter 62-730, F.A.C. | Applies |
| C-NUCLEAR-S05 | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (OT) | Voluntary benchmark | Adopted by management as the cybersecurity benchmark for OT and security systems |
| C-NUCLEAR-S06 | Florida breach notification | Fla. Stat. 501.171 | Applies to personal information (employee and background investigation data) |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| President (majority owner) | Accepts High and Very High risks; approves the security budget; senior management official for the DOT security plan (49 CFR 172.802(b)(1)) |
| General Manager | Executive owner of the security and compliance program; accepts risk up to Moderate; signs policies; **the individual with overall responsibility for the Part 37 security program** (37.43(a)(2)); second Part 37 reviewing official |
| Radiation Safety Officer (RSO) | Named on the license; Part 37 reviewing official (37.23(b)); runs the access authorization program, security zone, weekly source verification, and LLEA coordination |
| IT Manager | Cybersecurity lead with part-time compliance duties; manages the MSP; SSP owner (P02) |
| Operations Manager | Owns plant processing and the plant OT systems |
| Maintenance and Controls Supervisor | Maintains PLCs, HMIs, and the historian; business owner of the predictive maintenance pilot (P10) |
| Compliance and Transportation Manager | RCRA permit, e-Manifest, DOT hazmat and the DOT security plan, shipment coordination records |
| HR Manager | Hiring, terminations, background investigation file custody with the RSO |
| Controller | Billing and accounting |
| Customer Service Manager | Customer portal, waste profiles, certificates of processing |
| Field Services Supervisor | Field crews, including work at the 2 reactor sites |
| Managed service provider (MSP) | Help desk, patching, endpoint detection and response (EDR) monitoring for office endpoints; no access to OT |
| Alarm monitoring company | Central station monitoring of the vault intrusion detection system (37.49(a)(2)(i)) |
| Controls integrator | PLC and HMI vendor support, including remote support |

**Approved for unescorted access to the vault (Part 37 list): 14 people** (RSO, General Manager, 4 health physics technicians, 2 shift leads, 3 senior waste technicians, Operations Manager, Field Services Supervisor, Compliance and Transportation Manager).

## 3. Systems

| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Productivity suite (email, files, chat) | SaaS | Yes | Holds the Part 37 security plan, implementing procedures, and the approved-individuals list in a general "Radiation Safety" folder (see gaps) |
| SYS-02 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | Protects SYS-01, SYS-03, SYS-04, SYS-05, and the cloud console |
| SYS-03 | Waste tracking and customer portal | Vendor SaaS | Yes | System of record for customer accounts, waste profiles, container tracking, manifests, and certificates of processing. Vendor has a SOC 2 Type 2 report (P09) |
| SYS-04 | Accounting and billing | Vendor SaaS | Yes | Invoicing, receivables, payables |
| SYS-05 | HR and payroll | Vendor SaaS | Yes (PII) | Employee records, payroll |
| SYS-06 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes | Three company-managed workloads: the **source inventory application** (sealed source and radionuclide inventory, sum-of-fractions calculation, weekly verification records), the **records archive** (license, RCRA operating record, training and shipment records in object storage), and the **backup vault** |
| SYS-07 | Site business network and endpoints | On-premises | Yes (cached) | Firewall, switches, Wi-Fi; 44 laptops and desktops, 18 rugged plant-floor tablets, 6 truck tablets |
| SYS-08 | Plant OT network | On-premises | No | 5 PLCs (supercompactor, shredder, conveyor, drum handling, exhaust ventilation fans), 4 HMIs, a process historian server, an engineering workstation, and a vendor remote access appliance |
| SYS-09 | Radiation monitoring systems | On-premises | No | Area monitors, vehicle portal monitor at the gate, stack effluent monitor; data to a monitoring workstation on the OT network |
| SYS-10 | Physical security systems | On-premises plus central station | Yes (access lists) | Vault intrusion detection system (IDS) with a dual-path communicator (internet primary, cellular alternate) to the alarm monitoring company; physical access control system (PACS) server and door controllers; 22 IP cameras and a network video recorder (NVR) |
| SYS-11 | EPA e-Manifest accounts | Federal system | Yes | 3 company users |
| SYS-12 | Fleet telematics | Vendor SaaS | Low | Truck location tracking |
| SYS-13 | Predictive maintenance service | Vendor SaaS plus on-site sensor gateway | No | Pilot since April 2026 on 6 non-safety assets (see P10). The sensor gateway uses its own cellular link |

**SSP system (P02):** the *Business Operations and Records Platform (BORP)*: SYS-01, SYS-02, SYS-03 (company configuration), SYS-04, SYS-05, SYS-06, SYS-07 (including the PACS server and NVR while they remain on the business network), and the interfaces to SYS-11 and SYS-12. The OT and security systems (SYS-08, SYS-09, the rest of SYS-10, SYS-13) are interconnected systems outside the boundary; they are benchmarked in P03 against CSF 2.0 and SP 800-82 Rev. 3.

## 4. Current security posture: partially compliant

**In place today:**
- MFA through the identity provider for email, files, the waste tracking system, accounting, HR, and the cloud console
- A written Part 37 security plan (Rev. 2, 2024), approved by the General Manager, with implementing procedures
- Vault IDS monitored by the alarm monitoring company, with a cellular alternate path
- A Part 37 access authorization program: fingerprinting through the NRC, background investigations, two reviewing officials, 14 approved individuals
- Annual LLEA coordination with the county sheriff (last 2026-03-12)
- Annual Part 37 security training
- EDR on office laptops and desktops, monitored by the MSP
- Full-disk encryption on laptops and desktops
- A site firewall; the OT network is on its own VLAN behind firewall rules
- Daily backups of the cloud tenant workloads, and the SaaS vendors' own backups
- Annual security awareness training (no phishing exercises)

**Missing or weak, found in the 2026 assessments:**
1. The Part 37 security plan, implementing procedures, and approved-individuals list sit in a general "Radiation Safety" folder readable by 23 users, 9 of whom are not approved individuals. There is no written information protection procedure and no list of people approved to see this information (37.43(d)).
2. The PACS server and NVR are on the flat business network. A business network outage or ransomware event would take down badge control and video at the same time, and neither has an alternate path (37.49(c)).
3. The process historian is dual-homed on the OT network and the business network, which bypasses the OT firewall.
4. The controls integrator reaches the OT network through an always-on remote access appliance with one shared account and no MFA.
5. No OT asset inventory or network diagram. PLC program backups were last taken in 2024.
6. No written cyber incident response plan for OT and security systems. The Part 37 event reporting procedure names the NRC Operations Center instead of the Florida Bureau of Radiation Control and does not address suspicious cyber activity (37.57).
7. Scanned background investigation records sit in an HR folder that the payroll clerk can open. There is no written procedure for electronic copies (37.31).
8. Unescorted access removal is not tied to HR terminations. One of 3 departures in the last 12 months took 12 working days to remove from the list and the PACS (37.23(e)(5) allows 7).
9. The annual access authorization program review is overdue (last 2024-11; 37.33). The 2025 security program review did not look at the electronic security systems (37.55).
10. Cloud backups are in the same account and region as production, are not immutable, and have never been restore-tested. This includes the source inventory records (37.101).
11. No vulnerability scanning. PACS and camera firmware have not been updated since installation in 2023. Two HMIs run an unsupported operating system.
12. Category 2 shipment coordination records (no-later-than arrival times) are kept only in individual mailboxes, with no retention rule (37.75(e)).
13. The predictive maintenance vendor installed a sensor gateway with its own cellular link, outside the site firewall, without a security review.
14. No approved-tools list for generative AI. Customer service staff draft letters with public chatbots.
15. Five IP cameras still use the manufacturer's default admin password (found during P07 testing).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | Primary: 10 CFR Part 37 as imposed by the Florida license condition. Secondary: NIST CSF 2.0 with SP 800-82 Rev. 3 for OT and security systems (voluntary benchmark). 10 CFR 73.54 recorded as not applicable |
| P08 incident | Cyber attack on the site business network (phished credentials, then hands-on-keyboard activity) with an attempted pivot to the plant OT network and the physical security systems |
| P09 SOC 2 | The company is not a SOC 2 service organization. (a) Security-only self-benchmark against the Trust Services Criteria, used to answer a reactor customer's supplier security questionnaire; (b) review of the waste tracking vendor's SOC 2 Type 2 report |
| P10 AI | Predictive maintenance for non-safety plant equipment (pilot) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork (Plant walkthrough 2026-07-21) |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork |
| 2026-08-31 | Deliverables approved by the General Manager (High risks by the President) |

# Scenario facts: Cris Santos Company | Manufacturing | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or FDA guidance, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (medical device startup) |
| Business | Designs a wireless patient-monitoring system (NAICS 334510, Electromedical and Electrotherapeutic Apparatus Manufacturing) and is preparing its **first FDA premarket submission**. Production is outsourced to a contract manufacturer. The company is the manufacturer of record: it owns the design, the specifications, the software, and the regulatory submission |
| Location | Florida. One leased office suite with a small engineering lab |
| Workforce | 7 employees: Founder and CEO (owner), Head of Engineering, Firmware Engineer, Cloud Software Engineer, Verification and Test Engineer, Quality and Regulatory Manager, Operations Manager |
| Receipts | About $1.1 million a year (fictional), mostly from a paid development and evaluation agreement with a hospital system partner. Operating losses are funded by seed investment. SBA-small (standard for NAICS 334510: 1,250 employees; 13 CFR 121.201) |
| Product | **WM-1 wireless monitoring system** (in development; no units sold). Three parts: (1) the **WM-1 sensor**, a wearable chest sensor that measures heart rate (single-lead ECG), respiratory rate, skin temperature, and body position and sends them over Bluetooth Low Energy (BLE); (2) the **WM-1 hub**, a bedside unit that receives sensor data, shows vital signs, sounds local alarms, and connects to hospital Wi-Fi; (3) the **WM-1 cloud service**, which gives clinicians a web dashboard and secondary alert notifications and distributes signed firmware updates. Intended for adult patients on general hospital wards. Primary alarms always sound at the bedside hub |
| Regulatory status | Expected class II; a 510(k) is planned, with a predicate identified by the regulatory consultant. **Target submission date: 2027-03-31.** A pre-submission (Q-Submission) request to discuss the cybersecurity approach is planned for 2026-11. FDA establishment registration and device listing (21 CFR Part 807; 807.20(a)(1) covers a person who develops specifications for a device made by a second party) will be completed before commercial distribution, with timing confirmed by the regulatory consultant |
| Section 524B | FD&C Act section 524B (21 U.S.C. 360n-2) applies to the planned 510(k). WM-1 includes software and firmware, connects to the internet (Wi-Fi, BLE, and the cloud service), and could be vulnerable to cybersecurity threats, so it meets all three parts of the "cyber device" definition in 524B(c) |
| Quality system | The QMSR (21 CFR Part 820, which incorporates ISO 13485 by reference) took effect **2026-02-02** (final rule 89 FR 7496, 2024-02-02). It applies to the company because it designs the finished device: 820.1(a) and the 820.3 definition of manufacturer include specification development. Design and development controls (ISO 13485 clause 7.3) apply to class II devices (820.10(c)). Outsourcing production does not move these duties to the contract manufacturer |
| Units in existence | 30 pre-production sets (sensor plus hub) from a pilot build at the contract manufacturer in May 2026: 22 in the company lab for design verification, and 8 at the partner hospital's clinical simulation center for formative usability testing and network interoperability testing on the hospital's test network (since 2026-06-15). **No patient has been connected, and no patient data exists** |
| HIPAA status | **Not a covered entity or business associate today.** The company holds no PHI. After clearance, patient data sent by hospital customers' WM-1 units to the cloud service will make the company a business associate (45 CFR 160.103). BAAs and a HIPAA Security Rule program must be in place before the first clinical deployment. Tracked as a planned obligation |
| Not in scope | DFARS 252.204-7012, CMMC, ITAR (N31-33-R01 to R03): no defense work. EAR (N31-33-R04): U.S. sales only; export classification is outside these samples. SEC disclosure rules: privately held. FAR 52.204-25: no federal contracts. CIRCIA: proposed rule only. FTC Health Breach Notification Rule: the product is sold to hospitals and is not a consumer personal health record |
| Regulatory driver IDs | **N31-33-R05** (FD&C Act 524B) is the primary driver. FDA regulations are cited directly (21 CFR 803, 806, 807, 820) |
| State law approach | Florida law is cited only where unavoidable: Fla. Stat. 501.171 for personal information the company holds about its own workforce |

## 2. People (role titles only)
| Role | Security, product security, and compliance duties |
|---|---|
| Founder and CEO (owner) | Accepts risk at every level; approves policies, the security budget, and the submission |
| Head of Engineering | System architecture and hardware. **Product Security Lead** (part-time): threat model, SBOM, vulnerability intake, and custodian of the firmware signing key |
| Firmware Engineer | Sensor and hub firmware, secure boot, BLE link |
| Cloud Software Engineer | WM-1 cloud service and CI/CD pipeline; administers the cloud tenant and the source code repository |
| Verification and Test Engineer | Design verification; coordinates third-party security testing |
| Quality and Regulatory Manager (QA/RA Manager) | Owns the QMS and the 510(k); **owns section 524B compliance**; supplier control of the contract manufacturer; complaint handling (procedure drafted) |
| Operations Manager | Supply chain and contract manufacturer logistics, finance and HR administration. **Information Security Coordinator** for corporate IT: the MSP contact, onboarding and offboarding, cyber insurance |
| Managed service provider (MSP) | Laptops, productivity suite administration, office network, endpoint detection and response (EDR), patching |
| Contract manufacturer (CM) | ISO 13485-certified electronics manufacturer in another U.S. state. Builds units; its test stations load signed firmware and write device configuration |
| Regulatory consultant (fractional) | 510(k) strategy; reviews cybersecurity documentation before submission |

**Where roles overlap.** The Head of Engineering designs the system and also leads product security, so the same person builds and checks. This is compensated by a third-party penetration test before submission, the regulatory consultant's review, and an independent assessor for P07. The CEO both approves spending and accepts risk; the QA/RA Manager records each acceptance in the risk register.

## 3. Systems
| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Source code repository and CI/CD service | SaaS | Source code, build logs | Firmware and cloud code; hosted build runners. MFA enforced for the organization. Dependency alerts on cloud code only |
| SYS-02 | eQMS and PLM | SaaS | Design history file, risk management file, supplier records | Document control, requirements, design reviews, complaint module (not yet used) |
| SYS-03 | Productivity suite (email, files, chat) | SaaS | Contracts, HR records, investor documents | Built-in identity with MFA; single sign-on to SYS-02 only. The repository and the cloud console use separate logins |
| SYS-04 | WM-1 cloud service (pre-production) | Public cloud tenant (PaaS), vendor-agnostic | Simulator and test data only; firmware images | Ingestion API, clinician dashboard, update service, managed database, object storage, key management service. Development and pre-production share one tenant |
| SYS-05 | Endpoints | On premises and remote | Local code clones; test data | 7 laptops (MSP-managed: full-disk encryption, EDR, monthly patching) and 2 lab workstations (**not MSP-managed**; shared local login; used to flash units and run bench tests) |
| SYS-06 | Office and lab network | On premises | In transit | Small-business firewall, staff Wi-Fi, guest Wi-Fi, and a lab bench network. **The lab network is flat with the office network** |
| SYS-07 | Firmware signing key and release tooling | Head of Engineering's laptop | Signing private key | **The private key is a password-protected file on one laptop**, with a copy on an encrypted USB drive in the office safe. One person signs; no HSM |
| SYS-08 | WM-1 pre-production units | Company lab; partner hospital simulation center | Test data | Hub: embedded Linux, secure boot, signed updates. Sensor: real-time operating system (RTOS), signed updates verified by its bootloader. **Hub maintenance web page uses the same default password on every unit. Hub-to-cloud authentication uses one shared API key per environment. Sensor-to-hub BLE pairing uses the unauthenticated "Just Works" method** |
| SYS-09 | Contract manufacturer's MES and test stations | CM facility | Firmware images; hub provisioning file | Outside the company's control. Firmware images and the provisioning file (which contains the hub API key) are sent through a shared folder link from SYS-03 |

**SSP system (P02):** the *Product Development and Release Platform (PDRP)*: SYS-01 to SYS-07, the systems that design, build, sign, test, and distribute WM-1 software, with interfaces to the pre-production units (SYS-08) and the contract manufacturer's MES and test stations (SYS-09, external).

## 4. Current security posture: informal, with big gaps
**In place today:**
- QMS procedures in the eQMS (design controls, risk management, document control, supplier control), adopted in 2025; design history file started
- Quality agreement with the ISO 13485-certified contract manufacturer
- Signed firmware: the hub verifies its firmware at boot and before installing an update; the sensor bootloader verifies sensor updates
- TLS 1.2 or higher from hub to cloud; provider-managed encryption at rest in the cloud tenant
- MFA on the productivity suite, the source code repository, and named cloud console accounts
- MSP-managed laptops with full-disk encryption, EDR, and monthly patching
- One-reviewer code review required on the main branch
- Dependency alerts on cloud code
- Regulatory consultant engaged; a checklist against FDA's premarket cybersecurity guidance (issued 2026-02-03) started
- Cyber liability insurance (bought 2026-04 at an investor's request) with a 24x7 breach hotline and panel vendors
- MSP onboarding security video

**Missing:**
1. No system threat model. An engineering spreadsheet covers the sensor-to-hub radio link only; the hub-to-cloud path, update service, contract manufacturer provisioning, and cloud are not modeled. There is no cybersecurity risk assessment separate from the safety risk file.
2. No SBOM. Third-party software (the hub's embedded Linux distribution, the sensor RTOS, the BLE stack, a TLS library, and open-source libraries) is listed in a spreadsheet without versions, support status, or end-of-support dates.
3. No cybersecurity management plan, no coordinated vulnerability disclosure (CVD) policy, no published security contact, and no vulnerability monitoring.
4. The firmware signing key is a file on one laptop; one person can sign; no HSM and no second approval.
5. Every hub has the same default maintenance password, and hubs authenticate to the cloud with one shared API key per environment.
6. Sensor-to-hub BLE pairing is unauthenticated ("Just Works"), with no application-layer authentication.
7. No security testing beyond functional verification: no static analysis on firmware, no fuzzing, no penetration test (a third-party test is budgeted for 2026-12).
8. The contract manufacturer quality agreement has no cybersecurity terms. Firmware images and the provisioning file are sent by shared link.
9. The cloud tenant has one shared owner account known to two people; development and pre-production share one tenant; activity logs are kept for the 90-day default; database backups have never been restore-tested.
10. The 2 lab workstations are unmanaged (shared local login, no EDR, not patched), and the lab network is flat with the office network.
11. No written security policies (only a two-page MSP "IT rules" sheet), no incident response plan, and no product security incident procedure.
12. Offboarding is informal: the Operations Manager emails the MSP. Repository and cloud accounts are not on any checklist.
13. No security training beyond the MSP onboarding video; no secure coding training.
14. No inventory of devices, cloud resources, and software components.
15. No AI governance: engineers paste code into public AI chatbots, and AI-001 feasibility work uses a licensed research video dataset whose terms have not been reviewed.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 SSP | Product Development and Release Platform (PDRP) |
| P03 regulation | FD&C Act section 524B, with the FDA regulations that carry it (21 CFR Part 820; Parts 803 and 806 after marketing) and FDA's premarket cybersecurity guidance issued 2026-02-03. Focus: **premarket readiness** (threat model, SBOM, cybersecurity management plan) |
| P04 cloud | SaaS plus one cloud workload: the WM-1 cloud service on a PaaS tenant. Vendor-agnostic |
| P05 BIA | 9 business functions (BP-01 to BP-09) |
| P07 assessment | 13 controls on the PDRP and the release path, by an independent medical device cybersecurity consultant |
| P08 incident | Exploited vulnerability in a fielded WM-1 hub (the shared maintenance password), with the MSP and the cyber insurer in the notification chain. Written for units after clearance; applies now to the 8 evaluation units |
| P09 SOC 2 | Security plus Availability readiness self-assessment for the partner hospital system's vendor security review; plus a review of the cloud provider's SOC 2 Type 2 report |
| P10 AI | AI-001: AI-enabled device software function that estimates respiratory rate from hub camera video (image analysis). Feasibility stage |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis (QA/RA Manager and Head of Engineering, with the regulatory consultant and the MSP) |
| 2026-08-10 to 2026-08-12 | Control assessment (independent consultant; lab testing on 2026-08-11) |
| 2026-08-24 | SOC 2 readiness self-assessment completed |
| 2026-08-26 | AI risk assessment completed |
| 2026-08-27 | Incident response tabletop exercise with the MSP and the insurer's panel counsel |
| 2026-08-31 | Deliverables approved by the CEO |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Operating cost | Monthly operating cost is about $190,000 (about $8,600 per business day), funded mainly by seed investment. Cash runway is about 14 months, so a slip in the submission date is the main business impact | P01, P05 |
| Partner hospital system | The partner hospital system funds the development and evaluation agreement, hosts the 8 evaluation units, and plans a post-clearance clinical pilot. Its vendor security review questionnaire is due back 2026-10-30 | P05, P08, P09 |
| Hub software | The hub runs an embedded Linux distribution with a local maintenance web page on the hospital network, used by field service to view logs and change network settings. It can also change alarm limit defaults | P01, P03, P08 |
| Hub camera | The hub has a near-infrared camera module that is disabled in WM-1 firmware. AI-001 would enable it in a later product version, after its own submission | P10 |
| Firmware updates | Hubs receive signed firmware from the update service in SYS-04. Sensors are updated through the hub. The contract manufacturer flashes the initial image and loads the provisioning file at its test stations | P02, P04, P08 |
| Former firmware contractor | A contract firmware developer's engagement ended on 2026-03-13. P07 testing on 2026-08-11 found the contractor's account still had write access to the firmware repository. It was removed that day; the repository audit log showed no pushes or clones after 2026-03-13 | P01, P07 |
| CI build logs | P07 testing found the hub API key printed in plain text in CI build logs, readable by every account with repository read access | P01, P04, P07 |
| Cloud provider | The cloud provider's SOC 2 Type 2 report (Security, Availability, Confidentiality; 12 months ending 2026-03-31) was obtained under NDA on 2026-08-18 | P04, P09 |
| MSP contract | Covers help desk, laptops, EDR, patching, productivity suite administration, office network, and firewall, with a 4-business-hour response time. It does not cover the lab workstations, the source code repository, or the cloud tenant | P02, P05, P07 |
| Cyber insurance | The policy requires notice through the 24x7 hotline before hiring outside firms and use of panel vendors (breach counsel, forensics). Coverage of product-related incidents at customers is limited; product liability is a separate policy | P08 |
| Assessor | The P07 assessor is an independent medical device cybersecurity consultant under a fixed-fee engagement, not involved in the risk assessment or the gap analysis and operating no control | P07 |
| Evaluation network | The 8 evaluation hubs sit on the simulation center's isolated test network, which the hospital's security team monitors | P01, P08 |
| Office security | Keyed suite entry with an after-hours alarm; the office safe holds the signing key backup USB drive; keys held by the CEO and the Operations Manager | P02, P03 |

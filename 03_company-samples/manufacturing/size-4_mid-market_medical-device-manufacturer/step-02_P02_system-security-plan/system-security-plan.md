# System Security Plan: Device Lifecycle Platform (DLP)

**Organization:** Cris Santos Company, Inc. (PE-backed connected medical device manufacturer) | **Tier:** Mid-Market | **Vertical:** Manufacturing (NAICS 334510)
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Device Lifecycle Platform (**DLP**), identifier CSC-DLP-01. The DLP is the company's major system. It comprises SYS-01 to SYS-09 in `../00_company-facts.md`: everything the company uses to design, build, sign, manufacture, release, update, and operate its connected devices.

## 2. System Overview
The DLP supports the device side of every process in the BIA (P05): the Connected Care Cloud (CCC) services for about 290 hospitals, product security and regulatory reporting, software build and code signing, and production on the four plant lines. It serves about 600 workforce users (engineering, plant, quality, support, and IT) and holds PHI for about 2.4 million patients on behalf of hospital customers.

The DLP matters beyond ordinary IT risk for two reasons:
- **Section 524B related systems.** The CCC update service, the build and signing pipeline, and the connections to hospital networks are what FDA calls "related systems" of the company's cyber devices (FDA premarket cybersecurity guidance, 2026-02-03, section VII.C.2). Section 524B(b)(2) requires processes that give a reasonable assurance that "the device and related systems are cybersecure."
- **The plant gives each device its identity.** Test stations load signed firmware, and the factory provisioning server issues each device's certificate. A compromise there reaches every device shipped.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Connected Care Cloud: device gateway, container services (ingestion, viewing, notifications, pump programming, AI-001 inference, HL7 and FHIR interfaces, update service), managed database, object storage, key management | Public cloud IaaS/PaaS, CCC production and non-production accounts (P04) |
| SYS-02 | Cloud landing zone: management, security and log archive, shared network, build and signing, CCC production, CCC non-production, backup | Public cloud, vendor-agnostic |
| SYS-03 | Identity provider with SSO, MFA, and conditional access | SaaS |
| SYS-04 | Source repositories (SaaS), CI/CD runners, SBOM store, HSM-backed code-signing service; VM-5 legacy signing key offline | SaaS plus the build and signing account |
| SYS-05 | Product lifecycle management (design history, risk files, threat models) | SaaS |
| SYS-06 | eQMS (complaints, MDR, corrections and removals, CAPA, CVD queue) | SaaS |
| SYS-07 | MES and plant OT: 2 MES servers, 14 MES terminals, 52 test and calibration stations, SMT and AOI equipment, line PLCs, historian, factory provisioning server, building management system | On premises, plant |
| SYS-08 | 780 laptops, 140 desktops, 3 engineering lab networks | Company-managed |
| SYS-09 | SIEM and EDR operated by the MSSP (a subcontractor business associate) | SaaS |

The ERP (SYS-10), productivity and support apps (SYS-11), fielded devices (SYS-12), third parties (SYS-13), and AI tools (SYS-14) connect to the DLP as external or interconnected systems (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the DLP |
|---|---|---|---|
| N31-33-R05 | FD&C Act section 524B, ensuring cybersecurity of devices | 21 U.S.C. 360n-2 | Primary driver. Postmarket vulnerability monitoring and CVD (b)(1); processes for device and related systems, and patches on a regular cycle and out of cycle (b)(2); SBOM (b)(3). Failure to comply with (b)(2) is a prohibited act (21 U.S.C. 331(q)(3)) |
| QMSR | Quality Management System Regulation | 21 CFR Part 820 (ISO 13485 incorporated by reference; effective 2026-02-02) | Design and development controls (820.10(c)) cover device and CCC software; production and process validation cover test station and calibration software; complaint records (820.35(a)) |
| FDA reporting | Medical device reporting; corrections and removals | 21 CFR Part 803; 21 CFR Part 806 | A cybersecurity event can be a reportable malfunction or require a correction report (P08) |
| FDA guidance | Premarket cybersecurity guidance (2026-02-03); postmarket cybersecurity guidance (2016) | Nonbinding | Sets FDA's expectations for threat modeling, SBOM content, architecture views, testing, management plans, and uncontrolled-risk handling |
| N62-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C | Applies to the CCC as a business associate (164.302) |
| N62-R03 | HIPAA Breach Notification Rule | 45 CFR 164.410 | Notice to hospital customers after discovery of a breach |
| Contract | 290 BAAs; CCC service agreements (99.9% availability); group purchasing contract (SOC 2) | Contracts | Notice terms, availability, SOC 2 Type 2 (P09) |
| State | State breach and third-party agent notice laws (Florida worked example: Fla. Stat. 501.171(6)) | Each state where affected individuals reside | Notice to hospitals (P08) |
| Benchmark | NIST SP 800-82 Rev. 3, Guide to OT Security (Appendix F OT overlay) | Nonbinding | Tailoring for plant components (section 10.1). Rev. 4 was released as an initial public draft on 2026-09-21 (comments due 2026-11-30) and is not used as the baseline |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Policy basis for every control |

Not applicable: DFARS 252.204-7012, CMMC, and ITAR (no defense work); EAR (U.S. sales only, not analyzed); SEC cybersecurity disclosure rules (privately held); HIPAA group health plan provisions (fully insured plan).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-17, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the DLP accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the IP-4 factory service mode correction (POAM-001) and the other High POA&M items meet their milestones; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (for example the AI-002 submission).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Plant OT segmentation of Line 1 and Line 3 and removal of the persistent vendor VPN (due 2027-03-31)
- Move of the factory provisioning issuing key into the HSM (due 2026-12-31)
- SIEM onboarding of the MES, provisioning server, build pipeline, and PLM, plus OT network monitoring (due 2027-03-31)
- Automated CCC regional failover (due 2027-03-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the DLP; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber and product security reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Security Officer | IT Director | Security Officer for IT and plant networks; designated HIPAA security official for the CCC (45 CFR 164.308(a)(2)) |
| Security operations and GRC | Security Manager and 2 security analysts | MSSP liaison, vulnerability management, GRC |
| Product security | Product Security Manager and 3 engineers | PSIRT, threat models, SBOMs, CVD, ISAO liaison |
| Section 524B and FDA reporting | VP QA/RA | 524B compliance, MDR and 806 decisions, FDA correspondence |
| Engineering owner | VP Engineering | Device and CCC software, SPDF, build and signing |
| CCC operations | Director of Cloud Operations | Production, backups, failover |
| Plant OT | Plant Manager; OT Engineering Manager | Lines, MES, test stations, provisioning server |
| Privacy | Compliance and Privacy Officer | BAAs, breach risk assessments, notices to hospitals |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP (subcontractor business associate) | 24x7 EDR and SIEM monitoring of IT and cloud |

**Where roles overlap.** The IT Director is both the HIPAA security official for the CCC and the owner of many controls this plan describes. The co-sourced internal audit firm, which reports to the audit committee, assesses those controls (P07), so the person who runs a control does not assess it. The vCISO reviews this plan but does not operate controls.

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (telemetry, alarms, infusion records, skin images; PHI held for hospitals) | Moderate | Moderate | Moderate | Disclosure is a reportable breach for hospitals. Altered data could delay a clinical response, but bedside alarms and pump safety limits stay on the device. P05 sets the MTD for remote monitoring at 4 hours |
| System maintenance (firmware, model files, drug libraries, update distribution) | Low | Moderate | Low | Released images are not secret, but a tampered image could cause harm. Devices reject unsigned images, which bounds integrity at Moderate for this boundary |
| Research and development (design files, source code, threat models) | Moderate | Moderate | Low | Trade secrets and unpatched vulnerability details; submissions can wait days |
| Production and quality records (device history records, test results, certificate issuance) | Low | Moderate | Moderate | Altered test records could release a nonconforming device; lots cannot ship without complete records (P05 BP-12) |
| Information security (audit logs, keys, certificates) | Moderate | Moderate | Low | Needed for investigations and breach determinations |
| **DLP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Integrity was considered for High.** A compromised signing key or provisioning server could affect every device shipped, which is a multi-patient harm scenario in FDA's terms. The team kept integrity at Moderate for three reasons: devices verify signatures before install, release signing needs two approvers in the HSM, and pumps enforce dose limits in the device. To compensate, the plan adds integrity tailoring (section 10.1) and treats the signing and provisioning paths as the highest-value assets in P01.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the 7 cloud accounts and the CCC workloads, keys, and backups;
- the identity provider tenant configuration;
- the source repositories' configuration, the CI/CD runners, the SBOM store, the HSM-backed signing service, and the offline VM-5 signing laptop;
- the PLM and eQMS tenants' configuration, roles, and records;
- the MES, test and calibration stations, SMT and AOI equipment, line PLCs, historian, factory provisioning server, and building management system;
- 920 endpoints and 3 engineering lab networks;
- the company's SIEM tenant and its use cases.

**Outside the boundary (interconnected):**
- fielded devices (SYS-12), operated by hospitals on hospital networks;
- hospital EHRs, interface engines, clinical communication systems, and identity providers;
- the cloud provider's, identity vendor's, repository vendor's, PLM vendor's, eQMS vendor's, and MSSP's platforms (inherited controls);
- the ERP (SYS-10) and productivity and support apps (SYS-11);
- the line equipment vendor's remote support service;
- the ISAO, CISA, and FDA electronic submission systems.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement / protection |
|---|---|---|---|
| VM-7 and IP-4 devices (SYS-12) | Inbound telemetry and infusion records; outbound settings, drug libraries, firmware | Vitals, alarms, pump events; signed firmware and libraries | Mutual TLS with per-device certificates |
| VM-5 devices (SYS-12) | Inbound telemetry | Vitals, alarms | TLS with a per-hospital shared API key (**gap**, R-013) |
| Hospital EHRs and clinical communication systems | Bidirectional | Orders to pumps, results, secondary notifications | BAA; HL7 and FHIR over TLS (259 hospitals) or site-to-site VPN (31 hospitals); **no written interconnection security terms for the 31 VPNs (gap, CA-3)** |
| Hospital identity providers | Inbound assertions | Clinician identities | Federation (212 hospitals) |
| ERP (SYS-10) | Bidirectional with MES | Work orders, serial numbers, UDI, shipments | ERP vendor SOC 2; API with service credentials |
| Line equipment vendor | Inbound remote support | Equipment diagnostics and programs | Persistent VPN appliance with a shared account (**gap**, R-020) |
| MSSP | Inbound logs; remote response actions | Security logs that can contain PHI fragments | Subcontractor BAA; SOC 2 Type 2 |
| ISAO | Bidirectional | Vulnerability and threat information, customer communications | Membership terms |
| Call-recording and field service scheduling vendors | Inbound support data | Case notes with occasional patient identifiers | **No subcontractor BAA (gap 10)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Device gateway and web front end with denial-of-service protection and web application firewall | Managed edge and load balancing | CCC production account | Director of Cloud Operations |
| Container platform (ingestion, viewing, notification, pump programming, AI-001 inference, interfaces, update service) | Managed container orchestration | CCC production account | Director of Cloud Operations |
| Clinical data store | Managed relational database with point-in-time recovery | CCC production account | Director of Cloud Operations |
| Images, reports, firmware, drug libraries | Object storage | CCC production account | Director of Cloud Operations |
| Data keys | Managed key service | CCC production account | Product Security Manager |
| Backup vault | Backup service with write-once retention | Backup account (second region) | Director of Cloud Operations |
| Network hub, cloud firewall, site-to-site VPN gateways | Network services | Shared network account | IT Director |
| Organization guardrails, posture management, log archive | Policy and security services | Management and security accounts | Security Manager |
| CI/CD runners, SBOM store, signing service with cloud HSM | Compute, storage, HSM | Build and signing account | VP Engineering |
| VM-5 legacy signing laptop (offline, in a safe) | Endpoint | Engineering vault room | Product Security Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| Repositories, PLM, eQMS tenants | SaaS | Vendors | VP Engineering; VP QA/RA |
| MES servers (2) and terminals (14) | Servers and workstations | Plant | Plant Manager |
| Test and calibration stations (52: Line 1: 10, Line 2: 14, Line 3: 20, Line 4: 8) | Workstations with fixtures | Plant | OT Engineering Manager |
| SMT and AOI equipment, line PLCs, historian, building management system | OT | Plant | OT Engineering Manager |
| Factory provisioning server (issuing CA key in software) | Server | Plant | Product Security Manager |
| Laptops (780), desktops (140), lab networks (3) | Endpoint and network | Campus and remote | IT Director |
| SIEM tenant | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The DLP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 120 controls** in `control-implementation.csv`: 113 from the Moderate baseline plus 7 added by tailoring. They cover every control that carries the section 524B processes for related systems, the HIPAA Security Rule for the CCC (Health Care crosswalk, an author mapping), and the risks rated Moderate or higher in P01.
- **Selected by tailoring (added, 7):** CA-8 (independent penetration testing, which FDA's premarket guidance expects for devices and related systems), CM-14 and SI-7(15) (signed components and code authentication, the core device integrity protections), PM-1, PM-2, PM-9 (program, leadership, and risk strategy, needed for HIPAA 164.308(a)(1)-(2) and 524B governance), and PM-15 (ISAO membership, a condition of FDA's enforcement-discretion policy).
- **OT overlay for plant components.** For SYS-07 the plan applies the SP 800-82 Rev. 3 Appendix F OT overlay guidance: compensating controls where a control would disrupt production (application allowlisting instead of EDR on test stations for SI-3; network isolation and monitoring instead of patching for unsupported test stations under SA-22; shared-station operator authentication replaced by badge-based individual login as the planned fix for IA-2). Rev. 4 (initial public draft, 2026-09-21) will be reviewed when final.
- **Integrity tailoring:** CM-3, CM-4, and CM-5 statements cover test station and calibration software changes, not only product changes, because R-049 showed a station script change can change what ships.
- **Inherited without separate statements:** the remaining Moderate-baseline physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17) and platform-level SC and SA controls. These are inherited from the cloud provider, identity vendor, repository vendor, PLM and eQMS vendors, and the MSSP, and are evidenced by their SOC 2 Type 2 reports, reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other Moderate controls with no HIPAA or 524B mapping and no Moderate-or-higher risk in P01 (for example AC-11 device lock on shared plant terminals, which is handled by the planned badge login). They are recorded as tailoring decisions and reviewed yearly.

**Status of the 120 documented controls:**
| Status | Count |
|---|---|
| Implemented | 45 |
| Partially implemented | 70 |
| Planned | 5 |
| Not applicable | 0 |

**Inheritance of the 120 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 78 | Company |
| Hybrid | 33 | Cloud provider, identity vendor, repository vendor, MSSP, hospital identity providers |
| Common/Inherited | 9 | Identity vendor (AC-2(1), AC-7, IA-2(1), IA-2(2)), cloud provider (AU-9, CP-6, SC-5, SC-13), MSSP (IR-7) |

The Partially implemented statements trace to the 15 gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 36 controls from 2026-08-10 to 2026-08-28 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** Users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. Administrators of cloud, identity, repositories, and the signing service use phishing-resistant hardware keys. This fits the Moderate categorization and the all-tenant reach of administrative access.
- **Plant floor.** MES terminals and test stations use shared operator logins today, which does not meet this statement. Badge-based individual login with a PIN is planned by 2027-03-31 (R-022; POAM-006).
- **Clinicians.** Clinicians authenticate through their hospital's identity provider (212 hospitals) or local portal accounts with MFA. Identity proofing of clinicians is the hospital's responsibility under the BAA.
- **Devices.** VM-7 and IP-4 authenticate with unique certificates. VM-5's shared per-hospital key does not meet this statement and is tracked in R-013. The factory provisioning key gap (R-010) affects the assurance of every device certificate until the key moves into the HSM.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10); design history files, threat models, and SBOMs (PLM).

## 13. Acronym List and Glossary
- **AOI:** automated optical inspection
- **BAA:** business associate agreement
- **CCC:** Connected Care Cloud
- **CVD:** coordinated vulnerability disclosure
- **DLP:** Device Lifecycle Platform
- **HSM:** hardware security module
- **ISAO:** information sharing and analysis organization
- **KEV:** CISA Known Exploited Vulnerabilities catalog
- **MDR:** medical device report (21 CFR Part 803)
- **MES:** manufacturing execution system
- **OT:** operational technology
- **PSIRT:** product security incident response team
- **QMSR:** Quality Management System Regulation (21 CFR Part 820)
- **SBOM:** software bill of materials
- **SMT:** surface-mount technology
- **SPDF:** secure product development framework

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | Security Manager with the Product Security Manager |
| 1.0 | 2026-09-17 | Updated with P07 results; approved by the Chief Operating Officer | IT Director (Security Officer) |

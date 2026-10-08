# System Security Plan: Hospital EHR and Clinical Systems (HECS)

**Organization:** Cris Santos Company, Inc. (PE-backed 112-bed community acute-care hospital) | **Tier:** Mid-Market | **Vertical:** Healthcare and Public Health
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Hospital EHR and Clinical Systems (**HECS**), identifier CSC-HECS-01. HECS is the hospital's major system. It comprises the hospital's configuration and use of SYS-01 to SYS-08 and SYS-10 in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv), and their interfaces to the external services in SYS-12.

## 2. System Overview
HECS supports every clinical process in the BIA (P05): emergency care, inpatient and critical care, women's services, surgery, pharmacy, laboratory and blood bank, imaging and the catheterization lab, patient access, and the affiliated practice program, at the main campus and the off-campus outpatient center. It serves 600 employees, about 280 independent physicians with privileges, contracted clinicians and agency nurses, and about 240 affiliated practice users, and it holds records for about 310,000 individuals.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Hospital EHR (ED, inpatient, eMAR, order entry, pharmacy, surgery, labor and delivery, patient accounting, HIM, portal, ambulatory module for the affiliated practices), including the sepsis prediction model (AI-001) | Vendor-hosted SaaS; vendor SOC 2 Type 2 |
| SYS-02 | Identity provider with single sign-on, MFA, and conditional access; on-premises directory | SaaS plus on-premises directory |
| SYS-03 | PACS and RIS, including the FDA-cleared stroke and hemorrhage triage software (AI-002) | Vendor-managed software in the hospital's cloud workloads account |
| SYS-04 | Cloud landing zone: management, security and log archive, shared services, workloads, and backup accounts; interface engine, data warehouse, file services | Public cloud IaaS/PaaS, vendor-agnostic (P04) |
| SYS-05 | On-premises data center: LIS with blood bank module, dispensing cabinet server, infusion pump server, monitoring gateway, fetal surveillance server, cardiology system, directory, file and print, downtime extract server, backup appliance | On-premises virtualization cluster (3 hosts) |
| SYS-06 | Campus and outpatient center networks, SD-WAN, Wi-Fi, two internet carriers | On-premises |
| SYS-07 | 960 workstations and laptops (including 260 workstations on wheels and 12 downtime workstations), 380 clinical smartphones, 120 barcode scanners | Hospital-managed |
| SYS-08 | About 1,650 networked medical devices | On-premises |
| SYS-10 | SIEM operated by the MSSP (a business associate), EDR, email security gateway | SaaS and MSSP |

Building and clinical OT (SYS-09) and clinical communications (SYS-11) share the campus network but are separate systems (section 7). Vendors and external connections (SYS-12) and AI tools (SYS-13) connect to HECS as external services (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects HECS |
|---|---|---|---|
| C-HPH-R01 | HIPAA Security Rule | 45 CFR Part 164, Subpart C | Primary control requirement; mapped in `control-implementation.csv` |
| C-HPH-R02 | HIPAA Breach Notification Rule | 45 CFR 164.400-164.414 | Logging and investigation must support breach determinations (P08) |
| C-HPH-R03 | HIPAA Security Rule NPRM | 90 FR 898 (2025-01-06) | **Proposed only.** Tracked in P03; not a current obligation |
| C-HPH-R04 | FDA premarket cybersecurity for cyber devices | FD&C Act sec. 524B, 21 U.S.C. 360n-2 | Binds manufacturers, not the hospital. Used in purchasing to obtain software bills of materials, vulnerability plans, and update support for SYS-08 |
| C-HPH-R07 | CMS emergency preparedness condition of participation | 42 CFR 482.15 | HECS must support the emergency plan, including a medical documentation system that preserves patient information, protects confidentiality, and keeps records available (482.15(b)(5)) and alternate communications (482.15(c)(3)) |
| C-HPH-R08 | HHS HPH Cybersecurity Performance Goals (voluntary) | HHS HPH CPGs | Self-benchmark in P03 `cpg-benchmark.csv`; cited in the driver column where a goal applies |
| C-HPH-R09 | HHS 405(d) HICP (voluntary) | Cybersecurity Act of 2015 sec. 405(d) | Practice reference for a medium-sized hospital |
| C-HPH-R10 | HITECH recognized security practices | 42 U.S.C. 17941 | Operating CPG and HICP practices for 12 months is a mitigating factor in any OCR enforcement |
| Other federal | Medical record services | 42 CFR 482.24(b) | Records retained at least 5 years, confidential, and protected from unauthorized access or alteration |
| Other federal | EMTALA | 42 CFR 489.24 | Screening and stabilization continue during any outage; diversion rules (P05, P08) |
| Other federal | Medicare Promoting Interoperability Program | 42 CFR 495.24 | Annual security risk analysis measure, satisfied through P01 |
| Other federal | Section 1557 patient care decision support tools | 45 CFR 92.210 | Applies to AI-001, AI-002, and AI-004 inside HECS (P10) |
| Other federal | FDA medical device reporting by user facilities | 21 CFR 803.30 | Device-related deaths and serious injuries, including those caused by a compromised device, reported within 10 work days (P08) |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Breach notification (P08) |
| Contract | Affiliated practice services agreements and BAAs | Contract | Access, availability, and breach notice commitments to 18 practices; SOC 2 Type 2 requested (P09) |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Policy basis for every control |

Not applicable:
- **42 CFR Part 2 (C-HPH-R06).** The hospital is not a Part 2 program (intake obligations register, C-HPH-R06; EV-047, EV-056).
- **FTC Health Breach Notification Rule (C-HPH-R05).** Covered entities and business associates acting as such are excluded (16 CFR 318.1).
- **HIPAA group health plan requirements (164.314(b)).** The employee health plan is fully insured, and the hospital as plan sponsor receives only summary health and enrollment information (P03).
- **CIRCIA (C-HPH-R11).** Proposed only. If finalized as proposed, it would cover this hospital because it has 100 or more beds (P03, P08).
- **PCI DSS scope.** Card payments use a validated point-to-point encryption service outside HECS (noted, not assessed).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-17, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The hospital is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of HECS accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** Chief Executive Officer for High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities). The Very High risk (P01 R-001) is under a 90-day CEO exception noticed to the audit committee chair, with treatment under way.
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (for example a new EHR, an acquisition, or a new care site).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Medical device and OT segmentation at the main campus (due 2027-06-30)
- Privileged access management for the directory, identity provider, EHR, PACS, LIS, and network devices (due 2027-03-31)
- Vendor remote access consolidated on the vendor access platform with MFA (due 2026-12-31)
- SIEM onboarding of the LIS, the on-premises clinical servers, the interface engine, and passive device monitoring (due 2027-03-31)
- IT disaster recovery plan and quarterly restore tests (first test 2026-10-20)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for HECS; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting; approves Very High exceptions |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Security Officer | IT Director | HIPAA Security Officer (45 CFR 164.308(a)(2)); day-to-day control owner |
| Security operations and GRC | Information Security Manager and 2 security analysts | Vulnerability management, MSSP oversight, SIEM use cases, GRC |
| Privacy Officer and Section 1557 Coordinator | Compliance and Privacy Officer | Privacy Rule, breach determinations, BAAs, 45 CFR 92.7 and 92.210 |
| Clinical oversight | Chief Medical Officer; Chief Nursing Officer | Clinical decision support and AI (CMO); nursing downtime and diversion decisions (CNO) |
| Medical devices | Director of Biomedical Engineering | Device inventory, maintenance, and device security with IT |
| Emergency preparedness | Director of Emergency Management | 482.15 program; integration of IT outage scenarios |
| Department owners | ED Director; Pharmacy Director; Laboratory Director; Imaging Director; HIM Director; Director of Revenue Cycle; Director of Physician Services | Downtime procedures and access approvals for their departments |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP (business associate) | 24x7 EDR and SIEM monitoring |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Health care delivery services (patient records, orders, medications, results, images, ePHI) | Moderate | Moderate | Moderate | Disclosure of records for up to 310,000 individuals is serious but not catastrophic to the organization; altered orders or results could harm a patient, but clinicians verify medications and allergies at each administration (barcode scanning, pharmacist verification); paper downtime procedures carry the first hours (P05 MTD 1-4 hours) |
| Health care administration (claims, eligibility, coding) | Moderate | Moderate | Low | Financial and identity data; payers accept late claims (P05 MTD 72 hours) |
| Health care research and practitioner safety (quality reporting, analytics) | Moderate | Low | Low | Aggregated reporting; can be rebuilt from the EHR |
| Human resources management (workforce and practice user identities) | Moderate | Low | Low | Account data; limited harm if unavailable |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for breach investigations and recovery validation |
| **HECS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Integrity and availability were considered for High.** A tampered infusion pump drug library or an altered blood bank record could contribute to death, and a network-wide outage forces diversion. The team kept both at Moderate for four reasons: clinicians independently verify medications at the bedside (barcode scanning and pharmacist verification), pumps run standalone on a validated library, blood products are re-verified at the bedside by two nurses, and documented paper procedures sustain care through the 4-hour MTD. To compensate, the baseline adds integrity-focused tailoring (section 10.1), and P01 carries pump library and device risks separately (R-007, R-015).

## 7. Authorization Boundary Description
The boundary was drawn from the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv). The endpoint counts are the endpoint console totals (EV-010); the server count is the CMDB total of 52 (EV-012); the medical device count is the clinical engineering maintenance inventory total of about 1,650, of which about 1,150 are in the security inventory (EV-013).

**Inside the boundary:**
- the hospital's EHR tenant configuration, the 64-role security catalog, the sepsis model settings, and the ambulatory module used by the affiliated practices;
- the identity provider tenant and the on-premises directory;
- the PACS and RIS application stack and the AI triage module in the workloads account;
- all 5 cloud accounts and their workloads (interface engine, data warehouse, file services, backups);
- the on-premises data center and its clinical servers;
- the campus and outpatient center networks;
- 960 workstations and laptops, 380 smartphones, and 120 scanners;
- about 1,650 networked medical devices;
- the hospital's SIEM tenant, EDR console, and email security gateway.

**Outside the boundary (separate systems on the same network):**
- building and clinical OT (SYS-09), owned by the Director of Facilities;
- clinical communications (SYS-11), owned by the IT Director.
Both share the campus network today, which is why HECS segmentation work (SC-7) covers them.

**Outside the boundary (external services, interconnected):**
- the EHR vendor's platform;
- the cloud provider's infrastructure;
- the MSSP's platform;
- the clearinghouse, HIE, reference laboratory, teleradiology group, telestroke service, and public health agencies;
- the AI and coding vendors (AI-003, AI-005);
- the 18 affiliated practices' own networks and devices;
- about 210 PHI vendors.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Clearinghouse | Bidirectional (X12 over TLS through the interface engine) | Claims, eligibility, remittance | BAA; contract |
| Reference laboratory | Bidirectional (HL7 over TLS) | Send-out orders, results | BAA |
| Health information exchange | Bidirectional | Care summaries, admission and discharge notices | Participation agreement |
| Teleradiology group (overnight) | Outbound images, inbound reports | Studies, reports | BAA |
| Telestroke neurology service | Bidirectional video and image sharing | Stroke consults | BAA |
| State and county health departments | Outbound | Electronic laboratory reporting, syndromic surveillance, immunizations | Public health disclosure (no BAA required) |
| MSSP | Inbound logs; remote response actions | Security logs (may include PHI fragments) | BAA; SOC 2 Type 2 |
| Affiliated practices (18) | Bidirectional through the EHR | Practice patient records, orders, results | Services agreement; BAA with each practice (hospital as business associate) |
| AI scribe vendor (AI-003 pilot) | Outbound audio, inbound draft notes | ED encounter audio, notes | Vendor standard BAA (amendment pending, P10) |
| Coding assistance vendor (AI-005) | Bidirectional | Clinical documentation, codes | BAA |
| Device vendors (14 persistent VPNs) | Inbound remote support | Device data, logs | **No MFA; 3 without written interconnection terms (gap, CA-3)** |
| Former reference laboratory (legacy VPN) | None in use | None | **Tunnel still up; to be removed (CA-3)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| EHR tenant, portal, ambulatory module | SaaS | EHR vendor | Chief Operating Officer |
| Identity provider tenant; on-premises directory | SaaS; virtual servers | Identity vendor; data center | IT Director |
| PACS and RIS, AI triage module | Virtual machines and object storage | Workloads account | Imaging Director |
| Interface engine (production and test) | Virtual machines | Workloads account | IT Director |
| Data warehouse | Managed database service | Workloads account | Quality Director |
| File services | Managed file service | Workloads account | IT Director |
| Backup vault | Backup service with write-once retention | Backup account (second region) | IT Director |
| Network hub, cloud firewall, VPN, privileged access broker | Network and management services | Shared services account | IT Director |
| Organization guardrails, posture service, log archive | Policy, security, and storage services | Management and security accounts | Information Security Manager |
| LIS and blood bank module | Virtual server | Data center | Laboratory Director |
| Dispensing cabinet server; infusion pump server | Virtual servers | Data center | Pharmacy Director |
| Monitoring gateway and central stations; fetal surveillance server; cardiology system | Virtual and physical servers | Data center and units | Director of Biomedical Engineering |
| Backup appliance; downtime extract server | Appliance; virtual server | Data center | IT Director |
| Core and distribution switches, firewalls, Wi-Fi, SD-WAN edges | Network | Main campus; outpatient center | IT Director |
| Workstations and laptops (960), smartphones (380), scanners (120) | Endpoint | Both sites | IT Director |
| Medical devices (about 1,650 networked) | Medical device | Both sites | Director of Biomedical Engineering |
| SIEM tenant; EDR console; email security gateway | SaaS | MSSP and vendors | Information Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** HECS uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 133 controls** in `control-implementation.csv`. They cover every SP 800-53 control mapped to a HIPAA Security Rule standard or implementation specification in the Health Care crosswalk (an author mapping), plus the Moderate controls that address the risks in P01 (segmentation, privileged access, vendor access, monitoring, recovery, unsupported devices) and the controls that support 42 CFR 482.15 (CP-2, CP-2(1), CP-2(3), CP-3, CP-4, CP-8, IR-3, PE-11).
- **Selected by tailoring (added):** PM-1, PM-2, and PM-9, which are not in the Moderate baseline but are needed for HIPAA 164.308(a)(1)-(2), and SA-3(2), added because production PHI sits in the interface engine test environment (EV-025).
- **Integrity tailoring:** CM-3 and CM-4 statements cover EHR build changes and vendor feature activations; SI-7 covers the drug library and interface mappings; SI-10 covers interface validation.
- **Inherited without separate statements:** the remaining Moderate-baseline physical and environmental controls for cloud and SaaS data centers (for example PE-9, PE-10, PE-12, PE-13, PE-15) and platform-level SA and SC controls. They are inherited from the EHR vendor, the identity vendor, the cloud provider, and the MSSP, and are evidenced by their SOC 2 Type 2 reports, which are reviewed each year (P09 `vendor-soc2-review.csv`). The PACS vendor has no SOC 2 report, so the PACS application controls are rated as hybrid and assessed directly.
- **Deferred:** the other Moderate controls with no HIPAA mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the hospital does not develop software). They are recorded as tailoring decisions and reviewed each year.

**Status of the 133 documented controls:**
| Status | Count |
|---|---|
| Implemented | 36 |
| Partially implemented | 97 |
| Planned | 0 |
| Not applicable | 0 |

**Inheritance of the 133 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 88 | Hospital |
| Hybrid | 38 | EHR vendor, identity vendor, cloud provider, MSSP, medical device manufacturers, vendor access platform provider, email security vendor |
| Common/Inherited | 7 | Identity vendor (AC-7, IA-2(8)), EHR vendor (AC-12), cloud provider (CP-6, SC-12), carriers and cloud provider (SC-5), MSSP and insurer panel (IR-7) |

The large share of Partially implemented statements reflects the scenario: the hospital has a defined program, but its controls do not yet reach medical devices, OT, vendors, non-employee users, or on-premises recovery. The statements trace to the intake observations cited in the `evidence` column of `control-implementation.csv` (for example EV-013, EV-022 and EV-028) and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls from 2026-07-27 to 2026-08-14 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce on campus.** Clinical workstations use badge tap (something the user has) plus a password (something the user knows) through the identity provider's single sign-on agent. This gives two factors at the bedside without slowing clinicians, and it is accepted for the Moderate categorization.
- **Remote and external access.** Workforce, contracted physicians, and affiliated practice users authenticate with a password and push MFA with number matching, under conditional access that checks device compliance and sign-in risk.
- **Administrators.** Administrators will move to phishing-resistant authenticators (FIDO2 security keys) by 2027-03-31 (P01 R-009). Until then, cloud administration goes through the privileged access broker with just-in-time elevation; other administration does not (EV-007).
- **Vendors.** Vendor support must move to named accounts on the vendor access platform with MFA by 2026-12-31 (P01 R-010). The 14 persistent VPN accounts are a documented exception until then.
- **Patients.** Patients use the EHR vendor's portal, which provides identity proofing and optional MFA. It is governed by the vendor and outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); intake evidence, inventories and obligations register ([step-00](../step-00_P00_intake/intake-report.md)); risk register (P01); gap analysis, CPG benchmark, and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10); emergency operations plan (482.15 program).

## 13. Acronym List and Glossary
- **BAA:** business associate agreement
- **CUEC:** complementary user entity control (in a SOC 2 report)
- **ED:** emergency department
- **EDR:** endpoint detection and response
- **eMAR:** electronic medication administration record
- **EMTALA:** Emergency Medical Treatment and Labor Act
- **HECS:** Hospital EHR and Clinical Systems
- **LIS:** laboratory information system
- **MDS2:** Manufacturer Disclosure Statement for Medical Device Security
- **MSSP:** managed security service provider
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **OT:** operational technology
- **PACS, RIS:** picture archiving and communication system, radiology information system
- **POA&M:** plan of action and milestones
- **STEMI:** ST-elevation myocardial infarction

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-17 | Draft from the risk analysis, BIA, and gap analysis | Information Security Manager |
| 1.0 | 2026-09-17 | Updated with P07 results; approved by the Chief Operating Officer | IT Director (Security Officer) |

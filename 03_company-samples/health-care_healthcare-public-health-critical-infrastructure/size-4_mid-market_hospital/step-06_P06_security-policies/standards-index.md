# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Information Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2023 policies stated intent but had few supporting standards, so IT, biomedical engineering, facilities, and vendors had no measurable rules for configuration, logging, vendor access, or medical devices (intake library review, EV-027; P03 164.316(a); P01 R-040). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them.

The policy set has 5 policies (POL-01 to POL-05, 66 statements mapped in `policy-control-map.csv`, 42 of them tested in P07). This index adds the 10 standards the Mid-Market tier calls for.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Information Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard names what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | Information Security Manager | Draft in progress (EV-027) | 2027-03-31 | Benchmark-based baselines for workstations, servers, the virtualization cluster, cloud virtual machines, network devices, and SaaS tenants; vendor-managed clinical servers documented with the vendor's hardening guide; monthly drift report; change control with a second reviewer for EHR build, interface mapping, and drug library changes | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Information Security Manager | Draft in progress (EV-022, EV-024) | 2027-01-31 | Required event types per system class; all HECS components send logs to the SIEM, including the LIS, cabinet and pump servers, monitoring gateway, fetal surveillance server, cardiology system, interface engine, PACS, and passive device and OT monitoring; 1 year searchable and 6 years archived for EHR audit and security logs; MSSP high-severity call within 30 minutes; monthly EHR access analytics review | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor risk and remote access standard** | POL-01, POL-02 | Compliance and Privacy Officer with the Information Security Manager | Draft in progress (EV-015, EV-041, EV-042) | 2026-12-31 | Vendor tiers (Tier 1: PHI at scale, privileged or network access, or support for a High-criticality BIA process; Tier 2: limited PHI; Tier 3: no PHI); BAA before any PHI; Tier 1 annual SOC 2 Type 2 or equivalent with CUEC mapping and bridge letter; breach and incident notice of 5 business days for Tier 1; vendor remote access only through the access platform with named accounts, MFA, approval, and recording; exit and data return terms | SA-9, SR-6, RA-3(1), SA-4, AC-17, MA-4 |
| STD-04 | **Medical device and OT security standard** | POL-01, POL-02, POL-04 | Director of Biomedical Engineering with the Director of Facilities and the IT Director | Draft in progress (EV-013, EV-014, EV-016) | 2027-03-31 | Security inventory for every networked device and OT component (owner, location, OS, support end date, PHI storage, MDS2, SBOM where available); passive discovery and monitoring; device and OT segments with deny-by-default rules; default credentials changed before connection; security review before purchase using FD&C Act sec. 524B deliverables; compensating controls for unsupported devices; sanitization certificate before return; weekly OT configuration export | CM-8, SC-7, AC-4, SA-22, SA-4, MA-4, MP-6 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Chief Medical Officer with the vCISO and the Compliance and Privacy Officer | Draft in progress (EV-055) | 2026-12-31 | AI inventory including vendor-enabled EHR features; risk tiering per P10; security, privacy, and clinical review before use; BAA with a no-training clause; 45 CFR 92.210 identification and mitigation record; local validation before go-live for clinical models; human review of outputs; all-party recording consent for ambient tools; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3, CM-4 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2023); update due | 2027-03-31 | 14-character minimum and banned list; MFA as in POL-02 4.3; phishing-resistant MFA for administrators; privileged access management with just-in-time elevation; vaulted and rotated service and vendor credentials; break-glass accounts tested quarterly; non-employee end dates | IA-2, IA-5, AC-2, AC-6(2), AC-6(5) |
| STD-07 | Contingency, recovery, and downtime standard | POL-03, POL-04 | IT Director with the Director of Emergency Management | Draft in progress (EV-028, EV-030) | 2026-12-31 | Recovery objectives from the BIA (P05); IT disaster recovery plan as an annex to the emergency operations plan; quarterly restore tests per hospital-managed system; 72-hour unit downtime procedures and quarterly drills; diversion criteria; alternate communications on every unit; annual functional downtime exercise | CP-2, CP-4, CP-8, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2023); minor update | 2027-03-31 | Approved algorithms and protocols (TLS 1.2 or higher); encryption at rest for all Restricted data; hospital-managed keys for cloud workloads; separate backup keys; device encryption required in purchasing | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Information Security Manager | Existing (2023); update due | 2026-12-31 | Monthly authenticated scans (moving from quarterly); weekly Known Exploited Vulnerabilities review; remediation targets: Critical 7 days for internet-facing systems on the known-exploited list, 14 days other internet-facing, 30 days internal; High 60 days; passive scanning only for medical devices; annual penetration test | RA-5, SI-2, SI-5, CA-8 |
| STD-10 | Facility and network space security standard | POL-01 | Director of Facilities | Existing (2023); update for network closets | 2027-03-31 | Badge access for the data center, all 41 network closets, pharmacy, and nursery; key logs where keys remain; visitor logs; quarterly badge review; video for the data center | PE-2, PE-3, PE-6, PE-8 |

**Summary:** 10 standards. The 5 new standards requested in the gap analysis (STD-01 to STD-05) are in draft, and STD-07 is new and also needed for the 482.15 IT outage annex. STD-06, STD-08, STD-09, and STD-10 exist from 2023 and need updates.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Vendor risk and remote access; STD-05 AI use; STD-07 Contingency, recovery, and downtime; STD-09 Vulnerability and patch |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-04 Medical device and OT security; STD-06; STD-08; STD-10 |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process

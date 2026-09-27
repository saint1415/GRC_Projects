# Scenario facts: Cris Santos Company | Manufacturing | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or FDA guidance, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (private; private equity-backed; board with an audit committee) |
| Business | Designs, builds, and services connected patient-care devices (NAICS 334510, Electromedical and Electrotherapeutic Apparatus Manufacturing), and runs the **Connected Care Cloud (CCC)**, a device cloud service for hospital customers |
| Location | Florida headquarters campus: offices, engineering labs, a warehouse and distribution center, and the company's own plant with four lines (Line 1 printed circuit board assembly, Line 2 monitor final assembly and test, Line 3 infusion pump assembly, flow calibration, and test, Line 4 service and refurbishment depot). 64 field service engineers work from home in the customer states |
| Workforce | 850 employees: 210 engineering (95 device firmware and software, 38 cloud and site reliability, 35 hardware, 30 verification and validation, 12 security and IT engineering), 290 manufacturing operations, 70 quality and regulatory, 110 customer support and field service, 80 sales and marketing, 90 general and administrative |
| Revenue | About $240 million a year (fictional): monitors about $118 million, infusion pumps and pump service about $62 million, CCC and software subscriptions (including AI-001) about $34 million, service, parts, and refurbishment about $26 million |
| Size status | The SBA size standard for NAICS 334510 is 1,250 employees (13 CFR 121.201), so the company is still SBA-small. It is Mid-Market under this library's tier rule, which sizes this industry at 500-999 employees (Census SUSB class) and flags it (see README) |
| Products | **VM-7** vital-signs monitor (current model; class II; 510(k) cleared 2024-02, after section 524B took effect; about 21,000 units in the field). **VM-5** monitor (legacy; cleared 2018, before section 524B; sales ended 2025-06; supported until 2028-12-31; about 11,500 units in the field). **IP-4** large-volume infusion pump (class II; 510(k) cleared 2025-03; about 7,800 units in the field). **AI-001** skin-image analysis software function (De Novo request granted 2025-10 with an authorized predetermined change control plan; in clinical use at 22 hospitals since 2026-01) |
| Connected Care Cloud | Multi-tenant service in the company's multi-account public cloud landing zone (vendor-agnostic). Receives telemetry from VM-7 and VM-5, gives clinicians remote viewing and secondary alarm notifications, manages IP-4 drug libraries and EHR-integrated pump programming, runs the AI-001 image analysis service, sends results to hospital EHRs, and distributes signed firmware. Primary alarms always sound at the bedside monitor or pump |
| Customers | About 290 hospitals and health systems in 24 states (about 80 in Florida). Each has a business associate agreement (BAA) with the company |
| HIPAA status | **Business associate** for the CCC and for the support and field service activities covered by the BAAs. The CCC creates, receives, maintains, and transmits PHI for the hospitals (45 CFR 160.103), so the HIPAA Security Rule applies to it (45 CFR 164.302), and breach notice to hospitals follows 45 CFR 164.410. The company is not a covered entity |
| PHI in the CCC | Patient name, medical record number, date of birth, location, vital-sign trends, alarm history, infusion records, and skin images with AI-001 results for about 2.4 million patients (24-month rolling retention set by the BAAs) |
| FDA status | Registered device manufacturer. Quality management system under the QMSR (21 CFR Part 820, which incorporates ISO 13485 by reference; effective 2026-02-02). Section 524B of the FD&C Act (21 U.S.C. 360n-2) applies to the VM-7, IP-4, and AI-001 submissions, all made after the 2023-03-29 effective date. The company is an active member of a health sector ISAO (since 2024) |
| Not in scope | DFARS 252.204-7012, CMMC, ITAR (N31-33-R01 to R03): no defense contracts or defense articles. EAR (N31-33-R04): U.S. sales only; export classification is outside these samples. FAR 52.204-25: no federal contracts. SEC disclosure rules: privately held. CIRCIA: proposed rule only. HIPAA group health plan rules: the employee health plan is fully insured and the company receives only summary health and enrollment information |
| Regulatory driver IDs | N31-33-R05 (FD&C Act 524B) is the primary driver. For the CCC's HIPAA scope this folder cites the Health Care vertical's verified IDs **N62-R01** (Security Rule) and **N62-R03** (Breach Notification Rule). FDA regulations are cited directly (21 CFR 803, 806, 820) |
| State law approach | Customers and affected individuals are in 24 states, so state breach laws are treated generically ("each state where affected individuals reside"). Florida is the worked example: the third-party agent notice duty in Fla. Stat. 501.171(6) |

## 2. People (role titles only)
| Role | Security, product security, and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber and product security risk reporting |
| Chief Executive Officer (CEO) | Accepts High risks; approves the risk appetite and the security budget |
| Chief Operating Officer (COO) | Executive sponsor of the security program; system owner of the Device Lifecycle Platform; accepts Moderate risks |
| Chief Financial Officer (CFO) | Cyber insurance; finance processes |
| General Counsel | Legal lead in incidents; privilege; engages outside counsel; supervises the Compliance and Privacy Officer |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting; SSP review |
| IT Director | Security Officer for corporate IT and plant networks; designated HIPAA security official for the CCC (45 CFR 164.308(a)(2)) |
| Security Manager plus 2 security analysts | Security operations with the MSSP, vulnerability management, GRC |
| VP Engineering | Device and cloud engineering; secure product development framework (SPDF) |
| Product Security Manager plus 3 product security engineers | Product security incident response team (PSIRT) lead; threat models; SBOMs; coordinated vulnerability disclosure (CVD); ISAO liaison |
| Director of Cloud Operations (12 site reliability engineers) | CCC production, backups, and monitoring |
| VP Quality and Regulatory Affairs (VP QA/RA) | Owns section 524B compliance; FDA submissions; complaint handling; medical device reporting (21 CFR 803); corrections and removals (21 CFR 806) |
| Compliance and Privacy Officer | BAAs; breach risk assessments and notices to hospitals; reports to the General Counsel |
| Plant Manager | Owns the four lines, the MES, and production continuity |
| OT Engineering Manager (4 controls engineers) | Plant OT network, test station and line equipment configurations |
| Chief Medical Officer (physician) | Clinical safety input to risk management; AI oversight |
| Director of Customer Support and Field Service | Hospital communications; complaint intake; field updates |
| Internal audit (co-sourced firm) | Annual IT audit; P07 assessment |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring of IT and cloud. A subcontractor business associate |

## 3. Systems
| ID | System | Hosting | Holds PHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Connected Care Cloud (CCC) | Public cloud workloads accounts (IaaS/PaaS), vendor-agnostic | Yes | Device gateway (mutual TLS), container platform (ingestion, viewing, notification, pump programming, AI-001 inference, HL7 and FHIR interfaces, update service), managed database, object storage, key management |
| SYS-02 | Cloud landing zone | Public cloud, 7 accounts | Yes (in the CCC and backup accounts) | Management, security and log archive, shared network, build and signing, CCC production, CCC non-production, backup (second region) |
| SYS-03 | Identity provider (SSO and MFA) | SaaS | No (identities only) | All workforce systems. **MES stations and test stations are not integrated** |
| SYS-04 | Source repositories, CI/CD pipeline, and code-signing service | Repositories: SaaS. Build runners and signing service: build and signing account, with a cloud HSM | No | HSM-backed release signing with two-person approval for VM-7, IP-4, and AI-001. **VM-5 is still signed with a legacy key held on an offline laptop in a safe, with one backup copy** |
| SYS-05 | Product lifecycle management (PLM) | SaaS | No | Design history files, requirements, risk management and threat models |
| SYS-06 | Electronic quality management system (eQMS) | SaaS | Incidental | Complaints, CAPA, MDR and correction or removal records, CVD intake queue. Includes the AI-005 complaint summarization feature |
| SYS-07 | MES and plant OT | On premises, plant | No | 2 MES servers, 14 MES operator terminals, 52 test and calibration stations, SMT line equipment including automated optical inspection (AI-003), line PLCs, a historian, the factory provisioning server that issues device certificates, and the building management system. About 310 networked OT assets |
| SYS-08 | Endpoints and engineering lab networks | On premises and remote | Incidental | 780 laptops and 140 desktops with EDR and full-disk encryption; 3 engineering lab networks with test devices |
| SYS-09 | SIEM and EDR (MSSP-operated) | SaaS | Yes (log fragments) | IT, identity, and cloud logs. **OT, MES, PLM, and the build pipeline do not send logs** |
| SYS-10 | Enterprise resource planning (ERP) | SaaS | No | Orders, shipping, UDI and serial-number traceability |
| SYS-11 | Productivity suite, support ticketing, and field service apps | SaaS | Incidental | Email (including security@), files, chat, hospital support tickets |
| SYS-12 | Fielded devices | At hospital customers | Yes (local buffers, under hospital control) | VM-7 and IP-4 use per-device certificates, signed firmware, and secure boot. VM-5 uses a per-hospital shared API key and signature checks without secure boot |
| SYS-13 | Third parties | Various | Some | About 160 suppliers, 38 with system or data access; 18 subcontractors receive PHI, 16 of them under a subcontractor BAA |
| SYS-14 | AI tools | Various | Some | AI-001 to AI-006 (section 5) |

**SSP system (P02):** the *Device Lifecycle Platform (DLP)*: SYS-01 to SYS-09 (the Connected Care Cloud and its landing zone, identity, the build and code-signing pipeline, PLM, eQMS, the MES and plant OT, endpoints, and the SIEM), with fielded devices, hospital networks, and the ERP as interconnected systems outside the boundary.

## 4. Current security posture: defined program with gaps in scale
**In place today:**
- A QMSR quality system with design controls and a written secure product development framework (SPDF) procedure (2025) covering device firmware and the CCC
- Section 524B documentation in the VM-7, IP-4, and AI-001 submissions: threat models, cybersecurity risk assessments, SBOMs, cybersecurity management plans, and penetration test reports
- A published CVD policy with a 3-business-day acknowledgment target; active health sector ISAO membership
- Automated SBOM generation in every VM-7, IP-4, AI-001, and CCC build since 2025
- HSM-backed code signing with two-person approval for current products
- MFA for all workforce users except MES and test stations; phishing-resistant keys for cloud administrators
- EDR on all IT endpoints with 24x7 MSSP monitoring and a SIEM
- A 7-account cloud landing zone with organization guardrails and write-once backups in a separate backup account
- Annual independent penetration tests of VM-7, IP-4, and the CCC (last in 2025)
- A SOC 2 Type 2 report (Security category) for the CCC for 2025-04-01 to 2026-03-31
- Policies adopted in 2024; annual training and phishing simulations; an annual co-sourced internal IT audit
- The plant office network separated from the plant OT network by a firewall

**Gaps found in the 2026 assessments:**
1. Vulnerability triage has fallen behind the automated SBOM matching: 41 component vulnerabilities in fielded firmware are older than 90 days with no documented exploitability assessment. KEV matching is a weekly manual step. VM-5 has no SBOM.
2. The IP-4 update cycle is semiannual and field adoption is slow: 38% of IP-4 pumps run firmware more than two releases old. Adoption is not measured for VM-5, and the TPLC security metrics are tracked only for VM-7.
3. VM-5 (cleared before 524B) uses a per-hospital shared API key, its embedded operating system reaches end of support in 2027-06, its signing key sits on an offline laptop with one backup, and no end-of-support notice has gone to customers.
4. Plant OT: Line 1 and Line 3 share one flat OT network segment; a line equipment vendor has a persistent VPN appliance into it; 11 test stations run an unsupported operating system; the OT asset inventory is about 70% complete; OT traffic is not monitored.
5. MES and test stations use shared operator logins and no MFA.
6. The factory provisioning server holds the intermediate certificate authority key that issues device identity certificates in software, not in the HSM.
7. Access reviews for the CCC and the landing zone are annual, not quarterly. Nine site reliability engineers keep standing production access; just-in-time access covers only the database.
8. The SIEM does not receive logs from plant OT, the MES, PLM, or the build pipeline, and the MSSP contract excludes OT.
9. The corporate incident response plan and the PSIRT procedure are not integrated with crisis management, MDR and correction decisions, and business associate notice. Notice terms in the 290 BAAs are not tracked in one place. No combined exercise has been held.
10. Third parties: 2 of 18 subcontractors that receive PHI have no subcontractor BAA. Critical software suppliers are not assessed, and 6 of 22 have no vulnerability notification terms.
11. Recovery: the CCC regional failover test in 2025 took 6 hours against a 2-hour target; recovery of the HSM keys, the build pipeline, and the MES has never been tested.
12. Change control for plant equipment and test station software does not require a cybersecurity impact review or revalidation for script changes.
13. AI governance is limited to AI-001. The AI-005 complaint summarization feature was switched on without review, public AI assistants are not blocked, and AI-003 model updates are not validated under the production software validation procedure.
14. Policies exist (2024), but standards for OT security, secure configuration, and supplier security are missing.
15. Customer security documentation: the VM-5 manufacturer disclosure statement dates from 2022, and SBOMs reach customers only on request.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 SSP | Device Lifecycle Platform (DLP), Moderate baseline with tailoring and the SP 800-82 Rev. 3 OT overlay for the plant components |
| P03 regulation | Primary: FD&C Act section 524B with the FDA regulations and guidance that carry it out (21 CFR 803, 806, 820; FDA premarket cybersecurity guidance issued 2026-02-03; FDA postmarket cybersecurity guidance, December 2016). Secondary: HIPAA Security Rule and business associate breach notice for the CCC. Benchmark (nonbinding): NIST SP 800-82 Rev. 3 for plant OT |
| P04 cloud | The 7-account landing zone and the CCC workloads, vendor-agnostic |
| P05 BIA | 17 business processes (BP-01 to BP-17) across the device cloud, product security and quality, the plant, and support functions |
| P07 assessment | 36 controls with sampling by the co-sourced internal audit firm. Device lab testing on 2026-08-19 found IP-4 pumps shipped with the factory service mode enabled (R-049) |
| P08 incidents | **Two incident types:** (1) an exploited vulnerability in a fielded connected device (IP-4 or VM-7), with coordinated disclosure, FDA decisions, and business associate duties; (2) ransomware in the plant OT that threatens the build and signing pipeline. Both integrated with crisis management and legal |
| P09 SOC 2 | Readiness to add Availability and Confidentiality to the CCC SOC 2 Type 2 report from the 2027-04-01 period, requested by a group purchasing organization contract; plus a vendor SOC 2 review program |
| P10 AI | Portfolio: AI-001 skin-image analysis (on market), AI-002 alarm artifact reduction model (in development for VM-7), AI-003 automated optical inspection on Line 1, AI-004 enterprise coding assistant, AI-005 complaint summarization in the eQMS, AI-006 public AI assistants (prohibited) |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | BIA interviews, risk assessment, and gap analysis fieldwork |
| 2026-08-10 to 2026-08-28 | Control assessment by the co-sourced internal audit firm (plant walkthrough 2026-08-18; device lab testing 2026-08-19) |
| 2026-09-04 | SOC 2 readiness assessment completed |
| 2026-09-09 | AI risk assessment completed |
| 2026-09-17 | Deliverables approved by the COO (Moderate and below) and the CEO (High and above); results to the audit committee |

## 7. Facts added during the build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Revenue per business day | About $960,000 over about 250 business days: monitors $472,000, pumps $248,000, subscriptions $136,000, service $104,000 |
| Service commitments | CCC contracts promise 99.9% monthly availability with service credits of up to 25% of monthly fees |
| Inventory buffers | About 3 weeks of finished monitors and 2 weeks of finished pumps in the distribution center |
| Cyber insurance | $15 million aggregate limit, $500,000 retention; the carrier's panel supplies breach counsel and forensics; notice through the carrier hotline before incident vendors are engaged |
| Backups | CCC database point-in-time recovery (5-minute log interval); daily snapshots to the backup account with 35-day write-once retention and separate administrator credentials; MES database backed up nightly to a plant file server only |
| Workforce activity | 96 terminations and 58 internal transfers in the 12 months to 2026-06-30; last access review January 2026; June 2026 phishing click rate 5.9% |
| CVD activity | 14 external vulnerability reports received in 2026 through June; median acknowledgment 2 business days; 1 report acknowledged late (6 business days) |
| MSSP | Contract requires a call to the Security Manager within 30 minutes of a high-severity alert |
| Terminology | "Device Lifecycle Platform (DLP)" is the SSP system in P02, identifier CSC-DLP-01. "Connected Care Cloud (CCC)" is SYS-01 |
| Additional role titles | Director of Supply Chain; Director of Marketing and Communications; HR Director; Director of Clinical Affairs; Regulatory Affairs Manager; Quality Manager (complaints and CAPA) |
| AI-005 | eQMS vendor's generative AI feature, switched on 2026-05-04 by the Quality Manager; it summarizes complaints and suggests whether each may be MDR-reportable |

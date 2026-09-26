# Scenario facts: Cris Santos Company | Health Care | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (private; private equity-backed; board with an audit committee) |
| Business | Multi-specialty physician group (NAICS 621111) with one Medicare-certified ambulatory surgery center (ASC) and one imaging center (MRI, CT, X-ray) |
| Location | Florida only: 8 clinics, the ASC, the imaging center, and a central business office |
| Workforce | 600 employees, including 90 providers (60 physicians, 30 advanced practice providers) |
| Patients | About 110,000 active patients |
| Revenue | About $100 million a year (fictional). Not SBA-small (standard $16.0 million) |
| Payers | Medicare, Florida Medicaid, commercial. Section 1557 applies |
| HIPAA status | **Covered entity** |
| Added at this size | The ASC must meet the CMS emergency preparedness condition for coverage (42 CFR 416.54). The imaging center uses an FDA-cleared AI triage tool |
| Not in scope | 42 CFR Part 2; the group health plan is fully insured, so the insurer is the covered entity (confirm in P03); payment cards are handled by a validated point-to-point encryption solution (noted, not assessed) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting |
| Chief Executive Officer | Accepts High risk |
| Chief Operating Officer | Executive sponsor of the security program; accepts Moderate risk |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting |
| IT Director | HIPAA **Security Officer** |
| Security Manager plus 2 security analysts | Operations; vulnerability management; GRC |
| Compliance and Privacy Officer | HIPAA **Privacy Officer**; breach determinations |
| Chief Medical Officer | Clinical AI oversight; downtime clinical decisions |
| Internal audit (co-sourced firm) | Annual IT audit |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring. A business associate |

## 3. Systems
| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Enterprise EHR/PM | Vendor-hosted (SaaS) | System of record; SOC 2 Type 2 |
| SYS-02 | Identity provider with SSO and MFA | SaaS | All users; conditional access |
| SYS-03 | Imaging archive (PACS) and radiology information system | Vendor-managed in the practice's cloud tenant | Includes the FDA-cleared AI triage tool (AI-003) |
| SYS-04 | Cloud landing zone: 4 accounts/subscriptions (identity, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Interface engine, data warehouse, file services |
| SYS-05 | Clinic networks (10 sites), SD-WAN | On-premises | Medical devices are on the same VLAN as workstations at 5 of 10 sites |
| SYS-06 | Endpoints: 750 workstations and laptops, 120 tablets | Managed | EDR on all managed endpoints |
| SYS-07 | Medical devices: about 400 networked (infusion pumps at the ASC, imaging modalities, ECG, monitors) | On-premises | Partial inventory |
| SYS-08 | SIEM (MSSP-operated) | SaaS | EHR, IdP, cloud, firewall, and EDR logs |
| SYS-09 | About 140 third-party vendors with PHI access | Various | 110 BAAs on file |
| SYS-10 | AI tools | Vendors | AI scribe (40 providers), prior-authorization automation, imaging triage (FDA-cleared), patient chatbot on the website |

**SSP system (P02):** the *Enterprise Clinical Platform (ECP)*: SYS-01 to SYS-08. Moderate baseline with tailoring.

## 4. Current security posture: partially compliant, with tooling
**In place today:**
- MFA for all users
- EDR and 24x7 MSSP monitoring
- SIEM
- Annual risk analysis (last done July 2025)
- Policies adopted in 2023
- Quarterly vulnerability scanning
- Immutable backups in a separate backup account
- EHR disaster recovery tested by the vendor annually
- Annual training and phishing simulations
- Annual internal IT audit

**Gaps:**
1. Medical devices are not segmented at 5 of 10 sites, and the device inventory is about 60% complete.
2. Access reviews are annual, not quarterly. Privileged access management is limited to the cloud.
3. Third-party risk: 30 PHI vendors have no BAA on file. Vendor reviews happen only at onboarding.
4. DR tests cover only the EHR vendor. The interface engine, PACS, and data warehouse are untested.
5. Audit log review for the EHR covers only VIP patients; there is no broad inappropriate-access analytics.
6. The ASC emergency preparedness plan does not address cyber events such as EHR loss or infusion pump network loss.
7. There is no AI governance: 4 AI tools were adopted by departments without a security or privacy review.
8. Policies exist but supporting standards (configuration, logging, vendor) are thin.
9. The ASC and imaging center still have 2 legacy Windows systems on modality consoles.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | **Two incident types:** (1) ransomware with PHI exfiltration, and (2) a clearinghouse or major vendor outage. Integrated with crisis management and legal |
| P09 | Readiness for a SOC 2 Type 2 examination requested by a hospital joint venture partner (Security, Availability, Confidentiality); plus a vendor SOC 2 review program |
| P10 | AI use-case portfolio: AI-001 scribe, AI-002 EHR decision-support alerts, AI-003 imaging triage (FDA-cleared), AI-004 prior-authorization automation, AI-005 website chatbot |
| Cloud | Multi-account landing zone, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | Risk analysis and gap analysis |
| 2026-08-03 to 2026-08-21 | Control assessment (co-sourced internal audit) |
| 2026-09-15 | Results to the audit committee |

## 7. Facts added during the Phase 2 build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Sites | Clinics are numbered Clinic 1 to Clinic 8. The central business office (CBO) shares the headquarters building and network with Clinic 1, so the 10 network sites are the 8 clinics, the ASC, and the imaging center |
| Segmentation | Medical devices are on a separate VLAN at Clinics 1-3, the ASC, and the imaging center. Clinics 4-8 are flat (devices share the workstation VLAN) |
| Legacy systems | The 2 legacy Windows systems are the C-arm fluoroscopy console at the ASC and one MRI console at the imaging center. Both are vendor-locked; the vendors support them only on those versions |
| Revenue split | Clinics about $60 million, ASC about $22 million, imaging center about $12 million, other ancillary services about $6 million, over about 250 operating days a year. That is about $240,000 per operating day for the clinics, $88,000 for the ASC, and $48,000 for the imaging center |
| Clearinghouse | One clearinghouse handles eligibility, claims, and remittance for all payers. About $1.9 million in expected collections per week flows through it |
| Cyber insurance | $10 million aggregate limit, $250,000 retention. The carrier's panel supplies breach counsel and forensics. The policy requires notice through the carrier hotline before incident vendors are engaged |
| EHR vendor recovery commitments | The EHR vendor's SOC 2 system description states RTO 12 hours and RPO 1 hour. Each site has a downtime report workstation that receives an hourly read-only extract (schedules, medication lists, allergies, problem lists) |
| Workforce activity | 118 terminations and 64 internal transfers in the 12 months to 2026-06-30. The last access review was completed in January 2026. The June 2026 phishing simulation click rate was 7.8% |
| Backups | Daily backups of the workloads account to the backup account, with 35-day write-once retention and separate administrator credentials |
| MSSP | 24x7 monitoring; contract requires a call to the Security Manager within 30 minutes of a high-severity alert. Medical devices, the PACS, and the interface engine do not send logs to the SIEM today |
| Joint venture | A regional hospital system and the company are forming a joint venture for a second ASC. The company's CBO and the Enterprise Clinical Platform will provide revenue cycle and clinical platform services to the joint venture, which is why the partner asked for a SOC 2 Type 2 report |
| AI tools | AI-001 scribe in use since 2026-02 (40 providers); AI-003 triage flags suspected intracranial hemorrhage on head CT and pulmonary embolism on chest CT angiography; AI-004 prior-authorization automation in use since 2025-11; AI-005 website chatbot in use since 2026-04 (scheduling and general questions). AI-002 is the EHR's built-in rule-based alert library (212 active rules) |
| Terminology | "Enterprise Clinical Platform (ECP)" is the SSP system in P02, identifier CSC-ECP-01 |

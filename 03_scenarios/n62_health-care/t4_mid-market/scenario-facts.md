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

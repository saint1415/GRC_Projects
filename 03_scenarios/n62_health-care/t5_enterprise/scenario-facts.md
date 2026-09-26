# Scenario facts: Cris Santos Company | Health Care | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant) |
| Business | Large multi-specialty medical group (NAICS 621111) with ambulatory surgery centers, imaging centers, and a CLIA-certified clinical laboratory |
| Location | Headquartered in Florida. 140 clinic locations, 6 ASCs, 12 imaging centers, and 1 central lab across Florida, Georgia, Alabama, and South Carolina. **State breach laws are handled generically:** notify under the law of each state where affected patients reside, with Florida as the worked example |
| Workforce | 12,000 employees, including about 1,800 providers |
| Patients | About 2.1 million active patients |
| Revenue | About $4.8 billion a year (fictional) |
| Payers | Medicare, Medicaid (4 states), commercial, Medicare Advantage. Section 1557 applies |
| HIPAA status | **Covered entity** (organized as a single covered entity) |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); SOX IT general controls; CMS emergency preparedness for ASCs (42 CFR 416.54); growth by acquisition (8 practices acquired in 2025-2026) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board (audit committee plus a risk committee) | Cyber oversight (Item 106 disclosure) |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner; HIPAA **Security Officer** is the Director of Security Operations, reporting to the CISO |
| Chief Privacy Officer | HIPAA **Privacy Officer** |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Medical Information Officer | Clinical systems and AI clinical oversight |
| GRC team (8), Security Operations Center (24x7, in-house plus MSSP overflow), Internal Audit (in-house) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Enterprise EHR/PM (vendor-hosted) | Single instance; acquired practices migrate within 12 months |
| SYS-02 | Identity platform (SSO, MFA, privileged access management, identity governance) | Acquired practices' identities are not yet federated at 3 of 8 acquisitions |
| SYS-03 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers | Data warehouse, interface engines, lab information system, patient apps |
| SYS-04 | Enterprise network (SD-WAN, NAC at 60% of sites) | |
| SYS-05 | About 20,000 endpoints; about 9,000 networked medical devices | Medical device inventory about 85% complete |
| SYS-06 | ERP and payroll (SOX-relevant) | SOX IT general controls tested annually |
| SYS-07 | About 900 third-party vendors (320 with PHI) | Tiered third-party risk program; single clearinghouse for 70% of claims |
| SYS-08 | AI portfolio (14 use cases) | Governed by an AI council formed in 2025 |

**SSP system (P02):** the *Laboratory Information System (LIS)*, a high-value system that is Moderate, with integrity treated at High for result accuracy, and inherits common controls from the enterprise platform.

## 4. Current security posture: mostly compliant, with targeted gaps
**In place today:**
- A mature program aligned to CSF 2.0
- Annual risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC
- PAM
- Quarterly access certification
- Immutable backups
- Annual DR tests for tier-1 systems
- Tiered vendor reviews
- Annual SOC 2 Type 2 for its patient-app platform
- SEC Item 106 disclosure in its 10-K

**Targeted gaps:**
1. **Acquisition integration.** 3 of 8 acquired practices are still on legacy identity and flat networks, and 2 still run their own EHR instances.
2. **Clearinghouse concentration.** One clearinghouse handles 70% of claims, and the manual fallback is untested. The industry saw this risk in 2024, when an attack on a major clearinghouse disrupted claims processing nationwide.
3. **Medical devices.** The inventory is 85% complete, 1,100 devices run unsupported operating systems, and network access control covers 60% of sites.
4. **AI.** 14 AI use cases, but only 9 have completed council review. Bias testing has been done only on vendor-supplied data.
5. **Materiality.** The playbook has not been exercised with the disclosure committee since the 2025 acquisitions.
6. **Legacy.** Two acquired practices' EHR instances lack audit log feeds to the SIEM.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | Ransomware with PHI exfiltration, including an **SEC materiality assessment and 8-K Item 1.05** step, and a multi-state breach-notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to external clients (the patient-app platform, and lab reference testing for other practices) |
| P10 | Enterprise AI portfolio (14 use cases), with the council operating model |
| Cloud | Multi-cloud (vendor-agnostic) with common controls |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment (internal audit, second-line GRC) |
| 2026-09-10 | Results to the risk committee |

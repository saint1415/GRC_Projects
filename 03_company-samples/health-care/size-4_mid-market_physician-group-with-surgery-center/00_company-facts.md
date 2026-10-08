# Scenario facts: Cris Santos Company | Health Care | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

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
| HIPAA status | **Covered entity**, determined in the intake obligations register (N62-R01): the clearinghouse agreement covers standard electronic transactions for all payers (EV-042) |
| Added at this size | The ASC must meet the CMS emergency preparedness condition for coverage (42 CFR 416.54; obligations register N62-R08). The imaging center uses an FDA-cleared AI triage tool |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): 42 CFR Part 2, the FTC Health Breach Notification Rule, and HIPAA applicability to social assistance do not apply. The group health plan is fully insured and the company receives only summary health and enrollment information, so the insurer is the covered entity (confirmed in P03, EV-064). Payment cards are handled by a validated point-to-point encryption solution (noted, not assessed) |

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
The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Enterprise EHR/PM | Vendor-hosted (SaaS) | System of record; SOC 2 Type 2 |
| SYS-02 | Identity provider with SSO and MFA | SaaS | All users; conditional access |
| SYS-03 | Imaging archive (PACS) and radiology information system | Vendor-managed in the practice's cloud tenant | Includes the FDA-cleared AI triage tool (AI-003) |
| SYS-04 | Cloud landing zone: 4 accounts/subscriptions (identity, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Interface engine, data warehouse, file services |
| SYS-05 | Clinic networks (10 sites), SD-WAN | On-premises | Medical devices are on the same VLAN as workstations at 5 of 10 sites (EV-012) |
| SYS-06 | Endpoints: 750 workstations and laptops, 120 tablets | Managed | EDR on all managed endpoints (EV-010) |
| SYS-07 | Medical devices: about 400 networked (infusion pumps at the ASC, imaging modalities, ECG, monitors) | On-premises | Partial inventory: about 240 of about 400 listed (EV-011) |
| SYS-08 | SIEM (MSSP-operated) | SaaS | EHR, IdP, cloud, firewall, and EDR logs |
| SYS-09 | About 140 third-party vendors with PHI access | Various | 110 BAAs on file (EV-036) |
| SYS-10 | AI tools | Vendors | AI scribe (40 providers), prior-authorization automation, imaging triage (FDA-cleared), patient chatbot on the website |

**SSP system (P02):** the *Enterprise Clinical Platform (ECP)*: SYS-01 to SYS-08. Moderate baseline with tailoring.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the HIPAA Security Rule, the Breach Notification Rule and 42 CFR 416.54** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-06-15 to 2026-07-02 | Intake: evidence requests, exports, walk-throughs at 4 sites, inventories, obligations register |
| 2026-07-06 to 2026-07-31 | BIA interviews, risk analysis and gap analysis fieldwork |
| 2026-07-27 to 2026-07-31 | 2026 policy revisions (POL-01 to POL-05) and P08 runbooks drafted from the gaps |
| 2026-08-03 to 2026-08-21 | Control assessment (co-sourced internal audit): operating tests of controls already in place; design review of the draft policies and runbooks |
| 2026-08-24 to 2026-09-10 | AI governance assessment (P10) |
| 2026-09-15 | Deliverables, policies and runbooks approved; results to the audit committee |
| 2026-10-01 | 2026 policies take effect |
| 2027-03 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies and standards introduced, after at least one quarter of operation |

## 7. Facts added during the Phase 2 build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Sites | Clinics are numbered Clinic 1 to Clinic 8. The central business office (CBO) shares the headquarters building and network with Clinic 1, so the 10 network sites are the 8 clinics, the ASC, and the imaging center |
| Security-relevant details | Segmentation by site, the 2 legacy modality consoles, the EHR vendor's recovery commitments and downtime extracts, workforce activity and access review dates, phishing results, backup design, and the MSSP's terms and log coverage are recorded from the systems of record in the intake evidence register (EV-003, EV-005, EV-012, EV-014, EV-018, EV-019, EV-025, EV-033, EV-038), not stated here |
| Revenue split | Clinics about $60 million, ASC about $22 million, imaging center about $12 million, other ancillary services about $6 million, over about 250 operating days a year (EV-048). That is about $240,000 per operating day for the clinics, $88,000 for the ASC, and $48,000 for the imaging center |
| Clearinghouse | One clearinghouse handles eligibility, claims, and remittance for all payers. About $1.9 million in expected collections per week flows through it (EV-042) |
| Cyber insurance | $10 million aggregate limit, $250,000 retention. The carrier's panel supplies breach counsel and forensics. The policy requires notice through the carrier hotline before incident vendors are engaged (EV-041) |
| Joint venture | A regional hospital system and the company are forming a joint venture for a second ASC. The company's CBO and the Enterprise Clinical Platform will provide revenue cycle and clinical platform services to the joint venture, which is why the partner asked for a SOC 2 Type 2 report (EV-044) |
| AI tools | AI-001 scribe in use since 2026-02 (40 providers); AI-003 triage flags suspected intracranial hemorrhage on head CT and pulmonary embolism on chest CT angiography; AI-004 prior-authorization automation in use since 2025-11; AI-005 website chatbot in use since 2026-04 (scheduling and general questions). AI-002 is the EHR's built-in rule-based alert library (212 active rules) (EV-050) |
| Terminology | "Enterprise Clinical Platform (ECP)" is the SSP system in P02, identifier CSC-ECP-01 |
| Additional role titles | Chief Financial Officer; HR Director; Director of Clinic Operations; Director of Revenue Cycle; Director of Patient Access; Director of Marketing and Communications; ASC Administrator; ASC Medical Director; ASC Director of Nursing; Imaging Center Director |
| Other operating details | The ASC has 4 operating rooms (about 28 cases a day); the imaging center performs about 160 studies a day (about 70 CT); the CBO has about 120 staff; the EHR role catalog has 48 roles; 12 of the 140 PHI vendors are Tier 1 under the P09 tiering approach; the employee health plan's broker confirmed on 2026-07-22 that the company receives only summary health and enrollment information (EV-064) |

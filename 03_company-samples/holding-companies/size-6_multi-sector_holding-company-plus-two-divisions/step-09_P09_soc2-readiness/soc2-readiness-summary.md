# SOC 2 Readiness Summary: Cris Santos Company Holdings | Management of Companies and Enterprises | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Management of Companies and Enterprises (focus: the holding company) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs with short topic labels in the author's words |
| Scoping | Per division (section 1). Two readiness assessments: the Shared Corporate Services Platform for an affiliate assurance report (`soc2-readiness.csv`) and the Health Care Services occupational health employer portal (`soc2-readiness-occupational-health.csv`). Insurance is out of scope |
| Prepared | 2026-09-15 by the Group Chief Risk Officer's assurance team with the SCSP platform director and the Health Care Services HIPAA Security Officer |

## 1. Scoping decisions per division
A SOC 2 report covers controls at a **service organization** relevant to the **user entities** that rely on its service. The question for each division is who relies on its controls, and whether a SOC 2 report is the right way to give them assurance.

| Division | Service line | Who relies on it | Decision | Categories | Report |
|---|---|---|---|---|---|
| Holding company | Shared Corporate Services Platform (identity, ERP, HCM and payroll, treasury) for the group's subsidiaries | **The insurers, Health Care Services, and the group health plan.** They are affiliates, but the insurers must perform due diligence on the holding company as their Third-Party Service Provider (Model #668 sec. 4F), and Health Care Services must oversee it as a business associate | **In scope as an affiliate assurance report.** A SOC 2 examination by an independent CPA, with the subsidiaries as the specified users. It replaces separate due diligence by each subsidiary (POL-01 4.8(b)) | Security, Availability, Confidentiality, Processing Integrity | Type 2 for 2027-04-01 to 2027-09-30, after readiness by 2027-03-31 |
| Health Care Services | Occupational health employer portal (SYS-H2) for about 6,200 employer clients | **Employer clients**, which receive work-status reports and manage their own users. 140 larger clients asked for a SOC 2 report in 2026 security questionnaires | **In scope (full).** A true service organization for this line | Security, Availability, Confidentiality | Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| Health Care Services | Clinical care in 340 clinics | Patients are not user entities | Out of scope | n/a | n/a |
| Insurance | Property and casualty and workers' compensation insurance | **No user entities.** Policyholders and employers buy coverage; they do not build their own controls on the insurers' systems | **Out of scope** (reasons below) | n/a | n/a |

**Why Insurance is out of scope:**
1. **No user entities.** Insurance coverage is not an outsourced service that customers rely on in their own control environment.
2. **Assurance comes from regulators.** The Florida Office of Insurance Regulation examines the insurers and their affiliates (Fla. Stat. 628.801(3)), and commissioners in Alabama, South Carolina, and Tennessee can examine compliance with their data security laws.
3. **Agency and employer questionnaires** are answered with the group program description and the P03 and P07 results.
4. **Revisit trigger:** if the insurers begin administering self-insured workers' compensation programs for employers (acting as their service provider), assess whether a SOC 1 or SOC 2 report is needed.

**Why an affiliate report for the SCSP and not a self-assessment.** The insurers' due diligence on the holding company must be credible to their regulators, and the Group CISO who runs the SCSP cannot assess it for them. An independent examination with the subsidiaries as specified users gives each subsidiary one report to rely on, and group internal audit's work (P07) can be used by the service auditor where appropriate. The SOX ITGC testing already covers part of Processing Integrity for the ERP, treasury, and payroll.

**Other assurance considered.** The ERP, HCM, treasury, and identity vendors already provide SOC 2 Type 2 reports; the SCSP report will use the carve-out method for them. HITRUST was considered for the employer portal and rejected because clients ask for SOC 2.

## 2. System descriptions (scope)
### 2.1 Shared Corporate Services Platform
- **Services:** identity and access for all workforce; general ledger, payables, and consolidation; HR, payroll, and benefits enrollment; treasury and payments, including claims disbursements and patient refunds.
- **Infrastructure and software:** SYS-G1, SYS-G4, SYS-G5, SYS-G6 (SaaS) and the integration services in provider A, with a warm standby in provider B; group SOC (SYS-G2) and cloud and network (SYS-G3).
- **Subservice organizations (carve-out):** identity, ERP, HCM, and treasury SaaS vendors; cloud providers A and B.
- **Complementary user entity controls (the subsidiaries):** approve and certify their staff's access; report joiners, movers, and leavers the same day; verify payee bank details before sending payment files (Insurance claims); review payment and payroll reports.

### 2.2 Occupational health employer portal
- **Services:** exam scheduling, work-status reports, and injury visit summaries for employer clients.
- **Infrastructure and software:** SYS-H2 in provider A; customer identity service; group common controls carved in.
- **Subservice organizations (carve-out):** cloud provider A; customer identity vendor.
- **Complementary user entity controls (employer clients):** add and remove their own users; protect reports they download; tell the division when a client administrator leaves.

## 3. Readiness results
### 3.1 Shared Corporate Services Platform (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 24 | 8 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3. There is no system description and no written security commitment to the subsidiaries; the insurers' 2017 agreement has no security schedule (scenario gap 2).
**Partially ready:** CC3.4, CC6.1, CC6.2, CC6.3, CC6.7, CC7.2, CC7.4, CC9.2, A1.3, C1.1, and PI1.2. They map directly to the P07 findings: identity recovery and privilege (POAM-001, POAM-002), ERP superusers (POAM-003, POAM-004), the benefits export (POAM-005), the legacy trust (POAM-006), the integration failover (POAM-007), vendor complementary controls (POAM-008), the notification matrix (POAM-009, POAM-010), labels (POAM-023), and upstream bank-detail verification (POAM-013).

**Processing Integrity is in scope here** because what the subsidiaries most rely on is that payments and payroll are complete, accurate, and timely. PI1.2 is only partially ready because a fraudulent bank detail entered upstream in Insurance passes the SCSP's validation as a valid input.

### 3.2 Occupational health employer portal (`soc2-readiness-occupational-health.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 25 | 7 | 1 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first report:** control environment, risk, monitoring, identity, network, and SOC criteria are met by group common controls already evidenced in P07.
**Not ready:** CC2.3 (no system description; commitments vary by client contract) and A1.3 (no recovery test of SYS-H2).
**Partially ready:** CC3.4, CC4.1, CC5.3, CC6.2, CC6.7, CC7.4, CC9.2, C1.1, and C1.2. The most important is CC6.7: work-status reports include free-text visit notes beyond the work-related findings employers need (P01 HCS-006), which is also a HIPAA minimum necessary issue (164.512(b)(1)(v); P03).

## 4. Remediation plan and evidence calendar
| Quarter | Service line | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | SCSP | CC3.4, CC6.1, CC6.2, CC6.3, CC6.7, CC7.2, CC7.4, CC9.2, A1.3, C1.1, PI1.2 | Change template with privacy review; selective authentication on the legacy trust; reset procedure and scoped roles; PAM for ERP superusers; export removed; analytics; matrix and tabletop; complementary controls mapped; failover retest; labels; bank-detail verification in Insurance |
| 2026 Q4 | Employer portal | CC3.4, CC5.3, CC6.7, CC7.4, CC9.2, C1.1 | Release privacy review; re-issued supplement; structured template; matrix rows; identity vendor review; labels |
| 2027 Q1 | SCSP | CC2.3 (and CC6.1 follow-up) | System description; security schedules signed; legacy trust removed at clinic migration. Readiness confirmed 2027-03-31 |
| 2027 Q1 | Employer portal | CC2.3, CC4.1, CC6.2, A1.3, C1.2 | System description; standard security exhibit; complementary user entity controls; recovery test; offboarding procedure |
| 2027 Q2 to Q3 | SCSP | All in-scope criteria | Operating evidence for the Type 2 period 2027-04-01 to 2027-09-30 |
| 2027 Q2 to Q4 | Employer portal | All in-scope criteria | Type 1 as of 2027-06-30; Type 2 period 2027-07-01 to 2027-12-31 |

**Communication:** the Group General Counsel sends each insurer's board and the Health Care Services Privacy Officer the SCSP readiness results and the 2027 timeline; this also supports the insurers' 2027 board reports (Model #668 sec. 4E(2)(b)). The occupational health vice president sends the 140 requesting employer clients a readiness letter.

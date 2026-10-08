# SOC 2 Readiness Summary: Cris Santos Company Holdings | Health Care | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Health Care and Social Assistance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). Two readiness reports: Health-Tech SaaS (`soc2-readiness.csv`) and the Care Delivery patient-app platform (`soc2-readiness-patient-app.csv`). The Health Plan is out of scope |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the SaaS and Care Delivery security and compliance leads |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service to other organizations that rely on its controls.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Health-Tech SaaS | Care-coordination SaaS (SYS-D3) for about 420 hospitals and practices | **Yes, a true service organization.** Customers are covered entities that rely on the SaaS as their business associate | **In scope (full).** Existing annual Type 2 | Security, Availability, Confidentiality | Type 2, 12 months ending September 30 |
| Care Delivery | Patient-app platform (SYS-D4) offered white-label to 38 independent practices | **Yes, for this service line.** The practices are user entities and asked for a Type 2 report by the end of 2027 | **In scope.** First readiness assessment | Security, Availability, Confidentiality | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| Care Delivery | Clinical care to patients | No. Patients are not user entities | Out of scope | n/a | n/a |
| Health Plan | Medicare Advantage and commercial health coverage | **No.** It sells insurance coverage to members and employer groups, not an outsourced service that customers build their own controls on | **Out of scope** (reasons below) | n/a | n/a |

**Why the Health Plan is out of scope:**
1. **No user entities.** Members and employer groups buy coverage. They do not rely on Health Plan systems as part of their own control environment, which is what a SOC 2 report is for.
2. **Assurance comes from regulators instead.** The Health Plan is examined by state insurance departments in each state where it is licensed, audited by CMS as an MA organization, and bound by HIPAA and state insurance data security laws where enacted (P03 regulation-by-division matrix).
3. **Employer questionnaires** are answered with the group security program description and this sample's P03 and P07 results, not a SOC 2 report.
4. **Revisit trigger:** if the Health Plan begins administering benefits for self-funded employers (acting for them as a service provider), assess whether a SOC 1 or SOC 2 report is needed.

The Health Plan still benefits from this work: its delegated vendors' SOC reports are reviewed under POL-01 4.8, and the group common controls that both in-scope reports carve in are the same ones the Health Plan inherits.

**Other assurance options considered.** HITRUST certification is common in health care and some SaaS customers accept it. The group decided SOC 2 remains the primary report because customer contracts already require it. The vertical overlay names no other standard assurance mechanism.

## 2. System descriptions (scope)
### 2.1 Health-Tech SaaS
- **Services:** referrals, transitions of care, and care team coordination for about 420 customers; the "care summary assist" generative AI feature for 61 opt-in customers (launched 2026-04-15).
- **Infrastructure and software:** SYS-D3 on cloud provider B (container platform, managed database, warm standby region); group identity (SYS-G1) and SOC (SYS-G2) carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud provider B; **the third-party model provider** (not yet in the description, group gap 4).
- **People:** about 6,000 SaaS employees plus group SOC and identity teams.
- **Data:** customer PHI (about 12 million patients' records).
- **Complementary user entity controls:** customer SSO and MFA, user provisioning and removal, review of customer audit reports.

### 2.2 Care Delivery patient-app platform
- **Services:** patient scheduling, messaging, results, and bill pay under each practice's brand.
- **Infrastructure and software:** SYS-D4 on cloud provider A; customer identity service; group common controls carved in.
- **Subservice organizations (carve-out):** cloud provider A; customer identity vendor.
- **Data:** PHI of the 38 practices' patients (Care Delivery acts as their business associate) and of Care Delivery's own patients.
- **Complementary user entity controls:** practices provision and remove their staff users and handle patient identity disputes.

## 3. Readiness results
### 3.1 Health-Tech SaaS (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3. The AI feature and its model provider were not communicated to customers, and the system description does not include them.
**Partially ready:** CC3.4, CC8.1 (the launch skipped a privacy impact analysis), CC9.2 (no monitoring of the model provider), CC6.3 (support access without a ticket), CC6.7 (identifiable data exported to GDP staging), CC7.2 (AI requests not logged per patient), C1.1 (97 BAAs do not permit de-identification), and C1.2 (manual deletion certificates).

**The immediate issue is the report now being prepared.** The observation period ends 2026-09-30, and the feature operated for about five and a half months of it. Management must describe the feature, the model provider (as a subservice organization, with the carve-out method and any complementary subservice organization controls), and the change itself. Expect the service auditor to evaluate CC2.3, CC3.4, CC8.1, and CC9.2 for exceptions. POAM-018 covers the fix; the target is to have customer notices sent before the report is issued.

**Processing Integrity** is out of scope today because the SaaS makes no processing integrity commitments. It is under evaluation for 2027, because customers now ask whether AI summaries are complete and accurate (P10).

### 3.2 Care Delivery patient-app platform (`soc2-readiness-patient-app.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 23 | 9 | 1 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first-time report:** control environment, risk, monitoring, identity, network, and SOC criteria are met by group common controls already evidenced for the SaaS report.
**Not ready:** CC2.3 (no system description or written service commitments to the practices) and A1.3 (no DR test of SYS-D4).
**Partially ready:** CC2.1, CC3.4, CC4.1, CC5.3, CC6.2, CC7.1, CC7.4, CC8.1, CC9.2, and C1.2. Most are documentation or scope gaps specific to the platform.

## 4. Remediation plan and evidence calendar
| Quarter | Division | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | SaaS | CC2.3, CC3.4, CC8.1, CC9.2 | Updated system description; customer notices and BAA amendments; privacy impact analysis; model provider attestation |
| 2026 Q4 | SaaS | CC6.7, CC7.2 | De-identification inside SYS-D3; per-patient AI request logs |
| 2026 Q4 | Care Delivery app | CC7.1, CC7.4, CC8.1, CC9.2 | Authorization test results; matrix rows for practices; change records; identity vendor report review |
| 2027 Q1 | Care Delivery app | CC2.1, CC2.3, CC3.4, CC4.1, CC5.3, CC6.2, A1.3, C1.2 | Inventory; system description; runbooks; complementary user entity controls; DR test; offboarding procedure. Type 1 as of 2027-03-31 |
| 2027 Q2 to Q3 | Both | All in-scope criteria | Operating evidence for the SaaS 2027 period and the app's first Type 2 period (2027-04-01 to 2027-09-30) |
| 2027 Q2 | SaaS | C1.1, C1.2, CC6.3 | BAA amendments at renewal; automated deletion; ticket-linked support access |

**Communication:** the SaaS general manager briefs the top 50 customers on the AI feature change and the remediation before the 2026 report is issued. Care Delivery sends the 38 practices a readiness letter with the 2027 timeline.

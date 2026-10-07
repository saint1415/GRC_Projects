# SOC 2 Readiness Summary: Cris Santos Company Holdings | Healthcare and Public Health | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Healthcare and Public Health |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: the Hospital System's community-connect EHR service (`soc2-readiness.csv`). The Health Plan relies on its SOC 1 report for its one service line; the College is out of scope |
| Prepared | 2026-09-15 by the Group Chief Risk Officer's assurance team with the Hospital System community-connect director and security and compliance lead |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service to other organizations that build their own controls on it.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Hospital System | Community-connect EHR: the hospitals' EHR instance (SYS-H1) extended to 64 independent physician practices | **Yes, for this service line.** The practices are covered entities that rely on the Hospital System as their business associate and asked for a Type 2 report by the end of 2027 | **In scope.** First readiness assessment | Security, Availability, Confidentiality | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30, issued by 2027-12-15 |
| Hospital System | Patient care in 9 hospitals | No. Patients are not user entities | Out of scope | n/a | n/a |
| Health Plan | ASO claims administration for 40 self-funded employer plans | **Yes, for this service line.** The employer plans rely on it, but mainly for claims processing that affects their financial reporting | **SOC 2 out of scope this cycle.** The existing **SOC 1 Type 2** report on ASO claims administration (12 months ending June 30) meets what the employers ask for | n/a | SOC 1 Type 2 (existing) |
| Health Plan | Medicare Advantage and fully insured commercial coverage | No. Members and employer groups buy coverage; they do not build controls on Health Plan systems | Out of scope | n/a | n/a |
| College | Nursing and allied health education | **No.** Students are not user entities, and the College provides no outsourced service to other organizations | **Out of scope** (reasons below) | n/a | n/a |

**Why the Health Plan uses SOC 1, not SOC 2, for its ASO line.** The 40 employer plans need assurance mainly over claims processing that feeds their financial statements, which is what a SOC 1 report covers. None has asked for a SOC 2 report. Security questions from employers are answered with the group program description, the P03 and P07 results, and the ASO BAAs. **Revisit trigger:** if two or more employers ask for security assurance beyond SOC 1, or the Health Plan starts offering data or analytics services to employers, assess a SOC 2 report for the ASO line. Assurance for the insurance lines comes from regulators instead: state insurance departments in each state of license, CMS for the MA contract, and the HIPAA and state insurance data security laws mapped in P03.

**Why the College is out of scope.**
1. **No user entities.** Students and their families receive education; they do not rely on College systems as part of their own control environment.
2. **Assurance comes from Title IV oversight instead.** The College's GLBA Safeguards Rule program is tested in its annual compliance audit, and findings can affect Title IV administrative capability (N61-R02; P03 ED-G27).
3. **Revisit trigger:** if the College starts offering its clinical placement or compliance tracking service to other schools, assess whether it becomes a service organization.

**Other assurance options considered.** HITRUST certification is common in health care, and some practices accept it. The group decided SOC 2 remains the right report because the community-connect agreements and the practices' request name it, and because the same SOC 2 work reuses the group's SP 800-53 controls. The vertical overlay names no other standard assurance mechanism.

## 2. System description (scope): community-connect EHR service
- **Services:** clinical documentation, orders, results, e-prescribing, scheduling, and billing for 64 independent practices (about 1,100 users) on the hospitals' EHR instance, with help desk support and EHR build services.
- **Infrastructure and software:** SYS-H1 in DC1 with a replica in DC2; group identity (SYS-G1), SOC (SYS-G2), and data center, network, and backup services (SYS-G3) **carved in** as internal shared services of the same company.
- **Subservice organizations (carve-out):** the EHR vendor (software releases and support), cloud provider B (immutable vault), and the colocation operator for DC2 (building perimeter).
- **People:** the community-connect team, the HCIS application teams, and the group SOC, identity, and infrastructure teams.
- **Data:** the practices' patients' records (the Hospital System is their business associate).
- **Complementary user entity controls (to be written, CC2.3):** each practice runs its identity provider with MFA, provisions and removes its users, reviews its user list each quarter, trains its staff, and reports suspected incidents to the Hospital System.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 20 | 11 | 2 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first-time report:** the control environment, risk assessment, change management, monitoring, and malware criteria are met by group common controls and the HCIS controls already assessed in P07.

**Not ready (3):**
- **CC2.3:** no system description and no written service commitments for the practices.
- **CC7.5 and A1.3:** no tested recovery if ransomware reaches both data centers (POAM-012). This is the same gap as the HCIS authorization condition in P02, so fixing it serves the hospitals and the practices at once.

**Partially ready (12):** CC2.1 (service inventory), CC3.1 (service objectives), CC4.1 (no community-connect audit sample), CC5.3 (onboarding and offboarding procedures), CC6.1 (data center zones, POAM-007), CC6.2 and CC6.3 (student accounts on the same instance, POAM-001; practice attestations not checked), CC6.6 (device vendor connections, POAM-013), CC7.1 (ancillary patching, POAM-010), CC7.4 (practice notice procedure, POAM-005), CC9.1 (multi-day downtime guidance for practices), and C1.2 (data return or destruction when a practice leaves).

**Processing Integrity and Privacy are out of scope.** The service makes no processing integrity commitments, and the practices, as covered entities, own their patients' privacy under HIPAA.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC6.2, CC6.3, CC6.6, CC7.4 | Student accounts in identity governance (POAM-001); vendor connections in PAM (POAM-013); practice notice register; tabletop results (POAM-005) |
| 2027 Q1 | CC2.1, CC2.3, CC3.1, CC5.3, C1.2 | Service inventory and data flows; system description; service commitments; complementary user entity controls; onboarding and offboarding procedures |
| 2027 Q1 | CC7.1, CC7.5, CC9.1, CC4.1, A1.3 | Patch compliance; clean recovery environment and full restore test (POAM-012); practice downtime guidance; internal audit sample. **Type 1 as of 2027-03-31** |
| 2027 Q2 | CC6.1 | Data center zone separation (POAM-007, due 2027-06-30). The Type 1 description will disclose the separation as in progress |
| 2027 Q2 to Q3 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30) |

**Communication:** the Hospital System community-connect director sends the 64 practices a readiness letter with this timeline in 2026 Q4 and briefs the practice advisory group each quarter.

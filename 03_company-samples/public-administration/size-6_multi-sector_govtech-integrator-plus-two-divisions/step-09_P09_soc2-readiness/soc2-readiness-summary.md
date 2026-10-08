# SOC 2 Readiness Summary: Cris Santos Company Holdings | Public Administration | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Public Administration (focus division: GovTech Integration) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division and service line (section 1). Three readiness checklists: the ACMP (`soc2-readiness.csv`, GovTech), the Public Safety RMS (`soc2-readiness-rms.csv`, Government Software Products), and the Civic Suite (`soc2-readiness-civic-suite.csv`, Government Software Products). IT Consulting is out of scope; Grants Management relies on its FedRAMP authorization |
| Basis | P07 assessment results and POA&M, P03 gap analyses, and P01 registers |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the GovTech division CISO and the Government Software Products security and compliance lead; reviewed by the board audit committee 2026-09-15 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each service line is whether agencies or customers build their own control environment on the group's controls.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| GovTech Integration | ACMP (SYS-D1), hosted for about 430 agency tenants | **Yes.** Revenue, criminal justice, and local agencies rely on the group's controls over their FTI, CJI, and constituent data | **In scope.** Existing annual Type 2 | Security, Availability, Confidentiality | Type 2, 12 months ending June 30. This readiness review covers the current period, 2026-07-01 to 2027-06-30 |
| GovTech Integration | IEP (SYS-D2) and MVSP (SYS-D3) | Yes, but each state's contract names its own assurance: the IEP states accept the SSP, P07 results, and their own audits; the MVSP states audit DPPA compliance themselves | Not in scope this cycle. Revisit when a state asks for a SOC 2 report at renewal | n/a | n/a |
| GovTech Integration | Implementation and data migration services | No. Project services, not an ongoing system that agencies rely on | Out of scope | n/a | n/a |
| Government Software Products | Public Safety RMS (SYS-D7) for about 620 agencies | **Yes.** Agencies rely on it for CJI | **In scope.** Existing annual Type 2 | Security, Availability, Confidentiality | Type 2, calendar year. The current period (2026-01-01 to 2026-12-31) includes the AI assist beta |
| Government Software Products | Civic Suite (SYS-D6) for about 1,900 local governments | **Yes** | **In scope.** Existing annual Type 2 | Security, Availability, Confidentiality | Type 2, calendar year (2026-01-01 to 2026-12-31) |
| Government Software Products | Grants Management federal edition (SYS-D8) | Yes, for federal agencies | **Relies on its FedRAMP Moderate authorization** (P03 SW-G09, SW-G10). Federal customers use the FedRAMP package; no SOC 2 report is planned | n/a | n/a |
| IT Consulting | Advisory, program management, modernization, and managed application support | **No** for advisory work; managed application support runs on agency-owned systems under the agencies' controls | **Out of scope** (reasons below) | n/a | n/a |

**Why IT Consulting is out of scope:**
1. **No system that clients rely on.** Advisory and program management are professional services. The division's managed application support operates agency-owned systems under each agency's own authorization and controls (P03 IC-G21 notes the same distinction for CMMC).
2. **Assurance comes from other regimes.** DoD work is assessed under DFARS 252.204-7012 and CMMC (Level 2, with a voluntary C3PAO assessment while Phase 2 is suspended, P03 IC-G19); federal civilian work follows FAR 52.204-21; public hospital and county health clients rely on business associate agreements (P03 IC-G23 to IC-G25).
3. **Client questionnaires** are answered with the group security program description and this sample's P03 and P07 results.
4. **Revisit trigger:** if the division starts hosting a system for clients (for example a shared data migration service), assess whether a SOC 2 report is needed.

**Corporate shared services** are part of the service organization, not a subservice organization. The group identity platform, SOC, cloud landing zones, backups, and personnel processes are described inside each report and tested by the service auditors. The group's own suppliers (cloud providers A and B, the identity SaaS vendor, the IT service management SaaS, and the managed model service) are subservice organizations presented with the **carve-out** method.

**Assurance alternatives and complements (not replacements):**
| Option | What it is | Role for the group |
|---|---|---|
| GovRAMP (formerly StateRAMP) | Nonprofit membership program, not law (N92-R08). SP 800-53-based verification for cloud providers serving state and local governments | Civic Suite already holds Authorized status. Agencies in several states now ask about the ACMP. Plan: use the ACMP SSP (P02), this readiness work, and the SOC 2 report as evidence for a GovRAMP verification of the ACMP in 2027, after POAM-001, POAM-011, and POAM-012 close |
| State CSA CJIS audits | Audits of each criminal justice agency and its contractors against CJISSECPOL v6.1 (N92-R02) | Required for the ACMP CJI cluster and the RMS regardless of SOC 2. Results are not shareable with other customers |
| IRS Office of Safeguards reviews | Reviews of each revenue agency, which can include contractor facilities (Pub. 1075 Exhibit 7 III; N92-R01) | Required for the 7 FTI tenants regardless of SOC 2 |
| FedRAMP | Federal authorization program (N51-R07) | Grants Management only. Its continuous monitoring discipline is the model for the Civic Suite and RMS change process |

## 2. System descriptions (scope)
### 2.1 ACMP (GovTech)
- **Services:** hosting, operation, and support of the ACMP tax compliance, supervision and court, and constituent services modules for about 430 agency tenants in 29 states; the integration gateway to revenue agency systems and 11 state message switches.
- **Infrastructure and software:** the ACMP production and non-production accounts in provider A's government-community landing zone; ACMP backups in the provider B vault; group identity (SYS-G1), SOC (SYS-G2), and cloud platform (SYS-G3) as internal shared services.
- **Subservice organizations (carve-out):** cloud provider A; cloud provider B (backup vault); identity SaaS vendor; IT service management SaaS.
- **Data:** FTI (7 dedicated tenants), CJI including CHRI (CJI cluster), and constituent data; about 27.7 million individuals.
- **Complementary user entity controls:** agencies enforce MFA and remove leavers in their identity providers; approve and review their users; keep FTI and CJI out of support tickets; tell the group promptly about suspected incidents on their side; maintain their IRS 45-day notifications with the services the group lists.

### 2.2 Public Safety RMS (Government Software Products)
- **Services:** records management for about 620 law enforcement agencies, with on-premises connectors at 41 agencies to state message switches and CAD; the AI report-writing assist beta for 37 agencies (since 2026-04-06).
- **Subservice organizations (carve-out):** cloud provider A; the managed model service (provider A government-community region). **The model service is not yet in the description** (P03 SW-G13).
- **Data:** CJI.
- **Complementary user entity controls:** agencies protect connector appliances on their premises, manage their users, and approve officer access.

### 2.3 Civic Suite (Government Software Products)
- **Services:** permitting, licensing, code enforcement, 311 (including an AI chatbot for residents), utility billing, and the permit plan review assistant for about 1,900 local governments.
- **Subservice organizations (carve-out):** cloud provider B; payment processor for utility billing.
- **Data:** constituent and permit data; payment pages hand card data to the processor.
- **Complementary user entity controls:** customer administrators manage users and use MFA; local governments approve published content used by the 311 chatbot.

## 3. Readiness results
### 3.1 ACMP (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 20 | 13 | 0 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** A1.3. Only per-tenant restores are tested; a full restore of about 430 tenants is estimated at more than 30 hours against the 8-hour contract RTO (POAM-011).
**Partially ready:** CC1.4 (corporate staff screening and training), CC2.3 (agency contacts and support terms), CC6.2 and CC6.3 (service accounts, dormant accounts, subcontractor staff), CC6.6 (directory trust to the acquired firm), CC6.7 (FTI and CJI in support tickets), CC7.1 (image remediation and guardrail exceptions), CC7.2 (no bulk-read alert), CC7.3 and CC7.4 (cross-division handling and notification), CC7.5 (recovery at scale), CC8.1 (emergency changes), CC9.2 (subcontractor flowdown and IRS notifications), and C1.1 (FTI log retention).

**What this means for the current period.** Every P07 finding falls inside the period that started 2026-07-01. The service auditor should be expected to report exceptions for controls that failed early in the period. The aim is to fix each control early enough that it operates for most of the period, and to describe the fixes accurately in management's description. The ACMP's design strengths (tenant isolation, FIPS 140-3 modules on CJI paths, customer-managed keys for FTI, immutable backups) are all Ready.

### 3.2 Public Safety RMS (`soc2-readiness-rms.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 24 | 8 | 1 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC6.7. 41 connectors use FIPS 140-2 certified modules, which CJISSECPOL v6.1 SC-13 does not accept after 2026-09-21 (POAM-021).
**Partially ready:** CC1.4 (31 support staff without checks for every state), CC2.3, CC3.4, CC8.1, CC9.2, and C1.1 (the AI assist beta and its model service: no description, no change review, no CJIS review, retention unconfirmed; POAM-022), CC6.6 (directory trust), CC7.3 and CC7.4 (handling consistency; RMS agency contacts missing from the matrix).

**The immediate issue is the 2026 report.** The beta has run since 2026-04-06 and sends CJI to the model service until that flow is stopped (target 2026-10-01, POAM-022). Management's description for the 2026 period must describe the beta, the model service as a subservice organization (carve-out, with the complementary subservice organization controls the group expects), and the change itself. Expect the service auditor to evaluate CC2.3, CC3.4, CC8.1, and CC9.2 for exceptions. The 37 beta agencies receive notice before the report is issued.

### 3.3 Civic Suite (`soc2-readiness-civic-suite.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 28 | 5 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Partially ready:** CC3.4 (the 2026-03 logging change not assessed as a GovRAMP significant change; POAM-023), CC6.1 (MFA optional for customer administrators in 9% of tenants), CC6.6 (directory trust), CC6.8 (no script integrity monitoring on the payment page), CC7.3 (handling consistency), and A1.3 (no second-region recovery test).

**Processing Integrity and Privacy** are out of scope in all three reports. No division makes processing integrity commitments today, and the agencies, not the group, give notice to and handle access and correction requests from the people in their records. The 311 chatbot and plan review assistant are described as features; if the Civic Suite starts making accuracy commitments for AI output, Processing Integrity will be evaluated (P10).

## 4. Remediation plan and evidence calendar
| Quarter | Report | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | RMS | CC2.3, CC3.4, CC8.1, CC9.2, C1.1 | Updated system description; beta agency notices; CJIS and vendor review of the model service; AI change gate records |
| 2026 Q4 | RMS | CC6.7 | Connector module replacement records; schedules sent to each CSA |
| 2026 Q4 | ACMP | CC1.4, CC6.2, CC6.3, CC9.2 | Group screening register; suspended-access records; service account onboarding; subcontractor flowdown checklist; updated IRS notifications |
| 2026 Q4 | ACMP, RMS, Civic Suite | CC6.6, CC7.2, CC7.3, CC7.4 | VPN MFA change; SIEM onboarding of the acquired estate; group handling procedure; completed notification matrix; tabletop report (2026-12-15) |
| 2026 Q4 | ACMP | CC2.3, CC6.7, CC7.1, CC8.1 | Support terms; ticket attachment block; image age gate; emergency change reviews |
| 2026 Q4 | Civic Suite | CC3.4 | GovRAMP significant change filing; updated change template |
| 2027 Q1 | ACMP | A1.3, CC7.5, C1.1 | Full-scale restore exercise report (2027-02-28); 7-year log retention settings |
| 2027 Q1 | Civic Suite | CC6.1, CC6.8 | MFA enforcement report; payment page script monitoring |
| 2027 Q2 | Civic Suite | A1.3 | Second-region recovery test |
| 2027 Q2 | ACMP | All in-scope criteria | Operating evidence through 2027-06-30 for the current ACMP period |

**Owner and follow-up.** The Group Chief Risk Officer's assurance team tracks this plan with the POA&M (P07) and reports quarterly to the board audit committee. The GovTech division president and the Government Software Products president brief their largest customers on the findings and fixes before each report is issued. The readiness review is repeated in 2027-01 for the RMS and Civic Suite 2027 periods.

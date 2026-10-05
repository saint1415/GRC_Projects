# SOC 2 Readiness Summary: Cris Santos Company | Dams | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (owner and operator of the fictional Bramble Shoals Hydroelectric Project) |
| Tier / Vertical | Micro / Dams |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is AICPA's |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the cooperative's generator security questionnaire and the cyber insurance renewal application |
| Part B | Review of the remote monitoring service vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Target report | None. No SOC 2 examination is planned |
| Prepared | 2026-08-20 by the Office and Compliance Administrator with the Plant Superintendent; approved by the Owner and General Manager 2026-08-31 |

## 1. Why SOC 2 (or an alternative) for this organization
**The company is not a service organization, so a SOC 2 report is not the right assurance product for it.** It sells electricity to one local cooperative under a power purchase agreement. It hosts, processes, and operates nothing for the cooperative or anyone else; the cooperative reads its own revenue meter. The recreation facilities are free. No customer has asked for a SOC 2 report, and the vertical lists no sector alternative to SOC 2. The assurance that matters most is regulatory: the FERC dam safety inspections and the Security Program, analyzed in P03.

The Trust Services Criteria are still useful here for two practical reasons:

**A. Answering two outside requests.**
- The cooperative sent a generator security questionnaire in July 2026, due **2026-09-30**. It asks about remote access to generator controls, MFA, and incident notice. Its questions follow the Trust Services Criteria, and its instructions accept a self-assessment.
- The cyber insurance renewal application, due **2026-11-01**, asks similar questions about MFA, backups, and remote access.

The company will answer both with this self-assessment, the POA&M (P07), and a named security contact. **It will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months; most of the company's controls were defined in August 2026, and an audit would cost far more than either request needs.

**B. Relying on the monitoring vendor.** The remote monitoring service carries the night alarm callouts (P05 BP-04) and runs the AI anomaly trial (P10). Its SOC 2 Type 2 report is the main evidence for the controls the company relies on there (SA-9). Reviewing it every year is part of POL-02 A.5.

**Why Availability and not another category.** The cooperative's questions are about whether the plant stays available and controlled, and the night callouts depend on the monitoring service. CEII protection is covered under the Security criteria and the FERC analysis in P03. Processing Integrity and Privacy were not requested, and the company processes no customer data.

## 2. System description (scope)
- **Services:** hydroelectric generation and dam operation at the Bramble Shoals project; license-required recreation facilities.
- **Infrastructure and software:** the HPCDMS (P02), the remote monitoring service, office IT, the productivity suite, the MSP-operated cloud backup, and the accounting and payroll services (P04).
- **People:** 7 employees, the controls integrator, the MSP, and the monitoring vendor.
- **Data:** CEII-type documents and control system details, dam safety instrument readings, employee personal information, business records.
- **Procedures:** POL-02, POL-03, POL-04, the P08 runbook, and the EAP.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 18 | 10 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: security roles and FERC contacts designated in writing
- CC3.1 and CC3.2: risk tolerance set and the first risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked in the POA&M
- A1.1: UPS, an annually load-tested generator for the gate hoists, and 60 days of local instrument storage

**Not ready:**
- CC1.4: no security training for anyone who operates the plant
- CC2.1: no OT inventory
- CC3.4: the remote desktop tool, the cellular gateway, and the AI add-on were added without a risk review
- CC6.1, CC6.2, CC6.3, and CC6.6: one shared remote password with no MFA, no account approvals or removals, and a bypassed firewall
- CC7.1 and CC7.2: no OT version tracking and no security monitoring
- CC7.5 and A1.3: OT recovery depends on 3-year-old integrator copies that have never been restored

The results match P01, P03, and P07: the weak area is remote access to the control system and its recovery, not the office or the cloud services.

**What the cooperative will be told.** Remote access to generator and gate controls today uses one shared password without MFA (limited to 5 staff since 2026-08-12, with the integrator's router off except for watched sessions from 2026-09-15). Named accounts with MFA are due 2026-11-30 (POAM-002). The company will notify the cooperative at once of any forced outage and of any security incident affecting generation (P08 matrix).

## 4. Evidence inventory
| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Monitoring vendor SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| EAP drill record and 18 CFR 12.54 gate and generator test statement | CC9.1, A1.1 | Yes | Yearly |
| MSP monthly report (office patching, antivirus, backup) | CC6.8, A1.2 | Yes (July 2026) | Monthly |
| Weekly remote session review checklist | CC7.2 | No | Weekly from 2026-09 |
| Remote access configuration (named accounts, MFA) | CC6.1 | No | 2026-11 |
| OT inventory and copy record | CC2.1, CC7.5 | No | 2026-10 |
| Training records | CC1.4, CC2.2 | No | 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |
| OT restore test record | A1.3 | No | 2027-03 |

## 5. Findings from the monitoring vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31, Security and Availability. One exception (a late quarterly review of vendor support staff access), remediated.
- **Scope gap:** the AI anomaly add-on is **outside the system description**, so no SOC 2 evidence covers it. P10 relies on the company's own trial results until the vendor adds it.
- **Availability:** the stated RTO of 12 hours is longer than the BIA's 8 hours for BP-04. That is acceptable only because an operator-mechanic can stay in the control room overnight during an outage (P05). RPO 15 minutes meets the BIA.
- **Controls the company must run** (complementary user entity controls): manage its portal accounts and MFA, protect the gateway credentials, keep callout lists current, and own every operational decision made from the data. Three are open gaps at the company: portal MFA (POAM-003), the gateway default password (POAM-009), and account removal (POAM-001). **The vendor's controls protect the company only once those gaps close.**
- **Follow-ups:** bridge letter to 2026-09-30; contract terms keeping the setpoint-write feature off and barring use of company data for other customers' models; 24-hour incident notice; the AI add-on in the next report (POAM-013).

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC1.5, CC6.4 | Acknowledgments; questionnaire response; lock change and key inventory (POAM-012) |
| 2026 Q4 | CC1.2, CC1.4, CC2.1, CC2.2, CC2.3, CC3.3, CC3.4, CC5.3, CC6.1, CC6.2, CC6.3, CC6.5, CC6.6, CC6.7, CC6.8, CC7.1-CC7.5, CC8.1, CC9.2, A1.2 | Monthly oversight notes; training (POAM-011); OT inventory (POAM-007); change form; remote access rebuild and MFA (POAM-002, POAM-003); firewall and router (POAM-004, POAM-005); account process (POAM-001); session review (POAM-010); OT copies and recovery procedure (POAM-006); vendor terms (POAM-013) |
| 2027 Q1 | CC5.1, CC5.2, A1.3 | HMI replacement (POAM-008); first OT restore test |
| 2027 Q2 | CC9.1 | Hurricane checklist in the OT recovery procedure (P01 R-013) |

**Response to the cooperative:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Plant Superintendent as security contact, and commit to an updated self-assessment in April 2027. The same package supports the insurance renewal application due 2026-11-01.

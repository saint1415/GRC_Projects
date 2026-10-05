# SOC 2 Readiness Summary: Cris Santos Company | Energy | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (small intrastate natural gas transmission pipeline operator) |
| Tier / Vertical | Micro / Energy |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1), as a self-assessment |
| Target report | None. The company is not a service organization and does not plan a SOC 2 examination |
| Part A | Readiness self-assessment (`soc2-readiness.csv`), used to answer the municipal gas system's supplier questionnaire |
| Part B | Review of the hosted SCADA vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-04 by the Office Manager and the Operations Manager with the independent consultant; approved by the Owner 2026-09-15 |

## 1. Why SOC 2 (or an alternative) for this organization
**The company is not a SOC 2 service organization.** SOC 2 reports on controls at a company whose services affect its customers' own information systems. Cris Santos Company transports natural gas. Its customers depend on the gas, not on company systems that process their data.

**The assurance alternative named for this vertical does not apply either.** The overlay names TSA pipeline security directive compliance reviews, but those are only for TSA-designated pipelines, and this pipeline is not designated (P03). FPSC inspections under 49 CFR Part 192 are pipeline safety inspections, not cybersecurity assurance.

**So the company uses the Trust Services Criteria in two practical ways:**
- **A. Answering a questionnaire.** In July 2026 the municipal gas system, the company's largest customer, sent a supplier questionnaire on cybersecurity and supply reliability, after its own insurer asked it to review critical suppliers. The questions follow the Security and Availability criteria. The company will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-10-15. The municipal system said in its instructions that a self-assessment is acceptable.
- **B. Relying on the SCADA vendor.** The hosted SCADA vendor carries most of the inherited controls for the pipeline's control system (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls, and reviewing it each year is part of supplier oversight (POL-02 A.4; SA-9).

**Why Availability and not another category.** The municipal system's main question is whether gas will keep arriving and whether the company can see and control the line. The company cannot see the pipeline without the SCADA platform, the telemetry, and its devices (P05). Confidentiality, Processing Integrity, and Privacy were not requested. The company holds personal information only about its own employees.

**Why not a SOC 2 audit or another option.** A Type 2 report needs controls that have operated for a period, and most of the company's controls were defined in September 2026. An OT-focused third-party assessment (such as one based on ISA/IEC 62443) would be more useful for the pipeline itself, and the 2026 independent assessment (P07) is a first step toward it.

## 2. System description (scope)
- **Services:** natural gas transportation from one interstate tap to 3 delivery stations, with gas control, nominations, measurement, and billing.
- **Infrastructure and software:** the Pipeline SCADA and Gas Control System (P02), office IT, and business SaaS (P04).
- **People:** 7 employees, the MSP, and the SCADA vendor.
- **Data:** SCADA and measurement data, customer contracts and nominations, and employee personal information.
- **Procedures:** POL-02, POL-03, POL-04, the P08 runbook, the O&M manual, and the emergency plan.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 7 | 16 | 10 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles designated in writing
- CC3.1 and CC3.2: risk tolerance set and the 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: fenced and locked field sites; vendor data centers under SOC 2
- CC6.7: encrypted telemetry and web traffic
- A1.1: SCADA capacity managed by the vendor

**Not ready:**
- CC2.1: no PSGCS inventory
- CC3.4 and CC8.1: changes, including the vendor's, are not approved or assessed
- CC6.1, CC6.2, and CC6.3: password-only SCADA access, a shared login, and late removal
- CC7.1, CC7.2, and CC7.3: no vulnerability tracking, log review, or incident log
- CC7.5 and A1.3: recovery unproven (no configuration copy, no restore test)

The pattern matches P03 and P07: the governance and risk work done in 2026 is ready; the company's side of access, change, and recovery is not.

## 4. Evidence inventory
What the company can send the municipal system now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation memo; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-10) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-10) |
| SCADA vendor SOC 2 review | CC9.2, A1.1, A1.2 | Yes | Bridge letter (2026-10) |
| Emergency plan and November 2025 drill report | CC9.1 | Yes | Tabletop report (2026-11) |
| MSP monthly report (patching, antivirus) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| SCADA user reviews and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| PSGCS inventory and SIM status | CC2.1, CC6.6 | No | 2026-10 |
| Configuration exports and restore test records | CC7.5, A1.3 | No | Quarterly from 2026-10 |
| Training and phishing simulation records | CC1.4, CC2.2 | No | From 2026-10 |

## 5. Findings from the SCADA vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-06-30. One exception (2 of 25 sampled platform releases deployed without documented change approval), remediated.
- **Availability:** the vendor's RPO of 15 minutes meets the BIA (1 hour), but its **RTO of 4 hours does not meet the 2-hour target** for gas control (P05). Manual operation must cover hours 2 to 4.
- **Not covered:** the leak-detection anomaly module was released after the report period began and is outside its scope. The company treats it as unassured (P10).
- **Controls the company must run.** The report lists complementary user entity controls: user and role management, enabling MFA, prompt removal, audit log review, approval of the customer's own configuration changes, and endpoint protection. **All were open gaps at the company at fieldwork** (POAM-001, POAM-002, POAM-004, POAM-010). The vendor's controls protect the pipeline only once the company runs its side.
- **Follow-ups:** bridge letter to 2026-09-30; 24-hour incident notice and notice of support sessions and releases in a security addendum; raise the RTO at renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q4 (by 2026-10-31) | CC1.1, CC2.1, CC2.2, CC2.3, CC5.2, CC5.3, CC6.2, CC6.3, CC7.3 | Acknowledgments; questionnaire response; inventory (POAM-006); named accounts and last-day checklist (POAM-001); SCADA MFA (POAM-002); incident log |
| 2026 Q4 (by 2026-12-31) | CC1.2, CC1.5, CC3.4, CC5.1, CC6.1, CC6.5, CC6.6, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, A1.2, A1.3 | Monthly oversight notes; desk segment (POAM-004); EDR; log review (POAM-010); tabletop and restore tests (POAM-008, POAM-009); configuration exports (POAM-007); supplier addendums (POAM-011); second-carrier SIMs |
| 2027 | CC1.4, CC3.3 | OT security course for the Operations Manager (2027-03-31); fraud scenarios in the July 2027 risk assessment |

**Response to the municipal gas system:** send this summary, the readiness checklist, and the POA&M by 2026-10-15, name the Office Manager as security contact, and commit to an updated self-assessment in April 2027.

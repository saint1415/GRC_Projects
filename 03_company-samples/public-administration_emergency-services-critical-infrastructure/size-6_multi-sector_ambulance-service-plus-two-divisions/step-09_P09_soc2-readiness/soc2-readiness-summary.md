# SOC 2 Readiness Summary: Cris Santos Company Holdings | Emergency Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Emergency Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). Two readiness reports, both for Billing and Dispatch Services (BDS): dispatch services (`soc2-readiness.csv`, first readiness) and revenue cycle services (`soc2-readiness-revenue-cycle.csv`, existing Type 2). Ambulance Services and Urgent Care are out of scope |
| Prepared | 2026-09-02 by the Group Chief Risk Officer's assurance team with the BDS security and compliance lead; presented to the board risk committee 2026-09-16 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations build their own controls on.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| BDS | Revenue cycle services for about 170 external clients and both internal divisions | **Yes.** Clients rely on BDS for claims, payment posting, and the PHI it holds as their business associate | **In scope (continuing).** Existing annual Type 2 | Security, Availability, Confidentiality, Processing Integrity | Type 2, 12 months ending June 30 |
| BDS | Dispatch services for 14 external EMS agencies (and the Ambulance division) | **Yes.** Client agencies rely on the CAD and the communications centers to dispatch their units; 9 of 14 asked for a report in 2026 | **In scope (new).** First readiness assessment | Security, Availability, Confidentiality | Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| BDS | Patient billing contact center | Part of revenue cycle services | Covered by the revenue cycle report; card data assurance comes from PCI DSS, not SOC 2 | n/a | PCI DSS validation (P03) |
| Ambulance Services | Ambulance response and transport | **No.** Patients and counties receive a health care service, not an outsourced system they build controls on | **Out of scope** (reasons below) | n/a | n/a |
| Urgent Care | Clinic and telehealth visits | **No.** Patients are not user entities | **Out of scope** | n/a | n/a |

**Why Ambulance Services is out of scope:**
1. **No user entities.** Counties contract for ambulance coverage and response times, not for the use of Ambulance Services' information systems inside their own control environment.
2. **Assurance comes from other sources.** State EMS licensing and inspections, county contract performance reports, Medicare enrollment, and HIPAA obligations (P03 regulation-by-division matrix).
3. **County questionnaires** are answered with the group security program description and this sample's P03 and P07 results.
4. **Revisit trigger:** if Ambulance Services starts offering its systems (for example, its ePCR tenant or crew scheduling) to other agencies, assess whether a SOC 2 report is needed. Dispatch is already offered through BDS, which is why the dispatch report sits there.

**Why Urgent Care is out of scope:** it delivers care to patients and has no user entities. Assurance comes from HIPAA, Medicare and Medicaid program rules, and state licensing.

**Other assurance options considered.** The Emergency Services overlay names no standard alternative to SOC 2. Some EMS agencies ask about the FBI CJIS Security Policy for dispatch vendors; that applies only if BDS handles criminal justice information, which is under review for one county (P03 BD-G28), and it is not a substitute for SOC 2. For card payments, PCI DSS (N56-R06) is the assurance mechanism clients and acquirers expect.

## 2. System descriptions (scope)
### 2.1 Dispatch services
- **Services:** call intake, emergency medical dispatch, unit recommendation and status, and CAD-to-CAD exchange for 14 client agencies, from 4 regional communications centers.
- **Infrastructure and software:** the CAD and integration engine on the group cloud platform (provider A; moving out of the legacy account, POAM-012); communications center consoles, call handling, and radio console gateways; group identity (SYS-G1) and SOC (SYS-G2) carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud provider A; the CAD vendor (software support and the AI triage service). The AI triage service must be described, and client agencies' callers are excluded from it until their agreements are amended (POAM-017).
- **People:** about 1,100 telecommunicators, center supervisors, the platform team, and group SOC and identity teams.
- **Data:** client agencies' incident and patient data in their CAD partitions.
- **Complementary user entity controls:** client agencies manage their own users in federation, keep their duty officer contacts current, and maintain their own radio and PSAP arrangements.

### 2.2 Revenue cycle services
- **Services:** coding, claim submission, payment posting, denials management, and the patient billing contact center for about 170 clients.
- **Infrastructure and software:** the revenue cycle platform on provider A, file transfer servers (moving out of the legacy account), the contact-center service, and clearinghouse connections.
- **Subservice organizations (carve-out):** cloud provider A; the contact-center SaaS vendor; clearinghouses.
- **Data:** client patients' PHI in about 34 million patient accounts.
- **Complementary user entity controls:** clients supply complete clinical documentation, approve coding policies, and review remittance reports.

## 3. Readiness results
### 3.1 Dispatch services (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 20 | 12 | 1 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first-time report:** the control environment, risk assessment, monitoring, identity, and SOC criteria are met by group common controls already evidenced in the revenue cycle report.
**Not ready:** CC2.3 (no system description or standard commitments to client agencies, and the AI triage processing was not disclosed to them) and A1.3 (CAD failover never tested; drills assume a few hours).
**Partially ready:** CC2.1, CC3.4, CC4.1, CC5.3, CC6.2, CC6.3, CC6.7, CC7.1, CC7.2, CC7.4, CC9.1, CC9.2, A1.2, and C1.1. Most map directly to the DPCP findings in P07 (vendor access, the legacy account, monitoring gaps, the missing CAD standby, and the county premise notes).

**Timing.** A Type 1 as of 2027-06-30 is realistic only if POAM-003, POAM-012, and POAM-017 close on schedule. A1.3 depends on the provider B standby (POAM-013, 2027-06-30). If the standby slips, the Type 1 should go ahead with Availability described as it is, rather than wait.

### 3.2 Revenue cycle services (`soc2-readiness-revenue-cycle.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 27 | 6 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**Partially ready:** CC3.4 and PI1.3 (the claim coding assistant went live on 2026-07-15, after the last report period, and must be described with accuracy controls for the period ending 2027-06-30), CC6.5 and C1.2 (disposal certificates and the 90-day file retention), CC6.7 and CC7.2 (the file transfer servers in the legacy account), CC7.4 (72-hour client notices not exercised), and CC9.2 (no PCI DSS attestation from the contact-center vendor). **No criterion is Not ready**, so the 2027 report can proceed on schedule; the service auditor should expect to test the coding assistant and the file transfer move.

## 4. Remediation plan and evidence calendar
| Quarter | Service line | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | Dispatch | CC3.4, CC6.3, CC9.2, C1.1 | AI mode-change gate; PAM vendor sessions; BAA amendment and client notices; CJIS determination and purge record |
| 2026 Q4 | Revenue cycle | C1.2, PI1.3, CC7.4 | 14-day purge job; coding audit by level of service; tabletop record |
| 2027 Q1 | Both | CC6.7, CC7.1, CC7.2 | Migration out of the legacy account; scan scope; SIEM sources for the new accounts |
| 2027 Q1 | Dispatch | CC2.1, CC2.3, CC4.1, CC5.3, CC6.2, CC7.4 | Inventory; system description; audit plan; interface field lists; identity governance for CAD accounts; client call tree |
| 2027 Q2 | Dispatch | CC9.1, A1.2, A1.3 | Provider B standby; failover test; multi-day drill. Type 1 as of 2027-06-30 |
| 2027 Q1 to Q2 | Revenue cycle | CC6.5, CC9.2, CC3.4 | Destruction certificates; vendor PCI attestation; updated system description |

**Communication:** the BDS president sends the 14 dispatch clients a readiness letter with the 2027 timeline and a plain statement that their callers' audio has been excluded from the AI triage module until their agreements are amended.

# SOC 2 Readiness Summary: Cris Santos Company Holdings | Admin and Support Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Administrative and Support and Waste Management and Remediation Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division and service line (section 1). One readiness report: Staffing's Managed Workforce Solutions program (`soc2-readiness.csv`). Consulting and Home Health are out of scope, with reasons |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the Staffing security and compliance lead and the Managed Workforce Solutions vice president |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service and build their own controls on it. The question for each service line is whether clients rely on the group's systems as part of their own control environment.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Staffing | **Managed Workforce Solutions**: managed service provider programs run on a VMS tenant the division configures and operates for 48 clients and about 1,900 suppliers (requisitions, timesheets, consolidated invoicing) | **Yes.** Clients rely on the program's controls over their contingent workforce data and on the accuracy of consolidated invoices; 31 client contracts require a SOC 2 Type 2 report by 2027-12-31 | **In scope.** First readiness assessment | Security, Availability, Confidentiality, Processing Integrity | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| Staffing | Commercial, Professional, and Healthcare Staffing placements | No. The group supplies workers who work under client supervision; clients do not rely on group systems to process their data. Client questionnaires are answered from P03 and P07 | Out of scope | n/a | n/a |
| Consulting | Health IT Advisory, HR Technology Consulting, Federal Solutions | **No.** Consultants work inside clients' own systems; Consulting operates no system that clients use to process their transactions. Hospital clients rely on BAAs (HIPAA) and federal agencies on FAR 52.204-21 | **Out of scope** (reasons below) | n/a | n/a |
| Home Health | Home health services to patients | **No.** Patients and payers are not user entities | **Out of scope** | n/a | n/a |
| Corporate | Group Workforce Platform | Internal shared service, not offered to outside entities | Out of scope as a report; **carved in** to the MWS report as an internal shared service (payroll for program workers; identity; SOC) | n/a | n/a |

**Why Consulting is out of scope:**
1. **No system offered to clients.** Health IT consultants and HR technology consultants work in the client's EHR or HR tenant, under the client's controls. The client's own SOC reports and controls cover those systems.
2. **Assurance comes from other mechanisms.** HIPAA business associate agreements (with Consulting's own HIPAA program, P03) cover hospital clients; FAR 52.204-21 and agency oversight cover Federal Solutions.
3. **Revisit triggers:** if Consulting begins operating payroll or HR systems for clients as a managed service, a **SOC 1** report (controls relevant to clients' financial reporting) is likely needed first; if it offers the denial-prediction model (P10 AI-008) as a hosted service, a SOC 2 report with Processing Integrity would be considered.

**Why Home Health is out of scope:** patients and Medicare do not rely on a SOC report. Home Health is surveyed against the Medicare conditions of participation and regulated under HIPAA (P03).

**Other assurance options considered.** The vertical overlay names no standard assurance alternative for staffing firms. Some hospital clients accept HITRUST certification from Consulting; the group decided not to pursue it now because no contract requires it.

## 2. System description (scope)
- **Services:** requisition intake and distribution to suppliers, supplier onboarding and compliance tracking, timesheet capture and approval, rate management, and weekly consolidated invoicing for 48 clients.
- **Infrastructure and software:** the VMS tenant (vendor SaaS) configured and operated by Managed Workforce Solutions; integrations to clients' systems and to the GWP for workers the program payrolls; group identity (SYS-G1) and SOC (SYS-G2) carved in as internal shared services.
- **Subservice organizations (carve-out):** the VMS vendor (SOC 2 Type 2 on file); cloud provider A for the integration platform.
- **People:** about 160 program managers and coordinators, plus group identity, SOC, and payroll teams.
- **Data:** client requisitions and cost centers, supplier rates and markups, worker names, timesheets, and invoices (Confidential under POL-04).
- **Complementary user entity controls:** clients approve timesheets, provision and remove their own hiring managers, and review consolidated invoices.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 22 | 9 | 2 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first report:** control environment, risk assessment, identity, network, malware, and incident evaluation criteria are met by group common controls that P07 already tested (118 of 133 common statements satisfied).

**Not ready:**
- **CC2.3:** there is no system description, and service commitments are scattered across 48 contracts.
- **CC7.2:** VMS tenant audit logs are not monitored (P07 AU-6 finding; POAM-016).
- **A1.3:** manual program procedures and vendor recovery have never been tested.

**Partially ready:** CC2.1, CC3.3, CC4.1, CC5.3, CC6.2, CC6.3, CC7.4, CC8.1, CC9.2, C1.1, C1.2, PI1.3, and PI1.5. Most are program-level documentation and access hygiene: client and supplier user provisioning without approval records, 37 supplier users of ended programs still active, configuration changes without peer review (P01 ST-014), and manual invoice reconciliation without evidence.

**Processing Integrity is in scope** because clients pay on the consolidated invoice and their contracts promise invoice accuracy. **Privacy is out of scope:** the program makes no privacy commitments to clients; worker privacy is handled under group policy and state law.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC3.3, CC6.3, CC7.2, CC7.4 | Monthly audit log reviews; access review and cleanup; SIEM onboarding; MSP clients in the 2026-12-15 tabletop |
| 2027 Q1 | CC2.1, CC2.3, CC4.1, CC5.3, CC6.2, CC8.1, CC9.2, A1.3, C1.1, C1.2, PI1.3, PI1.5 | System description and commitments schedule; data flow documentation; procedure sets; request workflow; peer review and configuration tests; vendor complementary control map; outage exercise with 3 clients; export labels; end-of-program data procedure; reconciliation sign-offs; retention entries. **Type 1 as of 2027-03-31** |
| 2027 Q2 to Q3 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30) |
| 2027 Q4 | n/a | Type 2 report issued before the 2027-12-31 contract deadline |

**Communication:** the Managed Workforce Solutions vice president sends the 31 clients whose contracts require a report a readiness letter with this timeline, and offers the other 17 clients the report when it is issued.

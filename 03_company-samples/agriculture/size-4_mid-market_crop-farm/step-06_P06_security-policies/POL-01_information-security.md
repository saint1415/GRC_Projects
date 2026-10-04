# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-30, PL-1, PS-8, RA-3, CA-2, CA-5, SA-4, SA-9, SR-2, SR-6 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RM-02, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-01, GV.SC-05, GV.SC-07 |
| Benchmark and other requirements | NIST CSF 2.0 (voluntary benchmark, P03); NIST SP 800-82 Rev. 3 for OT; Fla. Stat. 501.171(2) and (6); 7 CFR 46.32(b) (grower accounting records) |
| Languages | Issued in English; a Spanish summary is given to all field staff at pre-season meetings |
| Supporting standards | See `standards-index.md` (STD-01 to STD-11) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of company, worker, grower, and customer information and of the systems that grow, protect, pack, and ship the company's crops. Because the company's operational technology (OT) controls water, fertilizer, ripening gas, and cold storage, the program also protects crops, food safety, and worker safety.

## 2. Scope
All workforce members (year-round employees, seasonal employees including H-2A workers, contractors, and vendor staff working on company systems) at headquarters, the Irrigation Operations Center (IOC), the central packinghouse, Farms 1 to 3, and the H-2A housing sites. It covers all systems and data: the Farm Management and Irrigation Control Platform (FMICP, P02), its OT (SCADA, PLCs, pumps, fertigation, pivots, sensors, packinghouse controls), the cloud landing zone, the grower portal and settlement service, SaaS services, and systems that vendors operate for the company. Any farm or business the company acquires is in scope from the date it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, incidents, and the roadmap |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and FMICP system owner; approves POL-02 to POL-05 and the standards; accepts Moderate risks |
| Chief Financial Officer | IT and security report through the CFO; owns finance and settlement payment controls |
| vCISO (part-time contractor) | Owns this policy and the program strategy; reports to the audit committee |
| Security Manager | Designated security lead (in writing); runs the program day to day; risk register, POA&M, vendor reviews, MSSP oversight |
| IT Director | IT control owner: identity, networks, IT/OT boundary firewalls, endpoints, cloud, backups |
| Director of Irrigation and Water Resources | OT control owner for irrigation, fertigation, pumps, pivots, sensors, and freeze protection |
| Packinghouse Manager | OT control owner for packing lines, graders, cooling, ripening, cold storage, and cold-chain alarms |
| Director of Food Safety and Quality | Owner of Produce Safety, pesticide application, and traceability records; food defense plan |
| HR Director | Worker data, H-2A records, sanctions with the Security Manager |
| Vice President of Grower Services | Owner of the grower portal and settlement service, including the development firm |
| Precision Agriculture Manager | Owner of the AI portfolio (P10) with the vCISO; drone program |
| Co-sourced internal audit firm | Independent annual control assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

**Where roles overlap.** The IT Director runs controls that the Security Manager monitors. Because both report through the CFO, the co-sourced internal audit firm (reporting to the audit committee) assesses the controls independently each year (P07), and the vCISO reports to the audit committee directly.

## 4. Policy statements
4.1 The company must maintain an information security program, documented in this policy set, the supporting standards, and the System Security Plan, and measured against the NIST CSF 2.0 Target Profile in P03. OT security must follow NIST SP 800-82 Rev. 3. (PM-1; GV.PO-01)
4.2 The Security Manager is the designated security lead. The designation must be in writing and reaffirmed each year. OT control owners (section 3) must be named in writing for irrigation and for the packinghouse. (PM-2; GV.RR-02)
4.3 An enterprise risk assessment must be performed at least annually and after major changes (including acquisitions), using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-05)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. **No risk that could plausibly send unsafe produce to customers or expose workers to chemicals may be accepted above Low.** (PM-9; GV.RM-02)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, incidents, and progress against the P03 roadmap. (CA-5; GV.OV-01)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.8 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm, from retraining to termination. Sanctions are applied the same way to every worker regardless of visa status, and HR documents each one. (PS-8; GV.RR-04)
4.9 **Suppliers.** Before any vendor receives company data or access to company systems, it must pass a security review scaled to its tier and sign security terms under STD-03. Vendors with access to OT or to company code (SCADA integrator, pivot manufacturer, refrigeration contractor, development firm) must accept named accounts, brokered and recorded access, breach notice within 72 hours, and, for code, secure development terms. Purchasing must not issue a purchase order to such a vendor without the Security Manager's approval. Third-party agents that hold personal information must also notify the company of a breach within the 10 days the law allows (Fla. Stat. 501.171(6)). (SA-4; SA-9; SR-2; PM-30; GV.SC-01; GV.SC-05)
4.10 Tier 1 vendors (those with privileged or OT access, personal information at scale, or that support a High-criticality BIA process) must be reassessed each year, including a review of their SOC 2 report or equivalent (STD-03; P09). (SR-6; GV.SC-07)
4.11 Security controls must be independently assessed at least annually (P07) and after major changes. (CA-2; ID.IM-01)
4.12 Security policies, risk assessments, assessments, and incident records must be retained for at least 3 years. Regulated records follow the retention schedule in POL-04. (PL-1; GV.PO-02)
4.13 AI tools, and AI features turned on in existing tools, must be approved through the AI governance process (STD-05; P10) before use. No AI may act automatically on irrigation, spraying, or grower settlements without the controls P10 sets. (PM-9; GV.RM-01)
4.14 Legal, regulatory, and contractual security requirements must be kept in the requirements register (P03 workbook) and reviewed each July with outside general counsel. (GV.OC-03)

## 5. Compliance and enforcement
Violations are handled under section 4.8. Compliance is checked through the annual independent assessment (P07), quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); risk register and appetite statements (P01); gap analysis and roadmap (P03); NIST CSF 2.0; NIST SP 800-82 Rev. 3; Fla. Stat. 501.171

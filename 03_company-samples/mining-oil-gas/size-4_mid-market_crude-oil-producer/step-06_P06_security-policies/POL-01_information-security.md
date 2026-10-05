# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | Security Manager (Information Security Lead) |
| Approved by | Chief Executive Officer, with the VP Operations agreeing to the statements that affect field operations; noted by the board audit committee |
| Approval date | 2026-09-16 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes (acquisitions, gathering system changes, a TSA notification) or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, CA-5, CM-4, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RM-02, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.RA-05, ID.IM-01 |
| Benchmark (N21-BM) | NIST CSF 2.0 with NIST SP 800-82 Rev. 3, sections 3.3.1 (governance), 3.3.4 (policies), 4.1 (OT risk management), 6.1.5 (supply chain) |
| Binding rules referenced | 49 CFR 195.11(d) (gathering line records); Fla. Stat. 501.171(2) (reasonable security measures) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects the safety and reliability of field and gathering operations, the integrity of production and custody transfer measurement, and the confidentiality of royalty owner, employee, shipper, and reservoir information.

## 2. Scope
All workforce members (employees, contractors, and temporary workers) at headquarters, the 3 field offices, the Operations Control Center (OCC), the Backup Control Center (BCC), the Panhandle Central Facility, and every well site and facility. It covers business IT and operational technology (OT): corporate systems, the cloud landing zone, SaaS applications, the SCADA system, field controllers, flow computers, and field communications, including systems that vendors operate for the company. Any field or company acquired by Cris Santos Company is in scope from the date it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor of the program and system owner of the FSPA; approves POL-02 to POL-05; accepts Moderate risks; chairs the crisis management team |
| VP Operations | Must agree to any policy statement, exception, or risk acceptance that affects field operations or safety |
| General Counsel | Tracks legal and contractual requirements with the Security Manager; owns contract security terms and breach determinations |
| Security Manager (Information Security Lead) | Owns this policy and the program day to day; maintains the risk register, SSP, and standards index; oversees the MDR provider; dotted line to the audit committee chair |
| SCADA and Automation Manager | OT technical owner; approves every security change to SCADA and field devices for operational impact |
| OT Security Engineer | OT security day to day (OT DMZ, jump host, OT monitoring, OT patching); reports to the SCADA and Automation Manager with a dotted line to the Security Manager |
| VP IT | Owns business IT, the cloud landing zone, and the identity provider |
| Pipeline Compliance Manager | Makes sure security decisions keep the gathering system within its Part 195 duties |
| HSE Director | Reviews any change that touches shutdown logic or safety alarms |
| Co-sourced internal audit firm | Independent annual control assessment (P07) |
| All workforce | Follow the policies; report suspected incidents immediately (POL-03 4.2) |

**IT and OT split.** The Security Manager owns the program and the business IT side. The OT Security Engineer and the SCADA and Automation Manager own the OT side. A written RACI, reaffirmed each year with this policy, lists who decides, who does the work, and who must be consulted for each control family on each side.

## 4. Policy statements
4.1 The company must maintain an information security program that covers both business IT and OT, documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01)
4.2 The Security Manager is the designated Information Security Lead, and the OT Security Engineer is the designated OT security lead. Both designations, and the IT and OT RACI in section 3, must be in writing and reaffirmed each year. (PM-2; GV.RR-02)
4.3 An enterprise risk assessment must be performed at least annually and after major changes (acquisitions, gathering system expansions, new vendor connections to OT), using NIST SP 800-30 Rev. 1 and the OT threat guidance in NIST SP 800-82 Rev. 3. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-05)
4.4 **Risk acceptance authority and appetite.** Risk owners may accept Very Low and Low risks. The COO may accept Moderate risks, with the VP Operations' agreement when field operations or safety are affected. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair while treatment is under way. No cyber risk that could plausibly cause an injury, an H2S exposure, or a release of oil or produced water may be accepted above Low; any such risk rated Moderate or higher must have a funded treatment plan within 90 days. The risk appetite statements in the risk register (P01) apply. (PM-9; GV.RM-01; GV.RM-02)
4.5 **Safety first.** No security control, test, scan, or change may disable, bypass, or slow a safety shutdown or safety alarm, including the hardwired H2S, tank high-level, and compressor emergency shutdowns and the gathering pump station's high-pressure shutdown switches. Every security change to SCADA or field devices must be reviewed for operational and safety impact by the SCADA and Automation Manager before it is made, and changes that touch shutdown logic also by the HSE Director. (CM-4; GV.RM-02)
4.6 The Security Manager must report to the audit committee each quarter on the top risks, POA&M status, incidents, OT metrics, and progress against the program roadmap. (CA-5; PM-9; GV.OV-01)
4.7 Security policies must be reviewed at least annually and after major changes or incidents. Each supporting standard must be reviewed at least annually by its owner. (PL-1; GV.PO-02)
4.8 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. Good-faith incident reporting is never sanctioned. (PS-8; GV.RR-04)
4.9 **Suppliers.** No supplier may connect to the SCADA network or receive Restricted data (POL-04) until it has signed the company's security schedule (named accounts, MFA, incident notice, cooperation in breach response, data return and deletion) and passed a security review scaled to its tier (STD-03). **No supplier connection to OT, including cellular gateways, support modems, and remote access tools, may be installed or enabled without a review by the OT Security Engineer.** Purchasing must not issue a purchase order for such a service without the Security Manager's approval. Existing contracts must add the schedule at renewal. (SA-9; GV.SC-05)
4.10 **Exceptions.** Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months or less. Exceptions for OT systems also require the VP Operations' agreement. (PL-1; GV.PO-01)
4.11 Tier 1 suppliers (those with SCADA network access, Restricted data at scale, or support for a High-criticality BIA process) must be reassessed each year, through a SOC 2 report review or an OT vendor assessment (STD-03; P09). (SR-6; GV.SC-07)
4.12 Security controls must be assessed at least annually by an assessor independent of their operation (the co-sourced internal audit firm, P07), and after major changes. (CA-2; ID.IM-01)
4.13 General Counsel and the Security Manager must review the cybersecurity laws, rules, and contract terms that apply to the company each quarter, and recheck applicability whenever a trigger occurs: a TSA notification for the gathering system, publication of the CIRCIA final rule, a new unusually sensitive area along the gathering system, an acquisition, or growth past the SBA size standard. (PL-1; GV.OC-03)
4.14 Security policies, standards, risk assessments, assessment results, and incident records must be retained for at least 6 years. Gathering system records follow 49 CFR 195.11(d) (segment identification and internal corrosion records for the life of the pipe) when that period is longer. (SI-12; GV.PO-02)
4.15 AI tools and AI features must be approved through the AI governance process (STD-05; P10) before use. No AI tool may write to SCADA or field devices, and no AI tool may make an employment decision without human review. (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (section 4.8). Compliance is checked through the annual independent control assessment (P07), the quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.10. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); Regulatory Gap Analysis and roadmap (P03); emergency response plan and pipeline emergency procedures; NIST SP 800-82 Rev. 3

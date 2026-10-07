# Scenario facts: Cris Santos Company | Utilities | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given; regulation text was read from eCFR (point-in-time 2026-09-23) or the official publisher.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Electric Cooperative, Inc. (member-owned, not-for-profit electric cooperative; the README tier defaults "Cris Santos Company, LLC" and "privately held by Cris Santos" do not fit a cooperative and are replaced here) |
| Legal form and ownership | Cooperative, nonprofit, membership corporation organized under Florida's Rural Electric Cooperative Law (Fla. Stat. chapter 425; purpose in 425.02). Owned by its members, one member, one vote. A Board of Trustees of 7 member-elected volunteers governs it. There are no shareholders |
| Business | Electric power distribution (NAICS 221122). Buys all of its power from a generation and transmission cooperative (the **G&T**, of which it is a member) under a full-requirements wholesale power contract, and delivers it over its own 12.47 kV distribution system to residential and commercial members |
| Location | Florida (one rural county). Headquarters on one site: office, warehouse, truck yard, and standby generator. One distribution substation (**Substation 1**) about 3 miles away |
| Members and load | About 820 meters: 742 residential and 78 commercial, including the county water treatment plant, a K-8 school, a medical clinic, and a county fire station. 26 residential members are on the medical-needs list (they depend on electric medical equipment). 128 miles of overhead line on 3 feeders. 2025 peak load 2.6 MW |
| Workforce | 7 employees: General Manager, Office and Finance Manager, Member Services Representative, Line Superintendent, 2 Journeyman Lineworkers, and a Meter and Service Technician |
| Revenue | About $1.1 million a year in total operating revenue (fictional), about $3,000 a day. Purchased power from the G&T is about $640,000 a year (about $53,000 a month, paid by ACH). The SBA standard for NAICS 221122 is 1,100 employees (13 CFR 121.201), so the cooperative is SBA-small |
| Financing | **Rural Utilities Service (RUS) electric distribution borrower.** Its RUS loan contract and mortgage carry the operations and maintenance duties in 7 CFR Part 1730. Last RUS operations and maintenance review (RUS Form 300): March 2023. Next review planned for March 2027. A new RUS loan application (substation transformer replacement and AMI upgrade) is planned for the first half of 2027 |
| Grid connection | One delivery point. The G&T owns the 69 kV radial tap line, the high-side circuit switcher and its protection, and the wholesale meter at Substation 1. The cooperative owns the 69/12.47 kV transformer, the low-side bus, 3 feeder reclosers, and the voltage regulators. It owns no facility operated at 100 kV or above |
| NERC registration | **Not registered** on the NERC Compliance Registry. The Distribution Provider criteria in NERC Rules of Procedure Appendix 5B (Revision 8, effective 2024-06-27) are not met: III.a.1 (peak 2.6 MW, far below 75 MW, and served from a 69 kV tap, not directly from the BES); III.a.2 (no UVLS program, Remedial Action Scheme, or transmission Protection System); III.a.3 (no Nuclear Plant Interface Requirements); III.a.4 (no field switching tasks in a Transmission Operator restoration plan); III.b (no UFLS relays: the required UFLS program for this load is carried out by the G&T at its own transmission substations). The G&T confirmed in writing in 2024 that it does not rely on cooperative equipment for UFLS |
| State regulation | Under Fla. Stat. 366.02 the cooperative is an "electric utility" (366.02(4)) but not a "public utility" (366.02(8) excludes cooperatives organized under the Rural Electric Cooperative Law). The Florida Public Service Commission has limited jurisdiction, for example over rate structure (366.04(2)(b)). No Florida cybersecurity rule applies to the cooperative |
| Primary regulation (P03) | RUS electric system operations and maintenance rule, **7 CFR Part 1730, Subpart B** (1730.20 to 1730.29): operations, inspections, borrower analysis, the system security **Vulnerability and Risk Assessment (VRA)** (1730.27), and the **Emergency Restoration Plan (ERP)** (1730.28). Secondary: Form **DOE-417** electric emergency incident reporting (mandatory under Federal Energy Administration Act of 1974 sec. 13(b), Pub. L. 93-275; OMB 1901-0288) |
| Not in scope | **NERC CIP (N22-R01) and NERC EOP-004:** not registered (see above). **TSA pipeline directives (N22-R02):** no pipelines. **NRC 10 CFR 73.54 (N22-R03):** no reactors. **SDWA section 1433 (N22-R04):** the cooperative serves the county water plant but does not own or operate a water system. **SEC disclosure rules:** not an issuer. **Payment cards:** members pay by card through the processor's hosted page and IVR; no card data is stored or entered in cooperative systems; PCI DSS duties are noted, not assessed |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: breach notification (Fla. Stat. 501.171, whose "covered entity" definition names cooperatives). Member records hold Social Security numbers (membership applications, used for deposit decisions), bank account numbers for automatic payment, and the medical-needs list (information about a member's physical condition, 501.171(1)(g)1.a.(IV)) |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board of Trustees (7 member-elected volunteers) | Approves the ERP (7 CFR 1730.28(d)), policies, and the security budget; accepts High risks; discusses RUS reviews with management (1730.24) |
| General Manager | Chief executive (the "Manager" in 7 CFR 1730). Signs the ERP and the VRA and ERP certification letters to RUS (1730.26(b), 1730.28(d)). **System owner** of the SSP system. Accepts Moderate risks. Decision maker in incidents (money, ransom, outside notices). In post since 2024-01 |
| Office and Finance Manager | **Security Coordinator** for the cooperative (designated in writing by the General Manager on 2026-08-31; covers IT and the administrative side of OT). Also accounting, payroll, HR, and vendor files. Grants and removes accounts in the business suite, email, and AMI; MSP contact; breach notice logistics. Overlap: also releases vendor payments, compensated by the General Manager's callback approval of any bank change |
| Member Services Representative | Billing, payments, new service, office-hours outage calls; enters AMI remote connect and disconnect requests |
| Line Superintendent | **Operations and OT lead.** SCADA administrator, recloser and RTU settings, Substation 1, the ERP coordinator, and operational incident commander for outages and OT incidents |
| Journeyman Lineworkers (2) | On-call rotation; respond to SCADA alarms; operate reclosers remotely from truck tablets after hours |
| Meter and Service Technician | AMI meters and collectors, load-control switches, field checks of remote disconnects |
| External parties | G&T (wholesale supplier; its 24x7 control center monitors the delivery point); managed service provider (**MSP**: office IT); hosted SCADA vendor; AMI vendor; utility business suite vendor (CIS, billing, accounting, mapping, outage management); after-hours call center; card payment processor; cellular carrier; cyber insurer and its panel; RUS General Field Representative; independent assessor (P07) |

## 3. Systems
| ID | System | Hosting | Member personal information? | Notes |
|---|---|---|---|---|
| SYS-01 | Hosted distribution SCADA service: master station, web HMI, historian, alarm texts | Vendor SaaS | No | Monitors and controls the 3 feeder reclosers, the regulators, and 6 line reclosers. One shared operator login used by the 4 field staff and one administrator account (Line Superintendent); vendor support staff hold standing administrator access. MFA available but not enabled |
| SYS-02 | Substation and field control devices | Substation 1 and 6 line recloser sites | No | Substation RTU, 3 feeder recloser controls, 3 regulator controls, and a cellular gateway with a VPN tunnel to the SCADA vendor over a private cellular network. The 6 line reclosers each have their own cellular modem on a public-IP data plan |
| SYS-03 | AMI head-end, meter data management, and load management | Vendor SaaS | Yes (interval usage data, linked to account numbers) | About 820 meters, 2 collectors (Substation 1 and headquarters), 120 meters with a remote disconnect switch, 310 water-heater load-control switches (voluntary program). Outage events feed the outage management module. A vendor peak-forecasting add-on has been on trial since 2026-06-01 (P10) |
| SYS-04 | Utility business suite: CIS, billing, accounting and payroll, mapping, outage management, member portal, IVR | Vendor SaaS | Yes (names, addresses, phone numbers, SSNs, bank account numbers, medical-needs list) | MFA enforced. Vendor SOC 2 Type 2 report on file. Card payments go to the processor's hosted page |
| SYS-05 | Productivity suite (email, calendar, shared drive) | SaaS | Yes (incidental, plus scanned membership applications) | MFA enforced |
| SYS-06 | Office network and endpoints | On-premises, MSP-managed (partly) | Cached | Small-business firewall, staff and guest Wi-Fi, 5 office computers (General Manager laptop, Office and Finance Manager desktop, Member Services desktop, Line Superintendent laptop, Meter and Service Technician laptop), 1 operations workstation in the Line Superintendent's office, 3 rugged tablets in trucks (cellular), 7 company smartphones |
| SYS-07 | Cloud backup vault | Public cloud object storage (IaaS) in an account owned by the cooperative and administered by the MSP | Yes | Nightly copy of the shared drive; weekly CIS data export; SCADA point database export and recloser and RTU settings files copied by hand by the Line Superintendent |

**SSP system (P02):** the *Distribution SCADA and Outage Management System (DSOMS)*: SYS-01, SYS-02, SYS-03, the outage management module of SYS-04, the operations endpoints of SYS-06 (operations workstation, Line Superintendent and Meter and Service Technician laptops, 3 truck tablets), and the settings backups in SYS-07.

## 4. Current security posture: early to partial
**In place today:**
- RUS borrower in good standing; the March 2023 RUS operations and maintenance review was completed, and its corrective action plan (right-of-way clearing) was closed in 2024
- A written ERP (Board-approved 2021-05-20) exercised each May in the G&T's hurricane tabletop; activated for a hurricane in October 2024
- An initial VRA (2005) covering physical security of the substation and headquarters
- MSP patching, antivirus, and firewall management for the 5 office computers
- MFA on email and the utility business suite
- The business suite vendor's SOC 2 Type 2 report on file
- Substation 1 fenced and locked; RTU and recloser control cabinets locked
- Substation SCADA traffic carried over a private cellular network with a VPN to the SCADA vendor
- Card payments only through the processor's hosted page and IVR
- Cyber insurance with a 24x7 breach hotline and panel vendors
- Standby generator at headquarters

**Missing:**
1. The VRA dates from 2005 and covers physical security only. It was never updated for the AMI (2019), the hosted SCADA (2021), the load-control program (2022), or the cellular line reclosers (2023).
2. The ERP has no business continuity section for computer and business systems (1730.28(c)(4)), its contact list is out of date (no MSP, SCADA vendor, AMI vendor, or insurer; two former employees listed), the current General Manager has not signed it, and there is one paper copy, at the office.
3. No incident response plan. Nobody knew about the DOE-417 duty, and there is no agreement with the G&T on who files.
4. The SCADA web HMI uses one shared operator login for the 4 field staff, unchanged from 2023 until 2026-07-24, including after a lineworker left in May 2025. No MFA on SCADA. SCADA vendor support has standing administrator access to SCADA and the substation gateway.
5. Recloser controls and line recloser modems still use vendor default or installer-set passwords. There is no OT inventory with firmware versions, and no firmware has been updated since installation.
6. AMI remote disconnect and load-control commands can be sent by any of 4 users with no second approval and no limit on how many meters one command reaches. No MFA on the AMI head-end.
7. Recloser and RTU settings files are kept on the Line Superintendent's laptop; the cloud copy is made by hand. No backup has ever been restore-tested. The backup vault's administrator login has no MFA, and backups are not immutable.
8. The operations workstation and the 3 truck tablets are not under MSP management (no patching or antivirus reporting). The operations workstation signs in to Windows and to SCADA automatically.
9. No security awareness training or phishing exercises. In 2025 an email posing as the G&T asked to change the bank account for the power bill; the General Manager caught it by calling the G&T, but no callback rule is written down.
10. MSP, SCADA vendor, and AMI vendor contracts have no security terms (incident notice, remote access rules). The AMI vendor's SOC 2 report has never been requested.
11. About 2,400 scanned membership applications (current and former members since 2009), with Social Security numbers, sit in the shared drive.
12. No written account termination process.
13. The AMI vendor's peak-forecasting add-on was switched on for a trial using member interval data without a review of the vendor's data-use terms.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 SSP | Distribution SCADA and Outage Management System (DSOMS). The registry default system ("Distribution SCADA and outage management system") fits, scaled to a vendor-hosted SCADA service and the outage module of the business suite |
| P03 regulation | **Changed from the registry default.** The registry names NERC CIP, but the cooperative is not NERC-registered, so no CIP standard applies (see section 1). P03 analyzes the binding rule that does reach it through its RUS loan documents, 7 CFR Part 1730 Subpart B, requirement by requirement with documentary evidence, plus applicability rows for the four registry IDs (N22-R01 to N22-R04) and the DOE-417 reporting duty. OT controls that no binding rule covers are benchmarked against NIST CSF 2.0 with SP 800-82 Rev. 3 in P02 and P07 |
| P08 incident | Intrusion into distribution control systems (OT), the registry default, scaled: an attacker signs in to the hosted SCADA web HMI with the shared operator password and opens the 3 feeder reclosers at night, dropping every member. The MSP, the SCADA vendor, the G&T, and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Availability. The cooperative is not a service organization. The checklist answers the G&T's first member cybersecurity questionnaire (received 2026-06-15, due 2026-10-30); also a review of the hosted SCADA vendor's SOC 2 Type 2 report |
| P10 AI | **Adapted from the registry default.** The cooperative does not build models; the G&T forecasts system load for wholesale planning. The cooperative's own use is the AMI vendor's machine-learning peak-forecasting add-on, used to predict the G&T's monthly coincident peak hour and trigger member peak alerts and water-heater load control (AI-001). Also inventoried: AMI tamper and theft analytics (AI-002) and public generative AI chatbots (AI-003) |
| Cloud | SaaS plus one cloud workload: the cloud backup vault (SYS-07, IaaS object storage administered by the MSP). Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | VRA update interviews, risk assessment, and gap analysis with the MSP (Substation 1 and recloser site walkthrough 2026-07-23) |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent consultant (substation and field testing 2026-08-11) |
| 2026-08-31 | Deliverables approved by the General Manager |
| 2026-09-17 | Board of Trustees approves the policies (P06), the High-risk treatment plans, and the 2026-2027 security budget |
| 2027-03 | Planned RUS operations and maintenance review (borrower analysis due within the 90 days before it, 1730.22(b)(1)) |

## 7. Facts added while building the deliverables
| Topic | Added fact | Used in |
|---|---|---|
| Shared SCADA password | Changed on 2026-07-24, the day after the walkthrough found it unchanged since 2023. The SCADA vendor's login history (90 days kept) showed no sign-ins from unknown locations | P01, P03, P07 |
| Line recloser modem | P07 testing on 2026-08-11 found that the web management page of the modem at line recloser LR-4 answered from the internet and accepted the installer's default password. The Line Superintendent changed the passwords on all 6 modems and the MSP closed the management ports by carrier setting on 2026-08-12. Moving the 6 modems to the private cellular network is planned | P01, P04, P07 |
| G&T coincident peak | The G&T bills a monthly demand charge on the cooperative's load at the G&T's monthly coincident peak hour, about $18 per kW-month. A well-timed load-control event (310 switches, about 0.35 MW) saves about $6,300 in a month | P05, P10 |
| After-hours calls | A contracted after-hours call center answers outage calls and enters tickets in the outage module; it holds a named account with MFA | P02, P05 |
| Cellular carrier | One carrier serves the substation gateway, the line recloser modems, both AMI collectors' backhaul, and the truck tablets | P01, P05 |
| Cyber insurance | Policy held through a cooperative insurance program; 24x7 hotline; panel breach counsel and forensics, including an OT-capable firm; prompt notice required | P08 |
| BEC attempt | October 2025: an email posing as the G&T's accounting office asked to change the bank account for the monthly power bill. The General Manager called the G&T at its known number and the change was refused | P01, P06 |
| MSP contract | Covers office computers, firewall, Wi-Fi, email administration, and the backup vault, with a 4-business-hour response time. No OT devices and no recovery time commitment | P02, P04, P05 |
| Assessor | The P07 assessor is an independent consultant with OT experience, not involved in the risk assessment or in operating any control | P07 |
| Settings backups | The Line Superintendent last copied recloser and RTU settings to the vault in February 2026 | P05, P07 |
| ERP exercise | 2026-05-14: G&T hurricane tabletop (sign-in sheet kept). After the October 2024 activation, nobody recorded the check of emergency contacts that 1730.20 requires for an actual event to count as the annual exercise | P03 |
| Regulatory driver IDs | None of the vertical registry IDs (N22-R01 to N22-R04) applies (P03 G-046 to G-050). The `regulatory_driver` columns therefore cite the binding rules directly: 7 CFR 1730 sections, DOE-417 criteria, and Fla. Stat. 501.171 subsections, plus the voluntary benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3) | P01, P02, P04, P06 |
| Policy adoption | The General Manager approved POL-02 to POL-04 on 2026-08-31; the Board of Trustees adopted them on 2026-09-17; effective 2026-10-01 | P02, P06 |
| Security budget | 2026-2027 security budget approved by the Board on 2026-09-17: about $9,400 one-time and $6,900 a year | P01, P03 |
| Field device passwords | P07 testing on 2026-08-11 also found that recloser controls at Substation 1 and LR-2 accept the vendor default password at the local port; the shared SCADA password had been passed among field staff by text message | P01, P07 |
| Operations workstation | P07 testing found it missing 4 months of operating system updates; one truck tablet was 2 versions behind | P07 |
| ERP copy | The single paper ERP is kept in a locked cabinet in the General Manager's office | P03, P07 |
| SCADA vendor SOC 2 report | Type 2, unqualified, 12 months ending 2026-06-30; received 2026-08-06; reviewed 2026-08-20. One exception (late removal of vendor support access to one customer VPN endpoint); field devices out of scope | P02, P09 |
| Incident readiness dates | DOE-417 filing arrangement with the G&T and the Balancing Authority due 2026-10-31; first tabletop of the P08 runbook with the MSP and SCADA vendor on 2026-11-18 | P08, P09 |
| Peak-forecast trial results | June to August 2026: the G&T's coincident peak hour fell inside a called 4-hour event window in all 3 months; in August the add-on placed the peak 1 hour early on 2 of 6 flagged days. No medical-needs member is enrolled in load control | P01, P10 |
| G&T questionnaire | Based on the Trust Services Criteria for security and availability; the G&T's instructions accept a member self-assessment with a remediation plan instead of an audit report | P09 |

# Intake Report: Cris Santos Company | Communications | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (regional broadband and wired telecommunications carrier, three Florida counties) |
| Intake window | 2026-07-06 to 2026-07-17 |
| Collected by | IT Manager (security and compliance lead), with the Regulatory Affairs Manager |
| Approved | COO, 2026-09-04 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-20. It covers the organization, the systems that hold CPNI, call detail and subscriber information or run the network, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests, walkthroughs) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-008 | Identity provider; HR system; IT ticketing; BSS admin console; cloud console; TACACS+ server | 2026-06-30 to 2026-07-09 |
| Devices and network | EV-009 to EV-018 | EDR and device management consoles; network documentation; OSS; scanning vendor portal; patch tools; syslog and NOC tools; VPN gateway | 2026-06-30 to 2026-07-09 |
| Cloud and backups | EV-019 to EV-022 | Cloud backup service; configuration backup server; cloud console; API gateway | 2026-06-30 to 2026-07-09 |
| Customer authentication and CPNI | EV-023 to EV-033 | Portal configuration; BSS; chatbot admin console; care knowledge base; marketing files; FCC ECFS; regulatory files; contracts; mediation | 2026-02-26 to 2026-07-14 |
| People and training | EV-034 to EV-036 | Learning management system; HR files; contracts | 2026-06-30 to 2026-07-10 |
| CALEA | EV-037, EV-038 | Regulatory files; FCC filing record; restricted room records | 2026-07-07 to 2026-07-09 |
| Outage reporting and resilience | EV-039 to EV-042 | NOC procedures; NORS and DIRS records; NOC file share; facilities logs; contracts | 2026-07-08 to 2026-07-10 |
| Facilities and disposal | EV-043, EV-044 | Badge access and alarm system; destruction certificates | 2026-06-30 to 2026-07-07 |
| Suppliers and contracts | EV-045 to EV-050 | Accounting system; vendor files; vendor and provider portals; contracts folder | 2026-06-30 to 2026-07-10 |
| Business volume | EV-051, EV-052 | Accounting system; BSS reporting | 2025-12-31 to 2026-06-30 |
| Records and AI tools | EV-053, EV-054 | Finance files; staff survey and identity provider app list | 2026-07-10 to 2026-07-14 |

## 3. Observations by area
**Users and access.** 250 active employee accounts, each with MFA registered; cloud and identity administrators use hardware security keys, and 3 cloud administrators have standing access (EV-001). MFA is required for email, single sign-on applications, the VPN and the cloud console, using push approval without number matching (EV-002). HR recorded 8 terminations and 5 transfers from January to June 2026 (EV-003). The 8 termination tickets show the identity account disabled on the last working day. Termination tickets have no step for shared network device passwords, and transfer tickets have no BSS role change step (EV-004). 14 BSS roles carry the bulk export right, and 64 BSS accounts belong to overflow call center agents (EV-005). The BSS audit report records every flag change and call detail view for the 10 sampled accounts, with no record of review (EV-006). The mediation service account can read, write and delete across the CDR archive (EV-007). TACACS+ with MFA covers the core routers only. OLTs, DSLAMs, the 42 cabinet switches and the SBCs use shared local administrator accounts (EV-008).

**Devices and network.** EDR runs on all 285 laptops and desktops and on the cloud VMs. Alerts are emailed to the IT team with no after-hours routing (EV-009). The 105 field tablets are under device management with encryption and remote wipe, and no EDR (EV-010). The network diagram shows no filter between the corporate and management networks, with the lawful-intercept mediation appliance on the management path and one fiber route between CO-1 and CO-2 (EV-011). The OSS inventory has no firmware version or vendor support fields (EV-012). The SBC vendor lists the CO-1 SBC's release as past end of support (EV-013). The 4 quarterly scans cover external addresses only, and 2 edge router findings appear in both 2026 reports (EV-014). Endpoints and cloud VMs are patched monthly; the patch tool holds no network element records (EV-015). Network syslog is kept 30 days, NOC tools watch availability, and there is no SIEM (EV-016). Network changes go through NOC maintenance tickets, with a hardened template for core routers only (EV-017). Vendors reach the voice core through the VPN with named accounts (EV-018).

**Cloud and backups.** Daily snapshots of the OSS, mediation and portal workloads completed from April to June 2026. The vault is in the same account and region as production, immutability is off, and no restore jobs were run (EV-019). Network element configurations are backed up nightly to one server at CO-1, with no second copy listed (EV-020). The CDR archive holds 36 months online with object read logging off, and the chatbot's API client is scoped to all account endpoints (EV-021). Chatbot free-text requests reach the account API with no allow-list of actions (EV-022).

**Customer authentication and CPNI.** The portal and app password reset asks for date of birth and the last 4 digits of the SSN (EV-023). Only a password change sends a notice; address-of-record and security answer changes send none (EV-024). The chatbot pilot, live since 2026-04-06, has quick help mode on, verifying users with account number and service ZIP code, and its API carries no CPNI approval flag (EV-025). By phone, call detail is released only with the account password or by sending it to the address or number of record; payment office clerks check photo ID (EV-026). Every BSS account carries an approval flag, and the opt-out workflow waits 33 days after mailing; the data warehouse carries no flag (EV-027). The last biennial opt-out mailing on record is 2023 (EV-028). Approval emails were found for 4 of 6 CPNI campaigns, and there is no campaign register (EV-029). The CY2025 CPNI certification was filed on 2026-02-26; its statement uses template text and says the online password reset complies (EV-030). The CPNI manual is dated 2019. The request for a CPNI breach procedure, an incident response plan, a breach register, an IT recovery plan and a tabletop record returned none (EV-031). The 40 enterprise and government contracts carry CPNI terms and named contacts (EV-032). Toll fraud reports are built from mediation CDRs (EV-033).

**People and training.** Training records show the 2019 CPNI module at hire for in-house care agents, annual awareness for office staff only, and no records for overflow vendor agents (EV-034). The handbook's discipline section does not mention CPNI or security (EV-035). The overflow vendor contract has confidentiality terms and no CPNI training, departure reporting or incident notice terms (EV-036).

**CALEA.** The SSI policies were filed in 2014 and not since. The appendix names the former senior officer and a disconnected pager number, and a 2025-05-12 memo names the Vice President of Network Operations (EV-037). Four activations in 2025 and 2026 each had a TTP-validated order and one of 3 named employees, and the TTP delivery test is dated 2025-11 (EV-038).

**Outage reporting and resilience.** The NOC procedure has a wireline worksheet and no interconnected VoIP thresholds. Two NORS reports were filed in 2025 after storm-related fiber cuts, and DIRS reports during the 2024 activation (EV-039). The PSAP contact list was last confirmed in 2024 (EV-040). Generators at both central offices hold 72 hours of fuel, and the storm plan and restoration runbooks cover the network (EV-041). Transit contracts provide DDoS scrubbing on request, and the SS7 hub and TTP contracts have no interconnection security terms (EV-042).

**Facilities and disposal.** Badge readers, cameras and alarms protect CO-1 and CO-2, the lawful-intercept room has its own badge group of 3, and cabinet door alarms report to the NOC (EV-043). Drives and retired network elements are destroyed by a certified vendor (EV-044).

**Suppliers and contracts.** Payments go to 24 suppliers with system, data or network access (EV-045). Only the BSS vendor's SOC 2 report is reviewed each year; no review is on file for the chatbot, CCaaS, overflow call center, TTP or SS7 hub (EV-046). The BSS vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31, with a stated RTO of 4 hours and RPO of 1 hour (EV-047). Cloud and identity provider reports and shared responsibility documents are on file (EV-048). The CCaaS and chatbot contracts have no CPNI or 24-hour incident notice terms (EV-049). A cyber insurance policy provides a breach hotline and response panel (EV-050).

**Business volume.** FY2025 receipts were $92.4 million, about $253,000 per day (EV-051). The BSS shows about 64,000 accounts, 61,000 broadband subscribers and 23,400 voice lines, with no wireless or video service (EV-052).

**Records and AI tools.** CDRs are kept 36 months, and SSN4 and date of birth for the life of the account (EV-053). Customer operations runs the chatbot pilot, and staff report using public generative AI services to draft emails, scripts and documents (EV-054).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public generative AI services, and what they enter | Department heads | 2026-07-14 | Not established at intake; P10 treats it as unknown |
| Complaint log behind the complaint summary in the CY2025 CPNI certification | Regulatory Affairs Manager | 2026-07-07 | None provided; taken up in the P03 COO interview (EV-057) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Receipts and subscriber counts (EV-051, EV-052), backup records (EV-019, EV-020), NOC and PSAP records (EV-039, EV-040), BSS vendor recovery objectives (EV-047), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-027 and EV-043 |
| P04 Cloud mapping | Cloud and SaaS components (EV-007, EV-019, EV-021, EV-022) and provider assurance (EV-047, EV-048) |
| P01 Risk register | Likelihood inputs from configuration exports, backup, scan and patch records, and the CPNI and CALEA records |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The 2019 CPNI manual and the document request response (EV-031), and the handbook (EV-035) |
| P07 Control assessment | Populations to sample from (EV-003, EV-004, EV-005, EV-014) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; insurer panel (EV-050) |
| P09 SOC 2 | Vendor assurance on file (EV-046, EV-047) |
| P10 AI governance | AI tools found (EV-025, EV-045, EV-054) |

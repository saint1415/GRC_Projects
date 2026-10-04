# Scenario facts: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (independent crude oil producer and operator of one field) |
| Business | Independent crude oil producer (NAICS 211120 Crude Petroleum Extraction). Operates one mature, sour-crude oil field in the Florida Panhandle, with field SCADA at the well sites, the tank battery, and the saltwater disposal facility |
| Location | Florida, onshore only. **Main office** in a northwest Florida town (owner, office staff). **Field office and yard** on the lease, about 20 miles away (field staff, SCADA host, radio base station). No offshore, Outer Continental Shelf, or waterfront facilities |
| Workforce | 7 employees (see section 2). Well servicing (pulling unit), trucking of crude, and major repairs are contracted |
| Assets operated | 22 wells: 16 producing oil wells on rod pumps (stripper wells, about 3.4 barrels of oil per day each), 2 saltwater disposal (SWD) wells, and 4 shut-in wells. 1 central tank battery with 3 oil tanks, a heater-treater, and a truck loading point. 1 SWD facility (2 injection pumps) next to the tank battery |
| Production | About 55 barrels of oil per day gross operated, plus about 1,400 barrels of produced water per day that is injected into the 2 SWD wells. The small volume of associated gas is used as lease fuel in the heater-treater; there is no gas sale and no gas line leaving the lease |
| Revenue | About $1.1 million a year (fictional), about $3,000 per day net to the company's interest |
| Size status | SBA-small. NAICS 211120 uses an employee-based standard of 1,250 employees (13 CFR 121.201); 7 employees is far below it |
| How product leaves the lease | Crude is sold at the lease tank battery and hauled away in the purchaser's tank trucks. The company owns only production facilities and flow lines, which PHMSA excludes from 49 CFR Part 195 (195.1(b)(8) and (b)(9)(i)). It operates no gas gathering line (49 CFR 192.1(b)(4); 192.8(a)(1)) |
| Owners and partners | Cris Santos holds the company. The company holds an 80% working interest and operates for 2 non-operating working interest owners (joint interest billing). It pays about 140 royalty owners monthly (about 90 live in Florida, the rest in other states) |
| Sensitive data | Royalty owner records (names, Social Security or taxpayer numbers, bank account numbers for direct deposit); employee records (Social Security numbers, driver license numbers, health plan IDs); licensed 3D seismic data (the license limits access to named users) and the company's reservoir interpretations (trade secret); well control and safety data (H2S monitoring, shutdown settings, controller programs) |
| Not in scope | Offshore/OCS and MTSA facilities (none). TSA-designated pipelines (none). EAR-controlled technology (none identified; the company buys commercial well equipment). SSI under 49 CFR Part 1520 (none held). Federal contracts (none). Payment cards (not accepted). SEC reporting (private company) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: the Florida Information Protection Act, Fla. Stat. 501.171 (data security, breach notice, third-party agents). State oil and gas program requirements (permits, production and injection reports) are operational, not cybersecurity rules, and are not analyzed |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Owner (Managing Member) | Petroleum engineer; runs the company. Accepts Moderate risk; approves treatment plans for High risks, policies, and spending. Owner of the predictive maintenance pilot (P10) and of the reservoir and seismic data |
| Office Manager | **Security Coordinator** (designated in writing 2026-08-31). Runs HR, payables, vendor contracts, and insurance; directs the MSP; keeps the risk register and the incident log |
| Production Accountant | Run tickets, state production reports, royalty distribution, joint interest billing; production accounting SaaS administrator |
| Field Superintendent | Business owner of field operations and the SCADA system; OT lead in practice; decides manual operations and shut-ins; agrees to any risk acceptance that affects field safety |
| Lease Operators (2) | Daily well routes, tank gauging, run tickets, after-hours alarm on-call rotation |
| Field Technician (electrical and instrumentation) | Maintains pump-off controllers, PLCs, radios, and the SCADA host; holds the controller programming software on the engineering laptop |
| Managed service provider (MSP) | Office IT: laptops and desktops, email suite administration, main-office firewall, cloud backup. Not contracted for the SCADA host or the field office network |
| SCADA integrator (contractor) | Regional automation firm that installed the SCADA system in 2019; remote support of the SCADA host and controller programs |

**Role overlap.** The Office Manager both runs and checks the business IT controls, and the Field Technician both operates and changes the SCADA system. The compensating checks are the MSP's monthly report, the Owner's monthly review, and an independent assessor once a year (P07).

## 3. Systems

| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Field SCADA host: one PC running the SCADA vendor's software (radio polling master, HMI, alarm engine, local historian) | On-premises, field office | Yes (process data, controller settings) | Runs a desktop operating system version past end of vendor support; signature antivirus only. A USB backup drive stays attached to it |
| SYS-02 | Field controllers and communications: 16 pump-off controllers (one per producing well), 1 tank battery PLC, 1 SWD facility PLC; licensed 900 MHz radio network (base radio at the field office, 15 remote radios); 3 cellular modems at remote well sites | Field sites | Yes (control logic) | Safety shutdowns (H2S detection, tank high-level, SWD pump high-pressure) are hardwired and do not depend on SCADA |
| SYS-03 | Production accounting and revenue distribution | Vendor SaaS (SOC 2 Type 2) | Yes (royalty owner PI, volumes, revenue) | Run tickets, allocations, state production reports, royalty payments, joint interest billing. MFA enforced |
| SYS-04 | Productivity suite (email, files, chat) | SaaS | Yes (royalty exports, licensed seismic data, reservoir files) | MSP-administered; MFA enforced. The shared drive holds a "Geology" folder open to all staff (see gaps) |
| SYS-05 | Endpoints: 7 computers and 5 company smartphones | Main office, field office, mobile | Yes (cached) | Main office: 3 laptops (Owner, Office Manager, Production Accountant) and 1 desktop. Field office: Field Superintendent laptop, shared field desktop, Field Technician's engineering laptop. MSP manages all except the engineering laptop. Smartphones receive SCADA alarms |
| SYS-06 | Networks: main-office firewall and Wi-Fi (MSP-managed); field office internet router and Wi-Fi (set up by the SCADA integrator in 2019) | On-premises | In transit | The field office network is flat: SCADA host, field PCs, and Wi-Fi share one network |
| SYS-07 | Cloud backup service | SaaS, operated by the MSP | Yes | Nightly backup of the 4 main-office computers and the shared drive; 30 days of versions. Does not cover the SCADA host or field office computers |
| SYS-08 | SCADA alarm callout and mobile viewer | SCADA vendor's cloud service (SaaS) | Yes (process data) | A connector on SYS-01 pushes alarms and well status outbound; on-call phones get calls and texts; staff view wells on phones. Individual accounts; MFA available but not enabled |
| SYS-09 | SCADA integrator remote access | Third-party remote access tool installed on SYS-01 | Access path | Always on, one shared integrator account, no MFA, no session log |
| SYS-10 | Business online banking | Bank portal (SaaS) | Yes (company and owner bank data) | ACH royalty and payables files; the bank requires a second approver (the Owner) for every ACH batch |

**SSP system (P02):** the *Field SCADA and Production Accounting System (FSPA)*: SYS-01 to SYS-09, meaning the company's field control system, its production accounting and office tools, and the vendor services and access paths that connect to them. SYS-10 is an external service outside the boundary.

**Data flow in one line:** field controllers (SYS-02) report by radio and cellular to the SCADA host (SYS-01); the SCADA host pushes alarms to the vendor's cloud service (SYS-08), which calls the on-call phone; lease operators write paper run tickets and photograph them; the Production Accountant enters run tickets and monthly volumes into production accounting (SYS-03), which produces the royalty ACH file that the Owner approves in the bank portal (SYS-10).

## 4. Current security posture: early to partial

**In place today:**
- MFA on the productivity suite, production accounting, and the bank portal
- Bank dual approval: every ACH batch needs a second approver (the Owner)
- MSP patching, antivirus, and firewall at the main office; laptops encrypted
- Nightly cloud backup of main-office computers and the shared drive
- Hardwired safety shutdowns independent of SCADA (H2S detection, tank high-level, SWD pump high-pressure)
- Fenced, locked tank battery and SWD facility; locked controller cabinets at well sites
- Licensed (private) radio network for most field sites
- A written emergency response plan for spills, fire, H2S releases, and hurricanes, with a manual-operations and shut-in procedure (not cyber)
- Cyber insurance with ransomware coverage (the application stated MFA on remote access and offline backups)
- Lease operators visit every well daily on a route, so SCADA loss is noticed and covered quickly

**Missing:**
1. No inventory of field controllers, radios, and modems, with models and firmware; no drawing of the field office network.
2. The field office network is flat. The SCADA host, the field PCs, and the Wi-Fi share one network behind the internet router, with no firewall between business IT and SCADA. The shared field desktop has a saved remote desktop shortcut to the SCADA host.
3. The SCADA integrator's remote access is an always-on tool on the SCADA host, with one shared account, no MFA, and no session record.
4. The SCADA host runs an operating system version past end of vendor support, has not been patched since 2024, and has signature antivirus only.
5. SCADA host backups are weekly copies to a USB drive that stays attached to the host. Controller programs exist only on the Field Technician's engineering laptop. No restore has ever been tested.
6. One shared "operator" login on the SCADA HMI for all field staff; the password has not changed since 2019. MFA is not enabled on the SCADA mobile viewer.
7. No incident response plan; the emergency response plan does not cover cyber events; no tabletop exercise.
8. No security terms in the SCADA integrator, SCADA vendor, or production accounting contracts; vendor security never reviewed.
9. Access removal is informal. A Lease Operator who left in March 2026 still had an active SCADA mobile viewer account, and the HMI password, gate code, and field Wi-Fi password were never changed.
10. No security training beyond occasional MSP tip emails; field staff never trained; no phishing exercises.
11. Royalty owner exports are emailed and saved to laptops; owner bank detail changes are accepted by email without a call-back.
12. Licensed seismic data and reservoir interpretations sit in a shared folder open to all 7 staff, although the seismic license limits access to named users.
13. The predictive maintenance add-on (P10) started in May 2026 without a risk review or contract terms.
14. No log review anywhere; the SCADA host event log is not kept beyond its default size.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P03 benchmark | **NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary benchmark).** No binding federal sector cyber rule applies: USCG N21-R01 does not (onshore, no facility required to have a security plan, 33 CFR 101.605); TSA N21-R02 does not (no TSA-notified pipeline); CIRCIA N21-R03 is proposed only, and as proposed the company would be outside it (SBA-small, no sector criterion met). Secondary binding rule: Fla. Stat. 501.171 |
| Regulatory driver labels | `N21-BM (...)` means the P03 voluntary benchmark (NIST CSF 2.0 with SP 800-82 Rev. 3), with the SP 800-82 Rev. 3 section in parentheses. It is a scenario label, not a row in `requirements.csv`. `N21-R03 (proposed)` marks items tracked for CIRCIA but not required. `Fla. Stat. 501.171(x)` marks binding state duties |
| P08 incident | Ransomware that starts with a phishing email on a field office PC and spreads across the flat field office network to the SCADA host (registry default kept; it fits the flat network at this size) |
| P09 SOC 2 | Security plus Confidentiality, as a self-assessment to answer the larger non-operating partner's security questionnaire and the seismic data license renewal; plus a review of the production accounting vendor's SOC 2 Type 2 report. The company is not a service organization |
| P10 AI | Predictive maintenance for well equipment (registry default), adapted to this size: a **vendor add-on** to the SCADA cloud service that analyzes pump-off controller data to predict rod pump failures, piloted by the Owner on 8 wells since May 2026. A micro producer buys this capability rather than building a model. Second inventory entry: staff use of public generative AI |
| Cloud | SaaS plus one cloud workload: the MSP-operated cloud backup (SYS-07). Vendor-agnostic |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | Risk analysis and gap analysis by the Office Manager and the Field Superintendent, with the MSP lead technician (field walkthrough 2026-07-22) |
| 2026-08-10 to 2026-08-12 | Control assessment by an independent consultant with OT experience (field office testing 2026-08-11) |
| 2026-08-31 | Deliverables approved by the Owner, with field-operations items agreed by the Field Superintendent |

## 7. Facts added while building the deliverables

| Topic | Added fact | Used in |
|---|---|---|
| Former Lease Operator | Left on 2026-03-13. His SCADA mobile viewer account was found active on 2026-07-22 and disabled that day. The viewer log showed no sign-ins after his last day | P01, P03, P07 |
| Remote desktop exposure | P07 testing on 2026-08-11 found a remote desktop port on the field office router forwarded to the SCADA host and reachable from the internet. The SCADA integrator had set it up in 2022 as a fallback. The Field Superintendent removed the rule at 15:40 the same day; a rescan on 2026-08-12 confirmed it closed | P01, P02, P07 |
| AI write-back | During the P10 review the Owner found that the vendor had enabled "auto-optimize idle time" on 2 of the 8 pilot wells, which changed pump-off idle-time setpoints 11 times in July within vendor-set limits. Write-back was turned off on 2026-08-26 | P01, P04, P10 |
| MSP contract | Covers help desk, patching, antivirus, main-office firewall, suite administration, and cloud backup, with a 4-business-hour response time and no recovery time commitment. Does not cover the SCADA host or field office network | P02, P04, P05 |
| SCADA host backup | The Field Technician copies a SCADA software backup to the attached USB drive each Friday. The SCADA integrator estimates 2 to 3 days to rebuild the host from installation media without a good backup | P01, P05, P08 |
| Field office power | The SCADA host and radio base have a 30-minute UPS; there is no generator at the field office | P01, P05 |
| Partner questionnaire | The larger non-operating partner sent a security questionnaire in June 2026 before a joint drilling program; the response is due 2026-09-30. The seismic data license renews 2026-12-31 and asks for a statement of access controls | P09 |
| Cyber insurance | The policy has a 24x7 breach hotline and panel vendors (breach counsel, forensics). It requires prompt notice and use of panel vendors | P08 |
| Assessor | The P07 assessor is an independent consultant with OT experience, not involved in the risk or gap analysis and operating no control | P07 |
| Finances | A cash reserve covers about 60 days of expenses; payroll runs biweekly through an outside payroll service | P01, P05 |

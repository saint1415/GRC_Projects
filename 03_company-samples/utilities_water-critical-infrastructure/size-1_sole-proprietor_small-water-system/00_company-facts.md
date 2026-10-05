# Scenario facts: Cris Santos Company | Water and Wastewater Systems | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a law or regulation, the citation is given. This scenario is independent of the other sizes.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-operator files Schedule C) |
| Business | Privately owned small community water system (NAICS 221310): two groundwater wells, disinfection with sodium hypochlorite, one 50,000-gallon ground storage tank, two high-service pumps, a hydropneumatic pressure tank, and the distribution mains for one rural subdivision. No wastewater service (homes use septic systems) |
| Location | Florida. The well house (wells, treatment, storage, and control panel) is on a fenced lot inside the subdivision. The office is in the owner's home, about 4 miles away |
| Customers | 138 residential connections used by year-round residents. **Population served: 330 persons**, the figure the owner reports to the state drinking water primacy agency. Average day demand is about 45,000 gallons |
| Public water system status | **Community water system**: a public water system that serves at least 15 service connections used by year-round residents (40 CFR 141.2). The owner is the "supplier of water" (40 CFR 141.2) and is responsible for the national primary drinking water regulations in 40 CFR Part 141 |
| Treatment status under the Ground Water Rule | The owner has notified the state that the system provides at least 4-log treatment of viruses before the first customer for both wells, so it does **compliance monitoring under 40 CFR 141.403(b)(3)(i)(B)** (systems serving 3,300 or fewer): a daily grab sample of the residual disinfectant during the hour of peak flow, with follow-up samples every 4 hours if a reading falls below the state-determined level. The state-specified minimum residual is kept in the owner's 4-log notification file |
| Workforce | The owner-operator only (0 employees). The owner holds the state drinking water treatment plant operator license required for this plant. Contracted services are used instead of staff |
| Revenue | About $180,000 a year (fictional), almost all from monthly water charges. SBA-small (standard $41.0 million in average annual receipts for NAICS 221310; 13 CFR 121.201) |
| SDWA section 1433 status | **Not covered.** Section 1433 (42 U.S.C. 300i-2(a)(1) and (b)) applies to community water systems "serving a population of greater than 3,300 persons". At 330 persons the system is outside the risk and resilience assessment (RRA) and emergency response plan (ERP) duties. 300i-2(e) directs EPA to give guidance and technical assistance to systems serving fewer than 3,300 persons, so EPA's small-system tools are used here as a **voluntary** benchmark |
| Not in scope | Wastewater (no POTW). Federal contracts: none. HIPAA: not a covered entity. Payment cards: customers pay through the payment processor's hosted page, so card numbers never touch the owner's systems |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (customer data breach notice and disposal, Fla. Stat. 501.171). State primacy agency rules are referred to generically ("the primacy agency") |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-operator | Every role: owner, licensed operator, security and compliance lead, incident commander, and risk acceptor. Visits the well house every day and takes the compliance grab sample |
| Licensed relief operator (contractor) | Covers the owner's scheduled days off (about 4 days a month) and vacations under a written relief agreement. Takes the daily grab sample on those days. **Signs in to the remote access portal with the owner's login** (no account of its own) |
| Controls integrator (regional panel shop) | Built and programmed the control panel in 2019. Gives remote support through the cloud remote access portal with **its own always-enabled administrator account**. Holds the only known current copy of the PLC program and HMI project. **No security terms in its service agreement** |
| On-call IT technician | Hourly help with the laptop, phone, and home network. No standing access. Signed a written confidentiality agreement on 2026-07-15, before the self-assessment |
| Certified laboratory | Analyzes bacteriological and chemical compliance samples; posts results to its customer portal and reports them to the state |
| Owner's attorney | General business counsel; holds the sealed emergency access envelope once it exists (P05) |

## 3. Systems
| ID | System | Hosting | Holds sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Treatment control panel: one PLC with a local touchscreen HMI, the online chlorine residual analyzer, the well flow meter, hand-off-auto switches for every pump, and a cellular alarm dialer | On premises (well house) | Yes (control logic, setpoints, process data) | Installed 2019 by the controls integrator. The PLC paces the hypochlorite metering pump from the well flow signal. The pump's stroke-length knob caps maximum feed whatever the PLC asks for. PLC and HMI passwords are the integrator's defaults, and the HMI setpoint screens have no login |
| SYS-02 | Cellular router at the well house and the vendor's cloud remote access portal with its phone app | Router on premises; portal is vendor SaaS | Yes (remote control of SYS-01; setpoints; portal audit log) | Lets the owner see HMI screens and change setpoints from the phone or laptop. Accounts: owner (shared with the relief operator) and the integrator. **Password only; MFA available but off.** The portal keeps a 90-day audit log of sign-ins and setpoint changes. The P08 incident path |
| SYS-03 | Utility billing SaaS with customer portal | Vendor SaaS | Yes (customer names, service addresses, account numbers, usage, phone numbers and email addresses; customer portal user names and passwords held by the vendor) | 138 accounts. MFA on for the owner's account. Payments go through the payment processor's hosted page. Also used for automated email and text notices to customers |
| SYS-04 | Email and file storage (business plan of a productivity suite) | SaaS | Yes (monthly operating reports, lab report copies, customer list exports, as-built drawings, the 4-log notification file) | MFA on (text-message code). The provider keeps file version history |
| SYS-05 | Laptop in the home office | Owner device | Yes (cached files, the daily residual spreadsheet, billing exports) | Built-in full-disk encryption on; automatic updates; built-in antivirus. **The owner works in the administrator account every day** |
| SYS-06 | Owner's mobile phone | Personal device used for business | Yes (portal app with a saved password, alarm calls, email, MFA codes) | Passcode on |
| SYS-07 | Home office internet router and Wi-Fi | Owner device | No (traffic only) | Supplied by the internet provider; WPA2 with a unique passphrase |
| SYS-08 | Anomaly alert feature of the remote access portal | Vendor SaaS (machine learning) | Process data only (residual, flows, tank level, pump run times) | Turned on 2026-06-01 as a free trial without any review. The vendor's terms let it use customer data to improve its models. See P10 |

**SSP system (P02):** the *Water System Operations Profile (WSOP)*: SYS-01 to SYS-08, centered on the treatment control panel and its remote access path (SYS-01 and SYS-02).

Paper records: the daily operating log at the well house, laboratory chain-of-custody forms, and customer service applications in a locked file cabinet in the home office.

## 4. Current security posture: early (few formal controls)
**In place today:**
- Every pump can be run by hand at the panel (hand-off-auto switches). The owner visits the well house every day and takes the compliance grab sample with a field test kit, so compliance monitoring does not depend on the PLC or the portal
- The hypochlorite metering pump's stroke-length setting caps maximum feed; the residual analyzer's low and high alarms, low tank level, low pressure, power failure, and the well house door alarm all go to the cellular alarm dialer, which calls the owner and then the relief operator
- Fenced, locked well house with a door alarm
- Written relief operator agreement for scheduled days off
- MFA on email and on the billing SaaS
- Laptop full-disk encryption, automatic updates, and built-in antivirus
- Card payments through the processor's hosted page
- The primacy agency's boil water notice template and after-hours contact number, used after a 2024 hurricane power outage (precautionary boil water notice issued within about 10 hours and certified to the state within 10 days)
- Portable generator with a transfer switch sized for Well 1 and one high-service pump
- Certified laboratory contract

**Missing:**
1. No risk assessment ever performed. The owner assumed no cyber duties applied because the system is below SDWA section 1433's 3,300-person threshold.
2. No written security policy or procedures.
3. The remote access portal uses a password only. MFA is available but off, the password is saved in the phone app, and the relief operator uses the owner's login.
4. The controls integrator's portal account is always enabled, can change setpoints, needs no approval per session, and sends no notice when used. The integrator's agreement has no security terms.
5. The cellular router at the well house still had the default administrator password printed on its label, and remote web administration was on (found in P07 testing on 2026-07-23; remote administration turned off that day).
6. The PLC and HMI use the integrator's default passwords, and the HMI setpoint screens have no login.
7. No offline backup of the PLC program and HMI project. The integrator holds the only known current copy; a 2019 USB stick of unknown version is in the desk drawer.
8. No incident plan or contact list for a cyber event. The hurricane checklist is the only written emergency procedure, and the public notice routine does not treat a cyber-caused loss of disinfection as a trigger or know the Ground Water Rule 4-hour clocks.
9. The customer contact list for notices exists only in the billing SaaS (no offline copy).
10. The portal audit log (sign-ins and setpoint changes) has never been reviewed.
11. The owner uses the laptop's administrator account every day.
12. The owner has had no cybersecurity training.
13. Manual operation and recovery steps are not written down. The relief operator has never run the plant by hand during an alarm.
14. The anomaly alert feature (SYS-08) was turned on without review, and its data-use terms were accepted by click-through.
15. No cyber insurance. Whether the general liability policy covers a cyber event is unconfirmed.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 system | The registry default "Water treatment SCADA" is adapted: at this size there is no SCADA server, only one PLC panel reached through a cloud remote access portal. The SSP covers that panel plus the owner's SaaS stack and devices as one short-form profile |
| P03 regulation | SDWA section 1433 (C-WATER-R01) is tested first and found **not applicable** (330 persons). CIRCIA (C-WATER-R02) is proposed only. The binding analysis covers the 40 CFR Part 141 duties a cyber event would trigger: the public notification rule (Subpart Q), the Ground Water Rule compliance monitoring, treatment technique, and reporting rules (141.403(b)(3), 141.404(c), 141.405), and reporting and records (141.31, 141.33). The 300i-2 assessment elements and CSF 2.0 outcomes (with SP 800-82 Rev. 3) are used as a voluntary benchmark, as EPA's small-system guidance invites. Fla. Stat. 501.171 is covered narrowly for customer data |
| P08 incident | Remote-access compromise of the treatment HMI through the cloud remote access portal: an attacker signs in with the owner's reused password and sets the hypochlorite feed to zero and a well pump to off. The registry default fits this size once "treatment-plant HMI" means the panel HMI reached through the portal |
| P09 SOC 2 | Security criteria only, as the owner's self-check. The company is not a service organization. The remote access portal vendor's SOC 2 Type 2 report is reviewed with the same criteria (`vendor-soc2-review.csv`) |
| P10 AI | The registry default "Water-quality anomaly detection" fits as the portal's anomaly alert feature (SYS-08), a third-party AI tool. A consumer AI chat assistant used to draft customer letters is the second inventory entry |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-24 | Self-assessment by the owner with the on-call IT technician (after the confidentiality agreement): BIA, system profile, risk register, gap analysis |
| 2026-07-22 | Review of the remote access portal vendor's SOC 2 report |
| 2026-07-23 | Tests at the well house, on the portal, and on the laptop and phone (P07) |
| 2026-08-31 | Deliverables adopted by the owner-operator |
| 2026-09-15 | First due date for the High-risk fixes (portal MFA, integrator account, router) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Portal password reuse | The owner's portal password is the same one used for an online shopping account whose provider reported a breach in 2025. This is why P08 starts from a password-reuse sign-in | P01, P08 |
| Integrator account use | The portal audit log for the 90 days before 2026-07-23 shows the integrator signed in 3 times. The owner could match only one of them to a support call | P01, P07 |
| Router finding | During the 2026-07-23 test, the IT technician reached the cellular router's web administration page from the internet side and signed in with the label password. Remote administration was turned off the same day; the default password was left for a firmware update planned with the integrator | P01, P04, P07 |
| PLC program copy | The integrator confirmed on 2026-07-24 that it holds the 2023 program version (changed when the second high-service pump was replaced). The 2019 USB stick predates that change | P01, P05, P07 |
| Portal vendor assurance | The portal vendor provided its SOC 2 Type 2 report (Security category) under a nondisclosure agreement. The owner reviewed it on 2026-07-22 | P02, P09 |
| Customer notice channels | The billing SaaS sends automated emails and texts to the 112 accounts with a phone number or email on file. The other 26 households need posting or hand delivery | P03, P05, P08 |
| AI chat assistant | In 2025 the owner used a free consumer AI chat assistant to draft a rate-change letter and a reminder about the 2024 boil water notice. No customer list was pasted in | P10 |
| Previous relief operator | A previous relief operator covered until 2025 and used the same shared portal login. The password was not changed when that operator left | P07 |
| Router label | The router sits inside the locked panel enclosure, and its default administrator password is printed on its label | P07 |
| Anomaly alert history | In its first 12 weeks (2026-06-01 to 2026-08-23) the feature sent 9 alerts: 6 normal events, 2 real problems already caught on the daily visit (a weak hypochlorite batch and a sticking check valve), and 1 dropped cellular signal | P10 |

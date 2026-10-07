# Scenario facts: Cris Santos Company | Emergency Services | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (a licensed basic life support ambulance service that provides non-emergency transport only) |
| Business | Non-emergency ambulance transport (NAICS 621910 Ambulance Services): scheduled and unscheduled basic life support (BLS) stretcher transports for patients whose condition requires an ambulance. Trips are hospital discharges, transfers between facilities, dialysis runs, and medical appointments. The company does not respond to 911 calls |
| Location | Florida. One leased building with an office, a dispatch desk, a supply room, and a 2-bay garage. Service area: one county of about 250,000 residents and the facilities in the neighboring county |
| Workforce | 7 employees (about 6 full-time equivalents): the owner (managing member and a state-certified paramedic who also works crew shifts), 1 Office Manager, 1 Scheduler-Dispatcher, and 4 EMTs (2 full-time, 2 part-time). The Medical Director is a contracted physician, not an employee |
| Volume | About 3,000 transports a year (about 12 on a weekday, fewer on weekends). About 45% are scheduled repetitive dialysis runs, 35% are hospital discharges and facility transfers, and 20% are appointments |
| Fleet | 2 BLS ambulances. Both are staffed on weekdays from 5:00 a.m. to 7:00 p.m.; one on-call crew covers evenings and weekends |
| Revenue | About $1.1 million a year (fictional). Under the SBA standard of $22.5 million for NAICS 621910 (13 CFR 121.201), so SBA-small |
| Payers | Medicare Part B (about 60% of trips), Florida Medicaid, commercial plans, and facilities that pay for some discharges under transport agreements. Medicaid is federal financial assistance, so Section 1557 of the Affordable Care Act applies (45 CFR Part 92) |
| Licenses and county authority | State EMS license as a basic life support service (Fla. Stat. 401.25; Chapter 64J-1, F.A.C.). Certificate of public convenience and necessity from the home county (Fla. Stat. 401.25(2)(d)), limited to non-emergency and interfacility transport. A contracted Medical Director, as Fla. Stat. 401.265(1) requires |
| Medicare claims | Medicare-enrolled ambulance supplier. With fewer than 10 full-time equivalent employees it is a "small supplier" (42 CFR 424.32(d)(1)(viii)(B)), so Medicare would accept paper claims (424.32(d)(3)(ii)). The company still bills every payer electronically through an outsourced billing company |
| HIPAA status | **Covered entity.** A health care provider that transmits health information electronically in HIPAA standard transactions (45 CFR 160.103). Using a business associate (the billing company and its clearinghouse) to send the claims does not change that (45 CFR 162.923(c)) |
| 911 relationship | None. The county 911 center and county fire-rescue handle emergencies. If a caller describes an emergency, the Scheduler-Dispatcher tells the caller to hang up and dial 911. The company has no CAD-to-CAD link with the county and no access to criminal justice information |
| Not in scope | FBI CJIS Security Policy and 28 CFR 20.21 and Part 23 (no criminal justice information); FCC EAS rules (not an EAS participant); 42 CFR Part 2 (no federally assisted substance use disorder program); group health plan requirements (45 CFR 164.314(b)); payment cards (patients pay through the billing company's hosted payment page) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: EMS records (Fla. Stat. 401.30; Rule 64J-1.014, F.A.C.), call recording (Fla. Stat. 934.03), and breach notification (Fla. Stat. 501.171) |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Owner (managing member) | Accepts risk; approves policies and spending; backup incident lead; works crew shifts when needed |
| Office Manager | HIPAA **Privacy Officer and Security Officer** (combined; designated in writing by the Owner on 2026-07-27). Also handles billing liaison, certification statements, payroll, and HR files |
| Scheduler-Dispatcher | Takes trip requests by phone, fax, and the facility portal; schedules and dispatches crews; carries the on-call phone on weekdays; the only user of the AI intake pilot |
| EMTs (4) | Patient care; electronic patient care reports (ePCR) on tablets; daily vehicle and equipment checks |
| Medical Director (contracted physician) | Clinical oversight, protocols, and quality review (Fla. Stat. 401.265); owns the rules for recognizing callers who need 911 |
| Managed service provider (MSP) | Help desk, patching, antivirus, firewall, Wi-Fi, mobile device management, and backup administration. A business associate (BAA on file) |
| Billing company | Coding, claims, payment posting, denials, and patient statements through its own software and clearinghouse. A business associate (BAA on file) |

## 3. Systems
| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | Ambulance operations platform: computer-aided dispatch (CAD) board and trip scheduling, facility trip-request portal, and electronic patient care reporting (ePCR) with hospital record delivery and state data export | Vendor SaaS | Yes | BAA on file; vendor SOC 2 Type 2 report. MFA is available but **not enabled**. The dispatch board uses one shared "dispatch" login |
| SYS-02 | Productivity suite (email, shared drive, shared fax mailbox) | SaaS | Yes | Business plan; BAA accepted in the admin console in 2024; MFA enforced |
| SYS-03 | Billing company portal (claims status, remittances, denials, reports) | Billing company's SaaS | Yes | BAA on file; MFA enforced by the billing company |
| SYS-04 | Hosted phone system: request lines, call recording, on-call forwarding, and fax-to-email | Vendor SaaS | Yes | **No BAA on file** at the start of the work |
| SYS-05 | Endpoints: 2 office desktops (dispatch desk and Office Manager), 1 owner laptop, 3 rugged ePCR tablets (one per ambulance and a spare), 4 company smartphones (on-call phone, owner phone, and one crew phone per ambulance) | MSP-managed (computers through remote management; tablets and phones through mobile device management) | Yes (cached) | Laptop, tablets, and phones encrypted; **the 2 desktops are not** |
| SYS-06 | Office network: small-business firewall, one Wi-Fi network, one cable internet line | On-premises, MSP-managed | In transit | Staff devices and crew personal phones share one Wi-Fi network |
| SYS-07 | Vehicle equipment: a cellular hotspot in each ambulance and a GPS tracker that reports to a fleet tracking service | In vehicles; fleet tracking is SaaS | Tablet traffic in transit; the tracker holds no PHI | Hotspots set up by the owner in 2022, not managed by the MSP |
| SYS-08 | Cloud backup of the productivity suite (mailboxes and shared drive), nightly, 30 days of versions | SaaS backup, resold and administered by the MSP | Yes | **Never restore-tested**; the console accepts a password alone |
| SYS-09 | AI intake assistant: a SYS-01 feature that transcribes recorded trip-request calls from SYS-04 and pre-fills the trip request with a suggested level of service, a medical necessity checklist, and a "possible emergency, redirect to 911" flag | SYS-01 vendor's cloud AI service | Yes | Pilot since 2026-06-01; data-use terms not reviewed (see P10) |

External systems the company connects to but does not operate: receiving hospitals (they get patient care records through the SYS-01 hospital portal), the state EMS data system (EMSTARS), the billing company's clearinghouse and payers, and facility staff who use the SYS-01 request portal.

**SSP system (P02):** the *Transport Operations Platform (TOP)*: SYS-01, SYS-02, SYS-04, SYS-05, SYS-06, SYS-07, and SYS-08, with their interfaces to SYS-03 and SYS-09.

## 4. Current security posture: early to partial
**In place today:**
- MFA on the productivity suite and the billing company portal
- Unique ePCR logins for each EMT
- BAAs with the operations platform vendor, the billing company, the MSP, and the productivity suite vendor
- Encryption and remote wipe on the laptop, tablets, and phones through mobile device management
- MSP patching, antivirus, and firewall on the office computers
- Background checks, driving record checks, and state EMT and paramedic certification checks at hire
- A HIPAA video at hire
- The operations platform vendor's own backups and replication

**Missing or weak, found in the 2026 assessments:**
1. No documented HIPAA security risk analysis has ever been done. The only prior review is a 2024 questionnaire from a hospital transport agreement.
2. No security policies have been adopted. The employee handbook has one paragraph on patient privacy.
3. MFA is not enabled on the operations platform for anyone, including the two administrator accounts. The dispatch board uses one shared "dispatch" login, on the dispatch desktop and on the on-call phone.
4. No BAA with the hosted phone and fax vendor, which stores call recordings and faxed certification statements.
5. The AI intake assistant was switched on under the platform's feature terms without anyone reviewing data use.
6. Physician certification statements (PCS) arrive by fax, portal upload, and paper. Paper copies sit in a binder, and nothing ensures the 7-year Medicare retention (42 CFR 424.516(f)).
7. No incident response plan and no contingency plan. Dispatchers print the next day's run sheet "most nights", but manual dispatch has never been practiced.
8. The suite backup has never been restore-tested, and its console has no MFA.
9. No review of audit logs, platform access reports, or suite sign-ins.
10. Accounts of departing EMTs stay active. Two former part-time EMTs still had ePCR accounts when the work began.
11. Training happens only at hire. There are no reminders or phishing exercises.
12. One Wi-Fi network for office computers and crew personal phones, with a password unchanged since 2022.
13. No inventory of devices or of where ePHI is stored.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Ransomware from a phishing email encrypts the two office desktops, including the dispatch desk, and the shared drive. The attacker also used the shared dispatch password to sign in to the operations platform and export the trip list. The company loses its dispatch board and runs manual dispatch. This adapts the registry scenario ("computer-aided dispatch outage from ransomware"): at this size the CAD is vendor SaaS that ransomware on office computers cannot encrypt, so the outage comes from losing the dispatch desk and from locking down the compromised login. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | The company is not a SOC 2 service organization. (a) Security plus Availability self-assessment, used to answer the security questionnaire in the regional hospital's transport agreement renewal; (b) review of the operations platform vendor's SOC 2 Type 2 report |
| P10 AI | AI intake assistant for trip requests (SYS-09). This adapts the registry use case ("AI-assisted emergency call triage"): the company takes no 911 calls, but its request line does receive calls that describe emergencies, and the assistant suggests the level of service and flags possible emergencies for redirection to 911 |
| Cloud | SaaS plus one cloud workload: the suite backup (SYS-08). Vendor-agnostic; AWS, Azure, and Google Cloud are named only in an equivalents table |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-27 to 2026-08-07 | BIA, risk analysis, and gap analysis with the MSP |
| 2026-08-17 to 2026-08-19 | Control assessment (independent consultant) |
| 2026-08-26 | Readiness self-assessment and platform vendor SOC 2 report review |
| 2026-08-28 | AI intake assistant assessment |
| 2026-09-04 | Deliverables approved by the Owner |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Patients in the platform | The company has used SYS-01 since 2021. It holds trip and patient care records for about 5,200 unique patients, nearly all Florida residents | P01, P05, P08 |
| Daily revenue | About $3,000 of billed revenue per day; a cash reserve covers about 30 days of expenses | P01, P05 |
| Dialysis runs | About 18 patients ride three times a week to two dialysis centers; the first pickups are at 5:00 a.m. A missed session is a patient safety event | P01, P05, P08 |
| Vendor recovery objectives | The SYS-01 vendor's SOC 2 system description states an RTO of 4 hours and an RPO of 15 minutes | P05, P09 |
| MSP contract | Covers business hours only (7:00 a.m. to 6:00 p.m. weekdays), with a 4-business-hour response time, no after-hours line, and no recovery time commitment | P01, P05, P07, P08 |
| Cyber insurance | The company holds a cyber liability policy (required by the hospital transport agreement since 2024) with a 24x7 breach hotline and panel vendors. The policy requires prompt notice and use of panel vendors | P08 |
| Former EMT accounts | Two former part-time EMTs (departed 2026-03 and 2026-05) still had active ePCR accounts on 2026-07-29. The Office Manager disabled both that day. The platform access report showed no sign-ins after their last shifts | P01, P03, P07 |
| Hosted phone BAA | The Owner signed the hosted phone and fax vendor's BAA on 2026-08-21, after the gap analysis found the gap | P01, P03, P07 |
| Remote access tool | P07 testing on 2026-08-18 found a free remote desktop tool on the dispatch desktop, installed in 2025 by a former scheduler for after-hours access, outside MSP management and with a reused password. The MSP removed it on 2026-08-19 | P01, P04, P07 |
| PCS sample | A sample of 20 dialysis trips from June 2026 found 3 with no PCS on file dated within the 60 days before the trip (42 CFR 410.40(e)(2)) | P01, P03 |
| Hospital questionnaire | The regional hospital sent its transport vendor security questionnaire in July 2026; the response is due 2026-09-30 | P09 |
| Assessor | The P07 assessor is an independent HIPAA security consultant with EMS experience who did not take part in the risk or gap analysis and operates no control | P07 |
| Call recording | All request lines are recorded. Until 2026-08-25 there was no recorded announcement. The company does not staff a public safety answering point, so it relies on all-party consent (Fla. Stat. 934.03(2)(d)) through a recorded announcement added 2026-08-25; counsel to confirm | P01, P10 |
| AI intake pilot | Since 2026-06-01 the Scheduler-Dispatcher sees the assistant's suggestions on screen (advisory use, not shadow mode). About 1,150 recorded request calls were processed by 2026-08-14 | P01, P10 |
| Office security | Keyed office and garage entry with an alarm; keys held by the Owner, the Office Manager, and the Scheduler-Dispatcher; the network equipment sits in an unlocked supply room | P02, P03 |
| Past events | In 2025 a crew phone was left at a hospital and recovered the next day, and a facility face sheet was faxed to the wrong dialysis center. Neither was logged | P03, P09 |

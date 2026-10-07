# Scenario facts: Cris Santos Company | Emergency Services | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute or regulation, the citation is given; Florida statute text was read from the 2026 Florida Statutes (flsenate.gov) on 2026-10-07.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C; licensed as a Class "B" security agency under Fla. Stat. Chapter 493) |
| Business | Unarmed mobile security patrol and alarm response (NAICS 561612 Security Guards and Patrol Services). One marked patrol vehicle. Night patrols of client properties, checkpoint scans, incident and daily activity reports, and response to client alarm calls |
| Why this business at this size | The vertical's primary industry is ambulance services (NAICS 621910). A sole proprietor cannot staff an ambulance, so this size uses a private security patrol, which is also part of the Emergency Services Sector. The owner is often first on scene at a client property and calls 911 for fire, medical, and police emergencies, but does not provide public safety services |
| Location | Florida. The licensed physical location and principal place of business is the owner's home office (Fla. Stat. 493.6106(2)); the agency license and the Department notice are posted there. All clients are in one county |
| Licenses | Class "B" security agency license (493.6301(1)), first issued 2023-02 and renewed every 3 years (493.6113(1)). The owner holds a Class "D" security officer license (493.6301(5)), held since 2019, and is designated as the agency's manager as a Class "D" licensee of more than 2 years (493.6301(3)(a)). **Unarmed**: no Class "G" license and no firearm on duty (493.6101(9)) |
| Insurance | Commercial general liability policy, $1,000,000 per occurrence, with the Department of Agriculture and Consumer Services as additional insured (493.6110 requires at least $300,000). No standalone cyber insurance |
| Workforce | The owner only (0 employees). No subcontractors perform patrols |
| Clients | 7 active patrol contracts: two gated homeowners' associations (HOA A, about 240 homes; HOA B, about 180 homes), a construction site, a self-storage facility, an auto dealership, a marina dry-storage yard, and a multi-tenant industrial park. A retail plaza contract ended 2025-12-31 |
| Service pattern | Patrols 10 p.m. to 6 a.m., six nights a week (no contracted service Sunday night). On call at all hours for alarm responses at 4 clients (self-storage, dealership, marina, industrial park), about 6 alarm calls a month. Daily activity reports go to clients at 6:30 a.m.; incident reports within 24 hours |
| Revenue | About $180,000 a year (fictional), about $580 per patrol night. SBA-small (standard $29.0 million in average annual receipts for NAICS 561612; 13 CFR 121.201) |
| Personal information held | Incident reports since 2023-03 name about 210 individuals; about 90 of them with a driver license or ID number (trespass warnings and vehicle checks) and about 15 with injury notes (first aid given or 911 called). HOA gate lists hold names, addresses, phone numbers, and license plates for about 420 households. Body-camera video since 2024. GPS patrol tracks of the owner. Under Fla. Stat. 501.171(1)(g), the driver license numbers, injury notes, and online account credentials are "personal information"; a name with geolocation information also is |
| Client access data held | Alarm codes, gate codes, keyholder lists, and post orders for all 7 clients, plus 23 keys and 6 access cards or fobs |
| HIPAA status | **Not a covered entity or business associate.** The owner gives first aid on patrol but does not bill for health care or conduct HIPAA standard transactions (45 CFR 160.103) |
| CJIS status | **No access to criminal justice information.** The business has no connection to state or national criminal justice systems and no agreement with a criminal justice agency (P03) |
| Not in scope | HIPAA; FBI CJIS Security Policy; 28 CFR Part 20 and Part 23; FCC EAS rules (not an EAS participant); CIRCIA (proposed only, and would not reach the business; P03); payment cards (clients pay by ACH or check through the accounting SaaS invoice links) |
| State law approach | Florida law is cited because the business's governing rules are state rules: Chapter 493 (licensing, information release, records), Fla. Stat. 501.171 (reasonable measures, breach notice, disposal), and Fla. Stat. 934.03 (audio recording consent for the body camera) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner (Class "D" licensee and designated agency manager) | Every role: owner, information security lead, records custodian, incident commander, and risk acceptor |
| On-call IT technician | Hourly help with the laptop, phone, and home router. No standing access. Signed a confidentiality agreement on 2026-08-07 |
| Backup patrol agency | Another licensed Class "B" agency in the county. **Verbal** coverage arrangement only: no written agreement, and it holds no client keys, codes, or app access |
| Client site contacts | Property managers, HOA board members, and site supervisors who read reports in the patrol app's client portal |
| Alarm monitoring companies | Contracted by 4 clients; they call the owner as the responding keyholder |

## 3. Systems
| ID | System | Hosting | Holds personal information? | Notes |
|---|---|---|---|---|
| SYS-01 | Patrol management app (guard tour SaaS): phone app, web admin console, and client portal. Checkpoint scans, GPS tracking during shifts, daily activity reports, incident reports with photos, post orders | Vendor SaaS | Yes | **System of record.** Owner admin account had no MFA (see gaps). 12 client portal accounts. Includes an AI report assistant (see P10) |
| SYS-02 | Email and cloud file storage (consumer account) | SaaS | Yes | Contracts, post orders, the client access code spreadsheet, report exports, body-camera clips. Text-message MFA. Synced to the laptop |
| SYS-03 | Accounting and invoicing SaaS | SaaS | No (client billing contacts and bank details for ACH) | Vendor enforces MFA |
| SYS-04 | Laptop (home office) | Owner device | Yes (synced files, video) | Full-disk encryption on. **Shared with a family member under one user account** |
| SYS-05 | Mobile phone | Owner device | Yes | Runs the patrol app; calls and texts with clients; MFA codes; hotspot in the vehicle. 4-digit passcode; message previews show on the lock screen |
| SYS-06 | Body-worn camera | Owner device | Yes (video and audio) | Removable storage card, not encrypted. Clips copied weekly to the laptop and the cloud drive |
| SYS-07 | Home internet and Wi-Fi router | ISP-provided | In transit | WPA2 with a strong passphrase; firmware updated by the ISP |

**SSP system (P02):** the *Patrol Business SaaS Stack*: SYS-01 to SYS-07, with the patrol app (SYS-01) as the system of record, plus client keys and paper records in the owner's custody.

## 4. Current security posture: early (few formal controls)
**In place today:**
- Agency and officer licenses current; insurance on file
- Accounting SaaS MFA (enforced by the vendor); text-message MFA on email
- Laptop full-disk encryption (on from purchase)
- Automatic OS and app updates on the laptop and phone; built-in antivirus on the laptop
- Patrol app vendor's backups and access separation between clients
- Paper key log: each key and access card is signed for when received from a client and when returned
- Paper is shredded at home with a cross-cut shredder

**Missing:**
1. No risk assessment and no written security policy.
2. Client alarm codes, gate codes, and keyholder lists are kept in an unprotected spreadsheet in the consumer cloud drive and in a phone note. Clients text new codes, which show on the phone's lock screen.
3. The patrol app admin account has no MFA, and its password was reused on another site.
4. Client portal accounts have never been reviewed.
5. The laptop is shared with a family member under one user account.
6. Body-camera video is kept with no retention rule; the storage card is not encrypted; clips are shared by public links that never expire.
7. No backup of email and files beyond the sync service, which would copy ransomware damage.
8. Client keys hang on one ring labeled with site names, kept in the patrol vehicle with no lockbox.
9. No incident response plan, contact list, or knowledge of breach notice duties.
10. Phone: 4-digit passcode, lock-screen previews, remote wipe never tested.
11. The patrol app's AI report assistant was turned on without reviewing the vendor's data terms, and its priority label decides which events alert the client immediately.
12. No written coverage arrangement with the backup agency.
13. The home router's admin password is the default printed on its label.
14. No security training.
15. No records retention schedule for the 2-year records duty (Fla. Stat. 493.6121(2)).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Ransomware on the home office laptop encrypts the synced cloud drive (including the client access code spreadsheet), and the attacker takes over the email account and tries the patrol app admin console. This is the one-person version of the registry's "computer-aided dispatch outage from ransomware": the patrol app is the business's dispatch and reporting tool, and losing the codes and email stops alarm response at night |
| P09 SOC 2 | Security criteria only. The business is not a service organization that would obtain a SOC 2 report. Used as (a) the owner's self-check, which supports a self-attestation to clients who send security questionnaires, and (b) a checklist for reading the patrol app vendor's SOC 2 Type 2 report |
| P10 AI | The patrol app's AI report assistant: it drafts incident reports from voice notes and assigns a priority that decides whether the client is alerted at once. This is the one-person version of the registry's "AI-assisted emergency call triage" (triage of incident alerts, not 911 calls) |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-08-07 | IT technician signs the confidentiality agreement |
| 2026-08-10 to 2026-08-14 | Self-assessment with the IT technician (tests on 2026-08-12; vendor SOC 2 report review on 2026-08-13) |
| 2026-08-24 | AI report assistant assessment |
| 2026-08-31 | Deliverables adopted by the owner |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Former client | The retail plaza contract ended 2025-12-31. Its keys were returned in January 2026, but its alarm and gate codes were still in the spreadsheet and its client portal account was still active at assessment | P01, P03, P07 |
| Client portal accounts | 12 client portal accounts. 3 were stale at assessment: an HOA A board member whose term ended, a dealership manager who left, and the former retail plaza contact | P01, P04, P07 |
| Client contract terms | Each patrol agreement requires the owner to keep client access information (keys, codes, post orders, reports) confidential and use it only for the services; to tell the client within 2 hours of a lost key or a code that may be compromised; to tell the client within 24 hours of any other security incident affecting client information; to return keys and client information at contract end; to pay for rekeying if a key is lost; and to arrive within 45 minutes of an alarm company call. Patrols are suspended during declared storm emergencies. The owner read all 7 agreements for this assessment on 2026-08-11 | P01, P03, P05, P07, P08 |
| Test findings (2026-08-12) | The patrol app admin password matched one exposed in a public breach list (password manager breach check) and was changed that day; the router admin page accepted the default password from its label (changed that day); a browser extension with permission to read all sites, installed by the family member, was found and removed; 14 body-camera clips were shared by public links with no expiry; the storage card held about 1,100 clips back to 2024; 9 alarm or gate codes were found in text message threads | P01, P04, P07 |
| Patrol app vendor assurance | The vendor gave its SOC 2 Type 2 report (Security and Availability, 12 months ending 2026-04-30, unqualified opinion) under a nondisclosure agreement. Hosting provider and the AI model provider are carved out. Reviewed 2026-08-13. The report states an RPO of 1 hour and an RTO of 8 hours for the platform | P02, P04, P09 |
| AI report assistant | Turned on 2026-05-04 with a plan upgrade. Voice notes and transcripts go to a third-party AI model provider. The vendor's AI terms allowed customer content to improve the vendor's features unless the admin opted out; the owner opted out on 2026-08-12. Prompts are kept 30 days by the AI provider. About 140 reports were drafted with it by 2026-08-12. Reports labeled "Immediate" alert the client at once; "Routine" events wait for the 6:30 a.m. daily report | P01, P10 |
| AI near miss | On 2026-07-19 at about 1:40 a.m. the owner dictated a note about water coming from under a unit door at the self-storage facility. The assistant labeled it "Maintenance, Routine", so no alert was sent. The manager read the daily report at 6:30 a.m. and arrived at about 7:15 a.m.; the contents of 3 units were water-damaged. The client did not claim against the insurance | P01, P03, P10 |
| Backup agency license check | The owner confirmed the backup agency's Class "B" license on the Division of Licensing's online lookup on 2026-08-11 | P03, P05 |
| Phone and patrol app offline mode | The patrol app stores checkpoint scans and reports on the phone when there is no signal and syncs within minutes of reconnecting | P02, P05 |
| Body-camera audio | The camera records audio with video. The owner usually, but not always, says the camera is recording at the start of a contact | P01, P03, P06 |
| Paper code book | Replacement for the spreadsheet: codes move into the password manager vault, with one sealed paper copy kept in a locked safe at the home office for recovery (POL-01 6.3). Safe purchased 2026-08-20 | P05, P06, P08 |
| Post orders | Each site's post orders in the patrol app include its alarm and gate codes, so the owner can read them on patrol. The admin account can read every site's post orders | P01, P02, P04 |
| Device settings | Phone locks after 30 seconds; laptop after 10 minutes. Remote locate and erase is on but has never been tested. The accounting SaaS uses an app-based second factor. Family devices share the home Wi-Fi with the laptop; a guest network is planned | P02, P04, P09 |
| Spare phone | The owner's previous phone is kept charged at home with the patrol app installed and signed out, as a spare | P05, P06 |
| Training | The owner's only training is the 40-hour Class "D" licensing course (Fla. Stat. 493.6303(4)); no security training | P02, P09 |
| Billing | About $15,000 is invoiced a month; clients pay within 30 days; personal savings cover about 6 weeks of expenses. Clients have never been told how a change of bank details would be announced | P01, P05 |
| Law enforcement contact | The owner talks with sheriff's deputies on most shifts (trespass calls, area checks) and has never been offered criminal justice information, but has no rule against accepting it | P01, P03 |
| Budget | Password manager about $40 a year; versioned backup service about $100 a year; business email and file plan about $110 a year; bolted vehicle lockbox about $150 once | P01, P07 |
| Key count finding | During the 2026-08-12 count, one access fob had no key log entry. The client confirmed it was issued in 2025, and the log was corrected | P07 |
| Personal information count | About 105 individuals in all records have personal information under 501.171 (about 90 with ID numbers and about 15 with injury notes) | P03, P08 |
| Patrol app vendor details | The AI report assistant was released in 2026-03. The SOC 2 report has 1 exception (2 of 40 sampled departed vendor employees kept access more than 3 business days; remediated). Vendor terms promise customer notice of security incidents "without undue delay" with no fixed time. The vendor reviews its AI model provider by questionnaire only. Bridge letter requested 2026-08-13 | P03, P09 |
| AI priority setting | On 2026-08-24 the owner changed the app setting so the AI priority is only a suggestion and the owner must choose a priority before any report is submitted | P10 |
| Emergency sheet | A one-page emergency sheet in the home safe tells a trusted family member how to reach the backup agency and clients if the owner is incapacitated | P05, P06 |

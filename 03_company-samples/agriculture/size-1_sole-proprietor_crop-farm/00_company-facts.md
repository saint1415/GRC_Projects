# Scenario facts: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-operator reports farm income on Schedule F, the farm counterpart of Schedule C) |
| Business | Precision-agriculture combination crop farm (NAICS 111998, All Other Miscellaneous Crop Farming): peanuts in rotation, U-pick strawberries, and watermelons and sweet corn for a farm stand. No single crop is the majority of crop value. Uses connected irrigation, a camera drone, and farm management software |
| Location | Florida. About 120 farmed acres in two parcels. **Home Farm** (owned, 20 acres): 6 acres of U-pick strawberries on drip irrigation with overhead sprinklers for freeze protection, 4 acres of watermelons and sweet corn, the well and pump house, an equipment barn, the farm stand, and the owner's home office. **River Field** (leased from an individual landowner for cash rent, about 100 acres, 3 miles away): peanuts under one center pivot in rotation with a winter cover crop. No buildings at River Field |
| Workforce | The owner-operator only (0 employees). U-pick customers harvest their own strawberries; a custom harvest operator digs and combines the peanuts with its own equipment and crew; the owner does everything else |
| Revenue | About $180,000 a year in receipts (fictional): peanuts to a buying point about $80,000 (44%); U-pick strawberries about $70,000 (39%); farm stand and online pre-orders of watermelons and sweet corn about $30,000 (17%). Under the SBA standard of $2.5 million in average annual receipts for NAICS 111998 (13 CFR 121.201), so SBA-small |
| Sales channels | (1) A peanut buying point (one buyer; settlement sheets). (2) U-pick strawberries, December to April, by online time-slot reservation with prepayment through the booking platform's hosted payment page. (3) Farm stand and online pre-order with on-farm pickup, May to July. About 1,800 customer accounts in the booking platform and about 2,100 subscribers on the email list. Nearly all customers live in Florida |
| Card payments | Prepayment through the booking platform's hosted payment page; at the farm stand, a processor-managed card reader paired with the owner's phone that encrypts card data at the reader. No card numbers are stored on or pass through farm-managed systems. The processor's merchant terms require the farm to protect card data and report suspected compromise; no self-assessment questionnaire has been requested |
| USDA programs | Federal crop insurance on peanuts through a private crop insurance agent; Farm Service Agency farm records and acreage reports; a 2024 Natural Resources Conservation Service (NRCS) conservation contract that cost-shared the Home Farm irrigation automation (pump controller, soil moisture probes, freeze sensor). The farm keeps its own copies of these program documents |
| Food safety status | **Not a covered farm, by qualified exemption** under the FDA Produce Safety Rule. Average annual food sold over the previous 3 years is about $172,000, under the $500,000 inflation-adjusted cut-off (21 CFR 112.5(a)(2); FDA lists $686,476 as the 2023-2025 3-year average value), and about 56% of it was sold directly to qualified end-users (consumers at the U-pick and farm stand), more than the 44% sold to the buying point (112.5(a)(1); 112.3 definition of qualified end-user). The farm is therefore subject only to the modified requirements: farm name and complete business address at the point of purchase or, for Internet sales, in an electronic notice (112.6(b)(2)-(3)), and records showing eligibility, including a written annual review and verification (112.7). Peanuts and sweet corn are on the rarely-consumed-raw list (112.2(a)(1)); strawberries and watermelons are not. The qualified exemption is close: if peanut sales grew to more than half of food sales, the farm would become a covered farm, because its produce sales are well above the $25,000 inflation-adjusted threshold in 112.4(a) (FDA lists $34,324 for 2023-2025) |
| Water use | Groundwater from one Home Farm well and one River Field well under a water use permit from the regional water management district. Flow totals are kept in SYS-01 |
| Drone | One camera drone (RGB and multispectral), registered with the FAA (14 CFR 107.13). The owner-operator holds a remote pilot certificate with a small UAS rating (14 CFR 107.12) and completed recurrent training in 2025 (107.65). The drone only takes pictures; it dispenses nothing, so 14 CFR Part 137 (agricultural aircraft operations, 137.1 and 137.3) does not apply |
| Cybersecurity regulation | **No binding federal cybersecurity rule applies** (P03 section 1). The farm uses **NIST CSF 2.0** as its benchmark, with **NIST SP 800-82 Rev. 3** for the irrigation operational technology (OT) |
| Binding rules that reach farm data | Produce Safety Rule qualified exemption records and notices (21 CFR 112.6, 112.7, Subpart O); Florida's data security, disposal, and breach notice duties (Fla. Stat. 501.171; the statute's definition of covered entity names a sole proprietorship, 501.171(1)(b)) |
| Personal information held | Under Fla. Stat. 501.171(1)(g): (a) the W-9 forms of the custom harvest operator and the River Field landowner (both individuals; names with Social Security numbers), scanned into SYS-02 and entered in SYS-09; (b) about 1,800 booking platform customer accounts (user names or email addresses with passwords), held by the booking vendor as a third-party agent (501.171(1)(h)). The email list and the customer export spreadsheet (names, emails, phone numbers, order history) are not personal information under the statute on their own, but are treated as Confidential |
| Not in scope | **21 CFR Part 121 (N11-R01, FSMA intentional adulteration):** applies only to facilities required to register under FD&C Act section 415 (21 CFR 121.1); farms are exempt from registration (21 CFR 1.226(b)). **H-2A (20 CFR Part 655, Subpart B):** the subpart sets the process for an employer seeking H-2A workers (655.103(a)); the farm has no employees. **Reportable Food Registry (21 U.S.C. 350f):** the duty is on the person who registers a food facility (350f(a)(1)); the farm registers none. **SEC disclosure rules:** not a public company. **FAR 52.204-21, -23, -25:** no federal contracts or subcontracts (the NRCS contract is a conservation cost-share agreement, not a procurement contract). **HIPAA:** not a covered entity. **State comprehensive privacy laws:** none applies; the farm sells in Florida only and is far below the consumer-count thresholds in the cross-sector list; Florida's own privacy law was not analyzed. **CIRCIA:** proposed only, and as proposed would not reach a food and agriculture entity below the SBA size standard |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (data security, disposal, and breach notice, Fla. Stat. 501.171). The samples otherwise stay federal |
| Regulatory driver labels | The vertical requirement N11-R01 does not apply (above). `regulatory_driver` columns therefore cite the benchmark as "CSF 2.0 <subcategory> (benchmark)", the OT guide as "SP 800-82r3 <section>", and binding rules by their own citation: "21 CFR 112.<section>" and "Fla. Stat. 501.171(<subsection>)". N11-R01 is cited only in the not-applicable row of P03 |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-operator | Every role: owner, security lead, risk acceptor, incident lead, food safety (qualified exemption records), and remote pilot in command for the drone |
| On-call IT technician (local computer repair shop) | Hourly help with the laptop, phone, and home router. No standing access. Assisted the 2026 self-assessment |
| Irrigation dealer | Installed the pivot control panel, the Home Farm pump controller, and the soil moisture probes in 2024 and supports them. **Keeps a technician account in SYS-01 with full irrigation control rights, always on.** The service agreement has no security terms |
| Custom harvest operator | Digs and combines the peanuts in September and October with its own crew. No system access. W-9 on file |
| Crop insurance agent | Peanut policy; receives acreage and production reports |
| Tax preparer (CPA) | Prepares Schedule F from SYS-09 exports |
| River Field landowner | Cash rent; W-9 on file |
| Service providers | FMIS vendor, booking platform vendor, card processor, email marketing service, accounting SaaS vendor, AI yield vendor, internet and cellular carriers |

## 3. Systems
| ID | System | Hosting | Holds personal or regulated data? | Notes |
|---|---|---|---|---|
| SYS-01 | Farm management and irrigation software (FMIS): field and crop records, pesticide application records, planting and harvest records, yield maps, flow totals, and the **irrigation control module** (remote start and stop of the pivot and the Home Farm pump, schedules, freeze and pressure alarms sent as text messages) | Vendor SaaS, web and mobile app | Farm records; no personal information | System of record for farm operations. **Owner account uses a password only (MFA available, off), and the same password is used on SYS-10.** The irrigation dealer's technician account has full control. The vendor provides a SOC 2 Type 2 report on request (reviewed in P09) |
| SYS-02 | Email and cloud file storage (consumer-grade personal account, also used for the owner's personal life) | SaaS | Yes: scanned W-9s, the customer export spreadsheet, program documents, the lease | MFA by text message turned on in 2023 at the provider's prompt. No version history or backup turned on |
| SYS-03 | Laptop | Owner device | Yes (downloads; browser-saved passwords) | Full-disk encryption on (enabled by default when bought in 2025). **Shared with family members under one administrator account**; the browser stores the passwords for every farm account. Receives yield monitor and as-applied files from the tractor display by USB stick |
| SYS-04 | Phone and tablet | Owner devices | Yes (SYS-01 app; card reader app; MFA text messages) | Phone: SYS-01 app with irrigation control and alarm texts, the card reader app, and the email account. Tablet: drone ground-station app and field scouting. Both have passcodes and device encryption |
| SYS-05 | Home Farm network | On premises | In transit | Internet provider's router (**default admin password; firmware never updated**), an outdoor access point that bridges Wi-Fi to the pump house, and a farm-stand customer Wi-Fi whose password is posted at the stand. **One flat network:** customer Wi-Fi, the laptop, and the pump controller share it |
| SYS-06 | Irrigation OT | Home Farm pump house and fields; River Field | No | Home Farm pump controller (variable-frequency drive for the well pump, fertigation injector, freeze-protection sprinkler zone) with a local web page; River Field pivot control panel with a cellular modem managed through SYS-01; 12 soil moisture probes; 1 weather and freeze temperature sensor. About 16 devices. Both pump and pivot panels have Hand-Off-Auto switches and a local/remote selector, and the owner can run them by hand |
| SYS-07 | Drone and imagery | Owner device; imagery to SYS-08 and SYS-01 | Incidental (U-pick customers may appear in images) | One camera drone; weekly flights over the strawberries in season |
| SYS-08 | Agronomy analytics SaaS (computer-vision yield prediction) | Vendor SaaS | Farm operational and yield data | Trial for the 2025-26 strawberry season on click-through terms (see P10) |
| SYS-09 | Accounting SaaS and online banking | SaaS | Yes: W-9 data (names and Social Security numbers), bank account details | Bank requires a one-time code before a new payee is added |
| SYS-10 | Sales systems: booking and online pre-order platform (with website and hosted payment page), processor-managed card reader, email marketing service | SaaS and processor service | Yes: about 1,800 customer accounts (held by the vendor) | Booking platform admin account uses a password only, the same as SYS-01. The farm website on the booking platform shows the farm name but **not the complete business address** (112.6(b)(2) gap) |

**SSP system (P02):** the *Farm Management and Irrigation Control Platform (FMICP)*: the whole farm system, SYS-01 to SYS-10, as one boundary, centered on SYS-01 and the irrigation OT (SYS-06) it controls.

## 4. Current security posture: early (few formal controls)
**In place today:**
- MFA by text message on the email account (SYS-02)
- Full-disk encryption on the laptop and device encryption on the phone and tablet
- Automatic operating system updates and built-in antivirus on the laptop; automatic updates on the phone and tablet
- Card data kept off farm systems (encrypting card reader; hosted payment page)
- FMIS vendor-managed backups (stated in its SOC 2 system description)
- Manual operation: Hand-Off-Auto switches and a local/remote selector on the pump controller and the pivot panel; the owner knows how to start freeze protection by hand (not written down)
- The bank requires a one-time code before adding a payee
- Freeze alarm: SYS-01 texts the owner's phone when the field sensor reads at or below the set temperature
- Locked pump house and equipment barn; program documents and the lease also kept on paper in the home office
- Drone registered; remote pilot certificate and recurrent training current
- Farm name and address sign posted at the farm stand and the U-pick check-in table (112.6(b)(2))

**Missing or weak, found in the 2026 self-assessment:**
1. No cybersecurity risk assessment ever performed, and no written security policy.
2. SYS-01 (including irrigation control) and the booking platform admin account use the same password, with no MFA, although both offer it.
3. The irrigation dealer's technician account in SYS-01 has full irrigation control, is always on, and has not been reviewed since 2024. The dealer agreement has no security terms.
4. The laptop is shared with family members under one administrator account, and the browser stores every farm password.
5. No backups of the laptop or the cloud files (no version history). SYS-01 records have never been exported. The sales records that prove the qualified exemption exist only in SYS-09 and SYS-10.
6. Flat home network: the farm-stand customer Wi-Fi, the laptop, and the pump controller share one network. The router keeps its default admin password and has never had a firmware update.
7. The pump controller's local web page still uses the manufacturer's default password (found in P07 testing on 2026-07-16).
8. No incident plan, contact list, or written manual irrigation and freeze-night procedure. The owner is a single point of failure.
9. The freeze alarm has one path (sensor to SYS-01 cloud to a text message). If the internet, the cellular network, or SYS-01 is down on a freeze night, no alarm arrives.
10. The AI yield trial (SYS-08) started on click-through terms that let the vendor use farm imagery and yield data to improve its models. No review of AI tools.
11. No security training.
12. Customer and W-9 records have no retention or disposal rule (Fla. Stat. 501.171(8)); the customer export spreadsheet sits in SYS-02 and on the laptop.
13. No written annual review and verification of qualified exemption eligibility for 2026 (21 CFR 112.7(b)), and the online booking site does not show the farm's complete business address (112.6(b)(2)-(3)).
14. No cyber insurance. Whether the farm liability policy covers cyber events is unconfirmed.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 benchmark | NIST CSF 2.0 (all 106 subcategories) as a self-attested checklist, with SP 800-82 Rev. 3 applied to the OT subcategories. Also checked: Produce Safety Rule qualified exemption requirements (21 CFR 112.5-112.7, Subpart O) and Fla. Stat. 501.171. N11-R01 and H-2A documented as not applicable |
| P08 incident | Ransomware on farm-management and irrigation control systems, **adapted to this size**: the farm runs no server, and SYS-01 is SaaS, so the incident is ransomware on the farm laptop plus takeover of the SYS-01 irrigation control account and the booking platform with passwords stolen from the laptop browser, during the January freeze-protection season |
| P09 SOC 2 | Security criteria only. (a) Owner's self-check; (b) review of the FMIS vendor's SOC 2 Type 2 report. The farm is not a service organization and no buyer asks for a report |
| P10 AI | Computer-vision crop yield prediction (AI-001): the SYS-08 trial used to set how many U-pick reservation slots to open each weekend. Kept from the registry default because the owner really uses it |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-17 | Self-assessment with the on-call IT technician (off-season for strawberries; peanuts under irrigation). OT tests on 2026-07-16, outside pivot run times |
| 2026-08-31 | Deliverables adopted by the owner-operator |
| 2026-11-30 | Freeze-season readiness deadline: every irrigation and freeze-alarm action must be done before the strawberry season starts in December |

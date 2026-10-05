# Scenario facts: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company, its clients, and their facilities are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given. Regulatory text was checked against eCFR (version date 2026-09-23) and rulemaking status against the Federal Register API (checked 2026-10-05).

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner, a board-certified health physicist, files Schedule C) |
| Business | Independent radiation safety consultant (NAICS 541690 Other Scientific and Technical Consulting Services). Radiation protection support during nuclear power plant refueling outages (ALARA planning, radiation work permit reviews, dose assessments), annual radiation protection program reviews for materials licensees, annual security program review support for one Part 37 licensee, shielding calculations, and radiation surveys |
| Why not a plant operator | A sole proprietor cannot operate a nuclear generating station (NAICS 221113, the vertical's primary industry, needs a large licensed staff). The business serves licensees instead, so the vertical's reactor rules reach it only through client contracts and through rules that bind individuals with plant access. P03 confirms this |
| Radioactive materials license | **None.** The business holds no NRC or Florida radioactive materials license and possesses no radioactive material. Survey instrument response checks use the client's check sources on site or are done by the calibration laboratory |
| Owner's qualifications | Board-certified health physicist with 22 years of experience, including 12 years in a power plant radiation protection department. Never an employee of any current client |
| Location | Florida. Home office in the owner's residence; field work at client sites in the Southeast |
| Workforce | The owner only (0 employees). Uses one per-diem health physics technician on a 1099 for about 10 outage days a year, and hourly outside IT help, instead of staff |
| Revenue | About $180,000 a year (fictional), about $3,500 a week. SBA-small (standard $19.0 million, NAICS 541690; 13 CFR 121.201) |
| Clients | Client A about 55% of receipts, Client B about 20%, other small jobs about 25% (section 5 gives the security terms each main client passes down) |
| Client A | A Part 50 power reactor licensee operating a two-unit nuclear power plant in the Southeast. Client A runs a 10 CFR 73.54 cyber security program and a 10 CFR 73.56 access authorization program. It grants the owner **unescorted access** to the protected area for outage work, and a named account with MFA on its **contractor document portal** (vendor SaaS operated for Client A) for work packages, survey maps, and dose reports |
| Client B | A Florida regional hospital holding a Florida radioactive materials license. Its cesium-137 blood irradiator (about 1,200 Ci) is an aggregated **category 2** quantity (Part 37 Appendix A: Cs-137 category 2 is 27.0 Ci, category 1 is 2,700 Ci). Florida applies 10 CFR Part 37 through a standard license condition (Florida submission to the NRC, ADAMS ML23178A117, as recorded in this vertical's Small sample). The owner performs Client B's annual radiation protection program review and supports its annual Part 37 security program review (37.55). Client B's reviewing official found the owner trustworthy and reliable and placed the owner on its list of people approved to see the security plan (37.43(d)(3), (d)(6)) |
| Other small jobs | Shielding calculations and radiation surveys for medical and industrial x-ray facilities and portable gauge users. Facility drawings and workload estimates only; no security plans and no patient information |
| Personal information | Very little: the per-diem technician's W-9 (name and Social Security number) and the owner's own records. This makes the business a Florida "covered entity" in a narrow way (Fla. Stat. 501.171(1)(b) names a sole proprietorship that maintains personal information) |
| Safeguards Information | **None held.** The owner has never produced, received, or acquired Safeguards Information (SGI). Client A's contract says SGI is never sent to contractors. A search of email, files, and paper on 2026-07-21 found none |
| Not in scope | 10 CFR 73.54 and 73.77 as direct duties (the business is not a power reactor licensee); 10 CFR 73.110 (no Part 53 license); NERC CIP (not a registered entity); 10 CFR Part 810 and Part 110 (no export or import); DOT hazmat (ships no radioactive material); HIPAA (Client B's contract excludes patient records); federal contracts (none, so no FAR clauses); payment cards (clients pay by bank transfer and check) |
| State law approach | Florida law is cited only where unavoidable (breach notice for the W-9, Fla. Stat. 501.171; Client B's Florida license condition). The samples otherwise stay federal |

### Regulatory driver IDs used in this sample
The vertical's `requirements.csv` lists power reactor and grid rules (C-NUCLEAR-R01 to R05). None binds this business directly (P03 section 1). C-NUCLEAR-R01 and R03 still appear in driver columns because Client A's contract terms come from Client A's 73.54 program. To keep traceability for the rules that do reach the owner, this sample adds **scenario-level driver IDs (C-NUCLEAR-S01 to S05)**. They are defined here and nowhere else.

| ID | Requirement | Citation | Status for this business |
|---|---|---|---|
| C-NUCLEAR-R01 | NRC cyber rule for power reactors | 10 CFR 73.54 | Not a direct duty. Reaches the owner through CSR-A, which Client A wrote from its 73.54 program (73.54(d)(1) names contractors) |
| C-NUCLEAR-R02 | Part 53 cyber rule | 10 CFR 73.110 | Not applicable |
| C-NUCLEAR-R03 | NRC cyber security event notifications | 10 CFR 73.77 | Not a direct duty. Client A reports; CSR-A (5) makes the owner tell Client A promptly |
| C-NUCLEAR-R04 | NERC CIP | 16 U.S.C. 824o; 18 CFR Part 40 | Not applicable |
| C-NUCLEAR-R05 | CIRCIA (proposed) | Proposed 6 CFR Part 226 | Not in effect; not covered as proposed |
| **C-NUCLEAR-S01** | Client A Contractor Security Requirements (CSR-A) | Contract, signed 2026-02-16 | **Applies (primary analysis in P03)** |
| C-NUCLEAR-S02 | Personnel access authorization, duties of individuals with unescorted access | 10 CFR 73.56(f) and (g) | Applies to the owner as an individual |
| C-NUCLEAR-S03 | Safeguards Information | 10 CFR 73.21 and 73.22 | Applies only if SGI is ever received (none held) |
| C-NUCLEAR-S04 | Part 37 protection of information, as Client B's license condition and CSIA-B pass it down | 10 CFR 37.43(d) and 37.55, through the Florida license condition; CSIA-B, signed 2025-05-14 | Applies through contract |
| C-NUCLEAR-S05 | Florida breach notification and data security | Fla. Stat. 501.171 | Applies (narrow: one W-9) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-consultant | Every role: owner, the only health physicist, security and compliance lead, incident commander, and risk acceptor. Signs every report |
| Per-diem health physics technician | A retired plant radiation protection technician paid on a 1099 for about 10 outage days a year at Client A. Client A approved the technician as a subcontractor and processed the technician through its own access authorization program. Has no access to the business's systems. **No written confidentiality agreement with the business** |
| On-call IT technician | Hourly help with the laptops, phone, and home network. No standing access and no access to client folders. Signed a non-disclosure agreement on 2026-07-14, before the self-assessment |
| Tax accountant | Read-only access to the accounting SaaS for year-end work |
| Calibration laboratory | Calibrates the owner's survey instruments each year and posts certificates to the calibration-tracking SaaS |
| Insurer | Professional liability (errors and omissions) policy. **It excludes data breach and cyber costs; there is no cyber policy** |
| Client security contacts | Client A cyber security program contact and its contractor coordinator; Client A access authorization reviewing official; Client B Radiation Safety Officer (RSO) and its Part 37 reviewing official |

## 3. Systems
| ID | System | Hosting | Holds client security information? | Notes |
|---|---|---|---|---|
| SYS-01 | Business email, calendar, and file storage suite (business plan) | SaaS | Yes: client correspondence, project folders, report drafts | MFA by **text message code** only. File version history 30 days. **Client B's 2025 Part 37 review report folder was shared by an "anyone with the link" link that was still active, and Client B's approved-individuals list and security plan arrived as email attachments (2026-05-12)** |
| SYS-02 | Main laptop | Owner device | Yes: analyses, report drafts, synced project folders | Full-disk encryption on since purchase (2024-01). Built-in antivirus and automatic OS updates. Runs dose assessment and shielding software. **The owner works in an administrator account every day, and the browser saves passwords, including the Client A portal password** |
| SYS-03 | Mobile phone | Personal device | Yes: photos taken under Client A photo permits; texts with Client A radiation protection staff | Passcode and device encryption. Receives the email MFA text codes and holds the authenticator app for the Client A portal. **Camera roll syncs to a personal consumer photo cloud** |
| SYS-04 | Field instrument laptop and survey instruments | Owner devices | Yes: raw survey data from client sites | An older laptop kept only because the survey meter data-logging software needs it. **Its operating system is no longer supported, it has no disk encryption, and it joins the home Wi-Fi to email data files.** Six portable survey instruments, two with data logging |
| SYS-05 | Accounting and invoicing SaaS | SaaS | No (client billing records, bank feed, the W-9 copy) | **Password only, no MFA.** Tax accountant has read-only access |
| SYS-06 | Client-operated access: Client A contractor document portal; Client B secure file share | Client-operated | Yes (the clients' systems) | Named accounts. Client A enforces MFA with an authenticator app; Client B enforces a one-time code by email. The client systems are outside the boundary; the owner's credentials and devices are inside |
| SYS-07 | Home office network | ISP router and Wi-Fi | In transit | Shared with household devices. Router firmware updates automatically. **Router administrator password still the default printed on the label** (found in P07 testing) |
| SYS-08 | AI tools: the drift prediction feature in the instrument calibration-tracking SaaS (AI-001), and a consumer generative AI chat assistant (AI-002) | SaaS | AI-001: instrument readings tagged with client site, building, and room. AI-002: one paragraph of a Client B report draft | See P10. Neither tool was reviewed before use |
| Media | One personal 64 GB USB drive | Owner device | Yes: survey data and dose files from several clients | **Not encrypted.** Used on the field laptop, the main laptop, and (after a kiosk scan) a Client A radiation protection workstation during the spring 2026 outage |
| Paper | Field notebooks, printed survey maps, a locked file cabinet, a cross-cut shredder | Home office | Yes | Printed work packages from Client A's fall 2025 outage are still in the cabinet |

**SSP system (P02):** the *Core Business SaaS Stack (CBSS)*: SYS-01 to SYS-08, the USB drive, and paper records in the home office, including the owner's own credentials and devices used to reach the client-operated systems in SYS-06 (those client systems themselves are outside the boundary).

## 4. Current security posture: early (few formal controls)
**In place today:**
- Full-disk encryption on the main laptop (since 2024-01); device encryption with a passcode on the phone
- MFA on the email and file suite (text message codes); client-enforced MFA on the Client A portal and the Client B share
- Automatic OS updates and built-in antivirus on the main laptop
- Client A's annual cyber security awareness module and behavioral observation refresher completed 2026-03-02, before unescorted access was renewed for the spring outage
- Client B's trustworthiness and reliability determination for information access completed 2025-05-14
- File version history (30 days) in the business suite
- Locked file cabinet and a cross-cut shredder in the home office
- Professional liability insurance (no cyber cover)
- No Safeguards Information held (search 2026-07-21)

**Missing:**
1. No risk assessment, written policies, or incident plan had ever been prepared.
2. Client B security information sits outside Client B's secure share: the 2025 Part 37 review report (which describes uncorrected weaknesses) was shared with an "anyone with the link" link that was still active, and the 2026 security plan and approved-individuals list arrived by email and synced to the laptop. Found 2026-07-21; link turned off and copies deleted the same day; Client B told on 2026-07-22.
3. On 2026-06-09 the owner pasted one paragraph of the draft 2026 Client B review report into a consumer AI chat assistant to improve the wording. Client B was told on 2026-07-22.
4. Email MFA uses text message codes only; the accounting SaaS has no MFA; there is no password manager, and passwords are reused across instrument vendor portals and the accounting SaaS.
5. The owner works in an administrator account every day, and the browser stores the Client A portal password.
6. The field instrument laptop runs an unsupported operating system, has no disk encryption, and connects to the internet.
7. One unencrypted personal USB drive carries data between the field laptop, the main laptop, and Client A's site, and mixes several clients' data.
8. Raw survey data on the field laptop has no backup; the main laptop relies on file sync only (30-day version history).
9. No register of client information. Client A work packages from the fall 2025 outage were never returned or destroyed (CSR-A (8) allows 30 days).
10. Photos taken under Client A photo permits sync to a personal consumer photo cloud.
11. No written procedure for the notices Client A (8 hours) and Client B (24 hours) require, and no rule for an accidental receipt of SGI.
12. The AI drift prediction feature was turned on (2026-05-18) without review, and sends site-tagged readings to the vendor.
13. Home Wi-Fi shared with household devices; router administrator password still the default.
14. No vendor list, no review of SaaS terms, and no confidentiality agreement with the per-diem technician; the technician's W-9 sits in email.
15. No security training beyond Client A's modules, and no cyber insurance.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | The vertical's primary regulation, 10 CFR 73.54 (with RG 5.71 Rev. 1 controls), binds power reactor licensees, not their contractors. It reaches the business **only through Client A's contract**, labeled **CSR-A (1) to (10)**. Binding non-contract duties are added: 10 CFR 73.56(f) and (g) duties of an individual with unescorted access; the SGI rules (73.21 and 73.22) as a conditional duty; Part 37 information protection as Client B's license condition and its agreement (CSIA-B) pass it down; and Fla. Stat. 501.171 (narrow). 73.77, 73.110, NERC CIP, and CIRCIA are recorded as not applicable |
| Client A terms | Contractor Security Requirements (CSR-A), signed 2026-02-16 with the outage work order, written by Client A from its 73.54 cyber security program and 73.56 access authorization program: (1) never connect a non-Client A device or media to any plant digital asset or plant network; contractor devices on site use only the guest wireless network; (2) any portable media used on a Client A computer must be Client A-issued, or scanned at Client A's portable media kiosk before each use, and media used at the site must be dedicated to Client A work; (3) complete Client A's cyber security awareness training before access and every 12 months; (4) use the contractor portal only with the named account and MFA, from a device the contractor controls that is encrypted, patched, and running anti-malware, and never store the portal password in a browser or share it; (5) report to Client A's cyber security contact within 8 hours any suspected compromise of a device, account, or media used for Client A work, and any contact that seeks plant security or system information; (6) keep Client A information only in the portal or in encrypted storage under the contractor's sole control; SGI is never sent to contractors, and any SGI received by mistake must not be copied or forwarded, must be kept in the owner's personal custody, and Client A must be called at once; (7) take photographs in the protected area only under a Client A photo permit, and handle the photos as Client A information; (8) return or destroy Client A information within 30 days after each work order ends, and certify it in writing; (9) keep the duties of an individual with unescorted access (self-reporting, behavioral observation reporting, refresher training); (10) no subcontractor may do Client A work or see Client A information without Client A's approval and access processing |
| Client B terms | Confidentiality and Security Information Agreement (CSIA-B), signed 2025-05-14: (1) see Client B's security plan, implementing procedures, approved-individuals list, and security review reports (together, "Client B security information") only on site or in Client B's secure file share; (2) never keep Client B security information in email or any account other than Client B's share; working notes go only in encrypted storage under the owner's sole control, protected by a password; (3) do not disclose Client B security information to any person or service, including software services, without Client B's written consent; (4) tell Client B's RSO within 24 hours of any suspected unauthorized access to or disclosure of Client B security information; (5) return or destroy working notes within 30 days after Client B accepts each annual review report, and certify it; (6) tell Client B when the owner no longer needs access, so Client B can remove the owner from its list (37.43(d)(6)) |
| P08 incident | Registry default "Cyber attack on plant business network with attempted pivot to digital assets", adapted: the business has no plant network, so the incident is **information-stealing malware on the owner's main laptop, with stolen portal session tokens and saved passwords used to reach Client A's contractor portal, and an attempted pivot toward Client A's plant digital assets through the owner's USB drive** before the fall 2026 outage |
| P09 SOC 2 | Security criteria only. The consultant is not a service organization that would obtain a SOC 2 report; Client A's supplier security questionnaire is answered from this self-check. Part A is the owner's self-check; Part B reviews the email and file suite provider's SOC 2 Type 2 report |
| P10 AI | Registry default "Predictive maintenance for non-safety plant equipment", adapted to the consultant's own equipment: the **drift prediction feature in the calibration-tracking SaaS** that predicts when the owner's survey instruments will drift out of tolerance (AI-001). The consumer AI chat assistant is AI-002 |
| Cloud | SaaS only. No IaaS. The primary system keeps the registry default name ("Core business SaaS stack") and adds the laptops, phone, instruments, and media because they carry client data |

## 6. Assessment calendar (fictional unless a regulation is cited)
| Date | Event |
|---|---|
| 2025-05-14 | CSIA-B signed; Client B's reviewing official completes the trustworthiness and reliability determination and adds the owner to its information access list |
| 2025-06-20 | 2025 Client B Part 37 review report delivered through an "anyone with the link" file link |
| 2025-10-13 to 2025-11-14 | Client A fall 2025 outage (Unit 2) |
| 2026-02-16 | CSR-A signed with the spring 2026 outage work order |
| 2026-03-02 | Client A cyber security awareness module and behavioral observation refresher completed |
| 2026-03-09 to 2026-04-10 | Client A spring 2026 outage (Unit 1). The USB drive is used on a Client A radiation protection workstation after kiosk scans |
| 2026-05-12 | Client B's RSO emails the 2026 security plan and approved-individuals list to the owner for the annual review |
| 2026-05-18 | AI-001 drift prediction feature turned on |
| 2026-06-09 | AI-002 used on one paragraph of the draft 2026 Client B review report |
| 2026-07-14 | IT technician signs a non-disclosure agreement |
| 2026-07-20 to 2026-07-24 | Self-assessment with the on-call IT technician. SaaS mapping 2026-07-22; tests 2026-07-23 |
| 2026-07-21 | Client B link and email copies found, link turned off, copies deleted; SGI search (none found) |
| 2026-07-22 | Client B told under CSIA-B (4) about the link, the email copies, and the AI paste |
| 2026-08-25 | P10 AI use assessment completed |
| 2026-08-31 | Deliverables adopted by the owner-consultant |
| 2026-10-19 to 2026-11-20 | Client A fall 2026 outage (Unit 2), planned |
| 2026-11-30 | 2026 Client B review report due |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Client A's plan | Client A does not share its cyber security plan with contractors, so the owner knows its requirements only through CSR-A | P03 |
| Kiosk | Client A's portable media kiosk refuses unregistered media and prints a scan slip; the owner kept the slips from the spring 2026 outage | P03, P07 |
| Router password | The router administrator password was changed from the label default during the P07 test session on 2026-07-23 | P01, P07 |
| Calibration-tracking MFA | The calibration-tracking SaaS offers MFA, but it was off (found in P04 mapping) | P02, P04, P07 |
| Field laptop | Taken off all networks on 2026-08-31, pending replacement | P01, P07 |
| Old phone | A phone retired in 2023 was traded in with no recorded wipe | P07 |
| Software checks | The owner checks the dose and shielding software against a reference calculation after each update | P07 |
| Suite provider assurance | The suite provider supplied a SOC 2 Type 2 report (Security, Availability, Confidentiality; period ending 2026-03-31; no exceptions), reviewed 2026-07-23 | P02, P09 |
| Bank | The business bank requires its own MFA to approve payments | P01, P09 |
| Instrument checks | The calibration laboratory calibrates each instrument once a year; the owner runs a pre-use response check on a check source before each job (client check sources on site) | P05, P10 |
| AI-002 follow-up | The chat history was deleted and a deletion request sent to the AI chat service on 2026-07-22 | P10 |

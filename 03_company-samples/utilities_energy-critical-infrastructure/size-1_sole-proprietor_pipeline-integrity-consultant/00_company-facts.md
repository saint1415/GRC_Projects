# Scenario facts: Cris Santos Company | Energy | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the engineer-owner files Schedule C) |
| Business | Pipeline integrity engineering consultant (NAICS 541330 Engineering Services). Services: review of in-line inspection (ILI) results and anomaly assessments, dig prioritization, support for operators' integrity management programs (49 CFR Part 192 Subpart O for transmission and Subpart P for distribution), and leak-detection program reviews that use operators' SCADA historian data |
| Why not a pipeline operator | Size substitution from the registry: a sole proprietor cannot operate a transmission pipeline. The business works **for** pipeline operators. Pipeline safety and pipeline security obligations stay with the operators; they reach this business only through contracts and through the rules on Sensitive Security Information (see P03) |
| Location | Florida. A dedicated room used as a home office in the owner's residence. Field visits to client dig sites and stations as an escorted visitor |
| Workforce | The engineer-owner only (0 employees). The owner is a licensed professional engineer. Two independent subcontractors (1099) are used per project (section 2) |
| Clients | Three pipeline operators under written contracts: **Client A**, an interstate natural gas transmission operator that TSA has designated as critical (about 50% of revenue); **Client B**, a Florida intrastate natural gas transmission operator that is not TSA-designated (about 30%); **Client C**, a Florida municipal gas distribution system (about 20%) |
| Revenue | About $180,000 a year (fictional). SBA-small (standard $25.5 million, NAICS 541330; 13 CFR 121.201) |
| Client data held | ILI vendor reports and feature lists, GIS route and high consequence area data, integrity records, dig reports, SCADA historian exports (pressure and flow) for leak-detection reviews, and draft and sealed deliverables. Client A also provided **two records it treats as Sensitive Security Information (SSI)**: an excerpt of its TSA-approved Cybersecurity Implementation Plan describing the data path from its leak-detection system to its business network, and a network zone drawing. Client A's work order documents the owner's need to know for the leak-detection review (49 CFR 1520.11(a)(1)) |
| Personal information held | W-9 forms (names and Social Security numbers) for 5 individual subcontractors used since 2023, and their payment details, in the accounting SaaS and the cloud file account. This makes the business a "covered entity" under Fla. Stat. 501.171(1)(b), which names sole proprietorships |
| Contracts that set security terms | Client A master services agreement with a **Supplier Cybersecurity and Information Protection Addendum** (2025): MFA, encryption, approved services only, approved subcontractors only, incident notice to Client A **within 24 hours**, SSI handled under 49 CFR Part 1520, return or destruction of data within 30 days after each project with written certification, annual security questionnaire, annual training. Client B NDA with incident notice **within 72 hours**. Client C contract with a general confidentiality clause and no notice period |
| TSA status | The business is **not** a pipeline Owner/Operator under TSA Security Directive Pipeline-2021-02G (Section VII.P) and has received no TSA notification. Client A's MSA states that the consultant performs no measures in Client A's Cybersecurity Implementation Plan, so the consultant is not an Authorized Representative (SD Section II.A.4 and VII.A) |
| Not in scope | NERC CIP (no BES assets); DOE-417 (no electric operations); PHMSA 192.631 control room management (no control room); CEII rules (the owner never requests CEII from FERC; client documents come directly from clients under contract); federal contracts and FAR clauses (none); SEC disclosure (not public); payment cards (clients pay by bank transfer) |
| State law approach | Florida law is cited only where it is unavoidable: breach notice and data security for subcontractor personal information (Fla. Stat. 501.171) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Engineer-owner | Every role: owner, security lead, SSI custodian, risk acceptor, incident lead, and the person being assessed |
| GIS and drafting subcontractor (1099) | Prepares maps and alignment sheets from client GIS data. Works remotely on a personal laptop with a personal email address. Signed a one-page NDA in 2024. **Has had access to the whole Client A project folder, including the SSI records** |
| Field NDE and corrosion subcontractor (1099) | Attends digs, records field measurements and photos, and sends field data sheets. Uses a personal phone and email. Signed the same NDA. No access to SSI |
| On-call IT support contractor | Local small IT firm, hourly. Signed an NDA on 2026-08-07 before helping with the self-assessment. No standing access |
| Breach counsel | Not retained in advance; the cyber endorsement on the E&O policy provides a hotline and panel firms (section 3) |

## 3. Systems
| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Business productivity suite: email, calendar, cloud file storage with desktop sync, built-in AI writing assistant | SaaS (business plan) | One tenant. The owner's daily account is also the tenant administrator. MFA with an authenticator app. 30-day file version history. Provider publishes a SOC 2 Type 2 report under NDA |
| SYS-02 | Engineering laptop (workstation class) with licensed engineering analysis software and the owner's scripts | Owner device | Full-disk encryption on since 2025. Automatic OS updates. Built-in antivirus. **Owner works daily in an administrator account** |
| SYS-03 | Mobile phone | Personal device | Authenticator app for every MFA prompt; email; field photos at dig sites. Passcode and device encryption on |
| SYS-04 | Removable media: ILI vendor hardware-encrypted drives (returned to the client after loading) and the owner's USB backup drive | Owner custody | **The backup drive is unencrypted**, kept in an unlocked desk drawer next to the laptop, and updated by a manual monthly copy |
| SYS-05 | Accounting and invoicing SaaS | SaaS | Invoices, payments, bank feed, subcontractor W-9s and 1099s. **Password only; the password is reused elsewhere** |
| SYS-06 | Client-provided access: Client A integrity data portal (client account through Client A's remote access gateway, MFA enforced by Client A) and Client B secure file transfer site | Client systems | Outside the boundary. The owner reaches them from SYS-02 only |
| SYS-07 | Third-party AI anomaly-screening SaaS (free trial) | Vendor SaaS | Screens historian time series and ILI feature lists for leak signatures and anomaly growth. **Trialed with Client A data without Client A's written approval** (see P10) |
| SYS-08 | Home office network | ISP-provided router | Shared with household devices (smart TV, game console). **Router admin password is the factory default** |

**SSP system (P02):** the *Core Business SaaS Stack*: SYS-01 to SYS-05, SYS-07, SYS-08, and the paper client files in the home office, with the client-provided access in SYS-06 as external interfaces.

## 4. Current security posture: informal (basic hygiene, big gaps)
**In place today:**
- Business-plan productivity suite (not a consumer account) with MFA on the owner's account
- Full-disk encryption on the laptop; passcode and encryption on the phone
- Automatic OS updates and built-in antivirus on the laptop and phone
- Client A's portal enforces its own MFA; ILI data arrives on vendor hardware-encrypted drives
- Signed contracts or NDAs with all three clients; one-page NDAs with both subcontractors
- Professional liability (E&O) insurance with a cyber endorsement ($100,000 sublimit; the carrier's breach hotline must be called before hiring outside firms)
- A monthly manual copy of project files to a USB drive

**Missing:**
1. No risk assessment, written security policy, or security procedure has ever existed.
2. Client A's SSI records sit in the general Client A project folder, which is shared with the GIS subcontractor, who has no need-to-know determination. A printed copy of the plan excerpt is in an unlocked desk drawer.
3. The network zone drawing arrived without SSI markings. The owner did not mark it or tell Client A. The owner's draft leak-detection review quotes zone details from the plan excerpt and is not marked.
4. The accounting SaaS (W-9s with Social Security numbers, bank feed) uses a reused password with no MFA.
5. No password manager; passwords are reused across several services.
6. The only backup is the unencrypted USB drive, copied by hand about monthly, kept next to the laptop, and never test-restored. It holds old client data and a copy of the SSI records.
7. Data from three finished projects (2023 to 2025), including one Client A project, is still in cloud storage and on the backup drive. Client A's addendum requires return or destruction within 30 days with a certificate.
8. Subcontractors receive client data through "anyone with the link" share links and personal email, on personal devices of unknown security. Client A never approved either subcontractor in writing.
9. The AI anomaly-screening tool was trialed with Client A historian exports and ILI feature lists without Client A's written approval. The free-trial terms let the vendor use uploaded data to improve its models.
10. No incident response plan. The owner did not know the 24-hour notice term in Client A's addendum or the duty to report unauthorized release of SSI to TSA (49 CFR 1520.9(c)).
11. The home network is shared with household devices, the router keeps its default admin password, and the owner works daily as a laptop administrator.
12. The 2025 Client A security questionnaire said a written incident plan existed. None did.
13. No security training.
14. Single-person dependency: the owner holds every credential, every MFA prompt goes to one phone, and nobody can deliver client work or reach client portals if the owner is unavailable.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 regulation | TSA SD Pipeline-2021-02G (the vertical's named regulation) is recorded as **not applicable** to the consultant, with the contract flow-down explained. Analyzed instead: **49 CFR Part 1520** (binding, because the owner holds Client A's SSI as a covered person under 1520.7(j) and (k)), the Client A addendum (contract flow-down), and Fla. Stat. 501.171(2) (binding for subcontractor personal information) |
| P08 incident | Adapted from the registry default "Ransomware on business IT forcing precautionary pipeline shutdown". The consultant has no pipeline to shut down. The incident is ransomware on the laptop and synced cloud files, with theft of client data (including Client A's SSI) and subcontractor W-9s, while a Client A portal session is open. Client A cuts the consultant's access and decides on any precautions for its own systems, so the runbook centers on giving Client A what it needs within 24 hours |
| P09 SOC 2 | The business is not a service organization whose systems clients rely on, and a SOC 2 examination would cost more than a year's profit. Security-only self-check to support Client A's questionnaire, plus a review of the productivity suite provider's SOC 2 report |
| P10 AI | Adapted from the registry default "Pipeline leak-detection anomaly model": the consultant does not run a leak-detection model for a pipeline; it used a **third-party AI anomaly-screening SaaS** on client leak-detection and ILI data. The productivity suite's AI writing assistant is a second, lower-risk inventory entry |
| Cloud | SaaS only. No IaaS or PaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-31 | AI anomaly-screening tool trial with Client A data (stopped 2026-08-10 when the self-assessment started) |
| 2026-08-10 to 2026-08-14 | Self-assessment with the on-call IT support contractor (tests on 2026-08-13) |
| 2026-09-11 | Deliverables adopted by the engineer-owner |
| 2026-10-30 | Client A annual supplier security questionnaire due (answers to be based on these deliverables) |
| 2026-12-31 | Client A master services agreement renewal |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Subcontractor folder access | The file service's activity log (kept 180 days on this plan) shows the GIS subcontractor opened the Client A folder listing several times but shows no open or download of the two SSI files. Access was removed on 2026-08-13 during testing | P01, P03, P07 |
| Client A notice | On 2026-08-14 the owner told Client A's security contact in writing about the SSI handling gaps, the unmarked drawing, and the AI trial, and asked for written approval or deletion instructions. Client A asked for a deletion request to the AI vendor and a corrected handling plan by 2026-09-30 | P03, P07, P10 |
| AI trial data | About 60 days of pressure and flow historian exports for one Client A segment and one ILI feature list were uploaded to the AI tool. No SSI records and no personal information were uploaded | P01, P10 |
| Recovery targets | The productivity suite provider's SOC 2 system description states daily replicated storage and a recovery objective of 24 hours for the file service; the owner reviewed the report on 2026-08-12 | P04, P05, P09 |
| Urgent findings | Client A and Client B contracts ask the consultant to tell the client within 1 business day after identifying an ILI anomaly that appears to need immediate action, so the operator can decide on pressure reductions under its own program | P05, P08 |

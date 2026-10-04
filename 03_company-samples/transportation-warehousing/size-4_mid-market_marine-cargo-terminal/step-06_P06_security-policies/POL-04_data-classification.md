# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Director of IT and Cybersecurity (CySO), with both FSOs for SSI |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 version) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, incidents or changes to the Coast Guard rule |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-3, MP-4, AC-3, AC-21, SC-8, SC-13, SC-28, CM-8, CM-2, CM-6, CM-7, CM-11, PL-8, CP-9, CP-4, CP-10, CP-2, AU-2, AU-9, AU-11, AU-12, MP-6, AC-20, SA-9, SI-12 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, ID.AM-01, ID.AM-02, ID.AM-03, PR.PS-01, PR.DS-11, RC.RP-03, PR.PS-04, DE.CM-01, GV.SC-05 |
| USCG cyber rule (N48-49-R01) | 33 CFR 101.630(b), 101.640, 101.650(b)(1)-(4), 101.650(b)(3), 101.650(c)(1), 101.650(c)(2), 101.650(f)(1), 101.650(g)(4) |
| Other requirements | 33 CFR 105.225; 33 CFR 105.305(e); 49 CFR 1520.9(a); 49 CFR 1520.9(a)(2); 49 CFR 1520.9(a)(5); Fla. Stat. 501.171(2); Fla. Stat. 501.171(8) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |
| Handling | Internal |

## 1. Purpose
Classify company information, protect it in proportion to its sensitivity, and make sure critical system data, logs and backups are available when needed.

## 2. Scope
All Cris Santos Company workforce members (employees, temporary staff and contractors) at Terminal 1, Terminal 2, the off-dock depot and the headquarters office, plus longshore labor and vendor technicians whenever they use company IT or OT. It covers every system and data set: the cloud landing zone, SaaS services, gate systems, crane and yard equipment controllers (OT), security systems, and systems that vendors operate or support for the company, including any terminal the company acquires, from the day it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Data owners (department heads and terminal General Managers) | Classify their data; approve access and sharing |
| FSOs (T1 and T2) | SSI custodians; keep the SSI repository and the distribution list |
| Director of IT and Cybersecurity (CySO) | Inventory, configuration, encryption, backups and logging |
| General Counsel | Personal information rules and retention |
| All workforce and vendors | Handle data according to its level |

## 4. Policy statements
| Level | Examples | Minimum handling |
|---|---|---|
| **SSI** (49 CFR part 1520) | FSPs, FSAs, the Cybersecurity Plan, network maps, vulnerability and assessment findings, PACS reader records | Marked; SSI repository only; covered persons with a need to know; SSI terms for vendors; destroyed as SSI |
| **Restricted** | Personal information under Fla. Stat. 501.171 (driver license numbers, employee records), credentials and keys, customs release and hold data, dangerous cargo locations | Encrypted at rest and in transit; access by role; logged |
| **Confidential** | Bay plans, manifests, customer contracts and rates, EDI data, financials | Encrypted in transit; approved systems only |
| **Internal** | Procedures, schedules, internal email | Company systems only |
| **Public** | Published tariffs, website content | No restrictions |

4.1 Information must be classified in one of the five levels in the table above. When in doubt, use the higher level. (RA-2; ID.AM-05; 101.650(b)(3))

4.2 **SSI** (the FSPs, FSAs, the Cybersecurity Plan, network maps, vulnerability findings and this program's risk and assessment reports) must be marked, stored only in the SSI repository, shared only with covered persons who need it, given to vendors only under SSI terms, and destroyed as SSI requires. Requests from others are referred to TSA or the Coast Guard (STD-10). (MP-3; MP-4; AC-3; AC-21; PR.DS-01; 101.630(b); 49 CFR 1520.9(a); 33 CFR 105.305(e))

4.3 Restricted, Confidential and SSI data must be encrypted in transit with TLS 1.2 or higher. EDI and file transfers with partners must use AS2, SFTP or TLS; plain FTP is prohibited from 2026-12-31. Where OT protocols cannot be encrypted, the feasibility review and compensating controls must be documented. (SC-8; SC-13; PR.DS-02; 101.650(c)(2))

4.4 Restricted, Confidential and SSI data may be stored only in approved systems and must be encrypted at rest. Driver license numbers may be kept in the TOS gate module for no more than 90 days. (SC-28; PR.DS-01; 101.650(c)(2); Fla. Stat. 501.171(2))

4.5 **Inventory and configuration.** The CySO must keep an inventory of network-connected IT and OT systems at both terminals and the depot, designating critical IT and OT systems, and a consolidated network map with OT device configuration records. Only hardware, firmware and software on the approved list may be installed; systems follow secure baselines (STD-05), and applications running executable code are disabled by default on critical systems. (CM-8; CM-2; CM-6; CM-7; CM-11; PL-8; ID.AM-01; ID.AM-02; ID.AM-03; PR.PS-01; 101.650(b)(1)-(4))

4.6 **Backups and recovery.** Critical IT and OT systems must be backed up and the backups protected from the systems they protect: the TOS database (hourly isolated snapshots and daily write-once copies), gate server images at all three gates (weekly), network device configurations, and PLC programs and HMI settings for both terminals (held offline by the company, not only by an OEM). Restores must be tested at least quarterly against the BIA recovery objectives (STD-06). (CP-9; CP-4; CP-10; CP-2; PR.DS-11; RC.RP-03; 101.650(g)(4))

4.7 Logs must be captured centrally, protected so that only privileged users can access them, kept searchable for 1 year and in a locked archive for 2 years. Required sources include gate servers at all gates, the TOS application audit log and OT monitoring (STD-03). (AU-2; AU-9; AU-11; AU-12; PR.PS-04; DE.CM-01; 101.650(c)(1); 101.640)

4.8 Media and devices that held Restricted, Confidential or SSI data, including gate kiosks, OCR servers and OT media, must be wiped for reuse or destroyed by a certified vendor that provides a certificate. (MP-6; PR.DS-01; Fla. Stat. 501.171(8); 49 CFR 1520.9(a)(5))

4.9 Restricted, Confidential and SSI data must not be entered into AI tools or other third-party services unless the tool is approved under POL-01 4.13 and its contract forbids use of company data to train models for others. (AC-20; SA-9; GV.SC-05; PR.DS-01; 49 CFR 1520.9(a)(2); 101.650(f)(1))

4.10 Records are kept according to POL-01 4.11 and the FSP record rules. (SI-12; PR.PS-04; 101.640; 33 CFR 105.225)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.8. Sanctions range from retraining to termination of employment or of a contract, depending on intent and harm. For longshore labor, the company may refuse further access to its systems and refer the matter to the hiring hall. Compliance is checked through the annual independent assessment (P07), the Cybersecurity Assessment (33 CFR 101.650(e)(1)), the annual Cybersecurity Plan audit once the Plan is approved (101.630(f)), and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved under POL-01 section 4.4, recorded in the risk register (P01), and expire within 12 months. Where a Subpart F measure is not technically feasible (for example MFA on an HMI in a crane cab), the compensating control must be documented for the Cybersecurity Plan, as 101.650 allows.

## 7. Related documents
POL-01; POL-05; STD-03 logging and monitoring; STD-05 configuration; STD-06 contingency and recovery; STD-08 encryption; STD-10 SSI handling; 49 CFR part 1520; Fla. Stat. 501.171

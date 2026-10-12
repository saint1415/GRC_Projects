# Intake Report: Cris Santos Company | Management of Companies and Enterprises | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (family holding company and single-family office, one Florida office suite) |
| Intake window | 2026-07-20 to 2026-07-31 |
| Collected by | Family Office Director, with the Office Manager and the MSP lead technician for the console and MSP exports |
| Approved | Principal, 2026-09-18 |

## 1. Purpose and scope
Intake collected the office's own records before any assessment work began on 2026-08-03. It covers the organization, the systems that hold or reach family and employee information, the suppliers that touch them, and the rules that may bind the office. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

A 7-person family office has no HR system, CMDB or contract management system. Its systems of record are the vendor admin consoles (productivity suite, accounting, bill pay, payroll, investment platform, document vault), the bank and custodian entitlement and activity reports, the MSP's exports, reports and tickets, the contracts folder and company records binder, the staff mailboxes, and what can be seen in the office.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and accounts | EV-001 to EV-004, EV-044 | Payroll service; productivity suite admin console; emails from the Subsidiary Presidents | 2026-07-17 to 2026-07-24 |
| Logging, file sites and the AI add-on | EV-005 to EV-008 | Productivity suite admin console | 2026-07-21 to 2026-07-22 |
| Business systems and money movement | EV-009 to EV-014 | Accounting, bill pay, investment platform and vault admin consoles; bank and custodian portals | 2026-06-30 to 2026-07-23 |
| Devices, network and the cloud workload | EV-015 to EV-020; EV-045 (received 2026-08-04) | MSP device, encryption and antivirus consoles; firewall documentation; cloud console; MSP tickets and monthly report | 2026-06-30 to 2026-07-31 |
| Documents and contracts | EV-021 to EV-026 | Document request; contracts folder; Family Office Director's files; company records binder | 2024-05-15 to 2026-07-27 |
| Finance and vendor assurance | EV-027 to EV-031 | Accounting system reports; vendor folders, websites and portals | 2025-12-31 to 2026-07-28 |
| Insurance, benefits, training and governance | EV-032 to EV-036 | Family Office Director's files; insurer portal; training vendor portal; company records binder | 2024-01-15 to 2026-07-28 |
| Events and AI tools | EV-037 to EV-039 | Staff mailboxes; staff survey | 2026-03-17 to 2026-07-29 |
| Office and interviews | EV-040 to EV-043 | Walk-through; key list and alarm contract; shredding receipts; intake interviews | 2026-06-30 to 2026-07-29 |

## 3. Observations by area
**People and accounts.** Payroll lists 7 office employees and 5 household employees paid on behalf of family members, a biweekly pay schedule, and 1 office employee termination in 2025 and none in 2026. Its document store holds new-hire forms for current and former household employees with no deletion dates (EV-001). The productivity suite has 7 named staff accounts and 9 guest accounts from the subsidiaries, with no guest expiry and no record of a guest review (EV-002). The subsidiaries list 8 current contacts who need access (EV-044). Two accounts hold the global administrator role: the Office Manager's and one account that MSP technicians use, whose MFA is registered to the MSP help desk phone (EV-003). MFA is required for all staff and guests by push approval with number matching off, and sign-in is not limited to managed devices (EV-004).

**Logging, file sites and the AI add-on.** Audit logging is on at the license default retention, shorter than one year. No alert policies exist for new inbox rules, forwarding, mass download or administrator changes, and no backup application is connected to the tenant (EV-005). In the Family site every staff account can open every family member's folder, including tax returns, estate plans, ID copies and medical bills. Every guest can open the whole Subsidiaries site (EV-006). The AI assistant add-on was assigned to 4 users on 2026-06-15 and paused on 2026-07-23 (EV-007). Tax returns and ID copies in the Family site go back to 2009, and no site applies retention labels (EV-008).

**Business systems and money movement.** The accounting system holds the office and family entity ledgers and payee bank details; sign-in is through the productivity suite (EV-009). The bill pay platform has 2 users and about 140 family payments a month (EV-010). The investment platform receives read-only feeds from the two custodians and shows about $310 million in securities and 14 private fund and direct deal interests; its generative commentary feature is off (EV-011). The vault gives each family member a folder of their own. Two family users sign in with SMS codes, no account exists in the name of the Principal's spouse, and share links have no expiry by default (EV-012). The banks enforce dual approval for wires and ACH batches, each approver holds one hardware token, and the Principal is backup approver on every bank portal (EV-013). About 15 outgoing wires a month leave office and family entity accounts, and the office approves about 30 subsidiary payments over $25,000 a month (EV-014).

**Devices, network and the cloud workload.** The MSP manages 8 laptops (1 spare), a conference-room PC signed in with a shared account, and a multifunction printer. Laptops patch automatically, staff have no local administrator rights, and screens lock after 10 minutes. Staff personal phones are not enrolled in any device management (EV-015). All 8 laptops are encrypted (EV-016). Antivirus runs on the laptops, the conference-room PC and SYS-11, with alerts to the MSP help desk in business hours and no endpoint detection and response agent (EV-017). The firewall blocks unsolicited inbound traffic, guest Wi-Fi is separate, the staff Wi-Fi password was last changed in 2023, and there is one internet line (EV-018). SYS-11 is one virtual machine whose operating system support ends in October 2026. Remote desktop is allowed from the office IP address only, on a port that faces the internet, and daily snapshots are kept 14 days in the same cloud account (EV-019). The ticket history shows no restore tests and setting changes made on email requests with no approval record (EV-020). The July MSP report, received on 2026-08-04, shows the printer is not on the patch schedule (EV-045).

**Documents and contracts.** The document request returned no written information security program, policies, incident response or contingency plan, retention schedule, payment verification procedure, service provider list, incident log, prior risk assessment, or designation of a security lead (EV-021). The MSP contract sets a 4-business-hour response time with no recovery time commitment and no security terms, and does not include vulnerability scanning or endpoint detection and response (EV-022). The CPA firm engagement letter and the three management agreements have no security terms, and no vendor file holds a security questionnaire (EV-023). The office serves 11 family members and 10 family entities under written service agreements (EV-024). It is owned 51% by the Principal and 49% by a family trust, owns the three subsidiaries outright, and holds no bank interest or registered securities (EV-025). Outside counsel reviewed the family office exclusion in 2024 (EV-026).

**Finance and vendor assurance.** FY2025 receipts were about $1.1 million: $640,000 in management fees and $460,000 in service fees. The budgets have no security line (EV-027). The accounts payable list shows the SaaS vendors, the cloud provider, the MSP and other suppliers, the AI add-on charges from June 2026, and no backup service or card processor (EV-028). SOC 2 Type 2 reports from the accounting system vendor (12 months ending 2025-12-31) and the investment platform vendor (12 months ending 2026-06-30) are on file with no review record (EV-029, EV-030). The SaaS vendors describe encryption at rest and in transit and account lockout on their defaults (EV-031).

**Insurance, benefits, training and governance.** The cyber policy has a breach hotline and panel vendors, and its social engineering fraud coverage requires documented verification of payment changes (EV-032). The group health plan is fully insured, and the office sees enrollment and billing data only (EV-033). One general awareness video is assigned each year, with completion records for 2026 only (EV-034). Board of Managers minutes for 2025 and 2026 have no security item (EV-035). The 2024 family governance charter states the office's purpose and has no security section (EV-036).

**Events and AI tools.** In March 2026 a look-alike email in an adult child's name asked for a $48,000 wire to a new account. The Senior Accountant declined it, and no incident record refers to it (EV-037). On 2026-07-22 the AI assistant's summary for the Executive Assistant included a trust distribution memo from the Family site, and the pilot was paused the next day (EV-038). Four staff use the AI assistant pilot. An adult grandchild wrote in July 2026 that a custodian statement had been pasted into a free public chatbot. No approved AI tools list was found (EV-039).

**Office and interviews.** The suite has keyed entry with an after-hours alarm, a locked file room, a safe for bank tokens and originals, and a locked shredding bin (EV-040). Three people hold keys (EV-041). The shredding service leaves monthly receipts (EV-042). Staff describe payment instructions arriving by email and a callback habit that is not written or recorded, accounts created and removed on email request with no checklist, no log review, the insurer's hotline known only to the Family Office Director, and the Principal's spouse using the Principal's vault account (EV-043).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Whether staff or other family members use public chatbots for office information, and what they enter | Family Office Director (survey follow-up) | 2026-07-30 | Not established at intake; P10 treats it as unknown |
| MSP technician list, use of the shared administrator account, and evidence of MFA on the remote management platform | MSP lead technician | 2026-07-24 | Not provided; asked again in P07 on 2026-08-24 (EV-SA-9) and carried into the P01 risk register (R-005) and POAM-010 |
| MSP subcontractor list | MSP lead technician | 2026-07-24 | Not provided; asked again in P07 and carried into POAM-010 |
| MSP monthly service report for July 2026 | MSP lead technician | 2026-07-24 | Received 2026-08-04 (EV-045, intake follow-up) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-043), receipts (EV-027), wire, approval and bill pay volumes (EV-010, EV-014), positions and custodians (EV-011), SYS-11 snapshots (EV-019), the MSP contract (EV-022), vendor assurance (EV-029, EV-030), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-020 and EV-045 |
| P04 Cloud mapping | SaaS components and the SYS-11 workload (EV-002 to EV-012, EV-019), the MSP's role (EV-022) and provider documentation (EV-029 to EV-031) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the March 2026 request (EV-037), the AI events (EV-038, EV-039), the contracts and insurance policy (EV-022, EV-023, EV-032) and the intake interviews (EV-043) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the CSF 2.0 profile and the Safeguards Rule |
| P06 Policies | The document request result (EV-021) and the governance charter (EV-036) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-012, EV-013, EV-015, EV-044) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cyber policy (EV-032) |
| P09 SOC 2 | Vendor assurance on file (EV-029, EV-030, EV-031) |
| P10 AI governance | AI tools found (EV-007, EV-011, EV-028, EV-038, EV-039) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not an office-maintained inventory: the SSP (CM-8) records that the office keeps no list of its SaaS systems and service providers, and the service provider list is planned in POAM-010.

# Intake Report: Cris Santos Company | Defense Industrial Base | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts manufacturer, DoD subcontractor, one Florida plant) |
| Intake window | 2026-06-29 to 2026-07-10 (plant walk-through 2026-07-08) |
| Collected by | IT Manager, with the Contracts Manager (contracts and export records) and the Manufacturing Systems Engineer (MES, DNC and machine records) |
| Approved | Vice President of Operations, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the CUI Engineering Enclave and the systems around it (MES, DNC, CNC machines, the corporate network, ERP, payroll), the suppliers that touch them, the subcontract clauses, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, configuration reviews, scans, control tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets an SP 800-171 requirement or a DFARS clause is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-009 | Enclave identity provider; payroll and HR SaaS; HR files; IT mailbox; export compliance files; IT ticketing | 2024-06-01 to 2026-07-06 |
| Endpoints and network | EV-010 to EV-015 | Device management and EDR consoles; patch records; enclave firewall; wireless controller; key spreadsheet | 2026-06-30 to 2026-07-02 |
| Cloud enclave | EV-016 to EV-018, EV-022, EV-023 | Cloud provider console; log workspace; backup service; collaboration suite; SFTP gateway | 2026-06-30 to 2026-07-02 |
| Shop floor | EV-019 to EV-021, EV-036, EV-037 | MES and DNC servers; OT inventory spreadsheet; plant walk-through; printed traveler sample | 2026-07-06 to 2026-07-08 |
| Documents and records | EV-024 to EV-032 | Web filter; IT shared drive; SPRS; document request list; learning records; HR and sales files | 2024-01-01 to 2026-07-06 |
| Facilities | EV-033 to EV-035 | Badge system; facilities files; reception visitor log | 2026-06-30 to 2026-07-06 |
| Contracts and suppliers | EV-038 to EV-048 | Contract files; ERP purchasing and finance; supplier files; provider portal; MSP agreement; insurance; maintenance records; QMS | 2026-03-16 to 2026-07-06 |
| Business volume and customers | EV-049 to EV-052 | ERP finance and orders; PLM; sales files | 2025-12-31 to 2026-07-06 |

## 3. Observations by area
**Users and access.** The enclave identity provider holds 64 accounts: 50 named users, 4 administrators, 2 break-glass and 8 service accounts, all under the MFA requirement. Administrator and break-glass accounts use hardware security keys (EV-001). Every sign-in needs MFA and a compliant enrolled device; standard users register an authenticator app. Lockout is set at 10 failed attempts, passwords need 14 characters, and sessions end after 30 minutes idle (EV-002). Privileged roles are activated just in time with IT Manager approval. The 2 Systems Administrators hold all cloud roles, including log and backup settings, and all 4 administrators can change logging settings (EV-003). HR lists 250 employees, with the terminations and transfers from January to June 2026 (EV-004). The HR checklist requires a background check, and enclave access waits for the Contracts Manager's U.S.-person verification. At termination HR emails IT, with no time requirement and no step for transfers (EV-005 to EV-007). The company is registered with DDTC and has an export compliance manual (EV-008). Access requests carry manager approval. There are no change tickets for enclave systems and no incident category in the ticket system (EV-009).

**Endpoints and network.** Device management lists 24 CAD workstations and 16 enclave laptops, all with full-disk encryption, a 15-minute screen lock and the CUI banner. Allowlisting runs in audit mode (EV-010). Endpoints are patched monthly; VMs are patched by hand with no schedule, and MES quarterly (EV-011). EDR runs on the endpoints, the cloud VMs and the MES and DNC servers, and its alerts are worked during business hours (EV-012). The enclave firewall separates the enclave VLANs from the corporate network. The engineering VLAN allows any outbound traffic, firewall logs stay on the device, the VPN uses a pre-shared key with the firewall's FIPS mode off, and the plant has one internet circuit (EV-013). No access points sit on enclave VLANs (EV-014). The VPN key has not changed since installation (EV-015).

**Cloud enclave.** The cloud subscription holds 2 PLM VMs, a 20-session virtual desktop pool, the SFTP gateway in its own subnet, and the log, key and backup vaults, all in one region. Network security groups deny by default (EV-016). The log workspace collects identity, suite and cloud logs for 90 days. It has no MES, DNC or firewall source, and no alert rules or review records (EV-017). PLM backs up daily, and no restore job ran from April to June 2026 (EV-018). The suite limits external sharing to 6 domains; some project sites are shared with all enclave users, and the AI assistant add-on is off (EV-022). The SFTP gateway gives Prime B and the 3 outside processors one shared directory tree, and its cryptographic library is not in FIPS mode (EV-023).

**Shop floor.** MES and DNC back up weekly to a local disk in the same room. Their disks are not encrypted, and the MES server runs web administration and remote desktop (EV-019). MES uses shared terminal logins, 6-character passwords, no lockout and no MFA, and operators can edit NC programs. DNC runs under a shared service account (EV-020). Of 38 CNC machines, 32 take programs from DNC and 6 are loaded by USB drive. The OT spreadsheet was last updated in 2024 (EV-021). On the walk-through, printed drawings and travelers lay at machines and in open bins, general recycling bins stood in the cells, and unlabeled USB drives sat in an open drawer at the programming desk. MES terminals had no session lock, and the 3 shop-floor printers stand in open aisles (EV-036). The 10 sampled MES travelers carry no CUI marking (EV-037).

**Documents and records.** The web filter has no category rule for generative AI or file-sharing sites (EV-024). SSP v1.0 and the POA&M date from 2024-08-30 and cover the cloud enclave only (EV-025). SPRS shows a score of 96 posted 2024-09-12. The self-assessment sheet behind it has no evidence references (EV-026). The request for a risk assessment, baselines, a change procedure, scan reports, log reviews, a contingency plan, restore tests, an evidence preservation procedure, a forensic retainer, DIBNet records, a medium assurance certificate, insider threat or role-based training, a sanitization procedure for CNC controller storage, an approved USB list, and an approved AI tools list returned none (EV-027). The 2024 incident response outline has no DIBNet or preservation steps (EV-028). Annual awareness training reached 96% of staff and has no CUI, export or insider threat content (EV-029). The handbook has no security section (EV-030). Website postings get a Contracts Manager release review (EV-031). The telework template has no rule on printed CUI (EV-032).

**Facilities.** Badge groups restrict the engineering wing and the server room, and server room keys are logged (EV-033). Cameras cover the entrances, the dock and the server room, and the alarm is monitored after hours (EV-034). The June visitor log is missing an exit time or host name on 11 of 30 days (EV-035).

**Contracts and suppliers.** Both subcontracts include DFARS 252.204-7012, 252.204-7019, 252.204-7020, FAR 52.204-21 and FAR 52.204-25, and not 252.204-7021 (EV-038). Prime A told suppliers that solicitations from 2026-11-10 would require CMMC Level 2 (C3PAO) (EV-039). The 3 outside processors' purchase orders carry no DFARS clause, and their files hold no SPRS or CMMC status (EV-040, EV-041). Accounts payable shows the cloud, SaaS, MSP, software, machine tool, insurance and processor payments and no AI service subscription (EV-042). The cloud provider's customer responsibility matrix is on file (EV-043). The MSP's scope is the corporate network and its 170 endpoints only (EV-044). The cyber policy starts claims at the carrier hotline (EV-045). Vendor visits are escorted and logged, and MES remote support uses a watched guest desktop with MFA (EV-046). IT drives are wiped with certificates (EV-047). Paper drawings travel to outside processors in envelopes with no sealing step (EV-048).

**Business volume and customers.** FY2025 revenue was $68 million over about 250 production days: Prime A about 40%, Prime B about 18%, Customer C about 25% (EV-049). PLM holds about 41,000 controlled documents, and about 3 new part numbers start each week (EV-050). ERP orders hold DoD purchase order data and no drawings (EV-051). Customer C's supplier review accepts a Security-only Trust Services Criteria self-assessment (EV-052).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Staff use of public generative AI tools, and what was pasted | Director of Engineering | 2026-07-07 | Not established at intake; the use by 3 engineers was found in the gap analysis interviews on 2026-07-16 (EV-057) |
| FedRAMP Marketplace listing for the cloud offering | IT Manager | 2026-07-06 | Checked on 2026-07-14 during P03 (EV-054) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-004), revenue per production day (EV-049), part number volume (EV-050), backup schedules (EV-018, EV-019), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-003, EV-010 to EV-024 and EV-036 |
| P04 Cloud mapping | Cloud and SaaS components (EV-016, EV-017, EV-022, EV-023) and the provider's responsibility matrix (EV-043) |
| P01 Risk register | Likelihood inputs from the configuration exports, the walk-through, the records request (EV-027) and the supplier records |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the 110 SP 800-171 Rev. 2 requirements and the clause duties |
| P06 Policies | The 2024 incident response outline (EV-028), the handbook (EV-030) and the telework template (EV-032) |
| P07 Control assessment | Populations to sample from (EV-001, EV-004, EV-020, EV-021, EV-035) |
| P08 IR runbook | Notification duties from the obligations register and the subcontracts (EV-038); contacts from the vendor register |
| P09 SOC 2 | Customer C's request (EV-052) and the provider's responsibility matrix (EV-043) |
| P10 AI governance | AI tools found (EV-022, EV-024, EV-043) |

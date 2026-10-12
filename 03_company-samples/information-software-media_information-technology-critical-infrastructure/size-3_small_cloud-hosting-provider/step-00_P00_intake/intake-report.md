# Intake Report: Cris Santos Company | Information Technology | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (cloud hosting and managed infrastructure provider; HQ, NOC and DC-1 in Florida, DC-2 in another state) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (Information Security Officer), with the Director of Platform Engineering and the Controller |
| Approved | Chief Operating Officer, 2026-09-25 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that host, manage or reach customer workloads and data, the vendors that operate parts of the service, and the laws and contracts that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, scans, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement or a commitment is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-011 | Identity provider; HR system and files; ticketing system; cloud IAM and secrets manager; hypervisor managers and BMCs; password vault; RMM console; customer portal admin console | 2026-06-30 to 2026-07-06 |
| Network, data center and cloud | EV-012 to EV-023 | Firewall management and cloud network rules; bastion; platform asset spreadsheet; hypervisor, storage and replication consoles; cloud backup service; key management; DNS and registrar; SIEM; device management and EDR; code hosting and CI/CD | 2026-06-30 to 2026-07-03 |
| Engineering and operations records | EV-024 to EV-029 | Engineering wiki and documentation site; scanning service; penetration test report; status page and NOC monitoring; ticketing system | 2026-03-27 to 2026-07-06 |
| Documents and people | EV-030 to EV-034 | Shared drive and document request list; HR learning records; COO's files; HR files; Controller's files | 2025-01-01 to 2026-07-06 |
| Vendors and contracts | EV-035 to EV-043 | Controller's vendor files and contracts folder; billing and finance system; Sales Director's files; colocation customer portals | 2026-05-18 to 2026-07-06 |
| Business volume | EV-044, EV-045 | Billing and finance system; control plane metering and customer portal | 2025-12-31 to 2026-06-30 |
| AI tools and productivity suite | EV-046, EV-047 | Identity provider app list and staff survey; productivity suite admin console | 2026-07-01 to 2026-07-07 |

## 3. Observations by area
**Users and access.** The identity provider holds 62 active named accounts (60 employees and 2 contract engineers), each with a hardware security key registered. No attribute marks contractor status or an expiry date (EV-001). Conditional access requires a hardware key for single sign-on, the cloud console, the code repository and the RMM web console, and accounts lock after 10 failed attempts (EV-002). HR recorded 14 new hires, 12 terminations and 3 internal transfers from July 2025 to June 2026, with a background check date for each hire; all 60 employees work in the U.S. (EV-003). HR emails IT on the start date and the last day, with no timeframe for removal (EV-004). The 12 disable tickets closed 0 to 3 business days after the last working day, and RMM, hypervisor manager and BMC local accounts were removed by hand (EV-005). One cloud account and region hold production, non-production, build runners and backups. The build runner role can read production secrets, and the same administrator roles manage production and backups (EV-006). The control plane holds long-lived credentials for all 4 hypervisor managers (EV-007). Hypervisor managers and BMCs use local and shared root accounts with no MFA, and all 12 platform engineers hold the full administrator role (EV-008). The shared root credentials sit in the password vault with no rotation after checkout (EV-009). The RMM tool has 3 shared technician accounts, no source-IP restriction and no second approval for scripts, and its agents reach about 1,900 servers for 58 customers (EV-010). Customer portal MFA is optional, and 38% of customer administrators have enrolled (EV-011).

**Network, data center and cloud.** A firewall rule lets the NOC network reach the management network, although the bastion is the documented administration path (EV-012, EV-013). Bastion sessions have no idle timeout (EV-013). The asset spreadsheet lists 96 hypervisor hosts in 4 clusters and 6 storage arrays. One cluster is one major release behind, BMC firmware has no update schedule, and BMCs and network devices are only partly listed (EV-014). Storage arrays use self-encrypting drives, customer VM volumes are not encrypted by default, and array firmware is applied directly to production (EV-016). About 30% of customer VMs replicate to DC-2 (EV-017). Nightly tenant database backups all completed from April to June 2026. They sit in the production account and region with object lock off, and no restore job was run (EV-018). DNSSEC signing is off for company zones, and the registrar account's recovery address is a shared mailbox (EV-020). The SIEM collects identity provider, cloud and EDR logs only, keeps them 90 days, and auto-closes alerts scoring under 30 with the AI triage feature enabled in April 2026 (EV-021). All 64 laptops and 6 NOC workstations have EDR and full-disk encryption (EV-022). Branch protection requires one approver but can be bypassed, a hotfix path merges without review, and the VM template signing key is a pipeline secret (EV-023).

**Engineering and operations records.** The development lifecycle has no security steps (EV-024). External scans run quarterly, with no internal or authenticated scans, and 2 High findings from the Q1 scan were still open (EV-025). The 2026-03 penetration test covered the portal and API only (EV-026). The NOC monitors availability 24x7 and posts maintenance on a separately hosted status page (EV-027). Three security incidents in 2025-2026 were handled in tickets with no category, severity or lessons-learned notes (EV-028). No change tickets exist for data center changes in the 12 months to June 2026 (EV-029).

**Documents and people.** The policy set is a 2022 draft with no approval record, assembled to answer customer questionnaires. The request for a risk assessment, an incident response plan, a customer or bank notification procedure, a contingency plan, a control plane recovery runbook, access review records and a cryptographic module inventory returned none (EV-030). All 60 employees completed 2026 annual awareness training. No role-based or insider threat content is assigned (EV-031). The IT Manager is the designated part-time Information Security Officer (EV-032). The cyber insurance policy offers an incident response panel (EV-034).

**Vendors and contracts.** The colocation SOC 2 reports on file have review notes dated 2024. No report or review record exists for the RMM or SIEM vendor (EV-035). Payments went to the vendors in the [vendor register](vendor-register.csv), including an enterprise coding assistant with 4 seats (EV-036). The RMM vendor terms have no security or incident notice terms, and the SIEM order form sets 90-day retention (EV-037). The MSA promises 99.95% and 99.9% availability, confidentiality and incident notice within 72 hours of confirmation, and prohibits PHI, CUI and payment card data (EV-039). Fourteen community banks treat the company's services as subject to the Bank Service Company Act (EV-040). An agency program office sent a letter of interest in May 2026 (EV-041), and the FedRAMP advisor's engagement letter is on file (EV-042). Colocation access lists name only platform engineers and show no review record (EV-043).

**Business volume.** FY2025 revenue was $24.0 million, about $2.0 million billed per month (EV-044). About 430 customers, including 14 community banks, run about 2,300 VMs, and 58 managed services customers have about 1,900 servers with RMM agents (EV-045).

**AI tools and productivity suite.** AI triage in the SIEM was turned on in April 2026 by a platform engineer during a trial, with no change record. Four software engineers pilot an enterprise coding assistant, and staff report using public chatbots for drafting. No approved-tools list was found (EV-046). Productivity suite spam filtering is on (EV-047).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Current SOC 2 Type 2 reports from the DC-1 and DC-2 colocation providers | Controller | 2026-07-06 | DC-1 report received 2026-08-07 (EV-057); DC-2 report not received, carried into P09 and POAM-020 |
| SOC 2 reports or security questionnaires from the RMM and SIEM vendors | Controller | 2026-07-06 | Not provided; carried into P01 (R-025) and POAM-020 |
| Bank-designated points of contact for all 14 banks | NOC and Support Manager | 2026-07-06 | Contact list exported during P03 fieldwork (EV-055); carried into P01 (R-022) |
| Number of staff using public chatbots, and what they paste | Chief Operating Officer | 2026-07-08 | Not established at intake; P10 treats it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue and billing (EV-044), customer and usage volume (EV-045), MSA service levels and credit tiers (EV-039), replication and backups (EV-017, EV-018), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-023 |
| P04 Cloud mapping | Cloud and SaaS components (EV-006, EV-007, EV-018, EV-019, EV-021, EV-023) and vendor assurance on file (EV-035, EV-037) |
| P01 Risk register | Likelihood inputs from the configuration exports, the incident and change tickets (EV-028, EV-029), the scan reports (EV-025) and the contracts (EV-037, EV-039) |
| P03 Gap analysis | The obligations register (which rules and commitments apply) and every observation above, compared with the FedRAMP Rev5 Class C rules and the bank service provider rule |
| P06 Policies | The 2022 draft policy set (EV-030) and the handbook (EV-033) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-005, EV-008, EV-010, EV-014) |
| P08 IR runbook | Notification duties from the obligations register; contract clocks (EV-039, EV-040); insurer panel (EV-034) |
| P09 SOC 2 | Bank requests for a SOC 2 report (EV-040) and vendor assurance on file (EV-035) |
| P10 AI governance | AI tools found (EV-021, EV-036, EV-046) |

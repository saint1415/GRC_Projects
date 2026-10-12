# Intake Report: Cris Santos Company | Information | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher, Vendor Compliance Platform) |
| Intake window | 2026-07-13 to 2026-07-24 |
| Collected by | CTO (security and compliance lead), with the Operations and Finance Manager and the MSP lead technician |
| Approved | Chief Executive Officer, 2026-09-15 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-27. It covers the organization, the production platform and the SaaS services that build, run and support it, the laptops used to administer it, the suppliers that receive customer data, and the rules that may bind the company. For a 7-person SaaS company the systems of record are the cloud console, the repository host, the productivity suite admin console (exported by the MSP), the MSP's device reports, the payroll service, the accounting and billing SaaS, the contracts folder, the company website, and short interviews. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, exports, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement or a commitment is decided in the regulatory analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-005, EV-029 | Payroll service; productivity suite admin console and MSP tickets; cloud console; repository host; application configuration; designation letter | 2026-06-30 to 2026-07-15 |
| Cloud and data | EV-006 to EV-010 | Cloud console; infrastructure code; production database queries; repository design documents; error tracking console | 2026-07-14 to 2026-07-15 |
| Endpoints | EV-011 | MSP device management and antivirus consoles | 2026-07-10 |
| Documents and statements | EV-012 to EV-014 | Document request list and shared drive; company website; CRM and questionnaire answer document | 2026-07-14 to 2026-07-16 |
| Suppliers and contracts | EV-015 to EV-021 | Contracts folder; published sub-processor list; model provider console; card statements and invoices; cloud provider compliance portal | 2024-09-30 to 2026-07-16 |
| Business volume | EV-022, EV-023 | Accounting SaaS; payment processor and CRM | 2026-06-30 |
| Interviews | EV-024, EV-025 | CTO; Operations and Finance Manager | 2026-07-16 |
| AI tools and monitoring | EV-026 to EV-028 | Staff survey; AI coding assistant console; uptime monitoring SaaS | 2026-07-14 to 2026-07-16 |

## 3. Observations by area
**People and access.** The payroll register lists 7 employees, all with Florida addresses, and a part-time contract developer in another U.S. state; the former Customer Success Manager left in March 2026 (EV-001). The productivity suite has named accounts for the employees and the contract developer, enforces MFA by authenticator app push, and gives single sign-on to the repository, support desk and CRM. Two MSP technicians hold global administrator accounts. The former Customer Success Manager's suite account was disabled on the last working day (EV-002). In the cloud account, the CTO, both engineers and the contract developer each have a console account with MFA and the full administrator policy, and no narrower roles exist. The CI pipeline uses one administrator access key created in March 2024 and never rotated (EV-003). The repository requires one pull request review on main, which administrators can bypass, and its dependency alerts go to the CTO's inbox (EV-004). Customer passwords need 8 characters, lock after 5 failures, and MFA is optional for customer users. The internal admin console has its own password-only login, and its view-as-customer feature opens any tenant with no approval step or session record (EV-005). A letter from the Chief Executive Officer names the CTO as security and compliance lead and the Operations and Finance Manager as privacy lead (EV-029).

**Cloud and data.** Production runs in one cloud account and region. Storage is encrypted at rest with provider-managed keys and the load balancer requires TLS 1.2 or higher. Database point-in-time recovery and daily snapshots are each kept 7 days in the production account. Bucket versioning, object read logging, database audit logging and threat detection are off, and management events are kept for the 90-day default. Application secrets are container environment variables, and no restore job appears in the event history (EV-006). About 60% of production resources are in infrastructure code (EV-007). The database holds 45 active tenants and 2 terminated tenants whose data is still stored, about 41,000 vendor records, about 165,000 documents and about 29,000 W-9s, about 9,800 of them with a Social Security number; auto-accept is on for 31 of 45 customers (EV-008). The extraction worker sends full W-9 images and text, including TINs, to the model provider, and the full TIN is shown to every customer user. The feature was released to all customers on 2026-04-20 (EV-009). Error tracking keeps events 14 days with data scrubbing off, and some stored payloads contain W-9 text with TINs (EV-010).

**Endpoints.** The MSP reports 7 company laptops with device management, full-disk encryption, antivirus, monthly patching and a 10-minute screen lock. The contract developer's personal laptop is not enrolled (EV-011).

**Documents and statements.** The request for policies, a risk assessment, incident response and recovery plans, a customer security contact list, notice templates, a retention schedule, training records, penetration test reports, a SOC 2 report, an AI risk assessment and vendor reviews returned none (EV-012). The website says tax IDs "never leave our platform" and the product page says "99% accuracy" (EV-013). Fourteen questionnaires in 12 months were answered from a 2024 answer document that says "SOC 2 compliant" and "annual penetration test performed"; two prospects and one anchor renewal require a SOC 2 report (EV-014).

**Suppliers and contracts.** The customer DPA and security exhibit promise 72-hour incident notice, 30 days' notice of new sub-processors, deletion within 60 days, MFA, annual penetration testing and 30-day backup retention (EV-015). The published list names 4 sub-processors, each with a signed DPA. The AI model provider is not on it and has no DPA, and the contractor agreement has a confidentiality clause and no security terms (EV-016). The model provider was taken on through click-through API terms that allow 30-day retention for abuse monitoring, with production calls from 2026-04-20 (EV-017). The MSP contract has a 4-business-hour response time and no recovery, incident notice or technician change terms (EV-018). The cyber policy was bound in February 2026 with a 24x7 breach hotline and panel vendors (EV-019). Card statements and invoices show the SaaS suppliers and no payments to an audit or penetration testing firm (EV-020). The cloud provider's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 (EV-021).

**Business volume.** FY2025 receipts were about $1.1 million, about $3,000 per calendar day, and cash covers about 60 days of expenses (EV-022). There are 45 customers in Florida and 5 other southeastern states, averaging about $24,000 a year; the 2 anchor customers provide about 30% of revenue (EV-023).

**Interviews.** The CTO does security work when time allows. Engineers copy production extracts to laptops, including the contractor's personal laptop, where copies of the CI key and the email delivery API key also sit. No restore has ever been run, and the AI feature was released with no risk review or accuracy test (EV-024). Departures are announced by email, and accounts outside single sign-on are removed when someone remembers (EV-025).

**AI tools and monitoring.** Engineers and the contractor use a licensed AI coding assistant whose business terms exclude training on inputs. Staff report using public chatbots to draft emails, sales material and questionnaire answers. No approved-tools list was found (EV-026, EV-027). External uptime checks page the CTO, and the status page is hosted outside the production account (EV-028).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they enter | Chief Executive Officer | 2026-07-17 | Not established at intake; P10 treats it as unknown (AI-003) |
| SOC 2 reports from the AI model provider and the error tracking service | Operations and Finance Manager (vendor trust portals) | 2026-07-20 | Received 2026-09-01 (EV-045, EV-046); reviewed in P09 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001), revenue and cash (EV-022), customers and contract terms (EV-015, EV-023), backup settings (EV-006), infrastructure code coverage (EV-007), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-011 and the contracts in EV-015 to EV-018 |
| P04 Cloud mapping | Cloud and SaaS components (EV-003 to EV-010, EV-020) and provider assurance (EV-021) |
| P01 Risk register | Likelihood inputs from the configuration exports, the interviews (EV-024, EV-025), the statements and questionnaires (EV-013, EV-014) and the contracts |
| P03 Regulatory analysis | The obligations register (which rules apply) and every observation above, compared with the FTC guidance and the company's own commitments |
| P06 Policies | The document request response (EV-012) and the AI coding assistant terms (EV-027) |
| P07 Control assessment | Populations to test from (EV-001 to EV-003, EV-011, EV-016) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the insurance policy (EV-019) |
| P09 SOC 2 | Commitments (EV-015), questionnaires (EV-014) and vendor assurance (EV-021, EV-045, EV-046) |
| P10 AI governance | AI tools found (EV-009, EV-017, EV-026, EV-027) |

# Intake Report: Cris Santos Company | Information | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher, workforce scheduling and timekeeping platform) |
| Intake window | 2026-07-27 to 2026-08-07 |
| Collected by | IT Manager (security and compliance lead), with the Platform Engineering Lead and the COO (privacy lead) |
| Approved | CTO, 2026-09-22 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-08-10. It covers the organization, the systems that store, process or transmit customer worker data, the vendors and sub-processors that touch them, and the laws and contracts that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, scans, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement or a commitment is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-011 | Identity provider; HR information system; People Operations tickets; cloud IAM; secrets vault; SOC 2 evidence folder; source hosting and CI service; internal admin console; WSP configuration | 2026-06-30 to 2026-07-31 |
| Cloud platform and engineering | EV-012 to EV-023 | Cloud provider console and infrastructure code; logging and monitoring SaaS; backup service; engineering wiki; CI test reports; scanners; uptime and status page service | 2026-01-21 to 2026-07-31 |
| Endpoints and people | EV-024 to EV-026 | Device management and EDR consoles; recycler certificates; HR learning records | 2026-06-30 to 2026-07-31 |
| Documents and records | EV-027 to EV-035 | Company intranet; engineering ticket system; SOC 2 evidence folder; engineering wiki; HR system; CRM content library; productivity suite and website | 2025-12-15 to 2026-08-04 |
| Vendors and contracts | EV-036 to EV-042 | Finance system; identity provider app list; COO's contracts folder; public sub-processor list and notice log; cloud provider compliance portal | 2026-03-31 to 2026-08-04 |
| Business volume and data | EV-043 to EV-045 | Finance system; WSP reporting and CRM; data dictionary and DPA data exhibit | 2025-12-31 to 2026-07-31 |
| AI assistant | EV-046, EV-047 | Product release notes; WSP AI service, model provider account and engineering wiki | 2026-07-15 to 2026-07-30 |

## 3. Observations by area
**Users and access.** The identity provider holds named accounts for the 60 employees and active contractors, all with MFA. The 6 engineers with production access and the 3 super-administrators have hardware security keys (EV-001). Admin console and cloud console sessions last up to 12 hours, and no alert is set for administrator changes (EV-002). The HR system lists 60 employees and their joiners and leavers; contractors are not held there (EV-003). Leaver tickets record the identity provider disable on the last day and a manual checklist for apps outside single sign-on, and cover employees only (EV-004). Production engineer roles are read-only by default. One shared break-glass role has database write access, 2 static CI access keys are more than 1 year old with broad read and write permissions, and all 21 engineers hold write roles in staging (EV-005). The vault log records who checked out the break-glass credential, not what they ran, and has no review record (EV-006). The three quarterly access reviews on file cover the identity provider only (EV-007). Repository administrators can bypass branch protection, and push protection for secrets is off (EV-008). Long-lived cloud keys and third-party API keys sit in CI secrets with no rotation dates, and CI actions are referenced by tag (EV-009). All 10 support agents can use view-as-tenant without customer approval; the sessions are logged and no review record exists (EV-010). MFA is enforced for customer administrators and optional for workers (EV-011).

**Cloud platform and engineering.** Most production resources are in infrastructure code; 3 buckets and 2 queue policies were set by hand (EV-012). Cloud audit logs use the provider's default 90-day history with no export, object-level and database query logging are off, and the threat detection service is not enabled. Application logs are kept 30 days (EV-013). Data stores are encrypted at rest with provider-managed keys, and the listener policy allows TLS 1.2 or higher (EV-014). The database has 7-day point-in-time recovery and daily snapshots copied to a second region, all in the production account (EV-015). The only restore test on record, in January 2026, took 5 hours (EV-016). Staging is refreshed monthly from an unmasked production snapshot (EV-017). Isolation tests cover 80% of about 190 API endpoints and are not a merge gate (EV-018). The January 2026 penetration test had 2 High findings, both closed per the retest letter (EV-019). Scan findings do not block deployment and have no due dates (EV-020). Some application log messages include worker names and phone numbers (EV-021). The mobile and kiosk apps queue punches offline for up to 24 hours (EV-022). Measured availability was 99.95% over 12 months (EV-023).

**Endpoints and people.** All 66 laptops have full-disk encryption, EDR, automatic patching and remote wipe (EV-024), and retired laptops have certificates of destruction (EV-025). 2025 awareness training completion was 98%, and no secure coding course is assigned to engineers (EV-026).

**Documents and records.** The December 2025 policy set adopted for the SOC 2 Type 1 is on file. The request for a disaster recovery plan, recovery runbook, security test plan, remediation timelines, sub-processor reviews, a public statement review, an AI risk assessment and tenant deletion records returned none (EV-027). The December 2025 incident response plan states no 72-hour or 48-hour customer notice deadline and has no test record (EV-028). Two security incidents were logged in 2026, both closed with no severity or lessons-learned notes (EV-029). The SOC 2 Type 1 report as of 2026-02-28 has an unmodified opinion with 3 exceptions: the shared break-glass role, unmasked production data in staging, and no sub-processor review (EV-030). The December 2025 risk assessment did not cover staging, sub-processors or the AI assistant (EV-031). The engineering handbook has no security or privacy review step (EV-032). Sales questionnaire answers have no owner or review date, and several state that all systems get quarterly access reviews (EV-034). The security mailbox is not published on the website (EV-035).

**Vendors and contracts.** The vendor spend report shows payments to the 6 DPA sub-processors, the identity provider, the source hosting and CI service, corporate SaaS vendors, an enterprise generative AI assistant and service firms (EV-036). Four corporate SaaS apps paid for in the period are not connected to single sign-on (EV-037). The MSA and DPA promise 99.9% availability, incident notice within 72 hours (48 hours for 3 customers), 30 days' sub-processor notice and deletion within 90 days (EV-038). DPAs are signed with 5 of the 6 sub-processors; the AI model provider is on click-through API terms (EV-039). The notice adding the model provider went to customers 12 days before it began receiving data (EV-040). The cloud provider's SOC 2 report covers the period ending 2026-03-31 (EV-041). The cyber insurance policy names panel forensic firms, and no separate forensic retainer is on file (EV-042).

**Business volume and data.** Annual receipts were $28.2 million in FY2025, about $77,000 per calendar day (EV-043). About 310 customers in 46 states use the platform for about 140,000 workers, about 18,000 in Florida and about 9,500 in California (EV-044). The data dictionary lists no Social Security, health, geolocation or payment card data, and does not cover staging copies, logs, support tickets or model prompts (EV-045).

**AI assistant.** The assistant was released in beta to 40 customers on 2026-07-15, and the release notes call the shift-swap suggestions "fair and unbiased" (EV-046). Prompts include worker first names, availability, a reliability score and free-text shift notes. The zero-retention setting is on in the provider account, and summaries are shown without a check against schedule data (EV-047).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using the enterprise generative AI assistant, and whether staff use other AI tools outside single sign-on | IT Manager | 2026-08-03 | Not established at intake; P10 records it as not established |
| Written confirmation of the model provider's zero-retention terms | COO | 2026-08-04 | Not provided; carried into P01 (R-019) and the P10 conditions |
| Owners and data held in the 4 corporate SaaS apps outside single sign-on | IT Manager | 2026-08-03 | Not established at intake; carried into P01 (R-032) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue and usage (EV-043, EV-044), contract availability terms (EV-038), backups and the restore test (EV-015, EV-016), offline punch queues (EV-022), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-024 |
| P04 Cloud mapping | Cloud and SaaS components (EV-005, EV-012 to EV-015, EV-036) and provider assurance (EV-041) |
| P01 Risk register | Likelihood inputs from the configuration exports, the SOC 2 Type 1 exceptions (EV-030), the incident tickets (EV-029) and the contracts (EV-038 to EV-040) |
| P03 Gap analysis | The obligations register (which rules and commitments apply) and every observation above, compared with the FTC guidance and the company's commitments |
| P06 Policies | The December 2025 policy set (EV-027) and the incident response plan (EV-028) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-004, EV-005, EV-009) |
| P08 IR runbook | Notification duties from the obligations register; contract clocks (EV-038); insurer panel (EV-042) |
| P09 SOC 2 | The Type 1 report (EV-030) and vendor assurance on file (EV-041) |
| P10 AI governance | AI tools found (EV-036, EV-037, EV-046, EV-047) |

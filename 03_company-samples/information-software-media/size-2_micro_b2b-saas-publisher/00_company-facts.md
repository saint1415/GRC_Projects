# Scenario facts: Cris Santos Company | Information | Micro

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute, regulation, or FTC guidance page, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; the founder and Chief Executive Officer is the sole owner) |
| Business | B2B SaaS software publisher (NAICS 513210). Sells the **Vendor Compliance Platform (VCP)**, a multi-tenant SaaS service that collects and tracks subcontractor and supplier compliance documents (certificates of insurance, W-9 tax forms, business licenses, safety certifications) for mid-size property management companies and general contractors |
| Location | Florida. One small leased office; 3 of 7 employees work remotely, all in Florida. One part-time contract developer works remotely from another U.S. state. No offshore staff, contractors, or hosting |
| Workforce | 7 employees: Founder and Chief Executive Officer, Chief Technology Officer (CTO), Senior Software Engineer, Software Engineer, Customer Success Manager, Account Executive, Operations and Finance Manager. Plus 1 part-time contract developer (about 15 hours a week) |
| Customers | 45 customer organizations (mid-size property management companies and general contractors, typically 200 to 2,000 employees) in Florida and 5 other southeastern states. About 900 customer users. Two anchor customers provide about 30% of revenue (EV-023) |
| Data held for customers | About 41,000 vendor records with about 52,000 vendor contacts (name, business email, phone, address); about 165,000 stored documents. Of about 29,000 W-9 forms, about 9,800 show a **Social Security number** as the taxpayer identification number (sole proprietors and single-member LLCs); about 4,100 of those individuals have Florida addresses, and the rest live in about 20 other states. Certificates of insurance show insurer names, policy numbers, limits, and dates. **No** payment card data, bank account data, or health data (EV-008) |
| Revenue | About $1.1 million in annual receipts (fictional), about $3,000 per calendar day (EV-022). SBA-small (standard $47.0 million for NAICS 513210) |
| Role under privacy and breach laws | For customer vendor data: a **service provider** acting on customers' instructions under the DPA, and a **third-party agent** under Fla. Stat. 501.171(1)(h). The customers own the data. For its own employee data, customer user accounts, and sales contacts: the business that owns the data. Recorded in the intake obligations register (FL-501.171) |
| Customer commitments (MSA, DPA, security exhibit) | Notice of a security incident affecting customer data without undue delay and within 72 hours of confirmation; a published sub-processor list with 30 days' notice of new sub-processors; deletion of customer data within 60 days after termination; customer data used only to provide the service; security exhibit promising encryption in transit and at rest, MFA for personnel access, **annual third-party penetration testing**, and **daily backups retained 30 days**; 99.5% monthly uptime target (service credits for the 2 anchor customers only) (EV-015) |
| Public statements | Website security page: "bank-level 256-bit encryption" and "your vendors' tax IDs are encrypted and never leave our platform." Product page: "AI reads certificates with 99% accuracy" (EV-013) |
| Assurance | None yet. Two mid-market prospects require a SOC 2 report before signing, and one anchor customer's renewal (2027-06-30) requires one (EV-014). Target: **SOC 2 Type 1** (Security and Confidentiality) as of 2027-03-31, then a Type 2 |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): HIPAA and the FTC Health Breach Notification Rule (no health data); PCI DSS (customers pay through a payment processor's hosted page; no card data held); COPPA (B2B service, not directed to children); FCC CPNI rules (not a carrier); FedRAMP (no federal customers); SEC disclosure rules (private); bank service provider notification rules (no banking customers); CCPA (not a "business": revenue far below the threshold and no selling or sharing; no California customers); DOJ Data Security Program and PADFA (applicability checks in P03 section 1) |
| State law approach | Florida law is cited where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171). Vendors live in about 21 states, so other state law is treated generically: "each state where affected individuals reside," with Florida as the worked example |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Founder and Chief Executive Officer (owner) | Accepts Moderate risk and approves treatment plans for High and Very High risks; approves the budget, policies, these deliverables, and every public security statement |
| Chief Technology Officer (CTO) | System owner of the VCP and designated **security and compliance lead** (part-time duties). Runs the cloud account and CI/CD; accepts Low risk; maintains the SSP, risk register, and policy set |
| Operations and Finance Manager | Designated **privacy lead**. Contracts, DPAs, sub-processor list, cyber insurance, onboarding and offboarding checklists, training records |
| Senior Software Engineer | Second cloud administrator; backup technical lead for incidents; backups and deployments |
| Software Engineer | Application development, code review |
| Customer Success Manager | Customer onboarding and support; uses the internal admin console; customer communications during incidents |
| Account Executive | Sales; answers customer security questionnaires (from 2026-09-15 only with CTO approval) |
| Contract developer (part-time, U.S.-based) | Feature development under a contractor agreement with a confidentiality clause and no security terms |
| Managed service provider (MSP) | Manages the 7 company laptops (device management, disk encryption, antivirus, patching), administers the productivity suite (users, MFA policy, email security), and runs the help desk. Holds 2 global administrator accounts in the suite. No access to the production cloud account |
| Outside counsel (as needed) | Wrote the MSA and DPA templates in 2024; advises on breach notification together with the cyber insurer's panel counsel |
| Independent security consultant | Performed the P07 control assessment under a fixed-fee engagement; not involved in the risk or gap analysis or in operating any control; will not be the SOC 2 auditor |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds customer vendor data? | Notes |
|---|---|---|---|---|
| SYS-01 | VCP production environment: web application, API, and background workers (document processing, AI extraction, reminder jobs) on a managed container service; managed relational database (multi-tenant); object storage bucket for uploaded documents; provider-managed encryption keys; internal admin console | Public cloud, one account, one region (vendor-agnostic) | Yes | Tenant isolation is enforced in application code (every query filtered by tenant ID). Database point-in-time recovery for 7 days and daily snapshots kept 7 days, both in the same account. Document bucket versioning is off. Application secrets are stored as container environment variables (EV-005; EV-006) |
| SYS-02 | Source repository and CI/CD pipeline | SaaS | No (holds secrets) | Deploys to production with **one long-lived static cloud access key with administrator rights**, created in March 2024 and never rotated (EV-003; EV-004) |
| SYS-03 | Productivity suite (email, files, chat, calendar) with its identity service | SaaS, administered by the MSP | Incidental (email attachments) | Its identity service is the single sign-on for the repository, support desk, and CRM. The cloud console uses separate per-person cloud accounts with MFA (EV-002; EV-003) |
| SYS-04 | Transactional email delivery service | SaaS | Yes (vendor contact names and emails) | Sends document expiry reminders and upload links to vendors |
| SYS-05 | Error tracking and log management | SaaS | Yes (incidental) | 14-day retention. Some error payloads contain text extracted from W-9s, including TINs (EV-010) |
| SYS-06 | Generative AI model provider (API) | SaaS | Yes | Used by the AI document extraction feature (P10) since 2026-04-20, under click-through API terms (EV-017) |
| SYS-07 | Business SaaS: support desk, CRM, accounting, and the payment processor for customer billing | SaaS | Incidental (support tickets with screenshots) | The payment processor hosts the payment page; the company holds no card data (EV-023) |
| SYS-08 | Endpoints: 7 company laptops; the contract developer's personal laptop | Company laptops MSP-managed; the contractor's laptop unmanaged | Incidental (cached; occasional database extracts) | Company laptops have device management, full-disk encryption, and antivirus. The contractor's laptop has none of these under company control (EV-011) |

**Sub-processors listed in the published DPA list (4):** the cloud provider (SYS-01), the email delivery service (SYS-04), the error tracking and log management service (SYS-05), and the support desk SaaS (SYS-07). The AI model provider (SYS-06) has processed customer data since 2026-04-20 but is **not on the list** (EV-016; EV-017).

**SSP system (P02):** the *Vendor Compliance Platform (VCP)*: the multi-tenant production environment (SYS-01) and the components that build, operate, and support it (SYS-02, the SYS-03 identity service, SYS-05), with interfaces to SYS-04 and SYS-06, administered from SYS-08 laptops.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). For a 7-person SaaS company the systems of record are the cloud console, the repository host, the productivity suite admin console (exported by the MSP), the MSP's device reports, the payroll service, the accounting and billing SaaS, the contracts folder, the company website, and short interviews. Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against FTC Act Section 5 and the company's own commitments** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Gap analysis against FTC Act Section 5 data security expectations (FTC business guidance) and the company's own security representations and DPA commitments. The SOC 2 criteria are mapped in each row and assessed criterion by criterion in P09. CCPA and the DOJ Data Security Program are applicability checks only |
| P08 incident | Cloud credential compromise exposing customer data (registry default, kept because it fits): the long-lived CI/CD cloud key is stolen from the contractor's personal laptop by information-stealing malware and used to download the document bucket (including W-9s with SSNs) and copy a database snapshot. The MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | SOC 2 Type 1 readiness self-assessment for Security plus Confidentiality (the second category customers ask about, because the platform stores vendors' tax forms). Evidence inventory, plus reviews of key vendors' assurance reports |
| P10 AI | Generative AI feature embedded in the product (registry default, refined): AI document extraction that reads certificates of insurance and W-9s, fills in fields, and drafts a compliance summary for the customer's reviewer |
| Cloud | SaaS plus a single cloud workload: the company's own production account (SYS-01). Vendor-agnostic; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| Primary system | "Multi-tenant SaaS production platform" (registry default) is the VCP |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-04-20 | AI document extraction released to all customers |
| 2026-07-13 to 2026-07-24 | Intake: evidence requests, exports from the cloud console, the repository host, the suite (through the MSP), the MSP's device reports, the payroll and accounting SaaS, the contracts folder, inventories, obligations register |
| 2026-07-27 to 2026-08-07 | BIA interviews, risk assessment and gap analysis (CTO with the Operations and Finance Manager; MSP lead technician for laptops and the suite) |
| 2026-08-10 to 2026-08-21 | Policies drafted from the gaps |
| 2026-08-24 to 2026-08-26 | Control assessment (independent security consultant): operating tests of controls already in place; design review of the draft policies |
| 2026-08-31 to 2026-09-04 | SOC 2 readiness self-assessment and AI risk assessment |
| 2026-09-15 | Deliverables and policies approved by the Chief Executive Officer |
| 2026-11-12 | First incident response tabletop exercise (P08 scenario) |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |
| 2027-03-31 | Target SOC 2 Type 1 report date ("as of" date); report expected by 2027-05-31 |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6. Facts drawn from the company's records cite the evidence register ID they rest on.

| Topic | Added fact | Used in |
|---|---|---|
| Registry defaults | The primary system, P08 incident, and P10 use case are the registry defaults. The AI use case was narrowed to document extraction because that is the generative AI feature this product actually has | All |
| Customer sign-in | Customer passwords need 8 characters with no breached-password check; accounts lock for 15 minutes after 5 failed attempts; 3 customers sign in through their own single sign-on (EV-005; EV-035) | P02, P03 |
| Former Customer Success Manager | Left in March 2026; the suite account was disabled on the last day, but the admin console and support desk accounts stayed active until P07 found them; disabled 2026-08-26. The admin console keeps no sign-in history (EV-002; EV-AC-2; EV-AU-2) | P01, P07 |
| Account Executive | Moved from customer support to sales in 2025 and kept an admin console account until 2026-08-26 (EV-AC-2) | P07 |
| Root account | The cloud root password is in a team vault entry that all engineers and the contractor can open; its MFA device is the CTO's personal phone; unchanged since 2024 (found in P07; EV-IA-5, EV-IA-2(1)) | P01 R-025, P07 |
| Contractor's laptop | Held the CI key and 3 production extracts with vendor tax IDs, the newest from 2026-07-14; the extracts were deleted 2026-08-28 and the deletion confirmed in writing (EV-SA-3(2); EV-044) | P07, P08 |
| Dependency alerts | 14 High-severity dependency alerts older than 30 days at fieldwork (EV-034) | P01, P03, P07 |
| Error tracking | 14-day retention; offers data scrubbing that is not turned on (EV-010) | P04, P09 |
| Model provider terms | Standard API terms say inputs are not used for training but allow retention for up to 30 days for abuse monitoring; its SOC 2 Type 2 report (Security) does not cover the zero-retention option (EV-017; EV-045) | P03, P09, P10 |
| AI auto-accept | A customer setting that saves extracted fields without review; turned on by 31 of 45 customers (EV-008) | P10 |
| AI test results | 400-document test set (2026-09-02): 93.5% field-level accuracy; 7 of 250 certificates with a critical error; phone photos and handwritten forms much worse (13.9% versus 0.9%) (EV-047) | P03 G-034, P10 |
| AI coding assistant | The company licenses a business AI coding assistant with no training on inputs, used by the CTO, the engineers, and the contractor (EV-026; EV-027) | P06 POL-04 4.7, P10 AI-002 |
| Uptime | External monitor: 99.94% over August 2025 to July 2026; lowest month 99.71% (EV-043) | P03 G-041 |
| Questionnaires | 14 customer and prospect security questionnaires answered in the last 12 months from a 2024 answer document (EV-014) | P03 G-040 |
| MSP contract | Covers laptops, the productivity suite, and the help desk, with a 4-business-hour response time, no recovery commitment, no security incident notice term, and no notice of technician changes. The MSP holds 2 suite global administrator accounts (EV-018; EV-002) | P04, P05, P09 V-04 |
| Finances and payroll | A cash reserve covers about 60 days of expenses; payroll runs biweekly through an outside payroll service (EV-022; EV-001) | P05 |
| SOC 2 plan | CPA firm to be engaged by 2026-12-15; a compliance automation tool for evidence collection from 2026-11; readiness check with the CPA firm 2027-02-28 | P01, P09 |

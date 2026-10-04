# Access Control Policy (with Program Governance and Acceptable Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | CTO (security and compliance lead) |
| Approved by | Chief Executive Officer, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-15), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, PL-2, RA-3, CA-2, CA-8, SA-9, PS-7, PS-8. Part B: AC-1, AC-2, AC-3, AC-6, AC-17, IA-2, IA-2(1), IA-5, PS-4, AU-6. Part C: PL-4, AT-2, AT-3 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.OC-03, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02 |
| Regulatory drivers | N51-R01 (FTC Act Section 5: reasonable security and accurate representations); Fla. Stat. 501.171(2) (reasonable measures); customer DPA and security exhibit; SOC 2 CC1 to CC6 |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people and systems reach customer data and production, and only as far as their job requires, and tell everyone who works for the company how to use company systems.

## 2. Scope
All employees, the contract developer, and anyone else given access to company systems, including MSP staff. It covers every system that stores or processes customer data or company data: the production cloud account, the repository and CI/CD pipeline, the productivity suite, the internal admin console, the SaaS tools in `../00_company-facts.md` section 3, and every laptop used for company work.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Executive Officer | Approves policies, the security budget, and every public security statement; accepts Moderate risk |
| CTO | Security and compliance lead; runs this policy; grants cloud, repository, and admin console access; reviews accounts and logs |
| Operations and Finance Manager | Privacy lead; runs onboarding and offboarding checklists; keeps contracts and training records |
| MSP | Creates and disables suite accounts on request; enforces suite MFA; manages laptops |
| Everyone | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security and privacy leads.** The CTO is the security and compliance lead and the Operations and Finance Manager is the privacy lead. The Chief Executive Officer must record both designations in writing and update them within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The CTO must update the risk assessment every July, and after any major change such as a new sub-processor, a new AI feature, or a new type of customer data, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The CTO may accept Low and Very Low risks. Only the Chief Executive Officer may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Chief Executive Officer. (PM-9; GV.RM-01)

A.4 **Accurate statements.** No one may publish, send, or sign a security, privacy, or AI performance statement (website, product page, sales material, questionnaire answer, contract exhibit, or release note) unless the CTO has confirmed it is true today and the Chief Executive Officer has approved it. Questionnaires are answered only from the approved answer library. The CTO must review all public statements and the answer library every quarter. (PL-2; GV.OC-03; FTC Act Section 5 deception)

A.5 **No contract, no customer data.** No vendor or contractor may receive customer data, including in a trial, until a written agreement with security and confidentiality terms is signed, the vendor is on the published sub-processor list where the DPA requires it, and customers have had 30 days' notice. The Operations and Finance Manager keeps the vendor file and reviews each sub-processor's SOC 2 report or questionnaire every year. (SA-9; PS-7; GV.SC-05)

A.6 **Independent checks.** Security controls must be assessed at least once a year by someone who does not operate them, and the production platform must have an external penetration test at least once a year, as the security exhibit promises. (CA-2; CA-8; ID.IM-01)

A.7 **Records.** Policies, risk assessments, assessment reports, incident records, vendor reviews, training records, and access reviews must be kept for at least 3 years, or longer where a contract or law requires. (PL-2; GV.PO-02)

A.8 **Policy review and access to policies.** The CTO must review this policy set every September and after an incident or major change, and keep the current version in the shared policy folder where everyone can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

A.10 **Sanctions.** Breaking a security rule leads to coaching, a written warning, or termination of employment or contract, in proportion to intent and harm. The Chief Executive Officer decides. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

### Part B. Access control
B.1 **Named accounts only.** Every person must have their own account in every system. Shared accounts are not allowed, except the cloud root account and one sealed emergency administrator account, which only the Chief Executive Officer and CTO may open and which must alert on use. (IA-2; AC-2; PR.AA-01)

B.2 **Single sign-on first.** Every system that supports it must use the suite's single sign-on, including the internal admin console and the support desk, so that disabling one account removes all access. (AC-2; IA-2)

B.3 **MFA.** MFA is required for every staff and contractor account, every administrator account (including the MSP's), and every customer administrator account. The CTO, the engineers, and the root account must use hardware security keys. (IA-2(1); PR.AA-03)

B.4 **Least privilege in production.** Day-to-day work in the cloud account uses read-only or deploy-only roles. Administrator rights are used only through a break-glass role limited to the CTO and the Senior Software Engineer, and each use must be logged and explained in the incident or change ticket. The contract developer gets repository access and a deploy-only role, never administrator rights. (AC-6; PR.AA-05)

B.5 **No long-lived keys.** CI/CD and other automated jobs must use short-lived, federated credentials scoped to their task. Long-lived access keys are not allowed. Application secrets must be kept in the provider's secrets manager and rotated at least once a year and whenever someone with access leaves. (IA-5; PR.AA-01)

B.6 **Access to customer tenants.** Staff may open a customer's tenant only to work an open support ticket, through the ticket-linked, time-limited view-as-customer feature. Each session is logged and reviewed monthly. (AC-3; AC-6; AU-6)

B.7 **Onboarding.** The Operations and Finance Manager must approve each person's access on the onboarding checklist before it is granted, based on their role. (AC-2; PR.AA-05)

B.8 **Offboarding.** On or before a person's last day, the Operations and Finance Manager must complete the offboarding checklist: ask the MSP to disable the suite account; disable or remove cloud, repository, admin console, support desk, and CRM accounts that sit outside single sign-on; collect the laptop; and rotate any secret the person could read. For an involuntary departure, access is removed before the person is told. (PS-4; AC-2)

B.9 **Monthly account reconciliation.** Each month the CTO must compare the user lists of the cloud account, repository, admin console, support desk, and suite (including the MSP's administrator accounts) with the staff and contractor roster, and remove anything that does not match. Every quarter the CTO must confirm each person's cloud and repository role still fits their job. (AC-2; AC-6)

B.10 **Remote work and devices.** Company work, including all access to customer data or production, must be done only on a company laptop managed by the MSP. Personal devices may be used only for suite email and chat through the suite's mobile app. (AC-17; PR.AA-05)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Staff may look at customer data only to do their job.

C.2 Customer data, credentials, and secrets must never be put in personal email, personal cloud storage, personal messaging apps, public code repositories, or any AI tool that is not on the approved list in POL-04 section 4.7. (PL-4; PR.AT-01)

C.3 Production data must never be copied to a laptop. Use the synthetic test data set for development and debugging. (PL-4; SA-3(2))

C.4 Lock your laptop when you step away, keep the MSP's security software running, and never share passwords, MFA codes, or security keys, including with the MSP. (PL-4)

C.5 Everyone must complete security awareness training at hire and every year and take part in phishing simulations. The CTO, the engineers, and the contract developer must also complete secure coding training every year. (AT-2; AT-3; PR.AT-01; PR.AT-02)

C.6 Report suspected incidents at once under POL-03 section 4.2, including your own mistakes. (IR-6)

C.7 Sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.10. The CTO checks compliance through the monthly reconciliation (B.9), the log review in POL-03, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and offboarding checklists; approved questionnaire answer library; P01 risk register; P02 SSP control statements AC-2, AC-6, IA-2(1), IA-5, PS-4, PS-7

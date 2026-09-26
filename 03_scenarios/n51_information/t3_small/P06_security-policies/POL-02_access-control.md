# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | Chief Executive Officer |
| Effective date | 2026-09-22 (replaces the December 2025 policy adopted for the SOC 2 Type 1) |
| Review cycle | Annually (next review 2027-09-22), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(9), AC-7, AC-11, AC-12, AU-1, AU-2, AU-6, AU-11, SI-4, IA-1, IA-2, IA-2(1), IA-2(2), IA-4, IA-5, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, DE.CM-01, DE.CM-03, DE.CM-09 |
| Also supports | SOC 2 CC6.1 to CC6.3, CC7.2; FTC Act Section 5 reasonable security (N51-R01); DPA access commitments |

## 1. Purpose
Make sure only authorized people and services can reach customer data and company systems, only to the extent their job requires, and that every access to customer data can be traced to a person.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors), whether they work in the Florida office or remotely. Covers all company systems and data, including the Workforce Scheduling Platform (WSP), the staging environment, the source repository and CI/CD pipeline, corporate SaaS, laptops, and systems that sub-processors operate for the company. It applies to customer data (customer worker data the company processes as a service provider under the DPA) and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| System owners (CTO for the WSP; IT Manager for corporate SaaS) | Approve access and complete quarterly access reviews |
| People Operations Manager | Opens onboarding, transfer, and termination tickets on or before the effective date |
| IT Manager | Runs the identity provider; provisions and removes workforce access |
| Platform Engineering Lead | Cloud roles, just-in-time access, CI/CD credentials, and logging |
| Customer Support Manager | Approves and reviews support access to customer tenants |
| Workforce | Protect credentials; never share accounts or keys |

## 4. Policy statements
4.1 Every person must have a unique account, and every workload or pipeline must have its own identity. Shared or generic accounts are prohibited. The shared break-glass database role is a documented exception (approved by the Chief Executive Officer, expires 2026-10-23) until named just-in-time access replaces it. (AC-2; IA-2; IA-4; PR.AA-01)
4.2 Access must be role-based, least privilege, and approved by the system owner before it is granted. Engineers get read-only production roles by default. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for every workforce sign-in through the identity provider. Engineers with production access and identity provider administrators must use phishing-resistant hardware security keys. MFA must be enforced for customer administrator accounts. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Privileged production access.** Write access to production data or infrastructure must be requested for a named person, approved by a second engineer or the CTO, limited to 1 hour, and recorded (session recording for database sessions). No one may hold standing write access to customer data. (AC-2; AC-6; AC-6(9); PR.AA-05)
4.5 **Staff access to customer tenants.** Support and engineering staff may open a customer tenant ("view as tenant") only for a ticket, with the customer administrator's approval recorded in the ticket, for no more than 24 hours. Sessions are logged and reviewed monthly. (AC-3; AC-6; AU-6)
4.6 **Joiners, movers, and leavers.** Access is granted only from a People Operations ticket. Access must be disabled in the identity provider on the last day, or immediately for involuntary terminations. Systems not connected to single sign-on must be removed the same day, with evidence in the ticket. Company systems must use single sign-on; local accounts outside the identity provider are not allowed. (AC-2; PS-4; PS-7)
4.7 **Access reviews.** System owners must review access every quarter for the identity provider, production and staging cloud roles, database users, the source repository, the admin console, and corporate SaaS. Findings must be fixed within 10 business days. (AC-2; AC-6; PR.AA-05)
4.8 **Machine credentials and secrets.** Long-lived static cloud access keys are not allowed; CI/CD must use short-lived federated credentials scoped to each pipeline. Third-party API keys must be kept in the secrets manager, rotated at least annually and at once when exposure is suspected, and never committed to source code. Secret scanning with push protection must be on for all repositories. (IA-5; IA-4; PR.AA-01)
4.9 **Logging and review.** The following must be logged and kept for at least 1 year in a log archive account that production administrators cannot change: cloud management events, object access to storage holding customer data, database sessions and privileged queries, identity provider events, and admin console events. The IT Manager must review privileged activity weekly and view-as-tenant sessions monthly. Alerts must be set for unusual cloud API activity, bulk reads of customer data, and snapshot copies or sharing. (AU-2; AU-6; AU-11; AC-6(9); SI-4; DE.CM-01; DE.CM-03; DE.CM-09)
4.10 Workforce accounts lock after 10 failed sign-in attempts. Laptops lock after 5 minutes idle. Admin console and cloud console sessions must require re-authentication after 1 hour. (AC-7; AC-11; AC-12)
4.11 **Emergency access.** Two sealed emergency cloud accounts protected by hardware keys may be used only when the identity provider is unavailable. They must be tested quarterly, and every use is reviewed by the IT Manager and the CTO. (AC-2)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the SOC 2 examination (P09), and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved at the level set in POL-01 section 4.4, recorded in the risk register (P01), and expire within 12 months.

## 7. Related documents
POL-01; POL-03; POL-05; engineering handbook (access procedures); P02 control statements AC-2, AC-6, IA-2, IA-5, AU-6; P04 cloud control map

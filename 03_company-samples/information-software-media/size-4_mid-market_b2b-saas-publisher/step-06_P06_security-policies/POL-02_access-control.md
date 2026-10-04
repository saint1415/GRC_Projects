# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Director of IT (workforce identity) with the Director of Security (privileged and machine access) |
| Approved by | Chief Technology Officer |
| Approval date | 2026-09-29 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(1), AC-2(3), AC-3, AC-5, AC-6, AC-6(1), AC-6(2), AC-6(5), AC-6(9), AC-17, IA-2, IA-2(1), IA-2(2), IA-4, IA-5, IA-5(7), IA-8, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.IR-01, GV.RR-04 |
| Regulatory drivers | N51-R01 (FTC Start with Security lessons 2, 3, 5, 6); HIPAA as a business associate, 45 CFR 164.308(a)(3)-(4), 164.312(a), 164.312(d); SOC 2 CC6.1 to CC6.3 (contract) |
| Supporting standards | STD-06 Authenticator, secrets, and privileged access standard |

## 1. Purpose
Make sure that only the right people and workloads can reach company systems and customer data, with the least access they need, and that every access to customer data can be attributed and reviewed.

## 2. Scope
Workforce accounts (employees and contractors), machine identities (workload roles, CI/CD credentials, API keys), customer agent and administrator accounts on the platform, and support access to customer tenants. It covers the CEP, the healthcare cell, the data warehouse, source hosting and CI/CD, the identity provider, and corporate SaaS.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of IT | Identity provider, joiner-mover-leaver automation, quarterly workforce access reviews |
| Director of Security | Privileged access design, break-glass accounts, machine credential standard, review of support view and just-in-time logs |
| VP Platform Engineering | Cloud roles, just-in-time access tool, workload identities |
| VP Engineering | Tenant isolation and platform authorization design |
| VP Customer Support | Support view use and monthly session review |
| VP People | Timely HR entries for hires, transfers, and terminations |
| Managers and system owners | Approve access requests and confirm access in reviews |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic workforce accounts are prohibited, except sealed break-glass accounts under 4.9. (IA-2; IA-4; 164.312(a)(2)(i))
4.2 Access must be granted on least privilege and need to know, requested through the identity provider, and approved by the system owner. Access to the healthcare cell must also be approved by the VP Platform Engineering. (AC-2; AC-6; 164.308(a)(4)(ii)(B))
4.3 MFA is required for all workforce access. **Phishing-resistant authenticators (security keys) are required** for production, the healthcare cell, cloud administration, the identity provider administration console, and source hosting administration. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d))
4.4 **Production and healthcare cell access is just-in-time.** Write or data access must be requested through the just-in-time tool, approved by the on-call lead, limited to 1 hour per session, and logged. No standing administrator roles are permitted in any account that holds customer data after 2026-12-31. (AC-6(2); AC-2; PR.AA-05)
4.5 **Machine credentials.** Workloads and pipelines must use short-lived, federated credentials. Long-lived cloud access keys are prohibited. Any remaining key must be listed in the key inventory with an owner and a removal date, stored in the secrets manager, and rotated at least every 90 days until removed. (IA-5; IA-5(7); PR.AA-01)
4.6 Joiners, movers, and leavers must flow from the HR system. Access must be removed within 4 hours of a termination being entered, and HR must enter terminations the same day. Transfers must remove access that the new role does not need. Accounts outside single sign-on are prohibited for source hosting and must be justified for any other system. (PS-4; PS-5; AC-2(1); 164.308(a)(3)(ii)(C))
4.7 **Access reviews** must be performed quarterly for identity provider groups, cloud roles in every account, database and search users, the data warehouse, source hosting, and the admin console. The GRC Manager tracks completion; a missed review is reported to the CTO. (AC-2; 164.308(a)(4)(ii)(C))
4.8 **Support access to customer tenants** (support view) requires the customer's approval for each session on all plans from 2026-12-31, a linked ticket, and a time limit. The VP Customer Support must review 100% of sessions on healthcare tenants and a monthly sample on other tenants. (AC-6(9); AU-6; 164.308(a)(3)(ii)(A))
4.9 Break-glass accounts for the cloud organization and the identity provider must use hardware security keys, be sealed, alert the security team when used, and be tested each quarter. (AC-6(5); 164.312(a)(2)(ii))
4.10 Tenant isolation must be enforced in at least two independent layers for customer data stores (application and database or service credentials) by 2027-03-31, and verified by automated cross-tenant tests on every release. (AC-3; SC-4; PR.IR-01; 164.312(a))
4.11 Remote access to company systems is allowed only through single sign-on from managed devices or company-managed virtual desktops. Contractors may not access production or customer data unless the CTO approves it in writing. (AC-17; AC-20)
4.12 Customer administrators must be offered MFA and single sign-on. MFA is enforced for customer administrators and will be enforced by default for agents on Enterprise and healthcare tenants by 2027-03-31. (IA-8; PR.AA-03)
4.13 Sessions must time out: workforce sessions per the identity provider standard; agent sessions after 30 minutes of inactivity by default. (AC-12; 164.312(a)(2)(iii))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through quarterly access reviews, the independent assessment (P07), and the SOC 2 examination.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may allow a long-lived key with access to customer data beyond 90 days.

## 7. Related documents
POL-01; STD-06; System Security Plan (P02) section 11; P04 cloud architecture; P08 runbooks (credential revocation steps)

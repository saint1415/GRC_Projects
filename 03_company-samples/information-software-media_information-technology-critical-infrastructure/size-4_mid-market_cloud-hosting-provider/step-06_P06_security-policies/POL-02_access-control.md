# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Director of Cloud Operations (workforce identity), with the Security Engineering Lead (privileged access) |
| Approved by | Chief Technology Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-17, IA-1, IA-2, IA-4, IA-5, IA-8, IA-12, PS-4, PS-5, MA-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.IR-01 |
| Regulatory drivers | C-IT-R01 (Rev5 Class C AC and IA controls; SCG rules); C-IT-R05 (12 CFR 53.4) |
| Supporting standards | STD-02 Privileged access and authenticator standard |

## 1. Purpose
Make sure only authorized people and services can reach customer data and the systems that control it, with the least privilege they need, and that every action can be traced to a person.

## 2. Scope
Workforce, contractor, vendor, and service identities in the identity provider, the cloud landing zone, the code repository and pipeline, PAM, hypervisor managers and BMCs, network devices, the RMM tool, the backup platform, and IT service management. Customer accounts in the portal are covered by section 4.12 and 4.13.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Cloud Operations | Identity provider, cloud federation, permission sets, access reviews for cloud accounts |
| Security Engineering Lead | PAM, just-in-time elevation, machine credential inventory, STD-02 |
| VP Platform Engineering | Hypervisor manager, BMC, and network device access |
| Director of Managed Services | RMM accounts and script approvals |
| HR Director | Starter, mover, and leaver events that drive account changes |
| Managers | Approve access for their staff; complete access reviews on time |

## 4. Policy statements
4.1 **Unique identities.** Every person must use a unique, named account. Shared or group accounts are prohibited except documented break-glass accounts, which must be sealed, monitored, and tested quarterly. (AC-2; IA-2; IA-4; PR.AA-01; C-IT-R01)
4.2 **Phishing-resistant MFA.** All workforce sign-ins must use the identity provider with a phishing-resistant hardware authenticator. Local accounts on hypervisor managers, BMCs, and network devices are prohibited except break-glass accounts. (IA-2; IA-2(1); IA-2(2); PR.AA-03; C-IT-R01)
4.3 **Privileged access through PAM.** Administrative access to hypervisor managers, BMCs, management networks, and cloud production accounts must go through PAM with just-in-time elevation, approval for standing roles, and session recording, in both partitions and at all three data centers. (AC-6; AC-17; AU-12; PR.AA-05; C-IT-R01)
4.4 **Least privilege.** Access must be limited to what the role needs. Privileged roles must be separate from everyday accounts, and production changes must go through the pipeline, never by direct access, except approved emergency changes. (AC-6; AC-6(2); AC-5; CM-5; PR.AA-05; C-IT-R01)
4.5 **Access reviews.** Managers must review privileged access in both partitions every quarter and all other access every 6 months. Unconfirmed access must be removed within 5 business days of the review. (AC-2; AC-6(7); PR.AA-05; C-IT-R01)
4.6 **Leavers and movers.** The identity provider must disable a leaver's access the same day HR records the departure. Any account outside the identity provider must be removed within 1 business day. Transfers trigger a review of prior access within 5 business days. (PS-4; PS-5; AC-2; PR.AA-05; C-IT-R01)
4.7 **Inactive accounts.** Workforce accounts inactive for 35 days must be disabled automatically. (AC-2(3); PR.AA-01; C-IT-R01)
4.8 **Machine credentials.** Every service account, API key, and deploy token must be in the secrets inventory with an owner and must expire within 90 days, or be replaced by short-lived workload credentials. Credentials that can act on more than one cluster must be scoped per cluster and per job. (IA-5; AC-6; CM-5; PR.AA-01; C-IT-R01)
4.9 **Remote management tools.** The RMM tool must use named accounts only, restricted to company devices. Any script or action that targets more than one customer needs approval by a second engineer, and engineers may reach only the customers assigned to them. The RMM tool must never connect to Government Cloud tenants. (AC-2(9); AC-17; AC-6; PR.AA-05; C-IT-R05 (12 CFR 53.4))
4.10 **Government partition access.** Only U.S. persons who passed the government-access screening may hold roles in the government partition or enter government cages. (PS-3; AC-3; PR.AA-02; C-IT-R01)
4.11 **Vendor access.** Vendor maintenance and support sessions must go through PAM with approval for each session and recording. Standing vendor remote access tools are prohibited. (MA-4; AC-17; PR.AA-05; C-IT-R01)
4.12 **Customer administrator MFA.** Customer administrator accounts in the government partition must use MFA. In the commercial partition, MFA must be required for customer administrators by 2027-03-31 and offered to every user. (IA-8; IA-2; PR.AA-03; C-IT-R01 (SCG-CSO-SDF))
4.13 **Customer account recovery.** The NOC must not reset a customer's MFA or password on a call alone. Resets need a callback to the registered number and approval by a second customer administrator. (IA-12; IA-5; PR.AA-02; C-IT-R01)
4.14 **Lockout and sessions.** Accounts must lock after repeated failed sign-ins (10 in the identity provider, 5 in PAM), and sessions must end after the idle times in STD-02. (AC-7; AC-12; PR.AA-03; C-IT-R01)

## 5. Compliance and enforcement
P07 tests these statements each year. Quarterly access review completion and PAM coverage are reported to the CTO. Violations are handled under POL-01 section 4.15.

## 6. Exceptions
Through POL-01 section 4.8. Known exceptions at approval: DC-1 clusters A and B local accounts until federation (due 2026-12-31); commercial customer administrator MFA until 2027-03-31.

## 7. Related documents
POL-01; STD-02; System Security Plan (P02); risk register (P01 R-001, R-002, R-003, R-007, R-009, R-026)

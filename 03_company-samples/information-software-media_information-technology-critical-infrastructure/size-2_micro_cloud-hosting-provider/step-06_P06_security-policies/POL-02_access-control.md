# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (managed cloud hosting provider) |
| Policy ID | POL-02 |
| Owner | Operations Manager (Compliance Coordinator), with the Lead Systems Engineer (Information Security Lead) for technical content |
| Approved by | Owner, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually each September (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, CA-2, SI-12. Part B: AC-1, AC-2, AC-3, AC-5, AC-6, AC-17, IA-2, IA-2(1), IA-5, IA-8, PS-4. Part C: PL-4, AT-2, AT-3, AC-11 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.RA-01, ID.IM-01, PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02 |
| Regulatory drivers | Interagency Guidelines II.A, III.A, III.B, III.C.1.a, III.C.1.e, III.C.2, III.C.3, III.D, III.F (bank contracts); Fla. Stat. 501.171(2) |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people and processes reach the tools that control customer systems, and only as far as their job requires, and tell the workforce how to use company systems. The company's tools reach about 260 customer VMs and about 310 customer servers, including two banks' systems, so one shared or stolen credential can harm every customer at once. Most rules in Part B exist to break that concentration.

## 2. Scope
All workforce members: the Owner, employees, and any contractor. It covers every company system (SYS-01 to SYS-11 in the scenario facts), including the SaaS tools, the cloud tenant, and the management interfaces at DC-1, and every account that can act on a customer VM or server. It also covers access by vendors and the MDR provider to those systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves this policy and the security budget; accepts Moderate risks and approves treatment plans for High and Very High risks; holds the sealed break-glass credentials; approves exceptions above Low risk |
| Lead Systems Engineer (Information Security Lead) | Runs the security program day to day; sets up and removes administrator access; owns MFA, the VPN, the identity provider, and the MDR relationship; quarterly privilege review |
| Operations Manager (Compliance Coordinator) | Keeps policies, training records, vendor contracts, and the bank service register; requests access at hire and removal at departure; runs the monthly account reconciliation. Does not approve their own access |
| Systems Engineers and Support Engineers | Use only their own named accounts; follow Part C; report problems within 1 hour (POL-03) |
| MDR provider | Monitors and contains threats under its contract; uses named analyst accounts; changes automated actions only with the company's approval (B.5) |

**Overlap and compensation.** The Lead Systems Engineer grants administrator access and also judges whether it is right. The Operations Manager's monthly reconciliation (B.9), the MDR's independent view of sign-ins, the Owner's monthly report (A.10), and the yearly independent assessment (A.6) are the checks on that overlap.

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security roles.** The Lead Systems Engineer is the designated Information Security Lead and the Operations Manager is the Compliance Coordinator. The Owner must record both designations in writing and update them within 30 days of any change. (PM-2; GV.RR-02; Interagency Guidelines III.A.2)

A.2 **Risk assessment.** The Information Security Lead must update the risk assessment every July, and after any major change (for example a new site, a new bank customer, or a new RMM vendor), using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register (P01). (RA-3; ID.RA-01; Interagency Guidelines III.B)

A.3 **Risk acceptance.** The Information Security Lead may accept Very Low and Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; the Owner approves a dated treatment plan instead. A risk that can reach every customer at once is never accepted at High or above. (PM-9; GV.RM-04)

A.4 **Sanctions.** A workforce member who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Operations Manager records each sanction; the Owner approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Vendors.** Before a vendor receives customer data or administrative access to company systems, the Operations Manager must review its security (a SOC 2 report or a questionnaire) and the contract must include: security incident notice to the company within 72 hours or less, limits on use of company and customer data, and the vendor's duty to protect it. Critical vendors (colocation, cloud, RMM, PSA, DNS, identity, MDR) are reviewed every year. Existing contracts are brought in line at renewal, and by 2026-12-31 for the RMM and MDR providers. (SA-9; GV.SC-05; GV.SC-07; Interagency Guidelines III.D)

A.6 **Independent assessment.** Key security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; ID.IM-01; Interagency Guidelines III.C.3)

A.7 **Retention.** Policies, risk assessments, assessment results, incident records, bank notices, training records, vendor reviews, and sanction records must be kept for at least 3 years, or longer where a contract or legal hold requires. (SI-12; GV.PO-02)

A.8 **Policy review and access to policies.** The Operations Manager must review this policy set and the SSP every September and after an incident or major change, recheck the rules in the P03 gap analysis for amendments, and keep the current versions in the PSA knowledge base where every workforce member can read them. (PL-1; GV.PO-02; Interagency Guidelines III.E)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated with the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

A.10 **Reporting to the Owner.** The Information Security Lead must give the Owner a short security report every month (POA&M progress, the MDR monthly report, incidents, exceptions) and a yearly program report each September covering the risk assessment, decisions, vendors, test results, incidents, and recommended changes. (PM-9; GV.OV-01; Interagency Guidelines III.A.2, III.F)

### Part B. Access control
B.1 **Named accounts only.** Every person must use their own named account in every system: identity provider, VPN, RMM tool, hypervisor manager, BMCs, cloud tenant, DNS account, PSA, and firewalls. Shared or generic accounts are prohibited. The 2 shared RMM support accounts must be removed by 2026-10-15 and the shared hypervisor administrator account by 2026-12-31. The only allowed exception is the break-glass accounts in B.7. (AC-2; IA-2; PR.AA-01; Interagency Guidelines III.C.1.a)

B.2 **Least privilege.** Access must match the person's role, approved in writing by the Information Security Lead on the onboarding checklist before it is granted.
- Support Engineers get portal administration and RMM technician rights only, without script authoring or global policy rights.
- RMM technician rights are limited to the customers each person supports wherever the tool allows.
- PSA vault folders are restricted by role. Bank server passwords are kept in the business password manager with per-person access.
- Service accounts get only the actions their integration needs. The portal's account in the hypervisor manager must be limited to VM power, console, and provisioning actions by 2026-11-30, and its secret moved out of plain-text files.

(AC-6; AC-3; PR.AA-05)

B.3 **MFA.** MFA is required for every workforce sign-in and every administrative interface: the identity provider, VPN, RMM tool, cloud tenant, DNS account, firewalls, and the hypervisor manager. BMCs are reached only from a jump host that requires MFA. Push approvals must use number matching. Administrators must use phishing-resistant hardware security keys by 2026-12-31. No one may store an MFA seed in a shared vault. (IA-2(1); PR.AA-03)

B.4 **Separate administrator accounts.** Administrator rights must be held in accounts separate from everyday email and browsing accounts, and used only for planned administrative work. This applies to the Owner. (AC-6; PR.AA-05)

B.5 **Two-person approval.** These actions need a second engineer's recorded approval before they run:
- an RMM script or policy aimed at more than one customer (from 2026-11-30);
- deleting backups or shortening backup retention (from 2026-12-31);
- changing the MDR's automated containment or auto-close settings.

In an emergency the incident commander may act alone under POL-03 4.4 and must record the reason. (AC-5; PR.AA-05; Interagency Guidelines III.C.1.e)

B.6 **Leavers.** On or before a person's last day, the Operations Manager must complete the termination checklist:
- disable the person's accounts in every system in B.1;
- remove them from the colocation authorized-person list;
- collect the laptop and security key;
- have the Information Security Lead rotate every shared secret the person knew (break-glass seals, BMC and device passwords, vault entries).

For an involuntary departure, access is disabled before the person is told. (PS-4; AC-2; PR.AA-05)

B.7 **Break-glass access.** Two break-glass accounts per critical system (identity provider, cloud tenant, hypervisor manager, RMM tool) must be created, protected with hardware keys or sealed credentials, and stored offline: one set with the Owner and one in the company safe. They are excluded from automatic suspension by the MDR. Any use must be reported to the Information Security Lead the same day, logged, and followed by a credential change. (AC-2; PR.AA-05)

B.8 **Remote access.** Only these types of remote access are allowed:
1. the firewall VPN with identity provider MFA, the only path to the DC-1 management network;
2. the RMM and cloud consoles, only from the company's VPN egress addresses (from 2026-11-30);
3. SaaS tools through single sign-on.

No other remote access tools may be installed on company or customer systems. Vendor remote sessions to DC-1 equipment need a named account, a ticket, and an engineer watching. (AC-17; PR.AA-05; Interagency Guidelines III.C.1.a)

B.9 **Account reviews.** Each month the Operations Manager must compare the user lists of every system in B.1, and the colocation authorized-person list, with the staff roster and remove anything that does not match. Each quarter the Information Security Lead must confirm that every administrator right and service account is still needed. (AC-2; PR.AA-05)

B.10 **Authenticators.**
- Passwords must be at least 14 characters, generated by the password manager, and never reused.
- Vendor default passwords must be changed before a device is connected.
- BMC passwords must be unique per host and checked out per person.
- Secrets must never sit in plain-text configuration files.
- Any credential a departing or compromised person knew must be changed at once.

(IA-5; PR.AA-01)

B.11 **Customer identity checks.** Before the support desk resets a customer's password or MFA, opens a VM console for a customer, or adds a customer administrator, it must call back the customer's account owner at the number in the contract. Customer administrator accounts must use MFA by 2027-01-31, starting with Bank A and Bank B by 2026-10-31. (IA-8; PR.AA-02; Interagency Guidelines III.C.1.a)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Workforce members may open a customer's VM, server, or data only to work a ticket or an approved change for that customer. (PL-4; PR.AT-01)

C.2 Workforce members must not put customer data, bank customer information, or credentials into personal email, personal cloud storage, personal messaging apps, or public AI chatbots. POL-04 4.6 lists the approved AI tools. (PL-4; PR.AT-01)

C.3 Workforce members must lock their laptop when stepping away, keep it encrypted and updated, never share passwords or MFA codes, and never approve an MFA prompt they did not start. (AC-11; PL-4)

C.4 Workforce members must complete security training at hire and every year and take part in phishing simulations. Technical staff must also complete role-based training on RMM script safety, caller verification, and the bank notice duty by 2026-12-31 and yearly after that. (AT-2; AT-3; PR.AT-01; PR.AT-02; Interagency Guidelines III.C.2)

C.5 Workforce members must report suspected incidents within 1 hour under POL-03 4.2, including their own mistakes. (IR-6)

C.6 **Monitoring notice.** Company laptops, accounts, and systems are monitored 24x7 by the MDR provider, which uses AI-assisted analysis and can isolate a laptop or suspend an account on its own (P10). Workforce members should not expect privacy on company systems. (PL-4)

C.7 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. Current staff sign by 2026-10-31. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. Compliance is checked through the monthly account reconciliation (B.9), the MDR monthly report, and the yearly independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; P01 risk register; P02 SSP control statements AC-2, AC-5, AC-6, AC-17, IA-2(1), IA-5, PS-4; P03 gap rows G-008, G-011, G-013, G-014, G-018, G-022, G-026, G-029 to G-033

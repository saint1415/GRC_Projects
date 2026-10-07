# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Property Manager (security and privacy lead) |
| Approved by | Managing Member, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, CM-7, CA-2, SI-12, SI-2, SI-3. Part B: AC-1, AC-2, AC-3, AC-6, AC-17, IA-2, IA-2(1), IA-5, MA-4, PE-2, PS-4, AU-6, MP-7, SC-7. Part C: PL-4, AT-2, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.PS-01, PR.PS-02, PR.IR-01 |
| Benchmark and obligations | CISA CPG 2.0 goals 1.A, 1.B, 1.D, 1.E, 2.B, 3.A to 3.I, 3.M, 3.P, 3.R, 3.S, 4.A (voluntary); PCI DSS v4.0.1 12.1.1 to 12.1.3; Fla. Stat. 501.171(2) |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people reach the company's systems, buildings, and information and only as far as their job requires, and tell the workforce how to use company systems.

## 2. Scope
All employees, temporary staff, and contractors who use company systems or hold building credentials issued by the company: the MSP, the controls contractor, the security integrator, and the janitorial contractor. It covers the building systems (BAS, access control, video, property networks), the business SaaS, every company device, and every copy of company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managing Member | Approves policies and the security budget; accepts Moderate and higher risks; approves exceptions; reviews the Property Manager's own administrator activity each month |
| Property Manager | Security and privacy lead; runs this policy; administers access control and video; directs the MSP; reviews accounts and logs |
| Building Engineer | Owns BAS accounts; approves and watches every controls contractor session |
| Tenant Services and Leasing Coordinator | Issues and disables building credentials on written tenant requests (operator role only) |
| MSP | Creates and disables suite and computer accounts on the Property Manager's request; runs the remote access service |
| Controls contractor and security integrator | Use only the named accounts and access paths this policy allows |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security lead.** The Property Manager is the designated security and privacy lead. The Managing Member must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02; CPG 1.A; PCI DSS 12.1.3)

A.2 **Risk assessment.** The Property Manager must update the risk assessment every July, and after any major change such as a new building system, a new property, or a new vendor with remote access, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01; CPG 1.B)

A.3 **Risk acceptance.** The Property Manager may accept Low and Very Low risks. Only the Managing Member may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Managing Member. (PM-9; GV.RM-01)

A.4 **Sanctions.** An employee who breaks a security rule is sanctioned in proportion to intent and harm: coaching, a written warning, suspension, or termination. Reporting a mistake in good faith is never sanctioned. Contractors who break the rules lose access and may lose the contract. (PS-8; GV.RR-04)

A.5 **No security terms, no access.** No vendor or contractor may get remote access to a company system or hold personal information for the company until its agreement includes the company's security addendum: named accounts, MFA, incident notice within 24 hours, return or deletion of data at the end of the work, and for the controls contractor, copies of controller programs after every change. Existing agreements must be amended by 2026-12-31. (SA-9; GV.SC-05; CPG 1.D, 1.E; Fla. Stat. 501.171(6)(a))

A.6 **Independent assessment.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; CPG 2.C)

A.7 **Security records.** Policies, risk assessments, assessments, incident records, training records, and vendor reviews must be kept for at least 5 years. (SI-12; GV.PO-02)

A.8 **Policy review.** The Property Manager must review POL-02, POL-03, and POL-04 every August and after an incident or major change, and keep the current versions in the shared drive where every employee can read them. (PL-1; GV.PO-02; PCI DSS 12.1.1, 12.1.2)

A.9 **New devices, software, and features.** No device may be connected to a company network, no software installed on the BAS workstation, and no new feature turned on in a cloud platform (including any video analytics or AI feature) until the Property Manager has approved it in writing and, for analytics or AI, the Managing Member has approved it after a P10 assessment. Vendors and contractors may not turn on features on the company's behalf. (CM-7; PR.PS-01; CPG 3.P)

A.10 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. A patching or antivirus exclusion on any device is an exception. (PL-1; GV.PO-01)

A.11 **Baseline protections.** Every computer that connects to a company network must receive security patches monthly (critical patches within 14 days) and run the MSP-managed malware protection. The BAS workstation follows the same rule, with each patch approved by the controls contractor within 14 days of release and tested with a rollback plan; if the contractor cannot approve a patch, an exception under A.10 is required. Building devices (controllers, door controllers, cameras, routers) must run supported firmware, checked at each quarterly review. (SI-2; SI-3; PR.PS-02; CPG 2.B, 4.A)

### Part B. Access control
B.1 **Unique accounts.** Every person must have their own account in every system: the suite, the property management system, the access control and video platform, the BAS workstation, and the remote access service. Shared or generic accounts, including a shared "engineer" login or a shared contractor account, are not allowed. (IA-2; AC-2; PR.AA-01; CPG 3.C)

B.2 **Least privilege.** Access must match the person's job. Platform administrator rights are limited to the Property Manager and the Managing Member (backup); the Tenant Services and Leasing Coordinator has operator rights only. The security integrator gets administrator access only for a scheduled job, for no longer than 7 days, and the Property Manager removes it afterwards. Administrators use a separate account for administration. (AC-6; AC-3; PR.AA-05; CPG 3.G, 3.H)

B.3 **MFA.** MFA with an authenticator app or stronger is required for the suite, the property management system, every platform administrator and operator account, the remote access service, the backup console, and the MSP's own management platform. Text-message codes are not accepted for administrators. (IA-2(1); PR.AA-03; CPG 3.F)

B.4 **Staff departures.** On or before an employee's last day, the Property Manager must complete the departure checklist: disable the suite, property management system, platform, and BAS accounts; ask the MSP to remove computer access; remove MFA registrations; disable the employee's building credential; collect keys, fobs, and devices; and change any password the person knew. For an involuntary departure, access must be disabled before the person is told. (PS-4; AC-2; CPG 3.D)

B.5 **Building credentials.** Credentials are issued only on a written request from a tenant's designated contact or, for contractors, from the Property Manager. Each quarter the Tenant Services and Leasing Coordinator sends every tenant contact its credential list to confirm; credentials not confirmed within 14 days are disabled. Credentials not used for 90 days are disabled automatically. Leases renewed after 2026-09-01 must require tenants to report departures within 2 business days. (PE-2; AC-2; PR.AA-06; CPG 3.D)

B.6 **Monthly review.** Each month the Property Manager must compare the user lists of the suite, the platform, the BAS workstation, the remote access service, and the backup console with the staff and contractor roster, and remove anything that does not match. The Managing Member reviews the platform's administrator change report at the same meeting. (AC-2; AU-6; PR.AA-05)

B.7 **Emergency access.** Sealed break-glass credentials for the suite, the platform, and the property management system are kept in the incident binder in the Managing Member's safe. Any use must be reported to the Property Manager, and the passwords changed afterwards. (AC-2; PR.AA-05)

B.8 **Remote access by contractors and the MSP.** Contractors may reach the BAS workstation only through the approved remote access service, with a named account and MFA, after the Building Engineer approves each session. Sessions are recorded and kept 90 days. Always-on unattended remote access tools are not allowed on building systems. The MSP must give the Property Manager a current list of its technicians with access each year. (AC-17; MA-4; PR.AA-05; CPG 1.E)

B.9 **Passwords and defaults.** Staff must use the company password manager. Passwords must be at least 16 characters where the system allows, and never reused or written down. Every device's default password must be changed before it is connected to any network, and the new password stored in the password manager. (IA-5; PR.AA-01; CPG 3.A, 3.B)

B.10 **BAS workstation.** The BAS workstation is used only to run the BAS. No email, web browsing, or personal use. USB storage is blocked except the company-owned drive kept by the Building Engineer, which is scanned on an office computer before each use. The screen locks after 15 minutes idle. (CM-7; MP-7; CPG 3.M, 3.R)

B.11 **Network separation.** At each property, building devices (BAS workstation and controllers, door controllers, cameras) must be on their own network segment, separate from office computers and guest Wi-Fi, with rules that deny all traffic not needed. Only the approved remote access service may reach the BAS workstation from outside. No building device may be reachable from the internet, and router and firewall management must never be exposed to the internet. (SC-7; AC-3; PR.IR-01; CPG 3.I, 3.S)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Staff must look at tenant, applicant, and video information only when their job needs it. (PL-4; PR.AT-01)

C.2 Staff must not store or send company information with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. POL-04 4.6 lists approved tools and features. (PL-4)

C.3 Staff must lock their screen when stepping away and never share passwords or MFA codes with anyone, including the MSP or a contractor. (PL-4; IA-5)

C.4 Staff must complete security training at hire and every year, take part in phishing simulations, and, for engineering staff, complete the OT module. (AT-2; PR.AT-01; CPG 3.J; PCI DSS 12.6.1)

C.5 Staff must report suspected incidents at once under POL-03 4.2, including their own mistakes. (IR-6)

C.6 Staff must sign an acknowledgment of this policy at hire and after each annual update. (PL-4; PCI DSS 12.1.3)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Property Manager checks compliance through the monthly review (B.6), the quarterly credential confirmation (B.5), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.10.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; departure checklist; credential request form; P01 risk register; P02 SSP control statements AC-2, IA-2(1), MA-4, PE-2

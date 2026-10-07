# Access Control Policy (with Program Governance, Secure Product Development, and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Operations Manager (Information Security Coordinator), with the Head of Engineering (Product Security Lead) for Part A.10 to A.12 |
| Approved by | CEO, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), at design freeze, and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, RA-3, PS-8, SA-9, SR-3, CA-2, SI-12, PL-1, SA-8, SA-11, SA-11(2), CM-8, SC-12, CM-14, SI-7, IA-5, IA-3. Part B: AC-2, AC-6, IA-2, IA-2(1), IA-5, PS-4, PS-7, AC-17, SC-7, SI-2. Part C: PL-4, AT-2, AT-3, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, ID.AM-02, PR.PS-06, PR.DS-10, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02 |
| Regulatory basis | FD&C Act 524B(b)(2)-(3) (N31-33-R05); 21 CFR 820.10(a) and (c) (ISO 13485 cl. 6.2, 7.3, 7.4, incorporated by reference) |

**Why this policy has three parts.** A 7-person startup does not need five separate policies. This policy carries the program governance and secure product development rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people reach company systems and product secrets and only as far as their job requires, make sure WM-1 is built with the security processes FDA expects, and tell the workforce how to use company systems.

## 2. Scope
All employees, contractors, and consultants of Cris Santos Company. It covers every company system and every copy of company information, including systems run for the company by the MSP, SaaS vendors, the cloud provider, and the contract manufacturer, and every WM-1 product release.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| CEO | Approves policies and the security budget; accepts risk; decides sanctions |
| Operations Manager | Information Security Coordinator; runs Part B for corporate systems; onboarding and offboarding; MSP contact |
| Head of Engineering | Product Security Lead; approves access to the repository and cloud tenant; runs A.10 to A.12 |
| QA/RA Manager | Owns section 524B compliance and the QMS procedures that carry this policy; approves eQMS access |
| MSP | Creates and disables suite and laptop accounts on request; operates laptop and network controls |
| All workforce | Protect credentials and product secrets; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance and secure product development (essentials of POL-01)
A.1 **Roles.** The CEO is the system owner and risk acceptor. The Operations Manager is the Information Security Coordinator for corporate IT. The Head of Engineering is the Product Security Lead. The QA/RA Manager owns section 524B compliance. The CEO must record these designations in writing and update them within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The QA/RA Manager and Head of Engineering must update the risk register every July, at design freeze, before each premarket submission, and after a major change, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Operations Manager or Head of Engineering may accept Low and Very Low risks in their area. Only the CEO may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the CEO. A risk that could affect patient safety after clearance is never accepted at High. (PM-9; GV.RM-01)

A.4 **Sanctions.** A person who breaks a security rule must be sanctioned in proportion to intent and harm: coaching, a written warning, removal of access, or termination of employment or contract. The CEO decides, and the Operations Manager records each sanction. Reporting a mistake or a vulnerability in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Vendors and suppliers.** No vendor, contractor, or supplier may receive Restricted or Confidential information (POL-04) until written security terms are in place. The contract manufacturer's quality agreement must cover handling of firmware images and provisioning secrets, test station security, and security incident notice within 72 hours. The QA/RA Manager reviews these terms at each supplier audit. (SA-9; SR-3; GV.SC-05; ISO 13485 cl. 4.1.5, 7.4)

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and before each premarket submission. (CA-2)

A.7 **Retention.** Security records (risk assessments, assessments, incident and vulnerability records, sanctions, training) must be kept for 6 years, or for the QMS retention period for design history records if that is longer. (SI-12; GV.PO-02)

A.8 **Policy review and access.** The Operations Manager must review this policy set every August, at design freeze, and after an incident, and keep the current version in the eQMS where every workforce member can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception must be requested in writing, rated on the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. No exception may allow a shared or default credential in a released product. (PL-1; GV.PO-01)

A.10 **Secure product development.** Every WM-1 software release must have: security requirements written as design inputs; a current system threat model that includes related systems (the cloud service, update path, CI pipeline, and contract manufacturer provisioning); a machine-readable SBOM generated by the build; security testing traced to the security requirements; and a release record linking the image to the reviewed commit. The secure product development procedure in the eQMS carries the detail. (SA-8; SA-11; SA-11(2); CM-8; PR.PS-06; 524B(b)(2)-(3); 820.10(c))

A.11 **Signing and release.** Firmware may be signed only through the release pipeline, with the signing key held in an HSM-backed key service and approved by two named people. From 2027-01-01, no signing key material may exist on a laptop, USB drive, or file share. Until the key is moved, no firmware may be released beyond the company lab and the partner hospital's evaluation network. (SC-12; CM-14; SI-7; PR.DS-10)

A.12 **Device credentials.** No WM-1 product may ship with a hardcoded, default, or shared password, key, or certificate. Each unit must receive unique credentials at manufacture, and compromise of one unit must not reveal credentials for another. (IA-5; IA-3; PR.AA-01; FDA premarket guidance App. 1)

### Part B. Access control
B.1 **Unique accounts.** Every person must have their own account in each system. Shared accounts are not allowed, except one break-glass owner account for the cloud tenant, whose credentials and MFA device are sealed in the office safe and used only when named accounts fail. Each use must be logged and the password changed afterwards. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege and approval.** Access must match the job. The system owner approves access in writing before it is granted: the Head of Engineering for the repository and cloud tenant, the QA/RA Manager for the eQMS, and the Operations Manager for the suite. Only the Head of Engineering and one named backup may change release scripts or hold cloud owner rights, and not for daily work. (AC-2; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for every account in the suite, eQMS, repository, cloud tenant, and every administrator login, including logins held by the MSP (firewall, remote management). (IA-2(1); PR.AA-03)

B.4 **Leavers and contractors.** On or before a person's last day, the Operations Manager must complete the offboarding checklist: disable suite, eQMS, repository, cloud, and lab accounts; remove MFA registrations; collect laptops, keys, and pre-production units; and rotate any shared secret the person could have seen. Contractor and test lab accounts must be created with an end date matching the contract. (PS-4; PS-7; AC-2; PR.AA-05)

B.5 **Monthly reconciliation.** Each month the Operations Manager must compare the user lists of the suite, eQMS, repository, and cloud tenant with the staff and contractor roster and remove anything that does not match. Each quarter the Head of Engineering must confirm who has repository write access and cloud roles. (AC-2; AC-6)

B.6 **Secrets.** Keys, API keys, passwords, and provisioning files must be kept only in the CI secret store or the key management service. They must never appear in source code, build logs, email, chat, or shared links. A secret that leaks must be rotated within 5 business days. (IA-5; SC-12)

B.7 **Remote and vendor access.** MSP technicians, contractors, and test labs must use named accounts with MFA. The MSP must give the Operations Manager a current list of technicians with access every year. (AC-17; IA-2(1); SA-9)

B.8 **Lab systems.** Lab workstations must have named logins, be managed and patched by the MSP, and sit on a lab network segment separated from the office network. (IA-2; SI-2; SC-7)

B.9 **Passwords.** Passwords must be at least 12 characters and never reused from personal accounts. (IA-5)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Workforce members may access only the information their job needs. (PL-4; PR.AT-01)

C.2 Workforce members must not store or send Restricted or Confidential information with personal email, personal cloud storage, personal messaging apps, or AI tools that are not on the approved list (POL-04 4.7). (PL-4)

C.3 Workforce members must lock their screen when stepping away and never share passwords, MFA codes, or signing approvals. (PL-4)

C.4 Workforce members must complete security training at hire and every year and take part in phishing simulations. Engineers must also complete secure development training at hire and every two years. (AT-2; AT-3; PR.AT-01; PR.AT-02)

C.5 Workforce members must report suspected incidents and vulnerabilities at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.6 Any change to a supplier's or investor's bank details must be confirmed by a phone call to a number already on file before any payment. (AT-2)

C.7 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Operations Manager checks Part B through the monthly reconciliation (B.5); the QA/RA Manager checks A.10 to A.12 at each design review and release; the annual independent assessment (P07) checks all parts.

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; secure product development procedure (eQMS); offboarding checklist; P01 risk register; P02 SSP control statements AC-2, IA-2(1), IA-5, SC-12, PS-4

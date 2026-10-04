# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Store Manager (Security and PCI Lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Yearly (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, CA-2, SA-9, CM-3, SI-12. Part B: AC-1, AC-2, AC-3, AC-6, AC-17, IA-2, IA-2(1), IA-5, PS-4. Part C: PL-4, AT-2, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.PS-01 |
| PCI DSS v4.0.1 (N44-45-R01) | 6.5, 7.1-7.2, 8.1-8.4, 12.1-12.3, 12.6, 12.8 |
| FTC Act Section 5 (N44-45-R02) | 45(n) reasonable security |

**Why this policy has three parts.** A 7-person store does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the store's security program, make sure only authorized people can reach the commerce platform, the online store, email, and customer information, and only as far as their job requires, and tell staff how to use store systems.

## 2. Scope
All workforce members of Cris Santos Company, including the Owner, part-time staff, and temporary help, and every outside party with a login: the MSP, the marketing freelancer, and provider support staff. It covers every system and every copy of store information, including systems that the provider, the MSP, and other SaaS vendors run for the store.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate and higher risk; the only person who may change the payout bank account |
| Store Manager | Security and PCI Lead; runs this policy; grants and removes access; reviews accounts and the activity log |
| Bookkeeper | Keeps vendor agreements and the service provider list; checks daily deposits against sales |
| MSP | Creates and disables mailboxes and computer accounts on the Store Manager's request |
| All workforce and outside users | Protect their codes and passwords; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security and PCI Lead.** The Store Manager is the designated Security and PCI Lead. The Owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02; PCI DSS 12.1)

A.2 **Risk assessment.** The Security and PCI Lead must update the risk register every July, and after any major change such as a new payment provider, a second store, or a new AI feature, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment. (RA-3; ID.RA-01; PCI DSS 12.3)

A.3 **Risk acceptance.** The Store Manager may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. (PM-9; GV.RM-01)

A.4 **PCI DSS scope and SAQs.** Before signing any SAQ, the Security and PCI Lead must confirm in writing which devices, pages, and vendors are in scope, and the Owner must not sign an SAQ answer that lacks evidence. Only payment devices that belong to the provider's validated P2PE solution may be used to take card payments in person. (CM-8; PCI DSS 12.5)

A.5 **Service providers.** The Bookkeeper must keep a list of every service provider that handles card or customer data or can change the store's systems, with what each is responsible for. No outside party may receive customer data or a login until a written agreement covers security, data use, and deletion. The provider's AOC must be checked every year before the SAQs are signed. (SA-9; GV.SC-05; PCI DSS 12.8)

A.6 **Changes to the online store.** No one may add, remove, or change a script, app, or custom code on the online store without the Store Manager's written approval, recorded in the change log with the reason. Nothing is added to the checkout page. (CM-3; PR.PS-01; PCI DSS 6.4.3, 6.5)

A.7 **Assessment.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2)

A.8 **Records.** Policies, risk registers, assessments, SAQs and their evidence, incident records, inspection logs, and training records must be kept for at least 3 years. (SI-12; GV.PO-02)

A.9 **Policy review and exceptions.** The Store Manager must review this policy set every August and after any incident. An exception must be requested in writing, rated on the risk register scale, approved under A.3, and limited to 12 months or less. (PL-1; GV.PO-01; GV.PO-02)

### Part B. Access control
B.1 **Personal accounts and codes.** Every person must have their own dashboard login, POS code, and mailbox. Shared codes and shared logins are not allowed, except the shared orders mailbox, which may be reached only through personal logins with delegated access. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2)

B.2 **Least privilege.** Cashiers and the Stock and Produce Clerk get the cashier role; the Store Manager gets the manager role and administrator rights for users and settings; only the Owner may change payout or bank details. The marketing freelancer gets a content-only role. The Store Manager must approve access in writing before it is granted. (AC-2; AC-3; AC-6; PR.AA-05; PCI DSS 7.2)

B.3 **MFA.** MFA is required for every dashboard and online store login with more than cashier rights, every mailbox, and every administrator login held by the MSP (firewall, backup console, remote management). (IA-2(1); PR.AA-03; PCI DSS 8.4)

B.4 **Last day.** On or before a person's last day, the Store Manager must complete the last-day checklist: disable the POS code, dashboard login, and mailbox; remove MFA registrations; collect keys; change the store phone code and the staff Wi-Fi password. For an involuntary termination, access is removed before the person is told. (PS-4; AC-2; PCI DSS 8.2)

B.5 **Monthly review.** Each month the Store Manager must compare the dashboard users, POS codes, online store administrators, and mailboxes with the payroll roster and the service provider list, remove anything that does not match, and sign the review sheet. (AC-2; AC-6; PR.AA-05)

B.6 **Outside access.** MSP technicians, provider support staff, and the freelancer must use named accounts with MFA. The MSP must give the Store Manager a current list of technicians with access every year. (AC-17; IA-2(1); SA-9)

B.7 **Passwords and codes.** Passwords must be at least 12 characters and never reused from personal accounts; a password manager is provided to office staff. POS codes must not be shared or written down. The staff Wi-Fi password must change every year and whenever someone leaves. (IA-5; PCI DSS 8.3)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Store systems are for store work. Staff must look up customer information only to serve that customer. (PL-4; PR.AT-01)

C.2 Staff must never write down, type, email, text, or photograph a full card number or security code. If a customer sends one, delete it and reply with the standard message (POL-04 4.3). (PL-4; PCI DSS 3.2, 4.2)

C.3 Staff must not put customer, loyalty, or card information into personal email, personal cloud storage, messaging apps, or public AI chatbots. POL-04 section 4.8 lists the approved AI tools. (PL-4)

C.4 Staff must lock the office PC when stepping away, never share codes or MFA prompts, and never approve an MFA prompt they did not start. (PL-4; IA-2(1))

C.5 Staff must complete security training at hire and every year, including terminal tampering for cashiers and phishing for office staff. (AT-2; PR.AT-01; PCI DSS 12.6)

C.6 Staff must report suspected incidents at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.7 Staff must sign an acknowledgment of this policy at hire and after each yearly update. (PL-4; PCI DSS 12.2)

## 5. Compliance and enforcement
Breaking this policy may lead to retraining, a written warning, or dismissal, decided by the Owner. Reporting a mistake in good faith is never punished. The Store Manager checks compliance through the monthly review (B.5) and the weekly activity log check, and an independent assessor checks it each year (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; account and last-day checklists; change log; P01 risk register; P02 SSP control statements AC-2, AC-6, IA-2(1), PS-4, CM-3

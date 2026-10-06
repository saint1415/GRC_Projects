# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Broker-owner, 2026-09-14 |
| Effective date | 2026-09-15 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, SA-9, SI-12, CA-2, PS-8. Part B: AC-2, AC-3, AC-5, AC-6, AC-17, AC-19, IA-2, IA-2(1), IA-2(2), IA-5, PS-4, PS-7. Part C: PL-4, AT-2, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01 |
| Rules served | Fla. Stat. 501.171(2) (reasonable measures); Fla. Admin. Code r. 61J2-14.010(1); FTC Safeguards Rule elements used as the benchmark (16 CFR 314.4(a), (b), (c)(1), (c)(5), (e), (f), (i)) |

**Why this policy has three parts.** A 7-person brokerage does not need five separate policies. This policy carries the program rules that would otherwise be in an Information Security Policy (POL-01) and the use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the brokerage's security program, make sure only authorized people reach client information and escrow systems and only as far as their work requires, and tell employees and contractor agents how to use brokerage systems.

## 2. Scope
All employees and all contractor sales associates affiliated with Cris Santos Company, LLC, plus temporary staff and the MSP's technicians when they act for the brokerage. It covers every system and every copy of brokerage information: the transaction platform, email and files, e-signature, the property management platform, online banking, accounting, company devices, and agents' personal devices while they reach brokerage systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Broker-owner | Approves policies and the security budget; accepts Moderate risk; approves escrow payments; decides sanctions with the Office Manager |
| Office Manager | Security and compliance lead; runs this policy; grants and removes access; reviews accounts and alerts; keeps the vendor list |
| MSP | Sets up and maintains company devices and network on the Office Manager's request; holds only named, MFA-protected administrator access |
| Employees and contractor agents | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security lead.** The Office Manager is the security and compliance lead (the benchmark "qualified individual"). The Broker-owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02; benchmark 314.4(a))

A.2 **Risk assessment.** The Office Manager must update the risk assessment every July, and after a major change such as a new transaction platform, a new vendor that holds client data, or adding closing, title, or mortgage services, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment. (RA-3; ID.RA-01; benchmark 314.4(b))

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the Broker-owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Broker-owner. (PM-9; GV.RM-01)

A.4 **Sanctions.** An employee who breaks a security rule must face consequences in proportion to intent and harm: coaching, a written warning, or termination. A contractor agent who breaks a security rule may have system access suspended or the affiliation ended under the independent contractor agreement. The Office Manager records each case; the Broker-owner decides suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Vendors.** No vendor may store or process client information for the brokerage until the Office Manager has added it to the vendor list, checked its security (a SOC 2 report or a short questionnaire), and confirmed it will report a breach. The MSP contract and every renewal of a SaaS contract must include a breach notice duty (no more than the 10 days in Fla. Stat. 501.171(6)(a); 24 hours for the MSP). (SA-9; GV.SC-05; benchmark 314.4(f))

A.6 **Assessment.** Security controls must be assessed every August by someone who does not operate them. (CA-2; benchmark 314.4(d)(1))

A.7 **Reporting to the Broker-owner.** The Office Manager reviews the POA&M with the Broker-owner for 30 minutes each month and gives a one-page written report on the program each September. (PM-9; GV.OV-01; benchmark 314.4(i))

A.8 **Policy review and availability.** The Office Manager must review this policy set every August and after an incident or major change, and keep the current version in the shared files where every employee and agent can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated with the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Named accounts.** Every employee and agent must have their own account in each system. Shared or generic accounts are not allowed, including administrator accounts. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Agents see only their own transaction files. Administrator roles are limited to the Office Manager and one named MSP technician in each system. The Office Manager approves access in writing (the onboarding checklist) before it is granted. (AC-2; AC-3; AC-6; PR.AA-05; benchmark 314.4(c)(1)(ii))

B.3 **MFA everywhere.** MFA is required for every account in the productivity suite, the transaction platform, the e-signature service, the property management platform, accounting, and online banking, and for every administrator login, including the backup console and the MSP's remote management tool. Sign-in methods that bypass MFA (legacy protocols) must be blocked. (IA-2(1); IA-2(2); PR.AA-03; benchmark 314.4(c)(5))

B.4 **Offboarding.** On an employee's last day, or on the same day the brokerage learns an agent's license is moving to another broker, the Office Manager must complete the offboarding checklist: disable every account, remove MFA registrations and mobile mail access, transfer open files, collect keys and devices, and remind the person in writing of their confidentiality duty and the duty to delete client files from personal devices. (PS-4; PS-7; AC-2; benchmark 314.4(c)(1)(i))

B.5 **Monthly reconciliation.** Each month the Office Manager compares the user lists of each system with the employee and agent roster and removes anything that does not match. (AC-2; PR.AA-05)

B.6 **Payment approval.** Outgoing escrow wires and ACH batches require two people in online banking: an initiator (Office Manager or Bookkeeper) and the Broker-owner as approver. No one may approve a payment they initiated. The Broker-owner must be a signatory on every escrow account. (AC-5; r. 61J2-14.010(1))

B.7 **Emergency access.** One break-glass administrator account for the productivity suite, with MFA, is kept sealed by the Broker-owner. Any use must be reported to the Office Manager and the password changed afterwards. (AC-2)

B.8 **MSP access.** MSP technicians must use named accounts with MFA. The MSP must give the Office Manager a current list of technicians with access each year. (AC-17; IA-2(1); SA-9)

B.9 **Passwords.** Passwords must be at least 12 characters and must not be reused from personal accounts. The staff Wi-Fi password changes every year and when an employee leaves. (IA-5; PR.AA-01)

### Part C. Use rules for employees and agents (essentials of POL-05)
C.1 Brokerage systems are for brokerage work. Look only at the client files your work needs. (PL-4; PR.AT-01)

C.2 Do not send or store client information in personal email, personal cloud storage, or text messages, and do not set your brokerage mailbox to forward to a personal account. POL-04 4.6 covers AI tools. (PL-4; AC-4)

C.3 **Personal devices.** An agent's or employee's personal phone or laptop may reach brokerage email or the transaction platform only if it has a screen lock, current operating system updates, and no shared login, and only through the approved apps (which let the brokerage wipe company data). Report a lost or stolen device to the Office Manager within 1 hour. (AC-19; PR.AA-05)

C.4 Never share passwords or MFA codes with anyone, including the MSP and the Office Manager. Never approve an MFA prompt you did not start. (IA-5; PL-4)

C.5 Never send wire instructions by email. Share them only through the transaction platform's client document sharing, and follow the verification rule in POL-03 4.9. (IA-8; PL-4)

C.6 Complete security training at onboarding and every year, including the wire fraud module, and take part in phishing simulations. (AT-2; PR.AT-01; benchmark 314.4(e)(1))

C.7 Report suspected incidents at once under POL-03 4.2, including your own mistakes. (IR-6)

C.8 Sign an acknowledgment of this policy at onboarding and after each annual update. For agents, the acknowledgment is part of the independent contractor agreement. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Office Manager checks compliance through the monthly reconciliation (B.5), the weekly alert review (POL-03), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9. No exception may remove MFA from an account that can send email to clients or approve a payment.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and offboarding checklist; independent contractor agreement; P01 risk register; P02 SSP control statements AC-2, AC-5, IA-2(1), IA-2(2), PS-4, PS-7

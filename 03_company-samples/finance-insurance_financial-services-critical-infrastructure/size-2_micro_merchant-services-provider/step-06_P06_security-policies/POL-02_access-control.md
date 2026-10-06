# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Operations Manager (Qualified Individual and security lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after a significant change or incident |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, CA-2, CA-7, CM-8, SA-9, SI-12, PS-8. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, AU-6, IA-2, IA-2(1), IA-5, IA-8, PS-4. Part C: PL-4, AT-2, IR-6 |
| CSF 2.0 | GV.RR-01, GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, ID.RA-01, ID.AM-03, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, DE.AE-02 |
| Drivers | PCI DSS v4.0.1 Requirements 7, 8, 10.4, 12.1 to 12.6, 12.8; 16 CFR 314.4(a), (c)(1), (c)(5), (c)(8), (e), (f) |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01) and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security and PCI DSS program, make sure only the right people reach the payment console and merchant information, and tell employees and outside agents how to use company systems.

## 2. Scope
All employees and the outside sales agents. It covers every system in the Merchant Payments Platform (P02), including systems run for the company by the MSP, the processor partner, and SaaS vendors, and every copy of card data and merchant information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Executive responsibility for PCI DSS; approves policies and the security budget; accepts Moderate risk; signs the SAQ and AOC; runs the quarterly PCI review |
| Operations Manager | Qualified Individual and security lead; grants and removes access; reviews logs and accounts; keeps the inventory and the service provider list |
| Merchant Support Lead | Backup administrator for the console, phone system, and CRM |
| Sales and Agent Manager | Tells the Operations Manager the same day an agent starts or leaves |
| MSP | Creates and disables suite and laptop accounts on the Operations Manager's request; operates laptop controls |
| All employees and agents | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Qualified Individual and security lead.** The Operations Manager is the Qualified Individual under 16 CFR 314.4(a) and the PCI DSS lead. The Owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Executive responsibility.** The Owner is responsible for the protection of card data and for the PCI DSS program. The Owner must review the SAQ with the Operations Manager, line by line, before signing it each year. (PM-2; GV.RR-01; PCI DSS 12.4.1)

A.3 **Risk assessment.** The Operations Manager must update the risk assessment every July, and after any significant change, using NIST SP 800-30 Rev. 1. A written targeted risk analysis must support every PCI DSS requirement where the company chooses how often to do something. (RA-3; ID.RA-01; PCI DSS 12.3.1)

A.4 **Risk acceptance.** The Operations Manager may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. A risk that would leave a PCI DSS requirement not in place must not be accepted. (PM-9; GV.RM-01)

A.5 **Quarterly PCI review.** At least every three months the Owner and the Operations Manager must review and sign a checklist confirming that log reviews, account reconciliations, the change log, terminal inventory checks, and incident readiness tasks were done. (CA-7; GV.OV-01; PCI DSS 12.4.2, 12.4.2.1)

A.6 **Scope confirmation.** The Operations Manager must confirm the PCI DSS scope every March and September, and whenever the company adds or stops a service that touches card data, changes a vendor that touches card data, moves office, or changes a person in a security role. Each confirmation is recorded and given to the Owner. (CM-8; ID.AM-03; PCI DSS 12.5.2.1, 12.5.3)

A.7 **Service providers.** The Operations Manager must keep a list of every service provider that touches card data or merchant information, with a written agreement, an AOC or other evidence each year, and a responsibility matrix showing which PCI DSS requirements each one covers. No new provider may receive card data or merchant information before this is in place. (SA-9; GV.SC-05; PCI DSS 12.8; 16 CFR 314.4(f))

A.8 **Testing.** The company must run an ASV scan and an internal vulnerability scan every quarter, a penetration test every year, and an independent control assessment every year by someone who does not operate the controls. (CA-2; RA-5; CA-8; PCI DSS 11.3, 11.4)

A.9 **Records.** Security policies, risk assessments, SAQs, AOCs, scan and test reports, review checklists, incident records, and training records must be kept for at least 3 years. (SI-12; GV.PO-02)

A.10 **Policy review.** The Operations Manager must review this policy set every August and after an incident or significant change, and keep the current version in the shared drive where every employee and agent can read it. (PL-1; GV.PO-02; PCI DSS 12.1.2)

A.11 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.4, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

A.12 **Sanctions.** An employee or agent who breaks a security rule must be dealt with in proportion to intent and harm: coaching, a written warning, removal of access, or termination of employment or of the agent agreement. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

### Part B. Access control
B.1 **Named accounts only.** Every employee and agent must have their own account in each system. Shared or generic accounts, including the phone system's "support" login, are not allowed. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2.1, 8.2.2)

B.2 **Least privilege.** Access must match the job and be approved in writing by the Operations Manager on the onboarding checklist before it is granted. Only the two support staff may hold the console role that can log in as a merchant. Outside agents may hold only the console's view-only sales role and CRM access to their own merchants. (AC-2; AC-3; AC-6; PR.AA-05; PCI DSS 7.2)

B.3 **MFA.** MFA is required on the gateway console, processor partner portal, CRM, productivity suite, phone system administration, web hosting account, and every administrator login held by the MSP. Push approvals must use number matching. (IA-2(1); PR.AA-03; PCI DSS 8.4; 16 CFR 314.4(c)(5))

B.4 **Leavers.** On or before an employee's last day, or the day an agent agreement ends, the Operations Manager must complete the offboarding checklist: disable console, portal, CRM, suite, and phone accounts; remove MFA registrations; ask the MSP to remove laptop access; collect laptops and keys; and change the staff Wi-Fi password. For an involuntary exit, access is removed before the person is told. (PS-4; AC-2; PCI DSS 8.2.5)

B.5 **Reviews.** Each month the Operations Manager must compare the user lists of the console, portal, CRM, suite, and phone system with the employee and agent roster and remove anything that does not match. Every six months the Owner must review and sign off each person's access and role. Accounts unused for 90 days must be disabled. (AC-2; AC-6; PR.AA-05; PCI DSS 7.2.4, 8.2.6)

B.6 **Passwords.** Passwords must be at least 14 characters, unique to each system, never reused from personal accounts, and kept only in the company password manager. (IA-5; PR.AA-01; PCI DSS 8.3.6)

B.7 **Locking.** Laptops must lock after 15 minutes idle and whenever left unattended, at home as well as in the office. (AC-11; PR.AA-03; PCI DSS 8.2.8)

B.8 **MSP and vendor access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the Operations Manager a current list of technicians with access every year. (AC-17; IA-2(1); SA-9; PCI DSS 8.2.2)

B.9 **Caller verification.** Any request to change a merchant's deposit bank account, owner details, or contact phone or email must be confirmed by calling the merchant back at the number already on file in the CRM, never at a number the caller gives. The change must then be approved in the processor partner portal by a second person. (IA-8; PR.AA-03; 16 CFR 314.4(c)(1))

B.10 **Log review.** The Operations Manager must read the console's daily alert digest each business day and review console impersonation, refund, and settings-change events and suite sign-in alerts every week, record the review on a checklist, and open an incident under POL-03 for anything unexplained. (AU-6; DE.AE-02; PCI DSS 10.4.1, 10.4.2; 16 CFR 314.4(c)(8))

### Part C. Workforce and agent use rules (essentials of POL-05)
C.1 Company systems are for company work. Employees and agents must look only at the merchant records their job needs. (PL-4; PR.AT-01; PCI DSS 12.2.1)

C.2 Card numbers and card security codes must never be typed, pasted, or kept in email, chat, tickets, notes, spreadsheets, or paper, and never spoken on a recorded line. Merchant owner information (Social Security numbers, bank accounts, ID images) must travel only through the CRM's secure upload link. Neither may ever be entered into a public or personal AI tool. (PL-4; PCI DSS 3.2.1; 16 CFR 314.4(c)(3))

C.3 Only AI tools on the approved list in POL-04 4.6 may be used for company work. (PL-4; SA-9)

C.4 Employees and agents must lock their screens when stepping away and must never share passwords or MFA codes, including with the MSP, the processor partner, or anyone who calls claiming to be from them. (AC-11; PL-4; PCI DSS 8.2.1)

C.5 Employees and agents must complete security training at hire and every year, take part in phishing simulations and call-back drills, and complete a short course on recognizing tampered terminals if they handle terminals. (AT-2; PR.AT-01; PCI DSS 12.6; 16 CFR 314.4(e))

C.6 Employees and agents must report suspected incidents at once under POL-03 4.2, including their own mistakes. (IR-6)

C.7 Employees and agents must sign an acknowledgment of this policy at start and after each annual update. Agent agreements must require it. (PL-4; PCI DSS 12.6.3)

## 5. Compliance and enforcement
Breaking this policy leads to action under A.12. The Operations Manager checks compliance through the monthly reconciliation (B.5), the log review (B.10), and the quarterly PCI review (A.5). The annual independent assessment (P07) and the SAQ test it.

## 6. Exceptions
Exceptions follow A.11.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and offboarding checklist; quarterly PCI review checklist; P01 risk register; P02 SSP control statements AC-2, IA-2(1), PS-4, PM-2

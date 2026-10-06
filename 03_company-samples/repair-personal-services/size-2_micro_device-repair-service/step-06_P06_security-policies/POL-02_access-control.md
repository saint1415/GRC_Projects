# Access Control Policy (with Program Governance and Staff Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Shop Manager (Security and Privacy Lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-3, PS-6, PS-8, SA-9, CA-2. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, IA-2, IA-2(1), IA-5, PS-4, PE-3. Part C: PL-4, AT-2 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-02, GV.PO-01, GV.PO-02, GV.SC-05, GV.SC-06, ID.RA-05, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01 |
| Regulatory drivers | N81-R01 (15 U.S.C. 45(n)); N81-R02 (Fla. Stat. 501.171(2), (6)); N81-R03 (PCI DSS v4.0.1 12.1.1-12.1.3, 12.6.1, 12.8.1-12.8.5) |

**Why this policy has three parts.** A 7-person shop does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the staff use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C. Part A also serves as the shop's overall information security policy for PCI DSS 12.1.1.

## 1. Purpose
Set up the shop's security program, make sure only authorized people reach shop records, customer records, and customer devices, and only as far as their job requires, and tell staff how to use shop systems.

## 2. Scope
All workforce members of Cris Santos Company: the Owner, employees, temporary staff, and anyone who works on customer devices. It covers every shop system, every customer device in the shop's custody, and every copy of shop or customer information, including systems run for the shop by the MSP and SaaS vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate risk; approves treatment plans for High risks; decides sanctions with the Shop Manager |
| Shop Manager | Security and Privacy Lead; runs this policy; grants and removes access; runs the monthly account and log checks; keeps the vendor list |
| Senior Technician | Custodian of the bench workstations and bench storage; applies Part B there until the MSP takes them over |
| MSP | Creates and disables productivity suite accounts on the Shop Manager's request; operates office endpoint and network controls; holds no shop credential without MFA |
| All workforce | Protect credentials; follow Part C and POL-04; report problems at once (POL-03) |

**Overlap and compensation.** The Shop Manager runs security and also works the counter, so the Owner reviews the monthly account reconciliation (B.5) at the monthly security check-in. The Senior Technician administers the bench and also uses it, so bench access is logged once EDR is in place, and the independent assessor checks it each year (A.6).

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security and Privacy Lead.** The Shop Manager is the designated Security and Privacy Lead. The Owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02; PCI DSS 12.1.3)

A.2 **Risk assessment.** The Shop Manager must update the risk assessment every July, and after a major change such as a new ticketing platform, a second location, or a new AI feature, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-05)

A.3 **Risk acceptance.** The Shop Manager may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. (PM-9; GV.RM-02)

A.4 **Sanctions.** A workforce member who breaks a security or privacy rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. Browsing or copying customer device content outside the access standard (POL-04 4.4) is serious misconduct. The Shop Manager records each sanction; the Owner approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **No terms, no customer data.** No vendor, tool, or feature may receive customer information or customer devices until the Shop Manager has done a vendor check (what data, where it goes, security evidence) and written terms are in place: confidentiality, use only for the shop's job, deletion at the end of the job or contract, and breach notice to the shop within 10 days. That includes free tools, trials, and new features in existing SaaS (such as AI assistants). The Shop Manager keeps a vendor list showing each vendor's data, criticality, and whether it handles or can affect card data. (SA-9; GV.SC-05; GV.SC-06; Fla. Stat. 501.171(6); PCI DSS 12.8.1-12.8.3)

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them. Each year before signing the SAQ, the Shop Manager checks the processor's PCI DSS attestation and P2PE listing. (CA-2; PCI DSS 12.8.4)

A.7 **Records.** Policies, risk assessments, assessments, incident records, training records, sanitization records, and sanction records must be kept for at least 5 years. (SI-12; GV.PO-02)

A.8 **Policy review and access to policies.** The Shop Manager must review this policy set every August and after any incident or major change, and keep the current version in the productivity suite where every workforce member can read it. (PL-1; GV.PO-02; PCI DSS 12.1.2)

A.9 **Exceptions and changes.** An exception to any security policy, and any new tool or feature that touches customer data, must be requested in writing, rated on the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; CM-3; GV.PO-01)

A.10 **Background checks and confidentiality.** Anyone who will handle customer devices must pass a background check before starting, and every workforce member must sign the customer data confidentiality agreement at hire. Background reports are handled under POL-04 4.7. (PS-3; PS-6; GV.RR-04)

### Part B. Access control
B.1 **Unique accounts.** Every workforce member must have their own account in SYS-01, the productivity suite, the merchant portal (if needed), and the bench workstations. Shared or generic logins, including a shared counter login, are not allowed. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access must match the person's job. In SYS-01: Counter Associates get the counter role; technicians get the technician role, without export rights; only the Owner and the Shop Manager hold administrator or manager roles. The restricted passcode field (POL-04 4.3) is visible only to the technician assigned to the ticket and the Shop Manager. The Shop Manager approves access in writing on the joiner checklist. (AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for SYS-01, the productivity suite, the merchant portal, and every administrator login, including logins held by the MSP (backup console, firewall, remote management) and the bench storage administrator account. (IA-2(1); PR.AA-03)

B.4 **Leavers.** On or before a workforce member's last day, the Shop Manager must complete the leaver checklist: disable SYS-01, suite, portal, and bench accounts; ask the MSP to remove device access; change the back room keypad code and the staff Wi-Fi password; collect keys and any company USB drives; and remind the person in writing of their confidentiality duty. For an involuntary departure, access is disabled before the person is told. (PS-4; AC-2; PE-3)

B.5 **Monthly reconciliation.** Each month the Shop Manager compares the user lists of SYS-01, the suite, the merchant portal, the backup console, and the bench workstations with the staff roster, removes anything that does not match, and checks that no technician holds export rights. The Owner reviews the result at the monthly security check-in. (AC-2; AC-6; PR.AA-05)

B.6 **Locking.** Counter PCs, laptops, and bench PCs must lock after 10 minutes idle. Counter PCs must not stay signed in to SYS-01 overnight. (AC-11)

B.7 **Vendor and MSP access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the Shop Manager a current list of technicians with access every year. Remote desktop tools may be installed only with the Shop Manager's approval. (AC-17; IA-2(1); SA-9)

B.8 **Passwords.** Passwords must be at least 12 characters, never reused from personal accounts, and never written on devices or labels. Default administrator accounts must be disabled or renamed with a new password before a device is used. (IA-5)

B.9 **Physical access.** Only workforce members enter the back repair room. Finished devices, customer drives, and the spare payment terminal are kept in locked cabinets. (PE-3; PR.AA-06)

### Part C. Staff use rules (essentials of POL-05)
C.1 Shop systems are for shop work. Workforce members must access only the customer information their job needs.

C.2 Workforce members must not store or send customer information or device content with personal email, personal cloud storage, personal phones, messaging apps, or personal USB drives. Only company-issued encrypted USB drives may hold customer data, and only for a transfer job (POL-04 4.4). (PL-4; MP-7)

C.3 Workforce members must lock their screen when stepping away and never share passwords or MFA codes, including with the MSP or a caller claiming to be a vendor. (AC-11; PL-4)

C.4 Workforce members must complete security, privacy, and payment terminal training at hire and every year, and take part in phishing simulations. (AT-2; PR.AT-01; PCI DSS 9.5.1.3, 12.6.1)

C.5 Workforce members must report suspected incidents at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.6 Workforce members must sign an acknowledgment of POL-02, POL-03, and POL-04 at hire and after each annual update. (PL-4; PCI DSS 12.1.3)

C.7 Any request to change a vendor's or employee's bank details must be confirmed by phone to a number already on file, never to a number in the request. (AT-2; PR.AT-01)

C.8 Only AI tools on the approved list (POL-04 4.8) may be used for shop work, and never with customer data unless the tool is approved for it. (PL-4; SA-9)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Shop Manager checks compliance through the monthly reconciliation (B.5), the monthly log review (POL-04 4.9), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; joiner and leaver checklists; customer data confidentiality agreement; vendor list; P01 risk register; P02 SSP control statements AC-2, AC-6, IA-2(1), PS-4, PS-6

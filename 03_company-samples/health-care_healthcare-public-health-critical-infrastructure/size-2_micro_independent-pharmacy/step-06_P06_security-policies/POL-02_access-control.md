# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent community pharmacy) |
| Policy ID | POL-02 |
| Owner | Store Manager (Privacy Officer and Security Officer) |
| Approved by | Pharmacist-owner, 2026-08-28 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-4, SA-9, SI-12, CA-2. Part B: AC-1, AC-2, AC-3, AC-5, AC-6, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-4, SC-12. Part C: PL-4, AT-2, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, GV.SC-07, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01 |
| HIPAA Security Rule | 164.308(a)(1), (a)(1)(ii)(A)-(C), (a)(2), (a)(3), (a)(4), (a)(5), (a)(8), (b)(1); 164.310(b), (c); 164.312(a), (d); 164.316 |
| DEA | 21 CFR 1311.200(a)-(b), (e); 1311.205(a), (b)(10); 1311.30(a)-(d) |

**Why this policy has three parts.** A 7-person pharmacy does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01) and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the pharmacy's security program, make sure only authorized people reach patient, prescription, and controlled substance information and only as far as their job requires, and tell the workforce how to use pharmacy systems.

## 2. Scope
All workforce members of Cris Santos Company: both pharmacists, technicians, the front-store clerk, the delivery driver, and any temporary or relief staff, interns, or students. It covers every system and every copy of pharmacy information, including systems run for the pharmacy by the MSP and SaaS vendors (SYS-01 to SYS-09 in `../00_company-facts.md`), and the DEA CSOS certificate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Pharmacist-owner | Approves policies and the security budget; accepts Moderate risk; decides sanctions with the Store Manager; decides who may alter controlled substance records; holds the CSOS certificate; backup PMS administrator |
| Store Manager | Privacy Officer and Security Officer; runs this policy; grants and removes access; reviews accounts and logs; primary PMS administrator. Because the Store Manager both administers and checks access, the pharmacist-owner reviews the PMS administrator log each month |
| Staff Pharmacist | Covers the pharmacist-owner's duties under this policy on days the owner is away, except risk acceptance and budget |
| MSP | Creates and disables suite and device accounts on the Store Manager's request; operates device controls |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security and Privacy Officer.** The Store Manager is the designated HIPAA Security Officer and Privacy Officer. The pharmacist-owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02; 164.308(a)(2))

A.2 **Risk analysis.** The Store Manager must update the risk analysis every July, and after any major change such as a new PMS release with new clinical features, new packaging equipment, or a new vendor handling ePHI, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01; 164.308(a)(1)(ii)(A)-(B))

A.3 **Risk acceptance.** The Store Manager may accept Low and Very Low risks. Only the pharmacist-owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the pharmacist-owner. A risk of patient harm or of breaking a DEA or Florida controlled substance duty must not be accepted at Moderate or above. (PM-9; GV.RM-01)

A.4 **Sanctions.** A workforce member who breaks a security or privacy rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Store Manager must record each sanction, and the pharmacist-owner must approve suspension or termination. The employee handbook must point to this rule. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

A.5 **No BAA, no ePHI.** No vendor may create, receive, maintain, or transmit ePHI for the pharmacy until a business associate agreement is signed or accepted. That includes free apps, trials, and equipment vendors with remote access. The Store Manager keeps every BAA in the BAA folder and checks each year that the MSP holds BAAs with its own subcontractors. (SA-9; GV.SC-05; 164.308(b)(1); 164.314(a))

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; 164.308(a)(8))

A.7 **Retention.** Security policies, procedures, risk analyses, assessments, incident records, BAAs, training records, and sanction records must be kept for 6 years from the date created or the date last in effect, whichever is later. Electronic controlled substance prescription records are kept electronically for at least 2 years (21 CFR 1311.305(b); Fla. Stat. 893.07(4)); the PMS keeps them for the life of the contract. (SI-12; GV.PO-02; 164.316(b)(2)(i))

A.8 **Policy review and access to policies.** The Store Manager must review this policy set every August and after an incident or major change, and must keep the current version in the shared drive and a printed copy at the pharmacist verification station. (PL-1; GV.PO-02; 164.316(b)(2)(ii)-(iii))

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

A.10 **EPCS application compliance.** The pharmacy may process electronic controlled substance prescriptions only in a pharmacy application whose current third-party EPCS audit or certification report has been obtained and reviewed by the pharmacist-owner. The pharmacist-owner must record the determination, including any information the report says the application cannot handle, and repeat it for each new report (at least every two years). (SA-4; SA-9; GV.SC-07; 21 CFR 1311.200(a)-(b); 1311.205(a))

### Part B. Access control
B.1 **Unique accounts.** Every workforce member must have their own account in the PMS, the productivity suite, the fax portal, the delivery app, and the computer they use. Shared or generic accounts are not allowed, including the counter desktop and packaging software logins. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i); 21 CFR 1311.205(b)(10))

B.2 **Least privilege and controlled substance records.** Access must match the person's job, using the PMS role list:

| Job | PMS role | May annotate or alter dispensed controlled substance records |
|---|---|---|
| Pharmacist-owner, Staff Pharmacist | Pharmacist | Yes |
| Store Manager | Technician plus administrator (no controlled substance alteration) | No |
| Lead Pharmacy Technician, Pharmacy Technician | Technician | No |
| Front-Store Clerk | Clerk (pickup and register) | No |
| Delivery Driver | None (delivery app only) | No |

The pharmacist-owner decides who may enter dispensing information and annotate or alter controlled substance records, and the PMS permission must be set to match this table. The Store Manager must approve other access in writing on the onboarding checklist before it is granted. PMS administrator roles are limited to the Store Manager and the pharmacist-owner as backup. (AC-2; AC-3; AC-5; AC-6; PR.AA-05; 164.308(a)(4)(ii)(B)-(C); 21 CFR 1311.200(e))

B.3 **MFA.** MFA is required for the productivity suite, PMS sign-in from inside and outside the store (in-store as soon as the vendor's option is enabled), the fax portal where offered, and every administrator login, including logins held by the MSP (backup console, firewall, remote management). MFA prompts must use number matching. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d))

B.4 **Termination.** On or before a workforce member's last day, the Store Manager must complete the termination checklist: disable PMS, suite, fax, and delivery app accounts; ask the MSP to remove device access; remove MFA registrations; collect keys and change the alarm code; and remind the person in writing of their confidentiality duty. For an involuntary termination, access must be disabled before the person is told. (PS-4; AC-2; 164.308(a)(3)(ii)(C))

B.5 **Monthly reconciliation.** Each month the Store Manager must compare the user lists of the PMS, suite, fax portal, delivery app, and backup console with the staff roster, and remove anything that does not match. Every quarter the Store Manager and the pharmacist-owner must confirm each person's PMS role, including the controlled substance permission in B.2, still fits their job. (AC-2; AC-6; PR.AA-05; 164.308(a)(4)(ii)(C))

B.6 **Locking and sessions.** Computers must lock after 10 minutes idle, and the PMS must end sessions after 15 minutes idle. Staff must sign in to the PMS as themselves for each task and must never work under another person's open session, because the PMS records the signed-in user as the person who dispensed. No computer is exempt; screens are placed out of patients' view. (AC-11; AC-12; 164.310(c); 164.312(a)(2)(iii); 21 CFR 1311.205(b)(10))

B.7 **Emergency access.** A sealed copy of a PMS administrator credential must be kept by the pharmacist-owner for use when the Store Manager is unavailable. Any use must be reported to the Store Manager and the password changed afterwards. (AC-2; 164.312(a)(2)(ii))

B.8 **Vendor and MSP access.** MSP technicians and vendor support staff must use named accounts with MFA. The packaging equipment vendor may connect to the packaging workstation only when a pharmacy staff member opens the session on request, and each session must be logged. The MSP must give the Store Manager a current list of technicians with access every year. (AC-17; MA-4; IA-2(1); SA-9)

B.9 **Passwords and shared secrets.** Passwords must be at least 12 characters and never reused from personal accounts. Browsers must not save passwords for the PMS, the CSOS certificate, or administrator logins. Each computer must have a unique local administrator password managed by the MSP. The staff Wi-Fi password must be changed every year and whenever a workforce member leaves. (IA-5; 164.308(a)(5)(ii)(D))

B.10 **CSOS certificate.** Only the person named on a CSOS certificate may use its private key, and only on their own computer account. The holder must store the key securely, must not copy it, must not share its password, and must never let anyone else sign an order with it. Anyone else who needs to sign Schedule II orders must obtain their own certificate under a power of attorney from the registrant. (SC-12; IA-5; AC-6; 21 CFR 1311.30(a)-(d); 1311.25(a))

### Part C. Workforce use rules (essentials of POL-05)
C.1 Pharmacy systems are for pharmacy work. Workforce members must access only the patient information they need for their job, and never their own, family members', or neighbors' records unless they are filling that prescription as part of their job. (PL-4; PR.AT-01; 164.310(b))

C.2 Workforce members must not store or send ePHI with personal email, personal cloud storage, personal messaging apps, unapproved apps, or public AI chatbots. POL-04 section 4.6 lists the approved tools. (PL-4; 164.310(b))

C.3 Workforce members must lock their screen when stepping away, keep screens out of patients' view, and never share passwords or MFA codes, including with the MSP or a vendor. (AC-11; PL-4; 164.310(b)-(c))

C.4 Workforce members must complete security and privacy training at hire and every year, and must take part in phishing simulations. Pharmacists also complete the EPCS, PDMP, and CSOS module. (AT-2; PR.AT-01; 164.308(a)(5))

C.5 Workforce members must report suspected incidents at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.6 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Store Manager checks compliance through the monthly reconciliation (B.5) and log review; the pharmacist-owner checks the Store Manager's own access through the monthly PMS administrator log review; the annual independent assessment (P07) checks both.

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; PMS role list; P01 risk register; P02 SSP control statements AC-2, AC-6, IA-2(1), IA-5, PS-4, PS-8; P03 gap analysis rows for 21 CFR 1311.200(e) and 1311.30

# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (Security Coordinator) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, SR-8, SI-12, CA-2. Part B: AC-2, AC-3, AC-6, AC-11, AC-17, AC-18, IA-2, IA-2(1), IA-5, MA-4, PS-4, SC-7, AU-6. Part C: PL-4, AT-2 |
| CSF 2.0 | GV.OC-03, GV.RR-02, GV.RR-04, GV.RM-02, GV.PO-01, GV.SC-05, ID.RA-05, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.IR-01, DE.CM-06 |
| Binding duties carried | FAR 52.204-21(b)(1)(i)-(vi), (x)-(xi); G&T cooperative exhibit sec. 3 (CIP-013-2 R1.2.3 flow-down); Fla. Stat. 501.171(2) |

**Why this policy has three parts.** A 7-person shop does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the shop's security program, make sure only authorized people and vendors reach shop systems and equipment and only as far as their job requires, and tell everyone how to use shop systems.

## 2. Scope
All employees of Cris Santos Company and anyone working for it, including temporary staff. It covers every system and copy of company information, including systems run for the shop by the MSP and SaaS vendors, and the shop equipment that connects to a network or to a vendor: the test PC and test set, the drying oven controls and the OEM modem, the winding machine, and the camera recorder.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate and higher risk; decides sanctions with the Office Manager; approves any internet-facing connection |
| Office Manager | Security Coordinator; runs this policy; grants and removes access; reviews accounts and logs; keeps the obligations list |
| Shop Manager | Owner of shop equipment; approves every vendor session on shop equipment |
| MSP | Creates and disables suite and computer accounts on the Office Manager's request; operates the firewall, Wi-Fi, and computer controls |
| All employees | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Roles.** The Office Manager is the Security Coordinator. The Shop Manager owns the security of shop equipment. The Owner must record both designations in writing and update them within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Office Manager must update the risk assessment every July, and after any major change such as a new system, a new vendor with remote access, new shop equipment, or a new customer security term, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-05)

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. A risk with a safety impact (oven, test bay) must not be accepted above Low. (PM-9; GV.RM-02)

A.4 **Sanctions.** An employee who breaks a security rule must be dealt with in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Office Manager records each case, and the Owner approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **No terms, no access.** No vendor may receive remote access to shop systems or equipment, or hold Restricted information, until written security terms are in place: MFA for its access, incident notice to the shop within 24 hours, and return or deletion of data at the end. Existing vendors (MSP, oven OEM, test set vendor, AI vendor) must be brought under such terms by 2026-12-31. (SA-9; SR-8; GV.SC-05)

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2)

A.7 **Retention.** Security policies, risk assessments, assessments, incident records, notices, training records, and sanction records must be kept for at least 5 years, or longer where a contract requires. (SI-12)

A.8 **Policy review and access to policies.** The Office Manager must review this policy set every August and after an incident or major change, and must keep the current version in the shared drive where every employee can read it. (PL-1; GV.PO-01)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less.

A.10 **Obligations list.** The Office Manager must keep a one-page list of every legal and contract security duty (the cooperative exhibit, FAR 52.204-21, -23, and -25, Fla. Stat. 501.171), with the trigger, the deadline, and who acts. The list is reviewed each quarter and whenever a contract is signed or changed. (PM-28; GV.OC-03)

### Part B. Access control
B.1 **Unique accounts.** Every person must have their own account in the ERP, the suite, and any shop computer they use. Shared accounts are not allowed, except the test PC administrator account until the test PC is replaced (target 2026-12-31), and then only with a written log of who used it. (IA-2; AC-2; PR.AA-01; FAR 52.204-21(b)(1)(v))

B.2 **Least privilege.** Access must match the job. The Office Manager approves access in writing (the onboarding checklist) before it is granted. Administrators must use a separate administrator account only for administration. The rewind data sheet library and the federal order folder are limited to the people who need them. (AC-2; AC-3; AC-6; PR.AA-05; FAR 52.204-21(b)(1)(i)-(ii))

B.3 **MFA.** MFA is required for the ERP, the suite, the AI portal, every administrator login, and every login held by the MSP (firewall, backup service, remote management). (IA-2(1); PR.AA-03; FAR 52.204-21(b)(1)(vi))

B.4 **Leavers.** On or before a person's last day, the Office Manager must complete the leaver checklist: disable ERP, suite, and portal accounts; ask the MSP to remove computer access; remove MFA registrations; collect keys, badges, and devices; change any shared password the person knew (test PC, Wi-Fi, alarm code); and remind the person in writing of their confidentiality duty. If the person held a cooperative substation badge, the Office Manager must notify the cooperative **within 1 business day** of the decision that access should end. For an involuntary termination, access is disabled before the person is told. (PS-4; AC-2; GV.RR-04; cooperative exhibit sec. 3)

B.5 **Monthly reconciliation and review.** Each month the Office Manager must compare the user lists of the ERP, suite, AI portal, and backup service with the staff list, remove anything that does not match, and review sign-ins, administrator changes, and email forwarding rules with a checklist. The Owner signs the checklist. (AC-2; AU-6; PR.AA-05)

B.6 **Locking.** Office computers and tablets must lock after 15 minutes idle. The shop-floor PC may stay unlocked for the job board only if it is signed in with an account that can view, not change, the schedule. (AC-11)

B.7 **Remote access and vendor sessions.** Remote access to shop systems is allowed only through the MSP's remote management tool or its attended session tool. The oven OEM's cellular modem stays powered off except during a session the Shop Manager has requested and approved; the OEM must send a record of each session. No firewall port forwarding or other internet-facing connection may be created without the Owner's written approval. (AC-17; MA-4; DE.CM-06; FAR 52.204-21(b)(1)(iii))

B.8 **Networks.** Office computers, shop equipment, and guests must be on separate networks. The shop equipment network (test PC, oven HMI, camera recorder) has no Wi-Fi access and reaches the internet only for an approved vendor session. Guests and personal phones use the guest Wi-Fi only. (SC-7; AC-18; PR.IR-01; FAR 52.204-21(b)(1)(x)-(xi))

B.9 **Passwords and shared secrets.** Passwords must be at least 12 characters and never reused from personal accounts. The staff Wi-Fi password must not be posted or given to visitors, and must be changed every year and whenever an employee leaves. (IA-5)

B.10 **Emergency access.** A sealed copy of an ERP and suite administrator credential is kept by the Owner for use when the Office Manager is unavailable. Any use is reported to the Office Manager and the password changed afterwards. (AC-2)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Shop systems are for shop work. Look only at the information your job needs. (PL-4; PR.AT-01)

C.2 Do not store or send company information with personal email, personal cloud storage, or personal messaging apps. Do not plug personal USB sticks or phones into the test PC, the oven HMI, or the winding machine. AI tools follow POL-04 4.7. (PL-4; FAR 52.204-21(b)(1)(iii))

C.3 Lock your screen when you step away. Never share passwords or MFA codes, including with the MSP or a vendor on the phone. (AC-11; PL-4)

C.4 Complete security training at hire and every year, and take part in phishing simulations. (AT-2; PR.AT-01)

C.5 Report suspected incidents at once under POL-03 section 4.2, including your own mistakes and anything odd on shop equipment. (IR-6)

C.6 Sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

C.7 **Payment changes.** Never change a supplier's or customer's bank details, or send a payment to new details, based on an email or text. Call the supplier back on the number already in the ERP, and record the call. (PL-4; AT-2)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Office Manager checks compliance through the monthly reconciliation (B.5) and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and leaver checklists; obligations list; P01 risk register; P02 SSP control statements AC-2, AC-17, IA-2(1), MA-4, PS-4, SC-7

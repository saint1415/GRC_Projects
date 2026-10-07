# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Community Federal Credit Union |
| Policy ID | POL-02 |
| Owner | Operations Manager (Information Security Officer and Privacy Officer) |
| Approved by | Board of Directors, 2026-08-25 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, RA-3, PS-8, SA-9, CA-2, PL-1, SI-12. Part B: AC-2, AC-3, AC-5, AC-6, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, PS-4. Part C: PL-4, AT-2, AT-2(3), IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01 |
| NCUA Part 748 | 748.0(a), (b)(2); Appendix A II.A, III.A, III.B, III.C.1.a, III.C.1.e, III.C.2, III.C.3, III.D, III.E, III.F |

**Why this policy has three parts.** A 7-person credit union does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01) and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the credit union's information security program as 12 CFR 748.0 requires, make sure only authorized people reach member information and member money and only as far as their job requires, and tell the workforce how to use credit union systems.

## 2. Scope
All employees, volunteers with system access (board and Supervisory Committee members who use credit union email), temporary staff, and vendors with access. It covers every member information system (Appendix A I.B.2.e), including systems run for the credit union by the core processor, the digital banking provider, the corporate credit union, the MSP, and SaaS vendors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board of Directors | Approves this policy and the written program; receives the annual report; accepts High risks |
| President and CEO | Accepts Moderate risks; approves spending and sanctions |
| Operations Manager (ISO) | Runs this policy; grants and removes access; reviews logs and accounts; manages vendors |
| Accounting and Compliance Officer | Backup for access removal; reviews core override and employee-account reports |
| MSP | Creates and disables suite, device, and cloud accounts on the ISO's request; operates device controls |
| All workforce | Protect credentials and tokens; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Information Security Officer.** The board must designate the ISO in writing and update the designation within 30 days of any change. The ISO is also the Privacy Officer. (PM-2; GV.RR-02; App. A III.A.2)

A.2 **Risk assessment.** The ISO must update the risk assessment every July, and after any major change such as a new core processor, a new online service, or expanding the AI scoring pilot, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01; App. A III.B.1-3)

A.3 **Risk acceptance.** The ISO may accept Low and Very Low risks. Only the President and CEO may accept a Moderate risk. High and Very High risks must not be accepted by management; the board approves a dated treatment plan and hears progress each month. (PM-9; GV.RM-01)

A.4 **Sanctions.** A workforce member who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The ISO records each sanction; the President and CEO approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Service providers.** Before a vendor or a new vendor feature receives or reaches member information, the ISO must complete the due diligence checklist and confirm the contract requires appropriate security measures and prompt incident notice. Each year the ISO must review the SOC report (or equivalent) of every critical vendor, map the complementary user entity controls to credit union controls, and report exceptions to the President and CEO. (SA-9; GV.SC-05; GV.SC-07; App. A III.D.1-3; App. B II)

A.6 **Independent testing.** Key controls must be tested at least once a year by someone who does not operate them, engaged by the Supervisory Committee. (CA-2; App. A III.C.3)

A.7 **Board reporting.** The ISO must give the board a written report each August on the program's status and compliance with Appendix A, covering the risk assessment, risk decisions, service providers, test results, incidents and responses, and recommended changes, and a one-page status each quarter. (PM-9; GV.OV-01; App. A III.F)

A.8 **Policy review and access to policies.** The ISO must review this policy set every August and after an incident or major change, and keep the current version where every workforce member can read it. (PL-1; GV.PO-02; App. A III.E)

A.9 **Retention.** Security policies, risk assessments, assessments, incident records, vendor reviews, training records, and sanction records must be kept at least 5 years. (SI-12; GV.PO-02)

A.10 **Exceptions.** An exception to any security policy must be requested in writing, rated with the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Unique accounts.** Every person must have their own account in the core, the admin console, the wire portal, the LOS, the suite, and the cloud console. Shared sign-in accounts are not allowed. A shared mailbox may exist only as a mailbox that named users reach through their own accounts. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access must match the person's job. The ISO approves access in writing (the onboarding checklist) before it is granted. The core supervisor override profile is limited to the Senior MSR, the Operations Manager, and the Accounting and Compliance Officer. (AC-2; AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for the suite, the online banking admin console, the wire portal (hardware token), the LOS, the cloud console, and every administrator login, including logins held by the MSP. Where a vendor offers no MFA (core teller users), access must be limited to the office IP address. (IA-2(1); IA-2(2); PR.AA-03; App. A III.C.1.a)

B.4 **Termination.** On or before a person's last day, the ISO must complete the termination checklist: disable core, admin console, wire portal, LOS, suite, and cloud accounts; collect the wire token, keys, and devices; change any password the person knew (including Wi-Fi and alarm codes); and remind the person in writing of their confidentiality duty. For an involuntary termination, access is disabled before the person is told. (PS-4; AC-2)

B.5 **Monthly reconciliation.** Each month the ISO must compare the user lists of the core, admin console, wire portal, LOS, suite, and cloud console with the staff roster and remove anything that does not match. Each quarter the ISO must confirm each person's role profile still fits their job. (AC-2; AC-6; PR.AA-05)

B.6 **Locking.** Computers must lock after 10 minutes idle. Teller stations are not exempt; tellers lock the screen when leaving the station. (AC-11)

B.7 **Member authentication.** Online banking must require a second factor when a member signs in from a new device and when a member changes their phone number, email address, or payees. Members must get alerts for those changes and for transfers above the alert threshold. A change to a member's phone number or email made through staff must be confirmed by a call to the number already on file or in person with ID. (IA-8; PR.AA-03; App. A III.C.1.a; 12 CFR 717.90)

B.8 **Vendor and MSP access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the ISO a current list of technicians with access every year and on request. (AC-17; IA-2(1); SA-9)

B.9 **Passwords.** Passwords must be at least 12 characters and never reused from personal accounts. A password known to more than one person (for example the alarm code) must be changed when any of them leaves. (IA-5)

B.10 **Wire security procedure.** For every outgoing wire request not made in person with ID:
- the MSR must call the member at the phone number already on file, never a number or link in the request, and confirm the amount, beneficiary, and account;
- an emailed request or emailed change to wire instructions is never enough on its own, even from the member's usual address;
- the callback (number called, time, person reached, and the MSR's initials) must be recorded in the wire file before keying;
- the approver must see the callback record before approving in the portal; no record, no approval.

The member agreement for wire transfers must describe this callback as the credit union's security procedure. (IA-8; AC-5; AT-2(3); App. A III.C.1.a, III.C.1.e; Fla. Stat. 670.202)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Credit union systems are for credit union work. Workforce members may look only at the member information their job needs, and never at their own, family members', or friends' accounts except to serve them in the normal course with another employee present in the record. (PL-4; PR.AT-01)

C.2 Workforce members must not store or send member information with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. POL-04 section 4.6 lists the approved tools. (PL-4)

C.3 Workforce members must lock their screen when stepping away and never share passwords, MFA codes, or wire tokens, including with the MSP or a caller who claims to be a vendor. (AC-11; PL-4)

C.4 Workforce members must complete security training at hire and every year, including business email compromise, wire fraud red flags, and pretext calls, and must take part in phishing exercises. (AT-2; AT-2(3); PR.AT-01; App. A III.C.2)

C.5 Workforce members must report suspected incidents at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.6 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The ISO checks compliance through the monthly reconciliation (B.5), monthly log review, monthly sampling of wire files for callback records, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.10. No exception may be granted to B.10.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; wire transfer member agreement; Identity Theft Prevention Program; P01 risk register; P02 SSP control statements AC-2, AC-5, IA-2(1), IA-8, PS-4

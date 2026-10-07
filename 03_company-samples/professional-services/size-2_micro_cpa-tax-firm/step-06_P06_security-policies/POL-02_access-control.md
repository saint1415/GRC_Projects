# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (Qualified Individual) |
| Approved by | Owner CPA, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after material changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-1, PM-2, PM-9, RA-3, PS-8, SA-9, CA-2, SI-12, PL-1, CA-5. Part B: AC-2, AC-3, AC-6, AC-11, AC-17, AC-19, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, PS-4, PS-6, CM-3, AU-6, SI-4. Part C: PL-4, AT-2, IR-6, SC-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OC-03, GV.SC-05, GV.SC-07, ID.RA-01, ID.IM-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.PS-01, DE.AE-02 |
| FTC Safeguards Rule (N54-R01) | 314.3(a); 314.4(a), (b), (b)(2), (c)(1), (c)(5), (c)(7), (c)(8), (d)(1), (e)(1), (f), (g) |
| IRC 7216 (N54-R02) | 26 CFR 301.7216-1(a); 301.7216-2(d)(2) |

**Why this policy has three parts.** A 7-person firm does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

**This policy set is the firm's WISP.** The Safeguards Rule requires a written information security program "in one or more readily accessible parts" (314.3(a)). The firm's program is: POL-02, POL-03, and POL-04; the system security plan (P02); the risk register (P01); and the incident response runbook (P08). It replaces the 2024 WISP built from the IRS Pub. 5708 template.

## 1. Purpose
Set up the firm's information security program, make sure only authorized people reach client and firm information and only as far as their job requires, and tell the workforce how to use firm systems safely.

## 2. Scope
All workforce members of Cris Santos Company: the Owner CPA, employees, seasonal and temporary staff, and interns. It covers every system and every copy of client and firm information, including systems run for the firm by the MSP and SaaS vendors, and firm email on staff-owned phones.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner CPA | Senior person responsible for the program; approves policies and the security budget; accepts Moderate risk; decides sanctions with the Office Manager |
| Office Manager (Qualified Individual) | Runs this policy; grants and removes access; reviews logs and accounts; directs the MSP |
| Senior Tax Accountant | Administers tax software users and roles |
| Client Services Coordinator | Administers portal staff accounts and client portal settings |
| MSP | Creates and disables suite accounts and makes security changes on the Office Manager's approval; operates device controls |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Qualified Individual.** The Office Manager is the Qualified Individual responsible for overseeing, implementing, and enforcing the program. The Owner CPA must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02; 314.4(a))

A.2 **Written program.** The Office Manager must keep a one-page index of the parts of the written program (listed above) in the shared policy folder, readable by every workforce member, and update it when a part changes. (PM-1; GV.PO-01; 314.3(a); Form W-12 line 11)

A.3 **Risk assessment and consumer count.** Every July, and after any material change (a new system holding client data, a new AI tool, or buying a client list), the Office Manager must update the risk assessment using NIST SP 800-30 Rev. 1 and recount the consumers whose information the firm holds. If the count reaches 4,500, the Office Manager must tell the Owner CPA and plan for the four elements that 314.6 now exempts. (RA-3; ID.RA-01; 314.4(b), (b)(2); 314.6)

A.4 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the Owner CPA may accept a Moderate risk, with a treatment plan or a written reason. High and Very High risks must not be accepted; they need a dated treatment plan, approved by the Owner CPA, due before the next filing season. (PM-9; GV.RM-01)

A.5 **Sanctions.** A workforce member who breaks a security rule or discloses tax return information without permission must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Office Manager records each sanction; the Owner CPA approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04; 301.7216-1(a))

A.6 **Service providers.** Before any vendor receives client information, the Office Manager must check that it can protect it (POL-04 4.5), and the contract must require safeguards and notice of any breach. Each year the Office Manager reviews the tax software vendor's SOC 2 report, the MSP's security evidence, and the portal and payroll vendors' security evidence. Every contractor technician who may see tax return information must sign the written notice of IRC sections 6713 and 7216 before access. (SA-9; GV.SC-05; GV.SC-07; 314.4(f)(1)-(3); 301.7216-2(d)(2))

A.7 **Testing.** Key controls must be tested at least once a year by someone who does not operate them, and the MSP must run a quarterly external vulnerability scan of the office firewall and report the results. (CA-2; ID.IM-01; 314.4(d)(1))

A.8 **Retention of security records.** Policies, risk assessments, assessments, incident records, training records, signed 7216 notices, and sanction records must be kept for at least 5 years. (SI-12; GV.PO-02)

A.9 **Policy review and program adjustment.** The Office Manager must review this policy set every August, and after an incident, a test result that shows a weakness, or a material change, and must update the program to match. (PL-1; GV.PO-02; 314.4(g))

A.10 **Monthly program review.** The Office Manager meets the Owner CPA for 30 minutes each month to review the POA&M, new risks, incidents, and vendor issues, and keeps short notes. This is the firm's light version of the 314.4(i) report, which is not required at this size. (CA-5; ID.IM-01; 314.6)

A.11 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.4, recorded in the risk register, and limited to 12 months or less. An exception to MFA or encryption also needs the Qualified Individual's written approval of the compensating control. (PL-1; GV.PO-01; 314.4(c)(3), (c)(5))

### Part B. Access control
B.1 **Unique accounts.** Every workforce member must have their own account in the tax software, the suite, the portal, and the payroll and client accounting platforms. Shared or generic accounts are not allowed. A device that must send mail (the MFP) uses a send-only method approved by the Office Manager, never a mailbox that can be signed in to. (IA-2; AC-2; PR.AA-01; 314.4(c)(1)(i))

B.2 **Least privilege.** Access must match the person's job. Client folders are grouped so that payroll files are open only to the Bookkeeper and the Owner CPA, and the seasonal assistant reaches only the current season's intake folders. The Office Manager approves access in writing (the onboarding checklist) before it is granted. (AC-3; AC-6; PR.AA-05; 314.4(c)(1)(ii))

B.3 **MFA.** MFA is required for every account in every system that holds client information, including the tax software, the suite (with number matching), the portal for staff and, from 2027-01-15, for clients, the payroll and client accounting platforms, and every administrator login, including logins held by the MSP (backup console, firewall, remote management). Legacy authentication that bypasses MFA is blocked. Any exception needs the Qualified Individual's written approval under A.11. (IA-2(1); IA-2(2); IA-8; PR.AA-03; 314.4(c)(5))

B.4 **Administrator accounts.** Administrator rights in the suite and the tax software are used only from separate administrator accounts, never from the account used for email. Two break-glass suite administrator accounts are sealed, kept by the Owner CPA, and tested twice a year. (AC-6; IA-2(1); PR.AA-05)

B.5 **Onboarding.** New staff, including seasonal staff, complete security and IRC 7216 training and sign the Part C acknowledgment before they receive access. Seasonal accounts are created with an end date no later than the end of the season. (PS-6; AT-2; PR.AT-01)

B.6 **Termination.** On or before a workforce member's last day, the Office Manager completes the termination checklist: disable the suite, tax software, portal, payroll and client accounting platform, and AI assistant accounts; remove MFA registrations and the firm mail profile from the person's phone; collect keys and devices; and remind the person in writing of their duties under IRC 7216. For an involuntary termination, access is disabled before the person is told. (PS-4; AC-2; PR.AA-05; 314.4(c)(1)(i))

B.7 **Monthly reconciliation.** Each month the Office Manager compares the user lists of the suite, tax software, portal, payroll platform, AI assistant, and backup console with the staff roster and removes anything that does not match. Every quarter the Office Manager confirms that each person's roles and folders still fit their job. (AC-2; AC-6; PR.AA-05; 314.4(c)(1))

B.8 **Devices and phones.** Computers lock after 10 minutes idle, with no exemptions; a front-desk screen is placed out of clients' view instead. Firm email on a staff-owned phone is allowed only through the suite app with app protection (PIN and remote wipe of firm data). (AC-11; AC-19; PR.AA-03)

B.9 **MSP and vendor access.** MSP technicians and vendor support staff use named accounts with MFA. The MSP gives the Office Manager a current list of technicians with access every year, and each one signs the IRC 6713 and 7216 notice (A.6). (AC-17; PS-6; SA-9; 301.7216-2(d)(2))

B.10 **Changes.** The MSP may change the firewall, suite security settings, backup settings, or MFP settings only after the Office Manager approves the change by email or ticket. Each change is recorded in the change log. Emergency changes are recorded the same day. (CM-3; PR.PS-01; 314.4(c)(7))

B.11 **Logging and review.** Suite alerts for new inbox rules, external forwarding, risky sign-ins, and mass downloads go to the Office Manager and the MSP. Audit logs are kept for at least one year. Each month the Office Manager reviews the alerts, tax software access by user, and bank account changes on returns, using a checklist. (AU-6; SI-4; DE.AE-02; 314.4(c)(8))

B.12 **Passwords.** Passwords are at least 14 characters and never reused from personal accounts. Default passwords on devices (the MFP, the firewall, Wi-Fi) are changed at installation. The staff Wi-Fi password changes every year and whenever someone leaves. (IA-5; PR.AA-01)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Firm systems are for firm work. Workforce members open only the client files they work on and never look up friends, family, or neighbors without a work reason. (PL-4; PR.AT-01; 301.7216-1(a))

C.2 Workforce members must not store or send client information with personal email, personal cloud storage, personal messaging apps, or any AI tool that is not on the approved list in POL-04 4.7. (PL-4; 301.7216-1(a))

C.3 **Call-back rule.** Any request to change a refund bank account, a payroll employee's bank account, a vendor's payment details, or a client's address or email must be confirmed by phone on the number already on file before the change is made. A request that arrives only by email or portal message is never enough. (AT-2; PR.AT-01)

C.4 Returns and source documents go to clients through the portal. Staff must not email them as plain attachments; if a client cannot use the portal, use the suite's encrypted email. (SC-8; 314.4(c)(3))

C.5 Workforce members lock their screen when stepping away, never share passwords or MFA codes (including with the MSP), and never approve an MFA prompt they did not start. An unexpected prompt is reported at once. (AC-11; PL-4)

C.6 Workforce members complete security and IRC 7216 training at hire, before access, and every year before the filing season, and take part in phishing simulations. (AT-2; PR.AT-01; 314.4(e)(1))

C.7 Workforce members report suspected incidents at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.8 Workforce members sign an acknowledgment of this policy and of the IRC 7216 and 6713 rules at hire and after each annual update. (PL-4; PS-6)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.5. The Office Manager checks compliance through the monthly reconciliation (B.7), the monthly log review (B.11), the monthly program review (A.10), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.11.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; change log; P01 risk register; P02 SSP control statements AC-2, IA-2(2), PS-4, PS-6; P08 runbook

# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (security and compliance lead) |
| Approved by | Owner and President, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or new federal contract requirements |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, RA-3, PS-8, SA-9, AC-5, CA-2, SR-5, SA-4, PL-1. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, AC-18, AC-19, AC-22, IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5, PS-4, PE-3, PE-8, SC-7. Part C: PL-4, AT-2 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, GV.OV-01, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01 |
| Federal contract requirements | FAR 52.204-21(b)(1)(i)-(vi), (viii)-(x), (c) (N23-R01); FAR 52.204-25(b), (e) and 52.204-26 (N23-R02); 32 CFR 170.15, 170.22, 170.23 and DFARS 252.204-7021 (N23-R04) |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people and devices reach company and federal contract information and only as far as their job requires, protect the way the company sends and receives money, and tell the workforce how to use company systems.

## 2. Scope
All Cris Santos Company workforce members (the Owner, employees, and temporary staff) at the office, the yard, and every jobsite. It covers every company system and every copy of company information, including systems the MSP and SaaS vendors run for the company and company-issued phones and tablets wherever they are used. Subcontractors are bound through their subcontracts (A.9).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner and President | Approves policies and the security budget; accepts Moderate risk; approves every bank change and releases every payment; CMMC Affirming Official; signs federal representations |
| Office Manager | Security and compliance lead; runs this policy; grants and removes access; keeps the call-back log, key list, and inventory; MSP contact |
| Project Manager and Estimator | Adds and removes users in SYS-01; Section 889 check in submittal review |
| Superintendents | Jobsite devices, storage containers, keys, and visitors |
| MSP | Creates and disables suite and device accounts on the Office Manager's request; operates device, network, and backup controls |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security lead and Affirming Official.** The Office Manager is the designated security and compliance lead. The Owner is the CMMC Affirming Official under 32 CFR 170.22(a)(1). Both designations are recorded here and must be updated within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Office Manager must update the risk assessment every July, and after any major change such as a DoD award, a new SaaS that holds FCI, or wider use of the AI tool, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. A risk that would make a federal representation or affirmation inaccurate must be fixed, not accepted. (PM-9; GV.RM-01)

A.4 **Sanctions.** A workforce member who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Office Manager records each sanction; the Owner decides suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Vendors and external systems.** No vendor or external system may hold FCI or Restricted information (POL-04) until it is on the approved-systems list in POL-04 4.3. Before it is added, the Office Manager must check its security evidence (a SOC 2 report or a security questionnaire) and confirm contract terms covering confidentiality, incident notice, and no use of company data to train models. The MSP is reviewed every year. (SA-9; GV.SC-05; FAR 52.204-21(b)(1)(iii))

A.6 **Payment instruction changes.** Any new or changed bank details must be verified before money is sent to them. This covers a subcontractor, supplier, owner, or employee, and the company's own EFT information in SAM. Verification means all four of these steps:
- a phone call to a number already on file (never a number, link, or attachment in the requesting message);
- the Owner's approval of the change in writing before the next payment batch;
- an entry in the call-back log (date, number called, person spoken to, who verified);
- the first payment to a changed account is held 5 business days.

Urgency, seniority, or a familiar voice on an inbound call is never a reason to skip a step. The Owner reviews the SYS-02 vendor-change report every month. (AC-5; PR.AA-05; FAR 52.204-21(b)(1)(ii))

A.7 **Assessments, representations, and affirmations.** Security controls must be assessed every year by someone who does not operate them (P07). The CMMC Level 1 self-assessment must be repeated at least every year and its results entered in SPRS (32 CFR 170.15(a)(1)). CMMC affirmations in SPRS and Section 889 representations in SAM may be made only by the Owner, after the Office Manager has completed a documented evidence review and outside counsel has reviewed it. (CA-2; GV.OV-01)

A.8 **Section 889.** The company must not provide, install, or use any equipment or service from an entity named in FAR 52.204-25, or its subsidiaries or affiliates, on any project or in company operations. Every submittal and purchase of video surveillance, telecommunications, or networking equipment must name the actual manufacturer, confirmed in writing by the supplier or subcontractor. Covered equipment that is identified must be reported under POL-03 4.7. (SR-5; GV.SC-05; FAR 52.204-25(b))

A.9 **Subcontract flowdown.** Subcontracts under federal prime contracts must include the substance of FAR 52.204-21 (when the subcontractor may hold FCI) and FAR 52.204-25. Once a prime contract includes DFARS 252.204-7021, the subcontract must also carry the CMMC level required by 32 CFR 170.23, and the Owner must confirm the subcontractor's current status in SPRS before award. (SA-4; GV.SC-05)

A.10 **Policy review and exceptions.** The Office Manager must review this policy set every August and after an incident or major change, and keep the current version in the shared drive where every workforce member can read it. An exception must be requested in writing, rated on the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months. No exception may be granted against a FAR 52.204-21 requirement while the company holds or seeks a CMMC status. (PL-1; GV.PO-02)

### Part B. Access control
B.1 **Unique accounts.** Every workforce member who uses a system must have their own account. Shared or generic accounts are not allowed; the bids mailbox is reached only by delegation from named accounts. Jobsite tablets must require each user to sign in to SYS-01 with their own account. (IA-2; AC-2; PR.AA-01; FAR 52.204-21(b)(1)(i), (v))

B.2 **Least privilege.** Access must match the person's job. The Office Manager approves access in writing on the onboarding checklist before it is granted. SYS-01 company administrator rights are limited to the Project Manager and the Office Manager. Only the Office Manager and Owner may sign in to SYS-02 and the bank portal. Shared drive folders for HR, payroll, and owners' security drawings are limited to the people who need them. (AC-3; AC-6; PR.AA-05; FAR 52.204-21(b)(1)(ii))

B.3 **MFA.** MFA is required for the productivity suite, SYS-01, SYS-02, SYS-03, the bank portal, and every administrator login, including logins held by the MSP (backup console, firewall, remote management). The Owner, Office Manager, and Project Manager must use security keys for the productivity suite from 2026-10-31. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03; FAR 52.204-21(b)(1)(vi))

B.4 **Termination.** On or before a workforce member's last day, the Office Manager must complete the termination checklist: disable suite, SYS-01, SYS-02, and SYS-03 access; ask the MSP to remove device access and MFA registrations; collect keys, phones, tablets, and laptops; change any alarm code or shared lock combination the person knew. For an involuntary termination, access must be disabled before the person is told. (PS-4; AC-2; FAR 52.204-21(b)(1)(i))

B.5 **External users and reviews.** The Project Manager must remove subcontractor and design-team users from SYS-01 at project closeout. Every quarter the Office Manager must compare the user lists of the suite, SYS-01, SYS-02, SYS-03, and the bank portal with the staff roster and active projects, and remove anything that does not match. (AC-2; PR.AA-05)

B.6 **Passwords.** Passwords must be at least 12 characters, kept in the company password manager, and never reused from personal accounts. Default passwords on any device, including printers, plotters, and network equipment, must be changed before first use. (IA-5; FAR 52.204-21(b)(1)(vi))

B.7 **Devices.** Only company devices enrolled in device management may reach company email, SYS-01, or FCI. Phones and tablets must have a passcode, encryption, and remote wipe. Computers and tablets must lock after 10 minutes idle. (AC-19; AC-11; FAR 52.204-21(b)(1)(i))

B.8 **Network.** Visitors and subcontractors may use only the guest Wi-Fi, which has no route to company devices. The staff Wi-Fi password must change every year and whenever a workforce member leaves. (SC-7; AC-18; FAR 52.204-21(b)(1)(x))

B.9 **Physical access.** The Office Manager keeps a list of office keys and alarm codes; each person has an individual alarm code. Office visitors sign the visitor sheet and are escorted beyond the front area; the sheet is kept 1 year. Jobsite storage containers must be locked whenever no company employee is present, and no laptop or federal plan set may be left in a vehicle. (PE-3; PE-8; PR.AA-06; FAR 52.204-21(b)(1)(viii)-(ix))

B.10 **Public content.** No photos or details of a federal project may be posted to the website or social media without the Owner's check against the pre-posting checklist and, for federal facilities, the Contracting Officer's agreement. (AC-22; FAR 52.204-21(b)(1)(iv))

B.11 **MSP and vendor access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the Office Manager a current list of technicians with access every year. (AC-17; IA-2(1); SA-9)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Use only the systems on the approved-systems list (POL-04 4.3) for company and federal contract information. (PL-4)

C.2 **Never act on a bank change received by email, text, or an inbound call.** Pass it to the Office Manager, who follows A.6. This applies even when the message comes from someone you know, because their mailbox may be taken over. (AT-2; PR.AT-01)

C.3 Do not store or send company information through personal email, personal cloud storage, personal messaging apps, or public AI chatbots. To print drawings at a print shop, share them from SYS-01 or the shared drive, not from personal email. (PL-4; FAR 52.204-21(b)(1)(iii))

C.4 Lock your screen when stepping away. Never share passwords or MFA codes, including with the MSP. Never approve an MFA prompt you did not start; report it. (AC-11; PL-4)

C.5 Complete security awareness training at hire and every year, including the payment-fraud module, and take part in phishing simulations. (AT-2; PR.AT-01)

C.6 Report suspected incidents at once under POL-03 4.2, including your own mistakes. (IR-6)

C.7 Sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Office Manager checks compliance through the quarterly user review (B.5), the monthly vendor-change report (A.6), the monthly MSP report, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.10.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; call-back log; P01 risk register; P02 SSP control statements AC-2, AC-5, IA-2(2), PS-4, PE-3

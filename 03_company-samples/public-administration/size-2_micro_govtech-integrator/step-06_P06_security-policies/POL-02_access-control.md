# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Operations Manager (Security and Compliance Officer) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), after major changes or incidents, and within 60 days of a new CJIS Security Policy version |
| Implements (SP 800-53 Rev. 5) | Part A: PL-1, PL-2, RA-3, PS-8, SA-9, SR-6, CA-2, SI-12. Part B: AC-1, AC-2, AC-6, AC-7, AC-11, AC-17, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, PS-3, PS-4, PS-6, CM-3, CM-5, AU-6. Part C: PL-4, AT-2, PE-17 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.PS-04 |
| Contract and legal drivers | SP 800-53 Moderate (AC-02, AC-03, AC-04 contracts); CJISSECPOL v6.1 and the CJIS Security Addendum (AC-01); Pub. 1075 Exhibit 7 (SC-01); Fla. Stat. 501.171(2) |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01) and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only screened and authorized people reach agency data and only as far as their job requires, and tell staff how to use company systems.

## 2. Scope
All staff of Cris Santos Company and anyone working for it, including contractors. It covers every company system and account (SYS-01 to SYS-09), every company laptop, and the company's use of agency systems (the sheriff's file drop and identity provider, and the revenue agency's virtual desktop). It applies to all agency data and all company data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies, the security budget, and exceptions; accepts Moderate and higher risk; decides sanctions |
| Operations Manager | Security and Compliance Officer; runs this policy; tracks screening and agency terms; reviews logs and accounts; holds no administrator rights |
| Lead Platform Engineer | Creates, changes, and removes platform and SYS-02 access; applies technical settings |
| MSP | Creates and disables suite and laptop accounts on the Operations Manager's request; runs laptop controls |
| All staff | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security and Compliance Officer.** The Operations Manager is the designated Security and Compliance Officer and the security contact named in agency contracts. The owner must record the designation in writing and update it within 30 days of any change. The Lead Platform Engineer is the technical backup. (PL-1; GV.RR-02)

A.2 **Risk assessment.** The Operations Manager must update the risk assessment every July, and after any major change (a new agency customer, a new type of regulated data, a new vendor that touches agency data, or a change to the AI pre-screening), using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Operations Manager may accept Low and Very Low risks. Only the owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the owner. No one may accept a risk that would breach the CJIS Security Addendum or Pub. 1075 Exhibit 7; the risk must be treated or the access removed. (RA-3; GV.RM-01)

A.4 **Sanctions.** Staff who break a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, removal of access to agency data, or termination. The owner decides; the Operations Manager records each sanction. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **No review, no contract, no agency data.** No vendor may store, process, or reach agency data until the Operations Manager has reviewed its security evidence (FedRAMP status, SOC 2 report, or questionnaire) and the contract includes: notice of security incidents within 24 hours, U.S. data location and support, no use of agency data to train models, and return or deletion at the end. A vendor that would hold CJI also needs the agency's approval and, where the agency requires it, a CJIS Security Addendum. This applies to trials, pilots, and add-on features. (SA-9; SR-6; GV.SC-05)

A.6 **Independent assessment.** Security controls must be assessed at least once a year by someone who does not operate them. (CA-2; ID.IM-01)

A.7 **Retention of security records.** Policies, risk assessments, assessments, incident records, training records, screening confirmations, and sanction records must be kept at least 3 years after they are superseded, or longer where a contract or an agency's records retention schedule requires. Audit logs are kept 1 year (POL-04 4.7). (SI-12; GV.PO-02)

A.8 **Policy review and access.** The Operations Manager must review this policy set every August, after an incident, and within 60 days of any new CJIS Security Policy version or Pub. 1075 revision, and must keep the current version where all staff can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception must be requested in writing, rated with the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months. No exception may weaken a CJIS Security Addendum or Exhibit 7 term. (PL-1; GV.PO-01)

A.10 **Agency terms register.** The Operations Manager must keep a one-page register of each contract's security terms (recovery times, notice clocks, screening, data location, records duties) and check it against this policy set every quarter. (PL-2; GV.OC-03)

### Part B. Access control
B.1 **Unique and separate accounts.** Every person has a named account in the platform, the suite, the helpdesk, and the repository. Shared accounts are not allowed. People who administer the platform or SYS-02 must use a separate administrator account that is used for nothing else (no email, no browsing). (IA-2; AC-2; AC-6; PR.AA-01)

B.2 **Least privilege and the screening gate.** Access must match the job and be approved in writing by the Operations Manager before it is granted.
- No one may receive any role that can reach CJI (the AC-01 workspace, SYS-02, or AC-01 support tickets) until state and national fingerprint-based record checks are complete, the CJIS Security Addendum certification page is signed, and CJIS security awareness training is done.
- No one may work on SC-01 until the revenue agency's background investigation, initial certification, and written penalty notice are complete, and the person's laptop is on the agency CISO's approved list.
- Developers may not read production data except for a logged break-fix task.
(AC-2; AC-6; PS-3; PS-6; PR.AA-05)

B.3 **MFA.** MFA is required for every staff account in every system, every administrator account, SSH access to SYS-02 (through the MFA-protected session service), and every agency user account in every workspace. (IA-2(1); IA-2(2); PR.AA-03)

B.4 **Termination.** On or before a person's last day, the Operations Manager must complete the termination checklist: disable platform, suite, helpdesk, and repository accounts; remove SSH keys and session service access; ask the MSP to collect and wipe the laptop; tell the AC-01 LASO and the prime on the same day if the person had CJI or FTI access; and remind the person in writing of their confidentiality duties. For an involuntary termination, access is disabled before the person is told. (PS-4; AC-2)

B.5 **Account reviews.** Each quarter the Lead Platform Engineer and the Operations Manager must review staff and agency accounts in each workspace with that agency's administrator, remove what no longer matches, and disable accounts unused for 90 days. Each month the Operations Manager compares staff accounts in all systems with the staff list. (AC-2; PR.AA-05)

B.6 **Lockout and locking.** Platform accounts lock after 5 failed sign-ins in 15 minutes until an administrator releases them. Laptops lock after 15 minutes idle. Platform sessions end after 30 minutes idle. (AC-7; AC-11; AC-12)

B.7 **Changes to access and production.** Production promotions, role changes, and security group or network rule changes need a change ticket approved by the Lead Platform Engineer or the owner (never the person making the change). Only the Lead Platform Engineer and the owner may promote to production. (CM-3; CM-5)

B.8 **Secrets and keys.** Passwords, keys, and tokens must never be stored in code, scripts, tickets, email, or chat. System credentials live in the IaaS secrets service; personal passwords are never written down or shared. SSH keys must have passphrases. Interface credentials are rotated yearly and whenever a person with access leaves. (IA-5; SC-12)

B.9 **Vendor and remote access.** MSP technicians and vendor support staff use named accounts with MFA. The MSP must give the Operations Manager a current list of technicians every year and its remote session logs on request. SC-01 work may be done only from laptops on the agency CISO's approved list. (AC-17; AC-20; MA-4)

B.10 **Log review.** Each month the Operations Manager reviews administrator actions, bulk exports, failed sign-ins, and record views by staff in the platform and SYS-02 logs, and records the result. (AU-6; PR.PS-04)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Staff may look only at the agency records their task needs. (PL-4; PR.AT-01)

C.2 Agency data may be kept only in the approved locations in POL-04 4.3, and handled only on company laptops. Never on personal devices, personal email or storage, messaging apps, or public AI tools. FTI never leaves the agency virtual desktop (POL-04 4.5). (PL-4; AC-20)

C.3 Lock the screen when stepping away. When working from home: keep screens out of view of others, do not print agency data, and do not let anyone else use the company laptop. (AC-11; PE-17)

C.4 Complete security awareness training at hire and every year, take part in phishing exercises, and complete every training an agency requires (CJIS awareness training for AC-01 access; disclosure awareness training and annual recertification for SC-01) before the due date. (AT-2; PR.AT-01)

C.5 Report suspected incidents at once, and within 1 hour at most, under POL-03 4.2, including your own mistakes. (IR-6)

C.6 Sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Operations Manager checks compliance through the monthly account comparison and log review (B.5, B.10), the quarterly agency terms check (A.10), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; account procedure and termination checklist; P01 risk register; P02 SSP control statements AC-2, AC-6, IA-2(1), PS-3; CJIS Security Addendum; SC-01 subcontract (Exhibit 7)

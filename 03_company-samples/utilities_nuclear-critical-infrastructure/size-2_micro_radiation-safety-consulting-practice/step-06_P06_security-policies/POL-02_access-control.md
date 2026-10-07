# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (Security Officer) |
| Approved by | Principal Health Physicist (owner), 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-15), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, CA-2, SA-9, SR-6, SI-12. Part B: AC-1, AC-2, AC-3, AC-6, AC-17, AC-21, IA-2, IA-2(1), IA-5, PS-3, PS-4. Part C: PL-4, AT-2, MP-7 |
| CSF 2.0 | GV.RR-02, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, ID.IM-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01 |
| Client and contract drivers | 10 CFR 37.43(d)(1), (3), (5), (6) flowed down by the 6 Part 37 client contracts (C-NUCLEAR-S01); reactor client access and media terms (C-NUCLEAR-S03) |

**Why this policy has three parts.** A 7-person practice does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the practice's security program, make sure only authorized people reach practice and client information, and only as far as their job and each client's approval allow, and tell staff how to use practice systems and media.

## 2. Scope
All staff of Cris Santos Company, including temporary staff and contractors. It covers every system and every copy of practice and client information, including systems the MSP and SaaS vendors run for the practice, laptops and USB drives taken to client sites, and paper.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Principal Health Physicist (owner) | Approves policies and the security budget; accepts Moderate risk; decides sanctions |
| Office Manager (Security Officer) | Runs this policy; requests and removes accounts; reviews logs and accounts; keeps the inventory |
| Senior Health Physicist (Part 37 services lead) | Keeps the client approval list; controls membership of each client's restricted folder |
| Senior Health Physicist (field services lead) | Issues and tracks company USB drives; enforces the media rule for client sites |
| MSP | Creates and disables suite and laptop accounts on the Office Manager's request; operates device controls |
| All staff | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security Officer.** The Office Manager is the designated Security Officer. The owner must record the designation in writing and update it within 30 days of any change. The Security Officer is the security contact named to clients. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Office Manager must update the risk assessment every August, and after any major change such as a new Part 37 or reactor client, a new vendor that holds client information, or enabling an AI feature, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the owner. No risk to a client's security information or to a reactor plant may be accepted above Low. (PM-9; GV.RM-01)

A.4 **Sanctions.** A staff member who breaks a security rule must be dealt with in proportion to intent and harm: coaching and retraining, a written warning, removal from client work, or termination. The Office Manager records each case; the owner decides anything beyond a written warning. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Supplier terms.** No vendor may hold client information or administer practice systems until the owner has approved its security terms. Contracts must require incident notice to the practice and name any subcontractors. The Office Manager reviews the MSP every year and each key SaaS vendor's SOC 2 report or security documentation every year. (SA-9; SR-6; GV.SC-05)

A.6 **Evaluation.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; ID.IM-01)

A.7 **Records.** Policies, risk assessments, assessments, incident records, client approval letters, client notices, and training records must be kept for at least 3 years, or longer if a client contract requires. (SI-12; GV.PO-02)

A.8 **Policy review and access to policies.** The Office Manager must review this policy set every September and after an incident or major change, and keep the current version where every staff member can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated using the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. No exception may give an unapproved person access to client security information or allow personal media at a client site. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Named accounts.** Every staff member must have their own account in the suite, SYS-02, and SYS-03. Shared or generic accounts are not allowed, including for the MSP. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access must match the person's job. The Office Manager must approve access in writing (the onboarding checklist) before it is granted. Administrator roles are used only from separate administrator accounts, never for daily email and file work. (AC-2; AC-3; AC-6; PR.AA-05)

B.3 **Client security information.** Each Part 37 client's security plan, implementing procedures, approved-individual list, and review reports must be kept only in that client's restricted folder (POL-04 4.3). Only staff that the client's reviewing official has approved in writing may be members of that folder. The Part 37 services lead must keep a client approval list (client, staff member, date approved, approval letter on file) and change folder membership only from it. Staff not on the list must not open, format, print, or forward these documents. (AC-3; AC-21; PS-3; 37.43(d)(1), (3), (5))

B.4 **Departures and role changes.** On or before a staff member's last day, the Office Manager must complete the departure checklist: disable suite, SYS-02, and SYS-03 accounts; remove MFA registrations and folder memberships; collect laptops, company USB drives, and keys; ask the MSP to remove device access. Within **2 working days** the Part 37 services lead must tell every client that had approved the person, and the field services lead must tell each reactor plant where the person had unescorted access. The same notices apply when someone stops working for a client. (PS-4; AC-2; 37.43(d)(6); reactor contract terms)

B.5 **Monthly reconciliation.** Each month the Office Manager must compare the user lists of the suite, SYS-02, SYS-03, the backup console, and the firewall with the staff roster, and the Part 37 services lead must compare each restricted folder's members with the client approval list. Anything that does not match is removed the same day. (AC-2; AC-6; PR.AA-05)

B.6 **MFA.** MFA is required for the suite (with number matching), SYS-02, SYS-03, the dosimetry portal where offered, and every administrator login, including logins held by the MSP (firewall, backup console, remote management). (IA-2(1); PR.AA-03)

B.7 **Vendor and MSP access.** MSP technicians and vendor support staff must use named accounts with MFA. Remote support to a lab workstation must be started by practice staff for each session; no always-on remote access and no inbound firewall rules for vendors. The MSP must give the Office Manager a current list of technicians with access every year. (AC-17; IA-2(1); SA-9)

B.8 **Passwords.** Passwords must be at least 12 characters, unique to the service, and stored only in the practice's password manager. The staff Wi-Fi passphrase must change every year and whenever a staff member leaves. (IA-5; PR.AA-01)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Practice systems are for practice work. Open only the client information your current engagement needs. (PL-4; PR.AT-01)

C.2 Do not store or send practice or client information with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. POL-04 4.6 lists the approved AI tools. (PL-4)

C.3 **Media at client sites.** Use only company-issued, encrypted USB drives listed in the inventory. Scan each drive on a clean practice laptop before every site trip, and give it to the plant's scanning kiosk at every reactor gate. Never connect a practice laptop or drive to a client's network or plant equipment unless the client's own procedure allows it. Personal USB drives are banned for practice work. (MP-7; reactor contract terms)

C.4 Lock your screen when you step away, never share passwords or MFA codes (including with the MSP), and never approve an MFA prompt you did not start. (AC-11; PL-4)

C.5 Complete security training at hire and every year, and take part in phishing exercises. Approved Part 37 staff also complete the client-information module every year. (AT-2; PR.AT-01)

C.6 Report suspected incidents at once under POL-03 4.2, including your own mistakes. (IR-6)

C.7 Sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to action under A.4. The Office Manager checks compliance through the monthly reconciliation (B.5), the monthly log review, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and departure checklist; client approval list; P01 risk register; P02 SSP control statements AC-2, AC-3, AC-21, IA-2(1), PS-3, PS-4

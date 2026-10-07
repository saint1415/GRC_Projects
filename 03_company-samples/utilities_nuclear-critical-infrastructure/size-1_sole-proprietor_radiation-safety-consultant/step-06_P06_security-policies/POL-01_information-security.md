# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent radiation safety consultant) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-consultant |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new client, a change in a client's security terms, a new system, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-6, RA-2, RA-3, CA-2, SA-9, CM-8, AC-2, AC-3, AC-6(5), AC-11, AC-17, AC-19, AC-20, AC-21, AU-6, IA-2, IA-2(1), IA-2(2), IA-5, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, MP-7, SI-2, SI-3, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8, PS-3 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, GV.SC-07, ID.AM-07, ID.AM-08, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-02, PR.IR-01, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Client terms and rules | CSR-A (1)-(10) (Client A); CSIA-B (1)-(6) (Client B); 10 CFR 73.56(f)-(g); 10 CFR 73.21-73.22; Fla. Stat. 501.171 |

## 1. Purpose
Protect the information clients trust the business with, and the business's own records, in a way one person can actually run. Above all, make sure the business is never the weak link in a client's nuclear security program: not for Client A's plant, and not for Client B's Part 37 security information. Each rule is written so it can be checked (P07).

## 2. Scope
All business and client information in any form (electronic, paper, photographs, spoken), on every component of the Core Business SaaS Stack (SYS-01 to SYS-08, the USB drive, and paper), and at every vendor that handles it. It applies to the owner and to any future employee. The per-diem technician and the IT technician are bound through their agreements.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security and compliance lead, incident commander | Owner-consultant | Runs this policy; decides incident and notice questions; keeps records |
| Risk acceptor | Owner-consultant | Accepts or treats every risk (section 4.4) |
| On-call IT technician (NDA) | Contractor | Technical help on request; no standing access; no access to client folders |
| Per-diem health physics technician | Subcontractor | Client A field work only, under the subcontract and Client A's rules |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check.

## 4. Governance and risk
4.1 The business must keep a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner is designated, by this policy, as the security and compliance lead and incident commander. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk is recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan. A risk to a client's security information or plant systems is never accepted above Low. (PM-9; GV.RM-01)
4.5 Controls must be evaluated every July (P07). At least every second year the evaluation must include an outside reviewer (for example the IT technician under NDA or a peer consultant), and Client A's supplier questionnaire answers must match the evaluation. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Sanctions and exceptions
5.1 Any future employee who breaks this policy must be sanctioned in proportion to intent and harm, up to termination, and the sanction documented. (PL-4)
5.2 A subcontractor or vendor that breaks its agreement or this policy is dealt with under its contract, up to ending it. (SA-9)
5.3 The owner must record any personal departure from this policy as an exception under 5.4, with the reason and the fix.
5.4 Exceptions must be written, risk-rated under 4.4, recorded in the risk register, and expire within 12 months. **No exception may relax a client's contract term**; only the client can. (PL-1)

## 6. Clients and vendors
6.1 **Client terms come first.** Where CSR-A, CSIA-B, or another client agreement is stricter than this policy, the client term applies. The owner keeps a one-page summary of each client's terms with the register in 8.6. (PL-4; GV.PO-01)
6.2 The owner must keep a vendor list showing each service, the data it holds, its MFA status, and the date its terms were last reviewed. (SA-9; GV.SC-05)
6.3 The email and file suite provider's SOC 2 report must be reviewed every year, and the owner must operate the customer controls it lists. (SA-9; GV.SC-07)
6.4 Remote support sessions by the IT technician must be started and watched by the owner, with client folders closed. (AC-17)
6.5 No subcontractor may work on client matters without a written agreement that passes down the client's confidentiality and security terms, and, for Client A, Client A's approval (CSR-A (10)). (PS-6; GV.SC-05)
6.6 **End of engagement.** When a work order or engagement ends, the owner must, within the client's deadline: return or destroy client information and send the written certificate (CSR-A (8); CSIA-B (5)), tell Client B when access to its security information is no longer needed (CSIA-B (6)), and record the close-out in the register (8.6). (MP-6; SI-12)

## 7. Access control
7.1 Every person has their own account. Credentials are never shared. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service that offers it. Email and the suite use an authenticator app, not text message codes. Recovery codes are kept offline (7.6). (IA-2(1); IA-2(2); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, kept in a password manager. Browsers must not save passwords. The mobile carrier account has a PIN to prevent SIM swaps. (IA-5)
7.4 Daily work, email, and client portals use a standard account. The administrator account is used only to install or change software. (AC-6(5))
7.5 Laptops lock after 5 minutes idle; the phone after 1 minute. (AC-11)
7.6 **Emergency access.** Recovery codes and a one-page contact sheet are kept in a sealed envelope held by the owner's attorney. The sheet says to notify Client A and Client B and not to open client files. (AC-2; CP-2)
7.7 On the first working day of each month the owner reviews the suite sign-in history and its external sharing report, and records the review in the security log. Any link that is not to a named person is removed. (AU-6; DE.AE-02)

## 8. Data handling
8.1 Information is classified in four levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Client Security** | Client B security plan, implementing procedures, approved-individuals list, security review reports and notes; Client A documents marked security-related; any SGI (8.4) | Only where the client allows (8.2); never in email, the suite, AI tools, or personal accounts |
| **Client Confidential** | Client A work packages, survey maps, permit photos, dose reports; other clients' drawings and survey data | Client portal or encrypted storage under the owner's sole control; returned or destroyed on time |
| **Business Confidential** | W-9, bank and tax records, this policy set | Encrypted storage with MFA; owner only |
| **Public** | Published qualifications, website | No restriction |

8.2 **Client Security information stays with the client.** Client B security information is opened only on site or in Client B's secure share (CSIA-B (1)-(2)). Working notes go only in the encrypted, password-protected notes container on the main laptop, which is not synced. Client A security-related documents stay in Client A's portal. (AC-3; AC-21; SC-28)
8.3 Client Security and Client Confidential information is sent only through the client's own portal or share, never as an email attachment. (SC-8; PR.DS-02)
8.4 **Safeguards Information.** The business does not accept SGI. If anything marked "Safeguards Information" arrives: do not open it further, copy, print, or forward it; keep it in the owner's personal custody (for email, do not download; for paper, keep it on the owner's person); call Client A or the sender at once and follow their instructions for return; record the event in the incident log. (PL-4; IR-6; 10 CFR 73.21(a)(1); CSR-A (6))
8.5 Files may be shared outside the business only with named people. "Anyone with the link" sharing is not allowed. (AC-3; AC-21)
8.6 The owner keeps a **register of client information**: what is held, where, the client's level (8.1), and the return or destruction date. It is checked monthly with 7.7. (CM-8; ID.AM-07)
8.7 Client and business files not in a client portal are kept in the suite with version history on, and copied monthly to an encrypted drive kept in the locked cabinet. Field data is copied to the suite the same day it is collected. One restore is tested each quarter. (CP-9; PR.DS-11)
8.8 Paper goes through the cross-cut shredder. Electronic copies are deleted from every location, including trash and version history where the service allows. Drives are wiped (encrypted, then reset) before reuse or disposal, and each destruction of client information is recorded with a certificate where the client requires one. Personal information is disposed of when no longer retained (Fla. Stat. 501.171(8)). (MP-6; ID.AM-08)
8.9 Security records (this policy, risk assessments, assessments, incident records, client certificates) are kept for 6 years. (SI-12)

## 9. Acceptable use, media, and training
9.1 Business devices are for business work. Household members must not use them. (PL-4)
9.2 **Client A sites.** No business device or media is ever connected to a plant digital asset or plant network. On site, devices use only the guest wireless network. (AC-20; SC-7; CSR-A (1))
9.3 **Portable media.** Only one encrypted drive, marked for Client A, may be used at Client A, and it is scanned at Client A's kiosk before each use. It is not used for any other client and is wiped after each outage. Personal drives are not used for client data. (MP-7; SI-3; CSR-A (2))
9.4 The field laptop is kept offline. Data leaves it only on the encrypted drive, to the main laptop, until it is replaced with a supported system. (SI-2; SC-7)
9.5 Automatic updates and antivirus stay on. Software comes only from official stores or the vendor's site. (SI-2; SI-3; PR.PS-02)
9.6 Business work at home uses the separate business wireless network, or the phone hotspot. The router administrator password is unique. (SC-7; PR.IR-01)
9.7 Photos in a client's protected area are taken only under the client's photo permit, kept in a separate phone album with cloud sync off, moved to the client's portal the same week, and then deleted. (AC-19; CSR-A (7))
9.8 **AI tools.** No Client Security or Client Confidential information may be entered into any AI tool unless the client agrees in writing and a written P10 assessment approves the tool. AI predictions may only bring an instrument check forward, never delay a calibration or response check. (PL-4; SA-9; CSIA-B (3))
9.9 The owner completes Client A's training before each access renewal and a general security course every year. (AT-2; PR.AT-01; 10 CFR 73.54(d)(1) through CSR-A (3))

## 10. Incident response
10.1 The business keeps an incident runbook (P08) with a printed contact list in the field bag and at home. (IR-8; RS.MA-01)
10.2 Every suspected incident (malware alert, phishing click, lost device or drive, a link or file sent to the wrong person, a vendor notice, a contact seeking plant information) is written in the incident log the same day, with the time it was discovered. (IR-5; RS.MA-02)
10.3 **Client clocks.** Suspected compromise of anything used for Client A work, or any contact seeking Client A security or system information, is reported to Client A's cyber security contact within 8 hours (CSR-A (5)). Any suspected unauthorized access to or disclosure of Client B security information, including entering it into a software service, is reported to Client B's RSO within 24 hours (CSIA-B (4)). When in doubt, report. (IR-6; RS.CO-02)
10.4 For incidents involving personal information, notices follow the P08 notification matrix (Fla. Stat. 501.171). (IR-6)
10.5 No ransom is paid without legal advice and an OFAC sanctions check. (IR-4)
10.6 The runbook is walked through before each Client A outage and after any real incident; lessons are recorded within 30 days. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner keeps a written coverage agreement with a qualified peer health physicist, with Client A's consent, for urgent outage work. (CP-2)
11.3 Before each outage the owner prints the work package index and contact list, checks instrument calibration dates, and confirms the encrypted Client A drive is empty. (CP-2)

## 12. Duties of an individual with unescorted access
12.1 The owner promptly reports to Client A's reviewing official any legal action described in 10 CFR 73.56(g)(1). (PS-3)
12.2 The owner reports concerns from behavioral observation to Client A as 10 CFR 73.56(f)(3) requires. (PS-3; IR-6)
12.3 The owner keeps Client A's behavioral observation and cyber security training current (10 CFR 73.56(f)(2)(iv); CSR-A (3)). (AT-2)

## 13. Compliance and enforcement
Compliance is checked in the annual control assessment (P07), the monthly review in 7.7, and the pre-outage checklist in 11.3.

## 14. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

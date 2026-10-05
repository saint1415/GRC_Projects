# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent dam safety engineering consultant) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-engineer |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new client, a new system or vendor, a subcontractor, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, RA-2, RA-3, CA-2, SA-9, PS-7, AC-2, AC-3, AC-6(2), AC-11, AC-17, AC-19, AC-21, AU-6, IA-2(1), IA-2(2), IA-5, IA-5(2), SC-7, SC-28, CP-2, CP-9, MP-3, MP-4, MP-6, MP-7, SI-2, SI-3, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-11, PR.IR-01, ID.AM-07, ID.AM-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Duties carried | CSCA-A (1) to (9), which pass down parts of the FERC Security Program for Hydropower Projects Rev. 3A (C-DAMS-R01); 18 CFR 388.113(h)(2) (CEII); 18 CFR 12.36(g) and (h); GRS-B (1) to (3); Fla. Stat. 501.171 |

## 1. Purpose
Protect client information, CEII, and the owner's access to client dam systems, and meet every security term the business has signed, in a way that one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All business information in any form (electronic, paper, photos, spoken), on every component of the Core Business SaaS Stack (SYS-01 to SYS-08, the backup drive, and paper), at every vendor that handles it, and on any device that connects to a client system. It applies to the owner-engineer and to anyone working for the business, including the field assistant. Vendors are bound through their contracts.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead, incident commander, risk acceptor | Owner-engineer | Runs this policy; decides incident and notice questions; keeps records |
| Independent consultant of record | Owner-engineer | Personal FERC approval for Client A; signs and seals reports |
| Field assistant | Contractor (1099) | Field safety partner; follows section 9.6 |
| On-call IT technician | Contractor under NDA | Technical help on request; no standing access; no access to client folders |
| Client security contacts | Client A, Client B | Receive notices under section 10 |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The business must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner-engineer is designated in writing, by this policy, as the security lead and incident commander. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9; CSCA-A)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every July (P07). At least every second year, the evaluation must include review by someone outside the business, such as the IT technician under NDA or a peer engineer. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)
4.7 Before signing any client agreement, the owner must list its security terms in the client information register and check them against this policy. (PL-1; GV.SC-05)

## 5. Exceptions
5.1 The owner must record any departure from this policy as an exception, with the reason, the risk level under 4.4, and the fix. Exceptions expire within 12 months. (PL-1)
5.2 No exception may break a client agreement or a CEII duty. Those need the client's or FERC's written agreement. (PL-1)

## 6. Vendors, subcontractors, and clients' systems
6.1 **No agreement, no client data.** No vendor, AI tool, or person may receive client data or CEII until the owner has checked the vendor's terms, recorded them in the vendor list, and has the client's written consent where the client agreement requires it. (SA-9; GV.SC-05; GRS-B (1))
6.2 The owner must keep a vendor list showing each vendor, the data it handles, and the review date, and must review the email and file suite provider's SOC 2 report every year. (SA-9; GV.SC-07)
6.3 Anyone who works with the owner on a client job, including the field assistant, must sign the business's confidentiality and field rules agreement and, for Client A, be approved in writing by Client A before seeing its material or entering its restricted areas. (PS-7; CSCA-A (9))
6.4 Client systems: the owner connects to Client A's gateway only in windows Client A enables, only from the standard account on the laptop, and only over the phone hotspot or the separate business network. The gateway password is kept only in the password manager. (AC-17; CSCA-A (3))
6.5 The owner must log each gateway session (date, start and end time, purpose) the same day and answer Client A's weekly session review within one business day. (AU-6; CSCA-A (4))

## 7. Access control
7.1 Every person has their own account. Credentials are never shared. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service that offers it: the suite, the accounting SaaS, and every client system. (IA-2(1); IA-2(2); PR.AA-03; GRS-B (2))
7.3 Passwords must be unique passphrases of at least 14 characters, kept only in the password manager. Browsers must not save passwords. (IA-5)
7.4 Daily work uses a standard account. The laptop administrator account is used only to install or update software. (AC-6(2))
7.5 The owner must review the accounts in the account list every quarter and remove any that are no longer needed. (AC-2; PR.AA-05)
7.6 Laptop locks after 5 minutes idle; phone and tablet after 1 minute. (AC-11)
7.7 The digital signing certificate used to seal reports must be kept on a hardware token with its own PIN and used only by the owner. (IA-5(2); 18 CFR 12.36(h))
7.8 On the first working day of each month, the owner reviews the suite sign-in history and notes the review in the security log. (AU-6; DE.AE-02)
7.9 **Emergency access.** Suite and password manager recovery codes and a one-page emergency sheet are kept in a sealed envelope held by the owner's attorney (P05). (AC-2; CP-2)

## 8. Data handling
8.1 Information is classified in four levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Security-sensitive** | Client Security Plans, Form 3 answers, Security Checklist results; notes and photos about security features | **Never stored by the business.** Read only in the client's portal or on site (8.2). Notes and photos that cannot be avoided are marked (8.3) and kept only in the encrypted client folder |
| **CEII** | Material designated CEII by FERC, or released by FERC as CEII | Encrypted container only; register entry; purpose and recipient limits (8.4) |
| **Client confidential** | Drawings, instrument data, gate test records, drafts, field photos of non-security features | Owner-only client folders in the suite or encrypted laptop storage |
| **Public** | Published reports, marketing material | No restriction |

8.2 Client A's Security Plan and Form 3 answers must be read only on site or in Client A's portal. They must never be downloaded, printed, photographed, or kept. (AC-21; CSCA-A (2); Rev. 3A 7.3)
8.3 Any note or photo derived from security-sensitive material must carry the footer "Privileged - Security Sensitive Material". (MP-3; CSCA-A (1))
8.4 CEII must be used only for the purpose for which it was released, discussed only with authorized recipients, kept encrypted, and protected even after its designation lapses. Before any Client B deliverable is sent, the owner checks that it holds no upstream project CEII. (AC-21; PL-4; 18 CFR 388.113(h)(2))
8.5 Every device and drive that can hold client data or CEII must be encrypted. (SC-28; PR.DS-01)
8.6 Field photos are moved from the phone or tablet to the owner-only client folder the same day and then deleted from the device. Phone photo sync to any personal cloud must be off. (AC-19)
8.7 The laptop is backed up every week to an encrypted drive kept in the locked cabinet and never taken to the field. A restore is tested every quarter. (CP-9; PR.DS-11; MP-4)
8.8 Removable media must never be connected to client equipment. (MP-7; CSCA-A (6))
8.9 The owner keeps a client information register listing, for each client and for CEII, what is held, where every copy is, and when it must be returned or destroyed. Within 30 days after an engagement ends (or on FERC's request for CEII), material is returned or destroyed and a written certificate is sent. (MP-6; SI-12; CSCA-A (8); 388.113(h)(2))
8.10 Paper is cross-cut shredded. Old devices and drives are crypto-erased and reset, or destroyed by a recycler that gives a certificate. Each disposal is recorded. (MP-6; Fla. Stat. 501.171(8))
8.11 Security records (this policy, risk assessments, assessments, incident records, client notices, CEII register) are kept for at least 6 years, and longer if a client agreement says so. (SI-12)

## 9. Acceptable use and training
9.1 Business devices are for business work. Family members must not use them. (PL-4)
9.2 Software comes only from vendors' official sites or app stores. Automatic updates and the built-in antivirus stay on. (SI-2; SI-3)
9.3 The laptop and tablet use the separate business network, or the phone hotspot, never the shared household network. (SC-7)
9.4 **AI tools.** An AI tool may receive client data only after a written assessment (P10), a review of its terms, and the client's written consent. CEII and security-sensitive material must never go to any AI tool. AI output is a lead to check, never a finding or conclusion: every conclusion in a sealed report is the owner's own (18 CFR 12.36(g)). (PL-4; SA-9)
9.5 The owner completes Client A's module every year and one other short security course every year that covers phishing and information-stealing malware. (AT-2; PR.AT-01; CSCA-A (5))
9.6 **Field rules.** At client sites: follow the client's escort and photo rules; no photos of security features (cameras, locks, access control, gate control panels) unless the client's escort approves; the field assistant takes no photos on a personal device. (PL-4; PS-7; CSCA-A (9))

## 10. Incident response
10.1 The business keeps an incident runbook (P08) with a printed contact sheet in the home office and in the field bag. (IR-8; RS.MA-01)
10.2 Every suspected incident (lost device or drive, phishing click, odd MFA prompt, a client's alert, a misdirected file) is written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 Client notices: Client A within 24 hours of a suspected incident affecting its information, accounts, or systems, and at once for suspicious activity at its site; Client B within 24 hours. Notices go by phone and then in writing. (IR-6; RS.CO-02; CSCA-A (7); GRS-B (3))
10.4 Any unauthorized disclosure of CEII must be reported promptly to FERC's CEII Coordinator, and to Client A for Client A's CEII. (IR-6; 388.113(h)(2))
10.5 Breach notices to individuals follow the P08 notification matrix (Fla. Stat. 501.171). (IR-6)
10.6 No ransom may be paid without legal advice and an OFAC sanctions check. (IR-4)
10.7 The runbook is walked through every year and after any real incident. Lessons learned are recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner keeps a written arrangement with a peer engineer for client communications and non-FERC work, and the client call list in the sealed emergency sheet. (CP-2)

## 12. Compliance
Compliance is checked in the annual control assessment (P07) and the monthly review in 7.8. A broken client term is handled under section 10 and the client agreement.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Where client information may be kept
| Location | Security-sensitive | CEII | Client confidential |
|---|---|---|---|
| Client portal or site (read only) | Yes | Yes | Yes |
| Encrypted CEII container on the laptop | Marked notes only | Yes | Yes |
| Owner-only client folders in the suite | No | No | Yes |
| Encrypted backup drive in the locked cabinet | Marked notes only | Yes | Yes |
| Phone and tablet | No (move the same day) | No | Same day only |
| Personal accounts, consumer apps, AI tools, the field assistant's phone | No | No | No (AI only under 9.4) |

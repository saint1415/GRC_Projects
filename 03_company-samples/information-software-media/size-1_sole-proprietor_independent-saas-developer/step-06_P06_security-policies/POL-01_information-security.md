# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent B2B SaaS software publisher) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-developer |
| Effective date | 2026-09-28 (adopted 2026-09-25) |
| Review cycle | Every August with the risk assessment, and after a new sub-processor, a new AI feature, a contractor change, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-7, PS-8, RA-2, RA-3, RA-5, CA-2, SA-9, SA-11, AC-2, AC-3, AC-6(5), AU-2, AU-6, IA-2, IA-2(1), IA-5, IA-5(7), SC-8, SC-28, CM-6, CP-2, CP-4, CP-9, MP-6, SI-2, SI-12, AT-2, AT-3, IR-4, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RM-01, GV.OC-03, GV.SC-05, GV.SC-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.AT-02, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-02, PR.PS-06, ID.AM-07, ID.AM-08, ID.RA-08, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Drivers | FTC Act Section 5 (N51-R01) as analyzed in P03; Terms of Service and DPA promises; Fla. Stat. 501.171(6) |

## 1. Purpose
Protect subscribers' and their clients' information, keep every promise the company makes about it, and do this in a way one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All company and subscriber information in any form, on every system in the Multi-tenant Booking Platform (SYS-01 to SYS-09), and at every service provider that receives it. It applies to the owner-developer and to any future employee. Contractors (the support contractor, the security consultant, any standby developer) are bound through their agreements.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security and privacy lead, incident commander | Owner-developer | Runs this policy; decides incident and notice questions; keeps records |
| Risk acceptor | Owner-developer | Accepts or treats every risk (section 4.4) |
| Support operator | Freelance support contractor | Uses only the support role; reports anything suspicious the same day |
| Independent check | Contract security consultant | Yearly challenge of the self-assessment (4.5) |
| Service providers | Hosting provider and SaaS sub-processors | Operate their safeguards under their terms and DPAs |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check every year.

## 4. Governance and risk
4.1 The company must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner-developer is designated, by this policy, as the security and privacy lead. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. A risk that would break a promise to subscribers must be treated. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every August (P07). Each evaluation must include at least one day of challenge and testing by an outside consultant who does not operate the controls. (CA-2; ID.IM-02)
4.6 **Public statements.** Every security or data-use statement on the website, in release notes, in questionnaire answers, or in sales material must be true when published. The owner must review all of them every quarter against the latest P07 results, and before any new claim is published. (PL-4; GV.OC-03; N51-R01 deception)
4.7 **New features.** Any feature that sends subscriber data to a new service provider, or that uses AI, must pass a written review (P10 for AI) before release, including the sub-processor notice in 6.2. (SA-9; SA-11)
4.8 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Sanctions and exceptions
5.1 A contractor who breaks this policy or the security terms of its agreement must be dealt with under the agreement, up to ending it and removing access the same day. Any future employee faces proportionate sanctions (retraining, written warning, termination), documented and kept 3 years. (PS-7; PS-8)
5.2 The owner must record any personal departure from this policy as an exception under 5.3, with the reason and the fix.
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 6. Service providers and sub-processors
6.1 **No terms, no data.** No service provider may receive subscriber data until its terms include security commitments and a DPA (or equivalent data-use terms) and the owner has saved a copy. (SA-9; GV.SC-05)
6.2 Every service provider that receives subscriber data must be on the public sub-processor list before it receives data, and subscribers must get 14 days' notice of any addition, as the DPA promises. (SA-9; GV.SC-05)
6.3 Each sub-processor's SOC 2 report or security page must be reviewed every year, and the owner must operate the customer controls the report lists (P09). (SA-9; GV.SC-07)
6.4 Contractor agreements must include security terms: confidentiality, use of named accounts only, MFA, device basics (encryption, updates, screen lock), same-day incident reporting, and return or deletion of data at the end. (PS-7; SA-9)

## 7. Access control
7.1 Every person must have their own account. Credentials must never be shared, including with contractors. (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every administrator account, including the hosting console, source repository, domain registrar, email, password manager, payment processor, and the product's admin console. Security keys are used where the service supports them. (IA-2(1); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, stored in the password manager. (IA-5; PR.AA-01)
7.4 Only the owner holds super-admin rights in the product. The support contractor uses a named support role that can view but not export subscriber data. Access is removed the day a contract ends. Accounts in every service are reviewed each quarter. (AC-6(5); AC-2; PR.AA-05)
7.5 **Secrets.** Production secrets (tokens, keys, database passwords) must live only in the hosting platform's encrypted settings, the CI secret store, and the password manager. They must never be stored in plaintext files or committed to a repository. Secret scanning with push protection must be on for every repository. Secrets must be rotated every 90 days, when a contractor leaves, and at once if exposure is suspected. (IA-5; IA-5(7); PR.AA-01)
7.6 **Emergency access.** Recovery codes, a spare security key, and a one-page access sheet must be kept in a sealed envelope held by the owner's attorney, for use if the owner or the owner's phone is unavailable. (AC-2; CP-2)
7.7 On the first business day of each month, the owner must review the hosting audit log, the repository security log, failed sign-ins, and the admin action log, and note the review in the security log. Hosting logs must be exported so 12 months are kept. (AU-6; AU-2; DE.AE-02)

## 8. Data handling
8.1 Information is classified in three levels. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Subscriber and end-client data, service notes, photos, secrets, credentials | Approved systems only (8.2); encrypted; minimum necessary |
| **Confidential** | Contracts, financial records, this policy set, questionnaire answers | Encrypted storage; owner only |
| **Public** | Website, pricing, help articles | No restriction |

8.2 Restricted data may be kept only in the production platform and the listed sub-processors. It must not be copied to the laptop, personal accounts, or any tool that is not on the sub-processor list. (AC-3; SA-9)
8.3 Development and testing must use synthetic data, never copies of production data. (SA-11; PR.DS-01)
8.4 Every device that can hold Restricted data must use full-disk encryption. (SC-28; PR.DS-01)
8.5 Subscriber exports must be delivered through expiring download links, not email attachments. (SC-8; PR.DS-02)
8.6 Error reports and logs must scrub client names, phone numbers, and message text. Error data is kept 30 days. (SI-12; ID.AM-08)
8.7 Subscriber data must be deleted, including photos, within 30 days after an account closes, as the DPA promises, and each deletion run is logged. Old devices must be encrypted and reset before reuse or trade-in, and the disposal recorded. (SI-12; MP-6; ID.AM-08)
8.8 Security records (this policy, risk assessments, assessments, incident records, notices) must be kept at least 5 years. (SI-12)

## 9. Secure development, acceptable use, and training
9.1 Every change goes through the repository and CI; nothing is deployed by hand except in an incident under P08. Automated tests must include tenant isolation and authorization tests once built (due 2027-03-31). (SA-11; PR.PS-06)
9.2 Dependency alerts must be triaged monthly. High and critical issues are fixed within 14 days; others within 30 days. The running application is scanned every quarter. (RA-5; SI-2; ID.RA-08)
9.3 The laptop is used for company work through a separate administrator browser profile. Software is installed only from official sources, and new development packages are checked for name and publisher before install. (PL-4; CM-6)
9.4 Automatic updates and the built-in antivirus must stay on. (SI-2; PR.PS-02)
9.5 **AI tools.** An AI feature or tool may process subscriber data only after a written P10 assessment, a DPA with no-training terms, a sub-processor list entry with notice (6.2), and the owner's written approval. AI-generated messages to end clients must be reviewed by a person before sending unless the P10 assessment allows otherwise. (PL-4; SA-9)
9.6 The owner must complete a security awareness course and a secure coding course every year. Contractors complete a short awareness module before access is issued. (AT-2; AT-3; PR.AT-01; PR.AT-02)

## 10. Incident response
10.1 The company must keep an incident runbook (P08), a notification matrix, a subscriber security contact list, and notice templates, with a copy outside the company's own systems. (IR-8; RS.MA-01)
10.2 Every suspected incident (exposed secret, unusual sign-in, malware alert, vendor notice, subscriber report) must be written in the incident log the same day, with the time of discovery and, later, the time of confirmation. (IR-6; RS.MA-02)
10.3 Subscribers must be notified within the DPA deadlines (72 hours after confirmation; 48 hours for the two negotiated DPAs), and Florida subscribers no later than 10 days after determination of a breach (Fla. Stat. 501.171(6)(a)), as set out in the P08 matrix and confirmed by counsel. Notices must be accurate and must not understate what is known. (IR-6; RS.CO-02)
10.4 No ransom or extortion payment may be made without counsel's advice and an OFAC sanctions check. (IR-4)
10.5 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-8; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 Database backups must have a copy outside the production account, and photo storage must keep versions. (CP-9; PR.DS-11)
11.3 A restore must be tested every August and before any risky database migration, with the time recorded against the 4-hour RTO. (CP-4)
11.4 The owner must keep a standby developer arrangement and the sealed emergency kit (7.6) current. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the yearly control assessment (P07), the monthly review in 7.7, and the quarterly statement review in 4.6. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P04 cloud control map; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P09 SOC 2 self-check; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Where Restricted data may live
| Location | Restricted data held | Rules |
|---|---|---|
| Production platform (SYS-01) | All subscriber and end-client data | 7.2, 7.4, 7.5, 11.2 |
| Listed sub-processors (SYS-03, SYS-04, SYS-06, SYS-07) | Only the fields each one needs | 6.1, 6.2, 8.6 |
| CI secret store and password manager | Secrets | 7.5 |
| Laptop | No subscriber data; no plaintext secrets | 8.2, 8.3, 8.4 |
| Phone | Authenticator; help desk app | 7.2, 8.4 |

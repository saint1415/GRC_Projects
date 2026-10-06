# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (web hosting reseller) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner |
| Effective date | 2026-10-01 (adopted 2026-09-28) |
| Review cycle | Every August with the risk assessment, and after a new tool, a new contractor, a change of upstream provider, or an incident (next review 2027-08-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-7, RA-2, RA-3, RA-5, CA-2, SA-9, AC-2, AC-3, AC-6, IA-2, IA-2(1), IA-5, IA-8, AU-6, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-4, SI-12, AT-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OC-03, GV.SC-05, GV.SC-07, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-02, ID.AM-07, ID.AM-08, ID.RA-01, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Legal basis | FTC Act Section 5 (15 U.S.C. 45); Fla. Stat. 501.171(2), (6), (8) |

## 1. Purpose
Protect customers' websites, mailboxes, and domains, and the tools that control them, and meet the reasonable-security and notice duties that apply to a hosting reseller, in a way that one person can actually run. Each rule below is written so it can be checked (P07).

## 2. Scope
All information the company handles, on every system in the Hosting Control Plane and Customer Portal (SYS-01 to SYS-07) and in any other tool used for company work (including AI tools), and at every vendor that handles it. It applies to the owner, to the freelance developer and any future contractor or employee, and through contracts to vendors.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security and privacy lead, incident commander | Owner | Runs this policy; decides breach questions; keeps records |
| Risk acceptor | Owner | Accepts or treats every risk (4.4) |
| Contractor with privileged access | Freelance web developer | Follows the security addendum (5.1) and sections 7 to 10 |
| Independent check | Contract security consultant | Challenges the self-assessment (4.5) |
| Vendors | Upstream hosting provider, registrar, portal, dashboard, and security service vendors | Operate their safeguards; meet their contract terms |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance and risk
4.1 The company must maintain a security program documented in this policy, the system security plan (P02), and the risk register (P01). (PM-1; GV.PO-01; Fla. Stat. 501.171(2))
4.2 The owner is designated, by this policy, as the security and privacy lead and incident commander. (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every August and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. A risk that could reach many customers' sites at once must not be accepted above Moderate. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every August (P07). At least every second year, the evaluation must include testing by someone outside the company, such as the contract security consultant. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)

## 5. Contractors and exceptions
5.1 **Contractors.** No contractor may receive access to a control plane tool or to customer data until a signed security addendum requires: MFA on every account; an encrypted, updated device with antivirus; credentials kept only in the company's password manager vault; reporting any suspected incident to the owner within 24 hours; and return or deletion of all credentials and data when the engagement ends. (PS-7; GV.RR-04; FTC Start with Security 8)
5.2 A contractor who breaks the addendum or this policy loses access the same day; the owner then decides whether to end the engagement. (PS-7)
5.3 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. The owner records any personal departure from this policy the same way. (PL-1)

## 6. Vendors
6.1 The owner must keep a vendor list showing, for each vendor: the customer data it holds, where the data is stored, its security and incident notice terms, and the date of the last review. (SA-9; GV.SC-05)
6.2 The upstream hosting provider's SOC 2 report must be reviewed every year, and the owner must operate the customer controls that report lists. Other vendors that hold customer data must be asked each year for their assurance report or security summary and their data locations. (SA-9; GV.SC-07)
6.3 A new vendor that will touch customer data may be used only after the owner reviews its terms under 6.1 and checks that the company's public statements stay true (section 12). (SA-9; GV.SC-05)

## 7. Access control
7.1 Every person must have their own account in every tool. Credentials must never be shared. (AC-2; IA-2; PR.AA-01)
7.2 MFA must be on for every account that can reach a control plane tool or customer data: the customer portal administrator login, the reseller console, the registrar, the site management dashboard, the security service, email, and the password manager. Security keys must be used for the portal, console, registrar, and dashboard by 2027-03-31. (IA-2(1); PR.AA-03)
7.3 **Least privilege.** Only the owner may hold system-wide administrator rights in a control plane tool or push code or settings to more than one customer site at once. A contractor's access must be limited to the sites assigned to the current task, without package upload or bulk actions. (AC-6; PR.AA-05; FTC Start with Security 2)
7.4 Every control plane account must be reviewed on the first business day of each month. A contractor's accounts must be disabled the day the engagement ends. (AC-2; PR.AA-05)
7.5 Passwords must be unique and generated by the password manager. Customer site, control panel, and SFTP credentials must be kept only in the shared password manager vault and shared only through it, never by email or in a document. (IA-5; PR.AA-01; FTC Start with Security 3)
7.6 **Emergency access.** Recovery codes and a one-page access sheet must be kept in a sealed envelope held by the owner's attorney, for use under the backup-operator arrangement (11.2). (CP-2; AC-2)
7.7 Every Monday the owner must review the dashboard activity log and the sign-in history of the portal, reseller console, and registrar, and review every AI-dismissed finding in the protected categories (new administrator users, changed executable files), and note the review in the security log. New-device sign-in alerts must be on wherever a tool offers them. (AU-6; SI-4; DE.AE-02)
7.8 Customers who run online stores or whose mailboxes hold Social Security numbers or client files must use MFA on their portal and control panel accounts. Other customers must be offered it. (IA-8; PR.AA-03)

## 8. Data handling
8.1 Information is classified in three levels. The company collects only the customer data its services need. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | Customer site files and databases, mailbox contents, credentials, API credentials, recovery codes | Approved systems only (8.2); encrypted; access by need only |
| **Confidential** | Customer contacts, contracts, this policy set, assessment results | Encrypted storage; owner and the consultant under agreement |
| **Public** | Plans and prices, status notices | No restriction |

8.2 Restricted data must stay in the upstream platform, the approved SaaS tools on the vendor list, and the password manager. A troubleshooting copy on the laptop must be deleted the same day. (AC-3; SA-9; FTC Start with Security 1)
8.3 Every device that can hold Restricted data must use full-disk encryption, and remote wipe must be on. (SC-28; PR.DS-01)
8.4 Restricted data sent to anyone must go through the password manager vault or an expiring, access-controlled download link, never as an email attachment. (SC-8; PR.DS-02)
8.5 Every customer site and mailbox must have an independent daily backup, kept 30 days outside the upstream provider, by 2026-12-31. Three sites must be restore-tested each quarter, and the result recorded. (CP-9; PR.DS-11)
8.6 A closed customer must be offered an export, and the hosting account must be terminated 30 days after closure so that the upstream provider deletes the data. (SI-12; ID.AM-08; Fla. Stat. 501.171(8))
8.7 Old devices must be encrypted and reset before reuse or trade-in, or destroyed by a recycler that gives a certificate. Each disposal is recorded. (MP-6; ID.AM-08; Fla. Stat. 501.171(8))
8.8 Security records (this policy, risk assessments, assessments, incident records, breach determinations) must be kept at least 5 years. (SI-12; Fla. Stat. 501.171(4)(c))

## 9. Acceptable use, patching, AI, and training
9.1 Company devices may be used for personal purposes only in a separate operating system user account; family members must not use them. Devices must never be left unattended outside the home office. (PL-4)
9.2 Automatic updates, the built-in antivirus, and the host firewall must stay on. Software must come only from official stores or the vendor's site. (SI-2; SI-3)
9.3 **Patching.** Care-plan sites must be updated at least weekly, and within 72 hours for a vulnerability rated critical by the security service. Bulk updates must be applied first to one test site. Each hosting-only customer must be told of open vulnerabilities on its site every month and offered automatic security updates. (SI-2; RA-5; PR.PS-02; FTC Start with Security 9)
9.4 **AI tools.** Customer data, logs, site files, and credentials must not be entered into an AI tool unless the tool is on the vendor list with a written P10 assessment and terms that bar training on company data. Redacted excerpts with no customer identifiers may be used in an approved tool. AI features that close or dismiss security findings must not do so in the protected categories without the owner's review (7.7). (PL-4; SA-9)
9.5 The owner and any contractor must complete security awareness training every year; the freelance developer must also complete phishing and credential-handling training before access. (AT-2; PR.AT-01)

## 10. Incident response
10.1 The company must keep the provider tooling runbook (P08), a printed contact list, and an offline export of customer contacts, updated monthly. (IR-8; RS.MA-01)
10.2 Every suspected incident (unusual sign-in, scan alert, customer report, vendor notice) must be written in the incident log the same day, with the time it was discovered. (IR-5; IR-6; RS.MA-02)
10.3 For every incident that touches customer data, the owner must write down whether a breach of security under Fla. Stat. 501.171(1)(a) occurred or there is reason to believe one occurred, and the date of that determination. (IR-4; IR-6)
10.4 Each affected customer must be notified as soon as practicable and **no later than 10 days** after that determination, with all the information it needs for its own notices. Notices for the company's own data follow the P08 notification matrix, confirmed by counsel. (IR-6; RS.CO-02; Fla. Stat. 501.171(6)(a))
10.5 No ransom or extortion payment may be made without counsel's advice and an OFAC sanctions check. (IR-4)
10.6 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-3; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner must keep a written backup-operator arrangement with a named hosting professional, covering customer communication, renewals, and restores when the owner is unavailable, with access only through the emergency envelope (7.6). (CP-2)
11.3 DNS zone records must be exported monthly to an offline file. (CP-9)

## 12. Customer commitments and public statements
12.1 Every security, backup, uptime, or data location claim on the website or in sales material must be true for every customer it describes, and backed by a substantiation file (screenshots, reports, vendor confirmations). (GV.OC-03; FTC Act Section 5 deception)
12.2 Answers to customer security questionnaires must come from a maintained answer document that matches P02, P03, and P07. Wrong answers already given must be corrected in writing. (GV.OC-03)
12.3 The Terms of Service must state who patches site software, what backups each plan includes, and how and when the company notifies customers of a security incident. (SA-9; GV.OC-03)
12.4 Uptime must be measured every month. Service credits must be offered whenever the guarantee is missed. (CP-2)

## 13. Compliance and enforcement
Compliance is checked in the annual control assessment (P07) and the weekly and monthly reviews in 7.4 and 7.7. Contractor breaches are handled under 5.2.

## 14. Related documents
P01 risk register; P02 system security plan; P03 gap analysis; P04 control map; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P09 SOC 2 self-check; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Where Restricted data may be (8.2)
| Location | Restricted data held | Protection required |
|---|---|---|
| Upstream platform (SYS-02) | Customer sites, databases, mailboxes | 7.2, 8.5, 8.6 |
| Customer portal (SYS-01) | API credentials; customer sign-ins | 7.2, 7.8 |
| Registrar (SYS-03) | Domain contacts | 7.2 |
| Dashboard (SYS-04) | Admin access to 120 sites; premium backups | 7.2, 7.3, 7.4 |
| Security service (SYS-05) | Site files; findings | 7.2, 7.7 |
| Password manager (SYS-06) | All credentials and recovery codes | 7.2, 7.5 |
| Laptop and phone (SYS-07) | Same-day troubleshooting copies only | 8.2, 8.3 |

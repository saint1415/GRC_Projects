# Information Security Policy (consolidated)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated wireless internet service provider) |
| Policy ID | POL-01. At the Sole Proprietorship tier this one policy replaces POL-02 to POL-05 |
| Owner and approver | Owner-operator |
| Effective date | 2026-09-01 (adopted 2026-08-31) |
| Review cycle | Every July with the risk assessment, and after a new service, a new vendor, a hire, a new tower site, or an incident (next review 2027-07-31) |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-4, PS-8, RA-2, RA-3, RA-5, CA-2, SA-9, AC-2, AC-3, AC-17, AU-6, CM-2, CM-6, IA-2, IA-2(1), IA-5, IA-8, SC-7, SC-8, SC-28, CP-2, CP-9, MP-6, SI-2, SI-3, SI-12, AT-2, IR-4, IR-5, IR-6, IR-8, PT-3 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, GV.SC-07, ID.AM-07, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, PR.DS-01, PR.DS-02, PR.DS-11, PR.PS-01, PR.PS-02, PR.IR-01, DE.AE-02, RS.MA-01, RS.MA-02, RS.CO-02, RC.RP-01 |
| Regulations | FCC CPNI rules, 47 CFR 64.2001-64.2011 (C-COMMUNICATIONS-R01); CALEA SSI rules, 47 CFR 1.20003-1.20006 (C-COMMUNICATIONS-R03); outage rules, 47 CFR 4.9(g), (h) (C-COMMUNICATIONS-R02); Fla. Stat. 501.171 |

## 1. Purpose
Protect customer information, especially customer proprietary network information (CPNI), and keep internet and home phone service running, in a way one person can actually do. Each rule below is written so it can be checked (P07).

## 2. Scope
All company information in any form (electronic, paper, spoken) on every system in the ISP Operations Systems Profile (SYS-01 to SYS-08), on the network at SITE-1 to SITE-4, on paper in the home office, and at every vendor that handles it. It applies to the owner-operator and to any future employee. Contractors and vendors are bound through their terms.

## 3. Roles and responsibilities
| Role | Held by | Responsibility |
|---|---|---|
| Security lead and privacy lead | Owner-operator | Runs this policy; decides breach questions; keeps records |
| CPNI certifying officer | Owner-operator | Signs the annual CPNI certification (section 4.8) |
| CALEA senior officer | Owner-operator | Section 4.7 |
| Risk acceptor | Owner-operator | Section 4.4 |
| On-call network consultant | Contractor (terms signed 2026-07-17) | Network help on request, in sessions the owner approves; no standing access |
| Tower and installation contractor | Contractor | Installs with a named installer account; no CPNI access |
| Vendors | Billing platform, wholesale VoIP provider, radio vendor, email, accounting | Operate their safeguards under their terms |

Because one person writes, follows, and checks these rules, independence is limited. Section 4.5 adds an outside check where it is affordable.

## 4. Governance, risk, and filings
4.1 The company must maintain a security program documented in this policy, the system profile (P02), and the risk register (P01). (PM-1; GV.PO-01)
4.2 The owner-operator is designated in writing, by this policy, as security lead, privacy lead, the officer for the annual CPNI certification (47 CFR 64.2009(e)), and the CALEA senior officer (47 CFR 1.20003(a)). (PM-2; GV.RR-02)
4.3 A risk assessment must be completed every July and after any major change, using NIST SP 800-30 Rev. 1. Every risk must be recorded with a treatment and a due date. (RA-3; PM-9)
4.4 Risk decisions: Low risks may be accepted with a written reason. Moderate risks may be accepted only with a dated plan or a written reason. High and Very High risks must be treated with a dated plan and must not be accepted as they are. (PM-9; GV.RM-01)
4.5 Security controls must be evaluated every July (P07). At least every second year, the evaluation must include review by someone outside the company, such as the network consultant. (CA-2)
4.6 This policy must be reviewed at least every year and after major changes or incidents. (PL-1; GV.PO-02)
4.7 **CALEA.** The company must keep written CALEA policies and procedures with a 24x7 contact appendix, file them with the FCC through CEFS, and refile within 90 days of any amendment. No interception or access to call-identifying information may be enabled without both a court order or other lawful authorization and the owner's personal approval and action, and each one must be recorded with the 47 CFR 1.20004 fields. (AC-3; PL-1; 1.20003-1.20005)
4.8 **Annual CPNI certification.** By March 1 each year the owner must sign and file the CPNI compliance certificate for the prior calendar year in EB Docket No. 06-36, with a statement that explains, accurately and with evidence, how the company's procedures ensure compliance, any actions against data brokers, and a summary of customer complaints about unauthorized release of CPNI. (CA-2; 64.2009(e))

## 5. Sanctions and exceptions
5.1 **Sanctions.** Any future employee who breaks this policy, including any misuse of CPNI, must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. Each sanction must be documented and kept for 2 years. (PS-8; GV.RR-04; 64.2009(b))
5.2 A contractor or vendor that breaks its terms or this policy must be dealt with under its contract, up to ending it. (SA-9)
5.3 The owner must record any personal departure from this policy as an exception under 5.4, with the reason and the fix.
5.4 **Exceptions** must be written, risk-rated under 4.4, recorded in the risk register, and must expire within 12 months. (PL-1)

## 6. Vendors and contractors
6.1 No vendor or contractor may receive or access CPNI or subscriber data until written terms cover confidentiality, security, and breach notice to the company. (SA-9; GV.SC-05)
6.2 The owner must keep a vendor list showing each vendor, whether it can access CPNI, the terms in place, and the date of its last security review. This list is also the record of third-party access to CPNI and must be kept for at least 1 year after each entry ends. (SA-9; ID.AM-07; 64.2009(c))
6.3 The billing vendor's SOC 2 report must be reviewed every year and the customer controls it lists must be operated. The wholesale VoIP provider must be asked for a SOC 2 report or a security questionnaire every year. (SA-9; GV.SC-07)
6.4 The network consultant connects only through the VPN with a named account, in sessions the owner approves each time; the owner disables the account after each engagement. (AC-17; PR.AA-05)

## 7. Access control and customer authentication
7.1 Every person must have their own account on every SaaS tool and network device. Shared accounts must not be used; the device local admin account is for emergencies only and its password is kept in the sealed envelope (7.9). (IA-2; AC-2; PR.AA-01)
7.2 MFA must be on for every service that offers it, including the billing platform, VoIP reseller portal, cloud radio controller, email, and accounting. (IA-2(1); PR.AA-03)
7.3 Passwords must be unique passphrases of at least 14 characters, stored in a password manager, never in the browser. Every network device must have a unique password, and vendor-default passwords and SNMP community strings must be changed before a device carries customer traffic. (IA-5; CM-6)
7.4 The owner must remove a helper's accounts the same day the work ends and review all accounts every quarter. (AC-2; PR.AA-05)
7.5 Device management (router, switch, access points, customer radios) must be reachable only from the management VLAN and the VPN, never from the internet or subscriber networks. (SC-7; PR.IR-01)
7.6 On the first business day of each month, the owner must review the sign-in histories of the VoIP portal, billing platform, email, and radio controller, and the router log server, and note the review in the security log. (AU-6; DE.AE-02)
7.7 **CPNI by phone and in person.** Call detail must never be given out on a customer-initiated call unless the customer gives a password that was not prompted by biographical or account information. Otherwise send it to the address of record or call back the telephone number of record. CPNI is not discussed in person at installs. (IA-8; 64.2010(b))
7.8 **CPNI online.** Customers may see CPNI only after signing in to the portal with a password set without biographical or account prompts. The AI support assistant and the text line may show CPNI only inside a signed-in portal session. The billing platform must notify the customer at the prior contact of record whenever a password, online account, email of record, or service address is created or changed. (IA-8; 64.2010(c), (e), (f))
7.9 **Emergency access.** SaaS recovery codes, the device emergency admin password, and a one-page access sheet must be kept in a sealed envelope held by the owner's attorney, for release to the network consultant if the owner is unavailable. (CP-2; AC-2)

## 8. Data handling
8.1 Information is classified in three levels. The whole customer account record is treated as Restricted, because the billing platform keeps broadband and home phone data in one record. (RA-2; ID.AM-07)

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | CPNI (call detail, home phone features, home phone invoices), customer account records, 911 registered addresses, NAT logs, credentials, router configurations | Approved systems only (8.2); MFA; encrypted; minimum necessary |
| **Confidential** | Contracts, tax and bank records, network maps, this policy set | Encrypted storage; owner only |
| **Public** | Plans, prices, broadband labels, outage banner | No restriction |

8.2 Restricted data may be kept only in the billing platform, the VoIP reseller portal, the radio controller, the business email and file storage, and the encrypted laptop. (AC-3; SA-9)
8.3 CPNI may be used only to provide, bill, support, and protect the home phone service, and to investigate fraud. It must not be used for marketing. Every customer's CPNI approval status is "none". Any future marketing use requires counsel review and the approval and notice rules first. (PT-3; 64.2005; 64.2009(a))
8.4 CDR exports must be imported straight into billing where the vendors support it. Otherwise each export must be deleted from the laptop and the file storage once the billing run is checked, and must never be sent by email. (SI-12; SC-28)
8.5 Every device that can hold Restricted data must use full-disk encryption. (SC-28; PR.DS-01)
8.6 Router and switch configurations must be copied automatically every week to the business file storage. (CP-9; PR.DS-11)
8.7 Old network devices, laptops, and phones must be reset to factory settings and wiped before reuse or disposal, and each disposal recorded. Paper sign-up forms are shredded after entry. (MP-6)
8.8 Security records (this policy, risk assessments, assessments, incident and breach records, CPNI certifications, CALEA records) must be kept at least 2 years, or longer where a rule requires. (SI-12; 64.2011(d))

## 9. Network, devices, and acceptable use
9.1 Company devices are for company work. Family members must not use them. (PL-4)
9.2 Router, switch, and radio firmware must be reviewed every quarter and security updates rated critical applied within 30 days. The owner subscribes to the router and radio vendors' advisories and to CISA Known Exploited Vulnerabilities alerts, and runs a monthly external port check. (SI-2; RA-5; PR.PS-02; ID.RA-01)
9.3 Automatic updates and the built-in antivirus must stay on for the laptop and phone. (SI-2; SI-3)
9.4 Router and switch configuration changes must be written in the change log with date and reason; radio settings come from controller templates. (CM-2; PR.PS-01)
9.5 Home phone ATAs must use the wholesale platform's encrypted signaling and media once available on each model. (SC-8; PR.DS-02)
9.6 **AI tools.** No customer data or CPNI may go into an AI tool except the billing platform's AI support assistant within the limits of 7.8 and the P10 assessment. Any new AI feature that reads account data needs a written P10 reassessment and the owner's approval first. (PL-4; SA-9)
9.7 The owner must complete a CPNI compliance course and a security awareness course every year and read monthly security bulletins. Any future employee must be trained on when CPNI may and may not be used before getting access. (AT-2; PR.AT-01; 64.2009(b))

## 10. Incident response
10.1 The company must keep an incident runbook (P08) with a printed contact list at home and in the SITE-1 shed. (IR-8; RS.MA-01)
10.2 Every suspected incident (unknown router login, portal alert, lost laptop, strange text-line request, vendor notice) must be written in the incident log the same day, with the time it was discovered. (IR-5; RS.MA-02)
10.3 **CPNI breach.** When the owner reasonably determines that someone intentionally accessed, used, or disclosed CPNI without authorization, the owner must notify the USSS and FBI through the FCC's reporting facility as soon as practicable and within 7 business days, and must not tell customers or the public until 7 full business days after that notice, unless the investigating agency agrees to earlier notice. (IR-6; RS.CO-02; 64.2011(a)-(c))
10.4 Each CPNI breach must be recorded (dates of discovery and notices, the CPNI involved, the circumstances) and the record kept at least 2 years. (IR-5; 64.2011(d))
10.5 Any compromise of a lawful intercept or any unlawful electronic surveillance on company premises must be reported to the affected law enforcement agencies within a reasonable time. (IR-6; 1.20003(c))
10.6 Outages that could affect the county 911 center must follow the P08 matrix. The 911 center's outage contact must be confirmed every year. The outage thresholds must be rechecked if home phone lines pass 1,000. (IR-6; CP-2; 4.9(h))
10.7 No ransom may be paid without counsel's advice and an OFAC sanctions check. (IR-4)
10.8 The runbook must be walked through every year and after any real incident. Lessons learned must be recorded within 30 days of closing an incident. (IR-8; ID.IM-02)

## 11. Contingency
11.1 Recovery follows the BIA (P05) priorities. (CP-2; RC.RP-01)
11.2 The owner must keep a standby agreement with the network consultant to restore service if the owner cannot. (CP-2)
11.3 A spare router loaded with the latest weekly configuration (8.6) must be kept in the SITE-1 shed, and a restore must be tested twice a year. (CP-9; PR.DS-11)
11.4 Before each hurricane season (by May 31), the owner must check tower mounts, batteries, generator fuel, and spare radios. (CP-2)

## 12. Compliance and enforcement
Compliance is checked in the annual control assessment (P07), the monthly review in 7.6, and the annual CPNI certification in 4.8. Sanctions follow section 5.

## 13. Related documents
P01 risk register; P02 system profile; P03 gap analysis; P05 BIA; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI use assessment. Pointer files POL-02 to POL-05 explain where each topic lives in this policy.

## Appendix A. Where CPNI and Restricted data live
| Item | Restricted data held | Protection required |
|---|---|---|
| VoIP reseller portal | Call detail, features, 911 addresses for 58 lines | 7.2, 7.6, 8.2 |
| Billing platform and portal | Accounts; home phone invoices with toll calls | 7.2, 7.8, 8.2 |
| AI support assistant | Account data it reads | 7.8, 9.6 |
| Laptop | Temporary CDR exports; configurations | 8.4, 8.5 |
| Router and switch | Signaling in transit; NAT logs; configurations | 7.5, 8.6, 9.2 |
| Business email and files | Weekly configuration copies; sign-up forms | 7.2, 8.4 |

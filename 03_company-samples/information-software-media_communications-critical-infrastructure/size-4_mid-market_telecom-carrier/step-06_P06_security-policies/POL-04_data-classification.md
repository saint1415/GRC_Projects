# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Vice President of Regulatory Affairs (CPNI compliance officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, incidents, or FCC rule changes |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-28, SI-12, CP-9, PT-2, PT-4, PT-5 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| FCC and CALEA rules | 47 U.S.C. 222; 64.2005-64.2009; 64.2011(d); 1.20004; 4.2; 9.20(c), (e) |
| Supporting standards | STD-08 Encryption and key management standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Classify company information by sensitivity and set handling rules so protection matches the harm a disclosure would cause, and so CPNI is used only as the FCC rules allow.

## 2. Scope
All workforce members and vendor agents, all systems (including vendor-operated systems and AI tools), and all company information: CPNI, lawful-intercept information, subscriber personal information, network configuration and outage information, Business Services customer data, and all other information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Vice President of Regulatory Affairs | Owns classification; approves new uses of CPNI, new models that use CPNI, and new vendors that receive Restricted data |
| Marketing Director | Checks CPNI approval before any campaign or model-driven offer; keeps the campaign register |
| Data Analytics Manager | Builds models only from the approved data warehouse views (section 4.4) |
| IT Director and Security Manager | Implement encryption, backup, retention, and disposal controls |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | CPNI (call detail, voice services and features, voice bills); the whole customer account record; lawful-intercept orders and content; account passwords and authentication answers; SSN digits and dates of birth; workforce and network element credentials; Business Services customers' call records | Encrypted at rest and in transit; need-to-know; approved systems only; access logged |
| **Confidential** | Network topology and device configurations; NORS filings (presumptively confidential, 47 CFR 4.2); 911 reliability certifications and supporting records (presumed confidential to the extent they describe non-public network details, 9.20(c)); security assessments; contracts | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules | Workforce only |
| **Public** | Rates, public outage status, website | No restriction |

(RA-2; ID.AM-07)
4.2 **Whole-account rule.** Broadband usage data is not CPNI while broadband is classified as an information service, but the BSS keeps one record per customer. The company therefore protects the whole customer account record, including broadband data, to the CPNI standard. (PT-2)
4.3 CPNI may be used without customer approval only as 47 CFR 64.2005 allows. Using CPNI to market communications-related services the customer does not already buy (including broadband to a voice customer) requires opt-out or opt-in approval, checked against the approval flag at the time of use. CPNI must never be used to identify or track customers who call competing providers (64.2005(b)(2)). (PT-2; PT-4; 64.2007; 64.2009(a))
4.4 **Models and analytics.** Any model, offer engine, or AI tool that uses CPNI must read it only through the data warehouse views that filter on the approval flag, must be approved by the Vice President of Regulatory Affairs before use, and must be listed in the campaign register when its outputs drive marketing. (PT-2; PT-4; 64.2009(a), (c))
4.5 Every campaign that uses CPNI must be approved in advance by a supervisor and recorded in the campaign register; every disclosure of CPNI to a third party must be recorded. The biennial opt-out notice must be sent every two years to every voice account, including SYS-18 accounts. Notices translated into another language must be translated in full. (PT-5; 64.2008(c)(8), (d)(2); 64.2009(c), (d))
4.6 Restricted data must be encrypted at rest on every device and service and encrypted in transit (STD-08). Configuration backups that contain device credentials are Restricted. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.7 Restricted data may be stored only in approved systems: the BSS, SYS-18 (until retirement), the cloud production and backup accounts, the contact center platform, the chatbot platform under its amended contract, the Business Services platform, the lawful-intercept system, and the backup vault. It must never be kept on personal devices, in personal cloud accounts, or in unapproved AI tools. (AC-3)
4.8 Backups must be encrypted, stored apart from production (the backup account in a second region; a copy of element configurations at CO-4), protected from alteration, and restore-tested quarterly (STD-07). (CP-9; PR.DS-11)
4.9 **Retention.** Call detail records are kept online for 18 months and then archived offline until 36 months, then destroyed, unless a legal hold applies (online retention reduced from 36 months by 2027-03-31). SSN digits and dates of birth are removed from account records once they are no longer used for authentication or credit. Lawful-intercept records follow the CALEA SSI policies (1.20004). 911 reliability supporting records are kept at least 2 years from each filing (9.20(e)). Other retention follows POL-01 4.13. (SI-12)
4.10 Media and network elements with storage must be wiped for reuse or destroyed by a certified vendor that provides a certificate of destruction. (MP-6; ID.AM-08)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.8), which expressly covers misuse of CPNI (47 CFR 64.2009(b)). Compliance is checked through the annual assessment (P07), the access reviews in POL-02, and the evidence gathered for the annual CPNI certification.

## 6. Exceptions
Exceptions follow POL-01 section 6. No exception may permit a practice the CPNI or CALEA rules prohibit.

## 7. Related documents
POL-01; POL-05; STD-07; STD-08; CPNI operating procedures; campaign register; P10 AI governance assessment

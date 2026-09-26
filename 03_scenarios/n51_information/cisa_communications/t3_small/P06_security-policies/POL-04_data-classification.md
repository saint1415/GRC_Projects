# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Regulatory Affairs Manager (privacy lead) |
| Approved by | COO |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes, incidents, or FCC rule changes |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-6, SC-8, SC-28, SI-12, CP-9, PT-2, PT-4, PT-5 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| FCC and CALEA rules | 47 U.S.C. 222; 64.2005-64.2009; 64.2011(d); 1.20004; 4.2 |

## 1. Purpose
Classify company information by sensitivity and set handling rules so protection matches the harm a disclosure would cause, and so CPNI is used only as the FCC rules allow.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at CO-1, CO-2, the warehouse and fleet yard, remote cabinets, and remote work locations, and the agents of vendors who access company systems, including the overflow call center. Covers all systems and data, including systems that vendors operate for the company. It applies to customer proprietary network information (CPNI), lawful-intercept information, subscriber personal information, network configuration and outage information, and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Regulatory Affairs Manager | Owns classification; approves new uses of CPNI and new vendors that receive Restricted data |
| Marketing Manager | Checks CPNI approval before any campaign; keeps the campaign register |
| IT Manager | Implements encryption, backup, retention, and disposal controls |
| All workforce | Handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted** | CPNI (call detail, voice services and features, voice bills); the whole customer account record; lawful-intercept orders and content; account passwords and authentication answers; SSN digits and dates of birth; workforce credentials | Encrypted at rest and in transit; need-to-know; approved systems only; access logged |
| **Confidential** | Network topology and device configurations; outage reports (NORS filings are presumptively confidential, 47 CFR 4.2); security assessments; contracts | Encrypted in transit; need-to-know |
| **Internal** | Procedures, schedules | Workforce only |
| **Public** | Rates, public outage status, website | No restriction |

(RA-2; ID.AM-07)
4.2 **Whole-account rule.** Broadband usage data is not CPNI while broadband is classified as an information service, but the BSS keeps one record per customer. The company therefore protects the whole customer account record, including broadband data, to the CPNI standard. (PT-2)
4.3 CPNI may be used without customer approval only as 47 CFR 64.2005 allows. Using CPNI to market communications-related services the customer does not already buy (including broadband to a voice-only customer) requires opt-out or opt-in approval, checked against the BSS approval flag at the time of use. Disclosure to third parties or affiliates for other marketing requires opt-in approval. (PT-4; 64.2007; 64.2009(a))
4.4 Every campaign that uses CPNI must be approved in advance by the Marketing Manager's supervisor and recorded in the campaign register. The biennial opt-out notice must be sent every two years. (PT-5; 64.2008(d)(2); 64.2009(c)-(d))
4.5 Restricted data must be encrypted at rest on every device and service and encrypted in transit. Configuration backups that contain device credentials are Restricted. (SC-28; SC-8; PR.DS-01; PR.DS-02)
4.6 Restricted data may be stored only in approved systems: the BSS, the cloud tenant, the contact center platform, the lawful-intercept system, and the backup vault. It must never be kept on personal devices, in personal cloud accounts, or in unapproved AI tools. (AC-3)
4.7 Backups must be encrypted, stored apart from production (a separate account and a second region; a copy of device configurations at CO-2), protected from alteration, and restore-tested quarterly. (CP-9; PR.DS-11)
4.8 **Retention.** Call detail records are kept online for 18 months and then archived offline until 36 months, then destroyed, unless a legal hold applies. SSN digits and dates of birth are removed from account records once they are no longer used for authentication or credit. Lawful-intercept records follow the retention stated in the CALEA SSI policies (1.20004). Other retention follows POL-01 4.10. (SI-12)
4.9 Media and network elements with storage must be wiped for reuse or destroyed by a certified vendor that provides a certificate of destruction. (MP-6; ID.AM-08)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.8), which expressly covers misuse of CPNI (47 CFR 64.2009(b)). Sanctions range from retraining to termination, and for vendor agents, removal from company work. Compliance is checked through the annual control assessment (P07), the access reviews in POL-02, and the evidence gathered for the annual CPNI certification.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the Chief Executive Officer for High risk), and expire within 12 months. No exception may permit a practice the CPNI, CALEA, or outage rules prohibit.

## 7. Related documents
POL-01; POL-05; CPNI operating procedures; campaign register; P10 approved AI tools list

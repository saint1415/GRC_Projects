# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Compliance and Security Coordinator |
| Approved by | Vice President of Operations |
| Effective date | 2026-09-01 |
| Review cycle | Annually each November (next review 2027-11-15), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-3, MP-6, AC-3, SC-8, SC-28, SI-12, CP-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-11 |
| FERC and related | Security Program Rev. 3A 3.2 (protection of sensitive information, OPSEC), 3.4.3.4 and 8.0 (marking), Table 9.3a (disposal, restoration), Form 1 Q22; 18 CFR 388.113 (CEII); 18 CFR 12.12 (project records) |

## 1. Purpose
Classify company information by sensitivity and set handling rules, so that information that could help someone attack the dam is protected, and so project records survive any failure of the project works.

## 2. Scope
All Cris Santos Company workforce members (employees, seasonal staff, contractors, and vendors with access). Covers information in every form: paper, OT systems, corporate systems, SaaS, cloud, removable media, and email.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Compliance and Security Coordinator | Owns classification; approves membership of the restricted CEII library |
| Chief Dam Safety Engineer | Owner of project records (18 CFR 12.12) and inundation maps |
| Controls Engineer | Owner of OT configuration data and PLC logic |
| IT Manager | Implements encryption, library permissions, backups, and disposal |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of four levels:

| Level | Examples | Handling |
|---|---|---|
| **Restricted: CEII and Security Sensitive** | Design drawings, EAP inundation maps, gate and unit control details, PLC logic, network diagrams, the Security Assessment, Security Plan, and certification letters, vulnerability findings (including P07 and P08 of this set) | Restricted library or locked cabinet only; named access; marked; encrypted; never on public AI tools or personal devices |
| **Confidential** | Employee personal information, contracts, settlement data, instrumentation readings and trends, historian data | Encrypted in transit; need-to-know |
| **Internal** | Procedures without security details, schedules | Workforce only |
| **Public** | Recreation information, public safety notices | No restriction |

(RA-2; ID.AM-07)
4.2 Restricted documents must be marked. CEII must carry "CEII - Do Not Release"; the Security Assessment, Security Plan, certification letters, and security correspondence with FERC must carry "Privileged - Security Sensitive Material". When CEII is filed with FERC, the filing must follow 18 CFR 388.113(d)(1) (justification, marking, and a public redacted version). (MP-3)
4.3 Electronic Restricted information must be stored only in the restricted CEII library, the OT systems, or the backup vault. It must not be kept in general file shares. Seasonal staff and recreation staff must not have access unless their role requires it. (AC-3; PR.DS-01; Rev. 3A Form 1 Q22)
4.4 Restricted and Confidential information must be encrypted in transit and at rest in SaaS, cloud, laptops, and removable media. (SC-8; SC-28; PR.DS-01; PR.DS-02)
4.5 Security details must not be sent to outside parties by email unless the recipient has a need to know and the message is encrypted. Hard copies of the Security Plan must not be given to outside agencies (Rev. 3A 7.3). (AC-3)
4.6 The Compliance and Security Coordinator must keep an inventory of where Restricted information is stored and which vendors receive it. (ID.AM-07)
4.7 Media and devices that held Restricted information, **including retired PLC cards, HMI drives, and panel memory**, must have operational data and configurations removed and be destroyed by a certified vendor that provides a certificate of destruction. (MP-6; ID.AM-08; Rev. 3A Table 9.3a; Form 3 Q19b)
4.8 PLC logic and HMI projects must be backed up after every approved change and at least monthly to an offline, write-protected copy and to the cloud backup vault, and must be restore-tested every year. Corporate data must be backed up daily and restore-tested quarterly. (CP-9; PR.DS-11; Rev. 3A Table 9.3a)
4.9 Permanent project records must be kept as 18 CFR 12.12 requires: originals at a central location secure from any failure of the project works, with key copies at the site. Security documentation must be kept for at least 6 years or longer if a license or FERC requires it. (SI-12)
4.10 Restricted information must not be entered into AI tools or other third-party services unless the tool is on the approved list for that level (see P10 and POL-05). (SA-9)

## 5. Compliance and enforcement
Violations are handled under the company's disciplinary procedure (POL-01 section 5). Unauthorized release of CEII is a serious violation. Compliance is checked through the annual control assessment (P07) and quarterly library membership reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; P10 AI approved-tools list; 18 CFR 388.113; 18 CFR 12.12; records retention schedule

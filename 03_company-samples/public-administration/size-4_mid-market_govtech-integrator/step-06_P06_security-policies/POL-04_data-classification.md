# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Director of Contracts and Compliance |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-4, MP-1, MP-3, MP-6, SA-3, SA-9, SC-8, SC-13, SC-28, SI-12, CP-9, CM-12 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| Agency requirements | Pub. 1075 sections 1.8.2, 2.C.5, 2.E.6.4, 3.3.1, Exhibit 7 I(5); CJISSECPOL v6.1 SC-13, SC-28; 7 CFR 272.1(c); 42 CFR 431.300-431.307; 18 U.S.C. 2721; Fla. Stat. 501.171(8) |
| Supporting standards | STD-08 Encryption and key management; STD-07 Contingency and recovery |

## 1. Purpose
Classify information by sensitivity and legal restriction, and set handling rules so protection matches the harm and the law.

## 2. Scope
All workforce members, and all information the company creates or receives, in every system, environment, account, and vendor service, including agency systems the company administers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Contracts and Compliance | Owns classification; approves any new use or location of Regulated data; keeps the data inventory |
| Director of Cloud Operations | Encryption, backup, retention, and deletion in the landing zone |
| VP of Engineering | Keeps production data out of non-production; tags FTI fields; data flows to analytics |
| Director of Data and AI | Data sent to AI services |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Information must be classified in one of five levels:

| Level | Examples | Handling |
|---|---|---|
| **Regulated** | FTI (AG-01), CJI including CHRI (AG-02, AG-39, and AG-02's agency-hosted systems), motor vehicle record personal information (AG-04) | Only in the owning agency's tenant or system; U.S. only; FIPS-validated encryption; screened and trained staff only; never in tickets, email, chat, analytics, or non-production |
| **Restricted** | Benefits applicant and household data (AG-03), Social Security numbers, driver license numbers, other agency personal information | Encrypted at rest and in transit; need-to-know; approved systems only |
| **Confidential** | Credentials and keys, security documents, source code, contracts | Encrypted in transit; need-to-know; secrets only in the secrets manager |
| **Internal** | Procedures, schedules | Workforce only |
| **Public** | Website, status page | No restriction |

(RA-2; ID.AM-07)
4.2 Regulated data must be encrypted in transit and at rest with FIPS 140 validated modules (FIPS 140-3 certified for CJI in transit), with keys controlled by the company, and must stay in U.S. systems reached only from the United States. (SC-8; SC-13; SC-28; PR.DS-01; PR.DS-02)
4.3 **FTI stays in the FTI enclave.** FTI may be stored only in the AG-01 enclave, its backups, and its log archive. It must never be copied to the analytics service, the AG-03 tenant, tickets, or any other account. Where FTI may be mixed with other data (for example free-text case notes), the whole field is treated and tagged as FTI and excluded from exports. If FTI is found anywhere else, it is reported under POL-03 and removed. (AC-4; MP-3; CM-12)
4.4 **No production data in non-production.** Development and staging use synthetic data or data from the masking pipeline. FTI is never copied out of production; any other use of real agency data outside production needs the agency's written approval first. (SA-3; PR.DS-01)
4.5 The Director of Contracts and Compliance keeps an inventory of where Regulated and Restricted data are stored and replicated, including analytics, backups, archives, and vendors, and confirms it each quarter. (CM-12; ID.AM-07)
4.6 **Deletion at contract end.** When a contract ends, the agency's data, including backups and archive copies beyond required retention, is returned or deleted within the contract's deadline, and the Director of Cloud Operations signs a deletion certificate for the agency. For FTI this is the Exhibit 7 purge certification. Disposal makes the data unreadable (Fla. Stat. 501.171(8)). (MP-6; SI-12; ID.AM-08)
4.7 Backups of Regulated and Restricted data must be encrypted, write-once, stored in a separate account and a second U.S. region, and restore-tested on the schedule in STD-07. (CP-9; PR.DS-11)
4.8 Regulated or Restricted data may be sent to an AI service only if the service is on the approved list (P10), is within the provider's FedRAMP authorization, and has signed data-use, retention, and no-training terms. FTI and CJI may never be sent to an AI service. (SA-9)
4.9 Retention follows each agency contract; security records are kept 7 years (POL-01 4.13). (SI-12)
4.10 **Motor vehicle records** are used only to perform AG-04's functions and are never resold or redisclosed. Highly restricted personal information (photographs, Social Security numbers, medical or disability information) is shown only to roles that need it and is never replicated outside the tenant. (AC-3; 18 U.S.C. 2721)

## 5. Compliance and enforcement
Violations are handled under POL-01 statement 4.8. Compliance is checked through quarterly data discovery scans, the annual control assessment (P07), and contract-end deletion certificates.

## 6. Exceptions
Exceptions follow POL-01 statement 4.7. Statements 4.2, 4.3, 4.4, and 4.10 cannot be excepted without the agency's written approval.

## 7. Related documents
POL-01; POL-05; STD-07; STD-08; P10 approved AI services list; agency contracts; IRS Publication 1075; CJIS Security Policy v6.1

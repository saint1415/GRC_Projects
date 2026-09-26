# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Contracts and Compliance Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-3, MP-6, SA-3, SC-8, SC-13, SC-28, SI-12, CP-9, CM-12 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| Agency requirements | Pub. 1075 sections 2.C.5, 2.E.6.4, 3.3.1, Exhibit 7 I(5); CJISSECPOL v6.1 SC-13, SC-28; AC-03 contract (7 CFR 272.1(c); 42 CFR 431.300-431.307) |

## 1. Purpose
Classify information by sensitivity and legal restriction, and set handling rules so protection matches the harm and the law.

## 2. Scope
All Cris Santos Company workforce members, wherever they work, and all information the company creates or receives, in every system, environment, and vendor service.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Contracts and Compliance Manager | Owns classification; approves any new use or location of Regulated data |
| Cloud Operations Lead | Implements encryption, backup, retention, and deletion |
| Director of Engineering | Keeps production data out of non-production |
| All workforce | Handle information according to its level |

## 4. Policy statements
4.1 Information must be classified in one of five levels:

| Level | Examples | Handling |
|---|---|---|
| **Regulated** | FTI (AC-01), CJI including CHRI (AC-02) | Only in the owning agency's tenant; U.S. only; FIPS-validated encryption; screened and trained staff only; never in tickets, email, chat, or non-production |
| **Restricted** | Benefits applicant and household data (AC-03), Social Security numbers, driver license numbers, other agency personal information | Encrypted at rest and in transit; need-to-know; approved systems only |
| **Confidential** | Credentials and keys, security documents, source code, contracts | Encrypted in transit; need-to-know; secrets only in the secrets manager |
| **Internal** | Procedures, schedules | Workforce only |
| **Public** | Website, status page | No restriction |

(RA-2; ID.AM-07)
4.2 Regulated data must be encrypted in transit and at rest with FIPS 140 validated modules (FIPS 140-3 certified for CJI in transit), with keys controlled by the company, and must stay in U.S. systems accessed only from the United States. (SC-8; SC-13; SC-28; PR.DS-01; PR.DS-02)
4.3 **FTI stays where the IRS approved it.** FTI may be stored only in the AC-01 tenant and its backups. It must never enter the AC-03 tenant, because human services agencies may not disclose FTI to contractors. Where FTI is mixed with other data, the whole record is treated and labeled as FTI, and exports from the AC-01 tenant carry an FTI label. (MP-3; CM-12)
4.4 **No production data in non-production.** Development, test, and staging use synthetic or masked data. Any use of real agency data outside production needs written approval from the agency and, for FTI, an approved IRS Data Testing Request obtained by the agency, before the data is copied. (SA-3; PR.DS-01)
4.5 The Cloud Operations Lead must keep an inventory of where Regulated and Restricted data are stored, including vendors and backups. (CM-12; ID.AM-07)
4.6 **Deletion at contract end.** When a contract ends, the agency's data (including backups and logs beyond required retention) is returned or deleted within the contract's deadline, and the Cloud Operations Lead signs a deletion certificate for the agency. For FTI this is the Exhibit 7 purge certification. (MP-6; SI-12; ID.AM-08)
4.7 Backups of Regulated and Restricted data must be encrypted, immutable, stored in a separate account and a second U.S. region, and restore-tested quarterly. (CP-9; PR.DS-11)
4.8 Regulated or Restricted data may be sent to an AI service only if the service is on the approved list (P10) and meets POL-01 4.9. (SA-9)
4.9 Retention follows each agency contract; security records are kept 7 years (POL-01 4.11). (SI-12)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through data discovery scans, the annual control assessment (P07), and contract-end deletion certificates.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. Statements 4.2, 4.3, and 4.4 cannot be excepted without the agency's written approval.

## 7. Related documents
POL-01; POL-05; P10 approved AI services list; agency contracts; IRS Publication 1075; CJIS Security Policy v6.1

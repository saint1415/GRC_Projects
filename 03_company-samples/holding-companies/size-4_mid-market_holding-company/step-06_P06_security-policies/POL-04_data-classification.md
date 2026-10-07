# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and its subsidiaries |
| Policy ID | POL-04 |
| Owner | General Counsel (with the Security Manager) |
| Approved by | CEO |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (new; the 2024 set had no classification policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-21, CM-12, SC-8, SC-28, MP-6, SI-12 |
| CSF 2.0 | ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10 |
| FTC Safeguards Rule (Finance) | 16 CFR 314.4(c)(2), (c)(3), (c)(6) |
| HIPAA (group health plan) | 45 CFR 164.310(d); 164.312(a)(2)(iv), (e)(1); 164.504(f)(2)(iii) |
| Florida | Fla. Stat. 501.171(2), (8) |
| Supporting standards | STD-08 Encryption; STD-12 Retention schedule |

## 1. Purpose
Set one way to label and handle information across five companies, so that each company's sensitive data stays with that company, and so that the people and tools that can reach data (including the AI assistant) only reach what they should.

## 2. Scope
All information created, received, or kept by any group company, in any format, including data held by service providers and data inherited through acquisitions.

## 3. Classification levels
| Level | Examples | Minimum handling |
|---|---|---|
| **Restricted** | Finance customer information (SSNs, bank accounts, credit reports); plan PHI; employee SSNs and bank details; vendor bank details; ACH and wire files; credentials and secrets; material non-public deal information | Named access approved by the data owner; encrypted at rest and in transit; Restricted label applied; no all-employee sharing; no external forwarding without approval; no AI retrieval unless approved under 4.6 |
| **Confidential** | Financial statements before release; contracts; pricing; HR records other than SSNs; security reports | Need-to-know access; encrypted in transit; external sharing with approval |
| **Internal** | Procedures, schedules, internal announcements | Group workforce only |
| **Public** | Marketing, published price lists | No restriction |

## 4. Policy statements
4.1 Every collaboration site, shared folder, and data store must have an owner and a classification. Owners must review permissions every quarter. (RA-2; AC-3; ID.AM-05)
4.2 The Security Manager must keep a data map showing where Restricted data is stored, by company and data type, and update it at each acquisition and new system (by 2026-12-31). (CM-12; ID.AM-07; 314.4(c)(2); 164.308(a)(1)(ii)(A))
4.3 Restricted data of one company may not be placed where staff of another company can reach it unless that company's data owner approves. Sites holding Restricted data must carry the Restricted label, which blocks all-employee access, external sharing, and AI assistant retrieval. (AC-3; AC-21; PR.DS-10; 314.4(c)(1)(ii))
4.4 **Plan PHI** may be kept only in the restricted benefits site, the HRIS, and the TPA, PBM, and stop-loss portals. It must not be downloaded to local drives or sent by email except through the TPA's secure channels, and it may never be used for employment decisions (164.504(f)(2)(ii)(C)). (AC-3; SC-28; 164.504(f)(2)(iii); 164.310(d))
4.5 Restricted data must be encrypted at rest and in transit (TLS 1.2 or higher; SFTP for bank files). Where encryption is infeasible, the Qualified Individual must approve compensating controls in writing for Finance data. (SC-8; SC-28; PR.DS-01; PR.DS-02; 314.4(c)(3); 164.312(a)(2)(iv), (e)(1))
4.6 Restricted data may be used in an approved AI tool only for approved purposes listed in the P10 decision, and never in an unapproved tool. (AC-21; PR.DS-10)
4.7 **Retention and disposal.** Data must be kept only as long as STD-12 allows. Finance customer information must be disposed of no later than 2 years after its last use for the customer, unless a legal or business exception in STD-12 applies; ACH files on the SFTP server must be deleted after 90 days; plan security documentation must be kept 6 years. (SI-12; 314.4(c)(6); 164.316(b)(2)(i); Fla. Stat. 501.171(8))
4.8 Media and devices must be sanitized or destroyed with a certificate before disposal or reuse, at every site, and the disposal tracked to the asset record. (MP-6; 164.310(d)(2)(i)-(ii))
4.9 Deal information must be shared only in the virtual data room or Restricted deal sites; personal sharing links are prohibited. (AC-21; PR.DS-01)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Compliance is checked through quarterly permission reviews, the AI cross-entity test (P10), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.7. Exceptions for Finance encryption need the Qualified Individual's written approval.

## 7. Related documents
POL-01; POL-05; STD-08; STD-12; STD-13; P10 AI decision

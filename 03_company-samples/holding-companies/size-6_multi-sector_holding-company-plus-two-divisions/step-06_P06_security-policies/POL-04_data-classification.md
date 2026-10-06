# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all subsidiaries |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-4, AC-21, MP-6, PT-2, PT-3, RA-2, SC-8, SC-28, SI-12 |
| CSF 2.0 | ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10 |
| Regulatory drivers | N55-R06 (164.504(f)(2)(iii)); N62-R02 (164.502(b); 164.514(d)); N52-R07 (Model #668 sec. 3K, 4B(4), 4D(2)(d), (k)); N55-R01 and N55-R02 (MNPI); Fla. Stat. 501.171(2) and (8) |

## 1. Purpose
Classify group information so it can be protected and shared correctly, and keep each regulated entity's information within the purposes its law allows, even though the entities share one platform.

## 2. Scope
All information created or held by the group in any form, including information in collaboration sites, email, and AI assistant outputs.

## 3. Classification levels
| Level | Examples | Owner |
|---|---|---|
| **Restricted** | Health Care Services PHI; group health plan PHI; insurers' nonpublic information about consumers (including claimant medical information, Model #668 sec. 3K(3)); SSNs and bank account numbers; payment templates; MNPI on results and transactions; credentials and keys | The owning entity's data owner |
| Confidential | Contracts, internal financial data, security reports | Function head |
| Internal | Policies, procedures, internal communications | Author's manager |
| Public | Published materials | Communications |

## 4. Policy statements
4.1 Every collaboration site, file share, and dataset holding Restricted data must carry a Restricted sensitivity label naming the owning entity by 2026-12-31. Restricted sites must not be open to all employees of the group. (RA-2; ID.AM-07)

4.2 **Entity boundaries.** Restricted data belongs to one regulated entity. It may be shared with another entity only with the owning data owner's approval, a documented legal basis and purpose, and only the minimum necessary. Routine and recurring disclosures (for example, clinic reports to the group insurer and to employers) must follow a written protocol. (AC-21; PT-3; 164.502(b); 164.514(d)(3))

4.3 **Group health plan PHI** may be stored only in the plan administration unit's restricted workspace and the administrator's systems. No export from SYS-G5 or the administrator may land anywhere else. (AC-4; PT-3; 164.504(f)(2)(iii))

4.4 **MNPI** must stay in the board portal and deal rooms; exports to collaboration sites are prohibited. (AC-21; PR.DS-10)

4.5 Restricted data must be encrypted in transit over external networks and at rest on all devices and storage. (SC-8; SC-28; PR.DS-01; PR.DS-02; Model #668 sec. 4D(2)(d))

4.6 **AI assistants** must not retrieve content from Restricted-labeled sites except for uses approved under the Group AI Standard (P10). Outputs inherit the highest classification of their sources. (AC-21; PR.DS-10)

4.7 **Retention and disposal.** Each division must keep a retention schedule and enforce it in its systems, including automated purge of closed insurance claims past retention. Media must be sanitized before reuse or disposal. (SI-12; MP-6; Model #668 sec. 4B(4), 4D(2)(k); Fla. Stat. 501.171(8))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Label coverage and over-shared sites are reported monthly.

## 6. Exceptions
Exceptions follow POL-01 section 4.12.

## 7. Related documents
POL-01; POL-02; POL-05; Group AI Standard (P10).

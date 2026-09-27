# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-04 |
| Owner | Radiation Safety Officer |
| Approved by | General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-4, MP-6, SC-8, SC-28, SI-12, CP-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-11, ID.AM-08 |
| Regulatory basis | 10 CFR 37.31, 37.43(d), and 37.101 through the Florida license condition; 49 CFR 172.802(c); 40 CFR 264.74; Fla. Stat. 501.171 |

## 1. Purpose
Classify company information by sensitivity and set handling rules, so protection matches the harm a disclosure, alteration, or loss would cause. Special attention goes to information that could help someone steal or sabotage radioactive material.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and temporary staff) at the Plant, in company vehicles, and at customer sites. Covers all company systems and data, including systems that vendors operate for the company, the plant OT network, and the physical security systems. It applies to Part 37 security-related information and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Radiation Safety Officer | Owns classification; keeps the information access list for Security-Related data |
| HR Manager | Custodian of background investigation files |
| IT Manager | Implements encryption, restricted libraries, backup, and disposal controls |
| All workforce | Label and handle information according to this policy |

## 4. Policy statements
4.1 Information must be classified in one of five levels:

| Level | Examples | Handling |
|---|---|---|
| **Security-Related** | Part 37 security plan, implementing procedures, list of approved individuals, DOT security plan, category 2 shipment schedules, security system layouts and credentials | Information access list only (need to know plus trustworthiness and reliability determination); restricted library with no sync, download, or external sharing; printed copies in a locked cabinet; never email outside the company |
| **Restricted** | Background investigation and criminal history records, Social Security numbers, identity documents, credentials | Named custodians only; encrypted at rest and in transit; restricted library |
| **Confidential** | Customer waste profiles, source serial numbers, manifests, contracts, payroll, financials | Encrypted in transit; need to know; shared with customers only through the portal |
| **Internal** | Procedures, schedules, training materials | Workforce only |
| **Public** | Website, brochures | No restriction |

(RA-2; ID.AM-07)

4.2 Security-Related files must carry a header "SECURITY-RELATED INFORMATION: access limited under 10 CFR 37.43(d)". They must be stored only in the RSO's restricted library or the locked cabinet. Information stored electronically must be protected by the identity provider's MFA. (MP-4; AC-3; 37.43(d)(1), (7))

4.3 Background investigation records must be kept in a system of files that only the RSO and HR Manager can open. They may be disclosed only to the individual, a representative, or people with a need to know for the access decision. (MP-4; 37.31(a)-(b))

4.4 Security-Related and Restricted data must never be entered into AI tools or any third-party service that is not approved for that level (see POL-05). (SA-9)

4.5 **Safeguards Information.** If anyone receives a document marked Safeguards Information, they must not copy or forward it. They must give it to the RSO at once, who will follow 10 CFR 73.21-73.22 and ask the sender for instructions. (MP-4)

4.6 Restricted and Confidential data must be encrypted at rest on every device and service, and encrypted in transit. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.7 Media and paper holding Security-Related or Restricted information must be cross-cut shredded, or destroyed by a certified vendor that provides a certificate of destruction. (MP-6; ID.AM-08)

4.8 **Records protection.** Regulatory records (source inventory, manifests, shipment coordination, training, and test records) must be backed up to storage that is separate from production and protected from alteration. They must be restore-tested quarterly. (CP-9; PR.DS-11; 37.101)

4.9 **Retention.** Records must be retained for the period in the regulation that requires them. Where Part 37 sets no period, keep them until license termination (37.103). Retention labels must be applied so that records cannot be deleted early. (SI-12; 40 CFR 264.74)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the Part 37 program reviews, and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months. No exception may allow Security-Related information outside the information access list.

## 7. Related documents
POL-01; POL-02; POL-05; SEC-10 Information Protection procedure (restricted); records retention schedule; P10 AI approved-tools list

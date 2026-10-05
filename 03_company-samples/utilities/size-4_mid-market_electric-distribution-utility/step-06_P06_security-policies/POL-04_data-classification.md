# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Information Security Manager, with the Vice President of Customer Operations for customer data |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2022 policy) |
| Review cycle | Annually (next review by 2027-09-30), and after new data types, new clients, or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-3, MP-6, SC-8, SC-12, SC-28, SI-12, AC-3, CP-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| NERC and other | 16 CFR 682.3; Fla. Stat. 501.171(2) and (8); 18 CFR 388.113 (CEII); client utility contracts |

## 1. Purpose
Make sure every piece of company and client information is protected according to the harm its disclosure, alteration, or loss could cause, and that the company keeps only what it needs.

## 2. Scope
All information the company creates, receives, or holds, in any form (electronic, paper, verbal), including information held for the 4 client utilities and information held by vendors for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Data owners (Vice President of Customer Operations for customer data; Director of Utility Services for client data; Director of Engineering and Protection for relay and substation data; Director of System Operations for operational data) | Classify their data; approve access and sharing; set retention |
| Information Security Manager | Maintains this policy and the encryption and logging standards |
| Records manager (in the General Counsel's office) | Maintains the records schedule |
| Workforce | Label, handle, and dispose of data as this policy requires |

## 4. Classification levels
| Level | Definition | Examples |
|---|---|---|
| **Restricted** | Disclosure or alteration could endanger the grid or crews, enable identity theft, or trigger breach notice | SSNs, driver license numbers, bank account numbers, consumer reports; relay settings and gateway access lists; OT network diagrams and one-line diagrams (potential CEII and BES Cyber System Information); SCADA configuration and credentials; client utility customer data |
| **Confidential** | Disclosure could harm customers, clients, or the company | Customer names, addresses, usage and interval data, call recordings; contracts; security assessments and this program's deliverables |
| **Internal** | For workforce use; limited harm if disclosed | Procedures, organization charts, non-sensitive email |
| **Public** | Approved for release | Outage maps, tariffs, press releases |

## 5. Policy statements
5.1 Every data set and system must be assigned a classification by its owner, recorded in the asset inventory. Data from different levels takes the highest level. (RA-2; ID.AM-07)

5.2 Restricted data must be encrypted in transit outside the OT network and at rest in all IT, cloud, and SaaS systems, using STD-10. Restricted OT data that cannot be encrypted on legacy devices must be protected by network isolation. (SC-8; SC-28; PR.DS-01; PR.DS-02)

5.3 **Minimize identity data.** SSNs and driver license numbers may be collected only for identity verification and credit decisions, must not be copied into reports, extracts, or analytics, and must be purged 2 years after the final bill and debt resolution. Bank account numbers must be tokenized outside the CIS. (SI-12; PR.DS-10; Fla. Stat. 501.171(2))

5.4 **Extracts.** Bulk extracts of Confidential or Restricted data from the CIS or AMI must be approved by the data owner, limited to the fields needed, kept no longer than 35 days unless the owner approves a longer period, and stored only in approved locations with access logging. (AC-3; SI-12)

5.5 **Client utility data** must be kept logically separate from company data, used only for the client's contracted services, and returned or destroyed at contract end as the contract requires. (AC-3; AC-4)

5.6 **CEII and BES Cyber System Information.** Relay settings, gateway access lists, network diagrams, and one-line diagrams must be labeled Restricted, stored only in the engineering repository, and shared with vendors only through the controlled file transfer service under a non-disclosure agreement. Material filed with FERC that qualifies as CEII must be submitted with the CEII designation request under 18 CFR 388.113. (MP-3; AC-3)

5.7 **Disposal.** Paper with Confidential or Restricted data must go in locked shred bins at every site and be shredded by the contracted vendor. Electronic media must be wiped or destroyed with a certificate. Relays, RTUs, and gateways leaving service must have settings and credentials erased first. Consumer information must be disposed of by these methods. (MP-6; PR.DS-01; 16 CFR 682.3; Fla. Stat. 501.171(8))

5.8 Backups of Restricted and Confidential data must be encrypted, kept in a separate account or offline, and protected from deletion for their retention period. (CP-9; PR.DS-11)

5.9 Records must follow the records schedule kept by the General Counsel's office, which sets retention for customer, credit, operational, and compliance records. (SI-12)

## 6. Compliance and enforcement
Violations are handled under POL-01 4.10. Compliance is checked through P07, data-access logging, quarterly shred bin checks, and the yearly retention purge report.

## 7. Exceptions
Exceptions follow POL-01 4.9. Statements 5.3 and 5.7 carry federal and state requirements and cannot be excepted.

## 8. Related documents
POL-01; POL-02; STD-10 Encryption and key management standard; STD-11 Data retention and disposal standard; records schedule; Identity Theft Prevention Program; P04 cloud control map

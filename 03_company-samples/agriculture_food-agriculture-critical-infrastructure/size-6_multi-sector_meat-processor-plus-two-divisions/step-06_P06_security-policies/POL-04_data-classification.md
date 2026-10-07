# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer, with the Group Chief Food Safety and Quality Officer for food safety records |
| Approved by | Group CISO, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-4, AU-9, CM-8, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| Regulatory drivers | 9 CFR 417.5(d)-(e); 21 CFR 121.305, 121.315; 21 CFR 117.206(a)(5); 21 CFR 1.912; PCI DSS Req. 3, 4, 9.4; state breach laws |
| Division supplements | Meat Processing: formulations, food defense plan, CCP records. Food Distribution: 3PL customer data and temperature history. Grocery Retail: cardholder data and loyalty data |

## 1. Purpose
Classify group information by sensitivity and set handling rules, so that food safety records stay trustworthy, sensitive food defense and formulation information stays restricted, and personal and cardholder data is protected.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including OT data, records held by SaaS providers for the group, and data on shared platforms.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes and personal information rules |
| Division VP FSQA and Division food safety manager (Distribution) | Own food safety record rules for their divisions |
| Data owners | Classify datasets; approve access and sharing |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (cardholder data, personal information of customers and employees, food defense plans and vulnerability assessments, formulations, credentials, and keys), **Confidential** (CCP and food safety records, 3PL customer data, contracts), **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys. Cardholder data must not be stored; card payments must use P2PE terminals or the processor's hosted payment fields. (SC-28; SC-8; PR.DS-01; PR.DS-02; PCI DSS Req. 3.2, 4.2)

4.3 **Food defense plans and formulations** must be stored only in restricted libraries limited to named FSQA and controls engineering roles. A controlled printed copy of the Plant 6 food defense plan is kept onsite in the FSQA office. (AC-3; PR.DS-10; 21 CFR 121.315(c))

4.4 **Food safety records** (CCP, Sanitation SOP, food defense monitoring, DC temperature monitoring, and sanitary transportation records) must be created when the activity occurs, attributed to a named person, protected so that original values are kept on any edit, and retained for the period the governing rule sets. Electronic record systems must have audit trails enabled. (AU-9; SI-12; 9 CFR 417.5(b), (d)-(e); 21 CFR 121.305; 21 CFR 117.206(a)(5))

4.5 **3PL customer data and temperature history** must be visible only to that customer and kept append-only. (AC-3; AU-9)

4.6 Backups of Restricted and Confidential information must be immutable or offline, held apart from production (a different provider or account, or an offline copy for OT), and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11)

4.7 Media holding Restricted information must be sanitized or destroyed with a certificate. Returned payment terminals go back to the solution provider. (MP-6; ID.AM-08; PCI DSS Req. 9.4)

4.8 Information must be retained per the group retention schedule, which must meet or exceed each food safety rule's retention period. (SI-12)

4.9 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard with contract terms that prohibit training on group data. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AU-9, CP-9, SC-28), PCI DSS data discovery scans, and FSQA verification records.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP; P10 Group AI Standard; group retention schedule.

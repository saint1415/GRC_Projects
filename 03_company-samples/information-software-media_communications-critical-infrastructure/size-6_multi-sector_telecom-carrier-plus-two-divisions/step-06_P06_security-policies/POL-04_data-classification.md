# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, PT-3, AC-4, AC-21, CM-8, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| Regulatory drivers | C-COMMUNICATIONS-R01 (47 U.S.C. 222(c); 47 CFR 64.2005, 64.2007, 64.2009(c)); C-COMMUNICATIONS-R03 (47 CFR 1.20003, 1.20004); N54-R04 (FAR 52.204-21(b)(1)(i)-(iv), (vii)); 47 CFR 17.49; state breach laws |
| Division supplements | Carrier: CPNI manual. Engineering: FCI enclave standard; customer data rules. Tower: landowner data and fiber route rules |

## 1. Purpose
Classify group information by sensitivity and by whose data it is, and set handling rules so that CPNI, lawful-intercept information, federal contract information, customer network data, and landowner data are used only for their permitted purposes.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including on shared platforms such as the service assurance platform and in SIEM copies.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns classes, the purpose register, and affiliate data rules |
| Carrier CPNI compliance officer | Owns CPNI uses, approvals, and the campaign register |
| Data owners | Classify data and approve feeds and access |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (CPNI and the whole customer account record, call detail records, lawful-intercept information, landowner taxpayer IDs and bank data, credentials and keys, network element configurations, and fiber route maps), **Confidential** (federal contract information, customer network designs and data, outage filings), **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted and Confidential information must be encrypted at rest and in transit with approved algorithms and group-managed keys. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 **Whole-account rule.** The whole Carrier customer account record, including broadband usage data that is not CPNI under current law, must be protected to the CPNI standard. (PT-3; ID.AM-07)

4.4 **CPNI use and disclosure.** CPNI may be used or disclosed only for the purposes 47 U.S.C. 222(c)(1) and (d) allow, or with the customer approval 64.2007 requires, checked through the BSS approval flag at the time of use. CPNI may be disclosed to an affiliate only under an intercompany CPNI agreement that names the purpose. Every campaign by the Carrier or an affiliate that uses CPNI, and every disclosure to a third party, must be recorded in the campaign register and kept at least 1 year. (PT-2; PT-3; AC-21; PR.DS-10; 47 CFR 64.2007(b); 64.2009(a), (c))

4.5 **Lawful-intercept information** (orders, intercept content, call-identifying information, and intercept records) may be handled only by authorized lawful-intercept employees on SYS-C8. It must never be placed in shared tools, tickets, email, or AI tools. (AC-3; AC-4; 47 CFR 1.20003; 1.20004)

4.6 **Federal contract information** must stay in the SYS-E2 enclave. It must not be posted on public systems or copied to the general design workspace. (AC-4; AC-22; FAR 52.204-21(b)(1)(i)-(iv))

4.7 Backups of Restricted information must be immutable, held with a different provider or account from production, and restore-tested at least quarterly for High-criticality systems. Network element configurations must also have an offline encrypted copy in a second region. (CP-9; PR.DS-11)

4.8 Media holding Restricted or Confidential information must be sanitized or destroyed with a certificate before disposal or reuse. (MP-6; ID.AM-08; FAR 52.204-21(b)(1)(vii))

4.9 Information must be retained per the group retention schedule. CDRs are kept online no more than 24 months. Antenna structure light outage records must be kept 2 years. Staging copies must be purged within 7 days. (SI-12; 47 CFR 17.49)

4.10 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard and its contract prohibits training on group data and limits retention. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-3, AC-21, PT-3, MP-6, CP-9) and the campaign register review.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may permit a use of CPNI that the rules require approval for.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP for the OSS/BSS; Carrier CPNI manual; P10 Group AI Standard.

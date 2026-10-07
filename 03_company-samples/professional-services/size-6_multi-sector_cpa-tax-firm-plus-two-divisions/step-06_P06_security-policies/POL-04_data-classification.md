# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions; adopted by CPA Partners |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, PT-3, PT-4, AC-4, AC-21, CM-8, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory basis | 16 CFR 314.4(c)(2), (c)(3), (c)(6); 26 CFR 301.7216-1(b)(3), 301.7216-2(o), 301.7216-3; 17 CFR 248.30(b); 45 CFR 164.312(a)(2)(iv), (e) |
| Division supplements | Tax and Advisory: consent register and referral fields. Wealth: integrated planning data and archived records. Practice Cloud: customer data and sub-processors. CPA Partners: engagement files and PHI |

## 1. Purpose
Classify group information by sensitivity and by whose information it is, and set handling rules so that tax return information, customer information, and customer firms' data are used only for their permitted purposes.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including information one group entity holds for another.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns the classes, the purpose register, and the consent register design |
| Data owners | Classify and tag data stores; approve flows and access |
| System owners | Enforce tags, purposes, and retention in their systems |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (tax return information, GLBA customer information, Wealth customer information, Practice Cloud customer data, PHI, credentials, and keys), **Confidential** (engagement files, client business information, internal financials), **Internal**, or **Public**. (RA-2; ID.AM-07; 314.4(c)(2))

4.2 Restricted information must be encrypted at rest and in transit with approved algorithms and group-managed keys. Returns and source documents must be delivered to clients through the portal, not as email attachments. (SC-28; SC-8; PR.DS-01; PR.DS-02; 314.4(c)(3))

4.3 **Owner tags.** Every data store holding Restricted information must carry a tag for the entity whose information it is (Tax and Advisory, Wealth, a Practice Cloud customer, or a CPA Partners client) and its permitted purposes. (CM-8; PT-3; ID.AM-07)

4.4 **Tax return information leaving Tax and Advisory.** Tax return information may leave Tax and Advisory only through approved interfaces, and only for a 301.7216-2 permission or under a consent recorded in the consent register before the transfer. The interface must check the register and send only the fields the consent names. Consents to solicitation of non-tax services must name the recipient and each type of product or service, be requested at engagement start (never after the completed return is provided for signature), and record refusals so that no repeat request is made. (AC-4; AC-21; PT-4; PR.DS-10; 301.7216-3(a)(3), (b)(1)-(3))

4.5 **Statistical compilations.** Compilations of tax return information are tax return information. They may be produced only for Tax and Advisory's own tax preparation business or bona fide tax research, and may be shared only anonymously, from 10 or more returns, in direct support of that business. No other group entity may build or use them without a consent that covers the use. (PT-3; 301.7216-1(b)(3)(i)(B); 301.7216-2(o))

4.6 Backups of Restricted information must be immutable, held with a different provider or account from production, and restore-tested at least quarterly for High-criticality systems. (CP-9; PR.DS-11)

4.7 **Retention and disposal.** Information must be kept per the group retention schedule (tax return information 7 years, with Forms 8879 at least 3 years; Wealth required records at least 5 years) and securely disposed of afterward. Customer information must be disposed of no later than two years after its last use for the customer unless the schedule records a business or legal need. Purge jobs must be verified each quarter. (SI-12; MP-6; ID.AM-08; 314.4(c)(6); 248.30(b); 275.204-2(e)(1))

4.8 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard, the contract prohibits training and secondary use and requires U.S.-only processing, and the Chief Tax Officer (for tax return information) or the data owner has confirmed the legal basis. (SA-9; PL-4; 301.7216-3(b)(4))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the P07 assessment (AC-4, AC-21, PT-3, PT-4, SI-12) and quarterly purge and consent-register reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may permit a disclosure that IRC 7216 does not.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP for the TPCP; P10 Group AI Standard.

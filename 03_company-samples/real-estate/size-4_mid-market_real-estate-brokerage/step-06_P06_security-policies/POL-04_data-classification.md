# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC |
| Policy ID | POL-04 |
| Owner | General Counsel, with the Security Manager (Qualified Individual) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-29 |
| Effective date | 2026-10-15 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-8, SC-12, SC-13, SC-28, AC-5, SI-7, MP-4, MP-6, SI-12, CM-8 |
| CSF 2.0 | ID.AM-05, ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10 |
| FTC Safeguards Rule (N53-R01) | 16 CFR 314.4(c)(2), (c)(3), (c)(6)(i)-(ii) |
| Other rules | Fla. Stat. 501.171(8); 16 CFR 682.3; Fla. Stat. 626.8473(4) |
| Supporting standards | STD-05 Payment instruction and payee verification; STD-08 Encryption and key management; STD-10 Records retention and disposal |

## 1. Purpose
Classify information by the harm its loss or alteration would cause, and set handling rules for each class. Payment instructions get their own class because the main harm is alteration, not disclosure.

## 2. Scope
All information created or received by either entity or by contractor agents on the company's behalf, in any form (electronic, paper, voice).

## 3. Classes
| Class | Examples | Key handling rules |
|---|---|---|
| **Restricted: Payment** | Wire instructions, payee and bank account details, payoff statements, owner and agent payout accounts, disbursement ledgers | Integrity first: out-of-band verification and two-person control for any change (4.3 to 4.5); delivered only through the Closing Communications Portal; never sent or forwarded by email |
| **Restricted: Personal and financial** | Customer information under 16 CFR 314 (closing files, IDs, Social Security numbers, loan data); consumer reports and rental applications; client bank data | Encrypted in transit and at rest; minimum necessary access; disposal per STD-10 |
| **Confidential** | Contracts, listing agreements, transaction files without the items above, owner agreements, employee and agent records | Access by role; not shared outside the company without a business need |
| **Internal** | Policies, procedures, internal reports | Company systems only |
| **Public** | Listings as published, marketing | Fair housing review before publication (P10) |

## 4. Policy statements
4.1 Every system in the asset inventory must record the highest class of information it holds. System owners must keep data inventories for Restricted information current. (RA-2; CM-8; ID.AM-07; 314.4(c)(2))

4.2 **Encryption.** Restricted information must be encrypted in transit over external networks (TLS 1.2 or higher) and at rest (AES-256 or provider equivalent), under STD-08. Email containing Social Security numbers, account numbers, or ID numbers must be encrypted automatically by the email security rule. Where encryption is infeasible, the Qualified Individual must approve a compensating control in writing, and the approval must be listed in the SSP. (SC-8; SC-28; PR.DS-01; PR.DS-02; 314.4(c)(3))

4.3 **Payment instructions.** Wire instructions for buyers and sellers must be delivered only through the Closing Communications Portal. No employee or contractor agent may send, forward, or change wire instructions by email, text, or chat. (SI-7; PR.DS-10; Fla. Stat. 626.8473(4))

4.4 **Payee and bank account changes.** Any new payee or change to an existing payee's bank details, in any system (SYS-02, SYS-10, SYS-13, or a bank platform), requires (a) a callback to a phone number taken from the file or an independent published source, never from the request, and (b) entry by one person and approval by another. The first payment to a changed account must be held for the period set in STD-05. (AC-5; SI-7; PR.AA-05; 314.4(c)(1)(ii))

4.5 **Payoffs.** Payoff statements must be obtained from the lender's portal or confirmed by calling the lender at its published number. Payoff instructions received by email alone must not be used. (SI-7; Fla. Stat. 626.8473(4))

4.6 **Retention and disposal.** Information must be kept only as long as the retention schedule in STD-10 allows. Customer information must be disposed of no later than two years after the last date it was used to provide a service to the customer, unless the schedule documents a business, legal, regulatory, or underwriter reason to keep it longer or targeted disposal is not reasonably feasible. The schedule must be reviewed each year. (SI-12; MP-6; ID.AM-08; 314.4(c)(6)(i)-(ii))

4.7 Disposal must make information unreadable: cross-cut shredding or pulping for paper, and certified wiping or destruction for media, with certificates kept. Consumer reports from tenant screening are disposed of the same way, and the screening provider must confirm its own disposal practices. (MP-6; Fla. Stat. 501.171(8); 16 CFR 682.3(a))

4.8 Paper files with Restricted information must be kept in locked storage and moved to the headquarters records room within 30 days after closing. (MP-4; PR.AA-06)

4.9 Restricted information must not be entered into any AI tool that is not on the approved-tools list (P10). Approved tools must have contract terms that prohibit training on company data. (SA-9; PR.DS-01)

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), the STD-05 quarterly sample tests of payee changes, and the annual retention review.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may be granted to statements 4.3 to 4.5.

## 7. Related documents
POL-01; POL-02; POL-05; STD-05; STD-08; STD-10; P03 rows G-015, G-016, G-020, G-060, G-063, G-065

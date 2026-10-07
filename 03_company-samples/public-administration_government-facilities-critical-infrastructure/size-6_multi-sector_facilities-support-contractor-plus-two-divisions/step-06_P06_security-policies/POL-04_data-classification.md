# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group CISO, with the Group General Counsel |
| Approved by | Group CISO, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-2, MP-3, MP-4, MP-6, SC-8, SC-28, CM-12, AC-4, AC-21, CP-9, SI-12, SA-9, PL-4 |
| CSF 2.0 | ID.AM-05, ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | N23-R03 (DFARS 252.204-7012(b)(2)(ii)(D)); 32 CFR Part 2002 (CUI); C-GOVERNMENT-R05 (34 CFR 99.33(a)); N56-R01 (16 CFR 682.3); N56-R03 (8 CFR 274a.2(b)(2)); state breach laws and public records laws (Florida worked example: Fla. Stat. 501.171, 119.0701, 119.071(3)(a)) |
| Division supplements | Construction: CUI marking, plan rooms, and enclave. Janitorial and Security: consumer reports, I-9 and E-Verify records, body camera footage. Facilities Support: cardholder and face template data, security layouts |

## 1. Purpose
Make sure every piece of information the group holds is protected according to its sensitivity and the rules of the customer or law that governs it, kept only as long as needed, and disposed of safely.

## 2. Scope
All information the group creates, receives, or holds, in any form (digital or paper), in any location, including information held for customers in the IBOP.

## 3. Classification levels
| Level | Examples | Minimum handling |
|---|---|---|
| **Restricted** | CUI (including DoD controlled drawings); cardholder records, badge photos, and face templates; consumer reports, I-9 and E-Verify records; security system layouts, door schedules, and panel credentials; administrator credentials | Encrypted; access by named role; approved locations only; logged |
| **Confidential** | Federal contract information; customer contracts and building drawings that are not security-related; employee records other than Restricted; bid data | Encrypted in transit; access by role |
| **Internal** | Policies, procedures, internal communications | Company systems only |
| **Public** | Approved public content | None |

## 4. Policy statements
4.1 Information owners must classify information when it is created or received, and Restricted and Confidential documents must be labeled. (RA-2; MP-3; ID.AM-05)

4.2 Restricted information must be encrypted at rest and in transit. (SC-28; SC-8; PR.DS-01; PR.DS-02)

4.3 **CUI** may be stored and processed only in the Construction CUI enclave (SYS-C2) or in agency systems. It must not be placed in commercial SaaS, the IBOP commissioning workspace, email attachments, or AI services, because they do not meet the FedRAMP Moderate equivalent requirement of DFARS 252.204-7012(b)(2)(ii)(D). (CM-12; AC-4; PR.DS-01)

4.4 Paper CUI must be marked and kept in locked plan rooms with a sign-in log and visitor escort. (MP-3; MP-4; PE-3; PR.DS-01)

4.5 Customer information may be used only for the contracted purpose and must not be disclosed to anyone the customer has not authorized. Education records held for a school or university must not be redisclosed (34 CFR 99.33(a)). (AC-21; PR.DS-10)

4.6 Security system information (layouts, door schedules, vulnerabilities) is Restricted. Public records requests for it must be sent to the customer's records custodian; staff must not answer them directly. (AC-21; SI-12; PR.DS-10)

4.7 **Retention and disposal.** Information must be kept no longer than the retention schedule allows: consumer reports for the period set in the schedule and then destroyed (16 CFR 682.3); Form I-9 records for 3 years after hire or 1 year after termination, whichever is later (8 CFR 274a.2(b)(2)); cardholder data deleted at contract end; face templates deleted within 30 days after an enrollee withdraws or leaves. Disposal must make the information unreadable. (MP-6; SI-12; ID.AM-08)

4.8 Backups of Restricted and Confidential information must be immutable, kept with a second cloud provider, and restore-tested every quarter. (CP-9; PR.DS-11)

4.9 Restricted information must not be entered into any AI tool unless the tool is approved under the Group AI Standard for that data. (SA-9; PL-4; GV.SC-05)

4.10 **Biometric data.** Face templates are treated as biometric data. Whether templates computed from camera images are "biometric data" under every state's law is unsettled (in the Florida worked example, Fla. Stat. 501.702 excludes data generated from photographs and video recordings), so counsel confirms per state and the group applies the stricter handling either way: written consent before enrollment, Restricted handling, and the 4.7 deletion rule. (SI-12; PR.DS-01)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (MP-4, MP-6) and data location reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may permit CUI outside the approved locations in 4.3.

## 7. Related documents
POL-01; POL-02; POL-05; `division-supplements.md`; P10 AI governance.

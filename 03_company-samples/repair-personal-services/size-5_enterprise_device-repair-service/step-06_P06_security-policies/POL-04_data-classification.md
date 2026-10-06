# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Privacy Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | RA-2, SC-8, SC-28, SI-12, AC-3, AC-6, MP-6, MP-6(1), MP-7, SA-9 |
| CSF 2.0 | ID.AM-05, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.AA-05 |
| Other requirements | PCI DSS v4.0.1 Requirements 3, 4, and 9.4; Fla. Stat. 501.171(2) and (8); HIPAA 164.310(d) for SL-2; NIST SP 800-88 Rev. 2 |

## 1. Purpose
Classify the information the company handles, including what it can reach on customers' devices, and set how each class is protected, kept, and destroyed.

## 2. Scope
All company data in any form, data on customer and client devices in the company's custody, recovered data, and data sent to vendors and AI tools.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Policy owner; owns classification and the retention schedule |
| Senior Vice President, Store Operations | Customer data access standard at stores |
| Director of Sanitization and Asset Recovery | Sanitization standard and records |
| Director of Data Recovery | Recovered data custody and deletion |
| Vice President, Payments | Payment data handling |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Data must be classified as Restricted (card data, device passcodes, account credentials, customer device content, recovered data, ePHI), Confidential (customer records, client data, employee data), Internal, or Public, and handled by class. (RA-2; ID.AM-05)
4.2 Restricted and Confidential data must be encrypted in transit and at rest with keys managed under STD-04.1. (SC-8; SC-28; PR.DS-01)
4.3 A device passcode may be recorded only in the restricted passcode field, only when a test needs it, and never in notes, on tags, in chat, or on paper. Customer account passwords must not be collected. The field is purged at release. (SI-12; AC-3; PR.DS-01)
4.4 Customer data access standard (STD-04.2): technicians may open customer device content only as the test checklist for the repair requires, with the customer's consent; must not browse, copy, or photograph personal content; and may transfer data only at registered data transfer stations that record the session. (AC-6; MP-7; PR.AA-05)
4.5 Full card numbers must be entered only into P2PE PIN pads, the processor's hosted payment fields, the DTMF masking service, or the processor's virtual terminal, and never written down, typed into notes or chat, or kept in call recordings. (SI-12; PR.DS-01)
4.6 Recovered data must be deleted 30 days after delivery, and data transfer caches must be wiped at the end of each job. (SI-12; MP-6; ID.AM-08)
4.7 Every device leaving company custody for resale, recycling, or return to an SL-2 client without its data must be sanitized under STD-04.3 (NIST SP 800-88 Rev. 2), verified, and recorded with a per-device certificate. No device leaves without a record. (MP-6; MP-6(1); ID.AM-08)
4.8 Records must follow the retention schedule (STD-04.5): tickets 7 years, call recordings 90 days, background check reports 7 years in the HR system only, and security records as in POL-01 4.11. (SI-12; ID.AM-08)
4.9 Restricted data must not be entered into an AI tool unless the AI governance committee has approved the use and the vendor contract forbids training on company data. (SA-9; PR.DS-01)
4.10 ePHI on SL-2 health care client devices must be handled under the client's BAA; those devices must not be opened except to repair or sanitize them as the order requires. (MP-6; AC-6; PR.DS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-04.1 Encryption Standard
- STD-04.2 Customer Data Access Standard
- STD-04.3 Media and Device Sanitization Standard (NIST SP 800-88 Rev. 2)
- STD-04.4 Payment Data Handling Standard
- STD-04.5 Retention Schedule
- PRC-04.1 Data Recovery Case Handling Procedure
- PRC-04.2 PIN Pad Inspection Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, access certifications, the annual Internal Audit assessment (P07), and the annual PCI DSS ROC. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions to this policy follow the process in POL-01 section 7 and `policy-hierarchy.md` section 5: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, limited to 12 months, and recorded in the exception register with compensating controls.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 STPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.

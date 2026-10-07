# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-4, AC-21, CM-12, MP-3, SC-8, SC-12, SC-13, SC-28, CP-6, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11, ID.AM-08 |
| Agency and federal drivers | Pub. 1075 sec. 2.C.5, 2.C.11.2, 3.3.1, Exhibit 7 I(5); CJISSECPOL v6.1 SC-13, SC-28; DFARS 252.204-7012(b); 18 U.S.C. 2721; 42 CFR 431.305-431.306; 45 CFR 164.312(a)(2)(iv), (e) |
| Division supplements | GovTech: FTI tenancy, IEP no-FTI rule, DPPA permitted uses. IT Consulting: CUI only in the enclave. Software: CJI in the RMS and the AI assist |

## 1. Purpose
Classify group information by sensitivity and by whose data it is, and set handling rules so that each agency's and customer's data is used only as its contract and the governing rules allow.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including agency data in group systems and group staff's copies of agency data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns the classes and handling rules |
| System owners | Classify data in their systems; keep the data location register |
| Group cloud platform director | Operates keys, backups, and location guardrails |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Regulated** (FTI, CJI, CUI, motor vehicle personal information, Medicaid and SNAP applicant data, PHI), **Restricted** (other personal information, credentials, and keys), **Confidential**, **Internal**, or **Public**. The regulated type must be recorded, because each type has its own rules. (RA-2; ID.AM-07)

4.2 Regulated and Restricted information must be encrypted at rest and in transit with FIPS 140-3 validated or certified modules where CJISSECPOL or Pub. 1075 requires it, and with group-managed keys. FTI tenants must use customer-managed keys and dedicated database instances. (SC-28; SC-8; SC-13; SC-12; PR.DS-01; PR.DS-02; Pub. 1075 sec. 3.3.1; CJISSECPOL v6.1 SC-13, SC-28)

4.3 **Location.** Regulated information must stay in U.S. regions of FedRAMP authorized services and be supported only from the United States. FTI must not move to a new cloud service, region, or vault until the owning agency's IRS notification covers it. (CM-12; SA-9; Pub. 1075 sec. 3.3.1, sec. 2.E.6, Exhibit 6)

4.4 **Where each type may live.** FTI only in ACMP FTI tenants. **No FTI on the IEP** (Pub. 1075 sec. 2.C.11.2). CUI only in the IT Consulting enclave or government-furnished systems. CJI only in the ACMP CJI cluster and the RMS. Motor vehicle records only in the MVSP. Regulated information must not be placed in tickets, email, chat, or personal storage. (AC-4; AC-21; PR.DS-10)

4.5 **Labeling.** FTI fields, notes, and exports must be labeled as FTI; CUI must carry its marking. (MP-3; Pub. 1075 sec. 2.C.5)

4.6 **Permitted uses.** Motor vehicle personal information may be released only for a permitted use under 18 U.S.C. 2721(b), recorded per request and kept for 5 years. Medicaid and SNAP information may be used only for program administration purposes in the contract (42 CFR 431.302; 7 CFR 272.1(c)). (AC-21; AU-6)

4.7 Backups of Regulated information must be immutable, held with a different provider or account from production, and restore-tested at least quarterly for High-criticality systems, including a full-scale test at least once a year. (CP-9; CP-6; PR.DS-11)

4.8 Regulated information must be purged at contract end with a certificate, including backups as they expire. (MP-6; SI-12; ID.AM-08; Pub. 1075 Exhibit 7 I(5))

4.9 Regulated information must not be entered into any AI service unless the service is approved under the Group AI Standard for that data type, the governing agency or customer has been told in writing, and contract terms prohibit training on the data and limit retention. CJI requires a CJIS review of the service first. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the P07 assessment (AC-3, AC-4, SC-13, SC-28, CP-9) and data location reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may permit FTI on the IEP or CUI outside approved systems.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP; P10 Group AI Standard.

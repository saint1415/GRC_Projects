# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group CISO, with the Group General Counsel for legal categories |
| Approved by | Group CISO and Group General Counsel, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-2, MP-3, MP-6, SC-8, SC-28, CM-12, SI-12, AC-21 |
| CSF 2.0 | ID.AM-05, PR.DS-01, PR.DS-02, PR.DS-10 |
| Regulatory drivers | N48-49-R01 (101.630(b); 101.650(c)(2)); 49 CFR part 1520 (SSI); 33 CFR 105.225(c); N42-R04 (52.204-21(b)(1)(vii)); N42-R03 (252.204-7012(b)); state breach laws; 46 U.S.C. 41106(2) |

## 1. Purpose
Tell everyone how to recognize the group's sensitive information, who owns it, and how to protect it in use, in transit, at rest and at disposal.

## 2. Scope
All information created, received or held by any division or by corporate shared services, in any form, including OT configuration data and printed lists at the terminals.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Data owners | Classify their data and approve access and sharing |
| Division CySO and FSOs | Identify and protect SSI |
| Freight Trading federal contracts compliance manager | Identify FCI and CUI and keep them inside approved scopes |
| Group General Counsel | Affiliate data-sharing standard; contract confidentiality terms |
| All workforce | Label and handle data according to this policy |

## 4. Classification levels
| Level | Examples | Minimum handling |
|---|---|---|
| **Restricted: regulated** | Sensitive security information (Cybersecurity Plans, FSPs, FSAs, network maps of terminals, PACS reader records); CUI; FCI; personal information covered by state breach laws (driver license numbers, employee and guarantor records) | Need to know only; SSI library or approved scope; encrypted at rest and in transit; marked; no personal email or unapproved AI tools |
| **Restricted: commercial** | Customers' cargo, booking and appointment data; terminal services agreement terms; counterparties' contract terms; trading positions; tenant leases | Need to know; never shared with another division without approval under the affiliate data-sharing standard |
| Internal | Procedures, internal reports, non-sensitive operational data | Group systems only |
| Public | Published vessel schedules, marketing | Approved before release |

## 5. Policy statements
5.1 Every data owner must classify the data in their systems and record it in the group data inventory, including where copies are kept. (RA-2; CM-12; ID.AM-05)

5.2 **SSI** must be marked, stored only in the SSI library or approved systems, shared only with persons with a need to know, and protected under 49 CFR part 1520. The Cybersecurity Plan is SSI (101.630(b)); PACS reader records are SSI (33 CFR 105.225(c)). (MP-3; AC-3; PR.DS-01)

5.3 **Customer data is not shared across divisions.** Terminal customer cargo, vessel and appointment data may not be made available to Freight Trading or Port Real Estate, except a division's own shipments as a cargo owner, unless the Group General Counsel approves under the affiliate data-sharing standard. (AC-21; 46 U.S.C. 41106(2))

5.4 **FCI and CUI.** FCI may be stored only in systems inside the CMMC Level 1 scope. CUI may be accepted only into an environment approved under POL-01 4.10. CUI received anywhere else must be reported to the federal contracts compliance manager the same day and quarantined. (AC-3; MP-2; 252.204-7012(b))

5.5 Restricted data must be encrypted in transit over external networks and at rest. Partner exchanges must use the integration hub with AS2, SFTP or TLS; plain FTP is prohibited after 2026-12-31. OT traffic that cannot be encrypted must stay inside an OT zone, and the compensating control must be documented. (SC-8; SC-28; PR.DS-01; PR.DS-02; 101.650(c)(2))

5.6 Printed release lists and dangerous cargo lists must be controlled and shredded at shift end. (MP-2)

5.7 Media containing Restricted data, including scale PCs, HMIs and gate devices, must be sanitized or destroyed through the group disposal service with a certificate before reuse or disposal. (MP-6; 52.204-21(b)(1)(vii))

5.8 Data must be kept for the periods in the group retention schedule and then disposed of. (SI-12)

## 6. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through data loss prevention reports, the SSI library access review, the CMMC Level 1 self-assessment and the P07 assessment.

## 7. Exceptions and related documents
Exceptions follow POL-01 section 4.12. Related: POL-01, POL-02, POL-05; affiliate data-sharing standard; group retention schedule; 49 CFR part 1520.

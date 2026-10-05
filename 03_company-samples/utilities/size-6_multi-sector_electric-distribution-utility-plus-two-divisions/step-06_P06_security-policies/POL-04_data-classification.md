# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer, with the Group CISO |
| Approved by | Group CISO and Group General Counsel, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, AC-3, AC-4, AC-21, MP-3, MP-4, MP-6, SC-8, SC-28, SI-12 |
| CSF 2.0 | ID.AM-07, PR.DS-01, PR.DS-02, PR.DS-10 |
| Regulatory links | NERC CIP-011-3 R1 and R2 and CIP-004-7 R6 (BCSI); 18 CFR 388.113 (CEII); client CIP-011-3 terms; FAR 52.204-21(b)(1)(vii); state breach laws (Fla. Stat. 501.171 worked example) |

## 1. Purpose
Classify group and client information so that each kind gets the protection its owners, regulators, and clients require.

## 2. Scope
All information created, received, or held by the group, in any form, including information held for clients and information held by vendors and affiliates for a division.

## 3. Classification levels
| Level | Examples | Core handling |
|---|---|---|
| **Restricted** | BES Cyber System Information; the Electric Utility's CEII; client CEII and BCSI; grid and field network diagrams; security configurations; Social Security numbers and bank account numbers | Designated storage locations only; authorized access lists; encrypted at rest and in transit; never in personal storage or unapproved tools |
| **Confidential** | Customer and royalty owner personal information; employee data; Federal Contract Information; client project data; outage and restoration records | Need-to-know access; encrypted at rest and in transit |
| **Internal** | Policies, procedures, internal communications | Workforce only |
| **Public** | Published outage counts, rate filings, press releases | Approved for release |

## 4. Policy statements
4.1 Every data set and repository must have an owner and a classification. When data of different levels are mixed, the highest level applies. (RA-2; ID.AM-07)

4.2 Restricted and Confidential data must be encrypted in transit and at rest, and access must follow POL-02 4.2. (SC-8; SC-28; PR.DS-01; PR.DS-02)

4.3 **BES Cyber System Information.** The Electric Utility must keep a list of designated BCSI storage locations, **including locations at vendors and affiliates**, with an authorized access list for each, verified at least every 15 calendar months. BCSI found anywhere else must be moved or the location designated within 30 days. (AC-3; CIP-011-3 R1; CIP-004-7 R6)

4.4 **Client CEII and BCSI.** Engineering Services must keep each client's CEII and BCSI only in restricted project folders whose access list the client has approved. CEII obtained from FERC on a client's behalf requires the client's written authorization (18 CFR 388.113(g)(1)). (AC-3; AC-6; PR.DS-01)

4.5 **Federal Contract Information** must be handled under the FAR 52.204-21 controls and kept in approved repositories. (AC-3; PR.DS-01)

4.6 **Minimize personal information.** Social Security numbers collected for credit decisions must not be kept after the decision unless law requires it. Royalty owner exports must use secure file transfer. (SI-12; PR.DS-01)

4.7 **No Restricted or client data in unapproved services.** Restricted data and client data must not be placed in personal cloud storage, personal email, or any external service, including AI tools, that is not approved for that data. (AC-4; AC-21; SA-9)

4.8 **Disposal.** Media holding Restricted or Confidential data must be sanitized or destroyed through the group service with a certificate; for BCSI, before reuse or disposal of the Cyber Asset. (MP-6; CIP-011-3 R2)

4.9 **Labeling.** Restricted documents must carry a label (for BCSI and CEII, the label the owner's program requires). (MP-3)

4.10 **Retention.** Records are kept under the group retention schedule and POL-01 4.11. (SI-12)

## 5. Compliance and enforcement
Checked through repository permission reviews, data loss prevention alerts, the BCSI location review, and P07.

## 6. Exceptions
None for 4.3 and 4.4. Others follow POL-01 section 4.10.

## 7. Related documents
POL-02; POL-05; the Electric Utility CIP-011-3 information protection program; client contract register (Engineering Services).

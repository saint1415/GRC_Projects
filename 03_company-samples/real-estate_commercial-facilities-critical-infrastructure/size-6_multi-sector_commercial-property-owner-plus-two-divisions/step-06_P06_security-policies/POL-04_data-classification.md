# Data Classification and Handling Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-04 |
| Owner | Group Chief Privacy Officer |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | RA-2, PT-2, PT-3, AC-4, AC-20, SC-8, SC-28, CP-9, MP-6, SI-12, SA-9 |
| CSF 2.0 | ID.AM-07, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| Regulatory drivers | CISA CPG 2.0 goals 3.K, 3.O (voluntary, adopted); PCI DSS v4.0.1 Req. 3 and 9.4; DFARS 252.204-7021(d)(2); state reasonable-security and disposal laws (Fla. Stat. 501.171(2), (8) worked example); Fla. Stat. 509.101(2) |
| Division supplements | Commercial Property: badge, visitor, video, and biometric data. Construction: FCI and CUI handling, BTI intake check. Hotels: card data, guest IDs, the guest register |

## 1. Purpose
Classify group information by sensitivity and set handling rules, so that card data, CUI, biometric data, and the programs and credentials that run buildings are protected and kept only as long as needed.

## 2. Scope
All information the group creates, receives, maintains, or transmits, in any form, including building system programs, site configurations, drawings, and video.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group Chief Privacy Officer | Owns the classes, the retention schedule, and biometric rules |
| Data owners | Classify information and approve access and uses |
| Group building technology director | Protects BAACS programs and configurations |
| Construction director of federal contracts compliance | Owns FCI and CUI handling rules |
| All workforce | Handle information according to its class |

## 4. Policy statements
4.1 Information must be classified as **Restricted** (card data, CUI, biometric data including face templates, government ID numbers, bank account data, passwords and keys, and OT site configurations that contain credentials), **Confidential** (badge holder records, video, guest and tenant personal information, building drawings, FCI, controller programs), **Internal**, or **Public**. (RA-2; ID.AM-07)

4.2 Restricted and Confidential information must be encrypted in transit and at rest with approved algorithms and group-managed or provider-managed keys approved by the Group CISO. (SC-8; SC-28; PR.DS-01; PR.DS-02)

4.3 **Federal information.** CUI may be processed, stored, or transmitted only in the CUI enclave (SYS-D4). FCI may be held only in systems inside the Construction CMMC Level 1 scope. Any team that receives drawings or specifications for a federal facility (including the BTI unit) must check for CUI markings before saving them anywhere else. (AC-4; AC-20; PR.DS-10)

4.4 **Card data** may exist only in PCI DSS-scoped systems and the P2PE terminals. It must never be sent or accepted by email or chat, and paper with card data must be destroyed after authorization. Card security codes must never be written down. (SI-12; MP-6; PR.DS-01)

4.5 **Building system programs and configurations** must be backed up to the group immutable vault after every change, and the group, not a supplier or another division, must hold the authoritative copy. (CP-9; PR.DS-11)

4.6 **Retention.** Video: 30 days unless held for an incident or legal hold. Analytics alert clips: 30 days. Badge transaction history: 2 years after badge deactivation. Visitor ID scans: 30 days. Guest ID scans: 30 days after checkout. Guest register: at least 2 years (Florida worked example, Fla. Stat. 509.101(2)). Records past retention must be disposed of so they cannot be read. (SI-12; ID.AM-08)

4.7 **Biometric data** may be collected only for an approved use case (POL-01 4.13), with written notice and opt-in consent, a non-biometric alternative, and no use for supplier model training. It must be deleted within 30 days after enrollment ends or the use case is retired. (PT-2; PT-3)

4.8 Media holding Restricted or Confidential information must be sanitized or destroyed with a certificate, including drives in decommissioned recorders and site supervisors. (MP-6; ID.AM-08)

4.9 Restricted or Confidential information must not be entered into any AI tool unless the tool is approved under the Group AI Standard with terms that prohibit training on group data. FCI and CUI must not be entered into any AI tool outside the matching CMMC scope. (SA-9; PL-4)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (CP-9, SI-12, AC-20), data discovery scans (card data and CUI markings), and retention reports.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may allow CUI outside the enclave or card data in email.

## 7. Related documents
POL-01; POL-02; `division-supplements.md`; P02 SSP for the BAACS; P10 Group AI Standard.

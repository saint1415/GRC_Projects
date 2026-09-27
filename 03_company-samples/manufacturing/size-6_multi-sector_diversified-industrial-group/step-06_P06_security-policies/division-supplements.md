# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-15 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, HSM-only signing, information barrier, third-party terms | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, OT network standard, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (FDA decision points, FCI enclave, client notices) | Division president, after Group CISO alignment review |
| Division procedures | SPDF, PSIRT, complaint handling, recall and hold, laboratory intake | Division security and compliance lead, or the QMS owner for FDA procedures |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Medical Devices | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; update for the final 2026 policies due by 2026-12-30 (90 days after effective date) | Confirm alignment; add the IX-3 signing exception with its end date |
| Distribution | v2025 | 2025-05 | **Not aligned** to 2026 policies (P01 GR-20, DS-007): no FCI enclave rule, no handheld account rule, no contracting officer notice path | Re-issue by 2026-12-31 |
| Engineering and Product Testing Services | v2025 | 2025-11 | Aligned in text, but its barrier rules are not enforced (gap 5) and it has no AI tool rule (gap 8) | Add enforcement and AI rules by 2026-11-30 |

## 3. What each supplement adds
### 3.1 Medical Devices supplement (device manufacturer; DCC business associate)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| SPDF | Threat model, security requirements, security testing, and SBOM for every release of every product and related system | POL-01 4.7 | 524B(b)(2)-(3); 21 CFR 820.10(c) |
| Signing custody | Two custodians per ceremony; key ceremonies recorded; **exception:** IX-3 software key at Plant D until 2027-03-31 (POAM-003) | POL-02 4.8; POL-04 4.2 | 524B(b)(2) |
| Patch cycles | Quarterly security maintenance releases for IX-4 and PM-7; semiannual for US-2; out-of-cycle procedure for critical vulnerabilities | POL-01 4.7 | 524B(b)(2)(A)-(B) |
| Legacy products | Every marketed product, including IX-3, stays in PSIRT monitoring until its end-of-support date; end-of-support dates published in labeling | POL-01 4.8 | FDA postmarket guidance (2016) |
| PSIRT and FDA decisions | Each product incident gets a complaint record, an MDR decision, a controlled or uncontrolled risk decision, and an 806 decision in the eQMS | POL-03 4.4 | 21 CFR 820.35(a); 803.50; 806.10 |
| DCC breach decisions | 164.402 assessment for every product incident that may touch DCC PHI; BAA terms register | POL-03 4.5 | 164.410; 164.314(a)(2)(i) |
| Plant OT | Production zones separate MES and test stations from office networks; individual operator sign-in; MES logs to the SIEM | POL-02 4.1; POL-01 4.6 | 524B(b)(2); 21 CFR 820.35 |
| Hospital administrators | MFA required for DCC accounts that can change device settings or drug libraries by 2027-03-31 | POL-02 4.11 | 164.312(d) |
| Intercompany testing | Premarket and fix-verification tests by Testing require a signed independence statement | POL-01 4.10 | FDA premarket guidance (testing) |

### 3.2 Distribution supplement (distributor and importer; federal contractor)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| FCI enclave | Federal contract information only in the ERP federal module and the labeled FCI library | POL-04 4.5 | 52.204-21(b)(1)(i)-(ii) |
| CMMC Level 1 | Annual self-assessment against the 15 requirements; SPRS entry and affirmation by a named senior official | POL-01 4.1 | 32 CFR 170.15 |
| Subcontract flowdown | FAR 52.204-21 substance in every subcontract that may hold FCI | POL-01 4.9 | 52.204-21(c) |
| Warehouse handhelds | Badge sign-in; no site accounts | POL-02 4.1 | 52.204-21(b)(1)(v) |
| Visitors | Electronic visitor records at every distribution center | POL-02 4.12 | 52.204-21(b)(1)(ix) |
| Covered telecommunications | Equipment inventory by brand; report within 1 business day of identification | POL-03 4.3, 4.6 | 52.204-25(d) |
| Device complaints | Cybersecurity prompts at intake; forward to manufacturers the same day; importer reports within 30 calendar days | POL-03 4.4 | 803.18(d); 803.40 |
| Holds and recalls | Electronic hold from the Medical Devices eQMS applied within 4 hours | POL-03 4.4 | Manufacturers' corrections (21 CFR 806) |
| Relabeling gate | No repackaging or relabeling without regulatory approval | POL-01 4.1 | 803.3; 807.20(a)(3) |

### 3.3 Engineering and Product Testing Services supplement (independent laboratory)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Information barrier | Barrier groups enforced in SYS-G1; no shared collaboration spaces with other divisions; quarterly attestations | POL-02 4.3 | Client NDAs; accreditation |
| Findings vault | Unpublished findings only in the vault, encrypted per client; data loss prevention rules | POL-04 4.3, 4.6 | Client NDAs |
| Intake | PHI and export-control scanning of every submission before release to engineers | POL-04 4.4 | Contract PHI prohibition; EAR |
| Client notices | Notify affected clients as each NDA requires; terms kept in the notification matrix | POL-03 4.6 | Client NDAs |
| AI tools | AI drafting tools only for clients who agreed in writing | POL-04 4.10 | Client NDAs |
| Independence | Signed independence statement for every Medical Devices engagement | POL-01 4.10 | Accreditation; FDA premarket guidance (testing) |
| Acquired laboratories | Federate to SYS-G1 by 2027-03-31 | POL-01 4.6 | CSF 2.0 PR.AA-01 |

## 4. Distribution drift: conflicts with 2026 group policy
The 2025 Distribution supplement was written before the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 DS-007; P07 CA-2 finding).

| Topic | Distribution supplement (2025) | Group policy (2026) | Effect |
|---|---|---|---|
| Federal contract information | Not addressed | FCI enclave (POL-04 4.5) | FCI in email and file shares (DS-005) |
| Handheld accounts | Site accounts allowed | No shared accounts (POL-02 4.1) | Actions not attributable (DS-015) |
| Visitor records | Paper logs at site discretion | Visitor system at every site (POL-02 4.12) | Incomplete logs (DS-013) |
| Incident severity | Distribution 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation |
| Common control inheritance | Not addressed | Division documents inheritance (POL-01 4.6) | Gap 3 (POAM-013) |
| Contracting officer notices | Not addressed | Notification matrix includes federal contract terms (POL-03 4.6) | Missed 1-business-day clock risk (DS-009) |

**Why the drift happened.** Distribution's security lead role was vacant for 7 months in 2025-2026, and the supplement had no backup owner. **Fix:** the Group CISO's policy office now tracks supplement versions and owners in the policy register and escalates any supplement more than 90 days behind a group change.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Medical Devices, Testing) and on re-issue (Distribution).

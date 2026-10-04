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
| Group policy (POL-01 to POL-05) | MFA for all CUI access, U.S.-person gating, one severity scale, no flowdown no CUI, intercompany services treated as external | Board audit and risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, CUI location register, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Contract-, regulator-, and system-specific standards (for example, plant USB transfer, cleared-center rules, DoD edition data use) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Aircraft Parts | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after effective date) | Confirm alignment |
| Engineering Services | v2024 | 2024-05 | **Drifted** (scenario gap 9); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-020) |
| Defense Software | v2025 | 2025-10 | Aligned, but missing a data-use gate for Government-related data and a CSP reporting procedure for SYS-D4 tenants | Add both by 2026-11-30 (POAM-016, POAM-012) |

## 3. What each supplement adds
### 3.1 Aircraft Parts supplement (prime contractor and subcontractor; 9 plants)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Specialized Assets | Every CNC, additive, and CMM machine inventoried with its category; unsupported controllers isolated on machine VLANs; enduring exceptions recorded in the plant SSP annex | POL-01 4.6 | 32 CFR 170.19(c)(1); 252.204-7012(b)(3) |
| USB transfer | Device control with registered encrypted drives at every transfer workstation; drives issued per cell; DNC serial gateways replace USB loading by 2027-12-31 | POL-04 4.6 | 3.8.7; 3.8.8 |
| Release integrity | Checksum verification at DNC; revision reconciliation against PLM after any restore before release | POL-03 4.12 | Flight safety (AS9100 quality system) |
| Shop-floor accounts | MES sign-in through SYS-G1 where supported; local accounts disabled after 45 days of inactivity | POL-02 4.6 | 3.5.6 |
| Printed drawings | Covered during visits; locked shred bins at every cell | POL-04 4.7 | 3.8.1; 22 CFR 120.56 |
| Visitors | Electronic visitor system and escort at every plant; foreign-national visits pre-cleared by the Empowered Official | POL-05 4.6 | 3.10.3; 3.10.4; 22 CFR 120.56 |
| Sister-division services | Aircraft Parts CUI never sent to SYS-D4 until it is listed in the CUI location register | POL-01 4.9; POL-04 4.3 | 252.204-7012(b)(2)(ii)(D) |
| Program H | Access only by named staff; Program H release queue only to Program H cells; Level 3 controls as they are built | POL-02 4.3 | 32 CFR 170.19(e) |

### 3.2 Engineering Services supplement (prime contractor and subcontractor; cleared at 2 centers)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Customer sites and GFE | Site agreement states where CUI lives; GFE register per site; no sync of customer CUI to company laptops; customer-provided media only on customer systems | POL-02 4.10; POL-05 4.5 | 3.1.20; 3.1.21; 3.10.6 |
| Test data | Encrypted drives only for range data; network transfer where the range allows | POL-04 4.6 | 3.8.6 |
| HPC and test systems | Group baseline on HPC nodes; SSP annex and inheritance matrix; interconnection agreement for the GCEE link | POL-01 4.6 | 3.4.2; 3.12.4 |
| Cleared centers | FSO spillage procedure; FBI and DCSA reporting; FSO referrals to the identity team within 1 hour when access must change | POL-03 4.8, 4.11 | 32 CFR 117.7, 117.8 |
| Allied partners | Shares tagged with the technical assistance agreement that allows them | POL-02 4.2 | 22 CFR 120.56 |
| DoD reporting | At least 2 certificate holders at 2 different centers | POL-03 4.4 | 252.204-7012(c)(3) |

### 3.3 Defense Software supplement (DoD cloud service; CSP to contractors; SOC 2 service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Government-related data | Data-use gate in every release: no use of DoD edition data outside managing that environment without written Contracting Officer approval | POL-04 4.5 | 252.239-7010(c)(2) |
| DoD edition reporting | DIBNet reports for incidents related to the cloud service; 2 certificate holders; spillage procedure agreed with each Contracting Officer | POL-03 4.4, 4.11 | 252.239-7010(d), (k) |
| CSP duties to tenants | Written status of FedRAMP Moderate equivalency given to every CUI tenant; tenant incident support for their DoD reports | POL-01 4.9; POL-03 4.5 | 252.204-7012(b)(2)(ii)(D) |
| Security claims | Legal review of every security or compliance claim in marketing and proposals | POL-01 4.1 | FTC Act Sec. 5 |
| Support access | Ticket-linked PAM approval for every tenant access | POL-02 4.8 | SOC 2 CC6.1; 252.239-7010(c)(1) |
| Developer tools | Approved coding assistant inside the government-community boundary only; public assistants blocked on developer laptops | POL-05 4.7, 4.8 | 22 CFR 120.56 (export-controlled source code) |

## 4. Engineering Services drift: conflicts with 2026 group policy
The 2024 Engineering Services standards were written before the 2026 group policies and before the HPC cluster joined the CUI environment. Where they conflict, **group policy governs now** (POL-01 4.5), but field engineers follow the document they know, so the conflicts are real risks (P01 ES-010; P07 PL-01c.01[02]).

| Topic | Engineering Services standard (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| Removable media at customer sites | Company drives allowed on customer systems at customer request | Customer-provided media only on external systems (POL-02 4.10; POL-04 4.6) | 3.1.21 not met (POAM-010) |
| Cloud sync | Personal cloud sync allowed for non-CUI files | No sync clients for any CUI folder; personal cloud blocked on CUI endpoints (POL-02 4.10) | CUI synced to laptops at customer sites (ES-002) |
| Test data media | Encryption "recommended" | Encryption required (POL-04 4.6) | 3.8.6 not met |
| AI tools | Not addressed | Approved tools only; never CUI in public AI (POL-05 4.7, 4.8) | Public chatbot use in 2026-07 (ES-006) |
| New systems | Division IT may connect systems to the GCEE | SSP annex and interconnection agreement first (POL-01 4.6) | HPC cluster joined without either (scenario gap 6) |
| Incident reporting | Report to the customer only for incidents on customer systems | Report to the group SOC within 1 hour as well (POL-03 4.1) | ES-015 |

**Why the drift happened.** The 2024 re-organization moved Engineering Services security under the Group CISO, but the supplement had no owner or review date, and the 2025 review was skipped. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Aircraft Parts, Defense Software) and on re-issue (Engineering Services).

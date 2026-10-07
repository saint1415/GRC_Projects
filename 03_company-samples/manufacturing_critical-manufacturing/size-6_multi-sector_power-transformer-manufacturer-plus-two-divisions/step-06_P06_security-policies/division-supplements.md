# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-15 (group policies v2026.1 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, the customer security terms register, no always-on OEM connections | Board risk committee or Group CISO |
| Group standards | Group OT security standard (SP 800-82 Rev. 3 based), logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Plant, product, CIP, and client-specific requirements | Division president, after Group CISO alignment review |
| Electric Utility CIP program documents | CIP-003-9 policies, CIP-004-7 to CIP-013-2 plans and procedures | CIP Senior Manager. Where a CIP document is stricter for a BES Cyber System, it governs (POL-01 section 2) |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Transformer Manufacturing | v2026 (2026-05) | 2026-05-20 (to group policy v2026) | Aligned, but did not cover the acquired plant P8 or AI use cases (P03 G-064). Sections marked **new** below were added in this revision | Formal re-issue with the new sections by 2026-12-31 |
| Electric Utility | v2026 (2026-02) | 2026-02-27 | Aligned. Maps each group policy to the CIP program document that implements it | Add cross-division incident criteria to the CIP-008-6 plan by 2026-12-15 (POAM-026) |
| Grid Engineering | 2023 division standards (no supplement) | 2023-04 | **Drifted** (scenario gap 6); conflicts listed in section 4 | Replace the 2023 standards with section 3.3 by 2026-12-31 (POAM-014) |

## 3. What each supplement adds
### 3.1 Transformer Manufacturing supplement (focus division)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Plant network zoning | Every plant has an OT DMZ between office and control networks. No device may be dual-homed across them. MES servers and historian replicas sit in the OT DMZ | POL-01 4.13; POL-02 4.11 | CSF PR.IR-01; SP 800-82 Rev. 3 sec. 5.2.3 |
| OEM remote access | OEM access only through the central gateway, per session, approved by the plant shift supervisor, recorded. Always-on cellular routers removed | POL-02 4.10 | CSF PR.AA-03; SP 800-82 Rev. 3 sec. 6.2.1 |
| **New: P8 integration** | Until P8 meets the zoning and access rules: the P8 MES link to the GEPS hub sits behind an isolation switch the SOC can operate (by 2026-11-30); cellular routers disconnected (2026-11-30); legacy domain trust removed (2026-12-31); OT DMZ (2027-03-31); 19 unsupported HMIs isolated or replaced (2027-06-30) | POL-01 4.14 | POAM-006, POAM-007, POAM-008, POAM-020 |
| Controller and MES backups | Controller programs backed up after every change and at least weekly; MES databases nightly; copies in the group vault; one restore test per plant each quarter | POL-04 4.8 | CSF PR.DS-11; SP 800-82 Rev. 3 sec. 6.2.4 |
| Safe state and restart | Each plant keeps manual shutdown procedures for drying ovens, vacuum oil processing, and test labs, and a paper traveler procedure for 48 hours of production (P8 by 2027-03-31) | POL-03 4.8 | CSF RC.RP-01 |
| Firmware signing | TMU firmware signed in a hardware security module under split control (two of three named signers); build servers isolated from the corporate network | POL-04 4.7 | Utility addendum sec. 5; POAM-010 |
| Vulnerability disclosure | Advisory to affected utilities within 20 days of confirming a vulnerability in supplied firmware or software (the addenda allow 30) | POL-03 4.4 | Utility addendum sec. 4; POAM-011 |
| SBOMs | An SBOM for every firmware line and release | POL-04 4.7 | CSF PR.PS-06; POAM-018 |
| Utility notices | PSIRT sends addendum incident notices within 24 or 48 hours of confirmation as the register shows; field service sends access-revocation notices within 1 business day from the HR event | POL-03 4.4; POL-02 4.5 | Utility addendum secs. 1 and 3 |
| FMS | No inbound connection to any utility network or TMU; tenant isolation tested every release | POL-02 4.12 | Utility addendum sec. 6 |
| **New: AI use cases** | Demand forecast and predictive maintenance models (AI-001, AI-002) under model change control; a written storm-reserve allocation rule that the forecast cannot override; no plant historian connector to the internet except through the OT DMZ replica | POL-01 4.12 | Group AI Standard (P10); POAM-019, POAM-021 |
| Federal contracts and exports | FCI folders restricted to contract teams; covered equipment check before any new device joins a plant network; export screening manual fallback drilled every year | POL-04 4.5, 4.6; POL-01 4.14 | FAR 52.204-21, 52.204-25; 15 CFR 762.6 |

### 3.2 Electric Utility supplement (NERC-registered DP, TO, TOP)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CIP precedence | CIP-003-9 policies approved by the CIP Senior Manager govern BES Cyber Systems, their EACMS and PACS, and BCSI | POL-01 2, 4.2 | CIP-003-9 R1, R3 |
| Group services | SYS-G1 identities are not used inside ESPs; group SOC sensors at the TCC are monitored as EACMS-adjacent and their alerts feed CIP-008-6 | POL-02 4.11 | CIP-005-7 R1; CIP-008-6 R1 |
| Affiliates as vendors | Transformer Manufacturing and Grid Engineering are vendors under the CIP-013-2 plan: same risk assessment, contract terms, and PRA attestation as third parties | POL-01 4.8 | CIP-013-2 R1, R2; CIP-004-7 R3; POAM-009, POAM-017 |
| BCSI | TCC BCSI only in the utility BCSI repository; affiliate access only through CIP-004-7 R6 | POL-04 4.3 | CIP-011-3 R1; CIP-004-7 R6; POAM-024 |
| Low impact vendor access | Detection of known or suspected malicious communications on every vendor electronic remote access path to the 58 transmission substations | POL-02 4.10 | CIP-003-9 Att. 1 Sec. 6.3; POAM-015 |
| Data links | CIP-012-2 plan covers confidentiality, integrity, availability, and recovery of real-time data links | POL-04 4.2 | CIP-012-2 R1 Parts 1.1 to 1.3; POAM-016 |
| Reporting desk | CIP-008-6 R4, EOP-004-4, and DOE-417 reports made by the desk within their deadlines; DCC procedures include the DOE-417 cyber criteria | POL-03 4.5 | CIP-008-6 R4; EOP-004-4 R2; Form DOE-417; POAM-026 |
| Outside CIP scope | DCC, ADMS, AMI, CIS, and distribution substations follow group policy and the group OT standard | POL-01 4.1 | CSF 2.0 with SP 800-82 Rev. 3 |

### 3.3 Grid Engineering supplement (replaces the 2023 standards; effective on re-issue)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Client terms register | Every client security term (CIP-004-7 training and PRA, CIP-011-3 handling, CIP-013-2 notices, Transient Cyber Asset rules) recorded with deadline and contact | POL-01 4.8 | Client contracts; POAM-012 |
| Client notices | Contracts director sends incident notices within each client's deadline (24 to 72 hours) after the SOC handoff in POL-03 4.4 | POL-03 4.4 | Client CIP-013-2 R1 Part 1.2.1 terms |
| BCSI and CEII | Restricted folders per client, membership approved by the client; personal cloud storage blocked; return or destroy at project close | POL-04 4.3, 4.4, 4.10 | Client CIP-011-3 terms; 18 CFR 388.113; POAM-013 |
| Commissioning laptops | One hardened image at all 40 offices; patch exceptions closed within 35 days; a pre-connection record for each client | POL-05 4.7, 4.9 | CIP-010-4 R4 Att. 1 Sec. 2; CIP-003-9 Att. 1 Sec. 5.2 (client terms); POAM-025 |
| Settings integrity | Every released protection settings file carries a SHA-256 hash checked at deployment | POL-04 4.7 | Client CIP-013-2 R1 Part 1.2.5 terms |
| Logging | Project platform logs kept 1 year in the group archive | POL-01 4.11 | SOC 2 CC7.2 commitment; POAM-022 |
| Inheritance | Inheritance matrix from the group common control catalog, confirmed every year | POL-01 4.6 | SOC 2 CC2.3; POAM-014 |

## 4. Grid Engineering drift: conflicts with 2026 group policy
The 2023 Grid Engineering standards were written before the division moved onto group services. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 ES-007, GR-10; P07 PL-1 findings).

| Topic | Grid Engineering standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Log retention | 90 days on the project platform | 1 year (logging standard) | SOC 2 deviation; short incident scoping window (POAM-022) |
| Removable media | Personal USB drives allowed on commissioning laptops if scanned | Company-issued, kiosk-scanned media only (POL-05 4.7) | Malware path into client substations (ES-003) |
| Field tool passwords | Shared accounts on settings tools allowed | Unique identities (POL-02 4.1) | No accountability for settings changes (ES-010) |
| Incident severity | Division 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation (P07 IR-4 finding) |
| Client notices | Project manager discretion | Register and SOC handoff (POL-03 4.4) | Missed contract deadlines (ES-002) |
| Common control inheritance | Not addressed | Documented and confirmed every year (POL-01 4.6) | Gap 6 (POAM-014) |

**Why the drift happened.** Grid Engineering joined group identity and the group SOC in 2024, but its standards had no owner after the 2024 reorganization and were never compared with group policy. **Fix:** POL-01 4.5 requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office now tracks every supplement version in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations under v2026.1 are due 2026-12-31 for all three divisions. The Electric Utility's statement is co-signed by the CIP Senior Manager.

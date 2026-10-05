# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-15 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy, supplements, and regulator documents fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all remote OT access, one severity scale, affiliates treated as vendors, no Restricted data in unapproved tools | Board risk committee or Group CISO |
| Group standards | OT security standard (SP 800-82 Rev. 3 based), logging standard, cloud guardrails, OT security contract schedule, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (CIP program procedures, field SCADA rules, client contract rules) | Division president, after Group CISO alignment review |
| **Regulator-required documents** | The Electric Utility's CIP-003-9 R1 cyber security policies (medium and low impact), low impact cyber security plan, CIP-008-6 and CIP-009-6 plans, CIP-013-2 supply chain plan, EOP-004-4 Operating Plan | **CIP Senior Manager** (CIP documents); Electric Utility system operations director (EOP-004) |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

**Why the CIP documents sit beside, not under, group policy.** CIP-003-9 R1 requires policies approved by the CIP Senior Manager at least once every 15 calendar months. Group policy cannot be the evidence for that approval, and group policy changes cannot silently change a CIP document. The Electric Utility supplement therefore maps each group policy to the CIP document that carries it, and every group policy change triggers a CIP document review (section 3.1).

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Electric Utility | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Confirm alignment; review CIP documents for the POL-02 4.4 and 4.5 changes |
| Gas Production | v2023 | 2023-05 | **Drifted** (scenario gap 6); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-016) |
| Engineering Services | v2025 | 2025-10 | Aligned to the 2025 policies, but missing the client notice register, client CEII and BCSI folder rules, and AI rules required by POL-03 4.5, POL-04 4.4, and POL-05 4.5 | Add them by 2026-12-31 (POAM-020, POAM-021, POAM-022) |

## 3. What each supplement adds
### 3.1 Electric Utility supplement (NERC DP, TO, TOP; state-regulated utility)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CIP document map | Each group policy is mapped to the CIP document that carries it; any group policy change triggers review of the mapped CIP documents within 30 days | POL-01 4.1, 4.5 | CIP-003-9 R1 |
| TCC access | CIP-004-7 access program: training before access, personnel risk assessments, quarterly authorization verification, 15-month privilege review, BCSI access through designated locations only | POL-02 4.2, 4.6, 4.7 | CIP-004-7 R2 to R6 |
| DOP operator roles | Area-of-responsibility roles; switching orders prepared and approved by different people; tag changes logged | POL-02 4.11 | Voluntary benchmark |
| DOP remote access | Every SYS-G4 session approved by the DCC shift supervisor with a work order; no standing access after 2027-03-31 | POL-02 4.4 | CIP-003-9 Att. 1 Sec. 6 (substations); benchmark (DOP) |
| Substation gateways | DOP traffic into low impact substations limited to DNP3 from the FEPs; gateway rule check in every substation change | POL-02 4.2 | CIP-003-9 Att. 1 Sec. 3.1 |
| Transient Cyber Assets | Pre-connection checklist signed by the substation supervisor for every company, vendor, and Engineering Services laptop | POL-05 4.2 | CIP-003-9 Att. 1 Sec. 5; CIP-010-4 R4 |
| Reporting | TCC and DCC reporting checklists with DOE-417 criteria 2, 3, 11, 12, and 14 and CIP-008-6 attempt criteria; printed forms and contacts at all four control centers | POL-03 4.4, 4.5 | CIP-008-6 R1, R4; DOE-417; EOP-004-4 |
| AMI commands | Bulk remote disconnects above 500 meters in an hour need a second approver; rate limit at the head-end | POL-02 4.11 | Benchmark |
| Control Center links | CIP-012-2 plan covers confidentiality, integrity, availability, and recovery of links to the RC and neighboring TOPs | POL-04 4.2 | CIP-012-2 R1 |

### 3.2 Gas Production supplement (voluntary OT benchmark)
| Topic | Division requirement (re-issue v2026) | Group policy it builds on | Driver |
|---|---|---|---|
| Field SCADA accounts | Named accounts on POC consoles and RTU engineering tools; shared accounts only for devices that cannot support named accounts | POL-02 4.1 | N21-BM (CSF PR.AA-01; SP 800-82r3 6.2.1) |
| Field connectivity | No well pad or compressor device reachable from the internet; private APN for all cellular modems | POL-02 4.4 | N21-BM (CSF PR.IR-01; SP 800-82r3 5.2.3) |
| Remote support | SCADA integrator access only through SYS-G4; no other remote support tools | POL-02 4.4 | N21-BM (SP 800-82r3 6.2.10) |
| Local control | Wells and stations go to local control during a cyber event at the POC; operators trained on the procedure | POL-03 4.3 | N21-BM (CSF RC.RP-01) |
| Logs | POC logs to the SIEM, 1 year retention | POL-01 4.11 | Group logging standard |
| Generator customers | Notify firm-supply generator customers through the matrix when deliveries are at risk | POL-03 4.5 | Firm supply contracts |

### 3.3 Engineering Services supplement (vendor to utilities; federal contractor; SOC 2 service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Client notice register | Register of every client contract's notice terms (incidents, access revocation, vulnerabilities); SOC findings routed to the contracts team within 4 hours | POL-03 4.5 | Client CIP-013-2 Part 1.2 terms |
| Client CEII and BCSI | Restricted project folders with client-approved access lists; no personal cloud storage; FERC CEII requests only with written client authorization | POL-04 4.4 | Client CIP-011-3 terms; 18 CFR 388.113(g)(1) |
| Personnel | Central register of personnel risk assessments with renewal alerts; records producible to clients within 5 business days | POL-02 4.6 | Client CIP-004-7 R3 terms |
| Commissioning laptops | Allowlisting on all laptops; pre-connection attestation report per site | POL-05 4.2 | Client CIP-010-4 R4 and CIP-003-9 Sec. 5.2 terms |
| Deliverable integrity | Settings files and scripts delivered with published hashes or signatures | POL-01 4.8 | Client CIP-013-2 Part 1.2.5 terms |
| AI design assistant | No CEII, BCSI, or client documents unless the client has agreed in writing; engineer review attestation on every AI-assisted deliverable | POL-05 4.5 | Client confidentiality terms; Group AI Standard |
| Federal contracts | FAR clause register; FCI only in approved repositories | POL-04 4.5 | FAR 52.204-21 |
| SOC 2 commitments | Any change to SYS-S1 services or subservice organizations reviewed against the SOC 2 system description before release | POL-01 4.8 | SOC 2 commitments |

## 4. Gas Production drift: conflicts with 2026 group policy
The 2023 Gas Production standards were written before the 2026 group policies and before the group OT program. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 GP-005).

| Topic | Gas Production standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Log retention | 90 days at the POC | 1 year online (logging standard) | Investigations limited to 90 days (P03 GP-G24) |
| Termination | Next business day | Within 4 hours (POL-02 4.6) | Longer exposure window |
| OT access | Not addressed; shared SCADA accounts accepted | Named accounts; MFA and SYS-G4 for remote access (POL-02 4.1, 4.4) | Shared accounts (P01 GP-003) |
| Remote support tools | Integrator may use its own tool | SYS-G4 only (POL-02 4.4) | Legacy tool still installed (P01 GP-016) |
| Incident severity | Division 3-level scale | One group scale; any OT effect is Severity 1 (POL-03 4.2) | Inconsistent escalation |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 7 (POAM-017) |

**Why the drift happened.** Gas Production joined the group program in 2024, but its standards had no owner or review date. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The Electric Utility statement adds: "Each mapped CIP document was reviewed for the changes." First attestations are due 2026-12-31 (Electric Utility, Engineering Services) and on re-issue (Gas Production).

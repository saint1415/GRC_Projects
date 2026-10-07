# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-10 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA everywhere, one severity scale, affiliates are vendors, Restricted information locations | Board safety, risk, and reliability committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, OT security standard, commissioning standard (new, due 2026-12-31), Group AI Standard (P10) | Group CISO (OT standards with the CIP Senior Manager) |
| **Division supplement** | Regulator-specific and system-specific rules (FERC Section 9 and NERC CIP for Hydro; DFARS and CMMC for Constructors; client commitments for Engineering) | Division president, after Group CISO alignment review. Hydro CIP topics also need CIP Senior Manager approval |
| Division procedures | OT incident procedures, FPE operating procedures, DSMS runbooks | Division security and compliance lead |

## 2. Supplement status
| Division | Version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Hydro | v2026 | 2026-08-20 (to the 2026 draft group policies) | Aligned; add the affiliate-as-vendor rule (POL-01 4.8) and commissioning sessions by 2026-12-30 | Confirm alignment |
| Constructors | v2023 | 2023-05 | **Drifted** (scenario gap 7); conflicts listed in section 4 | Re-issue with a Hydro site section by 2026-11-30 (POAM-017) |
| Engineering | v2025 | 2025-10 | Aligned, but missing DSMS change control and the AI rules required by POL-01 4.13 | Add by 2026-12-31 (POAM-012) |

## 3. What each supplement adds
### 3.1 Hydro supplement (FERC licensee; NERC GO and GOP)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CIP policies | CIP-003-9 R1 topics for medium and low impact systems, approved by the CIP Senior Manager every 15 calendar months | POL-01 4.2 | C-DAMS-R03 (CIP-003-9 R1) |
| OT identity | Separate OT identity domain; OT PAM; Intermediate Systems with MFA; no trust of corporate identity | POL-02 4.4, 4.5 | C-DAMS-R03 (CIP-005-7 R2); C-DAMS-R01 (Table 9.3b access control) |
| Commissioning at Hydro sites | All commissioning by affiliates or vendors in scheduled, escorted sessions approved by the HOC shift supervisor; Hydro-managed or Section 5.2-reviewed laptops; no cellular routers; logic changes approved by the Hydro change board with a Hydro witness | POL-01 4.8; POL-02 4.5, 4.6 | C-DAMS-R03 (CIP-003-9 Att. 1 Sec. 5.2 and 6); C-DAMS-R01 (Table 9.3a remote and third-party connections; secure design) |
| Section 9 | Criticality reviewed at least every 12 months; Form 3 maintained; plan and schedule for every negative answer | POL-01 4.10 | C-DAMS-R01 (Sec. 9.1.1.3; Table 9.3a) |
| DSMS interface | Data leaves OT only one way; no inbound path from the DSMS | POL-04 4.3 | C-DAMS-R01 (Table 9.3a segregation) |
| Safe state first | Local control and EAP actions come before evidence collection | POL-03 4.2 | 18 CFR 12.10; EAPs |
| BCSI | Restricted library; access authorization and 15-month verification | POL-04 4.3, 4.4 | C-DAMS-R03 (CIP-004-7 R6; CIP-011-3 R1) |
| Statements to FERC | Two-person evidence review of every certification letter and Form 3 | POL-01 4.10 | C-DAMS-R01 (Sec. 8.0) |

### 3.2 Constructors supplement (federal contractor; contractor inside owners' plants)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CUI | CUI only in the FPE; no CUI on the project platform or in shares; CUI printing only at approved offices; DLP on uploads | POL-04 4.3 | N23-R03 (252.204-7012(b)); N23-R04 (SP 800-171 Rev. 2 3.1.3, 3.10) |
| Incident reporting | DFARS reports within 72 hours at dibnet.dod.mil; two medium assurance certificate holders; 90-day preservation | POL-03 4.4, 4.9 | N23-R03 (252.204-7012(c) to (e)) |
| Hydro sites (new section) | At Hydro plants Constructors is a vendor: Hydro escort, Hydro training, Section 5.2 device review, no remote support tools or cellular routers, Hydro change approval | POL-01 4.8 | C-DAMS-R03 (CIP-003-9 Att. 1 Sec. 5.2, 6); C-DAMS-R01 (Table 9.3a) |
| Commissioning kits | Enrolled in EDR and patching; inventory with owner; wiped between owners | POL-02 4.6; POL-04 4.7 | N23-R01 (52.204-21(b)(1)(xii) to (xv)) |
| Subcontractors | External accounts expire at the project end; DFARS flow-down for CUI work | POL-02 4.7; POL-01 4.9 | N23-R03 (252.204-7012(m)) |
| Covered equipment | Pre-install review of cameras and recorders on federal jobs | POL-01 4.9 | N23-R02 (52.204-25) |
| Payment changes | Call-back verification of every banking change | POL-05 4.1 | Contract terms |

### 3.3 Engineering supplement (service provider to clients and to Hydro)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| DSMS change control | Threshold and model changes approved by a dam safety engineer, recorded, and announced to clients before release | POL-01 4.13 | Client contracts (security schedule sec. 7); SOC 2 CC8.1 (P09) |
| Client notices | Notify clients within 48 hours of confirming an incident affecting their data | POL-03 4.4 | Client contracts (security schedule sec. 4) |
| Client CEII | Restricted project libraries; NDA terms followed; destroy or return at the end | POL-04 4.3 | Client NDAs (18 CFR 388.113 terms) |
| Independence | No Part 12D or ODSP audit work for Hydro; conflict check on every proposal | POL-01 4.8 | 18 CFR 12.31(a)(3) to (5); 12.65(b) |
| AI in engineering work | AI-001 limits stated to clients; no AI for calculations in sealed work; AI-assisted drafting noted in the quality checklist | POL-05 4.9 | FTC Act Sec. 5 (claims); state licensure rules (generic) |

## 4. Constructors drift: conflicts with 2026 group policy
The 2023 Constructors supplement was written before the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but crews follow the document they know, so the conflicts are real risks (P01 CN-012, GR-12; P07 PL-01 finding).

| Topic | Constructors supplement (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Owners' plants | Treated as ordinary jobsites; site safety orientation only | Affiliates are vendors in Hydro OT (POL-01 4.8) | Commissioning kits bypassed Hydro's vendor controls (gap 1) |
| Remote support | Remote support tools allowed on commissioning laptops "for vendor help" | Prohibited inside Hydro plants (POL-02 4.5) | Always-on path at DEV-05 for 41 days |
| Device management | Commissioning laptops managed by project teams | EDR and patching for all devices (POL-02 4.6) | About 140 unmanaged kits |
| CUI | "Store CUI in the project folder marked CUI" on the project platform | CUI only in the FPE (POL-04 4.3) | CUI in 6 of 20 sampled USACE folders |
| Incident severity | Constructors 3-level scale | One group scale (POL-03 4.3) | Inconsistent escalation |
| AI use | Not addressed | AI inventory and approval (POL-01 4.13) | Estimating assistant and site cameras not reviewed before pilot |

**Why the drift happened.** The supplement had no named owner after the 2024 re-organization, and Constructors' security staff saw group policy as aimed at offices. **Fix:** POL-01 4.5 requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Hydro, Engineering) and on re-issue (Constructors).

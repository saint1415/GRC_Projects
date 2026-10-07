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
| Group policy (POL-01 to POL-05) | MFA everywhere, one severity scale, per-session approval for OT remote access, CUI only in the enclave | Board risk committee or Group CISO |
| Group standards | Group OT security standard, logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO; Group OT Security Director for OT |
| **Division supplement** | Regulator-specific and system-specific standards (for example, Tier 1 notice decisions, CMMC affirmation, hazmat route data, client notices) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks, ERPs, playbooks, work instructions | Division security and compliance lead (ERPs: Water Utility president, who signs the EPA certification) |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Water Utility | v2025 | 2025-11 (to the 2025 group policies) | Aligned except for one conflict: its remote access section allowed "project exceptions" to per-session approval, which produced the WTP-A commissioning exception | Remove the project-exception clause by 2026-10-31 (POAM-002) |
| Infrastructure Construction | v2023 | 2023-06 | **Drifted** (P01 GR-17): written before the CUI enclave; section 4 lists the conflicts | Re-issue by 2026-11-30 |
| Environmental Services | None | n/a | **Missing.** The division follows group policy directly; no division rules exist for client gateways, client notices, or federal tenants | First issue by 2026-11-30 |

## 3. What each supplement adds
### 3.1 Water Utility supplement (58 community water systems; 42 covered by SDWA section 1433)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Process safety first | Operators may put any process in local or manual control at any time without approval; they report afterward | POL-03 4.1 | 42 U.S.C. 300i-2(b)(2) |
| Control room sessions | Staffed control rooms may keep operator HMI shift sessions open with named sign-in for changes; no lockout on operator HMIs | POL-02 4.1 | SP 800-82 Rev. 3 tailoring |
| Remote access | Per-session approval by the control room shift supervisor for every remote session, including Construction commissioning; weekly recording review | POL-02 4.4 | 300i-2(a)(1)(A)(ii) |
| Management of change | Every PLC, HMI, setpoint, or alarm change goes through the system's MOC, including changes made by commissioning teams | POL-01 4.8 | 300i-2(a)(1)(A)(vi) |
| Tier 1 notice decisions | Each system names a primary and backup decision owner; a cyber-caused interruption of key treatment is always a Tier 1 decision point | POL-03 4.4 | 40 CFR 141.202(a)-(b) |
| RRA and ERP | Each covered system's RRA cyber element uses its asset inventory and the division register; each ERP carries the OT playbook and recovery procedure | POL-01 4.3 | 300i-2(a)-(b) |
| Acquired systems | Within 30 days of closing an acquisition: inventory remote access paths, remove always-on vendor tools, change default and shared credentials | POL-02 4.4, 4.8 | 300i-2(a)(1)(A)(ii) |
| Anomaly detection (AI-001) | Alerts support operators; SCADA alarms, hardwired alarms, and grab samples remain the controls of record | POL-01 4.12 | P10 |

### 3.2 Infrastructure Construction supplement (DoD and federal contractor; controls integrator)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CUI handling | CUI only in SYS-C2; quarterly discovery scans of SYS-C1, file shares, and laptops; any CUI found outside is a reportable internal incident | POL-04 4.2 | 252.204-7012(b)(2); SP 800-171 3.1.3 |
| CMMC affirmation | The Affirming Official affirms only after group internal audit or counsel reviews scope and evidence | POL-01 4.9 | 32 CFR 170.22 |
| DFARS reporting | Two certificate holders; 72-hour clock starts at discovery | POL-03 4.5 | 252.204-7012(c) |
| Commissioning laptops | Group-managed; no CUI; reach client or Water Utility OT only through SYS-G4 or on site under an interconnection agreement | POL-02 4.10; POL-05 4.7 | SP 800-171 3.1.20 |
| Flowdown | Every subcontract involving CUI carries 252.204-7012; FCI subcontracts carry 52.204-21 | POL-01 4.8 | 252.204-7012(m); 52.204-21(c) |
| Covered equipment | Local job-site purchases of cameras and network gear are checked against the prohibited list before purchase | POL-01 4.8 | 52.204-25(b) |
| Video analytics | Notice to workers at each site; human review before any discipline | POL-05 4.8 | P10 |

### 3.3 Environmental Services supplement (to be issued; service organization for monitoring clients)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Client site gateways | Hardening baseline enforced; no default credentials; firmware within one version of current | POL-02 4.8 | 52.204-21(b)(1)(vi), (xii) |
| Client notices | Notice register by client contract; security incidents affecting a client's data or service are reported to the client within the contract time | POL-03 4.6 | Client contracts; SOC 2 commitments (P09) |
| Federal tenants | FCI tenants tagged and reviewed quarterly against the 15 basic safeguarding requirements | POL-04 4.5 | 52.204-21(b)(1) |
| Hazmat route data | Route, load, and schedule data for covered shipments visible only to named dispatchers | POL-04 4.1 | 49 CFR 172.802(a)(2)-(3) |
| Consumer reports | Disposal by shredding or secure erasure at every branch | POL-04 4.8 | 16 CFR 682.3 |

## 4. Construction drift: conflicts with 2026 group policy
The 2023 Construction standards were written before the CUI enclave existed. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 CN-001, CN-004; P03 CG-014, CG-016).

| Topic | Construction standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| CUI storage | "Project share or encrypted laptop" | Enclave only (POL-04 4.2) | CUI on 11 laptops and in 3 SYS-C1 workspaces |
| Removable media | Encrypted USB allowed for drawings | No removable media for CUI (POL-05 4.3) | USB copies found on 4 laptops |
| Laptop admin rights | Engineers are local administrators | No standing local admin (POL-02 4.7) | SP 800-171 3.5.3 fails on in-scope laptops |
| File transfer to subcontractors | Any encrypted transfer tool | FIPS-validated enclave transfer (POL-04 4.2) | 3.13.11 not met |
| Remote commissioning | "Coordinate with the owner" | Per-session approval through SYS-G4 (POL-02 4.4) | The WTP-A exception |
| Self-assessment | Program owner submits | Review before submission or affirmation (POL-01 4.9) | Inaccurate SPRS record |

**Why the drift happened.** The Construction supplement had no review date, and the enclave project in 2024 changed systems without changing the standard. **Fix:** POL-01 4.5 requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office now tracks supplement versions.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Water Utility) and on issue (Construction and Environmental Services).

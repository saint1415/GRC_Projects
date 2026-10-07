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
| Group policy (POL-01 to POL-05) | CUI only in the enclave, payment-instruction rule, Section 889 approved-manufacturer list, one severity scale | Board risk committee or Group CISO |
| Group standards | Building systems standard, logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Contract-, customer-, and system-specific rules (for example, TSSI client credentials, PCI DSS for parking, design-build subcontractor reporting) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks, jobsite checklists, work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Construction | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Add trailer visitor log and field CUI rules (sections 3.1) |
| Property | v2024 | 2024-04 | **Drifted** (scenario gap 4); conflicts listed in section 4 | Re-issue by 2026-12-31 (POAM-026) |
| A&E | v2026 | 2026-05-29 | Aligned; missing the subconsultant status check required by POL-01 4.8 | Add by 2026-12-31 (POAM-020) |

## 3. What each supplement adds
### 3.1 Construction supplement (federal prime contractor; TSSI systems integrator and managed service provider)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Field CUI access | Superintendents on DoD projects use enclave virtual desktops in trailers; no "field release" exports; plots only from enclave desktops, marked, in locked plan storage | POL-04 4.2-4.3 | DFARS 252.204-7012(b)(2); 252.204-7021(d)(2); SP 800-171 R2 3.1.3, 3.8.4, 3.10.6 |
| Jobsite trailers | Electronic visitor sign-in on the trailer tablet; escort visitors where FCI or CUI is displayed; screens face away from windows; locked plan storage | POL-02 4.13 | FAR 52.204-21(b)(1)(viii)-(ix) |
| Pay applications | Remittance block generated only from verified SYS-G4 bank data; standing remittance letter to every owner; confirmation call before the first payment to any account | POL-01 4.15 | FAR 52.232-33; P01 CON-001 |
| Subcontractors | SPRS status check before award of any subcontract that will receive FCI or CUI; award hold if missing; certified payrolls only through the PDPP intake | POL-01 4.8; POL-04 4.7 | DFARS 252.204-7021(f)(2); FAR 52.222-8 |
| TSSI Section 889 | Every submittal screened against the group approved-manufacturer list; private-label products traced to the parent manufacturer before purchase | POL-01 4.14 | FAR 52.204-25(b)(1) |
| TSSI client credentials | Per-client vault partitions; release only on an approved work order; rotate at handover and when a technician leaves; remote sessions through group PAM with recording | POL-02 4.10-4.11 | Client contracts; SOC 2 commitments (P09) |
| AI estimating assistant | Enterprise tenant only; no CUI; FCI only after the conditions in P10 are met; pooled pricing features off | POL-04 4.13; POL-05 4.8 | FAR 52.203-2; FAR 52.204-21(b)(1)(iii) |
| Drones and photos | No posting of federal site imagery without federal practice leader approval | POL-04 4.14 | FAR 52.204-21(b)(1)(iv) |

### 3.2 Property supplement (owner and operator of 64 properties; merchant for parking)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Building systems | BAS, access control, and video on segmented networks; no integrator VPNs; controller configuration backups held by Property; default credentials changed and checked at every acceptance | POL-01 4.13; POL-02 4.10 | Group building systems standard; P01 PRP-001, PRP-018 |
| Accounts payable | All vendor and tenant-refund bank changes made in the payment factory, not in SYS-D3 | POL-01 4.15 | FTC Act Section 5 (portal statements); P01 PRP-005 |
| Tenant remittance | Written notice to every tenant of how the group changes remittance details (it never does so by email); lookalike domain monitoring for property websites; DMARC reject on all property domains | POL-01 4.15 | P01 PRP-003 |
| Parking (PCI DSS v4.0.1) | Pay stations on their own network segment; named manager accounts with MFA on the provider portal; device inspection logs; written responsibility matrix with the provider; segmentation test after separation | POL-02 4.1; POL-04 4.9 | N53-R04 Requirements 1, 8, 9, 11, 12.8 |
| Federal leases | Lease security commitments mapped for all 9 federally leased properties; covered equipment removed under POL-01 4.14 | POL-01 4.14 | GSA lease contracts (clauses under counsel review) |
| Common control inheritance | Inheritance matrix for SYS-D3 and SYS-D4 in the common control catalog | POL-01 4.6 | P07 CA-2 findings (POAM-021) |

### 3.3 A&E supplement (designer of record; DoD architect-engineer contractor; digital twin service)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Design-build reporting | As Construction's subcontractor, A&E reports cyber incidents to DoD and gives the report number to Construction as soon as practicable, under the intercompany agreement | POL-03 4.4 | DFARS 252.204-7012(m)(2)(ii) |
| Subconsultants | SPRS status check before award; enclave guest accounts for subconsultants without the required status | POL-01 4.8 | DFARS 252.204-7021(f)(2); 32 CFR 170.23 |
| Specifications | Master specifications for video surveillance and networks reference the group approved-manufacturer list | POL-01 4.14 | FAR 52.204-25(b)(1), (e) |
| Sealed drawings | Sealed drawing sets hashed at sealing; any later change requires a new seal | POL-04 4.1 | P01 AE-012 |
| AI design tools | Generative design and code compliance assistants are advisory; the engineer of record reviews every output before it enters sealed drawings | POL-01 4.12 | State professional licensing rules (generic); P10 |
| Digital twin service | Tenant isolation tests at every release; backups include system documentation; no CUI in the service | POL-04 4.2, 4.10 | Client agreements; SOC 2 (P09) |

## 4. Property drift: conflicts with 2026 group policy
The 2024 Property standards were written before the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but building engineers and property accountants follow the document they know, so the conflicts are real risks (P01 PRP-009; P07 PL-01c.01[02] and PL-01c.02[02]).

| Topic | Property standard (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| Integrator remote access | Integrators may keep site VPNs for support | Group PAM only; persistent tunnels prohibited (POL-02 4.10) | 11 integrators with persistent access (POAM-023) |
| Vendor bank changes | One approver in SYS-D3 | Payment factory with call-back and second approver (POL-01 4.15) | Fraud exposure in Property AP (POAM-031) |
| Building networks | Not addressed | Segmented networks (POL-01 4.13) | 41 of 64 properties flat (POAM-022) |
| Monitoring | Local controller logs only | Logs to the group SOC (POL-01 4.13) | Attacks on building systems go unseen (POAM-003) |
| Controller credentials | Integrator sets credentials | Default credentials changed before use (POL-01 4.13) | Default credentials on 14 controllers (POAM-024) |
| Section 889 | Not addressed | Group approved-manufacturer list (POL-01 4.14) | Covered cameras at 2 federally leased properties (POAM-029) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 4 (POAM-021) |

**Why the drift happened.** Property security moved under the Group CISO in 2025, but the supplement kept its 2024 owner (the former Property IT manager) and had no review date. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Construction, A&E) and on re-issue (Property).

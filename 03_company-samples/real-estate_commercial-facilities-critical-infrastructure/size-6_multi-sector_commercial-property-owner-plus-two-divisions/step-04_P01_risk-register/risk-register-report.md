# Risk Register Report: Cris Santos Company Holdings | Commercial Facilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Real Estate, Construction, Accommodation) |
| Focus division | Commercial Property (NAICS 531120) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1; OT threats informed by NIST SP 800-82 Rev. 3 |
| Registers | `risk-register.csv` (group), `risk-register-commercial-property.csv`, `risk-register-construction.csv`, `risk-register-hotels.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads and the Group OT security lead |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that controls buildings or holds personal, card, or federal contract data in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and WAN, SYS-G4 ERP and treasury, and SYS-G5, the BAACS (the P02 SSP system). Division systems are SYS-D1 to SYS-D8 (`../00_company-facts.md` section 3).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Commercial Property, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not simply copied from the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Life-safety risks rated High (heat, ventilation, egress, fire alarm interfaces) may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 OT threat examples, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), site walkthroughs, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Safety impact (tenants, guests, workers) is rated alongside cost, operations, regulatory, and reputation. Group impact reflects enterprise consequences: many buildings at once, several regulators, SEC disclosure, and more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 12 | 2 | 0 | 18 | n/a |
| Commercial Property | 0 | 5 | 15 | 8 | 0 | 28 | 14 |
| Construction | 0 | 2 | 11 | 3 | 0 | 16 | 10 |
| Hotels | 0 | 3 | 10 | 3 | 0 | 16 | 6 |
| **All registers** | **0** | **14** | **48** | **16** | **0** | **78** | **30** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Ransomware spreads through the BAACS and stops building supervision at many sites at once | CF-001, CF-002, HO-004, CN-003 | Remove legacy remote tools; segment remaining sites; back up every site program; OT monitoring; cross-division tabletop | Group CISO | 2027-12-31 |
| GR-02 | Compromise of the BTI integrator tools gives an attacker programs, drawings, and credentials for every group building | CN-001, CN-002, CF-005, CN-015 | Move SYS-D5 into the landing zone; group vault for OT credentials; security terms in the intercompany agreement | Group CISO | 2026-12-31 |
| GR-03 | The group cannot restore building supervision at scale | CF-005, CF-006, HO-004 | Site program backups; standby supervisor; manual procedures; multi-site restore exercise | Group building technology director | 2027-06-30 |
| GR-05 | AI and biometric features deployed without governance | CF-010, CF-011, CF-012, HO-010, HO-012, HO-013, CN-010, CN-011 | Group AI program applied to every use case; vendor feature change gate (P10) | Group Chief Risk Officer | 2027-03-31 |

### Commercial Property (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| CF-001 | Ransomware through a legacy vendor remote-support tool at 47 sites | Remove all legacy tools; gateway only; block vendor relay services | Group OT security lead | 2026-12-31 |
| CF-002 | Malware on building IT reaches BAS and access control devices on flat networks (81 of 142 properties) | OT zones with deny-by-default rules at every property | Group OT security lead | 2027-12-31 |
| CF-005 | Site programs cannot be rebuilt because the only copy is in the BTI repository | Export every site program to the group vault; quarterly restore tests | Group building technology director | 2027-03-31 |
| CF-011 | Face verification creates biometric data and denies tenants entry on false matches | Suspend automatic denial; consent and retention rules; bias testing; council decision | Group Chief Privacy Officer | 2026-12-31 |
| CF-019 | A life-safety interface can be changed through the BAS where the read-only assumption is wrong | Verify every interface with the fire alarm vendor; document in site diagrams | Commercial Property vice president of engineering | 2027-03-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| CN-001 | Construction | CUI drawings for 2 DoD client facilities stored in the BTI repository, outside the enclave | Construction director of federal contracts compliance | 2026-11-30 |
| CN-002 | Construction | BTI tools compromised through the legacy cloud account | Construction division security and compliance lead | 2026-12-31 |
| HO-001 | Hotels | Card numbers stolen from the legacy PMS at 14 acquired hotels | Hotels payment security lead | 2027-03-31 |
| HO-002 | Hotels | Failed segmentation lets attackers reach the cardholder data environment at 6 hotels | Hotels payment security lead | 2026-12-31 |
| HO-012 | Hotels | The hourly hiring screening tool screens out applicants unfairly | Group HR director | 2026-12-31 |

### What the results say
The corporate IT program is sound. There are no Very High risks, and identity, the SOC, cloud guardrails, and immutable backups work as designed (P07). The High risks cluster around **the buildings and the people who service them**, not around office IT:
1. **The BAACS is one platform for 264 buildings** (GR-01, GR-03). Where segmentation and the remote access gateway exist, it is well protected. Where they do not, one compromised integrator session can reach many buildings, and the group could not restore them quickly (scenario gaps 1 and 3).
2. **The integrator is inside the family but outside the program** (GR-02). The BTI unit holds credentials and programs for every group building, but its tools run in a Construction account outside the landing zone, under a 2021 agreement with no security terms (gap 4). The same tools held CUI that should never have left the enclave (CN-001).
3. **AI arrived through vendors** (GR-05). Tailgating detection, face verification, and the BAS optimization service were switched on by vendors before the Group AI Standard could reach them (gap 6).

Visibility (GR-09) and cross-division notification (GR-04) are Moderate at group level. They matter because they decide how fast the group would know about, and report, the High scenarios above.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q4):** legacy remote tool removal and OT segmentation (GR-01); BTI tools into the landing zone and OT credentials into the group vault (GR-02); site program backups, a standby supervisor, and manual procedures (GR-03); group AI program (GR-05); OT monitoring sensors at critical-occupancy sites (GR-09).
- **Accepted (all Low):** CF-020 (console operator video misuse, covered by GR-16 reviews), CF-022 (access control vendor outage, covered by offline door operation), CN-009 (jobsite tablet loss, encrypted and wiped), CN-014 (BIM model loss), and HO-015 (outlet skimmer, covered by inspections).
- **Shared or transferred:** CF-023 (parking operator attestation), CF-025 and HO-016 (hurricane damage, insurance).
- **Contract actions:** intercompany services agreement security terms (GR-02); federal subcontract flowdown riders (CN-007); guard contractor security addendum (CF-016).
- **Treatment status:** 54 risks are In progress, 19 are Open (treatment approved, work not started), and 5 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-15. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line), and GR-11 tracks the review of that text against these results.

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the ten High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-18.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.

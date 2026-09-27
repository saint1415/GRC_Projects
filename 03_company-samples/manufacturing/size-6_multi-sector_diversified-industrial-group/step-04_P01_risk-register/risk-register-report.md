# Risk Register Report: Cris Santos Company Holdings | Manufacturing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Manufacturing, Wholesale Trade, Professional Services) |
| Focus division | Medical Devices (NAICS 334510), a registered device manufacturer and, for its device cloud, a HIPAA business associate |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | Medical Devices: the risk input to cybersecurity risk management under FD&C Act 524B(b)(2) and the QMSR, and the device cloud's HIPAA risk analysis (45 CFR 164.308(a)(1)(ii)(A)). Distribution: the risk basis for its FAR 52.204-21 self-assessment scope |
| Registers | `risk-register.csv` (group), `risk-register-medical-devices.csv`, `risk-register-distribution.csv`, `risk-register-testing.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads and the Chief Product Security Officer |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Enterprise IT and OT in all three divisions, the software release chain and fielded devices of the Medical Devices division, and the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud, network, and colocation data center, and SYS-G4 ERP and HR. Division systems are SYS-D1 to SYS-D7 (`../00_company-facts.md` sections 3 and 7).

**Product risk and enterprise risk together.** For Medical Devices, a cybersecurity risk to a fielded device is also a patient safety risk. This register rates the cybersecurity side with SP 800-30. The safety side (hazard analysis and risk control under the QMSR design controls) stays in each product's risk management file, and each device risk here names the product. Exploitability-based scoring for premarket submissions follows FDA's guidance and lives in the product security risk assessments, not in this register.

**Two levels of register.**
- **Division registers** hold risks each division owns and can treat itself. Medical Devices, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back. Group risks are rated on their own group-level likelihood and impact. They are not simply the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Patient-safety risks rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment and DEMS testing (P07), PSIRT case history, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Device risks with plausible patient harm are rated Very High. Group impact reflects enterprise consequences: several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 11 | 5 | 0 | 20 | n/a |
| Medical Devices | 0 | 4 | 16 | 8 | 0 | 28 | 19 |
| Distribution | 0 | 2 | 6 | 8 | 0 | 16 | 11 |
| Engineering and Product Testing Services | 0 | 2 | 5 | 7 | 0 | 14 | 9 |
| **All registers** | **0** | **12** | **38** | **28** | **0** | **78** | **39** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Compromise of the device software release chain pushes malicious firmware to fielded devices | MD-003, MD-004, MD-012, MD-014 | IX-3 signing into the HSM service or a planned key transition; supplier SBOM coverage; independent release chain test | Group CISO with the Chief Product Security Officer | 2027-03-31 |
| GR-02 | Exploitation of fielded legacy IX-3 pumps with multi-regulator response | MD-001, MD-002, MD-011, DS-004 | IX-3 end-of-support plan; SBOM; field update campaign; cross-division exercise | Medical Devices division president | 2027-06-30 |
| GR-03 | Ransomware spreads from IT into plants and distribution centers | MD-005, MD-015, DS-001, DS-002, TS-010 | Segment Plants D and E; OT logs to the SIEM; vault copies of plant backups; tabletop | Group CISO | 2027-03-31 |
| GR-05 | Testing client data or unpublished findings reach Medical Devices staff or leak | TS-001, TS-002, TS-009, MD-020, MD-027 | Close the shared space; barrier groups; monitoring; independence statements | Group General Counsel with the Testing division president | 2026-12-31 |

### Medical Devices (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| MD-001 | IX-3 embedded web server exploited to change pump configuration or drug library limits | Out-of-cycle IX-3 fix; interim hospital guidance; field campaign | VP Engineering | 2026-12-31 |
| MD-002 | IX-3 embedded operating system component loses supplier support in June 2027 | End-of-support plan: extended support, compensating controls, trade-in to IX-4 | Medical Devices division president | 2027-03-31 |
| MD-003 | IX-3 software signing key on the Plant D build server stolen or misused | Move signing to the HSM service or transition IX-3 to a new HSM key | VP Engineering | 2027-03-31 |
| MD-005 | Ransomware spreads through flat networks at Plants D and E | Production zones and firewalls as at Plants A to C | VP Manufacturing Operations | 2027-03-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| DS-001 | Distribution | Ransomware encrypts the distribution ERP and warehouse systems and halts hospital supply | Distribution security and compliance lead | 2027-06-30 |
| DS-003 | Distribution | No CMMC Level 1 status when DoD exercises the 2027-03-31 option | Distribution federal contracts compliance director | 2027-02-28 |
| TS-001 | Testing | Unpublished client vulnerability findings leak from the findings vault or collaboration tools | Cybersecurity testing practice lead | 2026-12-31 |
| TS-002 | Testing | Competitor design data reaches Medical Devices staff | Testing division president | 2026-12-31 |

### What the results say
The group program is mature: there are no Very High risks, common controls are strong, and Medical Devices already runs a PSIRT, a published CVD policy, ISAO membership, automated SBOMs, and HSM signing for its current products. The High risks cluster in three places:
1. **Legacy and acquired assets** (GR-01, GR-02, GR-03). IX-3 predates section 524B and still depends on a software signing key at Plant D, and the 2024 acquisitions brought flat plant networks. These are the "legacy" residual gaps expected at this size (scenario gaps 1 and 2).
2. **Conflicts between divisions** (GR-05). Owning a testing business that serves competitors creates a confidentiality duty the rest of the group does not have. The barrier is policy only (gap 5).
3. **Contract eligibility** (DS-003). Distribution has federal contract clauses but has never measured itself against them (gap 4). This is rated High at division level and Moderate at group level (GR-06), because the group exposure is one contract.

Shared-service governance gaps (inheritance, notification, AI) are Moderate at group level (GR-04, GR-09, GR-10) but matter because they decide whether the High risks are handled on time. That is why P07 sampled Distribution and Testing controls and P08 builds one multi-regulator matrix.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** IX-3 key transition and end-of-support plan (GR-01, GR-02); Plants D and E segmentation and OT monitoring (GR-03, GR-12); Testing information barrier (GR-05); Distribution FCI enclave and CMMC Level 1 self-assessment (GR-06); colocation disaster recovery replica (GR-15); group AI governance program (GR-09).
- **Accepted (all Low):** MD-021 (primary HSM failure, covered by the backup HSM), MD-023 (encrypted laptop theft), MD-024 (DCC denial of service, bedside unaffected), TS-014 (encrypted laptop theft).
- **Avoided:** DS-014 (private-label relabeling stays on hold until a quality system and registration plan exist).
- **Treatment status:** 63 risks are In progress, 10 are Open (treatment approved, work not started), and 5 are Closed (the four accepted risks and the avoided one).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-15. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here: board risk committee oversight, the Group CISO's reporting line, and the role of the Chief Product Security Officer for product cybersecurity.

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the eight High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-10 to 2026-09-15.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.

# Risk Register Report: Cris Santos Company Holdings | Food and Agriculture | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Food and Agriculture, Wholesale Trade, Retail Trade) |
| Focus division | Meat Processing (NAICS 311612), six FSIS-inspected plants |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with SP 800-82 Rev. 3 for OT threat context; roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also supports | The Plant 6 food defense vulnerability assessment and its reanalysis (21 CFR 121.130, 121.157) for cyber-physical process steps; the PCI DSS targeted and annual risk analysis inputs for Grocery Retail (PCI DSS Req. 12.3) |
| Registers | `risk-register.csv` (group), `risk-register-meat-processing.csv`, `risk-register-food-distribution.csv`, `risk-register-grocery-retail.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads and the Group Chief Food Safety and Quality Officer |
| Approved | 2026-09-15 by the board risk committee (group register, all High and Very High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system in the three divisions that runs or records food production, storage, or transport, holds personal or payment card data, or supports a division's core service, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and colocation, SYS-G4 ERP, SYS-G5 OT security services, and SYS-G6 cold-chain monitoring (`../00_company-facts.md` section 3).

**What makes these registers different from an office IT register.** Many risks here end in adulterated or temperature-abused food, not in lost data. Impact ratings therefore weigh consumer health, product holds and recalls, and FSIS or FDA action as well as downtime, cost, and breach duties (P05 impact categories).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Meat Processing, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each of those division risks points back to it. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks that could put adulterated product into commerce may not be accepted at High or Very High. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, SP 800-82 Rev. 3, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), the Plant 6 food defense plan, and interviews with plant, DC, and store leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the P05 impact categories, which include a food safety category. Group impact reflects enterprise consequences: several divisions at once, several regulators, brand-wide recalls, and SEC disclosure.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 14 | 2 | 0 | 20 | n/a |
| Meat Processing | 1 | 7 | 10 | 12 | 0 | 30 | 19 |
| Food Distribution | 0 | 1 | 12 | 4 | 1 | 18 | 12 |
| Grocery Retail | 0 | 2 | 8 | 8 | 0 | 18 | 13 |
| **All registers** | **1** | **14** | **44** | **26** | **1** | **86** | **44** |

17 of the 20 group risks roll up at least one division risk; GR-07, GR-10, and GR-17 are group-only.

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Ransomware spreads through the corporate directory to plant OT and DC automation and halts production and deliveries in several divisions | MT-001, MT-004, FD-001, RT-007 | OT domain migration and DMZ at Plants 2 and 5; DC automation to the OT domain; privileged service accounts into PAM; offline OT backups; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-02 | Outage or compromise of the shared cold-chain monitoring platform blinds monitoring in all divisions at once | MT-011, FD-002, RT-006 | Active-active alert integration with tested failover; alerts into the SOC; segmented gateways; vendor assurance review | Group cold-chain services manager | 2027-01-31 |
| GR-09 | Intentional adulteration of product through the control system or recipe library | MT-003, MT-007, MT-009, MT-012, MT-017, MT-019 | Named HMI accounts; two-person formulation approval at all plants; library change alerts; Plant 6 food defense reanalysis | Group Chief Food Safety and Quality Officer | 2026-12-31 |
| GR-12 | An OT vendor remote access path is used to reach plant or DC control systems | MT-002, MT-005, MT-014, MT-030, FD-006 | SYS-G5 at Plants 2 and 5 and three DCs; remove the shared VPN and the modem; vendor security terms | Group OT security director | 2026-12-31 |

### Meat Processing (focus division): risks rated High or Very High
| Risk ID | Level | Risk | Treatment | Owner | Due |
|---|---|---|---|---|---|
| MT-030 | **Very High** | Default vendor passwords on OT devices at Plants 2 and 5 (found in P07 testing on 2026-08-15) | Changed during testing where safe; credential sweep at all plants | Division controls engineering manager | 2026-09-30 |
| MT-001 | High | Ransomware from the corporate domain halts lines and cold storage monitoring at Plants 2 and 5 | OT DMZ and OT domain migration; OT endpoint protection; offline backups | Meat Processing security and compliance lead | 2027-03-31 |
| MT-002 | High | Integrator's shared always-on VPN used to reach SCADA at Plants 2 and 5 | Disable; access only through SYS-G5 | Group OT security director | 2026-12-31 |
| MT-003 | High | Cure or brine formulation changed in MES or the recipe library | Named accounts and two-person approval at Plants 2 and 5; change alerts to FSQA | Division VP FSQA | 2026-12-31 |
| MT-004 | High | OT backups at Plants 2 and 5 lost with production | Offline, immutable copies; PLC repository; quarterly restores | Division controls engineering manager | 2026-12-31 |
| MT-005 | High | Plant 5 refrigeration controller reached through the contractor's modem | Remove the modem; SYS-G5 access | Plant 5 refrigeration manager | 2026-11-30 |
| MT-007 | High | CIP chemical routed into the Plant 6 plant-based brine system | Hardwired interlock; actionable process step in the reanalysis | Plant 6 plant manager | 2026-11-30 |
| MT-017 | High | Cloud administrator compromise used to change formulations in the recipe library | Separate library administration; change alerts; signed releases | Division controls engineering manager | 2026-12-31 |

**The Very High risk.** MT-030 was added on 2026-08-15 after P07 testing found manufacturer default passwords on three packaging HMIs at Plant 2 and on the Plant 5 refrigeration controller. The board risk committee was informed on 2026-09-15; it may not be accepted, and the credential sweep was due 2026-09-30.

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| FD-001 | Food Distribution | Ransomware encrypts DC automation and WMS integration servers and halts shipping | Food Distribution security and compliance lead | 2027-03-31 |
| RT-001 | Grocery Retail | Card data skimmed by malware at the 30 stores outside P2PE | Grocery Retail payments security manager | 2027-03-31 |
| RT-002 | Grocery Retail | Store Wi-Fi management network can reach POS lanes in one store design (12 stores) | Grocery Retail payments security manager | 2026-11-30 |

### What the results say
The program is defined and most common controls work: a 24x7 SOC, MFA, PAM, immutable cloud backups, and an OT gateway at four plants. The High risks cluster around **what the group shares and what it acquired**:
1. **The corporate directory reaches OT at two acquired plants and the DC automation** (GR-01, scenario gaps 1 and 7). One identity compromise can stop lines in Meat Processing and shipping in Food Distribution, which then empties store shelves.
2. **One cold-chain alert path serves every division** (GR-02, gap 2). Its failure is not a data problem; it is a food safety problem at 6 plants, 5 DCs, 900 trailers, and 120 stores at once.
3. **Food defense through the control system** (GR-09, gaps 3 and 4). Shared operator logins and an unreanalyzed Plant 6 plan leave formulation and CIP paths that cannot be attributed or stopped.
4. **Vendor remote access at acquired sites** (GR-12, gaps 1 and 9).

Grocery Retail is the most mature division because the annual PCI DSS ROC forces scope and testing discipline; its two High risks come from that testing (RT-002) and from terminals not yet replaced (RT-001). Food Distribution's governance gaps (drifted standards and undocumented inheritance) are Moderate at group level (GR-05, GR-06), but they hide whether its controls operate, which is why P07 sampled it on governance.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** OT domain migration, OT DMZ, and SYS-G5 rollout at Plants 2 and 5 and three DCs (GR-01, GR-12); active-active cold-chain alerting (GR-02); named HMI sign-in across all plants (GR-09); store network fix and terminal replacement (GR-11); OT monitoring extension (GR-15); group AI program (GR-04).
- **Accepted (all Low or Very Low):** MT-015 (phishing foothold on plant office workstations, covered by EDR and MFA), MT-028 (single WAN carrier at Plants 3 and 4, covered by standing schedules), FD-012 (telematics vendor location data), FD-018 (inventory manipulation, detected by cycle counts), RT-011 (guest Wi-Fi abuse).
- **Contract actions:** security terms for the Plants 2 and 5 integrator and refrigeration contractors (GR-12); cold-chain vendor assurance (GR-02); delivery partner terms (RT-014).
- **Treatment status:** 38 risks are In progress, 43 are Open (treatment approved, work not started), and 5 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter, next to the group's food safety and commodity risks. The four High group risks and the one Very High division risk were presented on 2026-09-15. The Reg S-K Item 106 description in the next annual report draws on the governance described here (GR-17).

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, the MT-030 response, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the 10 High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-15.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.

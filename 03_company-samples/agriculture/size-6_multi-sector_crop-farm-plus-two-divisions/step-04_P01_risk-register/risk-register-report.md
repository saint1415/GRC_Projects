# Risk Register Report: Cris Santos Company Holdings | Agriculture | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees at seasonal peak; Agriculture, Manufacturing, Wholesale Trade) |
| Focus division | Crop Farming (NAICS 111998), the least mature division |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1; OT threat events and predisposing conditions from NIST SP 800-82 Rev. 3 Appendix C |
| Registers | `risk-register.csv` (group), `risk-register-crop-farming.csv`, `risk-register-food-processing.csv`, `risk-register-farm-supply.csv` |
| Fieldwork | 2026-05-01 to 2026-07-31 (off-season for Florida strawberries) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads and the two OT security managers |
| Approved | 2026-09-10 by the board risk committee (group register, all High and Very High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system in the three divisions plus the corporate shared services they depend on: SYS-G1 (identity), SYS-G2 (SOC and OT monitoring), SYS-G3 (cloud platform and WAN), and SYS-G4 (ERP, HR, and payroll). Division systems are SYS-D1 to SYS-D5, with their components, in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv); suppliers are in the [vendor register](../step-00_P00_intake/vendor-register.csv). OT is in scope everywhere: farm irrigation and fertigation, plant process lines, ammonia refrigeration, and blending plants.

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Crop Farming, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating.

**Risk tolerance and who can accept risk** (group risk management strategy, EV-016):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

**Worker-safety and food-safety risks rated High must be treated, not accepted.** That rule covers FP-001 and FP-002 and the group risks GR-02 and GR-06.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E and SP 800-82 Rev. 3 Appendix C, the BIA (P05), the intake evidence, risk interviews with each division's operations, food safety, and OT leads (EV-079 group, EV-080 Crop Farming, EV-081 Food Processing, EV-082 Farm Supply), the gap analyses (P03), and the first results of the common control assessment and OT sampling (P07), which began on 2026-07-01 inside the fieldwork window. The farm data hub storage review during this fieldwork found the H-2A onboarding exports behind CF-009 (EV-083).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column of all four registers: configuration exports, inventories, contracts, plans, record samples, interviews, and the P07 tests completed by 2026-07-31. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05), including safety. Group impact reflects enterprise consequences: several divisions at once, SEC disclosure, and food supply effects beyond one plant or farm.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 11 | 5 | 0 | 20 | n/a |
| Crop Farming (`risk-register-crop-farming.csv`) | 1 | 3 | 16 | 9 | 1 | 30 | 20 |
| Food Processing (`risk-register-food-processing.csv`) | 0 | 2 | 6 | 10 | 0 | 18 | 13 |
| Farm Supply (`risk-register-farm-supply.csv`) | 0 | 1 | 8 | 9 | 0 | 18 | 12 |
| **All registers** | **1** | **10** | **41** | **33** | **1** | **86** | **45** |

### Group risks rated High
| Risk ID | Level | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| GR-01 | High | Ransomware enters through third-party remote access at a 2024 acquired farm, spreads from farm OT to the corporate cloud network and ERP, and steals personal data | CF-001; CF-002; CF-004; CF-016; FP-004; FS-009 | Replace integrator access with group PAM; OT DMZ at each ROC; farm directory under PAM with MFA; cross-division ransomware tabletop in freeze season | Group CISO | 2026-12-31 |
| GR-02 | High | Malicious manipulation of operational technology causes crop loss, worker injury, or a chemical release (farm irrigation and fertigation, plant process lines, ammonia refrigeration, blending plants) | CF-003; CF-005; CF-008; FP-002; FS-008 | Logic integrity checks; fail-safe settings at acquired farms; OT monitoring at all farms; review contractor sessions | Group CISO | 2027-06-30 |
| GR-06 | High | Food defense and food safety plans do not consider cyber manipulation of process controls or of the electronic records they rely on | FP-001; FP-003; FP-007 | Reanalyze vulnerability assessments with cyber attack scenarios; add record integrity controls | Food Processing VP Food Safety and Quality | 2027-03-31 |
| GR-12 | High | Compromise of the legacy farm operations directory gives control of all three ROCs | CF-002 | Bring administrators under PAM with MFA; forward directory events to the SIEM; migrate to SYS-G1 by 2027-12-31 | Group CISO | 2026-12-31 |

### Crop Farming (focus division): risks rated High or Very High
| Risk ID | Level | Risk | Treatment | Owner | Due |
|---|---|---|---|---|---|
| CF-001 | Very High | Ransomware operator uses the integrator remote tool at an acquired farm to reach ROC SCADA and the corporate network | Remove the tool; integrator sessions only through group PAM on request with named accounts and MFA | Crop Farming OT security manager | 2026-11-15 |
| CF-002 | High | Attacker takes over the legacy farm operations directory and controls all ROC HMIs and SCADA servers | Administrators under group PAM with MFA; directory logs to the SIEM; reduce administrators to 4 | Crop Farming OT security manager | 2026-12-31 |
| CF-003 | High | Freeze protection fails on a freeze night because ROC-1 SCADA is encrypted or unavailable | Written and drilled manual procedure at all ROC-1 farms by 2026-11-15; warm standby at ROC-2 by 2027-06-30 | Crop Farming VP Irrigation and Field Technology | 2027-06-30 |
| CF-004 | High | Attacker on the corporate cloud network reaches ROC SCADA through the farm data hub | OT DMZ at each ROC; hub reads DMZ replicas only | Crop Farming OT security manager | 2026-11-30 |

**CF-001 is the only Very High risk in the group.** The integrator's always-on remote tool, with one shared account and no MFA, is a common ransomware entry path, and through the shared farm operations directory it reaches ROC SCADA at all three centers, including ROC-1, which runs freeze protection for every strawberry block. Only the board risk committee may accept a Very High risk; it did not. On 2026-09-10 it approved the treatment plan and an interim measure: from 2026-09-14 the remote tool is switched off at each acquired farm server and turned on only for a scheduled window approved by the ROC lead, until group PAM replaces it (POAM-001, due 2026-11-15).

### Other division risks rated High
| Risk ID | Division | Level | Risk | Owner | Due |
|---|---|---|---|---|---|
| FP-001 | Food Processing | High | Attacker or insider changes PLC setpoints or recipes (for example blanching temperature or metal detector reject settings) and adulterated product ships | Food Processing VP Food Safety and Quality | 2027-03-31 |
| FP-002 | Food Processing | High | Compromise of ammonia refrigeration controls causes a release or loss of cold storage | Food Processing plant OT security manager | 2026-12-31 |
| FS-005 | Farm Supply | High | Grower credit files with Social Security numbers and personal guarantees are stolen | Farm Supply credit director | 2026-11-30 |

**Two passes.** Pass 1 was completed on 2026-07-31 from intake and fieldwork evidence, including the P07 common control tests run in July (for example the 1,140 seasonal accounts, EV-C-AC2, and the default credentials on sampled modems, EV-C-IA5). P07 testing continued to 2026-08-31; it confirmed existing risks and added none, so every risk in the four registers is Pass 1 (`assessment_pass`). Later test findings were tracked in the POA&M and linked to the risks they affect (`related_risk_ids`).

### What the results say
The corporate program is sound: a 24x7 SOC, PAM for IT, MFA for the workforce, immutable backups, and a PCI DSS-validated card environment. The High risks cluster where **corporate IT meets division OT** and where **one incident crosses divisions**:
1. **The path from third-party access and the corporate cloud into farm OT** (GR-01, GR-12; CF-001, CF-002, CF-004; EV-020, EV-037, EV-038).
2. **Manipulation of process controls with safety or food safety consequences** (GR-02, GR-06; CF-003, FP-001, FP-002; EV-057, EV-058, EV-061).
3. **Controls the division assumes it inherits but does not** (GR-04, Moderate at group level; EV-018, EV-008). It is Moderate only because the group SOC and EDR still cover farm IT; it explains why P07 sampled farm OT heavily.

Seasonal identity (GR-05), traceability under outage (GR-07), the notification matrix (GR-03), and AI governance (GR-08, GR-09) are Moderate at group level. Each has a dated plan because each one would make a High risk worse during a real incident.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** integrator access through group PAM and an OT DMZ at each ROC (GR-01); farm directory under PAM (GR-12); OT monitoring and vulnerability management at all 38 farms (GR-04); ROC-1 warm standby (GR-17, CF-003); cyber scenarios in food defense reanalysis (GR-06).
- **Avoided:** CF-009 (H-2A onboarding exports purged from the farm data hub on 2026-07-28 and the export job removed).
- **Accepted (15, all Low or Very Low):** GR-18, GR-19, CF-013, CF-022, CF-025, CF-027, CF-030, FP-008, FP-016, FP-017, FS-010, FS-011, FS-013, FS-017, FS-018.
- **Contract actions:** security schedule for the irrigation integrator (CF-028); buyer, customer, and cooperative notice rows in the P08 matrix (CF-019, FP-009, FS-007).
- **Treatment status:** 49 risks are In progress, 21 are Open (treatment approved, work not started), and 16 are Closed (accepted or avoided).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks and CF-001 were presented on 2026-09-10. The Reg S-K Item 106 description in the next annual report draws on this process (board risk committee oversight, the Group CISO's reporting line, and the use of an outside OT assessment firm).

## 6. Approval
- Board risk committee: approved the group register, the High group treatment plans, the CF-001 interim measure, and the funding request, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the High division risks, 2026-09-10.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-10.
- Next full review: May to July 2027 (off-season), or sooner after a major change, acquisition, or incident.

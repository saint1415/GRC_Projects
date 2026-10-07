# Risk Register Report: Cris Santos Company Holdings | Defense Industrial Base | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Manufacturing (Defense Industrial Base), Professional Services, Information) |
| Focus division | Aircraft Parts (NAICS 336413), a DoD prime contractor and subcontractor handling CUI |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | SP 800-171 Rev. 2 requirement 3.11.1 (periodic risk assessment) for the Enterprise CUI Environment; the risk basis for the Reg S-K Item 106 description of risk management |
| Registers | `risk-register.csv` (group), `risk-register-aircraft-parts.csv`, `risk-register-engineering-services.csv`, `risk-register-defense-software.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-15 by the board audit and risk committee (group register and all High risks); division presidents approved their Moderate treatments and acceptances the same week |

## 1. Scope and risk framing
**Scope.** Every system that processes, stores, or transmits CUI, FCI, export-controlled data, or Government data in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud, SYS-G4 ERP, and SYS-G5 CUI collaboration. Division systems are SYS-D1 to SYS-D5 and the GCEE (`../00_company-facts.md` section 3). Classified systems at the two cleared Engineering Services centers are out of scope; spillage and reporting risks that touch them are included.

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Aircraft Parts, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact. They are not simply the highest division rating.

**Risk tolerance and who can accept risk** (POL-01 4.4; added to `../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board audit and risk committee; temporary only, with a dated plan |
| Very High | Board audit and risk committee only |

Two kinds of risk rated High may not be accepted at all; they must be treated: risks that could put a nonconforming part on an aircraft, and risks of unauthorized export of ITAR or EAR technical data.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, DoD and CISA advisories on targeting of the defense industrial base, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: loss of award eligibility across many contracts, several regulators and primes at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 6 | 12 | 3 | 0 | 21 | n/a |
| Aircraft Parts | 0 | 5 | 16 | 9 | 0 | 30 | 22 |
| Engineering Services | 0 | 2 | 9 | 7 | 0 | 18 | 13 |
| Defense Software | 0 | 2 | 10 | 7 | 0 | 19 | 12 |
| **All registers** | **0** | **15** | **47** | **26** | **0** | **88** | **47** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Nation-state actor steals CUI from the shared GCEE using stolen sessions or tokens | AP-001, AP-028, ES-001, ES-016 | Phishing-resistant MFA for all GCEE users; per-project download baselines; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-02 | Ransomware spreads from plant OT or the Plant 9 legacy network to several plants | AP-002, AP-003, AP-004, AP-005, AP-007 | Plant 9 isolation and migration; device control; plant logs in the SIEM; MES restore tests | Group CISO | 2027-03-31 |
| GR-04 | The group cannot show Level 2 (C3PAO) status when Phase 2 solicitations require it | AP-010, AP-013, AP-030, ES-004, DS-019 | Close non-POA&M-eligible and multi-point requirements by 2026-11-30; C3PAO window 2026-12-07 | Group CMMC program director | 2026-12-18 |
| GR-05 | Sister-division CSP (SYS-D4) holds CUI without FedRAMP Moderate equivalency | AP-009, DS-001, DS-008 | Close 3PAO findings; authorization path; tenant notices; Aircraft Parts moves its CUI to the GCEE meanwhile | Defense Software president | 2027-06-30 |
| GR-08 | An insider takes CUI or export-controlled data before leaving | AP-012, ES-008 | Departure-risk feed to the SOC; notice-period download alerts | Group ITPSO | 2027-03-31 |
| GR-10 | CUI pasted into public AI services or exposed by an AI assistant with broad access | AP-024, ES-006, DS-009, DS-010 | Group AI governance program (P10) | Group Chief Risk Officer | 2027-03-31 |

### Aircraft Parts (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| AP-001 | Attacker steals an engineer session and downloads Aircraft Parts drawings and models from the GCEE | Phishing-resistant MFA; per-project download baselines (GR-01) | Aircraft Parts security and compliance lead | 2027-03-31 |
| AP-002 | Ransomware encrypts MES and DNC servers at several plants | Plant logs to the SIEM; segment plants 6 and 8; quarterly MES restore tests | Aircraft Parts VP of operations | 2027-03-31 |
| AP-003 | The Plant 9 legacy network is compromised and its 6,000 CUI drawings taken or encrypted | Migrate into the GCEE; interim MFA and FIPS-mode VPN; no new Phase 2 CUI work at Plant 9 | Aircraft Parts VP of operations | 2027-03-31 |
| AP-009 | Aircraft Parts stores sustainment CUI in SYS-D4 without equivalency evidence | Stop the export; move the data into the GCEE | Aircraft Parts VP of supply chain | 2026-11-30 |
| AP-010 | The Aircraft Parts portion of the scope is not ready for the C3PAO assessment | Close all non-POA&M-eligible and multi-point requirements | Aircraft Parts president | 2026-11-30 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| ES-001 | Engineering Services | A phished field engineer's single sign-on session is used to take GCEE and prime-tenant data | Engineering Services security and compliance lead | 2026-12-31 |
| ES-006 | Engineering Services | Engineers paste CUI into public AI chatbots | Engineering Services security and compliance lead | 2026-11-30 |
| DS-001 | Defense Software | Contractor customers store CUI in SYS-D4 without FedRAMP Moderate equivalency | Defense Software president | 2027-06-30 |
| DS-002 | Defense Software | A tenant isolation defect exposes one contractor tenant's CUI to another | Defense Software VP of engineering | 2027-03-31 |

### What the results say
The program is mature in its core: there are no Very High risks, and identity, encryption, the 24x7 SOC, backups, and export gating are in place. The High risks cluster around **what the group shares and where it has grown**, not around any one division's basics:
1. **The shared GCEE** (GR-01) concentrates many programs' CUI. Its controls are strong, but one stolen session reaches two divisions' data and, through single sign-on, prime tenants in SYS-D4.
2. **Edges of the estate** (GR-02, GR-11): the acquired Plant 9, plant OT, and USB loading are where common controls stop.
3. **Intercompany services are treated as trusted by default** (GR-05): the Aircraft Parts division uses its sister division's cloud service for CUI without the CSP evidence it would demand from a vendor.
4. **Timing** (GR-04): Phase 2 starts on 2026-11-10 and the C3PAO window is in December. The Enterprise CUI Environment scores 79 under 32 CFR 170.24 today (P03).
5. **AI** (GR-10): public chatbot use with CUI was observed in 2026, before the Group AI Standard existed.

The governance gaps (supplement drift, GR-13; undocumented inheritance, GR-14) are Low and Moderate at group level. They matter because they hide whether Engineering Services controls operate, which is why P07 sampled Engineering Services governance controls.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** phishing-resistant MFA for all CUI users (GR-01); Plant 9 migration and plant logging (GR-02); CMMC readiness sprint to the C3PAO window (GR-04); SYS-D4 FedRAMP Moderate path (GR-05); supplier status verification (GR-06); group AI governance program (GR-10); Program H Level 3 readiness (GR-12).
- **Accepted (7):** 5 Low (AP-016 printed drawings at cells, AP-021 carrier outage at plants 1 to 8, ES-013 lost encrypted laptop, ES-017 HPC outage, DS-014 maintainer contact data) and 2 Moderate accepted by division presidents (AP-026 hurricane at the Florida plants, DS-016 tenant key compromise).
- **Contract and disclosure actions:** written status notices to SYS-D4 CUI tenants and withdrawal of unsupported marketing claims (DS-001, DS-008); disclosure to DoD edition Contracting Officers about the 2026-05 data reuse as counsel advises (DS-003, GR-18); re-paper 46 Engineering Services subconsultant agreements (ES-012).
- **Treatment status:** 76 risks are In progress, 5 are Open (treatment approved, work not started), and 7 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board audit and risk committee each quarter. The six High group risks were presented on 2026-09-15. CMMC award eligibility (GR-04) is also tracked as a business risk by the chief financial officer because Phase 2 can affect revenue recognition on new defense awards. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the committee's oversight and the Group CISO's reporting line).

## 6. Approval
- Board audit and risk committee: approved the group register, the six High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the nine High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-11 to 2026-09-15.
- Next full review: May to July 2027, after the C3PAO assessment, or sooner after a major change, acquisition, or incident.

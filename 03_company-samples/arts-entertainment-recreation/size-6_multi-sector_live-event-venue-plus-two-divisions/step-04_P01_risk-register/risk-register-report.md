# Risk Register Report: Cris Santos Company Holdings | Arts, Entertainment, and Recreation | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Arts, Entertainment, and Recreation, Accommodation and Food Services, Information) |
| Focus division | Live Venues (NAICS 711310), a PCI DSS Level 1 merchant |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | PCI DSS v4.0.1 Requirement 12.3 (risk assessment and targeted risk analyses) for all three PCI roles in the group (N71-R04, N72-R01); the risk management process described under Reg S-K Item 106 (N51-R08) |
| Registers | `risk-register.csv` (group), `risk-register-live-venues.csv`, `risk-register-hotels-restaurants.csv`, `risk-register-ticketing-streaming.csv` |
| Fieldwork | 2026-05-01 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that stores, processes, or transmits card data or patron, guest, or subscriber data in the three divisions, plus the corporate shared services they depend on: the group identity platform (SYS-G1), the group SOC (SYS-G2), the group cloud platform and WAN (SYS-G3), and the patron data platform (SYS-G4). Division systems are SYS-D1 to SYS-D4 (`../00_company-facts.md` section 3). The 8 acquired theaters are in scope even though they are not yet on group systems.

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Live Venues, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services or the shared ticketing platform, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back. Group risks are rated on their own group-level likelihood and impact, not on the highest division rating.

**Risk tolerance and who can accept risk** (also in `../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Crowd-safety and guest-safety risks rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), the 2026 service provider ROC, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: card brand investigations across three PCI roles, client contract exposure across 1,150 clients, several regulators at once, and SEC disclosure.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service or the shared ticketing platform, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 6 | 13 | 1 | 0 | 20 | n/a |
| Live Venues | 0 | 3 | 15 | 12 | 0 | 30 | 17 |
| Hotels and Restaurants | 0 | 2 | 11 | 5 | 0 | 18 | 12 |
| Ticketing and Streaming | 0 | 2 | 12 | 6 | 0 | 20 | 11 |
| **All registers** | **0** | **13** | **51** | **24** | **0** | **88** | **40** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Card and patron data skimmed from the hosted checkout through a tenant-added tag or a script vendor | LV-001, HO-006, TS-001, TS-014 | Block tenant tags in checkout; script inventory and authorization; tamper detection for every tenant; assess script vendors | General Manager Ticketing | 2026-11-30 |
| GR-02 | Ransomware spreads through shared services and halts venues, hotels, and ticketing | LV-006, HO-002, TS-005 | Segment hotel networks; acquired theaters under EDR and the WAN; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-04 | AI pricing and access decisions harm patrons or breach fee, accessibility, or fairness rules | LV-003, HO-008, TS-003, TS-011 | Group AI program (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-09 | Card data captured at card-present channels outside validated P2PE (acquired theaters and hotel front desks) | LV-002, LV-005, LV-024, LV-026, HO-001 | Interim segmentation and EDR; validated P2PE devices; theater migration | Group PCI program director | 2027-03-31 |
| GR-10 | Patron data on the patron data platform used or exposed beyond its purpose | HO-007, TS-008, LV-030 | Stop and purge identity numbers; filter the training feed by contract; one purpose register | Group Chief Privacy Officer | 2027-03-31 |
| GR-11 | Advertised ticket and room prices omit mandatory fees | LV-004, HO-005 | Total price in every display and channel feed; pre-publication checks | Group General Counsel | 2026-10-31 |

### Live Venues (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| LV-001 | Skimming script on group venue checkout pages through one of 23 tenant-added tags | Remove all tenant tags from checkout; approved tag list for event pages only | Live Venues security and compliance lead | 2026-10-31 |
| LV-002 | POS malware captures card data at the 8 acquired theaters | Interim segmentation and EDR; validated P2PE devices; migration to the TVOP | VP Ticketing and Box Office | 2027-03-31 |
| LV-004 | Venue websites and emails advertise ticket prices without mandatory fees | Total price in all displays; pre-publication check | Live Venues marketing director | 2026-10-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| HO-001 | Hotels and Restaurants | POS malware captures card data from front desk terminals that are not P2PE | Director of Hotel Technology | 2027-03-31 |
| HO-005 | Hotels and Restaurants | Advertised room rates exclude the mandatory resort fee in some channels | VP Revenue Management | 2026-10-31 |
| TS-001 | Ticketing and Streaming | A tenant-added tag on any tenant's checkout skims card data | Chief Technology Officer | 2026-11-30 |
| TS-014 | Ticketing and Streaming | A script vendor is compromised and serves malicious code on checkout | Chief Technology Officer | 2026-11-30 |

### What the results say
The program is defined and mostly sound. There are no Very High risks. Identity, monitoring, backups, tokenization, and P2PE at the integrated venues all work, and the ticketing platform holds a current service provider AOC. The High risks cluster around **what the group shares and what it has not yet absorbed**:
1. **The shared checkout** (GR-01). One platform serves three internal merchant roles and 1,150 clients, and the checkout trusts code that tenants and script vendors control (group gap 1). This is the scenario of the P08 runbook.
2. **Card-present channels outside P2PE** (GR-09). The acquired theaters and the hotel front desks are the group's remaining card data on its own networks (gap 2).
3. **Data and pricing practices** (GR-10, GR-11, GR-04). The patron data platform takes more data than its uses need (gap 3), price displays outside the checkout omit fees, and the pricing and bot modules run without group AI approval (gap 4). These are FTC Act and fee rule exposures, not only security ones.
4. **Shared-service incidents** (GR-02, and the Moderate risk GR-03) would trigger client, card brand, state, and SEC duties at once (gap 5).

Governance gaps 6 and 7 (undocumented hotels inheritance and drifted hotels standards) are Moderate at group level (GR-06, GR-05). They matter because they hide whether hotel controls actually operate, which is why P07 sampled Hotels and Restaurants more heavily.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q1):** checkout tag isolation and script controls (GR-01); P2PE devices at the acquired theaters and hotel front desks, and theater migration (GR-09); patron data platform minimization (GR-10); group AI governance program (GR-04); SIEM onboarding of the hotel PMS (GR-12).
- **Accepted (all Low):** LV-028 (lost scanner with an encrypted manifest), LV-029 (broadcast feed drop), HO-018 (guest register loss in a PMS change, covered by vendor backups), TS-020 (engineer production access, covered by PAM).
- **Contract actions:** client agreement amendments for data use and notice terms (GR-16, GR-03); script vendor and channel manager terms (GR-13); seller's ticketing vendor AOC for the acquired theaters (LV-005).
- **Treatment status:** 55 risks are In progress, 29 are Open (treatment approved, work not started), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The six High group risks were presented on 2026-09-15. The Reg S-K Item 106 description in the next annual report draws on the governance described here (GR-15 tracks reconciling that description with the 2026 assessment results).

## 6. Approval
- Board risk committee: approved the group register, the six High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the seven High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-10 to 2026-09-15.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.

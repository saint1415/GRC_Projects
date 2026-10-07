# Risk Register Report: Cris Santos Company Holdings | Nuclear Reactors, Materials, and Waste | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Nuclear Generation, Engineering and Radiation Services, Radioactive Waste Management) |
| Focus division | Nuclear Generation (NAICS 221113), 3 stations and 5 units under 10 CFR Part 50 operating licenses |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | "Evaluate and manage cyber risks" for the business-network side of each station's cyber security program (10 CFR 73.54(d)(2)); the waste division's annual Part 37 program review input (37.55) |
| Registers | `risk-register.csv` (group), `risk-register-nuclear-generation.csv`, `risk-register-engineering-radiation-services.csv`, `risk-register-waste-management.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses); NG-024 added 2026-08-28 from the P07 assessment |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads and the fleet cyber security program manager |
| Approved | 2026-09-17 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every business system and process in the three divisions, plus the corporate shared services they depend on (SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network). Division systems are listed in `../00_company-facts.md` section 3.

**What is not scored here.** Risks to the CDAs themselves are managed inside each station's cyber security plan (CSP), through the CSP's own vulnerability assessments and the station corrective action program (CAP). This register scores the business-side risks that could **reach** CDAs (the kiosk update path, cross-division access, CDA information in business systems) and the business, regulatory, and safety consequences of business-system failures. Where a risk is also a CSP deficiency, it was entered in the station CAP within 24 hours of discovery, as 73.77(b)(1) requires, and the register says so.

**Two levels of register.**
- **Division registers** hold risks a division owns and can treat itself. Nuclear Generation, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back. Group risks are rated on their own group-level likelihood and impact, not on the highest division rating.

**Risk tolerance and who can accept risk** (in `../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president (the Chief Nuclear Officer for Nuclear Generation), with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

**Nuclear limit on acceptance.** A risk that is a deficiency in a station CSP, or that could affect nuclear safety or worker safety, cannot be accepted. It must be entered in the station CAP and corrected. None of the three accepted risks is of that kind.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the BIA (P05), the gap analyses (P03), the common control assessment (P07), operating experience shared through industry groups, and interviews with each division's leadership and each station's CST.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**. For CDA-adjacent risks, "adverse impact" means the attack would get past the business network to something the CSP protects; the one-way devices are why many of those ratings are Moderate rather than High.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Very High is reserved for outcomes that could affect nuclear safety, security, or emergency preparedness functions, a Part 37 category 2 quantity, or several divisions and regulators at once.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results
| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 13 | 3 | 0 | 20 | n/a |
| Nuclear Generation | 0 | 5 | 17 | 8 | 0 | 30 | 17 |
| Engineering and Radiation Services | 0 | 2 | 9 | 5 | 0 | 16 | 12 |
| Radioactive Waste Management | 0 | 2 | 9 | 5 | 0 | 16 | 9 |
| **All registers** | **0** | **13** | **48** | **21** | **0** | **82** | **38** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Cross-division identity or laptop used to enter a station business network and move toward CDA-adjacent systems | NG-001, NG-002, NG-015, ER-001, WM-008 | Assignment-bound access; contractor segment with device check; same-day removal | Group CISO | 2027-03-31 |
| GR-02 | Kiosk update path compromised to deliver malware toward CDAs | NG-003, NG-004 | Signature verification; restricted segment; replace Station B kiosk OS | Fleet cyber security program manager | 2026-11-30 |
| GR-03 | Ransomware through shared services halts outage work, dosimetry, and waste operations | NG-010, ER-005, WM-005 | Cross-division restore tests; WMS failover test; tiered admin; tabletop | Group CISO | 2027-03-31 |
| GR-04 | CDA details or SGI in business systems exposed to an adversary | NG-005, NG-006, NG-024, NG-026, ER-002, ER-003, ER-008 | Restricted CDA module and label; SGI marking scan; need-to-know determinations; reproduction equipment re-evaluation | Fleet security director | 2026-12-31 |

### Nuclear Generation (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| NG-001 | Phished cross-division engineer's identity used on station file shares and the WMS | Token protection; assignment-bound access; station-only roles | Fleet IT director | 2027-03-31 |
| NG-003 | Tampered kiosk update passes malicious files toward CDAs | Signature verification; restricted segment; CST release step (CAP entry made) | Fleet cyber security program manager | 2026-11-30 |
| NG-005 | CDA work packages exfiltrated from the WMS for attack planning | Restricted CDA module; label; bulk download alerts | Work management director | 2026-12-31 |
| NG-010 | Ransomware on station file servers and the WMS during a refueling outage | Segment server subnets; WMS failover test; outage drill | Fleet IT director | 2027-03-31 |
| NG-024 | Station security building printers with default admin passwords, used to copy SGI (**new, from P07**) | Change passwords; stand-alone copier for SGI; wipe storage (CAP entry made) | Fleet security director | 2026-10-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| ER-001 | Engineering and Radiation Services | Phished engineer's credentials used to reach group and client station networks | Engineering and Radiation Services security and compliance lead | 2027-03-31 |
| ER-004 | Engineering and Radiation Services | Contractor/vendor access authorization files for about 2,900 workers stolen from project shares (73.56(m)) | Contractor/vendor access authorization program manager | 2026-11-30 |
| WM-001 | Radioactive Waste Management | Attack on the Florida facility business network takes down vault PACS and intrusion detection (37.49) | Florida facility Radiation Safety Officer | 2026-12-31 |
| WM-003 | Radioactive Waste Management | Vendor remote access to processing PLCs without MFA abused | Radioactive Waste Management OT lead | 2026-11-30 |

### What the results say
There are no Very High risks, because the reactors' safety and security functions sit behind the CSP defensive architecture and the one-way devices. The High risks cluster around **what the divisions share**, not around any one division's basics:
1. **People and devices that cross divisions** (GR-01). Engineering and waste staff are station users through one group identity, on laptops the stations do not manage (scenario gap 1). That is the entry path used in the P08 scenario.
2. **The few business-side paths that touch CSP controls** (GR-02). The kiosk update server is ordinary infrastructure doing a CDA-protection job (scenario gap 3).
3. **Information about CDAs and SGI outside the places built for it** (GR-04): work packages, attachments, printers, and an engineering office scanner (scenario gaps 2 and 4, plus the P07 finding).
4. **Shared-service ransomware** (GR-03), which would hit outage work, dosimetry, and waste operations together.

Notification (GR-05) is Moderate on its own, but it decides how the regulators see every High risk: the group has never practiced deciding a 73.77 clock for a business-network event, and the matrix does not yet show that a report to the FBI starts one (scenario gap 8).

**Back from P07.** Testing in August found 6 multifunction printers in the Station A and B security buildings with manufacturer default admin passwords. They were networked and had been used to copy SGI, which 73.22(e) requires to be done only on equipment evaluated so that unauthorized people cannot reach retained images or the network. The finding became NG-024 (High) and POAM-002, was entered in the station CAP, and rolls up to GR-04 and GR-17.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** cross-division access redesign (GR-01); kiosk update path hardening (GR-02); restore and failover testing (GR-03); CDA information and SGI controls in business systems (GR-04); multi-regulator matrix and tabletop (GR-05); group AI program (GR-08).
- **Accepted (all Low):** NG-028 (rogue Wi-Fi, covered by wireless intrusion detection), NG-029 (encrypted laptop theft), WM-015 (driver background report disposal, covered by the shredding contract).
- **CAP entries made** for CSP-related items: NG-003, NG-004, NG-024. The CAP, not this register, is the record of correction for the CSP.
- **Contract actions:** end-of-assignment notices in intercompany service agreements (GR-01); a second background investigation vendor (ER-012); MFA terms for dosimetry customers (ER-006).
- **Treatment status:** 45 risks are In progress, 34 are Open (treatment approved, work not started), and 3 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-17. The Regulation S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight, the Group CISO's reporting line, and the separate NRC-inspected cyber security programs at the stations).

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-17.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the nine High division risks, 2026-09-17.
- Division presidents (including the Chief Nuclear Officer): approved Moderate and Low treatments and the three acceptances, 2026-09-14 to 2026-09-17.
- Next full review: May to July 2027, or sooner after a major change, an outage-season lesson, or an incident.

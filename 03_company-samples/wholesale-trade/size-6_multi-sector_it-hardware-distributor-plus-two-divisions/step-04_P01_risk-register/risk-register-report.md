# Risk Register Report: Cris Santos Company Holdings | Wholesale Trade | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Wholesale Trade, Transportation and Warehousing, Retail Trade) |
| Focus division | IT Distribution (NAICS 423430), including Federal Solutions (DoD CUI work) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | SP 800-171 Rev. 2 requirement 3.11.1 (periodic risk assessment) for the CUI environment; the risk assessment element of the PCI DSS program (Online Retail) |
| Registers | `risk-register.csv` (group), `risk-register-it-distribution.csv`, `risk-register-logistics.csv`, `risk-register-online-retail.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-15 by the board audit and risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that supports ordering, fulfillment, payments, federal work, and DC operations in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud, SYS-G4 ERP, SYS-G5 EDI hub, and SYS-G6 data platform. Division systems are SYS-D1 to SYS-D10 (`../00_company-facts.md` section 3).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. IT Distribution, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not as the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board audit and risk committee; temporary only, with a dated plan |
| Very High | Board audit and risk committee only |

Risks that could lead to worker injury (DC automation) or to covered or tampered equipment reaching a DoD system may not be accepted at High. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the BIA (P05), the gap analyses (P03), the common control assessment (P07), supply chain incidents seen in 2025 and 2026, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Group impact reflects enterprise consequences: several customers or regulators at once, loss of DoD eligibility, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 5 | 11 | 4 | 0 | 20 | n/a |
| IT Distribution | 0 | 3 | 12 | 9 | 0 | 24 | 15 |
| Logistics | 0 | 2 | 10 | 4 | 0 | 16 | 11 |
| Online Retail | 0 | 2 | 9 | 4 | 0 | 15 | 10 |
| **All registers** | **0** | **12** | **42** | **21** | **0** | **75** | **36** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Tampered or counterfeit products enter distribution through a compromised or dishonest supplier | ID-003, ID-004, LW-005, OR-004, OR-006 | Serial validation at all 9 DCs; broker assessments; firmware checks at receiving; product-integrity playbook (P08) | Group supply chain risk director | 2027-03-31 |
| GR-02 | Ransomware spreads through shared services and stops fulfillment in every division | LW-004, ID-010 | WMS ransomware recovery test including the replica; segmentation; isolated recovery account | Group CISO | 2027-03-31 |
| GR-03 | CUI is exposed or mishandled outside the Federal Fulfillment Enclave | ID-001, ID-002, ID-012 | Purge and block CUI outside the FFE; DLP on CUI markings; close the IC-2 route | Group CMMC program director | 2026-12-15 |
| GR-10 | Consumer payment or personal data is stolen from Online Retail | OR-001, OR-002, OR-015 | Script controls on all brands; stop recording card data; web application testing | Online Retail president | 2026-12-31 |
| GR-11 | DC automation is compromised or disrupted, stopping automated DCs and risking worker injury | LW-001, LW-002, LW-003 | PAM-brokered vendor access; OT segmentation and monitoring; PLC backups in the vault | Logistics vice president of operations | 2027-06-30 |

### IT Distribution (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| ID-001 | CUI in commercial ERP attachments and the commercial collaboration tenant is exposed | Purge; attachment block; DLP; prime exchange in the government-community tenant | Federal Solutions vice president | 2026-11-30 |
| ID-003 | Devices with tampered firmware are configured and shipped to a DoD installation | Signature verification from OEM sources only; serial provenance for every job | Integration center managers | 2026-12-31 |
| ID-007 | The 2025 SPRS score is unsupported for the full CUI environment | Re-assess the full scope; post a corrected score on counsel advice | Group CMMC program director | 2026-11-30 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| LW-001 | Logistics | Persistent vendor tunnel used to alter PLC logic | Logistics OT engineering manager | 2026-12-31 |
| LW-004 | Logistics | The single WMS instance fails or is encrypted, stopping all 9 DCs | Logistics vice president of operations | 2027-03-31 |
| OR-001 | Online Retail | Payment page script skims card data | Online Retail PCI compliance manager | 2026-11-15 |
| OR-015 | Online Retail | Web application flaw exposes the consumer account database | Online Retail chief digital officer | 2027-03-31 |

### What the results say
There are no Very High risks, and the common controls (identity, SOC, cloud guardrails, backups) carry little risk on their own. The High risks cluster around **what the divisions share physically and contractually**:
1. **Product integrity crosses every division** (GR-01). Logistics receives for everyone, so one weak receiving dock lets tampered stock reach DoD jobs, resellers, and consumers (scenario gaps 2 and 3).
2. **CUI leaks around a sound enclave** (GR-03, ID-001, ID-007). The FFE design is solid; the problem is people and process putting CUI in commercial systems, which also undermines the 2025 SPRS score (gap 1).
3. **One WMS and unmonitored DC automation** (GR-02, GR-11) make Logistics the group's operational single point of failure (gaps 6 and 7).
4. **Online Retail's card and consumer data** (GR-10) is well scoped but leaks at payment page scripts and in call recordings (gap 4).

Governance gaps (Logistics inheritance, supplement drift, AI governance, notification readiness) are Moderate at group level (GR-05, GR-06, GR-07, GR-09). They matter because they hide whether Logistics controls actually operate, which is why the P07 assessment sampled Logistics more heavily.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** CUI containment and CMMC readiness (GR-03, GR-04); receiving serial validation at 5 DCs and broker assessments (GR-01); WMS ransomware recovery design (GR-02); OT segmentation, monitoring, and vendor access through PAM (GR-11); payment page script controls and contact center recording fix (GR-10).
- **Accepted (all Low):** ID-024 (software license key theft), LW-013 (telematics outage, covered by the paper procedure), OR-014 (bot purchases of limited releases).
- **Contract actions:** DFARS 252.246-7008 terms for brokers (ID-014); recovery objectives in ERP and TMS renewals (GR-08); secure file exchange with customs brokers (LW-009).
- **Treatment status:** 42 risks are In progress, 30 are Open (treatment approved, work not started), and 3 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board audit and risk committee each quarter. The five High group risks were presented on 2026-09-15. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the committee's oversight and the Group CISO's reporting line).

## 6. Approval
- Board audit and risk committee: approved the group register, the five High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the seven High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments for their divisions, 2026-09-14 to 2026-09-15; the three Low acceptances were approved by the division security and compliance leads on 2026-08-20.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.

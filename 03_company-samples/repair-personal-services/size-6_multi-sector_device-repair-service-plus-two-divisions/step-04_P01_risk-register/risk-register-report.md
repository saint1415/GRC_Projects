# Risk Register Report: Cris Santos Company Holdings | Other Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Other Services, Retail Trade, Professional Services) |
| Focus division | Device Repair (NAICS 811210), a national repair chain |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | PCI DSS v4.0.1 Requirement 12.3.1 targeted risk analyses for both merchants (inputs); the risk analysis IT Support needs as a HIPAA business associate, 45 CFR 164.308(a)(1)(ii)(A) |
| Registers | `risk-register.csv` (group), `risk-register-device-repair.csv`, `risk-register-electronics-retail.csv`, `risk-register-it-support.csv` |
| Fieldwork | 2026-05-01 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-10 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that creates, receives, maintains, or transmits customer personal information, customer device content, card data, or managed customers' data in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and colocation, SYS-G4 customer engagement platform, and SYS-G5 ERP and HR. Division systems are SYS-D1 to SYS-D5 (`../00_company-facts.md` section 3).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Device Repair, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact. They are not simply the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks that would expose customers' device content or card data at scale may not be accepted at High. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the cloud mapping (P04), the SSP control gaps (P02), the internal PCI DSS pre-assessments, the common control assessment (P07), customer complaint data, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Group impact reflects enterprise consequences: two merchants at once, manufacturer and TPA contracts, managed customers' own breaches, and SEC disclosure.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 5 | 11 | 4 | 0 | 20 | n/a |
| Device Repair | 0 | 4 | 18 | 8 | 0 | 30 | 21 |
| Electronics Retail | 0 | 2 | 7 | 9 | 0 | 18 | 8 |
| IT Support Services | 0 | 3 | 10 | 5 | 0 | 18 | 11 |
| **All registers** | **0** | **14** | **46** | **26** | **0** | **86** | **40** |

17 of the 20 group risks roll up division risks. GR-08 (workforce phishing), GR-14 (SEC materiality), and GR-20 (regulatory change) are group-only risks.

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Customer device content or data viewed, copied, or exposed at repair benches anywhere in the group | DR-002, DR-003, DR-021, IT-006 | Named bench accounts; session logging and USB block; cache wipe; signed access standard | Device Repair chief operating officer | 2027-03-31 |
| GR-02 | Attacker or malware moves from in-store counter benches into the retail cardholder data environment | DR-004, ER-001 | Separate counter networks at 112 stores; segmentation tests every 6 months | Electronics Retail CISO with the Device Repair CISO | 2026-11-15 |
| GR-03 | Compromised RMM or remote support account pushes malicious scripts to managed customers | IT-001, IT-002, IT-003 | Break-glass only; phishing-resistant MFA; two-person script approval | IT Support security and compliance lead | 2026-12-31 |
| GR-04 | Compromised third-party tool update runs with administrator rights on group endpoints | DR-005, IT-003 | Tool review gate; signed updates through the group channel; allow-listing | Device Repair CISO | 2027-03-31 |
| GR-05 | Passcodes and account credentials kept in group systems exposed in bulk | DR-001, DR-027, IT-007, IT-014 | Vault everywhere; purge notes, transcripts, and attachments; stop collecting account passwords | Group Chief Privacy Officer | 2027-01-31 |

### Device Repair (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| DR-001 | Passcodes and account passwords in ticket notes read or exported | Vault at all stores; purge notes back to 2018; stop collecting account passwords | STPP product owner | 2027-01-31 |
| DR-002 | Technician views or copies personal content from a customer device | Session logging and USB block at all benches; approved test apps; customer-visible repair mode | Device Repair chief operating officer | 2027-03-31 |
| DR-004 | Malware on an in-store counter bench reaches retail POS lanes | Separate counter networks; joint test with Retail | Device Repair CISO with the Electronics Retail CISO | 2026-11-15 |
| DR-005 | Compromised bench tool update runs malicious code | Tool review gate; signed updates; allow-listing; remove administrator rights | Device Repair CISO | 2027-03-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| ER-001 | Electronics Retail | Memory-scraping malware reaches POS lanes through a connected network | Electronics Retail CISO | 2026-11-15 |
| ER-002 | Electronics Retail | Checkout scripts tampered with to skim card data | Electronics Retail chief digital officer | 2026-11-30 |
| IT-001 | IT Support | Compromised RMM account deploys ransomware to managed customers | IT Support managed services director | 2026-12-31 |
| IT-002 | IT Support | Attacker phishes an RMM global administrator | IT Support security and compliance lead | 2026-12-31 |
| IT-007 | IT Support | Customer credential vault exposed | IT Support security and compliance lead | 2027-03-31 |

### What the results say
The program is sound where the group built it centrally. There are no Very High risks. Identity, the SOC, cloud guardrails, immutable backups, and the two PCI programs are in place, and ransomware across shared services rates Moderate at group level (GR-07) because of them. The High risks cluster in **what the group does with other people's devices and systems**:
1. **Customer devices on the bench** (GR-01, GR-04, DR-002, DR-005). Technicians can open customer devices with no record of what they did, and about 40 self-updating tools run as administrator on the same workstations (scenario gaps 2 and 5).
2. **Credentials the group should not keep** (GR-05, DR-001). About 2.1 million passcodes and 96,000 account passwords sit in ticket notes, and the chatbot and PSA hold more (gap 1).
3. **Where divisions touch** (GR-02). An in-store counter is a Device Repair bench on a Retail network; at 112 stores that network reached POS lanes (gap 3). This is the path the P08 exercise uses.
4. **Managed customers' endpoints** (GR-03). One RMM console reaches 310,000 endpoints, and the people who could misuse it were not protected well enough (gap 6).

AI governance (GR-10) and notification across divisions (GR-06) are Moderate at group level. They matter because each would turn a contained event into a regulatory or contractual failure, which is why P08 and P10 address them directly.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q1):** bench access and logging program (GR-01); passcode vault rollout and credential purge (GR-05); in-store counter network separation (GR-02); bench tool supply chain gate (GR-04); RMM privileged access redesign (GR-03); group AI governance program (GR-10).
- **Accepted (all Low):** GR-17, GR-20, DR-024, DR-025, DR-029, DR-030, ER-009, ER-011, ER-012, ER-013, ER-015, ER-016, ER-017, IT-013, IT-015, IT-017.
- **Contract actions:** vendor terms for bench tool vendors and the AI diagnostics provider (DR-005, DR-012); subcontractor business associate agreement for the AI agent's model provider (IT-010); TPA failover terms (DR-014).
- **Treatment status:** 55 risks are In progress, 15 are Open (treatment approved, work not started), and 16 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The five High group risks were presented on 2026-09-10. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line).

## 6. Approval
- Board risk committee: approved the group register, the five High group treatment plans, and the funding request, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the nine High division risks, 2026-09-10.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-10.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.

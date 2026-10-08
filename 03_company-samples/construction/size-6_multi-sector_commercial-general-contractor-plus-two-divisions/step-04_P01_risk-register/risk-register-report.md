# Risk Register Report: Cris Santos Company Holdings | Construction | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Construction, Real Estate, and Professional Services) |
| Focus division | Commercial Construction (NAICS 236220) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | The risk assessment expected by NIST SP 800-171 R2 requirement 3.11.1 for the CUI enclave, and the risk input to the CMMC Level 1 and Level 2 self-assessments |
| Registers | `risk-register.csv` (group), `risk-register-construction.csv`, `risk-register-property.csv`, `risk-register-ae.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that processes FCI, CUI, payment instructions, personal information, client facility security details, or building controls in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network, SYS-G4 ERP and payment factory, SYS-G5 email, SYS-G6 CUI enclave, and the PDPP (`../00_company-facts.md` sections 3 and 7).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Construction, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact. They are not simply the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

High risks to life safety (jobsite safety systems, building life-safety interfaces) and to federal contract eligibility may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment and enclave pre-assessment (P07), the 2026-07-14 CUI discovery scan, and interviews with each division's leadership and finance teams.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: loss of DoD eligibility, several regulators at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 5 | 12 | 3 | 0 | 20 | n/a |
| Construction | 0 | 4 | 19 | 7 | 0 | 30 | 24 |
| Property | 0 | 2 | 10 | 6 | 0 | 18 | 15 |
| A&E | 0 | 3 | 8 | 7 | 0 | 18 | 14 |
| **All registers** | **0** | **14** | **49** | **23** | **0** | **86** | **53** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | CUI is processed or stored outside the authorized enclave | CON-005, CON-006, AE-001, AE-003 | Remove the field release export; enclave desktops for superintendents; CUI upload block and purge in the PDPP; field CUI training | Group CISO | 2026-12-31 |
| GR-02 | Business email compromise redirects progress payments, subcontractor payments, or tenant rent across divisions | CON-001 to CON-004, CON-027, CON-028, PRP-003, PRP-005, AE-011 | Validated remittance block; Property AP into the payment factory; owner and tenant remittance letters; DMARC reject on property domains | Group Chief Financial Officer | 2027-03-31 |
| GR-03 | Loss of DoD contract eligibility because CMMC statuses are inaccurate or the enclave is not ready for Level 2 (C3PAO) | CON-007, CON-008, CON-029, AE-002, AE-018 | Counsel review of the March affirmation; close the requirements that cannot be on a POA&M; independent re-test | Group General Counsel | 2027-02-28 |
| GR-05 | Ransomware spreads through shared services and halts project delivery in several divisions | CON-013, AE-010 | Quarterly restore tests including the PDPP export; jobsite segmentation; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-06 | Compromise of owned-building systems disrupts tenants and life-safety interfaces at several properties | PRP-001, PRP-004, PRP-007, PRP-008, PRP-018 | Segment building networks; integrator access through group PAM; SIEM onboarding; credential reset | Property division president | 2027-06-30 |

### Construction (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| CON-001 | Attacker in a project executive's mailbox diverts an owner's pay application payment | Standing remittance letter to every owner; confirmation call on first payment to any account; validated remittance block | Construction VP of project controls | 2026-12-31 |
| CON-005 | CUI drawings from design-build projects stored in the PDPP and commercial email | Enclave desktops in trailers; purge and block (GR-01) | Construction security and compliance lead | 2026-12-31 |
| CON-008 | Construction cannot compete for DoD design-build work that requires Level 2 (C3PAO) or Level 2 (Self) (CMMC Phase 2 is suspended) | Close blocking requirements; C3PAO assessment in 2027-02 (GR-03) | Construction division president | 2027-02-28 |
| CON-015 | Attacker steals client system credentials from the TSSI vault and disables client security systems | Per-client vault partitions; credential rotation at handover; hardware-backed keys | Systems Integration Director | 2027-03-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| PRP-001 | Property | Ransomware or an intruder reaches BAS and access control through an integrator's remote access | Property VP of building operations | 2027-06-30 |
| PRP-005 | Property | A fraudulent vendor or tenant-refund bank change is processed in Property accounts payable | Property Controller | 2026-11-30 |
| AE-001 | A&E | A&E staff send CUI drawings to construction field teams by commercial email or the PDPP | A&E federal practice leader | 2026-12-31 |
| AE-002 | A&E | The enclave fails a Level 2 (C3PAO) assessment | A&E division president | 2027-02-28 |
| AE-003 | A&E | A nation-state actor exfiltrates DoD facility designs | Group CISO | 2027-03-31 |

### What the results say
The program is mature in most places. There are no Very High risks. Identity, the SOC, backups, and the payment factory's bank-change controls are strong. The High risks cluster around **what the divisions share and hand to each other**:
1. **The handoff of CUI from design to the field** (GR-01). A&E produces CUI in the enclave, and Construction needs it on jobsites. The current workaround moves CUI into commercial systems (scenario gap 1).
2. **Federal eligibility** (GR-03). The group's CMMC statuses rest on a self-assessment that independent testing did not fully support (gap 2), just as Phase 2 begins.
3. **Money moving between the group, owners, tenants, and subcontractors** (GR-02). Controls are strong where payments run through the payment factory and weak where they do not: the pay application remittance block, Property accounts payable, and A&E invoices (gap 3).
4. **Buildings the group owns** (GR-06). Property's building systems are outside group monitoring and depend on integrators (gap 4).

Governance gaps (Section 889 screening, AI governance, subcontractor CMMC checks, policy drift) are Moderate at group level (GR-07, GR-08, GR-09, GR-12). They matter because each is a place where one division does the work well and the others do not.

**New risk from the control assessment.** P07 testing on 2026-08-12 found default credentials on 14 building controllers at 3 properties and covered cameras at 2 federally leased properties. These were added as PRP-018 and PRP-006.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** enclave field access and PDPP CUI blocking (GR-01); payment-instruction service and Property AP migration (GR-02); Level 2 (C3PAO) readiness (GR-03); building network segmentation and SIEM onboarding (GR-06); Section 889 approved-manufacturer list (GR-07).
- **Accepted (all Low):** CON-021 (lost jobsite tablet, covered by device management), CON-022 (telematics vendor breach), PRP-014 (single parking service provider outage, manual fallback).
- **Legal and contract actions:** counsel review of the March 2026 SPRS affirmation (GR-03); subcontractor and subconsultant status checks (GR-09); owner and tenant remittance letters (GR-02).
- **Treatment status:** 60 risks are In progress, 23 are Open (treatment approved, work not started), and 3 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The five High group risks were presented on 2026-09-15. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here (the board risk committee's oversight and the Group CISO's reporting line). Federal eligibility risk (GR-03) is also reported to the audit committee because of its revenue exposure (about 28% of Construction revenue is federal).

## 6. Approval
- Board risk committee: approved the group register, the five High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the nine High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-14 to 2026-09-15.
- Next full review: May to July 2027, or sooner after a major change, acquisition, CMMC assessment result, or incident.

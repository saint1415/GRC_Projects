# Risk Register Report: Cris Santos Company | Food and Agriculture | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant) |
| Size tier | Micro (7 employees) |
| Vertical | Food and Agriculture |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Prepared | 2026-07-31 by the Office Manager (security and compliance lead) with the MSP lead technician and the Production Supervisor |
| Updated | 2026-08-12 (R-023 added and closed from P07 testing); 2026-08-25 (R-017 and R-022 reviewed with the P10 assessment); 2026-08-31 (R-020 and R-021 accepted) |
| Risk owner / approver | Owner and General Manager, 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business and its key vendors: every system in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) (the plant machines, the cold-chain service, the records app, the office SaaS, the network and endpoints, the backup), and the vendors that run or reach them: the MSP, the smokehouse manufacturer, the packaging machine vendor, the cold-chain vendor, the records app vendor, the payroll service, and the card terminal provider ([vendor register](../step-00_P00_intake/vendor-register.csv)). Food safety outcomes are in scope where a cyber event can cause them (wrong cook cycle, lost monitoring, wrong label).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The owner approves a dated treatment plan instead. A High risk that could put unsafe or misbranded food into commerce is never accepted.

This is the company's first risk assessment. Before 2026 security was whatever the MSP did on the office computers.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the SSP (P02), the cloud mapping (P04), the intake evidence, a plant walkthrough on 2026-07-22 (EV-048), and interviews with the owner, the Production Supervisor, the Maintenance and Sanitation Technician, the Office Manager, two production workers, and the MSP lead technician (2026-07-20 to 2026-07-31, EV-046). The gap analysis (P03) ran in the same fieldwork window, and the two shared findings.
2. **Rate likelihood.** For each event, the likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, and so was the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the vendor console, controller and MSP exports, the contracts folder and food safety binder, the walk-throughs and the interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. Undercooked ready-to-eat product or an undeclared allergen reaching consumers is rated Very High; loss of the cold storage inventory or a week without production is High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 12 |
| Low | 7 |
| **Total** | **23** |

Status: 8 In progress, 12 Open, 3 Closed (R-023 treated; R-020 and R-021 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware on the office or labeling PC spreads over the flat network, stops both lines, and cuts cold-chain monitoring | High | Plant network; managed EDR; training; immutable backups and restore tests; offline copies of machine settings | Office Manager | 2026-12-31 |
| R-002 | Cook cycle changed through the smokehouse manufacturer's always-on portal | High | Supervised sessions only (done 2026-08-12); named accounts with MFA; change log; monthly cycle comparison | Production Supervisor | 2026-10-31 |
| R-004 | Cooler or freezer failure goes unnoticed because the gateway is offline or one person misses the alert | High | Escalation; gateway offline alert; cellular backup; manual log procedure | Production Supervisor | 2026-10-31 |
| R-023 | Default administrator password on the smokehouse controller (found in P07) | High | Password changed 2026-08-11; closed | Maintenance and Sanitation Technician | 2026-08-11 |
| R-019 | Insider deliberately changes a formulation or cook cycle | Moderate | Named access, change log, monthly comparison with approved versions | Production Supervisor | 2026-12-31 |
| R-005 | FSIS finds electronic CCP and SSOP records unreliable | Moderate | Named accounts; named administrators; read-only cook-log exports; integrity procedure | Production Supervisor | 2026-12-31 |

**The common theme is that the plant floor had no owner.** The MSP looks after the office computers, the equipment vendors look after their own machines, and nobody looked at how they connect. Two vendor connections could change food safety settings (R-002, R-003). A ransomware infection on an office PC could reach the line controls (R-001). The cold-chain alerts depend on the same network and one phone (R-004). The same small set of fixes treats most of the register: a separate plant network, no shared logins, supervised vendor sessions, and a written downtime binder.

**Food safety and cyber risk are the same risk here.** R-002, R-009, R-019, and R-023 are cyber events whose harm is unsafe or misbranded food. Each one also triggers the FSIS duties to hold product and review it (9 CFR 417.3(b)) and to notify FSIS within 24 hours if adulterated or misbranded product entered commerce (418.2). That is why the Production Supervisor owns them, not the Office Manager.

**Risks fixed or found during the work:**
- R-023: P07 testing on 2026-08-11 found the manufacturer default administrator password on the smokehouse controller's web interface (EV-SC-7). It was changed the same day. The cook-log history was checked against the paper handheld readings for July and showed no unexplained changes. Closed.
- R-002 and R-003: the smokehouse portal connection and the packaging vendor's remote desktop tool were set to supervised, on-request sessions on 2026-08-12 (EV-AC-17).
- R-007: all shared passwords and the smokehouse PIN were changed on 2026-08-12 (EV-AC-2).

**Two passes.** Pass 1 was completed on 2026-07-31 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-023 was added on 2026-08-12 from P07 testing. R-017 and R-022 were identified in Pass 1 and reviewed again with the P10 assessment on 2026-08-25. The `assessment_pass` column shows which pass produced each risk.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the owner; about $6,000 one-time and $1,800 a year):**
  - Plant network (VLAN) and firewall rules by the MSP: about $1,200 one-time
  - MSP-managed EDR with after-hours alerting on the three managed PCs: about $600 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Immutable 90-day backup retention: about $400 a year
  - Cellular backup for the cold-chain gateway: about $250 one-time and $300 a year
  - MFA, named accounts, password changes, and restore tests by the MSP: about $1,000 of MSP time
  - Independent assessment (P07) and policy work (P06): about $3,500 one-time
- **Budgeted for 2027:** stuffer HMI replacement, about $7,500 (R-010); transfer switch for a rental generator, quote due 2026-11-30 (R-014).
- **Accepted:** R-020 (Low; the provider manages the card terminal) and R-021 (Low; devices are encrypted).
- **Contract actions:** MSP contract amendment with incident notice, a recovery commitment, and MFA on its logins (R-012) at renewal by 2026-12-31; named accounts and session approval with the smokehouse manufacturer and packaging vendor (R-002, R-003) by 2026-10-31; AI camera data-use and change-notice terms (R-017) by 2026-11-30.

## 5. Approval
- Owner and General Manager: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, a new machine with remote support, the plant network going live, or the AI camera leaving the pilot) or an incident.

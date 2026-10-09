# Risk Register Report: Cris Santos Company | Food and Agriculture | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (meat processing plant with a smoked seafood room) |
| Size tier | Small (250 employees) |
| Vertical | Food and Agriculture (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with SP 800-82 Rev. 3 for OT threat context |
| Also supports | The food defense vulnerability assessment and its reanalysis (21 CFR 121.130, 121.157) for the cyber-physical process steps |
| Prepared | 2026-07-24 by the IT Manager with the FSQA Manager and the Controls Engineer |
| Approved | 2026-09-04 by the General Manager (Moderate and below) and the majority owner (High and Very High) |

## 1. Scope and risk framing
**Scope.** The Plant Production and Cold-Chain Monitoring System (PPCM) defined in the SSP (P02), the business systems it connects to, and the processes in the BIA (P05). That covers the process control network, SCADA and historian, the recipe and batch system, the ammonia refrigeration controls, cold-chain monitoring, the cloud tenant that holds electronic food safety records, and the vendors with remote access ([asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv)).

**What makes this register different from an office IT register.** Several risks here end in adulterated or temperature-abused food, not in lost data. Impact ratings therefore consider consumer health, product holds and recalls, and FSIS or FDA action, as well as downtime and cost.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the General Manager may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. Risks that could put adulterated product into commerce are not acceptable at High; they must be treated.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 (OT threats and vulnerabilities), the BIA, the intake evidence (including the 2023 food defense plan, EV-018), interviews with the Operations Manager, Controls Engineer, Maintenance and Refrigeration Manager, and Warehouse and Logistics Manager (EV-047), and the plant walkthrough on 2026-07-15 (EV-048). The gap analysis (P03) ran in the same fieldwork window, and the two shared findings.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: configuration exports, the ticket and incident log (EV-029), contracts, the walkthrough and interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories, which include a food safety category.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 6 |
| Moderate | 19 |
| Low | 6 |
| **Total** | **32** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware spreads from corporate IT to SCADA and MES and halts all lines and cold-chain monitoring | Very High | OT DMZ and segmentation; remove MES dual-homing; OT endpoint protection; offline OT backups | IT Manager | 2027-03-31 |
| R-002 | Integrator's shared VPN account used to reach SCADA | High | Named accounts with MFA, time-limited access, session recording | Controls Engineer | 2026-10-31 |
| R-003 | Cure (sodium nitrite) or brine formulation changed in the recipe system | High | Named logins; two-person approval; change alerts to FSQA | FSQA Manager | 2026-12-31 |
| R-004 | CIP chemical valves opened into the seafood brine tank during production | High | Hardwired CIP interlock; actionable process step in the food defense plan | Maintenance and Refrigeration Manager | 2026-11-30 |
| R-006 | Refrigeration controller reached through the contractor's cellular modem | High | Remove modem; contractor access through OT gateway with MFA | Maintenance and Refrigeration Manager | 2026-10-31 |
| R-007 | OT backups lost with production | High | Offline and immutable copies; PLC program repository; quarterly restores | Controls Engineer | 2026-12-31 |
| R-032 | Default administrator password on the refrigeration controller | High | Change now; restrict to the OT engineering subnet | Maintenance and Refrigeration Manager | 2026-09-30 |

The seven High and Very High risks share one theme: **the plant's process controls can be reached, changed, and disabled from places they should not be reachable from, and nobody would see it happen.** Three paths lead in (the corporate network, the integrator VPN, and the refrigeration modem). Once inside, shared logins and missing change logs mean a setpoint or formulation change cannot be attributed or stopped. Fixing segmentation, remote access, and shared logins (R-001, R-002, R-003, R-006, R-032) also lowers five Moderate or Low risks: R-013, R-014, R-019, R-023, and R-029.

**Food defense link.** R-003 and R-004 are intentional adulteration scenarios carried out through the control system rather than by hand. The 2023 vulnerability assessment did not consider them. They are the input to the food defense reanalysis required by 21 CFR 121.157(b)(2) (see P03).

**Two passes.** Pass 1 was completed on 2026-07-24 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-032 was added on 2026-08-14 after testing found the manufacturer default password on the refrigeration controller (EV-IA-5). The `assessment_pass` column shows which pass produced each risk.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $186,000):**
  - OT DMZ, firewall rebuild, and remote access gateway with MFA and session recording ($62,000)
  - OT endpoint protection and a monitoring service covering SCADA, historian, MES, and HMIs ($38,000 a year)
  - Offline and immutable OT backups and a PLC program repository ($14,000)
  - Replacement of two unsupported HMIs ($24,000)
  - Hardwired CIP interlock on the seafood brine tank ($9,000)
  - Escalating cold-chain alerting and cellular failover ($7,000)
  - Named HMI and recipe-system accounts, done by the controls integrator ($18,000)
  - Awareness and food defense training for production and temporary staff ($6,000)
  - A dedicated OT engineering workstation and a media scanning kiosk ($8,000)
- **Accepted:**
  - R-020: Low, vendor-managed online store with no card data on company systems
  - R-027: Low, with phishing-resistant MFA on both cloud administrator accounts; backup separation is tracked under R-007
- **Contract actions:** named-user, MFA, and notice terms for the controls integrator, the refrigeration contractor, and the AI vision vendor; SOC 2 reports from the cold-chain monitoring and payroll vendors (R-015, R-021, R-023), due by 2027-01-31.

## 5. Approval
- General Manager: approved Moderate and Low treatments and the two acceptances, 2026-09-04.
- Majority owner: approved the High and Very High treatment plans and the budget, 2026-09-04. No High or Very High risk was accepted.
- Next full review: July 2027, or sooner after a major change, an incident, or the food defense reanalysis.

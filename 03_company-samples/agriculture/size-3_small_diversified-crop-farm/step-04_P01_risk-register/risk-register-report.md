# Risk Register Report: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (diversified precision-agriculture crop farm) |
| Size tier | Small (15 employees) |
| Vertical | Agriculture, Forestry, Fishing and Hunting |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT threat sources and conditions from NIST SP 800-82 Rev. 3 Appendix C |
| Benchmark | NIST CSF 2.0 (ID.RA and GV.RM); no binding federal cybersecurity rule applies to the farm (P03 section 1) |
| Prepared | 2026-07-24 by the Operations and Technology Manager (security lead), with the Farm Manager and Irrigation Technician |
| Approved | 2026-08-31 by the Farm Manager (Moderate and below) and the majority owner and General Manager (High) |

## 1. Scope and risk framing
**Scope.** The Farm Management and Irrigation Control Platform (FMICP) defined in the SSP (P02), the ten business processes in the BIA (P05), and the systems that hold personal and regulated records: payroll and H-2A files, Produce Safety records, telematics location history, and online customer data (`../00_company-facts.md` section 3).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Operations and Technology Manager may accept.
- Moderate: the Farm Manager may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner and General Manager may accept, and only temporarily with a dated treatment plan. Risks that could injure a worker (fertigation, spray equipment) are not accepted at High.

This is the farm's first documented cybersecurity risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E and SP 800-82 Rev. 3 Appendix C (OT threat sources, vulnerabilities, and incidents), the BIA, interviews with the Farm Manager, Irrigation Technician, Food Safety and Packing Lead, and Office and HR Manager, and the gap analysis (P03).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (cost, operations, regulatory, safety, reputation). Season matters: impact was rated for the December to June harvest season, when the farm earns most of its receipts.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 18 |
| Low | 10 |
| **Total** | **32** |

Treatments: 29 Mitigate and 3 Accept (R-017, R-028, R-029, all Low).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware encrypts office endpoints, the SCADA HMI, and the farm data hub in season | High | EDR with after-hours alerting; segmentation; phishing training; immutable backups | Operations and Technology Manager | 2027-01-31 |
| R-002 | Integrator remote access account used to reach the HMI and change pumps, pivots, or fertigation | High | Remove always-on access; named accounts with MFA through a jump host; session logging; contract terms | Operations and Technology Manager | 2026-10-31 |
| R-003 | Backups destroyed along with production | High | Separate immutable backup account in a second region; monthly SYS-01 export; quarterly restore tests | Operations and Technology Manager | 2026-12-31 |
| R-007 | Freeze protection fails to start on a freeze night | High | Standalone temperature alarm; freeze-night staffing; tested manual start procedure | Farm Manager | 2026-11-15 |
| R-005 | Fertigation settings changed through the HMI | Moderate | Hard limits in PLC logic; setpoint change alerts; named HMI accounts | Irrigation Technician | 2026-12-31 |
| R-011 | Theft of payroll and H-2A files | Moderate | Restrict the personnel library; data inventory; mass-download alerts | Office and HR Manager | 2026-10-31 |

The four High risks share one theme: **the farm's irrigation depends on a small OT system that anyone who gets onto the network, or into the integrator's account, can reach, and the farm could not rebuild it quickly.** Access is too open (R-002, and the flat network in R-022), detection is absent (R-001), and recovery is unproven (R-003, and the PLC program held only by the integrator in R-015). R-007 is the exception: it is a physical, weather-driven risk where automation is a single point of failure on the most valuable nights of the year.

Fixing the four High risks also reduces six related Moderate risks: R-005, R-013, R-014, R-015, R-021, and R-022.

**Food defense note.** R-005 (fertigation manipulation) is the only risk where intentional adulteration of produce is plausible. 21 CFR Part 121 (N11-R01) does not apply to the farm (P03 section 1), but its vulnerability-assessment approach was used as a voluntary checklist for that risk.

R-014 was added on 2026-08-07 after control assessment testing (P07) found manufacturer default passwords on the LoRaWAN gateway and two pivot panel modems.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $31,500):**
  - Network segmentation of the pump house and packing shed (firewall and switch changes by the MSP): $6,000
  - Integrator remote access redesign (jump host, named accounts, MFA) and PLC hard limits: $4,500
  - EDR with after-hours alerting through the MSP: $5,500 per year
  - Backup redesign with immutable second-region storage: $2,500 per year
  - Standalone freeze and cooler alarm dialer with cellular path: $1,800
  - Cellular failover on the headquarters firewall: $1,200 plus $600 per year
  - Spare PLC CPU and surge protection: $4,900
  - Security awareness training with Spanish-language materials: $1,500 per year
  - Desktop encryption and tablet management: staff time and existing licenses
  - Outside counsel review of integrator, dealer, and AI vendor terms: $3,000
- **Accepted:**
  - R-017: Low, manual steering is an adequate fallback
  - R-028: Low, point-to-point encrypted terminals keep card data off farm systems
  - R-029: Low, vendor-managed; the vendor must notify the farm under Fla. Stat. 501.171(6)
- **Contract actions:** security terms for the irrigation integrator (R-002), data terms for the AI vendor (R-026), and access terms for the equipment dealer (R-016), all due by 2026-12-31.

## 5. Approval
- Farm Manager: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Majority owner and General Manager: approved the High-risk treatment plans and the budget, 2026-08-31.
- Next full review: July 2027, before the next season, or sooner after a major change or incident.

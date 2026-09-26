# Risk Register Report: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer) |
| Size tier | Small (250 employees) |
| Vertical | Mining, Quarrying, and Oil and Gas Extraction (NAICS 211120) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT threat sources and predisposing conditions from NIST SP 800-82 Rev. 3 Appendix C |
| Benchmark | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary; see P03 for why no binding federal sector rule applies) |
| Prepared | 2026-07-24 by the IT Manager with the SCADA and Automation Supervisor; R-032 added 2026-08-07 |
| Approved | 2026-08-31 by the CFO (Moderate and below), the majority owner (High), and the VP Operations (all field-operations risks) |

## 1. Scope and risk framing
**Scope.** The Field SCADA and Production Accounting System (FSPA, P02), the business IT systems that connect to it, and the business processes in the BIA (P05). That covers the OCC, all field devices and communications, the cloud tenant, the SaaS applications that hold production, royalty, and employee data, and the vendors with access to them (`../scenario-facts.md` section 3).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept, or the SCADA and Automation Supervisor for OT-only items.
- Moderate: the CFO may accept, with a treatment plan or a documented reason. If the risk affects field operations, the VP Operations must agree.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan.
- **Safety and environment:** no risk whose impact includes a plausible injury, H2S exposure, or release may be accepted at High. It must be treated.

This is the company's first documented cybersecurity risk assessment that includes the SCADA system.

## 2. Method
1. **Identify.** Threat sources and events were identified from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 Appendix C (OT threat sources, vulnerabilities, and incidents), the BIA, walkthroughs of the OCC and 6 field sites (2026-07-15 and 2026-07-16), and interviews with Production Controllers, both Field Superintendents, the Production Accounting Manager, and the SCADA integrator.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). The hardwired safety shutdowns were counted as an existing control: they limit the physical consequences of a SCADA compromise, which is why most SCADA risks rate High impact rather than Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables with a script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 20 |
| Low | 9 |
| **Total** | **32** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware from business IT spreads to SCADA servers and HMIs | High | OT DMZ; remove remote desktop to HMIs; retire the dual-homed workstation; 24x7 managed detection and response | SCADA and Automation Supervisor | 2027-01-31 |
| R-002 | Attacker uses the integrator's always-on remote access to operate HMIs | High | Jump host with named accounts, MFA, session recording, per-session approval | IT Manager | 2026-11-30 |
| R-003 | SCADA and cloud backups destroyed with production | High | Offline SCADA copies; separate immutable cloud backups; quarterly restore test | SCADA and Automation Supervisor | 2026-12-31 |
| R-032 | Internet-exposed well-pad modems with default passwords | Moderate | Private network only; change passwords; disable internet management | SCADA and Automation Supervisor | 2026-09-30 |
| R-006 | Unapproved PLC logic change alters an injection limit | Moderate | Change requests, peer review, program repository | SCADA and Automation Supervisor | 2026-12-31 |
| R-014 | Hurricane or fire disables both SCADA servers at the OCC | Moderate | Standby server moved to the South Florida field office | VP Operations | 2027-06-30 |
| R-026 | Uncoordinated response during a cyber incident | Moderate | POL-03, P08 runbook, joint IT and operations tabletop | IT Manager | 2026-11-30 |

The three High risks share one theme: **a ransomware or remote-access attack on business IT could take away the company's view and control of its fields, and the company could not rebuild SCADA quickly today.** The path in is open (R-001, R-002), and the way back is not protected (R-003). Fixing these three also reduces eight related Moderate risks:
- R-005 (unsupported operating system), R-013 (no OT monitoring), R-021 (USB and transient devices), R-025 (unwatched EDR alerts), and R-026 (no OT incident plan), all on the ransomware path.
- R-030 (insurance coverage dispute), which depends on MFA for vendor access.
- R-014 (single OCC room) and R-024 (cloud administrator compromise), which depend on the backup redesign.

R-032 was added on 2026-08-07 after control assessment testing (P07) found three well-pad cellular modems reachable from the internet with default passwords. The fix was already under way when this report was approved.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $195,000):**
  - OT DMZ and IT/OT firewall redesign with the SCADA integrator: $45,000
  - Vendor remote access jump host with MFA and session recording: $18,000
  - Passive OT network monitoring sensor and service: $40,000 per year
  - 24x7 managed detection and response for corporate EDR: $36,000 per year
  - Offline SCADA backups and a separate immutable cloud backup account: $12,000
  - SCADA server and HMI operating system upgrade with the integrator: $38,000
  - Cellular modem reconfiguration and two replacement modems: $6,000
- **Accepted:**
  - R-004: Low; authenticated radios at the 2028 radio refresh
  - R-015: Moderate; the pre-storm shut-in procedure controls safety and environmental impact (CFO and VP Operations)
  - R-016: Low; dual-carrier modems reviewed at the next refresh
  - R-017: Low; vendor availability commitments meet the BIA
  - R-020: Low; MDM wipe and MFA already in place
  - R-023: Low; cabinet door alarms added when cabinets are replaced
- **Contract actions:** security terms, breach notice terms, and MFA for remote access in the SCADA integrator, production accounting, HR and payroll, and telematics contracts at renewal (R-018, R-019, R-027).

## 5. Approval
- CFO: approved Moderate and Low treatments and acceptances, 2026-08-31.
- VP Operations: agreed to all treatments and acceptances that affect field operations, 2026-08-31.
- Majority owner: approved the High-risk treatment plans and the budget, 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, the OT DMZ cutover) or an incident.

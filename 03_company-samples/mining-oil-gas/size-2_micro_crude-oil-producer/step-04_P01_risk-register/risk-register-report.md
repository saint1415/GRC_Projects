# Risk Register Report: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer, one field) |
| Size tier | Micro (7 employees) |
| Vertical | Mining, Quarrying, and Oil and Gas Extraction (NAICS 211120) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT threat sources and predisposing conditions from NIST SP 800-82 Rev. 3 Appendix C |
| Benchmark | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary; see P03 for why no binding federal sector rule applies) |
| Prepared | 2026-07-31 by the Office Manager (Security Coordinator) with the Field Superintendent and the MSP lead technician |
| Updated | 2026-08-12 (R-025 added from P07 testing and closed); 2026-08-26 (R-022 updated after the P10 review); 2026-08-31 (R-013 and R-016 accepted) |
| Approved | 2026-08-31 by the Owner, with the Field Superintendent's agreement for field-operations risks |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors: the Field SCADA and Production Accounting System (FSPA, P02), which at this size is nearly all of the company's technology, the business processes in the BIA (P05), and the vendors that hold data or have access: the MSP, the SCADA integrator, the SCADA vendor, the production accounting vendor, the productivity suite vendor, the bank, and the payroll service (`../00_company-facts.md` sections 2 and 3).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept, or the Field Superintendent for field-only items.
- Moderate: only the Owner may accept, with a treatment plan or a written reason. If the risk affects field operations, the Field Superintendent must agree.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead.
- **Safety and environment:** no risk whose impact includes a plausible injury, H2S exposure, or release may be accepted at High. It must be treated.

This is the company's first documented cybersecurity risk analysis. Earlier risk work covered only spills, fire, H2S, and storms (the emergency response plan).

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 Appendix C (OT threat sources, vulnerabilities, and incidents), the BIA (P05), the gap analysis (P03), a walkthrough of the field office, tank battery, SWD facility, and 3 well sites on 2026-07-22, and interviews with all 7 staff, the MSP lead technician, and the SCADA integrator.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). The hardwired safety shutdowns were counted as an existing control: they limit the physical consequences of a SCADA compromise, which is why the SCADA risks rate High impact rather than Very High. Daily well visits by the Lease Operators were counted the same way.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 16 |
| Low | 5 |
| **Total** | **25** |

Status: 9 In progress, 13 Open, 3 Closed (R-025 treated; R-013 and R-016 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware from a field office PC spreads to the SCADA host and its attached backup | High | Firewall between field PCs and SCADA; remove the remote desktop shortcut; training; EDR with after-hours alerts | Field Superintendent | 2026-12-31 |
| R-002 | Attacker uses the integrator's always-on remote tool to operate the HMI | High | Remove the tool; MFA-protected sessions enabled per session by the Field Superintendent | Field Superintendent | 2026-10-31 |
| R-003 | SCADA host cannot be rebuilt because its only backup is lost with it | High | Rotated offline drives; programs copied off the laptop; immutable cloud copy; quarterly restore test | Field Technician | 2026-12-31 |
| R-025 | Remote desktop port to the SCADA host open to the internet | High (closed) | Port forward removed 2026-08-11; quarterly external scan | Field Superintendent | 2026-08-12 |
| R-004 | Payment redirected by business email compromise | Moderate | Call-back rule for bank detail changes; monthly change report | Production Accountant | 2026-09-30 |
| R-022 | Predictive maintenance add-on writes to controllers or misses failures | Moderate | Write-back off and checked monthly; vendor terms (P10) | Owner | 2026-11-30 |
| R-019 | Uncoordinated response during a cyber incident | Moderate | POL-03, P08 runbook, tabletop with the MSP and integrator | Office Manager | 2026-11-30 |

**The common theme is the field office network.** One flat network joins the office PCs, the Wi-Fi, and the SCADA host, and two outside paths reached the host with no MFA (the integrator's tool and, until 2026-08-11, an open remote desktop port). The only backup sits plugged into the host it protects. The treatments for R-001 to R-003 also reduce R-006, R-011, R-017, R-020, and R-021.

**Risks that were fixed or found during the work:**
- R-007: the former Lease Operator's mobile viewer account was disabled on 2026-07-22, the day it was found. The viewer log showed no sign-ins after his last day. The process gap (no checklist, unchanged shared passwords) remains open.
- R-025: added on 2026-08-12 after P07 testing found the remote desktop port forward on 2026-08-11. The Field Superintendent removed it the same afternoon and the assessor's rescan on 2026-08-12 confirmed it closed. The level shown is the level as found.
- R-022: updated on 2026-08-26, when the Owner found during the P10 review that the vendor had enabled write-back to 2 pilot wells, and turned it off.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner; about $11,500 one-time and $4,100 a year):**
  - Small industrial firewall for the field office, configured by the MSP with the integrator: about $1,800 hardware and $1,200 labor
  - Replacement SCADA host on a supported operating system, installed by the integrator: about $4,500
  - Vendor remote session tool with MFA, managed by the MSP: about $600 a year
  - Two encrypted rotation drives, a spare PC for restore tests, and the SCADA host added to the immutable cloud backup: about $900 one-time and $480 a year
  - MSP-managed EDR with after-hours alerting on 8 computers including the SCADA host: about $1,700 a year
  - Training and phishing exercises for 7 people: about $500 a year
  - Cellular backup for the field office internet line: about $300 one-time and $420 a year
  - MSP scope extension to the field office (inventory, quarterly external scan, change log support): about $400 a year
  - Independent assessment and policy work in 2026 (P07, P06): about $2,800 one-time
- **Accepted:** R-013 (Low; the vendor's RTO meets the BIA), R-016 (Low; MDM and a view-only viewer).
- **Contract actions:** security and change-notice terms for the SCADA vendor (R-022), named accounts and MFA for the integrator (R-002), breach notice terms for the production accounting vendor (R-014), and MSP scope for the field office, all at renewal or by 2027-03-31.

## 5. Approval
- Owner: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Field Superintendent: agreed to the field-operations treatments on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, the SCADA host replacement or any change to the predictive maintenance add-on) or an incident.

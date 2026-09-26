# Risk Register Report: Cris Santos Company | Chemical | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical formulator and packager) |
| Size tier | Small (162 employees) |
| Vertical | Chemical (CISA critical infrastructure sector; NAICS 325998) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT threat context from NIST SP 800-82 Rev. 3 (sec. 4.1, Managing OT Security Risk) |
| Also supports | RMP hazard review (40 CFR 68.50(a)(2)-(3)) for cyber-initiated malfunctions; CFATS RBPS 8 voluntary benchmark (P03) |
| Prepared | 2026-07-24 by the IT Manager with the Controls Engineer and EHS Manager; R-007 added 2026-08-14 |
| Approved | 2026-09-04 by the VP Operations (Moderate and below) and the CEO (High) |

## 1. Scope and risk framing
**Scope.** The whole plant: the Process Control and Batch Management System (PCBMS, P02), the business systems in the BIA (P05), the cloud tenant (P04), and the vendors with access to them (`../scenario-facts.md` section 3).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept, with the Controls Engineer for OT risks.
- Moderate: the VP Operations may accept, with a treatment plan or a documented reason.
- High and Very High: only the CEO may accept, and only temporarily with a dated treatment plan.
- **Safety rule:** any risk whose impact includes a toxic release that could reach the public is not accepted at High. It must be treated, and the Plant Manager (RMP qualified person) must agree that the treatment is adequate.

**How impact was rated for OT.** Impact follows Table H-3 and the BIA categories. For the aqueous ammonia process, the worst credible outcome is a toxic release. The independent SIS lowers the *likelihood of adverse impact* (it trips on high level and high pressure regardless of the DCS). It does not lower the *impact* if the SIS itself is defeated. That is why R-007 is rated Very High impact.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 (OT threats and safety considerations, sec. 5.3.1), the P08 scenario (intrusion into process control systems), interviews with the Plant Manager, Controls Engineer, EHS Manager, Process Engineer, and Shift Supervisors, and the gap analysis (P03).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 21 |
| Low | 8 |
| **Total** | **33** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Integrator remote access path used to change ammonia process setpoints | High | Remote access gateway with named accounts, MFA, session approval, and recording | IT Manager | 2026-11-30 |
| R-002 | Ransomware spreads into the historian and HMIs | High | OT DMZ with a historian replica; deny-by-default firewall rules | Controls Engineer | 2027-01-31 |
| R-006 | DCS configuration and recipes cannot be restored | High | Offline immutable copies; quarterly restore test on spare hardware | Controls Engineer | 2026-12-31 |
| R-007 | SIS logic altered or bypassed from the DCS engineering workstation | High | Keyswitch locked in run; SIS software removed from the EWS; shift check | Controls Engineer | 2026-10-15 |
| R-027 | Late release notification after a cyber-caused release | Moderate | OT runbook (P08); cellular phones and printed call lists | EHS Manager | 2026-11-30 |
| R-005 | Erroneous recipe change creates an incompatible mixture | Moderate | DCS, SIS, PLC, and recipe changes under MOC with two-person approval | Process Engineer | 2026-11-30 |

The four High risks share one theme: **an attacker who reaches the business network can reach the process controls, and the plant could not rebuild them quickly.** The remote access path (R-001) and the dual-homed historian (R-002) are the ways in. The SIS engineering path (R-007) is the way to defeat the last safeguard. The untested backups (R-006) mean there is no fast way back. Fixing these four also reduces seven related Moderate risks (R-004, R-005, R-008, R-009, R-010, R-029, R-030).

R-007 was added on 2026-08-14 after control assessment testing (P07) found the SIS keyswitch in the remote program position. The Controls Engineer returned it to run and locked it on 2026-08-12, the day it was found.

**Inherently safer option noted (not chosen).** Switching from 29% to 19% aqueous ammonia would take the process out of RMP coverage (the listing is "Ammonia (conc 20% or greater)", 40 CFR 68.130). The Process Engineer found it would require reformulating 60 products and nearly double deliveries. It stays on the 2027 review list.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $165,000):**
  - OT DMZ, historian replica, and firewall rebuild (R-002, R-022, R-025, R-028)
  - Remote access gateway with MFA and session recording (R-001)
  - Passive OT network monitoring sensor and log collection (R-010)
  - Offline immutable OT backups and a spare-hardware restore bench (R-006)
  - Media scanning station (R-009)
  - Cellular phones and radios for emergency notification (R-027)
- **Capital plan 2027:** DCS upgrade, $240,000, timed with the 2027 turnaround (R-032, R-008).
- **Staff time only:** unique DCS accounts (R-004), MOC for control system changes (R-005), SIS hardening (R-007), termination checklist (R-012), OT training (R-030).
- **Accepted:** R-026 (Low; rogue wireless, checked by an annual survey).
- **Contract actions:** security clauses for the DCS integrator and the data science contractor; ERP and HR vendor SOC 2 reviews (R-013, R-029, R-031), due by 2026-12-31.

## 5. Approval
- VP Operations: approved Moderate and Low treatments and the one acceptance, 2026-09-04.
- CEO: approved the four High-risk treatment plans and the budget, 2026-09-04. The Plant Manager confirmed that the R-001, R-002, and R-007 treatments are adequate for the toxic release scenario.
- Next full review: July 2027, before the RMP hazard review update, or sooner after a major change or incident.

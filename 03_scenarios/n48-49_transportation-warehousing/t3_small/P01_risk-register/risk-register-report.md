# Risk Register Report: Cris Santos Company | Transportation and Warehousing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (marine cargo terminal operator, NAICS 488320) |
| Size tier | Small (60 employees) |
| Vertical | Transportation and Warehousing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | The Subpart F Cybersecurity Assessment, 33 CFR 101.650(e)(1) (due 2027-07-16). This register is the risk analysis part; the network vulnerability analysis is still to come (see section 1) |
| Prepared | 2026-07-31 by the IT Manager (proposed Cybersecurity Officer) with the Security and Safety Manager (FSO) |
| Approved | 2026-09-04 by the General Manager (Moderate and below) and the majority owner (High) |

## 1. Scope and risk framing
**Scope.** The Terminal Operations and Gate Platform (TOGP) defined in the SSP (P02), the crane and yard equipment controllers (OT), CCTV and the physical access control system, and the business processes in the BIA (P05). That covers every system that could, if compromised, disrupt cargo operations or lead to a transportation security incident (TSI), plus the vendors with access to those systems (`../scenario-facts.md` section 3).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the General Manager may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. A High risk that could cause injury, a TSI or loss of control of cargo-handling equipment may not be accepted at all; it must be treated.

**Relationship to the Coast Guard rule.** Subpart F requires a Cybersecurity Assessment by 2027-07-16 that analyzes all networks to identify vulnerabilities to critical IT and OT systems and the risk posed by each digital asset (101.650(e)(1)(i)). This register gives the risk method, the threat picture and the priorities. The asset-by-asset network analysis needs the inventory and network map in R-025 first. It is scheduled for 2027-03-31.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews with the Operations Manager, Maintenance Manager, FSO and Vessel and Yard Planning Lead, the gap analysis (P03), and public reporting of cyber incidents at ports and terminals.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood that the event causes adverse impact were rated separately and combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories: cost, operations, safety, regulatory and reputation.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed by script from the two tables, not assigned by hand.

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
| R-001 | Ransomware encrypts the TOS and gate servers and stops the terminal | High | MFA on VPN and all TOS users; EDR with 24x7 alerting; segmentation; isolated backups | IT Manager | 2026-12-31 |
| R-002 | Attacker moves from IT into crane and RTG controllers | High | Separate OT zone behind an internal firewall; log and alert on IT-OT connections | Maintenance Manager | 2027-03-31 |
| R-003 | Crane vendor's always-on remote access is compromised | High | Off by default; per-session approval with named accounts, MFA, recording | Maintenance Manager | 2026-10-31 |
| R-004 | Backups destroyed along with production | High | Separate backup account, immutable retention, second region; quarterly restore tests | IT Manager | 2026-12-31 |
| R-006 | No Cybersecurity Officer drives the Subpart F work | Moderate | Written CySO and alternate designation; 24x7 contact rota | General Manager | 2026-10-31 |
| R-005 | Cyber incident not reported under 33 CFR 6.16-1 | Moderate | Cyber Incident Response Plan with reporting checklist (P08) | Security and Safety Manager | 2026-10-31 |
| R-007 | Missed Subpart F training deadline; untrained staff and longshore labor | Moderate | Role-based and OT training; hiring hall briefing | HR Specialist | 2026-11-30 |

The four High risks share one theme: **an attacker who gets into the terminal's IT can reach everything, and the terminal could not recover quickly.** Entry is easy through a password-only VPN (R-001) or the crane vendor's appliance (R-003). The flat gate and yard network puts crane controllers one hop from the gate servers (R-002). The backups sit where the attacker would be (R-004). Treating these four also reduces 8 related Moderate risks: R-008, R-009, R-010, R-013, R-021, R-022, R-025 and R-033.

R-033 was added on 2026-08-14, after control assessment testing (P07) found manufacturer default passwords on 2 RTG HMIs and the OCR camera controllers.

## 4. Treatment summary
- **Funded (2026 Q4 to 2027 Q1 budget, $145,000):**
  - MFA on the VPN and all TOS users (existing identity provider licenses)
  - MSP-managed EDR with 24x7 monitoring on servers and endpoints
  - An internal firewall and OT zone, with integrator labor (R-002)
  - A session-based vendor remote access service (R-003, R-018)
  - Backup redesign (R-004) and central log collection (R-021)
  - Replacement OCR servers before end of support (R-010)
  - A second internet circuit (R-016)
  - Role-based and OT-specific training (R-007)
- **Accepted:**
  - R-017 (Moderate): single-region TOS; multi-zone design and manual workarounds. Accepted by the General Manager until the contingency plan is written.
  - R-027 (Low): administrator takeover; MFA already applies to administrators.
- **Regulatory milestones:** CySO designation by 2026-10-31 (R-006); Cybersecurity Assessment by 2027-03-31 and Cybersecurity Plan submission by 2027-05-31, ahead of the 2027-07-16 deadline (R-026).
- **Contract actions:** vulnerability and incident notification clauses for the crane, OCR and TOS vendors at the next renewal, and no later than 2027-03-31 (101.650(f)(2)).

## 5. Approval
- General Manager: approved Moderate and Low treatments and acceptances, 2026-09-04.
- Majority owner: approved the High-risk treatment plans and the budget, 2026-09-04.
- Next full review: with the Cybersecurity Assessment in 2027-03, then annually (101.650(e)(1)), or sooner after a major change or incident.

# Risk Register Report: Cris Santos Company | Energy | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (small intrastate natural gas transmission pipeline operator) |
| Size tier | Micro (7 employees) |
| Vertical | Energy (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT threat sources and predisposing conditions from NIST SP 800-82 Rev. 3, Appendix C |
| Prepared | 2026-07-31 by the Office Manager (security program coordinator) and the Operations Manager, with the MSP lead technician |
| Updated | 2026-08-19 (R-023 added from P07 testing); 2026-09-15 (R-018 and R-022 accepted and closed) |
| Approved | 2026-09-15 by the Owner |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors: the Pipeline SCADA and Gas Control System (PSGCS, the SSP system in P02), office IT, business SaaS, the 7 field sites, and the vendors that run systems for the company: the hosted SCADA vendor, the MSP, the cellular carrier, and the productivity suite and backup vendors (`../00_company-facts.md` section 3). Business processes and impact levels come from the BIA (P05).

**What makes this register different from an office business.** The worst outcomes are physical: an undetected release, an unauthorized valve command, or loss of gas supply to a municipal system serving about 9,000 homes and businesses. Cyber risks are rated on those consequences, not only on data loss.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager (office IT) or the Operations Manager (SCADA and field) may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. A risk that could cause loss of pipeline control or public harm is never accepted at High.

This is the company's first cybersecurity risk assessment of any kind.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 Appendix C, the BIA (P05), the gap analysis (P03), and interviews with the Owner, the Operations Manager, both Pipeline Technicians, the Gas Scheduler, and the MSP lead technician (2026-07-20 to 2026-07-31).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). Safety and supply impacts set the rating when they are the worst case.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 14 |
| Low | 5 |
| **Total** | **23** |

Status: 11 In progress, 10 Open, 2 Closed (R-018 and R-022 accepted).

No risk is rated Very High. Two risks (R-002 and R-003) carry a Very High impact because a false command or a compromised SCADA platform could cause public harm; they stay at High only because of their likelihood ratings.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Office ransomware reaches the gas control desk and leads to a precautionary shut-in | High | Dedicated desk on its own segment; clean spare SCADA laptop; EDR; training; P08 decision table | Office Manager | 2026-12-31 |
| R-002 | Attacker uses a SCADA password to send valve commands | High | SCADA MFA; named accounts; sign-in alerts; command log review | Operations Manager | 2026-10-31 |
| R-003 | Hosted SCADA vendor compromise or failure | High | Contract terms; quarterly configuration export; tested manual operation call list | Owner | 2026-12-31 |
| R-005 | Wrong or late shut-in decision because no criteria exist | High | Cyber annex to the emergency plan with the P08 decision table; tabletop | Operations Manager | 2026-11-30 |
| R-023 | Municipal gate station gateway reachable from the internet with a default password | Moderate | Check all SIMs; change every default password | Operations Manager | 2026-10-31 |
| R-011 | On-call controller fatigue after night callouts | Moderate | Count callouts toward hours-of-service; rest rule; fatigue education | Operations Manager | 2026-10-31 |

**The common theme: the controls that protect the pipeline sit on the company's side of a vendor service.** The SCADA vendor runs a well-evidenced platform, but the company left the doors on its side open: a password-only web client with command rights (R-002), a control desk that is also an office computer (R-001), and no plan for deciding when not to trust SCADA (R-005). Treating these four High risks also lowers R-004, R-006, R-009, R-013, R-015, R-017, and R-023.

**Risks fixed or found during the work:**
- R-006: the departed Pipeline Technician's SCADA account was disabled and the shared desk password changed on 2026-07-23, the day after the gap was found. The vendor audit log showed no use after departure. The process gap remains open.
- R-023: added on 2026-08-19 after P07 testing found that a replacement SIM had put the municipal gate station gateway on the public internet with its default password. The carrier moved it back to the private network and the password was changed the same day. The check of the other 6 sites is open.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner; about $10,800 one-time and $3,260 a year):**
  - Gas control desk rebuild: 2 dedicated workstations and a separate firewall segment (MSP project): about $3,200 one-time
  - Clean spare SCADA laptop kept off the network: about $1,200 one-time
  - Cellular failover router for the office: about $400 one-time and $360 a year
  - Independent OT security assessment (P07): about $6,000 one-time
  - MSP-managed EDR with alert monitoring on 11 computers: about $1,300 a year
  - Second-carrier SIMs at the receipt station and the municipal gate station: about $700 a year
  - Suite backup upgrade to 90-day immutable versions: about $500 a year
  - Awareness training with phishing simulations for 7 people: about $400 a year
  - SCADA MFA and sign-in alerts: included in the vendor subscription
- **Accepted:** R-018 (Low; fences, locks, patrols, and door alarms) and R-022 (Low; few records, MFA in place).
- **Contract actions by 2026-12-31:** SCADA vendor amendment (24-hour incident notice, support-session notice, 30 days' notice of changes) for R-003 and R-014; MSP amendment (24-hour incident notice, approval of desk sessions) for R-004.

## 5. Approval
- Owner: approved all treatment plans, the two acceptances, and the budget on 2026-09-15.
- Next full review: July 2027, or sooner after a major change (a new SCADA vendor, any move of the leak module out of trial, or a TSA designation) or an incident.

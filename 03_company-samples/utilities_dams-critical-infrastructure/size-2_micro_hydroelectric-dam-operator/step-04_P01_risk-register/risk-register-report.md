# Risk Register Report: Cris Santos Company | Dams | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (owner and operator of the fictional Bramble Shoals Hydroelectric Project, Florida) |
| Size tier | Micro (7 employees) |
| Vertical | Dams (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | The Security Assessment that the FERC Security Program recommends for Group 3 dams (Rev. 3A 3.3.3), and the licensee duty to keep "a level of awareness of potential threats" (3.2) |
| Prepared | 2026-07-24 by the Office and Compliance Administrator and the Plant Superintendent, with the Controls and Electrical Technician, the MSP, and the controls integrator |
| Updated | 2026-08-12 (R-010 added from P07 testing) |
| Approved | 2026-08-31 by the Owner and General Manager |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors: the Hydro Plant Control and Dam Monitoring System (HPCDMS, the P02 system), the office IT and SaaS services, the MSP-operated cloud backup, and the business processes in the BIA (P05). Key vendors are the controls integrator, the MSP, the remote monitoring service vendor, the remote desktop tool vendor, the camera vendor, and the cooperative. See `../00_company-facts.md` sections 3 and 4.

**What makes this register different from an office business.** The worst outcomes are physical. Someone who can move the spillway gates can send a sudden flow change to the tailrace, the canoe launch, and the bank-fishing area, where recreation users could be swept away. The dam is Significant hazard potential (18 CFR 12.3(b)(13)(ii)), so dam failure would probably not cause loss of life, but a gate misoperation on a summer weekend could. Impact ratings follow the BIA safety category first and cost second.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Plant Superintendent or the Office and Compliance Administrator may accept.
- Moderate, High, and Very High: only the Owner and General Manager may accept. High and Very High risks are accepted only temporarily, with a dated treatment plan.
- Any risk that could cause an uncontrolled gate movement may not be accepted at High. It must be reduced.

This is the company's first documented risk assessment. The only earlier document is a 2011 one-page physical security checklist from the prior owner, which does not rate likelihood or impact and is not relied on.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the threat scenarios the FERC Security Program lists for vulnerability assessments (Rev. 3A 5.3, used as a checklist even though no Vulnerability Assessment is required for Group 3), the BIA (P05), the voluntary Section 9 screen and gap analysis (P03), and interviews with all 7 staff, the MSP, and the integrator (2026-07-13 to 2026-07-24).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood that the event causes adverse impact were rated and combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05). An unauthorized gate opening with recreation users present is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 13 |
| Low | 6 |
| **Total** | **23** |

Status: 8 In progress, 13 Open, 2 Closed (R-014 and R-021 accepted).

No risk rated Very High. The gate risks stop at High because the dam is Significant hazard, the tailrace horn sounds before any gate opens, and local panels can override remote commands.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Shared remote desktop password used to open spillway gates or trip units | High | One remote access path with named accounts, MFA, and view-only by default; weekly session review | Controls and Electrical Technician | 2026-11-30 |
| R-003 | Compromised integrator uses its always-on cellular VPN to reach the PLCs | High | Router off except for watched sessions; then retire it; security terms in the integrator agreement | Plant Superintendent | 2026-11-30 |
| R-004 | Office ransomware spreads to the unsupported HMI PC | High | Firewall rebuild; OT-only engineering laptop; no browsing on the HMI PC | Controls and Electrical Technician | 2026-10-31 |
| R-005 | HMI PC or a PLC cannot be rebuilt in time | High | Company-held copies after every change; OT recovery procedure; restore test | Controls and Electrical Technician | 2027-03-31 |
| R-002 | Former or current staff member misuses shared OT passwords | Moderate | Termination checklist; named accounts | Office and Compliance Administrator | 2026-09-30 |
| R-007 | Cyber incident not reported to FERC under 18 CFR 12.10 | Moderate | POL-03, P08 runbook, training, ODSP update | Plant Superintendent | 2026-12-31 |
| R-008 | FERC finds the remote control capability still has no security plan | Moderate | Site security plan with the SSP as its cyber section | Plant Superintendent | 2027-03-31 |

**The common theme is remote access.** Three of the four High risks (R-001, R-003, R-004) are ways into the control network from outside the control room: a shared password, an always-on vendor link, and an open firewall rule. Closing them (POAM-002, POAM-004, POAM-005 in P07) also lowers R-002, R-006, R-016, and R-023. The fourth High risk (R-005) is about recovery: today the company could not rebuild its gate and unit controls without the integrator, from copies that are three years old.

**Risks that changed during the work:**
- R-002: the former operator-mechanic's monitoring portal account was removed on 2026-07-21, the day it was found, and the shared remote desktop password was changed on 2026-08-12. The remote desktop tool keeps only 30 days of connection records, so nobody can show whether the password was used after he left; the 30 days available were reviewed in P07 and every session was tied to staff or the integrator. The process gap remains open.
- R-010: added on 2026-08-12 after P07 testing found manufacturer default passwords on the camera NVR and the cellular data gateway.

## 4. Treatment summary
- **Funded (approved by the Owner on 2026-08-31; about $21,000 one-time and $3,100 a year):**
  - Remote access rebuild: remote access tool business plan with named accounts and MFA (about $1,400 a year) and integrator setup (about $2,000)
  - Firewall rule rebuild and removal of the always-on router path: about $2,500 of integrator labor
  - Replacement HMI PC with a supported operating system and HMI software upgrade: about $9,500 (integrator, due 2027-03-31)
  - OT backup copies: 2 encrypted drives and integrator time to collect PLC, HMI, governor, and exciter copies and run the first restore test: about $1,700
  - OT-only engineering laptop: about $1,600
  - Independent assessment and policy work in 2026 (P07, P06): about $3,000
  - Industrial control system security course for the Controls and Electrical Technician: about $400
  - Hoist house lock change and key inventory: about $300
  - Annual security awareness training for 7 people: about $500 a year
  - Quarterly integrator check of OT component versions against manufacturer advisories: about $1,200 a year
- **Accepted:** R-014 (Low; cellular outages have been short and the monitoring service alerts when the gateway goes offline) and R-021 (Low; office laptops are encrypted).
- **Contract actions:** security and incident notice terms with the integrator (R-003) and the monitoring vendor (R-018, R-023) at renewal by 2026-12-31.
- **Regulatory actions:** a short site security plan with this SSP as its cyber section, and a brief Security Assessment built from this register, ready for the next FERC dam safety inspection (R-008). Neither is required for Group 3; both are highly recommended (Rev. 3A 3.3.3) and answer the FERC engineer's 2025 recommendation.

## 5. Approval
- Owner and General Manager: approved all treatment plans, the two acceptances, and the budget on 2026-08-31. No High risk was accepted.
- Next full review: July 2027, or sooner after a major change (for example, the HMI replacement or any proposal to let the monitoring service send commands) or an incident.

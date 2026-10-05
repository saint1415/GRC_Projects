# Risk Register Report: Cris Santos Company | Chemical | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical maker) |
| Size tier | Micro (7 employees) |
| Vertical | Chemical |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Benchmark | CFATS RBPS 8 (C-CHEMICAL-R01), voluntary; NIST CSF 2.0 with SP 800-82 Rev. 3 for OT |
| Prepared | 2026-07-24 by the Office Manager (Security Coordinator) with the Operations Manager, the MSP lead technician, and the control system integrator |
| Updated | 2026-08-11 (R-011 added from P07 testing); 2026-08-31 (R-020 and R-021 accepted; R-023 closed) |
| Approved | 2026-08-31 by the Owner and President |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors: every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-12), the site, and the vendors that run or reach those systems: the control system integrator, the MSP, the accounting and inventory vendor, the SDS service vendor, the backup vendor, the payroll vendor, and the ERI provider.

**What makes this business different from an office.** A cyber event here can move a dosing pump. The register therefore rates safety impact alongside cost, and it treats the integrator's remote access as a safety risk, not only an IT risk.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. A High risk that could injure a person is never accepted.

This is the company's first documented security risk assessment. The emergency action plan and the 2009 CFATS Top-Screen were reviewed for context, but neither rates cyber risk.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), CISA's RBPS 8 security measures, and interviews with all 7 employees, the MSP lead technician, and the integrator (2026-07-13 to 2026-07-24, site walkthrough 2026-07-15).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a company with about $4,400 of shipments a day, a week without blending or shipping is High, and an event that could injure people in the blend room is High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 16 |
| Low | 4 |
| **Total** | **23** |

Status: 12 In progress, 8 Open, 3 Closed (R-023 treated; R-020 and R-021 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Attacker uses the integrator's shared portal login to change a T-1 dose or alarm limit | High | Gateway off except for watched sessions; named portal accounts with MFA; remote desktop service off; session alerts | Operations Manager | 2026-10-31 |
| R-002 | Ransomware spreads from the office over the flat network to the HMI PC | High | HMI on its own firewall segment; allowlisting; phishing training; supported HMI PC in 2027 | Operations Manager | 2026-12-31 |
| R-005 | PLC program, HMI project, or recipes cannot be restored | High | Current program with checksums; weekly offline export; restore test on spare hardware | Operations Manager | 2026-12-15 |
| R-007 | Compromise of the integrator reaches the PLC and HMI | Moderate | Security terms, incident notice, and a response commitment in the integrator agreement | Owner and President | 2026-12-31 |
| R-016 | Compromise of the MSP's remote tool reaches every computer | Moderate | Yearly MSP review; incident notice and recovery commitment in the contract | Owner and President | 2026-12-31 |
| R-014 | A release during a cyber incident is reported late | Moderate | Printed call list at the exits and dock; cyber case in the next drill | Operations Manager | 2026-09-30 |

**The common theme is the batch control system's exposure.** One shared login reaches the PLC from the internet (R-001), the HMI PC is reachable from every office computer and, until fixed, from the guest Wi-Fi (R-002, R-011), and nothing can be restored if it is damaged (R-005). The treatments for these three also reduce R-003, R-006, R-007, and R-010.

**Risks that were fixed or found during the work:**
- R-004 and R-017: the former bookkeeper's accounting login was disabled on 2026-07-16, the day it was found. The accounting audit log showed no sign-in after the bookkeeper's last day. The process gap remains open.
- R-011: added on 2026-08-11 after P07 testing found that the guest Wi-Fi is not separated and that the HMI's remote desktop service answered from a guest device.
- R-023: the operator hired on 2026-04-20 completed DOT security awareness training on 2026-08-14, after the gap analysis found the 90-day deadline had passed. The risk is closed; the onboarding step is in POL-02 B.4.

## 4. Treatment summary
- **Funded (2026 Q3 and Q4, approved by the Owner; about $11,700 one-time and $1,100 a year):**
  - Integrator project: named portal accounts with MFA, remote desktop service off, named HMI logins, HMI audit trail, application allowlisting, configuration baseline with checksums, backup, and restore test: about $4,500 one-time
  - Spare panel PC for the HMI, kept on the shelf for restore tests and recovery: about $1,800 one-time
  - HMI network segment and guest Wi-Fi separation by the MSP: about $900 one-time
  - MSP project time for MFA on administrator logins, desktop encryption, and the first restore test: about $1,000 one-time
  - Independent assessment and policy work in 2026 (P07, P06): about $3,500 one-time
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Backup upgrade to 90 days of immutable versions: about $600 a year
- **Accepted:** R-020 (Moderate, accepted by the Owner: shipping continues on paper during an internet outage), R-021 (Low: laptops are encrypted).
- **Contract actions:** integrator agreement (R-007) and MSP contract (R-016) at renewal, by 2026-12-31.

## 5. Approval
- Owner and President: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (a new raw material on a screening list, a second peroxide tote connected, write-back switched on for the AI feature, or a new HMI PC) or an incident.

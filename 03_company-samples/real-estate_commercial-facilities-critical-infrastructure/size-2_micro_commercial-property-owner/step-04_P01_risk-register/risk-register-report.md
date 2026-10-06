# Risk Register Report: Cris Santos Company | Commercial Facilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| Size tier | Micro (7 employees) |
| Vertical | Commercial Facilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Benchmark | CISA CPG 2.0 (voluntary), adopted 2026-07-15 |
| Prepared | 2026-07-31 by the Property Manager (security and privacy lead) with the MSP lead technician and the Building Engineer |
| Updated | 2026-08-12 (R-022 and R-024 added from P07 testing) |
| Approved | 2026-08-31 by the Managing Member |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors: the building systems in the SSP boundary (BAS, access control and video, property networks), the business SaaS (productivity suite, property management system, payroll, tenant screening), the card terminal, and the outside parties that touch them: the MSP, the controls contractor, the security integrator, the platform vendor, and the backup vendor. Systems are listed in `../00_company-facts.md` section 3.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Property Manager may accept.
- Moderate: only the Managing Member may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Managing Member approves a dated treatment plan instead. Risks that could leave an entrance uncontrolled or a building without cooling for more than a day are never accepted at High.

This is the company's first risk assessment. Before July 2026 there was no written record of security risks or decisions.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the cloud mapping (P04), CPG 2.0, and interviews with all 7 employees, the MSP lead technician, and the controls contractor's service technician (2026-07-20 to 2026-07-31), plus walkthroughs of both properties on 2026-07-22.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a company with about $3,000 of revenue a day, a week without cooling at Property A, an entrance that cannot be secured at night, or a breach notice to every guarantor is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 15 |
| Low | 5 |
| **Total** | **24** |

Status: 9 In progress, 13 Open, 2 Closed (R-019 and R-020 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware through the controls contractor's remote-desktop tool encrypts the BAS workstation | High | Approved remote access service with named accounts, MFA, per-session approval, and recording; EDR | Building Engineer | 2026-10-31 |
| R-002 | The BAS workstation and controller programs cannot be restored | High | Immutable 90-day backup; controller program copies; restore test, then quarterly | Building Engineer | 2026-12-31 |
| R-003 | Phishing-led ransomware spreads over the flat Property A network to building devices | High | Building-device network segments; EDR with after-hours alerting; phishing training | Property Manager | 2026-12-31 |
| R-005 | Takeover of a platform administrator account unlocks doors or issues credentials | High | MFA on every administrator; remove the integrator's standing account; monthly change review | Property Manager | 2026-09-30 |
| R-004 | Guarantor files taken in an attack; Florida breach notice to about 60 people | Moderate | Restricted folder outside desktop sync; purge; stop emailing applications | Tenant Services and Leasing Coordinator | 2026-10-31 |
| R-022 | Supervisory controller accepts the manufacturer default password | Moderate | Unique passphrase; commissioning check | Building Engineer | 2026-09-15 |

**The common theme is the way in.** Three of the four High risks are about how someone gets into the building systems: an always-on contractor tool (R-001), a flat network (R-003), and single-factor administrator accounts (R-005). The fourth (R-002) decides how long the building runs by hand afterward. The same few fixes (MFA everywhere, segmentation, tested backups) also lower R-008, R-009, R-021, R-022, and R-024.

**Risks fixed or found during the work:**
- R-016: the face match trial was paused on 2026-07-24, two days after the walkthrough found it. The P10 assessment decides its future.
- R-006: the 51 unused credentials were sent to tenant contacts for confirmation on 2026-07-28; 38 were disabled by 2026-08-07. The process gap remains.
- R-022 and R-024: added on 2026-08-12 after P07 testing found the supervisory controller and the Property B router accepting factory default passwords.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Managing Member; about $8,100 one-time and $3,400 a year):**
  - Remote access service for the controls contractor, run by the MSP: about $600 a year
  - Property A building-device segment (managed switch and firewall rules): about $1,800 one-time
  - MSP-managed business router for Property B: about $400 one-time and $300 a year
  - Immutable 90-day backup: about $700 a year
  - MSP-managed EDR on the 6 office computers and the BAS workstation: about $1,300 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Controls contractor time for controller program copies, password changes, a rebuild checklist, and manual procedures: about $1,500 one-time
  - A spare laptop pre-imaged by the MSP: about $900 one-time
  - Independent assessment and policy work in 2026 (P07, P06): about $3,500 one-time
- **Accepted:** R-019 (Low; phone hotspot covers platform administration) and R-020 (Low; doors keep working for 72 hours on cached credentials).
- **Contract actions:** security addendum with 24-hour incident notice for the MSP, the controls contractor, and the security integrator (R-010, R-011) by 2026-12-31.

## 5. Approval
- Managing Member: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, a new building system, a new property, or turning on any video analytics feature) or an incident.

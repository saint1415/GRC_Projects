# Risk Register Report: Cris Santos Company | Dams | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (owner and operator of the fictional Cypress Fork Hydroelectric Project, Florida) |
| Size tier | Small (187 employees) |
| Vertical | Dams (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | The threat and risk-management elements FERC expects in the Security Assessment and Security Plan (Security Program for Hydropower Projects Rev. 3A, sections 3.2, 6.3, 7.3) and Form 3 Questions 23 and 29-32 |
| Prepared | 2026-07-24 by the IT Manager and the Controls Engineer, with the Compliance and Security Coordinator |
| Approved | 2026-08-31 by the Vice President of Operations (Moderate and below) and the President (High) |

## 1. Scope and risk framing
**Scope.** The whole company, tied to its key systems: the Plant Control and Dam Monitoring System (PCDMS, the P02 system), the corporate network and SaaS services, the cloud tenant, and the business processes in the BIA (P05). See `../00_company-facts.md` sections 3 and 4.

**What makes this register different from an office business.** The worst outcomes are physical. An attacker who can operate the spillway gates can release water toward a town of about 2,400 people inside the EAP inundation zone (the dam is High hazard potential under 18 CFR 12.3(b)(13)(i)). Impact ratings therefore follow the BIA safety category first and cost second.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager or the Controls Engineer may accept.
- Moderate: the Vice President of Operations may accept, with a treatment plan or a documented reason.
- High and Very High: only the President may accept, and only temporarily with a dated treatment plan.
- Any risk that could cause an uncontrolled release of the reservoir may not be accepted at High. It must be reduced.

This is the company's first documented cyber risk assessment. The 2017 Security Assessment (prepared by the prior licensee) covered physical security only.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the FERC Security Program threat scenarios that a Vulnerability Assessment must consider (Rev. 3A 5.3: insider, vandalism and theft, armed groups, vehicle and boat attack, and a SCADA controls attack), the BIA, the Section 9 determination and gap analysis (P03), and interviews with the Plant Manager, Chief Dam Safety Engineer, Operations Supervisors, and Compliance and Security Coordinator.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were rated and combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05). Uncontrolled release toward the downstream town is Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 5 |
| Moderate | 19 |
| Low | 9 |
| **Total** | **33** |

No risk rated Very High. R-001, R-003, and R-014 have Very High impact, but their likelihood is Moderate because the control room is staffed 16 hours a day and local gate panels can override remote commands.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Stolen on-call VPN password plus shared HMI account used to open spillway gates | High | MFA on the OT VPN; named HMI accounts; remote gate commands disabled until MFA is live | Controls Engineer | 2026-11-30 |
| R-005 | Corporate ransomware crosses into OT through the dual-homed engineering workstation | High | Remove the dual-homed interface; allow-list OT firewall rules | Controls Engineer | 2026-10-31 |
| R-009 | Control system cannot be rebuilt: stale, untested PLC and HMI backups | High | Offline and cloud backups after every change; annual restore test; written OT recovery procedure | Controls Engineer | 2026-12-31 |
| R-014 | Current or former operator misuses the shared operator password | High | Rotate shared passwords now; named accounts; OT access on the termination checklist | Plant Manager | 2026-10-15 |
| R-003 | SCADA integrator's always-on connection used as an entry point | High | On-demand, approved, MFA-protected vendor sessions with weekly log review | Plant Manager | 2026-12-31 |
| R-015 | FERC action over outdated Security Plan and Security Assessment and an inaccurate 2025 certification letter | Moderate | Corrected statement and plan and schedule to the Regional Engineer by 2026-09-30 | Vice President of Operations | 2026-11-15 |
| R-016 | Cyber attack on gates not escalated to the EAP or reported under 18 CFR 12.10 | Moderate | P08 runbook; cyber triggers in the Internal Emergency Response sub-element; tabletop | Chief Dam Safety Engineer | 2026-11-30 |

**Common theme.** Four of the five High risks run through **one path**: remote access to the control network. The OT VPN has no MFA, the HMI uses one shared operator account, vendors hold always-on connections, and the engineering workstation bridges the corporate network into OT. Closing that path (POAM-001 to POAM-004 in P07) also lowers R-002, R-004, R-007, R-010, and R-028. The fifth High risk (R-009) is about recovery: today the company could not quickly rebuild its gate and unit controls from known-good copies.

**Added after testing.** R-011 and R-012 were added on 2026-08-07 after the P07 assessor found manufacturer default passwords on 2 spillway gate local panels and on the 2 upstream gauge cellular modems (gap 15). Both passwords are being changed first, with due dates of 2026-09-30 and 2026-10-15.

## 4. Treatment summary
- **Funded (2026 Q4 to 2027 Q2 budget, $265,000, approved by the President on 2026-08-31):**
  - OT remote access redesign: jump host, MFA, named accounts, on-demand vendor sessions, session recording ($48,000)
  - OT firewall rule rebuild and removal of the dual-homed workstation ($12,000 integrator labor)
  - OT logging and a passive OT network monitoring sensor feeding the cloud log workspace ($46,000 first year)
  - SCADA platform upgrade to a supported operating system ($95,000, 2027 Q2)
  - First OT vulnerability assessment by an outside firm ($28,000)
  - OT backup and recovery: offline media, spare PLC for restore tests ($14,000)
  - Cameras for the spillway blind spot and intake; satellite phone and cellular failover ($22,000)
- **Accepted:**
  - R-021 (offtaker telemetry): Low; revisit at the next RTU upgrade.
  - R-022 (identity provider administrator takeover): Low; hardware keys already in place.
- **Shared or transferred:** R-019 (hurricane damage to generation) through property and business interruption insurance; R-031 (reservation vendor breach) through contract terms.
- **Regulatory actions:** the corrected statement to the FERC Regional Engineer (R-015) and the updated Security Assessment and Security Plan with an IT/SCADA section must be ready before the 2026-11-17 inspection and the 2026-12-31 certification letter.

## 5. Approval
- Vice President of Operations: approved Moderate and Low treatments and acceptances, 2026-08-31.
- President: approved the High-risk treatment plans and the $265,000 budget, 2026-08-31. No High risk was accepted.
- Next full review: July 2027, and each year before the Annual Security Compliance Certification Letter, or sooner after a major change (such as the SCADA upgrade) or an incident. The threat part of the review will be coordinated with local law enforcement. FERC requires that step only for Group 1 Vulnerability Assessments (Rev. 3A 5.4); the company adopts it voluntarily and it answers Form 3 Question 23a.

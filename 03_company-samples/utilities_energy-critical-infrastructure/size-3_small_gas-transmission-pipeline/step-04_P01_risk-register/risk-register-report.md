# Risk Register Report: Cris Santos Company | Energy | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (intrastate natural gas transmission pipeline operator) |
| Size tier | Small (60 employees) |
| Vertical | Energy (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT threat sources and predisposing conditions from NIST SP 800-82 Rev. 3, Appendix C |
| Prepared | 2026-08-14 by the IT Manager with the Gas Control Manager and SCADA Engineer; R-008 added 2026-08-26 |
| Approved | 2026-09-24 by the President (Moderate and below) and the majority owner (High) |

## 1. Scope and risk framing
**Scope.** The whole company: the Pipeline SCADA and Gas Control System (PSGCS, the SSP system in P02), business IT, the cloud tenant, SaaS services, field sites, and the vendors that support them (`../00_company-facts.md` section 3). Business processes and impact levels come from the BIA (P05).

**What makes this register different from an office business.** The worst outcomes are physical: overpressure, an undetected release, or loss of gas supply to about 140,000 homes and businesses and a power plant. Cyber risks are rated on those consequences, not only on data loss.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager (business IT) or the Gas Control Manager (OT) may accept.
- Moderate: the President may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. A risk that could cause loss of pipeline control or public harm may not be accepted at High.

This is the company's first risk assessment that covers OT. The 2024 review covered business IT only.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E and SP 800-82 Rev. 3 Appendix C (OT threats and vulnerabilities), the BIA, interviews with the Gas Control Manager, SCADA Engineer, Field Operations Manager, and Commercial Manager, and the gap analysis (P03).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). Safety and supply impacts set the rating when they are the worst case.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 5 |
| Moderate | 19 |
| Low | 7 |
| **Total** | **31** |

No risk is rated Very High, mainly because the IT/OT firewall and the separate OT domain lower the likelihood that a business IT attack reaches the pipeline. Six risks carry a Very High impact. They stay out of the Very High level only because of their likelihood ratings.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware on business IT leads to a precautionary pipeline shutdown | High | Incident response plan with an isolate-and-operate decision tree; OT monitoring; immutable backups | IT Manager | 2026-12-31 |
| R-002 | Ransomware crosses the DMZ through the shared jump host into SCADA | High | Separate vendor and staff jump hosts; on-demand vendor sessions with MFA; HMI allowlisting | SCADA Engineer | 2027-03-31 |
| R-003 | Attacker uses the SCADA integrator's remote access | High | Named accounts with MFA; access enabled per session; recording; contract terms | SCADA Engineer | 2026-11-30 |
| R-004 | SCADA backups lost with production | High | Monthly offline copy; annual bare-metal restore test | SCADA Engineer | 2026-12-31 |
| R-012 | Wrong or late shutdown decision because no criteria exist | High | Cyber annex to the emergency plan (192.615) with the P08 decision tree | VP Operations | 2026-11-30 |
| R-009 | Unverified SCADA display change misleads a controller | Moderate | Written SCADA change procedure with point-to-point verification (192.631(c)(2), (f)) | Gas Control Manager | 2026-10-31 |
| R-010 | Safety alarm set-point wrong (verification overdue) | Moderate | Complete verification; track the 15-month interval (192.631(e)(3)) | Gas Control Manager | 2026-10-31 |

**The five High risks share one theme: the company cannot yet prove that its OT is isolated and recoverable during a cyber attack.** It cannot see OT traffic (R-005), its vendor path into SCADA is weak (R-002, R-003), its SCADA backups are exposed (R-004), and it has no rules for deciding between isolation, manual operation, and shutdown (R-001, R-012). A Colonial-style precautionary shutdown is the likely result, even if the attack never touches OT. Fixing these also reduces the Moderate risks R-005, R-006, R-007, R-011, R-016, R-019, and R-029.

R-008 was added on 2026-08-26 after control assessment testing (P07) found default passwords on three cellular gateways at remote valve sites. The passwords are scheduled to be changed by 2026-09-30 (POAM-012).

## 4. Treatment summary
- **Funded (2026 Q4 to 2027 Q2 budget, $86,000):**
  - Passive OT network monitoring sensor with MSP alerting ($38,000 per year)
  - Secure remote access redesign: separate vendor jump host, MFA, session recording ($12,000)
  - Spare SCADA server for restore tests and offline backup media ($9,000)
  - Immutable cloud backup retention ($5,000 per year)
  - USB media scanning station and HMI allowlisting ($8,000)
  - Second-carrier cellular SIMs at 4 critical sites ($4,000 per year)
  - Incident response retainer and tabletop facilitation ($10,000)
- **Separate 2027 capital project:** SCADA software and HMI operating system upgrade (R-007), with an API RP 1165 review as 192.631(c)(1) requires when a SCADA system is expanded or replaced.
- **Accepted:**
  - R-022: Low; badge access and CCTV already in place
  - R-030: Low; tablets are encrypted and can be wiped remotely
- **Contract actions:** security terms, incident notice, and remote access rules for the SCADA integrator, MSP, telecom carrier, and anomaly model vendor (R-003, R-016, R-026), due by 2026-12-31.

## 5. Approval
- President: approved Moderate and Low treatments and acceptances, 2026-09-24.
- Majority owner: approved the High-risk treatment plans and the budget, 2026-09-24.
- Next full review: August 2027, sooner after a major change (including the SCADA upgrade or a TSA designation) or an incident.

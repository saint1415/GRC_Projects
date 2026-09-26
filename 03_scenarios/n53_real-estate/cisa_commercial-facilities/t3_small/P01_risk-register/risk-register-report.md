# Risk Register Report: Cris Santos Company | Commercial Facilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| Size tier | Small (60 employees) |
| Vertical | Commercial Facilities (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Benchmark served | CISA CPG 2.0 goals 1.B (cybersecurity oversight) and 2.B (track risk response in a risk register); Fla. Stat. 501.171(2) reasonable measures |
| Prepared | 2026-07-24 by the IT Manager with the Director of Engineering and the Security Manager |
| Approved | 2026-08-31 by the COO (Moderate and below) and the majority owner (High) |

## 1. Scope and risk framing
**Scope.** The whole company, tied to its key systems: the Building Automation and Access Control System (BAACS, the SSP system in P02), the corporate SaaS and cloud tenant, the card terminals, and the vendors that operate or support them (`../scenario-facts.md` section 3). The business processes are those in the BIA (P05).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the COO may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. Risks that could leave a building without working doors or cooling at High are not acceptable.

This is the company's first documented cybersecurity risk assessment. Building systems had been treated as engineering equipment, not as IT, so they had never been assessed.

## 2. Method
1. **Identify.** Threat sources and events were identified from SP 800-30 Appendices D and E, the BIA, the CPG 2.0 "risk addressed" statements, SP 800-82 Rev. 3 OT threat guidance, interviews with the Director of Engineering, chief engineers, Security Manager, and Controller, and walkthroughs of all three properties (2026-07-15 to 2026-07-17).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05), including occupant safety and rent abatement.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables with a script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 22 |
| Low | 9 |
| **Total** | **34** |

Treatments: 30 Mitigate, 3 Accept, 1 Avoid.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware through the BAS integrator's remote-support tool | High | Remote access gateway with named accounts, MFA, and per-session approval | Director of Engineering | 2026-10-31 |
| R-002 | BAS cannot be restored after an attack or failure | High | Immutable backups in a separate account; controller programs held by the company; quarterly restore tests | IT Manager | 2026-12-31 |
| R-003 | Ransomware spreads from the corporate network into OT | High | OT segments at all three properties with deny-by-default rules | IT Manager | 2027-03-31 |
| R-004 | Internet-exposed NVR at Property B exploited | Moderate | Port forward removed 2026-07-17; named cloud viewing accounts | IT Manager | 2026-09-30 |
| R-007 | Default passwords on BACnet field controllers | Moderate | Change all defaults; commissioning checklist | Director of Engineering | 2026-09-30 |
| R-013 | Card data on paper and in email; SAQ P2PE eligibility at risk | Moderate | Stop paper capture; purge and block card data in email | Controller | 2026-09-30 |

The three High risks share one theme: **the building systems could be taken over and could not be rebuilt.** The integrator's always-on remote tool is an open door into the BAS (R-001), the OT devices share networks with office PCs (R-003), and the backups would not survive the attack (R-002). Fixing these three also reduces eight related Moderate risks (R-004, R-007, R-008, R-009, R-015, R-020, R-021, R-031) and one Low risk (R-029).

R-007 was updated on 2026-08-07 after control assessment testing (P07) found manufacturer default passwords on 12 field controllers at Property B and on 2 NVRs.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $96,000):**
  - Remote access gateway with MFA and session recording for integrators ($14,000 a year)
  - OT segmentation at Properties B and C, including firewall licenses and integrator labor ($38,000)
  - Backup redesign with an immutable separate account ($7,000 a year)
  - BAS server OS and software upgrade by the integrator ($24,000)
  - Log collection by the MSP's log service ($9,000 a year)
  - Phishing exercises and OT role training ($4,000 a year)
- **Accepted:**
  - R-017: Low; doors run on cached credentials and guards cover entrances
  - R-030: Low; vendor-hosted, and the line of credit covers a short delay
  - R-032: Low; MFA already in place
- **Avoided:** R-025: face verification is not approved (P10).
- **Contract actions:** security addendum for the BAS integrator, the access control and video integrator, and the MSP (R-015, R-016), and retention and breach-notice terms for the visitor management vendor (R-012), due by 2026-12-31.

## 5. Approval
- COO: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Majority owner: approved the High-risk treatment plans and the budget, 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, OT segmentation cutover) or an incident.

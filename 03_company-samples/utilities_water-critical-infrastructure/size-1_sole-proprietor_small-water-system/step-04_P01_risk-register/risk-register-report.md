# Risk Register Report: Cris Santos Company | Water and Wastewater Systems | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (small community water system, 330 persons served) |
| Size tier | Sole Proprietorship (owner-operator only, 0 employees) |
| Vertical | Water and Wastewater Systems |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also serves as | The cyber part of a **voluntary** risk and resilience review. SDWA section 1433 does not require one at 330 persons (P03), but its elements are a sound checklist |
| Prepared | 2026-07-24 by the owner-operator, with the on-call IT technician (confidentiality agreement since 2026-07-15) |
| Risk owner and approver | Owner-operator (owner, licensed operator, security lead, and risk acceptor for every risk) |
| Approved | 2026-08-31 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-08, the well house, paper records, and the contracted services (relief operator, controls integrator, IT technician, laboratory, SaaS vendors). Processes come from the BIA (P05).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, three fixed rules apply:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Any risk that could leave customers with under-disinfected water is never accepted at High.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the voluntary 300i-2(a)(1)(A) elements (P03), and a walk through the panel, portal, router, laptop, and phone with the IT technician.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale, combined with **Table G-5**. The adverse-impact rating credits the safeguards that do not depend on any computer: the mechanical stroke cap on the chlorine pump, the hand-off-auto switches, the daily grab sample, and the dialer alarms.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (public health and regulatory impact dominate).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 2 |
| Moderate | 7 |
| Low | 6 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Portal takeover with the owner's reused password; chlorine feed stopped | High | App-based MFA, unique passphrase, named accounts | Owner-operator | 2026-09-15 |
| R-002 | Integrator's always-enabled account misused | High | Disable between approved sessions; MFA; contract terms | Owner-operator | 2026-10-31 |
| R-003 | Router administrable with its label password | Moderate | New password and firmware; remote administration already off | Owner-operator | 2026-09-15 |
| R-004 | No owner-held copy of the PLC program | Moderate | Two copies of the current program; restore steps | Owner-operator | 2026-10-15 |
| R-008 | Cyber-caused loss of disinfection not treated as a reporting trigger | Moderate | P08 runbook and notification matrix in the well house binder | Owner-operator | 2026-09-30 |
| R-005 | Owner unavailable; nobody else can run the plant by hand | Moderate | Manual-operation sheet; emergency relief coverage | Owner-operator | 2026-12-31 |

**Both High risks run through the same door: the cloud remote access portal.** A setpoint typed into the portal changes the chlorine dose at the well house. Turning on MFA costs nothing and takes an afternoon. Disabling the integrator's account between sessions costs one phone call each time support is needed. These two changes do more for public health than anything else in this register.

**Why the risk is not higher.** The plant was built so that the computer is not the last line of defense. The chlorine pump cannot exceed its mechanical stroke setting, the dialer alarms do not depend on the portal, and the owner measures the residual by hand every day. Those safeguards are why R-001's adverse-impact likelihood is High rather than Very High, and why R-012 (intruder at the HMI) can be accepted.

## 4. Treatment summary
- **Free fixes first (by 2026-09-15):** portal MFA and named accounts, integrator account disabled between sessions, router password and firmware, standard laptop account, password manager.
- **Low-cost work (by 2026-10-31):** program copies from the integrator (one paid visit), integrator contract terms, offline customer contact list, billing vendor's SOC 2 report.
- **People and procedures (by 2026-12-31):** P08 walkthrough with the relief operator (2026-09-30), manual-operation sheet, emergency relief coverage, sealed access envelope, cybersecurity course (2026-11-30).
- **Accepted (Low):** R-011 (hurricane; the owner can run the plant by hand on the generator, as in 2024) and R-012 (intruder at the HMI; fence, lock, and door alarm).

## 5. Approval
Owner-operator, 2026-08-31: approved all treatment plans and the two acceptances. Next full review July 2027, or sooner after a change to the panel or portal, a new vendor, a hire, or an incident.

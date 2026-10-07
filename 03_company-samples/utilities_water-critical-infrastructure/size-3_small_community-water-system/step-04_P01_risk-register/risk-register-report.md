# Risk Register Report: Cris Santos Company | Water and Wastewater Systems | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (investor-owned community water system, 46,200 population served) |
| Size tier | Small (60 employees) |
| Vertical | Water and Wastewater Systems (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT risk framing from NIST SP 800-82 Rev. 3 section 4.1 |
| Also supports | The risk element of the SDWA section 1433 risk and resilience assessment (RRA), 42 U.S.C. 300i-2(a)(1)(A)(i)-(vi) |
| Prepared | 2026-07-24 by the IT Manager with the Operations Manager (R-031 added 2026-08-07) |
| Approved | 2026-08-31 by the General Manager (Moderate and below) and the majority owner (High) |

## 1. Scope and risk framing
**Scope.** The Water Treatment SCADA System (WTSS, P02), the business processes in the BIA (P05), and the business and cloud systems that hold customer data, RRA and ERP contents, or water quality data (`../00_company-facts.md` section 3).

**How this register relates to the RRA.** SDWA section 1433 requires an assessment of the risk to the system from malevolent acts and natural hazards, and of the resilience of its assets, including "electronic, computer, or other automated systems (including the security of such systems)" (42 U.S.C. 300i-2(a)(1)(A)(ii)). The June 2026 RRA review carried forward a 2021 cyber checklist (P03 gap G-004). This register is the cyber and automated-systems addendum to that RRA. Its High and Moderate risks feed the revised emergency response plan (ERP) due for certification by 2026-12-26.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager or Operations Manager may accept.
- Moderate: the General Manager may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. **Risks that could affect public health through treatment or chemical feed are not accepted at High.**

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, EPA's baseline threat information for community water systems, the BIA, interviews with both Chief Plant Operators, the SCADA and Instrumentation Technicians, and the Customer Service and Billing Manager, and the gap analysis (P03). Natural hazards are included because section 1433 requires them; hurricanes and flooding dominate in Florida.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Engineered safeguards that do not depend on SCADA (hardwired chemical pump stroke limits, independent analyzer alarms, manual operation) lower the likelihood of adverse impact for several OT risks.
3. **Rate impact.** Impact was rated with **Table H-3** using the BIA impact categories (P05), including public health and safety.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 5 |
| Moderate | 17 |
| Low | 10 |
| **Total** | **32** |

Threat source types: 19 adversarial, 6 structural, 5 accidental, 2 environmental.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | HMI takeover through the integrator's remote desktop agent, with a chemical setpoint change | High | Remove the always-on agent; vendor access only through a gateway with MFA, per-session approval, and recording | Operations Manager | 2026-10-31 |
| R-002 | On-call VPN access to the HMIs with a stolen or guessed password | High | Patch the VPN; MFA; land sessions on an OT DMZ jump host | IT Manager | 2026-10-31 |
| R-006 | Only copy of PLC logic and HMI projects destroyed | High | Offline, encrypted backups monthly and after each change | Operations Manager | 2026-10-15 |
| R-008 | Malicious PLC logic download while PLCs sit in remote-program mode | High | Key switches to RUN; approval procedure; logic comparison | Operations Manager | 2026-10-31 |
| R-003 | Ransomware spreads from the business network to SCADA | High | OT DMZ, remove the dual-homed historian, deny-by-default rules | IT Manager | 2027-03-31 |
| R-016 | Tier 1 public notice missed after a cyber-caused treatment interruption | Moderate | OT cyber playbook in the ERP with the 24-hour notice decision point | Water Quality Supervisor | 2026-12-11 |
| R-017 | Revised ERP not certified by 2026-12-26 | Moderate | Project plan; RRA cyber addendum by 2026-11-13 | Operations Manager | 2026-12-11 |

The five High risks share one theme: **remote and network paths into the treatment process are open and unwatched.** Two remote access paths use passwords only (R-001, R-002), the OT network is flat and bridged to the business network (R-003), PLCs accept program changes remotely (R-008), and there is no offline copy of the control logic to recover with (R-006). None of the five is rated Very High because operators can run the plants manually and because chemical pumps have hardwired limits that SCADA cannot override. Those engineered safeguards are the most important controls the company has, and the ERP must keep them.

Closing the five High risks also reduces seven Moderate risks (R-005, R-009, R-015, R-020, R-024, R-027, R-031) and two Low risks (R-007, R-021).

R-031 was added on 2026-08-07 after control assessment testing (P07) found internet-reachable web administration with default credentials on 4 cellular modems at well sites. The SCADA and Instrumentation Technicians disabled the web administration and changed the passwords on 2026-08-06, during fieldwork.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $142,000):**
  - Remote access gateway with MFA and session recording, and VPN replacement ($38,000)
  - OT DMZ and firewall redesign with the integrator ($44,000)
  - Passive OT network monitoring sensor and log forwarding ($32,000 first year)
  - Offline backup media and procedure for PLC and HMI files ($3,000)
  - Portable generator connections at 4 wells ($25,000)
- **Capital plan (2027):** SCADA server and engineering workstation upgrade to a supported operating system (R-005), WTP-2 panel elevation (R-011), radio refresh (R-004, 2028).
- **Accepted:**
  - R-004: Low, until the 2028 radio refresh
  - R-028 and R-029: Low, vendor outages with manual workarounds
  - R-030: Low
- **Contract actions:** security terms in the SCADA integrator contract at renewal (R-015), due 2027-01-31.
- **Free assistance to request:** EPA's Water Sector Cybersecurity Evaluation Program offers a no-cost assessment with a risk mitigation plan template. The Operations Manager will request one for 2026 Q4 to validate this register.

## 5. Approval
- General Manager: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Majority owner: approved the High-risk treatment plans and the budget, 2026-08-31.
- Next full review: July 2027, or sooner after a major change, a cyber incident, or a named storm that damages facilities. The next RRA five-year review is expected by June 30, 2031 (five years after the 2026 cycle deadline, 42 U.S.C. 300i-2(a)(3)(B)).

# Risk Register Report: Cris Santos Company | Water and Wastewater Systems | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (privately held community water system, 2,850 population served) |
| Size tier | Micro (7 employees) |
| Vertical | Water and Wastewater Systems (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT risk framing from NIST SP 800-82 Rev. 3 section 4.1 |
| Prepared | 2026-07-24 by the Office Manager (security and compliance coordinator) with the Chief Operator and the MSP lead technician |
| Updated | 2026-08-12 (R-023 added from P07 testing); 2026-08-31 (R-020, R-021, R-022 accepted) |
| Approved | 2026-08-31 by the Owner and General Manager |

## 1. Scope and risk framing
**Scope.** The business and its key vendors: the Water Treatment SCADA System (WTSS, P02), the functions in the BIA (P05), the SaaS and office systems in `../00_company-facts.md` section 3, and the contractors and vendors that operate or reach them (SCADA integrator, MSP, remote monitoring vendor, remote desktop tool vendor, billing vendor).

**Why this register exists at this size.** SDWA section 1433 does not require a risk and resilience assessment from a system serving 2,850 people (P03). The company did this work because the cyber insurer asked about its controls, because the Chief Operator had no answer to "what happens if someone gets into the HMI", and because a new subdivision may take the system past the 3,300-person threshold by about 2029. This register covers the same ground a section 1433 assessment would: malevolent acts and natural hazards, automated systems, monitoring, and chemical handling. It is the company's first written risk assessment.

**Risk tolerance and who can accept risk (POL-02 A.3):**
- Low and Very Low: the Office Manager or Chief Operator may accept.
- Moderate: only the Owner and General Manager may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. **A risk that could affect public health through chemical feed or treatment is never accepted above Low.**

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), CISA and EPA water-sector advisories on internet-exposed HMIs, and interviews with all 7 staff, the MSP lead technician, and the SCADA integrator (2026-07-21). Natural hazards are included because hurricanes are the company's most frequent emergency.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Engineered safeguards that do not depend on SCADA (the mechanical stroke limit on the hypochlorite pump, the analyzer's alarm relays to the dialer, and hand operation) lower the likelihood of adverse impact for the chemical feed risks.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories, including public health and safety. For a system of 2,850 people with one plant, an unsafe chemical dose reaching customers is rated Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

**Qualitative scales.** At the Micro tier the company uses the qualitative five-level scale only (Very Low to Very High), with no numeric scores.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 14 |
| Low | 5 |
| **Total** | **23** |

Threat source types: 12 adversarial, 6 structural, 4 accidental, 1 environmental.
Status: 14 Open, 6 In progress, 3 Closed (R-020, R-021, and R-022 accepted at Low).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | HMI takeover through the remote desktop tool, with a chlorine feed change | High | Turn off unattended access; named accounts with MFA; integrator sessions approved and watched | Chief Operator | 2026-09-30 |
| R-004 | PLC program or HMI project lost with no company copy | High | Offline encrypted copies, monthly and after every change; HMI computer image | Chief Operator | 2026-09-15 |
| R-006 | Altered logic downloaded to the PLC | High | Key switch to RUN; PLC program password; quarterly logic comparison | Chief Operator | 2026-10-31 |
| R-003 | Ransomware spreads from an office computer to the HMI computer | High | Separate OT network; guest Wi-Fi; managed malware protection on the HMI computer | Office Manager | 2026-11-30 |
| R-010 | Tier 1 notice late after a cyber-caused treatment problem | Moderate | Cyber trigger in the emergency plan; printed contact list each month | Chief Operator | 2026-10-31 |
| R-023 | Tank modem reachable from the internet with the default password (found in P07) | Moderate | Fixed 2026-08-12; move both modems to a private carrier plan | Chief Operator | 2026-10-31 |

**The common theme is remote access to a flat network.** One shared password opens the HMI from anywhere (R-001, R-002), the HMI computer sits on the same network as the office (R-003), the PLC accepts program changes from that network (R-006), and the company could not restore a trusted PLC program if it had to (R-004). None of the four is rated Very High because operators can run the plant by hand and because the hypochlorite pump's mechanical stroke limit and the analyzer's alarm relays work without SCADA. Those safeguards are the most important controls the company has; every change in this plan must keep them.

Treating the four High risks also reduces R-002, R-005, R-009, R-014, R-016, R-019, and R-023.

**Risks that were fixed or found during the work:**
- R-002: the risk interviews on 2026-07-21 found that a former operator who left in March 2026 still knew the shared remote desktop password. The Chief Operator changed it on 2026-07-22. The tool's connection history showed no sessions from unfamiliar devices since March, so the company recorded that no unauthorized access was found. The process gap remains open.
- R-023: added on 2026-08-12 after P07 testing found the elevated tank modem's web administration reachable from the internet with the default password. The integrator turned off web administration and changed the password on 2026-08-12.

## 4. Treatment summary
- **Funded (2026 Q3 and Q4, approved by the Owner; about $9,800 one-time and $3,900 a year):**
  - Remote access rebuilt with named accounts, MFA, and attended sessions (remote desktop tool business plan): about $900 a year
  - Integrator time for PLC and HMI exports, offline backup drives, key switch, PLC password, and patch testing: about $3,200
  - Small industrial firewall and MSP and integrator time to separate the OT network: about $4,500
  - Private network plan for the 2 cellular modems: about $480 a year
  - Security awareness training and phishing simulations for 7 people: about $500 a year
  - Password manager for the Owner, Office Manager, and Chief Operator: about $120 a year
  - Managed malware protection on the HMI computer through the MSP addendum: about $400 a year
  - Independent OT security assessment (P07) and policy work: about $2,100 one-time
  - MSP security review and restore tests: about $1,500 a year in MSP time
- **Free help to request:** EPA's Water Sector Cybersecurity Evaluation Program and Water Cybersecurity Assessment Tool, and CISA's vulnerability scanning for water utilities. The Chief Operator will enroll in CISA scanning by 2026-09-30 (P03 G-031).
- **Accepted:** R-020 (Low; padlocked remote sites checked weekly), R-021 (Low; the alarm dialer uses cellular), R-022 (Low; cash reserve).
- **Contract actions:** security terms for the SCADA integrator, the MSP (including the HMI computer), and the remote monitoring vendor by 2026-12-31 (R-014, R-016).

## 5. Approval
- Owner and General Manager: approved all treatment plans, the three acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (connecting the new subdivision, replacing the HMI computer, or moving the anomaly detection feature beyond advisory use), a cyber incident, or a named storm that damages facilities.

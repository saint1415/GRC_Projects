# Risk Register Report: Cris Santos Company | Transportation and Warehousing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed marine cargo terminal operator: Terminal 1 container, Terminal 2 multipurpose, off-dock depot) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Transportation and Warehousing (NAICS 488320) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | Input to the Cybersecurity Assessment required by 33 CFR 101.650(e)(1) (risk posed by each digital asset, due 2027-07-16) and to the cyber items in each Facility Security Assessment (33 CFR 105.305(c)(1)(v)) |
| Prepared | 2026-07-31 by the Security Manager (alternate CySO) and the vCISO; R-045 added 2026-09-15 from the P10 portfolio review |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |
| Handling | Describes security vulnerabilities of MTSA-regulated facilities. Handle as SSI (49 CFR 1520.5(b)(5); POL-04 4.2) |

## 1. Scope and risk framing
**Scope.** Every business unit in the BIA (P05): Terminal 1, Terminal 2, the depot, the commercial group and corporate support. Systems are SYS-01 to SYS-15 in `../00_company-facts.md`, including the crane and yard equipment OT (SYS-03), security systems (SYS-09), the 27 vendors with access (SYS-15) and the AI portfolio (P10). Impact values come from the BIA; vulnerabilities come from the 15 gaps in the scenario facts, the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-15.

| Area | Appetite | Statement and measure |
|---|---|---|
| Safety of people on the terminals | **Very low** | No cyber or technology risk that could plausibly cause injury (crane or RTG motion, mis-stowed heavy or hazardous cargo, responders unable to find hazardous cargo) is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: safety-linked risks above Low (7 today: R-002, R-003, R-014, R-028, R-030, R-042, R-050; target 0 by 2027-12-31) |
| MTSA security and Coast Guard compliance | **Low** | Subpart F measures must be in place and documented before the Cybersecurity Plan is submitted (target 2027-05-28). Duties already in force (incident reporting, records, training) must have no open gap after 2026-12-31. Measure: open P03 rows that are in force or overdue |
| Availability of terminal operations | **Low** | Recovery capability must meet the BIA RTO for every High-criticality process (P05). Measure: every High process has a passed recovery test in the last 12 months (0 of 6 today) |
| Cargo integrity and customs status | **Low** | No container may leave a gate on a customs hold because of a system or data failure. Measure: wrongful releases (0 in 2026) and hold overrides without two-person approval |
| Third parties | **Moderate**, with conditions | Vendors are essential (TOS, OEMs, MSSP, cloud), but no vendor gets remote access to OT except through the privileged remote access service, and every vendor with access has a notification clause by 2027-03-31 |
| Innovation and AI | **Moderate** | AI is welcome in planning, maintenance and security operations, but only in advisory mode and only through the P10 process. No AI output may move equipment without a human decision |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the marine terminal threat themes in the Transportation and Warehousing overlay (ransomware against port operations, vendor remote access to OT, cargo theft through data manipulation), the BIA, interviews with every process owner and both FSOs, the gap analysis (P03) and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values (about $275,000 of revenue a day across the sites, plus longshore standby of about $5,000 an hour per vessel worked), used for the enterprise roll-up. The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 7 |
| Moderate | 33 |
| Low | 10 |
| Very Low | 0 |
| **Total** | **51** |

Treatments: 46 Mitigate, 5 Accept (R-024, R-038, R-044, R-047, R-051). Status: 22 Open, 24 In progress, 5 Accepted.

Cyber insurance ($15 million aggregate limit, $500,000 retention) transfers part of the financial exposure for R-001, R-004, R-035 and R-037. It is not recorded as the treatment for any risk, because it does not reduce the likelihood of harm to people or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware stops the TOS and gates at both terminals and the depot | Very High | Privileged access management; T2 OT zone; tested failover and hourly isolated snapshots; T2 image backups; runbook exercised | Director of IT and Cybersecurity (CySO) | 2027-03-31 |
| R-002 | Attacker moves from the T2 flat network into mobile harbor crane controllers | High | T2 OT zone with an industrial firewall; passive OT monitoring at T2 | Director of IT and Cybersecurity (CySO) | 2027-03-31 |
| R-003 | T2 crane OEM always-on cellular appliance compromised | High | Appliance off by default from 2026-10-15; OEM moved to the privileged remote access service | Director of Maintenance and Engineering | 2026-12-31 |
| R-004 | TOS database corruption replicates to the standby; recovery misses the RTO | High | Failover test 2026-11-07; hourly isolated snapshots; quarterly restore tests | Director of IT and Cybersecurity (CySO) | 2026-12-31 |
| R-009 | Privileged account takeover outside the cloud | High | Privileged access management for directory, identity provider and TOS administrators; FIDO2 keys | Security Manager (alternate CySO) | 2027-03-31 |
| R-017 | T2 cannot be rebuilt in time (no gate images; PLC programs only with the OEM) | High | T2 image backups; company-held PLC programs; T2 rebuild test | Director of Maintenance and Engineering | 2026-12-31 |
| R-037 | TOS vendor support path or software update used as a supply chain entry point | High | Vendor support through the privileged remote access service; update verification and staging | TOS Application Manager | 2026-12-31 |
| R-043 | Carrier alliance does not renew because a clean SOC 2 Type 2 report is not delivered | High | SOC 2 remediation; Type 1 by 2027-03-31; Type 2 period 2027-04-01 to 2027-09-30 | Chief Operating Officer | 2027-11-30 |

**Themes.**
- **Terminal 2 is the weak point (R-002, R-003, R-010, R-016, R-017, R-021, R-022, R-023).** The 2024 acquisition moved T2 onto the TOS, but its network, OT, backups and physical controls were not brought up to the T1 standard. Most High risks outside the cloud sit at T2.
- **Recovery and privileged access (R-001, R-004, R-009).** Detection is strong (EDR, MSSP, SIEM), but the company has not proven it can meet its RTOs, and standing domain administrator accounts would let one compromise reach everything.
- **Third parties with access to OT (R-003, R-018, R-037, R-041, R-045).** Only 1 of 27 vendors with access uses the privileged remote access service. Subpart F requires monitoring of every third-party remote connection (101.650(f)(3)).
- **Manual working limits (R-030, R-031).** Safety and road congestion, not revenue, set the shortest recovery targets.
- **AI adopted ahead of governance (R-028, R-029, R-039, R-044, R-045, R-046).** P10 addresses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15; $1.275 million one-time and $335,000 a year):**
- T2 OT zone: industrial firewall, switching, certificate-based VMT Wi-Fi and passive OT sensors ($420,000)
- Privileged access management extension and FIDO2 keys for administrators ($190,000 one-time; $85,000 a year)
- Privileged remote access service expanded to all 27 vendors with access ($60,000 a year)
- Replacement of the T2 OCR servers and 2 crane HMIs (2027 capital plan, $260,000)
- MSSP onboarding of T2 gate servers, TOS application logs and T1 OT alerts ($110,000 a year)
- Recovery program: hourly isolated snapshots, failover tests, T2 image backups ($90,000 one-time; $35,000 a year)
- Second diverse circuit at T2 ($45,000 a year)
- SOC 2 Type 1 and Type 2 examinations and readiness support ($240,000 across 2027)
- T2 gate server room badge readers and camera ($40,000)
- Longshore rules card, vendor technician briefing and OT training at T2 ($35,000)

Smaller items (default password changes, printed dangerous cargo lists, contract amendments, the vulnerability disclosure address) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (5, all Low):** R-024 (Director of Port Security, until the T2 OT zone separates security systems), R-038 (Security Manager, MSSP SLA tracked monthly), R-044 (Vice President, Terminal Operations, with quarterly misread-rate reporting), R-047 (Vice President, Terminal Operations), R-051 (Chief Operating Officer).

**Contract actions:** notification clauses for the 14 vendors with access that lack them (R-041), the T2 crane OEM access terms (R-003) and the AI vendor data terms (R-028, R-045), due 2026-12-31 to 2027-03-31.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and terminal technology resilience", owned by the Chief Operating Officer and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Terminal Operations and Gate Platform (TOGP; SSP in P02) | Director of IT and Cybersecurity (CySO) | 35 risks whose affected assets include SYS-01, SYS-02, SYS-04, SYS-05, SYS-07, SYS-08, SYS-10, SYS-13 or SYS-14 (filter the `affected_asset_or_process` column) |
| Crane and yard equipment OT (SYS-03; feeds the OT sections of the Cybersecurity Plan) | Director of Maintenance and Engineering | 17 risks: R-002, R-003, R-007, R-008, R-010, R-014, R-017, R-018, R-022, R-023, R-025, R-026, R-040, R-042, R-045, R-049, R-050 |
| Terminal 2 integration | T2 General Manager with the CySO | R-002, R-003, R-010, R-016, R-017, R-021, R-022, R-023, R-048 |
| AI portfolio (P10) | Director of Planning with the vCISO | R-028, R-029, R-039, R-044, R-045, R-046 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up. For the Coast Guard, the CySO will use these registers to document "the risk posed by each digital asset" in the Cybersecurity Assessment (101.650(e)(1)(i)) and will share the terminal-specific items with each FSO for the FSA updates.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-051, 2026-09-15.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements and the FY2027 security budget, 2026-09-15.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027 with the first Cybersecurity Assessment, or sooner after a major change (for example a change of ownership or another acquisition, R-048) or a significant incident.

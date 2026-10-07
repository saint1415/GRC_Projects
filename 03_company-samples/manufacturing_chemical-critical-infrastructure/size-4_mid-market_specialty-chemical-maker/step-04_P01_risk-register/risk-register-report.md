# Risk Register Report: Cris Santos Company | Chemical | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed specialty chemical formulator and packager) |
| Size tier | Mid-Market (850 employees) |
| Vertical | Chemical (NAICS 325998) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also feeds | The USCG Cybersecurity Assessment (33 CFR 101.650(e)(1), due 2027-07-16); cyber-initiated scenarios for the next RMP and PSM process hazard analyses (40 CFR 68.67(c)(4); 29 CFR 1910.119(e)) |
| Prepared | 2026-07-31 by the GRC Analyst and the vCISO with the Information Security Manager, the OT Security Engineer, and the process owners; R-011 added 2026-08-28 from P07 testing; R-024 and R-038 to R-042 updated after P09 (2026-09-04) and P10 (2026-09-11) |
| Approved | 2026-09-22: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** Every business unit (the Port plant and marine terminal, the Inland plant, the Distribution center, TTRS, and corporate functions), all systems SYS-01 to SYS-20, the 52 vendors with system or data access, and the AI portfolio. Processes and impact values come from the BIA (P05). Vulnerabilities come from the gap analysis (P03), the SSP (P02), the cloud mapping (P04), and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter. A High risk with a process safety consequence also needs the Port Plant Manager's confirmation, as RMP qualified person, that interim measures are adequate |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-22.

| Area | Appetite | Statement and measure |
|---|---|---|
| Process safety and the community | **Very low** | No cyber risk that could plausibly cause a toxic release, decomposition, or overfill is accepted above Moderate. Any such risk at High or above must have a funded treatment within 90 days. Measure: safety-linked risks at High or above (7 today: R-001, R-002, R-004, R-006, R-008, R-011, R-014; target 0 by 2027-12-31) |
| Regulatory compliance (USCG, RMP, PSM, DOT) | **Very low** | The Port plant submits its Cybersecurity Plan on time and keeps every binding process safety element Met. Measure: P03 roadmap milestones on schedule; R-012 at Low by 2027-07-16 |
| Availability for water utility customers | **Low** | Recovery must meet the BIA RTOs for every High-criticality process (P05). Measure: each High process has a passed recovery test in the last 12 months (2 of 10 today: BP-08 and BP-15, through the ERP vendor's yearly recovery test) |
| Confidentiality of SSI and formulations | **Low** | SSI is held only by people with a need to know (49 CFR 1520.9). Measure: SSI and formulation shares limited to named users by 2026-11-30 |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but every vendor with OT access or critical data is reviewed each year and must give notice of vulnerabilities and incidents |
| Innovation and AI | **Moderate** | AI is welcome for optimization, maintenance, forecasting, and documents, but only through the P10 process. No AI tool writes to a control system |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that lowers likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the chemical sector threat themes in CISA advisories (ransomware reaching OT through IT, abuse of remote access tools, default credentials on OT devices), the BIA, interviews with every process owner, site walkthroughs (Port 2026-07-14, Inland 2026-07-16, Distribution center 2026-07-21), P03, and P07.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA categories (cost, operations, regulatory, process safety, reputation). Any plausible toxic release that reaches the public is Very High.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 9 |
| Moderate | 30 |
| Low | 12 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 49 Mitigate, 3 Accept (R-030, R-042, R-050). Status: 27 Open, 22 In progress, 3 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-002 and R-003. It is not recorded as the treatment for any risk, because it does not lower the likelihood of a release or an outage.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-002 | Ransomware crosses the IT/OT conduits and forces a 7-day Port outage | Very High | MSSP OT monitoring 24x7; allowlisting on remaining OT workstations; full DCS restore test; joint exercise | Information Security Manager (CySO) | 2027-01-31 |
| R-001 | Remote session through the OT gateway used to change Ammonia Unit setpoints (toxic release) | High | FIDO2 for gateway users; logged approvals; download block outside MOC; session review; HAZOP cyber scenarios | OT Security Engineer | 2027-03-31 |
| R-003 | Corporate ransomware with data theft cuts shipping to 60% for 72 hours | High | Phishing-resistant MFA for administrators; restricted shares; restore tests; break-glass ERP access | IT Director | 2027-03-31 |
| R-004 | Inland SCADA reached from the office VLAN or the integrator's always-on remote tool | High | Remove the tool; gateway with MFA; firewall; change default passwords; Inland sensor | Controls Engineering Manager | 2026-12-31 |
| R-006 | Port DCS cannot be rebuilt within the 12-hour RTO | High | Full restore test 2026-11-10; OT contingency plan; clean-media rebuild procedure | Controls Engineering Manager | 2027-03-31 |
| R-007 | Inland PLC programs exist only on one laptop | High | Copy to the OT backup server and offline safe; quarterly compare | Controls Engineering Manager | 2026-10-31 |
| R-008 | SIS logic altered or drifted, found only at the yearly proof test | High | Monthly logic compare; keyswitch alarm; SIS EWS logging | Process Safety Manager (Port plant) | 2026-12-31 |
| R-011 | Tank gauging server default password used to falsify levels (found in P07) | High | Restrict web interface; sweep all Port OT devices for default passwords | OT Security Engineer | 2026-10-31 |
| R-012 | USCG Cybersecurity Assessment and Plan not done by 2027-07-16 | High | P03 roadmap; assessment 2027-01 to 2027-03; submission by 2027-06-15 | Information Security Manager (CySO) | 2027-06-15 |
| R-014 | Community warning and agency calls depend on the business network | High | Cellular phones, current printed call lists, second launch path; tested 2026-11-17 | VP EHS and Process Safety | 2026-10-31 |

**Themes.**
- **The Port plant's 2023-2024 OT investments work, but the edges are exposed (R-001, R-002, R-010, R-011, R-016, R-047).** The DMZ, gateway, and allowlisting cover the DCS core. Terminal equipment, historian clients, and monitoring outside business hours are where an attacker would go.
- **Recovery is the weakest function (R-006, R-007, R-008, R-021, R-034).** Backups exist, but no full OT restore has been tested and two critical sets of logic (Inland PLCs, SIS) cannot be verified quickly.
- **The Inland plant is a generation behind the Port plant (R-004, R-005, R-007, R-046, R-051).** It is outside the FSP, so the USCG rule does not reach it, but its risks are High.
- **Regulatory deadlines are concrete (R-012, R-013, R-037).** The USCG plan date, the missed training deadline, and the lapsed DOT plan review are compliance facts, not just risks.
- **TTRS and AI are newer exposures (R-021 to R-024, R-038 to R-043).** They drive the P09 and P10 work.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-22, $1.5 million one-time and $610,000 a year):**
- MSSP OT monitoring service for both plants, including an Inland OT sensor ($95,000 one-time, $240,000 a year)
- Inland plant segmentation, remote access gateway, and password remediation ($260,000)
- Unique operator accounts with badge-tap login at both plants ($180,000)
- FIDO2 security keys for administrators and gateway users ($25,000)
- OT recovery program: spare DCS server pair for restore tests, Inland PLC backup tooling, SIS logic compare tool ($210,000)
- USCG Cybersecurity Assessment and penetration test support ($140,000), and contractor training tracking ($20,000 a year)
- TTRS second-region standby and gateway firmware campaign ($230,000 one-time, $60,000 a year)
- SOC 2 readiness remediation and the Type 2 examination ($240,000 across 2027)
- Data loss prevention and file share restructuring ($90,000 one-time, $70,000 a year)
- Vendor risk program tooling and one additional GRC analyst ($30,000 one-time, $220,000 a year)
- The DCS upgrade and replacement of the 9 end-of-support workstations are in the 2027 turnaround capital plan ($1.4 million, not in the totals above)

Smaller items (cellular phones and call lists, switch port lockdown, contract amendments, exercise facilitation) are funded from operating budgets. Each funded item maps to a P07 POA&M entry or the P03 roadmap.

**Accepted (3):** R-030 (Low, COO; backups are in a separate account with write-once retention and separate credentials), R-042 (Low, COO; AI-003 is advisory and does not replace mechanical integrity inspections), R-050 (Low, COO; replenishment does not depend on the portal).

**Contract actions:** vulnerability and incident notice clauses for OT vendors (R-033, R-015) by 2027-03-31; recovery and notice terms for the MSSP OT service before it starts.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and process control resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks. The PE sponsor receives the same summary in the quarterly lender and sponsor pack (CFO).

System-level registers are filtered views of this file kept by each system owner, so there is one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Port plant PCBMS (SSP in P02; input to the USCG Cybersecurity Assessment) | Port Plant Manager with the CySO | 21 risks whose affected assets include SYS-01 to SYS-07, the Port OT workstations, or the Port plant (filter `affected_asset_or_process`) |
| Inland plant batch control | Inland Plant Manager | R-004, R-005, R-007, R-009, R-010, R-017, R-033, R-034, R-046, R-051 |
| TTRS (SOC 2 system, P09) | Director of Customer Solutions | R-021, R-022, R-023, R-024, R-039, R-050 |
| AI portfolio (P10) | Director of Data and Analytics | R-038, R-039, R-040, R-041, R-042, R-043 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-030, R-042, and R-050, 2026-09-22.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-22. The Port Plant Manager confirmed the interim measures for R-001, R-002, R-006, R-008, R-011, and R-014.
- Board audit committee: received the results on 2026-09-22. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, merged with the USCG Cybersecurity Assessment, or sooner after a major change (the 2027 DCS upgrade) or a significant incident.

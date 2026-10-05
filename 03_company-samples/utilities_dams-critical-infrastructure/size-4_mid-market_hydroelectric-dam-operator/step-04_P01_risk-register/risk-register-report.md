# Risk Register Report: Cris Santos Company | Dams | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (owner and operator of 4 FERC-licensed hydroelectric projects, with Hydro Services) |
| Size tier | Mid-Market (850 employees) |
| Vertical | Dams |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | FERC Security Program Form 3 Questions 23a, 29-31 (all-hazards risk management, periodic risk assessment reported to management); input to the annual Vulnerability Assessment update for Blackwater Bend (Rev. 3A 5.4) |
| Prepared | 2026-07-31 by the vCISO and the GRC Manager with the OT Security Manager; R-028, R-041, and R-045 updated 2026-08-14 from P07 testing |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units, the Hydro Control and Dam Monitoring System (HCDMS, SYS-01 to SYS-07; P02), corporate IT and the cloud landing zone (SYS-08 to SYS-16; P04), RMOS and field services, OT vendors, and the AI portfolio (P10). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (manager level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment and interim controls are in place |

A known noncompliance with a FERC requirement or a NERC Reliability Standard is never "accepted" as a risk. It is remediated, and the General Counsel decides on self-reporting.

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-17.

| Area | Appetite | Statement and measure |
|---|---|---|
| Public safety (dams, gates, warning) | **Very low** | No cyber or technology risk that could plausibly cause an uncontrolled release, a missed warning, or loss of a public water supply is accepted above Low. Any such risk rated Moderate or higher must have a funded plan within 90 days. Measure: risks with Very High impact rated Moderate or above (13 today: R-001, R-002, R-004, R-009, R-016, R-017, R-018, R-019, R-020, R-022, R-035, R-041, R-050); target: none above Moderate by 2027-12-31 |
| Regulatory compliance (FERC, NERC) | **Very low** | Every Form 3 negative answer has a plan and schedule accepted by the Regional Engineer; no CIP-003-9, CIP-012-2, or EOP-004-4 requirement stays unmet beyond 2026-12-31. Measure: open regulatory gaps in P03 |
| Generation availability | **Moderate** | Generation outages are tolerable while local control keeps the dams safe. Measure: BIA RTOs demonstrated for BP-03 and BP-05 by 2027-06-30 |
| RMOS client trust | **Low** | No client control path into company systems without zoning and contract terms; SOC 2 Type 2 by 2027-11-30. Measure: R-002, R-024, R-025 at Low by 2027-12-31 |
| Third parties | **Moderate**, with conditions | OEMs and vendors are essential, but none gets remote access to OT outside the jump hosts, and every Tier 1 vendor is reviewed each year (P09) |
| Innovation and AI | **Moderate** | AI may advise dam safety, operations, and security staff, but no AI output may command a gate or unit or replace a manual dam safety check (P10) |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable; scenarios above $5 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Dams overlay, CISA Dams Sector and ICS advisories, the FERC Section 9 measures, the BIA, interviews with every process owner, the Section 9 re-determination (2026-07-14 to 2026-07-16), the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA categories (cost, operations, regulatory, public safety, reputation). Any plausible uncontrolled release toward an inundation zone is Very High.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each level its SP 800-30 Appendix I value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event range from the BIA values, for the enterprise roll-up (NIST IR 8286 Rev. 1). Life-safety exposure is not converted to dollars.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 10 |
| Moderate | 28 |
| Low | 12 |
| Very Low | 0 |
| **Total** | **51** |

Treatments: 47 Mitigate, 4 Accept (R-042, R-046, R-047, R-049). Status: 21 Open, 26 In progress, 4 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-003 and R-031. It is not the treatment for any risk, because it does not lower the likelihood of harm downstream.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | OEM direct VPN used to command gates or units | Very High | Move both OEMs to the jump hosts with MFA, recording, and weekly log review | OT Security Manager | 2026-11-30 |
| R-002 | Pivot from an RMOS client tunnel into ROC SCADA | High | Separate RMOS zone at the ROC that can reach only client SCADA objects | OT Security Manager | 2027-03-31 |
| R-003 | Ransomware with RMOS data theft forcing IT/OT separation | High | Ransomware crisis plan with a pre-approved IT/OT separation procedure | IT Director | 2026-12-31 |
| R-004 | Lateral movement across the flat OT WAN | High | Per-site OT zones with conduits through site firewalls | OT Security Manager | 2027-03-31 |
| R-007 | Undetected intrusion at CDS, PNH, or SGR | High | Passive OT sensors and log collection at CDS, PNH, and SGR with MSSP alerting | OT Security Manager | 2027-06-30 |
| R-008 | OT configurations cannot be restored within the RTO | High | Complete and verify backups at all plants | Manager of Controls Engineering | 2027-06-30 |
| R-009 | Primary and backup ROC disabled together | High | Isolated recovery environment at the backup ROC with offline images | Manager of Controls Engineering | 2027-06-30 |
| R-016 | Late EAP notification after a cyber-caused release | High | Cyber triggers in all 4 EAP flowcharts and Security Plans | Chief Dam Safety Engineer | 2026-12-15 |
| R-018 | Too few qualified operators for all-local gate operation in a flood | High | Cross-train 12 more plant staff | Vice President of Generation Operations | 2027-03-31 |
| R-022 | OEM or SCADA vendor supply chain compromise | High | Vendor tiering and assessments | GRC Manager | 2027-03-31 |
| R-041 | Other undocumented remote connections like the SGR modem | High | Physical walkdown of every panel at CDS, PNH, and SGR | OT Security Manager | 2026-12-31 |

**Themes.**
- **Remote paths into OT (R-001, R-002, R-041, R-028).** The jump hosts work, but two OEM VPNs, RMOS client tunnels, and an undocumented modem bypass or undercut them. R-001 is the only Very High risk; interim controls since 2026-09-15 reduce exposure while the permanent fix is built.
- **Flat OT and partial visibility (R-004, R-007, R-009).** One SCADA domain and one routed WAN tie 4 dams and 6 client projects together, and 3 projects have no OT monitoring.
- **Recovery (R-008, R-009, R-018).** Recovery is proven only at Blackwater Bend, and all-local operation in a flood is thinly staffed.
- **Regulatory (R-011 to R-013, R-015, R-016).** Section 9 re-evaluation lapsed, two NERC requirements are unmet, and cyber events are not tied to 18 CFR 12.10 or the EAPs.
- **Third parties and clients (R-022 to R-025).** OEMs without security terms, and client contracts without security responsibilities.

## 4. Treatment summary
**Funded in the FY2027 security budget (approved by the CEO 2026-09-17: $1.86 million one-time and $540,000 a year):**
| Item | One-time | Annual | Risks |
|---|---|---|---|
| OT zone architecture at 5 sites, including the RMOS zone at the ROC | $420,000 | | R-002, R-004 |
| Replacement of 9 unsupported OT hosts; named-account HMI upgrade at PNH and SGR | $380,000 | | R-005, R-006 |
| OT recovery program: complete backups, governor settings escrow, isolated recovery environment at the backup ROC | $310,000 | | R-008, R-009, R-010 |
| OT monitoring at CDS, PNH, and SGR | $180,000 | $90,000 (MSSP OT service) | R-007, R-017, R-041 |
| SOC 2 readiness, Type 1 and Type 2 examinations | $150,000 | $60,000 (annual report) | R-025 |
| Jump host expansion, OEM migration, CDS session inspection, break-glass MFA | $140,000 | $25,000 | R-001, R-012, R-027 |
| Second ICCP path | $95,000 | $18,000 | R-013, R-014 |
| OT privileged access vault | $80,000 | $30,000 | R-044 |
| OT vulnerability assessments at CDS and PNH, then all Critical sites each year | $60,000 | $70,000 | R-005 |
| Restricted CEII library and data classification | $45,000 | | R-026, R-033 |
| One OT security engineer | | $137,000 | R-007, R-041 |
| One GRC analyst for vendor and client risk | | $110,000 | R-022 to R-024 |
| **Total** | **$1,860,000** | **$540,000** | |

Smaller items (tamper switches, satellite phones, cross-training, exercise facilitation, contract amendments) come from operating budgets. Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-042 (Low, ROC Manager); R-046 (Low, General Counsel); R-047 (Low, Vice President of Hydro Services); R-049 (Low, OT Security Manager). Each is reviewed annually.

**Regulatory items (not accepted, remediated):** R-012 (CIP-003-9 Section 6.3 at Cedar Shoals) and R-013 (CIP-012-2 Parts 1.2 and 1.3). The General Counsel decides on self-reporting to the Regional Entity by 2026-10-15.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company enterprise risk register as one line, "Cybersecurity, dam safety technology, and operational resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file kept by each system owner, so there is one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| HCDMS (SSP in P02; feeds the Blackwater Bend Vulnerability Assessment update and the Cedar Shoals and Pine Hollow Security Assessments) | Vice President of Generation Operations | 32 risks whose affected assets include SYS-01 to SYS-07 (filter `affected_asset_or_process`) |
| RMOS service (SOC 2 system, P09) | Vice President of Hydro Services | R-001, R-002, R-003, R-009, R-023, R-024, R-025, R-034, R-047 |
| AI portfolio (P10) | Chief Dam Safety Engineer with the Data Analytics Lead | R-035, R-036, R-037, R-038 |
| NERC compliance | NERC Compliance Manager | R-012, R-013 |

When a system-level review changes a rating, the owner updates this file and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of the Low risks, 2026-09-17.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-17. No High or Very High risk is accepted.
- Board audit committee: received the results on 2026-09-17. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (new RMOS client, new project, change in BES status) or a significant incident.

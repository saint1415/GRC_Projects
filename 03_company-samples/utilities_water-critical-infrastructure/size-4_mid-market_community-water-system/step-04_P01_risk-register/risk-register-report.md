# Risk Register Report: Cris Santos Company | Water and Wastewater Systems | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed investor-owned water utility: 11 community water systems and Utility Services for 3 municipal clients) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Water and Wastewater Systems |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); OT threat and impact guidance from NIST SP 800-82 Rev. 3 section 4.1; enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | The cybersecurity addendum to the SDWA section 1433 risk and resilience assessments (RRAs) of the Regional, Lakes, and Ridge Systems: risk from malevolent acts and natural hazards, and the resilience of electronic, computer, or other automated systems (42 U.S.C. 300i-2(a)(1)(A)(i)-(ii)) |
| Prepared | 2026-07-31 by the Security Manager, the vCISO, and the Emergency Management and Resilience Manager; R-004 and R-015 updated 2026-08-14 from P07 testing |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and the risk appetite); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units in the BIA (P05): the Regional, Lakes, and Ridge Systems, the 8 small systems, the ROC, water quality, customer service, Utility Services, field services, engineering, and enterprise functions. Systems SYS-01 to SYS-18, including the Integrated Water Operations SCADA (IWOS, SYS-01 to SYS-06; SSP in P02), the cloud landing zone (P04), and the 6 AI tools (P10). Impact values come from the BIA. Vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (manager level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-15.

| Area | Appetite | Statement and measure |
|---|---|---|
| Public health and safe water | **Very low** | No cyber or technology risk that could plausibly lead to unsafe water reaching customers is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: safety-linked risks above Low (13 today: R-001 to R-004, R-009 to R-012, R-015, R-019, R-044, R-051, R-053; target 0 High by 2027-06-30 and 0 above Low by 2028-06-30) |
| Regulatory compliance (SDWA) | **Very low** | Every RRA and ERP certification is made on time and reflects the system as it is. Measure: Ridge ERP certified by 2026-12-04 (latest date 2026-12-24); RRA addendum adopted for all 3 covered systems by 2026-12-31 |
| Availability of treatment and supervision | **Low** | Manual operation must be achievable within the BIA RTOs at every staffed plant, and every High-criticality process must have a passed recovery test or drill in the last 12 months. Measure: drills and rebuild tests by plant (P05 section 5) |
| Customer and client data | **Low** | No risk of a breach affecting more than 1,000 customers is accepted above Moderate. Measure: R-005 and R-006 at Moderate or lower by 2027-06-30 |
| Third parties and integrators | **Moderate**, with conditions | Integrators and vendors are needed, but none gets remote access to OT except through the gateway with MFA, approval, and recording, and every Tier 1 vendor is reviewed yearly (P09). Measure: unmanaged OT access paths (2 today, target 0 by 2026-10-31) |
| Acquisitions | **Moderate** | Growth by acquisition continues, but no acquired system connects to the ROC before an OT assessment and baseline controls (STD-07). Measure: acquired systems meeting STD-07 (0 of 2 today) |
| Innovation and AI | **Moderate** | AI is welcome for analytics and customer service, but only through the P10 process, and no AI tool may write to SCADA |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that lowers likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E; EPA's baseline threat information for water systems, CISA and water-sector ISAC advisories on remote access and HMI compromise, and SP 800-82 Rev. 3 section 4.1; the BIA; interviews with every process owner; the gap analysis (P03); and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**. Engineered safeguards that SCADA cannot override (hardwired stroke limits and analyzer alarms, P02 SC-24) lower the likelihood of adverse impact for chemical feed scenarios. They do not lower impact, which is rated on the potential outcome.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, public health and safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 0 |
| High | 10 |
| Moderate | 32 |
| Low | 11 |
| Very Low | 0 |
| **Total** | **53** |

Treatments: 50 Mitigate, 3 Accept (R-038, R-042, R-049). Status: 26 Open, 24 In progress, 3 Accepted.

**Why nothing is Very High.** Several OT scenarios have Very High potential impact (unsafe water reaching tens of thousands of people). Each is rated High rather than Very High because the hardwired chemical feed limits and analyzer alarms at every plant reduce the likelihood that an attack becomes harm. If those safeguards were bypassed or removed, R-001, R-002, R-003, R-019, and R-053 would move to Very High.

Cyber insurance ($15 million aggregate limit, $500,000 retention) transfers part of the financial exposure for R-005 and R-006. It is not recorded as the treatment for any risk, because it does nothing to keep water safe.

### Top risks (High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ridge HMI taken over through Integrator B's always-on remote desktop agent; hypochlorite feed changed | High | Remove the agent; gateway with MFA, approval, recording; Integrator B security amendment | IT Director (security officer) | 2026-10-31 |
| R-002 | Lakes on-call VPN (password only) used to reach the flat Lakes control network | High | Retire the VPN; on-call access through the gateway with MFA | IT Director (security officer) | 2026-10-31 |
| R-003 | Compromise at an acquired plant spreads through any-to-any site-to-site VPNs into the Regional network | High | Named flows only; isolate Ridge SCADA; monitor tunnels | IT Director (security officer) | 2026-12-31 |
| R-004 | Internet-exposed small-system modem used to change a well controller or stop chlorination | High | Private carrier network; disable web administration; quarterly exposure scans | SCADA and Controls Engineering Manager | 2026-10-15 |
| R-005 | Ransomware in business IT with customer data theft (double extortion) | High | Privileged access management for directory and SaaS administrators; service account vaulting; CIS data restore test; tabletop | IT Director (security officer) | 2027-03-31 |
| R-008 | Lakes or Ridge SCADA cannot be rebuilt within 24 hours | High | Offline backups; rebuild procedure and tests; Integrator B response terms | SCADA and Controls Engineering Manager | 2027-03-31 |
| R-012 | OT intrusion undetected at Lakes, Ridge, or small systems; Regional alerts reach the ROC late | High | OT playbooks and 15-minute ROC escalation; sensors at WTP-L1 and WTP-G1; log collection | Security Manager | 2027-06-30 |
| R-016 | Malware on the unsupported Ridge SCADA server and engineering workstation | High | Interim isolation and allowlisting (2026-12-31); platform replacement | SCADA and Controls Engineering Manager | 2027-09-30 |
| R-019 | Manual operation fails or starts late during a SCADA outage | High | Written manual-mode procedures for each chemical feed; Ridge drill; WTP-G2 on-call plan | Director of Water Operations | 2026-12-04 |
| R-053 | State-sponsored actor pivots from business IT to the OT DMZ | High | Separate OT DMZ identities; twice-yearly threat hunts; detections from CISA advisories | Security Manager | 2027-06-30 |

**Themes.**
- **The acquired systems carry most of the OT risk (R-001 to R-004, R-007 to R-011, R-013, R-015 to R-018).** The Regional System has a modern, segmented, monitored design. Lakes, Ridge, and the small systems were connected to the ROC in March 2026 before they had the same controls. Seven of the 10 High risks sit there.
- **Recovery depends on manual operation (R-008, R-019, R-021).** The BIA shows that safe water depends on licensed operators running plants by hand, not on restoring SCADA. That capability is strong at Regional and untested at Ridge.
- **Detection stops at the Regional fence (R-012, R-053).** The MSSP sees business IT and the Regional plants. It cannot see Lakes, Ridge, or the small systems, and it has no path to the ROC.
- **SDWA program quality (R-024 to R-027).** The certifications are on time, but the content lags the system: one RRA predates the interconnection, one cyber element was copied, and the Ridge ERP has no cyber procedures yet.
- **AI adopted without governance (R-043 to R-048).** Six tools went live or into pilot without review. P10 sets conditions.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15: $2.1 million one-time, $350,000 a year, and $240,000 for SOC 2 across 2027):**
- Remote access consolidation at Lakes and Ridge, MFA, and vendor gateway licensing ($90,000 one-time, $25,000 a year)
- OT DMZ and segmentation at WTP-L1 and WTP-G1, tunnel restrictions, Ridge isolation firewall ($420,000)
- Passive OT monitoring sensors at WTP-L1 and WTP-G1, MSSP OT playbooks and log onboarding ($160,000 one-time, $140,000 a year)
- OT backup program for Lakes, Ridge, and small systems, with rebuild tests ($120,000 one-time, $30,000 a year)
- Named HMI accounts, device credential vaulting, and privileged access management for directory and SaaS administrators ($210,000 one-time, $95,000 a year)
- Alternate ROC position at WTP-R2 ($180,000)
- Ridge SCADA platform replacement (2027 capital plan, $850,000)
- Vendor risk program and Integrator B re-bid support ($60,000 a year)
- SOC 2 readiness and the Type 2 examination for Utility Services ($240,000 across 2027)
- AI governance and validation work ($70,000 one-time)

Smaller items (key control at small-system sites, Spanish-language notice templates, exercise facilitation) come from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (3):** R-038 (Low, Director of Utility Services; read-only client links behind dedicated firewalls), R-042 (Low, COO; backups are isolated and write-once), R-049 (Low, SCADA and Controls Engineering Manager; unencrypted licensed radio compensated by protocol filtering, revisited when radios are replaced).

**Contract actions:** Integrator B security amendment and response-time terms (R-001, R-008, R-013) by 2026-12-31; vendor access agreements for all 14 OT vendors (R-014); CIS vendor 72-hour incident notice at renewal (R-006, R-035); AI vendor change-notice clauses (R-043, R-044).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and operational technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each owner, so there is only one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| IWOS (SSP in P02) | Director of Water Operations, with the SCADA and Controls Engineering Manager | 29 risks whose affected assets include SYS-01 to SYS-06 (filter `affected_asset_or_process`) |
| Regional System RRA cyber addendum (PWSID 1) | Emergency Management and Resilience Manager | R-003, R-005, R-012, R-019 to R-021, R-023 to R-029, R-043, R-044, R-049, R-053 |
| Lakes System RRA cyber addendum (PWSID 2) | Emergency Management and Resilience Manager | R-002, R-003, R-007 to R-012, R-013, R-015, R-017 to R-020, R-022, R-024 to R-028 |
| Ridge System RRA cyber addendum (PWSID 3) | Emergency Management and Resilience Manager | R-001, R-003, R-008 to R-013, R-016 to R-020, R-022, R-024 to R-028 |
| Small systems (not required to certify; same method applied) | Director of Water Operations | R-004, R-009 to R-012, R-018, R-020, R-022, R-051, R-052 |
| Utility Services (feeds SOC 2 readiness, P09) | Director of Utility Services | R-005, R-006, R-021, R-035 to R-038 |
| AI portfolio (P10) | Water Quality and Compliance Manager (program lead) | R-043 to R-048 |

**How this register serves the RRAs.** For each covered system, the RRA must assess risk from malevolent acts and natural hazards (300i-2(a)(1)(A)(i)) and the resilience of its automated systems, including their security ((a)(1)(A)(ii)). The filtered view for each PWSID, dated 2026-09-15, is attached to that system's RRA as a cybersecurity addendum. The Emergency Management and Resilience Manager records the attachment in each RRA's revision log, which keeps the records required by 300i-2(d). The Ridge ERP revision uses the Ridge view as its input, because the ERP must incorporate the findings of the assessment (300i-2(b)).

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-042, 2026-09-15.
- Chief Executive Officer: approved the High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (any acquisition, new interconnection, or platform replacement) or a significant incident.

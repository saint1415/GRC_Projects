# Risk Register Report: Cris Santos Company | Government Services and Facilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed facilities support contractor operating government buildings) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Government Services and Facilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); OT threats informed by NIST SP 800-82 Rev. 3; enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | State contract cybersecurity exhibit (SP 800-53 RA-3 risk assessment); County A and County B annual assessment requests |
| Prepared | 2026-07-31 by the Security Manager, the GRC analyst, and the vCISO; R-050 and R-051 added 2026-08-14 and R-032 updated 2026-08-13 from P07 testing |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (ROC, Building Technology, Federal Programs, State and Local Programs, field Operations, and corporate functions), the Integrated Facility Operations Platform (IFOP, the SSP system in P02), the corporate systems that hold customer or federal contract information (identity provider, email, CMMS, ERP and HR suite), the subcontractors with remote access, and the AI portfolio (P10). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**What is out of scope.** GSA's building systems on the GSA Building Systems Network (SYS-10) and the school district's own BAS server. Their owners authorize and monitor them. The register covers only the company's part: its staff, PIV cards, conduct, and connections.

**What makes this company different.** It does not own the buildings or the field equipment. Its risks come from operating other people's building systems around the clock: remote access into government OT networks by its own staff and by 7 subcontractors, holding cardholder data and security system layouts, supporting two critical facilities (the County A EOC and the state data center building), and meeting five sets of contract notice terms. A failure can open doors at a government building or overheat a data center, not only leak data.

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
| Physical security and safety at customer buildings | **Very low** | No risk that could unlock doors, disable a critical facility, or leave a building unsafe is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: such risks above Low (13 today: R-001, R-003, R-004, R-008, R-010, R-015, R-016, R-019, R-023, R-031, R-038, R-045, R-050; target 0 by 2027-12-31) |
| Customer data confidentiality (cardholder data, face templates, CUI, security plans) | **Low** | No risk of a breach of customer personal information or CUI is accepted above Moderate. Measure: R-005 and R-025 at Moderate or lower by 2027-06-30 |
| Availability of monitoring and critical facility support | **Low** | Recovery capabilities must meet the BIA RTOs for all High-criticality processes (P05). Measure: every High process has a passed recovery or failover test in the last 12 months |
| Contract and regulatory compliance | **Low** | No customer security term or FAR clause requirement stays Not met or Partially met at High gap risk beyond 2027-06-30. No notice clock is missed |
| Third parties and subcontractors | **Moderate**, with conditions | Subcontractors are essential to the business, but none gets remote access outside the broker or customer data without the security addendum, and every OT subcontractor is reviewed each year |
| Innovation and AI | **Moderate** | The company will use AI for building analytics and productivity only through the AI governance process in P10. It will not operate AI that identifies members of the public |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the OT threat discussion in SP 800-82 Rev. 3, CISA ICS advisories, the BIA, interviews with every process owner and program manager, site walkthroughs at 8 sites (2026-07-14 to 2026-07-23), the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were rated separately and combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, contract and regulatory, safety and physical security, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 12 |
| Moderate | 31 |
| Low | 8 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 44 Mitigate, 6 Accept (R-021, R-029, R-030, R-036, R-040, R-042), 1 Avoid (R-014), and 1 Share/Transfer (R-028). Status: 30 In progress, 15 Open, 6 Accepted, 1 Avoided.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, and R-005. It is not recorded as the treatment for those risks, because it does not lower the likelihood of harm at a customer building.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Intrusion through a subcontractor's remote-support tool unlocks doors and changes HVAC at County B or City sites | Very High | All subcontractors onto the broker; tools removed; management only from the broker | OT Security Engineer | 2026-12-31 |
| R-002 | Ransomware halts the ROC and BAS clusters and steals data | High | Cluster restore tests; ransomware runbook and tabletop; OT logs to the SIEM | IT Director (ISO) | 2027-03-31 |
| R-003 | Default passwords on controllers and NVRs | High | Change defaults; vault for all 46 sites | OT Security Engineer | 2026-12-31 |
| R-004 | Malware spreads from a customer network at a flat site | High | OT VLANs at 17 sites | OT Security Engineer | 2027-06-30 |
| R-005 | Theft of 41,000 cardholder records and face templates | High | Federated tenants; quarterly reviews; export alerts | Security Systems Manager | 2027-03-31 |
| R-008 | Long outage at the County A EOC and other sites without manual-mode procedures | High | EOC procedure by 2026-12-15, then every site | VP Operations | 2027-03-31 |
| R-009 | OT intrusion undetected for weeks | High | OT events to the SIEM; sensors at all sites | OT Security Engineer | 2027-06-30 |
| R-013 | Face verification bias or template exposure | High | P10 conditions; no new enrollments | Security Systems Manager | 2026-12-31 |
| R-016 | Exploit of out-of-date edge firewall firmware | High | Update 14 firewalls; monthly review | OT Security Engineer | 2026-11-30 |
| R-019 | Subcontractor network compromise exposes site credentials | High | Addendum, annual review, broker-only access | Contracts Director | 2026-12-31 |
| R-031 | Remote unlock or log tampering at the elections warehouse cage | High | Remove remote unlock before the 2026-11-03 general election; alerting | Security Systems Manager | 2026-10-15 |
| R-038 | Loss of cooling control at the state data center building | High | Quarterly hand-mode drill; direct alarm escalation | VP Operations | 2026-12-15 |
| R-050 | Cellular modem on a City BAS panel bypasses the edge firewall (found in P07) | High | Remove the modem; sweep all panels | OT Security Engineer | 2026-10-15 |

**Themes.**
- **Remote access and the OT boundary (R-001, R-003, R-004, R-010, R-016, R-019, R-050, R-051, R-052).** The broker works for company staff. The weak points are the subcontractors, the flat sites, stale firmware, and paths nobody inventoried, such as the cellular modem.
- **Visibility (R-009, R-032, R-047).** OT and tenant activity is logged but not watched, so an intruder could dwell for weeks.
- **Critical facilities and recovery (R-002, R-006, R-007, R-008, R-024, R-038).** Backups are isolated, but recovery and manual operation are proven only for federal and state sites.
- **Elections and public trust (R-031).** A small technical risk with a large reputational one; it has the earliest due date because of the November general election.
- **AI adopted without governance (R-013, R-014, R-034, R-035, R-037).** P10 addresses them.

**Added after the control assessment (P07):**
- R-050 (cellular modem) added 2026-08-14 after the City panel inspection on 2026-08-12.
- R-051 (shared subcontractor account in the County B tenant) added 2026-08-14.
- R-032 updated 2026-08-13 after passive discovery found 41 unlisted devices at County A.
- R-003 re-rated High on 2026-08-13 after the default-credential test.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15; about $1.2 million one-time and $350,000 a year):**
- OT segmentation at the 17 flat sites and passive sensors at the other 34 sites ($420,000 one-time; $60,000 a year in sensor licenses)
- Broker expansion to all subcontractors and vault coverage for all 46 sites ($90,000 one-time; $45,000 a year)
- OT log onboarding and detection use cases through the MSSP ($110,000 a year)
- Replacement of the 9 unsupported engineering workstations and legacy tool upgrades ($140,000)
- Edge firewall firmware updates and 6 hardware refreshes ($85,000)
- Recovery testing program and controller program collection ($160,000)
- A second OT security position ($135,000 a year)
- SOC 2 readiness, Type 1, and Type 2 examination ($260,000 across 2027)
- AI governance reviews and bias testing ($45,000)

Smaller items (key logs, wallet cards, the receiving checklist) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (6):** R-021 (Low, IT Director), R-029 (Low, Contracts Director), R-030 (Low, IT Director), R-036 (Low, Controls Engineering Manager, only while autonomous mode stays disabled), R-040 (Low, IT Director), R-042 (Low, VP Operations).

**Avoided:** R-014. The company will not configure or operate 1:N face identification of the public (P10).

**Shared:** R-028, through a 72-hour breach notice clause at the CMMS renewal and cyber insurance.

**Contract actions:** subcontractor security addendum for SUB-4 to SUB-7 and the 4 federal-site trades subcontracts without FAR 52.204-21 flow-down (R-019, R-027, R-044), due 2026-12-31; interconnection agreements with County A, County B, the City, and the school district (R-049, R-052), due 2027-03-31.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and building technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Integrated Facility Operations Platform (IFOP; SSP in P02) | IT Director (ISO) with the Director of Building Technology | 36 risks whose affected assets include SYS-01 to SYS-05, SYS-13, SYS-14, or SYS-15 (filter the `affected_asset_or_process` column) |
| County A critical sites (EOC and elections warehouse) | County A Program Manager | R-008, R-031, R-032, R-044 |
| State data center building | State Program Manager | R-038, R-002, R-006 |
| AI portfolio (P10) | vCISO (AI review group chair) | R-013, R-014, R-034, R-035, R-036, R-037 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the 6 acceptances, 2026-09-15.
- Chief Executive Officer: approved the Very High and High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15. R-001 is not accepted; it is in treatment with a 2026-12-31 deadline and weekly interim checks that the subcontractor tools are disabled between visits.
- Board audit committee: received the results on 2026-09-15. Next report: December 2026 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example an acquisition, R-048), a new contract, or a significant incident.

# Risk Register Report: Cris Santos Company | Transportation Systems | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Class II regional freight railroad, north and central Florida) |
| Size tier | Mid-Market (850 employees) |
| Vertical | Transportation Systems |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | Risk input to the TSA Cybersecurity Assessment Plan and to the CIP remediation schedule (SD 1580/82-2022-01E III.F); remediation planning required by SD 1580-21-01E II.E.2 |
| Prepared | 2026-07-31 by the Cybersecurity Manager and the vCISO; 8 ratings reviewed again on 2026-08-21 after P07 testing (R-006, R-008, R-018, R-024, R-025, R-043, R-048, R-051) |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units, the Train Dispatch and PTC Operations Platform (TDPO, SSP in P02), the cloud landing zone (P04), the TMS and other SaaS vendors, the wayside OT, and the AI tools (SYS-13). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

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
| Safety of train operations and the public | **Very low** | No cyber or technology risk that could plausibly contribute to a train accident, a roadway worker injury, or a hazmat release is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan. Measure: safety-linked risks rated High or Very High (6 today: R-001, R-003, R-004, R-005, R-009, R-051; target 0 by 2027-12-31) |
| Regulatory compliance (TSA and FRA) | **Very low** | Every measure in the TSA-approved CIP is implemented on its approved schedule or TSA is told in advance; every TSA, CISA, and FRA reporting clock is met. Measure: CIP milestones overdue (1 today, the field zones); CAP share of measures assessed per plan year (at least one-third) |
| Availability of train operations | **Low** | Recovery capabilities must meet the BIA RTOs for all High-criticality processes (P05). Measure: every High process has a passed recovery test in the last 12 months (0 of 9 today for a cyber scenario) |
| Confidentiality of SSI and personal information | **Low** | SSI stays in the restricted library with need-to-know access; no risk of a reportable breach of employee data above Moderate. Measure: SSI copies outside the library (0 target, checked quarterly) |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor reaches OT except through the PAM jump host, and every Tier 1 vendor is reassessed each year (P09) |
| Innovation and AI | **Moderate** | The company wants AI benefits in inspection, maintenance, and customer service, but only through the AI governance process in P10. No AI output replaces a required FRA inspection |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the TSA directives' threat statements (SD 1580/82-2022-01E section I), CISA advisories on critical infrastructure (cited in the directive), the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 2 |
| High | 8 |
| Moderate | 30 |
| Low | 12 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 48 Mitigate, 4 Accept (R-030, R-037, R-038, R-039). Status: 30 Open, 18 In progress, 4 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, and R-014. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to train operations or the public.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware crosses the IT/OT boundary and encrypts CAD/CTC, the BOS, and consoles | Very High | Clean-room recovery and restore tests; CAD/CTC patching; IT/OT isolation exercise; CTC-territory manual dispatch drill | Cybersecurity Manager | 2027-03-31 |
| R-003 | CAD/CTC cannot be restored within the 2-hour RTO after a cyber event | Very High | First end-to-end restore 2026-11-05, then quarterly; clean-room environment; delayed-replication snapshot | Director of Information Technology | 2027-03-31 |
| R-004 | Attacker on the flat field backhaul sends false requests to CTC controllers or suppresses detector alarms | High | Field zone segmentation; OT sensors at 6 hub towers; controller authentication upgrade | Director of Signals and Communications | 2027-03-31 |
| R-005 | Conflicting authority during unpracticed manual dispatch in CTC territory | High | CTC-territory drill 2026-12-10; cyber triggers in the procedure; train all dispatchers | Director of Network Operations | 2026-12-31 |
| R-007 | Radio or detector vendor's always-on access used to enter the backhaul | High | Move both vendors to the PAM jump host; security terms at renewal | Cybersecurity Manager | 2026-12-31 |
| R-009 | Unpatched CAD/CTC server OS exploited from inside the dispatch zone | High | Certified patch level; 60-day vendor certification commitment | Director of Information Technology | 2026-12-31 |
| R-010 | TSA inspection finds CIP and CAP measures not carried out | High | Architecture design review 2026-11; CIP schedule amendment; monthly milestone tracking | Cybersecurity Manager | 2026-11-30 |
| R-023 | Identity provider or PAM administrator account taken over | High | Quarterly break-glass test; dedicated admin workstations | Director of Information Technology | 2026-12-31 |
| R-028 | One storm affects both NOCs | High | Emergency read access in the cloud clean room; affiliate emergency dispatch support | Chief Operating Officer | 2027-12-31 |
| R-051 | Insider with CAD/CTC administrator rights sabotages dispatch | High | Remove dual rights; alert on administrator actions outside change windows | Director of Network Operations | 2026-12-31 |

**Themes.**
- **The IT/OT boundary is strong at the data center and weak in the field (R-001, R-004, R-007, R-008, R-018, R-020, R-036).** The CIP's defense in depth works where it was built first. The 38 tower sites, the code line, and the vendor paths into them are where an attacker would go.
- **Recovery is the gap that matters most (R-001, R-003, R-005, R-013, R-049).** The company can detect IT attacks and its backups are well protected, but it has never restored the dispatch system from them or run dispatch manually in CTC territory.
- **Compliance with the approved plans (R-010, R-011, R-012).** At this size the risk is not a missing program but an approved plan that is not kept on schedule. TSA inspects against the CIP.
- **Third parties (R-007, R-014, R-017, R-034, R-041, R-046).** The TMS vendor is a single point of failure for car data, and 2 OT vendors still have always-on access.
- **AI adopted without review (R-041 to R-046).** P10 addresses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15, $1.48 million one-time and $510,000 a year):**
- Field zone segmentation: OT firewalls at the 38 tower sites and OT sensors at 6 hub towers ($520,000 one-time)
- Clean-room recovery environment and the restore testing program ($160,000 one-time, $40,000 a year)
- MSSP scope extended to OT alerts, plus forwarding of CAD/CTC, BOS, and field logs ($150,000 a year)
- PAM extension for the radio and detector vendors and vaulting of field device credentials ($90,000 one-time, $30,000 a year)
- CAD/CTC certified patching and a vendor certification commitment ($110,000 one-time)
- Controller firmware upgrades at 41 locations ($180,000 one-time)
- Architecture design review and an OT purple team exercise ($140,000 one-time)
- One GRC analyst for vendor risk and CAP scheduling, with tooling ($130,000 a year)
- SOC 2 readiness and the Type 2 examination for the shared dispatch service ($190,000 one-time across 2027)
- Restricted-keyway locks and door alarms at all tower shelters ($90,000 one-time)
- Enterprise AI assistant licenses and AI governance ($90,000 a year)
- Phishing-resistant MFA for finance, HR, and IT users ($70,000 a year)

Smaller items (training, exercise facilitation, contract changes) come from the operating budget. Replacement of 18 crossing monitors and 4 detector modems (R-035) is in the 2027 capital plan, not the security budget. Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-030 (Moderate, COO; within appetite because the backup vault is write-once and isolated), R-037 (Low, PTC Program Manager; physical measures documented under SD III.C.6), R-038 (Low, Director of IT; tablets encrypted and wipeable), R-039 (Low, Director of Customer Service and Car Management; vendor DDoS protection).

**Contract actions:** OT vendor security and incident notice terms (R-007, R-034), TMS recovery terms (R-014), AI vendor data-use terms (R-041), at each renewal and no later than 2027-06-30.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and operational technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Train Dispatch and PTC Operations Platform (TDPO; SSP in P02) | Chief Operating Officer, maintained by the Cybersecurity Manager | 35 risks whose affected assets include SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, SYS-07, or SYS-09 (filter the `affected_asset_or_process` column) |
| TSA compliance view (CIP, CAP, part 1570, 1580, and 1520 duties) | Cybersecurity Manager with the Director of Safety, Security, and Hazmat | 43 risks with a C-TRANSPORTATION-R01, S01, S02, or S03 driver (filter the `regulatory_driver` column); reported to TSA only as required in the CAP annual report |
| AI portfolio (P10) | Chief Engineer, with the vCISO | R-041, R-042, R-043, R-044, R-045, R-046 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-030, 2026-09-15.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example a new Critical Cyber System, an acquisition by the sponsor, or a TSA directive revision) or a significant incident.

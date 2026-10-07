# Risk Register Report: Cris Santos Company | Wholesale Trade | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed IT hardware and software wholesale distributor) |
| Size tier | Mid-Market (850 employees) |
| Vertical | Wholesale Trade |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); supply chain threats per NIST SP 800-161 Rev. 1; enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also supports | SP 800-171 Rev. 2 requirement 3.11.1 (periodic risk assessment); the C-SCRM plan (SR-2) |
| Prepared | 2026-07-31 by the Security Manager and the vCISO with the process owners; R-051 added 2026-08-14 from P07 testing; R-026 to R-032 updated 2026-09-10 from the AI assessment (P10) |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units in the BIA (P05), the Distribution Operations Platform (DOP, SYS-01 to SYS-14) including the Federal Integration Enclave, the AI tools (SYS-15, SYS-16), and the supply chain that feeds them: 251 product suppliers (214 authorized sources, 31 brokers, 6 private-label contract manufacturers), the MSSP, the DC automation integrator, and about 180 vendors with system or data access. Vulnerabilities come from the gap analysis (P03) and the control assessment (P07). The register covers three kinds of harm:
- harm to the company's own systems, data, and operations;
- harm to customers and DoD missions from the **products** the company distributes and configures;
- loss of federal business through CMMC, DFARS, FAR, or Section 889 failures.

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-17.

| Area | Appetite | Statement and measure |
|---|---|---|
| Product integrity and DoD missions | **Very low** | No risk that could put counterfeit, tampered, or covered equipment into a DoD system is accepted above Moderate. Measure: product-integrity risks above Moderate (4 today: R-003, R-006, R-023, R-051; target 0 by 2027-06-30) |
| Federal contract compliance | **Low** | Every SP 800-171 requirement that cannot be placed on a CMMC POA&M is met before the C3PAO assessment. SPRS entries and affirmations always match a documented assessment. Measure: assessment score of at least 88 with only POA&M-eligible items open by 2027-01-31 |
| Availability of distribution | **Low** | Recovery capabilities meet the BIA RTOs for all High-criticality processes. Measure: every High process has a passed recovery test in the last 12 months |
| Confidentiality of customer and employee data | **Low** | No risk of a breach notifiable in several states above Moderate. Measure: R-002 and R-046 at Moderate or lower |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor receives CUI unless it meets FedRAMP Moderate equivalency, and every Tier 1 vendor is reviewed each year (P09) |
| Innovation and AI | **Moderate** | The company wants AI in planning, service, and finance, but only through the P10 process; no AI tool makes a consequential decision about a person without human review |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that lowers likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the supply chain threat examples in SP 800-161 Rev. 1, the BIA, interviews with every process owner, the 2026 near misses (spoofed bank change, portal credential stuffing), the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (P05 section 3). Harm to a DoD mission from distributed or configured products counts as Very High.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 2 |
| High | 9 |
| Moderate | 31 |
| Low | 10 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 48 Mitigate, 4 Accept (R-037, R-041, R-048, R-052). Status: 24 Open, 24 In progress, 4 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, and R-046. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to operations or DoD missions.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware halts DC-1 and DC-2 | Very High | OT segmentation; access broker for ERP, WMS, and enclave administrators; quarterly restore tests; P08 ransomware runbook | Director of Information Technology | 2027-03-31 |
| R-003 | Counterfeit or tampered broker products ship to a DoD or commercial customer | Very High | DC-2 authenticity inspection; broker reassessments; all 12 DFARS 252.246-7007(c) criteria | Director of Quality and Product Compliance | 2026-12-31 |
| R-004 | CUI outside the enclave is disclosed | High | CUI cleanup: ERP attachment block and purge, prime-domain mail rule, Prime C onboarding, FIL-only printing | Director of Federal Programs | 2026-11-30 |
| R-005 | Attack on DC automation through the corporate network or the integrator's remote tool | High | OT VLAN, remote access gateway, OT monitoring, integrator security terms | Director of Distribution Operations | 2027-03-31 |
| R-006 | Covered (Section 889) equipment delivered on a federal order | High | Mandatory manufacturer of record; drop-ship screening; white-label attestations | Director of Federal Programs | 2026-12-15 |
| R-008 | CMMC Level 2 (C3PAO) not achieved by 2027-06-01 | High | Monthly POA&M review; non-POA&M items closed by 2027-01-31; C3PAO booked for 2027-03 | Chief Operating Officer | 2027-03-31 |
| R-011 | Reseller portal account takeover | High | Enforce reseller MFA; bot management; ship-to change alerts | Vice President of Sales Operations | 2027-01-31 |
| R-017 | Takeover of an ERP, WMS, or enclave administrator account | High | Fewer administrators; just-in-time elevation; weekly privileged activity review | Security Manager | 2027-01-31 |
| R-023 | Tampered firmware in FIL-configured equipment reaches a DoD network | High | OEM signature or hash check on every device; per-job advisory screening | Federal Integration Lab Manager | 2026-12-31 |
| R-024 | Hurricane closes DC-1 for several days | High | Drop-ship agreements; DC-2 surge plan; annual pre-season test | Director of Distribution Operations | 2027-05-31 |
| R-051 | Suspect counterfeit optical transceivers already at 2 resellers (found in P07) | High | Recall 18 units; OEM authentication of all 64; broker review | Director of Quality and Product Compliance | 2026-10-31 |

**Themes.**
- **Product integrity (R-003, R-006, R-007, R-023, R-033 to R-035, R-051).** The company inspects broker product at DC-1 but not at DC-2, and the P07 transceiver finding (R-051) shows the gap is real. The DFARS 252.246-7007 system that Prime A flowed down is only partly built.
- **CUI scope and CMMC (R-004, R-008, R-009, R-017, R-022).** The enclave is well designed, but business processes moved CUI outside it, and that lowered the assessment score below what was posted in SPRS.
- **Operational resilience (R-001, R-005, R-013, R-014, R-016, R-024).** Detection and backups are strong; OT exposure, slow WMS rebuilds, and vendor recovery terms are not.
- **AI adopted without governance (R-026 to R-032).** P10 sets conditions for each tool.

## 4. Treatment summary
**Funded in the FY2027 security and compliance plan (approved by the CEO 2026-09-17, $1.31 million one-time and $585,000 a year):**
- DC-1 OT segmentation, remote access gateway, and OT monitoring: $260,000 one-time, $45,000 a year
- C3PAO readiness support and certification assessment: $175,000 one-time
- SOC 2 readiness and Type 2 examination (P09): $165,000 one-time
- DC-2 authenticity inspection and the counterfeit avoidance program, including third-party test lab use: $160,000 one-time, $40,000 a year
- WMS recovery redesign and DR testing program: $140,000 one-time
- CUI scope cleanup and enclave expansion: $110,000 one-time
- Item master cleanup and drop-ship screening automation: $95,000 one-time
- Access broker extension to ERP, WMS, and enclave administrators: $90,000 one-time, $60,000 a year
- AI governance (adverse impact analysis for AI-005, model monitoring): $40,000 one-time, $25,000 a year
- GRC tooling and one additional GRC analyst: $40,000 one-time, $135,000 a year
- Reseller portal MFA enforcement and bot management: $35,000 one-time, $50,000 a year
- SIEM onboarding of ERP, WMS, portal, FIL firewall, and OT logs (MSSP): $150,000 a year
- Role-based training (CUI, anti-counterfeit, insider threat): $40,000 a year
- Tabletop facilitation and exercise program: $40,000 a year

Each funded item maps to a P07 POA&M entry. Smaller items (DC-2 driver waiting area, carrier portal accounts, purchase order term updates) are funded from operating budgets.

**Accepted (4):** R-037 (Low, encrypted laptops), R-041 (Low, vendor denial-of-service protection with EDI and email fallback), R-048 (Low, CCPA readiness deferred until the expansion is approved), R-052 (Low, enclave outage within the 72-hour MTD).

**Contract actions:** purchase order terms that flow down FAR 52.204-25, FAR 52.204-30, and DFARS 252.246-7008 (R-049); integrator security terms (R-005, R-050); MSSP customer responsibility matrix (R-012); ERP recovery terms at the 2027 renewal (R-014); FAR 52.204-21 terms or a federal-order filter for the forecasting vendor (R-032).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as two lines, "Cybersecurity and operational resilience" (owner: Chief Operating Officer) and "Product integrity and federal compliance" (owner: Chief Operating Officer with the Vice President of Supply Chain), reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Distribution Operations Platform (SSP in P02) | Director of Information Technology | 33 risks whose `affected_asset_or_process` includes SYS-01 to SYS-14 |
| CMMC assessment scope (enclave and FIL) | Federal Integration Lab Manager with the Director of Federal Programs | R-004, R-008, R-009, R-017, R-018, R-019, R-020, R-022, R-023, R-034 |
| DC automation (OT) | Director of Distribution Operations | R-001, R-005, R-038, R-050 |
| Supply chain (C-SCRM plan) | Vice President of Supply Chain | R-003, R-006, R-007, R-015, R-023, R-033, R-034, R-035, R-049, R-051 |
| AI portfolio (P10) | Director of Inventory Planning (AI-001) with the vCISO | R-026 to R-032 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-037, R-041, R-048, and R-052, 2026-09-17.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security and compliance budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example the West Coast expansion, R-048), a significant incident, or a change in CMMC or FAR rules (P03 section 6).

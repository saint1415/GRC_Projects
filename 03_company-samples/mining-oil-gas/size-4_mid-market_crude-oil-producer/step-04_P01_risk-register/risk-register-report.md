# Risk Register Report: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed independent crude oil producer with a Panhandle gathering system) |
| Size tier | Mid-Market (850 employees) |
| Vertical | Mining, Quarrying, and Oil and Gas Extraction |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, and the Appendix I semi-quantitative values); OT threat guidance from NIST SP 800-82 Rev. 3 (section 4.1.2, Appendix C); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also supports | CSF 2.0 GV.RM and ID.RA outcomes (P03 benchmark); the hazard analysis behind the gathering system emergency procedures (49 CFR Part 195, P03 section 1) |
| Prepared | 2026-07-31 by the GRC Analyst and the Security Manager, with the OT Security Engineer; R-052 added 2026-08-14 from P07 testing |
| Approved | 2026-09-16: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High, risk appetite); field-operations items agreed by the VP Operations; presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (3 operating areas, the control room, gathering and measurement, production accounting, finance, engineering, and corporate support), the Field SCADA and Production Accounting System (FSPA, P02), the cloud landing zone (P04), the SaaS applications, the 64 vendors with system or data access, and the AI portfolio (P10). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (manager level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer, with the VP Operations' agreement when field operations or safety are affected | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-16.

| Area | Appetite | Statement and measure |
|---|---|---|
| Safety and environment | **Very low** | No cyber risk that could plausibly cause an injury, an H2S exposure, or a release of oil or produced water is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: cyber risks with a safety or release consequence above Low (9 today: R-001, R-003, R-004, R-006, R-008, R-028, R-033, R-040, R-052; target 0 by 2027-12-31) |
| Pipeline compliance | **Very low** | No condition that could cause a missed 1-hour accident notice or an operation above MOP on the regulated trunk line is tolerated. Measure: R-006 and R-028 at Low by 2027-06-30 |
| Availability of field operations | **Low** | Recovery capabilities must meet the BIA RTOs for all High-criticality processes (P05). Measure: every High process has a passed recovery or failover test in the last 12 months (0 of 6 today) |
| Confidentiality of personal information | **Low** | No risk of a breach affecting 500 or more people is accepted above Moderate. Measure: R-002 and R-037 at Low by 2027-06-30 |
| Measurement integrity and shipper commitments | **Low** | Shipper statements must be accurate and timely enough to pass a SOC 2 Type 2 examination with no exceptions on Processing Integrity criteria. Measure: R-007, R-021, and R-051 at Low by 2027-04-01, the start of the observation period (P09) |
| Third parties | **Moderate**, with conditions | Vendors are needed for OT support, but no vendor may reach the SCADA network except through the jump host, and every critical vendor is assessed each year |
| Innovation and AI | **Moderate** | AI is welcome in maintenance, leak analytics, and office productivity, but only through the P10 process. No AI may write to SCADA, and no AI may make an employment decision without review |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $3 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 Appendix C (OT threat sources and vulnerabilities), the BIA, interviews with every process owner and all 3 Field Superintendents, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, safety and environment, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 6 |
| Moderate | 28 |
| Low | 17 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 41 Mitigate, 9 Accept, 1 Share/Transfer (R-018), 1 Avoid (R-034). Status: 26 Open, 17 In progress, 9 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001, R-002, and R-018. It is the recorded treatment only for R-018, a vendor breach whose likelihood the company cannot change much; for the others it does not lower the likelihood of harm to people, the environment, or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware from business IT reaches SCADA through the BCC or South Florida paths around the OT DMZ | Very High | Extend the OT DMZ pattern to the BCC and South Florida; interim rule reduction by 2026-11-30 | OT Security Engineer | 2027-03-31 |
| R-002 | Exfiltration of royalty owner and employee personal information for extortion | High | Remove Social Security numbers from the data platform; secure transfer of owner tax files; egress alerting | Production Accounting Director | 2026-12-31 |
| R-003 | SCADA images and controller programs destroyed, so SCADA cannot be rebuilt within the RTO | High | Second offline image set with no network path; quarterly test restores; complete the controller repository | SCADA and Automation Manager | 2027-01-31 |
| R-006 | Manipulated pump station setpoints cause an overpressure event or hide a release near a drinking water area | High | Setpoint changes through the CAB with a second reviewer; alarm on setpoint writes; monthly MOP comparison | Pipeline Compliance Manager | 2027-01-31 |
| R-020 | OT vendors with weak security become the entry point to SCADA | High | Assess the 3 critical OT vendors; security schedules at renewal; vendor tiering | General Counsel | 2027-03-31 |
| R-036 | Cyber insurance claim disputed because vendor remote access lacked MFA | High | Close R-004 and R-052; confirm to the carrier before renewal | CFO | 2026-12-31 |
| R-052 | Packager gateways reachable from the internet with a shared password (P07 finding) | High | Block inbound internet access now; move support to the jump host; change passwords | OT Security Engineer | 2026-10-31 |

**Themes.**
- **The program stops at the edge of the Panhandle (R-001, R-005, R-011, R-012, R-014, R-024, R-041).** The OCC is segmented, monitored, patched, and under change control. The South Florida office, the BCC, and field devices outside the Panhandle are not, and the BCC is both the recovery site and a path around the OT DMZ.
- **Vendor paths are the largest exposure (R-004, R-019, R-020, R-036, R-052).** The jump host works for the integrator, but two vendors kept their own always-on paths, and one of them was reachable from the internet.
- **The gathering system turns cyber risk into pipeline safety and reporting risk (R-006, R-007, R-028, R-033).** Hardwired shutdowns limit the worst outcomes, but setpoint integrity, leak detection, and the 1-hour notice depend on people and procedures that were not linked to cyber events until this year.
- **Measurement integrity now has customers (R-007, R-021, R-022, R-051).** The shippers' request for a SOC 2 report makes measurement data a service commitment, not only an internal control.
- **Personal information at scale (R-002, R-009, R-018, R-037, R-038).** About 14,000 royalty owners spread over more than 40 states make any breach a multi-state notification event.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-16, $1.45 million one-time and $410,000 a year):**
- OT DMZ extension to the BCC and South Florida office, with firewall replacement ($320,000)
- OT monitoring sensors for South Florida, Alabama, and the BCC, plus OT coverage in the MDR contract ($180,000 one-time, $150,000 a year)
- BCC standby server and South Florida HMI upgrade with the SCADA vendor ($260,000)
- Vendor remote access consolidation on the jump host, including packager and flow computer vendor support ($60,000)
- Offline image vault, spare SCADA server for restore tests, and the BCC failover test program ($110,000)
- Controller program repository and change control tooling for all 3 areas ($90,000 one-time, $25,000 a year)
- Privileged access management extended to SCADA administrator accounts ($70,000 one-time, $35,000 a year)
- Vendor risk program and one additional GRC analyst position ($140,000 a year)
- SOC 2 readiness and Type 2 examination for gathering and measurement services ($240,000 across 2027)
- Flow computer configuration logging and measurement reconciliation automation ($120,000 one-time, $20,000 a year)
- Field security briefings and crisis management exercises ($40,000 a year)

Smaller items (USB blocking at field offices, cabinet door switches at replacement, contract amendments) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (9):** R-013 (Low, VP Operations; radio refresh in 2028), R-015 (Moderate, accepted by the COO with the VP Operations; weather risk controlled by the pre-storm shut-in procedure), R-017, R-023, R-026, R-027, R-043, R-044, and R-050 (all Low, accepted by their owners).

**Transferred (1):** R-018 (Moderate; notice terms plus insurance). **Avoided (1):** R-034 (the HR screening feature stays off).

**Contract actions:** OT vendor security schedules (R-020), gathering agreement amendments (R-021), and the telematics vendor SOC 2 request (R-030), due between 2026-12-31 and 2027-06-30.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and OT resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks. The enterprise risk register also holds the process safety and environmental risks owned by the HSE Director; the 9 cyber risks with a safety or release consequence (section 1) are cross-listed there so that the quarterly HSE risk review sees them.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Field SCADA and Production Accounting System (FSPA; SSP in P02) | SCADA and Automation Manager, for the COO | 35 risks whose affected assets include SYS-01, SYS-02, SYS-12, SYS-14, or BP-01 to BP-05 (filter the `affected_asset_or_process` column) |
| Gathering system (Part 195 duties) | Pipeline Compliance Manager | R-004, R-006, R-007, R-028, R-033, R-050, R-051 |
| Shipper services (SOC 2 scope, P09) | Measurement Supervisor | R-007, R-021, R-022, R-044, R-051 |
| AI portfolio (P10) | Production Engineering Manager (AI review chair) | R-031, R-032, R-033, R-034 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-015, 2026-09-16.
- VP Operations: agreed to the treatments and acceptances that affect field operations (R-013, R-015, R-026), 2026-09-16.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-16.
- Board audit committee: received the results on 2026-09-16. Next report: the December 2026 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example an acquisition, R-048, or a TSA notification, R-049) or a significant incident.

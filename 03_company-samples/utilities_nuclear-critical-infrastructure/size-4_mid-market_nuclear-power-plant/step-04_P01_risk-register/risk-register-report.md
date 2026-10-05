# Risk Register Report: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed owner and operator of a single-unit nuclear generating station) |
| Size tier | Mid-Market (850 employees) |
| Vertical | Nuclear Reactors, Materials, and Waste |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also supports | 10 CFR 73.54(d)(2) "evaluate and manage cyber risks" for the business network side of the CSP boundary; inputs to the 73.55(m) program review and the CIP-003-9 low-impact plan |
| Prepared | 2026-07-31 by the IT Security Manager and the vCISO with the Cyber Security Program Manager; R-052 added 2026-08-14 from P07 testing |
| Approved | 2026-09-17: Site Vice President (Moderate and below), Chief Executive Officer (High and Very High, and the risk appetite); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units at the Station and the EOF; the PBN-WMS (SYS-01 to SYS-11); the interfaces to the CSP scope (SYS-12 to SYS-14), the dispatch network (SYS-15), and the SGI computers (SYS-16); the AI tools (SYS-17); and about 210 vendors (SYS-18). Processes and impact values come from the BIA (P05). Vulnerabilities come from the gap analysis (P03) and control assessment (P07).

**What this register does not replace.** Cyber risk to CDAs is managed by the CST under the CSP (73.54(d)(2)), through CDA assessments, the corrective action program, and the defensive architecture. This register covers the enterprise, the business network, and **the boundary where the two meet**. Risks that touch the boundary (R-001, R-006, R-017, R-020, R-035, R-036, R-052) are co-owned with the Cyber Security Program Manager, and any change they drive in CSP scope goes through the CSP processes.

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (manager level or above) | Recorded in the register; reviewed annually |
| Moderate | Site Vice President | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

**Rules that override the table.** A risk that could create a regulatory noncompliance with the CSP, 73.77, 73.21-73.22, or 73.56 cannot be accepted at any level. It must be corrected and entered in the corrective action program. Acceptance can only cover the time needed to correct it.

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-17.

| Area | Appetite | Statement and measure |
|---|---|---|
| Nuclear safety and the CSP boundary | **None** | No business network risk may create a path to, or a dependency of, a safety, security, or EP function. Any such finding is corrected through the CSP and the CAP. Measure: unevaluated changes touching 73.54 scope (3 today: R-006, R-007, R-020; target 0 by 2026-11-30) |
| Personnel and radiological safety | **Very low** | No risk to worker protection (clearances, RWPs) is accepted above Low. Measure: R-002, R-010, R-018, R-019 at Low or below by 2027-06-30 |
| Regulatory compliance (NRC and NERC) | **Very low** | No known noncompliance stays open longer than the corrective action program allows. Measure: open regulatory gaps in P03 (tracked quarterly) |
| Refueling outage resilience | **Low** | Business systems must meet the BIA RTOs before each refueling outage. Measure: passed failover tests for WMS and CAP/EDMS before 2027-03-08 |
| Confidentiality of security information | **Low** | SGI never leaves the SGI program; SRI stays in restricted locations. Measure: SRI found outside restricted folders in quarterly searches (target 0 by 2027-03-31) |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but every Tier 1 vendor has current assurance reviewed each year (P09), and no vendor connects to the business network without named accounts and terms |
| Innovation and AI | **Moderate** | The company wants AI benefits in maintenance, engineering, and business work, but only through the P10 governance process, and never in a way that touches CDAs or makes decisions about safety |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $1 million insurance retention are tolerable. Scenarios above $3 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the nuclear vertical overlay (nation-state interest in nuclear facilities, insider threat, supply chain), the BIA, interviews with process owners and the CST, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA categories (cost, operations, regulatory, safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

**Why R-001 is High and not Very High.** A nation-state intrusion is plausible (initiation High) and the consequence of reaching Level 3 would be Very High. But the one-way deterministic device, the absence of remote access to Level 4, and the PMMD process make an adverse impact on CDAs unlikely (adverse impact Low). Table G-5 gives an overall likelihood of Moderate, and Table I-2 gives High. The boundary is doing its job; the risk is in the business network's weaknesses around it.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 8 |
| Moderate | 28 |
| Low | 15 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 44 Mitigate, 8 Accept (R-016, R-025, R-027, R-033, R-036, R-040, R-041, R-048, all Low). Status: 23 Open, 21 In progress, 8 Accepted.

Cyber insurance ($25 million limit, $1 million retention) transfers part of the financial exposure for R-002, R-003, and R-030. It is not recorded as the treatment for any risk, because it does not reduce safety or regulatory consequences.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-002 | Ransomware during a refueling outage halts work control, clearances, RWPs, and CAP | Very High | Failover tests before the 2027 outage; 15-minute clearance log shipping; segmentation; privileged access management | IT Director | 2027-02-28 |
| R-001 | Business network intrusion attempts to pivot toward Level 3 | High | Boundary-attempt alerting; receive server hardening; segmentation; joint drill | Cyber Security Program Manager | 2027-02-28 |
| R-003 | Ransomware on the business network while online | High | Same program as R-002 | IT Director | 2027-02-28 |
| R-004 | Domain administrator account takeover | High | Privileged access management; FIDO2 keys; remove vendor domain administrator accounts | IT Security Manager | 2027-01-31 |
| R-006 | Changes made outside the CST process create unevaluated data paths (73.54(d)(3)) | High | CST evaluates the 3 changes; CSP scope question on every IT change | Cyber Security Program Manager | 2026-11-30 |
| R-007 | ERO callout service outage or compromise delays emergency staffing | High | CST evaluation; second callout path; quarterly call tree test | Emergency Preparedness Manager | 2026-12-31 |
| R-008 | Vendor compromise through a shared VPN account | High | Named, time-limited vendor accounts through the access broker, with recording | IT Security Manager | 2026-11-30 |
| R-018 | Exploitation of the out-of-support clearance servers | High | Dedicated VLAN; disable SMBv1; upgrade after the outage | Director of Work Management | 2027-06-30 |
| R-052 | Receive server management interface with default credentials (found in P07) | High | Keep disconnected; management VLAN; inventory all management interfaces | Cyber Security Program Manager | 2026-10-31 |

**Themes.**
- **The boundary is strong; the business network around it is not (R-001, R-004, R-005, R-012, R-052).** Standing administrator rights, a flat server layer, and blind spots in monitoring are what an attacker would use to stage an approach to the one-way device.
- **Change management between IT and the CST (R-006, R-007, R-017, R-020).** Three changes reached Level 3 data or EP functions without a 73.54(d)(3) evaluation. The fix is a process, not a product.
- **Outage resilience (R-002, R-010, R-011, R-018, R-019).** The business network matters most during refueling outages, when it costs about $2.03 million a day. The next outage starts 2027-03-08.
- **Vendors and NERC (R-008, R-009, R-014, R-034).** Shared vendor accounts, a CIP-003-9 Section 6.3 gap, and missing transient asset evidence.
- **AI adopted without governance (R-020 to R-025).** P10 addresses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-17, $1.43 million one-time and $445,000 a year):**
- Privileged access management for on-premises administrators and FIDO2 keys ($210,000 one-time, $95,000 a year)
- Server segmentation of the business network, receive server and historian replica first ($280,000)
- SIEM onboarding of WMS, EDMS, CAP, the receive server, and GDSR, with boundary-attempt use cases ($110,000 a year through the MSSP)
- WMS and CAP/EDMS failover testing and 15-minute clearance log shipping ($160,000)
- Clearance and tagging module upgrade off Windows Server 2012 R2 (2027 capital plan, $450,000)
- Vendor risk program tooling and one GRC analyst position ($150,000 a year)
- SOC 2 readiness and the first Type 2 examination for the GDSR service ($240,000 across 2027)
- Sensitivity labels and DLP for SRI ($90,000 a year)
- Intrusion detection sensor on the dispatch network vendor path for CIP-003-9 Section 6.3 ($60,000)
- Cellular failover at the EOF ($25,000)

Smaller items (EOF network room badge reader, paper CAP intake forms, contractor training content) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (8, all Low):** R-016 (Director of Security; SGI program controls met in P03), R-025 (price forecast errors under fixed-price PPAs), R-027 (GDSR delays covered by manual fallback), R-033 (cloud regional outage), R-036 (one-way device failure; Level 3 unaffected), R-040 (encrypted laptops), R-041 (dual carriers), R-048 (pending NRC rule changes, monitored).

**Regulatory actions:** the CST evaluations (R-006, R-007, R-020) are entered in the CAP. The CIP-003-9 Section 6.3 gap (R-009) is being assessed with the Compliance and GRC Lead for a possible self-report to the Regional Entity; that decision is due 2026-10-31.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and technology resilience", owned by the Site Vice President and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, so there is one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| PBN-WMS (SSP in P02) | IT Security Manager | Every risk whose affected assets include SYS-01 to SYS-11 (filter the `affected_asset_or_process` column) |
| CSP boundary (interface with the CST's own CDA risk process) | Cyber Security Program Manager | R-001, R-006, R-017, R-020, R-035, R-036, R-052 |
| Refueling outage readiness | Outage Manager with the IT Director | R-002, R-010, R-011, R-018, R-019, R-038, R-045 |
| NERC CIP low impact | Compliance and GRC Lead | R-009, R-034 |
| AI portfolio (P10) | vCISO | R-020, R-021, R-022, R-023, R-024, R-025 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Site Vice President: approved Moderate and Low treatments, 2026-09-17.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example, a CSP amendment, a new PPA, or a significant incident).

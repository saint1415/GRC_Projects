# Risk Register Report: Cris Santos Company | Manufacturing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed connected medical device manufacturer) |
| Size tier | Mid-Market (850 employees; SBA-small for NAICS 334510, Mid-Market by the tier rule) |
| Vertical | Manufacturing (NAICS 334510) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | HIPAA risk analysis and risk management for the CCC as a business associate, 45 CFR 164.308(a)(1)(ii)(A)-(B); input to the cybersecurity risk assessments that section 524B and FDA's premarket guidance expect for devices and related systems |
| Prepared | 2026-07-31 by the Security Manager, the Product Security Manager, and the vCISO; R-049 added 2026-08-21 from P07 testing |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units, the Device Lifecycle Platform (DLP, SYS-01 to SYS-09), fielded devices (SYS-12), the ERP and support apps (SYS-10, SYS-11), third parties (SYS-13), and AI tools (SYS-14). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Two kinds of harm are rated together.** Enterprise cyber risks (ransomware, PHI exfiltration, fraud) and product security risks (exploitable devices, signing and provisioning paths) sit in one register, so the board sees one list. Device risks are also assessed in the design risk management files in PLM, where FDA's guidance expects exploitability to be rated separately from safety probability. This register uses the SP 800-30 scale for both, and each product risk links to its PLM risk file.

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
| Patient safety | **Very low** | No cyber risk that could plausibly contribute to patient harm is accepted above Low. Each such risk above Low must have a funded treatment plan within 90 days. Measure: 11 safety-linked risks are above Low today (R-001, R-002, R-006, R-009, R-010, R-015, R-016, R-024, R-033, R-037, R-049); target none above Moderate by 2027-06-30 |
| Product security and FDA compliance | **Low** | Every critical vulnerability with uncontrolled risk gets a customer communication within 30 days and a validated fix within 60 days of the company learning of it, as FDA's postmarket guidance describes. No section 524B statutory row in P03 may stay Partially met or Not met beyond 2027-06-30. Measure: time from identification to patch, and patch to field deployment (P03 TPLC metrics) |
| Confidentiality of PHI held for hospitals | **Low** | No risk of a breach affecting more than one hospital is accepted above Moderate. Measure: R-007 at Moderate or lower by 2026-12-31 |
| Availability of CCC services | **Low** | Recovery capabilities must meet the BIA RTOs for BP-01 and BP-02 (P05). Measure: a passed failover test in the last 6 months |
| Production continuity | **Moderate** | Plant outages up to the finished goods buffer (2 weeks for pumps) are tolerable. Scenarios that could exceed it need a treatment that reduces likelihood. Measure: R-005 at Moderate by 2027-03-31 |
| Third parties and suppliers | **Moderate**, with conditions | No subcontractor receives PHI without a BAA, and every Tier 1 vendor and critical software supplier is reviewed each year (P09) |
| Innovation and AI | **Moderate** | AI is welcome in products and operations, but only through the AI governance process in P10. No AI function that affects device performance or regulatory decisions is used without validation |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $3 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Manufacturing overlay, FDA's premarket and postmarket guidance (threat modeling, multi-patient harm, uncontrolled risk), SP 800-82 Rev. 3 Appendix C (OT threats and vulnerabilities), the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, patient safety, reputation). Any risk that could affect many patients at once (multi-patient harm) was rated Very High impact.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 0 |
| High | 9 |
| Moderate | 28 |
| Low | 13 |
| Very Low | 0 |
| **Total** | **50** |

Treatments: 46 Mitigate, 4 Accept (R-041, R-043, R-046, R-050). Status: 24 Open, 22 In progress, 4 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-005, R-006, and R-007. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm, and product liability for device failures sits outside the cyber policy.

### Top risks (High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Exploited vulnerability in fielded IP-4 pumps changes infusion settings | High | Quarterly IP-4 security release; adoption reporting; clear the triage backlog | VP Engineering | 2027-03-31 |
| R-002 | Exploited vulnerability in fielded VM-7 monitors alters alarms | High | Forward device security events to the CCC; keep the quarterly cycle | VP Engineering | 2027-06-30 |
| R-003 | Known exploited component vulnerability goes unassessed | High | Daily automated KEV matching; triage service levels; one more product security engineer | Product Security Manager | 2026-12-31 |
| R-005 | Ransomware stops all four plant lines and the MES | High | Segment Line 1 and Line 3; brokered vendor access; OT monitoring; offline MES backups | OT Engineering Manager | 2027-03-31 |
| R-006 | CCC intrusion interrupts remote monitoring and pump programming | High | Just-in-time access; automated failover; quarterly tests | Director of Cloud Operations | 2027-03-31 |
| R-007 | PHI for many hospitals exfiltrated from the CCC | High | Just-in-time production access; weekly privileged activity review; quarterly access reviews | Director of Cloud Operations | 2026-12-31 |
| R-009 | Malicious firmware signed through the pipeline | High | Remove standing runner administrator rights; reproducible build check | VP Engineering | 2027-03-31 |
| R-037 | AI-002 alarm model suppresses a true alarm once released | High | Bias and edge-case test plan before design freeze | Chief Medical Officer | 2027-03-31 |
| R-049 | IP-4 factory service mode left enabled on 1,140 pumps (found in P07) | High | Out-of-cycle firmware by 2026-10-16; CAPA on station change control | VP Engineering | 2026-10-16 |

**Themes.**
- **Postmarket product security at scale (R-001 to R-004, R-014, R-015, R-038, R-049).** The company met section 524B at submission time and runs the machinery (SBOMs, CVD, ISAO), but the volume of component vulnerabilities has outgrown a 4-person team, and slow field adoption means fixes do not reach patients quickly.
- **The trust chain runs through the plant (R-005, R-009, R-010, R-020, R-024, R-025).** Firmware is signed well, but device identities are issued from a plant server with a software-held key, and station changes are not controlled like product changes. R-049 is the proof.
- **Privileged cloud access (R-006, R-007, R-027).** One compromised engineer account could reach every hospital's data.
- **AI in products and quality decisions (R-033, R-034, R-036, R-037).** P10 addresses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-17, about $1.48 million one-time and $540,000 a year):**
- Plant OT segmentation, passive OT monitoring, brokered vendor access, and replacement of the 11 unsupported test stations ($520,000 one-time, $60,000 a year)
- Provisioning key and VM-5 key into the HSM, and a key recovery exercise ($90,000)
- One product security engineer and KEV automation ($180,000 a year)
- Just-in-time access for the container platform and access review tooling ($60,000 one-time, $40,000 a year)
- Automated CCC regional failover ($150,000)
- SIEM onboarding of the MES, provisioning server, build pipeline, and PLM, and OT coverage by the MSSP ($140,000 a year)
- IP-4 out-of-cycle release and field outreach ($300,000 from the engineering budget)
- SOC 2 scope expansion to Availability and Confidentiality ($160,000 across 2027)
- AI-001 postmarket subgroup monitoring and AI-002 test program ($200,000 from the product budget)
- A GRC analyst for supplier security reviews ($120,000 a year)

Smaller items (call-back verification for payments, standards writing, records retention updates) come from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted by the risk owners (4):** R-041 (Low, Director of Cloud Operations), R-043 (Low, IT Director; encrypted laptops), R-046 (Low, Product Security Manager; hospitals control segmentation), R-050 (Low, VP Engineering; the funded hire in R-003 reduces it further).

**Contract actions:** subcontractor BAAs for the 2 vendors without one (R-029) by 2026-10-31; vulnerability notification terms for critical software suppliers at renewal (R-030); interconnection terms for the 31 hospital VPNs (CA-3) by 2027-03-31.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as two lines owned by the COO and reported to the audit committee each quarter: "Cybersecurity and technology resilience" and "Product security and FDA cybersecurity compliance".

System-level registers are filtered views of this file, kept by each owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Device Lifecycle Platform (DLP; SSP in P02) | IT Director (Security Officer) | 33 risks whose affected assets include SYS-01 to SYS-09 (filter the `affected_asset_or_process` column) |
| Fielded products and PSIRT | Product Security Manager | R-001, R-002, R-003, R-004, R-009, R-010, R-012, R-013, R-014, R-015, R-038, R-045, R-046, R-049 |
| Plant OT | OT Engineering Manager | R-005, R-020, R-021, R-022, R-023, R-024, R-025, R-031, R-032, R-036 |
| AI portfolio (P10) | Chief Medical Officer | R-033, R-034, R-035, R-036, R-037 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up. Product risks are also kept in each product's design risk management file in PLM; the Product Security Manager reconciles the two each quarter.

## 6. Approval
- Risk owners: accepted R-041, R-043, R-046, and R-050 (all Low, within their authority), 2026-09-17.
- Chief Operating Officer: approved Moderate and Low treatments and noted the 4 acceptances, 2026-09-17.
- Chief Executive Officer: approved the High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. Next report: the 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example the AI-002 submission) or a significant incident.

# Enterprise Risk Register Report: Cris Santos Company | Information Technology | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded public cloud and managed infrastructure provider: regions R1 to R6, Government region G1, 41 edge PoPs; about 41,000 customers) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Information Technology |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | FedRAMP risk assessment controls RA-3 and PM-9 for FR-1 and FR-2; input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** The whole company: the six commercial regions, the Government region (G1), the edge, the software supply chain and fleet automation, the acquired managed services business (AQ-1), corporate IT, and about 2,600 vendors (310 tier 1 or tier 2). Business processes and impact values come from the enterprise BIA (P05). The HCP-G system is also covered at system level in the SSP (P02).

**The cloud provider's special risk.** Most of the company's risks are also its customers' risks. One flaw in provider tooling, isolation, or keys can affect thousands of customers at once. That aggregation is why the register rates multi-tenant events at Very High impact even when the direct cost to the company would be lower.

**Three lines.** Risk owners in engineering and operations (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).**
- **Customer trust and tenant isolation:** very low appetite for events that expose one customer's data to another or compromise customer workloads through company tooling.
- **Federal certification and regulatory compliance:** very low appetite for losing a FedRAMP certification or missing a regulatory notice or disclosure deadline.
- **Service availability:** low appetite for region-wide outages; SLAs set the measures.
- **Growth (acquisitions, new regions, AI):** moderate appetite, provided risks are identified and funded at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Multi-tenant service disruption | Moderate |
| ER-02 Compromise of customer data and tenant isolation | Moderate |
| ER-03 Integrity of provider tooling and software supply chain | Low |
| ER-04 Third-party and hardware supply chain | Moderate |
| ER-05 Integration of acquired businesses | Moderate |
| ER-06 Federal certification and regulatory compliance | Low |
| ER-07 SEC disclosure and financial reporting integrity | Low |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive |
| High | Executive risk committee (Chief Risk Officer, Chief Technology Officer, CISO, General Counsel, Chief Financial Officer), reported to the risk and technology committee of the board |
| Very High | Chief Executive Officer and Chief Financial Officer jointly, reported to the board committee at its next meeting |

Risks under ER-03 and ER-06 at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E; the cloud provider threat picture (attacks on provider tooling and managed service providers, isolation escapes, supply chain compromise, DDoS); the BIA (P05); the gap analysis (P03); and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). Events that reach many tenants at once are rated Very High.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. One severe risk is never averaged away.
   - The enterprise risk profile (section 4) is what the risk and technology committee of the board sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 10 |
| Moderate | 29 |
| Low | 25 |
| **Total** | **65** |

By threat source type: Adversarial 28, Structural 19, Accidental 16, Environmental 2.
By treatment: Mitigate 57, Accept 6, Avoid 2.
By status: In progress 48, Open 9, Closed 8 (6 accepted, 2 avoided).
**16 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Multi-tenant service disruption | Operational | 19 | 0 | 2 | 9 | 8 | **High** | Moderate | 2 |
| ER-02 | Compromise of customer data and tenant isolation | Compliance and reputational | 15 | 0 | 3 | 7 | 5 | **High** | Moderate | 3 |
| ER-03 | Integrity of provider tooling and software supply chain | Operational and strategic | 4 | 1 | 1 | 2 | 0 | **Very High** | Low | 4 |
| ER-04 | Third-party and hardware supply chain | Operational | 6 | 0 | 0 | 3 | 3 | **Moderate** | Moderate | 0 |
| ER-05 | Integration of acquired businesses | Strategic | 3 | 0 | 1 | 2 | 0 | **High** | Moderate | 1 |
| ER-06 | Federal certification and regulatory compliance | Compliance | 8 | 0 | 2 | 2 | 4 | **High** | Low | 4 |
| ER-07 | SEC disclosure and financial reporting integrity | Financial | 5 | 0 | 1 | 1 | 3 | **High** | Low | 2 |
| ER-08 | Responsible use of AI | Strategic | 5 | 0 | 0 | 3 | 2 | **Moderate** | Moderate | 0 |
| **Total** | | | **65** | **1** | **10** | **29** | **25** | | | **16** |

**Reading the profile:**
- **ER-03 (provider tooling)** carries the only Very High risk: a malicious guest-agent release pushed through fleet automation (R-001). All four of its risks are outside its Low tolerance, because the release path, the build system, signing, and BMC firmware are each a way to reach every host or guest.
- **ER-06 (federal certification)** holds two High risks: missing the Class D window before 2027-06-11 (R-012) and losing FR-1 or FR-2 when 2026 rule grace periods end (R-014).
- **ER-02 (tenant isolation)** has three High risks: hypervisor escape (R-003), a control plane authorization flaw (R-004), and late patching of known exploited vulnerabilities (R-006).
- **ER-05 (acquisitions)** is driven by the AQ-1 legacy RMM tool (R-002), which reaches about 9,500 customer servers outside the company's identity and logging controls.
- **ER-08 (AI)** is within tolerance today, but 5 of 15 use cases lack committee review (R-045) and AI triage can act without a human for some alert classes (R-019).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Stolen engineer session used to push a malicious guest-agent release to enrolled customer VMs and SL-3 servers | Very High | ER-03 | Two-person approval from separate teams; approver signature; automated rollout halt (POAM-001); runbook tabletop | Vice President, Software Supply Chain | 2026-12-15 |
| R-002 | Takeover of the AQ-1 legacy RMM tool reaches about 9,500 customer servers | High | ER-05 | PAM and workforce identity for AQ-1 staff; real-time logs; vendor terms; migration to fleet automation (POAM-022) | Senior Vice President, Managed Infrastructure Services | 2027-03-31 |
| R-003 | Tenant escapes VM isolation through a hypervisor flaw | High | ER-02 | Live patching for all hypervisor releases; dedicated hosts for the G1 High workload | Vice President, Platform Engineering | 2027-03-31 |
| R-004 | Control plane authorization flaw exposes other tenants' resources | High | ER-02 | Remaining APIs onto the central policy engine; cross-tenant fuzzing | Vice President, Control Plane Engineering | 2027-01-31 |
| R-005 | Faulty configuration change stops a whole region | High | ER-01 | Cell-based deployment for network configuration; rollback drills | Vice President, Global Network | 2027-03-31 |
| R-006 | Known exploited vulnerability exploited after its due date | High | ER-02 | Automated KEV due-date tracking; Class D timeframes for G1 (POAM-007) | Director of Security Operations | 2026-12-31 |
| R-011 | G1 site loss exceeds the 2-hour RTO | High | ER-01 | Parallel tenant database restore; full failover test (POAM-009) | Vice President, Control Plane Engineering | 2027-01-31 |
| R-012 | Class D certification not obtained before the 2027-06-11 Rev5 cutoff | High | ER-06 | Class D program (POAM-021); validated cryptographic modules (POAM-004); 20x fallback | Senior Vice President, Government Cloud | 2027-05-28 |
| R-014 | FR-1 or FR-2 lost when a 2026 ruleset grace period ends | High | ER-06 | Ongoing Certification Reports (POAM-019); SDR (POAM-020); trust center (POAM-024); VDR timeframes (POAM-007) | Director of FedRAMP Compliance | 2027-08-01 |
| R-018 | Material multi-tenant incident disclosed late or inaccurately | High | ER-07 | Multi-tenant factors in the materiality worksheet; disclosure committee tabletop 2026-11-18 (POAM-011) | General Counsel | 2026-11-30 |
| R-027 | Build system compromise injects code before signing | High | ER-03 | Isolated build runners per channel; provenance verified at signing; reproducible guest-agent builds | Vice President, Software Supply Chain | 2027-03-31 |

## 6. Themes from the 2026 analysis
1. **Provider tooling is the crown jewel (ER-03).** Fleet automation, the build system, the signing service, and firmware can each reach every host or guest. The guest-agent channel is the weakest link today (R-001), and it is the P08 scenario.
2. **FedRAMP is changing under a live certification (ER-06).** The company must keep two Rev5 Class C certifications current with the 2026 rules (ruleset dates from 2026-12-07 for vulnerability rules to 2028-02-01 when all grace periods end) while it upgrades SL-2 to Class D. Missing the 2027-06-11 Rev5 cutoff would force the 20x path for Class D (R-012).
3. **AQ-1 sits outside the controls (ER-05).** The acquired managed services business still runs a legacy RMM tool and directory (R-002, R-015). Future deals need a security gate (R-060).
4. **Tenant isolation is the brand (ER-02).** Isolation escapes and authorization flaws are rare but would affect many customers at once (R-003, R-004).
5. **Materiality for a multi-tenant incident (ER-07).** The worksheet does not yet quantify SLA credits, churn, or federal certification impact (R-018).
6. **AI in the SOC (ER-08).** AI triage scores and, for some classes, acts on alerts; human approval is being added for host isolation and account suspension (R-019), and adversarial testing for crafted log content (R-047).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $38 million:** Class D program including cryptographic module replacement ($14.5M), AQ-1 migration and identity integration ($6.2M), live patching and R3 hypervisor upgrade ($7.8M), release path hardening and build isolation ($4.1M), G1 recovery and failover work ($2.6M), FedRAMP 2026 rules tooling and trust center ($1.9M), and DDoS capacity ($0.9M). Items map to the POA&M in P07.
- **Accepted (6):** R-034, R-041, R-050, R-052, R-058, R-064. Each is Low residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-046 (support assistant restricted to public documentation and the current case) and R-055 (no supplier access to G1 data or customer content from countries of concern).
- **Very High risk R-001:** not accepted as is. The Chief Executive Officer and Chief Financial Officer approved the treatment plan and a residual target of Moderate on 2026-09-08; the risk and technology committee of the board reviewed it on 2026-09-10.

## 8. Board reporting
**Risk and technology committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting, risk acceptances, and Class D program status. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-057), disclosure controls (R-018), and the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- Chief Executive Officer and Chief Financial Officer: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk and technology committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, or acquisition. KRIs are refreshed quarterly.

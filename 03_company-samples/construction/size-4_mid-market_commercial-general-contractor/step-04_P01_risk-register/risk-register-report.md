# Risk Register Report: Cris Santos Company | Construction | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial and institutional building general contractor) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Construction |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | Risk assessment for NIST SP 800-171 Rev. 2 requirements 3.11.1 and 3.12.2 (CPE scope); input to the CMMC Level 2 readiness plan |
| Prepared | 2026-07-31 by the GRC analyst and Security Manager with the vCISO; R-051 added 2026-08-14 and R-052 added 2026-08-19 from P07 testing |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High, risk appetite); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units in the BIA (P05), the Project Delivery and Payment Platform and its CUI Project Enclave (P02), the cloud environment (P04), the MBSS platform, about 210 vendors and about 450 subcontractors and suppliers, and the 6 AI uses (P10). Impact values come from the BIA; vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

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
| Payment integrity | **Very low** | No payment instruction, bank change, or remittance change is acted on without out-of-band verification. Measure: payment-fraud risks (R-001, R-002, R-025, R-033, R-040) at Moderate or lower by 2027-03-31; zero bank changes without call-back evidence in quarterly samples |
| CUI and federal contract compliance | **Very low** | CUI is handled only on systems that meet DFARS 252.204-7012, and no federal representation (SPRS score, SAM, CMMC affirmation) is made without evidence reviewed by counsel. Measure: R-003 and R-008 at Moderate or lower by 2026-12-31; CMMC Level 2 (C3PAO) status before the follow-on MATOC award |
| Worker and client safety | **Very low** | No technology risk that could lead crews to work from wrong life-safety details, or leave a client's security systems unmonitored, is accepted above Low. Measure: R-021 and R-034 at Moderate or lower by 2026-12-31, and Low by 2027-06-30 |
| Availability of bidding, billing, and MBSS | **Low** | Recovery must meet the BIA RTOs for all High-criticality processes (P05). Measure: every High process has a passed recovery test in the last 12 months (today 1 of 7: BP-05) |
| Third parties and subcontractors | **Moderate**, with conditions | Subcontracting is the business model, but no subcontractor receives CUI without DFARS flowdown and a verified SPRS score, and every Tier 1 vendor is reviewed each year (P09) |
| Innovation and AI | **Moderate** | The company wants AI in estimating, safety, accounting, and MBSS, but only through the AI review process in P10. No AI tool receives CUI; no AI tool can change payment data |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $250,000 insurance retention are tolerable. Scenarios above $1 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Construction overlay (business email compromise and payment fraud, federal contract obligations), the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, contract and regulatory, safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.
6. **Registers.** `system_register` names the register or registers that own each risk (section 5).

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 2 |
| High | 7 |
| Moderate | 34 |
| Low | 9 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 49 Mitigate, 3 Accept (R-036, R-046, R-050). Status: 27 Open, 22 In progress, 3 Accepted.

Cyber insurance ($10 million limit, $1 million social engineering sublimit, $250,000 retention) transfers part of the financial exposure for R-001, R-002, and R-005. It is not recorded as the treatment for any risk, because the sublimit is smaller than one average pay app and insurance does not reduce contract or eligibility harm.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-003 | CUI handled outside the enclave (commercial project platform, tablets, printed sets) | Very High | Remove CUI from SYS-01 and tablets; assess the spill under DFARS 252.204-7012(c)(1)(i); CPE workflow and virtual desktop field access; CUI training | FC-4 Project Executive | 2026-12-31 |
| R-005 | Ransomware halts bidding, billing, payroll, and field document flow | Very High | Phishing-resistant MFA; router baseline; privileged access management for SaaS administrators; nightly SaaS exports; tabletop | IT Director | 2027-03-31 |
| R-001 | Business email compromise redirects an owner's progress payment | High | Phishing-resistant MFA for payment roles; owner remittance-change letters; lookalike-domain monitoring; DMARC reject | Chief Financial Officer | 2026-12-31 |
| R-002 | Fraudulent subcontractor bank change diverts a payment | High | Remove the urgent override; call-back evidence; change alerts; first-payment hold | Controller | 2026-10-31 |
| R-004 | CUI stolen from a subcontractor without flowdown or verified security | High | Flowdown to 14 trades; SPRS verification; CUI only through the CPE | Director of Contracts and Compliance | 2026-11-30 |
| R-007 | Not CMMC Level 2 (C3PAO) certified by the follow-on MATOC award | High | P03 roadmap; readiness check 2027-03; C3PAO assessment 2027-04 | Chief Operating Officer | 2027-04-23 |
| R-008 | SPRS score or affirmation overstates implementation (False Claims Act exposure) | High | Corrected score (-23) by 2026-09-30 with counsel review; independent reperformance | General Counsel | 2026-09-30 |
| R-016 | Stolen enclave session used to steal CUI without detection | High | Monitoring service inside the government-community cloud; correlation with corporate identities | Security Manager | 2027-01-31 |
| R-021 | MBSS remote access used to control a client's access control or cameras | High | All sites through the company gateway with named, recorded sessions | Director of Technology and Security Systems | 2026-12-31 |

**Themes.**
- **Money moves by email (R-001, R-002, R-025, R-026, R-033, R-040, R-041).** The company has good payment approvals, but the chain still starts with an email that can be faked or sent from a hijacked mailbox. The fixes are phishing-resistant MFA, out-of-band verification that cannot be overridden, and telling owners and subcontractors how the company will and will not change bank details.
- **CUI outgrew the enclave (R-003, R-004, R-007 to R-009, R-016, R-017, R-038, R-039, R-043, R-044, R-052).** The enclave itself is sound. The problem is that construction work moves drawings to trailers, tablets, and 14 trade subcontractors, and the enclave design did not follow them.
- **The field is the edge (R-011, R-012, R-023, R-024, R-047).** Jobsite routers, tablets, and short-term staff and subcontractors are where controls thin out.
- **Client-facing services (R-020 to R-022, R-034, R-036).** The MBSS line puts the company inside clients' security systems, which raises the stakes of a remote-access compromise.
- **AI adopted without review (R-029 to R-034).** Six AI uses went live without review. P10 addresses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-17, $1.05 million one-time and $360,000 a year):**
- CPE field access through virtual desktops on managed tablets, licenses, and the CUI room in the FC-4 trailer ($220,000)
- Jobsite router replacement and central management ($180,000)
- Phishing-resistant MFA for payment roles and executives ($60,000)
- C3PAO Level 2 assessment ($150,000) and a readiness check by the internal audit firm ($80,000)
- SOC 2 readiness and Type 2 examination for MBSS ($200,000 across 2027)
- SaaS export tooling for SYS-01 and SYS-02 ($40,000) and MBSS gateway expansion ($70,000)
- Training and exercises, including the CUI incident tabletop and DIBNet drill ($50,000)
- Annual: CPE monitoring service ($90,000), SaaS log collection ($60,000), CPE backup ($30,000), vendor risk tooling ($40,000), lookalike-domain monitoring ($20,000), and one additional security analyst for the CPE ($120,000)

Each funded item maps to a P07 POA&M entry or a P03 roadmap milestone.

**Accepted (3):** R-036 (Low, IT Director; second circuit and generator in place), R-046 (Low, Equipment and Fleet Manager; low data sensitivity), R-050 (Low, General Counsel; records exist in vendor systems).

**Contract actions:** DFARS 252.204-7012 flowdown to 14 FC-4 trades (R-004) by 2026-11-30; DFARS 252.204-7021 rider in subcontract templates before 2026-11-10; ERP billing-week priority support at the 2027 renewal (R-018); Section 889 confirmation from every jobsite technology rental vendor (R-051).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, payment integrity, and federal contract compliance", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each owner, rather than separate spreadsheets. That keeps one set of ratings. Filter the `system_register` column:

| Register | Owner | Risks | Notes |
|---|---|---|---|
| Enterprise (company-wide risks owned by an executive) | Chief Operating Officer | 24 | Includes the payment fraud, ransomware, and CMMC eligibility risks |
| PDPP (SSP in P02) | Security Manager | 19 | Corporate PDPP components |
| CPE (CMMC Level 2 scope) | Security Manager with the FC-4 Project Executive | 14 (1 Very High, 4 High, 9 Moderate) | Supports SP 800-171 Rev. 2 3.11.1 and the POA&M for the C3PAO assessment |
| MBSS (SOC 2 scope, P09) | Director of Technology and Security Systems | 5 | R-020, R-021, R-022, R-034, R-036 |
| AI portfolio (P10) | vCISO, chairing the AI review group | 6 | R-029 to R-034 |

A risk can sit in more than one register (for example, R-001 is in Enterprise and PDPP). When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-036, R-046, and R-050 (Low, recorded by their owners), 2026-09-17.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example the add-on acquisition, R-048), a new CUI contract, or a significant incident.

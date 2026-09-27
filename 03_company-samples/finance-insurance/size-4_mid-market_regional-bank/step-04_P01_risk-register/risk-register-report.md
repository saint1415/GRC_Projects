# Risk Register Report: Cris Santos Company | Finance and Insurance | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (privately held bank holding company) and Cris Santos Bank, N.A. (regional commercial bank) |
| Size tier | Mid-Market (600 employees; $2.5 billion in total assets) |
| Vertical | Finance and Insurance |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | Risk assessment under the Interagency Guidelines, 12 CFR 30 App. B III.B (N52-R02); input to the Identity Theft Red Flags program review (12 CFR 41.90(c)) |
| Prepared | 2026-07-24 by the IT Risk and Compliance Manager and the ISO; R-039 updated 2026-08-21 and R-049 added 2026-08-14 from P07 testing; R-011 updated 2026-08-28 after the vendor SOC reviews; AI risks R-017 to R-022 updated 2026-09-04 (P10) |
| Approved | 2026-09-18: Chief Operating Officer (Moderate and below); President and CEO with the CRO's concurrence (High); reviewed by the Board Risk Committee on 2026-09-15 |

## 1. Scope and risk framing
**Scope.** Every business unit in the BIA (P05); the Core and Online Banking Platform (COBP, P02) and the landing zone (P04); the core processor and other bank service providers; the correspondent services business; and the AI portfolio (P10). Fraud risks that run through these systems, such as business email compromise and account takeover, are in scope because the Guidelines require access controls that stop employees from giving customer information to people who seek it "through fraudulent means" (III.C.1.a). Vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) or the ISO | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer (or the executive who owns the business line) | Treatment plan or documented reason; reviewed every 6 months |
| High | President and CEO, with the CRO's concurrence | Temporary only (up to 12 months) with a dated treatment plan; reported to the Board Risk Committee at its next meeting |
| Very High | Board of Directors only | Temporary exception of up to 90 days while treatment is under way |

### Risk appetite statements (cyber and technology)
The board's enterprise risk appetite statement (2025) says the bank has a "low appetite" for operational and cyber risk but sets no measures (gap 1; R-012). The statements below add measurable tolerances. The Board Risk Committee reviewed them on 2026-09-15 and recommended them to the board for adoption on 2026-10-20.

| Area | Appetite | Statement and tolerance measure |
|---|---|---|
| Payment fraud through bank channels | **Low** | The bank will not accept fraud risk through its own processes (callback, contact changes, beneficiary changes) above Moderate. Tolerances: 100% callback evidence on sampled non-face-to-face wires; 100% out-of-band verification on sampled contact-information changes; fraud losses from bank-channel failures under $250,000 a year (today R-001 and R-002 are High) |
| Customer information confidentiality | **Low** | No risk of unauthorized access to sensitive customer information of 1,000 or more customers above Moderate. Tolerance: every system holding NPI has MFA for all users and is in the SIEM by 2027-06-30 |
| Availability of payment services | **Low** | Recovery must meet the BIA RTO for every High process (P05). Tolerance: every High process has a passed recovery test in the last 12 months (today BP-01 and BP-02 do not; R-004) |
| Regulatory compliance | **Very low** | No 12 CFR Part 53 notice may be late. No Interagency Guidelines "shall" provision may stay Not met beyond 2027-06-30. Tolerance: zero late regulator notices; High gaps in P03 closed on schedule |
| Third parties | **Moderate**, with conditions | Critical services may be outsourced, but every Tier 1 vendor has a reviewed SOC report with mapped CUECs, a notice time frame in its contract, and a 53.4 contact where it applies. Tolerance: 100% of Tier 1 vendors by 2027-03-31 |
| AI and models | **Moderate** | The bank will use AI in credit, fraud, and service, but only through the model risk and AI governance process (P10). Tolerance: no High-tier AI use without validation on bank data and fair lending testing |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 cyber insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance or the bond |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Finance and Insurance overlay, the BIA, interviews with every process owner and 8 Branch Managers, FS-ISAC and FBI advisories on business email compromise and account takeover, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, customer harm, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values and fraud case history, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 0 |
| High | 8 |
| Moderate | 36 |
| Low | 6 |
| Very Low | 0 |
| **Total** | **50** |

Treatments: 47 Mitigate, 3 Accept (R-032, R-034, R-035). Status: 25 Open, 22 In progress, 3 Accepted.

The cyber insurance policy ($15 million limit, $500,000 retention) and the financial institution bond transfer part of the financial exposure for R-001 to R-005. Neither is recorded as the treatment for any risk, because neither lowers the likelihood of harm to customers or operations.

### Top risks (High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | BEC wire after an unverified contact-information change redirects the callback | High | Out-of-band verification of contact changes; customer alerts; hold on wires after a change | Retail Banking Director | 2026-12-31 |
| R-002 | Business online banking takeover through a real-time phishing site | High | Phishing-resistant MFA; out-of-band beneficiary confirmation; beneficiary-change alerts | Treasury Management Director | 2027-03-31 |
| R-003 | Multi-day core processor outage from ransomware at the processor | High | Contract recovery and notice terms; 72-hour offline procedures; core outage runbook | Chief Operating Officer | 2027-03-31 |
| R-004 | Payments hub failover slower than the 4-hour RTO | High | Scripted failover; second-region Federal Reserve connection; reconciliation runbook | Chief Information Officer | 2027-03-31 |
| R-005 | Ransomware on bank-managed servers spreading toward the payments hub | High | Replace legacy servers; patch SLA; PAM extension; full restore tests | Chief Information Officer | 2027-06-30 |
| R-007 | Core or payments hub administrator account misused | High | PAM with hardware keys for these administrators; admin actions to the SIEM | Information Security Officer | 2027-03-31 |
| R-027 | Administrator and operator collude to change limits and push a wire | High | Dual approval for configuration changes; change alerts | Director of Payments Operations | 2026-12-31 |
| R-049 | Vendor-created generic administrator accounts in the correspondent portal (found in P07) | High | Remove accounts; vendor attestation; portal in quarterly reviews; log review | Correspondent Services Director | 2026-10-31 |

**Themes.**
- **Payment integrity is only as strong as the data behind it (R-001, R-002, R-013, R-025, R-027, R-028, R-047).** The bank has maker-checker and a required callback field, which are stronger than many peers. The weak points are upstream: who can change the phone number the callback uses, and whether a one-time code can be relayed.
- **Privileged access to money-moving applications (R-007, R-027, R-048, R-049).** PAM protects the directory and cloud but not the applications that actually move money.
- **Recovery of what the bank runs itself (R-004, R-005, R-014, R-023, R-024).** The core processor has tested recovery; the bank's own payments hub does not.
- **Third parties at scale (R-003, R-010, R-011, R-026, R-043, R-044).** The program works for the core processor but not yet for the other 33 critical vendors, and the bank is itself a service provider to 18 respondents.
- **AI adoption ahead of governance (R-017 to R-022).** P10 addresses them.

## 4. Treatment summary
**Funded in the 2027 technology and risk plan (approved by the President and CEO on 2026-09-18, $1.48 million one-time and $540,000 a year):**
- Phishing-resistant customer authentication and out-of-band beneficiary confirmation (provider fees, $160,000 one-time, $120,000 a year)
- Contact-change verification workflow and customer alerts ($90,000)
- PAM extension to core security administrators, payments hub administrators, and vendor access ($210,000 one-time, $60,000 a year)
- SIEM onboarding of the payments hub, correspondent portal, and core security reports ($150,000 a year through the MSSP)
- Payments hub failover redesign and testing ($240,000)
- Replacement of the 14 legacy item processing servers with the provider's hosted service ($380,000 one-time, $90,000 a year)
- Third-party risk tooling and one analyst ($120,000 a year)
- AI credit model outcomes validation and fair lending testing on bank data ($85,000)
- SOC 2 readiness and Type 2 examination of correspondent services ($260,000 across 2027)
- Legal work on respondent agreements and vendor side letters ($55,000)

**Accepted (3):**
- R-032: Moderate, accepted by the COO (within appetite; backups isolated and write-once)
- R-034: Low, accepted by the ISO (laptops encrypted)
- R-035: Low, accepted by the ISO (provider edge protection)

**Contract actions:** incident notice and recovery terms at the 2027 core processor renewal (R-003); 53.4 contacts to the 4 remaining bank service providers by 2026-10-31 and side letters for the 9 critical contracts without notice terms (R-010); updated respondent agreement (R-026).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the bank's enterprise risk register as one line, "Cybersecurity, fraud technology, and technology resilience", owned by the CRO and reported to the Board Risk Committee each quarter with the counts above, the top risks, and the tolerance measures in section 1.

System-level registers are filtered views of this file, kept by each system or business owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Core and Online Banking Platform (COBP; SSP in P02) | Chief Operating Officer, maintained by the ISO | 28 risks whose affected assets include SYS-01, SYS-02, SYS-03, SYS-05, SYS-06, SYS-07, or SYS-12 (filter the `affected_asset_or_process` column) |
| Correspondent services (P09 scope) | Correspondent Services Director | R-004, R-009, R-024, R-025, R-026, R-049 |
| AI and model portfolio (P10) | Model Risk Manager | R-017, R-018, R-019, R-020, R-021, R-022 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-032, 2026-09-18.
- President and CEO, with the CRO's concurrence: approved the High-risk treatment plans and the 2027 funding, 2026-09-18. No High risk was accepted without treatment.
- Board Risk Committee: reviewed the register and the proposed tolerances on 2026-09-15; the tolerances go to the full board on 2026-10-20.
- Next full risk assessment: December 2026 as part of the annual cycle, then after any major change (a new core processor, a new payments channel, or an acquisition) or a significant incident.

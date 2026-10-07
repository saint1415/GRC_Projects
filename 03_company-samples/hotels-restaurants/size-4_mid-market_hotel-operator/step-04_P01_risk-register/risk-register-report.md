# Risk Register Report: Cris Santos Company | Accommodation and Food Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Florida hotel owner and operator: 2 independent resorts and 4 franchised select-service hotels) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Accommodation and Food Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | PCI DSS v4.0.1 Requirement 12.3 (risks to the cardholder data environment identified, evaluated, and managed); the reasonableness analysis expected under FTC Act Section 5 and Fla. Stat. 501.171(2) |
| Prepared | 2026-07-31 by the GRC Analyst and the vCISO; R-050 added 2026-08-14 from P07 testing |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (Resorts 1 and 2, Hotels 3 to 6, the CRO, and corporate shared services), the Property Management and Point-of-Sale Platform (PMPS; SSP in P02), the franchisor's platform where it touches the company's hotels (SYS-02), the 31 vendors that handle card or guest data, and the AI tools in P10. Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

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
| Guest safety | **Very low** | No technology risk that could stop guests from securing or reaching their rooms, or stop the hotels from accounting for guests in an emergency, is accepted above Low. Measure: safety-linked risks above Low (5 today: R-002, R-005, R-015, R-018, R-050; target 0 by 2027-12-31) |
| Payment card data | **Low** | The company will not accept a risk of card compromise above Moderate. Card data is held only where a business process needs it. Measure: R-001, R-003, R-004, R-005, and R-006 at Moderate or lower by 2027-06-30; no card data outside the vault after 2026-12-31 |
| Guest personal data | **Low** | Keep only what the guest register and stays need. Measure: retention schedule in force and ID scans purged after check-out plus 30 days by 2026-12-31 (R-042) |
| Availability of guest operations | **Low** | Recovery must meet the BIA RTOs for all High-criticality processes (P05). Measure: every High process has a passed recovery test in the last 12 months |
| Contractual compliance (PCI DSS, franchise, management agreement) | **Low** | The CFO signs the SAQ D only with evidence for every answer. Measure: no "In Place" answer without evidence; SOC 2 Type 2 observation period starts on time (R-039, R-047) |
| Third parties and the franchisor | **Moderate**, with conditions | Vendors are used widely, but no vendor handles card data without a current AOC, and every Tier 1 vendor is reviewed each year (P09). The franchisor relationship must have a written PCI DSS responsibility matrix by 2027-03-31 |
| Pricing and AI | **Moderate** | AI is welcome in pricing, guest service, and operations, but only through the P10 process. No automated price change during a declared state of emergency without human approval |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $250,000 insurance retention are tolerable. Scenarios above $1.5 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews with every process owner and all 6 General Managers, the gap analysis (P03), the control assessment (P07), and the practices alleged in *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015), which describe how franchised hotel networks and PMS environments were breached.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, guest safety, reputation).
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

Treatments: 47 Mitigate, 4 Accept (R-029, R-044, R-045, R-048), 1 Avoid (R-023). Status: 26 In progress, 22 Open, 4 Accepted. The sum of semi-quantitative scores is 277, the baseline for tracking reduction each quarter.

Cyber insurance ($10 million limit, $250,000 retention) transfers part of the financial exposure for R-001, R-002, and R-004. It is not recorded as the treatment for any risk, because it does not lower the likelihood of a card compromise or of harm to guests.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | POS and reservation system compromise through the Resort 2 POS vendor's remote tool, spreading to CRO PCs | Very High | Vendor access through the broker with MFA; block POS-to-corporate traffic; allowlisting; P2PE cloud POS at Resort 2; keypad entry for CRO payments | Security Manager | 2027-06-30 |
| R-002 | Ransomware stops PMS interfaces and lock servers and steals guest data | High | Domain administrators in the broker; lock and POS logs to the SIEM; restore tests; cloud backups of lock servers | IT Director | 2027-03-31 |
| R-003 | Card data in CRO call recordings taken | High | Pause-and-resume recording; purge; 90-day retention | Director of Central Reservations | 2026-12-31 |
| R-004 | Card authorization forms stolen from mailboxes | High | Purge; data loss prevention rules; payment links | Chief Financial Officer | 2026-11-30 |
| R-005 | Resort 2 POS or lock vendor remote tool credentials stolen | High | Named vendor accounts through the broker with MFA | Security Manager | 2026-11-30 |
| R-006 | Brand-managed firewall or brand vendor access compromised at Hotels 3 to 6 | High | PCI DSS responsibility matrix; firewall rule attestation; company VLANs | General Counsel | 2027-03-31 |
| R-009 | Domain or server administrator account outside the broker taken over | High | Broker for all administrators; phishing-resistant MFA | Security Manager | 2027-03-31 |
| R-015 | Resort lock server cannot be restored within 1 hour | High | Cloud backups; documented rebuild; quarterly restore tests; replace Resort 2 server | Resort Chief Engineers | 2027-03-31 |
| R-018 | Hurricane damages on-site IT; no IT plan at Hotels 3 to 6 | High | IT sections in all hurricane plans; relocate Resort 1 equipment | Director of Loss Prevention and Safety | 2027-05-31 |
| R-027 | Known-exploited vulnerability in an internet-facing edge device | High | 72-hour emergency patch path for edge devices | IT Director | 2026-12-31 |
| R-030 | Unsupported Resort 2 POS server or lock server exploited | High | Restrict flows; replace both servers | IT Director | 2027-06-30 |
| R-041 | Card compromise cannot be scoped because logs are missing | High | Onboard missing sources; 12-month retention | Security Manager | 2027-01-31 |
| R-050 | Default administrator password on the Resort 2 lock server (found in P07) | High | Changed 2026-08-12; sweep for other defaults; hardening standard | Resort Chief Engineers | 2026-10-31 |

**Themes.**
- **Card data is held where the business does not need it (R-001, R-003, R-004, R-011, R-012).** Keyed CRO payments, call recordings, emailed forms, broad display rights, and a non-P2PE POS at Resort 2 widen the cardholder data environment. Fixing them reduces risk and PCI scope at the same time (P03 section 1.2).
- **Third-party and franchisor access (R-005, R-006, R-020, R-021).** Vendors and the franchisor hold standing access the company cannot see. *FTC v. Wyndham* shows that regulators look at how a hotel company manages exactly these connections.
- **Guest safety rests on lock servers that are not recoverable on demand (R-015, R-050, R-002).**
- **Visibility (R-041, R-007, R-013).** The SIEM sees the corporate office and resorts but not the systems most likely to be attacked.
- **AI adopted without governance (R-022, R-023, R-033 to R-038).** P10 addresses them.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15, $1.05 million one-time and $390,000 a year):**
- Resort 2 P2PE cloud POS replacement ($280,000) and loaner P2PE devices for outlets ($15,000)
- Keypad entry devices and pause-and-resume recording for the CRO ($90,000 one-time, $25,000 a year)
- Privileged access broker extension to domain, server, and vendor access, and phishing-resistant MFA for administrators ($140,000 one-time, $60,000 a year)
- SIEM onboarding of lock servers, the Resort 2 POS, and Hotels 3 to 6, plus EDR for the remaining 50 PCs ($110,000 a year)
- Segmentation behind the brand firewalls at Hotels 3 to 6 ($120,000)
- Resort 2 lock server replacement and Resort 1 equipment relocation ($95,000)
- Payment page script management and tamper detection ($35,000 a year)
- QSA scoping review and 2026 SAQ D support, internal penetration and segmentation tests ($110,000 one-time, $60,000 a year)
- SOC 2 readiness and Type 2 examination ($160,000 across 2027)
- Vendor risk tooling and data discovery for card numbers ($40,000 one-time, $100,000 a year including part of the GRC Analyst's time)

Smaller items (closet key logs, hurricane plan updates, contract amendments) come from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-029 (Moderate, COO; within appetite because backups are isolated and write-once), R-044 (Low, vendor-hosted booking continues), R-045 (Low, encrypted devices), R-048 (Low, separation confirmed).

**Avoided (1):** R-023, by opting out of the revenue-management vendor's pooled benchmarking.

**Contract actions:** PCI DSS responsibility matrix with the franchisor (R-006); current AOCs and notice clauses for 9 vendors (R-020, R-021); chatbot retention and masking (R-022); SYS-01 recovery terms (R-014); all by 2027-03-31.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, payment card, and technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| PMPS (SSP in P02) | IT Director | 31 risks whose affected assets include SYS-01, SYS-03, SYS-04, SYS-06, SYS-07, SYS-08, SYS-09, SYS-10, or SYS-12 (filter the `affected_asset_or_process` column) |
| Cardholder data environment (PCI DSS 12.3) | Chief Financial Officer | 35 risks with a PCI DSS driver (N72-R01 in the `regulatory_driver` column) |
| Franchised hotels (Hotels 3 to 6) | Hotel General Managers with the IT Director | R-006, R-010, R-012, R-013, R-016, R-018, R-046 |
| AI portfolio (P10) | General Counsel (chair of the AI review group) | R-022, R-023, R-033, R-034, R-035, R-036, R-037, R-038 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-029, R-044, R-045, and R-048, 2026-09-15.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example a new hotel, the start of the REIT management agreement, or a payment design change) or a significant incident.

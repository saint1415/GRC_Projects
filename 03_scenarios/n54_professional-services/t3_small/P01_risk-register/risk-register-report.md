# Risk Register Report: Cris Santos Company | Professional, Scientific, and Technical Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| Size tier | Small (60 employees) |
| Vertical | Professional, Scientific, and Technical Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | FTC Safeguards Rule written risk assessment, 16 CFR 314.4(b)(1) (criteria below) |
| Prepared | 2026-07-24 by the IT Manager (Qualified Individual) with the Risk and Quality Partner |
| Approved | 2026-08-31 by the Firm Administrator (Moderate and below) and the Managing Partner (High) |

## 1. Scope and risk framing
**Scope.** The Tax Preparation and Client Portal Platform (TPCP), the practice management and payroll services, and the business processes in the BIA (P05). That covers every system that stores, processes, or transmits customer information or tax return information, plus the service providers that handle it for the firm (`../scenario-facts.md` section 3).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the Firm Administrator may accept, with a treatment plan or a documented reason.
- High and Very High: only the Managing Partner may accept, and only temporarily with a dated treatment plan. Risks that could expose tax return information of many clients at once are not accepted at High.

This is the firm's first written risk assessment. The 2023 WISP listed threats but had no rating criteria.

## 2. Method and 16 CFR 314.4(b)(1) criteria
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the IRS Security Summit warnings in Pub. 4557 (phishing, account takeover, fraudulent returns), the BIA, interviews with the Tax Partner, Client Services Supervisor, and MSP, and the gap analysis (P03).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (cost, operations, regulatory, client harm, reputation).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

How this method meets the written risk assessment content in 314.4(b)(1):

| 314.4(b)(1) requires | Where it is met |
|---|---|
| (i) Criteria for evaluating and categorizing identified risks or threats | Steps 2 to 4 above: the SP 800-30 likelihood and impact scales and Tables G-5 and I-2 |
| (ii) Criteria for assessing the confidentiality, integrity, and availability of systems and customer information, including the adequacy of existing controls | The FIPS 199 categorization in the SSP (P02 section 6), the BIA impact categories (P05), and the `existing_controls` column, rated against the P03 gap results |
| (iii) How identified risks will be mitigated or accepted, and how the program will address them | The risk acceptance levels in section 1, the `treatment` and `treatment_plan` columns, and the POA&M (P07) |

## 3. Results

| Risk level | Count |
|---|---|
| High | 5 |
| Moderate | 20 |
| Low | 8 |
| **Total** | **33** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Business email compromise harvests client documents from a staff mailbox | High | Number-matching or phishing-resistant MFA; block legacy authentication and auto-forwarding; inbox-rule alerts; phishing exercises | IT Manager | 2026-11-30 |
| R-011 | Unpatched remote access VPN gateway exploited | High | Monthly scans; 14-day patching of critical flaws; annual penetration test | IT Manager | 2026-11-30 |
| R-010 | Partner everyday account with global admin rights phished | High | Separate admin accounts with hardware keys; remove standing rights from partners | IT Manager | 2026-10-31 |
| R-004 | Ransomware during filing season | High | 24x7 managed detection and response; quarterly restore tests | IT Manager | 2027-01-15 |
| R-018 | MSP remote management tool compromise reaches every endpoint | High | Security terms in the MSP contract; source restrictions; annual MSP assessment | Firm Administrator | 2026-12-31 |
| R-002 | Refund direct deposit changed through a hijacked client email thread | Moderate | Call-back verification procedure | Tax Partner | 2026-12-15 |
| R-012 | Client data pasted into public AI chatbots | Moderate | Approved-tools list; blocking; IRC 7216 training | Risk and Quality Partner | 2026-10-31 |

The five High risks share one theme: **an attacker who gets one privileged or trusted foothold (a mailbox, an admin account, the VPN, or the MSP tool) can reach every client's tax data, and nobody is watching after hours.** Treating them also lowers eight related Moderate risks (R-003, R-005, R-006, R-009, R-024, R-026, R-027, R-033).

R-033 was added on 2026-08-07 after control assessment testing (P07) found that the shared intake mailbox password was known to 6 staff and still worked over legacy authentication without MFA.

The deadline calendar drives the due dates. Every High-risk treatment except R-004 closes before 2027-01-15, when the filing season and its phishing wave begin; the 24x7 monitoring for R-004 goes live by that date.

## 4. Treatment summary
- **Funded (2026 Q4 budget, $61,000):**
  - 24x7 managed detection and response through the MSP ($26,000 a year)
  - Phishing-resistant keys for administrators and number matching for all users ($3,000)
  - Vulnerability scanning and an annual penetration test ($18,000 a year)
  - Log workspace with one-year retention and alerting ($6,000 a year)
  - Full-disk encryption on 12 desktops and a phishing exercise service ($8,000)
- **Accepted:**
  - R-022: Low, staff can work from home or the Main office
  - R-030: Low, vendor-managed
  - R-031: Low, laptops are encrypted
- **Contract actions:** security terms in the MSP contract (R-018), and AI sub-processor, U.S.-processing, and no-training terms with the tax software vendor (R-013), due 2026-10-31 to 2026-12-31.
- **Procedural:** call-back verification (R-002, R-025), data theft procedure (R-024), retention schedule (R-015).

## 5. Approval
- Firm Administrator: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Managing Partner: approved the High-risk treatment plans and the budget, 2026-08-31.
- To be reported to the Partner Group in the Qualified Individual's first written report, scheduled for 2026-10-20 (314.4(i)).
- Next full review: July 2027, or sooner after a material change or security event (314.4(b)(2) and (g)).

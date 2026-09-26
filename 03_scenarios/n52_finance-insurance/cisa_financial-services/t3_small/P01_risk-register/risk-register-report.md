# Risk Register Report: Cris Santos Company | Financial Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (payment processor serving merchants) |
| Size tier | Small (60 employees) |
| Vertical | Financial Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | FTC Safeguards Rule written risk assessment, 16 CFR 314.4(b); PCI DSS 12.3.1 inputs (the targeted risk analyses themselves are a P03 gap) |
| Prepared | 2026-07-24 by the IT Manager (Information Security Lead and Qualified Individual); R-031 added 2026-08-07 |
| Approved | 2026-08-31 by the COO (Moderate and below) and the majority owner and CEO (High) |

## 1. Scope and risk framing
**Scope.** The Payment Processing Platform (PPP) and every business process in the BIA (P05). That covers the cardholder data environment (CDE) in the cloud tenant, the systems that can change or watch it (identity provider, pipeline, SIEM), the systems where card data turned up unexpectedly (support ticketing, data warehouse), merchant owner data in onboarding, and the service providers listed in `../scenario-facts.md` section 3.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the COO may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner and CEO may accept, and only temporarily with a dated treatment plan. A risk that would leave a PCI DSS requirement "not in place" at the 2026 ROC cannot be accepted, because the AOC depends on it.

**Why the Safeguards Rule matters here.** 16 CFR 314.4(b)(1) requires the risk assessment to be written and to include criteria for evaluating and categorizing risks, criteria for assessing confidentiality, integrity, and availability, and requirements for how risks will be mitigated or accepted. Sections 1 and 2 of this report are those criteria.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the BIA (P05), the P03 gap analysis, interviews with the CTO, Platform Engineering Lead, Settlement Operations Manager, Merchant Support Manager, and Risk and Fraud Manager, and the scenario incident for P08 (compromise of the payment processing environment).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) and likelihood of adverse impact were rated separately, then combined with **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3** with the BIA impact categories (cost, merchant operations, regulatory and card brand, reputation). A card data compromise across many merchants is rated Very High: card brand non-compliance assessments, forensic costs, and possible loss of the sponsor bank relationship.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 5 |
| Moderate | 20 |
| Low | 6 |
| **Total** | **31** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | E-commerce skimming script injected into the hosted payment page | High | Script inventory and integrity controls; change- and tamper-detection | CTO | 2026-10-31 |
| R-002 | Stolen repository or pipeline credential used to push malicious code into the CDE | High | Revoke long-lived tokens; two approvals for CDE deployments; signed builds | Platform Engineering Lead | 2026-09-30 |
| R-003 | Card data exfiltration goes undetected after hours | High | 24x7 managed detection and response; egress and DNS intrusion detection | IT Manager | 2026-12-31 |
| R-004 | Merchant portal account takeover leads to fraudulent refunds and virtual terminal abuse | High | Required MFA for merchant users with refund or virtual terminal rights | CTO | 2026-10-31 |
| R-006 | Platform outage longer than 4 hours with no tested failover | High | Warm standby in the second region; recovery runbook; failover tests | Platform Engineering Lead | 2027-03-31 |
| R-031 | Unencrypted PAN in a data warehouse table | Moderate | Purged; fix the extract; monthly PAN discovery | Platform Engineering Lead | 2026-09-30 |

The High risks share two themes:
- **A card data compromise would be easy to start and slow to find.** R-001 and R-002 describe how malicious code could reach the payment page or gateway, and R-003 explains why nobody would see it at night. This chain is the P08 scenario.
- **The processor's promises to its bank and merchants depend on availability it has not tested.** R-006 would trigger the sponsor bank notice under 12 CFR 53.4 (a disruption of covered services for four or more hours).

Fixing R-001 to R-003 also reduces five Moderate risks (R-005, R-009, R-011, R-013, R-016).

R-031 was added on 2026-08-07 after control assessment testing (P07) found full card numbers in a data warehouse table. The table was purged on 2026-08-07. Whether the exposure is a reportable event is analyzed in P08 section 6: the warehouse is inside the company's cloud tenant, access was limited to 11 authorized staff, and access logs show no access from outside that group.

## 4. Treatment summary
- **Funded (2026 Q4 budget, $214,000):**
  - Managed detection and response service, 24x7 ($96,000 a year)
  - Payment page script monitoring service ($18,000 a year)
  - Egress and DNS intrusion detection in the cloud tenant ($22,000 a year)
  - Second-region warm standby for the authorization path ($48,000 a year in cloud costs)
  - Segmentation penetration test, October 2026 and April 2027 ($30,000)
- **Hiring:** a security engineer (approved 2026-08-31) to take security operations off the IT Manager (R-028).
- **Accepted:**
  - R-019: Low; provider DDoS protection in place
  - R-029: Low; laptops are encrypted and hold no card data
  - R-030: Low; phishing-resistant keys for all administrators
- **Contract actions:** responsibility matrices and current AOCs for the cloud provider, payment HSM service, content delivery service, and fraud model vendor (R-016, R-022), due 2026-10-31. Record the sponsor bank's designated points of contact for 12 CFR 53.4 notices (R-015), due 2026-09-30.

## 5. Approval
- COO: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Majority owner and CEO: approved the High-risk treatment plans and the budget, 2026-08-31. R-006 remains open past the 2026 ROC; it is an availability risk and does not leave a PCI DSS requirement "not in place".
- Next full review: July 2027, or sooner after a significant change or incident. The six-month PCI DSS scope confirmation (12.5.2.1) triggers a review of R-001 to R-005 and R-031 each time.

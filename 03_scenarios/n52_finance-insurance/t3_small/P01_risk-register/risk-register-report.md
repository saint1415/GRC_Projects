# Risk Register Report: Cris Santos Company | Finance and Insurance | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (community commercial bank; subsidiary of Cris Santos Company, a bank holding company) |
| Size tier | Small (120 employees; $510 million in total assets) |
| Vertical | Finance and Insurance |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | Risk assessment under the Interagency Guidelines, 12 CFR 30 App. B III.B (N52-R02) |
| Prepared | 2026-07-24 by the IT Manager (Information Security Officer), updated 2026-08-07 (R-005) and 2026-08-25 (R-011, R-012) |
| Approved | 2026-08-31 by the President and CEO (High and below); reviewed by the Audit and Risk Committee 2026-08-27 |

## 1. Scope and risk framing
**Scope.** Every system that stores, processes, or transmits customer information, and the business processes in the BIA (P05). That covers the core banking system hosted by the core processor, online and mobile banking, the wire and ACH platform, the loan origination system and the AI credit model, the identity provider, the cloud tenant, six branch networks with teller workstations, and the ATMs (`../scenario-facts.md` section 3). Fraud risks that run through these systems, such as business email compromise and account takeover, are in scope because the Guidelines require access controls that stop employees from giving customer information or funds to people who obtain them "through fraudulent means" (III.C.1.a).

**Risk tolerance and who can accept risk (proposed as the board's risk appetite):**
- Low and Very Low: the Information Security Officer may accept.
- Moderate: the COO may accept, with a treatment plan or a documented reason.
- High: only the President and CEO may accept, temporarily and with a dated treatment plan, and each acceptance is reported to the Audit and Risk Committee.
- Very High: only the board may accept.

**Why this matters now.** The bank has performed an annual risk assessment since 2021, but the board has never approved a risk appetite, so no one could say whether residual risk was acceptable (gap 1 in the scenario facts; R-008). The acceptance levels above, with the tolerance measures in section 4, go to the board for adoption on 2026-10-15.

## 2. Method
1. **Identify.** Threat sources and events were taken from SP 800-30 Appendices D and E, the vertical's critical systems, the BIA, interviews with the COO, Deposit Operations Manager, Treasury Management Officer, Chief Credit Officer, BSA/AML Officer, and all six Branch Managers, and the gap analysis (P03).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (financial loss, operations, regulatory, customer harm, reputation).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 5 |
| Moderate | 21 |
| Low | 6 |
| **Total** | **32** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Fraudulent wire from a compromised customer email (BEC) because branch callbacks are skipped | High | Mandatory callback enforced in the wire platform; branch training; monthly sampling | Deposit Operations Manager | 2026-10-31 |
| R-002 | Business online banking account takeover where the customer has not enabled MFA | High | Required customer MFA; out-of-band confirmation of new beneficiaries; change alerts | Treasury Management Officer | 2026-12-31 |
| R-003 | Core processor outage longer than the 4-hour RTO | High | Recovery and incident notice terms at the 2027 renewal; 53.4 contact; offline branch tests | Chief Operating Officer | 2027-03-31 |
| R-004 | Ransomware on branch networks and file shares | High | Network segmentation; immutable, separate-account backups; restore tests | IT Manager | 2027-01-31 |
| R-019 | Collusive insider wire fraud in the wire room | High | Separate beneficiary template maintenance from approval; monthly approver review | Deposit Operations Manager | 2026-12-31 |
| R-005 | Stale core accounts used by a former employee | Moderate | Disable now; quarterly core access reviews | IT Manager | 2026-10-31 |
| R-006 | Missed 36-hour OCC notice (and Federal Reserve notice for the holding company) | Moderate | Add determination step and clock to the plan (P08) | Information Security Officer | 2026-10-31 |
| R-011 | AI credit model gives adverse action reasons that are not specific | Moderate | Reason-code review; validation before expansion (P10) | Chief Credit Officer | 2026-11-30 |

Three of the five High risks share one theme: **payment fraud through customer channels.** A customer email account is taken over (R-001), a customer online banking password is stolen (R-002), or an insider abuses the wire room (R-019). In each case a control exists on paper (the callback standard, optional MFA, maker-checker) but is not enforced consistently. The other two High risks are about dependence on the core processor (R-003) and recovery from ransomware (R-004). Treating R-001 and R-002 also lowers four related Moderate risks: R-009, R-025, R-026, and R-029.

R-005 was updated on 2026-08-07 after control assessment testing (P07) found four enabled core accounts belonging to former employees. R-011 and R-012 were updated after the AI credit model assessment on 2026-08-25 (P10).

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $96,000):**
  - Customer MFA enforcement and out-of-band beneficiary confirmation in online banking (provider fees, $18,000 a year)
  - Branch, teller, and wire-room network segmentation ($26,000)
  - Immutable, separate-account backups for bank-managed cloud workloads ($7,000 a year)
  - Independent validation and fair lending testing of the AI credit model ($30,000)
  - Monthly authenticated vulnerability scanning through the MSSP ($9,000 a year)
  - Role-based BEC and wire-fraud training ($6,000)
- **Accepted:**
  - R-015: Low, laptops are encrypted
  - R-018: Low, provider DDoS protection reviewed in P09
  - R-031: Moderate, hardened and isolated payments workstations
- **Contract actions:** incident notice and recovery terms for the core processor at the 2027 renewal (R-003, R-007); designated 12 CFR 53.4 contacts sent to three bank service providers by 2026-09-30 (R-024).
- **Proposed tolerance measures for the board's risk appetite statement:** no High risk older than 90 days without a CEO acceptance; 100% callback evidence on sampled non-face-to-face wires; 100% of business online banking users on MFA by 2026-12-31; quarterly core access reviews completed within 30 days of quarter end.

## 5. Approval
- President and CEO: approved the treatments, the accepted risks, and the budget request, 2026-08-31.
- Audit and Risk Committee: reviewed the register and the five High risks, 2026-08-27. The risk appetite statement goes to the full board on 2026-10-15.
- Next full review: December 2026, as part of the annual risk assessment, then after any major change or incident.

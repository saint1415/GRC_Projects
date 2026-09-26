# Risk Register Report: Cris Santos Company | Other Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electronics and device repair service, four stores and a Depot) |
| Size tier | Small (60 employees) |
| Vertical | Other Services (except Public Administration) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | Fla. Stat. 501.171(2) "reasonable measures"; FTC Act Section 5 reasonable security; NIST CSF 2.0 ID.RA and GV.RM outcomes |
| Prepared | 2026-07-31 by the IT Manager (Information Security Lead) with the Operations Manager |
| Approved | 2026-09-04 by the General Manager (Moderate and below) and the majority owner (High) |

## 1. Scope and risk framing
**Scope.** The Service Ticketing and Point-of-Sale Platform (STPP), the business processes in the BIA (P05), and the customer devices and data that sit in the company's custody while they are being repaired, recovered, or recycled (`../scenario-facts.md` sections 1 and 3).

**What makes this business different.** Most companies protect data they collect. A repair shop also holds **customers' entire phones and laptops**, often unlocked, with photos, messages, health and location data, and saved passwords. The biggest risks here are therefore not only outside attackers but also **people with legitimate physical access**: technicians, counter staff, couriers, and the recycler.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the General Manager may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. **Risks to customer device data rated High may not be accepted without treatment**, because a single incident can end the manufacturer authorization.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews with the Operations Manager, the Store Managers, the Data Recovery Lead, and the Controller, the April 2026 customer complaint file, and the gap analysis (P03).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 19 |
| Low | 8 |
| **Total** | **31** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Technician views or copies personal data from a customer device | High | Customer data access standard; named bench accounts; USB block; session logging; confidentiality agreements | Operations Manager | 2026-12-31 |
| R-002 | Passcodes and account passwords in ticket notes exposed | High | Stop collecting account passwords; restricted passcode field purged at release; purge history | IT Manager | 2026-11-15 |
| R-006 | Recovered customer data kept indefinitely is stolen or exposed | High | 30-day retention; purge the 4.2 TB backlog; wipe bench caches; encrypt lab storage | Data Recovery Lead | 2026-11-30 |
| R-014 | Lab storage and backups lost together | High | Separate immutable backup account; quarterly restore tests | IT Manager | 2026-12-31 |
| R-015 | Manufacturer A suspends authorized status after its October audit | Moderate | Named portal accounts; 24-hour notice procedure | Operations Manager | 2026-10-15 |
| R-003 | Shared counter login phished and used to export customer records | Moderate | Named accounts with MFA; export alerts | IT Manager | 2026-10-31 |
| R-004 | Card numbers written down during phone payments; SAQ P2PE eligibility lost | Moderate | Key directly into the terminal; purge notes; block card-number patterns | Controller | 2026-10-31 |

Three of the four High risks share one theme: **the company keeps too much customer data, and too many people can reach it.** Passcodes stay on tickets forever (R-002), recovered data stays on the lab storage forever (R-006), and any technician can open any device without a record (R-001). Collecting less, deleting on a schedule, and logging access reduces these three and five related Moderate risks (R-003, R-009, R-011, R-019, R-024).

The fourth High risk (R-014) is about recovery: the only copy of in-progress data recovery images sits with backups an attacker could delete in the same step.

R-031 was added on 2026-08-12 after control assessment testing (P07) found the vendor default administrator password on the lab storage array console. The password was changed and the console restricted by 2026-08-31, so the risk is closed.

## 4. Treatment summary
- **Funded (2026 Q4 budget, $52,000):**
  - EDR for bench PCs and a bench VLAN at each store (R-008, R-019)
  - Separate immutable backup account and a weekly SYS-01 export (R-014, R-017)
  - Encryption at rest for the lab storage and USB blocking on bench PCs (R-001, R-006)
  - Device management for counter tablets and badge-plus-PIN sign-in (R-003, R-027)
  - Cellular hotspot kits for the four stores (R-020)
  - Security awareness and phishing training (R-013, R-025)
- **No-cost process changes, due first:** stop collecting account passwords (R-002); remove the "99% accurate" claim (R-012, due 2026-09-30); named Manufacturer A portal accounts (R-015); release checklist with ID check (R-010).
- **Accepted:**
  - R-029: chatbot vendor outage, Very Low residual
  - R-030: cloud administrator takeover, Low residual with MFA and sign-in alerts
- **Contract actions:** data-use and breach-notice terms for the chatbot and diagnostics vendors, the recycler, and the courier (R-007, R-011, R-022), due by 2026-12-31.
- **Closed:** R-031 (default storage password changed, 2026-08-31).

## 5. Approval
- General Manager: approved Moderate and Low treatments and the two acceptances, 2026-09-04.
- Majority owner: approved the four High-risk treatment plans and the budget, 2026-09-04.
- Next full review: July 2027, or sooner after a major change (for example, a new store or service) or an incident.

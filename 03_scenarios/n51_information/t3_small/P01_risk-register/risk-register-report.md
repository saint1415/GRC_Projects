# Risk Register Report: Cris Santos Company | Information | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher, workforce scheduling and timekeeping platform) |
| Size tier | Small (60 employees, $28.2 million receipts) |
| Vertical | Information |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | SOC 2 risk assessment criteria (CC3.1 to CC3.4); the "reasonable security" expectation the FTC enforces under Section 5 (15 U.S.C. 45(a)) |
| Prepared | 2026-08-21 by the IT Manager (security and compliance lead) with the Platform Engineering Lead; R-015 added 2026-09-04 |
| Approved | 2026-09-22 by the CTO (Moderate and below) and the Chief Executive Officer (High) |

## 1. Scope and risk framing
**Scope.** The Workforce Scheduling Platform (WSP) defined in the SSP (P02), the staging environment that holds production data copies, the sub-processors that receive customer worker data, and the business processes in the BIA (P05). See `../scenario-facts.md` sections 3 and 4.

**What the company protects.** About 140,000 worker profiles that belong to about 310 customers. Customers rely on the platform to capture time punches and produce payroll exports, so integrity and availability matter as much as confidentiality.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the CTO may accept, with a treatment plan or a documented reason.
- High and Very High: only the Chief Executive Officer (majority owner) may accept, and only temporarily with a dated treatment plan. A High risk to customer data confidentiality is not accepted long term, because it conflicts with the DPA and the company's public statements.

This is the company's second risk assessment. The first (December 2025) supported the SOC 2 Type 1 and did not cover staging, sub-processors, or the AI assistant.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the vertical's critical systems (multi-tenant platforms, identity, CI/CD), the three SOC 2 Type 1 exceptions, the P03 gap analysis, the BIA, and interviews with the CTO, Platform Engineering Lead, Engineering Manager, Customer Support Manager, and COO.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, were rated and combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3** using the BIA impact categories. "Very High" is reserved for events that could expose most customers' worker data or stop time capture for all customers.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 21 |
| Low | 9 |
| **Total** | **34** |

No risk rated Very High. Three risks were accepted (R-023, R-025, R-029, all Low).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Leaked long-lived CI/CD cloud key used to read payroll exports and copy database snapshots | High | Short-lived federated credentials; cloud API anomaly alerts; secret scanning | Platform Engineering Lead | 2026-10-16 |
| R-002 | Shared break-glass database role misused without attribution | High | Named just-in-time access; session recording; weekly review | CTO | 2026-10-23 |
| R-003 | Customer data in staging exposed through weaker controls | High | Stop production refreshes; purge copies; masked or synthetic data | Engineering Manager | 2026-10-30 |
| R-005 | Cross-tenant data exposure through an authorization flaw | High | Isolation tests on 100% of endpoints as a merge gate; database-level row security | Engineering Manager | 2027-01-31 |
| R-009 | Customer notice misses the 72-hour or 48-hour contract deadline | Moderate | Updated plan and runbook (P08); tabletop exercise | IT Manager | 2026-11-30 |
| R-031 | Incident cannot be scoped because logs expired or were never collected | Moderate | 1-year log archive in a separate account; object access logs; weekly review | Platform Engineering Lead | 2026-11-30 |
| R-019 | AI assistant data flows exceed DPA and public statements | Moderate | Zero-retention confirmation; re-notice to customers; statement update | Director of Product | 2026-10-31 |
| R-020 | Shift-swap suggestions disadvantage a protected group | Moderate | Remove names from prompts; bias testing before general availability | Director of Product | 2026-11-30 |

**The common theme: customer data can leave the platform through privileged paths that nobody watches.** Static CI keys (R-001), a shared database role (R-002), and unmasked staging copies (R-003) each give broad access to all tenants, and weak logging (R-031) means the company could not tell customers what was taken. Fixing R-001 to R-003 also lowers R-007, R-012, R-015, R-030, and R-031. R-001 is the scenario in the incident runbook (P08).

R-002 and R-003 are also SOC 2 Type 1 exceptions 1 and 2, and R-004 is exception 3. They must be closed before the Type 2 observation period starts on 2026-11-01 (P09 readiness gates).

R-015 was added on 2026-09-04 after control assessment testing (P07) found two former contractors with local repository accounts outside single sign-on. The accounts were removed the same day.

## 4. Treatment summary
- **Funded (2026 Q4 to 2027 Q1 budget, $78,000):**
  - Privileged access tool with just-in-time approval and session recording ($18,000 per year)
  - Log archive account, object access logging, and alerting ($12,000 per year)
  - Masked and synthetic test data tooling ($6,000)
  - Separate backup account with write-once retention ($4,000 per year)
  - Secure coding training for 21 engineers ($5,000)
  - Outside counsel review of public security and AI statements ($8,000)
  - AI bias testing support ($10,000)
  - Expanded penetration test covering tenant isolation and the AI assistant ($15,000)
- **Accepted:**
  - R-023 (DDoS): Low, with provider protection and offline punch queuing; revisit if SLA credits exceed $10,000 in a quarter.
  - R-025 (lost laptop): Low, with full-disk encryption and remote wipe.
  - R-029 (SMS outage): Low, with email and push fallback.
- **Contract actions (COO):** re-notice customers about the AI model provider (R-019), confirm written zero-retention terms, and add a DOJ Data Security Program question to sub-processor reviews (R-034), due 2026-10-31 to 2026-12-31.

## 5. Approval
- CTO: approved the Moderate and Low treatments and the Low acceptances, 2026-09-22.
- Chief Executive Officer (majority owner): approved the High-risk treatment plans and the budget, 2026-09-22.
- Next full review: August 2027, or sooner after a major change (for example, general availability of the AI assistant) or an incident.

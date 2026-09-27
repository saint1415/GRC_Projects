# Risk Register Report: Cris Santos Company | Management of Companies and Enterprises | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (holding company with three operating subsidiaries) |
| Size tier | Small (60 employees across the group) |
| Vertical | Management of Companies and Enterprises |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | Finance's written risk assessment under the FTC Safeguards Rule, 16 CFR 314.4(b)(1)-(2) |
| Prepared | 2026-08-28 by the IT Manager (Qualified Individual for Finance) |
| Approved | 2026-09-25 by the CFO (Moderate and below), the CEO (High), and the Board of Managers (High-risk treatment plans and budget) |

## 1. Scope and risk framing
**Scope.** The Shared Corporate Services Platform (SCSP) and every business process in the BIA (P05), for the holding company and all three subsidiaries: Supply, Home Services, and Finance. The register also covers the subsidiary systems that connect to the shared platform (SYS-10 to SYS-12) and the service providers that support it (`../00_company-facts.md` section 3).

**Why one register for the group.** The subsidiaries share one identity tenant, one email and file tenant, one ERP, one cloud tenant, and one IT team. A risk to the shared platform is a risk to every subsidiary at once, so risks are assessed at group level. Each risk names the affected subsidiary data or process where it differs.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the CFO may accept, with a treatment plan or a documented reason.
- High: only the CEO may accept, temporarily and with a dated treatment plan, and each acceptance is reported to the Board of Managers.
- Very High: only the Board of Managers may accept.
- Any risk to Finance customer information rated Moderate or above must also be reported to Finance's Board of Managers in the Qualified Individual's annual report (16 CFR 314.4(i)(2)).

This is the group's first documented risk assessment. Finance's last written risk assessment was in 2023 and covered only Finance's own systems.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the CSF 2.0 group profile and Safeguards Rule gap analysis (P03), and interviews at all three sites with the CFO, Controller, HR Director, Treasury and Payments Analyst, the three subsidiary Presidents, and the MSP.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. Harm to more than one subsidiary, or to Finance customer information, raised the rating by one level where the harm was not already rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 21 |
| Low | 7 |
| **Total** | **32** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Phishing that bypasses push MFA takes over a shared-services mailbox and single sign-on session | High | Phishing-resistant MFA for high-risk roles; conditional access for managed devices; token-theft alerts | IT Manager | 2026-12-31 |
| R-002 | Business email compromise redirects a vendor payment | High | Callback on every bank-detail change; second approver; 5-day hold | CFO | 2026-10-31 |
| R-003 | Abuse of one of 7 global administrator accounts takes over the group tenant | High | 2 standing admins plus 2 break-glass accounts; hardware keys; time-limited MSP elevation | IT Manager | 2026-11-30 |
| R-004 | Ransomware encrypts cloud workloads and deletes same-account backups | High | Immutable backups in a separate account and region; restore tests; 24x7 detection | IT Manager | 2027-01-31 |
| R-016 | Stolen treasury credentials send a fraudulent wire | Moderate | Bank hardware tokens; documented payee callback | CFO | 2026-11-30 |
| R-021 | A security event at Finance misses the FTC 30-day notice | Moderate | Group incident response plan and runbook; tabletop | IT Manager | 2026-11-30 |

The four High risks share one theme: **a single compromise of the shared platform reaches every subsidiary.** Identity is the front door (R-001, R-003), payments are the most likely target (R-002), and recovery depends on backups an attacker could delete (R-004). Fixing these four also reduces eight related Moderate risks (R-005, R-007, R-008, R-010, R-013, R-016, R-028, R-031).

R-006 and R-019 come from the same finding. On 2026-08-12 the AI assistant pilot showed a Finance loan document to a Supply user, which exposed all-employee access on three collaboration sites. All-employee access was removed from the loan archive the next day.

R-032 was added on 2026-09-11 after control assessment testing (P07) found a shared generic account on three Supply counter desktops.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $61,000):**
  - Hardware security keys for 22 high-risk users and a device-based conditional access policy
  - 24x7 managed detection and response
  - Immutable, separate-account backups and a third-party backup for email and files
  - A log workspace with 1-year retention
  - Vulnerability scanning and an annual penetration test (needed for Finance under 16 CFR 314.4(d)(2))
  - Cellular failover at the Supply warehouse
- **Accepted:**
  - R-024 (Low): ERP outage; the vendor's commitment meets the BIA. Accepted by the CFO.
  - R-027 (Low): lost technician tablet; remote wipe and encryption in place. Accepted by the IT Manager.
- **Contract actions:** security terms and incident notice in the MSP contract (R-013), due 2026-12-31.
- **No High risk was accepted without treatment.**

## 5. Approval
- CFO: approved Moderate and Low treatments and acceptances, 2026-09-25.
- CEO: approved the High-risk treatment plans, 2026-09-25.
- Board of Managers: reviewed the four High risks and approved the budget, 2026-09-25.
- Finance's Board of Managers: received this register as part of the Qualified Individual's 2026 written report, 2026-09-25.
- Next full review: August 2027, or sooner after an acquisition, a major change, or an incident.

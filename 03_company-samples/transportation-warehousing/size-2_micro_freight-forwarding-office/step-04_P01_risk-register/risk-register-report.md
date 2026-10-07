# Risk Register Report: Cris Santos Company | Transportation and Warehousing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (freight forwarding and customs brokerage office) |
| Size tier | Micro (7 employees) |
| Vertical | Transportation and Warehousing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Prepared | 2026-07-31 by the Office and Compliance Manager (Security Coordinator) with the MSP lead technician |
| Updated | 2026-08-12 (R-022 added from P07 testing); 2026-08-31 (R-020 accepted, R-022 closed) |
| Approved | 2026-08-31 by the owner |

## 1. Scope and risk framing
**Scope.** The whole business and its key vendors: every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-10), the office, and the vendors that hold or move client records or money: the customs platform vendor, the MSP and its backup service, the productivity suite vendor, the accounting SaaS vendor, the bank, ocean carriers, and overseas agents.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office and Compliance Manager may accept.
- Moderate: only the owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The owner approves a dated treatment plan instead.

This is the company's first documented risk assessment. The MSP's 2018 onboarding checklist did not rate likelihood or impact and is not relied on.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), and interviews with all 7 employees and the MSP lead technician (2026-07-20 to 2026-07-31).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a business with about $4,400 of revenue per day and about $9 million a year of client and carrier money moving through its account, a diverted wire or a theft of every client file is rated High; losing the license is rated Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 13 |
| Low | 7 |
| **Total** | **23** |

Status: 9 In progress, 12 Open, 2 Closed (R-020 accepted; R-022 treated).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | BEC changes a payee's bank details and a wire goes to the attacker | High | Call-back to a known number; dual approval for new or changed beneficiaries; impersonation protection; training | Owner | 2026-09-30 |
| R-002 | Ransomware encrypts computers and the archive and steals client files | High | Training and phishing simulations; EDR; suite alerts; importer number data map; restore tests | Office and Compliance Manager | 2026-12-31 |
| R-014 | MSP remote tool compromise reaches every computer | High | Annual MSP security review; incident notice and recovery terms at renewal | Owner | 2026-12-31 |
| R-003 | Shared entries@ account taken over | Moderate | Named access with MFA; scan-only printer credential | Office and Compliance Manager | 2026-09-30 |
| R-004 | 72-hour CBP breach notice missed | Moderate | Notice step and template in POL-03 and P08; data map | Office and Compliance Manager | 2026-10-31 |
| R-012 | AI classification suggestions accepted without broker review | Moderate | Broker approval for new products; recorded review sample (P10) | Entry Supervisor | 2026-10-31 |

**The common theme is the mailbox.** Money (R-001), client records (R-002, R-003), and the CBP notice clock (R-004) all run through email. The treatments for R-001 and R-003 (named accounts with MFA, impersonation protection, alerts on new forwarding rules, training) also reduce R-002, R-013, and R-017.

**Customs broker duties drive several Moderate risks.** R-004 (111.21(b)), R-005 (111.28(b)(3)), R-010 (163.5), R-011 (111.24), R-012 (111.28(a)(8)), and R-015 (111.45(a)) exist because the company is a licensed broker. They connect the security program to CBP's grounds for penalties and license action (111.53(c)).

**Risks that were found or changed during the work:**
- R-005: the former Entry Writer's platform account was disabled on 2026-04-01, 19 days after she left. Platform sign-in logs showed no use after her last day. The process gap remains open.
- R-022: added on 2026-08-12 after P07 testing found the printer's default administrator password. The MSP changed it on 2026-08-14; the risk is closed. The stored entries@ credential is handled under R-003.
- R-001: the 2026-05 near-miss (a look-alike agent domain) was recorded during interviews. It shows the likelihood is real, not theoretical.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the owner; about $3,900 one-time and $3,860 a year):**
  - MSP-managed EDR with alert monitoring on 9 computers: about $1,620 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Suite plan upgrade for impersonation protection, alerts, and longer audit logs: about $840 a year
  - Cellular failover router: about $400 one-time and $360 a year
  - Company password manager for shared portal logins: about $240 a year
  - Restore tests, account clean-up, entries@ conversion, and printer connector by the MSP: about $1,200 of MSP time
  - Independent assessment and policy work in 2026 (P07, P06): about $2,300 one-time
  - Annual MSP security review: about $300 a year
- **No-cost process changes:** payment call-back and dual approval (R-001); termination checklist (R-005); CBP notice template (R-004); alternative storage notice to CBP (R-010); AI review rule (R-012); new-client check (R-023).
- **Accepted:** R-020 (Low; laptops encrypted).
- **Contract and legal actions:** client terms clause authorizing service providers (R-011, with counsel) by 2026-12-31; MSP contract terms (R-014) at renewal by 2026-12-31; standby broker arrangement (R-007) by 2026-11-30; second licensed officer (R-015) by 2026-12-31.

## 5. Approval
- Owner: approved all treatment plans, the acceptance, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, a new customs platform, a third licensed broker, or a new AI feature) or an incident.

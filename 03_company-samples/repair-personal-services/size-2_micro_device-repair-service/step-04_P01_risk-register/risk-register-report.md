# Risk Register Report: Cris Santos Company | Other Services (except Public Administration) | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent electronics and device repair shop) |
| Size tier | Micro (7 employees) |
| Vertical | Other Services (except Public Administration) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | Fla. Stat. 501.171(2) "reasonable measures" (a documented risk basis for them); PCI DSS v4.0.1 SAQ P2PE; NIST CSF 2.0 ID.RA |
| Prepared | 2026-07-31 by the Shop Manager (Security and Privacy Lead) with the MSP lead technician |
| Updated | 2026-08-12 (R-024 added from P07 testing); 2026-08-31 (R-021 closed after treatment; R-022 accepted) |
| Approved | 2026-08-31 by the Owner |

## 1. Scope and risk framing
**Scope.** The whole shop and its key vendors: every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-10), the customer devices in the shop's custody, and the vendors that hold or touch customer data: the ticketing and POS vendor (with its AI model provider), the payment processor, the MSP, the backup provider, the productivity suite vendor, the outside data recovery lab, the courier, and the e-waste recycler.

**What the shop protects.** Two kinds of data with different owners:
- the shop's own records: about 15,500 customer records and tickets, invoices, staff records;
- customers' device content while the shop holds the device: photos, messages, health and location data, saved passwords. About 60 devices are in custody at any time.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Shop Manager may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead.

This is the shop's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), the 2026-03-14 customer complaint, and interviews with all 7 staff and the MSP lead technician (2026-07-20 to 2026-07-31). The SYS-01 searches and shop walkthrough on 2026-07-22 supplied the counts used here.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a shop with about $3,600 of revenue per business day and about 15,500 customer records, an exposure of passcodes and account passwords for thousands of customers, or a week-long closure, is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 17 |
| Low | 4 |
| **Total** | **24** |

Status: 11 In progress, 11 Open, 2 Closed (R-021 treated; R-022 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | A technician views or copies personal content from a customer device | High | Device access standard with a test checklist; named bench accounts; USB blocked; signed confidentiality agreements | Owner | 2026-12-31 |
| R-002 | Shared Counter login phished; ticket notes with passcodes, account passwords, and card numbers exported | High | Named counter accounts with MFA; no account passwords collected; restricted passcode field cleared at release; purge; export alerts | Shop Manager | 2026-10-31 |
| R-007 | Ransomware encrypts the counter PCs and bench storage | High | Training and phishing simulations; MSP-managed EDR; immutable backup with MFA; restore tests | Shop Manager | 2026-12-31 |
| R-024 | Bench storage console reachable with a default administrator account | Moderate | Named admin account; label removed; console restricted to the bench network | Senior Technician | 2026-09-15 |
| R-005 | Recycled devices leave with readable customer data | Moderate | SP 800-88 Rev. 2 sanitization standard with a record per device | Senior Technician | 2026-10-31 |
| R-008 | Card numbers on sticky notes and in ticket notes (SAQ P2PE eligibility) | Moderate | Key phone payments straight into the terminal; purge; training | Shop Manager | 2026-09-30 |

**The common theme is customer trust at the bench and the counter.** The two Highs that are specific to a repair shop (R-001, R-002) both come from collecting or reaching more customer data than the job needs, with no record of who did what. The third (R-007) is the ransomware risk every small business carries, made worse here by customer devices on the staff network (R-006) and an untested backup (R-010).

**Risks that were fixed or found during the work:**
- R-003: the Counter password was changed on 2026-07-22, the day the gap was found. The SYS-01 sign-in log showed no Counter sign-ins outside shop hours since the Counter Associate left on 2026-05-08, so the Shop Manager recorded that no unauthorized access was seen. The process gap (no leaver checklist; shared login) remains open.
- R-021: the 2 printed background reports were moved to the locked HR folder on 2026-08-05; the risk is closed.
- R-024: added on 2026-08-12 after P07 testing found the bench storage administrator password on a label and the console reachable from the staff Wi-Fi.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner; about $5,250 one-time and $3,960 a year):**
  - MSP-managed EDR with alert monitoring on the 4 office and 4 bench computers: about $1,500 a year
  - MSP management of the bench computers (patching, standard image): about $1,200 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Backup upgrade to immutable retention: about $400 a year
  - Cellular failover router: about $400 one-time and $360 a year
  - Separate network for customer devices and bench equipment (MSP project): about $900 one-time
  - 4 company-issued encrypted USB drives and bench storage encryption: about $600 one-time
  - Locked cabinet for finished devices: about $350 one-time
  - Independent assessment and policy work in 2026 (P07, P06): about $3,000 one-time
- **Accepted:** R-022 (Low; key-person dependency, reduced through documentation).
- **Contract actions:** written terms for the outside data recovery lab, courier, and recycler (R-018) and data-use terms for the AI assistant (R-012) by 2026-12-31 and 2026-10-31; an incident notice term and technician list in the MSP contract at renewal (R-013) by 2026-12-31.
- **Before the 2026 SAQ P2PE is signed (due 2026-12-15):** R-008 and R-009 treatments complete, with evidence kept.

## 5. Approval
- Owner: approved all treatment plans, the acceptance, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, a second store, a new ticketing platform, or enabling new AI assistant features) or an incident.

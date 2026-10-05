# Risk Register Report: Cris Santos Company | Critical Manufacturing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (transformer repair and remanufacturing shop, Florida) |
| Size tier | Micro (7 employees) |
| Vertical | Critical Manufacturing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Prepared | 2026-07-24 by the Office Manager (Security Coordinator) with the MSP lead technician |
| Updated | 2026-08-12 (R-024 added from P07 testing) |
| Approved | 2026-08-31 by the Owner |

## 1. Scope and risk framing
**Scope.** The whole shop and its key vendors: every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-10), the building and yard, and the vendors that hold shop data or can reach shop systems: the ERP vendor, the productivity suite vendor, the MSP and its backup service, the drying oven OEM, the test set vendor, and the oil laboratory's AI portal. It also covers the shop's duties to others: the G&T cooperative's Vendor Cyber Security Exhibit, the federal purchase order clauses, and Florida's breach law for employee data.

**Risk tolerance and who can accept risk (POL-02 A.3):**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. A risk with a plausible safety impact (oven, test bay) is never accepted above Low.

This is the shop's first documented risk assessment. Nothing earlier rated likelihood or impact.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), a shop walkthrough on 2026-07-14, and interviews with all 7 employees and the MSP lead technician (2026-07-13 to 2026-07-24).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). For a shop with about $4,200 of output per working day, a week without shipments in storm season, the loss of the cooperative contract, or an oven overheating event is rated High or Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 13 |
| Low | 7 |
| **Total** | **24** |

Status: 8 In progress, 16 Open. Treatment: 23 Mitigate, 1 Accept (R-022, Low).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware via phishing encrypts office computers and the shared drive, then reaches the test PC and oven HMI over the flat network | High | Separate networks; MSP-managed EDR; training and phishing simulations; restore tests; runbook | Office Manager | 2026-12-31 |
| R-024 | Internet-facing remote desktop on the unsupported test PC (found by P07) | High | Rule removed 2026-08-11; password change; quarterly external scan; no port forwarding without approval | Office Manager | 2026-09-30 |
| R-006 | Missed cooperative exhibit deadline leads to suspension as a substation vendor | High | Obligations list; notice step in the leaver checklist; notice template | Office Manager | 2026-09-30 |
| R-003 | Oven settings changed through the always-on OEM modem | High | Modem off except approved sessions; OEM credential change; recipe copies | Shop Manager | 2026-10-31 |
| R-002 | Test PC fails with no backup, so nothing ships | Moderate | Nightly database copy; locate media; replacement quote | Shop Manager | 2026-12-31 |
| R-009 | MSP RMM compromise reaches every managed computer | Moderate | MSP contract terms: MFA, 24-hour notice, technician list | Owner | 2026-12-31 |

**The common theme is that the shop floor is wired straight to the office and the internet.** The test PC, the oven HMI, and the camera recorder sit on the same Wi-Fi network as office computers and visitors' phones (R-001, R-016), the test PC was even reachable from the internet (R-024), and the oven OEM can connect at any time (R-003). Separating the shop equipment network (POAM-003) is the single change that lowers the most risks.

**Why R-003 is High despite Low likelihood.** An outsider changing oven settings is unlikely, but the impact is rated Very High because an overheating event could damage customers' transformers and injure staff. The oven's hard-wired over-temperature trip is the main reason the rating is not higher. Under POL-02 A.3, a risk with a safety impact is not accepted above Low.

**Risks found or changed during the work:**
- R-005: the former Field Service Technician's suite and ERP accounts were disabled on 2026-07-15, the day they were found. Sign-in logs showed no use after his last day. The process gap remains open.
- R-006: the Office Manager notified the cooperative on 2026-07-16 and sent a written corrective plan on 2026-07-20.
- R-007: the camera recorder was disconnected on 2026-07-17 pending replacement.
- R-024: added on 2026-08-12 after P07 testing found the port-forwarding rule; the MSP removed it on 2026-08-11.

## 4. Treatment summary
- **Funded (2026 Q3 to 2027 Q2, approved by the Owner; about $6,100 one-time and $3,900 a year):**
  - Network separation (new firewall rules, a managed switch, and a second access point for guest and shop networks): about $900 one-time plus MSP labor
  - MSP-managed EDR with after-hours alerting on 6 computers: about $1,100 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Cellular failover router: about $400 one-time and $360 a year
  - Desktop encryption, ERP MFA set-up, test database copy, and account clean-up by the MSP: about $1,200 of MSP time
  - Replacement camera kit with a documented manufacturer: about $700 one-time
  - Independent assessment and policy work in 2026 (P07, P06): about $2,900 one-time
  - Annual MSP review, quarterly external scan, and remaining MSP project time: about $1,940 a year
- **Quoted, not yet funded:** a supported replacement test PC from the test set vendor (R-002; quote due 2026-10-31) and a portable generator (R-012; decision before the 2027 season).
- **Accepted:** R-022 (Low; CIRCIA is proposed only).
- **Contract actions:** AI vendor data processing addendum and customer consents (R-018) by 2026-09-30; MSP contract amendment (R-009) at renewal by 2026-12-31; OEM written remote access terms (R-003) by 2026-10-31.

## 5. Approval
- Owner: approved all treatment plans, the one acceptance, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, a new test PC, a new cooperative contract term, or expanding AI-001 to more customers) or an incident.

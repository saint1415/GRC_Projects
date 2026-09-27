# Risk Register Report: Cris Santos Company | Transportation Systems | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (Class III short line freight railroad) |
| Size tier | Small (250 employees) |
| Vertical | Transportation Systems |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | Hazmat security plan risk assessment (49 CFR 172.802(a)); tracking of TSA and FRA duties (P03) |
| Prepared | 2026-07-24 by the IT Manager with the Manager of Safety and Security |
| Approved | 2026-08-31 by the President and General Manager (Moderate and below) and the majority owner (High and Very High) |

## 1. Scope and risk framing
**Scope.** The whole organization, tied to its key systems: the Train Dispatch and PTC Operations Platform (TDPO, P02), the TMS, the cloud tenant, office systems, the OT and radio network, and the AI pilot. The business processes are those in the BIA (P05). See `../00_company-facts.md` section 3.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the President and General Manager may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan.
- **Any risk that could lead to a train collision, derailment, or PIH release is not accepted at High or above.** It must be treated.

This is the railroad's first documented cyber risk assessment. The hazmat security plan has its own route and physical security assessment, reviewed in 2026-02. This register adds the cyber and IT risks to it.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), interviews with the Vice President of Operations, Chief Dispatcher, Manager of Safety and Security, and Signal and Communications Supervisor, and CISA and TSA public advisories on ransomware against transportation operators.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. Safety impacts (collision, crossing accident, PIH release) set the rating whenever present.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables with a script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 3 |
| Moderate | 19 |
| Low | 9 |
| Very Low | 0 |
| **Total** | **32** |

Treatment: 28 Mitigate and 4 Accept. Status: 19 Open, 9 In progress, 4 Closed (the 4 accepted risks).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware through the dispatch vendor's always-on remote access encrypts CAD servers, consoles, and the PTC workstation | Very High | On-request vendor access through a jump host with MFA and session logging; filtered dispatch zone; MSP-managed EDR | IT Manager | 2027-01-31 |
| R-003 | CAD backups destroyed along with production | High | Separate immutable backup account; weekly offline copy; quarterly restore test | IT Manager | 2026-12-31 |
| R-004 | Stolen password used on the staff VPN or a server administrator account | High | MFA on both VPNs and all administrators; remove stale accounts | IT Manager | 2026-11-30 |
| R-005 | Conflicting track warrant during an unpracticed switch to manual dispatch | High | Updated manual dispatch procedure; twice-yearly drills; paper kits at each console | Vice President of Operations | 2026-12-31 |
| R-006 | Cyber attack not reported to TSA within 24 hours | Moderate | Cyber triggers and TSOC call in POL-03 and P08; briefing; tabletop | Manager of Safety and Security | 2026-10-15 |
| R-007 | TSA RSSM location request cannot be answered within 30 minutes during an IT outage | Moderate | Clean standby laptop; RSSM car list printed every 4 hours | Car Management and Customer Service Manager | 2026-10-31 |
| R-017 | SSI and the hazmat security plan disclosed to people without a need to know | Moderate | Restricted SSI library with named access | Manager of Safety and Security | 2026-10-31 |

The four risks at High or above share one theme: **a ransomware attack would stop dispatching, and the railroad could neither restore the CAD system quickly nor run safely without it.** The way in is open (R-001, R-004), the backups would not survive (R-003), and the fallback has not been practiced (R-005). Fixing these four also reduces eight related Moderate risks (R-002, R-008, R-012, R-014, R-019, R-021, R-022, R-025).

R-006 and R-007 are Moderate in the register but are **regulatory must-fix items**: they are the only binding TSA duties the railroad is missing (P03 G-007, G-008, G-011). They are due first.

R-010 was added on 2026-08-06 after control assessment testing (P07) found manufacturer default credentials on all 3 wayside detector modems. The credentials are scheduled to be changed by 2026-09-30.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $142,000 approved by the majority owner):**
  - Jump host with session recording and hardware security keys for administrators and the dispatch vendor
  - Firewall rules and switch work for the restricted operations zone
  - MSP-managed EDR with 24x7 triage on servers, operations workstations, and office endpoints
  - Separate immutable backup account and an offline backup drive rotation
  - Log workspace with 1-year retention
  - Standby dispatch laptop and paper dispatch kits
- **Budgeted for 2027:** the CAD upgrade (R-023) and the North Yard standby server and alternate dispatch desk (R-019).
- **Accepted:**
  - R-016 (TMS outage): Moderate, accepted by the President and General Manager because billing can wait and train lists come from the daily export
  - R-028 (website denial of service): Low, vendor-protected
  - R-031 (lost crew tablet): Low, device management with remote wipe
  - R-032 (onboard PTC tampering): Low, sealed housings and the initialization test
- **Contract actions:** security terms for the dispatch vendor and MSP at renewal, and a restoration plan from the PTC back office vendor (R-013, R-022), due by 2026-12-31. Data use and retention terms for the AI pilot vendor (R-027), due 2026-10-31.

## 5. Approval
- President and General Manager: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Majority owner: approved the Very High and High treatment plans and the budget, 2026-08-31.
- Next full review: July 2027, or sooner after a major change, an incident, or a TSA designation notice.

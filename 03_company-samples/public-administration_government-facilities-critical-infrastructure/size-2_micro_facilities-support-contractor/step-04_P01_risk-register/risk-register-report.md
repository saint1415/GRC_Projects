# Risk Register Report: Cris Santos Company | Government Services and Facilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings, NAICS 561210) |
| Size tier | Micro (7 employees) |
| Vertical | Government Services and Facilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT threat considerations from NIST SP 800-82 Rev. 3 |
| Also satisfies | RA-3 Risk Assessment, required at the Moderate baseline by the county security exhibit (CT-C) |
| Prepared | 2026-07-24 by the Office and Compliance Manager (Information Security Officer) with the Lead Controls Technician and the MSP lead technician |
| Updated | 2026-08-06 (R-023 added from P07 testing); 2026-08-31 (R-021 and R-022 accepted and closed) |
| Approved | 2026-08-31 by the owner |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors: the Building Systems Operations Platform (SYS-01 to SYS-08 in `../00_company-facts.md`), the company's access into the city systems (SYS-10) and the GSA building (SYS-11), the 7 site gateways in customer buildings, and the vendors that hold customer data or administer company systems: the access control vendor, the BAS monitoring vendor, the MSP, the suite and backup providers, the CMMS vendor, and the mechanical subcontractor.

**Whose harm counts.** The company's own losses, and harm to the customers' buildings and the people in them. A door left unlocked at a county building or a cooling failure in a records room is the customer's harm, but it comes from the company's systems and is rated here.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office and Compliance Manager may accept.
- Moderate: only the owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The owner approves a dated treatment plan instead. Risks that can affect occupant safety at High are never accepted.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the OT threat discussion in SP 800-82 Rev. 3, the BIA (P05), the gap analysis (P03), walkthroughs of 3 county and 2 city buildings (2026-07-15 to 2026-07-16), and interviews with all 7 staff and the MSP lead technician (2026-07-13 to 2026-07-24).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a company with about $4,400 of receipts per business day, loss of the county contract or harm to building occupants is rated High or Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 13 |
| Low | 6 |
| **Total** | **23** |

Status: 6 In progress, 15 Open, 2 Closed (R-021 and R-022 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Unauthorized remote changes to county schedules and setpoints through the shared SYS-02 "oncall" account | High | Named SYS-02 accounts with MFA; weekly review of writes against work orders | Lead Controls Technician | 2026-10-31 |
| R-002 | Takeover of a SYS-01 administrator account unlocks county doors or exports cardholder data | High | Operator roles for daily work; alerts on new administrators and schedule changes; weekly audit review; MFA number matching | Security Systems Technician | 2026-11-30 |
| R-005 | Ransomware encrypts laptops that hold the only copies of controller programs | High | Engineering repository in the backed-up suite; MSP-managed endpoint detection and response; phishing training | Office and Compliance Manager | 2026-12-31 |
| R-010 | MSP remote management compromise reaches every laptop and the gateway VPN | High | MSP security addendum (RMM MFA, named technicians, 24-hour notice); certificate plus MFA on the VPN | Owner | 2026-12-31 |
| R-003 | Former workforce member keeps access | Moderate | Same-day termination checklist; monthly reconciliation | Office and Compliance Manager | 2026-09-30 |
| R-004 | Outdated gateway firmware or a weak login opens the BAS networks | Moderate | Quarterly firmware review; MFA on the VPN; narrower VPN reach | Lead Controls Technician | 2026-11-30 |

**The common theme is remote reach into customer buildings.** The company's value is that it can see and change 8 government buildings from anywhere. The same paths, a shared SYS-02 account (R-001), broad SYS-01 administrator rights (R-002), password-only gateway VPNs (R-004), and the MSP's tool on every laptop (R-010), are how an attacker would do it. Nobody would notice quickly, because no one reviews the logs (R-014). Closing named accounts, MFA, and weekly log review addresses six risks at once.

**Risks that were fixed or found during the work:**
- R-003: the former Security Systems Technician's SYS-01 administrator account was disabled on 2026-07-15, the day it was found. The SYS-01 audit trail showed no sign-ins after his departure on 2026-04-17. The shared SYS-02 password, which he had known, was changed on 2026-07-16. The process gap remains open.
- R-007: on 2026-07-20 a CUI drawing set was found shared with an "anyone with the link" link to the prime contractor's project manager. The link was removed the same day; the sharing log showed 2 opens, both from the project manager's signed-in account. The Office and Compliance Manager reported it to the prime's security officer on 2026-07-21, and the prime closed it with no further action.
- R-023: added on 2026-08-06 after P07 testing found the manufacturer default administrator password on the parks operations building gateway on 2026-08-05. It was changed that evening.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the owner; about $8,000 one-time and $3,700 a year):**
  - Named SYS-02 user licenses for the 3 technicians: about $600 a year
  - MSP-managed endpoint detection and response with after-hours alerting on 6 laptops: about $1,200 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Company password manager for 7 people: about $350 a year
  - Second-carrier hotspot for the on-call bag: about $300 one-time and $480 a year
  - MSP security addendum and yearly review: about $600 a year
  - Battery backup for 3 gateways: about $450 one-time
  - Engineering repository set-up and first restore tests (staff and MSP time): about $800 one-time
  - Counsel opinion on Fla. Stat. 501.171 scope for cardholder data and face templates: about $2,000 one-time
  - Independent assessment and policy work in 2026 (P07, P06): about $4,500 one-time
- **Staff time only:** gateway VPN MFA and narrower VPN rules (R-004), manual lockdown steps per county building (R-011), weekly log review (R-014), termination checklist (R-003).
- **Accepted:** R-021 (Low; GSA can revoke a lost PIV card, and the return step is added under R-003) and R-022 (Low; critical alarm classes cannot be downgraded by the vendor's model, with monthly review).
- **Contract actions:** MSP security addendum (R-010) and SYS-02 vendor questionnaire (R-001) by 2026-12-31; security addendum for the mechanical subcontractor (R-019) at renewal.

## 5. Approval
- Owner: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (a new contract, expansion of the face verification pilot, a new platform) or an incident.

# Risk Register Report: Cris Santos Company | Communications | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural fiber broadband and voice carrier) |
| Size tier | Micro (7 employees) |
| Vertical | Communications |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | "Reasonable measures to discover and protect against attempts to gain unauthorized access to CPNI" (47 CFR 64.2010(a)) and the evidence behind the annual CPNI certification (64.2009(e)) |
| Prepared | 2026-07-31 by the Office Manager (security and compliance lead) with the Network Operations Lead and the MSP lead technician |
| Updated | 2026-08-12 (R-024 added from P07 testing); 2026-08-31 (R-021 and R-022 accepted and closed) |
| Approved | 2026-08-31 by the Owner and General Manager |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors: every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-10), the office, the network hut, and the fiber plant, and the vendors that hold CPNI or run part of the network: the BSS vendor (which also runs the AI assistant), the hosted voice platform provider, the middle-mile provider, the network engineering consultant, the MSP, the monitoring service, the answering service, and the CALEA trusted third party.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the Owner and General Manager may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner and General Manager approves a dated treatment plan instead. Risks to 911 calling at High are never accepted.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), a walkthrough of the office and the hut on 2026-07-22, and interviews with all 7 employees, the MSP lead technician, and the network engineering consultant (2026-07-20 to 2026-07-31).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a carrier with about $3,000 of revenue a day and about 1,420 accounts, theft of all call detail or a multi-day loss of service is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 15 |
| Low | 5 |
| **Total** | **24** |

Status: 9 In progress, 13 Open, 2 Closed (R-021 and R-022 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Attacker exploits the out-of-date router VPN or the EMS web page to get into the hut | High | Router and OLT firmware upgrades; advisory review; external scan | Network Operations Lead | 2026-09-30 |
| R-002 | Intruder exports call detail records from the voice platform (P08 scenario) | High | MFA and named logins; export limited to 2 roles; password manager | Network Operations Lead | 2026-09-30 |
| R-006 | Intruder uses the stored BSS API key to read every customer record, including driver license numbers | High | Provisioning-only key in protected storage; stop collecting driver license numbers | Office Manager | 2026-11-30 |
| R-011 | A cut of the single middle-mile circuit stops all service | High | Diverse second circuit (2027 budget); customer 911 messaging | Owner and General Manager | 2026-12-31 |
| R-003 | Pretexter obtains call detail by phone | Moderate | Required PIN; send to the address of record otherwise; CPNI training | Office Manager | 2026-10-31 |
| R-004 | Online account takeover through the portal reset | Moderate | One-time-code reset; change notices | Office Manager | 2026-11-30 |

**The common theme is CPNI theft through weak doors.** An intruder can get into the hut through an out-of-date router (R-001), find shared passwords and a full-rights API key on the hut server (R-005, R-006), and walk out with every customer's call detail from a voice portal that has no MFA (R-002). Nothing would raise an alarm (R-010). On the customer side, call detail can be obtained by phone or through the portal with information printed on every bill (R-003, R-004). The treatments for R-001, R-002, and R-006 also reduce R-005, R-010, R-020, and R-024.

**Availability risks are structural.** The single middle-mile circuit (R-011) and the hurricane exposure (R-013) cannot be fixed with settings. A diverse circuit is a 2027 budget decision for the Owner and General Manager; until then the contingency plan covers customer 911 messaging and business number forwarding.

**Risks fixed or found during the work:**
- R-001: the Network Operations Lead removed internet access to the EMS web page on 2026-08-03. The router firmware is still out of date, so the risk stays High until 2026-09-20.
- R-005: the shared OLT and EMS password was changed on 2026-07-23, the day after the walkthrough found that a Field Technician who left in March 2026 still knew it. Device logs only go back about 14 days, so earlier use cannot be ruled out; no sign of misuse was found in the configurations. The shared-account gap remains.
- R-018: the AI assistant's guest verification was turned off on 2026-08-14.
- R-024: added on 2026-08-12 after P07 testing found a vendor default SNMP read-write string on the aggregation switch.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner and General Manager; about $6,900 one-time and $3,300 a year):**
  - Router and OLT firmware upgrades with the network engineering consultant (covered by support contracts): about $1,500 of consultant time
  - Named network accounts with RADIUS or TACACS+ authentication and MFA, and a named consultant login: about $1,800 of consultant time and $300 a year
  - Password manager for 7 users and the consultant: about $400 a year
  - Security awareness and CPNI training with phishing simulations: about $600 a year
  - Off-site encrypted configuration backup through the existing cloud backup: about $300 a year
  - Security alerts through the monitoring service and 1-year log retention: about $1,700 a year
  - Independent assessment and policy work in 2026 (P07, P06): about $3,600 one-time
- **Budget decision for 2027:** a physically diverse second middle-mile circuit (R-011). Quotes due 2026-12-31.
- **Accepted:** R-021 (Low; devices encrypted), R-022 (Low; physical controls proportionate).
- **Contract and filing actions:** voice platform and BSS contract terms for CPNI and incident notice (R-017, R-023) at renewal; consultant agreement (R-020) by 2026-12-31; CALEA SSI refiling (R-016) by 2026-10-31; an evidence-based CPNI certification statement (R-009) by 2027-03-01.

## 5. Approval
- Owner and General Manager: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, a second middle-mile circuit, a new voice platform, or expanding the AI assistant) or an incident.

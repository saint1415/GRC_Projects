# Risk Register Report: Cris Santos Company | Critical Manufacturing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated industrial equipment repair service) |
| Size tier | Sole Proprietorship (owner-technician only, 0 employees) |
| Vertical | Critical Manufacturing (about 80% of receipts from plants that build grid equipment) |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Prepared | 2026-08-28 by the owner-technician, with the on-call IT consultant (under NDA since 2026-08-20) |
| Risk owner and approver | Owner-technician (owner, security lead, and risk acceptor for every risk) |
| Approved | 2026-09-11 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: the FSBS (SYS-01 to SYS-06, SYS-08, SYS-09), the old laptop, paper in the home office, the service van, and the contracted services (IT consultant, bookkeeper). Processes and impact levels come from the BIA (P05). Harm to customers counts as harm to the business: a stopped customer line, a damaged machine, or a broken contract term can end the customer relationship, and Customer A alone is 45% of receipts.

**Risk tolerance.** The owner-technician owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules (POL-01 section 4):
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as they are. Any risk that could affect safety at a customer plant, or that breaks a customer contract term, is never accepted at High.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the contract terms (P03), and a walkthrough of the laptop, phone, field kit, SaaS accounts, and the router at Customer B with the IT consultant (2026-08-26 and 2026-08-27).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (cost, operations, contract, safety, reputation).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 9 |
| Low | 3 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware encrypts the library on the laptop and in synced storage; a customer line cannot be restarted | High | Offline backups with test restores; standard account; customer-held copies; training | Owner-technician | 2026-10-31 |
| R-002 | Malware from the laptop or a USB stick reaches customer plant equipment | High | Never skip Customer A's scanning station; scan every stick; one encrypted stick per customer; isolate the VM | Owner-technician | 2026-10-31 |
| R-003 | Attacker reaches Customer B's drying oven through the owner's always-on router | High | Powered off except approved sessions (done 2026-09-03); MFA; replace or remove | Owner-technician | 2026-12-31 |
| R-004 | Unverified firmware loaded on utility substation cabinets | Moderate | Hash check before every load (exhibit S5) | Owner-technician | 2026-09-30 |
| R-007 | Customer A data in the AI trial without consent | Moderate | Stop uploads; consent under a no-training addendum, or deletion (P10) | Owner-technician | 2026-09-30 |
| R-008 | Owner unavailable or phone lost (single point of failure) | Moderate | Customer-held copies; referral arrangement; sealed recovery codes | Owner-technician | 2026-12-31 |

The three High risks share one cause: **the laptop and USB sticks that carry customers' programs are treated like ordinary office equipment.** One administrator account does email, web, and PLC programming; sticks go from plant to plant unscanned; the only copy of the library besides the laptop is a synced folder that ransomware would overwrite; and a router the owner installed for convenience is a door into a customer's oven. None of these needs much money to fix. Most need a habit change, written down in POL-01 section 7 and checked in P07.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** MFA on the accounting SaaS and router portal (R-003, R-006); hash checks before every firmware load (R-004); never skipping Customer A's scanning station (R-002); stopping Customer A uploads to the AI trial (R-007); adopting the P08 runbook.
- **Low-cost fixes (about $450 once and $80 a year, by 2026-10-31):** two encrypted external drives, 10 encrypted USB sticks, a password manager, and a business Wi-Fi network at home (R-001, R-002, R-005, R-010, R-012).
- **Contract and customer actions (by 2026-12-31):** Customer B decides between its own gateway and removal of the router (R-003); customer-held program copies and a referral arrangement (R-008).
- **Transfer:** cyber liability insurance of at least $1 million before the Customer A renewal on 2027-09-30 (R-014; exhibit S8).
- **Accepted (Low):** R-015 (hurricane; the library is in cloud storage and the laptop travels with the owner).

## 5. Approval
Owner-technician, 2026-09-11: approved all treatment plans and the one acceptance. Next full review August 2027, or sooner after a new customer contract, a new system or vendor, a helper or subcontractor, or an incident.

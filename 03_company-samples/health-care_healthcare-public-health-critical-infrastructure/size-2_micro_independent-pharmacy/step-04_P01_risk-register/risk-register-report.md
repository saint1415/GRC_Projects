# Risk Register Report: Cris Santos Company | Healthcare and Public Health | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent community pharmacy) |
| Size tier | Micro (7 employees) |
| Vertical | Healthcare and Public Health |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A), and risk management, 164.308(a)(1)(ii)(B) |
| Prepared | 2026-07-24 by the Store Manager (Privacy and Security Officer) with the MSP lead technician |
| Updated | 2026-08-05 (R-023 added from P07 testing); 2026-08-28 (R-006 closed as treated; R-020 and R-021 closed as accepted) |
| Approved | 2026-08-28 by the pharmacist-owner |

## 1. Scope and risk framing
**Scope.** The whole pharmacy and its key vendors. That covers every system that creates, receives, maintains, or transmits ePHI (SYS-01 to SYS-09 in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv)), the store itself, and the vendors that handle ePHI or administer systems for the pharmacy: the PMS vendor (with the e-prescribing network, claims switch, and PDMP connection it runs), the MSP, the productivity suite vendor, the cloud fax vendor, the backup service, the packaging equipment vendor, and the proof-of-delivery app vendor ([vendor register](../step-00_P00_intake/vendor-register.csv)). The controlled substance risk score (SYS-09) is in scope as a risk (R-019); its full review is in P10.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Store Manager may accept.
- Moderate: only the pharmacist-owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The pharmacist-owner approves a dated treatment plan instead.
- Two kinds of risk are never accepted at Moderate or above, whatever the cost: risks of patient harm (a missed allergy, interaction, or dose) and risks of breaking a DEA or Florida controlled substance duty.

This is the pharmacy's first documented risk analysis. The only earlier document is a 2022 HIPAA checklist from the PMS vendor (EV-039), which did not rate likelihood or impact and is not relied on.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the intake evidence, the gap analysis (P03), and interviews with the pharmacist-owner, the Staff Pharmacist, the Store Manager, the Lead Pharmacy Technician, the Delivery Driver, and the MSP lead technician (2026-07-13 to 2026-07-24, EV-051). The gap analysis ran in the same fieldwork window, as is usual for a HIPAA risk analysis, and the two shared findings.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**. Each rating rests on evidence named in the `likelihood_basis` column: the vendor console and MSP exports, the payroll and contracts records, the walk-throughs, the account comparison of 2026-07-14 (EV-052), the controlled substance permission and EPCS report reviews (EV-055, EV-059) and the interviews. A rating with no evidence behind it would be a guess, so none was made.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). For a pharmacy with about $3,600 of sales per business day and records for about 11,500 individuals in the PMS, a breach of thousands of patients, a missed DEA duty, or a day without dispensing is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 16 |
| Low | 3 |
| **Total** | **23** |

Status: 10 In progress, 10 Open, 3 Closed (R-006 treated; R-020 and R-021 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware via phishing encrypts the store computers, the packaging workstation, and the synced shared drive | High | Training and phishing simulations; MSP-managed EDR; unique local administrator passwords; immutable backup versions; restore tests; downtime and diversion procedure | Store Manager | 2026-12-31 |
| R-002 | PHI stolen during ransomware (delivery logs, ALF medication lists, downloaded faxes) | High | ePHI inventory; delete old delivery log exports; download folder clean-up; suite alerts | Store Manager | 2026-12-31 |
| R-008 | Attack through the packaging vendor's always-on connection or the unsupported packaging workstation | High | Separate network segment; vendor access on request with a log; BAA; supported controller at the next refresh | Lead Pharmacy Technician | 2026-12-31 |
| R-013 | MSP remote tool compromise reaches every store computer | High | Annual MSP security review; 24-hour incident notice and a recovery time commitment in the MSP contract | Pharmacist-owner | 2026-12-31 |
| R-011 | An EPCS security event is missed and not reported to DEA and the PMS vendor within one business day | Moderate | Daily review of the EPCS audit report by the pharmacist on duty; reporting step in POL-03 | Pharmacist-owner | 2026-09-30 |
| R-014 | Someone other than the certificate holder signs Schedule II orders with the CSOS key | Moderate | Certificate revoked and replaced; the Store Manager applies for a separate certificate under a power of attorney | Pharmacist-owner | 2026-10-31 |
| R-019 | The PMS controlled substance risk score leads to unjustified refusals or treats patients differently by sex or age | Moderate | Pharmacist-only display; documented independent judgment; vendor asked about the sex input; quarterly bias check (P10) | Staff Pharmacist | 2026-10-31 |

**The common theme is ransomware on the store's own computers.** The PMS is vendor-hosted and well protected, but the pharmacy cannot yet detect an intrusion quickly (R-001), does not know every place PHI sits outside the PMS (R-002), and lets two outside parties reach its computers with little oversight: the MSP for every device (R-013) and the packaging vendor for an unsupported workstation on the same network as the counter desktops (R-008). The shared local administrator password found in testing (R-023) would let an attacker move from one computer to all of them. The treatments for these risks also reduce R-003, R-005, R-007, and R-022.

**The second theme is controlled substance duties that the software supports but nobody performs.** The PMS generates the daily EPCS audit report, but no one reads it (R-011). The CSOS certificate was used by someone other than its holder (R-014). Non-pharmacists could alter dispensed controlled substance records (R-006). The vendor switched on a risk score that pharmacists had not reviewed (R-019). None of these needs new technology; each needs a named person and a short routine.

**Risks that were fixed or found during the work:**
- R-006: the permission to annotate and alter dispensed controlled substance prescription records was removed from the Lead Pharmacy Technician and the Store Manager on 2026-07-17, the day after it was found (EV-055, EV-056). The pharmacist-owner reviewed the 12-month audit trail of alterations and found no change to a drug, quantity, or patient. The risk is closed.
- R-004: a former technician's PMS and email accounts were disabled on 2026-07-14, about 11 weeks after the last day. The PMS and email sign-in logs showed no use after the last day, so the Store Manager (Privacy Officer) documented that no breach occurred (EV-052). The process gap remains open.
- R-014: the CSOS certificate was revoked on 2026-07-17 and a new one was issued to the pharmacist-owner on 2026-08-03. Schedule II orders used paper DEA order forms in between. The wholesaler's order history showed no orders the pharmacist-owner did not recognize (EV-057, EV-058, EV-064).
- R-023: added on 2026-08-05 after P07 testing found the same local administrator password on all 5 desktops and the packaging workstation (EV-IA-5).

**Two passes.** Pass 1 was completed on 2026-07-24 from intake and fieldwork evidence. Pass 2 followed the control assessment (P07): R-023 was added on 2026-08-05 from P07 testing. The `assessment_pass` column shows which pass produced each risk.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the pharmacist-owner; about $5,200 one-time and $3,240 a year):**
  - MSP-managed EDR with alert monitoring on 7 computers: about $1,300 a year
  - Security awareness training with phishing simulations for 7 people: about $500 a year
  - Backup upgrade to 90-day immutable versions: about $600 a year
  - Cellular failover router: about $400 one-time and $360 a year
  - Paid proof-of-delivery plan that includes a BAA: about $480 a year
  - Network segments for the packaging workstation and for phones and cameras: about $600 of MSP time
  - Desktop encryption, unique local administrator passwords, account clean-up, and restore tests by the MSP: about $1,200 of MSP time
  - Independent assessment and policy work in 2026 (P07, P06): about $3,000 one-time
- **Staff time, no new spending:** daily EPCS report review (about 5 minutes a business day), monthly account reconciliation, the downtime card and hurricane checklist, the P10 conditions for the risk score, and the annual MSP security review.
- **Accepted:**
  - R-020 (Low): claims switch outages historically last hours; urgent prescriptions are dispensed and billed after recovery.
  - R-021 (Low): laptops and the delivery phone are encrypted, so their loss is not a breach of unsecured PHI (45 CFR 164.402).
- **Contract actions:**
  - BAAs with the proof-of-delivery app vendor (R-012) and the packaging equipment vendor (R-008) by 2026-10-31.
  - MSP contract amendment at renewal by 2026-12-31: 24-hour incident notice, a recovery time commitment, a technician list, and subcontractor BAAs (R-013).
  - PMS vendor: written confirmation of the RTO and RPO in the contract, and an answer on the sex input in the risk score (R-009, R-019).

## 5. Approval
- Pharmacist-owner: approved all treatment plans, the two acceptances, and the budget on 2026-08-28.
- Next full review: July 2027, or sooner after a major change (for example, a new PMS release with new decision support features, replacing the packaging equipment, or a new delivery app) or an incident.

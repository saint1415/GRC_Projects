# Risk Register Report: Cris Santos Company | Retail Trade | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional grocery retailer: 5 supermarkets, online ordering, a distribution center) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Retail Trade |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | PCI DSS v4.0.1 Requirement 12.3 (risks to the CDE identified and managed); the risk basis for FTC reasonable-security expectations (P03) |
| Prepared | 2026-07-31 by the Security Manager and the vCISO; R-050 added 2026-08-14 from P07 testing |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (5 stores, e-commerce, the distribution center and transportation, and support-center functions), the E-commerce and Point-of-Sale Platform (EPP, the SSP system in P02), the ERP and WMS, store operational technology, about 85 vendors (SYS-11), and the AI tools (SYS-12). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed yearly |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-15.

| Area | Appetite | Statement and measure |
|---|---|---|
| Payment card data | **Very low** | No risk of card data compromise is accepted above Low once its treatment is complete. Any card data risk rated Moderate or higher needs a funded plan within 90 days, and the company will not sign an AOC while a known card data gap is open. Measure: card data risks above Low (9 today: R-002, R-003, R-006, R-007, R-012, R-013, R-019, R-034, R-050; target 0 by 2027-09-30, after the P2PE migration) |
| Food safety | **Very low** | No technology risk that could let unsafe food reach customers is accepted above Low. Measure: R-008 and R-018 at Low or lower by 2027-06-30 |
| Customer personal data | **Low** | No risk of a breach of loyalty or customer data affecting 500 or more Floridians is accepted above Moderate. Measure: R-005 and R-022 at Moderate or lower by 2027-03-31 |
| Store and online availability | **Low** | Recovery must meet the BIA RTOs for all High-criticality processes (P05). Measure: each High process has a passed recovery test in the last 12 months |
| Truthful claims and fair pricing | **Low** | Privacy, savings, and pricing claims must match practice, and pricing tools must pass fairness tests before changes go live. Measure: R-023, R-025, R-026 at Low by 2026-12-31 |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no TPSP touches the CDE without a current AOC and a responsibility matrix, and no vendor receives customer data without contract terms on security, use, and deletion |
| Innovation and AI | **Moderate** | The company wants AI benefits in pricing, forecasting, and service, but only through the P10 process. No AI tool makes employment decisions without human review, and no biometric identification is used in stores |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $250,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Retail Trade overlay (card skimming, POS malware, ransomware, loyalty data theft, vendor compromise), the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory and contract, food and customer safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 9 |
| Moderate | 30 |
| Low | 10 |
| Very Low | 0 |
| **Total** | **50** |

Treatments: 46 Mitigate, 4 Accept (R-017, R-043, R-044, R-045). Status: 24 Open, 22 In progress, 4 Accepted.

Cyber insurance ($10 million limit, $250,000 retention) transfers part of the financial exposure for R-001, R-002, R-003, and R-005. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to customers or operations, and it does not satisfy the acquirer.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware halts store POS servers, cloud workloads, and the DC | Very High | Brokered vendor access; off-site immutable store server backups; quarterly restore tests; tabletop | IT Director | 2027-03-31 |
| R-002 | E-commerce skimming script on the checkout pages | High | Script inventory and integrity values; tag manager off checkout; tamper detection for the app checkout | Director of E-commerce and Marketing | 2026-11-15 |
| R-003 | Memory-scraping malware on registers or store servers | High | Validated P2PE at the 2027 terminal refresh; CDE logs to the SIEM; register anti-malware monitoring | IT Director | 2027-09-30 |
| R-005 | Exfiltration of loyalty and CDP data | High | Egress alerting; named export identity; governed transfers | Security Manager | 2027-01-31 |
| R-006 | POS vendor shared support accounts misused | High | Named vendor accounts through the access broker; remove vendor domain administrator rights | Security Manager | 2026-12-31 |
| R-008 | Refrigeration alarms silenced at Stores 4 and 5 | High | IoT VLANs; brokered contractor access; alarm heartbeat; manual-check drill | IT Director | 2026-12-31 |
| R-009 | Privileged account takeover outside the cloud | High | Separate privileged accounts; privileged access management; FIDO2 keys for administrators | Security Manager | 2027-03-31 |
| R-023 | Privacy notice does not match loyalty data sharing (FTC deception) | High | Pause supplier pilot; rewrite the notice; data use agreements | General Counsel | 2026-11-30 |
| R-037 | Hurricane causes multi-day outage at stores and the DC | High | Generator connections at Stores 4 and 5; battery-backed store devices with cloud data | Chief Operating Officer | 2027-05-31 |
| R-050 | Vendor cellular modem exposes a store POS server to the internet (found in P07) | High | Modem disconnected 2026-08-13; sweep all stores; contract clause | IT Director | 2026-10-31 |

**Themes.**
- **The store CDE is large and partly vendor-controlled (R-003, R-006, R-007, R-012, R-033, R-040, R-050).** Because the in-store encryption is not a listed P2PE solution, the registers and store servers carry card data risk, and the POS vendor holds standing, shared access to them. The P07 discovery of an unmanaged cellular modem (R-050) shows the cost of that blind spot.
- **Checkout page integrity (R-002, R-010).** The e-commerce vendor protects the platform, but the company owns the scripts on its checkout pages, and the marketing agency can change them.
- **Recovery and food safety (R-001, R-008, R-014, R-015, R-018, R-037).** Detection is good (EDR, MSSP), and cloud backups are isolated, but no cloud workload has been restored, and refrigeration monitoring depends on flat networks at 2 stores.
- **Data use and AI (R-023 to R-030).** Loyalty data sharing outran the privacy notice, and 4 AI tools went live without review. P10 addresses the AI tools.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15, $940,000 one-time and $360,000 a year):**
- Validated P2PE solution at the 2027 terminal refresh, replacing 65 PIN pads and the store encryption service ($260,000 one-time, offset in part by lower PCI assessment effort)
- Privileged access management for directory, identity provider, POS, and e-commerce administrators, with brokered vendor access and FIDO2 keys ($150,000 one-time, $70,000 a year)
- SIEM onboarding of registers, store servers, and the POS head-office application through the MSSP ($90,000 a year)
- IoT segmentation at Stores 4 and 5 and generator connections ($180,000 one-time)
- Payment page script management and tamper detection for the website and app checkouts ($45,000 a year)
- Recovery testing program, including off-site store server image backups ($80,000 one-time)
- TPSP and vendor risk tooling and part of the GRC analyst role ($85,000 a year)
- SOC 2 readiness and Type 2 examination of the supplier offers service ($210,000 across 2027)
- Penetration testing of the store CDE, segmentation, and the supplier reporting portal ($70,000 a year)

Smaller items (shredders and catering procedure, PIN pad inspection kits, wallet cards, exercise facilitation) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (4):**
- R-017 (Low, COO): processor outage beyond offline mode; a second processor is not justified today.
- R-043 (Low, Director of E-commerce and Marketing): denial of service, with protection inherited from the platform vendor.
- R-044 (Low, IT Director): rogue wireless access points, covered by the wireless controller's detection and locked switch ports.
- R-045 (Low, IT Director): key person dependency, while rebuild procedures are documented under POAM-008.

**Contract actions:** security, use, and deletion terms for the marketing agency and the supplier data pilot (R-023, R-024), due 2026-11-30; a 30-day critical patch term and a ban on unapproved connections in the POS vendor contract (R-033, R-050), due 2026-12-31; the ERP recovery term at the 2027 renewal (R-016).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, payment card, and technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| E-commerce and Point-of-Sale Platform (EPP; SSP in P02) | IT Director | 36 risks whose affected assets include SYS-01 to SYS-04 or SYS-06 to SYS-09 (filter the `affected_asset_or_process` column) |
| PCI DSS cardholder data environment (supports Requirement 12.3) | IT Director, with the Chief Financial Officer as AOC signer | R-002, R-003, R-004, R-006, R-007, R-010, R-011, R-012, R-013, R-019, R-033, R-034, R-042, R-044, R-050 |
| Distribution center and food safety | Distribution Center Director | R-008, R-018, R-037 |
| AI portfolio (P10) | Director of E-commerce and Marketing, with the vCISO | R-025, R-026, R-027, R-028, R-029, R-030 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-017, 2026-09-15.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example the P2PE migration or a store acquisition, R-048) or a significant incident.

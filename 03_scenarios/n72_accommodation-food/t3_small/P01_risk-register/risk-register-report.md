# Risk Register Report: Cris Santos Company | Accommodation and Food Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 140-room beachfront hotel with restaurant and bars) |
| Size tier | Small (60 employees) |
| Vertical | Accommodation and Food Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | PCI DSS v4.0.1 Requirement 12.3 (risks to the cardholder data environment identified and managed) |
| Prepared | 2026-07-24 by the IT Manager (Information Security Lead); R-007 added 2026-08-07; P10 risks refreshed 2026-08-21 |
| Approved | 2026-08-31 by the General Manager (Moderate and below) and the majority owner (High) |

## 1. Scope and risk framing
**Scope.** The Property Management and Point-of-Sale Platform (PMPS) defined in the SSP (P02), the business processes in the BIA (P05), and the vendors that store, process, or transmit card or guest data for the hotel (`../scenario-facts.md` section 3). That covers both merchant accounts (MID-1 Rooms and MID-2 Food and beverage), the guest data in the PMS and the cloud guest-marketing hub, the door lock system, and the two AI systems in P10.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the General Manager may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. Risks to guest physical safety (door locks, evacuation) at High are not acceptable.

This is the hotel's first documented risk assessment since it left the brand's franchise program in 2021. Before then, the brand's PCI program set most controls.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews (General Manager, Controller, Front Office Manager, Revenue Manager, Director of Sales and Marketing, Chief Engineer, MSP lead technician), the gap analysis (P03), and the allegations in *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015), which describe how hotel PMS environments were breached.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05).
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 5 |
| Moderate | 19 |
| Low | 7 |
| **Total** | **31** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Malware on front office PCs captures keyed card numbers | High | Move keyed payments to P2PE device keypads and payment links; EDR; payment VLAN | IT Manager | 2027-01-31 |
| R-002 | Card authorization forms stolen from mailboxes and the paper binder | High | Purge stored card data; payment links instead of forms | Controller | 2026-10-31 |
| R-004 | Stolen front desk login used to display card numbers and export guest profiles | High | MFA for all PMS users; remove excess card-display rights | IT Manager | 2026-10-31 |
| R-005 | MSP or lock vendor remote tool compromised | High | MFA and source restriction; on-demand sessions | IT Manager | 2026-11-30 |
| R-015 | Hurricane damages on-site IT and the lock server | High | IT section of the hurricane plan; protected equipment; tested lock server rebuild | Chief Engineer | 2027-05-31 |
| R-008 | 2026 SAQ D not completed or scope still wrong | Moderate | Scope document; SAQ D evidence file; QSA scoping review | Controller | 2026-12-31 |
| R-011 | Chatbot quotes rates without the mandatory amenity fee | Moderate | Quote total price (16 CFR 464.2) | Director of Sales and Marketing | 2026-09-30 |

Four of the five High risks share one theme: **card and guest data are exposed on ordinary staff systems that the hotel does not need to hold them on.** Keyed card entry on PCs (R-001), card forms in email and paper (R-002), broad card-display rights in the PMS (R-004), and wide-open vendor tools (R-005) all widen the cardholder data environment. The same fixes also shrink PCI scope for 2027 (P03 section 4) and reduce six Moderate risks (R-003, R-009, R-010, R-020, R-026, R-031).

These gaps closely match the practices alleged in *FTC v. Wyndham* (clear-text card data, default passwords, no separation between PMS systems and other networks, unrestricted vendor access, weak detection). R-031 records the resulting FTC Act Section 5 exposure.

The fifth High risk, R-015, is physical: a Gulf Coast hurricane could destroy the ground-floor lock server and network equipment, and nobody has planned how to rebuild them.

R-007 was added on 2026-08-07 after control assessment testing (P07) found the lock vendor's default administrator password on the lock server.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $71,000):**
  - Validated P2PE terminals at the front desk, with keypad entry for phone payments ($9,000 hardware plus processing changes)
  - EDR and 24x7 monitoring through the MSP ($14,000 per year)
  - Network segmentation and firewall rules ($6,000)
  - Central logging with 12-month retention ($5,000 per year)
  - Quarterly ASV scans, internal scans, and an annual penetration test ($12,000 per year)
  - Lock server upgrade and relocation ($15,000)
  - Immutable backups, cellular failover, and a QSA scoping review ($10,000)
- **Accepted:**
  - R-021: Low, vendor separation and client isolation confirmed
  - R-024: Low, MFA on the cloud console
- **Avoided:** R-013, by opting out of the vendor's pooled benchmarking feature.
- **Contract actions:** channel manager AOC (R-022), chatbot transcript retention and masking (R-010), PMS vendor recovery objectives (R-014), all by 2026-12-31.

## 5. Approval
- General Manager: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Majority owner: approved the High-risk treatment plans and the budget, 2026-08-31.
- Next full review: July 2027, or sooner after a major change, an incident, or a change of payment design.

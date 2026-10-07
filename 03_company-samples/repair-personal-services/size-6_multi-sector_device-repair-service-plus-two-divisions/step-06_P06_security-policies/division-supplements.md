# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes, attested every year, and say which division's rules apply where one division operates inside another's sites |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-10 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, no shared accounts, one severity scale, the passcode rule, no terms no data no code | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, sanitization standard (SP 800-88 Rev. 2), Group AI Standard (P10) | Group CISO |
| **Division supplement** | Card brand, manufacturer, TPA, and business associate duties; site-specific rules (bench, PIN pad, customer site) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Device Repair | v2024 | 2024-04 | **Drifted** (scenario gap 10); conflicts listed in section 4; no in-store counter annex | Re-issue with the in-store counter annex by 2026-11-30 (POAM-014) |
| Electronics Retail | v2026 | 2026-06-20 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 | Confirm alignment; co-sign the in-store counter annex |
| IT Support Services | v2025 | 2025-10 | Aligned, but missing the RMM approval rule (POL-02 4.8) and the AI change gate (POL-01 4.12) | Add both by 2026-10-31 (POAM-005; POAM-025) |

## 3. What each supplement adds
### 3.1 Device Repair supplement (repair merchant; manufacturer-authorized service provider; TPA repair network)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Intake and consent | Written or electronic consent to power on, test, and (if asked) transfer data, captured in the STPP before work starts | POL-04 4.6 | 15 U.S.C. 45(a)(1) |
| Passcodes | Vault only; account passwords never collected; paper claim tags show no passcode | POL-04 4.3 | Fla. Stat. 501.171(2); (1)(g)1.b. |
| Bench access | Named bench accounts with badge tap and PIN; session logging; USB blocked except data transfer stations; cache wipe at session end | POL-02 4.1; POL-04 4.6 | 15 U.S.C. 45(n); Manufacturer A agreement |
| Bench software | Only tools on the approved list; updates only through the group software channel after signature checks | POL-01 4.8 | CSF ID.RA-09, PR.PS-05 |
| Infected customer devices | Scan before any data transfer; isolate devices with detected malware on the customer device segment | POL-05 4.5 | Fla. Stat. 501.171(2) |
| Phone payments | Card numbers only into a P2PE terminal while the caller is on the line | POL-04 4.4 | PCI DSS 3.2.1, 9.4 |
| Payment terminals | Weekly logged inspection; device list reconciled with the processor each quarter | POL-05 4.3 | PCI DSS 9.5.1 |
| Data recovery | Delete 30 days after delivery; expiring links for every customer, including enterprise accounts | POL-04 4.5 | Fla. Stat. 501.171(8) |
| Sanitization | Group standard on SP 800-88 Rev. 2; per-device certificates; verification sampling at every depot; serial capture for drop-offs | POL-04 4.7 | Fla. Stat. 501.171(8) |
| Partner notices | Manufacturer A and B within 24 hours; TPA within 48 hours; enterprise accounts within 72 hours after confirmation; acquirer within 24 hours of suspicion | POL-03 4.4 | Contracts; PCI DSS 12.10.1 |
| Devices in incidents | Quarantine in the evidence cage until counsel releases them | POL-03 4.9 | Chain of custody |

### 3.2 Electronics Retail supplement (retail merchant; trade-in program)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CDE network | Lane networks reachable only from the payment switch and approved management hosts; segmentation tested every 6 months | POL-01 4.6 | PCI DSS 1.3, 11.4.5 |
| Payment pages | Only the payment-pages tag container on checkout; script inventory with justification; real-time change alerts to the SOC | POL-01 4.8 | PCI DSS 6.4.3, 11.6.1 |
| PIN pads | Daily inspection at opening; tamper training at hire and every year | POL-05 4.3 | PCI DSS 9.5.1 |
| Trade-ins | No resale listing without a sanitization certificate ID from Device Repair | POL-04 4.7 | Fla. Stat. 501.171(8) |
| Loss prevention | No facial recognition; CCTV kept 30 days | POL-01 4.12 | FTC Act Section 5 (Rite Aid order precedent) |

### 3.3 IT Support supplement (business associate; managed service provider; SOC 2 service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| RMM privilege | Two break-glass global administrators only; just-in-time elevation; phishing-resistant MFA | POL-02 4.3, 4.7 | 164.308(a)(4)(ii)(B); 164.312(d) |
| Multi-customer actions | Second approver for scripts to more than 50 customers or to domain controllers and backup systems; tested kill switch | POL-02 4.8 | 164.308(a)(1)(ii)(B) |
| Customer credentials | In the vault only, partitioned per customer; never in ticket notes or attachments | POL-04 4.3 | 164.312(a)(2)(iv) |
| Customer notices | Notice register by BAA term (10 calendar days standard; 5 business days for 47 practices) and contract term | POL-03 4.4 | 164.410; 164.314(a)(2)(i) |
| Subcontractors | No new vendor that touches ePHI without a subcontractor agreement | POL-01 4.8 | 164.308(b)(2); 164.504(e)(2)(ii)(D) |
| AI and product change gate | Risk analysis update, subcontractor check, and SOC 2 description impact before any AI feature acts on customer systems | POL-01 4.12 | SOC 2 CC2.3, CC8.1 |
| POS network customers | Written acknowledgment and a signed responsibility matrix for every POS network customer; PCI flag on change tickets | POL-01 4.8 | PCI DSS 12.9.1, 12.9.2 |

## 4. Device Repair drift: conflicts with 2026 group policy
The 2024 Device Repair standards were written before the 2025 group policy refresh. At the 260 in-store counters, staff also follow retail store procedures. Where these conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 DR-023; P07 PL-01 finding).

| Topic | Device Repair standard (2024) or retail store procedure | Group policy (2026) | Effect |
|---|---|---|---|
| Bench accounts | 2024 standard allows one shared bench login per counter "where store layout requires" | No shared accounts (POL-02 4.1) | Shared logins at 260 counters (DR-003; POAM-001) |
| Passcodes | 2024 standard says "record passcode in ticket notes if the vault is unavailable" | Vault only; never in notes (POL-04 4.3) | Notes keep growing at 440 stores (DR-001) |
| Account passwords | Not addressed | Never collected (POL-04 4.3) | 96,000 account passwords in notes |
| Screen lock | Retail store procedure disables bench screen lock at counters | 10 minutes idle (POL-02 4.9) | Unattended unlocked benches |
| Technician training | In-store counter technicians take the retail store course | Technician course (POL-05 4.3) | Counter technicians never trained on the access standard |
| Bench software | Store managers may approve tools | Approved list and group channel only (POL-01 4.8) | About 40 tools outside change control (DR-005) |
| Incident notices | 2024 standard lists the acquirer only | All contract clocks (POL-03 4.4) | Manufacturer and TPA terms missed in planning (DR-016) |

**Why the drift happened.** The 2025 group policy refresh was rolled out through the Retail and IT Support supplements first. The Device Repair supplement owner left in 2025 and the review date was not reassigned, and nobody owned the question of which rules apply at in-store counters. **Fix:** POL-01 4.5 now requires the in-store counter annex, re-alignment within 90 days of any group change, and an annual attestation. The Group CISO's policy office tracks supplement versions in the policy register.

## 5. In-store counter annex (to be issued with the Device Repair supplement)
| Area | Whose rules apply | Why |
|---|---|---|
| Bench workstations, tools, passcodes, device custody, technician conduct | Device Repair supplement | Device Repair owns the devices and the STPP |
| Store network, segmentation, physical store access, CCTV | Electronics Retail supplement | Retail owns the store and its cardholder data environment |
| Payments for counter tickets | Electronics Retail supplement (retail lanes) | The retail merchant takes the payment |
| Incidents | Group POL-03; both divisions' liaisons join the bridge | One incident can trigger both merchants' duties |

## 6. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Electronics Retail, IT Support) and on re-issue (Device Repair).

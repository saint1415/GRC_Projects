# Scenario facts: Cris Santos Company | Health Care | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the physician-owner files Schedule C) |
| Business | Solo primary care physician practice (NAICS 621111) |
| Location | Florida. One exam suite leased in a shared medical office building (shared waiting room and building reception) |
| Workforce | The physician-owner only (0 employees). Uses contracted services instead of staff |
| Patients | About 900 active patients; about 12 visits per clinic day, 4 days a week |
| Revenue | About $180,000 a year (fictional). SBA-small (standard $16.0 million, NAICS 621111) |
| Payers | Medicare, Florida Medicaid, and commercial plans. Medicaid is federal financial assistance, so Section 1557 (45 CFR Part 92) applies |
| HIPAA status | **Covered entity**, determined in the intake obligations register (N62-R01): a contracted billing company submits claims electronically on the practice's behalf (EV-017; 45 CFR 160.103) |
| Contrast worth noting | If the physician ran a cash-only direct primary care practice and never conducted standard electronic transactions, HIPAA would not apply. The applicability test is function, not size |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): 42 CFR Part 2, the FTC Health Breach Notification Rule, CMS emergency preparedness conditions, and group health plan requirements do not apply. Payment cards: a vendor-hosted card reader outside the practice's systems |
| State law approach | Florida law is cited only where unavoidable (breach notice, Fla. Stat. 501.171; recording consent, Fla. Stat. 934.03) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Physician-owner | Every role: owner, Privacy Officer, Security Officer, risk acceptor |
| Billing company | Claims and payment posting. A business associate (BAA on file) |
| Answering service | After-hours calls and messages. **No BAA on file** (EV-013, EV-016) |
| On-call IT consultant | Hourly help with the laptop and Wi-Fi. No standing access. **No BAA** (has had remote access to the laptop, EV-015) until the BAA signed on 2026-07-17 (EV-013; see section 7) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds ePHI? | Notes |
|---|---|---|---|---|
| SYS-01 | All-in-one EHR/PM with patient portal and e-prescribing | Vendor SaaS | Yes | System of record. BAA on file. The vendor enforces MFA |
| SYS-02 | Email and file storage (consumer-grade productivity account) | SaaS | Yes (incidental) | **Personal account, not a business plan; no BAA** |
| SYS-03 | Laptop and tablet | Owner devices | Yes (cached, downloads) | Laptop not encrypted; tablet has a passcode |
| SYS-04 | Mobile phone | Personal device | Yes (texts, photos) | Used to text patients and photograph skin conditions |
| SYS-05 | Cloud fax | Vendor SaaS | Yes | BAA on file |
| SYS-06 | Office Wi-Fi | Shared building network | Yes (in transit) | Shared with other tenants; separate password but same network |
| SYS-07 | Consumer AI scribe app on the phone | Vendor app | Yes | Trialed for 2 weeks; **no BAA**; see P10 |

**SSP system (P02):** the *Practice Systems Profile*: SYS-01 to SYS-07.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person practice the sources are the vendors' admin portals, the EHR's reports, bank and card statements, the inbox, signed agreements, the phone, and the insurance agent's portal.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the HIPAA Security Rule** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Ransomware on the laptop, with PHI exfiltration from downloads and email (the EHR SaaS is unaffected) |
| P09 SOC 2 | Security criteria only. Used as a checklist for the EHR vendor's SOC 2 report, and the owner's self-check. A self-attestation is sufficient for payers and referral partners |
| P10 AI | The consumer AI scribe app trial |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-17 | Intake: the owner collects portal exports, statements, agreements, device settings and the suite walk-through; inventories; obligations register |
| 2026-07-20 to 2026-07-24 | Self-assessment with the on-call IT consultant (after BAA signature): BIA, risk analysis, gap analysis, and control assessment (tests on 2026-07-23) |
| 2026-07-27 to 2026-08-28 | POL-01 drafted from the gaps and the test results |
| 2026-08-31 | Deliverables and POL-01 adopted by the physician-owner |
| 2027-02 (planned) | Follow-up check: operating effectiveness of the controls POL-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables (Phase 2)
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| IT consultant BAA | The on-call IT consultant signed a BAA on 2026-07-17, before the self-assessment began. Before that date the consultant had remote access to the laptop with no BAA. The consultant's remote-support tool was still installed with unattended access turned on (found in P07 testing on 2026-07-23 and turned off that day) | P01, P03, P07, P08 |
| AI scribe trial dates | The owner used the consumer AI scribe app for two weeks, 2026-07-06 to 2026-07-17 (8 clinic days, about 96 recorded visits), and paused it on 2026-07-20 when the self-assessment started. Patients were not asked for consent before recording | P01, P10 |
| Billing company access | The billing company works claims in the EHR/PM through its own named user accounts with a billing role, and submits claims electronically to payers on the practice's behalf | P02, P04, P05 |
| Clinical photos | Skin-condition photos are taken with the phone camera and stay in the phone's camera roll. Only some are uploaded to the EHR chart | P01, P04, P05 |
| Cyber insurance | No standalone cyber insurance policy. Whether the professional liability policy includes a cyber endorsement is unconfirmed (owner action in P08) | P01, P08 |
| EHR vendor assurance | The EHR vendor provided its SOC 2 Type 2 report (Security and Availability categories) under a nondisclosure agreement. The owner reviewed it on 2026-07-23 | P02, P09 |
| EHR decision support | The EHR has rule-based preventive care and drug interaction reminders that the owner uses during visits (AI-002 in the P10 inventory) | P10 |
| Cloud fax MFA | The cloud fax portal supports MFA, but it was not turned on (found in P04 mapping) | P04 |

# Scenario facts: Cris Santos Company | Health Care | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

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
| HIPAA status | **Covered entity.** A contracted billing company submits claims electronically on the practice's behalf (45 CFR 160.103) |
| Contrast worth noting | If the physician ran a cash-only direct primary care practice and never conducted standard electronic transactions, HIPAA would not apply. The applicability test is function, not size |
| Not in scope | 42 CFR Part 2; group health plan requirements; payment cards (a vendor-hosted card reader) |
| State law approach | Florida law is cited only where unavoidable (breach notice, Fla. Stat. 501.171; recording consent, Fla. Stat. 934.03) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Physician-owner | Every role: owner, Privacy Officer, Security Officer, risk acceptor |
| Billing company | Claims and payment posting. A business associate (BAA on file) |
| Answering service | After-hours calls and messages. **No BAA on file** |
| On-call IT consultant | Hourly help with the laptop and Wi-Fi. No standing access. **No BAA** (has had remote access to the laptop) |

## 3. Systems
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

## 4. Current security posture: early (few formal controls)
**In place today:**
- EHR MFA (enforced by the vendor)
- BAAs with the EHR vendor, billing company, and cloud fax
- The EHR vendor's backups
- Automatic OS updates on the laptop and phone
- Built-in antivirus
- Paper shredded with a building-provided shredding bin

**Missing:**
1. No risk analysis ever performed (Required, 164.308(a)(1)(ii)(A)).
2. No written policies or procedures.
3. Email is a personal consumer account with no BAA, and it holds PHI.
4. The laptop is unencrypted.
5. The office is on a shared building Wi-Fi network.
6. Patients are texted from a personal phone with no safeguards.
7. The answering service and IT consultant have no BAAs.
8. No incident plan and no contacts list.
9. No MFA on email.
10. No backup of downloaded files or photos.
11. The AI scribe app was used without a BAA or patient consent.
12. No security training (the owner has only CME exposure).

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
| 2026-07-20 to 2026-07-24 | Self-assessment with the on-call IT consultant (after BAA signature) |
| 2026-08-31 | Deliverables adopted by the physician-owner |

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

# Business Impact Analysis: Cris Santos Company | Healthcare and Public Health | Sole Proprietorship

**Organization:** Cris Santos Company (independent community pharmacy) | **Tier:** Sole Proprietorship (pharmacist-owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Pharmacist-owner, 2026-08-04, with the on-call IT consultant (under BAA since 2026-07-31) | **Adopted:** Pharmacist-owner, 2026-09-04
**Sources:** the owner's BIA worksheet, 2026-08-03 to 2026-08-04 (EV-034), the 2025 Schedule C (EV-028), the PMS prescription volume and payer reports (EV-006, EV-007), the PDMP submission log (EV-008), the DEA and CSOS records (EV-025), and the PMS vendor's SOC 2 system description, obtained on 2026-08-05 (EV-037), from which the vendor's stated recovery objectives were added before adoption. The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owner's own statements, adopted by the owner on 2026-09-04.

## 1. Overview and purpose
This one-page BIA lists the five business functions the pharmacy depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency plan standard of the HIPAA Security Rule (45 CFR 164.308(a)(7)), including the applications and data criticality analysis (164.308(a)(7)(ii)(E));
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order and downtime steps in the incident runbook (P08).

## 2. Business description
One pharmacist fills about 14 prescriptions a business day, Monday to Friday, in a storefront pharmacy in a small Florida town, including about 40 non-sterile compounded prescriptions a month. About 15% of prescriptions are controlled substances. The pharmacy has no employees; a relief pharmacist covers about 2 days a month. Almost everything runs in the vendor-hosted pharmacy management system (PMS, SYS-01): profiles, e-prescriptions including EPCS, claims, PDMP reporting, and refill reminders. The rest is a store desktop, a laptop, a phone, an email and file suite, a cloud fax service, and the store network. See `../00_company-facts.md` and the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv).

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts (EV-028) across about 250 business days, Monday to Friday (EV-006), or about $720 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $3,600 (about a week of receipts) | $720 to $3,600 | Less than $720 |
| Operations | No prescriptions can be filled | Filling slowed, or some patients sent elsewhere | Administrative delay only |
| Regulatory | Reportable breach, or a missed DEA or PDMP duty | Missed documentation or timeliness requirement | Internal policy deviation |
| Safety | Plausible patient harm (missed allergy or interaction, interrupted critical medication) | Delayed but safe care | None |
| Reputation | Loss of PBM network status or prescriber trust | Patient complaints or online reviews | None outside the pharmacy |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Prescription intake, verification, and dispensing | High | 24 h | 4 h | 1 h |
| BP-02 Controlled substance dispensing and records | High | 24 h | 8 h | 1 h |
| BP-03 Claims adjudication and payment | Moderate | 72 h | 24 h | 24 h |
| BP-04 Non-sterile compounding | Moderate | 72 h | 24 h | 24 h |
| BP-05 Patient communications and business administration | Low | 72 h | 24 h | 24 h |

**What drives the values:** patient safety drives BP-01 and BP-02, because allergies, interactions, and medication history live only in the PMS. BP-02 also carries two legal clocks: the PDMP report is due by the close of the next business day (Fla. Stat. 893.055(3)(a)), and EPCS records must be kept electronically and intact (21 CFR 1311.305). Claims (BP-03) can wait longer than cash flow suggests, because claims can be submitted after recovery.

**The vendor does not meet the RTO for BP-01.** The PMS vendor's SOC 2 system description states an RPO of 1 hour and an RTO of 12 hours (EV-037; reviewed in P09). The RPO meets the BIA; the RTO does not meet the 4-hour target. The gap is bridged by the paper downtime kit, which does not exist yet (P01 R-001; P08). A regional vendor attack can also last longer than 12 hours, which is why P08 plans for several days.

**Single-person dependency (the key finding).** The pharmacy cannot open without a pharmacist. The owner is the only pharmacy management system administrator (EV-001), the only CSOS certificate holder (EV-025) (21 CFR 1311.30(a) lets only the certificate holder use the key), the DEA registrant contact, and the only person who holds the PDMP, email, fax, and wholesaler credentials. The second factor for email and remote PMS access is on the owner's one phone (EV-002). The relief pharmacist can cover a shift, but today only by using the owner's PMS account (P01 R-003), and cannot order Schedule II stock. If the owner is suddenly unavailable, BP-01 and BP-02 pass their MTD within one business day. Actions (P01 R-011, due 2026-12-31):
1. Create the relief pharmacist's own PMS account and role (also closes the shared-login finding).
2. Decide with the relief pharmacist whether to grant a power of attorney so the relief pharmacist can obtain a CSOS certificate for Schedule II orders (21 CFR 1311.25(a)).
3. Store recovery codes and a one-page emergency access sheet in a sealed envelope held by the owner's attorney (164.312(a)(2)(ii) emergency access procedure).
4. Sign a written arrangement with a nearby independent pharmacy to take patient transfers if the store must close.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 PMS (vendor SaaS) | Profiles, e-prescriptions and EPCS, DUR, labels, claims, PDMP file; vendor backups | BP-01, BP-02, BP-03, BP-05 |
| SYS-03 Store desktop | Counter workstation; label printer; scanner; CSOS certificate | BP-01, BP-02, BP-04 |
| SYS-07 Store network | Internet for the counter; phone hotspot is the fallback | BP-01, BP-02, BP-03 |
| SYS-06 Cloud fax | Faxed prescriptions and refill requests | BP-01 |
| SYS-02 Email and files | Fax copies, compounding records, correspondence (no accepted BAA) | BP-04, BP-05 |
| SYS-04 Laptop and SYS-05 phone | Spare access device; MFA device | All |
| Third parties | PMS vendor (BA) with its e-prescribing network and claims switch; cloud fax vendor (BA); Florida PDMP; drug wholesaler; card processor | BP-01 to BP-05 |
| People | Pharmacist-owner; relief pharmacist as backup | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone, MFA, credentials | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet at the store | 1 h | Phone hotspot |
| 3 | A clean access device | 2 h | Encrypted laptop as the spare; desktop reinstalled by the IT consultant |
| 4 | SYS-01 PMS | 12 h stated by the vendor (BIA RTO 4 h) | Paper downtime kit; 72-hour emergency refills; send acute prescriptions to a nearby pharmacy |
| 5 | Controlled substance records and PDMP reporting | By the close of the next business day | Paper controlled substance log; PDMP web portal upload or extension request |
| 6 | SYS-06 Cloud fax | 8 h | Fax portal from the laptop; phone the prescriber's office |
| 7 | Claims through the switch | 24 h | Hold claims; cash pricing on request |
| 8 | SYS-02 Email and files | 24 h | Printed master formulation records; vendor portals |

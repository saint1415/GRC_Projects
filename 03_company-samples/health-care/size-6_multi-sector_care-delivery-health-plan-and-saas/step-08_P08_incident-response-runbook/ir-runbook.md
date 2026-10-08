# Incident Response Runbook: Ransomware with PHI Exfiltration in the Group Data Platform

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Health Care and Social Assistance |
| Incident type | Ransomware with exfiltration (double extortion) in the Group Data Platform (GDP), a shared corporate system holding data from all three divisions |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-10 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The multi-regulator notification matrix has not been exercised** (group gap 5); the first cross-division tabletop is due 2026-12-15 (POAM-004) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** an attacker phishes a data engineering contractor with an adversary-in-the-middle page, steals a session token, and uses it to read the credentials of one of the 12 service accounts that can read every GDP zone (P07 AC-06 finding).
- **Dwell:** over 6 days the attacker stages and exfiltrates data from the Care Delivery zone, the Health Plan zone, and the staging area of the de-identified zone, where identifiable data from 3 SaaS customers had landed (P01 HT-008).
- **Impact:** on Day 0 the attacker encrypts workspace compute and deletes what it can in provider A, then emails an extortion demand naming all three divisions.
- **Forensic estimate at Day 5:** about 1.3 million Care Delivery patients (about 610,000 in Florida), about 480,000 Health Plan members (about 220,000 in Florida; about 150,000 are also in the Care Delivery count), and about 85,000 patients of 3 SaaS customers in 7 states (about 9,000 in Florida). The de-identified sets were also taken.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC and cloud platform teams | Forensic firm on retainer (through the insurer's panel) | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division general counsels | Out-of-band bridge |
| Care Delivery breach decisions | Care Delivery Privacy Officer | Care Delivery HIPAA Security Officer | Division bridge |
| Health Plan breach decisions | Health Plan Privacy Officer | Health Plan compliance officer (state insurance notices) | Division bridge |
| SaaS customer notices | SaaS security and compliance lead | SaaS general counsel | Division bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email and chat. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts, this runbook, and the notification matrix.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable GDP backups in provider B with a separate backup identity (CP-9; P07 satisfied)
- [x] 24x7 SOC with EDR on all GDP compute (SI-3, SI-4)
- [ ] Per-zone egress alerts on GDP storage (**gap until POAM-003 closes**)
- [ ] Service accounts in identity governance with no all-zone read (**gap until POAM-001 and POAM-006 close**)
- [ ] Notification matrix complete with state insurance contacts and SaaS BAA terms, and exercised (**gap until POAM-004 closes**)
- [ ] SaaS AI feature logs identify each patient (**gap**; needed for 164.410(c)(1) if the model provider is ever involved)
- [x] Forensic retainer and insurer panel confirmed
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Encryption of GDP compute, mass deletion, or ransom note | EDR, cloud audit logs, platform alerts | Declare Severity 1; open the bridge |
| Unusual volume of reads or exports from any zone by a service account | SIEM, platform query logs | Disable the account; start triage |
| Session token used from a new country or device | SYS-G1 risk signals | Revoke sessions; review activity |
| Extortion email or leak-site post naming any division | Email, threat intelligence, law enforcement | Declare Severity 1; preserve the message |
| A division or SaaS customer reports data it believes came from the group | Division liaison, customer | Treat as a potential breach; open an incident |

**Severity 1** (group scale, POL-03 4.2): confirmed encryption or exfiltration in a shared service, or PHI of more than one division involved.

**Record the discovery date for each entity.** For a covered entity, a breach is discovered on the first day it is known, or by reasonable diligence would have been known, to any workforce member or agent (164.404(a)(2)). For a business associate, to any employee or agent (164.410(a)(2)). Because the group SOC is corporate, **this runbook conservatively treats the day the SOC knew as the discovery date for Care Delivery, the Health Plan, and the SaaS.** Counsel may refine this, but no clock is planned from a later date.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Disable the compromised service account and the contractor identity; revoke all GDP tokens and sessions | Group identity director | Accounts disabled; sessions revoked |
| 2. Block GDP egress to the internet at the hub; isolate GDP accounts from division accounts (keep division systems running) | Group network director | Hub rules applied |
| 3. Snapshot affected compute and storage for forensics before rebuilding; place logs on legal hold | SOC; forensic firm | Evidence list signed |
| 4. Confirm the provider B vault and DR replica are intact and unreachable from the compromised identities | Group cloud platform director | Vault integrity report |
| 5. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 6. Notify division privacy officers and the SaaS lead **on the bridge** (this starts the internal 164.410 notice from corporate) | Incident commander | Each acknowledges |
| 7. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.6) | Group CISO | Committee convened |
| 8. Tell division operations that the GDP is down but EHR, claims, and the SaaS are not affected (P05: the GDP is Moderate for availability) | Division liaisons | Operations confirm normal service |

## 5. Analysis (RS.AN)
1. **Scope by zone and by entity.** Use platform query logs (AU-3 records identity, dataset, zone, and row counts) to list datasets read by the attacker. Map each dataset to its covered entity or customer by catalog tag. For the 39% of tables without tags (P07 CM-08a.05), data owners must classify them by hand; plan for this to take days.
2. **Individuals by state.** For each covered entity and SaaS customer, produce counts of affected individuals by state of residence. These drive HHS, media, state, and consumer reporting agency notices.
3. **Overlap.** Identify people who are both Care Delivery patients and Health Plan members. Each covered entity still owes its own notice.
4. **De-identified sets.** Confirm with the expert who certified them whether the stolen de-identified sets, combined with the stolen identifiable data, could re-identify individuals. If yes, treat them as PHI for the affected customers.
5. **Four-factor assessment (164.402)** for each covered entity: nature and extent of the PHI, who obtained it, whether it was actually acquired or viewed, and the extent the risk has been mitigated. With confirmed exfiltration by a criminal group, expect a breach finding.
6. **Root cause:** the contractor phishing path, the service account's all-zone access, and the lack of per-zone egress alerts. Feed these to P01 GR-01 and GR-02.

## 6. Containment and eradication (RS.MI)
1. Rotate every GDP service account credential and move jobs to workload identity (accelerates POAM-002).
2. Remove all-zone read from every service account before restoring (accelerates POAM-006).
3. Rebuild GDP compute from infrastructure code; do not reuse encrypted hosts.
4. Purge and restrict the staging area; stop SaaS exports until de-identification runs inside SYS-D3 (POAM-007).
5. Confirm with forensics that no persistence remains in SYS-G1, the landing zone, or division accounts before reconnecting.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (33 rows).** Counsel approves every notice. The matrix has three layers:
1. **Business associate chain inside the group:** corporate notifies Care Delivery and the Health Plan (164.410 and intercompany BAAs) and, as subcontractor, the SaaS.
2. **Each covered entity's own duties:** Care Delivery and the Health Plan each notify their individuals, HHS, and media (164.404-164.408). They are separate covered entities (no affiliated covered entity designation, P03), so there are **two** HHS reports and two sets of letters. Coordinated letters to people in both populations must identify both entities.
3. **Outward duties:** the SaaS notifies its 3 affected customers (BAA terms of 72 hours or 10 days; never later than 60 days), and every customer asks whether it was affected; the Health Plan notifies insurance commissioners in states that enacted Model #668 (72 hours after determination); the group decides SEC materiality.

| When (from SOC discovery, Day 0) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, forensics engaged; internal 164.410 notice from corporate to both covered entities and the SaaS on the bridge | Group Chief Risk Officer; incident commander |
| Day 0-1 | Voluntary report to FBI or IC3 and CISA (supports OFAC mitigation if payment is considered) | Group CISO |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts (POL-03 4.6) | Group General Counsel |
| Within 72 hours of determination | State insurance commissioners in adopting states (generic; Health Plan list) | Health Plan compliance officer |
| Within 72 hours of discovery | SaaS notice to the affected customers with 72-hour BAAs | SaaS security and compliance lead |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 calendar days of discovery | SaaS notice to affected customers on the standard BAA; 5-business-day incident reports where required | SaaS security and compliance lead |
| Within 10 days (Florida third-party agent duty, as the statute specifies) | Corporate to both divisions; SaaS to Florida customers | Group General Counsel |
| Within 30 days of determination | Florida individual notice (or HIPAA notice with a copy to the Department of Legal Affairs under the deemed-compliance path); Department notice (500 or more Floridians); consumer reporting agencies (more than 1,000). Apply each other state's law the same way | Each covered entity's Privacy Officer with counsel |
| Within 60 days of discovery | HIPAA individual notices; HHS notice (500 or more, contemporaneous); media in each state with more than 500 affected residents | Care Delivery and Health Plan Privacy Officers |
| Confirm before use | CMS notification under the MA contract (**unverified** in this sample) | Health Plan compliance officer |

**Plan to the shortest clock.** In this scenario the order is: SaaS 72-hour customers, state insurance commissioners, SEC (if material), SaaS standard BAAs and Florida third-party agent notices, Florida 30-day notices, then the HIPAA 60-day outer limit.

**Materiality factors for the disclosure committee:** number of people affected across both covered entities; regulatory exposure (OCR, state attorneys general and insurance departments, CMS); SaaS customer contracts and churn; cost of notification and recovery; and effects on operations (limited here, because division systems were not encrypted). Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove any notice duty when data was taken.

## 8. Recovery (RC.RP, RC.CO)
The GDP is Moderate for availability (P05 BP-G05: RTO 24 hours, RPO 4 hours). Restore in this order:
1. Identity and landing-zone controls confirmed clean (BP-G01, BP-G03)
2. GDP rebuilt from code in provider A, with **separated zones and no all-zone service accounts**
3. Data restored from the provider B vault, Health Plan zone first (UM model monitoring and quality deadlines), then Care Delivery, then de-identified
4. Feeds re-enabled one by one after privacy officer approval under a minimum-necessary protocol
5. SaaS exports re-enabled only after de-identification runs inside SYS-D3

Tell division users and SaaS customers when services are restored (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- Update P01 (GR-01, GR-02, GR-03, HT-008), the POA&M (POAM-001 to POAM-007), the notification matrix, and this runbook.
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain all incident records for 6 years (POL-01 4.11).

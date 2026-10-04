# Incident Response Runbook: Ransomware with Student Record Exposure Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Educational Services |
| Incident type | Ransomware with exfiltration (double extortion) that starts in Education Software's support console, takes student records from the college's Campus Platform tenant and other customers' tenants, and encrypts the group data platform and Student Health clinic file servers |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06). For the college, POL-03 and this runbook are the written incident response plan required by 16 CFR 314.4(h) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The cross-division notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop is due 2026-12-15 (POAM-004) |

**Where this plan meets 16 CFR 314.4(h) for the college:**

| Element | Where |
|---|---|
| (h)(1) Goals | POL-03 section 1 |
| (h)(2) Internal response processes | Sections 2 to 6 and 8 below |
| (h)(3) Roles, responsibilities, decision authority | Section 1 below; POL-03 section 3 |
| (h)(4) External and internal communications | Section 7 and `notification-matrix.csv` |
| (h)(5) Remediation of weaknesses | Section 9 (feeds the POA&M) |
| (h)(6) Documentation and reporting | Section 3 (dates); section 7 |
| (h)(7) Evaluation and revision | Section 9 |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (Day -9):** an attacker phishes an Education Software support engineer with an adversary-in-the-middle page and steals a session token. The engineer's support console role has standing read access to every customer tenant (P07 AC-06 finding; POAM-001).
- **Dwell (Day -9 to Day -1):** the attacker uses the console's export function to pull records from the Cris Santos College tenant, 14 other college tenants, and 3 district tenants. A support ticket attachment holds a static secret for a college integration hub service account (POAM-002). With it the attacker reaches the integration hub and the student data warehouse, and from the hub's clinic interface account reaches Student Health's legacy domain (SYS-S2, no MFA).
- **Impact (Day 0):** the attacker encrypts integration hub and warehouse compute in provider A and clinic file servers at 4 legacy clinic sites, then emails an extortion demand to the college president and posts a sample of student records on a leak site.
- **Forensic estimate at Day 5:**
  - **College:** about 610,000 student records, of which about 380,000 people have customer information (SSNs, aid and ledger data) under 16 CFR 314.2; about 140,000 live in Florida. Warehouse extracts with FAFSA-derived fields were also taken.
  - **Education Software customers:** about 230,000 students of 14 colleges in 9 states; about 41,000 students of 3 districts in 2 states, about 17,000 of them under 13 (directory, enrollment, and attendance data; no SSNs).
  - **Student Health:** file shares at 2 of the 4 encrypted sites were copied: scanned intake forms and insurance cards for about 5,800 nonstudent patients (PHI; about 2,100 in Florida) and about 8,100 students (FERPA records of the college and 2 contracting colleges).
- **Not affected:** the Campus Platform and District Platform stayed up; the clinic EHR (vendor-hosted) and FAMS were not reached.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC, cloud platform, and identity teams | Forensic firm on retainer (through the insurer's panel) | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| College determinations (FTC, FSA, FERPA, Florida) | College CISO (Qualified Individual); executive director of financial aid (FSA); university registrar (FERPA records) | College president | Division bridge |
| Customer and district notices | Education Software CISO with privacy counsel | Education Software support director | Division bridge |
| HIPAA determinations and clinic record classification | Student Health Privacy Officer | Student Health security and compliance lead | Division bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications (students, families, customers, patients, media) | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email and chat. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts, this runbook, the notification matrix, the FSA breach intake instructions, and the customer and district contact list.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable backups in provider B with a separate backup identity (CP-9; P07 satisfied)
- [x] 24x7 SOC with EDR on hub compute, campus servers, and clinic servers (SI-3, SI-4)
- [x] Forensic retainer and insurer panel confirmed
- [x] Disclosure committee charter includes cybersecurity materiality
- [ ] No standing cross-tenant support access (**gap until POAM-001 closes**)
- [ ] Integration hub secrets in workload identity, none in tickets or pipelines (**gap until POAM-002 closes**)
- [ ] Egress alerts on warehouse storage and rules for support console misuse (**gap until POAM-003 closes**)
- [ ] Notification matrix complete with district and contracting-college terms, and exercised (**gap until POAM-004 and POAM-024 close**)
- [ ] Clinic records flagged PHI or FERPA record with the owning institution (**gap until POAM-023 closes**; until then the Privacy Officer classifies affected records by hand from intake forms)
- [ ] Student Health legacy domain users on MFA (**gap until POAM-017 closes**)

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Encryption of hub, warehouse, or clinic file servers, mass deletion, or a ransom note | EDR; cloud audit logs; staff reports | Declare Severity 1; open the bridge |
| Support console exports outside a ticket, or from a new device or country | Support console logs; SYS-G1 risk signals | Revoke the session; suspend the account; start triage |
| Service account used from an unusual source or reading unusual volumes | SIEM; warehouse query logs | Disable the account; start triage |
| Extortion email or leak-site post naming the college, Student Health, or a customer | Email; threat intelligence; law enforcement; a customer | Declare Severity 1; preserve the message |
| A customer, district, or contracting college reports data it believes came from the group | Customer contact | Treat as a potential breach; open an incident |

**Severity 1** (group scale, POL-03 4.2): confirmed encryption or exfiltration in a shared service or platform, or Restricted data of more than one division involved.

**Record these dates in the incident log. They start the legal clocks:**
- **Suspected breach (FSA):** report immediately. Do not wait for confirmation.
- **Discovery (FTC, college):** the first day the event is known to any employee, officer, or other agent of the college other than the person committing the breach (16 CFR 314.4(j)(2)). Counsel treats Education Software staff operating the college tenant as the college's agents, so **the college plans from the day Education Software or the SOC first knew**, not the day the college was told (POL-03 4.6).
- **Discovery (HIPAA, Student Health):** the first day known, or that would have been known with reasonable diligence, to any workforce member or agent (164.404(a)(2)). The group SOC is corporate, a business associate of Student Health, so **Student Health plans from the day the SOC knew**.
- **Determination (Florida):** the day each entity determined a breach occurred or had reason to believe one did (Fla. Stat. 501.171(3)-(4)).
- **Materiality (SEC):** the day the disclosure committee decides; the 4-business-day clock starts then.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke the engineer's sessions and disable the account; **suspend all support console access to every tenant** until ticket-bound access is in place | Group identity director; Education Software support director | Console access off; customers can still open tickets by phone |
| 2. Disable the integration hub service accounts and the clinic interface account; reset legacy domain administrator passwords | Group identity director; Student Health security and compliance lead | Accounts disabled |
| 3. Isolate the hub and warehouse accounts at the landing-zone hub; disconnect the 4 clinic sites' file servers from the network (leave them powered on for memory evidence) | Group network director; clinic IT | Isolation confirmed |
| 4. Snapshot affected compute and storage for forensics before rebuilding; place logs (support console, platform, cloud, SIEM) on legal hold before they roll over | SOC; forensic firm | Evidence list signed |
| 5. Confirm the provider B vault and warehouse DR replica are intact and unreachable from the compromised identities | Group cloud platform director | Vault integrity report |
| 6. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 7. Notify the College CISO, the executive director of financial aid, the university registrar, the Education Software CISO, and the Student Health Privacy Officer **on the bridge** (this is the intercompany notice under POL-03 4.6 and corporate's 164.410 notice to Student Health) | Incident commander | Each acknowledges |
| 8. File the FSA breach report (Cybersecurity Breach Intake Form and CPSSAIG@ed.gov) | Executive director of financial aid | FSA confirmation saved |
| 9. Hold outgoing refund files and freeze student bank detail changes until integrity is confirmed | College chief financial officer | No payment file released |
| 10. Brief the Group CISO; convene the disclosure committee within 24 hours (POL-03 4.7) | Group CISO | Committee convened |
| 11. Tell operations what still works: the platforms, FAMS, and the clinic EHR are up; clinics use paper intake at the 4 sites; the SIS-to-FAMS sync is down (P05 workarounds) | Division liaisons | Operations confirm |

## 5. Analysis (RS.AN)
1. **Scope by tenant and system.** Use support console logs (tenant, record type, export size) to list every tenant read. Use warehouse query logs and storage access logs for the warehouse. Use EDR and file server logs for the clinic sites.
2. **Individuals by entity, type, and state.** For the college: students, former students, and parent borrowers, flagged for customer information (FTC and FSA) and education records (FERPA). For each customer: hand Education Software's facts to the customer. For Student Health: **classify every affected clinic record as PHI or FERPA record and, for students, the owning institution** (POAM-023 gap; done by hand from intake forms). Count each group by state of residence; these counts drive the FTC (500 consumers), HHS (500 people), media (more than 500 in a state), Florida (500 for the Department; more than 1,000 for consumer reporting agencies), and other states' thresholds.
3. **Children.** Identify district records of children under 13. COPPA has no breach notice clock, but districts' contracts and state student data laws do, and the FTC will expect the 312.8 program to be evaluated after the incident.
4. **Determinations.** The Qualified Individual and counsel document whether an FTC notification event occurred (16 CFR 314.2(m); unauthorized access to unencrypted customer information is presumed to be acquisition unless reliable evidence shows otherwise). The Student Health Privacy Officer completes the four-factor assessment for the nonstudent PHI (164.402); with confirmed exfiltration by a criminal group, expect a breach finding. Each entity documents its Florida determination.
5. **Root cause:** the phished support session, standing cross-tenant access, a secret in a ticket, and a legacy domain without MFA. Feed these to P01 GR-01, GR-02, GR-07, and GR-14.

## 6. Containment and eradication (RS.MI)
1. Rotate every hub, warehouse, and clinic interface credential and move integration jobs to workload identity (accelerates POAM-002).
2. Re-enable support access only through PAM with ticket and customer approval (accelerates POAM-001).
3. Rebuild hub and warehouse compute from infrastructure code; rebuild clinic file servers from clean images; do not decrypt and reuse encrypted hosts.
4. Search all ticket attachments and pipelines for secrets and remove them.
5. Confirm with forensics that no persistence remains in SYS-G1, the landing zone, the platforms, or the legacy domain before reconnecting.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (30 rows).** Counsel approves every notice. The matrix has four layers:
1. **Inside the group:** Education Software to the college (24 hours, POL-03 4.6); corporate to Student Health (164.410 and the intercompany BAA); Student Health to the college for campus clinic student records.
2. **The college's own duties:** FSA immediately; FTC within 30 days of discovery; Florida and each other state's breach law; FERPA disclosure records; the Qualified Individual's next board report.
3. **Education Software's outward duties:** the 14 colleges and 3 districts within 72 hours (or shorter contract terms); Florida third-party agent notices within 10 days; each customer then makes its own FSA, FTC, and state decisions.
4. **Student Health's duties:** HIPAA notices for about 5,800 nonstudent patients (individuals, HHS, and media where more than 500 residents of a state are affected); contract notices to the college and 2 contracting colleges for about 8,100 student records, which are FERPA records, not PHI.
5. **Group:** SEC materiality and, if material, Form 8-K Item 1.05.

| When (from first group knowledge, Day 0) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, forensics engaged; intercompany and 164.410 notices on the bridge; **FSA breach report** | Group Chief Risk Officer; incident commander; executive director of financial aid |
| Day 0 to 1 | Voluntary report to FBI or IC3 and CISA (supports OFAC mitigation if payment is considered) | Group CISO |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 72 hours | Education Software notices to the 14 colleges and 3 districts (earlier where contracts require); Student Health contract notices to the 2 contracting colleges | Education Software CISO; Student Health Privacy Officer |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days of the agent's determination | Florida third-party agent notices (Education Software to Florida customers; Student Health to contracting colleges) | Education Software privacy counsel; Student Health Privacy Officer |
| **No later than 30 days after discovery** | **FTC notice** on the ftc.gov form (about 380,000 consumers), including any law enforcement delay determination | College CISO with counsel |
| No later than 30 days after determination | Florida individual notices (college; Student Health may use its HIPAA notice with a copy to the Department), Department of Legal Affairs notice (500 or more Floridians, no extension), consumer reporting agencies (more than 1,000). Apply each other state's law the same way | College president with counsel; Student Health Privacy Officer |
| Within 14 days of individual notices | Registrar records the unauthorized disclosure in each affected student's FERPA disclosure record (34 CFR 99.32) | University registrar |
| No later than 60 days after discovery | HIPAA individual notices; HHS notice (contemporaneous, 500 or more); media in each state with more than 500 affected residents | Student Health Privacy Officer |
| Next October report | Event and response in the Qualified Individual's written report to the board of trustees (314.4(i)(2)) | College CISO |

**Plan to the earliest clock.** In this scenario the order is: FSA (immediately), customer and district notices (72 hours), SEC (if material), Florida third-party agent notices (10 days), FTC (30 days from discovery, which is the day the SOC or Education Software knew, often before the college's own determination), Florida (30 days from determination), and the HIPAA 60-day outer limit.

**Law enforcement delay.** A written request can delay Florida individual notices (501.171(4)(b)) and HIPAA notices (164.412). It does **not** remove the FTC notice, which still goes in on time and includes the determination (314.4(j)(1)(vi)).

**Materiality factors for the disclosure committee:** number of people and institutions affected (about 880,000 students across the college and customers, plus patients); regulatory exposure (FSA administrative capability, FTC, HHS, state attorneys general); customer contracts and churn across about 6,300 schools; cost of notification and recovery; and operational effects (limited, because the platforms stayed up). Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board risk committee, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not remove any notice duty when data was taken.

**Not in effect:** CIRCIA reporting to CISA (72 hours, or 24 hours after a ransom payment) is only proposed; the proposed rule would cover every Title IV institution. Reporting is voluntary until a final rule is published.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7):
1. Identity and landing-zone controls confirmed clean (BP-G01, BP-G03); support console access re-enabled only through PAM.
2. Campus and clinic connectivity (BP-G04) and SOC visibility (BP-G02); clinic sites reconnected after rebuild.
3. Campus Platform and District Platform confirmed clean (BP-ES01, BP-ES02); they stayed available, so recovery here means integrity checks and credential rotation, not restore.
4. Clinical care and counseling (BP-SH01 to BP-SH03) continue on the vendor-hosted EHR; clinic file shares restored from the group vault (backups exist since 2026-03; restore never tested, POAM-019).
5. College online instruction and registration (BP-HE01, BP-HE02) continue on the platform.
6. **Student accounts and refunds (BP-HE03, RTO 24 hours):** the integration hub is rebuilt first so the SIS-to-FAMS sync can resume; refunds are released only after student financials are reconciled to FAMS awards and every bank detail change made during the incident window is confirmed with the student by phone. Credit balances must still be paid within 14 days (34 CFR 668.164(h)(2)); urgent cases are paid by check from FAMS award data.
7. Financial aid and SAIG (BP-HE04) resume as soon as the hub sync is verified.
8. The warehouse (BP-G05, RTO 24 hours) is rebuilt **without** the clinic utilization tables and with FAFSA-derived fields restricted (POAM-006, POAM-007).

Tell staff, students, customers, and patients when each service is back (RC.CO). Keep manual workarounds running until each process meets its RTO.

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- **Remediation requirements (314.4(h)(5)):** record every weakness as a POA&M item with an owner and date (P07). Update P01, especially GR-01, GR-02, GR-03, GR-07, HE-001, HE-017, ES-001, and SH-001.
- **Evaluate and revise (314.4(h)(7)):** update this runbook, POL-03, and the notification matrix. Education Software evaluates and modifies its children's information security program (312.8(b)(5)).
- Report the event and response to the college board of trustees (314.4(i)(2)) and the board risk committee; consider the Reg S-K Item 106 description for the next annual report.
- Retain all incident records, determinations, and notices for at least 6 years (POL-01 4.11), which also covers Florida's 5-year retention of any no-harm determination (501.171(4)(c)).

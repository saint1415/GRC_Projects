# Incident Response Runbook: Group Workforce Platform Breach Exposing Worker PII

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Administrative and Support and Waste Management and Remediation Services |
| Incident type | Payroll and HR system breach exposing worker PII: data theft and pay diversion in the Group Workforce Platform (GWP), the shared payroll and applicant tracking platform for all three divisions, with Home Health patient data caught in the theft |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-10 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The multi-regulator notification matrix has not been exercised** (scenario gap 5); the first cross-division tabletop is due 2026-12-15 (POAM-004) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** infostealer malware on a contractor developer's laptop captures a GWP integration service account secret stored as a plain pipeline variable (P07 IA-5 finding) and a live session cookie.
- **Dwell (Day -8 to Day -1):** the attacker uses the service account to call the payroll engine's tax export API, which returns detokenized SSNs, and pulls the integration staging store (Form I-9 Section 1 data and E-Verify case numbers for recent hires) and the visit-pay tables in the workforce data hub.
- **Impact (Day -1, Wednesday):** the attacker changes direct deposit accounts for 1,940 associates through the same API before the weekly payroll run.
- **Detection (Day 0, Thursday morning):** an ACH originating bank flags many deposits to a few accounts. The SOC finds the API exports within hours. An extortion email arrives on Day 1.
- **Forensic estimate at Day 5:**
  - about **1.62 million current and former workers** (names, SSNs, dates of birth, home addresses, bank account and routing numbers): Staffing associates about 1.53 million, Consulting about 24,000, Home Health employees about 51,000, corporate about 12,000; residents of all 50 states and DC, including about 228,000 Floridians;
  - Form I-9 Section 1 data and **E-Verify case numbers for about 186,000 hires** from the last 90 days;
  - **about 214,000 Home Health patients** (names, addresses, visit dates, and visit types) from the visit-pay feed, in 5 states, about 118,000 of them in Florida;
  - **1,940 diverted deposits**; the payroll file was recalled for all but 230 paycard loads (about $118,000).

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC and workforce platform teams | Forensic firm on retainer (through the insurer's panel) | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division general counsels | Out-of-band bridge |
| Pay recovery and associate pay | Group payroll director | Group treasury | Payroll bridge |
| E-Verify notice | Staffing Vice President, Employment Compliance | Director of employment eligibility compliance | Division bridge |
| Home Health breach decisions | Home Health HIPAA Privacy Officer | Home Health HIPAA Security Officer | Division bridge |
| Client notices | Managed Workforce Solutions vice president; Healthcare Staffing president; Consulting HIPAA compliance officer | Account leaders | Division bridges |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads; associate service center director | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email and chat. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts, this runbook, and the notification matrix.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable payroll engine backups in provider B with a separate backup identity (CP-9; P07 satisfied)
- [x] SSN and bank tokenization in the payroll engine (SC-28; P07 satisfied); **but** the tax export API detokenizes for any caller with the export role
- [x] 24x7 SOC with EDR on GWP compute and managed laptops
- [ ] Integration secrets in the secret store and rotated (**gap until POAM-002 closes**)
- [ ] Bank-change and bulk-export detection rules (**gap until POAM-003 closes**)
- [ ] Visit-pay records without patient identifiers (**gap until POAM-006 closes**)
- [ ] Notification matrix complete with the state table, client contract terms, and E-Verify notice, and exercised (**gap until POAM-004 and POAM-005 close**)
- [ ] Payroll address-of-record report by state for former workers (**gap**, P03 RS.AN-08)
- [x] Forensic retainer and insurer panel confirmed
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Bank or paycard manager flags unusual deposits | Treasury | Declare Severity 1 (payroll at risk, POL-03 4.2); open the bridge |
| Burst of bank-account changes or bulk export from the payroll engine or data hub | SIEM, payroll engine logs | Disable the account; start triage |
| Service account used from a new network or outside its schedule | SYS-G1, cloud audit logs | Revoke the credential; review activity |
| Extortion email or leak-site post naming the group | Email, threat intelligence, law enforcement | Severity 1; preserve the message |
| Associates report missing pay | Associate service center, branches | Treat as possible diversion; check bank-change logs |

**Record the discovery and determination dates for each entity.** HIPAA counts from discovery: the first day the breach is known, or by reasonable diligence would have been known, to any workforce member (covered entity, 164.404(a)(2)) or employee or agent (business associate, 164.410(a)(2)). Florida counts from determination of the breach or reason to believe one occurred (501.171(3)-(4)). Because the GWP is run by corporate, **this runbook treats the SOC's declaration date as Day 0 for every division and both clocks.** Counsel may refine this, but no clock is planned from a later date.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Disable the service account and the contractor identity; revoke all GWP tokens and sessions; rotate every integration secret | Group identity director | Accounts disabled; secrets rotated |
| 2. Freeze bank-account changes in self-service and the associate service center | Group payroll director | Change functions off |
| 3. Recall the ACH file; ask the paycard manager to freeze the 230 loaded cards; revert the 1,940 changed accounts from the prior week's records | Group treasury; payroll | Recall confirmed |
| 4. Snapshot affected compute and storage for forensics; place logs on legal hold | SOC; forensic firm | Evidence list signed |
| 5. Confirm the provider B backups are intact and unreachable from the compromised identities | Group cloud platform director | Vault integrity report |
| 6. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 7. **Notify DHS E-Verify immediately** (MOU Art. II.A.16) for each affected employing entity, once the staging store is confirmed in scope | Staffing Vice President, Employment Compliance | Email and call logged |
| 8. Tell the Home Health HIPAA Privacy Officer and the division leads **on the bridge** (this starts corporate's 164.410 notice and Florida 501.171(6) notice) | Incident commander | Each acknowledges |
| 9. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.7) | Group CISO | Committee convened |
| 10. Decide by Wednesday 18:00 whether the next payroll runs normally or as a repeat payroll; send associates the pay message by text and branch scripts (POL-03 4.9) | Group payroll director; associate service center director | Message sent |

## 5. Analysis (RS.AN)
1. **Scope by data set.** Use payroll engine API logs and data hub query logs to list every export: worker register, tax export, staging store, visit-pay tables.
2. **People by employing entity and state.** For each employing entity, count affected workers by state of residence from the address of record. Former workers' addresses may be years old; use the most recent address and email, and plan substitute notice where a state allows it. Florida allows substitute notice only if direct notice would cost more than $250,000, the affected individuals exceed 500,000, or the entity has no mailing or email address for them (501.171(4)(f)); the plan is direct mail or email to every Floridian with a valid address, and substitute notice only for the rest, as counsel decides.
3. **Patients.** Map visit-pay records to Home Health patients by state. These drive HIPAA individual, HHS, and media notices.
4. **Four-factor assessment (164.402)** for Home Health: names, addresses, visit dates and visit types (which reveal that a person receives skilled nursing or therapy at home); taken by a criminal actor; actually exfiltrated; not mitigated by return or destruction. Expect a breach finding.
5. **E-Verify data.** Confirm which hires' case data was in staging and for which employing entity.
6. **Root cause:** a plaintext secret, a service account with detokenizing export rights, no bank-change velocity alert, and patient data in payroll. Feed these to P01 GR-01, GR-05, and GR-10.

## 6. Containment and eradication (RS.MI)
1. Remove detokenizing export rights from every integration service account; tax exports run only under a dedicated, monitored identity (accelerates POAM-002).
2. Move all integration jobs to workload identity before reconnecting (POAM-002).
3. Rebuild the contractor's laptop access path; block unmanaged developer devices.
4. Mask visit-pay patient fields immediately and purge them from the data hub (accelerates POAM-006 and POAM-007).
5. Confirm with forensics that no persistence remains in SYS-G1, the landing zone, or the GWP before re-enabling bank changes.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (31 rows).** Counsel approves every notice. The matrix has four layers:
1. **Inside the group:** corporate notifies Home Health under 164.410 (even though the intercompany BAA does not cover payroll, corporate is acting as Home Health's business associate for this data) and notifies each employing subsidiary as a third-party agent under Florida's 501.171(6) and similar state laws.
2. **Each employing entity's duties:** DHS E-Verify immediately; state breach laws for workers in every state (Florida worked example: individuals and the Department within 30 days; consumer reporting agencies over 1,000); the IRS W-2 data loss notice per EIN.
3. **Home Health's covered-entity duties:** individuals, HHS, and media in each of the 5 states (164.404-164.408); its HIPAA notice can also satisfy Florida's individual notice if a copy goes to the Department (501.171(4)(g)).
4. **Outward duties:** MSP clients within 48 hours; hospital clients per contract (shortest 48 hours); federal contracting officers per contract; banks and the paycard manager immediately; the SEC if material.

| When (from Day 0) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, forensics engaged; DHS E-Verify notice; internal notices to divisions on the bridge; bank recall | Group Chief Risk Officer; Staffing Vice President, Employment Compliance; treasury |
| Day 0-1 | FBI IC3 and CISA reports (support fund recovery and OFAC mitigation) | Group CISO |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 48 hours of discovery | Notices to the 48 MSP clients and to hospital clients with 48-hour terms | Division leads with counsel |
| As soon as confirmed | IRS W-2 data loss email per EIN | Group payroll director |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days of determination | Corporate to each employing subsidiary (Florida third-party agent duty, worked example) | Group General Counsel |
| Within 30 days of determination | Florida individual notices to about 228,000 workers; Department notice; consumer reporting agencies. Apply each other state's law the same way, using the shortest clock | Each employing entity with counsel |
| Within 60 days of discovery | Home Health HIPAA notices to about 214,000 patients; HHS (contemporaneous); media in each of the 5 states; copy of the Florida notices to the Department within its 30-day window | Home Health HIPAA Privacy Officer |

**Plan to the shortest clock.** In this scenario the order is: E-Verify (immediate), banks (immediate), MSP and hospital clients (48 hours), SEC (if material), corporate's third-party agent notices (10 days), state notices (Florida 30 days, others as their laws require), then the HIPAA 60-day outer limit. Home Health should not wait for day 60: patients in Florida are best notified within the 30-day window so one letter serves both laws.

**Materiality factors for the disclosure committee:** about 1.62 million workers and 214,000 patients affected; regulatory exposure (state attorneys general, OCR, DHS); client contract exposure and churn (MSP clients, hospitals); cost of notification, credit monitoring, repaid pay, and recovery; effects on operations (pay disrupted for one week for 1,940 associates; recruiting and onboarding slowed during containment); and reputational effects on recruiting. Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not remove any notice duty when data was taken.

**Credit monitoring and identity protection** are offered as a group decision with counsel and the insurer; some states set their own requirements, which counsel's state table covers.

## 8. Recovery (RC.RP, RC.CO)
The GWP payroll engine has an RTO of 12 hours and an RPO of 1 hour (P05 BP-G04). Restore in this order:
1. Identity and landing-zone controls confirmed clean (BP-G01, BP-G03)
2. Payroll engine with integration accounts on workload identity and no detokenizing export rights; bank changes re-enabled only with out-of-band confirmation and a 3-day hold for first-time changes
3. Integration feeds one by one: Staffing time, Consulting timesheets, then Home Health visit records **without patient identifiers**
4. Onboarding and E-Verify work resumes with a backlog plan so Form I-9 and E-Verify deadlines for new hires are met (8 CFR 274a.2(b)(1)(ii); MOU Art. II.A.7)
5. Data hub restored last, after the visit-pay purge

Tell associates, divisions, and clients when pay and services are back to normal (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.12).
- Update P01 (GR-01, GR-05, GR-10, ST-001, ST-002, HH-001), the POA&M (POAM-001 to POAM-008), the notification matrix, and this runbook.
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain all incident records for 6 years (POL-01 4.12).

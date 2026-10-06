# Incident Response Runbook: Compromise of the Shared Identity Platform Affecting All Subsidiaries

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (holding company, corporate shared services, Insurance, and Health Care Services) |
| Tier / Vertical | Multi-Sector / Management of Companies and Enterprises |
| Incident type | Compromise of shared services: an attacker takes over a privileged identity in the group identity platform (SYS-G1) through help desk social engineering, then reaches the SCSP (treasury payment routing, HCM data), insurance claims data, and clinic records |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; POL-02 4.4 (identity recovery); division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The multi-regulator notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop, using this scenario, is due 2026-12-15 (POAM-009) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (Day -1, Friday evening):** an attacker calls the Insurance division help desk posing as an SCSP integration engineer who has lost a phone while traveling. Using the engineer's employee ID and manager's name from public sources, the caller passes the current checks (P07 IA-05a.) and the agent, who holds group-wide reset rights (P07 AC-06), issues a temporary access pass.
- **Privilege use (Day -1 to Day 0):** the engineer's identity can request PAM elevation for integration services. The attacker:
  - changes the beneficiary mapping for 38 repair-shop payees in the claims disbursement route. The change is not found on Day 0; on Monday (Day 1) 3 payments totaling $610,000 are released through the altered mapping before positive pay review flags them, and the banks recover 2 of them ($425,000), leaving $185,000 lost;
  - pulls an HCM report through an integration service account: about 105,000 current and former employees (names, SSNs, bank accounts) and, from the linked plan administration site, appeal files of about 2,300 group health plan members;
  - uses single sign-on to export about 410,000 personal lines claim records from SYS-I2 (claimants' names, contact details, policy numbers, injury descriptions);
  - adds the identity to the clinic EHR adjuster group in SYS-G1 and views about 1,900 patient charts.
- **Detection (Day 0, Sunday 06:10):** the SOC's mass-export alert on SYS-G5 fires. Positive pay exceptions on Monday confirm the payment redirection.
- **Forensic estimate at Day 5:** about 105,000 employees and former employees in 31 states (about 61,000 in Florida); about 410,000 claimants and policyholders (Florida about 238,000, Alabama 41,000, South Carolina 33,000, Tennessee 29,000, Georgia 44,000, North Carolina 25,000); about 1,900 patients (about 1,200 in Florida); about 2,300 plan members (about 1,400 in Florida).

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Identity containment | Group identity director | Identity vendor's incident team | SOC bridge |
| Payments | Group Treasurer | Head of treasury operations | Bank fraud desks by phone on file |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| Insurance notices | Insurance chief compliance officer | Insurance information security officer | Division bridge |
| Health Care Services breach decisions | HIPAA Privacy Officer | HIPAA Security Officer | Division bridge |
| Group health plan breach decisions | Group benefits director (plan privacy official) | Group security governance director (plan security official) | Plan bridge |
| SEC materiality | Disclosure committee | Group Chief Financial Officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read email, chat, and identity administration consoles. Use the crisis line and managed mobile devices. The printed binder in each division holds contacts, this runbook, and the notification matrix.

## 2. Preparation checks (Identify / Protect)
- [x] Hardware keys for administrators (IA-2(1); P07 satisfied)
- [x] Immutable backups and SYS-G1 configuration exports (CP-9; P07 satisfied)
- [x] Positive pay and dual approval on treasury releases
- [ ] MFA resets verified to the strength of the authenticator; division-scoped help desk rights (**gap until POAM-001 closes**)
- [ ] Bank-detail and payee mapping changes verified out of band before payment (**gap until POAM-013 closes**; the integration route change in this scenario bypassed the claims system entirely)
- [ ] Service accounts owned and in analytics (**gap until POAM-002 closes**)
- [ ] Notification matrix complete with commissioner, producer, and plan rows, and exercised (**gap until POAM-009 and POAM-010 close**)
- [x] Forensic retainer and cyber insurance panel confirmed
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| MFA reset or temporary access pass for a privileged or payment-role user | SYS-G1 audit log; SOC rule | Call the user on the number in HCM; if not confirmed, disable and declare |
| Mass export from HCM, claims, or the EHR | SIEM; application logs | Disable the identity and service account; declare Severity 1 if data left |
| Change to a payment route, payee mapping, or bank template outside a change ticket | Integration audit log; treasury | Freeze the route; call treasury; check releases since the change |
| Positive pay exception or bank fraud call | Treasury; banks | Recall payments; preserve records; open an incident |
| Identity added to another division's application group | SYS-G1 governance alert | Remove; review the identity's activity |

**Severity 1** (group scale, POL-03 4.2): compromise of a privileged identity in SYS-G1, confirmed exfiltration from a shared service, or regulated data of more than one division involved.

**Record the knowledge date once, for everyone.** The group SOC is part of the holding company. Under POL-03 4.3 the date the SOC knew (Day 0) is recorded as:
- the HIPAA discovery date for Health Care Services and for the holding company as its business associate (164.404(a)(2); 164.410(a)(2)), and the date the plan sponsor knew for the group health plan;
- the date the insurers had actual knowledge of an event at their Third-Party Service Provider (Model #668 sec. 6D(2) starts their clock the next day);
- the starting point for state breach determinations.
Counsel may document a later determination date with reasons, but no clock is planned from a later date.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke all sessions and tokens for the compromised identity; disable it; remove the temporary access pass; remove it from every group it joined (including the EHR adjuster group) | Group identity director | Identity disabled; group changes reverted |
| 2. Freeze help desk resets for privileged and payment-role users; route all resets to the group identity team (interim POAM-001 procedure) | Group identity director | Freeze confirmed with all three help desks |
| 3. Freeze the claims disbursement route; restore the payee mapping from the last approved version; hold today's claims and vendor payment files for manual review | Group Treasurer; SCSP platform director | Route frozen; files held |
| 4. Call the banks' fraud desks to recall the 3 released payments; file an IC3 complaint for the wire and ACH fraud | Group Treasurer | Recall requests acknowledged |
| 5. Rotate the integration service account credentials and every PAM-vaulted secret the identity could reach | Group identity director | Rotation report |
| 6. Snapshot logs from SYS-G1, PAM, integration services, SYS-G5, SYS-I2, and the EHR; place them on legal hold | SOC; forensic firm | Evidence list signed |
| 7. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 8. Notify on the bridge: Health Care Services Privacy Officer, the plan privacy official, and the Insurance chief compliance officer (this is the holding company's internal notice as business associate, plan sponsor, and service provider) | Incident commander | Each acknowledges |
| 9. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.7) | Group CISO | Committee convened |
| 10. Tell operations: claims handling, clinics, and payroll continue; only the claims payment route is on manual review | Division liaisons | Operations confirm normal service |

## 5. Analysis (RS.AN)
1. **Scope by identity.** Reconstruct everything the compromised identity and the service account did from SYS-G1, PAM, integration, and application logs. Because SYS-G1 is shared, check for persistence in every division: new application registrations, federation trusts, conditional access changes, mailbox rules, and group memberships.
2. **Affected people by entity and state (POL-03 4.6).** Produce counts within 5 days for each regulated entity separately: Health Care Services patients; group health plan members; each insurer's consumers; and employees and former employees. These counts drive commissioner, HHS, attorney general, and media notices.
3. **Four-factor assessments (164.402)** for Health Care Services and, separately, for the group health plan. Confirmed viewing and exfiltration by a criminal group will usually mean a breach finding.
4. **Insurance criteria.** For each state that enacted Model #668 (Alabama, South Carolina, Tennessee), the insurers notify the commissioner if 250 or more of the state's consumers are involved and the event must be reported to another government body or is reasonably likely to materially harm a consumer or the insurer's operations (sec. 6A(2)). Here both prongs are met in all three states.
5. **Payment integrity.** Reconcile every payment released through the route since the change; confirm no payroll or other route was altered (SI-7 file integrity logs).
6. **Root cause:** help desk reset with weak verification (IA-5), group-wide reset rights (AC-6), a payee mapping change that bypassed the claims system's verification (POAM-013), and an unowned service account (AC-2). Feed these to P01 GR-01, GR-03, and GR-11.

## 6. Containment and eradication (RS.MI)
1. Confirm with forensics that no persistence remains in SYS-G1 or division applications before restoring normal help desk operations.
2. Re-verify every privileged and payment-role user's authenticator registered in the last 30 days.
3. Require change tickets and dual approval for any payment route or payee mapping change; compare all routes to the approved baseline.
4. Disable the HCM report the attacker used for anything except the payroll team; mask SSNs in standard reports (GR-12).
5. Remove group-wide reset rights from division help desks (accelerates POAM-001).

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (32 rows).** Counsel approves every notice. The matrix has four layers:
1. **Inside the group:** the holding company notifies Health Care Services (as its business associate, 164.410 and the 2021 BAA), the group health plan (as plan sponsor), and the insurers (as their Third-Party Service Provider; Fla. Stat. 501.171(6) third-party agent notice applies where Florida residents' information is involved).
2. **Each regulated entity's own duties:** Health Care Services and the group health plan are separate covered entities, so there are two HIPAA determinations, two HHS reports, and separate letters. The insurers give commissioner notices in Alabama, South Carolina, and Tennessee, consumer notices under each state's breach law, and producer of record notices as the commissioner directs.
3. **Employer duties:** the holding company and each employing subsidiary notify current and former employees under each state's breach law (Florida worked example: Fla. Stat. 501.171).
4. **Group duties:** SEC materiality; law enforcement; the cyber insurer; banks.

| When (from SOC knowledge, Day 0) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, forensics engaged; internal notices on the bridge to Health Care Services, the plan, and the insurers | Group Chief Risk Officer; incident commander |
| Day 0-1 | Bank recalls; IC3 complaint for the payment fraud; voluntary report to FBI and CISA | Group Treasurer; Group CISO |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts (POL-03 4.7) | Group General Counsel |
| Within 72 hours of determination (clock starts the day after actual knowledge, sec. 6D(2)) | Commissioners in Alabama, South Carolina, and Tennessee (250 or more residents each) | Insurance chief compliance officer |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days after determination of the breach (Florida third-party agent duty, Fla. Stat. 501.171(6)(a)) | Holding company to each affected entity, in writing, with all information the entity needs for its own notices | Group General Counsel |
| Within 30 days of determination | Florida individual notices (employees, claimants; patients and plan members may use the HIPAA notice with a copy to the Department of Legal Affairs); Department of Legal Affairs notice (500 or more Floridians); consumer reporting agencies (more than 1,000). Each other state's law applied the same way | Each entity's responsible official with counsel |
| With consumer notices | Copies of consumer notices to the commissioners notified (sec. 6C); producers of record as directed (sec. 6F) | Insurance chief compliance officer |
| Within 60 days of discovery | HIPAA individual notices for patients and plan members; HHS (500 or more, at the same time); media in each state with more than 500 affected residents | Health Care Services Privacy Officer; plan privacy official |

**Plan to the shortest clock.** In this scenario the order is: bank recalls and internal notices (Day 0), commissioners (72 hours), SEC (4 business days after a materiality determination), Florida third-party agent notices (10 days), Florida and other state 30-day notices, then the HIPAA 60-day outer limit.

**Materiality factors for the disclosure committee:** number of people affected across four regulated populations (about 519,000 in total); regulatory exposure (three commissioners, HHS for two covered entities, state attorneys general); the direct loss ($185,000) and response costs; the effect on the insurers' and clinics' reputation with agencies and employer clients; and whether the compromise of the shared identity platform shows a weakness in controls that matters to investors. Materiality is decided without unreasonable delay; the 4-business-day clock starts at the determination, not at discovery.

**Ransom or extortion:** if the attacker demands payment for the stolen data, any payment needs board risk committee approval, counsel, the insurer, and an OFAC sanctions check (POL-03 4.8). Paying does not remove any notice duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in the P05 order:
1. SYS-G1 identity, with privileged registrations re-verified (BP-G01)
2. Landing zones and SOC visibility confirmed clean (BP-G03, BP-G02)
3. SCSP integration services and the claims payment route from the approved baseline (BP-G12), then treasury releases with manual review for 10 business days (BP-G04)
4. HCM reporting, restricted (BP-G05, BP-G11)
5. Normal help desk operations under the new reset procedure

Tell division leaders, independent agencies (through the Insurance distribution team), and employer clients (if they ask) when services are back to normal (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.11).
- Update P01 (GR-01, GR-03, GR-07, GR-11), the POA&M (POAM-001, POAM-002, POAM-009, POAM-010, POAM-013), the notification matrix, and this runbook.
- Report the event and response in each insurer's next annual board report (Model #668 sec. 4E(2)(b)).
- Consider the Reg S-K Item 106 description for the next annual report.
- Keep all incident records at least 5 years for the insurers (sec. 5D) and 6 years for HIPAA documentation (POL-01 4.13).

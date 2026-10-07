# Incident Response Runbook: Exfiltration of CUI Spanning Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Defense Industrial Base |
| Incident type | Exfiltration of Controlled Unclassified Information (CUI) from the shared GCEE and from prime customers' tenants in the industry edition (SYS-D4), using one stolen single sign-on session |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Contract and legal basis | DFARS 252.204-7012(b)(2)(ii)(D), (c) to (g), (m)(2)(ii); DFARS 252.239-7010(d) to (f); 32 CFR 117.8; 22 CFR 127.12; 15 CFR 764.5; Form 8-K Item 1.05; Fla. Stat. 501.171 (worked example for state law). Text checked on eCFR (version date 2026-09-23) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The multi-regulator matrix has not been exercised** (scenario gap 8); the first cross-division tabletop with a DIBNet drill for every division is on 2026-11-18 (POAM-019) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** an Engineering Services field engineer working on a prime's site opens a lure about a test schedule change. An adversary-in-the-middle page relays the sign-in and steals the SYS-G1 session token. Push MFA does not stop it (P01 ES-001).
- **Reach:** the token gives the attacker the engineer's single sign-on access to (a) GCEE projects for two Aircraft Parts programs, including Program H, and three Engineering Services projects; and (b) the industry edition (SYS-D4) tenants of **Prime A** and **Prime D**, where the engineer supports sustainment engineering (P01 ES-016).
- **Dwell:** over 4 days the attacker downloads about 3,400 files from the GCEE through the virtual desktop web client, stays under the group-wide download threshold (P07 SI-4(4)), and exports reports from the two SYS-D4 tenants.
- **Personal information:** one Engineering Services project folder held a test range badging roster with names and Social Security numbers of 640 employees (280 in Florida; 360 in 5 other states).
- **Discovery (Hour 0):** the SOC sees the engineer's session used from a hosting provider while the engineer is badged in at the customer site.
- **Not affected:** the DoD edition (SYS-D3), plant MES and DNC, classified systems. No ransomware.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC, identity, and cloud platform teams | Forensic firm on retainer (insurer panel) | SOC bridge |
| Notifications and legal | Group General Counsel with outside government contracts and export counsel | Division general counsels | Out-of-band bridge |
| Aircraft Parts DoD reports and prime notices | Aircraft Parts director of contracts (certificate holder) | 3 other Aircraft Parts certificate holders | Division bridge |
| Engineering Services DoD reports | Engineering Services contracts director (certificate holder) | Second certificate holder | Division bridge |
| Defense Software CSP reports and tenant notices | Defense Software customer operations director | **No certificate holder until POAM-012 closes; an Aircraft Parts holder cannot file for Defense Software contracts** | Division bridge |
| What was taken (data owners) | Aircraft Parts VP of engineering; Program H chief engineer; Engineering Services VP of engineering | PLM administrators | Division bridge |
| Export decisions | Division Empowered Officials | Group export compliance director | Out-of-band bridge |
| NISPOM reports | Engineering Services facility security officers | Group ITPSO | Phone |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Employee notices | Group Chief Privacy Officer | Group HR director | Out-of-band bridge |
| Law enforcement | FBI field office; CISA | IC3 | Contacts in the printed incident binder |

**Out-of-band first.** Assume the attacker can read corporate email and chat while the session is live. Use the crisis line and managed mobile devices. Each division keeps a printed binder with contacts, this runbook, the notification matrix, and the DIBNet field list (CAGE codes, contract numbers, prime contacts, facility clearance status).

## 2. Preparation checks (Identify / Protect)
- [x] 24x7 SOC with EDR and SIEM coverage of the GCEE and SYS-D4 (SI-4; P07)
- [x] Forensic retainer with cloud and endpoint imaging; 1-year online log retention (252.204-7012(e))
- [x] Certificate holders: Aircraft Parts (4), Engineering Services (2, one center)
- [ ] Defense Software certificate holders and CSP reporting procedure with tenants (**gap until POAM-012 closes, 2026-11-30**)
- [ ] Phishing-resistant MFA for all CUI users (**planned by 2027-03-31; GR-01**)
- [ ] Per-project download baselines, Program H first (**gap until POAM-013 closes**)
- [ ] Group matrix exercised with every division (**gap until POAM-019 closes, 2026-11-18**)
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| One session used from two places, or from a hosting provider or anonymizing service | SYS-G1 risk signals; SIEM | Revoke sessions; open an incident |
| Download volume or project spread unusual for the user | PLM and gateway logs; SIEM | Suspend the account; open an incident |
| Exports from a SYS-D4 tenant by a group engineer outside working hours | SYS-D4 tenant audit records | Suspend the account; tell the Defense Software lead |
| A prime, DC3, the FBI, or another agency reports group data seen elsewhere | External notice | Declare Severity 1 at once |

**Severity 1** (group scale, POL-03 4.2): confirmed or strongly suspected access to CUI by an unauthorized party in a shared service, or CUI of more than one division or of a customer tenant involved.

**Record discovery per division and per contract.** The 72-hour DoD clock runs from discovery of the cyber incident, and a cyber incident includes any compromise, including possible copying of information to unauthorized media (252.204-7012(a)). **This runbook treats the time the SOC first suspected unauthorized access (Hour 0) as discovery for every division and for the SYS-D4 tenants.** No clock is planned from a later date.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke all sessions and refresh tokens for the account in SYS-G1; disable the account; revoke SYS-D4 tenant sessions | Group identity director; Defense Software platform operations | Sign-in logs show no further attacker activity |
| 2. Block attacker infrastructure and the phishing domain at the hub, SYS-G1, and email filtering; search for other recipients and revoke their sessions | Group SOC | Blocks confirmed; recipient list |
| 3. **Before changing anything else:** export SYS-G1, PLM, gateway, virtual desktop, and SYS-D4 tenant audit logs to the evidence store; snapshot affected cloud resources; image the engineer's laptop (EDR isolation); start chain of custody | Group SOC with the forensic firm | Hashes recorded |
| 4. Start the clocks on the bridge: Hour 0 for DIBNet (each division and the CSP role), and the time for the disclosure committee (24 hours) | Incident commander | Clock sheet signed by each division lead |
| 5. Call the cyber insurer; engage counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 6. Tell Prime A and Prime D security contacts (tenant agreements set 72 hours; sooner is better, because each prime has its own 72-hour DoD clock) | Defense Software customer operations director | Acknowledged |
| 7. Brief the Group CISO; convene the disclosure committee within 24 hours (POL-03 4.7) | Group CISO | Committee convened |
| 8. Tell plants and centers that operations continue (P05: no availability impact); hold new GCEE exports from affected projects | Division liaisons | Confirmed |

## 5. Analysis (RS.AN)
1. **Review for compromise of covered defense information** (252.204-7012(c)(1)(i)): identify compromised accounts, systems, and specific data, and check other systems the session could reach (gateway, CUI suite mailbox, HPC link).
2. **File list by owner.** From PLM, gateway, and virtual desktop logs, list every file the attacker opened or downloaded. Data owners map each file to program, contract, division, and prime. Program H files go to the Program H chief engineer first.
3. **Export status.** Empowered Officials mark each file ITAR, EAR, or no export control, and record where the data went (attacker infrastructure location, any sign of a foreign actor).
4. **Tenant data.** Defense Software lists the records exported from the Prime A and Prime D tenants and gives each prime its own list for its DoD report.
5. **Personal information.** The Group Chief Privacy Officer confirms the badging roster contents and counts affected individuals by state of residence (280 in Florida, 360 in 5 other states).
6. **Espionage indicators.** The facility security officers and counsel decide whether the facts suggest possible espionage, which triggers a prompt FBI report under 32 CFR 117.8(b) for the cleared entity.
7. **Root cause:** push MFA defeated by a relayed sign-in; single sign-on reaching both the GCEE and customer tenants; group-wide download thresholds. Feed to P01 GR-01, ES-001, ES-016.

## 6. Containment and eradication (RS.MI)
1. Confirm every attacker session is revoked across SYS-G1, the virtual desktop service, the CUI suite, and SYS-D4. Re-register authenticators for affected users with hardware keys.
2. Remove any attacker-created mailbox rules, app consents, registered devices, or tokens.
3. Tighten conditional access for field engineers: compliant device required, shorter session lifetime off company networks, block sign-in from hosting providers.
4. Rebuild the engineer's laptop from the standard image **only after the image is captured and hashed**.
5. Apply a temporary Program H download baseline at once (accelerates POAM-013).
6. **Preservation (252.204-7012(e)):** keep images and relevant monitoring and packet capture data for at least 90 days from each DIBNet report, and longer if DoD asks. Ask cloud provider A and the SYS-D4 platform team to preserve their logs. Malicious software, if isolated, goes to DC3 (252.204-7012(d)).

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (28 rows).** Counsel approves every external notice, except that a DoD report is never delayed for review. The matrix has four layers:
1. **DoD reports by contract holder:** Aircraft Parts and Engineering Services each file on DIBNet under their own contracts, with cross-references. Defense Software meets the paragraph (c) to (g) duties as a CSP for the SYS-D4 tenants. Each division sends the DoD incident report number to its primes for subcontract data (252.204-7012(m)(2)(ii)).
2. **Customers:** Prime A and Prime D under the SYS-D4 tenant agreements, so they can file their own reports.
3. **Export, NISPOM, and law enforcement:** Empowered Officials' disclosure decisions; FBI and DCSA for possible espionage; CISA voluntarily.
4. **SEC and employees:** materiality and Form 8-K; state breach notices for the 640 employees.

| When (from Hour 0) | Action | Owner |
|---|---|---|
| Hour 0 to 4 | Clocks started; insurer, counsel, forensics engaged; Prime A and Prime D told (out of band) | Incident commander; Group Chief Risk Officer; Defense Software customer operations director |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Promptly (when the facts suggest possible espionage) | Phone report to the FBI field office, followed in writing; notify DCSA with a copy | Engineering Services facility security officers |
| **Within 72 hours of discovery** | **DIBNet reports**: Aircraft Parts contracts; Engineering Services contracts; Defense Software for the CSP role (with Prime A and Prime D filing their own). Report what is known; update later | Division certificate holders. **Until POAM-012 closes, Defense Software has no one who can file its CSP report; the primes' reports and the Engineering Services report carry the facts, and counsel records the gap. This is why POAM-012 is due before the tabletop** |
| As soon as practicable after each report | DoD incident report numbers to Primes A to D for affected subcontracts | Division contracts leads |
| Immediately after the Empowered Official concludes a violation may have occurred | Initial voluntary disclosure to DDTC; full disclosure within 60 calendar days (22 CFR 127.12(c)); EAR self-disclosure decision (15 CFR 764.5) | Division Empowered Officials with export counsel |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 30 days of determination | Florida notices to the 280 Florida residents (Fla. Stat. 501.171(4)). No Department notice (fewer than 500 Florida residents) and no consumer reporting agency notice (640 in total, not more than 1,000). Other states: apply each state's law the same way | Group Chief Privacy Officer with counsel |
| On request | DoD access for forensics and damage assessment (252.204-7012(f), (g)) | Division contracts leads |

**Plan to the shortest clock.** In this scenario the order is: tenant notices to the primes (they have their own 72-hour clock), the disclosure committee (24 hours), the DIBNet reports (72 hours), any SEC filing (4 business days after the determination), then the 30-day employee notices. Draft DIBNet reports in parallel with analysis.

**Materiality factors for the disclosure committee:** which programs and how many (Program H is a high-priority program); effect on CMMC status and award eligibility (the C3PAO window is weeks away); prime and DoD customer reactions; Defense Software customer contracts and churn; regulatory exposure (DoD, DDTC, state attorneys general); cost of response. Materiality is decided without unreasonable delay; the 4-business-day clock starts at the determination, not at discovery.

**Extortion:** if the attacker demands payment not to publish the data, no payment without the board audit and risk committee, counsel, the insurer, and an OFAC sanctions check (POL-03 4.9). Paying does not remove any reporting duty.

## 8. Recovery (RC.RP, RC.CO)
Exfiltration rarely takes systems down, so recovery is about trust. Restore or confirm in BIA priority order (P05):
1. SYS-G1: sessions revoked, authenticators re-registered, conditional access tightened (BP-G01)
2. Hub and gateway blocks in place (BP-G03)
3. SOC monitoring with the new Program H baseline (BP-G02)
4. SYS-D4 tenant access for group engineers re-approved by each prime (BP-DS02)
5. GCEE: affected projects reviewed; exports from affected projects resumed after data owner sign-off (BP-AP03)
6. Engineering Services field operations with re-issued laptops (BP-ES04)

**Validate before closing:** 14 days without attacker activity, alerts tuned, and the preserved evidence set complete. Tell primes and affected tenants when containment is complete (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of containment; documented within 30 days (POL-03 4.12).
- Update P01 (GR-01, GR-07, ES-001, ES-016, DS-004), the POA&M (POAM-012, POAM-013, POAM-019), the SSP, and this runbook.
- Check whether the C3PAO assessment scope, SPRS information, or the CMMC affirmation needs updating because of control changes (POL-01 4.11).
- Consider the Reg S-K Item 106 description for the next annual report.
- Keep incident records for at least 6 years (POL-01 4.13), and the 252.204-7012(e) evidence for at least 90 days from each report or longer if DoD asks.

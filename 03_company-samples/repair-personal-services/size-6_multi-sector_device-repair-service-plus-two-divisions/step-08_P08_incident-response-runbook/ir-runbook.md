# Incident Response Runbook: Customer Device Data Exposure and Point-of-Sale Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Other Services (except Public Administration) (focus division: Device Repair) |
| Incident type | A compromised update of a third-party bench diagnostic tool exposes customer device data and STPP ticket data at repair benches across two divisions, and reaches retail POS lanes through in-store repair counter networks (point-of-sale compromise) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-10 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The cross-division notification matrix has not been exercised** (scenario gap 8); the first cross-division tabletop, using this scenario, is due 2026-12-15 (POAM-011) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (supply chain):** an attacker compromises the update server of a vendor whose device backup and data transfer tool runs on bench workstations. A signed-looking but malicious update installs itself on Day -9 on about 4,100 bench workstations (repair stores, in-store counters, 3 depots) and about 600 IT Support field laptops. Nothing checks the update's integrity (P07 SI-07a.[01]; POAM-008).
- **Device data exposure:** for 9 days the tool copies the backups it makes of customer devices (messages, photos, contacts, health and location data, saved credentials) to an attacker server: about 61,000 devices at repair benches and about 2,300 devices during IT Support in-home visits. IT Support technicians also ran the tool on 37 workstations at 14 medical and dental practices.
- **Ticket data exposure:** the malware reads the STPP session in the bench browser and pulls ticket notes for the user's region: about 380,000 tickets, about 9,800 of them with account email and password pairs and most with device passcodes (P07 AC-03; POAM-002).
- **Point-of-sale compromise:** at 41 of the 112 retail stores where in-store counter benches can reach POS lanes (P07 SC-07a.[04]; POAM-009), the attacker moves from a counter bench to lanes and installs memory-scraping malware for 6 days: about 210,000 payment card numbers with expiration dates (encryption at the PIN pad is not a validated P2PE solution, so lanes see card data in memory).
- **Day 0:** EDR flags an unknown process on lanes at 3 stores; the same morning a threat intelligence advisory names the tool vendor. The SOC declares Severity 1.
- **Forensic estimate at Day 5:** about 58,000 Device Repair customers with device content exposed and about 380,000 with ticket data exposed (overlapping) in 26 states (about 31% in Florida); about 210,000 retail card numbers (about 64,000 Florida cardholders); about 2,300 IT Support consumer customers; possible ePHI at 14 practices. Device Repair's P2PE terminals and booking page are not affected.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC, endpoint, and network teams | Forensic firm on retainer (through the insurer's panel); a PCI Forensic Investigator if the acquirer requires one | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| Device Repair decisions | Device Repair CISO with the chief operating officer | Device Repair vice president of partner programs (manufacturers, TPA) | Division bridge |
| Retail payment decisions | Electronics Retail CISO with the payments director | Electronics Retail chief operating officer | Division bridge |
| IT Support customer and HIPAA notices | IT Support Privacy Official and security and compliance lead | IT Support managed services director | Division bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; U.S. Secret Service (card data); CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read anything a compromised bench or field laptop can reach. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts, this runbook, and the notification matrix.

## 2. Preparation checks (Identify / Protect)
- [x] EDR on all benches, lanes, and field laptops, with remote isolation (SI-3; P07 satisfied)
- [x] Immutable STPP backups in provider B (CP-9; P07 satisfied)
- [x] Forensic retainer and insurer panel confirmed; acquirer contacts in the binder
- [x] Disclosure committee charter includes cybersecurity materiality
- [ ] Bench tool updates checked for integrity before they run (**gap until POAM-008 closes**)
- [ ] In-store counter benches separated from POS lanes at all 112 stores (**gap until POAM-009 closes**)
- [ ] Passcodes and account passwords out of ticket notes (**gap until POAM-002 closes**)
- [ ] Bench session and USB telemetry in the SIEM, so the SOC can tell which devices a bench touched (**gap until POAM-003 and POAM-006 close**)
- [ ] Notification matrix complete with manufacturer, TPA, enterprise, and customer clocks, and exercised (**gap until POAM-011 and POAM-012 close**)

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Unknown process or memory scraping indicators on a POS lane | EDR; retail SOC rules | Declare Severity 1; isolate lanes through EDR without powering them off |
| Advisory or vendor notice that a bench tool's update channel was compromised | Threat intelligence; vendor | Block the tool's update domains at all store firewalls; hunt for the update hash |
| Common point of purchase notice from an acquirer | Acquirer | Declare Severity 1; the 24-hour acquirer clock has already started at suspicion |
| Bulk ticket note reads from bench sessions | STPP audit logs in the SIEM | Revoke STPP sessions for the region; start triage |
| A customer, manufacturer, or practice reports misuse of data it believes came from the group | Contact center; partner contacts | Treat as a potential breach; open an incident |

**Severity 1** (group scale, POL-03 4.2): confirmed malicious code on benches or lanes in more than one store, or data of more than one division involved.

**Record the clock starts for each entity** (POL-03 4.3): the time each merchant first suspected a card compromise (acquirer clocks); the date each division determined a breach or had reason to believe one occurred (state law clocks); and IT Support's discovery date (164.410(a)(2)). Because the group SOC is corporate, **this runbook conservatively treats the SOC's Day 0 as the start for every division.** Counsel may refine this; no clock is planned from a later date.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected lanes through EDR; keep memory and disks for forensics; switch affected stores to lanes at unaffected registers or to the processor's standalone terminals | Electronics Retail CISO; SOC | Lanes isolated; stores still selling |
| 2. Block the tool's update domains and quarantine the tool on every bench and field laptop through EDR; stop all data transfers group-wide | Device Repair CISO; IT Support security lead | Quarantine report shows 0 running instances |
| 3. Cut in-store counter bench networks from store networks at all 112 failing stores (counters switch to paper intake and cellular-connected tablets) | Group network director | Firewall changes confirmed |
| 4. Revoke all STPP sessions; force re-authentication; disable bench accounts that ran the tool | Group identity director | Sessions revoked |
| 5. Snapshot affected benches, lanes, and field laptops for forensics; place STPP, EDR, and firewall logs on legal hold | SOC; forensic firm | Evidence list signed |
| 6. Quarantine customer devices that were connected to an affected bench and are still in custody; do not wipe or return them until counsel releases them (POL-03 4.9) | Device Repair chief operating officer | Devices tagged in the evidence cage |
| 7. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 8. Notify the retail acquirer (within 24 hours of suspicion), Manufacturers A and B (24 hours), and the TPA (48 hours), using counsel-approved holding language | Division owners per the matrix | Notices logged |
| 9. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.6) | Group CISO | Committee convened |

## 5. Analysis (RS.AN)
1. **Scope by bench.** Use EDR and firewall logs to list every bench and field laptop that ran the malicious update, and when. **Gap:** without bench session records (POAM-003), the list of customer devices connected to each bench comes from STPP ticket timestamps and the tool's own job logs, which is slower and less exact.
2. **Scope by ticket.** Use STPP audit logs to list tickets whose notes were read from affected sessions. Classify each ticket by what the notes held: passcode, account email and password, card number (historical notes; POAM-022), or none.
3. **Scope by card.** The forensic firm (or the PFI) identifies lanes with scraper activity and the exposure window. The acquirer receives the card number list through its secure process.
4. **Scope by practice.** IT Support lists practice workstations the tool ran on and works with each practice to determine whether ePHI was copied. Run the four-factor assessment (164.402) with each practice's input; each practice makes its own breach determination.
5. **Individuals by state and by division.** Produce counts of affected individuals by state of residence for each notifying division. They drive Department, attorney general, and consumer reporting agency notices.
6. **Good-faith access is not the question here.** The Florida exclusion for good-faith employee access (501.171(1)(a)) does not apply: the access was by an attacker.
7. **Root cause:** the unverified update channel, administrator rights on benches, the counter network path to lanes, and credentials in ticket notes. Feed these to P01 GR-02, GR-04, and GR-05.

## 6. Containment and eradication (RS.MI)
1. Rebuild every affected bench and field laptop from a clean gold image without the tool; reinstall the tool only after the vendor provides a verified clean version and the review gate approves it (POAM-008).
2. Rebuild affected lanes from the retail gold image; rotate store and lane credentials; retest segmentation before reconnecting counters (POAM-009).
3. Purge passcodes and account passwords from the notes of affected tickets at once; accelerate the full purge (POAM-002).
4. Confirm with forensics that no persistence remains in SYS-G1, the STPP, the payment switch, or the RMM before reconnecting.
5. Confirm that IT Support's RMM did not distribute the tool to managed customers' endpoints (the tool is not in the RMM catalog; verify).

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (29 rows).** Counsel approves every notice. The matrix has four layers:
1. **Contract clocks first:** the retail acquirer (24 hours from suspicion), Manufacturers A and B (24 hours), the TPA (48 hours), enterprise depot customers and managed services customers (72 hours after confirmation), and the practices' BAAs (5 business days for 47 practices; 10 calendar days otherwise). These are the shortest clocks in this incident.
2. **Third-party agent duties:** Device Repair to the TPA for plan holders' records, and IT Support to managed customers, no later than 10 days after determination in Florida (501.171(6)(a)), and earlier where the contract says so.
3. **Each division's own duties as the covered entity for its customers:** notices to individuals, the Florida Department of Legal Affairs (500 or more Floridians), consumer reporting agencies (more than 1,000 at a time), and every other state's equivalents, for Device Repair customers, retail cardholders, and IT Support consumer customers.
4. **Group duties:** SEC materiality and, if material, Form 8-K Item 1.05.

| When (from Day 0) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, forensics engaged; internal notice to all three divisions on the bridge | Group Chief Risk Officer; incident commander |
| Within 24 hours of suspicion | Retail acquirer notice; Manufacturer A and B notices | Electronics Retail payments director; Device Repair partner programs |
| Day 0 to Day 1 | Voluntary report to FBI or U.S. Secret Service and CISA; vendor coordination | Group CISO |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 48 hours | TPA notice | Device Repair partner programs |
| Within 72 hours of confirmation | Enterprise depot customers; managed services customers | Device Repair depot operations; IT Support managed services |
| Within 5 business days or 10 calendar days of discovery (by BAA) | Notice to the 14 practices with the identity of affected individuals where known (164.410(c)(1)) | IT Support Privacy Official |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days of determination | Third-party agent notices to the TPA and to managed customers (Florida worked example) | Device Repair; IT Support |
| Within 30 days of determination | Florida individual notices (15 more days only with written good cause to the Department) and the Department notice (no extension); consumer reporting agencies without unreasonable delay. Apply each other state's law the same way | Each division with counsel |
| No later than 60 days after discovery | Outer limit for business associate notice under 164.410 (the BAAs are shorter) | IT Support Privacy Official |

**Plan to the shortest clock.** In this scenario the order is: acquirer and manufacturers (24 hours), TPA (48 hours), enterprise and managed customers (72 hours), practices (5 business days for 47 of them), SEC (if material), third-party agent and practice notices (10 days), then state notices to individuals and regulators (30 days in Florida).

**Materiality factors for the disclosure committee:** number of people affected across the three divisions; the sensitivity of device content (health, location, messages) and of account credentials; card brand assessments and acquirer actions; the risk of losing Manufacturer A authorization or the TPA contract; managed customers' and practices' own breaches; regulatory exposure (FTC, state attorneys general, HHS through the practices); notification and remediation costs; and effects on operations (counter networks cut, data transfers stopped). Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Customer messages.** Customers whose device content was exposed get specific guidance (change passcodes and account passwords, review account security). Customers whose account passwords were in notes are told to change those passwords at once, and the division offers to help at any store.

**Extortion decision:** if the attacker threatens to publish device content, the board risk committee, counsel, insurer, and an OFAC sanctions check decide (POL-03 4.7). Paying does not remove any notice duty.

## 8. Recovery (RC.RP, RC.CO)
Restore in this order (P05 recovery priorities):
1. Identity and network controls confirmed clean (BP-G01, BP-G03, BP-G04)
2. Retail checkout (BP-ER01) on rebuilt lanes, after the PFI or forensic firm agrees and segmentation is retested
3. Repair intake and release (BP-DR01) and repair payments (BP-DR02); the STPP itself was not encrypted, so it stays up with re-authentication
4. Managed services (BP-IT01), after confirming the RMM was not used
5. Bench diagnostics and repair (BP-DR03) on rebuilt benches with the tool removed; manufacturer tools only until the review gate approves replacements
6. In-store counters reconnected only on separated networks (POAM-009)
7. Data transfers and data recovery (BP-DR07) resume last

Tell customers, manufacturers, the TPA, practices, and business accounts when services are restored (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- Update P01 (GR-02, GR-04, GR-05, DR-001, DR-004, DR-005, ER-001), the POA&M (POAM-002, POAM-003, POAM-008, POAM-009), the notification matrix, and this runbook.
- Brief Manufacturer A before its program audit and the QSA before ROC fieldwork.
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain all incident records for 6 years (POL-01 4.11).

# Incident Response Runbook: Point-of-Sale and Reservation System Compromise Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Accommodation and Food Services (focus division: Hotels) |
| Incident type | Point-of-sale and reservation system compromise: card-capturing malware through the shared legacy POS vendor at hotel outlets and park kiosks, plus a stolen CRS integration credential used to read the guest profile hub (SYS-G5), including owners' bank account data |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel; card brand and acquirer steps owned by the Group Director of Payments and PCI Compliance |
| Approved | 2026-09-10 by the Group CISO and the Group General Counsel |
| Last tested | Technical card compromise playbook tested 2026-03. **The multi-regulator notification matrix has not been exercised** (scenario gap 8); the first cross-division tabletop is due 2026-12-15 (POAM-008, POAM-009) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** an attacker compromises the legacy POS vendor's support environment and uses the vendor's always-on remote tool (P07 MA-4 finding) to install memory-scraping malware on legacy POS servers at **23 hotels** (8 owned or leased; 15 managed for 11 ownership groups) and on the kiosk servers at the **2 Florida theme parks** (96 kiosks and carts).
- **Pivot:** on a hotel POS server the attacker finds the cached CRS integration credential (P07 IA-5 finding) and uses it from the interface services to read the guest profile hub, which that credential can read in full (P07 AC-6 finding).
- **Dwell:** malware runs for 19 days; hub queries run for the last 4 days.
- **Detection (Day 0, a Monday, 02:10):** the SOC's volume rule fires on bulk reads by the CRS integration account. By Day 0 evening, forensics finds the malware on the source POS server.
- **Forensic estimate at Day 6:**
  - about **410,000 card numbers** with track data (hotel outlets about 265,000, of which about 170,000 at managed hotels; park kiosks about 145,000);
  - about **3.4 million guest profiles** read (names, contact details, loyalty numbers, stay and visit history), about **520,000 with identity document numbers** (about 118,000 Floridians);
  - the payment preferences table: **212,000 owners' bank account and routing numbers** (about 64,000 Floridians), of whom about **151,000 are loan customers of the finance subsidiary**;
  - no access to SYS-G4 (card vault), the kids' club store, the gate vendor, ride control, or loan origination.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC, network, and identity teams | Forensic firm on retainer (insurer panel); a PCI Forensic Investigator if Visa requires one | SOC bridge |
| Card brands and acquirers | Group Director of Payments and PCI Compliance | Hotels division payments and systems director | Payments bridge |
| Managed hotel owners | Hotels senior vice president of owner relations | Group General Counsel | Owner liaison line |
| FTC Safeguards Rule decision | Qualified Individual (Vacation Ownership security and compliance lead) | Finance subsidiary compliance officer | Division bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Group Chief Privacy Officer | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group Chief Financial Officer | Committee call |
| Operations | Hotels chief operating officer; Attractions vice president of park operations | Division continuity leads | Division bridges |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | U.S. Secret Service field office (named in Visa WTDIC); FBI field office or IC3 | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email and the vendor's ticketing system. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts, this runbook, the notification matrix, and the list of 41 ownership groups with their notice contacts.

## 2. Preparation checks (Identify / Protect)
- [x] Card vault and tokenization (SYS-G4) isolated in their own CDE account (P04; tested in the 2026 service provider ROC)
- [x] 24x7 SOC with EDR on hotel and park workstations and servers (SI-3, SI-4)
- [x] P2PE at 142 hotel outlets, 71 front desks, and 334 park points of sale (not exposed to memory scraping)
- [ ] Legacy POS vendor access through group PAM (**gap until POAM-001 closes**)
- [ ] Legacy POS and Vacation Ownership legacy logs in the SIEM (**gap until POAM-006 closes**)
- [ ] CRS integration credential rotated, scoped, and removed from POS servers (**gap until POAM-003 and POAM-013 close**)
- [ ] Owners' bank data out of the guest profile hub (**gap until POAM-013 closes**)
- [ ] Notification matrix exercised with owners, acquirers, the FTC step, and the disclosure committee (**gap until POAM-008 and POAM-009 close**)
- [x] Forensic retainer and insurer panel confirmed; QSA firm excluded from PFI selection (Visa WTDIC A.5.3)

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Bulk or unusual reads by an integration or service account | SIEM, database activity monitoring on SYS-G5 | Disable the account; start triage; declare Severity 1 if Restricted data is involved |
| Common point of purchase or fraud alert from an acquirer or card brand | Acquirer A, B, or C; owner's acquirer | Declare Severity 1; open the payments bridge |
| Malware, unknown process, or memory scraper on a POS server | EDR (where present), vendor anti-malware alert, forensic triage | Isolate the segment; preserve memory |
| Unscheduled vendor remote session | PAM, network monitoring at the payment segment boundary | Block the vendor tool at the property edge; call the vendor out of band |
| Extortion message or data on a leak site | Email, threat intelligence, law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): confirmed or suspected card data compromise, or Restricted data of more than one division involved.

**Record each clock's start date** (POL-03 4.3):
- **Card brands and acquirers:** reasonable suspicion of a compromise event (Day 0 evening, when malware is found).
- **FTC Safeguards Rule:** discovery is the first day the event is known to any employee, officer, or other agent of the finance subsidiary (314.4(j)(2)). The group SOC monitors the division, so **Day 0** is the discovery date. Unauthorized access to unencrypted customer information is presumed to be acquisition unless reliable evidence shows otherwise (314.2).
- **Florida and other states:** the date of determination of the breach or reason to believe one occurred (Florida 501.171(4)(a)); counsel records it (Day 6 in this scenario, when the scope is known).
- **SEC:** the date the disclosure committee determines materiality.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Disable the CRS integration account and revoke its keys; switch PMS and POS loyalty lookups to a degraded mode (no loyalty recognition) | Group identity director | Account disabled; lookups failing safely |
| 2. Block the legacy POS vendor's remote tool at every property edge and at the hubs (25 sites, 2 divisions); notify the vendor out of band | Group network director | Rule pushed and verified at all sites |
| 3. Isolate legacy POS segments at 23 hotels and 2 parks from the interface services; keep P2PE terminals and cloud POS running | Group network director with division operations | Segment isolation confirmed |
| 4. Capture memory and disk images from 3 representative POS servers before any rebuild; place logs on legal hold | SOC; forensic firm | Evidence list signed |
| 5. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 6. Notify Acquirers A and B **immediately**; start Visa's 3-day clock (WTDIC A.1.1, A.3.1) | Group Director of Payments and PCI Compliance | Acquirer acknowledgments logged |
| 7. Notify owners of the 15 managed hotels within 24 hours (POL-03 4.4) | Hotels senior vice president of owner relations | Each owner acknowledges |
| 8. Brief the Qualified Individual and the finance subsidiary president: owners' bank data was read | Incident commander | Acknowledged on the bridge |
| 9. Escalate to the disclosure committee within 24 hours (POL-03 4.7) | Group CISO | Committee convened |
| 10. Tell operations what still works: P2PE outlets and front desks, PMS, CRS bookings, gates, rides | Division liaisons | Operations confirm |

**Operations during containment.** The 72 legacy outlets at 23 hotels and 96 park kiosks switch to standalone P2PE terminals from the spares pool, or cash and room charge, as the BIA downtime procedures allow (P05 BP-H03, BP-A03). Loyalty recognition is unavailable until the credential is replaced (BP-G06, Moderate).

## 5. Analysis (RS.AN)
1. **Card scope.** The forensic firm (or the PFI) sets the window of exposure per site from malware timestamps. The Group Director of Payments and PCI Compliance pulls the card numbers processed at each site in the window and provides at-risk accounts to Visa within 3 calendar days (WTDIC A.4.1), through each acquirer.
2. **Owner scope.** For each managed hotel, list the owner, its acquirer, the card count, and any guest profile data tied to that hotel. The owner is the merchant of record and needs these facts for its own notices.
3. **Hub scope.** Use database audit logs to list tables and rows read. Map each record to the division that collected it (purpose tags, POL-04 4.4). Separate:
   - finance subsidiary loan customers among the 212,000 owners (Safeguards Rule customer information);
   - identity document numbers (state breach laws in nearly every state);
   - bank account numbers without a code (counsel decides state by state; in Florida, a financial account number counts only with any required security code, access code, or password);
   - contact and loyalty data only (generally not a notice trigger alone, but used for fraud warnings).
4. **Individuals by state** for each population, from loyalty and owner records; billing ZIP codes for walk-in guests where no residence is on file.
5. **What was not reached:** confirm SYS-G4, the kids' club store, the gate vendor's template store, ride control, and loan origination were not accessed (this changes several matrix rows to "not triggered").
6. **Root cause:** the vendor's always-on tool, no EDR on legacy POS servers, a cached broad credential, and bank data where it did not belong. Feed these to P01 GR-01 and GR-02.

## 6. Containment and eradication (RS.MI)
1. Rebuild every legacy POS server from vendor gold images under SOC supervision, or retire it early in favor of P2PE terminals (accelerates the 2027-06-30 replacement).
2. Reconnect the vendor only through group PAM with named accounts, per-session approval, and recording (POAM-001, done as an emergency change).
3. Issue a new CRS integration credential scoped to loyalty fields, stored only in the secret store, never on POS servers (POAM-003, POAM-013).
4. Move owners' bank data out of the hub to the tokenized store in SYS-V3 before loyalty lookups are restored.
5. Hunt across SYS-G1, the interface services, and both divisions' networks for persistence before reconnecting segments.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (33 rows).** Counsel approves every notice. The matrix has four layers:
1. **Card ecosystem (contractual):** Acquirers A and B immediately; Visa within 3 calendar days of suspicion, the incident report 3 days after that, and at-risk accounts within 3 days; PFI steps if Visa requires one; other brands through the acquirers.
2. **Owners (contractual and as service provider):** each owner of an affected managed hotel within 24 hours, with the facts for the owner's own acquirer notice. Owners' associations for the autopay data.
3. **Regulators and individuals:** the FTC within 30 days of discovery for the finance subsidiary; state notices to individuals, attorneys general, and consumer reporting agencies under each state's law (Florida worked example).
4. **Investors:** the disclosure committee's materiality decision and, if material, Form 8-K Item 1.05.

| When (from Day 0) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, forensics; acquirers notified immediately on suspicion; vendor contacted out of band | Group Chief Risk Officer; Group Director of Payments and PCI Compliance |
| Day 0-1 | Owners of the 15 managed hotels (24 hours); law enforcement (U.S. Secret Service or FBI, recommended by Visa WTDIC); disclosure committee convened | Owner relations; Group CISO; Group General Counsel |
| Within 3 calendar days of suspicion | Visa notification (A.1.1); at-risk accounts as soon as a window of exposure is set (A.4.1) | Group Director of Payments and PCI Compliance |
| Within 3 calendar days of the Visa notice | Incident report to Visa and the acquirers (A.2.1) | Group Director of Payments and PCI Compliance |
| Within 5 business days | Owners' associations notified (fictional agreement term) | Vacation Ownership vice president of association management |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 10 days of the agent's determination | Florida third-party agent notices: the division to owners (outbound); the legacy POS vendor to the group (inbound) | Group General Counsel |
| Within 30 days of discovery (Day 30) | FTC notice for the finance subsidiary (about 151,000 consumers) | Qualified Individual with counsel |
| Within 30 days of determination (Day 36) | Florida individual notices and Department of Legal Affairs notice (500 or more Floridians); consumer reporting agencies without unreasonable delay. Apply each other state's law the same way | Each affected entity with counsel |

**Who notifies individuals.** Each legal entity notifies the people whose data it holds: Hotels for hotel guests at owned hotels; owners (or the division as their agent, if the owner agrees in writing) for guests of managed hotels; Attractions for park visitors; Vacation Ownership and the finance subsidiary for owners. Coordinated letters to people in more than one population name every entity involved.

**Plan to the shortest clock.** In this scenario the order is: acquirers (immediately), owners (24 hours), Visa (3 days), the SEC (if material), Florida agent notices (10 days), the FTC (Day 30), then the state 30-day notices from determination.

**Materiality factors for the disclosure committee:** card brand assessments and fraud costs across three acquirers and the owners' acquirers; regulatory exposure (FTC Safeguards Rule and Section 5, state attorneys general); owner claims under the management agreements; loyalty and owner trust; operating effects at 25 sites; and remediation cost. Materiality is decided without unreasonable delay; the 4-business-day clock starts at the determination, not at discovery.

**Extortion decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.9). Paying does not remove any notice duty when data was taken.

## 8. Recovery (RC.RP, RC.CO)
Restore in the BIA order (P05):
1. SYS-G1 confirmed clean; new CRS integration credential issued (BP-G01)
2. Group payment services confirmed unaffected (BP-G05)
3. Park POS and hotel outlets: P2PE terminals first; rebuilt legacy servers only after forensic sign-off (BP-A03, BP-H03)
4. Guest profile hub lookups restored with the scoped credential, after bank data is removed (BP-G06)
5. Owner portal and autopay confirmed unaffected; owners told how to watch their accounts (BP-V04)

Tell owners, guests, and staff when services are restored (RC.CO). The Hotels division updates each owner's responsibility matrix if the incident changed any responsibility.

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.12).
- Update P01 (GR-01, GR-02, GR-03, GR-18), the POA&M (POAM-001, POAM-003, POAM-006 to POAM-009, POAM-013), the notification matrix, and this runbook.
- The Qualified Individual reports the event and the response to the finance subsidiary board (314.4(i)) and revises the incident response plan (314.4(h)(7)).
- Expect the acquirers and the QSA to revisit the Hotels and Attractions validations; the legacy POS compensating controls will not survive this scenario.
- Consider the Reg S-K Item 106 description for the next annual report.

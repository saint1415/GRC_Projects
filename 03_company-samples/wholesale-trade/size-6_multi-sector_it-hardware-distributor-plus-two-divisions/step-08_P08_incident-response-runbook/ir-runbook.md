# Incident Response Runbook: Supplier Compromise Introducing Tampered Products Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Wholesale Trade |
| Incident type | A supplier is compromised or dishonest, and tampered, counterfeit, or covered (Section 889) products enter group DCs and reach resellers, DoD integration jobs, and consumers. Includes supplier systems or accounts used to push altered shipping or product data into group systems |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); supply chain practices from NIST SP 800-161 Rev. 1 |
| Policy basis | Group POL-03 Incident Response Policy; POL-01 4.10 to 4.13 (supply chain); division supplements (P06) |
| Runbook owner | Group CISO (cyber side) with the Group supply chain risk director (product side); notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The cross-division notification matrix has not been exercised** (scenario gap 10); the first cross-division tabletop is due 2026-12-15 (POAM-003) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** attackers compromise **Supplier K**, a regional authorized distributor for a networking OEM and a consumer mesh router OEM. They reflash firmware on units in Supplier K's warehouse with an implant, reseal the boxes, and use Supplier K's EDI account to send advance ship notices whose serial lists match the units.
- **Receipt (Day -21 to Day -14):** Logistics receives 1,150 switches at DC-6 and 6,400 mesh routers at DC-3. DC-6 validates OEM serials, which pass because the serials are genuine; DC-3 does not validate serials (P07 SR-10, POAM-012). Nothing checks firmware at receiving.
- **Sale:** IT Distribution sells 820 switches to 37 resellers and allocates 96 to two Prime D integration jobs at IC-2. Online Retail sells about 2,900 routers to consumers in 41 states (about 310 in Florida).
- **Detection (Day 0):** an IC-2 technician powers on a switch in the lab network to load a CUI configuration template. The SOC detects the device beaconing to an unknown domain. On Day 1 the OEM's product security team warns channel partners about tampered units shipped through Supplier K.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Product lead (quarantine, suppliers, OEMs) | Group supply chain risk director | IT Distribution vice president of purchasing | Product bridge |
| DC operations | Logistics vice president of operations | DC-3 and DC-6 general managers | Product bridge |
| DoD and prime reporting | Federal Solutions vice president (certificate holder) | Federal Solutions contracts director (certificate holder) | Out-of-band bridge |
| Consumer remediation | Online Retail president | Online Retail vice president of customer care | Division bridge |
| Notifications and legal | Group General Counsel with outside counsel (insurer panel; government contracts counsel) | Division counsel | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Cyber insurer | Primary carrier hotline | n/a | Policy card in the incident binder; call before engaging any incident vendor |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume Supplier K's email and EDI accounts are attacker-controlled. Never confirm anything with Supplier K by email or through numbers in a recent message; use the numbers on file in the ERP supplier master.

## 2. Preparation checks (Identify / Protect)
- [x] Quarantine cages at every DC dock and a "HOLD - DO NOT SHIP" status in the ERP and WMS
- [x] 24x7 SOC with EDR on FFE lab workstations and network detection at the FFE boundary (P07 SI-4 satisfied for IT)
- [x] Serial records for every integration job (SR-4)
- [ ] OEM serial validation at all 9 DCs (**gap until POAM-012 closes**; DC-3 has none)
- [ ] Firmware verification from OEM portals only (**gap**: 2 of 10 sampled jobs used supplier-portal hashes; POAM-012)
- [ ] Four DIBNet certificate holders in two locations (**gap until POAM-002 closes**)
- [ ] Notification matrix exercised across divisions (**gap until POAM-003 closes**)
- [ ] Manufacturer of record for every SKU (**gap until POAM-009 closes**), needed for the Section 889 check in section 5

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A device in an integration lab or a DC beacons, scans, or contacts an unknown domain | SOC network detection; EDR on lab workstations | Isolate the port; open an incident; pull the serial and lot |
| OEM or industry advisory about tampered or counterfeit units in the channel | OEM product security team; threat intelligence | Search the ERP and WMS for affected serials and suppliers; open a product incident |
| Serial validation fails, packaging is resealed, or labels and weights do not match | Receiving at any DC | Quarantine the lot; photograph; do not power on |
| Firmware hash or signature differs from the OEM portal value | Integration technicians | Stop the job; isolate the device; call the SOC |
| A supplier's advance ship notice or bank details change unexpectedly | EDI hub validation; Controller | Hold the receipt or payment; call back on the number on file |
| Customers report odd device behavior (unexpected traffic, failed updates) | Reseller support; Online Retail contact center | Open an incident; pull serial history |

**Severity 1** (group scale, POL-03 4.2): tampered or counterfeit products confirmed in more than one division, or any affected product connected to a CUI network or shipped to a DoD installation.

**Record when each clock starts** (POL-03 4.3):
- **DFARS 252.204-7012(c):** discovery of a cyber incident affecting a covered contractor information system. In this scenario that is **Day 0**, when the SOC saw the beacon from a device on the IC-2 lab network where CUI was loaded.
- **FAR 52.204-25(d):** identification of covered equipment (1 business day). FAR 52.204-23(c) and 52.204-30, where in the contract, use 3 business days. These run only if covered articles are identified.
- **Form 8-K Item 1.05:** the materiality determination, not discovery.
- **State breach laws:** determination of a breach of personal information, if any is found.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate the IC-2 lab segment from the FFE; keep the affected switch powered for imaging; stop all integration jobs that use Supplier K stock | Integration center managers; SOC | Lab segment isolated; jobs paused |
| 2. Stop ship: place every open order line for Supplier K SKUs and lots on hold in the ERP and WMS across all DCs and both selling divisions | Logistics vice president of operations | No affected item can be picked |
| 3. Quarantine remaining stock at DC-3 and DC-6 and any returns; keep packaging | DC general managers | Units counted and tagged |
| 4. Suspend Supplier K on the approved supplier list; disable its EDI and supplier portal accounts; freeze payments | Group supply chain risk director; Group integration director; Controller | Accounts disabled; payment hold confirmed |
| 5. Call the cyber insurer; engage counsel and forensics through the panel; engage government contracts counsel | Group Chief Risk Officer | Claim number issued |
| 6. Start the DIBNet report preparation (72-hour clock from Day 0) and confirm both certificate holders are reachable | Federal Solutions vice president | Draft report open; holders confirmed |
| 7. Escalate to the disclosure committee within 24 hours of declaration (POL-03 4.6) | Group CISO | Committee convened |
| 8. Tell divisions what continues: unaffected SKUs ship normally; DC operations are not stopped | Division liaisons | Operations confirm |

## 5. Analysis (RS.AN)
1. **Product scope.** List every Supplier K SKU, lot, serial, advance ship notice, receipt, and shipment since the earliest suspect receipt. Split by division: resellers (IT Distribution), integration jobs (Federal Solutions), consumers (Online Retail), returns, and any 3PL client stock (none in this scenario).
2. **Authenticity and firmware.** Send serials and firmware images to the OEM for validation. Compare firmware against the OEM portal values only. For integration jobs, arrange OEM or independent lab testing (DFARS 252.246-7008(b)(3)(ii)).
3. **Covered equipment check.** Confirm the true manufacturer of every affected SKU against the FAR 52.204-25 covered manufacturers, including rebranded units. Record who decided and why. In this scenario both OEMs are not covered, so no Section 889 report is due, but the check is documented.
4. **Cyber scope.**
   - Which IC-2 lab devices did the switch reach, and did the implant read or alter the CUI configuration template loaded onto it?
   - Did the attacker use Supplier K's EDI or supplier portal access to read group data (pricing, contacts, personal information)? Pull portal and EDI hub logs before they roll over.
   - Were any switches already installed at a DoD site? (In this scenario, none had shipped; both jobs were in staging.)
5. **Personal information.** Determine whether any group-held personal information was accessed. The routers in consumers' homes are a consumer safety and security issue, but they are not a breach of group-held data unless analysis shows group systems were accessed.
6. **Evidence.** Image the switch and affected lab workstations; preserve EDI messages with headers, packaging, and logs. Keep images and monitoring data at least 90 days from the DIBNet report (252.204-7012(e)), and submit any malware to DC3 as instructed (252.204-7012(d)).

## 6. Containment and eradication (RS.MI)
1. Rebuild affected IC-2 lab workstations from the standard image; rotate credentials and keys that were present on the lab network; reconnect the segment only after the SOC confirms no persistence.
2. Keep all suspect units; do not return them to Supplier K or scrap them until counsel, the OEMs, and Prime D give disposition instructions (POL-03 4.7).
3. Replace integration stock only from the OEM directly, with firmware verified from the OEM portal.
4. Block Supplier K SKUs on all channels until the Group supply chain risk director releases them in writing.
5. Remove any Supplier K access paths: EDI certificates, portal accounts, and API keys.
6. Warn buyers and the Controller about Supplier K lookalike domains and phone numbers.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (29 rows).** Counsel approves every external notice. The matrix has three layers:
1. **Inside the group:** every division reports to the group SOC within 1 hour (POL-03 4.1); the SOC runs one case for all divisions.
2. **Each division's outward duties:** Federal Solutions to DoD, primes, and contracting officers; IT Distribution to resellers and OEMs; Online Retail to consumers; Logistics to 3PL clients if their stock or data is affected.
3. **Group duties:** SEC materiality, the insurer, law enforcement, and state breach laws if personal information is involved.

| When (from SOC discovery, Day 0) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, and forensics engaged; internal reports from Logistics and IC-2 on the bridge | Group Chief Risk Officer; incident commander |
| Day 0 to 1 | Voluntary report to FBI or IC3 and CISA; notice to the OEM product security teams | Group CISO; Group supply chain risk director |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Day 1 | Section 889 check documented (not triggered); 3PL client check documented (not affected) | Federal Solutions vice president; Logistics |
| **Within 72 hours of Day 0** | **DIBNet cyber incident report**; then the incident report number to Prime D as soon as practicable; malware to DC3 as instructed | Federal Solutions vice president |
| Day 2 (counsel decision) | Written notice to the contracting officer through Prime D that 96 staged switches cannot be confirmed as unaltered (252.246-7008(b)(3)(ii)) | Federal Solutions vice president |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 2 business days of confirming serials | Reseller notices with serial lists and instructions | IT Distribution chief operating officer |
| When remediation is ready | Consumer security advisory and recall or replacement offer | Online Retail president |
| Within 60 days of awareness, if the clause applies | GIDEP report and contracting officer notice under FAR 52.246-26 (counsel decides whether tampered genuine units are suspect counterfeit) | Federal Solutions vice president |
| Within 30 days of determination, only if personal information was breached | State notices for each state where affected individuals reside (Florida worked example: individuals and, at 500 or more, the Department of Legal Affairs) | Group General Counsel |

**Plan to the shortest clock.** In this scenario the order is: internal reports (1 hour), disclosure committee (24 hours), DIBNet (72 hours from discovery), the SEC filing if material (4 business days from the determination), then customer and consumer notices. If a covered article had been identified, the FAR 52.204-25(d) report (1 business day) would come before DIBNet.

**Materiality factors for the disclosure committee:** units affected in three channels and recall cost (estimated $8 million to $11 million); the DoD relationship and the pause of integration work for Prime D (about $570 million a year of integration revenue depends on CMMC and prime trust); reseller and consumer trust; regulatory exposure (DoD, FTC, state attorneys general); and operational effects (limited: DCs kept shipping unaffected SKUs).

**Customer messages.** Tell resellers, primes, and consumers which serials they received, what is known, and what to do. Do not speculate in writing about Supplier K's fault. Scripts are approved by counsel.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05), adjusted for this incident:
1. Order capture and fulfillment for unaffected SKUs (BP-G05, BP-ID01, BP-LW02, BP-OR01): lift holds that do not involve Supplier K stock.
2. Receiving (BP-LW01): add firmware spot checks against OEM portal values at DC-3 and DC-6 for networking SKUs until POAM-012 closes.
3. Federal integration (BP-ID03): restart only after the lab rebuild, with OEM-direct stock and verified firmware, and after Prime D accepts the plan.
4. Online Retail replacements and returns (BP-OR06): use the Lifecycle Services sanitization method for returned routers.
5. Supplier K: resume only after it shows its systems are clean, bank details are confirmed by call-back, and the Group supply chain risk director re-approves it.

Tell resellers, primes, and consumers when replacements ship (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.11).
- Update P01 (GR-01, GR-05, ID-003, LW-005, OR-006), the POA&M (POAM-002, POAM-003, POAM-012), the C-SCRM plan, the notification matrix, and this runbook.
- Add firmware verification at receiving for networking SKUs to the 2027 budget (SI-7, planned in P02).
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain all incident records for at least 6 years (POL-01 4.15).

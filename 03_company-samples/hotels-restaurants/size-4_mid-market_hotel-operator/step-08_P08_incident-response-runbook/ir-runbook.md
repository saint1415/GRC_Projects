# Incident Response Runbook: Point-of-Sale and Reservation System Compromise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Florida hotel owner and operator: 2 independent resorts and 4 franchised select-service hotels) |
| Tier / Vertical | Mid-Market / Accommodation and Food Services |
| Incident type | Card data theft from the POS and reservation systems. Attackers enter through the Resort 2 POS vendor's always-on remote tool, install memory-scraping malware on the legacy Resort 2 POS workstations and server, use directory access from the POS VLAN to reach the corporate network, and capture card numbers keyed by CRO agents on their PCs. Usually discovered through an acquirer common-point-of-purchase (CPP) alert weeks after it starts (P01 R-001, Very High) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy (4.3 to 4.8) |
| Companion documents | `ir-runbook-ransomware.md` (ransomware with guest data theft); `notification-matrix.csv`; BIA (P05); hotel downtime and hurricane procedures |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Card compromise tabletop with breach counsel, the acquirer contact, and the franchisor's incident contact scheduled 2026-11-30 (POAM-009) |

## 0. Governance, roles, and contacts (Govern)
Three teams with separate decisions, so that technical work, hotel operations, and legal and contractual notice each have a clear owner.

| Team | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, IT Director, Vice President of Sales and Marketing, Corporate Communications Manager, HR Director, outside breach counsel | Business decisions (stopping card acceptance at an outlet, the CRO, or a hotel), external statements, guest remediation (call center, credit monitoring), budget |
| **Incident response team (IRT)** | Incident commander: Security Manager. IT Director (containment and recovery lead), security analyst, MSSP, forensic firm or PCI Forensic Investigator (PFI) through counsel, SYS-01, gateway, and Resort 2 POS vendor contacts | Containment, evidence, investigation, eradication, recovery order |
| **Hotel operations command** | Lead: the Resort 1 General Manager (named by the COO). The other 5 General Managers, both Resort Directors of Food and Beverage, both Resort Front Office Managers, Director of Central Reservations | Payment fallbacks at each outlet and front desk, CRO call handling, guest communication at the desk |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | IT Director | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Acquirer and card brands | Chief Financial Officer | Director of Finance | Acquirer risk line (incident binder) |
| Breach and notice decisions; decision log | General Counsel | Outside breach counsel | Out-of-band group |
| Legal counsel | Outside breach counsel (insurer panel) | Company's outside corporate counsel | Through the insurer hotline, then direct |
| Cyber insurer | Carrier breach hotline ($10 million limit, $250,000 retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm engaged by counsel; a PFI if Visa requires one (never the QSA firm that supports the SAQ D) | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 security operations center | Security analyst | MSSP hotline |
| Franchisor | Franchisor's incident contact (Hotels 3 to 6) | Franchisor regional IT contact | Numbers in the incident binder |
| Hotel owner (from 2027-01-01) | REIT asset management and legal contacts | n/a | Numbers in the management agreement |
| Communications | Corporate Communications Manager | Outside crisis PR (through counsel) | Out-of-band group |
| Board and sponsor | CEO informs the audit committee chair and the PE sponsor's board representative | COO | Phone |
| Law enforcement | U.S. Secret Service field office | FBI field office or IC3 | Numbers in the incident binder |

**Out-of-band first.** The attacker may be in the corporate directory and email. The CMT and IRT use a pre-provisioned messaging group on personal phones and the printed call trees kept at every front office, the CRO, and the corporate office.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from conclusions. Do not speculate in email or chat. A PFI report goes to the card brands and the acquirer, so assume it will not be privileged.

## 1. Preparation checks (Identify / Protect)
- [x] Incident binder at every front office, the CRO, and the corporate office: this runbook, call tree, notification matrix, merchant agreement and franchise agreement notice terms, downtime forms
- [x] EDR with 24x7 MSSP monitoring on 470 of 520 PCs, including all 22 CRO PCs (SI-3)
- [ ] EDR or allowlisting on the 38 Resort 2 POS workstations and the 50 Hotels 3 to 6 PCs. **Gap until POAM-014 closes (2027-01-31)**
- [ ] Resort 2 POS server, lock servers, and Hotels 3 to 6 logging to the SIEM with 12 months retention. **Gap until POAM-005 closes. Today the Resort 2 POS server keeps 30 days of logs, which may already have rolled over when a CPP alert arrives (R-041)**
- [ ] Vendor remote access only through the privileged access broker. **Gap until POAM-004 closes (2026-11-30)**
- [ ] Complete payment device list with serial numbers for all 120 devices (POAM-007, due 2026-10-31)
- [x] Insurer panel counsel and forensics confirmed; PFI list on the PCI SSC website bookmarked
- [ ] Loaner P2PE devices for Resort 2 outlets (POAM-010; budgeted, not yet bought)
- [ ] Out-of-band messaging group tested quarterly (first test 2026-10-15)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Acquirer or card brand names the company (or a MID) as a common point of purchase for fraud | Acquirer letter or call to the CFO | **Declare severity 1.** Record the time as the start of the acquirer 24-hour and Visa 3-day clocks |
| New remote session, new service, or unknown process on the Resort 2 POS server or workstations | Resort 2 Director of Food and Beverage; POS vendor; EDR once deployed | Isolate at the switch; call the incident commander |
| Directory sign-ins from the Resort 2 POS VLAN to corporate systems, or a new privileged account | SIEM (identity logs) | Disable the account; declare if unexplained |
| EDR alert on a CRO PC: keylogger, form-grabber, credential dumping, or an unknown browser extension | MSSP (call within 30 minutes) | MSSP isolates the PC; declare if more than one PC |
| Guest fraud complaints clustered on stays or CRO bookings | Front desks; Director of Finance; chargeback reports | Log each; escalate if 3 or more in 30 days from one channel |
| Large SYS-01 card display or profile export activity by one user | SYS-01 activity report (daily review due under POAM-005) | Disable the account; open an incident |

**Declare a card compromise incident (severity 1) when** there is evidence sufficient to raise a reasonable suspicion that card data or a payment system was accessed without authorization. Visa's 3-day clock starts at that point, not at confirmation.

**Record three times in the incident log (POL-03 4.3):** time of suspicion (acquirer, Visa, franchisor, and later the REIT owner clocks), time of declaration, and, later, the time the General Counsel determines a breach occurred or there is reason to believe one occurred (Florida 30-day clock, Fla. Stat. 501.171(3)(a) and (4)(a)).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Open the out-of-band channel and the incident log; declare severity 1 | Incident commander | Log open |
| 0-30 min | **Isolate, do not power off.** Unplug the Resort 2 POS server and workstations from the network at the switch, or block the POS VLAN at the firewall. Do not reboot, rebuild, or sign in with administrator credentials (Visa WTDIC). Isolate affected CRO PCs through EDR network containment | IT Director; MSSP | Hosts isolated and labeled |
| 0-30 min | Disable both vendor remote tools at Resort 2 at the firewall; revoke the POS vendor's and lock vendor's accounts | IT Director | No vendor path open |
| 0-60 min | Call the cyber insurer hotline **before** engaging any vendor; insurer assigns counsel; counsel engages forensics | CFO | Claim number; counsel on the call |
| 0-60 min | **Payment fallbacks.** Resort 2 outlets: room charge to the folio and cash only, until loaner P2PE devices arrive. CRO: stop taking card numbers by phone; send the guest a payment link from SYS-01 instead. Resort 1 outlets and both resort front desks (P2PE) keep trading after a quick device check. **Never write card numbers on paper** | Hotel operations command | Fallback running at each point of sale |
| 0-2 h | Ask the Resort 2 POS vendor, the SYS-01 vendor, the gateways, the SD-WAN provider, and the MSSP in writing to preserve logs, images, and session records | Security Manager | Written requests sent |
| 0-2 h | Revoke sessions for CRO and Resort 2 users in the identity provider; reset the passwords of any account used from the POS VLAN; review new or changed privileged accounts | Security Manager | Sessions revoked |
| 0-4 h | Convene the CMT; first situation report (what is known, channels affected, fallbacks, decisions needed) | CMT chair | Meeting held |
| 0-4 h | Notify the acquirer by phone (contract: 24 hours) and get a case number; agree how Visa and the other brands will be notified | CFO | Acquirer case number |
| 0-4 h | Scope check of Hotels 3 to 6: are their company PCs joined to the affected directory, and is there any sign of activity on their flat networks? If yes, the General Counsel notifies the franchisor (24 hours) | IT Director; General Counsel | Decision recorded in the decision log |
| 0-4 h | Staff briefing script for front offices, outlets, and the CRO: what to do, what not to say, report anything unusual | Corporate Communications Manager with HR | Script sent by text |
| Within 24 h | CEO informs the audit committee chair and the PE sponsor's board representative | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Window of exposure.** First and last date card data could have been captured on each channel: Resort 2 outlets (malware install date to containment), CRO (first malicious process on any CRO PC to containment). This decides which cards are at risk and is required by Visa (WTDIC). Missing Resort 2 logs make this harder; use EDR telemetry, vendor session records, POS application logs, and firewall logs from the SIEM.
2. **Entry point and spread.** Confirm the vendor tool as the entry point. Trace directory use from the POS VLAN, any new accounts, and the path to the CRO PCs. Check whether the attacker reached the call recording store, the 6 shared mailboxes with card forms (if not yet purged under POAM-013), or the SYS-01 card vault through stolen user sessions.
3. **Card data at risk, by channel.**
   - Resort 2 outlets: card numbers and expiration dates from memory on the POS workstations and server (magnetic stripe fallback transactions may include track data).
   - CRO: card numbers with expiration dates **and security codes**, plus guest names, keyed during phone payments (about 48,000 card-not-present numbers a year, or about 130 a day).
   - Recordings and mailboxes, if reached: card numbers with security codes.
   - Resort 1 and both resort front desks: validated P2PE, so card data should not be readable. Confirm device integrity and serial numbers against the device list.
4. **Personal information at risk (Florida and other states).** Guest names with card numbers and required security codes (CRO payments) are personal information under Fla. Stat. 501.171(1)(g)1.a. If the attacker reached SYS-01 through a stolen session, check for profile exports with ID document numbers. Build the **affected individuals list** by data element and state of residence. This drives every legal notice.
5. **Preserve evidence.** Forensic images of the Resort 2 POS server, a sample of POS workstations, and affected CRO PCs; memory captures before any shutdown; SIEM, EDR, firewall, identity, and vendor session exports, with chain of custody (who collected, when, hash, storage). Evidence is held by the forensic firm under counsel. If Visa requires a PFI, give the PFI full access.
6. **Vendor and franchisor status.** Ask the Resort 2 POS vendor whether other customers were reached through the same tool, and get its incident report. Confirm with the franchisor that brand systems at Hotels 3 to 6 show no related activity.

## 5. Containment and eradication (RS.MI)
1. Block attacker infrastructure at all 7 site firewalls, the SD-WAN, and the cloud firewall.
2. Remove the Resort 2 POS vendor tool permanently; vendor support returns only through the privileged access broker with named accounts, MFA, and per-session approval (POL-02 4.8; POAM-004).
3. Block all directory traffic from the POS VLAN (POAM-003). Reset the passwords of every privileged account, service account, and interface credential the attacker could have seen (POS to PMS, PMS to lock server, gateway portals). Reset the directory's Kerberos ticket-signing account twice, as the forensic firm directs.
4. Rebuild the CRO PCs from the standard image. **Do not clean and reuse them.** Rebuild the Resort 2 POS workstations and server from vendor media with the vendor's integrity statement, or bring forward the P2PE cloud POS replacement (POAM-010) and keep Resort 2 outlets on room charge, cash, and loaner P2PE devices until then.
5. Purge any card data the attacker could reach: mailboxes, recordings, and files (POL-04 4.4; POL-03 4.11).
6. Forensics or the PFI confirms that no persistence remains (scheduled tasks, services, remote tools, rogue accounts) before any reconnection.

## 6. Legal, contractual, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel confirms every legal notice before it goes out. The CFO owns all acquirer and card brand communication. The General Counsel keeps the **decision log** (POL-03 4.5).

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is there a reasonable suspicion of card data compromise? (Starts the acquirer and Visa clocks) | Incident commander with the CFO | Incident log time |
| D2 | Do the franchise agreements apply (brand systems or guest data at Hotels 3 to 6)? Does the REIT management agreement apply (from 2027-01-01)? | General Counsel | Decision log |
| D3 | Is it a breach of personal information under Fla. Stat. 501.171 and other states' laws? Which data elements, for whom? Date of determination | General Counsel with breach counsel | Decision log with the analysis |
| D4 | How many individuals in total, in Florida, and by state? (Florida thresholds: 500 for the Department; more than 1,000 for consumer reporting agencies) | General Counsel | Affected individuals list |
| D5 | Has law enforcement asked in writing for a delay (501.171(4)(b))? | Breach counsel | Written request filed |
| D6 | Guest remediation: call center, credit or identity monitoring, card reissue coordination with the acquirer | CMT | CMT minutes |

**Is it a Florida breach?** Under 501.171(1)(g)1.a., personal information includes a name with a card number **in combination with any required security code**. A card number alone captured at an outlet may not qualify, but CRO phone payments include security codes and guest names, so this scenario very likely does. Counsel decides and documents the analysis.

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | CFO |
| Within 24 hours of suspicion | Acquirer notified (contract term; fictional) | CFO |
| Within 24 hours of suspicion, if D2 applies | Franchisor notified (franchise agreement; fictional) | General Counsel |
| Within 48 hours of suspicion, from 2027-01-01, if D2 applies | REIT owner notified (management agreement; fictional) | General Counsel |
| Within 3 calendar days of suspicion | Compromise reported to Visa (through the acquirer); other brands per the acquirer's instructions | CFO |
| Within 3 calendar days of the Visa notice | Incident report to Visa and the acquirer (WTDIC Attachment A) | Security Manager and CFO |
| Within 3 calendar days of identifying at-risk cards or the window of exposure | At-risk account numbers to Visa through the acquirer | CFO |
| Within 5 business days of a Visa PFI notice | PFI contracted; Visa and the acquirer told the PFI's name | CFO with the General Counsel |
| As soon as practical | Voluntary report to the U.S. Secret Service or FBI | Security Manager through counsel |
| Within 30 days of determination | Florida individual notices (15 more days only with written good cause to the Department); Department of Legal Affairs notice if 500 or more Florida residents (no extension) | General Counsel and breach counsel |
| Without unreasonable delay | Consumer reporting agencies if more than 1,000 individuals are notified at once | Breach counsel |
| Per each state | Notices to residents of other states; most resort guests live outside Florida | Breach counsel |
| Within 10 days of determination, from 2027-01-01 | If the managed hotels' guest data was affected: notice to the REIT owner as third-party agent (501.171(6)(a)), with all information it needs for its own notices | General Counsel |

**Card brands do not replace legal notice, and legal notice does not replace card brand reporting.** Both run in parallel. The Visa 3-day clock expires long before the Florida 30-day clock.

**Communications.**
- Guests: no statement until counsel approves. Then a website notice, a call center script through the insurer's notification vendor, and front desk talking points.
- Group clients, the franchisor, and (from 2027) the REIT owner: direct calls from the COO or General Counsel after the contractual notices.
- Media: holding statement approved by counsel; no details on attribution, card counts, or vendors.
- Staff: daily briefings through the out-of-band channel; outlet and CRO staff told why the fallbacks are in place.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05), validating each step: EDR clean, credentials rotated, patches applied, and forensics or PFI sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Identity provider and privileged access (break-glass if needed) | 1 h | Sessions revoked; privileged and service credentials rotated |
| 2 | SD-WAN and site firewalls with the POS VLAN blocked from corporate networks | 1 h | Rule review by the IT Director |
| 3 | Resort front desk P2PE devices and gateways (normally unaffected) | 4 h (BP-03) | Device serial numbers and seals checked against the device list |
| 4 | Clean CRO PCs (rebuilt) and CRO card handling through payment links only | 4 h (BP-05) | EDR healthy; no keyed card entry until keypad devices or the acquirer agrees |
| 5 | Resort 2 outlet card acceptance: loaner P2PE devices first; legacy POS only after vendor rebuild and forensics sign-off | 4 h (BP-06) for room charge and cash; card acceptance when validated | Acquirer agrees the outlet may resume |
| 6 | SIEM feeds from the rebuilt segments | 8 h | Monitoring confirmed before reconnection |
| 7 | Night audit, card settlement, and folio reconciliation for the outage period | 12 h (BP-08) | Director of Finance reconciles room charges and payment links |

Tell staff, guests, group clients, and the franchisor when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-005, R-030, R-040, R-041), the POA&M (P07), the PCI DSS scope document (POAM-016), and this runbook.
- Expect the acquirer to require a new validation, possibly a Report on Compliance by a QSA, and card brand non-compliance assessments. The CFO budgets for them with the insurer.
- Retain all incident documentation, the decision log, and copies of notices; keep any Florida no-harm determination at least 5 years (501.171(4)(c)).

# Incident Response Runbook: Ransomware Affecting Agency Systems Holding CJI and FTI

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded GovTech systems integrator; about 145 agency customers in 16 states) |
| Tier / Vertical | Enterprise / Public Administration |
| Incident type | Ransomware with data theft (double extortion) that enters through the AQ-1 e-filing platform, spreads over the network peering into the integration hub and legacy hosting, encrypts court and sheriff systems, and steals staged revenue agency files (FTI). Includes the SEC materiality assessment and a multi-agency, multi-state notification workflow |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Multi-Agency and Multi-State Notification Procedure |
| Systems in the attack path | SYS-15 AQ-1 platform; SYS-02 integration hub (cloud services and the DC-1 edge); SYS-09 legacy hosting in DC-1 and DC-2; SYS-01 ACMC tenants reachable through the hub |
| Runbook owner | Director of Security Operations (incident commander), with the General Counsel for sections 7 and 8 |
| Approved | Executive risk committee, 2026-09-10 |
| Last tested | Technical ransomware exercise on 2026-05-21 (SOC, cloud platform, and data center teams; **no disclosure committee and no agency contacts took part**). The disclosure committee last exercised in 2025-04. Next: full tabletop with the disclosure committee, the filing step, and the AG-01 and AG-02 security contacts on 2026-11-12 (POAM-013) |
| Notification matrix | `notification-matrix.csv` (35 obligations: 3 CJIS, 3 Pub. 1075, 2 HIPAA, 1 Medicaid and SNAP, 1 DPPA, 8 Florida worked example, 1 other states, 5 SEC, 3 DFARS, 2 FAR, plus OFAC, law enforcement, supply chain, cyber insurance, CIRCIA status, and other agency contracts) |

**Why this incident.** It combines the company's only Very High risk (P01 R-001, ransomware across many agencies) with the High risks that make it likely and costly: the AQ-1 peering (R-003), data theft and extortion (R-002), unsupported legacy servers (R-005), and legacy backups that are not immutable (R-015). Internal Audit reached integration hub management ports from an AQ-1 host in August 2026 (P07 SC-7; POAM-004), so the path in this runbook is the one an attacker would most likely use.

**Whose clocks.** The company is a contractor. Many of the legal clocks in this incident belong to the **agencies**: a criminal justice agency's CJIS reporting, a revenue agency's 24-hour report to TIGTA and the IRS Office of Safeguards, and each Florida agency's 12-hour ransomware report. The company's job is to tell each agency within 1 hour and give it the facts it must report. The company also has **its own** clocks: the SEC Form 8-K Item 1.05 filing (4 business days after a materiality determination), third-party agent notices under state law (10 days in Florida, Fla. Stat. 501.171(6)(a)), the AG-04 business associate notice if IES is touched, and DoD reporting within 72 hours if the CUI enclave is touched.

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | SOC manager on duty (second SOC site) | SOC bridge on the out-of-band conferencing service |
| Executive incident lead | CISO | Deputy CISO | Out-of-band group on company mobile phones |
| Crisis management team chair | President, State and Local Platforms | President, Systems Integration | Crisis line |
| Crisis management team | Four segment presidents, CIO, CISO, General Counsel, Chief Privacy Officer, Chief Human Resources Officer, Director of Regulated Data Compliance, Vice President, Corporate Communications, Vice President, Investor Relations | Designated alternates | Roster in the sealed incident binder |
| Disclosure committee chair | General Counsel | Deputy General Counsel | Direct mobile |
| Disclosure committee members | General Counsel (chair), CFO, Chief Accounting Officer, CISO, Chief Risk Officer, Chief Privacy Officer, Vice President, Investor Relations (seven members); outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Agency notices (CJI, FTI, IES, DPPA) | Director of Regulated Data Compliance | Regulated data compliance managers (one per program) | Printed agency contact list in the incident binder |
| Breach determinations and AG-04 business associate notice | Chief Privacy Officer | Chief Compliance Officer | Direct mobile |
| Outside breach counsel and forensics | Retained firms, engaged through counsel and the insurer panel | Co-sourced incident response retainer | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Recovery owners | Vice President, ACMC Platform Operations; Integration Engineering Manager; Director of Network and Data Center Operations; Vice President, Integration Management Office (AQ-1) | Named deputies | Crisis line |
| Federal Programs (DoD and FAR reports) | President, Federal Programs | Federal Programs security lead | Direct mobile |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read company email, chat, and the ticketing system, and may hold identity sessions. Coordinate on company mobile phones, the out-of-band conferencing service, and the printed incident binder held at headquarters, both SOC sites, and each delivery center. **Never put FTI, CJI, or ePHI in the incident log, email, chat, or tickets** (POL-03 4.3); evidence goes to the restricted evidence store.

**Roles that overlap.** The CISO sits on both the crisis management team and the disclosure committee, which keeps facts consistent. To keep disclosure judgments independent of the response team, the General Counsel, not the CISO, records the materiality determination, and outside securities counsel reviews it.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder current at every site: this runbook, the notification matrix, the agency contact list for about 145 customers, the agency fact sheet template (section 6.2), the materiality worksheet (section 7), and Form 8-K drafting notes
- [ ] Immutable backups for ACMC and IES in separate accounts and a second U.S. region, restore-tested in the last 90 days (CP-9, CP-4; POL-04 4.7)
- [ ] **Legacy hosting backups are not immutable (gap until POAM-008 closes, 2026-12-31).** Until then, the weekly offline vault copy in DC-2 is the only copy an attacker cannot reach; confirm it is rotated every week
- [ ] SIEM receives logs from every system in the attack path, retained at least 1 year online (AU-11). **Gap until POAM-003 closes (2026-12-31):** AQ-1 keeps 90 days of logs outside the SIEM, and legacy hosting keeps 180 days
- [ ] AQ-1 peering limited to the 4 e-filing endpoints on named ports. **Gap until POAM-004 closes (2026-11-30)**; management ports are scheduled to be blocked by 2026-09-30
- [ ] AQ-1 identities federated, with no standing administrator rights. **Gap until POAM-001 closes (2027-01-31)**
- [ ] VPN appliances on CJI paths use FIPS 140-3 modules with no default credentials (POAM-006, POAM-007)
- [ ] SOAR 1-hour timer live for any incident tagged CJI or FTI. **Gap until POAM-014 closes (2026-12-15)**; until then the SOC manager starts a manual timer
- [ ] Sealed break-glass accounts tested this quarter (POL-02); second SOC site able to run the SIEM and EDR consoles
- [ ] Materiality playbook updated with customer-harm and public-trust factors, and the disclosure committee roster current. **Gap until POAM-013 closes (2026-11-30)**
- [ ] Outside counsel, forensics, insurer, and law enforcement contacts confirmed this quarter; counsel's state breach law matrix updated in the last 12 months

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Mass file renames, encryption, or a ransom note on any legacy hosting server, hub edge device, or AQ-1 host | EDR; backup job failures; agency user reports | SOC opens a severity-1 case; contains hosts through EDR; pages the incident commander |
| Traffic from the AQ-1 account to integration hub subnets other than the 4 e-filing endpoints | Network flow logs; cloud firewall alerts | Cut the AQ-1 peering at the hub side; open a severity-1 case |
| New or changed administrator accounts, or use of a dormant AQ-1 administrator | PAM; identity platform; AQ-1 directory logs (pulled locally until POAM-003 closes) | Revoke sessions; disable the account; open a case |
| Staged revenue agency files read in bulk, or large outbound transfers from the hub or DC-1 | Database activity monitoring; egress monitoring; data loss prevention | Block the destination; preserve logs; open a case |
| Backup jobs deleted or failing on the legacy backup system | Backup console; SIEM | Isolate the backup system; protect the DC-2 vault copy; open a case |
| Extortion message to the company or an agency, or a leak-site post naming the company or a customer | Email; agency; threat intelligence; law enforcement; media | Declare; preserve; do not engage without counsel |
| An agency, cloud provider, or subcontractor reports suspicious activity involving company systems | Agency security contact; provider security channel; subcontractor notice | Open a case; start the supply chain track (section 6) |

**Declare a severity-1 ransomware incident when** encryption or a ransom note is confirmed on any production or hosted system, an unknown actor has used administrator rights in production, or an extortion claim names company or agency data. When in doubt, declare. First notices to agencies are for **suspected** incidents.

**Record three times, separately, in the incident log:**
1. **Discovery (T0).** When any workforce member or subcontractor first knew of the incident. It starts the 1-hour internal and agency reporting rule (CJISSECPOL v6.1 IR-6; POL-03 4.2 and 4.4), the agencies' 24-hour FTI clock (Pub. 1075 sec. 1.8.4) once they are told, and the 72-hour DoD clock if the CUI enclave is affected (DFARS 252.204-7012(c)).
2. **Breach determination,** or the first "reason to believe" a breach occurred. It starts the 10-day third-party agent notice in Florida (501.171(6)(a)) and similar clocks in other states. In a data-theft case this can be the day of discovery, for example when the ransom note claims data was taken.
3. **Materiality determination.** Recorded later by the disclosure committee (section 7). It starts the 4-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log and evidence register; record T0 and the trigger | Incident commander | Log open with T0 |
| 2. Cut the AQ-1 peering at the integration hub side, then isolate the AQ-1 account from the internet except the forensic path | Director of Cloud Platform Engineering | Peering down; confirmed by flow logs |
| 3. Contain affected hosts through EDR; do not power them off (preserve memory). On legacy servers without EDR support, isolate at the switch | SOC; Director of Network and Data Center Operations | Hosts contained |
| 4. Protect backups: lock the ACMC and IES backup accounts against deletion changes; disconnect the legacy backup system from the management network; confirm the DC-2 vault copy is offline | Director of Cloud Platform Engineering; Director of Network and Data Center Operations | Backup integrity confirmed |
| 5. Revoke sessions and rotate credentials for privileged and service accounts in the attack path; use break-glass accounts if the identity platform is in doubt | Director of Identity and Access Management | Revocations logged |
| 6. **Agency calls within 1 hour of T0 (suspected incident):** each criminal justice agency whose legacy system or ACMC tenant is in the path, each revenue agency whose files pass through the hub, then all other affected customers. Say what is known, what is not, and when the next update comes | Director of Regulated Data Compliance | Each contact reached; call times logged |
| 7. Suspend affected interfaces at the hub (message switch links for affected court and sheriff systems, revenue agency file transfers) only with each agency's agreement, unless the interface is actively carrying the attack | Integration Engineering Manager | Interface status agreed and logged |
| 8. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics under privilege; the insurer is notified | CISO; General Counsel | Claim number; engagement letters |
| 9. Crisis management team activated; affected courts and sheriffs move to their downtime procedures (printed dockets, message switch warrant checks; P05 section 7) | President, State and Local Platforms | Team convened; agency downtime confirmed |
| 10. Written fact sheet to every affected agency within 4 hours of T0 (POL-03 4.4) | Director of Regulated Data Compliance | Fact sheets sent through the agreed secure channel |

## 4. Analysis (RS.AN)
1. **Scope.** Hosts, cloud accounts, identities, interfaces, and data stores the attacker touched. Use EDR, the SIEM, cloud audit logs, PAM records, and network detection. For AQ-1, collect directory and console logs locally **before the 90-day retention drops them** (R-038). List every customer whose system, tenant, or staged files sit in an affected zone.
2. **Initial access.** Confirm the AQ-1 entry point: a password-only console sign-in, one of the 31 standing administrator accounts, or a compromised engineer laptop. Check whether the attacker used the peering, a shared legacy vendor VPN account (R-039), or the flat legacy management network (POAM-024) to move.
3. **Evidence.** Forensics images hosts and exports logs; chain of custody is kept in the evidence register with hashes. Evidence is kept 7 years (POL-01 4.11). If the CUI enclave is in scope, keep images and packet captures at least 90 days for DoD (DFARS 252.204-7012(e)).
4. **Exfiltration.** Determine what left, from where, and for which agencies and individuals: egress logs, hub file transfer logs, database activity monitoring, and the attacker's claims and samples. For each customer, record data types (FTI, CJI and CHRI, sealed or juvenile court records, Social Security numbers, driver records), record counts, and the state of residence of affected individuals. **This drives sections 6 and 8.**
5. **Boundaries that should hold.** Confirm with evidence that the IES environments (Cloud provider B), the CUI enclave, and the AG-05 tenant were not reached. Each confirmation removes or keeps a block of obligations in the matrix (HIPAA, Medicaid and SNAP, DFARS, DPPA).
6. **Integrity.** For court and sheriff systems, confirm that warrant, docket, and supervision data were not altered (compare with backups and audit trails). Agencies decide whether to suspend reliance on a record until it is validated.
7. **Business impact.** Finance and the BIA owners estimate daily impact from P05 values: for example, about $0.80 million per day for legacy court and sheriff systems (BP-09), $0.60 million for the integration hub (BP-05), and $1.10 million for revenue casework (BP-02), plus service credits, contract termination exposure, and response costs. These estimates feed section 7.

## 5. Containment and eradication (RS.MI)
1. Contain by zone: the AQ-1 account, the hub edge in DC-1, each legacy customer segment, and any ACMC tenant in scope.
2. Disable compromised accounts; reset all privileged credentials and service secrets in the attack path; rotate interface credentials and keys for every affected agency interface. Coordinate any action on a customer-managed key with the revenue agency that controls it (R-056).
3. Rebuild from known-good images and infrastructure code; never decrypt and reuse encrypted hosts. Unsupported legacy servers (POAM-005) are rebuilt on supported platforms where possible, or kept isolated behind application gateways.
4. Close the entry path before reconnecting: AQ-1 peering limited to the 4 endpoints, AQ-1 administrators federated with MFA and no standing rights, legacy vendor accounts removed.
5. Forensics confirms persistence is removed before recovery starts in each zone.

## 6. Agency and regulatory notices (RS.CO)
### 6.1 Notice timeline
**Follow `notification-matrix.csv`.** Outside counsel confirms every external notice before it goes out. T0 is the recorded discovery time.

| When | Action | Owner |
|---|---|---|
| T0 + 1 hour | Phone notice of a suspected incident to each affected criminal justice agency's local agency security officer (CJISSECPOL v6.1 IR-6; Security Addendum) and each affected revenue agency's disclosure officer (Pub. 1075 Exhibit 7 contract terms), then every other affected customer | Director of Regulated Data Compliance |
| T0 + 1 hour | Cyber insurer breach hotline | General Counsel |
| T0 + 4 hours | Written fact sheet to every affected agency (section 6.2) | Director of Regulated Data Compliance |
| Agency discovery + 12 hours | Each affected Florida state agency (for example AG-01) and each Florida county or city reports the ransomware incident to the Cybersecurity Operations Center and the FDLE Cybercrime Office; counties and cities also report to their sheriff (Fla. Stat. 282.318(3)(c)9.c.(I); 282.3185(5)) | Agencies, with company facts |
| Agency discovery + 24 hours | Each affected revenue agency reports to TIGTA and the IRS Office of Safeguards (Pub. 1075 sec. 1.8.2 to 1.8.4). The company confirms each report was made, and reports directly if it cannot confirm | Revenue agencies; Director of Regulated Data Compliance confirms |
| As the state CSA requires | Each criminal justice agency reports the contractor security violation to its CJIS Systems Officer and the FBI (Security Addendum sec. 4.01 to 4.03) | Agencies, with company facts |
| T0 + 24 hours | CISO briefs the General Counsel (POL-03 4.6); voluntary report to the FBI and CISA, coordinated with the agencies | CISO |
| T0 + 72 hours, only if the CUI enclave is affected | DoD report through DIBNet; malware to DC3; incident number to the prime (DFARS 252.204-7012(c), (d), (m)) | President, Federal Programs |
| Within 4 business days of a materiality determination | Form 8-K Item 1.05 (section 7) | General Counsel |
| No later than 10 days after breach determination | Written third-party agent notice to each affected Florida agency with everything it needs for its own notices (Fla. Stat. 501.171(6)(a)); the same duty under each other state's law per counsel's matrix | Chief Privacy Officer with counsel |
| Agency: 30 days after its determination | Florida individual notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 are notified at once (501.171(3)-(5)) | Agencies; the company sends notices on an agency's behalf if asked (501.171(6)(b)) |
| Agency: 1 week after remediation | After-action report by each affected Florida county or city to the Florida Digital Service (Fla. Stat. 282.3185(6)) | Agencies, with company input |

**Plan to the shortest clock.** The 1-hour agency calls come first. A company that waits for its own investigation leaves the agencies in breach of their own 12-hour and 24-hour duties (R-019; POAM-014).

### 6.2 Agency fact sheet
Florida agency reports and the IRS data incident report ask for specific facts (Fla. Stat. 282.318(3)(c)9.b.; Pub. 1075 sec. 1.8.3). The company keeps one fact sheet per agency, with no FTI or CJI in it, updated at least every 12 hours:
- summary of facts; date and time the incident occurred and was discovered; how it was discovered
- the date of the most recent backup, where it is, whether it was affected, and whether it is cloud-based
- types of data and data elements involved; potential number of records (a range if unknown)
- systems involved and where they are (cloud region, DC-1, DC-2); whether any company employee or subcontractor was involved
- estimated fiscal impact to the agency, if known; details of any ransom demand
- the company's point of contact and the time of the next update

### 6.3 Other communications
- **Agency users:** status pages updated at least every 4 hours while services are down.
- **Media:** only the Vice President, Corporate Communications speaks, after affected agencies have seen the statement. Statements about FTI go through the revenue agencies, which share any media release with the IRS Office of Safeguards before release (Pub. 1075 sec. 1.8.5).
- **Investors:** only through the Form 8-K and Investor Relations scripts approved by the General Counsel (section 7).
- **Staff:** a script from the incident commander; no posts or outside discussion; a special trading blackout for those with knowledge (section 7).

## 7. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 to 6. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery (Form 8-K Item 1.05, Instruction 1), from the perspective of a reasonable investor, weighing quantitative and qualitative factors together.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 7.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.6) | CISO | Brief logged |
| 7.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 7.3 | **Special trading blackout** for committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 7.4 | Committee completes the materiality worksheet (below) with facts from sections 4 to 6 | Committee | Worksheet completed |
| 7.5 | **Materiality determination** recorded with the date, time, and reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 7.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Leave out technical details that would impede response or remediation, and anything an agency contract or law bars the company from disclosing (FTI and CJI are never described in detail) | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 7.7 | **File within 4 business days after the determination.** Only a written determination by the U.S. Attorney General that disclosure poses a substantial risk to national security or public safety allows delay (Item 1.05(c)); any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 7.8 | Tell the most affected agencies shortly before the filing becomes public, so no agency learns of it from the news; brief the chairs of the audit committee and the board risk committee | Director of Regulated Data Compliance; General Counsel | Agencies and chairs briefed |
| 7.9 | Keep reassessing as facts change. File an amendment within 4 business days after information that was not determined or was unavailable at filing becomes available (Item 1.05, Instruction 2). Carry lessons into the next Reg S-K Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist).** The rows marked *new* are the customer-harm and public-trust factors added under POAM-013, because most of the harm in a GovTech incident falls on agencies and the public before it reaches the company's income statement.
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Lost revenue and service credits from P05 values (the company earns about $18.5 million per business day); response, forensic, and legal costs; ransom demand; notification and credit monitoring costs the company bears under contracts; insurance coverage and retention |
| Operational | Tier-1 services down and for how long; number of agencies and states affected; courts and sheriffs on downtime procedures |
| Data | Agencies and individuals affected; data types (FTI, CJI and CHRI, sealed or juvenile records, Social Security numbers); whether data was published |
| *New:* customer harm | Public safety effects (warrant or supervision data unavailable or altered); benefit or court deadlines missed; agency costs the company may have to reimburse |
| *New:* contract and procurement | Termination for default or convenience rights triggered; suspension of CJI access by the FBI (Security Addendum sec. 4.01 to 4.03); IRS action on a revenue agency's contract; effect on GovRAMP status, pending bids, and renewals |
| *New:* public trust | National media; legislative inquiries in customer states; agency public statements naming the company |
| Legal and regulatory | Expected IRS, FBI, state attorney general, or legislative inquiries; litigation by individuals or agencies; DoD or prime contractor action if the CUI enclave is involved |
| Strategy | Effect on the AQ-1 integration and future acquisitions; analyst or ratings reaction |

## 8. Multi-agency and multi-state breach notification workflow (RS.CO)
| Step | Action | Owner | Output |
|---|---|---|---|
| 8.1 | Build the affected population from forensic results, per customer: data elements, record counts, and **state of residence** of each individual. Keep three groups apart: (a) agency data where the company is a contractor or third-party agent; (b) AG-04 ePHI, where the company is a business associate (only if IES is reached); (c) company employee data, where the company is the data owner | Chief Privacy Officer; data team | Affected-population file per customer |
| 8.2 | Breach analysis per customer and data type: CJI and FTI incident rules (the agencies decide their own reports with company facts); HIPAA four-factor risk assessment if AG-04 ePHI is involved (45 CFR 164.402); state breach law definitions of personal information | Chief Privacy Officer; outside counsel | Signed analysis per customer |
| 8.3 | **Vendor notices (company duty):** written notice to each affected agency within the shortest of its contract term and each applicable state's vendor-to-owner deadline; Florida worked example: no later than 10 days after determination (501.171(6)(a)) | Chief Privacy Officer; Director of Regulated Data Compliance | Notices sent and logged |
| 8.4 | **Business associate notice (only if AG-04 ePHI is involved):** to AG-04 within the BAA term and no later than 60 calendar days after discovery, with the identity of each individual (164.410) | Chief Privacy Officer | AG-04 notice |
| 8.5 | **Agency notices to individuals and regulators (agency duty):** apply each state's law with counsel's state matrix. The company offers to send notices on an agency's behalf, staff a call center, and provide credit monitoring where the contract or the agency asks | Agencies; Chief Privacy Officer supports | Agency notice plans |
| 8.6 | **Florida worked example:** each Florida agency notifies affected Floridians within 30 days of its determination, the Department of Legal Affairs within 30 days if 500 or more Floridians are affected (the 15-day good-cause extension applies only to notice to individuals), and consumer reporting agencies if more than 1,000 are notified at once | Florida agencies | Florida filings |
| 8.7 | **Plan to the shortest clock** across agencies, states, the SEC, and contracts. Publish one master calendar for the crisis management team | Chief Privacy Officer | Master calendar |
| 8.8 | Honor any written law enforcement delay request and document it; tell the affected agencies | General Counsel | Delay record |
| 8.9 | Track notices from vendors and subcontractors if the attack came through them (Fla. Stat. 501.171(6)(a) and other states' third-party agent rules) | Director of Third-Party Risk Management | Vendor notices logged |

**Ransom decision.** Florida state agencies, counties, and municipalities may not pay or otherwise comply with a ransom demand (Fla. Stat. 282.3186). The data belongs to the agencies, and the company will not pay over the objection of any agency (POL-03 4.7). Any payment by the company requires the CEO, the General Counsel, and the insurer, consultation with every affected agency, and an OFAC sanctions check. Report to the FBI or CISA; full and timely reporting is a mitigating factor in OFAC's 2021 advisory. Paying removes no notification or disclosure duty.

**Worked example of the clocks (fictional dates).** The SOC confirms encryption on DC-1 legacy servers at **03:20 on Wednesday 2027-01-13** (T0). The ransom note claims the attackers took revenue agency tax files.
- **By 04:20:** calls to the affected courts and sheriffs and to the 6 revenue agencies, including AG-01. **By 07:20:** written fact sheets.
- **By 15:20 the same day:** AG-01, a Florida state agency, must make its 12-hour ransomware report if it treats the company's call as its discovery. **By 03:20 on 2027-01-14:** each revenue agency's 24-hour report to TIGTA and the IRS Office of Safeguards.
- **Disclosure committee** convenes Thursday 2027-01-14 and determines the incident is material on **Friday 2027-01-15 at 15:00**. Monday 2027-01-18 is a federal holiday, so the 4 business days are January 19, 20, 21, and 22: the **Form 8-K is due by Friday 2027-01-22**.
- **Florida third-party agent notice:** counsel decides the ransom note's claim on 2027-01-13 gave "reason to believe" a breach occurred, so the 10-day notice to AG-01 is due Saturday 2027-01-23 and is sent Friday 2027-01-22. If counsel had used the forensic confirmation on Tuesday 2027-01-19, it would have been due 2027-01-29. The company plans to the earlier date.
- **AG-01's own notices:** if AG-01 determines the breach on 2027-01-13, its 30-day notices to Floridians and the Department of Legal Affairs are due 2027-02-12.
- **Not triggered in this example:** forensics confirms that IES, the CUI enclave, and the AG-05 tenant were not reached, so the HIPAA, DFARS, and DPPA rows do not apply. That conclusion is documented with its evidence.

## 9. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Out-of-band communications, agency contact list, and status pages (BP-11)
2. Identity platform and break-glass access
3. Security tooling (SIEM, EDR) for clean-room validation, from the second SOC site if needed
4. Integration hub cloud services and the DC-1 VPN edge; agencies use message switch terminals meanwhile
5. ACMC criminal justice tenants, if affected
6. ACMC FTI tenants, with each revenue agency's key coordination
7. IES environments, only if affected (8-hour contract RTO; AG-04 recovery is slower until POAM-015 closes)
8. Eligibility contact centers and document processing
9. Legacy court and sheriff systems, DC-1 then DC-2. **Warning (current state):** legacy backups are not immutable and the real RPO is 24 hours (POAM-008). If the backup system was encrypted, the DC-2 offline vault copy (up to 7 days old) is the fallback, and agencies re-enter recent records from paper and the message switch
10. ACMC motor vehicle tenant
11. AQ-1 e-filing, rebuilt inside the landing zone where possible; courts accept paper filings meanwhile
12. Software delivery platform, CUI enclave, corporate systems
13. ACMC local government tenants
14. Payroll, ERP, and billing

**Validate before reconnecting:** forensics confirms each zone is clean; credentials and interface keys rotated; patched; logging to the SIEM; VPN tunnels on CJI paths use FIPS 140-3 modules (SC-13). **Each agency's security contact approves reconnection of its interface;** for CJI interfaces the agency confirms whether its CJIS Systems Agency must approve first. Tell agency users when each service is back (RC.CO). Agencies keep downtime procedures until each process is back within its RTO.

## 10. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days of closing the incident (POL-03 4.10). Invite the security contacts of the most affected agencies.
- Post-incident review of the incident procedures, with fixes made as soon as reasonably possible and training on the changes given to staff with FTI access (Pub. 1075 sec. 1.8.4); refresher training within 30 days for staff involved in an incident affecting CJI (POL-03 4.10).
- Update the risk register (P01, especially R-001, R-002, R-003, R-005, R-010, R-015, R-019, R-038), the POA&M (P07), the BIA (P05), this runbook, and the materiality playbook.
- The disclosure committee reviews the incident's effect on the next Item 106 disclosure (17 CFR 229.106).
- Provide each Florida county or city its after-action input within 1 week of remediation (Fla. Stat. 282.3185(6)).
- Retain the incident log, evidence, determination minutes, breach analyses, and notices for at least 7 years (POL-01 4.11).

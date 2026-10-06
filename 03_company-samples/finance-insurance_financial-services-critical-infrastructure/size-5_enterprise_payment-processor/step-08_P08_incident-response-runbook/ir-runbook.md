# Incident Response Runbook: Compromise of the Payment Processing Environment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded merchant payment processor; sponsor Banks A, B, and C; NYDFS-licensed payouts subsidiary) |
| Tier / Vertical | Enterprise / Financial Services |
| Incident type | Compromise of the payment processing environment: an attacker exploits a zero-day vulnerability in the managed file transfer (MFT) appliances in DC-1, steals clearing files (full PAN) and merchant funding files, then deploys ransomware on the settlement batch servers. Funding files to all three sponsor banks miss their cutoffs. Includes the **SEC materiality assessment and Form 8-K Item 1.05** step |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response and Resilience Policy; PRC-03.1 (this runbook); PRC-03.2 SEC Materiality Assessment Procedure; PRC-03.3 Bank Service Provider Notice Procedure; PRC-03.4 NYDFS Notice and Annual Filing Procedure; PRC-03.5 Ransomware Response Runbook |
| Runbook owner | Director of Security Operations, with the General Counsel for section 6 and the Chief Compliance Officer for section 7 |
| Approved | Executive risk committee, 2026-09-08 |
| Last tested | Technical tabletop 2026-03-18 (Cyber Fusion Center and platform teams). Last executive exercise 2025-06; **the 2026 disclosure committee has not been exercised**. Next: full tabletop with the disclosure committee and the President of Cris Santos Payouts, LLC on 2026-11-12 (POAM-005) |
| Notification matrix | `notification-matrix.csv` (35 obligations: 3 card brand and sponsor bank compromise notices, 4 bank incident notification rows, 2 FTC, 3 NYDFS, 4 SEC, 1 insider trading, 4 generic state, 5 Florida worked example, 2 contractual, OFAC, law enforcement, insurance, and 4 not-applicable or pending rules) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Security Operations | Cyber Fusion Center manager on duty | Out-of-band bridge on company mobile phones |
| Executive incident lead | CISO | CTO | Out-of-band group on company mobile phones |
| Crisis management team chair | Chief Operating Officer | Chief Financial Officer | Crisis line |
| Settlement and funding lead | Senior Vice President, Settlement and Treasury Operations | Director of Settlement Systems | Crisis line |
| Disclosure committee chair | General Counsel | Deputy General Counsel (securities) | Direct mobile |
| Disclosure committee members | CFO, Controller, CISO, Chief Risk Officer, Chief Compliance Officer, Vice President Investor Relations, Deputy General Counsel; outside securities counsel advises | Designated alternates | Roster in the sealed incident binder |
| Notices lead (banks, card brands, FTC, NYDFS, merchants) | Chief Compliance Officer | PCI Program Director | Direct mobile |
| Payouts subsidiary | President, Cris Santos Payouts, LLC | Payouts operations director | Direct mobile |
| Outside breach counsel, forensics, PCI Forensic Investigator (PFI) | Retained firms, engaged through counsel and the insurer panel | Insurer panel alternates | Retainer hotline |
| Cyber insurer | Carrier breach hotline | Broker | Policy card in the incident binder |
| Sponsor banks | Banks A, B, and C designated points of contact. **Bank C contacts to be loaded by 2026-10-31 (POAM-007)** | Each bank's CEO and CIO (fallback under 53.4(a)(2), 304.24(a)(2), 225.303(a)(2)) | Contact register in the incident binder |
| Communications | Vice President, Corporate Communications | Vice President, Investor Relations (investor messages) | Direct mobile |
| Law enforcement | U.S. Secret Service or FBI field office | IC3; CISA | Numbers in the incident binder |

**Out-of-band first.** Assume email, chat, the identity platform, and the ticketing system may be watched. Use company mobile phones, the out-of-band conferencing service, and the printed incident binder kept at headquarters, DC-1, DC-2, and each operations center.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable cloud backups and DC-2 virtual tape replicas verified; settlement restore tested within 90 days (CP-9; CP-9(1))
- [ ] MFT appliances: vendor advisories watched daily; 72-hour emergency patch path agreed with the vendor; file-level transfer events in the SIEM (**gap until POAM-009 closes**)
- [ ] Batch scheduler and job script secrets vaulted (**31 scripts open until POAM-002 closes**)
- [ ] Settlement operators on MFA (**interim compensating controls under EXC-2026-017 until POAM-004 closes**)
- [ ] Segmentation between DC-1 management subnets and the Cloud A CDE confirmed (**gap until POAM-003 closes**)
- [ ] Bank designated contacts for all three banks confirmed this quarter (**Bank C gap until POAM-007 closes**)
- [ ] Materiality playbook current, including the NYDFS 72-hour and bank 4-hour clocks; disclosure committee roster current (**gap until POAM-005 closes**)
- [ ] Manual funding fallback ready: prior validated funding files, delta-file procedure, and wire procedure for the top 300 enterprise merchants
- [ ] Counsel, forensics, PFI shortlist, and insurer contacts confirmed this quarter

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file renames, or batch job failures across settlement servers | EDR; scheduler alerts; operators | Cyber Fusion Center opens a severity-1 case; isolate hosts through EDR; page the incident commander and the settlement lead |
| Unusual outbound transfer from the MFT segment, or MFT vendor advisory of active exploitation | Network detection; egress logs; vendor or CISA advisory | Block destinations; preserve appliance logs; open a case; check for file exfiltration |
| A card brand or a sponsor bank reports a common point of purchase tracing back to the company | Bank; card brand | Declare immediately. This is reasonable suspicion of an account data compromise (Visa clock starts) |
| Extortion message or leak-site post naming the company | Email; threat intelligence; law enforcement | Declare; preserve; do not engage without counsel |
| Funding file control totals fail or a file is not delivered by cutoff | Scheduler; treasury | Settlement lead and incident commander assess cause; start the 4-hour determination (section 7.1) |

**Declare a severity-1 payment environment compromise when** encryption or a ransom note is confirmed on any CDE component, card data exfiltration is suspected, or a brand or bank reports a common point of purchase.

**Record these times separately in the case clock fields:**
1. **Discovery** (FTC): the first day the event is known to any employee, officer, or agent other than the attacker (16 CFR 314.4(j)(2)). Starts the FTC 30-day clock.
2. **Reasonable suspicion or confirmation of an account data compromise** (Visa and sponsor agreements). Starts the 3-calendar-day Visa report and the 24-hour contractual bank notice.
3. **4-hour determination** (banks): when the company determines covered services have been, or are reasonably likely to be, disrupted for 4 or more hours. Notices go out as soon as possible after it.
4. **NYDFS determination**: when the Chief Compliance Officer determines that a cybersecurity incident has occurred for the payouts subsidiary. Starts the 72-hour clock.
5. **Breach determination or reason to believe** (state law, Florida worked example). Starts the 10-day third-party agent clock where state definitions are met.
6. **Materiality determination** (SEC): recorded by the disclosure committee (section 6). Starts the 4-business-day Form 8-K clock.

## 3. First 4 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected settlement servers and the MFT appliances from the network through EDR and firewall rules. **Do not power off or reboot** compromised systems (Visa WTDIC evidence rules; preserves memory) | Cyber Fusion Center; Network Engineering | Hosts contained; appliances cut off from the internet |
| 2. Block attacker infrastructure at egress proxies and DNS; close the DC-1 to Cloud A interconnect to everything except authorization traffic if the attacker may be moving toward the cloud CDE | Cyber Fusion Center; Network Engineering | Blocks confirmed |
| 3. Revoke sessions and rotate credentials for privileged accounts, batch scheduler service accounts, and MFT service accounts; use break-glass accounts if SSO is affected | Identity team | Revocations logged |
| 4. Confirm backup integrity: cloud vault locks intact; DC-2 virtual tape replicas not deleted or encrypted; pause replication from DC-1 to DC-2 if it could carry encrypted data | Infrastructure Engineering | Integrity confirmed |
| 5. Keep authorization running. The authorization platform in Cloud A is separate from the settlement servers; stop it only if forensics shows it is affected | CTO; incident commander | Decision recorded |
| 6. CISO briefs the CEO and the General Counsel; the General Counsel engages outside counsel, who retains forensics and, if a brand requires, a PFI under privilege; the CFO notifies the insurer | CISO; General Counsel; CFO | Claim number and engagement letters |
| 7. COO activates the crisis management team; the settlement lead starts the manual funding fallback for the top 300 enterprise merchants and asks each bank to hold its ACH window open where the agreement allows | COO; settlement lead | Fallback running; bank requests logged |
| 8. **4-hour determination for Banks A, B, and C** (section 7.1), no later than the second hour after declaration (POL-03 4.6) | Incident commander with the settlement lead and the Chief Compliance Officer | Decision and reason recorded for each bank |
| 9. Start the incident log (timeline, decisions, who, when), the evidence register, and the notice clock table | Incident commander | Log open |

## 4. Analysis (RS.AN)
1. **Initial access.** Confirm the MFT exploit path: appliance logs, vendor indicators, network detection, and the appliance configuration compared with the last known-good export. Check whether the attacker used the DC-1 management subnet (POAM-003 path) or plain-text job script credentials (POAM-002) to reach the batch servers.
2. **What was taken.** List every file that left: clearing files (full PAN, expiry date, transaction data; no cardholder names and no security codes) and funding files (merchant names, business bank routing and account numbers, amounts). Use egress logs, appliance transfer records, and the attacker's samples.
3. **Scope the cards and merchants.** Count PANs by brand and by sponsor bank program, and merchants by program and state. Set the window of exposure from the first malicious transfer to containment. Visa needs at-risk accounts within 3 calendar days of setting the window.
4. **Integrity.** Compare settlement records, funding files, and clearing files with journaled records and control totals. If any funding file may have been altered, hold it and regenerate it from the journal (CP-10(2)) with dual approval.
5. **Payouts subsidiary.** Determine whether payouts were delayed or the payouts platform (Cloud B) was touched. This drives the NYDFS determination (section 7.4).
6. **Preserve evidence.** Image memory and disks of affected servers, export appliance and SIEM logs, hash every artifact, and keep chain of custody. Give the PFI read-only access.
7. **Business impact.** Finance estimates impact with P05 values: about $2.1 billion of merchant funding per business day delayed; about $2.1 million a day of advance funding cost and service credits; clearing delays and interchange downgrades of about $2.4 million a day. These feed section 6.

## 5. Containment and eradication (RS.MI)
1. Replace the MFT appliances with clean builds on the vendor's fixed version, or move file delivery to the manual portal upload fallback until a fix exists.
2. Rebuild affected settlement servers from known-good images in DC-2 or on new hardware; never decrypt and reuse encrypted hosts.
3. Rotate every secret the attacker could reach, including HSM-protected TLS keys for bank and network links (through key ceremonies), service account credentials, and file encryption keys for funding files.
4. Remove the root cause before reconnecting: patch, close the management subnet path, remove embedded credentials.
5. Forensics (and the PFI where required) confirms that no persistence remains before recovery starts in each zone.

## 6. SEC materiality assessment (disclosure committee)
This step runs in parallel with sections 4 and 5. It does not wait for the investigation to finish: the materiality determination must be made without unreasonable delay after discovery, from the perspective of a reasonable investor, considering all relevant facts and both quantitative and qualitative factors.

| Step | What happens | Who | Done when |
|---|---|---|---|
| 6.1 | CISO briefs the General Counsel on every severity-1 incident within 24 hours of declaration (POL-03 4.4) | CISO | Brief logged |
| 6.2 | The disclosure committee convenes within 48 hours of declaration and meets at least every 2 business days until a decision | General Counsel | Minutes started |
| 6.3 | **Special trading blackout** issued to committee members, responders with knowledge, and executives | General Counsel | Blackout notice sent |
| 6.4 | Committee reviews the materiality worksheet (below) with facts from sections 4, 5, and 7, including the status of every regulatory clock | Committee | Worksheet completed |
| 6.5 | **Materiality determination** made and recorded with the date, time, and reasoning, whether the answer is material or not yet material. If not yet material, the committee sets the next review date and the facts that would change the answer | Committee (General Counsel records) | Determination minute signed |
| 6.6 | If material: draft Form 8-K Item 1.05 describing the material aspects of the nature, scope, and timing of the incident, and its material impact or reasonably likely material impact, including on financial condition and results of operations. Do not include technical details that would impede response or remediation | General Counsel; CFO; outside securities counsel | Draft approved by the CEO and CFO |
| 6.7 | **File within 4 business days after the determination.** Only a written U.S. Attorney General determination (national security or public safety) allows delay; any request goes through outside counsel to the Department of Justice | General Counsel | Filing confirmation |
| 6.8 | Align the timing and content of bank, merchant, partner, media, and investor communications with the filing; brief the audit committee and the risk and technology committee chairs before filing. Facts given to the banks, NYDFS, and the FTC must be consistent with the 8-K | Communications; Investor Relations; General Counsel; Chief Compliance Officer | Messages approved |
| 6.9 | Keep reassessing as facts change; counsel decides whether an amended filing is needed as information becomes available (see SEC Release 33-11216). Carry lessons into the next Item 106 disclosure | Committee | Reassessment logged |

**Materiality worksheet (company playbook, not a regulatory checklist):**
| Factor | Examples of what the committee considers |
|---|---|
| Quantitative | Revenue lost from processing disruption; advance funding, service credit, and recovery costs (P05 values); card brand assessments and fraud reimbursement exposure; ransom demand; legal and notification costs; insurance tower of $150 million with a $25 million retention |
| Operational | Hours of authorization or funding disruption; number of merchants and banks affected; payouts disruption |
| Data | Number of PANs and brands; whether names or security codes were included; merchant bank data; whether data was published |
| Relationships | Sponsor bank reaction (any bank invoking termination or remediation rights); card brand actions; loss of top enterprise merchants or ISV partners |
| Legal and regulatory | Bank, FTC, NYDFS, and state inquiries; litigation exposure from merchants and issuers |
| Reputation and strategy | Media coverage; analyst and ratings reaction; effect on new sponsor bank or partner deals |

## 7. Notices (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every legal notice before it goes out. The Chief Compliance Officer keeps the clock table.

### 7.1 Bank service provider notices: the 4-hour determination
- **Rule.** A bank service provider must notify at least one bank-designated point of contact at each affected banking organization as soon as possible after it determines it has had a computer-security incident that has materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, covered services for four or more hours. The rule text is the same for Bank A (12 CFR 53.4), Bank B (304.24), and Bank C (225.303). If a bank never provided contacts, notify its CEO and CIO or two people of comparable responsibility. Previously communicated maintenance is excluded.
- **Covered services here:** authorization processing, clearing, settlement, reconciliation, and merchant funding file services named in each sponsor agreement.
- **How to decide (PRC-03.3).** By the second hour after declaration, the incident commander and the settlement lead answer for each bank: has a covered service been disrupted, and will the disruption reach 4 hours? A funding file that cannot be delivered by the bank's cutoff, with no fix possible within 4 hours of the failure, is a "yes".
- **Record the decision either way**, with the reason. Each bank uses the company's notice to decide on its own 36-hour notice to its regulator (53.3, 304.23, 225.302).
- **Apply it to this scenario.** Ransomware stops the funding batch at 02:05. Bank A's cutoff (03:00) is already lost, and a rebuild in DC-2 has taken 9.5 hours in testing (POAM-006). The answer is "yes" for all three banks at the first decision point.

### 7.2 Card brands and sponsor banks (account data)
- Stolen clearing files carry full PAN, so this is an account data compromise. Notify the acquiring banks immediately (Visa WTDIC Section A.3.1), and in any case within 24 hours under each sponsor agreement.
- Report to Visa within 3 calendar days of reasonable suspicion; send the incident report within 3 calendar days after that notice; send at-risk account numbers within 3 calendar days of setting the window of exposure. Follow each other brand's rules through the banks.
- Engage a PFI when a brand requires one (WTDIC Section A.5).

### 7.3 FTC notice (16 CFR 314.4(j))
- **Notification event?** The clearing files were taken from the MFT appliances where they sit before file-level encryption is applied, so the PANs were acquired unencrypted without authorization (314.2(m)). Yes.
- **Who counts?** Cardholders are the customers of their issuing banks, but the rule covers that information in the company's possession (314.1(b)), and the company counts affected cardholders toward the 500 (conservative reading; counsel confirms).
- **Content:** company name and contact, data types, date range, number of consumers, a general description, and whether law enforcement asked in writing for a delay (314.4(j)(1)(i)-(vi)).
- **Deadline:** as soon as possible and no later than 30 days after discovery.

### 7.4 NYDFS notice for Cris Santos Payouts, LLC (23 NYCRR 500.17(a))
- **Is it a cybersecurity incident for the subsidiary?** The event occurred at its affiliate (the parent) on shared systems the subsidiary adopted. It has a reasonable likelihood of materially harming a material part of the subsidiary's normal operations, because payouts depend on settlement outputs (500.1(g)(2)). The parent's notices to the banks are notices to supervisory bodies, which may also meet 500.1(g)(1) if the subsidiary is affected. Yes.
- **Deadline:** as promptly as possible and no later than 72 hours after the determination, through the NYDFS portal, with updates as facts change (500.17(a)(2)).
- **Extortion payment:** if any payment is made, notice within 24 hours and an explanation within 30 days (500.17(c)).

### 7.5 Merchants and state law
- **Is it a state-law breach?** It depends on the stolen elements and each state's definition. Florida worked example: a card number is personal information only together with the person's name and any required security code (501.171(1)(g)). The clearing files have no names or security codes, so they are not Florida personal information. The funding files have business bank account numbers but no access codes, so they are not either. Counsel checks each state where affected individuals reside, because definitions differ.
- **Where a state's definition is met,** the company is a third-party agent for its merchants and must notify each affected merchant (Florida: no later than 10 days after determination, 501.171(6)(a)) and give them what they need for their own notices.
- **Contract notices go out regardless:** merchants, ISV partners, and enterprise merchants are notified under their agreements, after the banks.

### 7.6 Notice clock table and worked example (fictional dates)
Ransomware note found Tuesday 2027-03-09 at 02:05 Eastern; severity 1 declared at 02:20.

| Clock starts | Action | Deadline in the example | Owner |
|---|---|---|---|
| 4-hour determination, 2027-03-09 03:30 | 53.4, 304.24, and 225.303 notices to the designated contacts of Banks A, B, and C | As soon as possible (sent 03:50) | Chief Compliance Officer |
| Reasonable suspicion of account data compromise, 2027-03-09 15:00 (forensics confirms clearing files left the MFT) | Acquiring banks (Visa A.3.1; sponsor agreements) | Immediately; contract outer limit 2027-03-10 15:00 | Chief Compliance Officer |
| Same | Visa compromise report | 2027-03-12 | Chief Compliance Officer |
| Discovery, 2027-03-09 | FTC notice (if 500 or more consumers) | 2027-04-08 | Chief Compliance Officer with counsel |
| NYDFS determination, 2027-03-09 10:00 | NYDFS 72-hour notice for the payouts subsidiary | 2027-03-12 10:00 | Chief Compliance Officer |
| Committee convenes 2027-03-10; materiality determined Thursday 2027-03-11 at 17:00 | Form 8-K Item 1.05 | 2027-03-17 (4 business days: March 12, 15, 16, and 17) | General Counsel |
| Breach determination for any state whose definition is met | Third-party agent notices to merchants (Florida outer limit 10 days) | For a determination on 2027-03-12: 2027-03-22 | Chief Compliance Officer |

**Plan to the shortest clock.** The bank notices come first (minutes to hours), then the 24-hour contractual notices, then the NYDFS 72 hours and Visa's 3 calendar days, which end on the same day in this example. The 8-K follows on 2027-03-17 and the FTC deadline last. Every notice must tell a consistent story, so the Chief Compliance Officer and the General Counsel review each one against the facts log.

**Ransom decision:** requires the CEO, the General Counsel, and the insurer, plus an OFAC sanctions check (POL-03 4.8). Report to the FBI or Secret Service and CISA; timely reporting is a mitigating factor in OFAC's advisory. Paying does not remove any notice or disclosure duty, and any payment triggers the NYDFS 24-hour notice.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 7), in a clean environment first:
1. Identity platform, PAM vault, and break-glass access
2. Network core, card network links, DNS, and the DC-1 to Cloud A interconnect (with the management subnet path closed)
3. Cyber Fusion Center tooling for validation
4. Payment HSMs (verify from HSM audit logs that no key material was exported)
5. Authorization platform (if it was stopped) and token vault
6. Settlement platform in DC-2 or on rebuilt servers: reconcile from journaled records, regenerate funding files with control totals, release with dual approval, and agree the delivery window with each bank
7. Clean MFT path (fixed appliances or manual portal upload)
8. Payouts platform, once settlement outputs are validated
9. Treasury workstations and bank portals
10. Contact centers and portals (merchant status messages throughout)
11. Chargebacks, onboarding, reporting feeds

**Validate before reconnecting:** EDR clean, credentials rotated, patched, logging to the SIEM, and the PFI or forensic firm agrees. Tell banks, merchants, and partners when funding and file delivery return to normal (RC.CO).

## 9. Earlier event: PAN in a data lake table (2026-07)
On 2026-07-27 monthly PAN discovery found about 410,000 full, unencrypted PANs in a data lake analytics table. A settlement extract job had written them since 2026-05-21 after a schema change. The table was purged on 2026-07-29 after access logs were preserved. The notice analysis, completed by the Chief Compliance Officer with counsel on 2026-08-04:

- **Access.** Access to the table was limited to 23 analysts and data engineers through SSO. Logs for the whole window show only scheduled feature jobs and aggregate queries; no query selected the PAN column and no export occurred. The table held PAN, expiry date, and transaction data: no names and no security codes.
- **FTC.** The logs are reliable evidence that there was no unauthorized acquisition, which rebuts the presumption in 16 CFR 314.2(m). **Not a notification event.**
- **Card brands and banks.** No reasonable suspicion of unauthorized access to account data, so no Visa compromise report was due. No covered service was disrupted, so no 53.4, 304.24, or 225.303 notice was due. The three banks' compliance contacts were told on 2026-08-05 as a PCI DSS compliance matter.
- **NYDFS.** No act or attempt to gain unauthorized access occurred, so there was no cybersecurity event and no 500.17(a) notice.
- **State law.** No names or security codes were stored with the PANs, so the data was not personal information under Fla. Stat. 501.171(1)(g); counsel checked other states' definitions with the same result.
- **SEC.** Reviewed by the General Counsel; not material, so the disclosure committee was informed but did not convene.
- **PCI DSS.** Handled under 12.10.7 and disclosed to the QSA for the 2026 ROC. Root cause fix and wider PAN discovery are tracked in POAM-014.

## 10. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; root cause analysis and written report within 30 days (POL-03 4.11; 23 NYCRR 500.16(a)(1)(viii)).
- Update the risk register (P01: R-001, R-002, R-003, R-004, R-012, R-013), the POA&M (P07), this runbook, the materiality playbook, and the bank contact register.
- Give the QSA the incident report, the PFI report, and remediation evidence; a brand or bank may require an out-of-cycle assessment.
- The disclosure committee reviews the incident's effect on the next Item 106 disclosure; the CISO includes it in the annual report to the board (16 CFR 314.4(i); 500.4(b)).
- Keep all records, including determinations, clock tables, and notices, for at least 5 years (POL-01 4.11).

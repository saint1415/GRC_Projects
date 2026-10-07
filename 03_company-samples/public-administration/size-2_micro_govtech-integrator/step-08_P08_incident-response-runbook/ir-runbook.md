# Incident Response Runbook: Ransomware That Reaches Agency Data (CJI, and Access to FTI)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Micro / Public Administration |
| Incident type | A phishing email gives an attacker a company laptop and its sessions, and through them other laptops. The attacker encrypts the integration server (SYS-02) and its export bucket, pulls or deletes CJI in the AC-01 workspace, and may use a sign-in saved on an SC-01 laptop to try the revenue agency's virtual desktop, where FTI lives |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| System | Hosted Case Management Service (HCMS), per the SSP (P02) |
| Runbook owner | Operations Manager (Security and Compliance Officer) |
| Approved | 2026-08-31 by the owner |
| Last tested | Not yet. First tabletop with the MSP and the AC-01 LASO due 2026-11-30 (POAM-009) |

**Why this incident.** It is the company's only Very High risk (P01 R-001) and it drives the High risks R-002, R-004, R-005, and R-012. Today an administrator laptop holds the platform administrator session and the SSH keys to SYS-02, the 2 laptops approved for SC-01 hold the agency's virtual desktop client and saved sign-in names, and the exports sit in the same account as the server (P04 findings 1 and 2). The MSP's remote tool reaches all of them (R-012).

**Whose clocks.** Most legal clocks in this incident belong to the **customers**: the sheriff's CJIS reporting, the revenue agency's 24-hour TIGTA and IRS report, and the 12-hour ransomware reports of the county and cities. The company's job is to tell each of them fast enough and give them the facts they must report. The company's own legal clock is the 10-day third-party agent notice under Fla. Stat. 501.171(6)(a). All obligations are in `notification-matrix.csv`.

## 0. Roles and notification chain (Govern)
The company has 7 people and no security team. The MSP handles laptops and the suite; the cyber insurer supplies breach counsel and forensics; the Lead Platform Engineer handles the platform tenant and SYS-02.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead and agency notices | Operations Manager | Owner | Company mobile phones (numbers on the printed contact card) |
| Technical lead (platform tenant, SYS-02) | Lead Platform Engineer | Owner (holds platform administrator access and the second SSH key) | Company mobile phone |
| Decision maker (money, ransom, customer communication) | Owner | Operations Manager | Company mobile phone |
| Laptops and suite | MSP emergency line (in the MSP contract) | MSP lead technician's mobile | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel firms | n/a | Assigned by the insurer on the first call |
| Platform vendor and IaaS provider | Security incident channels in the support portals | Account managers | Portal and phone |
| Customer and prime contacts | AC-01 LASO; AC-02 IT security liaison; AC-03 and AC-04 IT managers; prime's security officer and the revenue agency's disclosure officer | Named alternates in each contract | Printed contact card |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** staff member → Operations Manager → Lead Platform Engineer, MSP emergency line, and owner (at the same time) → AC-01 LASO, prime and revenue agency, and the 3 other customers (Operations Manager) → insurer hotline (owner) → counsel and forensics (through the insurer).

**Out-of-band first.** Assume the attacker can read company email, chat, and the helpdesk. Coordinate by phone on company mobiles, using the printed contact card. Keep the incident log on the paper template in the binder until a clean account is confirmed. **Never put CJI or FTI in the log, email, chat, or tickets** (POL-03 4.3).

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder with the owner, the Operations Manager, and the Lead Platform Engineer: this runbook, the notification matrix, the contact card, the agency fact sheet template (section 6.2), and the paper incident log
- [ ] Write-once exports in a separate account, every 4 hours for AC-01 and AC-02, restore-tested within the last 90 days (CP-9, CP-4). **Gap until POAM-008 closes (2026-11-30).** Today the exports sit next to SYS-02 and can be deleted with the key stored on it
- [ ] Platform and SYS-02 logs copied weekly to write-once storage and kept 1 year (AU-11). **Gap until POAM-007 closes (2026-10-31)**
- [ ] Separate administrator accounts used only for administration (AC-6). **Gap until POAM-002 closes (2026-10-31)**
- [ ] SSH only through the MFA-protected session service; no SSH keys on laptops (IA-2(1)). **Gap until POAM-003 closes (2026-12-31)**
- [ ] MSP-managed EDR with after-hours alerting (SI-4). **Gap until 2026-12-31 (P01 R-001)**
- [ ] All staff briefed on the 1-hour reporting rule (POL-03 4.2; briefing 2026-09-15)
- [ ] Insurer hotline and policy number checked at each renewal; contact card checked each quarter against the contracts (POL-02 A.10)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A staff member clicked a link or opened an attachment and then saw an unexpected MFA prompt, or files will not open, or a ransom note appears | Staff report | **Disconnect the laptop from the network (Wi-Fi off). Do not turn it off.** Call the Operations Manager |
| The nightly sheriff load or the nightly export fails; SYS-02 does not answer | Job failure email; Lead Platform Engineer | Lead Platform Engineer checks from the IaaS console (not SSH) and calls the Operations Manager |
| Platform administrator sign-in from an unfamiliar place, a bulk export, or mass deletion of records | Platform audit log; agency users report missing cases | Lead Platform Engineer disables the account and opens an incident |
| Antivirus alert on a laptop that is not cleared automatically | MSP console | MSP isolates the laptop and calls the Operations Manager |
| The revenue agency or the prime reports an unusual sign-in to the virtual desktop with a company person's account | Prime or agency | Treat as a possible FTI incident; declare |
| Extortion email, or a leak-site post naming the company or a customer | Email; customer; law enforcement | Do not reply. Save the message. Declare |

**Declare a ransomware incident** when any company laptop, SYS-02, the exports, or a workspace is encrypted, deleted, or locked by an unauthorized actor; when an unknown actor has used administrator rights; or when anyone claims to hold company or agency data. When in doubt, declare. **The first notices to customers are for suspected incidents.**

**Write down the time of discovery (T0)** in the paper log. These clocks start there:
- the 1-hour report to the AC-01 LASO (CJISSECPOL v6.1 IR-6; AC-01 contract);
- the revenue agency's 24-hour TIGTA and Office of Safeguards report, which must not wait for an internal investigation (Pub. 1075 sec. 1.8.4), so the company calls the prime and the agency at once;
- the counties' and cities' 12-hour ransomware reports, which run from **their** discovery, which in practice is the company's call (Fla. Stat. 282.3185(5)(b)).

The 10-day clock under Fla. Stat. 501.171(6)(a) starts when the company determines a breach occurred "or reason to believe the breach occurred," which in a data-theft case can be the same day.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the paper incident log; record T0 and the trigger | Operations Manager | Log open |
| 2. Isolate the laptop: MSP isolates it through its console; the person does not use it again. Do not power it off | MSP; staff member | MSP confirms isolation |
| 3. Cut the attacker's access to agency data: from a clean laptop (the spare), the owner or Lead Platform Engineer signs in to the platform with the owner's administrator account, ends all sessions, disables the affected administrator account, and turns off bulk export for all roles. In the IaaS console, revoke the bucket access key and stop SYS-02 network access with a deny-all security group (keep the server running for evidence) | Lead Platform Engineer or owner | No active sessions except the responders'; SYS-02 isolated |
| 4. Protect the revenue agency: the Operations Manager asks the prime and the agency to disable the affected person's virtual desktop account and to check its sign-ins | Operations Manager | Agency confirms the account is disabled |
| 5. **Call the customers (suspected incident):** AC-01 LASO first, then the prime and the revenue agency's disclosure officer, then AC-02, AC-03, and AC-04. Say what is known, what is not, and when the next update comes. Ask AC-01 to suspend the sheriff's file drop credential | Operations Manager | Each contact reached by phone; call time logged; written follow-up through the agreed channel |
| 6. Call the cyber insurer's breach hotline; engage counsel and forensics through the panel | Owner | Claim number issued; counsel assigned |
| 7. Reset the suite password and MFA of every staff member from a clean device, starting with administrators; MSP checks for forwarding rules and new app consents | MSP with Operations Manager | Done for all 7 |
| 8. Put a neutral status message on the helpdesk portal and tell staff, by phone, who speaks to customers | Implementation and Support Analyst; Operations Manager | Message posted; staff briefed |

**Do not** delete attacker files or rebuild anything yet, and do not restore into the compromised IaaS account. Evidence and a clean rebuild come first.

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP and the Lead Platform Engineer supplying access and logs.
1. **Scope.** Which laptops, accounts, workspaces, and cloud resources did the attacker touch? Sources: MSP antivirus console, suite sign-in and mail logs, platform audit log (90 days kept, so export it now), IaaS account activity log, SYS-02 logs (14 days kept, so copy them now).
2. **Initial access.** Find the phishing email and remove it from every mailbox. Image the affected laptop through the MSP.
3. **Preserve evidence.** Forensics images the laptop and SYS-02 disk and exports the platform, suite, and IaaS logs before they roll off. Keep a chain-of-custody record (who collected what, when, with hashes) and store evidence in a new storage account only the Operations Manager and the forensic firm can reach.
4. **Data theft.** Did data leave? Check platform export events and record views, SYS-02 outbound traffic (no flow logs today, so use the IaaS billing and network metrics), and suite downloads. **This drives every breach decision.** For each workspace, record the number of records and the data elements involved (CJI and CHRI; Social Security numbers; driver license numbers) and where affected people live.
5. **FTI.** Ask the prime and the agency for the virtual desktop sign-in history of the affected person's account. If anyone other than the person signed in, or if that cannot be ruled out within 24 hours, the agency's TIGTA and Office of Safeguards report goes ahead (Pub. 1075 sec. 1.8.2-1.8.4). The company confirms within 24 hours that it did.
6. **Backups.** Find the last clean export for each workspace and confirm with the platform vendor which tenant restore points (14 days) predate the attack.
7. **Agency facts.** Keep one fact sheet per customer (section 6.2), updated at least every 12 hours.

## 5. Containment and eradication (RS.MI)
1. Remove attacker changes in the platform: new users, roles, API tokens, and workflow changes; compare with the last exported configuration in the repository.
2. Rotate every secret: platform service account, sheriff file-drop credential (with sheriff IT), bucket keys, and any token in the repository.
3. Rebuild SYS-02 from the repository scripts in a **new, clean IaaS account**, with SSH closed and the FIPS 140-3 certified mode on (P05 recovery priority 5).
4. The MSP reimages every laptop that shows the same indicators from its standard build. **Do not decrypt and reuse them.**
5. Forensics confirms that no persistence remains, including in the MSP's remote management platform, before anything reconnects. If the MSP's tools may be the entry point, the owner asks the forensic firm to lead and requires the MSP to share its own investigation (P01 R-012).

## 6. Reporting and communication (RS.CO)
### 6.1 Notice timeline
**Follow `notification-matrix.csv`.** Counsel reviews every written notice. T0 is the recorded discovery time.

| When | Action | Owner |
|---|---|---|
| T0 + 1 hour | Phone notice of a suspected incident to the AC-01 LASO (CJISSECPOL IR-6), the prime and the revenue agency (Pub. 1075 sec. 1.8.2), and AC-02, AC-03, AC-04 (POL-03 4.4) | Operations Manager |
| T0 + 1 hour | Insurer breach hotline | Owner |
| T0 + 4 hours | First written fact sheet to each affected customer (section 6.2), so the county and cities can file within their 12 hours | Operations Manager |
| Customer T0 + 12 hours | AC-02, AC-03, AC-04 report the ransomware incident to the Cybersecurity Operations Center, the FDLE Cybercrime Office, and their sheriff (Fla. Stat. 282.3185(5)(b)) | Customers, with company facts |
| T0 + 24 hours | The revenue agency reports to TIGTA and the IRS Office of Safeguards if FTI involvement cannot be ruled out (Pub. 1075 sec. 1.8.4). The company confirms the report was made, and contacts TIGTA directly if it cannot confirm | Revenue agency; Operations Manager confirms |
| As the state CSA requires | AC-01 reports the security violation to the CSO and the FBI (Security Addendum sec. 4.01) | AC-01, with company facts |
| Within 48 hours | Voluntary report to the FBI (IC3) and CISA, coordinated with the customers | Owner |
| No later than 10 days after determining a breach | Written third-party agent notice to each affected agency with all the information it needs for its own notices (Fla. Stat. 501.171(6)(a)) | Operations Manager and counsel |
| Customer: 30 days after determination | Florida individual notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 (Fla. Stat. 501.171(3)-(5)). The company sends notices for an agency only if asked (501.171(6)(b)) | Customers |
| Customer: 1 week after remediation | After-action report to the Florida Digital Service (Fla. Stat. 282.3185(6)) | AC-02, AC-03, AC-04, with company input |

**Plan to the shortest clock.** The 1-hour CJI notice comes first, and the 12-hour Florida reports and the 24-hour IRS report run on the customers' side. A company that waits for its own investigation leaves its customers in breach of their rules.

### 6.2 Fact sheet for customer reports
Florida local government reports and the IRS data incident report ask for specific facts (Fla. Stat. 282.3185(5)(a); Pub. 1075 sec. 1.8.3). Keep one fact sheet per customer, with no CJI or FTI in it:
- summary of facts; date and time the incident occurred and was discovered; how it was discovered
- the date of the most recent backup of the customer's data, where it is, whether it was affected, and that it is cloud-based
- types of data and data elements involved; potential number of records (a range if unknown)
- systems involved (platform tenant, SYS-02, laptops) and where (U.S. cloud regions); whether a company employee was involved
- estimated fiscal impact to the customer, if known; details of any ransom demand
- the company's contact and the time of the next update

### 6.3 Ransom decision
- Florida state agencies, counties, and municipalities **may not pay or otherwise comply with a ransom demand** (Fla. Stat. 282.3186). The data belongs to the customers; the company will not negotiate over agency data that any customer objects to.
- Any payment by the company requires the owner, counsel, the insurer, consultation with every affected customer, and an OFAC sanctions check (POL-03 4.7).
- Paying does not remove any notice duty if data was taken.

### 6.4 Other communications
- Agency users: helpdesk portal status updates at least every 4 hours while a workspace is down (Implementation and Support Analyst).
- Media: only the owner speaks, and only after the affected customers have seen the statement. The revenue agency shares any media release about FTI with the Office of Safeguards before release (Pub. 1075 sec. 1.8.5).
- Staff: a short script from the Operations Manager; no posts or outside discussion.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05 section 6).

| Priority | Resource | Target |
|---|---|---|
| 1 | Customer communications: contact card, company phones, helpdesk status message | 1 hour |
| 2 | Staff identity from a clean laptop: suite and platform administrator access | 2 hours |
| 3 | Platform tenant check: AC-01 and AC-02 workspaces intact, or vendor tenant restore requested (up to 48 hours) | 4 hours (check) |
| 4 | AC-01 and AC-02 workspaces back in service, from intact data, a clean export, or the vendor restore | 24 hours (contract RTO) |
| 5 | SYS-02 rebuilt in a clean account; sheriff file replayed from the 7-day drop | 24 hours |
| 6 | AC-03 and AC-04 workspaces | 72 hours |
| 7 | Approved laptop for SC-01 (the agency CISO must approve any replacement device) | 24 hours after approval |
| 8 | Repository, release tooling, implementation work, billing | 48 to 72 hours |
| 9 | AI pre-screening (only after the P10 conditions are met) | After all others |

**Warning (current state).** If the attacker deleted the exports and records in the workspaces, the only other copy is the vendor's full-tenant restore, which takes up to 48 hours and rolls back **every** workspace to the same point (R-004, POAM-008). Tell the customers this early so they can plan paper work: pretrial officers run from printed rosters, and AC-02 caseworkers take paper applications (P05 section 4). Cases entered since the restore point must be re-keyed by agency staff.

**Validate before reconnecting:**
- Forensics confirms the environment is clean; all secrets are rotated.
- Record counts for each workspace match the last known good figures.
- SYS-02 runs the FIPS 140-3 certified mode for the sheriff transfer (SC-13; POAM-011).
- Each customer's security contact approves reconnection. For AC-01, the LASO confirms whether the state CJIS Systems Agency must approve first. For SC-01, the prime and the agency approve any device before it connects again.

Tell agency users when each workspace is back (RC.CO). Customers keep their paper workarounds until their process is back within its RTO (P05).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP and counsel; written summary within 30 days (POL-03 4.10). Invite the AC-01 LASO.
- Refresher security awareness training within 30 days for staff involved, as the CJIS Security Policy requires (CJISSECPOL v6.1 AT-2; POL-03 4.10).
- Update the risk register (P01, especially R-001, R-002, R-004, R-005, R-012), the POA&M (P07), the BIA (P05), and this runbook.
- Give each county and city its after-action input within 1 week of remediation (Fla. Stat. 282.3185(6)).
- Keep the incident log, evidence, and notices at least 3 years, or longer if a customer or the insurer requires (POL-03 4.11).

# Incident Response Runbook: Compromise of the Payment Processing Environment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (payment processor serving merchants) |
| Tier / Vertical | Small / Financial Services |
| Incident type | Compromise of the payment processing environment. An attacker uses a former contractor's still-active code repository token to push a malicious change to the hosted payment page script and the API gateway, captures card data from e-commerce transactions, and exfiltrates it over DNS |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | IT Manager (Information Security Lead) |
| Approved | 2026-08-31 by the COO |
| Last tested | Not yet. First tabletop exercise on this scenario due 2026-10-31 (POAM-015) |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Manager | Platform Engineering Lead | Security on-call phone, then the out-of-band group on personal phones |
| Technical lead (cloud, pipeline) | Platform Engineering Lead | CTO | On-call phone |
| Notices and card brand liaison | Compliance and Risk Manager | COO | Cell |
| Executive decisions | COO | Majority owner and CEO | Cell |
| Legal counsel | Outside breach counsel (insurer panel) | n/a | Through the insurer hotline |
| Cyber insurer | Carrier breach hotline | n/a | Policy card in the incident binder |
| PCI Forensic Investigator (PFI) | Firm from the PCI SSC list, engaged through counsel | n/a | Engaged on day 1 if a brand requires it |
| Sponsor bank | Designated security and compliance contacts (**to be recorded by 2026-09-30, POAM-014**) | Bank CEO and CIO (fallback under 12 CFR 53.4(a)(2)) | Numbers in the incident binder |
| Managed detection service | 24x7 analyst line (from 2026-11-30, POAM-003) | n/a | Service portal and phone |
| Law enforcement | U.S. Secret Service or FBI field office | IC3 | Numbers in the incident binder |

**Out-of-band first.** The attacker controlled a repository token and may be watching chat, email, and ticketing. Coordinate on personal phones and the printed contact list in the incident binder at the office and at the IT Manager's home.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed incident binder: this runbook, contacts, the notification matrix, and the network and data-flow diagrams (POAM-007)
- [ ] Payment page script inventory, integrity checks, and tamper-detection live (PCI DSS 6.4.3, 11.6.1). **Gap until POAM-001 closes (2026-10-15)**
- [ ] Two approvals for CDE deployments; signed builds; alerts on console changes (CM-3). **Gap until POAM-002 closes (2026-09-30)**
- [ ] Repository tokens tied to single sign-on and expiring within 30 days; termination checklist covers tokens (POL-02 4.5, 4.9). **Gap until POAM-005 closes**
- [ ] DNS query logging with tunneling detection and egress intrusion detection (PCI DSS 11.5.1.1). **Gap until POAM-003 (egress part) closes 2026-10-31**
- [ ] 24x7 alert monitoring (PCI DSS 10.4.1, 12.10.5). Interim on-call from 2026-10-15 (POAM-009)
- [ ] Sponsor bank designated contacts on file and confirmed this quarter (12 CFR 53.4(a)(1))
- [ ] PFI shortlist and insurer panel confirmed; counsel retainer active
- [ ] Break-glass cloud accounts sealed and tested (POL-02 4.1)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Payment page script or header changed outside an approved release | Tamper-detection service (after POAM-001) | On-call engineer confirms against the release record within 30 minutes; if unapproved, declare |
| DNS queries with long, random subdomains from a CDE subnet, or DNS volume spike | DNS tunneling detection (after POAM-003) | Block the domain at the resolver; declare |
| Repository push or pipeline run with a token of a departed person, or from an unusual location | Repository audit log alert in the SIEM | Revoke the token; review the change; declare if it reached production |
| Common point of purchase alert: the sponsor bank or a card brand says fraud traces back to the company's merchants | Sponsor bank, card brand | Declare immediately. **This starts the Visa 3-day clock (reasonable suspicion)** |
| Several e-commerce merchants report customer fraud after checkout | Merchant support | Escalate to the IT Manager; compare with payment page changes |
| QSA, ASV, or researcher reports unexpected script on the payment page | External report | Declare |

**Declare a payment environment compromise when** any unapproved code is found running on the hosted payment page, API gateway, or other CDE component, or a brand or the bank reports a common point of purchase.

**Record the time of discovery and the time of reasonable suspicion.** Several clocks start from them:
- Visa: 3 calendar days from reasonable suspicion or confirmation.
- FTC: the event is discovered on the first day it is known to any employee, officer, or agent other than the attacker (16 CFR 314.4(j)(2)).
- Florida third-party agent notice: 10 days from determination of the breach or reason to believe it occurred (Fla. Stat. 501.171(6)).

## 3. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log (timeline, actions, who, when). Start the notice clock table in section 6 | IT Manager | Log open with discovery and suspicion times |
| 2. Revoke every repository and pipeline token; disable all pipeline deployments to the CDE; require re-authentication for all repository users | Platform Engineering Lead | No token older than the revocation time works; pipeline paused |
| 3. Replace the hosted payment page and payment form script with the last known-good signed version from the release archive. Do not delete the malicious version: copy it to evidence storage first | Platform Engineering Lead | Tamper-detection or a manual hash check confirms the known-good version is served |
| 4. Roll back the API gateway to the last known-good image on fresh containers. Keep the compromised containers stopped but not deleted (snapshot their storage) | Platform Engineering Lead | Gateway runs the known-good image; compromised containers preserved |
| 5. Block the exfiltration domain(s) at the DNS resolver and deny all DNS from CDE subnets except to the approved resolver | Platform Engineering Lead | Test query to the attacker's domain fails |
| 6. Call the cyber insurer; engage counsel; engage a PFI through counsel if a brand requires one | COO | Claim number; counsel engaged |
| 7. Notify the sponsor bank's designated contacts (suspected account data compromise) | Compliance and Risk Manager | Notice sent and acknowledged; time recorded |
| 8. **12 CFR 53.4 check:** will containment disrupt clearing, settlement, reconciliation, or merchant funding files for 4 or more hours? (Section 6.2) | Incident commander with the Compliance and Risk Manager | Decision and reason recorded |

**Keep authorizations running if it is safe.** Card-present authorization and the funding engine were not changed by the attacker in this scenario. Stopping them would harm 4,200 merchants and may trigger a 53.4 notice. Stop a component only when forensics or the PFI shows it is affected.

## 4. Analysis (RS.AN)
1. **Initial access.** Identify the token that pushed the change, whose it was, when it was created, and every action it took (repository audit log, pipeline logs, cloud audit logs). In this scenario: a token belonging to a contractor who left in 2025.
2. **What changed.** Diff the malicious commit(s) against the last known-good release for the payment page script and the API gateway image. Look for other pushes by the same token.
3. **Window of exposure.** First malicious deployment to containment. Use pipeline deployment records and content delivery service logs to set it precisely. Visa requires at-risk accounts within 3 calendar days of setting the window of exposure.
4. **What was taken.**
   - Work out which data elements the skimmer captured: name, PAN, expiry, card verification code, billing address.
   - Count the affected transactions, cards, and merchants from authorization records inside the window, split by brand and by the cardholder's state where known.
5. **Exfiltration path.** Confirm DNS tunneling from resolver logs (if available) or the gateway's own logs. Identify the attacker's domains and IPs.
6. **Preserve evidence.**
   - Snapshot the compromised container storage.
   - Export repository, pipeline, cloud, SIEM, and resolver logs before they roll over.
   - Hash every artifact.
   - Keep chain of custody in the incident log.
   - Give the PFI read-only access. Follow Visa's evidence rules: do not access or alter compromised systems with administrator credentials, and do not reboot them.
7. **Other CDE components.** Check the token vault, HSM service logs, and settlement engine for access by the attacker. Key material exposure would change every downstream decision (encrypted data counts as unencrypted under 16 CFR 314.2 if the key was accessed).

## 5. Containment and eradication (RS.MI)
1. Rotate every secret the pipeline could read: API gateway TLS keys (through the HSM service), service account credentials, and third-party API keys.
2. Remove all personal access tokens. Re-enable deployments only after two-approval rules and signed builds are in force (POAM-002).
3. Rebuild the API gateway and payment page from clean source after reviewing every commit in the window of exposure.
4. Add the attacker's domains and IPs to blocklists. Keep the DNS lockdown in place.
5. Confirm with the PFI or forensic firm that no persistence remains before declaring eradication complete.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every legal notice before it goes out. The Compliance and Risk Manager keeps the clock table.

### 6.1 Notice clock table
| Clock starts | Action | Deadline | Owner |
|---|---|---|---|
| Reasonable suspicion or confirmation | Sponsor bank (Visa WTDIC A.3; sponsor agreement) | Immediately; no later than 24 hours (contract) | Compliance and Risk Manager |
| Reasonable suspicion or confirmation | Report the compromise to Visa (through the sponsor bank) | 3 calendar days | Compliance and Risk Manager |
| Notice to Visa | Incident report to Visa and the acquiring bank | 3 calendar days after notice | IT Manager |
| Window of exposure set (or discovery, or Visa request) | At-risk account numbers to Visa | 3 calendar days | Settlement Operations Manager with the IT Manager |
| Determination that covered services were or will be disrupted 4+ hours | 12 CFR 53.4 notice to bank-designated contacts | As soon as possible | Compliance and Risk Manager |
| Determination of breach or reason to believe | Notice to affected merchants as their third-party agent (Florida 501.171(6); other states vary) | As expeditiously as practicable; Florida outer limit 10 days | Compliance and Risk Manager with counsel |
| Discovery (known to any employee) | FTC notice if 500+ consumers (16 CFR 314.4(j)) | As soon as possible; no later than 30 days | Compliance and Risk Manager with counsel |
| Day 0 to 2 | Voluntary report to the U.S. Secret Service or FBI | As soon as practicable | IT Manager |
| Other card brands | Each brand's incident rules, through the sponsor bank | Per brand rules (confirm with the sponsor bank) | Compliance and Risk Manager |

**Plan to the shortest clock.** Visa's 3 calendar days will arrive first. Merchants then need the company's notice early, because their own state-law clocks start when they learn of the breach.

### 6.2 12 CFR 53.4 decision (bank service provider notice)
- **Trigger:** a computer-security incident that has materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, covered services to the sponsor bank for four or more hours (12 CFR 53.4(a)).
- **What counts as covered services here:** clearing, settlement, reconciliation, and merchant funding files. The sponsor agreement names these as services subject to the Bank Service Company Act (12 U.S.C. 1867(c)).
- **Apply it to this scenario.** The skimming itself does not disrupt settlement or funding, so card theft alone does not trigger 53.4. If containment or the PFI's work stops the settlement and funding engine for 4 or more hours, or makes a missed daily cutoff likely, notify as soon as possible. Use the bank's designated contact, or its CEO and CIO if none is on file.
- **Record the decision either way.** The bank uses the company's information to decide whether it has its own 36-hour notice to the OCC under 12 CFR 53.3.
- **Not applicable today:** 12 CFR 304.24 (FDIC) and 225.303 (Federal Reserve). 304.24 will apply once the second sponsor agreement is signed.

### 6.3 FTC notice decision (16 CFR 314.4(j))
- **Is it a notification event?** Card data typed into a skimmed payment page is taken before encryption. That is acquisition of unencrypted customer information without the cardholder's authorization (314.2(m)). Yes.
- **Who counts?** Cardholders are the customers of their issuing banks. The rule covers that information in the company's possession (314.1(b)), and the company counts affected cardholders toward the 500 (conservative reading; counsel confirms).
- **What the notice contains (314.4(j)(1)(i)-(vi)):**
  - company name and contact
  - data types
  - date range
  - number of consumers affected
  - a general description of the event
  - whether law enforcement has asked for a delay in writing
- **Deadline:** as soon as possible and no later than 30 days after discovery.

### 6.4 Merchant and state-law notices
- For cardholder data the company is usually its merchants' **third-party agent**. It must give each affected merchant the information it needs for its own notices: no later than 10 days after determination under Fla. Stat. 501.171(6)(a), and within whatever each other state requires. The company may send notices on a merchant's behalf (501.171(6)(b)), but merchants remain responsible under that statute.
- Under Florida law, a card number is "personal information" only together with the person's name and any required security code or password (501.171(1)(g)). An e-commerce skimmer that captures name, PAN, and card verification code meets that definition.
- Where the company itself owns the data (for example merchant owner SSNs in onboarding), it is the covered entity and gives the individual, Department of Legal Affairs (500+ Floridians), and consumer reporting agency (more than 1,000) notices directly. The deadline is no later than 30 days after determination.

### 6.5 Communications
- Merchants: counsel-approved notice plus a support script, sent after the sponsor bank is informed.
- Software-platform partners: same content, under their contracts.
- Staff briefing: what happened, what not to say, where to send questions.
- No public statement without counsel and COO approval.

### 6.6 Earlier event: PAN in the data warehouse (R-031)
On 2026-08-05, control assessment testing (P07) found about 2.3 million full, unencrypted PANs in a data warehouse table used for fraud model training. A faulty extract job had written them since 2026-05-19. The table was purged on 2026-08-07 after access logs were preserved. The notice analysis, completed by the Compliance and Risk Manager with counsel on 2026-08-12:

- **Access.** Warehouse access is limited to 11 analysts and engineers through single sign-on. Access logs for the whole window show only the scheduled training job and aggregate queries by two data engineers. No query selected the PAN column, and no export occurred. The table held PAN only: no cardholder names, expiry dates, or security codes.
- **FTC.** The logs are reliable evidence that there was no unauthorized acquisition. Under 16 CFR 314.2(m), that rebuts the presumption, so this was **not a notification event**. No FTC notice.
- **State law.** No name or security code was stored with the PANs, so the data was not "personal information" under Fla. Stat. 501.171(1)(g). Other states' definitions were checked by counsel with the same result. No merchant or individual notice.
- **Card brands and 53.4.**
  - There was no reasonable suspicion of unauthorized access to account data, so no Visa compromise report was due.
  - No covered service was disrupted, so no 12 CFR 53.4 notice was due.
  - The sponsor bank's compliance contact was informed on 2026-08-10 as a PCI DSS compliance matter, not a compromise.
- **PCI DSS.** Handled under 12.10.7 (PAN found where not expected) and disclosed to the QSA for the 2026 ROC. Root cause fix and monthly PAN discovery are tracked in POAM-012.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Identity provider and administrator access (break-glass accounts if single sign-on is suspect)
2. Cloud network, payment HSM service, and card network links. Verify that no key material was exported (HSM audit log)
3. Authorization path (BP-01): known-good API gateway and hosted payment page, verified by hash
4. Log collection and alerting (BP-09), with the new DNS and egress detections
5. Settlement and funding engine (BP-03, BP-04): if it was stopped, reconcile the last processed file before restarting and confirm the daily cutoff with the sponsor bank
6. Merchant support and portal (BP-08, BP-07)
7. Pipeline deployments: only after two approvals, signed builds, and new tokens are in place

**Validate before closing:**
- the PFI or forensic firm confirms eradication
- tamper-detection has run clean for 7 days
- the DNS tunneling detection is tested
- no deployment happened outside the approved pipeline

Tell merchants when the payment page is confirmed clean (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update the risk register (P01: R-001, R-002, R-003, R-011, R-015), the POA&M (P07), POL-02 and POL-03 if needed, and this runbook.
- Give the QSA the incident report, the PFI report (if any), and the remediation evidence. A compromise may require an out-of-cycle assessment at the brands' or sponsor bank's request.
- Include the incident and management's response in the next Qualified Individual report to the CEO and COO (16 CFR 314.4(i)).
- Retain all incident documentation for at least 3 years (POL-01 4.15), or longer if counsel or a brand requires.

# Incident Response Runbook: Business Email Compromise and Taxpayer Data Theft Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Tax and Advisory, Wealth, Practice Cloud, and corporate shared services; CPA Partners on standby) |
| Tier / Vertical | Multi-Sector / Professional, Scientific, and Technical Services (focus division: CPA and Tax Services) |
| Incident type | Business email compromise and taxpayer data theft that starts in a tax office mailbox and spreads to Practice Cloud and Wealth through the shared email tenant (SYS-G4) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; POL-05 4.5 call-back rule; division supplements (P06). With POL-03, this runbook is part of Tax and Advisory's written incident response plan (16 CFR 314.4(h)) and Wealth's response program (17 CFR 248.30(a)(3)) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-10 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The combined notification matrix has not been exercised** (scenario gap 6); the first cross-division tabletop, using this scenario, is due 2026-12-15 (POAM-005) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative. Day 0 is a Thursday in late February, in the middle of the filing season.
- **Entry (Day -6):** a manager of a Florida tax office receives an email that imitates an IRS e-Services notice. The link opens an adversary-in-the-middle page that relays the sign-in, so number-matching MFA is completed by the manager and the attacker captures the session token (SYS-G1).
- **Mailbox takeover (Day -6 to Day -1):** the attacker creates inbox rules that hide messages containing "refund," "bank," and "transfer," and forwards mail externally. The manager's mailbox is on the 2019 forwarding exception list (P07 AC-4, SYS-G4), and tax office mailboxes have no inbox-rule alerts (P07 SI-4; POAM-004), so nothing fires.
- **Document theft (Day -5 to Day -2):** with the same session, the attacker opens the Tax and Advisory tenant of Practice Cloud. The manager has regional read access (P07 AC-6), so the attacker bulk-downloads client documents for about 38,000 returns: about **61,000 individuals** (about 54,000 Florida residents; the rest in 22 other states). The files include custodial statements of about **3,900 Wealth integrated planning households** (about 6,800 individuals) that Tax and Advisory holds for Wealth. Bulk-download alerts stay in the Practice Cloud console (SW-011).
- **Practice Cloud staff session (Day -3):** from the manager's mailbox, the attacker emails a Practice Cloud support engineer about a "failed tenant export" with a link to a fake ticket page and captures the engineer's session. Support access is ticket-linked and time-limited (SW-005), which limits the attacker to the **5 outside customer firms** with open tickets. The attacker downloads documents for about **7,200 of their end clients**.
- **Fraud (Day -2 to Day 0):** the attacker emails 14 office staff, as the manager, asking them to change refund bank accounts for 41 clients; 9 changes are made without the call-back, and **3 refunds (about $31,000)** are deposited to attacker accounts. The attacker also emails 26 Wealth advisers, as the manager, forwarding "client" transfer requests supported by stolen tax documents. Call-backs stop 3 of 4; **one wire of $240,000** passes second review because the request came from an internal sender (WM-G23 red flag gap).
- **Discovery (Day 0, 10:40):** a Wealth client calls about a transfer she did not request. Wealth operations reports to the group SOC, which links it to the manager's account within the hour.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO (Qualified Individual) | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC, identity, and collaboration services teams; Practice Cloud CISO for SYS-S1 | Forensic firm on retainer (through the insurer's panel) | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Group Chief Privacy Officer | Out-of-band bridge |
| Tax and Advisory decisions: IRS, state tax agencies, FTC, refund holds | Chief Tax Officer | Tax division security and compliance lead | Division bridge |
| Wealth decisions: Regulation S-P notices, red flags, custodians | Wealth Chief Compliance Officer | Wealth security and compliance lead | Division bridge |
| Practice Cloud customer notices | Practice Cloud trust and assurance director | Practice Cloud CISO | Division bridge |
| CPA Partners (standby) | CPA Partners risk and quality partner | CPA Partners managing partner | Called if SYS-T3 or CPA Partners mailboxes are involved |
| SEC materiality | Disclosure committee (chaired by the Group Chief Financial Officer) | Group General Counsel | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement and IRS | FBI field office or IC3; local IRS Stakeholder Liaison | n/a | Contacts in the offline incident binder |

**Out-of-band first.** One email tenant serves every division, so assume the attacker can read group email and chat. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts, this runbook, and the notification matrix.

## 2. Preparation checks (Identify / Protect)
- [x] 24x7 group SOC, EDR, SIEM, and email security gateway (SI-3, SI-4)
- [x] Session revocation and conditional access controls in SYS-G1 tested quarterly
- [x] Call-back rule for refund, payroll, and transfer changes (POL-05 4.5); Wealth second review over $50,000
- [x] Forensic retainer and insurer panel confirmed; disclosure committee charter includes cybersecurity incidents
- [ ] Inbox-rule and forwarding alerts on tax office mailboxes; Practice Cloud bulk-download alerts in the SIEM (**gap until POAM-004 closes**)
- [ ] Legacy authentication blocked on office intake mailboxes (**gap until POAM-002 closes**)
- [ ] Forwarding exception list cut to approved mailboxes (**gap until POAM-007 closes**)
- [ ] Daily review of refund bank-field changes and portal bulk downloads (**gap until POAM-010 closes**)
- [ ] Combined notification matrix adopted and exercised (**gap until POAM-005 closes**)
- [ ] Wealth red flags for internal senders and requests citing tax documents (**gap**, P03 WM-G23)

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A client reports a refund, payroll, or transfer change they did not request | Tax office, Wealth operations, client service | Report to the SOC within 1 hour (POL-03 4.1); hold the account |
| New inbox rule hiding finance keywords, or new external forwarding | SYS-G4 audit log, SIEM (corporate and Wealth today; tax offices after POAM-004) | Disable the rule; revoke sessions; triage |
| Sign-in from an unfamiliar network or a token replayed from a new device | SYS-G1 risk signals | Revoke sessions; reset credentials; review mailbox activity |
| Bulk download from a staff or support account | Practice Cloud alert console; SIEM after POAM-004 | Suspend the account; start triage |
| IRS or a state tax agency reports suspicious returns under a firm EFIN | IRS, state agencies, weekly EFIN volume check | Treat as a data theft incident; call the Chief Tax Officer |
| An internal email asks for a bank or transfer change for a client | Any employee | Call the client at the number of record; report to the SOC |

**Severity 1** (group scale, POL-03 4.2): confirmed theft of client data from more than one division, or any confirmed fraudulent movement of client funds. This scenario is Severity 1 on Day 0.

**Record each clock date for each entity** (POL-03 4.3) in the incident log:
- **Tax and Advisory, FTC:** discovery, the first day the event is known to any employee, officer, or other agent other than the attacker (314.4(j)(2)).
- **Tax and Advisory, IRS:** confirmation of the incident (Pub. 1345).
- **Wealth:** the day it becomes aware that unauthorized access occurred or is reasonably likely (248.30(a)(4)(iii)).
- **State law:** the determination of a breach (Florida worked example, 501.171(4)(a)).
- **Practice Cloud:** confirmation that a customer's data was affected (customer agreements).
- **Group:** the materiality determination (Form 8-K Item 1.05).

Because the group SOC serves every division, the day the SOC knows is treated as the day each affected entity knows. **Check for an earlier date.** In this scenario, an office staffer questioned a bank-change request on Day -2 but did not report it. Counsel decides whether that is "known" for 314.4(j)(2); until counsel decides, plan the FTC clock from Day -2.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Revoke all sessions and reset credentials for the manager and the support engineer; require new MFA registration in person | Group identity director | Sessions revoked; sign-ins from the attacker's infrastructure fail |
| 2. Remove the inbox rules and external forwarding; search the tenant for the same rules, sender, and phishing URL; purge the phishing emails from all mailboxes | Group collaboration services director; SOC | Search results logged; messages purged |
| 3. Suspend Practice Cloud support access to customer tenants except by two-person approval until scoping is done | Practice Cloud CISO | Support access policy changed |
| 4. **Money holds** (POL-03 4.8): hold all refund bank-account changes made in the manager's region in the past 30 days, all pending return releases with a changed bank account, and all Wealth transfers requested by email in the past 14 days, until verified by call-back | Chief Tax Officer; Wealth operations director | Hold lists signed off |
| 5. Call the custodian's fraud desk to recall the $240,000 wire; report it to the FBI or IC3 | Wealth operations director; Group CISO | Recall request and IC3 reference numbers recorded |
| 6. Preserve evidence: sign-in logs, mailbox audit logs, message traces, Practice Cloud download and support logs, SYS-T1 change history; legal hold (POL-03 4.11) | SOC; forensic firm | Evidence list signed |
| 7. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 8. On the bridge: corporate notifies Tax and Advisory, Wealth, and Practice Cloud; Tax and Advisory notifies Wealth as its service provider (this starts Wealth's awareness) | Incident commander; Chief Tax Officer | Each acknowledges in the incident log |
| 9. Brief the Group CISO; convene the disclosure committee within 24 hours of declaration (POL-03 4.7) | Group CISO | Committee convened |

## 5. Analysis (RS.AN)
1. **Scope by entity.** From Practice Cloud download logs, list every document the two hijacked sessions downloaded and map it to its owner: Tax and Advisory clients, Wealth integrated planning households, and each of the 5 outside customer firms. Practice Cloud logs record tenant, document, and staff account, so end-client lists can be produced for each tenant.
2. **Individuals by state.** For each notifying entity, count affected individuals by state of residence. These counts drive the FTC 500-consumer test, state notices, attorney general and consumer reporting agency notices, and the Florida Department of Legal Affairs notice.
3. **Data types.** Classify what was taken: SSNs, dates of birth, bank account numbers, wage and income documents, custodial statements, and identity documents. Most state definitions, and the Regulation S-P definition of sensitive customer information, are met by name with SSN or account number.
4. **Overlap.** Integrated planning households are customers of both Tax and Advisory and Wealth. Each entity still owes its own notice. A coordinated letter must identify both entities and meet both content rules (Florida and each other state; 248.30(a)(4)(iv)).
5. **Fraud already committed.** Confirm every refund bank change, return release, and transfer request linked to the attacker. Give the IRS the 9 changed returns and 3 diverted refunds. Wealth logs each red flag and response (248.201(d)(2)(iii)).
6. **Scope checks.** Confirm that SYS-T3 (attest), CPA Partners mailboxes, SYS-T1 itself (as opposed to the portal), and SYS-W1 were not accessed. If any were, add their owners to the matrix.
7. **Root cause.** Session-token phishing defeated number-matching MFA; no inbox-rule alerts for tax offices; regional read access; a forwarding exception; trust in internal senders. Feed these to P01 GR-02, GR-20, TX-001, TX-002, TX-007, WM-001, SW-005, and SW-011.

## 6. Containment and eradication (RS.MI)
1. Require phishing-resistant MFA for all office managers and Practice Cloud support engineers before restoring their access (extends the administrator standard in POL-02 4.4).
2. Remove the regional read access of all office managers now, ahead of POAM-008.
3. Remove the 37 unneeded forwarding exceptions now (POAM-007) and block external forwarding for all tax office mailboxes.
4. Release held refunds and transfers only after a recorded call-back. Re-sign returns whose bank details changed (TX-002 control).
5. Block the attacker's domains and infrastructure at the email gateway and web proxy; add the lure to the next phishing exercise.
6. Confirm with forensics that no persistence remains (other inbox rules, OAuth app consents, registered devices) before closing containment.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (34 rows).** Counsel approves every external notice (POL-03 4.5). The matrix has four layers:
1. **Inside the group:** corporate notifies the divisions; Tax and Advisory notifies Wealth as its Regulation S-P service provider (72 hours at most, applied now although the 2022 agreement lacks the term).
2. **Tax and Advisory's own duties:** FTC (500 or more consumers), IRS (next business day after confirmation), state tax agencies, and state breach laws.
3. **Wealth's own duties:** Regulation S-P notices to about 6,800 individuals within 30 days of becoming aware, incident records, red flag response, and the custodian recall.
4. **Outward and group duties:** Practice Cloud notices to the 5 customer firms (24 or 72 hours) and as a third-party agent; the SEC materiality decision.

| When (Day 0 = Thursday discovery) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, forensics engaged; bridge notices to divisions; Tax and Advisory notice to Wealth; custodian recall; FBI or IC3 report | Group Chief Risk Officer; incident commander; Chief Tax Officer; Wealth operations director |
| Day 1 (Friday) | Incident confirmed for Tax and Advisory; customer impact confirmed for the 5 Practice Cloud firms; disclosure committee convened | Group CISO; Practice Cloud CISO; Group General Counsel |
| Day 2 (Saturday), within 24 hours of confirmation | Practice Cloud notice to the 2 customer firms with 24-hour terms | Practice Cloud trust and assurance director |
| Day 4 (Monday), next business day after confirmation | IRS report through the Stakeholder Liaison; state tax agencies the same day | Chief Tax Officer |
| Day 4 (Monday), within 72 hours of confirmation | Practice Cloud notice to the 3 customer firms on standard terms | Practice Cloud trust and assurance director |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| By Day 11 at the latest | Practice Cloud third-party agent notices (Florida worked example: 10 days after determination); already covered by the contract notices | Practice Cloud trust and assurance director |
| By Day 28 (planning from Day -2) | FTC notice (no later than 30 days after discovery) | Group General Counsel |
| By Day 30 | Wealth Regulation S-P notices; Florida individual and Department notices for Tax and Advisory and Wealth; consumer reporting agencies; other states' notices under their own deadlines | Wealth Chief Compliance Officer; Group Chief Privacy Officer |

**Plan to the shortest clock.** Here the order is: Tax and Advisory's notice to Wealth (on the bridge), the 24-hour customer firms, the IRS next-business-day report, the 72-hour customer firms, the SEC if material, the Florida agent notices, then the 30-day FTC, Regulation S-P, and state notices.

**Materiality factors for the disclosure committee:** about 68,000 affected individuals across Tax and Advisory, Wealth, and 5 customer firms; regulatory exposure (FTC, IRS, SEC examination of Wealth, state attorneys general); direct losses (about $271,000 before recovery) and notification and credit monitoring costs; Practice Cloud customer confidence before the next SOC 2 report (SW-018); and effects on operations in the filing season. The 4-business-day clock starts at the determination, not at discovery.

**Messages to clients and staff:** tell affected tax clients how to get an Identity Protection PIN from the IRS and what the IRS may send them; tell Wealth households about the heightened verification; tell all staff that no bank or transfer change is made on an email request, even from a manager.

## 8. Recovery (RC.RP, RC.CO)
Business systems kept running in this scenario. Recovery means restoring trust in identities and money movement, in BIA order (P05):
1. BP-G01 identity: affected accounts re-registered with phishing-resistant MFA; session lifetime shortened for office managers and support engineers
2. BP-G05 email: rules and forwarding cleaned; tax office mailbox detections live (POAM-004 accelerated)
3. BP-T03 and BP-T04 client portal: the Tax and Advisory tenant's staff access re-scoped to office queues; bulk-download limits set
4. BP-T02 e-file: held returns released after call-back and re-signature
5. BP-W02 money movement: held transfers released after call-back; the internal-sender red flag added
6. BP-S01 and BP-S02 Practice Cloud: support access restored with phishing-resistant MFA and two-person approval for customer tenants

Tell clients, advisers, and customer firms when normal service resumes (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.12).
- Update P01 (GR-02, GR-03, GR-20, TX-001, TX-002, WM-001, SW-005, SW-011), the POA&M (POAM-002, POAM-004, POAM-005, POAM-007, POAM-008, POAM-010, POAM-018), the notification matrix, and this runbook.
- Include the incident in the Qualified Individual's next report to the Tax and Advisory board of managers (314.4(i)(2); POL-03 4.12).
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain incident records for at least 6 years (POL-01 4.12); Wealth also keeps its Regulation S-P records under 275.204-2.

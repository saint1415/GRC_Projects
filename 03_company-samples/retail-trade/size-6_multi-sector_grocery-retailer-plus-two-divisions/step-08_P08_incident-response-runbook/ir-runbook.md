# Incident Response Runbook: Payment Card Data Compromise Through E-commerce Skimming Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Retail Trade (focus division: Grocery Retail) |
| Incident type | Payment card data compromise through e-commerce skimming: a compromised third-party script, loaded through the group tag management service (SYS-G4), captures card data on the retail web checkout (brand cards and Rewards Card numbers) and on the Retailer Services Portal invoice payment page |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06); PCI DSS v4.0.1 Requirement 12.10 (N44-45-R01); 16 CFR 314.4(h) and (j) (N44-45-R03) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-10 by the Group CISO and the Group General Counsel |
| Last tested | The brand card compromise playbook is tested every year (last in March 2026). **The cross-division parts of this runbook and the notification matrix have never been exercised** (scenario gap 10); the first cross-division tabletop is due 2026-12-15 (POAM-011) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative and come from the volumes in `00_company-facts.md`.
- **Entry:** attackers compromise the content delivery account of a small script vendor whose product-review widget is published through an "all pages" container in the shared tag management service (P07 CM-03b.[02]; SC-18b.[01]). The widget's script is replaced with a skimmer.
- **What it does:** on the retail web checkout the skimmer draws a fake card form over the processor's hosted payment fields and reads the company-hosted Rewards Card field directly (P07 AC-04). On the wholesale portal invoice payment page it draws the same fake form. It sends the data to a look-alike domain. The cardholder portal does not load the shared container and is not affected. The mobile app's native checkout uses the processor SDK and is not affected; its web checkout view does not load the widget.
- **Missed signal:** the payment page monitoring service alerted on Day -11, but the alert went to the marketing shared mailbox and was not read before the weekly review (P07 SI-07b.[03]).
- **Day 0:** the processor's fraud team tells the Grocery Retail payments director that the retail web channel is a likely common point of purchase.
- **Forensic estimate at Day 4:** an 11-day exposure window. About 112,000 brand cards (about 64,000 held by Florida residents) and about 9,400 Rewards Cards (about 5,400 Florida) were entered on the retail web checkout. About 380 cards were entered on the wholesale portal by about 290 independent grocers in 8 states; about 80 are owners' personal cards.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC; group digital team (tag management and front door) | Forensic firm on retainer; a PCI Forensic Investigator (PFI) if the acquirer or a brand requires one | SOC bridge |
| Payment pages and checkout decisions | Grocery Retail chief digital officer | Group digital director | Division bridge |
| Acquirer and card brand liaison (retail) | Grocery Retail payments director | Grocery Retail CISO | Acquirer merchant risk contact (binder) |
| Acquirer and customer notices (wholesale) | Grocery Wholesale finance director; retailer services director | Grocery Wholesale security and compliance lead | Division bridge |
| Rewards Card decisions and FTC notice | Financial Services CISO (Qualified Individual) | Financial Services chief compliance officer | Division bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division counsel | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI (IC3) or U.S. Secret Service field office | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker may also hold tag management or marketing credentials. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts, this runbook, and the notification matrix.

## 2. Preparation checks (Identify / Protect)
- [x] Processor hosted payment fields on the web checkout and the wholesale portal; processor SDK in the app (no card data stored by the group)
- [x] 24x7 SOC with EDR and SIEM; immutable backups (CP-9; P07 satisfied)
- [ ] Payment pages removed from "all pages" containers; page owners approve every script; the SOC can disable a tag (**gap until POAM-001 closes**)
- [ ] Payment page monitoring on all four payment pages with alerts to the SOC within 1 hour (**gap until POAM-002 closes**)
- [ ] Tag management vendor and script vendors on the TPSP list with contacts in the binder (**gap until POAM-003 closes**)
- [ ] Rewards Card field moved into an isolated frame run by Financial Services (**gap until POAM-004 closes**)
- [ ] Notification matrix approved, Financial Services on the group severity scale, and a cross-division exercise held (**gap until POAM-011 closes**)
- [ ] A known-good tag container that can be restored on its own (**gap until POAM-013 closes**)
- [x] Forensic retainer and cyber insurer panel confirmed; disclosure committee charter includes cybersecurity

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| New, changed, or unknown script on any payment page | Payment page monitoring (to the SOC once POAM-002 closes) | SOC triages within 1 hour (POL-03 4.4); compare with the page's script inventory |
| Acquirer or processor names a group channel as a likely common point of purchase | Acquirer, processor | Payment liaison opens the incident at once. **This is suspicion: the 24-hour acquirer clock starts** |
| Rewards Card fraud rising on web-originated accounts | Financial Services fraud scoring; card processing platform | Financial Services fraud lead calls the SOC |
| Several customers or grocers report fraud after paying online | Customer service; retailer services | Escalate to the SOC when there are 3 or more reports in 7 days for one channel |
| Tag published by an unexpected account or at an unusual time | Tag management publishing log (SOC use case from 2026-11) | SOC checks against approved changes |
| Payment page sends data to an unfamiliar domain | Browser capture, security researcher, or threat intelligence | SOC captures evidence and opens the incident |

**Severity 1** (group scale, POL-03 4.2 and 4.4): a confirmed unauthorized change on any payment page, or a common point of purchase notice.

**Record each clock start in the incident log (POL-03 4.3).** One event starts several clocks with different triggers:
| Clock | Starts at | Who records it |
|---|---|---|
| Acquirer notices (both merchant accounts) | Suspicion of a compromise | Incident commander |
| FTC Safeguards notice | Discovery: first day known to any employee, officer, or agent of Financial Services (16 CFR 314.4(j)(2)). **This runbook treats the day the group SOC knew as Financial Services' discovery date**, because the SOC acts for every division | Financial Services CISO |
| State breach notices | Determination of a breach or reason to believe one occurred (Florida: 501.171(4)(a)) | Group General Counsel |
| Independent grocer contract notices | The division confirms the incident | Grocery Wholesale retailer services director |
| SEC Form 8-K | The disclosure committee's materiality determination | Group General Counsel |

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Capture evidence before changing anything:** a browser capture of each payment page as delivered, copies of every script, hashes, the tag management publishing history, and the monitoring alert history | SOC; group digital team | Evidence list signed; chain-of-custody log open |
| 2. **Stop card capture on affected pages.** Disable the compromised tag; if that cannot be done within 30 minutes, take the web checkout to "pay at pickup" mode (P05 BP-RT02 workaround) and switch the wholesale portal to ACH only (BP-WD07 workaround) | Grocery Retail chief digital officer; Grocery Wholesale retailer services director | No customer can type a card number into an affected page |
| 3. Freeze all publishing in the tag management service; revoke marketing publisher sessions; suspend the script vendor | Group digital director | Only the incident team can publish |
| 4. Call each acquirer and follow its instructions, including any PFI requirement. **No later than 24 hours after suspicion** | Grocery Retail payments director; Grocery Wholesale finance director | Acquirer reference numbers recorded |
| 5. Tell Financial Services on the bridge that Rewards Card data was exposed on a retail page (this is also the Florida third-party agent notice) | Incident commander | Qualified Individual acknowledges |
| 6. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 7. Brief the Group CISO; escalate to the disclosure committee within 24 hours of declaration (POL-03 4.7) | Group CISO | Committee convened |
| 8. Ask the processor to confirm its hosted fields were not altered and to flag brand cards used in the window; ask the card processing platform to flag Rewards Cards entered on the web in the window | Payment liaisons; Financial Services fraud lead | Confirmations in the incident log |

## 5. Analysis (RS.AN)
1. **Window of exposure** for each page: first and last appearance of the malicious script, from publishing history, monitoring alerts, content delivery logs, and browser captures. The alert on Day -11 sets the earliest confirmed date.
2. **Entry point:** the script vendor's content delivery account, a marketing publisher account, or the tag management vendor itself. Confirm that the attacker did not hold group credentials (SYS-G1 sign-in logs).
3. **What was captured:** card number, expiration date, security code, and name and billing address for brand cards; Rewards Card number and code for store cards; check whether the script also ran on sign-in pages, which would add email addresses with passwords (a separate personal information element under Fla. Stat. 501.171(1)(g)).
4. **Who was affected, by division and by state:** orders paid on the web during the window (Grocery Retail), Rewards Card accounts used on the web (Financial Services), and portal card payments (Grocery Wholesale). Count unique cards and people, grouped by state of residence from billing addresses.
5. **Confirm what was not affected:** in-store lanes (encrypted at the PIN pad), EBT, the mobile app native checkout, and the cardholder portal. Record the evidence for each.
6. **Notification event decision (Financial Services):** unauthorized acquisition is presumed from unauthorized access to unencrypted customer information unless reliable evidence shows otherwise (16 CFR 314.2). With about 9,400 Rewards Cards captured, expect an FTC notice.
7. **Root cause:** "all pages" containers on payment pages, alerts not reaching the SOC, a script vendor outside oversight, and the Rewards Card field outside the hosted fields. Feed these to P01 GR-01, RT-001, RT-002, RT-024, and WD-006.

## 6. Containment and eradication (RS.MI)
1. Remove the compromised script and vendor from every container in every division. Restore a known-good payment page container (accelerates POAM-001 and POAM-013).
2. Separate payment pages from "all pages" containers before reopening card entry, and allow only inventoried scripts with integrity values and a content security policy (PCI DSS 6.4.3).
3. Rotate all tag management and storefront administrator credentials and API tokens; confirm phishing-resistant MFA on publisher accounts.
4. Turn on payment page monitoring for the wholesale portal and the app web checkout view, with alerts to the SOC (accelerates POAM-002).
5. Forensics (or the PFI) confirms no persistence and agrees before card entry reopens.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (27 rows).** Counsel approves every external notice (POL-03 4.5). The matrix has four layers:
1. **Payment system duties (contract):** both acquirers within 24 hours of suspicion. Visa's rules also require the compromise to be reported to Visa within 3 calendar days of suspicion, through the acquirers (Visa What To Do If Compromised v10.0, A.1.1). Other brands' rules were not verified; follow the acquirer.
2. **Inside the group:** Grocery Retail notifies Financial Services at once (as its agent for the Rewards Card field, Fla. Stat. 501.171(6)(a) gives at most 10 days).
3. **Each division's own duties to people and regulators:**
   - *Grocery Retail* notifies brand card holders under the law of each state where they reside.
   - *Financial Services* files the FTC notice (at least 500 consumers; no later than 30 days after discovery), notifies Rewards Card holders under state law, runs its Red Flags response, blocks and reissues cards, and handles disputes under Reg Z (liability limit in 1026.12(b); acknowledgment within 30 days and resolution within 2 billing cycles, never more than 90 days, under 1026.13(c)).
   - *Grocery Wholesale* notifies affected independent grocers within 72 hours of confirming the incident (supply agreement term) and, for owners' personal cards, follows state law.
4. **Group duties:** the SEC materiality decision, law enforcement, the insurer, and OFAC if there is an extortion demand.

| When | Action | Owner |
|---|---|---|
| Day 0 (suspicion) | Incident declared; Financial Services told on the bridge; insurer, counsel, and forensics engaged | Incident commander; Group Chief Risk Officer |
| Within 24 hours of suspicion | Retail and wholesale acquirer notices | Payment liaisons |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Day 0 to Day 2 | Voluntary report to the FBI (IC3) or the U.S. Secret Service | Group CISO |
| Day 2 (division confirms) plus 72 hours | Notices to the about 290 affected independent grocers | Grocery Wholesale retailer services director |
| Within 4 business days of a materiality determination | Form 8-K Item 1.05, if material | Disclosure committee; Group General Counsel |
| Within 5 days of the account list | Rewards Cards blocked and reissued; dispute surge staffing in place | Financial Services cardholder service director |
| As soon as possible, no later than 30 days after discovery | FTC Safeguards notice | Financial Services Qualified Individual |
| No later than 30 days after determination | Florida individual notices (15 more days only with written good cause to the Department) and Department notice (500 or more Floridians, no extension); consumer reporting agencies without unreasonable delay (more than 1,000); apply each other state's law the same way | Grocery Retail and Financial Services (each for its own customers); Grocery Wholesale for personal cards |

**Plan to the shortest clock.** In this scenario the order is: acquirers (24 hours from suspicion), the disclosure committee, wholesale customers (72 hours from confirmation), the SEC filing if material, then the FTC notice and state notices (30 days). Starting all notices from the earliest date keeps every clock safe.

**Materiality factors for the disclosure committee:** the number of cards and people affected in three divisions; card brand assessments and fraud losses; regulatory exposure (FTC, state attorneys general); effect on online sales and the wholesale relationship with 1,100 independent grocers; remediation cost; and whether the incident reveals a weakness that investors would see as important (shared tag management across divisions). The 4-business-day clock starts at the determination, made without unreasonable delay, not at discovery.

**Worked example (exercise scenario).** Determination on Day 4. Grocery Retail notifies about 112,000 brand card holders in 6 states, the Florida Department (about 64,000 Floridians), and the consumer reporting agencies. Financial Services files the FTC notice (about 9,400 consumers), notifies Rewards Card holders, and notifies the Florida Department (about 5,400 Floridians). Grocery Wholesale notifies about 290 grocers within 72 hours of confirming the incident and about 80 owners whose personal cards were taken under the laws of their states. The Rewards Card numbers are reissued, so cardholder liability for later fraud is limited under 1026.12(b).

**Not applicable:** HIPAA (no pharmacy), FAR reporting clauses (no federal contracts), and CIRCIA (no final rule; reporting is voluntary). EBT was not involved in this scenario; if a store PIN pad skimming incident involves EBT, use the state EBT processor row in the matrix after confirming its terms.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). In-store checkout, card authorization, and SNAP EBT acceptance (BP-RT01, BP-RT07) keep running throughout, because store card data never touches a web page.
1. Workforce identity and administrator access confirmed clean (BP-G01)
2. Landing zones and hub network confirmed (BP-G03)
3. **Digital front door restored with a known-good, payment-pages-only container** (BP-G05). Integrity comes before speed: no tag is restored until the incident team approves it
4. SOC visibility confirmed for all four payment pages (BP-G02)
5. Online card payments reopened on the retail web checkout (BP-RT02, RTO 4 hours, MTD 8 hours) after forensics or the PFI and the acquirer agree. Until then, orders are paid at pickup
6. Rewards Card authorization on the web (BP-FS01) reopened only after the Rewards Card field is protected by the same controls as the hosted fields (interim POAM-004 controls)
7. Wholesale portal card payments (BP-WD07) reopened last; ACH continues meanwhile

Tell shoppers, cardholders, and independent grocers when card payment is available again (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 30 days of recovery (POL-03 4.11).
- Update P01 (GR-01, GR-03, GR-08, RT-001, RT-002, RT-024, WD-006, FS-002, FS-008), the POA&M (POAM-001 to POAM-004, POAM-011, POAM-013), the notification matrix, and this runbook.
- Review with each acquirer what the incident means for the 2026 ROC and the wholesale self-assessment (SAQ A eligibility, P03 WD-G09).
- Cover the incident in the Qualified Individual's annual report to the Financial Services board (16 CFR 314.4(i)) and consider the Reg S-K Item 106 description for the next annual report.
- Keep all incident records for at least 6 years (POL-01 4.11) and any no-notice determination for 5 years (Fla. Stat. 501.171(4)(c)).

# Incident Response Runbook: Ticketing Platform Breach Exposing Customer and Card Data

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Arts, Entertainment, and Recreation |
| Incident type | Card-skimming script on the TVOP hosted checkout, delivered through a compromised tag management vendor, affecting group venues, hotel packages, streaming purchases, and 41 client venues |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **This multi-role scenario and the notification matrix have not been exercised** (scenario gap 5); the first cross-division tabletop is due 2026-12-15 (POAM-005) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** an attacker compromises the tag management vendor's publishing account and inserts a skimming script into the tag container that tenants load on their pages. Because the TVOP content security policy trusts the tag manager domain and tenant tags also load in checkout (P07 CM-8, SC-18, SI-7 findings), the script runs on payment pages.
- **What it takes:** card number, expiration date, security code, cardholder name, and billing address typed into the payment step, plus email and password from the "create an account" step of guest checkout.
- **Whose pages:** every tenant that loads that vendor's container on checkout: the Live Venues tenant, the hotels tenant (event-and-stay packages), the streaming checkout, and 41 client tenants.
- **Dwell:** 11 days, including two major on-sales.
- **Detection (Day 0):** the Live Venues acquirer reports the group as a common point of purchase for fraud, and the same morning a client venue reports fraud complaints from its patrons.
- **Forensic estimate at Day 4:** about 412,000 checkouts in the window (Live Venues about 236,000; hotel packages about 9,800; streaming about 61,000; 41 clients about 105,000); about 382,000 unique cards; about 52,000 new accounts with email and password captured; about 104,000 affected people live in Florida.

**Who owns this incident.** The TVOP is run by the Ticketing and Streaming division, so the incident commander is the group SOC director and the platform fix is the division's. But **each merchant owns its own notices** (Live Venues, Hotels and Restaurants, streaming, and each client), and the division owes notices to all of them as their service provider.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Platform containment | Chief Technology Officer (Ticketing and Streaming) | Director of Payments Engineering | Platform bridge |
| Card brands and acquirers | Group PCI program director | Division security and compliance leads | Out-of-band bridge |
| Client notices | General Manager Ticketing | Ticketing and Streaming security and compliance lead | Client notice register; out-of-band client contact list |
| Notifications and legal | Group General Counsel with outside breach counsel | Division general counsels | Out-of-band bridge |
| Merchant-of-record decisions | Live Venues, Hotels and Restaurants, and streaming security and compliance leads | Division presidents | Division bridges |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Forensics | PFI from the insurer panel that has not served the group in the past 3 years | Forensic retainer (non-PFI work) | Through counsel |
| Law enforcement | FBI field office or IC3; U.S. Secret Service field office; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker may watch corporate email and chat. Use the crisis line and managed mobile devices. The printed binder in each division's command center holds contacts, this runbook, the notification matrix, and the client notice register.

## 2. Preparation checks (Identify / Protect)
- [x] Tokenization and HSM key management in the CDE account (P07 SC-12, SC-28 satisfied)
- [x] 24x7 SOC with EDR and WAF on the TVOP
- [x] Provider B disaster recovery tested twice in 2026 (if containment requires a rebuild)
- [ ] No tags in any checkout step; script inventory for every payment page (**gap until POAM-006 closes**)
- [ ] Tamper detection covers every tenant's payment page and alerts the SOC (**gap until POAM-007 closes**)
- [ ] Script vendors assessed and under contract (**gap until POAM-009 closes**)
- [ ] Client notice register with each client's term and state third-party agent clocks (**gap until POAM-004 closes**)
- [x] Forensic retainer, PFI on the insurer panel, and breach counsel confirmed
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Common point of purchase or compromise notice | Any acquirer or card brand | **Declare Severity 1 at once.** Acquirer and Visa clocks start at suspicion |
| A client reports patron fraud after buying tickets | Client support | Open an incident; check that client's checkout pages now |
| Tamper detection alert or an unknown script on a payment page | Detection service (after POAM-007), weekly captures | Capture the page; if the script is not on the authorized list, declare |
| Tag vendor or threat intelligence reports a compromised container | Vendor, threat intelligence | Declare; block the vendor domain at checkout |
| Spike in card-testing or chargebacks on one tenant | Payment orchestration fraud scoring | Investigate within 4 hours |

**Severity 1** (group scale, POL-03 4.2): confirmed malicious code on any payment page, or card data of more than one merchant role involved.

**Record two times for every entity.** The **time of suspicion** starts the acquirer clocks (24 hours, fictional merchant terms) and Visa's 3-day clock. The **time of determination** of a breach starts state clocks (Florida: 30 days) and the Florida third-party agent clock (10 days). Client contract clocks start at the division's discovery. The incident log records each (POL-03 4.3).

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Capture before changing anything:** browser captures with network logs of checkout pages for each affected tenant type; save the script and the tag container version | Chief Technology Officer with the SOC | Captures hashed and stored on legal hold |
| 2. Block the tag manager domain and every tenant tag in all checkout steps through the content security policy (emergency change, POL-01 4.13) | Chief Technology Officer | A second capture shows only the 14 platform scripts |
| 3. Block the attacker's collection domain at the WAF and CDN; preserve logs of calls to it | Group SOC director | Block confirmed |
| 4. Freeze tag changes for all tenants; revoke the tag vendor's integration keys | General Manager Ticketing | Settings locked |
| 5. Call the cyber insurer; engage breach counsel and the PFI panel through the insurer | Group Chief Risk Officer | Claim number issued |
| 6. Notify each acquirer for Live Venues, Hotels and Restaurants, and streaming (within 24 hours of suspicion) and ask how each wants the Visa report handled | Group PCI program director | Three acquirer case numbers recorded |
| 7. Notify Live Venues and Hotels and Restaurants on the bridge (intercompany terms); start the client notice clock for the 41 clients | General Manager Ticketing | Each acknowledges |
| 8. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.6) | Group CISO | Committee convened |

**Keep selling if it is safe.** Blocking tags does not stop checkout. Do not take the TVOP offline during an on-sale unless containment fails; if it must stop, follow the P05 on-sale pause procedure and keep doors working on offline scanner mode (BP-LV01).

## 5. Analysis (RS.AN)
1. **Window of exposure per tenant.** From tag container version history, CDN logs, and checkout captures, find when the malicious version first loaded and when the block took effect, for each tenant. Each tenant's window can differ because tenants publish container versions at different times.
2. **Affected transactions and cards.** Payment orchestration lists every checkout in each tenant's window, by merchant role and acquirer. This list drives the Visa at-risk account submission (3 calendar days) for each merchant.
3. **Accounts created in the window.** List new accounts whose email and password were entered on an affected page. Force password resets before notices go out.
4. **Who is the covered entity.** Live Venues for its patrons; Hotels and Restaurants for package buyers; Ticketing and Streaming for streaming subscribers; each client for its own patrons. The division is a third-party agent and service provider for everyone except streaming.
5. **Residency.** Count affected people by state for each covered entity to drive state notices (Florida worked example: Department notice at 500 or more; consumer reporting agencies above 1,000).
6. **Data elements.** Name with card number and security code is personal information in Florida (501.171(1)(g)1.a.(III)); email with password is personal information on its own (501.171(1)(g)1.b). Card numbers in the token vault were not accessed; the vault and CDE account are not in the attack path.
7. **Root cause:** tags trusted on payment pages, no tamper detection for them, and an unassessed vendor. Feed these to P01 GR-01, TS-001, TS-014.

## 6. Containment and eradication (RS.MI)
1. Keep the content security policy that allows only the 14 inventoried platform scripts on payment pages; tags return only to event pages, from an approved list, after POAM-006 to POAM-009 close.
2. Confirm with the PFI that the platform's own code, build pipeline, and CDE account were not changed (signed images, deployment logs).
3. Force password resets for accounts created in the window and for any account that signed in on an affected page; offer MFA.
4. Rotate any integration keys the tag vendor held; remove the vendor until it shows a security assessment and contract terms.
5. Turn on tamper detection for every tenant's payment page with SOC alerting (accelerates POAM-007).

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (30 rows).** Counsel approves every notice. Card brand rules are contractual, not law, but missing them brings assessments. The matrix has three layers:
1. **Card brands and acquirers, per merchant role:** three acquirer notices (Live Venues, Hotels and Restaurants, streaming), Visa reports and at-risk accounts through each acquirer, and a PFI if Visa requires one.
2. **Service provider duties:** the division notifies 41 clients within their contract terms (24 hours for those with that term, 72 hours standard), and in any case within Florida's 10-day third-party agent deadline (501.171(6)(a)); it supports each client's own card brand and state notices.
3. **Each group covered entity's own duties:** state breach notices for its own customers, and the group's SEC materiality decision.

| When | Action | Owner |
|---|---|---|
| Hour 0 | Insurer, counsel, PFI panel engaged; divisions notified on the bridge | Group Chief Risk Officer; General Manager Ticketing |
| Day 0 to 1 | Voluntary report to the FBI (IC3) or U.S. Secret Service and CISA | Group CISO |
| Within 24 hours of suspicion | Three acquirer notices | Group PCI program director |
| Within 24 hours of discovery | Notice to clients with a 24-hour term | General Manager Ticketing |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 72 hours of discovery | Notice to all other affected clients | General Manager Ticketing |
| Within 3 calendar days of suspicion | Compromise reported to Visa through each acquirer | Group PCI program director |
| Within 3 calendar days of notifying Visa | Incident report to Visa and the acquirers | Group PCI program director |
| Within 3 calendar days of each window of exposure | At-risk card numbers to Visa through the acquirers | Director of Payments Engineering |
| Within 4 business days of a materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 5 business days of a Visa PFI requirement | PFI retained; initial report 5 business days after signing | Group General Counsel |
| Within 10 days of determination | Florida third-party agent notice to clients and group merchants (already met by contract notices; confirm content) | General Manager Ticketing |
| Within 30 days of determination | Florida individual and Department notices for each group covered entity; consumer reporting agencies; each other state's law applied the same way | Each covered entity with counsel |

**Plan to the shortest clock.** In this scenario the order is: acquirers and 24-hour clients, other clients, Visa (3 calendar days), SEC (if material, 4 business days after the determination), Florida third-party agent (10 days), then state individual and regulator notices (Florida 30 days). The 15-day Florida extension, if counsel requests it in writing within the 30 days, applies only to the individual notice, never to the Department notice.

**Materiality factors for the disclosure committee:** about 382,000 cards and 52,000 account credentials; three merchant roles and 41 clients; card brand assessments and PFI costs; client contract claims and churn (1,150 clients rely on the platform); regulatory exposure (FTC Act, state attorneys general); reputation during the on-sale season. Operations were not interrupted, which lowers the operational factor but not the others. The 4-business-day clock starts at the determination, not at discovery.

**What not to say.** No public statement blames a client or names the vendor before counsel approves. The platform served the page, so the group owns the explanation.

**Ransom or extortion:** if the attacker threatens to publish stolen data, any payment needs board risk committee approval, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying removes no notice duty.

## 8. Recovery (RC.RP, RC.CO)
The TVOP stayed available, so recovery is about trust in the payment page (P05 BP-TS01, RTO 1 hour, was never breached):
1. Payment pages verified clean for every tenant (third capture; tamper detection live)
2. Account resets complete for affected accounts
3. Tag use restored on event pages only, from the approved list, for tenants that request it
4. Client-facing incident summary and updated responsibility matrix (PCI DSS 12.9.2)
5. Live Venues and hotels box offices briefed for patron questions; guest services scripts issued

Tell divisions, clients, and patrons when normal service is confirmed, as counsel approves (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- Update P01 (GR-01, GR-03, TS-001, TS-014, LV-001, HO-006), the POA&M (POAM-004 to POAM-011), the PCI scope documents (12.5.2.1), the SOC 2 description (P09), and this runbook.
- Expect acquirers to ask for new validations and the SOC 2 service auditor to evaluate the incident. Budget for both.
- Update the Reg S-K Item 106 description for the next annual report.
- Retain incident records, notices, and determinations for at least 5 years (POL-03 4.10; Fla. Stat. 501.171(4)(c) sets 5 years for a no-notice determination, and the group applies that period to all incident records).

# Incident Response Runbook: Network Intrusion Exposing CPNI

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated wireless internet service provider) |
| Tier / Vertical | Sole Proprietorship / Communications |
| Incident type | Network intrusion exposing CPNI: an attacker takes over the edge router, captures home phone signaling (who called whom and when), and uses a password stolen from the laptop browser to export call detail from the VoIP reseller portal |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner-operator, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the network consultant due 2026-09-30 (POAM-008) |

Keep a printed copy at home and in the SITE-1 shed. Assume the router, the laptop, and any password saved in its browser are in the attacker's hands: **use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| On-call network consultant | Isolate the router, preserve evidence, rebuild from the spare | Hour 0 |
| Telecommunications counsel | Breach determination, the 64.2011 sequence, CALEA question, Florida notice | Hours 0-4 |
| Wholesale VoIP provider fraud and support line | Lock the reseller account, block call forwarding changes, pull portal access logs, watch for toll fraud | Hour 1 |
| Billing platform vendor support | Revoke sessions; pull admin and portal sign-in logs; confirm no bulk export | Hours 1-4 |
| Upstream fiber provider | Check for unusual traffic; help block attacker addresses | Hours 1-4 |
| FBI field office (and IC3 report) | Voluntary early contact; supports the later 64.2011 notice and any CALEA report | Day 1 |
| CISA (voluntary report) | No CIRCIA duty yet; voluntary report | Day 1-2 |
| Cyber insurer | **None.** The general liability policy has no cyber coverage, so the owner pays counsel and the consultant directly | n/a |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a network intrusion when any of these happens: an unknown admin login or configuration change on the router; the router's management answers from somewhere it should not; a VoIP portal sign-in alert or a call forwarding change the owner did not make; the wholesale provider reports toll fraud; a customer reports hearing about their own calls from someone else. **Write down the date and time.**

**Is it a CPNI breach?** Under 64.2011(e) a breach occurs when a person, without authorization or exceeding authorization, *intentionally* gains access to, uses, or discloses CPNI. CPNI here is call detail, home phone features, and home phone bills. Broadband data (IP addresses, usage) is not CPNI (P03 section 1.2). The owner, with counsel, records the **reasonable determination** and its date in the incident log. The 7-business-day clock starts then.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. From the phone, change the VoIP reseller portal password, turn on MFA, sign out all sessions, and ask the provider to freeze call forwarding changes | Portal locked to the owner's phone |
| 2. With the consultant, cut router management to the console port only, and **save the running configuration and logs before changing anything**. Do not reboot (logs are kept in memory) | Configuration and log copied |
| 3. Disconnect the laptop from the network but leave it on; change the billing, email, and radio controller passwords from the phone and sign out other sessions | Other accounts secured |
| 4. Call counsel; start the paper incident log: time, what was seen, each action, who was called | Log started |
| 5. Decide with the consultant whether to keep the router running (preserves service and 911 calling) or swap to the spare router (P05 priority 3) | Decision written in the log |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **What CPNI was exposed?** Ask the VoIP provider for the portal access log for the last 90 days: sign-ins, CDR exports, feature changes. List the home phone accounts whose call detail was exported or whose signaling passed the router while it was compromised.
2. **What else?** Check the billing platform for admin sign-ins and exports. Portal user names with passwords would bring in Florida law (`notification-matrix.csv`).
3. **Router.** The consultant compares the saved configuration to the last weekly copy: new accounts, port mirroring, tunnels, changed DNS. Then rebuild the spare router from the clean copy with the current firmware and management limited to the VPN and management VLAN (POL-01 7.5), and swap it in.
4. **Laptop.** Scan with the built-in antivirus; assume the browser passwords were stolen. The consultant images the disk before any cleanup.
5. **Preserve evidence** with a chain-of-custody note (who, when, where stored): router configuration and logs, laptop image, portal and billing logs. No wiping until counsel agrees.

## 5. Hours 8-24: keep service running and prepare notices (RS.CO, RC.RP)
- **Service:** internet and home phone stay up on the clean spare router. If home phone service must stop, ask the VoIP provider to forward lines to customers' mobile numbers and post a website and text-line notice that 911 by home phone is down.
- **Law enforcement notice:** once counsel and the owner reach a reasonable determination of a CPNI breach, file through the FCC central reporting facility to the USSS and FBI **within 7 business days**. If there is an extraordinarily urgent need to warn customers sooner (for example, active stalking), say so in the notice and consult the investigating agency first.
- **Hold:** do not tell customers or post publicly until 7 full business days after that notice, unless the agency agrees or directs otherwise.
- **CALEA:** if the attacker captured home phone signaling on the company's router, counsel decides whether it is unlawful electronic surveillance on company premises that must be reported to the affected law enforcement agencies (1.20003(c)).
- **Count affected customers and their states of residence.** This sets which Florida and other-state rows of the matrix apply.
- **Ransom or extortion:** not paid without counsel's advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| No later than 7 business days after reasonable determination | USSS and FBI through the FCC reporting facility | CPNI breach |
| Not before 7 full business days after that notice | Affected home phone customers | CPNI breach (after the hold) |
| No later than 30 days after determination | Florida residents, if Florida-defined personal information was involved | For example, portal credentials taken |
| Within a reasonable time | Affected law enforcement agencies | CALEA compromise or unlawful surveillance on premises |
| 2 years | CPNI breach record kept | Every CPNI breach |

**Plan the dates together.** The Florida 30-day clock can run while the CPNI hold is in place. File the law enforcement notice early in the 7-day window so the hold ends well before day 30, and let counsel decide whether the deemed-compliance path in 501.171 applies.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, SITE-1 power and upstream, the clean router, home phone lines, access points, support channels, then billing. Within 30 days of closing the incident, record lessons learned; update P01 (R-001, R-002, R-006), P07, and this runbook; count any customer complaints about the release of their CPNI for the complaint summary in the next CPNI certification (64.2009(e)); and keep the CPNI breach record for at least 2 years (POL-01 10.4).

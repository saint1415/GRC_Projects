# Incident Response Runbook: TMS Vendor Ransomware or Extended Outage

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Class II regional freight railroad, north and central Florida) |
| Tier / Vertical | Mid-Market / Transportation Systems |
| Incident type | Ransomware at, or an extended outage of, the **transportation management system (TMS) vendor** (SYS-06, vendor SaaS). Variants: the **PTC vendor's managed service** for the BOS, and the **MSSP** |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF GV.SC-08 (suppliers included in incident planning) |
| Policy basis | POL-03 Incident Response Policy (4.1, 4.4, 4.10); STD-03 Vendor risk management standard |
| Companion documents | `ir-runbook.md` (ransomware on the TDPO); `notification-matrix.csv`; BIA (P05 BP-06, BP-07, BP-08, BP-02, BP-03); risk register (P01 R-012, R-014, R-015); P09 vendor review VEN-01 |
| Runbook owner | Director of Customer Service and Car Management (business lead) with the Cybersecurity Manager (security lead) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. RSSM outage-mode drill 2026-11-30 (POAM-019); TMS vendor tabletop with the vendor 2027-02-24 (POAM-012) |

## 0. Why this runbook exists
The TMS is one vendor-hosted system that carries almost everything about the freight: car management, waybills, train consists, interchange EDI with the Class I railroads, the RSSM car location data TSA can ask for at any hour, the shipper portal, demurrage, and invoicing. It does this for the company and for the 2 affiliated short lines. Its consists also initialize PTC on the trackage-rights trains.

The vendor's SOC 2 system description states an RTO of 24 hours and an RPO of 1 hour. The BIA needs 8 hours for car management (BP-06) and 30 minutes for the RSSM duty (BP-07). A 72-hour TMS outage would cost about $260,000, mostly interchange delay and manual car work (P05). If the vendor was attacked, it may also be a **breach of company and customer data held by a third party** and a **cybersecurity incident affecting a Critical Cyber System** listed in the CIP.

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Business lead | Director of Customer Service and Car Management | Chief Dispatcher on duty (nights and weekends) | Manual car work, consists, interchange, shipper and affiliate contact |
| Security lead | Cybersecurity Manager | Director of IT | Cut and later re-establish connections safely; assess exposure of company data and credentials; CISA reporting decision |
| RSSM and TSA | Director of Safety, Security, and Hazmat | Chief Dispatcher on duty | 30-minute RSSM answers; TSOC call and 1570.203 decision; SSI questions |
| Operations | Director of Network Operations | Chief Dispatcher on duty | Train lineups, consists for departing trains, interchange schedule with the Class I partners |
| PTC | PTC Program Manager | PTC administrators | Manual consist entry in the BOS; trackage-rights train decisions |
| CMT chair (if escalated) | Chief Operating Officer | CEO | Declares a Severity 1 vendor outage; approves spending and communications |
| Finance | Chief Financial Officer | Controller | Billing delay, cash forecast, lender and sponsor updates |
| Vendor management and legal | General Counsel | Outside counsel | Contract rights, the vendor's notice duties, breach determination |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| TMS unavailable for more than 30 minutes, or the vendor's status page reports an outage | Car management staff; vendor status page | Business lead opens a ticket; RSSM fallback check (step 3) at once |
| Vendor notice or public report of a cyber incident at the vendor | Vendor; industry alerts (the rail information sharing and analysis center); CISA; news | Declare at least Severity 2; security lead cuts integrations (step 3) |
| Consist feed errors, unexpected data changes, or wrong hazmat positions in consists | BOS consist validation; crew reports | Stop using the feed; validate consists manually; treat as a possible integrity attack |
| Unusual sign-ins to the TMS with company accounts, or EDI files that do not match the partner's records | Identity provider logs; interchange partner | Disable the integration accounts; declare |

**Severity 1:** the TMS is unavailable for more than 4 hours, or there is any sign that the vendor incident reached company data, credentials, or the consist feed.

**Record the time the company first learned of the problem** in the incident log. It may start the CISA, TSA, and Florida clocks (section 5).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | **RSSM first.** Confirm the latest standby extract on the offline laptops and the printed list; brief the Chief Dispatcher that TSA requests are answered from them, adjusted by the train sheets since the extract | Director of Safety, Security, and Hazmat | A TSA request can be answered within 30 minutes |
| 0-30 min | If the vendor reports a cyber incident: disable the consist feed, the EDI relay, the single sign-on connection, and the API accounts; block the vendor's addresses at the boundary | Cybersecurity Manager | Integrations off; time recorded |
| 0-1 h | **Consists.** Dispatchers and yard staff build consists for departing trains from the yard lists and the paper switch lists; PTC administrators enter them in the BOS by hand, with a second person checking hazmat positions | Director of Network Operations; PTC Program Manager | Each departing train has a checked consist |
| 0-1 h | Call the vendor's incident line; ask for the scope, the estimated restoration time, whether company data was accessed, and whether backups are intact | Business lead with the security lead | Vendor answers recorded |
| 1-2 h | Call the cyber insurer hotline if the vendor reports a cyber incident (company data or service at risk); counsel decides on forensics support | Chief Operating Officer | Claim number |
| 1-2 h | Tell the 2 affiliated short lines (and the contracted short line from 2027-01-01) that car management runs manually; agree on paper interchange and car order exchange | Business lead | Calls logged |
| 2-4 h | Interchange: agree with the 2 Class I partners on paper interchange reports and car lists by secure email; confirm which cars are in the HTUA | Director of Network Operations | Interchange continues |
| 0-12 h | **TSOC call** if the vendor reports a cyber incident (IC Surface-2025-01 recommendation; see section 5) | Director of Safety, Security, and Hazmat | Call logged |

## 4. Running without the TMS (RC.RP)
| Process (BIA) | Workaround | Limit |
|---|---|---|
| BP-07 RSSM location (RTO 0.5 h) | Standby extract (every 4 hours; every 2 hours while PIH cars are in the HTUA) updated by hand from train sheets and yard checks | Accuracy drops after about 24 hours; after 24 hours the Director of Safety, Security, and Hazmat runs a physical yard check of PIH cars each shift |
| BP-06 consists and waybills (RTO 8 h) | Paper switch lists; manual consist entry in the BOS with a second check; waybills by email from shippers | About 60% of normal car handling capacity |
| BP-08 interchange (RTO 12 h) | Paper interchange reports; car lists by secure email with each Class I partner | Class I partners may limit acceptance after 48 hours |
| BP-02 shared service for affiliates | Affiliates send car orders and switch lists by email; the company dispatches as usual (CAD/CTC is unaffected) | Car management for affiliates is slower |
| BP-12 shipper portal | Customer service phones and email | Car tracing by phone only |
| BP-13 billing (RTO 72 h) | Bill from the last waybill extract after restoration | About $2.9 million of billing delayed at 120 hours |

## 5. Reporting and legal questions (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms each notice.

| Decision point | Question | Decider |
|---|---|---|
| V1 | Is this a cybersecurity incident the company must report to CISA under SD 1580-21-01E II.C? The directive covers incidents involving systems the company operates or maintains. **Default: report** if company accounts, the consist feed, or the integrations were touched, or if the outage disrupts train operations; a vendor outage with no company system involved and no operational disruption is logged with the reasons. When in doubt, report within 72 hours (target 24 hours) | Cybersecurity Manager with General Counsel |
| V2 | TSA: a cyber attack on the vendor that disrupts company operations is a significant security concern. Make the TSOC call within 12 hours (company practice) and meet 1570.203 within 24 hours of discovery | Director of Safety, Security, and Hazmat |
| V3 | Was company personal information (shipper contacts with portal credentials, employee data in the TMS) or SSI in the vendor's systems accessed? If personal information: the vendor as third-party agent must notify the company within 10 days of its determination (Fla. Stat. 501.171(6)); the company then decides on Florida notices within 30 days. If SSI: TSA under 1520.9(c) | General Counsel; Director of Safety, Security, and Hazmat |
| V4 | Contract notices: the shared service clients within 24 hours of confirming an incident affecting the service; the host and interchange partners as the agreements require | Director of Customer Service and Car Management through counsel |
| V5 | Does the outage prevent any CIP measure on time (for example the TMS's role in a CIP control)? If yes, notify TSA immediately (SD 1580-21-01E III.C) | Cybersecurity Manager |

**Communications.** Shippers get a notice within 24 hours through email and the customer service line. Class I partners get operations calls and written updates each shift. The vendor's statements are not repeated as fact until confirmed.

## 6. Reconnection and recovery (RC.RP, RC.CO)
1. Get the vendor's written confirmation of containment, the forensic firm's summary, and the restore point. Ask for the bridge letter or other evidence that the controls in its SOC 2 report are operating again.
2. Rotate all integration credentials (consist feed, EDI relay, API accounts) and single sign-on certificates; re-enable single sign-on only with MFA enforced.
3. Reconnect integrations one at a time, consist feed last. Compare the first 10 consists with the paper consists before the feed is trusted again (P01 R-015).
4. Reconcile car locations, waybills, and interchange records entered on paper; confirm every PIH car's location matches the yard check.
5. Bill the backlog; tell shippers, affiliates, and partners when service is normal.

## 7. Variants
| Variant | What changes |
|---|---|
| **PTC vendor managed service unavailable or compromised** | The standby BOS runs without vendor support. If both BOS servers are suspect, hold or reroute trackage-rights trains and report en route failures to the host (236.1029(b)(4)). Disable the vendor's PAM access. Vendor SLA is 8 hours against a 6-hour RTO (P03 G-095) |
| **MSSP unavailable or compromised** | The cybersecurity team monitors the SIEM and EDR consoles directly; revoke the MSSP's administrative access to EDR and the SIEM; treat MSSP-held logs and any SSI shared with the MSSP as possibly exposed (V3) |

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; written report within 30 days, including the vendor's root cause.
- Update P01 R-012, R-014, and R-015, the P09 vendor review (VEN-01), and STD-03.
- Contract follow-up at renewal: recovery terms that meet the BIA (8-hour RTO), 24-hour security incident notice, and a right to the vendor's post-incident report (POAM-014).

# Incident Response Runbook: Event-Day Outage of Ticketing and Scanning

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (live event venue operator with ticketing; private equity-backed; three Florida venues) |
| Tier / Vertical | Mid-Market / Arts, Entertainment, and Recreation |
| Incident type | Loss of ticket scanning, the box office, or venue networks during doors or a show. Worked example: an Amphitheater headliner (19,500 capacity). Causes covered: a ticketing vendor outage, an internet or SD-WAN failure, and a cyberattack (for example ransomware) on the venue network |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF GV.SC-08 (suppliers included in incident planning); NIST SP 800-34 Rev. 1 for continuity |
| Policy basis | POL-03 Incident Response Policy (4.1, 4.4, 4.9); STD-07 Contingency and event-day continuity standard |
| Companion documents | `ir-runbook.md` (ticketing platform breach); `notification-matrix.csv`; BIA (P05 BP-01 to BP-04, BP-08, BP-09); venue emergency plans; risk register (P01 R-018 to R-021, R-050) |
| Runbook owner | Vice President of Venue Operations (business lead) with the Security Manager (security lead) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Amphitheater manual entry drill 2026-03 (passed). Music Hall drill due 2026-10-31 and Club drill due 2026-11-30 (POAM-014). Full event-day tabletop with the crisis management team 2027-02-17 (POAM-016) |

## 0. Why this runbook exists
On a show day the time-critical window is the 60 to 90 minutes before doors. At the Amphitheater, gates must admit about 217 people a minute (P05 BP-01, MTD 1 hour). If scanning stops and the queue stalls, the first harm is **crowd pressure at the gates**, not lost revenue. A cancelled Amphitheater headliner costs about $1.2 million (P05). The ticketing vendor's 4-hour RTO cannot protect doors, so **the manual entry procedure is the recovery strategy**. This runbook ties the IT response to the venue's emergency operations so that life safety decisions are made by the right people.

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| **Event commander** | Venue General Manager | Venue operations manager | Owns the show: doors, holds, delayed start, cancellation, with the Director of Safety and Security |
| Safety lead | Director of Safety and Security | Venue security manager | Crowd management, gate staffing, liaison with on-site police and fire, evacuation decisions under the venue emergency plan |
| Entry lead | Venue box office manager | Ticketing operations supervisor | Offline scanning, printed manifests, wristbands, will-call |
| Technology lead | Venue technology technician on site; IT Director remotely | Infrastructure engineer on call | Network, scanners, cellular failover, vendor escalation |
| Security lead (cyber cause) | Security Manager | Security analyst | Decide whether the outage is a cyberattack; containment without stopping life safety systems |
| CMT chair (if escalated) | Chief Operating Officer | Chief Executive Officer | Cancellation, refunds policy, external statements, artist and County communications |
| Communications | Vice President of Marketing and Digital | Digital team lead | Patron messages, social media, venue screens and announcements |
| Food and beverage | Director of Food and Beverage | Venue concessions manager | Stand operations under the POS fallback |
| Ticketing vendor | Vendor priority support and named account manager | n/a | Status, restoration time, offline manifest support |

**Command post.** The event commander runs the incident from the venue command post with the safety lead. Technology and security leads report to the event commander, not the other way round, while attendees are on site.

## 2. Before every event (Protect)
Checklist owned by the entry lead and the technology lead, completed by 2 hours before doors and recorded on the door checklist (STD-07):
- [ ] Scan manifest downloaded to every scanner for **offline mode**; spot test 3 scanners in airplane mode
- [ ] Printed manifests by gate, sorted by last name and order number, plus will-call lists, in the gate kits
- [ ] Wristbands and hand stamps in each gate kit for manual admission; counters (clickers) for capacity counts
- [ ] Cellular failover tested at the venue edge (and the second ISP at the Amphitheater and the Music Hall)
- [ ] Radio channel for entry confirmed; gate supervisors briefed on the hold signal
- [ ] Box office P2PE devices charged; spare devices from HQ on site for headliners
- [ ] Ticketing vendor status page checked; vendor told of headliner shows in advance

**Status today:** done at every Amphitheater show since 2025. Not yet in use at the Music Hall and the Club (P01 R-018, POAM-014).

## 3. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Scanners show sync errors or fail to validate tickets | Gate supervisors; entry lead | Switch scanners to offline mode immediately; tell the event commander |
| Ticketing platform unreachable from the box office or apps | Box office; vendor status page | Technology lead checks local network versus vendor; opens a vendor priority case |
| Venue internet or SD-WAN down | Network monitoring; technology lead | Confirm failover to the second ISP or cellular; check scanners and POS |
| Ransom note, mass file encryption, or EDR alerts on venue office systems | EDR and MSSP; staff | **Security lead declares a cyber incident**; MSSP isolates affected hosts; follow section 6 |
| POS devices cannot authorize | Bar leads; food and beverage manager | POS vendor support; offline mode only if the P2PE instruction manual allows (P01 R-019) |

**Severity:**
- **Severity 2:** scanning works offline and lines move; vendor or network outage expected to last less than 1 hour. Entry lead and technology lead manage it; the event commander is informed.
- **Severity 1:** offline scanning fails or lines stop moving, or any cyberattack on the venue network, or an outage expected to exceed the BP-01 MTD (1 hour) during doors. The event commander activates manual entry and the CMT is convened (POL-03 4.4).

**Record the time the outage started, the time manual entry began, and every decision on doors**, in the event log at the command post.

## 4. Doors decision flow (RC.RP)
| Situation | Decision | Who decides |
|---|---|---|
| Offline scanning works | Continue. Reconcile scans when the connection returns | Entry lead |
| Offline scanning fails at some gates | Move scanners from low-traffic gates; manual entry at the failed gates | Entry lead with the safety lead |
| Scanning fails at all gates | **Manual entry procedure:** gate staff check ticket name or order number against printed manifests (or accept visibly valid mobile tickets during heavy queues, with the event commander's approval), wristband each admitted attendee, count admissions with clickers for capacity | Event commander |
| Queues exceed about 30 minutes or crowd pressure builds | Open more gates; slow the inflow with staged queue lines; announce expected wait; if pressure keeps building, **hold doors** and coordinate with on-site police and fire | Event commander with the safety lead |
| Manual entry cannot keep capacity and safety under control | Delay the start with the artist's tour manager; as a last resort, cancel under the venue emergency plan | Event commander, with the COO (CMT chair) |

**Capacity always rules.** Manual entry must never let the venue exceed its permitted occupancy. Clicker counts are reported to the command post every 15 minutes.

## 5. Other event-day processes
| Process (P05) | Fallback | Owner |
|---|---|---|
| BP-03 Food and beverage | POS vendor support; offline acceptance only within the P2PE instruction manual; otherwise close stands rather than take card data any other way. Never write card numbers down | Director of Food and Beverage |
| BP-04 Box office and will-call | Standalone P2PE devices work over cellular; will-call from printed lists | Entry lead |
| BP-08 Production | Consoles run standalone; no network dependency | Production manager |
| BP-09 Urgent notices | Venue screens and announcements; social media; ticketing buyer messages when the platform returns | Vice President of Marketing and Digital |
| BP-02 Safety and security | Radios are independent of the network; extra guards where CCTV is lost | Safety lead |

## 6. Cyber cause: ransomware or intrusion on the venue network (RS.MI, RS.AN)
If the security lead declares a cyber incident:
1. **Life safety first.** Do not shut down radios, door access needed for egress, emergency lighting, or public address systems. Isolate other systems around them.
2. The MSSP isolates affected hosts through EDR; keep them powered on for memory evidence.
3. Disconnect the venue's SD-WAN tunnel to HQ and the cloud to stop spread; standalone P2PE devices and the vendor-managed POS segment continue over their own paths if possible.
4. Revoke sessions in the identity provider for accounts used at the venue; reset venue administrator credentials with break-glass accounts.
5. Call the cyber insurer hotline before engaging vendors (POL-03 4.7); counsel engages forensics.
6. From this point, the incident also follows the analysis, notification, and recovery steps of a security incident: if card data or patron data may be involved, switch to `ir-runbook.md` for those parts, and keep this runbook for the event.

## 7. Vendor cause: ticketing platform outage (GV.SC-08)
1. Open a priority case; ask for the cause, scope, and expected restoration time every 30 minutes.
2. If the vendor reports a **cyber incident** on its side, the security lead treats company data as possibly affected: request a written statement, hunt for the vendor's indicators of compromise in company logs, and track the vendor's notice duty. Florida requires a third-party agent to notify the company no later than 10 days after determining a breach (Fla. Stat. 501.171(6)(a)); the company then owns the notices.
3. Do not reconnect integrations (the sync function, the marketing connector) until the vendor confirms containment in writing.
4. Record outage duration against the vendor's stated RTO (4 hours) for service credits at the 2027 renewal (P01 R-021).

## 8. Notifications and legal analysis (RS.CO)
**Follow `notification-matrix.csv`.** Most outages carry no legal notice duty. These are the ones that can apply:
| Situation | Notice | Owner |
|---|---|---|
| Any severity 1 event | Insurer hotline (policy terms); CEO informs the audit committee chair | COO |
| Show delayed or cancelled | Artist and promoter under the performance agreement; patrons (statements about refunds must not misrepresent whether fees are refundable, 16 CFR 464.3) | Event commander and Vice President of Ticketing |
| County PAC show affected (from 2027-07-01) | County within 48 hours of a security incident affecting County PAC data or services | COO through counsel |
| Cyberattack with possible card or patron data access | Acquirer within 24 hours of suspicion; Visa through the acquirer within 3 calendar days; Florida and other state breach notices after determination (see `ir-runbook.md`) | CFO and General Counsel |
| Ransom demand | OFAC sanctions check and law enforcement report before any payment (POL-03 4.8) | CEO with counsel |
| Vendor-caused outage with a vendor breach | Inbound Florida 10-day agent notice; the company's own notices then apply | General Counsel |

## 9. After the event (RC.RP, ID.IM)
1. **Reconcile admissions:** compare clicker counts and wristbands with the manifest; upload offline scans; resolve duplicates for refund and settlement purposes.
2. **Settlement:** the Controller adjusts the show settlement for any refunds, comps, or delayed sales (BP-07).
3. **Refunds and patron messages** for a cancelled or delayed show, with total prices stated accurately.
4. **Lessons learned** within 14 days; written report within 30 days; update this runbook, the door checklist, and P01 R-018 to R-021.
5. **Evidence and records:** keep the event log, decisions, and any cyber evidence for at least 5 years.

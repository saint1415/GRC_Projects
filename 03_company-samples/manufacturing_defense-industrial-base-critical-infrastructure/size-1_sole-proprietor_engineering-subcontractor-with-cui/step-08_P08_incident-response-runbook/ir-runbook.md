# Incident Response Runbook: Exfiltration of CUI from the Owner's Cloud Account

| Field | Value |
|---|---|
| Organization | Cris Santos Company (engineering subcontractor handling CUI drawings) |
| Tier / Vertical | Sole Proprietorship / Defense Industrial Base |
| Incident type | Exfiltration of Controlled Unclassified Information (CUI): an adversary-in-the-middle phishing page posing as a Prime A portal notice captures the owner's SYS-01 password and session token, and the attacker syncs the CUI project folder (Prime A drawings and models, some ITAR-marked) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours plus the 72-hour DoD report |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner, 2026-08-31 |
| Last tested | Not yet. Tabletop with the IT consultant due 2026-11-30 (POAM-009). **Until the medium assurance certificate arrives (2026-10-31), the DoD report in section 6 cannot be filed; call Prime A instead and record the attempt** |

Keep a printed copy in the home office and in the home safe. Assume the SYS-01 account is in the attacker's hands: **work from the laptop's local files, the phone's carrier connection, and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Prime A subcontract administrator | Tell Prime A a report is coming; Prime A's security team may already see phishing from the owner's account; it receives the DoD incident number | Hours 0-4 |
| On-call IT consultant | Isolate the laptop, help image it, check the router and other devices | Hour 0-2 |
| On-call digital forensics firm (terms agreed by 2026-10-31) | Laptop image, SaaS log export, chain of custody, malware packaging for DC3 | Hours 2-24 |
| Legal counsel with export control experience | ITAR and EAR questions, contract exposure, any extortion demand | Hours 4-24 |
| SYS-01 provider support | Lock the account, revoke sessions and tokens, preserve audit logs | Hours 0-2 |
| DoD via DIBNet | Mandatory report within 72 hours of discovery | By hour 72 at the latest |
| Professional liability carrier | Ask whether any cyber coverage applies before hiring outside help | Day 1 |
| FBI (IC3 online report) | Voluntary report of suspected theft of controlled technical information | Day 1-3 |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a CUI exfiltration incident when any of these happens: SYS-01 alerts on a sign-in the owner did not make; Prime A reports phishing sent from the owner's address; the SYS-01 activity page shows bulk downloads or a new sync device; the owner realizes credentials were typed into a page reached from an email link; files appear on a public site or in an extortion note. **Write down the date and time.** DFARS 252.204-7012 counts 72 hours from **discovery** of the cyber incident, not from confirmation of data loss.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. From the laptop (not a link in any email), change the SYS-01 password, sign out all sessions, revoke app passwords and sync devices, re-register MFA, and delete any forwarding or inbox rules | Only the owner's laptop is signed in |
| 2. Call SYS-01 provider support: confirm sessions and tokens are revoked; ask them to preserve audit logs | Case number recorded |
| 3. Change the Prime A portal and SYS-05 passwords from the laptop; check the password spreadsheet's account list for every password it held and change them all | All exposed passwords changed |
| 4. Do not wipe or reinstall the laptop. Disconnect it from Wi-Fi if malware is suspected; otherwise keep it on for imaging | Laptop preserved |
| 5. Call Prime A and the IT consultant | Both informed |
| 6. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and preserve (RS.AN, DFARS 252.204-7012(c)(1)(i) and (e))
1. **Which CUI?** Export SYS-01 audit records for the last 90 days: sign-ins (time, location, device) and file access and downloads. List every CUI file downloaded or synced by the attacker. Mark which are ITAR-marked.
2. **Other systems.** Check the laptop for an unknown sync client or remote tool, the router for changed DNS settings, and the phone for unknown profiles. Check SYS-05 for changed bank details.
3. **Preserve.** With the forensics firm, image the laptop to the spare encrypted evidence drive; save SaaS exports and router logs; record chain of custody (who, when, where stored). Keep everything at least 90 days from the DoD report.
4. **Malware.** If malware is isolated, keep it for DC3 (252.204-7012(d)); never send it to the Contracting Officer.

## 5. Hours 8-24: decide and prepare the report (RS.CO)
- **Is it reportable?** If the attacker accessed covered defense information or a covered system, yes. When unsure, report: the clause covers potentially adverse effects as well as confirmed compromise (definition of "cyber incident," 252.204-7012(a)).
- **Prepare the DIBNet report** with what is known: company and CAGE code, contract and subcontract numbers, Prime A as the higher-tier contractor, dates, systems, CUI affected, and actions taken. Updates can follow.
- **Export control.** Send counsel the list of ITAR-marked and EAR-controlled files taken and what is known about the attacker. Counsel advises whether a voluntary disclosure to DDTC (22 CFR 127.12) or BIS (15 CFR 764.5) is warranted. Theft by an outside attacker may not be the owner's violation; the reasoning is documented either way.
- **Keep working safely.** CUI work continues only on the laptop with the exposed account locked down, or pauses until the IT consultant confirms it is clean. Tell Prime A about any schedule change (P05 BP-01).
- **Extortion:** no payment without counsel's advice and an OFAC sanctions check.

## 6. By hour 72: report and follow up (RS.CO, RC.CO)
1. Submit the report at https://dibnet.dod.mil with the medium assurance certificate. Save the confirmation and the DoD incident report number.
2. Give the incident report number to Prime A as soon as practicable (252.204-7012(m)(2)(ii)).
3. Answer any DoD request for images or information (252.204-7012(f) and (g)).
4. Check whether the SPRS score and date-to-110 still hold, and do not submit any CMMC affirmation until the incident's lessons are fixed.

## 7. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 72 hours of discovery | DoD report through DIBNet | Any cyber incident affecting CUI or a covered system |
| As soon as practicable after the report | Incident report number to Prime A | After the DIBNet report |
| At least 90 days from the report | Keep images and monitoring data | Every reported incident |
| Immediately after discovery, if counsel advises | Initial voluntary disclosure to DDTC; full disclosure within 60 calendar days | Possible ITAR violation |
| Within 30 days of determination | Florida individual notice | Only if personal information of Florida residents is involved (unlikely) |

## 8. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, internet, a clean laptop, project files (from version history or the encrypted backup), Prime A portal, email, accounting. Speed up the SYS-10 migration (POAM-001) and hardware security keys. Within 30 days of closing the incident, record lessons learned and update P01 (R-001, R-002, R-006), P03, P07, and this runbook. Keep all incident records for 6 years (POL-01 5.3).

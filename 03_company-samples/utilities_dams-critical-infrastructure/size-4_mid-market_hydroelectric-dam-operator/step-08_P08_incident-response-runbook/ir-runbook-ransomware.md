# Incident Response Runbook: Corporate Ransomware with RMOS Client Data Theft and Forced IT/OT Separation

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Tier / Vertical | Mid-Market / Dams |
| Incident type | Ransomware encrypts corporate IT (endpoints, file services, business applications) after the attacker steals RMOS client data and employee records (double extortion). The company separates IT from OT to protect the HCDMS (P01 R-003) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook.md` (unauthorized access to spillway and turbine control systems; use it as well if any sign of OT compromise appears); `notification-matrix.csv`; BIA (P05) |
| Runbook owner | IT Director (incident commander for IT incidents) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Executive tabletop with outside counsel and the insurer panel scheduled 2026-12-08 (POAM-008) |

**Two rules for this runbook.**
1. **The dams do not depend on corporate IT.** The ROC and the plants keep operating on the HCDMS. If IT is compromised, separating IT from OT early is safer than waiting for proof that OT is clean.
2. **Client data is the company's promise.** RMOS clients hear about an incident affecting their data or connections within 24 hours, even before the investigation is finished.

## 0. Governance, roles, and contacts (Govern)
| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, General Counsel, CFO, Vice President of Hydro Services, Vice President of Generation Operations, vCISO, IT Director, HR Director, Director of Communications, outside breach counsel | IT/OT separation (with the VP of Generation Operations), client communications, ransom recommendation to the CEO, statements, resources |
| **Incident response team (IRT)** | Incident commander: IT Director. Security analysts, MSSP, forensic firm (through counsel), identity, cloud, and SaaS vendor contacts | Containment, investigation, eradication, recovery sequence |
| **OT protection cell** | OT Security Manager, ROC Manager, Manager of Controls Engineering | Executes and watches the IT/OT separation; looks for any sign of OT compromise; switches to `ir-runbook.md` if found |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | IT Director | vCISO | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Legal, privilege, breach decisions | General Counsel | Outside breach counsel (insurer panel) | Through the insurer hotline, then direct |
| Cyber insurer | Carrier hotline ($15 million limit, $500,000 retention) | Broker | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| RMOS client communications | Vice President of Hydro Services | RMOS desk lead | Client contact list (printed) |
| Employee communications | HR Director with the Director of Communications | | Text message tree; site managers |
| Board and sponsor | CEO informs the audit committee chair and the sponsor operating partner | COO | Phone |
| Law enforcement | FBI field office | CISA | Numbers in the binder |

**Legal privilege protocol.** Counsel engages the forensic firm. Label analysis "Privileged and confidential, prepared at the direction of counsel". Facts and conclusions stay separate. No speculation in email or chat.

## 1. Preparation checks (Identify / Protect)
- [ ] Immutable corporate backups in the separate cloud backup account (write-once, 35 days); separate backup administrator credentials stored offline
- [ ] **IT/OT separation procedure** pre-approved: one rule set on the OT DMZ firewall that blocks all corporate-to-OT traffic (including jump host sign-in) and stops the cloud push, while the ROC and plants keep running. Tested at the 2026-12-08 tabletop
- [ ] **Break-glass MFA for the jump hosts** that does not depend on the corporate identity provider (POAM-020, due 2027-03-31). Until then, separation means no remote OT support: OEMs and engineers must come on site
- [ ] Out-of-band messaging group and printed call trees at the ROC and every site
- [ ] Client contact list and the client notice template (printed)
- [ ] Insurer panel counsel and forensics pre-approved; OFAC check procedure in POL-03 4.9

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file renaming or encryption | EDR alert; staff report | MSSP isolates hosts; calls the IT Director within 30 minutes; declare severity 1 |
| Backup deletion attempts, EDR or logging disabled | Cloud audit logs; EDR tamper alert | Treat as ransomware precursor; declare |
| New privileged accounts, unusual elevation, identity provider changes | SIEM; identity provider alerts | Disable; declare if unexplained |
| Large outbound transfer from file services or the RMOS portal | Cloud firewall flow logs; portal download alerts | Block the destination; declare |
| Extortion email or leak-site post naming the company or a client | Email; threat intelligence; FBI; a client | Declare; preserve |
| Any sign that the attacker touched a jump host, the OT DMZ, or an OT account | Jump host logs; OT sensors | **Separate IT from OT immediately** and also open `ir-runbook.md` |

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MSSP; security analysts | Hosts contained |
| 0-30 min | **Decision S1: separate IT from OT.** Default is yes for any confirmed ransomware in corporate IT. Apply the separation rule set; stop the cloud push; disable jump host access from corporate | Vice President of Generation Operations with the IT Director (either may order it) | Separation confirmed at the OT DMZ firewall; ROC reports all sites normal |
| 0-30 min | ROC confirms gates and units are normal at all 4 projects and the operated client projects; operators told to report anything unusual. No change to gate operations | ROC shift supervisor | Status logged |
| 0-60 min | Call the insurer hotline before engaging any vendor; counsel engages forensics | Chief Financial Officer; General Counsel | Claim number; counsel on the call |
| 0-60 min | Protect the backup account: confirm write-once retention; suspend cross-account jobs; rotate backup administrator credentials out of band | IT Director | Backup integrity confirmed |
| 0-2 h | Revoke all identity provider sessions; reset privileged credentials with break-glass accounts; disable vendor and client guest access to the portal | IT Director | Sessions revoked |
| 0-2 h | Activate business workarounds: field services on printed packets, phone schedules with the BA/TOP and cooperative, paper work orders (P05 BP-06, BP-10, BP-12) | Process owners | Workarounds running |
| 1-2 h | Convene the CMT; first situation report | CMT chair | Meeting held |
| 2-4 h | Staff briefing script (what happened, workarounds, no external discussion, report anything unusual) | Director of Communications with HR | Script sent by text |
| 2-4 h | CEO informs the audit committee chair and the sponsor | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Entry and spread.** Forensic timeline from EDR, identity provider, email, and cloud audit logs. Look specifically for jump host sign-ins, OT DMZ access, and engineering staff accounts.
2. **What was taken.** Flow logs, portal and file service access logs, and attacker tooling. Build a data inventory: which clients, which projects, which data types (control details, instrument data, inundation maps, monthly reports), and which employee records.
3. **CEII exposure.** If inundation maps, drawings, or Security Program documents were taken, tell the Corporate Security Manager and the Chief Dam Safety Engineer at once. Stolen CEII changes the threat to the dams: raise physical security at the affected projects and treat it as a security incident for FERC reporting.
4. **OT check.** The OT protection cell confirms no OT accounts, jump hosts, or OT DMZ systems were used. Any doubt moves the response to `ir-runbook.md` as well.

## 5. Containment, eradication, and the separation period (RS.MI)
- Keep IT and OT separated until the forensic firm confirms the corporate environment is clean and the identity provider is trusted. During separation:
  - the ROC and plants run normally on the HCDMS; remote OT support is on site only;
  - historian data stays local (the cloud push resumes last);
  - dam safety technicians work from local data acquisition screens and manual reads; AI-001 and AI-002 are offline (advisory only; nothing is lost, P10).
- Rebuild compromised endpoints and servers from clean images; reset all credentials; patch the entry point.
- Restore from immutable backups after scanning restore points.

## 6. Legal, regulatory, and external communication (RS.CO)
| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Was personal information (employees) breached? Date of determination starts the state clocks | General Counsel | Decision log |
| D2 | Which RMOS clients' data or connections were affected? | Vice President of Hydro Services with the IT Director | Client impact list |
| D3 | Was CEII or a Security Program document taken? If yes, report as a security incident to the FERC Regional Office and review physical security | Corporate Security Manager | Decision log |
| D4 | Is any FERC, NERC, or 12.10 report triggered? Corporate ransomware alone is not a condition affecting project safety; it becomes one if project works or controls are affected | Chief Dam Safety Engineer; NERC Compliance Manager | Decision log |
| D5 | Ransom: recommend pay or not pay | CMT recommends; CEO decides after counsel, insurer, and an OFAC check | Decision memo |

| When | Action | Owner |
|---|---|---|
| Within 24 hours of confirming client impact | Phone, then written notice to each affected RMOS client: what is known, what the company is doing, contact point | Vice President of Hydro Services |
| Same day, voluntary | FBI field office and CISA | IT Director through counsel |
| Usually within one working day, if D3 is yes | FERC Regional Office (security incident) | Corporate Security Manager |
| No later than 30 days after determination (Florida worked example) | Notices to affected employees under the law of each state where they reside; Florida Department of Legal Affairs if 500 or more Florida residents; consumer reporting agencies if more than 1,000 | General Counsel |
| Per vendor contracts | Vendors that hold company personal information must notify the company within 10 days of their own breach determination (Fla. Stat. 501.171(6)) | GRC Manager |
| Before any payment | OFAC sanctions check; law enforcement notice | General Counsel |

**Not required:** CIRCIA (proposed rule only) and NERC CIP-008 (no high or medium impact systems). A CIP-003 Reportable Cyber Security Incident determination is needed only if a low impact BES asset is involved (D4).

**Public and client statements** come only from the CMT. Clients hear before the public.

## 7. Recovery (RC.RP, RC.CO)
Recover in BIA order for corporate services (P05 section 8): identity provider and break-glass, email and mass notification, scheduling and settlement, ERP and EAM, the RMOS portal (only after a clean rebuild and a client-visible validation), payroll, then reservations. Then reconnect IT to OT in this order:
1. Jump host access for staff from rebuilt, clean endpoints, with MFA
2. Vendor sessions, one vendor at a time
3. The one-way cloud push from the OT DMZ historian replica

The Vice President of Generation Operations approves each reconnection step. Tell clients, staff, and the board when services are restored (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; documented within 30 days.
- Update P01 (R-003, R-026, R-027), P07 POA&M, the SOC 2 readiness plan (P09, the incident affects the Availability and Confidentiality criteria), this runbook, and the client security schedule.
- Brief clients on the root cause and the fixes.

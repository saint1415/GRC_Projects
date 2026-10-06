# Incident Response Runbook: Access Control and Video Platform Compromise or Outage

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial office and retail property owner-operator) |
| Tier / Vertical | Mid-Market / Commercial Facilities |
| Incident type | Compromise or extended outage of the cloud access control and video platform (SYS-02, SYS-03) that controls about 410 door controllers, 36 turnstile lanes, and about 3,400 cameras at all 14 properties. Three variants: **A** vendor outage; **B** compromise of the vendor or of a company administrator account (door schedules changed, credentials created, data taken); **C** abuse of the tenant app's mobile credential integration (SYS-14) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF GV.SC-08 (suppliers included in incident planning) |
| Policy basis | POL-03 Incident Response Policy (4.1, 4.4, 4.6, 4.7); POL-02 4.6, 4.7, 4.12; STD-05 Vendor risk management standard |
| Companion documents | `ir-runbook.md` (BAS ransomware); `notification-matrix.csv`; BIA (P05 BP-01, BP-04, BP-06, BP-08); risk register (P01 R-005, R-006, R-019, R-024) |
| Runbook owner | Director of Security Operations (business lead) with the Security Manager (security lead) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Access platform tabletop with the platform vendor scheduled 2027-02-17 (POAM-011) |

## 0. Why this runbook exists
One multi-tenant SaaS platform decides who can enter 14 buildings and records what about 3,400 cameras see. Door controllers cache credentials for up to 72 hours, so doors keep working through an outage, but no credential can be issued or revoked. The vendor's SOC 2 system description states RTO 8 hours and RPO 1 hour; the BIA needs RTO 2 hours for administration (P05 finding 3). A compromise is worse than an outage: an attacker with administrator rights can unlock doors, create credentials, and take records for about 14,500 tenant employees, which can trigger lease notice clauses and Florida breach notice duties.

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Business lead | Director of Security Operations | SCC shift lead | Door modes, officer posts, credential freeze, temporary cards |
| Security lead | Security Manager | IT Director | Platform administrator accounts, logs, evidence, coordination with the vendor's security team |
| CMT chair (severity 1) | Chief Operating Officer | CEO | Declares severity 1; approves spending, property restrictions, and communications |
| Breach and notice decisions | General Counsel | Outside breach counsel | Determination, decision log, lease and Florida notices |
| Vendor management | GRC Analyst | General Counsel | Contract terms, vendor incident statements, SOC 2 bridge letters |
| Tenant communications | VP of Property Management | Property Managers | Tenant notices and calls |
| Communications | Director of Marketing and Communications | n/a | Staff, tenant, and media messages through counsel |
| Tenant app integration (variant C) | VP of Property Management with the Security Manager | n/a | App vendor contact; mobile credential suspension |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Variant | Action |
|---|---|---|---|
| Platform portal unavailable or door controllers show "cloud offline" at several properties | SCC; vendor status page | A | Business lead opens an incident; confirm with the vendor; start the 2-hour clock (BP-01 RTO) |
| Vendor notice of a security incident or suspected compromise | Vendor notice under the SaaS agreement (72 hours today; 24 hours requested at renewal) | B | **Immediately** run step 3.1; inform the General Counsel |
| Door schedules, door groups, or administrator accounts changed with no ticket; doors unlocked outside schedule | SCC alarms; platform audit log (exported to the SIEM from 2026-12-31, POAM-006) | B | Treat as compromise; declare severity 1 |
| Bulk creation of credentials or mobile credentials, or credentials issued to unknown tenants | Platform report; tenant app alerts | C | Suspend the integration; declare |
| Video exports nobody requested, or video viewed from unknown locations | Platform audit log | B | Treat as compromise; preserve logs |

**Severity levels:**
- **Severity 3:** variant A under 2 hours, no security concern. The business lead manages it.
- **Severity 2:** variant A expected to exceed 2 hours, or any suspected compromise under investigation. Security lead engaged; the COO is informed.
- **Severity 1:** variant A expected to exceed 24 hours, any confirmed variant B or C, or any door control failure that leaves an occupied building unsecured. Convene the CMT (POL-03 4.4).

**Record the time the company first learned of the incident**, and later the determination date (section 5).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | **3.1 Freeze and secure.** Variants B and C: disable all platform administrator accounts except 2 named break-glass accounts held by the security lead; revoke sessions; rotate API keys for the tenant app and visitor management integrations; disable the tenant app integration (variant C) | Security lead | Only break-glass administrators active |
| 0-30 min | **Secure the doors.** Set perimeter doors to scheduled lock (or locked with officer release where schedules may be altered); turnstiles to card-only; officers at main entrances with printed tenant lists; check that egress releases work (they are hardwired to the fire alarm and do not depend on the platform) | Business lead | Each property confirms door status to the SCC |
| 0-1 h | **Credential freeze.** No credential is issued or revoked in the platform until the security lead confirms the administrator plane is clean. Revocation requests are logged on paper and the affected people are added to the officers' deny list at the lobby desks | Business lead | Paper log in use at each lobby |
| 0-1 h | Variant B: call the cyber insurer hotline; counsel engaged; request the vendor's written incident statement (what happened, whether company data is affected, indicators of compromise, expected restoration) | COO; GRC Analyst | Claim number; request sent |
| 0-2 h | **SCC fallback.** Property desks use local NVR clients; recording continues on the 46 NVRs; SCC moves to radio dispatch | SCC shift lead | Local video at each property |
| 0-4 h | Export and preserve the platform audit log for the last 90 days (the vendor keeps only 90 days) and the identity provider sign-ins of all platform administrators | Security lead | Logs stored in the locked bucket |
| 0-4 h | Tenant service notice: entry may take longer; use cards, not mobile credentials, if variant C | VP of Property Management | Notice sent |
| 2-4 h | Convene the CMT if severity 1; first situation report | CMT chair | CMT meeting held |

## 4. Business continuity workarounds (RC.RP)
| Process (P05) | Workaround | Capacity and limits |
|---|---|---|
| BP-01 Access control | Cached credentials (up to 72 hours); officers at about 60 entrances with printed tenant lists; deny list at lobby desks for revoked people | One shift of officers before overtime limits; cache expiry at 72 hours means doors must go to officer-controlled mode |
| BP-04 SCC monitoring | Local NVR clients at property desks; radio dispatch; extra patrols | No single view of all properties |
| BP-06 Visitor management | Paper visitor log and escort | About 3 times slower |
| BP-08 Mobile credentials | Temporary cards issued from the platform once clean, or officer-verified entry until then | About 6,200 mobile-only users |

**If the outage approaches 72 hours** (the cache limit): the CMT decides, property by property, whether to run doors in officer-controlled mode, restrict building hours, or reprogram controllers for local-only operation with the integrator. Local-only operation needs the integrator on site and a printed, verified credential list.

## 5. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** The General Counsel keeps the decision log.

| Decision point | Question | Decider |
|---|---|---|
| P1 | What data was accessed? The platform holds tenant employee names, employers, badge photos, credential numbers, and access history; the tenant app holds names, phone numbers, user names, and passwords. Under Fla. Stat. 501.171(1)(g), a name with a credential number or photo is not a listed element, but a user name or email with a password is, and access history may be "information regarding an individual's geolocation" (counsel to decide). Face templates from the AI-002 pilot, if still held, are treated as biometric data | General Counsel with outside counsel |
| P2 | Discovery date (lease clocks; plan from discovery) and determination date (Florida 30-day clocks) | General Counsel |
| P3 | Is the vendor a third-party agent under 501.171(1)(h)? If so, it must notify the company within 10 days of its own determination (501.171(6)(a)), and the company then owes the notices under (3) and (4). The vendor may send notices for the company, but a failure is the company's violation (501.171(6)(b)) | General Counsel |
| P4 | Which tenants must be told under lease clauses (31 with 72-hour clauses; other 2024-template leases "promptly")? | General Counsel with the VP of Property Management |
| P5 | JV partner, lender, and insurer notices | CFO |

**Timeline:**
| When | Action | Owner |
|---|---|---|
| Hour 0-4 | Tenant service notice | VP of Property Management |
| Within 24 hours of a severity 1 declaration | Voluntary report to CISA and the FBI (POL-03 4.10) | Security Manager through counsel |
| Within 72 hours of discovery (plan) | Notice to the 31 tenants with 72-hour clauses if tenant employee data may have been accessed; other tenants promptly | General Counsel and Property Managers |
| Within 2 business days | JV partner notice if JV properties are affected | CFO |
| Within 30 days of determination | Florida individual notices and Department of Legal Affairs notice (500 or more Florida residents); consumer reporting agencies if more than 1,000 at a single time | General Counsel with counsel |
| Each other state | Tenant employees who live outside Florida: apply each state's law | Outside counsel |

## 6. Containment, eradication, and recovery (RS.MI, RC.RP)
1. With the vendor's security team, confirm how access was gained (vendor-side compromise, a company administrator account, or the tenant app integration) and that it is closed.
2. Recreate administrator accounts from the POL-02 role design (6 administrators), each with a security key; delete all others.
3. Compare door schedules, door groups, and the credential list against the last known-good export (weekly export to the locked bucket from 2026-11-30); correct differences one property at a time with the property's security supervisor.
4. Revoke and reissue any credential created during the incident window; re-enable the tenant app integration only after the app vendor confirms its fix and a test of 10 credentials passes.
5. Lift the credential freeze; process the paper revocation log first.
6. Return SCC monitoring to the platform; keep extra patrols for 24 hours.
7. Tell tenants when normal access is restored (RC.CO).

## 7. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days, with the vendor; written report within 30 days (POL-03 4.13).
- Update P01 (R-005, R-006, R-019, R-024), the POA&M, the vendor review (P09 VEN-02), and this runbook.
- At renewal, negotiate 24-hour incident notice, recovery terms that meet the BIA, and audit log export (STD-05).
- Retain the decision log and notices for at least 5 years (POL-01 4.14).

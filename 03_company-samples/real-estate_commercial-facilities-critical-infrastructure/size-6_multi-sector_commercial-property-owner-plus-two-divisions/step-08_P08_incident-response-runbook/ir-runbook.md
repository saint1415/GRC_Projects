# Incident Response Runbook: Ransomware on Building Automation Systems Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Commercial Facilities |
| Incident type | Ransomware with data theft on the BAACS (SYS-G5), entering through a legacy integrator remote-support tool and the BTI unit's tools (SYS-D5), affecting owned properties, hotels, managed buildings, and Construction's federal data |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; building operations led by the Group building technology director; notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The cross-division notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop is due 2026-12-15 (POAM-004) |

**Safety comes first.** The group's product is safe, conditioned, and secure space for tenants and guests. In this incident the buildings keep running on their own: BAS field controllers keep their last programs and schedules, door controllers cache credentials for up to 72 hours, and life-safety systems (fire alarm, elevators, emergency voice) are on separate networks with read-only relays into the BAS. **Nothing in this runbook touches life-safety systems.** Chief engineers and hotel engineers may move any site to manual operation at any time (POL-03 4.2).

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** an attacker buys the shared vendor account for a legacy remote-support tool from an infostealer log and connects to a site supervisor at an unsegmented office tower (one of the 47 sites with legacy tools; P07 AC-17 finding).
- **Spread:** from the flat building network, the attacker reaches a BTI technician's laptop on site, steals a browser session for the BTI tools (SYS-D5, outside the landing zone) and for the access control platform (the technician holds enterprise administrator rights, P02 AC-6 gap), and harvests local OT credentials for about 100 sites from the BTI credential vault.
- **Theft:** over 4 days the attacker copies the BTI configuration repository (programs, drawings, and credentials for group buildings and about 60 client buildings, including **CUI-marked drawings for 2 DoD client facilities**) and exports badge holder records for about 118,000 tenant employees at 58 properties, plus the face verification enrollment records for about 1,900 people at the 2 Florida pilot towers.
- **Impact on Day 0:** the attacker encrypts 31 site supervisors (19 office properties, 9 hotels, 3 managed buildings) and posts a ransom note naming the group, its tenants, and a DoD client. EDR blocks encryption of the central BAS supervisor. Field controllers keep running. The hotel PMS, the cardholder data environment, and the P2PE terminals are on separate systems and are not reached.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Building operations lead | Group building technology director | Group OT security lead | RBOC secondary console room; engineering radios |
| Site safety leads | Regional chief engineers; hotel engineers | Property and hotel general managers | Site radios; cell |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC and cloud teams; forensic firm with OT experience (insurer panel) | Assessment firm OT specialist | SOC bridge |
| BTI liaison | BTI unit general manager | BTI regional leads (verified by call-back) | Out-of-band bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division general counsels | Out-of-band bridge |
| DoD reporting | Construction director of federal contracts compliance (certificate holder) | Second certificate holder (due 2026-11-30, CN-013) | Enclave workstation |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Tenant, owner, and guest communications | Commercial Property vice presidents of property management and third-party management; hotel general managers | Group communications lead | Printed contact lists |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email, chat, and the BTI unit's tools. Use the crisis line, managed mobile devices, and engineering radios. The printed binder at every property, hotel, and the RBOC holds contacts, this runbook, the notification matrix, and the manual operating procedures.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable backups of the central BAS supervisor in provider B (CP-9; P07 satisfied)
- [x] 24x7 SOC with EDR on central BAACS components (SI-3, SI-4)
- [ ] All legacy remote-support tools removed; integrators only through the gateway (**gap until POAM-006 closes, 2026-12-31**)
- [ ] OT segmentation at every property and hotel (**gap until POAM-007 closes, 2027-12-31**)
- [ ] Every site's programs in the group vault (**gap until POAM-009 closes**); otherwise restoration depends on a clean copy of the BTI repository
- [ ] OT credentials in the group vault, not the BTI vault (**gap until POAM-002 closes**)
- [ ] Manual operating procedures at every property and hotel (**gap until POAM-015 closes**)
- [ ] Notification matrix complete with lease and owner clauses, and exercised (**gap until POAM-004 closes**)
- [x] Forensic retainer with OT experience and insurer panel confirmed
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note or unreadable graphics on a site supervisor; many sites dropping off the central supervisor at once | RBOC, chief engineers | Declare Severity 1; open the bridge. **Do not power off** supervisors; disconnect them at the site firewall or switch |
| Setpoints, schedules, or equipment states changed with no change record | RBOC, chief engineers | Check equipment locally; if confirmed, treat as a BAACS compromise |
| Remote session nobody approved, or traffic to a vendor relay service | Gateway logs; SIEM rule (from POAM-003) | Disconnect the site; call BTI on a known number |
| Bulk badge export or new administrator role in the access control platform | Platform audit log; SIEM | Suspend the account; revoke sessions; declare if unexplained |
| Extortion message or leak-site post naming the group, tenants, or a client | Email, threat intelligence, law enforcement | Declare Severity 1; preserve the message |

**Severity 1** (group scale, POL-03 4.2): encryption or theft in a shared service, more than one division affected, or any building safety impact.

**Record each clock's start.** Discovery (SOC declaration time) starts the DoD 72-hour clock, the lease 72-hour clauses, and the 48-hour owner clauses. **Determination** of a breach of personal information starts the Florida 30-day clock (Fla. Stat. 501.171(4)(a)). **Determination of materiality** starts the SEC 4-business-day clock. Record all three in the incident log (POL-03 4.3).

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Make buildings safe.** At every affected site, engineers check plant and critical spaces (tenant server rooms, hotel guest floors, kitchens) and switch to local hand control where the BAS is no longer trusted; hourly manual rounds start | Site safety leads | Each site reports stable conditions to the RBOC |
| 2. **Cut the entry paths.** Block all vendor relay services at every site firewall; disconnect the 47 legacy-tool sites from the WAN at the site router; suspend all BTI technician sessions and the gateway | Group OT security lead; network operations | No relay traffic; gateway sessions ended |
| 3. **Protect what is clean.** Isolate the central BAS supervisor and historian from the WAN (keep running); confirm the provider B vault is intact and unreachable from compromised identities | Group cloud and network director | Vault integrity report |
| 4. **Contain identities.** Disable the stolen vendor account; revoke all BTI and access control platform sessions; remove enterprise administrator rights from all but the 6 named administrators; reset access control platform administrator credentials | Group identity director | Sessions revoked; roles reduced |
| 5. **Isolate the BTI tools.** Snapshot SYS-D5 for forensics, then disconnect it; BTI stops all remote work | BTI unit general manager with the SOC | SYS-D5 offline; evidence list signed |
| 6. **Preserve evidence** (images of affected site supervisors, the technician laptop, SYS-D5; gateway, platform, and SIEM logs) on legal hold; keep CUI-related images 90 days from the DoD report (POL-03 4.9) | SOC; forensic firm | Evidence list signed |
| 7. Call the cyber insurer; engage breach counsel and the OT forensic firm through the panel | Group Chief Risk Officer | Claim number issued |
| 8. Tell the Construction director of federal contracts compliance on the bridge (DoD clock) and escalate to the disclosure committee within 24 hours (POL-03 4.5) | Incident commander; Group CISO | Both acknowledge |
| 9. Tell tenants, owners, and hotel guests about service impact (not yet about data) | Property managers; hotel general managers | Service notices sent |

## 5. Analysis (RS.AN)
1. **Scope by site.** Which site supervisors were reached, which programs changed, and whether any field controller logic was altered. Compare running programs with the last trusted copy (group vault where it exists; otherwise a BTI copy taken before the dwell period).
2. **Scope by data.** From platform audit logs and forensic images: which badge records and enrollment records were exported; which repository folders were copied. Map badge holders and enrollees to tenants and to states of residence.
3. **Federal data.** Confirm the CUI-marked drawings were in the copied folders. Construction conducts the review for compromise that 252.204-7012(c)(1)(i) requires.
4. **Personal information.** Counsel decides, state by state, which data elements are personal information. Florida worked example: face templates are treated as biometric data (unsettled under 501.702; counsel to confirm); badge records alone generally are not, but whether access history counts as geolocation information needs counsel's view.
5. **Card data.** Confirm with forensics that the CDE and P2PE terminals were not reached, and record why (separate networks, no shared credentials). If that cannot be confirmed, notify the acquirers.
6. **Root cause:** the shared vendor account and legacy tool (POAM-006), flat networks (POAM-007), BTI tools outside the landing zone (POAM-018), OT credentials in the BTI vault (POAM-002), and excessive administrator rights. Feed these to P01 GR-01 and GR-02.

## 6. Containment and eradication (RS.MI)
1. Remove the legacy tool from every site before reconnecting it, not only the 31 encrypted ones.
2. Rotate every local OT credential held in the BTI vault and move them to the group vault (accelerates POAM-002).
3. Rebuild SYS-D5 in a landing-zone account (accelerates POAM-018); restore its repository from a pre-dwell copy and scan it for CUI before use.
4. Rebuild each encrypted site supervisor from a known-good image; reload programs only from a verified copy.
5. Confirm with forensics that no persistence remains in SYS-G1, the gateway, the central supervisor, or the access control platform before reconnecting sites.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (23 rows).** Counsel approves every external notice. The matrix has three layers:
1. **Inside the group:** BTI notifies the SOC (24 hours, POL-01 4.8); each subsidiary that owns affected data makes its own notices (Cris Santos Properties, LLC for badge and enrollment data; Cris Santos Builders, LLC for federal and client data).
2. **Legal duties:** DoD within 72 hours of discovery (DFARS 252.204-7012(c)); state breach notices by state of residence (Florida worked example: individuals and the Department of Legal Affairs within 30 days of determination; consumer reporting agencies when more than 1,000 are notified); SEC Form 8-K within 4 business days of a materiality determination.
3. **Contract duties:** 410 tenants with 72-hour lease clauses, all other tenants promptly; 3 managed-building owners within 48 hours; about 60 Construction clients per contract; the insurer per policy. Acquirers only if card data is involved (not in this scenario).

| When (from SOC discovery, Day 0) | Action | Owner |
|---|---|---|
| Day 0 | Insurer, counsel, OT forensic firm engaged; BTI notice to the SOC on the bridge | Group Chief Risk Officer; incident commander |
| Day 0 to 1 | Voluntary report to the FBI or IC3 and to CISA (supports OFAC mitigation if payment is considered) | Group CISO |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts (POL-03 4.5) | Group General Counsel |
| Within 48 hours of discovery | Notice to the 3 affected managed-building owners | Commercial Property vice president of third-party management |
| Within 72 hours of discovery | DoD report through DIBNet; malware to DC3 after isolation; image preservation starts | Construction director of federal contracts compliance |
| Within 72 hours of discovery | Notice to the 410 tenants with 72-hour lease clauses; other tenants with them | Property managers with counsel |
| Within 4 business days of the materiality determination | Form 8-K Item 1.05 if material | Disclosure committee; Group General Counsel |
| Within 30 days of determination | Florida notices to about 1,900 enrollees and to the Department of Legal Affairs; consumer reporting agencies without unreasonable delay; each other state's law the same way | Group Chief Privacy Officer with counsel |
| Per contract | Construction client notices (about 60 clients) | BTI unit general manager with counsel |
| Not in effect | CIRCIA reports (proposed rule only) | Group CISO tracks |

**Plan to the shortest clock.** In this scenario the order is: owners (48 hours), DoD and the 72-hour tenants (72 hours), SEC (4 business days after determination, if material), then the state 30-day notices.

**Materiality factors for the disclosure committee:** number of buildings and hotels affected and for how long; tenant and guest safety effects; tenants' and owners' contract remedies and lease renewals at risk; federal contract consequences for Construction (DoD review, CMMC status); number of people whose data was taken; cost of response and rebuild; and reputational effects with investor owners. Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board risk committee, counsel, the insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove any notice duty when data was taken, and buildings can be recovered without the attacker's key if verified program copies exist.

## 8. Recovery (RC.RP, RC.CO)
Recovery follows the BIA order (P05 section 7):
1. Identity, landing zone, and SOC visibility confirmed clean (BP-G01, BP-G03, BP-G02)
2. Central BAS supervisor reconnected to clean sites only (BP-G04)
3. Encrypted site supervisors rebuilt and reloaded, **critical-occupancy sites first**: tenant server rooms and medical office tenants, then hotels with guests, then remaining offices and retail (BP-CF01, BP-HO04)
4. BTI tools rebuilt in the landing zone before BTI does any remote work (BP-CN03)
5. Access control administration back with reduced administrators and reset credentials (BP-G05)
6. Sites reconnected to the WAN one at a time after the legacy tool is removed and credentials rotated

At the BTI estimate of 3 to 5 sites per day per regional team (P07 CP-10), rebuilding 31 sites takes about 2 to 3 days with all regional teams working. Sites whose programs exist only in the stolen repository take longer, because a trusted copy must first be found and verified.

Tell tenants, owners, and hotel guests when services are restored (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- Update P01 (GR-01, GR-02, GR-03, GR-06, CN-001), the POA&M (POAM-002, POAM-006, POAM-007, POAM-009, POAM-017, POAM-018), the notification matrix, and this runbook.
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain incident records for at least 6 years (POL-01 4.12), and CUI-related images as DoD requests.

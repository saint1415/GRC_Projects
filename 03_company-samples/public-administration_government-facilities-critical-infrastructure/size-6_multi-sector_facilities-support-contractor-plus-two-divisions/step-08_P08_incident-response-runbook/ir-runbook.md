# Incident Response Runbook: Intrusion into IBOP Building Access Control and Automation Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Government Services and Facilities |
| Incident type | Intrusion into the Integrated Building Operations Platform (IBOP) through a legacy remote-support tool, leading to door schedule changes, alarm suppression, cardholder data theft, and exposure of CUI drawings, with effects in all three divisions |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response practices from NIST SP 800-82 Rev. 3 |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-15 by the Group CISO and the Group General Counsel |
| Last tested | OT technical playbooks tested quarterly at the ROCs. **The multi-party notification matrix has never been exercised across divisions** (scenario gap 10); the first cross-division tabletop, with a county customer and the disclosure committee, is due 2026-12-15 (POAM-005) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (Day -4):** an attacker logs in to a vendor remote-support tool on an engineering workstation at an acquired school site, using one of the 22 integrator accounts with no MFA (scenario gap 1; P07 IA-02(01)). A credential stealer on the workstation captures the browser session of a Facilities Support security systems administrator who holds the standing global administrator role in the access control SaaS (gap 2; P07 AC-06), and finds a synced folder that a commissioning engineer left on the workstation at turnover.
- **Dwell (Day -4 to Day 0):** working through the same workstation, so no new-device sign-in alert fires, the attacker:
  - exports cardholder records from 9 county, school, and university tenants: about 64,000 people (about 38,000 university students), including about 3,400 contractor badge records that carry driver license numbers, and 90 days of door events;
  - creates 2 administrator accounts and changes door schedules at 6 county buildings so that two exterior doors at each unlock between 01:00 and 04:00;
  - masks door-forced alarms for 37 doors at 11 county sites, so the Janitorial and Security central monitoring station at ROC-2 does not see them for about 5 hours;
  - copies drawings from 2 DoD projects out of the synced commissioning folder (CUI).
- **Discovery (Day 0, 02:25):** a sheriff's deputy finds a courthouse annex door unlocked at 02:10 and calls the county security desk, which calls ROC-1. The ROC operator sees schedule changes with no ticket and declares at 02:25. OT logs from the acquired site never reached the SIEM (gap 4), so nothing alerted earlier.
- **Forensic picture at Day 5:** cardholder records from Florida (about 52,000 people) and Georgia (about 12,000); no face templates taken (the vendor confirms the module stores them separately and no export ran); no evidence of access to agency systems at federal buildings; no ransomware.

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Building safety lead (per site) | Facilities Support ROC director, with each site manager | Facilities Support operations director | Site phones; customer security desks |
| OT and access control technical lead | IBOP security lead, with the Facilities Support security systems and controls engineering directors | Group building technology director | SOC bridge |
| Monitoring service lead | Janitorial and Security monitoring director | ROC-2 shift supervisor | ROC-2 console line |
| CUI and DoD reporting | Construction CUI program manager (certificate holder) | Construction division security and compliance lead | Division bridge |
| Customer notices | Division security and compliance leads (Facilities Support; Janitorial and Security) | Division presidents | Division bridge |
| Notifications and legal | Group General Counsel, with outside breach counsel | Group contracts compliance director | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Forensics | OT-capable incident response firm through the insurer's panel | Group SOC forensic team | SOC bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Numbers in the incident binder |

**Out-of-band first.** Assume the attacker can read corporate email, chat, and the access control SaaS. Use the crisis line and managed mobile devices. A printed binder at ROC-1, ROC-2, and each division command center holds contacts, this runbook, building recovery procedures, emergency revocation lists, and the notification matrix with each customer's notice term.

**Customer security staff are part of the response.** They control guards, lobbies, and lockdowns at their buildings. Janitorial and Security officers at the 74 shared sites take direction from the customer's security lead, not from the group bridge.

## 2. Preparation checks (Identify / Protect)
- [x] Immutable IBOP backups in provider B and versioned controller programs for 61% of sites (CP-9; P07 satisfied)
- [x] 24x7 SOC with EDR on IBOP servers and ROC workstations (SI-3, SI-4)
- [x] Building recovery (manual operation) procedures at all 46 federal buildings
- [ ] All OT remote access through the jump service with MFA (**gap until POAM-003, POAM-009, and POAM-010 close, 2026-12-15**)
- [ ] Per-customer, just-in-time administration of access control tenants (**gap until POAM-011 closes, 2027-03-31**)
- [ ] OT logs from every site in the SIEM, with detections for schedule, setpoint, and alarm-mask changes (**gap until POAM-004 and POAM-015 close**)
- [ ] Building recovery procedures at every state, local, and education site (**74% today; POAM-016**)
- [ ] Notification matrix complete for every contract, with CUI and monitoring service steps, and exercised (**gap until POAM-005 closes**)
- [ ] Three DoD medium assurance certificate holders (**one today; POAM-005**)
- [x] Forensic retainer (OT-capable) and insurer panel confirmed
- [x] Disclosure committee charter covers cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Door unlocked outside its schedule, or a schedule changed with no ticket | Access control alarms; customer security staff; officers at shared sites | ROC confirms with the site manager; if no approved change, declare |
| Alarm masking or suppression rule created without a ticket | Monitoring module audit log; ROC-2 supervisor | Remove the mask under the two-person rule; declare |
| Setpoint, schedule, or program change with no ticket | Building automation alarms; building engineers | Controls lead checks the audit trail; if unexplained, declare |
| Administrator account created, or cardholder export run, by an unknown user | Access control SaaS audit trail; vendor alert | Disable the account; declare |
| Remote session nobody booked; remote-support tool active outside a visit | Jump service, edge gateway, workstation EDR | Disconnect; declare |
| A customer, GSA, or law enforcement reports suspicious activity | Customer IT or security; agency | Declare and start the notice clocks |

**Severity 1** (group scale, POL-03 4.2): any unauthorized change to doors, alarms, or building equipment at more than one customer, or confirmed theft of cardholder data or CUI, or effects in more than one division. This scenario is Severity 1 at declaration.

**Record the discovery time.** The incident log records when any employee first knew (POL-03 4.3): here **Day 0, 02:25**, when the ROC operator learned of the unlocked door. Every contract and legal clock is planned from that time unless counsel documents a later start. The DoD 72-hour clock is planned from the same time, even though CUI involvement was confirmed later, because the intrusion affected a system holding covered defense information from the start.

## 4. First hours: make the buildings safe, then contain (RS.MA, RS.MI)
**Safety comes before evidence.** Wrong door states and masked alarms affect people now.

| Step | Who | Done when |
|---|---|---|
| 1. Call each affected customer's security desk; agree on door posture (exterior doors locked to the approved schedule, guards posted at key entrances, officers at shared sites briefed) | Building safety lead with site managers | Each customer acknowledges |
| 2. Remove alarm masks and confirm every door-forced and intrusion alarm reaches ROC-2; ROC-2 calls back the 2 county monitoring customers | Monitoring service lead | Test alarms received from all 11 sites |
| 3. Disable the 2 rogue administrator accounts and the compromised administrator; revoke all SYS-G1 sessions and tokens for the 41 global administrators; keep administration running through 2 per-tenant break-glass accounts checked out in PAM | Group identity director; IBOP security lead | Sessions revoked; break-glass use recorded |
| 4. Cut the entry path: isolate the acquired-site workstation, disable remote-support tools and integrator VPNs at all 37 acquired sites, and block their site tunnels to the supervisory servers. Controllers keep running on their last programs | IBOP security lead; Facilities Support controls engineering director | No remote session into any acquired site except through the jump service |
| 5. Restore approved door schedules at the 6 county buildings from the program repository (hash-verified) and have customer security walk each changed door | Facilities Support security systems director | Doors walked and confirmed |
| 6. Snapshot cloud workloads, export SaaS audit trails, and image the acquired-site workstation before any rebuild; place logs on legal hold | Group SOC with the forensic firm | Evidence list signed (chain of custody) |
| 7. Call the cyber insurer; engage breach counsel and the OT-capable forensic firm through the panel | Group Chief Risk Officer | Claim number issued |
| 8. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.9) | Group CISO | Committee convened |

**Do not** reboot or re-download controllers, wipe the supervisory servers, or restore from backup yet. That destroys evidence and can push a tampered program to more devices. Do not remove the standing global role from all 41 administrators without break-glass access in place, or the group loses the ability to fix door schedules at 188 sites.

## 5. Analysis (RS.AN)
1. **Scope by tenant and by site.** Use the access control SaaS audit trail, jump service recordings, and edge gateway logs to list every tenant, door, schedule, alarm rule, and account the attacker touched. At non-onboarded sites (39%), collect local logs before their 30-day retention expires (gap 4).
2. **Data taken, by customer and by state of residence.** For each tenant, list the data elements exported (names, badge numbers, photos, driver license numbers, door events) and count affected people by state. These drive every customer and state notice.
3. **Breach determination with counsel.** Under the Florida worked example, names with badge numbers and photos are not "personal information" by themselves; names with driver license numbers are (Fla. Stat. 501.171(1)(g)1.a.(II)). Whether door-event logs count as geolocation information (501.171(1)(g)1.a.(VII)) is for counsel. Face templates would be biometric data only if counsel concludes they are not excluded as data generated from photographs or video (501.702); here they were not taken. The university decides how to treat its students' records as education records.
4. **CUI.** The Construction CUI program manager confirms which drawings were on the workstation, which DoD contracts they belong to, and whether CUI also reached the integrator. The review for evidence of compromise follows DFARS 252.204-7012(c)(1)(i).
5. **Reach into federal buildings.** A technician who used the compromised workstation also holds a PIV card for a GSA building. His group password was captured, though agency systems are reachable only through agency virtual desktops with PIV. Report to GSA IT **immediately** anyway (BTTRG v3.0 section 1.6.1), and let GSA assess its own systems.
6. **Supply chain angle.** If forensics ties the entry or any affected component to covered equipment (for example the 4 unconfirmed NVRs at ROC-2), the FAR 52.204-25(d) clock (1 business day) starts at identification. Kaspersky and FASCSA articles are 3 business days (52.204-23(c); 52.204-30(c)).
7. **Root cause:** the legacy remote-support tool, an integrator account without MFA, a standing cross-tenant administrator role, CUI left on a site workstation, and no OT logging at the site. Feed these to P01 GR-01, GR-05, and GR-12.

## 6. Containment, eradication, and restoration of control (RS.MI)
1. Remove remote-support tools and integrator VPNs from all 37 acquired sites and move those sites to the jump service (accelerates POAM-009 and POAM-010). Rebuild the acquired-site workstation from the standard image.
2. Rotate every credential the attacker could have seen: the administrator's SYS-G1 credentials and hardware key, integrator accounts, shared supervisory passwords at acquired sites, and controller passwords (accelerates POAM-002 and POAM-003).
3. Replace the standing global role with per-customer, just-in-time roles for the 9 affected tenants first (accelerates POAM-011).
4. Delete CUI from every site workstation and the commissioning workspace; confirm with the Construction CUI program manager that CUI exists only in SYS-C2 (accelerates POAM-019).
5. Verify controller programs and door schedules at every affected site against the hashed repository copies; at sites outside the repository (39%), compare with the last commissioning records and walk the doors with customer security.
6. Confirm with forensics that no persistence remains (new accounts, scheduled tasks, remote tools, API keys in the SaaS tenants) before reconnecting the acquired sites.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (32 rows).** Counsel approves every external notice, except a first notice under a contract term that would otherwise be late (POL-03 4.5). The matrix has six layers:
1. **Inside the group:** 1-hour internal report; disclosure committee within 24 hours.
2. **Customers by contract:** county and municipal (24 hours; 12 hours under 9 county contracts), state agency (24 hours), the state university (24 hours), commercial monitoring (72 hours), and federal agency contracts as each one specifies. Each notice goes from the subsidiary that signed the contract.
3. **Customers' own legal duties:** Florida state agencies and counties must report severity level 3 to 5 incidents to the state within 48 hours of discovery (12 hours for ransomware) (Fla. Stat. 282.318(3)(c)9.c.; 282.3185(5)(b)1.). The group's notice must give them the facts in time. Other states vary.
4. **Federal:** GSA immediately; DoD within 72 hours (DFARS 252.204-7012(c)), with DC3 malware submission and 90-day media preservation; FAR supply chain reports if covered equipment is identified; DHS if E-Verify data is involved.
5. **State breach laws:** the group is a third-party agent for its public customers (Florida worked example: notice to the customer within 10 days of determination, 501.171(6)(a); a county is a covered entity for notice purposes, 501.171(1)(b)), and a covered entity for its own workforce data. Apply each other state's law the same way.
6. **SEC:** Form 8-K Item 1.05 within 4 business days after a materiality determination.

| When (from discovery, Day 0 02:25) | Action | Owner (notifying entity) |
|---|---|---|
| Day 0, within 1 hour | Internal report to the SOC; Severity 1 declared; insurer, counsel, and forensics engaged | ROC-1 operator; incident commander |
| Day 0, as soon as known | Report to GSA IT and the contracting officer's representative (technician with GSA access affected) | Facilities Support security and compliance lead (Cris Santos Facility Services, LLC) |
| Day 0, by 14:25 | First notice to the 2 affected counties under 12-hour contracts | Facilities Support security and compliance lead |
| Day 0 to Day 1 | Voluntary report to the FBI (IC3) and CISA, coordinated with the counties | Group CISO |
| Day 1, by 02:25 | 24-hour notices to the other affected counties, the school district, the state agency, and the university, including the facts each customer needs for its own state report (summary, data types, last known-good backup, estimated impact) | Facilities Support security and compliance lead |
| Day 1, by 02:25 | Notice to the 2 county monitoring customers about the masked alarms (their contracts carry 24-hour terms) | Janitorial and Security security and compliance lead (Cris Santos Protective and Building Services, LLC) |
| Day 1 | Disclosure committee convened (within 24 hours of declaration); materiality assessment starts | Group General Counsel |
| Day 3, by 02:25 | DoD cyber incident report through DIBNet; preserve images and packet captures for at least 90 days from the report; submit isolated malware to DC3 | Construction CUI program manager (Cris Santos Builders, LLC) |
| 4 business days after a materiality determination | Form 8-K Item 1.05 if the incident is determined material | Disclosure committee; Group General Counsel (parent) |
| No later than 10 days after the breach determination (Day 2) | Third-party agent notices with all the information each Florida customer needs (Fla. Stat. 501.171(6)(a)); for Georgia customers, apply Georgia law, which counsel confirms (some states set shorter clocks than Florida) | Group General Counsel with Facilities Support |
| 1 or 3 business days after identification | FAR 52.204-25(d) (1 business day) or 52.204-23(c) and 52.204-30(c) (3 business days) reports, only if covered equipment or articles are identified | Group contracts compliance director, for each affected federal contract |
| Within 1 week after remediation | Input to each Florida county's after-action report (Fla. Stat. 282.3185(6)) | Facilities Support security and compliance lead |
| Customer's decision | Individual notices to cardholders are the customers' to give (as covered or governmental entities); the group supports with mailing data and call center capacity if asked | Group General Counsel |

**Plan to the shortest clock.** In this scenario the order is: GSA (immediately), 12-hour county contracts, 24-hour customer notices, the customers' own 48-hour state reports, the DoD 72-hour report, the SEC filing if material, the Florida 10-day third-party agent notices, and the county after-action input.

**Materiality factors for the disclosure committee:** the number of public customers and contracts affected and the risk of terminations or default notices; physical security consequences at government buildings; regulatory and contract exposure (DoD and CMMC eligibility, GSA, state customers, state attorneys general); notification and recovery cost; and reputation with public agencies. Qualitative factors can make an incident material even when the cost is small relative to $18.0 billion of revenue. The 4-business-day clock starts at the determination, not at discovery.

**Ransom demands.** Florida state agencies, counties, and municipalities may not pay a ransom (Fla. Stat. 282.3186, worked example). The group never pays on a public customer's behalf. Any payment for the group's own systems needs the board risk committee, counsel, the insurer, and an OFAC sanctions check first (POL-03 4.10). Paying would not remove any notice duty.

**Public records.** Incident reports to public customers may become public records unless an exemption applies. Mark door layouts, schedules, and vulnerabilities as security system information (Florida worked example: Fla. Stat. 119.071(3)(a)) and route requests to the customer's custodian (119.0701).

## 8. Recovery (RC.RP, RC.CO)
Restore in the BIA recovery order (P05 section 7):
1. SYS-G1 identity and break-glass access, with the compromised administrator and integrator identities rebuilt
2. Cloud landing zones and the corporate network
3. IBOP platform services: the **monitoring module first**, then access control administration (per-customer roles for the affected tenants), then building automation supervision
4. Remote video and alarm monitoring at the central monitoring station, with masks removed and alarm flow tested end to end
5. ROC alarm monitoring and dispatch
6. SOC visibility, including OT log forwarding from every acquired site before it reconnects
7. Acquired sites, one at a time, only through the jump service

**Validate before reconnecting each site:** credentials rotated; programs and door schedules match the hashed known-good copies; doors walked by customer security; the edge gateway allows management traffic only from the jump service. Tell each customer in writing when its site returns to normal operation (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons-learned review with each affected customer within 14 days of recovery; documented within 30 days (POL-03 4.13).
- Update P01 (GR-01, GR-03, GR-05, GR-12, FS-001, FS-003, JS-010), the POA&M (POAM-002, -003, -005, -009 to -011, -015, -019), the notification matrix, and this runbook.
- Consider the Reg S-K Item 106 description in the next annual report.
- Retain all incident records for 6 years, or longer where a contract or a public customer's records schedule requires (POL-01 4.12).

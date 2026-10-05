# Incident Response Runbook: Network Intrusion Exposing CPNI Across Divisions

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Communications |
| Incident type | Network intrusion exposing customer proprietary network information (CPNI): entry through an Engineering remote access gateway (SYS-E1), movement into the Carrier management plane in the acquired regions, theft of call detail records, and loss of tower lighting alarms during containment |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-17 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The multi-regulator notification matrix and the service-impact gate have not been exercised** (scenario gap 8); the first cross-division tabletop is due 2026-12-15 (POAM-004) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry:** an attacker exploits a known exploited vulnerability in an internet-facing SYS-E1 remote access gateway that was 19 days past the group's 14-day patch target (P01 NE-001). It reads the six shared gateway administrator passwords (POAM-025).
- **Movement:** through a persistent tunnel (POAM-024), the attacker reaches the Carrier management plane in one acquired region and logs in to OLTs and 6 SBCs with shared local accounts (P01 TC-002). From the management segment it reaches the mediation collectors and a staging share holding a legacy billing export.
- **Theft:** over 9 days it exfiltrates 24 months of CDRs for about 610,000 voice lines on about 520,000 accounts in the two acquired regions, plus a legacy billing export with names and SSNs used for credit checks for about 48,000 accounts. Using the MNO tenant's legacy role, it also reads about 41,000 Carrier trouble tickets and the tickets and configurations of 3 Engineering customers.
- **Lawful intercept:** logs show activity on the management subnet next to SYS-C8 in one region. Access to SYS-C8 itself cannot be ruled out (P01 TC-013).
- **Discovery (Day 0, a Tuesday):** a CISA and FBI advisory names the gateway flaw; the group SOC hunts and finds the attacker's account on the gateway.
- **Forensic estimate at Day 5:** about 280,000 of the affected accounts are in Florida; about 21,000 Floridians are in the legacy billing export (Florida-defined personal information: name with SSN).

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC; forensic firm on retainer (through the insurer's panel) | Carrier network security team | SOC bridge |
| Service impact (calling, 911, broadband) | Carrier NOC director | Carrier Vice President, Network Operations | NOC bridge, joined to the incident bridge |
| Lighting monitoring | Tower site operations director | Alarm Monitoring Center supervisor | Alarm center line, joined to the incident bridge |
| CPNI breach determination and law enforcement notice | Carrier CPNI compliance officer | Carrier deputy general counsel | Division bridge |
| Lawful intercept | Carrier Vice President, Network Security and Lawful Intercept (CALEA senior officer) | Lawful-intercept operations manager | Separate LI bridge (no forensic vendor staff) |
| Engineering customer notices | Engineering MNO general manager | Engineering security and compliance lead | Division bridge |
| Notifications and legal | Group General Counsel with outside breach counsel and telecommunications counsel | Division general counsels | Out-of-band bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office; USSS (through the FCC reporting facility for CPNI); CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read corporate email, chat, the service assurance platform, and the management network. Use the crisis line and managed mobile devices. The printed binder in each division command center holds contacts, this runbook, the notification matrix, PSAP and 988 contact lists, the FAA contact procedure, and a business-day calendar.

## 2. Preparation checks (Identify / Protect)
- [x] 24x7 SOC with EDR on all IT hosts, including the SYS-E1 gateway hosts (SI-3, SI-4)
- [x] Immutable backups of OSS and BSS data in provider B (CP-9; P07 satisfied)
- [x] FCC CPNI reporting facility accounts for two named filers
- [ ] Acquired-region element logs, SYS-E1 gateway logs, and RMU logs in the SIEM (**gap until POAM-003 closes**; export local logs on Day 0 before they roll over at 30 days)
- [ ] Object-level read logging on the CDR store (**gap until POAM-014 closes**: without it, treat the whole 24-month archive in the affected regions as exposed)
- [ ] Named AAA accounts in the acquired regions (**gap until POAM-010 closes**)
- [ ] Written lighting fallback with crew assignments (**gap until POAM-019 closes**)
- [ ] Notification matrix exercised, with Engineering customer terms and landowner states (**gap until POAM-004 closes**)
- [x] Forensic retainer and insurer panel confirmed; telecommunications counsel on retainer
- [x] Disclosure committee charter includes cybersecurity materiality and the Form 8-K Item 1.05(d) CPNI step

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Government or vendor advisory naming an exploited flaw in a gateway, SBC, or router the group runs | CISA, FBI, FCC, vendor | Treat as a possible compromise; hunt on matching devices |
| Login to a network element from a host that is not a jump host | AAA accounting; SIEM (legacy regions); local logs (acquired regions) | Block the source; open a security ticket |
| New administrator account or configuration change on an SYS-E1 gateway | EDR; gateway logs | Disable the account; open a security ticket |
| Large reads or transfers from mediation collectors or the CDR store | Cloud audit logs; network detection | Block the destination; open a security ticket |
| Bulk ticket exports by an Engineering or Tower operator role | SIEM use case on the service assurance platform | Suspend the role; open a security ticket |
| RMU heartbeat loss across many sites at once | Alarm Monitoring Center | Treat as possible tampering; start the lighting fallback |
| Law enforcement contact about the group's networks or data | FBI, USSS, or another agency | Route to the Group General Counsel and the Group CISO at once |

**Severity 1** (group scale, POL-03 4.2): confirmed unauthorized access to a management plane, a CPNI store, or SYS-C8, or an incident that spans more than one division.

**Record these times in the incident log:**
1. **Discovery** (Day 0): when anyone in the group first knew of the suspected intrusion. Starts outage, FAA, and contract clocks, and the CALEA "reasonable time."
2. **Reasonable determination of a CPNI breach** (Day 2 in the scenario): when the Carrier CPNI compliance officer, with counsel, concludes that a person intentionally gained access to, used, or disclosed CPNI without or beyond authorization (64.2011(e)). Starts the 7-business-day law enforcement clock and the Florida 30-day clock. Do not wait for forensics to finish; evidence that CDRs left the network is enough.
3. **Materiality determination** (Day 6 in the scenario): when the disclosure committee decides. Starts the Form 8-K clock.

## 4. First hours (RS.MA, RS.MI)
**Service-impact gate first (POL-03 4.3).** Before any step below that isolates a shared platform or network element, the incident commander asks the NOC director and the Tower site operations director: will this affect calling, 911, broadband, Engineering customers' networks, or lighting alarms? Record the answer and start the matching clocks in section 7.

| Step | Who | Done when |
|---|---|---|
| 1. Open the out-of-band bridge; start the incident log | Incident commander | Log open |
| 2. Disable the SYS-E1 gateway administrator accounts and the attacker's account; take the exploited gateways offline; rotate all six shared passwords | Engineering MNO general manager with SOC | Gateways offline; passwords rotated |
| 3. Block every route from the SYS-E1 aggregation account into the Carrier management plane at the hub (accelerates POAM-024) | Group network director | Routes removed |
| 4. **Engineering customers:** gateways offline means remote monitoring and remediation stop for 64 customers. Tell every customer within 30 minutes that remote service is suspended, without describing the Carrier breach (outage clause) | Engineering MNO general manager | Notices logged |
| 5. Suspend the legacy cross-tenant role on the service assurance platform (accelerates POAM-008). Do **not** isolate the whole platform unless forensics shows it is compromised; if it must be isolated, start the lighting fallback (step 6) and PSAP checks first | Carrier OSS/BSS platform vice president | Role suspended |
| 6. **Lighting fallback (if alarms are lost):** switch about 5,100 newer RMUs to vendor direct alerting; assign field crews to observe the about 1,100 legacy-monitored structures within 24 hours (17.47(a)(1)); report any outage not corrected within 30 minutes to the FAA (17.48(a)) | Tower site operations director | Crew roster and observation log started |
| 7. In the affected region, move element administration to break-glass console access from a clean jump host; block shared local accounts where the element supports it | Carrier network engineering vice president | Shared accounts blocked or monitored |
| 8. **Preserve evidence before it rolls over:** export regional syslog and AAA accounting (30-day retention), gateway logs, collector logs, cloud audit logs, and ticket access logs to write-once storage; snapshot gateways and collectors | SOC; forensic firm | Exports hashed and stored |
| 9. Call the cyber insurer; engage breach counsel and forensics through the panel; call telecommunications counsel | Group Chief Risk Officer | Claim number issued |
| 10. Ask the CALEA senior officer to assess SYS-C8 through the authorized LI team only; if compromise cannot be ruled out, start the CALEA report (section 7) | Incident commander | Decision recorded |
| 11. Voluntary report to the FBI and CISA (CIRCIA is not in effect) | Group CISO | Report reference recorded |
| 12. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.7) | Group CISO | Committee convened |

## 5. Analysis (RS.AN)
1. **Initial access:** confirm the gateway flaw, the time of first access, and whether any other internet-facing gateway, SBC, or router matched the advisory (P07 RA-5 coverage gap).
2. **Movement:** trace from the gateway through the tunnel to the management segment, element logins, and the collectors. Check AAA accounting, jump host logs, and element login histories exported in step 8.
3. **What CPNI was taken:** without object-level read logs on the CDR store, scope by what the collectors and the staging share held and by network flows. **Treat the whole 24-month CDR set for the affected regions as exposed** unless forensics proves otherwise.
4. **Personal information for state law:** the legacy billing export holds names with SSNs (Florida-defined personal information). CDRs with names and numbers alone may not meet Florida's definition; counsel decides. Identify affected customers' states of residence for each state's law.
5. **Tickets and tenants:** list the Carrier tickets read through the MNO tenant (customer names, addresses, call detail) and the 3 Engineering customers' data, including subscriber names and addresses in 2 carrier customers' tickets.
6. **Lawful intercept:** determine through the authorized LI team whether SYS-C8, its management path, or intercept records were accessed. Forensic vendors may not view intercept content.
7. **Persistence:** look for new accounts, modified configurations, implants on gateways, SBCs, and routers, and changed AAA or SNMP settings. Where firmware integrity cannot be verified, replace the device.
8. **Root cause for P01:** the unpatched gateway (NE-001), shared credentials (NE-002, TC-002), unauthorized tunnels (GR-01), missing logs (GR-09), and the cross-tenant role (GR-02).

## 6. Containment and eradication (RS.MI)
1. Rebuild the SYS-E1 gateways on a patched release with named PAM accounts; keep them offline until brokered sessions replace persistent tunnels for at least the 3 affected customers.
2. Rotate every shared network element password, SNMP string, AAA key, VPN key, and service account credential in the affected region. Assume all were exposed.
3. Rebuild the mediation collectors from clean images; delete the legacy billing export from the staging share.
4. Remove the cross-tenant role permanently.
5. Isolate SYS-C8's management path in the acquired regions (accelerates TC-013's treatment).
6. Confirm with forensics that persistence is removed before reconnecting any tunnel or management path.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (34 rows).** Counsel approves every notice. The current 47 CFR 64.2011 is the rule in force; the 2023 amendments are not yet effective (P03 section 1.1). Recheck the Federal Register for an FCC effective-date notice at the start of every incident.

The matrix has four layers:
1. **Safety clocks that do not wait for anything:** PSAP and 988 notices (30 minutes), NORS notifications (120 or 240 minutes), and FAA lighting reports (immediately after 30 minutes uncorrected). Containment can trigger them (section 4).
2. **The CPNI chain:** reasonable determination, law enforcement notice within 7 business days, the 7-full-business-day hold, then customer notices. The hold binds every division's public statements about the Carrier breach.
3. **Group and state duties:** SEC Form 8-K with the Item 1.05(d) delay, Florida and other states' breach notices, and the CALEA compromise report.
4. **Contract duties:** Engineering customers (30 minutes for outages; 24 or 72 hours for incidents), Carrier enterprise and government customers, tower tenants, and the insurer.

| When (scenario days; Day 0 is Tuesday) | Action | Owner | Citation |
|---|---|---|---|
| Within 30 minutes of discovering a 911-affecting outage (if containment causes one) | PSAP and 988 notices by telephone and in writing; follow-up within 2 hours | Carrier NOC director | 47 CFR 4.9(h), (i) |
| Within 120 minutes (wireline) or 240 minutes (VoIP, 911 facility affected) | NORS notification; initial report within 72 hours (wireline); final report within 30 days | Carrier NOC director | 47 CFR 4.9(f), (g) |
| Day 0, within 30 minutes of suspending remote service | Outage notice to all 64 Engineering customers | Engineering MNO general manager | Contracts |
| Day 0 onward, immediately after 30 minutes uncorrected | FAA report of any obstruction light outage found during the fallback; daily observation of structures without alarms | Tower site operations director | 47 CFR 17.47(a); 17.48(a) |
| Day 0 to Day 1 | Insurer, counsel, forensics engaged; voluntary FBI and CISA report | Group Chief Risk Officer; Group CISO | Contract; voluntary |
| Within a reasonable time of discovery | CALEA compromise report to affected law enforcement agencies, because SYS-C8 access cannot be ruled out | CALEA senior officer | 47 CFR 1.20003(c) |
| Day 1 (24 hours after discovery) | Security incident notice to the 3 affected Engineering customers on 24-hour terms (72-hour terms: by Day 3), describing the incident in their networks without disclosing the Carrier CPNI breach | Engineering MNO general manager | Contracts |
| Day 2 | Reasonable determination of a CPNI breach recorded with its basis | Carrier CPNI compliance officer with counsel | 47 CFR 64.2011(e) |
| **Day 3 (Friday; internal target 1 business day, legal limit 7 business days after determination)** | Law enforcement notice to the USSS and FBI through the FCC reporting facility | Carrier CPNI compliance officer | 47 CFR 64.2011(b) |
| Day 3 to end of Day 14 (Tuesday) | **Hold:** no customer notice or public statement about the Carrier breach by any division, unless the investigating agency agrees or directs otherwise | All divisions; Group communications lead | 47 CFR 64.2011(a), (b)(1)-(3) |
| Day 6 (Monday) | Disclosure committee determines the incident is material | Disclosure committee | Form 8-K Item 1.05 |
| By Day 10 (Friday; when the 8-K would otherwise be due) | EDGAR correspondence to the SEC invoking Item 1.05(d) | Group General Counsel | Form 8-K Item 1.05(d) |
| Within 10 days of determination (by Day 12) | Third-party agent notice from Engineering to the 2 carrier customers whose subscriber data was in tickets | Engineering MNO general manager with counsel | Fla. Stat. 501.171(6) (worked example) |
| Day 15 (Wednesday), the first business day after the hold, as counsel confirms | Form 8-K Item 1.05 filed; Carrier customer notices begin (about 520,000 accounts); enterprise and government accounts through their representatives | Disclosure committee; Carrier customer operations vice president | Form 8-K Item 1.05(a), (d); 47 CFR 64.2011(c) |
| By Day 32 (30 days after determination) | Florida notices to about 21,000 individuals in the billing export (or the FCC-rule notice with a copy to the Department, if counsel confirms the deemed-compliance path); Department of Legal Affairs notice (500 or more Floridians); consumer reporting agencies (more than 1,000). Apply each other state's law the same way | Carrier CPNI compliance officer; Group General Counsel | Fla. Stat. 501.171(3)-(5); other state statutes |
| Throughout | CPNI breach record (2 years); FAA outage records (2 years) | Carrier CPNI compliance officer; Tower site operations director | 47 CFR 64.2011(d); 17.49 |

**How the CPNI hold and the SEC clock fit together.** Without Item 1.05(d), the 8-K would be due Day 10, inside the CPNI hold, and filing it would be a public disclosure 64.2011(a) forbids. Item 1.05(d) lets a registrant subject to 64.2011 delay the filing for the 64.2011(b)(1) period, never more than 7 business days after the law enforcement notice, if it sends correspondence on EDGAR by the original due date. The group therefore files the correspondence by Day 10 and the 8-K when the hold ends. **If the agency directs a longer delay under 64.2011(b)(3), the 1.05(d) exception does not extend with it:** counsel must then consider the Attorney General delay in Item 1.05(c) or file as the rules require.

**Materiality factors for the disclosure committee:** number of customers affected and the nation-state context; regulatory exposure (FCC CPNI enforcement, state attorneys general, CALEA); remediation cost across three divisions; effects on Engineering's customer contracts and SOC 2 timetable; wholesale and enterprise customer reaction; and operational effects (limited, because calling and lighting were protected through the gate).

**If the agency directs a delay** of customer notice under 64.2011(b)(3), get the direction in writing; Florida also allows delay on a law enforcement agency's written request (501.171(4)(b)).

**Ransom or extortion demand:** board risk committee approval, counsel, the insurer, and an OFAC sanctions check (POL-03 4.10). Paying does not remove any notice duty when data was taken.

**Next annual CPNI certifications** (due March 1) must include a summary of customer complaints about unauthorized release of CPNI, and the statements must describe operating procedures accurately in light of the incident (64.2009(e)).

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Voice and 911 (BP-C01): confirm calls complete in the affected region; SBCs rebuilt or verified
2. Network monitoring and outage reporting (BP-C04), with the service assurance platform cleaned and the cross-tenant role gone
3. Tower lighting monitoring (BP-T01): restore the alarm tenant; end the field observation fallback only after every lit structure reports
4. Workforce identity (BP-G01): verify administrator accounts and MFA registrations
5. Broadband and enterprise transport (BP-C02, BP-C03): elements rebuilt from verified configurations where tampering is suspected
6. Lawful intercept (BP-C05): re-provisioned by the authorized LI team after SYS-C8 path isolation
7. Managed Network Operations (BP-E01): brokered sessions customer by customer, starting with the 3 affected customers once they approve
8. Billing and mediation (BP-C09): collectors rebuilt within 72 hours, before switch CDR buffers overflow

**Validate before reconnecting:** credentials rotated, devices patched, logs flowing to the SIEM for the rebuilt components. Tell customers, PSAPs, and Engineering customers when service is fully restored (RC.CO), send final NORS reports within 30 days, and close FAA outage reports.

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.12).
- Update P01 (GR-01, GR-02, GR-04, GR-09, NE-001, TC-002, TC-003, TF-002), the POA&M (POAM-003, POAM-008, POAM-010, POAM-014, POAM-019, POAM-024, POAM-025), the notification matrix, and this runbook.
- Consider the Reg S-K Item 106 description for the next annual report.
- Keep the CPNI breach record at least 2 years (64.2011(d)), FAA outage records 2 years (17.49), and all incident documentation at least 6 years (POL-01 4.11).

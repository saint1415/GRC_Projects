# Incident Response Runbook: Intrusion into Building Access Control and Automation Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings) |
| Tier / Vertical | Micro / Government Services and Facilities |
| Incident type | Unauthorized access to the company's access control tenant (SYS-01), BAS monitoring service (SYS-02), or site gateways (SYS-03), for example through the shared SYS-02 "oncall" account, a phished SYS-01 administrator credential, or the MSP's remote tool on a technician laptop, leading to door schedule changes, setpoint changes, or theft of cardholder data |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), with OT response guidance from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Office and Compliance Manager (Information Security Officer) |
| Approved | 2026-08-31 by the owner |
| Last tested | Not yet. First tabletop with the county and the MSP due 2026-11-30 (POAM-011) |

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The two technicians who administer the platforms do the technical work; the MSP handles laptops, the office network, and the suite; the cyber insurer supplies breach counsel and forensics. The Office and Compliance Manager runs the incident and keeps the log. **The customers' security staff are part of the response**: they control guards, lobbies, and door lockdowns at their buildings.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead and notices | Office and Compliance Manager | Owner | Company phone (numbers on the printed contact card) |
| Decision maker (money, ransom, customer escalation) | Owner | Office and Compliance Manager | Company phone |
| Access control technical lead (SYS-01) | Security Systems Technician | Owner (break-glass account, POL-02 B.8) | Company phone |
| BAS and gateway technical lead (SYS-02, SYS-03) | Lead Controls Technician | Controls Technician | Company phone |
| Building safety on site | On-call technician with the customer's security staff | Building Engineer (county administration building) | Company phone; customer contact list in the binder |
| Laptops, office network, suite | MSP emergency line (in the MSP contract) | MSP lead technician's phone | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Policy card in the binder |
| Breach counsel and forensics | Insurer panel counsel; OT-capable forensic firm through counsel | n/a | Assigned by the insurer on the first call |
| Platform vendors | SYS-01 and SYS-02 vendor support and security contacts | Vendor account managers | Phone numbers in the binder |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Notification chain in the first hour:** person who notices → customer security staff if a door or building condition is unsafe → Office and Compliance Manager → owner and the relevant technical lead (at the same time) → insurer hotline (owner) → MSP (if a laptop, the suite, or the RMM may be involved) → breach counsel and forensics (through the insurer) → customer IT contact (within 24 hours) and the prime (immediately, if GSA systems, CUI, or a PIV card may be involved).

**Out-of-band first.** Assume the attacker can read company email and chat. Coordinate by phone and text, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the office, in the on-call bag, and at the owner's home: this runbook, contact card, notification matrix, customer notice terms, manual lockdown steps for each county building, and the face template and cardholder data map
- [ ] Named SYS-02 accounts with MFA; "oncall" account retired (AC-2, IA-2(1)). **Gap until POAM-001 closes**
- [ ] MFA on the gateway VPN and named gateway logins (AC-17). **Gap until POAM-002 and POAM-003 close**
- [ ] Known-good copies of controller programs, door schedules, gateway configurations, and SYS-01 and SYS-02 settings in the engineering repository, with hashes (CP-9). **Gap until POAM-004 closes**
- [ ] Weekly log review in place, so there is a baseline of normal SYS-01 and SYS-02 activity (AU-6). **Gap until POAM-008 closes**
- [ ] MSP security addendum with 24-hour incident notice (SA-9). **Gap until POAM-005 closes**
- [ ] OT-capable forensic firm confirmed with the insurer (IR-7)
- [ ] Manual lockdown steps agreed with the county for the 2 libraries and the parks operations building (P01 R-011)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Doors unlocked outside schedule, or a door schedule changed with no work order | SYS-01 door alarms; county security staff | Security Systems Technician checks the SYS-01 audit trail; if the change is not tied to a work order, declare |
| Setpoints or schedules changed with no work order; equipment running oddly (air handlers off, chillers cycling) | SYS-02 alarms; Building Engineer; customer facilities staff | Lead Controls Technician checks the SYS-02 audit log; if the "oncall" or any account made an unexplained write, declare |
| New SYS-01 administrator account, cardholder export, or face template export by an unknown user | SYS-01 audit trail; weekly review | Disable the account; declare |
| Gateway VPN session nobody booked; gateway configuration changed | Gateway log (kept about 7 days); weekly review | Disconnect the session; declare |
| A technician reports a phishing email they answered, or MFA prompts they did not start | Staff report | MSP resets the password and signs out all sessions; check SYS-01 and SYS-02 sign-ins; declare if a platform account was used |
| Antivirus alert on a technician laptop | MSP console | MSP isolates the laptop; the technician's platform passwords are reset |
| Customer or the prime reports suspicious activity | Customer IT or security; prime | Declare and start the notice clocks |

**Declare an incident** when any change to a door, schedule, setpoint, program, or account cannot be tied to an approved work order, or when an unknown session reached SYS-01, SYS-02, or a building network.

**Write down the discovery time.** It starts the 24-hour clocks to the county and the city and the "immediately" clock to the prime. The Florida 10-day third-party agent clock starts later, at the determination of a breach of personal information, or reason to believe one occurred (Fla. Stat. 501.171(6)(a)).

## 3. First hour: make the buildings safe, then contain (RS.MA, RS.MI)
**Safety comes before evidence.** Wrong door states and HVAC settings affect people now.

| Step | Who | Done when |
|---|---|---|
| 1. Tell the customer's security staff and facilities contact what is happening; agree on the door posture (for example lock exterior doors to schedule with the local lockdown buttons at the administration building, keys and a guard at the other buildings) | On-call technician; Security Systems Technician | Customer security acknowledges |
| 2. Put affected BAS equipment in local or manual mode at the controller and restore safe setpoints | Lead Controls Technician with the Building Engineer | Building conditions stable |
| 3. Cut remote paths: set all SYS-02 sites to read-only, disable the "oncall" account, shut the technician VPN on every gateway. Field controllers keep running their last programs; door controllers keep their last cardholder list | Lead Controls Technician | No remote write into any building |
| 4. In SYS-01, disable any unknown or suspect administrator, reset the passwords and MFA of all company administrators, and export the audit trail | Security Systems Technician | Accounts disabled; audit export saved |
| 5. Call the insurer's breach hotline; counsel and an OT-capable forensic firm are assigned | Owner | Claim number issued |
| 6. Call the MSP emergency line if a laptop, the suite, or the RMM may be involved; the MSP isolates laptops and signs out suite sessions | Office and Compliance Manager | MSP confirms |
| 7. Open the incident log: timeline, actions, who, and when | Office and Compliance Manager | Log started |

**Do not** re-download controller programs, factory-reset a gateway, or restore SYS-01 settings yet. That destroys evidence and may push a tampered setting to more devices.

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the technical leads and the MSP supplying access and logs.
1. **Scope.** Which buildings, doors, controllers, and accounts were touched? Compare current door schedules and controller programs with the last known-good copies (where they exist; see section 1). Sources: SYS-01 audit trail, SYS-02 audit log (90 days), gateway logs (about 7 days), suite sign-in logs, MSP antivirus console.
2. **Initial access.** The shared "oncall" password, a phished SYS-01 administrator, a gateway login, or the MSP's RMM? Ask both vendors for their own logs of sign-ins to the company tenants. If the RMM may be the entry point, the owner asks the forensic firm to lead and requires the MSP to share its own investigation.
3. **Preserve evidence.** Export SYS-02 and gateway logs at once, before they age out. Image any affected laptop. Keep a chain-of-custody record for every image and export.
4. **Data theft.** Was the cardholder list, access history, badge photos, video, or the **face template set** exported? Were drawings or CUI in the suite accessed? **This drives the breach determination** (section 6).
5. **Reach into GSA.** Did the attacker use or obtain anything belonging to the 2 PIV holders, or touch the CUI folder? If there is any chance, **notify the prime immediately** so it can report to GSA IT (BTTRG 1.6.1). GSA handles its own systems.
6. **Supply chain angle.** If the entry point was equipment or software supplied under CT-F, check it against FAR 52.204-25, 52.204-23, and FASCSA orders; the clause clocks start at identification.

## 5. Containment, eradication, and restoration of control (RS.MI)
1. Retire the "oncall" account permanently; issue named SYS-02 accounts with MFA before restoring write access.
2. Rotate every credential the attacker could have seen: SYS-01 and SYS-02 passwords, gateway administrator and VPN passwords, city system passwords (with the city IT manager), and suite passwords.
3. Update gateway firmware and reapply the standard configuration from the repository, one building at a time.
4. Restore controller programs and door schedules from known-good copies, **checking hashes where they exist**, with a technician on site watching equipment behavior. Where no good copy exists, rebuild the sequence from drawings and get the customer's sign-off.
5. Have the customer's security staff walk every changed door and confirm the correct state; review every cardholder added or changed during the incident window.
6. Confirm with the forensic firm that no persistence remains (unknown accounts, API keys, scheduled exports, remote tools) before turning remote write back on.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel reviews every notice about personal information.

| When | Action | Owner |
|---|---|---|
| Immediately | Notice to the prime if GSA systems, GSA data, CUI, or a PIV card or GSA credential may be involved | Office and Compliance Manager |
| Within hours, no later than 24 hours after discovery | Notice to the county and/or the city. Include the facts each needs for its own state report: summary, date and location of the last backup, data types, estimated fiscal impact (Fla. Stat. 282.3185(5)(a)) | Office and Compliance Manager; owner calls the county facilities director |
| Customer's clock | The county and the city must report to the Cybersecurity Operations Center, the FDLE Cybercrime Office, and the sheriff within 48 hours of discovery (12 hours for ransomware) for a severity level 3 to 5 incident (282.3185(5)(b)1.). The company's notice must leave them time | Office and Compliance Manager |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA, coordinated with the customer | Owner with counsel |
| As soon as scope is known | Breach determination for personal information (cardholder data, face templates, company HR data), with counsel. Record the date | Owner and counsel |
| No later than 10 days after the breach determination | Third-party agent notice to the county with all information it needs for its own notices (Fla. Stat. 501.171(6)(a)). The county decides on notices to individuals, the Department of Legal Affairs (500 or more), and consumer reporting agencies (more than 1,000); SYS-01 holds about 1,050 cardholders | Office and Compliance Manager and counsel |
| No later than 30 days after determination | Individual notice for the company's own employee data, if affected (501.171(4)) | Office and Compliance Manager and counsel |
| One business day / 3 business days | FAR 52.204-25(d) / 52.204-23(c) and 52.204-30(c) reports to the prime if covered equipment or articles are identified | Office and Compliance Manager |
| Within 1 week after remediation | Input to the county's or city's after-action report (282.3185(6)) | Office and Compliance Manager |
| At the start and weekly | Status to the owner, the customers, and the insurer | Office and Compliance Manager |

**Plan to the shortest clock.** The prime's "immediately" and the customers' 24 hours run first and must feed the customers' own 48-hour and 12-hour state reports. The Florida 10-day clock is an outer limit, not a target.

**Inbound notices.** If the breach happened at the SYS-01 vendor, the vendor notifies the company within 72 hours of confirming it (vendor terms); the company still notifies the county within 24 hours of learning of it. If the MSP is the source, there is no notice term today (POAM-005).

**Ransom demands.** Counties and municipalities may not pay or otherwise comply with a ransom demand (Fla. Stat. 282.3186). The company will not pay on a customer's behalf. Any payment for the company's own systems needs the owner, counsel, the insurer, and an OFAC sanctions check (POL-03 4.9). Paying would not remove any notice duty.

**Public records.** Incident reports to a customer may become public records. Mark door layouts, vulnerabilities, and security details as exempt security system plan information (Fla. Stat. 119.071(3)(a)) and let the customer's custodian decide on requests.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. On-call phone and alarm notifications (SYS-02 read-only first, so buildings are watched again)
2. SYS-01 administration with clean, named administrator accounts; re-verify all door schedules and recent cardholder changes
3. Dispatch (CMMS, suite, office phones)
4. Gateways and remote write, one building at a time, after firmware, configuration, and credentials are checked
5. Engineering records repository
6. Federal subcontract work orders
7. Video exports
8. Billing and payroll

**Validate before turning remote write back on at each building:** credentials rotated and MFA in place, gateway configuration matches the standard, programs and schedules match the known-good copies, and door states walked by customer security. Tell each customer in writing when its buildings return to normal remote operation (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting with each affected customer and the MSP within 14 days of recovery; written summary within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-002, R-004, R-010, R-014), the POA&M (P07), and this runbook.
- Keep the incident log, breach determination, notices, and forensic report at least 3 years, or longer where a contract or the customer's records schedule requires (POL-02 A.8). A written determination that notice to individuals is not required must be kept at least 5 years (Fla. Stat. 501.171(4)(c)).

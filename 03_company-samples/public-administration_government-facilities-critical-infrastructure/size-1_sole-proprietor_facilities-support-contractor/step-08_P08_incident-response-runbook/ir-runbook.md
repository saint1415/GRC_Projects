# Incident Response Runbook: Intrusion into the City's Building Automation and Access Control Systems

| Field | Value |
|---|---|
| Organization | Cris Santos Company (facilities support contractor operating government buildings) |
| Tier / Vertical | Sole Proprietorship / Government Services and Facilities |
| Incident type | Someone uses the owner's access (the remote-desktop account, a stolen suite or city credential, the shared BAS administrator password, or the owner's phone or laptop) to change the city's BAS or access control system, or to take city data. The registry default "intrusion into building access control and automation systems," adapted to the owner's access path: the owner does not host these systems |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours; OT practice from NIST SP 800-82 Rev. 3 |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner, 2026-09-04 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-10-31; tabletop with the city IT manager due 2026-12-31 (POAM-007) |

Keep a printed copy in the van and the home office with the contact sheet. **Assume the attacker can read the owner's email and has the owner's passwords: use the phone to call, not to email, and use this paper copy.** The city owns these systems. **The city IT manager leads the response on city systems; the owner's job is to make the building safe with the city, cut off the owner's own access paths, preserve what the owner holds, and give notices on time.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| City facilities manager | Agree safe door and equipment states; send staff or a guard to doors if needed | Minute 0 if doors or equipment are affected |
| City IT manager | Owner of the VPN, identity provider, and access control tenant; leads the response on city systems; **24-hour contract notice** | Hour 0 (call, then written notice) |
| Prime contractor's security officer | **Immediate** notice if the same laptop, suite account, or phone holds GSA data or CUI, or if the PIV card may be involved | Hour 0 to 1 if any chance |
| On-call IT technician | Check and preserve the laptop and phone; reset the router | Hour 1 |
| Access control vendor support (through the city IT manager) | Session revocation, audit trail export, emergency lockdown help | As the city directs |
| Attorney | Breach questions under Fla. Stat. 501.171; public records questions | Hours 4 to 24 |
| FBI field office or IC3; CISA | Voluntary report, coordinated with the city | Day 1 |
| Backup controls firm (once approved by the city, R-006) | Hands-on help at the controllers if the owner cannot cover all buildings | As needed |

There is **no cyber insurer** to call (P01 R-010). Contact numbers are on the printed contact sheet only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens:
- A door unlocks or locks outside its schedule, or a schedule, setpoint, or program changed and nobody can tie it to an approved request.
- The access control audit trail or the monthly review (POL-01 7.7) shows an administrator change or a cardholder export the owner did not make.
- The suite or a city system warns of a sign-in the owner did not make; an MFA prompt arrives that the owner did not start.
- The remote-desktop history shows a session the owner did not make (until the agent is removed).
- The laptop or phone is lost or stolen, or the antivirus reports malware.
- The city or the prime reports suspicious activity involving the owner's accounts.

**Write down the date and time of discovery.** It starts the city's 24-hour clock and the prime's "immediately" clock. A determination that city personal information was taken starts the Florida 10-day third-party agent clock (Fla. Stat. 501.171(6)(a)).

## 3. First hour: make the building safe, then cut off the owner's access (RS.MA, RS.MI)
**Safety before evidence.** Wrong door states and HVAC settings affect people now.

| Step | Done when |
|---|---|
| 1. Call the city facilities manager. Agree the door posture (for example, return exterior doors to their scheduled state, or lock down and post staff) and which equipment to put in hand mode at the panel with the city maintenance worker, using the building's manual operation sheet | City staff confirm doors and equipment are safe |
| 2. Call the city IT manager. Ask the city to disable the owner's VPN and access control accounts and to change the BAS supervisory administrator password. **Do not try to clean up inside the city's systems alone** | City IT manager has the details and controls the city side |
| 3. From the phone, cancel the remote-desktop subscription or disable the account (if it still exists), change the suite password, sign out all sessions, and check the suite for forwarding rules and new sharing links | Owner's own paths closed |
| 4. Disconnect the laptop from the network (Wi-Fi off, cable out). **Do not power it off or wipe it** | Laptop isolated and still on |
| 5. If the laptop, suite, or phone holds CUI, FCI, or the PIV card may be involved, call the prime's security officer now | Prime informed, time noted |
| 6. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

## 4. Hours 1 to 8: scope and preserve (RS.AN)
1. **Which path was used?** With the city IT manager, compare the access control audit trail, the BAS audit log, the VPN log, and the owner's remote-desktop and suite sign-in history. Look for activity at times the owner was not working.
2. **What changed?** The owner uploads (reads, does not write) the running program from each affected controller and compares it with the saved copies (POL-01 8.5). The city exports the door schedules and administrator changes from the tenant.
3. **What data could be gone?** List what the attacker could reach through the owner's accounts: cardholder exports, drawings, door schedules, CUI sets, work orders.
4. **Preserve.** The IT technician images the laptop disk and saves the suite sign-in history and remote-desktop session history before they roll over, with a chain-of-custody note. Nothing is wiped until the city and, if involved, the prime agree.
5. **Supply chain check.** If the investigation finds equipment that may be covered telecommunications equipment at the federal building, the 1-business-day FAR 52.204-25(d) clock starts (through the prime).

## 5. Hours 8 to 24: notices, restore, and keep the buildings running (RS.CO, RC.RP)
- **Written notice to the city IT manager** before hour 24, even if facts are incomplete. Include what the owner knows of the date and location of the city's last backups, because the city must report them under Fla. Stat. 282.3185(5)(a)2. (48 hours after discovery, 12 hours for ransomware).
- **Restore only clean programs.** Load a saved program into a controller only after the city approves and the copy is confirmed older than the intrusion. Until then, equipment stays in hand mode or on its last safe program.
- **Owner's access comes back last**, through new credentials, a named BAS account, and the city VPN only. The remote-desktop path is never restored.
- **Personal information.** If cardholder exports may have been taken, the owner and the attorney decide whether there is a breach. The owner tells the city within 10 days of determination at the latest (the 24-hour notice normally covers this), and gives the city everything it needs for its own notices.
- **Ransom.** Not paid for any city system. The city may not pay (Fla. Stat. 282.3186).

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Immediately | Prime contractor (for GSA IT, BTTRG 1.6.1); lost PIV card | GSA data, CUI, FCI, or GSA credentials may be involved |
| Within 24 hours of discovery | City IT manager (contract) | Any suspected incident affecting city systems or data |
| Within 1 business day | Covered telecommunications equipment, through the prime (FAR 52.204-25(d)) | Covered equipment identified |
| Within 3 business days | Kaspersky or FASCSA order items, through the prime (FAR 52.204-23(c); 52.204-30(c)) | Such an item identified |
| Within 10 days of determination | City, as third-party agent (Fla. Stat. 501.171(6)(a)) | Breach of city personal information the owner maintains |
| 12 or 48 hours after the city's discovery | The city's own report to the state (Fla. Stat. 282.3185(5)(b)1.) | The city's duty; the owner's facts must arrive first |

**Plan to the shortest clock.** The city's 24-hour contract notice and the prime's "immediately" come long before any statutory deadline.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, internet, city VPN and tenant access with new credentials, a clean laptop, controller program copies, email and files, accounting. Give the city input for its after-action report (due 1 week after remediation, Fla. Stat. 282.3185(6)). Within 30 days of closing, record lessons learned and update P01 (R-001, R-002, R-010), P07, and this runbook. Keep the incident records for 3 years after the contract ends (POL-01 8.6).

# Incident Response Runbook: Ransomware on the Laptop That Reaches the Building Controls

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operator of one mixed-use commercial building) |
| Tier / Vertical | Sole Proprietorship / Commercial Facilities |
| Incident type | Ransomware on the owner's laptop. The attacker uses passwords saved in the browser to sign in to the access control and thermostat portals, and takes guarantor files from the laptop and the file account. Adapted from the registry default "ransomware on building automation systems": at this size the building automation is cloud-managed, so it is reached through the owner's credentials, not by encrypting a server |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 sections 10 and 11 |
| Owner and approver | Owner, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT consultant due 2026-09-30 (P01 R-012) |

Keep a printed copy in the home office and in the management closet. Assume the laptop, the email account, and every password saved in the browser are in the attacker's hands: **use the phone and this paper copy.** Exits are mechanical and always open from inside; no step below may lock an exit.

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Insurer's breach response hotline (data compromise endorsement) | Opens the claim; provides breach counsel and notification help. Call **before** hiring anyone so costs are covered | Hour 0-1 |
| On-call IT consultant | Isolate the laptop, preserve evidence, check the router and the portals | Hour 0-1 |
| Breach counsel (from the insurer) or the real estate attorney | Breach determination, Florida notices, ransom questions | Hours 1-4 |
| Access control vendor support | Confirm administrator sessions are ended, pull the administrator audit log, confirm the door controllers' schedules | Hours 1-4 |
| Installer | Come on site if door hardware or controllers misbehave; confirm its own accounts were not used | Hours 1-8 |
| HVAC contractor | Set thermostats at the wall if schedules were changed | Hours 1-8 |
| Tenants (each lease contact) | Tell them doors and HVAC are being checked; ask them to report anything odd | Hours 4-8 |
| FBI (IC3 online report) and CISA | Voluntary report; supports OFAC mitigation if payment is ever considered | Within 24 hours |

Phone numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: a ransom note or renamed files on the laptop; the antivirus reports ransomware or a password stealer; a door unlocked outside its schedule; an administrator, credential, or schedule appears that the owner did not add; a thermostat schedule changes unexpectedly; a vendor emails about a new sign-in the owner did not make; anyone claims to have the owner's files. **Write down the date and time of discovery.** If personal information may be involved, also write down when the owner first has reason to believe a breach occurred: Florida's 30-day clock runs from that determination (Fla. Stat. 501.171(4)(a)).

## 3. First hour: secure the building first (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Turn off Wi-Fi on the laptop and unplug any cable. **Do not power it off** and do not reply to or pay the attacker | Laptop offline, still on |
| 2. From the phone, in the access control portal: change the password, sign out all sessions, turn on MFA, remove any administrator or credential the owner did not add, and set the entrances to their normal schedule | Only the owner is signed in; no unknown users |
| 3. Same in the thermostat and video portals. Remove the installer's and any unknown accounts for now | Sessions ended; MFA on |
| 4. If the access control portal cannot be trusted or reached: go to the building, lock the entrances with the mechanical keys, and stay or arrange cover until it is fixed. Door controllers keep their cached schedule | Building physically secure |
| 5. From the phone: change the email password, sign out all sessions, move MFA to the app, delete forwarding rules | Email recovered |
| 6. Call the insurer's hotline, then the IT consultant | Both engaged |
| 7. Start the paper incident log: times, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Building controls.** Export the administrator audit log and door event history from the access control portal for the past 30 days before they roll over. Look for added credentials, schedule changes, and remote unlocks. Check the thermostat history and the video portal for deleted clips or new users. Record what changed and set everything back.
2. **What files were taken?** With the IT consultant, list what was on the laptop (downloads, synced folders) and in the file account, and check the file account's activity log. The guarantor and applicant files decide whether Florida notice applies.
3. **Router.** The consultant changes the router password, checks for new port forwards or remote management, and turns on guest isolation. Building devices keep working because they connect outbound to their clouds.
4. **Other accounts.** Change the passwords for the property management, screening, and bank accounts from the phone; confirm their MFA. Warn the bank and the CPA about possible payment fraud.
5. **Preserve evidence.** The consultant images the laptop and saves the portal exports, with a chain-of-custody note (who, when, where stored). No wiping until counsel agrees.

## 5. Hours 8-24: keep the building running and prepare notices (RS.CO, RC.RP)
- **Doors and HVAC:** run on the cached schedules; set thermostats at the wall if the platform is still in doubt (P05 manual procedures). Walk the building at closing time and confirm both entrances locked.
- **Tenants:** tell each tenant what happened to building systems and when doors and HVAC were confirmed normal. Re-issue phone credentials if the credential list was tampered with.
- **Laptop:** do not decrypt and reuse. Reinstall from clean media after evidence is saved; restore files only from a backup made before the incident.
- **Breach determination:** counsel and the owner decide whether personal information was accessed and record the date. Count the affected people and their states of residence. This sets which rows of `notification-matrix.csv` apply.
- **Ransom:** not paid without counsel's advice and an OFAC sanctions check. Paying does not remove notice duties if data was taken. The endorsement does not cover extortion payments.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| No later than 10 days after the vendor determines a breach (inbound) | A vendor that holds personal information for the owner must notify the owner | A vendor breach |
| Within 30 days of determination | Florida individual notice | Guarantor or applicant personal information accessed |
| Within 30 days of determination | Department of Legal Affairs | Only if 500 or more Floridians (not expected) |
| Within 24 hours of declaration (target) | Voluntary report to CISA and the FBI | Any ransomware or portal takeover |
| Same day | Tenants | Doors, credentials, or HVAC affected |

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, trusted door control, thermostat schedules, router and internet, video, property management, then email, files, and the laptop. Within 30 days of closing the incident, record lessons learned and update P01 (R-001, R-002, R-004), P07, and this runbook. Keep all incident records for at least 5 years (POL-01 8.7).

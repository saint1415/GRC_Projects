# Incident Response Runbook: Compromised Laptop with an Attempted Pivot to Client A

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent radiation safety consultant) |
| Tier / Vertical | Sole Proprietorship / Nuclear Reactors, Materials, and Waste |
| Incident type | Registry default "cyber attack on plant business network with attempted pivot to digital assets", adapted: the business has no plant network. Information-stealing malware on the owner's main laptop steals saved passwords and session tokens; the attacker signs in to Client A's contractor portal and the email suite, and malware is copied to the owner's USB drive, the only path toward Client A's plant digital assets |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner-consultant, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-10-09, before the fall outage (POAM-008) |

Keep a printed copy in the field bag and at home. Assume the main laptop, the browser, and the suite account are in the attacker's hands: **use the phone and this paper copy.** The plant is protected by Client A, not by the owner. The owner's job is to stop being a path in, and to tell Client A fast.

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Client A cyber security contact | **8-hour contract clock (CSR-A (5)).** Client A can lock the portal account, check what was accessed, and decide its own 10 CFR 73.77 reports | Hour 0, before anything else that takes time |
| Client A contractor coordinator | Hold the owner's media and any planned kiosk use; plan outage coverage if the owner is tied up | Hours 0-2 |
| On-call IT technician (NDA) | Isolate the laptop, preserve evidence, check the phone and field laptop | Hours 0-1 |
| Client B RSO | **24-hour contract clock (CSIA-B (4))** if Client B working notes were on the laptop or anything of Client B's was in the suite | Within 24 hours |
| Attorney | Contract notices, the W-9 breach question, any extortion demand | Hours 1-8 |
| Professional liability carrier | No cyber policy; report only if a client claim is possible | Day 1 |
| Suite provider support and accounting SaaS support | Lock out the attacker; export sign-in and sharing history | Hours 1-4 |
| FBI (voluntary) | Report after Client A is told, coordinated with Client A | Day 1 |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare this incident when any of these happens: Client A calls about a portal sign-in the owner did not make; **Client A's kiosk flags malware on the owner's USB drive**; the antivirus reports password-stealing malware; the suite warns of a new sign-in or a new forwarding rule; someone asks the owner for Client A plant, security, or network information. **Write down the date and time.** Every clock below runs from that moment of suspicion, not from proof.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Disconnect the laptop from Wi-Fi. **Do not power it off** (memory may hold evidence). Do not plug the USB drive into anything | Laptop offline, still on; drive in a sealed envelope |
| 2. **Call Client A's cyber security contact** from the phone. Say what was seen, when, and that the portal account and the USB drive may be compromised. Ask Client A to disable the portal account and tokens. Note the time and the person | Client A told (8-hour clock met) |
| 3. From the phone, change the suite password, sign out all sessions, remove any forwarding rules or new sharing links, and confirm MFA settings | Only the phone is signed in |
| 4. Change the accounting SaaS and calibration-tracking passwords from the phone | Done |
| 5. Call the IT technician. Start the incident log on paper: time, what was seen, each action, each call | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Client A first.** Give Client A anything it asks for: the time line, the malware name if known, the drive's history (which Client A workstations it touched after kiosk scans, and when). Client A decides whether its plant is affected; do not guess, and do not contact plant staff about the event except through the cyber security contact.
2. **What the attacker could reach.** List with the IT technician: the Client A portal documents the account could open; suite folders and email; saved browser passwords (assume all are known); any Client B notes on the laptop.
3. **Suite and portal history.** Export the suite sign-in, download, and sharing history before it rolls over. Ask Client A for the portal access log for the account for the past 30 days.
4. **Other devices.** The technician checks the phone. The field laptop stays offline (POL-01 9.4). No device goes on the home Wi-Fi until checked; use the phone hotspot.
5. **Preserve evidence.** The technician images the laptop disk and saves logs with a chain-of-custody note (who, when, where stored). The USB drive is kept sealed for Client A if Client A asks for it. No wiping until the attorney and Client A agree.

## 5. Hours 8-24: notices and keep working (RS.CO, RC.RP)
- **Client B:** if any Client B security information was on the laptop or in the suite, tell Client B's RSO within 24 hours (CSIA-B (4)). Client B then decides whether this is suspicious activity under 10 CFR 37.57(b); that is its call.
- **Personal information:** the W-9 sits in the accounting SaaS (and until 2026-09-15 in email). If either account was reached, the attorney and the owner decide whether this is a breach under Fla. Stat. 501.171; the notice to the technician is due no later than 30 days after that determination.
- **Work:** client portals can be reached from the phone for urgent items. If the fall outage is under way, Client A's own workstations and printed work packages carry on (P05, BP-01); the per-diem technician covers surveys for up to one shift.
- **Laptop:** do not clean and reuse it. The technician reinstalls it from clean media (encryption on, standard daily account, no saved browser passwords) after evidence is saved. The USB drive is destroyed, not reused.
- **Extortion:** no payment without the attorney's advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 8 hours of suspicion | Client A cyber security contact (CSR-A (5)) | Anything used for Client A work may be compromised, or someone sought plant information |
| Within 24 hours | Client B RSO (CSIA-B (4)) | Client B security information may have been exposed |
| At once | Client A, if Safeguards Information was ever involved (POL-01 8.4) | Not expected; none held |
| Within 30 days of determination | The per-diem technician (Fla. Stat. 501.171(4)) | The W-9 was in a compromised account |
| Client A's and Client B's own clocks | NRC (10 CFR 73.77) and Client B's regulator (37.57) | Their duties, started by the owner's reports |

**Plan to the shortest clock.** Client A's 8 hours almost always comes first, and Client A's own 1-hour and 4-hour NRC clocks may depend on how fast the owner calls.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: owner access and phone, communications with the clients, a clean device, the field data path, the suite, then calibration-tracking and accounting. Get Client A's written confirmation before the owner's media is used on site again. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-004), P07, and this runbook, and keep all incident records for 6 years (POL-01 8.9).

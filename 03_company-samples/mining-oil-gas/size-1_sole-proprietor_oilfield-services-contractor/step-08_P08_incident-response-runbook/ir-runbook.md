# Incident Response Runbook: Ransomware on the Field Laptop, Threatening Customer SCADA

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated oilfield services contractor) |
| Tier / Vertical | Sole Proprietorship / Mining, Quarrying, and Oil and Gas Extraction |
| Incident type | Ransomware on the field laptop (business IT: email, files, invoices) that also holds customer control programs, the Customer A VPN client, the Customer B remote-desktop client, and customer passwords. The danger is the spread toward Customer A's and Customer B's field SCADA. The owner runs no SCADA of its own |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours; OT steps follow SP 800-82 Rev. 3 sections 6.4 and 6.5 (author mapping) |
| Policy basis | POL-01 sections 10 and 11 |
| Owner and approver | Owner-operator, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-09-30 (POAM-008) |

Keep a printed copy in the truck and the home office. Assume the laptop and the email account are in the attacker's hands: **use the phone and this paper copy.** The first job is to keep the infection out of customer control systems; the second is to tell the customers fast.

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Customer A production superintendent | **Contract clock: notice within 24 hours** (MSA-A (3)). Ask Customer A to disable the owner's VPN account and watch for unexpected setpoint changes | Hour 0 to 1 |
| Customer B operations manager | Ask Customer B to turn off its remote-desktop tool or change the shared password, and watch for unexpected changes | Hour 0 to 1 |
| Customers C and D contacts | Gauge sheets and run tickets may be exposed; rounds continue on paper | Same day |
| On-call IT technician | Isolate and image the laptop; check the phone; rebuild later | Hour 0 to 2 |
| Legal counsel (business attorney) | Contract notices, the helpers' Florida notice, any ransom question | Hours 2 to 8 |
| Insurance agent | No cyber policy yet (due 2026-10-31); ask whether any policy responds before hiring outside firms | Hours 2 to 8 |
| CISA or FBI | Voluntary report, coordinated with Customers A and B | Day 0 to 1 |
| Nearby contract pumper | Cover rounds if the owner is tied up (P05) | As needed |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a ransomware incident when any of these happens: a ransom note or renamed files on the laptop or in the synced folder; the antivirus reports ransomware; files in the email and file account change or vanish in bulk; a customer reports a setpoint change or remote session the owner did not make; a provider warns of a sign-in the owner did not make. **Write down the date and time.** That time starts the 24-hour Customer A clock and is the reference point for the Florida 30 days, which run from determination of the breach (Fla. Stat. 501.171(4)).

## 3. First hour: contain and warn (RS.MI, RS.CO)
| Step | Done when |
|---|---|
| 1. Turn off Wi-Fi on the laptop, disconnect the VPN, and unplug every cable (network, serial, USB). **Do not power it off** (memory may hold evidence). Do not reply to or pay the attacker | Laptop offline, still on |
| 2. **Do not connect the laptop or any USB drive to any customer equipment** until the IT technician clears it. Set the program drives aside in a labeled bag | Drives isolated |
| 3. Call Customer A, then Customer B (section 1). Tell them what was on the laptop and when it last connected to their systems | Both customers told; time noted |
| 4. From the phone, change the email password, sign out all sessions, and check forwarding rules; change the accounting password | Only the phone is signed in |
| 5. Call the IT technician | Engaged |
| 6. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

**If a customer sees loss of control or an unexpected setpoint:** that customer runs its own emergency steps (wells to hand mode or shut in; its hardwired shutdowns protect the tank batteries). The owner helps on site with a clean, offline method only (local panel, not the laptop). If oil reaches water, the customer reports to the National Response Center (notification matrix).

## 4. Hours 1 to 8: scope (RS.AN, RS.MA)
1. **Which customer systems did the laptop reach?** From the remote session log, the change log, and site visits, list every customer controller, workstation, and VPN session in the last 30 days, and every USB drive used since the last clean scan. Give each customer its list.
2. **Which credentials were on the laptop?** List every customer password, VPN profile, and device password the laptop or the synced folder held. These are treated as stolen.
3. **What data left?** With the IT technician, check the email and file account activity history and export it before it rolls over. Note whether the W-9 scans were reachable (they decide the Florida notice).
4. **Is the phone clean?** The technician checks it. Use the phone hotspot only for the phone.
5. **Preserve evidence.** The technician images the laptop disk and saves logs, with a chain-of-custody note. No wiping until counsel and the customers agree.

## 5. Hours 8 to 24: keep the rounds going and prepare notices (RS.CO, RC.RP)
- **Pumping rounds continue** on the paper gauge book; gauges go to customers by phone or text from the phone (P05 BP-01).
- **No automation work** until a clean laptop is ready (P05 BP-02, MTD 48 hours). Customers run affected wells in hand mode if needed.
- **Customer A written follow-up** by email within the 24 hours: what happened, what the laptop held, what Customer A should check, and next update time.
- **Credential changes with customers:** every stolen customer credential is changed by, or with the approval of, the customer that owns the device. Customer B's shared login is retired, not just changed, if Customer B agrees.
- **Florida check:** if the W-9 data was reachable, counsel decides on notice to the 2 helpers within 30 days of determination (notification matrix).
- **Report** to CISA or the FBI, coordinated with Customers A and B.
- **Ransom:** not paid without counsel's advice and an OFAC sanctions check. Paying does not remove any notice duty.

## 6. Deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 24 hours of discovery | Customer A production superintendent (MSA-A (3)) | Always for this incident type |
| Same day | Other customers whose systems or data the laptop held (POL-01 10.3) | Customers B, C, D as applicable |
| Immediately | National Response Center (by the person in charge of the facility) | Only if a release reaches water |
| Within 30 days of determination | Each affected helper (Fla. Stat. 501.171(4)) | W-9 data accessed |

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: phone and contacts, rounds, email access, then a clean laptop. The IT technician rebuilds the laptop from clean media with a standard daily account, MFA everywhere, and the configuration software reinstalled from the makers' sites. **Before any controller is touched again,** compare each one the laptop reached with the last approved version from the offline backup drive (file hashes in the change log), together with the customer (RC.RP-05). Recovery ends when every customer confirms its controllers run approved programs and every exposed credential is changed. Within 30 days, record lessons learned, update P01 (R-001, R-003, R-004), P07, and this runbook, and keep the records for 6 years (POL-01 8.8).

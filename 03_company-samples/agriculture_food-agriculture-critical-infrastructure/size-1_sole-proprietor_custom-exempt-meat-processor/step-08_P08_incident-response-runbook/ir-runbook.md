# Incident Response Runbook: Ransomware on the Shop Laptop with Takeover of the Cold-Chain and Smokehouse Accounts

| Field | Value |
|---|---|
| Organization | Cris Santos Company (custom-exempt meat processing shop) |
| Tier / Vertical | Sole Proprietorship / Food and Agriculture |
| Incident type | Ransomware halting processing and cold-chain monitoring, **adapted to this size**: ransomware on the shop laptop during the October to December busy season, plus sign-ins to the cold-chain account and the smokehouse app with passwords stolen from the laptop browser. Label printing, cut sheets, and the custom records copy on the laptop are lost; alerts may be silenced or redirected; a cook program may be changed |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 sections 10 and 11 |
| Owner and approver | Owner-operator, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-09-30 (POAM-007) |

Keep a printed copy in the shop binder and in the house. Assume the laptop and every password it stored are in the attacker's hands: **use the phone and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Second alert contact (neighboring custom processor, once the reciprocal agreement is signed) | Watch the walk-ins or take product while the owner deals with the computers | Hour 0 if product is at risk |
| Refrigeration service contractor (24-hour line) | Any walk-in above its set point or a unit not running | Hour 0 if temperatures are high |
| On-call IT technician | Isolate the laptop, preserve evidence, check the phone and router | Hour 0-1 |
| Cold-chain vendor support | Lock the account, list recent sign-ins and setting changes, restore alert contacts | Hour 1 |
| Smokehouse manufacturer support | Lock the app account; confirm which programs changed and when | Hour 1 |
| Business attorney (or a data breach attorney the insurer names) | Breach determination under Fla. Stat. 501.171, notices, any ransom question | Hours 1-8 |
| Business liability insurer | Ask whether a cyber endorsement applies **before** hiring any outside firm. No standalone cyber policy (EV-026, EV-028; the endorsement question is an open intake request) | Hours 1-8 |
| Card processor | Only if the phone or card reader may be affected | As needed |
| FBI (IC3 online report) | Voluntary report; supports OFAC mitigation if payment is ever considered | Day 1 |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: a ransom note or renamed files on the laptop; the antivirus reports ransomware; a cold-chain alert contact, set point, or the offline notice changed without the owner doing it; a smokehouse program differs from the printed binder; a vendor emails about a sign-in the owner did not make. **Write down the date and time** in the paper incident log. The Florida 30-day clocks run from "determination of the breach or reason to believe a breach occurred" (Fla. Stat. 501.171(3)-(4)).

## 3. First hour: product first, then contain (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. **Walk the cooler and freezer.** Read both dial thermometers and write them on the paper log. If either is above its set point, call the refrigeration contractor and the second alert contact | Temperatures known and logged |
| 2. **Check the smokehouse.** If a cook is running, compare the program on the panel with the printed binder. If it differs, stop the cook, hold the product, and tag it "HOLD" | No unverified cook running |
| 3. Turn off Wi-Fi on the laptop and unplug it from the printer. **Do not power it off** and do not pay or reply to the attacker | Laptop offline, still on |
| 4. From the phone: change the cold-chain password, turn on MFA, sign out other sessions, and **put the alert contacts and set points back** (38 F cooler, 10 F freezer, offline notice on). Change the smokehouse app password and confirm remote editing is off | Alerts reach the owner again |
| 5. From the phone: change the email, booking form, and accounting passwords; check email forwarding rules | Only the owner's phone signed in |
| 6. Call the IT technician, then the attorney | Both engaged |

Until the cold-chain account is confirmed clean, follow POL-01 11.2: **read the thermometers every hour while awake and at least every 4 hours overnight.**

## 4. Hours 1-8: scope and keep the product safe (RS.AN, RS.MI)
1. **Which product is in doubt?** From the cold-chain vendor, get the temperature history for the past 7 days (the gateway buffers 12 hours when offline) and the activity log of who changed what. From the smokehouse manufacturer, get the program change history. List every batch made or stored while a setting could have been wrong.
2. **Decide on each held batch.** Release product only when the temperature history and the cook record show it stayed within the owner's limits. Product whose safety cannot be shown is not released as food; the owner calls the animal's owner to explain and agree on next steps (`notification-matrix.csv`, customer notice row). Custom product must not be adulterated (9 CFR 303.1(b)(1)).
3. **What data was on the laptop?** With the IT technician, list the synced custom records (names and addresses of about 640 people), cut sheets, kill sheet photos, and the saved passwords. This list decides whether Fla. Stat. 501.171 notices apply.
4. **Keep working.** Label packages from the preprinted "Not for Sale" roll and write the owner's name and cut by hand (9 CFR 316.16, 317.16). Take cut sheets by phone on paper. Cure only from the supplier's printed chart.
5. **Preserve evidence.** The IT technician images the laptop disk and saves the vendor logs, with a chain-of-custody note (who, when, where stored). No wiping until the attorney agrees.

## 5. Hours 8-24: records and notices (RS.CO, RC.RP)
- **Custom records.** Rebuild the current month from kill sheet photos on the phone, paper cut sheets, and invoices. Restore older months from the monthly encrypted export once POAM-003 is in place. The records must stay producible for FSIS (9 CFR 300.6(b)(2); 320.3(a)).
- **Breach assessment.** With the attorney, decide whether personal information was accessed (the geolocation question in P03 section 1.2), how many Florida residents are affected, and whether a documented no-harm determination is appropriate (501.171(4)(c)).
- **Laptop.** Do not decrypt and reuse. The IT technician reinstalls it from clean media (standard user account, no saved passwords, password manager) after evidence is saved.
- **Ransom:** not paid without the attorney's advice and an OFAC sanctions check. Paying does not remove notice duties if data was taken.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Before pickup (same day if scheduled) | Owners of any held or lost product, by phone | Any batch in doubt |
| Within 10 days of a vendor's determination (inbound) | Vendor tells the shop of a breach of its system | Email, file, or booking vendor breached |
| Within 30 days of determination | Florida residents whose personal information was accessed (15 more days only with written good cause to the Department) | Attorney confirms personal information was accessed |
| Within 30 days of determination | Florida Department of Legal Affairs | 500 or more Florida residents affected |
| Within 30 days of the determination | Copy of a documented no-harm determination to the Department | If that path is used instead of individual notice |

**Not triggered for this shop:** FSIS 24-hour notice (9 CFR 418.2) and the Reportable Food Registry, which apply to official establishments and registered facilities. CIRCIA is still a proposed rule.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: temperature watch, power and refrigeration, owner access, internet, a clean laptop with label templates, cook programs and cure sheet, booking and email, then accounting and the records spreadsheet. Compare restored cook programs with the printed binder before use. Recovery ends when alerts have run for 7 days with no unexplained change and every held batch has a written decision. Within 30 days, record lessons learned, update P01 (R-001, R-002, R-003, R-004), P07, and this runbook, and keep the incident records with the custom records for at least the 9 CFR 320.3 period, and 5 years for any no-harm determination.

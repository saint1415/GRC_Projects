# Incident Response Runbook: Email Takeover Used to Divert a Hydrogen Peroxide Load

| Field | Value |
|---|---|
| Organization | Cris Santos Company (specialty chemical distributor, broker) |
| Tier / Vertical | Sole Proprietorship / Chemical |
| Incident type | An attacker controls the owner's email account and uses it to (a) send a supplier a forged pickup change that releases a bulk 50% hydrogen peroxide load to the attacker's truck, and (b) send a customer false bank details. The registry default, an intrusion into process control systems, does not fit a business with no facility. This is the incident that actually threatens chemical security here (P01 R-001, R-002) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10; HSP-01 section 7 |
| Owner and approver | Owner, 2026-10-05 |
| Last tested | Not yet. Walkthrough with one hydrogen peroxide supplier's shipping office due 2026-11-15 |

Keep a printed copy in the home office and one in the car. Assume the email account is in the attacker's hands: **use the phone, the phone's saved contacts, and this paper copy.** Never use a phone number from an email received during the incident.

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Each hydrogen peroxide supplier's shipping office, then the other suppliers | Hold every release; cancel all open pickup numbers; say whether any load left in the last 48 hours | Minute 0 |
| Local law enforcement (911 if a load may be on the road now) | Diverted hazmat: truck, trailer, and driver details from the supplier's gate log | At once if a load is missing |
| Producer's distribution security contact | Product stewardship terms; the producer may know of other attempts | Within the first hour |
| Carrier of record for any affected load | Confirm whether its truck picked up; the real driver's location | Within the first hour |
| Bank fraud line | Recall any wire; freeze new payees; check for attacker access | Within the first hour |
| On-call IT technician | Check the laptop and phone; preserve evidence; help lock down accounts | Hour 1 |
| Business attorney, who refers breach counsel | Driver data breach analysis; customer communications; notices | Hours 1-4 |
| Customers who received invoices in the last 30 days | Warn them not to pay to any changed bank details | Hours 2-8 |
| ERI provider | Tell them a load may be in unknown hands, so they can brief responders who call | Hours 2-8 |
| FBI (IC3 online complaint) | Business email compromise; supports wire recovery | Day 1 |
| Covering distributor | Answer customer calls while the owner works the incident | As needed |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare this incident when any of these happens:
- a supplier calls about a pickup change the owner did not make;
- a carrier arrives for a load that has already left;
- a customer asks about "new bank details";
- the email provider reports a sign-in the owner did not make;
- an unknown forwarding rule appears in the monthly review (POL-01 7.6);
- a bulk load is more than 2 hours overdue with no carrier contact (HSP-01 4.5).

**Write down the date and time.** The Florida 30-day clock runs from the determination of a breach or reason to believe one occurred (Fla. Stat. 501.171(4)(a)).

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Call every supplier's shipping office: **hold all releases, cancel every open pickup number**, and accept new ones only by phone from the owner | All five confirmed by name and time |
| 2. If a load may have gone to the wrong truck: call 911 or local law enforcement with the supplier's gate details, then the producer and the carrier of record | Case number recorded |
| 3. From the phone, take back the email account: new password, sign out all sessions, MFA on, **delete every forwarding rule and filter**, check the recovery phone and address | Only the owner's phone signed in |
| 4. Call the bank: stop or recall payments made in the last 7 days, remove unknown payees, turn on payee-change alerts | Bank reference recorded |
| 5. Start the incident log on paper: time, what was seen, each action, who was called | Log started |

Do not delete the attacker's sent messages or rules before taking screenshots (step 3 of section 4).

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Which loads?** With each supplier, list every release in the last 30 days and compare each driver and truck with the owner's records and the carrier's dispatch. Any mismatch is a possible diversion and goes to law enforcement.
2. **What did the attacker send?** Search the sent folder, deleted items, and the outbox for pickup changes, ship-to changes, bank details, and invoice edits. Screenshot each message with its full header.
3. **What did the attacker read?** Export the email provider's sign-in and activity history before it rolls over. List the folders the attacker could read, in particular driver data, BOLs, pickup schedules, and customer contacts.
4. **Other accounts.** The IT technician checks the laptop for malware and saved-password theft (R-009). The owner changes passwords for the accounting SaaS, bank, and every portal from the phone. Assume any password stored in the browser is known.
5. **Preserve evidence.** Keep the exported logs, screenshots, and the supplier gate records, with a chain-of-custody note (who, when, where stored). Do not wipe the laptop until counsel agrees.

## 5. Hours 8-24: keep shipping safely and prepare notices (RS.CO, RC.RP)
- **Restart releases one at a time.** Issue new pickup numbers by phone or the supplier portal only. Call the carrier dispatch from the approved carrier list to confirm each driver. Hold bulk hydrogen peroxide releases until the owner is confident the account is clean (HSP-01 4.8 elevated measures).
- **Customers.** Call each customer who was invoiced in the last 30 days. Confirm the bank details by phone and ask whether any payment went elsewhere.
- **Driver data.** Count the drivers whose name and license number were in the compromised mailbox, and their states of residence. That count sets which rows of `notification-matrix.csv` apply. Counsel decides between notice and a documented no-notice determination (501.171(4)(c)).
- **ERI provider.** Confirm it holds current data for every product shipped in the last 30 days, because responders may meet a diverted load.
- **No payment to anyone who claims to hold data**, and no payment of any kind without counsel's advice and an OFAC check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| At once | Local law enforcement, the producer, and the carrier of record (company policy) | Any load possibly diverted, or a suspicious order |
| Within hours | Bank fraud line | Any payment on fraudulent instructions |
| Within 30 days of determination | Florida drivers whose license numbers were accessed, or a written no-notice determination sent to the Department within 30 days of making it | Driver data in the compromised mailbox |
| Within 30 days of determination | Florida Department of Legal Affairs | Only if 500 or more Floridians (not expected) |
| Per each state's law | Drivers who live in other states | Non-Florida drivers affected |

The DOT incident reports in 49 CFR 171.15 and 171.16 fall on the carrier in physical possession, not the broker. The business gives the carrier and PHMSA shipment details when asked.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: the phone, control of email, a clean device, the workbook and BOL files, the partner portals, then accounting and the bank. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-008), the P07 POA&M, HSP-01 (which triggers in-depth security retraining within 90 days under 172.704(c)(2)), and this runbook. Keep all incident records for at least 5 years, which also covers the 501.171(4)(c) retention.

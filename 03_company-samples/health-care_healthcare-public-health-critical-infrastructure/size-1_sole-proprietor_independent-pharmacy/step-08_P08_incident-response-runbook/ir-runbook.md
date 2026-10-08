# Incident Response Runbook: Ransomware at the Pharmacy Management System Vendor

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent community pharmacy) |
| Tier / Vertical | Sole Proprietorship / Healthcare and Public Health |
| Incident type | Ransomware at the PMS vendor takes the PMS offline for several days: no profiles, e-prescriptions (including EPCS), DUR, labels, claims, or PDMP file. The vendor reports that patient data may have been taken. Patients are diverted to nearby pharmacies while the pharmacy works on paper. This is the pharmacy's version of "EHR downtime and ambulance diversion" |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours plus recovery |
| Policy basis | POL-01 sections 10 and 11 |
| Owner and approver | Pharmacist-owner, 2026-09-04 |
| Last tested | Not yet. Walkthrough with the relief pharmacist and the IT consultant due 2026-09-30 (POAM-006) |

Keep a printed copy in the downtime kit and at home. The PMS is gone and the vendor's support channel may be part of the attack: **use the phone, the laptop, and this paper copy.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| PMS vendor (status page, support line, account manager) | Confirm the outage, scope, expected restore time, and whether pharmacy data was taken; ask for written updates | Hour 0 |
| On-call IT consultant (BA) | Check the counter desktop for signs of compromise; disable the vendor's remote-support agent; preserve evidence | Hour 0-1 |
| Breach counsel (health care privacy attorney) | Breach and DEA reporting decisions; whether the vendor's discovery date counts as the pharmacy's; notices | Hours 0-4 |
| Insurance agent | No standalone cyber policy (EV-020, EV-029; the coverage question is an open intake request). Ask whether the business owner's or professional liability policy has a cyber or business-interruption endorsement *before* hiring any outside firm | Hours 0-4 |
| Nearby independent pharmacy (transfer arrangement) | Take new prescriptions and transfers for patients the pharmacy cannot serve | Hours 1-2 |
| Main prescriber offices (about 10 send most prescriptions; EV-009) | Route e-prescriptions to another pharmacy for the duration; phone or fax non-controlled prescriptions if the patient wants to wait | Hours 1-4 |
| Relief pharmacist | Extra coverage for the paper workload; confirm availability for the coming days | Hours 1-8 |
| DEA (local Diversion field office) | One-business-day EPCS security incident report (section 5) | By the end of the next business day |
| Florida PDMP (Department of Health) | Manual reporting or an extension request (section 5) | Day 0 to 1 |
| FBI (IC3 online report) | Voluntary report referencing the vendor's incident | Day 1 |

Contact numbers are kept on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a **PMS vendor incident** when any of these happens: the PMS is unreachable for more than 30 minutes with no local cause (check the internet from the phone hotspot); the vendor's status page or email reports a security incident; e-prescriptions stop arriving and prescribers report send errors; the vendor's support agent opens a session nobody requested. **Write down the date and time** and each later vendor statement, word for word. The vendor's notice starts the inbound clocks (vendor to pharmacy: 10 days under Fla. Stat. 501.171(6); 60 days under 45 CFR 164.410, 30 days under the BAA). The pharmacy's own HIPAA clock starts at discovery of a breach (164.404(a)(2)); counsel decides when that is.

## 3. First hour: protect the store side (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Disable or uninstall the PMS vendor's remote-support agent on the counter desktop (the attacker may control the vendor's tools). Do not power the desktop off | Agent stopped; desktop still on |
| 2. Look for signs the desktop is affected: ransom note, renamed files, antivirus alerts, a session nobody started. If any, unplug the network cable and call the IT consultant; treat the CSOS key as compromised (section 5) | Desktop checked; result written in the log |
| 3. From the laptop over the phone hotspot, change the email password and confirm MFA; sign out other sessions | Email secured |
| 4. Put up the door sign and the phone message: limited service, how to get urgent medicines, the nearby pharmacy's address | Patients informed |
| 5. Start the paper incident log: time, what was seen, each action, who was called | Log started |

## 4. Hours 1-8: keep patients safe and divert what cannot be done (RS.MI, RC.RP)
**What the pharmacy can still do, on paper (downtime kit, POL-01 11.2):**
- **Refills of non-controlled maintenance medications** for known patients, using the Friday printed active-patient medication list and the patient's prescription bottle. If the prescriber cannot readily be reached for a refill authorization, a one-time emergency refill of up to a 72-hour supply is allowed (Fla. Stat. 465.0275(1)).
- **New non-controlled prescriptions** that arrive by fax (open the fax portal on the laptop; the fax service is not affected) or by phone from the prescriber's office.
- **Safety checks without DUR:** ask every patient about allergies and other medications, check interactions in the standard drug reference, and write the check on the paper log.
- **Labels:** printed label stock and the handwritten template; record every dispensing on the paper dispensing log.
- **Payment:** hold claims for submission after recovery (BP-03); offer cash pricing only if the patient prefers. The card terminal runs on its own cellular connection.

**Controlled substances:**
- No EPCS can be received or processed. A prescription that says it was first sent electronically must be checked against the PMS once it returns, and one copy voided (21 CFR 1311.200(g)-(h)); until then, do not fill it unless the prescriber confirms by phone that the electronic version was not filled elsewhere.
- Schedule II only on a paper prescription, or in a true emergency on the prescriber's oral authorization, limited to the emergency period, reduced to writing at once, with the written prescription delivered within 7 days (21 CFR 1306.11(d)). If it does not arrive, notify the nearest DEA office.
- Log every controlled substance dispensing on the paper controlled substance log for PDMP reporting.

**Divert what cannot be done safely:** new controlled substance prescriptions, compounded prescriptions that need records the pharmacy cannot reach, and new patients with no history. Call the nearby pharmacy and the main prescriber offices (section 1). Expect most e-prescribed new prescriptions to go elsewhere until the PMS returns.

## 5. Hours 8-24: decisions and the short clocks (RS.AN, RS.CO)
1. **DEA one-business-day decision (21 CFR 1311.215(c)).** With counsel, decide by the end of day 0 whether the attack compromised or could have compromised the integrity of controlled substance prescription records. An attack on the pharmacy application itself usually means "could have." If so, report to the PMS vendor and DEA by the end of the next business day, and record the report.
2. **CSOS key (21 CFR 1311.30(e)).** If step 3.2 found the desktop affected, send a revocation request to the certification authority within 24 hours of confirming it, and apply for a new certificate. Order Schedule II stock by paper form only after counsel confirms the right process.
3. **PDMP (Fla. Stat. 893.055(3)(a)).** Every controlled substance dispensed on paper must still be reported by the close of the next business day. Enter them through the PDMP web portal, or ask the department for an extension before the deadline.
4. **Breach assessment.** Ask the vendor in writing which pharmacy data was on the affected systems and whether it was taken. Start the four-factor risk assessment (45 CFR 164.402) with counsel. The PMS holds records for about 2,400 individuals, so if PMS data was taken, plan for HHS notice at the same time as patient notice, media notice, Florida Department notice, and consumer reporting agency notice (`notification-matrix.csv`). The pharmacy may ask the vendor in writing to send notices for it, but the duty stays with the pharmacy.
5. **Ransom:** the pharmacy does not negotiate or pay; the attack is on the vendor. If the pharmacy's own devices are ever held for ransom, no payment without counsel's advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 24 hours of substantiation | CSOS revocation request | CSOS key or password compromised |
| By the end of the next business day | DEA (and the PMS vendor) EPCS security incident report | Integrity of EPCS records compromised or could have been |
| By the close of the next business day after dispensing | PDMP report (or an approved extension) | Every controlled substance dispensed |
| Within 10 days of the vendor's determination (inbound) | Vendor's notice to the pharmacy | Vendor breach of the pharmacy's data |
| Within 30 days of determination | Florida patient notice (or HIPAA notice with a copy to the Department of Legal Affairs); Department notice if 500 or more Floridians; consumer reporting agencies if more than 1,000 | Florida residents affected |
| Within 60 days of discovery | HIPAA patient notices; HHS at the same time if 500 or more; media if more than 500 Florida residents | Breach of unsecured PHI |
| Within 60 days after year end | HHS breach log | Fewer than 500 affected |

**Plan to the shortest clock.** The DEA and PDMP clocks run in business days, during the outage itself. Florida's 30 days (from determination) can end before HIPAA's 60 days (from discovery).

## 7. Recovery (day 2 onward) (RC.RP, ID.IM)
1. **Before reconnecting:** get the vendor's written statement that the restored PMS is clean and still EPCS-compliant (if it is not, keep EPCS processing stopped: 21 CFR 1311.200(c)-(d)). Change the PMS passwords and confirm MFA.
2. **Catch up:** enter every paper dispensing into the PMS with an annotation that it was filled during downtime; check for duplicate electronic prescriptions and void them (1311.200(g)); confirm all PDMP reports went in; submit held claims; read the daily EPCS audit reports for the whole outage period.
3. **Restore order (P05):** owner access and phone, internet, a clean desktop (the IT consultant reinstalls it if anything was found; the remote-support agent stays off until the vendor explains its role in the attack, then attended mode only), PMS, controlled substance records and PDMP, cloud fax, claims, email and files.
4. **If the vendor cannot restore service within about a week**, the owner considers a new PMS. The vendor must transfer the controlled substance records in a readable format, and the pharmacy must make sure they are migrated or stored so they can be retrieved and printed (21 CFR 1311.305(e)-(f)).
5. **Within 30 days of closing the incident:** record lessons learned; update P01 (R-001), P05 (whether the 12-hour vendor RTO is acceptable), P07, and this runbook; keep all incident records for 6 years (POL-01 8.8).

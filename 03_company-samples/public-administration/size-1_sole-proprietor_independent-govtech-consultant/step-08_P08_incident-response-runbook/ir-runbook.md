# Incident Response Runbook: Ransomware on the Consultant's Laptop (agency data and CJI access)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent GovTech consultant) |
| Tier / Vertical | Sole Proprietorship / Public Administration |
| Incident type | Ransomware on the business laptop (SYS-01) with theft of county extracts and city exports, and a risk that the attacker uses the owner's saved sessions or credentials to reach the sheriff's CJI system or the county's case management SaaS |
| Why this incident | It is the top High risk (P01 R-001) and carries R-002 with it. Adapted from the registry default ("ransomware affecting agency systems holding CJI and FTI"): the owner hosts no agency system and holds no FTI, so the agency systems are at risk **through the owner's access**, and the FTI clock does not apply |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Owner and approver | Owner-consultant, 2026-09-15 |
| Last tested | Not yet. Walkthrough with the IT technician due 2026-10-31 (POAM-009) |

Keep a printed copy, with the agency contact sheet, in the locked file box and with the owner's attorney. Assume the laptop, the browser, and possibly the email account are in the attacker's hands: **use the phone and this paper copy.**

**Whose clocks.** The owner's own clocks are short and come from the contracts: **1 hour** to the sheriff, **24 hours** to the county, **the same business day** to the city, and **10 days** after a breach determination under Fla. Stat. 501.171(6)(a). The longer legal clocks (12-hour ransomware reports, individual notices) belong to the county and city. The owner's job is to tell them fast and give them the facts.

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Sheriff's LASO (CL-03) | Suspected CJI incident: the laptop is the owner's only path into the virtual desktop. Ask the sheriff to end the owner's sessions and suspend the account until the laptop is replaced | **Within 1 hour** |
| Cyber insurer breach hotline | Required before hiring any response vendor; assigns panel breach counsel and a forensic firm | Hours 0-2 |
| County IT security officer (CL-01) | County extracts on the laptop; ask the county to revoke the owner's single sign-on sessions and secure file transfer credentials | Within 4 hours (contract: 24) |
| City IT director (CL-02) | City exports on the laptop; ask the city to disable the owner's 311 accounts | Within 4 hours (contract: same business day) |
| On-call IT technician | Isolate the laptop, preserve it for the forensic firm, check the phone | Hours 0-2 |
| Breach counsel (insurer panel) | Breach determination under Fla. Stat. 501.171, agency notices, ransom questions | Hours 2-8 |
| Productivity suite and password manager providers | Report possible account compromise if sign-ins look wrong (IR-6(3)) | As needed |
| FBI (IC3 online report) | Voluntary report; supports OFAC mitigation if payment is ever considered | Within 48 hours, coordinated with the agencies |

Contact numbers are on the printed contact sheet only, not in this file.

## 2. Declare (Detect)
Declare a ransomware incident when any of these happens: a ransom note or renamed files on the laptop; the antivirus reports ransomware; files in the sync folder change extension or vanish in bulk; an email or post claims to have agency data; a provider or agency warns of a sign-in the owner did not make. **Write down the date and time of discovery.** Every clock in section 6 starts there. When in doubt, declare: the first reports to agencies are for **suspected** incidents.

## 3. First hour (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Turn off Wi-Fi on the laptop and unplug any cable. **Do not power it off** (memory may hold evidence). Do not pay or reply to the attacker | Laptop offline, still on |
| 2. **Call the sheriff's LASO.** Say the laptop used for the virtual desktop has ransomware; ask the sheriff to end the owner's sessions and suspend the account. The hardware token stays with the owner | LASO reached; time logged (must be within 1 hour of discovery) |
| 3. From the phone: change the productivity suite password, sign out all sessions, check MFA methods and mail forwarding rules; change the password manager master passphrase | Only the phone is signed in |
| 4. Pause cloud sync from the web console if files are being encrypted, so the sync folder is not overwritten; note the time so the provider's version history can roll back | Sync paused |
| 5. Call the insurer's breach hotline; start the incident log on paper (time, what was seen, each action, who was called) | Claim number issued; log started |

## 4. Hours 1-8: scope, contain, tell the county and city (RS.AN, RS.MI, RS.CO)
1. **Tell the county and city within 4 hours**, even before scope is known, and ask them to revoke the owner's sessions and credentials. Give each the same short fact sheet (section 5).
2. **What was on the laptop?** From the data location log (POL-01 8.4) and the last quarterly search, list every agency folder, extract, and export and its record counts. This list decides which agencies are affected and how many people.
3. **Was data taken?** The forensic firm (through the insurer) checks for exfiltration. Export the productivity suite sign-in and file activity history before it rolls over.
4. **Agency systems.** Ask the county and the sheriff to check their own logs for the owner's accounts since the last known good day: sign-ins from unknown places, bulk exports, or new tokens. The owner cannot see those logs.
5. **Other devices and accounts.** The IT technician checks the phone. Change every password stored in the password manager that the laptop could have read, starting with agency-related ones.
6. **Preserve evidence.** The forensic firm images the laptop with a chain-of-custody note. No wiping until counsel and the LASO agree (a device that reached CJI is sanitized to the CJIS standard, POL-01 8.6).

## 5. Hours 8-24: keep agencies informed and keep working (RS.CO, RC.RP)
**Fact sheet for each agency** (no CJI, no Social Security or driver license numbers in it):
- what happened and when it was discovered; how it was discovered;
- which of the agency's data was on the laptop, with record counts and data elements;
- the date of the most recent backup, where it is, whether it was affected, and whether it is cloud-based (the county and city need this for a Fla. Stat. 282.3185(5)(a) report);
- any ransom demand details; the owner's contact and the time of the next update.

**Keep working:** agency systems are cloud-reachable from a clean device. Buy a replacement laptop, and have the IT technician build it from the build checklist (encryption on, standard daily account, MFA everywhere). The sheriff's IT unit registers it before the next virtual desktop sign-in (POL-01 12.3).

**Ransom:** no payment without counsel, the insurer, an OFAC sanctions check, and every affected agency's agreement. The county and city may not pay a ransom at all (Fla. Stat. 282.3186). Paying does not remove any notice duty if data was taken.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline (from discovery unless stated) | Notice | Who |
|---|---|---|
| Within 1 hour | Suspected CJI incident to the sheriff's LASO (CJISSECPOL v6.1 IR-6) | Owner |
| Within 4 hours (owner target) | County and city security contacts (contracts: 24 hours and same business day) | Owner |
| Within 12 hours of the agency's discovery | Ransomware report to the Cybersecurity Operations Center, FDLE Cybercrime Office, and sheriff, if the county or city treats it as its ransomware incident (Fla. Stat. 282.3185(5)(b)) | County or city, with the owner's fact sheet |
| No later than 10 days after a breach determination | Third-party agent notice to each affected agency with everything it needs (Fla. Stat. 501.171(6)(a)) | Owner, with counsel |
| No later than 30 days after the agency's determination | Florida individual notices; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 (Fla. Stat. 501.171(3)-(5)) | County or city |
| Within 1 week after remediation | After-action report to the Florida Digital Service (Fla. Stat. 282.3185(6)) | County or city, with owner input |

**Plan to the shortest clock.** The 1-hour sheriff call comes first, and a 4-hour target for the county and city protects their 12-hour clocks. Not applicable here: the IRS Pub. 1075 24-hour FTI report (no FTI), HIPAA (no PHI), CIRCIA (proposed only), and FAR reporting (no federal contracts).

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: phone and MFA, email, internet, a clean laptop, agency access (sheriff registration last, about 1 business day), project files and scripts, then accounting. Complete the sheriff's CJIS refresher training within 30 days of the incident itself (CJISSECPOL v6.1 AT-2 a.2). Within 30 days of closing the incident: record lessons learned, update P01 (R-001, R-002), P07, and this runbook, and keep all incident records for at least 3 years (POL-01 8.7).

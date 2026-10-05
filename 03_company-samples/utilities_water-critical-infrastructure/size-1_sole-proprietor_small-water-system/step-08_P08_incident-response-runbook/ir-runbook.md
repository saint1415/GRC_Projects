# Incident Response Runbook: Remote-Access Compromise of the Treatment HMI

| Field | Value |
|---|---|
| Organization | Cris Santos Company (small community water system) |
| Tier / Vertical | Sole Proprietorship / Water and Wastewater Systems |
| Incident type | Someone signs in to the cloud remote access portal (the owner's reused password or the integrator's account) and changes the panel: hypochlorite feed set to zero, a well pump turned off, or other setpoints changed |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours; OT steps from NIST SP 800-82 Rev. 3 sec. 6.4 |
| Policy basis | POL-01 sections 10 and 11 |
| Owner and approver | Owner-operator, 2026-08-31 |
| Last tested | Not yet. Walkthrough with the relief operator and IT technician due 2026-09-30 (POAM-007) |

Keep a printed copy in the well house binder and at home, with the contact sheet and the manual-operation sheet. **Water first, computers second.** Nothing in this runbook needs the portal to work.

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Relief operator | Second pair of hands at the well house; takes over if the owner must deal with calls | Hour 0 |
| State primacy agency (after-hours number) | Consultation within 24 hours if disinfection or pressure was interrupted (40 CFR 141.202(b)(2)) | As soon as the water is safe, and no later than hour 24 |
| Controls integrator | Confirms whether it made the change; compares the PLC program with its 2023 copy; helps restore | Hours 1-4 |
| Remote access portal vendor support | Lock accounts, end sessions, export the audit log beyond the 90-day screen view | Hours 1-4 |
| On-call IT technician | Checks the laptop and phone for stolen credentials; preserves the portal and router evidence | Hours 2-8 |
| CISA and FBI | Voluntary reports; help for other water systems; OFAC mitigating factor if extortion follows | Day 1 |
| General liability carrier | Ask whether any cyber coverage applies before paying any outside firm | Day 1 |
| Owner's attorney | Questions about notices to customers, the integrator agreement, or any extortion demand | As needed |

Contact numbers are kept on the printed sheet only, not in this file.

## 2. Declare (Detect)
Declare an incident when any of these happens: a setpoint or pump state changes that the owner did not make; the dialer calls with a low residual or low pressure alarm and the panel shows a changed setting; the portal emails a sign-in alert the owner did not cause; the anomaly alert (SYS-08) flags a feed change; the integrator or portal vendor reports a breach. **Write down the date and time.** The Ground Water Rule 4-hour clock starts when the owner determines the system is not maintaining 4-log treatment (141.404(c)), and the Tier 1 clock starts when the owner learns of the situation (141.202(b)).

## 3. First hour: make the water safe (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Go to the well house (call the relief operator on the way if the owner is more than 30 minutes out) | Operator on site |
| 2. **Unplug the cellular router** in the panel. This cuts the portal and the attacker at once; the dialer has its own line and keeps working | Router dark; dialer still armed |
| 3. Put the hypochlorite pump and the wells in HAND and set the dose from the manual-operation sheet | Feed running at a known rate |
| 4. Take a grab sample with the field test kit and record the time and value; repeat every 4 hours until the residual is back at or above the state-specified minimum (141.403(b)(3)(i)(B)) | Residual logged |
| 5. Photograph the HMI screens (setpoints, alarm history) before touching anything else | Photos taken |
| 6. Start the incident log on paper: time of discovery, what was seen, each action, each call | Log started |

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Who signed in?** From the laptop (not the phone, which holds the saved password), call the portal vendor, have it lock both portal accounts and end all sessions, and export the full audit log. Compare sign-ins with the owner's and integrator's known activity.
2. **Integrator check.** Ask the integrator whether it connected. If not, treat its account as compromised too.
3. **What changed?** With the integrator, compare the PLC program and setpoints with the integrator's 2023 copy (or the owner's copy once POAM-005 is done). Assume the logic may have been changed until it is compared.
4. **Credentials.** The IT technician checks the laptop and phone. Change the portal password to a new unique passphrase, turn on MFA before the router is plugged back in, and change any account that shared the old password.
5. **Preserve evidence.** Keep the photos, the exported log, and the router as it is. Write a chain-of-custody note (who, when, where stored).

## 5. Hours 8-24: notices and recovery decisions (RS.CO, RC.RP)
- **Was 4-log treatment restored within 4 hours?** If yes, record the times. If no, it is a treatment technique violation (141.404(c)) and a Tier 2 notice is due within 30 days. Either way, if the state-specified minimum residual was not restored within 4 hours, notify the state **by the end of the next business day** (141.405(a)(1)).
- **Consult the primacy agency** within 24 hours whenever disinfection or pressure was interrupted. If the agency or the owner decides it was a waterborne emergency, the **Tier 1 notice** goes out within 24 hours of learning of the situation (141.202(a) item (7), (b), (c)): hand delivery and posting from the printed contact list, plus billing SaaS email and text if it is working.
- **Stay in hand mode** until the program is verified and remote access has MFA and a new password. Two site visits a day replace remote view (P05 BP-03).
- **Customer data.** An HMI compromise alone involves no personal information. If the billing SaaS or the owner's email was also reached, follow the Florida rows of the matrix.
- **Ransom or extortion:** not paid without legal advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| Within 24 hours of learning of the situation | Tier 1 public notice; primacy agency consultation | Key treatment process interrupted (waterborne emergency) |
| End of the next business day | State notice | Residual not restored within 4 hours |
| Within 48 hours | Report of failure to comply | Any other NPDWR violation that follows (for example a missed grab sample) |
| Within 10 days of completing a notice | Certification and copy to the primacy agency | After any public notice |
| Within 30 days | Tier 2 public notice | 4-log treatment not restored within 4 hours |
| Within 30 days of determination | Florida notice to affected customers | Only if personal information was accessed |

**The shortest clock is the 4-hour one.** It is met at the well house with the hand switches, not at the computer.

## 7. After day 1 (RC.RP, ID.IM)
Restore in P05 order: operator on site, disinfection by hand, supply and pressure, notices, clean remote access (new passphrase, MFA, integrator account disabled), then PLC program verification with the integrator before returning to automatic. Within 30 days of closing the incident, record lessons learned, update P01 (R-001, R-002, R-008), P07, and this runbook, and keep the notice records 3 years and residual records 5 years (POL-01 8.5).

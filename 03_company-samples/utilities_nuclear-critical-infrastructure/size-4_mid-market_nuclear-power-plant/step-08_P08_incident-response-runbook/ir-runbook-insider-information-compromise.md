# Incident Response Runbook: Insider Compromise of Security-Related Information and Safeguards Information

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed owner and operator of a single-unit nuclear generating station) |
| Tier / Vertical | Mid-Market / Nuclear Reactors, Materials, and Waste |
| Incident type | A trusted insider (employee, long-term contractor, or outage contractor) copies, removes, discloses, or tries to obtain **Security-Related Information (SRI)** (CSP documents, CDA inventory and assessments, defensive architecture drawings, security CAP entries) or **Safeguards Information (SGI)**. Variants: (A) departing engineer copies SRI to personal storage; (B) SGI removed, photographed, or found outside the SGI program; (C) an outsider tries to elicit security information from staff; (D) an insider with electronic access to CDAs is suspected of tampering |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF PR.AA, PR.DS, DE.CM-03 (personnel activity monitoring) |
| Policy basis | POL-03 Incident Response Policy (4.1, 4.4, 4.5, 4.8); POL-04 Data Classification and Handling Policy (4.1 to 4.3, 4.8); STD-10 SRI handling standard; SGI program procedures; access authorization program procedures (10 CFR 73.56) |
| Companion documents | `ir-runbook.md` (business network attack); `notification-matrix.csv`; risk register (P01 R-015, R-016, R-017, R-030, R-050); POA&M (P07 POAM-014, POAM-020) |
| Runbook owner | Director of Security (incident lead), with the IT Security Manager for digital evidence and the Cyber Security Program Manager for anything in 73.54 scope |
| Approved | 2026-09-17 by the Site Vice President |
| Last tested | Not yet. Variants A and C are the second module of the 2026-11-05 joint tabletop (POAM-012). A full insider tabletop with Security, HR, General Counsel, IT, the CST, and a Shift Manager follows in 2027 Q1 under the annual exercise rule (POL-03 4.11) |

## 0. Why this runbook exists
The company holds two kinds of information that an adversary would want before attacking the Station:
- **SGI** (10 CFR 73.21-73.22): physical protection details such as security plans, protective strategy, and lock combinations. It is handled only on the stand-alone SGI computers (SYS-16) and in locked containers. The SGI program met every rated requirement in P03, so R-016 is Low and accepted.
- **SRI**: the CSP, the CDA inventory, CDA assessments, and the defensive architecture. It lives on the business network in EDMS restricted folders. P03 found SRI-marked documents on general engineering shares, there is no data loss prevention (DLP) until 2027-01-31 (POAM-020), and USB storage is allowed on business laptops (R-015 and R-050, both Moderate).

The people most able to take this information are trusted: about 64 SGI-authorized individuals, the CST and I&C staff, IT administrators, and engineers. Most of them are in the 73.56 access authorization program with behavioral observation. **An insider event is handled quietly, by a small team, with evidence preserved and the individual's access removed at the right moment.** It is a security event, a personnel action, and possibly a crime at the same time.

## 1. Roles (Govern)
Need-to-know applies to the response itself. The core team is the smallest group that can act; others are told only what they need.

| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Incident lead | Director of Security | Security Operations Manager | Runs the response; decides on access suspension with the reviewing official; SGI program actions |
| Access authorization reviewing official | Reviewing official designated in the 73.56 program (Security) | Alternate reviewing official | Decides whether to unfavorably terminate or maintain unescorted access; informs other licensees under 73.56(o)(6)(i) |
| 73.77 and 73.1200 decisions; ENS calls | Shift Manager on duty | Shift Manager on call | NRC reportability; makes every NRC Operations Center call |
| Digital evidence | IT Security Manager | Security analyst (named for the case) | Covert collection of logs, EDR telemetry, file audit trails; device imaging through counsel's forensic firm |
| CSP technical lead (variant D, or any SRI about CDAs) | Cyber Security Program Manager | CST on-call engineer | Assesses what the SRI reveals; integrity checks of CDAs the person could reach |
| Legal | General Counsel | Outside employment and breach counsel | Privilege, employment law, law enforcement contact, Florida breach decision, decision log |
| HR | HR Director | HR business partner (named for the case) | Personnel actions, interviews, separation, return of company property |
| Regulatory | Regulatory Affairs Manager | Licensing engineer | CAP and security event log entries; written follow-up reports; resident inspector communication |
| Executive | Site Vice President | Plant General Manager | Informed at declaration; convenes the CMT only if the event becomes public or affects operations |

**Conflict check.** If the suspected insider is in IT, the CST, or Security, that function's manager is told only after the incident lead confirms the manager is not involved. If an IT administrator is suspected, evidence collection uses a security analyst and the MSSP, not IT operations staff, and the administrator's privileged sessions are recorded before any action that could alert them.

## 2. Detection and declaration (Detect / DE.CM-03)
| Trigger | Source | Action |
|---|---|---|
| Behavioral observation report about a person with unescorted access (unusual interest in security areas or documents, statements about grievances, unexplained wealth) | Any workforce member (73.56(f)) | Reviewing official and incident lead assess the same day |
| Bulk download from EDMS restricted folders, or SRI copied to USB storage or personal cloud | EDR USB write events; productivity suite audit log; EDMS access log (until DLP is live, 2027-01-31) | Security analyst confirms quietly; incident lead called within 1 hour |
| SRI-marked document found in a general share, a printer tray, email to a personal address, or an AI tool | Quarterly share search (POL-04 4.8); staff report; email gateway | Incident lead decides whether it is a handling error or a possible insider event |
| SGI container inventory discrepancy, SGI found outside a container or the security building, or a phone photo of SGI | SGI custodian; security officer; staff report | **Incident lead at once**; protect the scene and the material |
| Someone asks staff for non-public security or emergency response information (recruiter pretext, social media, conference contact, vendor) | Staff report | Incident lead assesses as a possible 73.1215 suspicious activity (**4-hour** assessment and report clock) |
| CDA configuration change, PMMD kiosk bypass, or unexplained access by a CST or I&C staff member | CST monitoring under the CSP | **CST leads under the CSP** (variant D); Shift Manager informed at once |
| HR notice that a person with SRI or SGI access has resigned, been terminated, or is under discipline | HR | Same-day review of that person's recent downloads and SGI sign-outs (exit review) |

**Severity:**
- **Severity 2:** a handling error with no sign of intent (for example an SRI drawing saved to the wrong share and opened only by staff with need to know). Corrected under STD-10 and recorded in the CAP.
- **Severity 1 (declare immediately):** any sign of intent; any SGI outside the SGI program; any SRI or SGI that may have left company control; any elicitation attempt; any suspected insider action on a CDA.

**Record the date and time of discovery** in the incident log (POL-03 4.3). Several clocks below run from discovery, and two run from the moment law enforcement is called.

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Declare severity; open the case under a code name; list the core team; start the incident log with the discovery time | Incident lead | Log open |
| 0-30 min | **Brief the Shift Manager** with facts only: what information, which person's role, whether that person has unescorted access or electronic access to 73.54 systems, whether law enforcement has been or will be called | Incident lead | Shift Manager acknowledges; D1 opened |
| 0-1 h | General Counsel engaged; counsel engages the forensic firm; privilege protocol as in `ir-runbook.md` section 0 | General Counsel | Counsel on the case |
| 0-1 h | **Preserve evidence quietly:** EDR telemetry, file audit trails, EDMS and share access logs, email and cloud storage logs, badge and turnstile records, SGI sign-out logs, video. Place a legal hold on the person's mailbox and files. Do not image a device the person is still using without counsel's direction | IT Security Manager; Security | Evidence list started with chain of custody |
| 0-2 h | **Contain the information:** remove misplaced SRI from general shares; revoke external sharing links; block the identified personal cloud destination at the web proxy; secure any SGI found and inventory the container | IT Security Manager; SGI custodian | Information secured |
| 0-2 h | **Access decision (D3):** suspend unescorted access, SGI access, and electronic access now, or keep monitoring under counsel's direction? Default: suspend at once if the person has access to CDAs, SGI, or the protected area and intent is suspected | Incident lead with the reviewing official and General Counsel | Decision recorded |
| 0-4 h | **Variant D, or SRI about CDAs:** CST checks the CDAs the person could reach (configuration baselines, PMMD kiosk logs, maintenance and engineering work records) and states whether any CDA may have been affected | Cyber Security Program Manager | CST statement to the Shift Manager |
| 0-4 h | **Shift Manager makes the D1 and D2 decisions** (section 5) | Shift Manager | ENS call made, or "not reportable" documented with the basis |
| Same day | If the person also holds unescorted access under another licensee's program (outage contractors often do), inform that program's reviewing official (73.56(o)(6)(i)) | Reviewing official | Notice recorded |

## 4. Investigation and containment (RS.AN, RS.MI)
1. **Scope the information.** List every document and file the person accessed, copied, printed, or sent in the look-back period (90 days by default; longer if the evidence points earlier). For each item, record its class (SGI, SRI, Restricted personal information, Confidential) and what it reveals. The Director of Security assesses SGI items; the Cyber Security Program Manager assesses SRI about CDAs.
2. **Destinations.** USB devices (EDR device IDs), personal email, personal cloud storage, printing, phone photos (badge and video evidence around SGI rooms), and any AI tool use.
3. **Interview.** HR and counsel interview the person only after evidence is preserved and access decisions are made. A security representative attends. Ask for return of all company information and devices, and for a signed statement of what was taken and where it is. Do not promise any outcome.
4. **Recover.** Collect devices and media. For personal cloud accounts, counsel seeks the person's cooperation or a court order; the company does not log in to personal accounts.
5. **Rotate what the person knew:** shared and service account passwords; vendor VPN credentials; SGI container lock combinations (knowledge of combinations must be limited to authorized individuals with need to know, 73.22(c)(2)); alarm and door codes as the Director of Security decides; and, with the CST, any CDA credentials the person held.
6. **Look for others.** Check whether anyone else accessed the same folders or shared credentials with the person, and whether the event matches a pattern (for example several recruiter contacts across departments).

## 5. Regulatory, legal, and law enforcement decisions (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel keeps the decision log (POL-03 4.8). **No one calls the FBI, local police, or any other agency until the Shift Manager has been told (POL-03 4.5),** because such a call can itself start a 4-hour NRC clock under 73.1200(e)(2) or 73.77(a)(2)(iii). The Shift Manager makes every NRC call and does not wait for legal review.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Cyber notification under 73.77? (a)(2)(ii): a suspected or actual cyberattack initiated by personnel with physical or electronic access to 73.54-scope systems, **4 hours** from discovery. (a)(3): information that may indicate intelligence gathering or pre-operational planning for a cyberattack against 73.54-scope systems (for example someone collecting CDA inventories and network drawings), **8 hours** from receipt. (a)(1) **1 hour** if any CDA function was adversely impacted | Shift Manager with the CST | Shift Manager log; CAP entry within 24 hours (73.77(b)) |
| D2 | Physical security notification under 73.1200? (e)(1)(vii): the compromised SGI reveals a previously unrecognized vulnerability that could prevent implementation of the protective strategy, **4 hours** from discovery, with a written follow-up within 60 days (73.1205). (e)(2): law enforcement was notified of an event related to the security program, **4 hours** | Shift Manager with the Director of Security | Shift Manager log |
| D3 | Suspend or unfavorably terminate unescorted access and SGI access? Inform other licensee programs the same day (73.56(o)(6)(i)) | Reviewing official with the Director of Security | Access authorization file (73.56(m) protections apply) |
| D4 | Suspicious activity (variant C): assess and report within **4 hours** of discovery, in order: local law enforcement, FBI local field office, NRC Operations Center (73.1215(c)(2)-(3)). Not separately required if D2 results in a 73.1200 notification | Director of Security; Shift Manager makes the NRC call | Security event record |
| D5 | If nothing above is reportable: record within **24 hours** of discovery as a physical security event (73.1210(f)) in the safeguards event log or the CAP's security entries, and any cyber program weakness in the CAP (73.77(b)(1)) | Director of Security; Regulatory Affairs Manager | Log and CAP numbers |
| D6 | Refer to law enforcement? Counsel and the incident lead decide; the Shift Manager is told first (see the clock in D2) | General Counsel and Director of Security | Decision log |
| D7 | Was personal information taken (for example access authorization files, HR data)? If so, the Florida breach analysis starts: notice to individuals no later than 30 days after determination; Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 at one time; other states' laws for non-Florida residents | General Counsel | Affected individuals list |
| D8 | Contract notices: insurer (possible employee dishonesty or cyber claim), PE sponsor if severity 1 and material | CFO; CEO | Contract register |

**SGI in notifications.** If an NRC notification must include SGI, the Shift Manager asks the NRC Operations Center for a transfer to a secure telephone. If secure communication is unavailable, the Shift Manager gives the information needed without SGI and says so (73.77(c)(3)(i)). Written follow-up reports that contain SGI are prepared and handled under 73.21 and 73.22 (73.1205).

**Employment and privacy.** HR actions follow the company's disciplinary procedure and the 73.56(l) review procedure for any denial or unfavorable termination of unescorted access. Monitoring of an individual is limited to company systems and authorized by counsel. The person's access authorization file stays in the restricted enclave (SYS-11).

**Communications.** No company-wide announcement. Staff who must act (for example the SGI custodian rotating combinations) are told only what they need. The resident inspectors are informed by Regulatory Affairs after any NRC notification. Media questions go to the Communications Director with a holding statement approved by counsel; the company does not name the individual or describe the information involved.

## 6. Variants
| Variant | Key differences | Notes |
|---|---|---|
| **A. Departing engineer copies SRI** (most likely; R-050) | Usually found in the exit review or through EDR USB alerts. Suspend SRI folder access the day notice is given (R-050 exit review). Recover media before the last day | D1 (a)(3) is possible if the SRI describes CDAs or the defensive architecture. D5 recording and the CAP apply in every case |
| **B. SGI outside the program** (R-016) | Physical first: secure the material, inventory the container, review sign-out logs and video. SGI is never on the business network, so a digital copy anywhere (phone, email, share) is itself a serious finding | D2 and D5. Rotate combinations. The Director of Security decides whether compensatory security measures are needed |
| **C. Elicitation by an outsider** | The staff member who reports it is a witness, not a suspect. Thank them; do not discourage reporting | D4 (73.1215(d)(1)(ii)). If the contact targets cyber information, also D1 (a)(3), 8 hours |
| **D. Insider tampering with a CDA** | The CSP incident response procedure governs; this runbook supplies the personnel, legal, and access steps. Plant safety decisions stay with the Shift Manager | D1 (a)(2)(ii) 4 hours, or (a)(1) 1 hour if a function was adversely impacted. Possible 50.72 report, as set by that section |
| **E. IT administrator abuses access** (R-017, R-030) | Includes the 5 EP-support administrators not yet in the 73.56 program (POAM-014) and the 16 domain administrators who can reach the access authorization enclave (G-065) | Evidence collection by the MSSP and a security analyst; break-glass rotation; D7 if access authorization records were read |

## 7. Recovery (RC.RP)
- Restore the information to its controlled location (EDMS restricted folders or the SGI container) and confirm that all copies outside control are recovered or documented as unrecoverable.
- Complete credential and combination rotation (section 4, step 5) and confirm with the SGI custodian and the CST.
- The Cyber Security Program Manager reviews whether the exposed SRI changes the CSP risk picture (for example whether a compensating control is needed while an exposed design detail is changed) through the CSP change process.
- The Director of Security reviews whether the exposed SGI requires changes to the physical protection program and whether a 73.1200 notification or 73.1210 entry must be updated or retracted.
- Close the HR and access authorization actions and record the outcome in the access authorization file.

## 8. Preparation checks
- [x] SGI program: stand-alone computers, locked containers, marking, need-to-know with FBI criminal history checks (P03 SGI rows Met)
- [x] Behavioral observation training for everyone with unescorted access (73.56(f))
- [x] EDR records USB write events on business endpoints
- [ ] USB storage blocked by default on business laptops (R-050). **Gap until 2027-01-31**
- [ ] Sensitivity labels and DLP for SRI (POAM-020). **Gap until 2027-01-31**
- [ ] Quarterly restricted-folder access review and share search (POL-04 4.8). **First quarterly cycle 2026-12**
- [ ] Dedicated enclave administrators for SYS-11 (G-065). **Gap until 2027-01-31**
- [ ] EP-support administrators enrolled in the 73.56 program or administration reassigned (POAM-014). **Gap until 2026-12-31**
- [ ] HR exit review of SRI downloads and SGI sign-outs for every departure (R-050 treatment). **Starts 2026-11-01**
- [x] FBI field office and local law enforcement points of contact documented in the security communication procedures (73.1215(c)(5), (c)(8))

## 9. Post-incident (ID.IM)
- Lessons learned within 10 business days with the core team; findings into the CAP (with SGI kept in the security entries) and the P01 register (R-015, R-016, R-050).
- Update this runbook, STD-10 (due 2027-01-31), and the SGI program procedures as needed.
- Retain the incident record and decision log: physical security event records 3 years after the last entry or until license termination, whichever is later (73.1210(b)(2)); CSP-related records until license termination (73.54(h)); other records 6 years.
- Report the event and its outcome to the audit committee at its next meeting, without SGI or the individual's name.

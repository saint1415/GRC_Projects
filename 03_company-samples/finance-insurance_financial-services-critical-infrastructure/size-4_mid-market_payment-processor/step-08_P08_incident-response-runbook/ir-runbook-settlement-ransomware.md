# Incident Response Runbook: Ransomware Disrupting Settlement and Merchant Funding

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed payment processor serving merchants) |
| Tier / Vertical | Mid-Market / Financial Services |
| Incident type | Ransomware in the on-premises settlement and funding environment (primary colocation cage). It encrypts settlement batch servers and the managed file transfer servers, so clearing files to the card networks and merchant funding files to both sponsor banks are late by more than 4 hours. The attacker may also have taken data before encrypting |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-34 Rev. 1 for recovery |
| Policy basis | POL-03 Incident Response Policy (4.4, 4.7, 4.11, 4.12) |
| Companion documents | `ir-runbook.md` (compromise of the payment processing environment); `notification-matrix.csv`; BIA (P05 BP-05 to BP-07, section 7); risk register (P01 R-005, R-007, R-009, R-010, R-050) |
| Runbook owner | Director of Settlement and Treasury Operations (business lead) with the Director of Information Security (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Settlement ransomware tabletop with both sponsor banks scheduled 2027-01-27 (POAM-017) |

## 0. Why this runbook exists
Settlement, reconciliation, and merchant funding are **covered services** for both sponsor banks (P05 section 7). About $104 million of merchant funding moves each business day. A ransomware attack on the settlement environment is first a bank and merchant liquidity event, and only then a data question. It is the scenario where the bank service provider notice rules, 12 CFR 53.4 (Bank A) and 12 CFR 304.24 (Bank B), are most likely to apply. The settlement servers are the company's weakest point: 4 run an unsupported operating system (R-010), default credentials were found on management interfaces (R-050), and the DR test took 11 hours against an 8-hour RTO (R-007).

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Incident commander | Director of Information Security | vCISO | Containment, investigation, forensics through counsel |
| Business lead | Director of Settlement and Treasury Operations | Controller | Funding decisions, bank cutoff coordination, manual reconciliation |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Declares severity 1; approves DR cutover, communications, and spending |
| Finance | Chief Financial Officer | Controller | Liquidity view for merchants and the company; sponsor bank financial terms; insurer |
| Bank liaison and notices | Chief Risk and Compliance Officer | General Counsel | 12 CFR 53.4 and 304.24 notices; daily bank calls; card network contacts |
| Legal | General Counsel with outside breach counsel | n/a | Privilege; ransom decision support; notices if data was taken |
| Recovery lead | VP Platform Engineering | Site reliability lead | DR cage cutover, restores, rebuilds |
| Communications | Director of Corporate Communications | Director of Merchant Services | Merchant, ISV, and staff messages; status page |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, mass file encryption, or EDR ransomware detection on a cage server | EDR; MSSP | MSSP isolates the host and calls the incident commander within 30 minutes |
| Backup deletion attempts, disabling of EDR or logging, or new administrator accounts on cage systems | SIEM; PAM; EDR tamper alert | Treat as a ransomware precursor; declare |
| Settlement batch jobs failing across servers, or the managed file transfer service down | Settlement operations monitoring | Business lead and recovery lead triage within 30 minutes; declare if malicious |
| Sign-in to a baseboard management interface or the management network from an unexpected source | Management network logs (after POAM-007) | Block; declare |
| Extortion email or leak-site post naming the company | Email; threat intelligence; law enforcement | Declare; preserve the message |

**Severity 1 (declare immediately):** any confirmed ransomware execution in a cage, or any event that makes a missed funding cutoff likely.

**Start the four-hour clock in the incident log** at the time covered services first stopped or degraded, and record the time the company **determined** that a computer-security incident occurred. The bank notice duty runs "as soon as possible" from that determination (53.4(a); 304.24(a)).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence; declare severity 1; open the out-of-band channel | MSSP; incident commander | Hosts contained; log open |
| 0-60 min | Call the cyber insurer hotline before engaging vendors; counsel engages forensics | Chief Operating Officer | Claim number; counsel on the call |
| 0-60 min | **Protect the DR cage:** stop log shipping from the primary cage; confirm the DR settlement database and HSMs are clean and not reachable from the management network; rotate PAM credentials for cage administrators out of band | VP Platform Engineering | DR cage isolated and verified |
| 0-60 min | Protect backups: confirm the offline and write-once copies are intact; suspend backup jobs from infected hosts | VP Platform Engineering | Backup integrity confirmed |
| 0-2 h | Cut the private interconnect routes from the primary cage to Cloud A except card network links needed by the core switch; block known attacker infrastructure | VP Platform Engineering | Routes down or filtered |
| 0-2 h | **Bank notice decision (D1, section 5.1).** If covered services are, or are reasonably likely to be, disrupted for 4 or more hours, notify both banks' designated contacts as soon as possible. In this scenario the answer is almost always yes, so do not wait for the 4 hours to pass | Incident commander and Chief Risk and Compliance Officer | Decision recorded; notices sent |
| 1-2 h | Convene the CMT; decide whether to cut over settlement to the DR cage (target RTO 8 hours; demonstrated 11 hours) | CMT chair | Decision documented |
| 2-4 h | Ask each sponsor bank to hold its ACH origination window (up to 3 hours under the sponsor agreements); agree the fallback if the window is missed | Director of Settlement and Treasury Operations | Bank confirmation recorded |
| 2-4 h | Merchant and ISV status page notice: deposits may be delayed; no technical details | Director of Corporate Communications | Notice posted |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

**Card authorization keeps running.** The core platform and the gateway are in the clouds and authorize independently of settlement. Authorized transactions queue for clearing. Do not stop authorization unless forensics shows spread to a cloud CDE.

## 4. Analysis and containment (RS.AN, RS.MI)
1. **Scope.** Which cage servers, databases, file transfer servers, HSM management workstations, and identities are affected? Use EDR telemetry, PAM session logs, cage firewall logs, and management network logs.
2. **Entry point and dwell time.** Check the known weaknesses first: the management network route and default credentials on management interfaces (R-050, R-009), the unsupported batch servers (R-010), and vendor remote sessions.
3. **HSMs and keys.** Confirm with the HSM audit logs that no key was exported or used outside normal settlement jobs. If keys were touched, treat stored PAN in the settlement database and archive as potentially unencrypted (16 CFR 314.2) and follow `ir-runbook.md` section 6 for the data side.
4. **Data theft.** Look for archive tools, staging, and outbound transfers from the cage. If account data or merchant owner data was taken, this is also a data compromise: start the Visa, FTC, and state clocks from `ir-runbook.md` section 6.1.
5. **File integrity.** Before any file is sent, confirm that the clearing and funding files to be used were produced by clean systems and match control totals. An altered funding file is worse than a late one (R-052).
6. **Eradication.** Rebuild affected servers from clean images; do not decrypt and reuse compromised systems. Rotate service account, file transfer, and bank connectivity credentials. Forensics confirms that persistence is removed before reconnection.

## 5. Legal, regulatory, and bank communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every legal notice. The Chief Risk and Compliance Officer keeps the decision log.

### 5.1 Decision log
| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Has the incident materially disrupted or degraded, or is it reasonably likely to disrupt or degrade, covered services for either bank for 4 or more hours? | Incident commander and Chief Risk and Compliance Officer | Time of determination; services and banks affected |
| D2 | Does each bank have a designated contact on file? If not, notify its CEO and CIO or two individuals of comparable responsibilities (53.4(a)(2); 304.24(a)(2)) | Chief Risk and Compliance Officer | Contact used |
| D3 | Was any data taken or any key accessed? If so, start the data-compromise clocks | General Counsel with the forensic firm | Privileged findings summary |
| D4 | Ransom decision | CEO on CMT recommendation | See 5.3 |
| D5 | Was the disruption caused by previously announced maintenance or testing? (Then 53.4(b) and 304.24(b) exclude it; a real attack never qualifies) | Chief Risk and Compliance Officer | Change calendar reference |

### 5.2 Notice timeline (plan to the shortest clock)
| When | Action | Owner |
|---|---|---|
| As soon as possible after determination (D1) | **12 CFR 53.4** notice to Bank A's designated contact and **12 CFR 304.24** notice to Bank B's designated contact (or CEO and CIO). Content: what happened, which covered services are affected, expected duration, what the bank needs to do with its ACH window, and the next update time | Chief Risk and Compliance Officer |
| Same day | Card networks: inform them of the delayed clearing files through the sponsor banks, as the banks direct (network rules are the banks' to apply; not restated here) | Director of Settlement and Treasury Operations |
| Day 0 to 2 | Voluntary report to the FBI (IC3) or CISA. It helps the investigation and is a mitigating factor under the OFAC advisory if payment is ever considered | Director of Information Security through counsel |
| Daily until restored | Status calls with both banks; written updates at agreed times | Chief Risk and Compliance Officer |
| Per contract | Merchant and ISV notices of delayed funding; service credits under the agreements | Director of Merchant Services; Director of Sales and Partner Management |
| Only if data was taken (D3) | Visa (3 calendar days), FTC (30 days after discovery for 500 or more consumers), merchants as third-party agent (Florida: 10 days), and state notices: follow `ir-runbook.md` section 6 | Notices cell |

**What the banks do with the notice.** Each bank decides whether the disruption is a notification incident for the bank itself under 12 CFR 53.3 or 304.23, which it must report to its regulator no later than 36 hours after its own determination. The company's prompt, factual notice is what lets the banks meet that clock.

### 5.3 Ransom decision (POL-03 4.11)
The CEO decides after consulting the audit committee chair, the General Counsel, and the insurer. An **OFAC sanctions check** on the threat actor and any wallet is required: the September 2021 OFAC advisory warns that payments to sanctioned persons can bring civil penalties on a strict liability basis, and that license applications for such payments are reviewed with a presumption of denial. Paying does not remove any notice duty and does not guarantee a working decryptor or deletion of stolen data. **The default position, approved by the CEO, is not to pay while the DR cage and offline backups are intact.**

## 6. Business continuity workarounds (RC.RP)
| Process (P05) | Workaround | Limits |
|---|---|---|
| BP-06 Merchant funding | Banks hold the ACH window up to 3 hours. If the file still cannot be produced, fund only merchants whose net amounts can be recalculated from the last clean settlement data and the clearing records, with dual review; never resend an unvalidated file | A full-day delay of about $104 million is likely if the DR cutover exceeds 11 hours |
| BP-05 Clearing and settlement | Hold authorized transactions; send clearing files in the next network window once produced from clean systems | Interchange downgrades on late presentment (P05: about $310,000 a day) |
| BP-07 Reconciliation | Spreadsheet matching from network and bank reports for up to 2 days | Staff overtime; break backlog |
| BP-08 Chargebacks | Work disputes in the networks' portals | No deadlines lost in the first 72 hours |
| BP-13 Merchant support | Status page, scripted answers, callback queue for large merchants | Call volume expected to triple |

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order for the settlement environment (P05 section 8), validating each step before the next.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | PAM and cage administrator access (break-glass if needed) | 1 h | Credentials rotated; sessions recorded |
| 2 | DR cage: payment HSMs with current keys, settlement database promoted from the last clean log | 4 h | HSM key check values match; database integrity checks pass |
| 3 | Bank connectivity at the DR cage (SYS-16 standby) | 6 h | Test files accepted by both banks' file gateways |
| 4 | Funding engine (BP-06) and first funding files | 8 h | Control totals match; dual review; bank acknowledgment |
| 5 | Clearing file builder (BP-05) | 8 h | Network acceptance of the first file |
| 6 | Reconciliation (BP-07) | 12 h | Breaks from the outage listed and assigned |
| 7 | Primary cage rebuilt; log shipping re-established toward the primary only after forensics sign-off | Days | Clean rebuild; segmentation retest |

Tell both banks, merchants, and ISVs when funding is back on its normal schedule (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days, with both sponsor banks invited to the relevant part.
- Update P01 (R-005, R-007, R-009, R-010, R-050), P05 recovery times, the P07 POA&M, and this runbook.
- Report the incident and management's response to the audit committee and in the next Qualified Individual report (16 CFR 314.4(i)).
- If any PCI DSS control failed, inform the QSA; the sponsor banks may ask for evidence under their service provider oversight programs.

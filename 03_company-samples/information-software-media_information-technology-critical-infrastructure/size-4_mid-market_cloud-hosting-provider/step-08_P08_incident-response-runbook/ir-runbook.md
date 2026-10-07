# Incident Response Runbook: Compromise of Provider Tooling Affecting Downstream Customers

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (cloud hosting and managed infrastructure provider) |
| Tier / Vertical | Mid-Market / Information Technology |
| Incident type | An attacker uses a stolen managed services engineer session to push a malicious script through the RMM tool to managed customer servers, including bank customers, and tries to pivot into the Hosting Control Plane and Customer Portal (HCP). The same runbook covers a compromise of the control plane, the CI/CD pipeline, or a template signing key |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response, Logging, and Contingency Policy |
| Companion documents | `ir-runbook-dc1-site-loss.md` (second incident type); `notification-matrix.csv`; BIA (P05); contingency plan (STD-07) |
| Runbook owner | Security Operations Manager (incident commander and federal incident response coordinator) |
| Approved | 2026-09-22 by the Chief Technology Officer; effective 2026-10-01 |
| Last tested | Not yet. Executive and technical tabletop with outside counsel and the MDR partner scheduled 2026-12-15 (POAM-010) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so technical, customer, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Technology Officer. CEO, CFO, General Counsel, Director of Security, Federal Program Director, Financial Services Account Director, Director of Communications, VP Sales, outside breach counsel | Shutting down a service line, customer and public statements, agency and bank relationships, ransom decision (recommendation to the CEO), resources |
| **Incident response team (IRT)** | Incident commander: Security Operations Manager. Director of Managed Services, Security Engineering Lead, SOC analysts, MDR partner, forensic firm (through counsel), VP Software Engineering, VP Platform Engineering, RMM vendor contact | Containment, investigation, eradication, tool validation, recovery order |
| **Customer response cell** | Director of NOC and Customer Support (lead), managed services account managers, Federal Program Director, Financial Services Account Director | Which customers are affected, what each is told and when, help for customers to clean their servers |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander and federal incident response coordinator | Security Operations Manager | Director of Security | Out-of-band group on company phones; printed call tree in each NOC |
| CMT chair | Chief Technology Officer | Chief Executive Officer | Out-of-band group |
| Legal lead | General Counsel | Outside breach counsel (insurer panel) | Out-of-band group |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention). **Call before engaging any incident vendor** | CFO | Policy card in the incident binder |
| Forensics | Panel forensic firm, engaged by counsel | MDR partner incident response team | Through counsel |
| Agencies and FedRAMP | Federal Program Director (agency contacts); federal incident response coordinator (FedRAMP reports) | Director of Security | Agency contact list in the incident binder |
| Defense customers | Federal Program Director | General Counsel | Defense customer contact list |
| Banks | Financial Services Account Director | Director of NOC and Customer Support | Bank designated contact list (38 banks) |
| Communications | Director of Communications | Outside crisis PR (through counsel) | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | CTO | Phone |
| Law enforcement | FBI field office or IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume the attacker can read company email and chat, because the stolen session came from an engineer's laptop. The CMT and IRT use the pre-provisioned out-of-band group and printed call trees.

**Legal privilege protocol.** Outside counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions.

## 1. Preparation checks (Identify / Protect)
- [x] Hardware security keys on the RMM console, identity provider, cloud consoles, and code repository
- [x] EDR on managed customer servers (where the customer bought it), laptops, bastions, and build runners
- [ ] 2 shared RMM super-administrator accounts retired (POAM-020, due 2026-10-31). **Gap**
- [ ] Two-person approval for RMM scripts that target more than one customer (POAM-020, due 2026-11-30). **Gap**
- [ ] RMM audit logs streamed to the SIEM (vendor keeps only 90 days) (POAM-005). **Gap: export RMM logs at once in step 3**
- [x] RMM vendor emergency contact and the procedure to suspend script execution tenant-wide, tested 2026-09
- [ ] Commercial template signing key in the HSM and verified at deployment (POAM-015). **Gap**
- [x] Immutable control plane backups in the backup account (P07 CP-9(1) satisfied)
- [ ] FedRAMP Initial Incident Report template in the FedRAMP JSON format and a human-readable copy (POAM-010)
- [ ] DoD-approved medium assurance certificate for the coordinator and a backup (POAM-021)
- [ ] All 38 bank designated contacts verified (POAM-019, due 2026-10-31)
- [x] Affected-customer lookup: RMM site list joined to the CRM, with a "bank" and "federal" flag

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| RMM job that runs the same script on many customers, outside a change window | RMM job log; SIEM rule once RMM logs are onboarded; MDR partner | Suspend the job; call the incident commander within 15 minutes |
| EDR alerts on several managed customer servers at once with the RMM agent as parent process | EDR (MDR partner) | Declare; isolate affected servers through EDR where the customer contract allows |
| Engineer sign-in to the RMM console from a new device or location, or session reuse | Identity provider; RMM | Revoke sessions; declare if unexplained |
| A customer reports ransomware or unknown changes on managed servers | NOC ticket | Check the RMM job history for that customer within 30 minutes |
| Bulk snapshot, delete, or export actions by a control plane service identity | Control plane audit log; SIEM | Freeze the service credential; declare |
| Attempts to reach PAM, hypervisor managers, or the pipeline from managed services accounts | PAM; firewall logs | Block; declare |
| Pipeline or signing key used outside the release process | Code hosting audit log; HSM log | Freeze releases; declare |

**Severity 1 (declare at once):** any malicious script executed through the RMM tool on more than one customer, any confirmed use of control plane, pipeline, or signing credentials by an attacker, or any sign of access to the government partition.

**Record three times in the incident log** (POL-03 section 4.5): the time the incident was **discovered** (DFARS 72-hour clock), the time it was **confirmed** (MSA 72-hour clock), and the time of each **determination** (bank rule, FedRAMP reportability, state law).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | Suspend all RMM script execution tenant-wide through the vendor console or emergency contact; disable the compromised engineer's identity and revoke all RMM sessions | Director of Managed Services; SOC on call | No RMM jobs running |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log with discovery time | Incident commander | Log open |
| 0-30 min | **FedRAMP reportability (IEC-CSO-EFR).** The RMM tool is barred from government tenants, but the attacker may pivot. If federal customer data is affected or likely affected, it is a FedRAMP Reportable Incident: treat it as PAIN-5 unless a PAIN rating is estimated at once (IEC-CSO-DPR) | Federal incident response coordinator | Decision in the log with time |
| 0-60 min | If reportable: **Initial Incident Report within 1 hour** (Class C, PAIN-3 to PAIN-5) to fedramp_security@fedramp.gov, the affected agencies by their own procedures, and all necessary parties through the trust center (until it exists, the legacy secure repository) | Federal incident response coordinator | Report sent; time logged |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages forensics | CFO | Claim number; counsel on the call |
| 0-60 min | Export RMM audit logs, job history, and script contents before the vendor's 90-day retention matters; hash and store them in the log archive account | Security Engineering Lead | Exports hashed and stored |
| 0-2 h | **Protect the platform:** rotate control plane service credentials (government first), freeze releases, revoke all managed services engineers' standing access to PAM, and block managed services subnets from management networks | Security Engineering Lead; VP Software Engineering | Rotation and blocks confirmed |
| 0-2 h | Confirm backups are intact (control plane backups write-once; customer backup platform catalogs at DC-2 and DC-3) | Director of Backup and DR Services | Integrity confirmed |
| 1-2 h | Build the **affected customer list** from the RMM job history: customer, servers, script run, time, and flags for banks, defense contractors, and federal tenants | Customer response cell | List in the incident log |
| 1-2 h | Convene the CMT; first situation report (scope, customers affected, decisions needed) | CMT chair | Meeting held |
| 2-4 h | **Bank determination.** For each affected bank: has the incident materially disrupted or degraded covered services, or is it reasonably likely to, for 4 or more hours? If yes, notify the bank's designated contact as soon as possible (12 CFR 53.4(a)). Do not wait for the 4 hours to pass | Financial Services Account Director with General Counsel | Determination and notice times logged per bank |
| 2-4 h | First customer notice to affected managed services customers: what we know, what we suspended, what they should check | Director of NOC and Customer Support, approved by General Counsel | Notice sent |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |

## 4. Analysis (RS.AN)
1. **Scope on customer servers.** Which customers and servers ran the script, what it did (encryption, credential theft, persistence, data staging), and whether it spread inside customer networks. Use RMM job logs, EDR telemetry where the company manages EDR, and customer-provided logs.
2. **Initial access.** How the engineer session was stolen (token theft from the laptop, a malicious browser extension, a help desk reset). Check the identity provider for other sessions from the same device or network.
3. **Pivot attempts.** Review PAM, hypervisor manager, cloud, and pipeline logs for the stolen identity and any new identities. Confirm no access to the government partition, or bring the timeline forward for FedRAMP and DFARS reports.
4. **Preserve evidence.** Image the engineer's laptop and any affected company servers, export logs with chain of custody (who collected, when, hash, storage), and keep images and monitoring data at least 90 days after any DFARS report (252.204-7012(e)).
5. **Data affected.** For each affected customer, what personal information or covered defense information could the script reach? This drives the state law and DFARS steps.
6. **PAIN estimate.** If federal customer data is involved, estimate the PAIN rating (N1 minimal effect on one or more agencies, up to N5 debilitating effect on more than one agency) and record the reasoning (IEC-CSO-EFI).

## 5. Containment, eradication, and tool validation (RS.MI)
1. Keep RMM script execution suspended until validation is complete. Customers use their own remote access for urgent work (P05 BP-07).
2. Remove malicious scripts, scheduled jobs, and any agent policy changes from the RMM tenant; rotate every RMM credential and API key; rebuild the engineer's laptop.
3. Give each affected customer a cleanup package (indicators, script hash, steps) and offer engineer help. Customers decide on restores of their own servers; the backup service restores on request with bank and agency requests first.
4. **Validate the tool before reuse (POL-03 section 4.7).** The RMM vendor confirms its platform was not the source, the SIEM shows no unexplained jobs for 72 hours, two-person approval and per-customer scoping are on, and the shared super-administrator accounts are gone. The Director of Security signs off.
5. If the pipeline or a signing key was touched: revoke and replace the key in the HSM, rebuild templates from clean source, re-sign, and tell customers which template versions to redeploy.
6. Forensics confirms persistence is removed before managed services resume.

## 6. Legal, regulatory, and customer communication (RS.CO)
**Follow `notification-matrix.csv`.** General Counsel or outside counsel confirms every external notice before it goes out. The incident commander keeps the **clock log**: each obligation, the event that started it, the start time, the deadline, and the time sent.

| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | Is this a FedRAMP Reportable Incident (confidentiality or integrity of federal customer data affected or likely)? PAIN rating or default PAIN-5? | Federal incident response coordinator with the Federal Program Director | Clock log |
| D2 | Is covered defense information of a defense customer affected? If yes, the 72-hour DoD report runs from discovery | Federal Program Director with General Counsel | Clock log |
| D3 | For each bank: material disruption of covered services for 4 hours or more, actual or reasonably likely? | Financial Services Account Director with General Counsel | Per-bank determination |
| D4 | For each customer: breach of security of personal information we maintain for them (state third-party agent duty; Florida: 10 days) and MSA notice within 72 hours of confirmation | General Counsel | Customer notice log |
| D5 | Any FAR clause report (covered telecommunications, Kaspersky, FASCSA article found during the investigation)? | General Counsel | Clock log |
| D6 | Has law enforcement asked for a delay of any notice? | Outside counsel | Written record |
| D7 | Ransom decision | CEO, on CMT recommendation | See below |

**Timeline (plan to the shortest clock):**
| When | Action | Owner |
|---|---|---|
| Within 1 hour of the reportability decision (PAIN-3 to PAIN-5; 24 hours for PAIN-2; 1 business day for PAIN-1) | FedRAMP Initial Incident Report to FedRAMP, agencies, and all necessary parties (IEC-CSO-IIR, Class C). Mandatory from 2027-01-01; the company follows it now as its standard, alongside each agency's ATO terms | Federal incident response coordinator |
| Every 6 hours for PAIN-3 to PAIN-5 (24 hours for PAIN-2; 1 business day for PAIN-1) | Ongoing incident reports, including "no new information" updates (IEC-CSO-OIR) | Federal incident response coordinator |
| As soon as possible after the determination | Bank notice to at least one designated contact at each affected bank; if none on file, the bank's CEO and CIO (12 CFR 53.4(a)(1)-(2)) | Financial Services Account Director |
| Hour 0-1 | Insurer hotline; counsel engaged | CFO |
| Day 0-2 | Voluntary report to the FBI (IC3) and CISA; it helps the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory) | Security Operations Manager through counsel |
| Within 72 hours of discovery | DoD report through the DoD reporting portal for any incident affecting covered defense information, coordinated with the defense customer, who must also report under its own clause; submit malicious software to DC3 as instructed (252.204-7012(c), (d)) | Federal incident response coordinator |
| Within 72 hours of confirmation | MSA notice to every affected customer | Director of NOC and Customer Support with General Counsel |
| Within 10 days of determining a breach of personal information held for a customer (Florida worked example) | Third-party agent notice to the customer, which is the covered entity and owns the notices to individuals (Fla. Stat. 501.171(6)); other states' laws per affected residents | General Counsel |
| Within 6 hours of resolution and recovery (PAIN-3 to PAIN-5; 1 business day for PAIN-1 and PAIN-2) | FedRAMP Final Incident Report (IEC-CSO-FIR) | Federal incident response coordinator |
| 90 days after any DFARS report | Earliest date preserved images may be released, unless DoD asked for them | Security Operations Manager |

**Why the bank and FedRAMP clocks come first.** The FedRAMP clock is 1 hour from the reportability decision, and the bank clock runs "as soon as possible" from the determination that a 4-hour disruption is likely, which in a tooling compromise is usually within the first hours. Banks must notify their own regulator within 36 hours of their own determination (for example 12 CFR 53.3), so a late notice from the company makes the bank late too.

**Ransom decision (POL-03 section 4.8).** Needs the CEO, counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet; and a report to law enforcement. The extortion demand may target the company even though customer servers were encrypted. Paying does not remove any notice duty. The default position, approved by the CEO, is not to pay.

**Communications.**
- Managed services customers: first notice within 4 hours, then updates every 12 hours; a dedicated support line.
- All other customers: status page notice if any shared service is suspended; no customer names.
- Agencies and defense customers: direct calls from the Federal Program Director, matching the FedRAMP reports.
- Media: holding statement approved by counsel; no attribution, ransom, or customer names.
- Staff: daily briefings on the out-of-band channel; reminder of POL-05 section 4.7.

## 7. Recovery (RC.RP, RC.CO)
Recovery follows the BIA (P05). The RMM tool and the pipeline are restored last on purpose: after a compromise they must be validated before they are trusted again.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Identity provider, PAM, and break-glass access | 1 h | All sessions revoked; privileged credentials rotated |
| 2 | Control plane service credentials and releases (both partitions) | 4 h | New scoped credentials; no unexplained actions in audit logs |
| 3 | Customer backup restores for affected customers, banks and agencies first | 6 h for the first restores | Restore points before the script ran |
| 4 | SIEM coverage of RMM, PAM, and control plane | 8 h | Monitoring confirmed before managed services resume |
| 5 | RMM tool, read-only monitoring first | 24 h, after validation (section 5 step 4) | Director of Security sign-off |
| 6 | RMM patching and scripts, one customer at a time with two-person approval | 72 h | No anomalies for 72 hours |
| 7 | CI/CD pipeline (if touched) | 48 h | New signing key; clean rebuilds verified |

Tell customers, banks, agencies, and defense customers when each service is restored (RC.CO). Keep the bank and agency contacts updated until the final report.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days.
- Update the risk register (P01: R-001, R-002, R-011, R-015, R-022, R-025, R-030), the POA&M (P07), this runbook, and STD-02.
- Review the RMM vendor relationship under STD-09, including its own incident notice performance.
- Record whether any change made during recovery is a FedRAMP significant change (SCN-CSO-EVA) and notify accordingly.
- Retain all incident records, the clock log, notices, and evidence for at least 6 years (POL-01 section 4.16).

## 9. Not current obligations (tracked)
- **CIRCIA:** no final rule as of 2026-09-25. If finalized as proposed, a covered entity would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours. Not part of this runbook until a final rule takes effect.
- **SEC Form 8-K Item 1.05:** does not apply; the company is privately held.

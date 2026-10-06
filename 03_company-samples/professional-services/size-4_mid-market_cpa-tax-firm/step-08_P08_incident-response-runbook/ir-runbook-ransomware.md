# Incident Response Runbook: Ransomware with Data Extortion in Filing Season

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed CPA, tax, and advisory firm, with its attest affiliate) |
| Tier / Vertical | Mid-Market / Professional, Scientific, and Technical Services |
| Incident type | Ransomware that encrypts the DMS, the workpaper application, the virtual desktop pool, and endpoints, after the attacker has copied client files (double extortion), during the February to April filing season. Variant (section 9): the tax software vendor itself suffers ransomware or an outage near a deadline |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy; part of the written incident response plan required by 16 CFR 314.4(h) (N54-R01) |
| Companion documents | `ir-runbook.md` (BEC and taxpayer data theft; holds the full role tables, decision log, and three-date rule); `notification-matrix.csv`; BIA (P05); risk register (P01 R-004, R-005, R-007, R-017, R-018, R-019) |
| Runbook owner | Director of Information Security (incident commander); Chief Information Officer (recovery lead) |
| Approved | 2026-09-22 by the Chief Operating Officer |
| Last tested | A 2025 technical tabletop only. Executive tabletop with outside counsel scheduled for 2027-02-24, inside the filing season on purpose (POAM-014); deadline-week vendor outage tabletop 2027-01-12 (POAM-011) |

## 0. Governance (Govern)
The three tiers and contacts in `ir-runbook.md` section 0 apply. Two additions for ransomware:
- **Deadline cell.** The National Tax Practice Leader, the Director of Tax Operations, and the CAS Practice Leader form a deadline cell inside the CMT. It decides early extensions, payroll fallbacks, and which offices or teams work from which systems.
- **Recovery authority.** The Chief Information Officer leads recovery. No segment is reconnected without the incident commander's and the forensic firm's sign-off.

## 1. Preparation checks (Identify / Protect)
- [x] Immutable backups of the DMS, workpaper application, and file services in a separate backup account and region, 35-day write-once retention, separate credentials (CP-9; P07 fully satisfied)
- [x] EDR on all managed endpoints and servers with 24x7 MSSP (SI-3)
- [ ] Restore test of the workpaper application within the last 90 days. **Gap until POAM-011 closes (first test 2026-11-17)**
- [ ] Privileged access management for directory and SaaS administrators; no standing admin rights. **Gap until POAM-002 closes (2027-01-15)**
- [ ] Service account credentials vaulted and rotated. **Gap until POAM-012 closes**
- [ ] Break-glass accounts for the identity provider and productivity suite (P01 R-007)
- [x] Extension filing procedure for every return type, with the e-file team trained to file extensions in bulk through the tax software
- [ ] CAS repeat-payroll fallback documented and exercised with the payroll vendor (POAM-011, due 2027-03-31)
- [x] Incident binder at every office; printed client list with phone numbers for the 500 highest-priority deadline clients, refreshed each February 1

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass renaming or encryption of files | EDR; staff report | MSSP isolates the host (automatic for high-confidence detections) and calls the incident commander within 30 minutes |
| Attempts to delete backups, disable EDR, or stop logging | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| New directory administrator, or elevation outside hours | SIEM; privileged access broker | Disable the account; declare if unexplained |
| Large outbound transfer from the DMS or file services | Cloud firewall flow logs (egress alerting due 2026-12-15, POAM-007) | Block the destination; declare |
| Extortion email or a leak-site post naming the Company | Email; threat intelligence; FBI | Declare; preserve the message |
| Offices report the DMS or virtual desktops unavailable | Staff | IT triage; declare if malicious |

**Severity 1 (declare immediately):** any confirmed ransomware execution, confirmed data exfiltration, or an extortion claim naming Company data. Record the discovery date in the incident log (POL-03 4.3).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Isolate affected hosts through EDR; keep them powered on for memory evidence | MSSP; security engineers | Hosts contained |
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log | Incident commander | Log open |
| 0-1 h | Call the insurer's hotline; counsel assigned; counsel engages forensics | Chief Financial Officer | Claim number; counsel on the call |
| 0-1 h | Protect the backup account: confirm the write-once lock is intact; suspend cross-account backup jobs; rotate backup administrator credentials out of band | Chief Information Officer | Backup integrity confirmed |
| 0-2 h | Cut the site-to-cloud VPN tunnels and hub routes to affected segments; close the virtual desktop gateway (offshore and remote seasonal staff go offline); block attacker infrastructure | Chief Information Officer | Routes down or filtered |
| 0-2 h | Revoke all sessions in the identity provider; reset privileged credentials with break-glass accounts; disable vendor remote access | Director of Information Security | Sessions revoked |
| 1-2 h | Convene the CMT and the deadline cell; first situation report | CMT chair | CMT meeting held |
| 2-4 h | **Deadline decisions:** staff keep working in the tax software (vendor SaaS) from clean or personal-use-approved devices only if the incident commander confirms the identity provider and the tax software tenant are not affected; otherwise start early-extension triggers (section 5) | Deadline cell | Decision recorded |
| 2-4 h | **CAS payroll:** confirm the next 48 hours of client pay dates; if Company endpoints or identity are down, start the vendor repeat-payroll fallback | CAS Practice Leader | Payroll plan for each client due in 48 hours |
| 2-4 h | CEO informs the audit committee chair and the sponsor's operating partner; CFO checks lender notice terms | Chief Executive Officer; Chief Financial Officer | Notices given or scheduled |

## 4. Analysis (RS.AN)
1. **Scope.** Which endpoints, servers, cloud accounts, and identities are affected? Use EDR telemetry, identity provider logs, cloud control-plane logs in the locked log archive, and firewall flow logs.
2. **Initial access and dwell time.** Find the entry point (phishing, an exposed gateway, a vendor remote tool, or a stolen service account) and the first date of access. Backups taken after that date may hold attacker persistence.
3. **Exfiltration.** Determine what was taken: archive tools, staging folders, cloud storage access, egress volume, and leak-site samples. Build the **affected-individual list** as in `ir-runbook.md` section 4 step 7, by data class, state, covered entity client, and CAS client. Over-retained files (P01 R-016) count, which is why the disposal program matters.
4. **Tax data integrity.** Check whether the attacker reached the tax software tenant or changed refund bank fields (P01 R-047). If so, run the refund hold in `ir-runbook.md` section 3.
5. **Offshore pool.** Confirm the virtual desktop pool was not the entry point and that no offshore vendor account was used. The pool returns only after section 6 validation and only with masking and consent checks in place (BIA BP-06).
6. **Preserve evidence.** Forensics images key hosts and exports logs before retention expires, with chain of custody, held by the forensic firm under counsel.

## 5. Keeping deadlines and payrolls (RC.RP)
| Situation | Action | Owner |
|---|---|---|
| Tax software (vendor SaaS) unaffected, but Company endpoints or DMS down | Staff work in the tax software from clean devices; source documents come from portal uploads and paper originals (BIA BP-04 workaround) | National Tax Practice Leader |
| Recovery of BP-01 to BP-03 not expected within their 8-hour RTO, within 10 days of a deadline | **Early-extension trigger:** file extensions for every unfinished return due on that deadline, highest-balance clients first; tell clients by phone and the portal | Director of Tax Operations |
| Identity provider or endpoints unavailable within 48 hours of a client pay date | CAS repeat-payroll fallback through the payroll vendor; manual adjustments only for terminated employees | CAS Practice Leader |
| Workpaper application down | Attest teams work offline; engagement partners call clients with report dates in the next 10 days | Attest Firm Managing Partner |

## 6. Containment, eradication, and recovery (RS.MI, RC.RP)
Restore in BIA priority order (P05 section 7). Each step is validated before the next begins: EDR clean, credentials rotated, patches applied, and forensics sign-off for the segment.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Identity provider and administrator access (break-glass if needed) | 2 h | Sessions revoked; privileged credentials rotated; no attacker persistence in the directory |
| 2 | CAS payroll access for the payroll team | 8 h | Clean devices; payroll vendor confirms no unauthorized changes |
| 3 | Tax software access and the e-file queue | 8 h | Vendor confirms tenant integrity; held returns reviewed |
| 4 | Email (productivity suite) | 8 h | Mail rules and app consents reviewed tenant-wide |
| 5 | SIEM feeds and the EDR console | 4 h | Monitoring confirmed before wider reconnection |
| 6 | DMS, rebuilt from templates and restored from backups taken before the first attacker access | 12 h | Restore verified against a sample of client folders |
| 7 | Endpoints for tax teams, then CAS and the document processing center | 24 h | Rebuilt from gold images; EDR healthy |
| 8 | Virtual desktop pool (offshore and remote seasonal staff) | 48 h | Masked DMS view and consent gate in place before reconnection |
| 9 | Practice management and billing (vendor SaaS) | 48 h | Payment page and bank details checked |
| 10 | Workpaper application | 72 h | Restore from backup (first test due 2026-11-17) |

**Do not decrypt and reuse compromised systems.** Tell staff, clients, CAS clients, and the attest clients with near report dates when services return (RC.CO).

## 7. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv` and the decision log in `ir-runbook.md` section 6 (D1 to D7).** Counsel confirms every notice. Additions for ransomware:

| When | Action | Owner |
|---|---|---|
| Hour 0-1 | Insurer hotline; counsel engaged | Chief Financial Officer |
| Day 0-2 | Report to the FBI (IC3 or field office) and, voluntarily, to CISA. Reporting helps the investigation and is a mitigating factor if a payment is ever considered (OFAC advisory) | Director of Information Security through counsel |
| As soon as confirmed that taxpayer information may be affected, and **no later than the next business day** | IRS report through the Stakeholder Liaison (Pub. 1345); state tax agencies the same day | Director of Tax Operations |
| Per agreement | Lenders (credit agreement), the private equity sponsor, CAS clients (agreements), and attest clients (engagement letters) | Chief Financial Officer; CAS Practice Leader; Attest Firm Managing Partner |
| Per each BAA and no later than 60 days after discovery | Covered entity clients if PHI was in the encrypted or exfiltrated data (45 CFR 164.410) | Privacy Officer |
| No later than 30 days after discovery | FTC notice if customer information of 500 or more consumers was acquired. Exfiltrated data counts; data that was only encrypted in place by the attacker and not taken is a question for counsel | Privacy Officer with counsel |
| Within 30 days after determination | Florida individual, Department, and consumer reporting agency notices; other states by their laws | Privacy Officer with counsel |

**Ransom decision (POL-03 4.9).** Needs the Chief Executive Officer, outside counsel, and the insurer; an **OFAC sanctions check** on the threat actor and any wallet (OFAC can impose civil penalties for payments to sanctioned parties on a strict liability basis); and a report to law enforcement. Paying does not remove any notice duty when data was taken, and does not guarantee deletion. The default position, approved by the Chief Executive Officer, is not to pay while backups are intact.

**CIRCIA.** The final rule is not published, so no CISA report is required. The CISA report in the table above is voluntary.

**Communications.** A website and portal notice within 24 hours of any client-visible disruption, with a call-center script; direct calls from partners to the 500 highest-priority deadline clients; a holding statement for media approved by counsel (no ransom, attribution, or technical details); daily staff briefings by text or phone through the out-of-band channel.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery; written report within 30 days (POL-03 4.11).
- Update the risk register (P01 R-004, R-005, R-007, R-016, R-018), the BIA values if impacts differed (P05), the POA&M (P07), and this runbook.
- Include the event in the Qualified Individual's next written report to the board (314.4(i)).
- Keep all records for at least 6 years (POL-01 4.13).

## 9. Variant: tax software vendor ransomware or outage near a deadline
The tax software vendor (SYS-01) is a single point of failure for BP-01 to BP-03. Its SOC 2 RTO of 8 hours equals the BIA RTO with no margin (P05 finding 1; P01 R-017).

| Step | Action | Owner |
|---|---|---|
| 1 | Confirm the outage on the vendor status page and with the account manager; record the time the Company learned of any vendor security incident | Director of Tax Operations |
| 2 | If the vendor reports a cyber incident: disable integrations and API credentials to the vendor, and hunt for the vendor's indicators of compromise in Company logs | Director of Information Security |
| 3 | **Early-extension trigger:** if the vendor's expected restoration is later than 8 hours and a deadline is within 10 days, file extensions as soon as the vendor's extension service or IRS e-file is available, and paper extensions with proof of mailing as a last resort | Deadline cell |
| 4 | Tell clients through the portal and phones; the BIA BP-13 workaround applies | Director of Marketing and Communications |
| 5 | **If the vendor's incident exposed Company client data:** the vendor, as a third-party agent, must notify the Company no later than 10 days after its determination (Fla. Stat. 501.171(6)(a)), and the Company then gives the Florida notices. Counsel decides whether the event is an FTC notification event for the Company and when the Company's 30 days begin (an event is discovered when known to the Company or its employees, officers, or other agents, 314.4(j)(2)). The Company makes its own IRS report as an ERO | General Counsel; Director of Tax Operations |
| 6 | **Reconnect only after** written confirmation of containment from the vendor, credential and API key rotation, a clean indicator hunt, and the incident commander's approval | Director of Information Security |
| 7 | Contract follow-up: service credits, the vendor's root-cause report, and deadline-week commitments at renewal | General Counsel |

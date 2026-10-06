# Incident Response Runbook: Compromise of the Payment Processing Environment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed payment processor serving merchants) |
| Tier / Vertical | Mid-Market / Financial Services |
| Incident type | Compromise of the payment processing environment. An attacker phishes an Integrated Payments engineer, uses the engineer's standing administrator role in Cloud B to deploy a memory-scraping implant on the gateway's API containers, captures card data from card-not-present API requests, and exfiltrates it over HTTPS to attacker-controlled cloud storage |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy |
| Companion documents | `ir-runbook-settlement-ransomware.md` (ransomware disrupting settlement and funding); `notification-matrix.csv`; BIA (P05); risk register (P01 R-001 to R-004) |
| Runbook owner | Director of Information Security (incident commander) |
| Approved | 2026-09-15 by the Chief Operating Officer |
| Last tested | Not yet. Executive tabletop on this scenario with outside counsel 2026-11-04 (POAM-017) |

## 0. Governance, roles, and contacts (Govern)
The response runs on three tiers, so that technical, business, and legal decisions each have a clear owner.

| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, CTO, General Counsel, Chief Risk and Compliance Officer, vCISO, Director of Corporate Communications, Director of Sales and Partner Management (ISV relationships), outside breach counsel | Business continuity, whether to suspend the gateway or individual ISVs, external statements, sponsor bank and card brand engagement, ransom or extortion questions (recommendation to the CEO), resources |
| **Incident response team (IRT)** | Incident commander: Director of Information Security. Director of Integrated Payments Engineering (technical lead for Cloud B), VP Platform Engineering (core switch and network), security engineers and analysts, MSSP, forensic firm and PCI Forensic Investigator (through counsel) | Containment, investigation, eradication, recovery sequence |
| **Notices cell** | Chief Risk and Compliance Officer (lead), General Counsel, outside breach counsel, Director of Settlement and Treasury Operations (at-risk account data), Director of Merchant Services | Every notice in section 6 and the decision log |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Director of Information Security | vCISO | Out-of-band group on personal phones; printed call tree |
| Technical lead (Cloud B) | Director of Integrated Payments Engineering | VP Platform Engineering | Out-of-band group |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Legal | General Counsel | Outside breach counsel (insurer panel) | Out-of-band group; insurer hotline |
| Notices and sponsor bank and card brand liaison | Chief Risk and Compliance Officer | General Counsel | Out-of-band group |
| Cyber insurer | Carrier breach hotline ($20 million limit, $500,000 retention) | Broker | Policy card in the incident binder |
| PCI Forensic Investigator (PFI) | Firm from the PCI SSC list on the insurer panel, engaged through counsel | n/a | Engaged on day 1 if Visa or another brand requires it |
| Bank B (FDIC; sponsor for Integrated Payments merchants) | Designated security and compliance contacts (**to be recorded by 2026-10-15, POAM-017**) | CEO and CIO (fallback under 12 CFR 304.24(a)(2)) | Numbers in the incident binder |
| Bank A (OCC) | Designated security and compliance contacts (on file, confirmed 2026-07-01) | CEO and CIO (fallback under 12 CFR 53.4(a)(2)) | Numbers in the incident binder |
| MSSP | 24x7 security operations center | n/a | MSSP hotline |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | U.S. Secret Service field office (financial crimes) or FBI field office | IC3 | Numbers in the binder |

**Out-of-band first.** The attacker held an engineer's identity and Cloud B administrator rights and may read email, chat, and the gateway team's tickets. The CMT and IRT use a pre-provisioned messaging group on personal phones and printed call trees.

**Legal privilege protocol.** Outside counsel engages the forensic firm and the PFI and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts (timeline, logs) separate from legal conclusions. Do not speculate in email or chat. The PFI's report goes to the card brands under their rules; counsel advises on what else is shared.

## 1. Preparation checks (Identify / Protect)
- [x] 24x7 MSSP monitoring and on-call for the core platform and cages (SI-4; DNS test alerted in 4 minutes in P07)
- [x] Core hosted payment page script controls and tamper-detection (PCI DSS 6.4.3, 11.6.1)
- [ ] Cloud B logs in the SIEM with 12-month retention and MSSP use cases. **Gap until POAM-003 closes (2026-11-06)**. Until then, the Cloud B provider's threat detection findings are reviewed daily by the security team
- [ ] Cloud B administrator access through PAM with security keys; no standing roles. **Gap until the POAM-002 milestone of 2026-11-06**
- [ ] Cloud B egress allow list and DNS logging (PCI DSS 1.3.2, 11.5.1.1). **Gap until POAM-003 closes**
- [ ] Hosted payment field script controls and tamper-detection. **Gap until POAM-001 closes (2026-10-30)**
- [ ] Both sponsor banks' designated contacts on file and confirmed this quarter (12 CFR 53.4(a)(1); 304.24(a)(1)). **Bank B missing (POAM-017)**
- [x] Insurer panel counsel, forensic firm, and PFI shortlist confirmed; contact list verified 2026-09-15
- [ ] Break-glass accounts for Cloud B sealed and tested (after federation, POAM-002)
- [ ] ISV security contacts on file for the 420 partners (merchant notice path, Fla. Stat. 501.171(6)(a); G-113)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Common point of purchase (CPP) alert: Bank B, Bank A, or a card brand says fraud traces back to merchants on the Integrated Payments gateway | Sponsor bank; card brand | Declare severity 1 immediately. **This starts the Visa 3-calendar-day clock (reasonable suspicion)** |
| New or changed container image, privileged container, or unexpected process in the gateway API containers | Cloud B threat detection (daily review today); runtime agent; SIEM after POAM-003 | Isolate the workload; declare if not tied to an approved release |
| Administrator sign-in to Cloud B from a new location or device, or a role change outside a change ticket | Cloud B audit logs; identity provider (after federation) | Disable the identity; declare if unexplained |
| Large or unusual outbound HTTPS transfers from gateway subnets to cloud storage endpoints | Cloud B flow logs; egress controls after POAM-003 | Block the destination; declare |
| Several ISVs report customer fraud after checkout, or a researcher reports card data for sale tied to the gateway | Director of Sales and Partner Management; Merchant Services; external | Escalate to the incident commander within 1 hour |
| Phishing report from an Integrated Payments engineer who entered credentials or approved an unexpected MFA prompt | Report button; IT service desk | Reset credentials and revoke sessions; review that identity's Cloud B activity for 30 days |

**Severity 1 (declare immediately):** any confirmed unauthorized code in a CDE component, any CPP alert from a bank or brand, or confirmed card data exfiltration.

**Record three times in the incident log** (POL-03 4.5), because the clocks start from them:
- **Reasonable suspicion or confirmation** of unauthorized access to account data (Visa: 3 calendar days).
- **Discovery:** the first day the event is known to any employee, officer, or agent other than the attacker (FTC: 16 CFR 314.4(j)(2)).
- **Determination of the breach or reason to believe it occurred** (Florida third-party agent notice: 10 days, Fla. Stat. 501.171(6)(a)).

## 3. First 4 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Declare severity 1; open the out-of-band channel; start the incident log and the clock table (section 6.1) | Incident commander | Log open with suspicion and discovery times |
| 0-60 min | Call the cyber insurer hotline before engaging any vendor; insurer assigns counsel; counsel engages the forensic firm and, if a brand requires one, a PFI | Chief Operating Officer | Claim number; counsel on the call |
| 0-60 min | Revoke all sessions and keys for the phished identity and every Cloud B administrator; force re-authentication through the identity provider; freeze Cloud B role changes except by the incident commander | Director of Integrated Payments Engineering | No standing Cloud B session older than the revocation time works |
| 0-2 h | **Preserve before you change:** snapshot the storage and memory of the affected containers, export Cloud B audit, flow, and container logs (they are kept only 30 days today), hash every artifact, and record chain of custody. Do not log in to compromised containers with administrator credentials | Security engineers with the forensic firm | Evidence in counsel-controlled storage |
| 0-2 h | Block the exfiltration destinations and restrict gateway egress to the core switch link and named partner endpoints only | Director of Integrated Payments Engineering | Test connection to the attacker's storage endpoint fails |
| 1-2 h | Redeploy the gateway API from the last known-good signed image on fresh nodes; keep the compromised nodes stopped but preserved | Director of Integrated Payments Engineering | Known-good image hash verified in production |
| 1-2 h | Convene the CMT. Decide whether to keep the gateway running (preferred if the clean redeploy is verified) or suspend it, which stops payments for about 9,000 merchants | CMT chair | Decision and reason in the decision log |
| 2-4 h | Notify Bank B's designated contacts (suspected account data compromise; sponsor agreement: within 24 hours). Inform Bank A as a courtesy because the core switch is connected | Chief Risk and Compliance Officer | Notices sent and acknowledged; times recorded |
| 2-4 h | **12 CFR 53.4 and 304.24 check:** is containment disrupting, or reasonably likely to disrupt, clearing, settlement, reconciliation, or funding files for either bank for 4 or more hours? (section 6.3) | Incident commander with the Chief Risk and Compliance Officer | Decision and reason recorded |
| 2-4 h | CEO informs the audit committee chair and the PE sponsor's operating partner | CEO | Notice given |
| 2-4 h | Staff briefing script: what happened, do not discuss externally, report anything unusual, ISV questions go to partner management | Director of Corporate Communications with HR | Script sent by the out-of-band channel |

**Keep the rest of the business running if it is safe.** In this scenario the core platform, settlement, and funding were not touched. Stopping them would harm 22,000 more merchants and could trigger bank notices. The core switch link from Cloud B is restricted to authorization messages and monitored; it is cut only if forensics shows lateral movement.

## 4. Analysis (RS.AN)
1. **Initial access.** Confirm the phishing message, the time the engineer entered credentials or approved the prompt, and every action taken with the identity and its Cloud B roles (Cloud B audit logs, identity provider logs, the engineer's laptop EDR telemetry).
2. **What changed.** Compare running images and container configurations with the last approved release. Identify the implant, how it was deployed (image change, privileged container, or runtime injection), and every other change made by the same identity or keys.
3. **Window of exposure.** First malicious deployment to containment, set from deployment records, container start times, and flow logs. Visa requires at-risk accounts within 3 calendar days of setting the window of exposure.
4. **What was taken.** The gateway receives PAN, expiry, card verification code, and billing details in API requests. Work out which elements the implant captured, then count affected transactions, cards, merchants, and ISVs inside the window, split by brand, by sponsor bank (all Integrated Payments merchants are Bank B's), and by cardholder state where known.
5. **Exfiltration path.** Confirm the destinations, volumes, and times from flow logs; identify the attacker's storage accounts for law enforcement.
6. **Lateral movement.** Check the core switch, the token vaults, the Cloud B key service, and the private link for access by the attacker's identities or keys. **Key access changes every later decision:** encrypted data counts as unencrypted under 16 CFR 314.2 if the key was accessed, so a compromise of Cloud B key policies (R-051) widens the event to stored PAN in the gateway token vault.
7. **Cloud B log gap.** Cloud B keeps audit logs for 30 days. If the window of exposure is longer, record the gap; the PFI and counsel decide how it affects the scope and counts.

## 5. Containment and eradication (RS.MI)
1. Federate Cloud B to the company identity provider immediately (accelerating POAM-002); remove every IAM user and long-lived key; administrators use PAM with security keys only.
2. Rotate every secret the attacker could read: gateway TLS keys, database credentials (including the 2 that were hard-coded, POAM-006), partner API credentials if exposed, and the Cloud B data-encrypting keys if the key service was touched.
3. Rebuild the gateway, hosted payment fields, and partner portal from clean source after reviewing every change in the window of exposure; enforce a second approver on the Integrated Payments repository before re-enabling deployments (POAM-010).
4. Keep the egress allow list and add DNS logging and the MSSP use cases for Cloud B before declaring eradication complete (POAM-003).
5. Confirm with the PFI or forensic firm that no persistence remains (implants, rogue roles, scheduled tasks, unauthorized images).

## 6. Legal, regulatory, and external communication (RS.CO)
**Follow `notification-matrix.csv`.** The General Counsel or outside counsel confirms every legal notice before it goes out. The Chief Risk and Compliance Officer keeps the **decision log** and the clock table.

### 6.1 Decision log and notice clock table
| Decision point | Question | Decider | Record |
|---|---|---|---|
| D1 | When did reasonable suspicion arise, when was the event discovered, and when was the breach determined? | Incident commander with the General Counsel | Decision log |
| D2 | Which data elements were captured, and were any keys accessed? | Forensic firm or PFI through counsel | Privileged findings summary |
| D3 | How many cardholders, merchants, and ISVs are affected, by brand, by sponsor bank, and by state? | Notices cell | Affected population workbook |
| D4 | Are covered services disrupted, or reasonably likely to be disrupted, for 4 or more hours for either bank? | Incident commander and Chief Risk and Compliance Officer | 53.4 and 304.24 decision record |
| D5 | Is this an FTC notification event, and does it involve 500 or more consumers? | General Counsel | FTC decision record |
| D6 | Has law enforcement asked in writing for a delay? | General Counsel | Copy of the written request |
| D7 | Extortion demand or payment question | CEO on CMT recommendation | See section 6.6 |

| Clock starts | Action | Deadline | Owner |
|---|---|---|---|
| Reasonable suspicion or confirmation | Notify Bank B (sponsor for the affected merchants) and, as a courtesy, Bank A | Immediately (Visa WTDIC A.3); no later than 24 hours (sponsor agreements) | Chief Risk and Compliance Officer |
| Reasonable suspicion or confirmation | Make sure the compromise is reported to Visa's Global Risk Investigations group (through Bank B and Visa's Global Investigations Management Tool, GIMT) | 3 calendar days | Chief Risk and Compliance Officer |
| Notice to Visa | Incident report to Visa and the acquiring bank (Visa's Attachment A template) | 3 calendar days after notifying Visa | Director of Information Security |
| Window of exposure set (or discovery of compromised accounts, or Visa's request) | At-risk account numbers to Visa through GIMT or the Compromised Account Management System | 3 calendar days | Director of Settlement and Treasury Operations with the Director of Information Security |
| Visa requires a PFI | Engage a PFI and meet Visa's PFI rules | As stated in Visa's notice | General Counsel |
| Other card brands | Each brand's incident rules, through the sponsor banks | Per brand rules (confirm with the sponsor banks) | Chief Risk and Compliance Officer |
| Determination that covered services were or will be disrupted 4 or more hours | 12 CFR 53.4 (Bank A) and 304.24 (Bank B) notice to designated contacts | As soon as possible | Chief Risk and Compliance Officer |
| Determination of breach or reason to believe | Notice to affected merchants as their third-party agent (Florida 501.171(6)(a); other states vary), directly or through their ISV | As expeditiously as practicable; Florida outer limit 10 days | Notices cell with counsel |
| Discovery (known to any employee) | FTC notice if the information of 500 or more consumers is involved (16 CFR 314.4(j)) | As soon as possible; no later than 30 days | General Counsel |
| Day 0 to 2 | Voluntary report to the U.S. Secret Service or FBI | As soon as practicable | Director of Information Security through counsel |
| Per ISV agreements | ISV partner notice | Per contract | Director of Sales and Partner Management with counsel |

**Plan to the shortest clock.** Visa's 3 calendar days arrive first. Merchants need the company's notice early, because their own state-law clocks start when they learn of the breach. The FTC's 30 days run from discovery, not from determination, so a slow investigation does not extend them.

### 6.2 Card brands and the PFI
Visa's What To Do If Compromised (v10.0, effective 2026-06-25) applies to processors and gateways. As a third-party processor, the company reports through its acquirer and, where it has access, GIMT. Visa may require a PFI; if so, the investigation must be performed by a PFI under Visa's formal notification. Other brands' rules are followed through the sponsor banks; their specific timing is not restated here.

### 6.3 12 CFR 53.4 and 304.24 decision (bank service provider notice)
- **Trigger:** a computer-security incident that has materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, covered services to a banking organization customer for four or more hours (53.4(a) for Bank A; 304.24(a) for Bank B).
- **Covered services here:** clearing, settlement, reconciliation, and merchant funding files, named in both sponsor agreements as services subject to the Bank Service Company Act (12 U.S.C. 1867(c)).
- **Apply it to this scenario.** Card data theft at the gateway does not by itself disrupt settlement or funding, so the theft alone does not trigger the notice. If the CMT suspends the gateway, settlement of its transactions continues for the transactions already authorized. If containment stops or corrupts clearing or funding files for Bank B's merchants for 4 or more hours, or makes a missed cutoff likely, notify Bank B's designated contact as soon as possible; if none is on file, its CEO and CIO.
- **Record the decision either way.** Each bank uses the company's information to decide whether it has its own notification incident under 12 CFR 53.3 (Bank A) or 304.23 (Bank B), which it must report to its regulator within 36 hours of its own determination.

### 6.4 FTC notice decision (16 CFR 314.4(j))
- **Is it a notification event?** Card data captured in memory before encryption is acquisition of unencrypted customer information without the cardholder's authorization (314.2(m)). Yes.
- **Who counts?** Affected cardholders count toward the 500 under the company's conservative reading (314.1(b)); counsel confirms.
- **Content (314.4(j)(1)(i)-(vi)):** company name and contact; data types; date range; number of consumers affected or potentially affected; a general description; and whether a law enforcement official has given a written determination that public notice would impede a criminal investigation or damage national security. A law enforcement official may request an initial delay of up to 30 days after the FTC notice, extendable by up to 60 days on written request.
- **Deadline:** as soon as possible and no later than 30 days after discovery.

### 6.5 Merchant, ISV, and state-law notices
- For cardholder data the company is its merchants' **third-party agent**. It must give each affected merchant the information it needs for its own notices, no later than 10 days after determination under Fla. Stat. 501.171(6)(a), and within whatever each other state requires. Many Integrated Payments merchants are reachable only through their ISV (31 of 50 sampled had no direct contact; G-113), so the ISV relay must be started on day 1.
- Under Florida law, a card number is personal information only together with the person's name and any required security code or password (501.171(1)(g)). An implant that captures name, PAN, and card verification code meets that definition.
- Where the company owns the data (for example merchant owner data in onboarding), it is the covered entity and gives the individual notice (no later than 30 days after determination), the Department of Legal Affairs notice (500 or more Floridians, within 30 days), and the consumer reporting agency notice (more than 1,000 individuals at one time) directly.

### 6.6 Extortion and ransom
If the attacker demands payment not to publish card data, the decision follows POL-03 4.11: the CEO decides after consulting the audit committee chair, the General Counsel, and the insurer; an **OFAC sanctions check** on the actor and any wallet is required, and a report to law enforcement is made. Paying does not remove any notice duty. The default position is not to pay.

### 6.7 Communications
- **ISV partners:** a call from the Director of Sales and Partner Management to the top 20 partners, then a counsel-approved notice and integration guidance to all 420.
- **Merchants:** counsel-approved notice and support script, after Bank B is informed.
- **Sponsor banks:** daily status calls with Bank B (and Bank A while the core link is under review).
- **Media:** holding statement approved by counsel; no technical details or attribution.
- **Staff:** out-of-band briefings only.

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05), validating each step before the next: forensics sign-off for the segment, credentials rotated, monitoring in place.

| Order | Resource | Target (BIA RTO) | Validation |
|---|---|---|---|
| 1 | Identity provider and PAM; Cloud B federated, break-glass sealed | 1 h | No Cloud B IAM users or long-lived keys remain |
| 2 | Core switch link from Cloud B (restricted to authorization messages) | 1 h | Flow logs show only expected traffic |
| 3 | Gateway API and hosted payment fields from known-good images (BP-03) | 1 h | Image hashes match the release; tamper-detection baseline taken |
| 4 | Cloud B logs in the SIEM; MSSP use cases; egress allow list (BP-15) | 4 h | Test DNS query and test outbound transfer both alert |
| 5 | Partner portal with MFA enforced for administrators and refund and funding roles (BP-12) | 8 h | Sign-in tests |
| 6 | Settlement of affected transactions confirmed with Bank B (BP-05, BP-06) | Next cutoff | Reconciliation clean |

**Validate before closing:** the PFI or forensic firm confirms eradication; tamper-detection and runtime monitoring have run clean for 7 days; no deployment happened outside the approved pipeline. Tell ISVs and merchants when the gateway is confirmed clean (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery (POL-03 requires documentation within 30 days).
- Update the risk register (P01: R-001 to R-004, R-011, R-051), the POA&M (P07), POL-02 and POL-03 if needed, and this runbook.
- Give the QSA the incident report, the PFI report (if any), and the remediation evidence. A compromise may require an out-of-cycle assessment at a brand's or sponsor bank's request.
- Include the incident and management's response in the next Qualified Individual report to the board (16 CFR 314.4(i)).
- Retain all incident documentation for at least 3 years (POL-01 4.15), or longer if counsel or a brand requires.

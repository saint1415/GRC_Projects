# Incident Response Runbook: Compromise of Provider Tooling Affecting Downstream Customers (Cross-Division)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Tier / Vertical | Multi-Sector / Information Technology |
| Incident type | A stolen Managed IT engineer session is used through two provider tools at once: the HCP run-command service (partner-operator path) and the RMM. It reaches managed-hosting tenants, Managed IT clients, Payment Processing connected-to servers, and the CUI enclave (P01 GR-01, GR-02) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | Group POL-03 Incident Response Policy; division supplements (P06) |
| Runbook owner | Group CISO; notifications owned by the Group General Counsel |
| Approved | 2026-09-17 by the Group CISO and the Group General Counsel |
| Last tested | Technical playbooks tested quarterly. **The multi-regulator notification matrix has not been exercised** (scenario gap 7); the first cross-division tabletop, using this scenario, is on 2026-12-09 (POAM-004) |

## 0. Scenario used to build and test this runbook
An exercise scenario, not a real event. Counts are illustrative.
- **Entry (Day 0, 00:40):** an attacker sends a Managed IT engineer an adversary-in-the-middle phishing page that copies the legacy identity tenant's session token after the engineer approves a push MFA prompt. The token is valid for 12 hours, is not bound to a device, and works for both the HCP partner-operator path and the RMM console (scenario gaps 1 and 8).
- **HCP (01:05 to 02:30):** the attacker uses run-command to install a remote access tool and a credential harvester on about 600 virtual machines in 140 managed-hosting tenants, including 9 bank customers and 6 health care customers under BAAs.
- **RMM (02:10 to 03:30):** the attacker submits a multi-client job labeled "emergency patch." One on-call technician approves it (scenario gap 2). It runs on about 2,300 client servers across 64 Managed IT clients (11 bank clients, 7 health care clients, 5 DIB clients, two of whose CUI enclaves the division manages), on 140 Payment Processing settlement-support servers in the CDE connected-to segment, and on 4 management servers of the SYS-M2 CUI enclave.
- **Detection:** at 01:20 an EDR alert from a managed-hosting VM ("remote administration tool installed") is auto-closed by the AI triage service as an approved admin tool (scenario gap 4). At 03:25 EDR blocks credential dumping on settlement-support servers and a SOC analyst escalates. Severity 1 is declared at **03:40**.
- **Forensic estimate at Day 3:** credentials harvested from about 400 servers; data exfiltrated from 3 managed-hosting tenants (including a regional bank's document server and a clinic group's file server) and from one DIB client's file server inside its CUI enclave; an attempt to move from a settlement-support server into the CDE was blocked by segmentation; no account data accessed; G1 not touched (the partner-operator path does not exist in G1, and no RMM agents run there).

## 1. Roles and contacts (Govern)
| Role | Primary | Backup | Channel |
|---|---|---|---|
| Incident commander | Group SOC director | Group CISO | Out-of-band bridge (group crisis line; secure messaging on managed mobile devices) |
| Executive lead | Group CISO | Group Chief Risk Officer | Out-of-band bridge |
| Technical response | Group SOC; HCP site reliability; RMM administration | Forensic firm on retainer (through the insurer's panel) | SOC bridge |
| Notifications and legal | Group General Counsel with outside breach counsel | Division general counsels | Out-of-band bridge |
| Cloud Hosting notices (customers, banks, BAAs, FedRAMP evaluation) | Cloud Hosting customer success director; Government Cloud compliance director (federal incident response coordinator) | Cloud Hosting division CISO | Division bridge |
| Managed IT notices (clients, banks, BAAs, DIB clients, DIBNet, primes) | Managed IT client services director; Managed IT federal contracts compliance officer | Managed IT division security and compliance lead | Division bridge |
| Payment Processing notices (sponsor banks, card networks, FTC, licensing) | Payment Processing chief compliance officer | Payment Processing division CISO (Qualified Individual) | Division bridge |
| SEC materiality | Disclosure committee | Group chief financial officer | Committee call |
| Communications | Group communications lead | Division communications leads | Out-of-band bridge |
| Law enforcement | FBI field office or IC3; CISA | n/a | Contacts in the offline incident binder |

**Out-of-band first.** Assume the attacker can read email and chat for any identity federated from the legacy tenant. Use the crisis line and managed mobile devices. The printed binder in each division command center holds contacts, this runbook, the notification matrix, and the bank-designated contact registers.

## 2. Preparation checks (Identify / Protect)
- [x] EDR on all group-managed workloads, including the CDE connected-to segment (SI-3; this is what stopped the CDE pivot)
- [x] Immutable backups at external provider X with a separate backup identity (CP-9; P07 satisfied)
- [x] HSM-backed signing of HCP releases and guest-agent packages (SI-7; P07 satisfied)
- [ ] Partner-operator access through SYS-G1 PAM with hardware keys and per-client scope (**gap until POAM-001 closes, 2026-12-31**)
- [ ] Two-person approval for multi-client RMM jobs; no RMM agents in the CDE connected-to segment or the enclave (**gap until POAM-013 and POAM-014 close**)
- [ ] Run-command volume alert and RMM logs in the SIEM (**gap until POAM-002 and POAM-015 close**)
- [ ] AI triage auto-close validated; containment in G1 and the CDE needs analyst approval (**approval gate live 2026-10-15; validation gap until POAM-003 closes**)
- [ ] Notification matrix complete and exercised; bank-designated contacts for every bank (**gap until POAM-004 closes**)
- [x] Emergency stop procedure for RMM, run-command, partner-operator access, and fleet automation (POL-03 4.12)
- [x] Forensic retainer and insurer panel confirmed; two DIBNet medium assurance certificate holders in Cloud Hosting (Managed IT has one: POAM-004)
- [x] Disclosure committee charter includes cybersecurity materiality

## 3. Detection and declaration (Detect; RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Run-command executed in many tenants by one identity, or by a partner operator outside their client team | HCP audit logs (alert once POAM-002 closes) | Disable the identity; start triage |
| Multi-client RMM job outside a change window, or labeled "emergency" | RMM job history (in the SIEM once POAM-015 closes) | Suspend RMM jobs; call the approver |
| Remote access tool or credential dumping on servers of more than one customer or client | EDR; customer and client reports | Declare Severity 1 |
| Any EDR alert on a CDE connected-to server or an enclave server | EDR; SOC | Analyst review required (no auto-close) |
| A customer, client, bank, or agency reports activity it believes came from the group's tooling | Support desks; account teams | Treat as a potential Severity 1 |

**Severity 1** (group scale, POL-03 4.2): confirmed misuse of provider tooling across customers or divisions, or any activity in G1, the CDE, or the CUI enclave.

**Record discovery and determinations for each notifying entity (POL-03 4.3).** The AI triage service auto-closed the first alert at 01:20. No person saw it, but by reasonable diligence it would have been known. **This runbook conservatively treats 01:20 on Day 0 as the discovery time** for every clock keyed to discovery (DFARS 72 hours, HIPAA business associate notices). Counsel may refine this, but no clock is planned from 03:40. Determinations (the bank 4-hour determination, breach determinations, the sponsor bank determination, materiality) are recorded separately as they are made.

## 4. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. **Emergency stop** (POL-03 4.12): suspend all RMM jobs and technician sessions; disable the partner-operator path in the HCP; pause fleet automation releases | Incident commander, through RMM administration and HCP site reliability | RMM job queue empty; partner-operator federation disabled |
| 2. Revoke every token issued by the Managed IT legacy tenant; disable the compromised identity and the approving technician's account pending interview | Group identity director | Sessions revoked |
| 3. Isolate the 140 settlement-support servers and the 4 enclave management servers (analyst-approved containment) | SOC with Payment Processing and enclave owners | Network isolation confirmed |
| 4. Preserve evidence: export HCP run-command logs, RMM job history and audit logs (90-day vendor retention), EDR telemetry; snapshot enclave servers for the DFARS 90-day preservation | SOC; forensic firm; federal contracts compliance officer | Evidence list signed |
| 5. **FedRAMP reportability evaluation** for G1 (IEC-CSO-EFR) within the first hour: did the attacker's identity, tools, or the shared SOC tooling reach G1 or its federal customer data? | Government Cloud compliance director | Evaluation recorded |
| 6. Call the cyber insurer; engage breach counsel and forensics through the panel | Group Chief Risk Officer | Claim number issued |
| 7. Notify the three division notice owners **on the bridge** | Incident commander | Each acknowledges |
| 8. Brief the Group CISO; escalate to the disclosure committee within 24 hours (POL-03 4.6) | Group CISO | Committee convened |
| 9. Tell division operations what is stopped: managed services automation and managed hosting operations are paused; hosting, G1, and card authorization are not affected | Division liaisons | Status pages updated |

**The incident commander may take steps 1 to 3 without further approval.** Pausing the RMM for 2,900 clients and the partner-operator path for 4,100 tenants is acceptable: BP-M01 and BP-M02 have 24-hour MTDs (P05), and restoring a compromised tool fast would spread harm.

## 5. Analysis (RS.AN)
1. **Initial access.** Confirm the phished engineer, the token theft, and the approver's decision. Check whether other legacy-tenant identities show the same pattern.
2. **Blast radius by division.** From HCP and RMM logs, list every tenant, client, and server the attacker touched. Map each to its notifying entity and to the obligations in `notification-matrix.csv`.
3. **G1 (FedRAMP).** In this scenario the evaluation finds no G1 effect: the partner-operator path and RMM agents are absent from G1, and the SOC tooling that sees G1 logs was not altered. Record the evaluation and its time; **no FedRAMP report is due.** If any G1 effect is found later, the incident becomes a FedRAMP Reportable Incident from that evaluation, rated by PAIN (N1 minimal effect on one or more agencies; N2 narrow; N3 disruptive on one agency; N4 debilitating on one agency or disruptive on more than one; N5 debilitating on more than one) or treated as PAIN-5, and the Class C Initial Incident Report is due within 1 hour for PAIN-3 to PAIN-5.
4. **CUI enclave (DFARS).** The script ran on 4 enclave management servers, which are part of a covered contractor information system. Review for compromise of covered defense information as paragraph (c)(1)(i) requires. The DIBNet report is due within 72 hours of discovery whatever the review finds.
5. **DIB clients.** Two client CUI enclaves the division manages were touched, and one client's file server lost data. Each client must make its own DFARS report within 72 hours of its discovery, so the division gives them facts within 24 hours (ESP terms; internal target).
6. **Banks.** For each bank customer (Cloud Hosting) and bank client (Managed IT), decide whether the incident or the emergency stop has materially disrupted or degraded covered services, or is reasonably likely to, for four or more hours. Record each determination and its time.
7. **Payment Processing.** Confirm with forensics that no account data was accessed and that the CDE pivot failed. Decide whether a suspected account data compromise exists (card network reporting through the sponsor bank) and whether customer information of 500 or more consumers was acquired (FTC). Settlement-support servers hold merchant and biller settlement files; record what they contained.
8. **Personal information and PHI.** For exfiltrated tenants and clients, determine whether personal information or PHI was involved. The covered entities (bank, clinic group, and others) make their own breach determinations and notices; the group's duty is to notify them as a business associate or third-party agent with the facts they need.
9. **Root cause:** the legacy tenant's push MFA and 12-hour tokens, standing partner-operator scope, one-approver RMM jobs, RMM reach into other divisions, and an auto-closed first alert. Feed these to P01 GR-01, GR-02, and GR-04.

## 6. Containment and eradication (RS.MI)
1. Keep the RMM and the partner-operator path stopped until eradication is confirmed. Bring partner-operator access back only through SYS-G1 PAM with hardware keys and per-client scope (accelerates POAM-001).
2. Remove the remote access tool and harvester from every touched server using forensic indicators; the customer or client approves every action on its systems.
3. Rotate every credential harvested from touched servers, starting with the CDE connected-to segment, the enclave, and bank and health care tenants.
4. **Remove RMM agents from the settlement-support servers and the enclave management servers permanently** before they are reconnected (accelerates POAM-014).
5. Review the RMM script library and HCP run-command templates for tampering; restore from version control.
6. Confirm with forensics that no persistence remains in SYS-G1, the legacy tenant, the HCP, or the RMM tenant before recovery.

## 7. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv` (36 rows).** Counsel reviews every notice, but no review may delay a regulatory clock (POL-03 4.5). The matrix has three layers:
1. **Inside the group:** affiliate notices between divisions (Managed IT to Payment Processing and to Cloud Hosting), which the intercompany agreements will formalize (POAM-018).
2. **Each division's own regulated duties:** DIBNet and the primes (Managed IT); bank notices (all three divisions); BAA notices (Cloud Hosting and Managed IT); sponsor banks, card networks, and the FTC if triggered (Payment Processing); the FedRAMP evaluation (Cloud Hosting).
3. **Outward duties:** customer and client contract notices, Florida third-party agent notices and their equivalents in other states, and the group's SEC materiality decision.

| When (Day 0 starts at the 01:20 discovery) | Action | Owner |
|---|---|---|
| Hour 0 to 1 after declaration | FedRAMP reportability evaluation recorded (no G1 effect); insurer, counsel, and forensics engaged; division notice owners on the bridge | Government Cloud compliance director; Group Chief Risk Officer |
| As soon as possible after each 4-hour determination (expected about 08:00 on Day 0 for managed-service bank clients) | Bank notices to designated contacts, or CEO and CIO where none was given (12 CFR 53.4(a)). Phone first, then email. Banks must notify their regulator within 36 hours of their own determination, so give facts early | Cloud Hosting customer success director; Managed IT client services director; Payment Processing chief compliance officer |
| Day 0 to 1 | Voluntary report to FBI or IC3 and CISA | Group CISO |
| Within 24 hours of declaration | Disclosure committee convened; materiality assessment starts | Group General Counsel |
| Within 24 hours of the sponsor bank determination | Sponsor banks A and B | Payment Processing chief compliance officer |
| Within 24 hours of discovery (internal target) | DIB clients whose systems were touched | Managed IT federal contracts compliance officer |
| Within 48 hours of confirmation | Managed IT client notices (64 clients) | Managed IT client services director |
| Within 72 hours of discovery (by 01:20 on Day 3) | **DIBNet report** for the enclave; then the DoD report number to each affected prime as soon as practicable; malware to DC3; images held 90 days | Managed IT federal contracts compliance officer |
| Within 72 hours of confirmation | Cloud Hosting customer notices (140 tenants) | Cloud Hosting customer success director |
| Within 4 business days of a materiality determination | Form 8-K Item 1.05, if material | Disclosure committee; Group General Counsel |
| Within 10 calendar days of discovery (standard BAA) and never later than 60 days | HIPAA business associate notices to affected covered entity customers and clients (164.410), with the facts they need for their own four-factor assessments | Cloud Hosting and Managed IT notice owners |
| Within 10 days of each breach determination | Florida third-party agent notices to affected customers and clients (Fla. Stat. 501.171(6)(a)); apply each other state's service-provider rule the same way | Cloud Hosting and Managed IT notice owners with counsel |
| Within 30 days of discovery, if triggered | FTC notice for an event involving 500 or more consumers (16 CFR 314.4(j)) | Payment Processing Qualified Individual |
| As the network rules require, if account data compromise is suspected | Card network reporting through sponsor bank A | Payment Processing chief compliance officer |

**Plan to the shortest clock.** In this scenario the order is: the FedRAMP evaluation (minutes), bank notices (as soon as possible after hour 4), sponsor banks and DIB clients (24 hours), Managed IT clients (48 hours), DIBNet and Cloud Hosting customers (72 hours), SEC (4 business days after determination), BAAs and Florida third-party agent notices (10 days), and the outer limits (FTC 30 days if triggered, HIPAA 60 days).

**Materiality factors for the disclosure committee:**
- the number of customers, clients, banks, and DIB contractors affected across two divisions;
- regulatory exposure: bank regulators through the banks, DoD through DIBNet and the primes, the FTC, state attorneys general, and card networks;
- whether the G1 certification or the PCI DSS compliance status is affected;
- customer churn in managed hosting and managed services;
- the cost of response, notices, and service credits;
- the operational effect of pausing the RMM and managed hosting operations.

Materiality is decided without unreasonable delay. The 4-business-day clock starts at the determination, not at discovery.

**Ransom decision:** board risk committee, counsel, insurer, and an OFAC sanctions check (POL-03 4.7). Paying does not remove any notice duty when data was taken.

## 8. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05). In this incident the hosting platform, G1, and card authorization keep running, so recovery focuses on the tools and the touched systems:
1. **Identity:** SYS-G1 confirmed clean (BP-G01); all legacy-tenant identities re-enrolled or moved to SYS-G1 with hardware keys before any tool reopens.
2. **The CDE connected-to segment** (supports BP-P02, priority 10): rebuilt or cleaned, without RMM agents, credentials rotated, before the next settlement window.
3. **SOC visibility** (BP-G02): RMM logs and the run-command volume alert in the SIEM; AI triage containment and auto-close limits in place for affected sources.
4. **Managed operations** (BP-M01, priority 12; RTO 8 hours **after integrity validation**): reopen client by client only after two-person approval, per-client script scopes, a verified script library, forensic sign-off, and client agreement.
5. **Customer and client communications** (BP-H06, BP-M03): status updates every business day until closure.
6. **Managed hosting operations** (BP-M02, priority 18): reopen the partner-operator path only on the PAM design.
7. **DoD subcontract work** (BP-M04, priority 21): resume CUI work after the enclave is validated clean and the primes are informed.

Tell each customer, client, and bank when services resume (RC.CO).

## 9. Post-incident (ID.IM)
- Lessons learned within 14 days of recovery; documented within 30 days (POL-03 4.10).
- Update P01 (GR-01, GR-02, GR-03, GR-04, CH-001, MS-001, PY-001), the POA&M (POAM-001 to POAM-004, POAM-013 to POAM-015), the notification matrix, and this runbook.
- Re-test the AI triage service on the alert it closed at 01:20 (P10).
- Review the RMM vendor's role and contract terms (P01 MS-014).
- Consider the Reg S-K Item 106 description for the next annual report.
- Retain all incident records for at least 6 years (POL-01 4.12), and longer if litigation is expected.

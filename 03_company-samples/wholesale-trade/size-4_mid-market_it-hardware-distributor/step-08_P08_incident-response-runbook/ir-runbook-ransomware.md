# Incident Response Runbook: Ransomware Halting Distribution Operations

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed IT hardware and software wholesale distributor) |
| Tier / Vertical | Mid-Market / Wholesale Trade |
| Incident type | Ransomware (with possible data theft for extortion) that encrypts the WMS, integration services, file services, endpoints, or DC automation, stopping DC-1 and DC-2, with possible exposure of FCI, employee personal information, or CUI |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), organized by CSF Functions |
| Policy basis | POL-03 Incident Response Policy; STD-07 Contingency and recovery standard |
| Companion documents | `ir-runbook.md` (supplier compromise); `notification-matrix.csv`; BIA (P05); IT contingency plan |
| Runbook owner | Security Manager (incident commander) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | 2025-03 tabletop under the 2024 plan. Executive tabletop with outside counsel scheduled 2027-02-17 (POAM-015) |

## 0. Governance, roles, and contacts (Govern)
| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Operating Officer. CEO, CFO, General Counsel, vCISO, Director of Information Technology, Director of Distribution Operations, Vice President of Sales Operations, Director of Federal Programs, Director of Marketing and Communications, HR Director, breach counsel | Business continuity (manual mode, drop-ship), customer and prime statements, ransom decision (recommendation to the CEO), resources |
| **Incident response team (IRT)** | Incident commander: Security Manager. Director of Information Technology (recovery lead), security analysts, MSSP, forensic firm (through counsel), cloud and SaaS vendor contacts, DC automation integrator | Containment, investigation, eradication, recovery sequence |
| **Operations command** | Director of Distribution Operations, DC-1 and DC-2 General Managers, Customer Service Director, Federal Integration Lab Manager | Manual pick mode, carrier portals, worker safety on manual conveyor lanes, FIL pause |

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Security Manager | Director of Information Technology | Out-of-band group on personal phones; printed call tree |
| CMT chair | Chief Operating Officer | Chief Executive Officer | Out-of-band group |
| Legal and breach decisions | General Counsel with breach counsel (insurer panel) | Outside general counsel | Out-of-band group; insurer hotline |
| Cyber insurer | Carrier breach hotline ($15M limit, $500K retention) | Broker | Policy card in the binder |
| Forensics | Panel forensic firm, engaged by counsel | MSSP incident response team | Through counsel |
| Monitoring and first response | MSSP 24x7 operations center | n/a | MSSP hotline |
| DoD and prime reporting | Director of Federal Programs | Contracts Compliance Manager | Out-of-band group |
| Board and PE sponsor | CEO informs the audit committee chair and the sponsor's operating partner | COO | Phone |
| Law enforcement | FBI field office / IC3 | CISA | Numbers in the binder |

**Out-of-band first.** Assume email, chat, and VoIP are compromised. Use the messaging group on personal phones and the printed call trees at every site.

**Legal privilege protocol.** Breach counsel engages the forensic firm and directs the investigation. Label analysis "Privileged and confidential, prepared at the direction of counsel". Keep facts separate from legal conclusions.

## 1. Preparation checks (Identify / Protect)
- [x] Write-once backups in the separate backup account (CP-9; P07 satisfied except DC automation configurations)
- [x] EDR on all endpoints with 24x7 MSSP (SI-3; P07 fully satisfied)
- [x] WMS standby replica every 15 minutes
- [ ] WMS rebuild within the 8-hour RTO demonstrated. **Gap until POAM-011 closes**
- [ ] DC automation segmented and integrator access through a gateway. **Gap until POAM-004 and POAM-005 close**
- [ ] DC automation controller configurations backed up. **Gap until POAM-012 closes**
- [x] Break-glass accounts for the IdP, cloud, and backup account sealed offline
- [x] Clean laptop with the DIBNet certificate kept offline at HQ
- [x] Pre-printed manual pick procedure and carrier portal account list at DC-1
- [ ] Carrier portal accounts at DC-2. **Due 2026-12-31 (R-016)**

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Ransom note, or mass file renaming or encryption | EDR alert; staff report | MSSP isolates the host and calls the incident commander within 30 minutes |
| Attempts to delete backups or disable EDR or logging | Cloud audit logs; EDR tamper alert | Treat as a ransomware precursor; declare |
| New administrator accounts or broker elevation outside hours | SIEM; access broker | Disable the account; declare if unexplained |
| Sortation or WMS stops with unexplained errors | DC-1 operations; integrator | IT triage; declare if malicious |
| Large outbound transfer from file services or the data warehouse | Cloud firewall (egress alerting due 2027-01-31) | Block the destination; declare |
| Extortion email or leak-site post naming the company | Email; threat intelligence; FBI | Declare; preserve the message |

**Declare a ransomware incident** on any confirmed encryption or confirmed precursor. The incident commander declares; the CMT chair convenes the CMT within 1 hour.

## 3. First four hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Isolate affected hosts through EDR; block attacker infrastructure at the cloud firewall and site firewalls | MSSP; Security Manager | Spread stopped |
| 2. Disconnect the OT VLAN from corporate networks at the DC-1 core switch; integrator remote tool disabled | Director of Information Technology; integrator | OT isolated |
| 3. Protect backups: confirm the backup account and enclave vault are untouched; suspend the cross-account backup role | Director of Information Technology | Backup integrity confirmed |
| 4. Call the insurer's hotline; General Counsel engages breach counsel; counsel engages forensics | Chief Operating Officer; General Counsel | Claim number; counsel engaged |
| 5. Switch DC-1 to manual pick mode; DC-2 pauses; federal and next-day orders first; carrier portals for labels | Director of Distribution Operations | Manual operation running safely |
| 6. Decide whether the enclave or FIL is affected: check enclave sign-ins, VDI sessions from affected laptops, and FIL network logs | Security Manager; Federal Integration Lab Manager | Decision recorded with time |
| 7. Reset privileged credentials from clean devices; revoke sessions in the IdP and enclave | Director of Information Technology | Credentials rotated |
| 8. Start the incident log and the reporting clock sheet | Incident commander; Director of Federal Programs | Log open |

## 4. Analysis (RS.AN)
1. **Scope:** affected hosts, accounts, cloud accounts, OT components, and the initial access path.
2. **Data:** was data taken, and what kind (FCI, employee personal information, reseller pricing, CUI)? Use cloud flow logs, EDR telemetry, and forensic review.
3. **Enclave and CUI:** the enclave uses separate identity and networks. If any enclave system, FIL device, or CUI location was affected, the DIBNet clock runs from discovery.
4. **Preserve evidence:** image affected systems and keep monitoring data for at least 90 days after any DIBNet report (DFARS 252.204-7012(e)).

## 5. Containment, eradication, and the ransom decision (RS.MI)
- Rebuild affected servers from known-good images; never decrypt in place on production.
- Remove persistence: scheduled tasks, new accounts, remote tools, and malicious mailbox rules.
- **Ransom decision.** The company's position is not to pay. Any exception needs an OFAC sanctions check, counsel's advice, law enforcement contact, and the CEO's approval (POL-03 4.9). The CMT documents the decision.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.**

| What was found | Clock | Owner |
|---|---|---|
| Enclave, FIL, or any system holding CUI affected | DIBNet report within 72 hours of discovery; incident number to the prime; preserve images 90 days; malware to DC3 if instructed | Director of Federal Programs; Security Manager |
| FCI systems affected (ERP, WMS, email) but no CUI | No DFARS report; notify primes under their contract terms; check FAR clause duties with counsel | Director of Federal Programs; General Counsel |
| Employee or reseller-contact personal information taken | Each state's law; Florida example: individuals within 30 days of determination, the Department of Legal Affairs within 30 days if 500 or more, consumer reporting agencies if more than 1,000 | General Counsel |
| Partner Commerce Platform or reseller data affected | Reseller contract notice within 72 hours of confirmation | Vice President of Sales Operations |
| Extortion demand received | OFAC check before any payment; report to the FBI | General Counsel |
| Always | Insurer hotline before vendors | Chief Financial Officer |

**Not applicable:** SEC Form 8-K Item 1.05 (private company); CIRCIA (final rule not in effect as of 2026-09-25).

**Stakeholders.** Resellers get a status page message within 4 hours and updates twice a day; primes are called by the Director of Federal Programs; employees get scripted updates from HR; the CEO briefs the audit committee chair and the sponsor.

## 7. Recovery (RC.RP, RC.CO)
Recover in BIA priority order (P05 section 7), after forensics confirms the environment is clean:
1. Identity provider and break-glass accounts; clean administrator workstations.
2. DIBNet path (clean laptop) and out-of-band communications.
3. SD-WAN and DC-1 network.
4. WMS: promote the standby if clean, or rebuild from the backup account (target 8 hours; 14 hours in the 2025-09 test).
5. TMS and carrier label printing; ERP and portal sync replay of queued orders.
6. DC automation from integrator configurations (manual lanes until validated).
7. EDI, integration services, and file services.
8. FIL and enclave work resumes only after the Federal Integration Lab Manager and Security Manager confirm the enclave was not affected or is clean.
9. Forecasting auto-release (AI-001) stays off until data integrity is validated.

Validate each restored system with the MSSP before reconnecting it (CP-10).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; report within 30 days (POL-03 4.11).
- Update the risk register (R-001, R-002, R-005, R-013), the POA&M, the BIA, and this runbook.
- Retain records for 6 years.

# Incident Response Runbook: Extended Platform Outage (Regional Failure or Destructive Attack)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed B2B SaaS publisher of a multi-tenant customer service platform) |
| Tier / Vertical | Mid-Market / Information |
| Incident type | Extended outage of the Customer Engagement Platform: primarily **loss of the primary cloud region**; variant for a **destructive attack** in which an attacker with administrator access deletes production databases and backups |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); NIST SP 800-34 Rev. 1 for recovery |
| Policy basis | POL-03 Incident Response Policy (4.1, 4.4, 4.6); STD-07 Contingency and recovery standard |
| Companion documents | `ir-runbook.md` (credential compromise); `notification-matrix.csv`; BIA (P05 BP-01 to BP-05, BP-15); risk register (P01 R-006, R-007, R-042) |
| Runbook owner | VP Platform Engineering (incident commander for outages) with the Director of Security (security lead) |
| Approved | 2026-09-29 by the Chief Technology Officer |
| Last tested | Regional failover test 2026-02 (9 hours against a 4-hour objective). Next: failover exercise and outage tabletop 2027-02-17 (POAM-010, POAM-014) |

## 0. Why this runbook exists
About 2,400 customers run their support operations on the platform. An outage is visible to them and to their own customers within minutes. Service credits reach about $583,000 after 1 hour and the $2.08 million monthly cap after 7.2 hours (P05). At 4 hours the 9 bank customers must be notified (12 CFR 53.4), and the healthcare cell's availability safeguards under the BAAs are in question. Today the company has proven only a 9-hour regional recovery, so this runbook also covers how to communicate while recovery is slower than the targets.

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Incident commander (outage) | VP Platform Engineering | Senior site reliability engineer on call | Declares severity; decides failover; runs the recovery sequence |
| Security lead | Director of Security | Security engineer on call | Decides whether the cause is malicious; runs the destructive attack variant; protects evidence |
| CMT chair | Chief Technology Officer | Chief Executive Officer | Severity 1 decisions, spending, external statements |
| Customer communications | VP Customer Support | Chief Revenue Officer | Status page, customer updates, top-account calls |
| Bank and covered entity notices | Associate General Counsel, Privacy | General Counsel | 4-hour bank notices; BAA notices if ePHI availability is affected |
| Finance | Chief Financial Officer | Controller | Credit exposure, insurer notice (business interruption), cash forecast |
| Cloud provider liaison | Platform engineering lead on call | VP Platform Engineering | Provider support case at the highest severity; provider status |
| Legal | General Counsel | Outside counsel | Contract rights, termination risk, statements |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Synthetic checks fail for the agent workspace, API, or ingestion in more than one zone | Uptime monitoring; status alerts | On-call opens an outage incident within 5 minutes |
| Cloud provider reports a regional service event | Provider health dashboard | Incident commander assesses failover |
| Databases, snapshots, or backups deleted; administrator activity outside change windows | Cloud audit logs; guardrail alerts; backup job failures | **Treat as a destructive attack** (section 7); security lead takes joint command |
| Customers report the platform unavailable | Support; social media | Confirm with monitoring; open incident |

**Severity levels:**
- **Severity 3:** one feature or channel degraded, under 30 minutes. On-call manages.
- **Severity 2:** a core process (BP-01 to BP-04) down or degraded for more than 15 minutes, or the healthcare cell affected. Incident commander engaged; VP Customer Support informed.
- **Severity 1:** a core process down for more than 30 minutes or expected to exceed 1 hour, any regional failure, or any destructive attack. Convene the CMT within 1 hour (POL-03 4.4).

**Record the start time of the disruption.** The 4-hour bank clock, the SLA calculation, and the 24-hour Enterprise status commitment all run from it.

## 3. First 4 hours (RS.MA, RC.RP)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-15 min | Post on the status page (hosted by a separate provider); open the cloud provider support case | Incident commander; VP Customer Support | Status posted |
| 0-30 min | Decide: in-region repair or regional failover. **Default: start failover preparation at 30 minutes** if the provider has not given a restoration time, because credits step up at 43 minutes and recovery takes hours | Incident commander | Decision logged |
| 0-60 min | Security lead confirms whether the cause could be malicious (audit log check for deletions, new administrators, key use). If yes, switch to section 7 | Security lead | Cause recorded |
| 30-60 min | Start the DR sequence (section 5): promote database replicas, deploy services from signed images, start search index rebuild with recent tickets first | Platform engineering | Sequence running |
| 1 h | Convene the CMT; first situation report (scope, expected recovery time, customer impact, clocks) | CMT chair | CMT meeting held |
| 1-2 h | Customer update by email to security and administrator contacts; top 50 accounts called by customer success | VP Customer Support | Updates sent |
| 3 h | **Bank decision point.** If recovery for any bank customer is not certain within the next hour, prepare the 12 CFR 53.4 notices now | Associate General Counsel, Privacy | Notices drafted |
| 4 h | **Notify each affected bank's designated point of contact** "as soon as possible" once the company determines the disruption has lasted or is reasonably likely to last 4 or more hours. If a bank has not named a contact, notify its CEO and CIO or two people of comparable responsibility | Associate General Counsel, Privacy | 9 notices sent and logged |
| 4 h | Healthcare cell: if still down, the Associate General Counsel, Privacy calls each of the 46 covered entities and records the call; counsel decides whether any BAA reporting duty is triggered | Associate General Counsel, Privacy | Calls logged |

**Scheduled maintenance is not a notification incident.** The bank rule does not apply to scheduled maintenance, testing, or software updates previously communicated to the bank customer (12 CFR 53.4(b)).

## 4. Business continuity while recovering (RC.RP)
| Process (P05) | Customer-side workaround | Company action |
|---|---|---|
| BP-01 agent workspace | Customers use shared inboxes and phone | Status page every 30 minutes; template for customers to post on their own sites |
| BP-02 chat | Chat widget shows the offline form (if ingestion is up) or customers hide the widget | Instructions in the status update |
| BP-03 ingestion | Senders' mail servers queue and retry | Monitor backlog after recovery; process oldest first |
| BP-04 API | Customer systems queue and retry | Webhook replay in order after recovery, with idempotency keys (R-047) |
| BP-05 healthcare cell | Clinics use phone lines and their own patient portals | Direct calls to the 46 customers |
| BP-11 company support | Backup support mailbox at the email delivery service | Support works from the backup mailbox and status page |

## 5. Regional failover sequence (RC.RP)
Recover in BIA priority order (P05 section 8). Each step is validated before the next begins.

| Order | Resource | Target (BIA RTO) | Today | Validation |
|---|---|---|---|---|
| 1 | Identity provider and break-glass access (BP-15) | 1 h | 1 h | Responders signed in with security keys |
| 2 | Network hub, security tooling, and log archive in the DR region | 1 h | 2 h | Guardrails active; logs flowing |
| 3 | Database replicas promoted (12 shards, then the healthcare shard) | 1 h | 3 h | Replica lag checked; row counts compared |
| 4 | Core services deployed from signed images (agent workspace, API, chat) | 1 h | 3 h (manual DNS steps) | Synthetic checks pass |
| 5 | Channel ingestion connectors | 2 h | 4 h | Test emails and chats arrive |
| 6 | Healthcare cell services | 2 h | 5 h | Synthetic checks pass in the healthcare account |
| 7 | Monitoring, SIEM feeds, and MDR coverage | 4 h | 5 h | Alerts fire on test events |
| 8 | Search indexes (recent 30 days first) | 4 h | about 20 h for full rebuild | Agents can find recent tickets |
| 9 | CI/CD, AI services, reporting | 8 h | 9 h | Deploy pipeline and feature flags restored |

The "Today" column comes from the February 2026 test. The gap between the two columns is POAM-010; until it closes, customer updates must give realistic times, not the targets.

## 6. Communication and contracts (RS.CO, RC.CO)
- **Status page:** first post within 15 minutes; updates every 30 minutes; no speculation about cause.
- **Customers:** email to security and administrator contacts at 1 hour and every 2 hours; Enterprise customers with 24-hour terms receive a written status within 24 hours.
- **Banks:** 4-hour notice per section 3, then updates at least every 4 hours until restoration.
- **Covered entities:** calls at 4 hours if the healthcare cell is affected; a security incident report under the BAA if counsel decides the outage is one (for example in the destructive attack variant).
- **Service credits:** the CFO computes credits from the monitoring data and issues them automatically on the next invoice; the General Counsel tracks Enterprise termination rights (availability below 99.0% in 2 consecutive months).
- **After restoration:** a customer-facing incident summary within 5 business days.

## 7. Destructive attack variant (RS.AN, RS.MI)
If databases, snapshots, or backups were deleted, or administrator credentials were misused:
1. **Freeze administration.** Revoke all elevated sessions; suspend just-in-time approvals except for 2 named responders; switch to break-glass accounts with hardware keys.
2. **Protect what remains.** Confirm the state of replicas in the DR region and any write-once backups (the vault is due 2026-12-31 under POAM-011; until then, backups may be deletable). Snapshot what is left into the security tooling account.
3. **Call the insurer hotline and counsel** before engaging vendors; forensics through counsel; follow `ir-runbook.md` sections 4 to 6 for evidence, investigation, and any data-theft notices.
4. **Restore from the last known-good point** in the DR region or from point-in-time recovery, after forensics confirms the attacker's access is removed. Rebuild services from signed images only.
5. **Extortion:** the POL-03 4.8 rules apply, including the OFAC sanctions check.
6. **Notices:** the bank 4-hour notice applies to the disruption whatever its cause; the data-theft notices in `ir-runbook.md` apply if data was taken.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days; report within 30 days (POL-03 4.11).
- Update the BIA recovery times (P05), the risk register (P01 R-006, R-007, R-042), the POA&M (P07), the DR plan, and this runbook.
- Record the event in the SOC 2 availability evidence (P09 A1.2, A1.3) and the incident log (CC7.4, CC7.5).
- Retain records for 6 years (POL-01 4.14).

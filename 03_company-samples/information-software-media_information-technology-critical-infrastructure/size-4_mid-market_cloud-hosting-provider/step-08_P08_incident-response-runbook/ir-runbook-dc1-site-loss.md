# Incident Response Runbook: Loss of Data Center DC-1 (Hurricane or Facility Failure)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (cloud hosting and managed infrastructure provider) |
| Tier / Vertical | Mid-Market / Information Technology |
| Incident type | DC-1 (Florida, commercial only) is lost or must be shut down for days: hurricane, flood, extended power or cooling failure, or a facility evacuation. About 13,000 commercial VMs (54% of commercial VMs) run there, and about 65% of them have no replica |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) and NIST SP 800-34 Rev. 1 contingency planning |
| Policy basis | POL-03 sections 4.13 to 4.15; STD-07 Contingency and recovery |
| Companion documents | `ir-runbook.md` (tooling compromise); `notification-matrix.csv`; BIA (P05), including the 5-day DC-1 scenario |
| Runbook owner | VP Platform Engineering (incident commander for site loss), with the Director of NOC and Customer Support |
| Approved | 2026-09-22 by the Chief Technology Officer; effective 2026-10-01 |
| Last tested | Never. First tabletop 2027-03-15 and a partial failover exercise by 2027-03-31 (POAM-009, POAM-010) |

## 0. Governance and roles (Govern)
| Tier | Members | Decides |
|---|---|---|
| **Crisis management team (CMT)** | Chair: Chief Technology Officer. CEO, CFO, General Counsel, Director of Security, VP Sales, Financial Services Account Director, Director of Communications, HR Director | Pre-storm shutdown, customer priorities for scarce capacity, credits and commercial terms, staff safety, public statements |
| **Site and platform team** | Incident commander: VP Platform Engineering. DC-1 Data Center Operations Manager, platform engineers, network engineers, Director of Cloud Operations, Director of Backup and DR Services | Failover, capacity at DC-2 and DC-3, power-down and restart sequence |
| **Customer response cell** | Director of NOC and Customer Support (lead), account managers, Financial Services Account Director | Status updates, bank notices, restore queue, customer requests |

**Staff safety comes first.** No employee or contractor stays at DC-1 or travels into a storm path. The HR Director tracks staff check-ins. The secondary NOC desk at the DC-2 metro office takes over if the Florida NOC is affected.

**Security does not stop.** The Security Operations Manager stays in the IRT. Attackers use disasters for phishing and for access requests that skip normal checks (P01 R-047). Emergency changes still go through PAM and are recorded.

## 1. Preparation checks (Identify / Protect)
- [x] Government Cloud is not hosted at DC-1; government VMs are replicated between DC-2 and DC-3
- [x] Paid replication tier (about 35% of commercial VMs) replicates DC-1 VMs to DC-2 or DC-3
- [x] Customer backup platform runs at DC-2 and DC-3, outside the storm area
- [x] Status page runs on a separate provider; secondary NOC desk at the DC-2 metro office
- [ ] One contingency plan for both partitions, including DC-1 site loss (POAM-022, due 2026-12-31). **Gap: this runbook is the interim plan**
- [ ] DC-1 failover exercise (POAM-009). **Never tested**
- [ ] Spare capacity at DC-2 and DC-3 for replicated DC-1 VMs plus priority restores (POAM-022, due 2027-06-30). **Today about 4,550 replicated VMs fit; restores of unreplicated VMs compete for the rest**
- [ ] Commercial control plane restore within 4 hours (POAM-009). **Last test took 9 hours**
- [ ] Break-glass accounts documented for the DC-1 hypervisor managers (P05 key finding 5)
- [ ] All 38 bank designated contacts verified (POAM-019)
- [x] Printed call trees and the bank contact list at the Florida NOC and the DC-2 metro office

## 2. Triggers and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| National Hurricane Center forecast puts DC-1 within the cone of a Category 3 or stronger storm within 72 hours | Weather service; colocation provider notice | **Pre-storm phase (section 3)**; CMT convenes |
| Colocation provider declares an emergency, generator failure, or loss of cooling | Provider notice; facility alarms | Declare; start controlled shutdown if temperatures rise |
| Loss of both carriers at DC-1, or DC-1 unreachable for 15 minutes | NOC monitoring | Declare; confirm with the provider |
| Evacuation order covering DC-1 | Provider; local authorities | Declare; remote operations only |

**Declare severity 1** when DC-1 is down or expected to be down for more than the 4-hour MTD for commercial hosting (P05 BP-01).

## 3. Pre-storm phase (72 to 0 hours before landfall)
| Time | Step | Who |
|---|---|---|
| 72 h | CMT convenes; confirm fuel, spares, and provider staffing; freeze non-emergency changes at DC-1 | VP Platform Engineering |
| 72 h | Notice to all DC-1 customers: risk, what the company will do, recommended actions (take backups, buy replication, prepare to fail over their own services) | Director of NOC and Customer Support |
| 72 h | Notice to the 38 banks about any DC-1 services they use. A scheduled, previously communicated shutdown is not a notification incident (12 CFR 53.4(b)); an unplanned outage may be | Financial Services Account Director |
| 48 h | Verify replication is current for all replicated VMs; increase snapshot frequency for backup service customers at DC-1 | Director of Backup and DR Services |
| 48 h | Reserve capacity at DC-2 and DC-3; pause non-urgent provisioning there | VP Platform Engineering |
| 24 h | Move the commercial control plane's DC-1 dependencies (if any) and the DC-1 PAM bastion's role to DC-2 | Director of Cloud Operations |
| 24 h | CMT decision: run through the storm, or controlled shutdown before landfall. Shutdown is chosen if the provider cannot guarantee fuel and staffing for 72 hours | CTO |
| 12 h | If shutdown: fail over replicated VMs to DC-2 and DC-3, then power down DC-1 clusters in order (workloads, storage, management) | Platform engineers |

## 4. Response during the outage (RS.MA, RS.MI, RC.RP)
| Time after outage | Step | Who | Done when |
|---|---|---|---|
| 0-30 min | Declare; open the out-of-band channel; start the incident log with the outage time | Incident commander | Log open |
| 0-30 min | Status page: incident posted; updates every 30 minutes until stable (P05 BP-06) | Director of NOC and Customer Support | Posted |
| 0-2 h | Fail over replicated VMs to DC-2 and DC-3 (RTO 2 hours for BP-01). Confirm DNS and edge routing moved (BP-05 RTO 1 hour) | Platform and network engineers | Replicated VMs running |
| 0-4 h | **Bank determination.** For each bank using DC-1 services: is a material disruption of covered services for 4 hours or more actual or reasonably likely? A "computer-security incident" in 12 CFR 53.2(b)(4) is any occurrence that results in actual harm to the availability of an information system, so a facility loss counts. If yes, notify as soon as possible | Financial Services Account Director with General Counsel | Per-bank determination and notice times |
| 0-4 h | Confirm the commercial control plane and portal are healthy (they run in the cloud, but shared NOC staff and Florida offices may be affected) | Director of Cloud Operations | Portal up |
| 2-8 h | Start the restore queue for unreplicated VMs from the backup service (customers who bought it) into reserved capacity, in this order: banks, then customers with signed priority terms, then others by request time | Director of Backup and DR Services | Queue published to customers |
| 4-24 h | Customers without company backups restore from their own backups into new VMs at DC-2 or DC-3; the company provides capacity and engineer help | Customer response cell | Requests tracked |
| Daily | CMT review: capacity, restore progress, DC-1 return estimate, staff welfare, credits | CTO | Minutes |

**Security watch during the outage.** The SOC watches for phishing that uses the outage, for requests to reset customer administrator MFA (callback rule, POL-02 section 4.13), and for emergency firewall or access changes. Every emergency change is recorded and reviewed within 5 business days.

## 5. Notices and communications (RS.CO)
Follow `notification-matrix.csv`. An availability-only incident is **not** a FedRAMP Reportable Incident, because the IEC rules cover confidentiality and integrity of federal customer data (IEC-CSO-EFR), and the Government Cloud is not hosted at DC-1. The Federal Program Director still tells agencies about any effect on shared services, such as the portal or NOC response times, under their ATO terms.

| When | Action | Owner |
|---|---|---|
| As soon as possible after the determination | Bank notice to designated contacts (12 CFR 53.4(a)) | Financial Services Account Director |
| Within 30 minutes, then every 30 minutes | Status page updates for all customers | Director of NOC and Customer Support |
| Within 4 hours | Direct notice to DC-1 customers: what is down, expected restore path, how to request help | Director of NOC and Customer Support |
| Day 1 | Insurer notice (business interruption and extra expense, if covered) | CFO |
| After recovery | SLA credits applied automatically for the month (10%, 25%, or 50% tiers in the MSA) | CFO |
| From 2027-08-01 | Availability incidents also appear on the FedRAMP availability reporting service for Government Cloud core services, if any were affected (CDS-CSO-AVR) | Federal Program Director |

**Communications.**
- Customers: honest restore estimates; never promise a DC-1 return date the provider has not confirmed.
- Banks: direct calls from the Financial Services Account Director, followed by email to the designated contact.
- Media and public: statement approved by counsel focusing on staff safety and customer recovery.
- Staff: daily check-ins; HR support for affected employees and families.

## 6. Return to DC-1 (RC.RP)
1. Provider confirms the facility is safe, powered, and cooled; the DC-1 Data Center Operations Manager inspects the cage.
2. Power up management networks and PAM first, then storage, then hypervisor hosts, checking firmware and configuration against the baseline (STD-03) before workloads start.
3. Fail back replicated VMs during agreed customer windows; never fail back without customer agreement.
4. Verify that no unapproved changes were made at DC-1 during the outage (drift scan) and that monitoring of all DC-1 clusters reaches the SIEM.

## 7. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of return; written report within 30 days.
- Update the BIA (P05) with actual losses, the risk register (P01 R-018, R-005, R-022), the contingency plan, this runbook, and the capacity plan.
- Record whether recovery changes are FedRAMP significant changes (for example new capacity serving shared services).
- Report results to the audit committee, including credits paid and customers lost.

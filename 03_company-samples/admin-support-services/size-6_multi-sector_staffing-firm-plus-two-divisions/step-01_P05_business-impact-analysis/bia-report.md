# Business Impact Analysis: Cris Santos Company Holdings | Admin and Support Services | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 core employees plus about 230,000 temporary associates a week) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-01 to 2026-07-31 | **Approved:** board risk committee, 2026-09-10

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on: identity (SYS-G1), the SOC (SYS-G2), the cloud platform and network (SYS-G3), and the Group Workforce Platform (GWP, SYS-G4), which hires, credentials, and pays every worker in the group.
- **Division BIAs:** Staffing (focus), Professional Services and Consulting, and Home Health. They are rows in the same workbook (`bia.csv`, `division` column) so cross-division dependencies show in one place.

It supports:
- Home Health's HIPAA contingency plan and applications and data criticality analysis (45 CFR 164.308(a)(7), including (7)(ii)(E)) and its emergency preparedness program (42 CFR 484.102);
- the availability commitments in Staffing's Managed Workforce Solutions contracts and its planned SOC 2 report (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share four corporate services (SYS-G1 to SYS-G4). Division systems are SYS-D1 (Staffing front office, time capture, contact center, and the Managed Workforce Solutions VMS tenant), SYS-D2 (Consulting engagement systems and the Federal Solutions enclave), and SYS-D3 (the Home Health EHR, tablets, scheduling and EVV, and billing). See `../00_company-facts.md` sections 3 and 7.

The group's business is people. A day without hiring, credentialing, time capture, or pay is a day Staffing cannot fill orders, Home Health cannot staff visits, and associates stop reporting to work. That is why the GWP processes rank so high below, even though no patient care runs on them directly.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Staffing about $37 million per calendar day, Consulting about $10.4 million per business day, and Home Health about $4.9 million per calendar day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (fill orders, staff visits, deliver engagements) or a payroll is missed | One region, line, or service stops | Staff slowed but working |
| Regulatory | Reportable breach, missed Form I-9 or E-Verify deadline at scale, missed CMS requirement, or SEC disclosure | Missed contractual or internal deadline | Internal policy deviation |
| Safety | Plausible patient harm (missed home visit, unverified clinician on a shift) | Delayed but safe care | None |
| Reputation | National media, loss of major clients, or regulator attention | Regional media or client complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 24 processes: 8 group shared services, 7 Staffing, 4 Consulting, and 5 Home Health. 14 are High, 9 Moderate, and 1 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and network | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-G04 Payroll and pay delivery | Group | High | 48 h | 12 h | 1 h |
| BP-G05 Talent acquisition, onboarding, Form I-9, and E-Verify | Group | High | 24 h | 8 h | 1 h |
| BP-G06 Clinician credentialing | Group | High | 24 h | 8 h | 4 h |
| BP-HH01 Patient visits and point-of-care documentation | Home Health | High | 8 h | 4 h | 1 h |
| BP-HH02 Visit scheduling, EVV, and on-call | Home Health | High | 8 h | 4 h | 1 h |
| BP-ST04 Healthcare Staffing shift scheduling and deployment | Staffing | High | 12 h | 4 h | 1 h |
| BP-HH05 Emergency preparedness patient tracking | Home Health | High | 12 h | 4 h | 24 h |
| BP-CN02 Federal Solutions service desk operations | Consulting | High | 8 h | 4 h | 4 h |
| BP-ST01 Order fulfillment and associate dispatch | Staffing | High | 24 h | 8 h | 4 h |
| BP-CN01 Health IT Advisory engagement delivery | Consulting | High | 24 h | 8 h | 4 h |
| BP-ST02 Time capture and client approval | Staffing | High | 48 h | 12 h | 1 h |
| BP-ST05 Managed Workforce Solutions program operations | Staffing | Moderate | 24 h | 8 h | 4 h |
| BP-HH03 Intake and referrals | Home Health | Moderate | 24 h | 8 h | 4 h |
| BP-ST06 Recruiting contact center and associate service center | Staffing | Moderate | 24 h | 12 h | 4 h |
| BP-CN04 Client BAA incident notices and client access management | Consulting | Moderate | 24 h | 8 h | 4 h |
| BP-ST07 Background screening and drug testing orders | Staffing | Moderate | 48 h | 24 h | 4 h |
| BP-G08 Workforce data hub and reporting | Group | Moderate | 72 h | 24 h | 24 h |
| BP-ST03 Client billing and collections | Staffing | Moderate | 72 h | 48 h | 24 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-HH04 Medicare billing and OASIS submission | Home Health | Moderate | 120 h | 72 h | 24 h |
| BP-CN03 HR Technology consulting delivery | Consulting | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- **Patient safety** drives Home Health's 8-hour MTDs. Visits carry medication, wound care, and physician orders, and the clinical record must stay available (42 CFR 484.110). Healthcare Staffing (BP-ST04) and credentialing (BP-G06) are High for a related reason: an unconfirmed or unverified clinician leaves a hospital unit or a home visit uncovered.
- **Pay timing** drives payroll (BP-G04). Associates are paid every Friday, state wage-payment laws set pay timing, and an associate who is not paid often does not come back on Monday. The 48-hour MTD is the gap between the Wednesday payroll run and the Friday pay date; repeating the prior week's payroll is the workaround.
- **Employment eligibility deadlines** drive onboarding (BP-G05). Form I-9 Section 2 is due within 3 business days of hire (8 CFR 274a.2(b)(1)(ii)) and the E-Verify case within 3 employer business days (MOU Art. II.A.9). At about 2,500 hires a business day, a multi-day outage creates a compliance backlog, not just lost starts.
- **Contract commitments** drive Consulting (BP-CN01, BP-CN02) and Managed Workforce Solutions (BP-ST05): hospital go-lives and federal service levels are fixed in advance.
- **Revenue more than time** drives billing (BP-ST03, BP-HH04): invoices and claims can wait a few days.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. Break-glass accounts per critical system and cached credentials on field tablets are the fallback |
| GWP onboarding and credentialing | Group | Staffing fills; Home Health hires; Consulting hires | One platform hires about 640,000 people a year for all divisions |
| GWP payroll | Group | Every W-2 worker | Pays associates, consultants, and caregivers; a breach exposes all three divisions' workers (P08) |
| Time capture (BP-ST02) and visit records (BP-HH02) | Staffing; Home Health | GWP payroll | Without approved time and visit records, payroll repeats the prior week |
| Visit-pay records | Home Health | GWP | The feed carries patient names and addresses into payroll (scenario gap 1). It is not needed for pay calculation beyond visit date and type |
| Per diem clinicians (BP-ST04) | Staffing | Home Health visits (BP-HH01) | About 1,100 Staffing clinicians a week cover Home Health visits |
| SOC facts | Group | Every notice in P08; SEC filing | Every notice clock depends on the SOC establishing what happened |
| Client BAA notices (BP-CN04) | Consulting | About 160 hospital clients | 72-hour notice for 23 clients |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts, tested quarterly); one payroll engine instance for all workers (DR in provider B tested once a year, P01 GR-02); E-Verify itself (an outage is documented, not avoided); one VMS vendor for all 48 Managed Workforce Solutions clients (P01 ST-019).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs, SD-WAN | Cloud-hosted processes; branch and agency connectivity | Infrastructure as code; immutable backups in provider B; dual carriers at hubs |
| GWP payroll engine and integration platform (provider A) | BP-G04 | Database replication to provider B (RPO 15 minutes); immutable daily backups; payroll DR test once a year |
| GWP ATS, onboarding and I-9, credentialing (vendor SaaS) | BP-G05, BP-G06 | Vendor replication (RPO 1 hour per contract); weekly export of I-9 records to the group archive |
| SYS-D1 front office, time capture, VMS tenant | BP-ST01 to BP-ST07 | Vendor SaaS recovery commitments; time clock local buffering for 72 hours |
| SYS-D2 Federal Solutions enclave (provider B) | BP-CN02 | Snapshots every 4 hours; immutable daily backups |
| SYS-D3 Home Health EHR (vendor-hosted) | BP-HH01 to BP-HH05 | Vendor replication (RPO 15 minutes per contract); offline tablet documentation |
| People | All | Cross-trained payroll and onboarding centers in two states; remote work for 85% of payroll and onboarding staff |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and network
3. SOC visibility (SIEM and EDR)
4. Payroll and pay delivery (restore before the next pay date)
5. Talent acquisition, onboarding, Form I-9, and E-Verify
6. Clinician credentialing
7. to 10. Home Health visits and documentation, scheduling and EVV, Healthcare Staffing shifts, emergency preparedness patient tracking
11. to 14. Federal Solutions service desk, Staffing order fulfillment, Health IT Advisory delivery, time capture
15. to 24. Managed Workforce Solutions, Home Health intake, the contact centers, Consulting client notices, background screening, the data hub, billing, financial close, Medicare billing, and HR Technology consulting.

## 8. Key findings
1. **The GWP is the group's real single point of failure.** It is Moderate or High in every division's BIA because no division can hire, credential, or pay without it. Its availability rating in P02 is Moderate only because the weekly payroll workaround (repeat the prior payroll) holds for about 48 hours.
2. **The payroll DR path is tested once a year** (P01 GR-02). The 12-hour RTO has been met once, in a planned test, not after ransomware.
3. **The GWP is Moderate for availability but High for confidentiality and integrity** (P02). It holds SSNs and bank accounts for about 3.4 million current and former workers, Form I-9 records, consumer reports, clinician medical screening files, and (scenario gap 1) Home Health patient names and addresses.
4. **Notification capacity is itself a process** (BP-G02, BP-CN04, BP-G07). If the SOC or a contact center is down during an incident, the E-Verify, HIPAA, state, client, and SEC clocks keep running. The P08 runbook uses out-of-band channels for this reason.
5. **Home Health's emergency plan assumes the EHR is available.** The priority patient list (BP-HH05) is printed weekly, which covers a hurricane but not a cyber outage that starts mid-week. The P08 runbook and the Home Health supplement (P06) add a daily print during declared emergencies.

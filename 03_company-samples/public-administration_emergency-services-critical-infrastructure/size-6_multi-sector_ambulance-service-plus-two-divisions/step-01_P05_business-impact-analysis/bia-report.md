# Business Impact Analysis: Cris Santos Company Holdings | Emergency Services | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-16

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and network, email, finance, HR).
- **Division BIAs:** Ambulance Services (focus), Urgent Care, and Billing and Dispatch Services (BDS). They are rows in one workbook (`bia.csv`, `division` column), so cross-division dependencies are visible in one place.

It supports:
- each covered entity's contingency plan and applications and data criticality analysis (45 CFR 164.308(a)(7), including (7)(ii)(E)), for Ambulance Services and Urgent Care, and BDS's contingency plan as a business associate;
- the response-time and outage-notice terms in the 38 county ambulance agreements and the 14 external dispatch client contracts;
- the availability commitments in the BDS SOC 2 reports (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
The group dispatches about 8,500 ambulance responses a day through one CAD that BDS runs in the group cloud (SYS-D4 on SYS-G3) from 4 regional communications centers. Ambulance crews work from the ePCR and fleet mobile systems (SYS-D1). Urgent Care runs 520 clinics on a vendor-hosted EHR (SYS-D2). BDS also runs the revenue cycle platform and billing contact center (SYS-D3) for both divisions and about 170 external clients. Every division depends on SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network, and SYS-G4 corporate SaaS. See `../00_company-facts.md` sections 1, 3, and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Ambulance Services about $22.2 million per day, Urgent Care about $18.4 million per day, and BDS about $8.8 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (dispatch, transport, visits, claims) in a state or region | One center, clinic group, or service line stops | Staff slowed but working |
| Regulatory | Reportable breach, state EMS license action, county agreement default, or SEC disclosure | Missed records, reporting, or contract deadline | Internal policy deviation |
| Safety | Plausible delay of an emergency response, or patient harm from missing clinical information | Delayed but safe care (for example, a late discharge transport) | None |
| Reputation | National media, loss of county agreements or clients, or regulator attention | Regional media or client complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 26 processes: 7 group shared services, 8 Ambulance Services, 5 Urgent Care, and 6 BDS. 13 are High, 10 Moderate, and 3 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 2 h | 1 h | 15 min |
| BP-G04 Wide-area network and site connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-BD01 Emergency medical dispatch (CAD and call handling) | BDS | High | 2 h | 1 h | 15 min |
| BP-AM01 911 emergency response operations | Ambulance | High | 2 h | 1 h | 1 h |
| BP-BD02 CAD-to-CAD interfaces with county PSAPs | BDS | High | 4 h | 2 h | 15 min |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-AM04 12-lead ECG transmission to hospitals | Ambulance | High | 4 h | 2 h | 1 h |
| BP-AM05 Fleet connectivity and vehicle location | Ambulance | High | 4 h | 2 h | 24 h |
| BP-UC01 Urgent care visits and clinical documentation | Urgent Care | High | 8 h | 4 h | 1 h |
| BP-UC05 E-prescribing | Urgent Care | High | 8 h | 4 h | 1 h |
| BP-AM02 Interfacility and critical care transport | Ambulance | High | 8 h | 4 h | 1 h |
| BP-UC04 Lab and imaging results | Urgent Care | High | 12 h | 6 h | 1 h |
| BP-AM03 Patient care documentation and hospital record delivery | Ambulance | Moderate | 24 h | 8 h | 1 h |
| BP-UC02 Online check-in and scheduling | Urgent Care | Moderate | 24 h | 8 h | 4 h |
| BP-UC03 Telehealth visits | Urgent Care | Moderate | 24 h | 8 h | 4 h |
| BP-BD05 Client incident notices and reporting | BDS | Moderate | 24 h | 8 h | 4 h |
| BP-G07 Enterprise email and collaboration | Group | Moderate | 24 h | 8 h | 4 h |
| BP-AM06 Crew scheduling and credential tracking | Ambulance | Moderate | 48 h | 24 h | 24 h |
| BP-BD03 Claims and revenue cycle services | BDS | Moderate | 72 h | 48 h | 24 h |
| BP-BD04 Patient billing contact center and card payments | BDS | Moderate | 72 h | 24 h | 24 h |
| BP-G05 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-AM08 System status management (unit posting) | Ambulance | Low | 24 h | 12 h | 24 h |
| BP-BD06 AI call triage (advisory prompts) | BDS | Low | 72 h | 24 h | 24 h |
| BP-G06 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-AM07 County contract compliance reporting | Ambulance | Low | 336 h | 168 h | 24 h |

**What drives the values:**
- **Life safety drives dispatch and 911 response (BP-BD01, BP-AM01).** Dispatch never fully stops: telecommunicators switch to paper and radio at once. The 2-hour MTD is how long the communications operations leadership judges manual mode to be safe across a whole center before unit-tracking errors and delays grow. After that, county PSAPs are asked to send new calls to mutual-aid providers.
- **The landing zone inherits the CAD's limits (BP-G03).** Because the CAD runs only in provider A, a landing-zone outage is a dispatch outage. That is why its MTD (2 hours) and RPO (15 minutes) are the tightest of the shared services.
- **Patient safety drives Urgent Care (BP-UC01, BP-UC05).** Providers cannot treat safely without allergies, medications, and prior visits.
- **A state records rule drives the ePCR (BP-AM03).** In the Florida worked example, the receiving hospital can request the patient care record within 48 hours of dispatch (Rule 64J-1.014, F.A.C.). Each other state's EMS records rules are checked the same way. Tablets work offline, so short ePCR outages rarely lose data.
- **Revenue more than time drives claims (BP-BD03).** Payment can be delayed; payers accept late claims within filing limits. External clients with small cash reserves are prioritized.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. Cached CAD sessions and break-glass console accounts keep dispatch running |
| Landing zone and CAD hosting (SYS-G3) | Group | BDS dispatch; Ambulance 911 and interfacility response | One CAD instance in one provider is the group's largest single point of failure (gap 1) |
| Dispatch (BP-BD01) | BDS | Ambulance Services (BP-AM01, BP-AM02) and 14 external EMS agencies | A BDS outage is an Ambulance outage and a client outage at the same moment |
| CAD-to-CAD (BP-BD02) | County PSAPs | BDS, then Ambulance | Each PSAP must voice-transfer calls when the interface is down |
| ePCR and EHR data (BP-AM03, BP-UC01) | Ambulance; Urgent Care | BDS claims (BP-BD03) | Claims cannot be coded without the clinical record |
| Shared management subnet | Group (legacy account) | BDS CAD and revenue cycle file transfer servers | Not a business dependency, but a path for an attacker to move between the dispatch and billing systems (gap 3; P01 GR-02) |
| SOC facts (BP-G02) | Group | Every notice: two covered entities, BDS clients, counties, SEC | Every notice clock in P08 depends on the SOC establishing what happened |
| Client notices (BP-BD05) | BDS | 14 dispatch clients; about 170 billing clients; 38 counties (via Ambulance) | 15-minute phone notice of CAD outages; 72-hour BAA clocks for 31 billing clients |

**Single points of failure found:** the CAD in provider A (P01 GR-01; POAM-013); SYS-G1 (mitigated by break-glass accounts, tested quarterly); one clearinghouse for most ambulance claims (P01 BDS-012).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SYS-D4 CAD database (provider A) | BP-BD01, BP-BD02, BP-AM01, BP-AM02, BP-AM07 | Point-in-time restore (35 days) in provider A and hourly immutable copies to provider B. **The 15-minute RPO is met only inside provider A** until a provider B standby exists (POAM-013) |
| County P25 radio systems | BP-BD01, BP-AM01, BP-AM02 | County-operated; the fallback for everything |
| SYS-D1 ePCR (vendor SaaS) | BP-AM03 | Vendor replication (RPO 15 minutes per contract); offline tablets |
| SYS-D1 fleet mobile systems | BP-AM01, BP-AM04, BP-AM05 | Configuration in the router management cloud; no data of record on the vehicle |
| SYS-D2 EHR (vendor-hosted) | BP-UC01, BP-UC04, BP-UC05 | Vendor replication (RPO 15 minutes per contract) |
| SYS-D3 revenue cycle platform | BP-BD03, BP-BD04 | Nightly immutable backups to provider B; database replica in provider A |
| People | All | Cross-trained telecommunicators at all 4 centers; remote work for 80% of revenue cycle staff |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`). Manual dispatch mode and the county radio systems come before everything; they are procedures, not recovered systems.
1. SYS-G1 identity and break-glass access
2. Cloud landing zone and hub network in provider A (or the provider B standby once built)
3. WAN to the communications centers
4. CAD and call handling (BP-BD01)
5. 911 response operations (BP-AM01)
6. CAD-to-CAD interfaces (BP-BD02)
7. SOC visibility (SIEM and EDR)
8. to 13. 12-lead transmission, fleet connectivity, urgent care visits, e-prescribing, interfacility transport, lab and imaging results
14. to 26. ePCR delivery, check-in, telehealth, client notices, email, crew scheduling, claims, the billing contact center, financial close, unit posting, AI triage, payroll, and county reporting.

## 8. Key findings
1. **The CAD's 1-hour RTO is met only for failures inside provider A.** The database restores to a point in time, but a loss of the provider A region or of the legacy account (ransomware) would mean rebuilding the CAD elsewhere, which has never been done (P01 GR-01, POAM-013). Manual dispatch must be able to run for days with county help, not hours.
2. **One CAD serves 3 sets of stakeholders.** A CAD outage stops the Ambulance division's 911 and interfacility work, 14 external agencies' dispatch, and county CAD-to-CAD feeds at once. That is why P08 is built on this scenario.
3. **Notification capacity is itself a process** (BP-BD05, BP-G02, BP-G05). Client contracts expect a call within 15 minutes of a CAD outage. The center binders hold printed contact lists so this does not depend on email.
4. **Urgent Care can run without the CAD,** and the dispatch divisions can run without the EHR. The two covered entities share only corporate services and the revenue cycle platform, which is why a combined incident in P08 needs both a dispatch path and a billing path.

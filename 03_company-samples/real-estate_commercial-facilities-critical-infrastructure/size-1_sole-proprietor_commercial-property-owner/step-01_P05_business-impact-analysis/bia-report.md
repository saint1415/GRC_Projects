# Business Impact Analysis: Cris Santos Company | Commercial Facilities | Sole Proprietorship

**Organization:** Cris Santos Company (owner-operator of one mixed-use commercial building) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-07-22, with the on-call IT consultant | **Adopted:** Owner, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the building depends on, how long each can be down, and how much data each can lose. No law requires a BIA for this business. It is done because the CISA Cross-Sector Cybersecurity Performance Goals (CPG 2.0) ask for a recovery plan that covers degraded operations (goal 6.A), and because the owner needs to know what to restore first. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order and manual procedures in the incident runbook (P08).

## 2. Business description
The owner leases a two-story, 9,500 sq ft building in Florida to 8 tenants (3 ground-floor retail and food-service tenants, 5 second-floor offices) and manages it alone. The building's "automation" is three cloud services: access control for 4 doors (SYS-01), 6 cameras with cloud recording (SYS-02), and 8 smart thermostats for the rooftop HVAC units (SYS-03). They share one ISP router (SYS-04). Rent, leases, and maintenance requests run in a property management SaaS (SYS-05); everything else is email and files (SYS-06), a laptop (SYS-07), a phone (SYS-08), and a tenant screening service (SYS-09). See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 a year in rent and recoveries, or about $15,000 a month.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (a third of a month's rent, or a rent abatement claim) | $1,000 to $5,000 | Less than $1,000 |
| Operations | Building cannot be secured or tenants cannot open (doors or cooling unavailable) | Tenant services slowed; workaround needs the owner on site | Administrative delay only |
| Regulatory | Breach notice owed to individuals under Fla. Stat. 501.171 | Missed lease or contract obligation | Internal policy deviation |
| Safety | Building left open after hours, or a former credential holder can enter | Uncomfortable or unsafe heat in occupied suites | None |
| Reputation | A tenant does not renew or withholds rent over building security | Tenant complaints | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Building access and security | High | 24 h | 8 h | 24 h |
| BP-02 Building climate control | High | 24 h | 8 h | 24 h |
| BP-03 Tenant communications and maintenance | Moderate | 24 h | 8 h | 24 h |
| BP-04 Rent collection and tenant accounting | Moderate | 120 h | 72 h | 24 h |
| BP-05 Leasing and records | Low | 120 h | 72 h | 24 h |

**What drives the values:** physical security and tenant operations drive BP-01 and BP-02, not revenue. A day without door control or cooling in a Florida summer is the point where tenants cannot open safely. The equipment buys time: door controllers keep cached credentials and schedules, and thermostats keep their last schedule, when the internet or the cloud service is down. So an **outage** is tolerable for most of a day. A **compromise** is not: an attacker who signs in to the access control portal can unlock the entrances or add credentials, and the controllers will obey the cloud. That is why the RTO for BP-01 is 8 hours even though the hardware runs offline. The 24-hour RPO for BP-01 (door schedules, credentials) and BP-05 (files) is **not supported today**: no export of the access control configuration exists, and email, files, and the laptop have no backup (P01 R-011).

**Single-person dependency (the key finding).** The owner is the only administrator of every building system, the only person who can issue or remove a credential, the only holder of the mechanical keys, and the only person tenants call. Every second factor is on one phone. If the owner is ill, injured, traveling, or without the phone, BP-01 to BP-03 exceed their MTD together, and nobody else can lock the building or restore cooling. Actions (P01 R-009, due 2026-12-31):
1. Write one-page manual procedures: locking and unlocking the entrances with mechanical keys, setting each thermostat at the wall, and who to call for each failure.
2. Put the recovery codes for the building portals and email, a spare mechanical key set, and a one-page access sheet in a sealed envelope held by the owner's real estate attorney.
3. Agree in writing with the HVAC contractor (thermostats at the wall) and the installer (door hardware) on what each may do if the owner cannot be reached.
4. Give each tenant a printed emergency contact sheet with the owner, the HVAC contractor, and the installer.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Access control (SaaS plus 4 door controllers) | Door schedules, 58 credentials, door event history; controllers cache offline | BP-01 |
| SYS-02 Cloud video (6 cameras) | Entrance and parking video, 30-day retention | BP-01 |
| SYS-03 Smart thermostats (8) | HVAC schedules and setpoints; keep last schedule offline | BP-02 |
| SYS-04 Router and internet line | Connects SYS-01 to SYS-03 to their cloud services; lobby Wi-Fi | BP-01, BP-02 |
| SYS-08 Phone | Admin apps, every second factor, the owner's own door credential, tenant calls | BP-01, BP-02, BP-03 |
| SYS-05 Property management SaaS | Leases, ACH rent, maintenance requests | BP-03, BP-04, BP-05 |
| SYS-06 Email and files | Tenant mail, lease applications, guarantor files, contracts (no backup) | BP-03, BP-05 |
| SYS-07 Laptop | Main admin device; saved passwords (no backup) | BP-04, BP-05 |
| Contracted services | Installer, HVAC contractor, IT consultant, internet provider, CPA, attorney | BP-01 to BP-05 |
| Physical | Mechanical keys, thermostat wall controls, utility room, home-office file cabinet | BP-01, BP-02, BP-05 |
| People | Owner only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and second factors | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Trusted control of SYS-01 doors (locked after hours, correct credentials) | 2 h | Mechanical keys; owner on site; set entrances to locked in the portal from a clean device |
| 3 | SYS-03 thermostat schedules | 4 h | Set each thermostat at the wall; HVAC contractor on site |
| 4 | SYS-04 router and internet | 8 h | Controllers and thermostats run offline; phone hotspot for the owner |
| 5 | SYS-02 video | 8 h | Cameras keep recording to the cloud if the internet is up; owner on-site checks if not |
| 6 | SYS-05 property management access | 72 h | Phone and paper; tenants pay by check |
| 7 | SYS-06 email and files; SYS-07 laptop | 72 h | Vendor web portals from the phone; paper lease files |

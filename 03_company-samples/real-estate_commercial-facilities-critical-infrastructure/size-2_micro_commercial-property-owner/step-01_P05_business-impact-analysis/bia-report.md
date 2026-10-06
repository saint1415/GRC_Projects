# Business Impact Analysis: Cris Santos Company | Commercial Facilities | Micro

**Organization:** Cris Santos Company, LLC (commercial office and retail property owner-operator) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Property Manager (security and privacy lead) with the Building Engineer, the Bookkeeper, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** Managing Member, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the recovery goal in the CISA Cross-Sector Cybersecurity Performance Goals (CPG 6.A, execute the incident recovery plan, including operating in a degraded manner) and the backup goal (CPG 3.O);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the ransomware runbook (P08).

No regulation requires this company to have a BIA. It is done because the building systems are part of what tenants pay for: space that is secure, cooled, and reachable.

## 2. System and business description
Two Florida properties: a 3-story office building (Property A, 21 tenants) and a strip retail center (Property B, 12 tenants), about 300 credential holders, and 7 employees. Building operations run on the Building Automation and Access Control System (BAACS, P02): the BAS at Property A (one front-end workstation, one supervisory controller, about 60 field controllers), the cloud access control and video platform with 9 door controllers and 28 cameras, and the property networks. Business operations run on SaaS: the productivity suite, the property management and accounting system with the tenant portal, the payroll service, and the tenant screening service. The MSP runs the office IT and the cloud backup. See `../00_company-facts.md` sections 3 and 4.

**Life-safety systems are outside this BIA.** Fire alarm panels, elevators, and their emergency phones use vendor-maintained cellular communicators and do not depend on any system in scope. The BAS reads no life-safety points; keeping it that way is a design rule in the SSP (P02).

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $3,000 per day across both properties.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $15,000 (about 5 days of revenue), including rent abatement claims and emergency contractor or guard costs | $3,000 to $15,000 | Less than $3,000 |
| Operations | A property cannot be occupied normally (no cooling, entrances not controllable) | One building system or one property degraded | Staff slowed but working |
| Regulatory and contractual | Breach notice under Fla. Stat. 501.171, or loss of SAQ P2PE eligibility | Missed lease notice or acquirer deadline | Internal policy deviation |
| Safety | Plausible harm to occupants (heat stress, unsecured entrances at night) | Degraded but safe conditions | None |
| Reputation | Local media coverage or the loss of a major tenant at renewal | Tenant complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Building access control and tenant credentialing | High | 24 h | 8 h | 24 h |
| BP-02 Building environmental control at Property A | High | 24 h | 12 h | 24 h |
| BP-03 Tenant communications and emergency notices | High | 8 h | 4 h | 24 h |
| BP-04 Video surveillance and incident review | Moderate | 48 h | 24 h | 24 h |
| BP-05 Engineering work orders and tenant service requests | Moderate | 48 h | 24 h | 4 h |
| BP-06 Rent billing, ACH collection, and tenant accounting | Moderate | 72 h | 48 h | 4 h |
| BP-07 Card payment acceptance | Low | 120 h | 72 h | 24 h |
| BP-08 Leasing, tenant screening, and lease files | Low | 120 h | 72 h | 24 h |
| BP-09 Payroll and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Access control (BP-01).** Door controllers cache credentials and schedules for up to 72 hours, so the doors keep working. What stops is the ability to disable a lost or departed holder's fob. After one day the company must post a guard at the Property A front entrance at night (about $40 an hour).
- **HVAC (BP-02).** Field controllers keep their last programs, so cooling continues at first. Beyond one day without the workstation, the Building Engineer cannot see alarms, and comfort complaints and tenant server-room heat build up. Leases allow rent abatement after 5 consecutive business days of untenantable premises, so cost rises steeply after the first week.
- **Communications (BP-03).** Shortest MTD. Leases require notice of service interruptions, and leases signed since 2024 require notice within 72 hours of unauthorized access to tenant employees' data in the access control system.
- **Rent (BP-06).** About $92,000 a month, mostly collected in the first week. The ledger is vendor-hosted, and the company holds a cash reserve of about 45 days of expenses.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 BAS | Front-end workstation, supervisory controller, about 60 field controllers | Nightly image of the workstation in SYS-08 (**never restore-tested**); field controller programs held only by the controls contractor | BP-02 |
| SYS-02 Access control | Cloud platform, 9 door controllers and readers, 342 credentials | Vendor-hosted database; controllers cache credentials (vendor SOC 2 report, P09) | BP-01 |
| SYS-03 Video | 28 cameras with 30-day cloud recording | Vendor-hosted; no local recording | BP-04 |
| SYS-04 Property networks | Property A firewall, switches, Wi-Fi; Property B router; one internet line each | Firewall configuration backed up by the MSP; Property B router not backed up | BP-01, BP-02, BP-04 |
| SYS-05 Productivity suite | Email and the shared drive (leasing and HR files) | Vendor resilience; shared drive copied nightly to SYS-08 (never restore-tested) | BP-03, BP-08, BP-09 |
| SYS-06 Property management system | Leases, receivables, tenant portal, work orders | Vendor backups and replication (vendor states an RPO of 1 hour in its service terms) | BP-03, BP-05, BP-06 |
| SYS-07 Endpoints | 4 laptops, 2 desktops, 3 tablets | No local data by design, except the Bookkeeper's downloads | All |
| SYS-09 P2PE terminal | Stand-alone on cellular | Processor-hosted | BP-07 |
| People | Building Engineer (only person who can run the BAS and the plant by hand); Property Manager (only full platform administrator besides the integrator) | Cross-training of one Maintenance Technician on manual HVAC operation (to be done) | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Access control and video platform vendor | BP-01, BP-04 | SOC 2 Type 2 report (Security and Availability) reviewed in P09; 99.9% monthly availability target; controllers cache for 72 hours |
| Controls contractor | BP-02 (rebuild of the workstation and controller programs) | Service agreement with next-business-day on-site response; no written recovery commitment; holds the only controller program copies |
| MSP (and its backup subcontractor) | Recovery of every office computer, the firewall, and the backups | 4-business-hour response time; no recovery time commitment; no restore ever tested |
| Property management system vendor | BP-03, BP-05, BP-06 | Vendor service terms (RPO 1 hour, 99.5% availability) |
| Productivity suite vendor | BP-03, BP-08, BP-09 | Vendor service commitments (standard terms) |
| Internet providers (one per property) | Platform administration, cameras, BAS remote alarms | None; single line at each property |
| Security integrator | Door and camera hardware repair | On-call; no written response time |

**Key findings:**
1. **The BAS RPO of 24 hours is not supported today.** The workstation image has never been restored, it sits behind one MSP password, and the field controller programs exist only at the controls contractor. The 12-hour BAS RTO is unproven (risk R-002 in P01; CPG 3.O in P03).
2. **The access control platform meets the BIA.** Cached credentials (72 hours) outlast the 24-hour MTD, and the vendor's SOC 2 report covers availability. The weak point is the company's own administrator accounts, not the vendor.
3. **One person can run the building by hand.** Only the Building Engineer knows the manual procedures, and they are not written down (risk R-017).
4. **No vendor has a recovery commitment.** The MSP's 4-business-hour response and the controls contractor's next-business-day visit are response times, not recovery times. The contract terms in P01 (R-010, R-011) add them.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Administrator accounts (suite, access control platform, property management system) and one clean laptop | 2 h | Sealed break-glass credentials in the incident binder (POL-02 B.7); a spare laptop pre-imaged by the MSP (to be purchased) |
| 2 | Property A firewall and network (SYS-04) | 4 h | Disconnect building devices from the office network; phone hotspot for the administrator laptop |
| 3 | Tenant communications: email and tenant portal (SYS-05, SYS-06) | 4 h | Printed contact list; Property Manager's cell phone |
| 4 | Access control administration (SYS-02) | 8 h | Doors on cached credentials; on-call guard at night |
| 5 | BAS front-end workstation (SYS-01) | 12 h | Hand operation of rooftop units; controls contractor laptop to the supervisory controller; restore or rebuild the workstation |
| 6 | Cameras (SYS-03) | 24 h | Rounds by the Maintenance Technicians; on-call guard |
| 7 | Work orders (SYS-06 on clean tablets) | 24 h | Paper work orders |
| 8 | Rent and accounting (SYS-06 from the Bookkeeper's rebuilt desktop) | 48 h | Prior month's rent roll; checks |
| 9 | Shared drive restore (SYS-08 to SYS-05) | 72 h | Executed leases in SYS-06; attorney copies |
| 10 | Card terminal (SYS-09) and payroll (SYS-11) | 72 h | Invoice tenants; payroll service repeats the prior payroll |

The order (administrator accounts, network, communications, access control, BAS) is used in the P08 runbook. Access control comes before the BAS because an uncontrolled entrance is an immediate security exposure, while the field controllers keep cooling running and the plant can be run by hand.

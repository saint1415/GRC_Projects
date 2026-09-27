# Business Impact Analysis: Cris Santos Company | Commercial Facilities | Small

**Organization:** Cris Santos Company, LLC (commercial office and retail property owner-operator) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the Director of Engineering, Security Manager, and Controller | **Approved:** Chief Operating Officer, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the recovery goal in the CISA Cross-Sector Cybersecurity Performance Goals (CPG 6.A, execute the incident recovery plan, including operating in a degraded manner) and the backup goal (CPG 3.O);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the ransomware runbook (P08).

No regulation requires this company to have a BIA. It is done because the building systems are the product the company sells: a tenant pays for space that is secure, cooled, and accessible.

## 2. System and business description
The company owns and operates three Florida properties: an office tower (Property A), a retail center (Property B), and an office park (Property C). It has about 101 tenants, about 1,750 badge holders, and 60 employees. Building operations run on the Building Automation and Access Control System (BAACS): the building automation system (BAS), the cloud-hosted access control platform with on-premises door controllers, video surveillance, and the OT network segments. Business operations run on SaaS (property management and accounting, identity, productivity, visitor management, payroll) and one cloud tenant. See `../00_company-facts.md` sections 3-4.

**Life-safety systems are outside this BIA.** Fire alarm, elevator, and emergency voice systems run on separate vendor-maintained networks and do not depend on any system in scope. The BAS reads fire alarm status through read-only relay points. Keeping it that way is a design requirement (P02).

## 3. Impact categories and values
Dollar values are scaled to $20.4 million in annual revenue, about $56,000 per day across the portfolio.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $150,000 (about 3 days of revenue), including rent abatement claims | $30,000 to $150,000 | Less than $30,000 |
| Operations | A property cannot be occupied normally (no cooling, doors not controllable) | One building system or one property degraded | Staff slowed but working |
| Regulatory and contractual | Breach notice under Fla. Stat. 501.171, or loss of the ability to validate PCI DSS | Missed lease notice or reporting deadline | Internal policy deviation |
| Safety | Plausible harm to occupants (heat stress, doors that do not release, unsecured entrances) | Degraded but safe conditions | None |
| Reputation | Local media coverage or a major tenant non-renewal | Tenant complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Physical access control and tenant credentialing | High | 4 h | 2 h | 1 h |
| BP-02 Building environmental control (HVAC, lighting, metering) | High | 24 h | 12 h | 24 h |
| BP-03 Tenant and emergency communications | High | 8 h | 4 h | 24 h |
| BP-04 Video surveillance and security monitoring | Moderate | 24 h | 8 h | 24 h |
| BP-05 Engineering work orders and tenant service requests | Moderate | 48 h | 24 h | 4 h |
| BP-06 Visitor management at Property A | Moderate | 24 h | 8 h | 24 h |
| BP-07 Rent billing, collections, and tenant accounting | Moderate | 72 h | 48 h | 4 h |
| BP-08 Card payment acceptance | Low | 120 h | 72 h | 24 h |
| BP-09 Leasing and lease administration | Low | 120 h | 72 h | 24 h |
| BP-10 Payroll and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Access control (BP-01)** has the shortest MTD. Door controllers cache credentials for up to 72 hours, so doors keep working, but no badge can be issued or revoked. A badge that should have been revoked but still works is a physical security gap, and guards must staff the entrances.
- **HVAC (BP-02)** can run for a while because field controllers keep their last programs. Beyond one day without supervisory control, engineers cannot answer chiller or air handler alarms, and tenant spaces and tenant server rooms overheat in the Florida climate. Leases allow rent abatement after 5 consecutive business days of untenantable premises, so cost rises steeply after the first week.
- **Communications (BP-03)** are High because lease clauses require prompt notice, and 12 tenants have a 72-hour notice clause for access control data incidents.

**Key finding:** the BAS RPO of 24 hours is **not supported today**. The only BAS backup is a weekly server image in the same cloud account as production, and field controller programs and graphics are held only by the integrator (gap 6). No restore has ever been tested, so the 12-hour BAS RTO is unproven. This drives risk R-002 in P01 and CPG 3.O in P03.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 BAS | Supervisory server, 2 engineering workstations, about 420 field controllers | BP-02 |
| SYS-02 Access control platform | Cloud service, 46 door controllers, 180 readers, 6 turnstile lanes | BP-01, BP-06 |
| SYS-03 Video surveillance | About 260 cameras, 4 NVRs, the vendor cloud console | BP-04 |
| SYS-04 Property networks | Firewalls, switches, Wi-Fi, OT segments, site-to-site VPN, one ISP per property (Property A also has a backup ISP) | BP-01, BP-02, BP-04 |
| SYS-05 Identity provider | Single sign-on and MFA | BP-01 (administrator portal), BP-03, BP-07 |
| SYS-07 Property management system | Leases, receivables, tenant portal, work orders | BP-03, BP-05, BP-07, BP-09 |
| SYS-08 Cloud tenant | BAS historian, file storage, backup vault | BP-02, BP-09 |
| SYS-09 Endpoints | Engineering workstations and tablets, security console PCs, office laptops | All |
| SYS-10 P2PE terminals | Card acceptance | BP-08 |
| SYS-11 Visitor management | Lobby kiosks | BP-06 |
| People and facilities | Chief engineers who can run plant equipment by hand; security console operators; Property Managers with printed tenant contact lists | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 Identity provider and break-glass administrator accounts | 1 h | Two break-glass accounts sealed offline (to be created; POL-02 4.7) |
| 2 | SYS-04 Property networks and the OT firewall rules | 2 h | Isolate OT segments; cellular modem for the Property A security console (to be purchased) |
| 3 | SYS-02 Access control platform administration | 2 h | Doors run on cached credentials; guards at entrances |
| 4 | Clean engineering workstations and security console PCs | 4 h | Two pre-imaged spare laptops held by the Director of Engineering |
| 5 | SYS-01 BAS supervisory server | 12 h | Local hand control and manual rounds; restore from backup (backup redesign under POAM-004) |
| 6 | SYS-03 Video recorders and console | 8 h | Guard patrols |
| 7 | SYS-11 Visitor management | 8 h | Paper log |
| 8 | SYS-07 Property management system access | 48 h | Vendor-hosted; invoice from the prior register |
| 9 | SYS-10 P2PE terminals | 72 h | Invoice customers |
| 10 | Payroll SaaS | 72 h | Repeat prior payroll |

The priority order (identity, network, access control, clean endpoints, BAS) is used in the P08 runbook. The BAS RTO (12 hours) is longer than the access control RTO (2 hours) because field controllers keep running and engineers can operate plant equipment by hand, while an uncontrolled door is an immediate security exposure.

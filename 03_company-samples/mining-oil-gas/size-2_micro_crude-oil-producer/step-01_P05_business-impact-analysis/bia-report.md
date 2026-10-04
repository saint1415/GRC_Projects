# Business Impact Analysis: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Micro

**Organization:** Cris Santos Company, LLC (independent crude oil producer, one field) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, with the OT availability considerations of NIST SP 800-82 Rev. 3 (sections 3.3.9 and 5.3.2)
**Prepared by:** Office Manager (Security Coordinator) with the Field Superintendent, the Field Technician, the Production Accountant, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** Owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the contingency and recovery planning that the voluntary benchmark calls for (CSF 2.0 RC.RP; SP 800-82 Rev. 3 section 3.3.9);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

No binding federal rule requires a BIA from this company (P03 section 1). It is done because the cyber insurer, the larger non-operating partner, and the company's own emergency response plan all depend on knowing what must come back first.

For a small oil field, "downtime" has two layers. The SCADA host can be down while the wells keep pumping, because each pump-off controller runs its own logic and the safety shutdowns are hardwired. The real limit is how long 4 field staff can watch the field by hand. The values below reflect that.

## 2. System and business description
One Florida Panhandle field: 16 producing rod-pumped wells, 2 SWD wells, 4 shut-in wells, one tank battery, and one SWD facility. The field makes about 55 barrels of oil per day and about 1,400 barrels of produced water per day. The SCADA host at the field office (SYS-01) polls 18 field controllers by licensed radio and cellular (SYS-02) and pushes alarms to the SCADA vendor's cloud service (SYS-08), which calls the on-call phone. Production accounting (SYS-03), email and files (SYS-04), and online banking (SYS-10) are SaaS. The MSP runs office IT; the SCADA integrator supports the SCADA host. See `../00_company-facts.md` sections 1 to 4.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $3,000 per day net to the company.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $10,000 (about 3 days of revenue) | $3,000 to $10,000 | Less than $3,000 |
| Operations | The whole field is shut in, or produced water cannot be disposed of | Part of the field is shut in, or staff must run the field by hand | Staff slowed but production continues |
| Regulatory | Reportable discharge, injection permit violation, or breach notice to individuals | Late state production or injection report | Internal policy deviation |
| Safety and environment | Plausible injury, H2S exposure, or an oil or produced water release | Degraded safety alerting covered by patrols | None |
| Reputation | Loss of the purchaser's or partners' confidence, or royalty owner complaints to the state | Owner or partner complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Emergency alarm call-out and spill and H2S response | High | 4 h | 2 h | 24 h |
| BP-02 Produced water disposal | High | 12 h | 6 h | 24 h |
| BP-03 Well monitoring and remote control | High | 72 h | 24 h | 24 h |
| BP-04 Crude oil sales and hauling | Moderate | 120 h | 72 h | 24 h |
| BP-05 Production accounting, state reports, and royalty distribution | Moderate | 240 h | 120 h | 24 h |
| BP-06 Payables, banking, and crude sales settlement | Low | 120 h | 72 h | 24 h |
| BP-07 Payroll and HR | Low | 120 h | 72 h | 24 h |
| BP-08 Well servicing and maintenance | Low | 120 h | 72 h | 24 h |
| BP-09 Reservoir and geoscience work | Low | 240 h | 120 h | 24 h |

**What drives the values:**
- Safety drives BP-01. The H2S monitors, tank high-level switches, and SWD high-pressure switches act locally, but the SCADA call-out is how the on-call person learns about them after hours. Patrols every 2 hours can stand in for about 4 hours before the on-call Lease Operator needs relief.
- Water drives BP-02, not oil. The water tanks fill in about 12 hours at full rate, and then producing wells must be shut in.
- BP-03 tolerates 72 hours because Lease Operators already visit every well daily. SCADA mostly saves driving and catches failures between visits.
- For the SCADA-based processes (BP-01 to BP-03), the RPO is the age of the last good copy of the SCADA host configuration and controller programs. Process data from an outage cannot be recovered and is rebuilt from paper logs.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 SCADA host | One PC at the field office: polling, HMI, alarms, local historian | Weekly copy to an attached USB drive. **Never restore-tested; the drive would be lost with the host** | BP-01, BP-02, BP-03 |
| SYS-02 Field controllers and radios | 16 pump-off controllers, 2 PLCs, 900 MHz radio, 3 cellular modems | Controller programs only on the Field Technician's engineering laptop | BP-01, BP-02, BP-03 |
| SYS-08 SCADA alarm cloud service | Call-out to on-call phones; mobile viewer; analytics add-on | Vendor service; depends on SYS-01 sending data | BP-01, BP-03, BP-08 |
| SYS-03 Production accounting SaaS | Volumes, royalties, joint interest billing, state reports | Vendor backups (SOC 2 report states RPO 1 h; see P09) | BP-04, BP-05 |
| SYS-04 Productivity suite | Email, shared drive, run ticket photos | Vendor resilience; nightly copy to SYS-07 | BP-04 to BP-09 |
| SYS-07 Cloud backup (MSP) | Main-office computers and shared drive, 30 days of versions | **Never restore-tested** | BP-05 to BP-09 |
| SYS-05 Endpoints and phones | 7 computers, 5 smartphones | MSP reimage from its standard image (main office); none for the engineering laptop | All |
| SYS-06 Networks | Main-office firewall; field office router and Wi-Fi | Main-office configuration backed up by the MSP; field office router not backed up | All |
| People and facilities | Field Superintendent, 2 Lease Operators, Field Technician, Production Accountant, Office Manager, Owner; field office; tank battery | Cross-training: the Field Superintendent can cover a lease route; the Office Manager can cover payables | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| SCADA integrator | Rebuild of the SCADA host and recovery of controller programs | No written commitment; estimates 2 to 3 days to rebuild from installation media without a good backup |
| SCADA vendor (cloud alarm service) | BP-01 after-hours call-out; mobile viewing | Security whitepaper only; no availability commitment in the subscription terms |
| MSP | Recovery of main-office computers, email administration, cloud backup restores | Contract has a 4-business-hour response time, which is not a recovery time; does not cover the SCADA host |
| Production accounting vendor | BP-05 | SOC 2 Type 2 report reviewed (P09): RTO 24 h and RPO 1 h meet this BIA |
| Cellular carrier and radio tower lease | Polling of the 3 cellular sites and the radio base | None |
| Electric utility | Field office (30-minute UPS, no generator), SWD pumps, well motors | None |
| Crude purchaser and its carrier | BP-04 | Contract terms only |
| Payroll service and bank | BP-06, BP-07 | Standard service terms |

**Key findings:**
1. **The SCADA recovery point is unproven.** The only SCADA host backup is a USB drive that stays plugged into the host, so ransomware or a failure of the host would take both (gap 5; P01 R-003). Without a good copy, the integrator needs 2 to 3 days, which is past the 24-hour RTO for BP-03 and the 2-hour RTO for BP-01.
2. **Controller programs exist in one place.** They live only on the Field Technician's engineering laptop, which is not managed or backed up by the MSP (P01 R-020).
3. **After-hours alarms depend on a chain of 4 links:** the SCADA host, the field office internet line, the vendor's cloud service, and the on-call phone. Any one failing silences BP-01. Patrols are the only fallback (P01 R-024).
4. **The production accounting vendor meets the BIA.** Its stated RTO (24 h) and RPO (1 h) are inside the 120-hour RTO and 24-hour RPO for BP-05.
5. **The MSP contract has no recovery commitment** and does not cover the SCADA host. The P01 treatment adds the SCADA host to the MSP's backup and monitoring scope.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Field safety call-out (on-call Lease Operator, 2-hour patrols) | Immediate | Printed emergency response plan binder at the field office and in each truck |
| 2 | SWD facility on its local PLC panel | 6 h | Lease Operator on site runs the pumps; isolate the SWD PLC from SCADA if SCADA is compromised |
| 3 | SCADA host from a clean, verified backup, and the alarm connector to SYS-08 | 24 h (target; untested today) | Manual operations; shut-in order set by the Field Superintendent |
| 4 | Field radio base and cellular modems | 24 h | Manual operations |
| 5 | Smartphones and email for run ticket photos | 24 h | Paper run tickets carried to the main office |
| 6 | Production accounting access from a clean laptop | 72 h | Rebuild volumes from paper run tickets |
| 7 | Bank portal, payables, payroll | 72 h | Bank branch; payroll service repeats prior payroll |
| 8 | Shared drive restore (SYS-07 to SYS-04) | 120 h | Owner works from the encrypted laptop copy |

Priority 3 depends on a SCADA backup kept away from the host and restore-tested. Until POAM-003 and POAM-004 (P07) close, the company cannot rely on meeting it.

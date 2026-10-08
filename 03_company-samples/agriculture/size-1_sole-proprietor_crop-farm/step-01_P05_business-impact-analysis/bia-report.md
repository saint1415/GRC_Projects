# Business Impact Analysis: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Sole Proprietorship

**Organization:** Cris Santos Company (precision-agriculture crop farm) | **Tier:** Sole Proprietorship (owner-operator only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-operator, 2026-07-14, with the on-call IT technician | **Adopted:** Owner-operator, 2026-08-31
**Sources:** the owner's BIA worksheet, 2026-07-13 to 2026-07-14 (EV-034), the 2025 Schedule F (EV-024), the booking platform sales reports (EV-012), the sales by channel reports (EV-023), the buying point settlement sheets (EV-025), the SYS-01 alarm and export settings (EV-004, EV-005), the Home Farm and River Field walk-throughs (EV-009, EV-010), and the FMIS vendor's SOC 2 system description (EV-007). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owner's own statements, adopted by the owner on 2026-08-31.

## 1. Overview and purpose
This one-page BIA lists the five business functions the farm depends on, how long each can be down, and how much data it can lose. It is the first step of the 2026 security work and supports:
- the security category and availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the records the farm must keep to show it qualifies for the Produce Safety Rule qualified exemption (21 CFR 112.7; P03).

## 2. Business description
One owner-operator farms about 120 acres in Florida: U-pick strawberries, watermelons, and sweet corn at the 20-acre Home Farm, and peanuts under a center pivot at the 100-acre leased River Field. There are no employees. The farm management and irrigation software (SYS-01) is vendor SaaS; it holds the field records and remotely controls the Home Farm pump controller and the River Field pivot (SYS-06). Everything else runs on one laptop, a phone, a tablet, a consumer email and file account, an accounting SaaS, and a booking platform. See `../00_company-facts.md` and the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv).

The calendar drives the values below. **December to February is freeze season**: on a freeze night the strawberries must be covered by running sprinklers before the temperature reaches the critical level. May to September the peanuts need pivot irrigation. September and October are peanut harvest.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts (EV-024). In the U-pick season a weekend brings in about $4,000 (EV-012); the strawberry crop as a whole is worth about $70,000 (EV-024, EV-012).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $10,000 (a lost crop block, or about 3 weeks of average receipts) | $1,000 to $10,000 | Less than $1,000 |
| Operations | A crop cannot be irrigated or protected, or sales stop in season | Sales or harvest slowed; manual work needed | Administrative delay only |
| Regulatory | Records lost so the farm cannot show its qualified exemption or support a crop insurance claim; a reportable breach | Late program paperwork | Internal policy deviation |
| Safety | Harm to people (for example a fertigation error near U-pick customers) | Unsafe condition corrected quickly | None |
| Reputation | Loss of the buying point or a public breach notice | Customer complaints or online reviews | None outside the farm |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Irrigation and freeze protection | High | 2 h (freeze season); 48 h otherwise | 1 h | 24 h |
| BP-02 U-pick and farm stand sales | Moderate | 48 h | 24 h | 24 h |
| BP-04 Peanut harvest and marketing | Moderate | 72 h | 48 h | 24 h |
| BP-03 Field, exemption, and program records | Moderate | 120 h | 72 h | 24 h |
| BP-05 Farm administration and finance | Low | 120 h | 72 h | 24 h |

**What drives the values:** crop survival drives BP-01. The 1-hour RTO is met only by **manual operation** at the pump house (Hand-Off-Auto switch and local/remote selector), because the SYS-01 vendor states an 8-hour RTO in its SOC 2 report (EV-007; reviewed in P09). Revenue drives BP-02 only in season. BP-03 has a long MTD but a short RPO: the harm is losing records, not waiting for them. **The 24-hour RPO for BP-03 and BP-05 is not supported today**: SYS-01 has never been exported (EV-005), and the cloud files have no version history (EV-016; P01 R-007).

**Single-person dependency (the key finding).** The owner-operator is the only person who can start freeze protection, run the pivot, take bookings, pay bills, or reach any vendor, and the freeze alarm reaches only the owner's phone (EV-004, EV-034). If the owner is ill, injured, away, or asleep through the alarm on a freeze night, BP-01 exceeds its 2-hour MTD and the strawberry crop can be lost in one night. Actions (P01 R-006 and R-003, due 2026-11-30, before freeze season):
1. Write a one-page freeze-night and manual irrigation procedure and post it inside the pump house.
2. Sign a written mutual-aid arrangement with a neighboring grower who can start freeze protection by hand, and walk the neighbor through it once before December.
3. Install a standalone cellular freeze alarm at the field sensor that calls both the owner and the neighbor, independent of SYS-01 and the home internet.
4. Store SYS-01, email, bank, and booking recovery codes and a one-page emergency access sheet in a sealed envelope held by the owner's attorney.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-06 Irrigation OT | Pump controller, pivot panel, probes, freeze sensor; manual switches | BP-01 |
| SYS-01 FMIS and irrigation module (vendor SaaS) | Remote control, alarms, schedules; field and program records; vendor backups | BP-01, BP-03, BP-04 |
| SYS-04 Phone and tablet | Alarm texts; SYS-01 app; card reader; email codes | BP-01, BP-02, BP-04 |
| SYS-05 Home Farm network | Internet for the pump controller and laptop; phone hotspot is the fallback | BP-01, BP-02 |
| SYS-10 Sales systems | Booking platform, hosted payments, card reader, email list | BP-02 |
| SYS-09 Accounting and banking | Books, payments, W-9 data | BP-03, BP-05 |
| SYS-02 Email and files; SYS-03 Laptop | Correspondence and documents (no version history) | BP-03, BP-05 |
| Outside parties | Irrigation dealer, FMIS vendor, custom harvest operator, buying point, booking vendor, bank | BP-01 to BP-05 |
| People and places | Owner-operator only; pump house; home office | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual control of the pump and pivot (local and Hand) | Immediate | Written freeze-night procedure; neighbor under mutual aid |
| 2 | Owner access: phone and account second factors | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 3 | Internet at the Home Farm | 1 h | Phone hotspot |
| 4 | A clean access device | 2 h | Tablet as the spare; laptop rebuilt by the IT technician |
| 5 | SYS-01 FMIS and irrigation module | 8 h (vendor-hosted) | Manual operation; paper field notes entered later |
| 6 | SYS-10 booking and card reader | 24 h | Walk-ins; cash; card reader offline mode |
| 7 | SYS-02 email and files; SYS-09 accounting | 72 h | Vendor web portals; paper copies; checks |

# Business Impact Analysis: Cris Santos Company Holdings | Utilities | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the continuity leads of the Electric Utility, Gas Production, and Engineering Services | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services that more than one division depends on (identity, SOC, OT secure remote access, cloud and data platform, WAN, finance, HR).
- **Division BIAs:** the Electric Utility (focus), Gas Production, and Engineering Services. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the Electric Utility's CIP-009-6 recovery plans for the TCC and backup TCC and its storm restoration plans;
- the availability rating of the Distribution Operations Platform in the SSP (P02);
- impact ratings in the group and division risk registers (P01);
- the recovery order in the incident runbook (P08);
- the Availability commitments Engineering Services is preparing for its SOC 2 Type 2 report (P09).

## 2. System and business description
Corporate runs the shared services SYS-G1 (identity), SYS-G2 (SOC), SYS-G3 (cloud and data platform), SYS-G4 (OT secure remote access), and SYS-G5 (ERP, HR, finance). Division systems:
- **Electric Utility:** SYS-E1 Distribution Operations Platform (DOP), SYS-E2 transmission EMS at the TCC, SYS-E3 substations and field network, SYS-E4 AMI, SYS-E5 CIS, SYS-E6 load forecasting.
- **Gas Production:** SYS-N1 field SCADA and Production Operations Center (POC), SYS-N2 production accounting and royalty.
- **Engineering Services:** SYS-S1 client project platform, SYS-S2 design environment and commissioning laptops.

See `../00_company-facts.md` section 3.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 1: Electric Utility about $23 million per day, Gas Production about $10 million per day, and Engineering Services about $16 million per calendar day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $20 million for the group, or more than 1 day of a division's revenue | $2 million to $20 million | Less than $2 million |
| Operations | A division cannot deliver its core service (power delivery, gas deliveries, client projects) | One region, line, or service stops | Staff slowed but working |
| Regulatory | Missed NERC, DOE, or SEC deadline; potential violation of a Reliability Standard; client contract breach | Missed internal deadline | Internal policy deviation |
| Safety | Plausible harm to the public, line crews, or field operators (energized lines, gas releases) | Delayed but safe operations | None |
| Reputation | National media, state regulator attention, or loss of utility clients | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 28 processes: 7 group shared services, 10 Electric Utility, 5 Gas Production, and 6 Engineering Services. 15 are High, 12 Moderate, and 1 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-EU01 Transmission system operations (TOP) | Electric Utility | High | 2 h | 1 h | 0 h (real-time replication) |
| BP-EU02 Distribution system operations and switching | Electric Utility | High | 4 h | 2 h | 1 h |
| BP-EU05 Field area network and substation communications | Electric Utility | High | 4 h | 2 h | 24 h (configurations) |
| BP-EU03 Outage management and crew dispatch | Electric Utility | High | 4 h | 2 h | 1 h |
| BP-EU10 Regulatory event reporting (CIP-008, DOE-417, EOP-004) | Electric Utility | High | 1 h | 1 h | 24 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-GP05 Safety monitoring and emergency shutdown alarms | Gas Production | High | 4 h | 2 h | 1 h |
| BP-GP01 Field production monitoring and control | Gas Production | High | 8 h | 4 h | 1 h |
| BP-EU04 Substation protection and automation | Electric Utility | High | 8 h | 4 h | 24 h (settings) |
| BP-G01 Workforce identity and access | Group | High | 8 h | 2 h | 1 h |
| BP-G05 Wide-area network and site connectivity | Group | High | 8 h | 4 h | 1 h |
| BP-G04 Cloud landing zones and data platform | Group | High | 8 h | 4 h | 1 h |
| BP-GP02 Gas measurement, nominations, and firm supply | Gas Production | High | 12 h | 8 h | 1 h |
| BP-EU08 Customer outage communications | Electric Utility | Moderate | 12 h | 4 h | 1 h |
| BP-ES05 Client incident and vulnerability notices | Engineering Services | High | 24 h | 8 h | 24 h |
| BP-ES01 Client project delivery and collaboration | Engineering Services | High | 24 h | 8 h | 4 h |
| BP-EU09 Load forecasting and day-ahead purchasing | Electric Utility | Moderate | 24 h | 8 h | 24 h |
| BP-G03 OT secure remote access | Group | Moderate | 24 h | 8 h | 24 h |
| BP-GP03 Compressor station remote monitoring | Gas Production | Moderate | 24 h | 8 h | 4 h |
| BP-EU06 Metering and remote connect or disconnect (AMI) | Electric Utility | Moderate | 48 h | 24 h | 4 h |
| BP-ES04 Storm and emergency engineering support | Engineering Services | Moderate | 24 h | 12 h | 24 h |
| BP-EU07 Customer service, billing, and payments | Electric Utility | Moderate | 72 h | 24 h | 4 h |
| BP-ES02 Engineering design and analysis | Engineering Services | Moderate | 48 h | 24 h | 4 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-ES03 Field commissioning and testing | Engineering Services | Moderate | 72 h | 24 h | 24 h |
| BP-GP04 Production accounting and royalty payments | Gas Production | Moderate | 120 h | 72 h | 24 h |
| BP-G06 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-ES06 Federal contract delivery | Engineering Services | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Public and crew safety** drives the Electric Utility's short MTDs. Without SCADA and the OMS, every switching step needs a crew on site, and clearances depend on manual records. Storm season shortens the tolerable outage further.
- **Reliability Standard duties** drive BP-EU01. The TCC is a TOP Control Center; EOP-004-4 treats a complete loss of monitoring or control at a staffed BES control center for 30 continuous minutes as a reportable event, so the backup TCC must take over within the hour.
- **Reporting clocks** make reporting itself a process (BP-EU10, BP-ES05). DOE-417 Emergency Alerts are due within 1 hour of the incident, and CIP-008-6 initial notices within 1 hour of determining a Reportable Cyber Security Incident. These clocks keep running when systems are down.
- **Firm fuel deliveries** drive Gas Production's nominations process (BP-GP02). Safety systems at compressor stations act locally; the remote alarm path (BP-GP05) is what the POC loses.
- **Client schedules** drive Engineering Services. Outage windows at client substations are booked weeks ahead, so a 24-hour loss of the project platform is tolerable but a longer one is not.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| OT secure remote access (SYS-G4) | Group | Electric Utility DOP and 74 substations; Gas Production POC; Engineering Services engineers | One platform reaches three OT environments. Low availability need (Moderate), but a compromise spreads across divisions (P01 GR-01, P08) |
| Sign-in (SYS-G1) | Group | All IT processes; SYS-G4 MFA; AMI and CIS administration | A group identity outage stops Engineering Services and corporate. Grid operations keep running on separate OT domains |
| SOC facts (SYS-G2) | Group | Every notice in P08 | The CIP-008-6, DOE-417, client, state, and SEC clocks all depend on the SOC establishing what happened |
| Firm gas supply (BP-GP02) | Gas Production | Electric Utility power supply (BP-EU09) | Two plants fueled by Gas Production supply about 30% of the Electric Utility's purchased power. A Gas Production outage in a cold snap raises the Electric Utility's supply cost and reliability risk |
| Relay settings and commissioning (BP-ES03, BP-ES02) | Engineering Services | Electric Utility substations (BP-EU04) | Engineering Services prepares settings and commissions protection under the intercompany agreement, which has no security schedule (P03) |
| DOP changes and storm support (BP-ES04) | Engineering Services | Electric Utility (BP-EU02, BP-EU03) | About 180 Engineering Services engineers hold CIP access at the TCC; many more use SYS-G4 for the DOP |
| Cloud platform (BP-G04) | Group | SYS-S1, SYS-E6, outage map | Provider B hosts SYS-S1, so the project platform recovers independently of provider A |

**Single points of failure found:**
- SYS-G4 is one platform for three OT environments (mitigated for availability by on-site work; the confidentiality and integrity exposure is P01 GR-01).
- One EMS vendor support team for both the TCC and backup TCC (accepted; the vendor has a 4-hour on-site commitment).
- One nominations workstation path for Gas Production if SYS-N2 is down (P01 GP-012).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-E2 EMS at TCC and backup TCC | BP-EU01 | Real-time replication to the backup TCC; offline configuration backups (CIP-009-6 R1 Part 1.3) |
| SYS-E1 DOP at DCC and backup DCC | BP-EU02, BP-EU03 | Database replication to the backup DCC every 15 minutes; nightly backups to the OT backup server. **No offline copy and no full restore test since 2024** (P01 EU-006) |
| SYS-E3 substations and field network | BP-EU04, BP-EU05 | Approved relay settings and gateway configurations in the settings repository; configuration backups weekly |
| SYS-N1 field SCADA | BP-GP01, BP-GP03, BP-GP05 | Nightly SCADA backups at the POC; offline copy monthly |
| SYS-S1 client project platform | BP-ES01, BP-ES04 | Provider B snapshots every 4 hours; immutable copies in the group vault |
| SYS-G1, SYS-G2, SYS-G3 | All IT processes | Vendor multi-region services; infrastructure as code; immutable backups in provider B |
| SYS-G4 OT remote access | BP-G03 | Configuration exported daily; jump hosts rebuilt from images |
| People | All | Cross-trained operators at both control center pairs; mutual assistance agreements for crews; remote work for Engineering Services |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. Transmission operations (TCC or backup TCC)
2. Distribution switching on the DOP
3. Field area network and substation communications
4. Outage management and crew dispatch
5. Regulatory event reporting capability
6. SOC visibility
7. to 9. Gas safety alarm paths, field production control, and substation protection integrity checks
10. to 13. Group identity, WAN, cloud platform, and gas nominations
14. to 28. Outage communications, client notices, the project platform, load forecasting, OT remote access, compressor monitoring, AMI, storm engineering support, CIS, design, financial close, commissioning, royalty, payroll, and federal contract delivery.

**OT remote access is restored late on purpose (priority 18).** During an OT incident it stays off until the attacker's path is closed (P08).

## 8. Key findings
1. **Grid operations do not depend on group IT services**, which is right. The TCC and DOP run on their own OT domains, so a group identity or cloud outage does not stop switching. The dependency that crosses this line is SYS-G4, which is a security dependency rather than an availability one.
2. **The DOP's 2-hour RTO is unproven after a destructive attack.** Its backups sit on the same OT network and no full restore has been tested since 2024 (P01 EU-006; POAM-009).
3. **SYS-G4 is Moderate for availability but High for integrity and confidentiality.** Its recovery can wait; its protection cannot (P02, P04).
4. **Notification capacity is itself a process** (BP-EU10, BP-ES05, BP-G02). The P08 runbook keeps printed forms and contact lists at both control center pairs for this reason.
5. **The gas-to-power dependency is real but indirect.** Gas Production does not supply the Electric Utility directly, but a Gas Production outage in peak season affects about 30% of the Electric Utility's purchased power. Both divisions' winter and summer peak plans now name each other.

# Business Impact Analysis: Cris Santos Company Holdings | Energy | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level, with OT recovery guidance from NIST SP 800-82 Rev. 3
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-22

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, network and data centers, the OT remote access gateway, ERP, HR, and financial reporting).
- **Division BIAs:** Gas Transmission (focus), Gathering and Production, and Integrity Services. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the Gas Transmission Cybersecurity Incident Response Plan required by TSA SD Pipeline-2021-02G Section III.F, which must reduce the risk of operational disruption and of other significant impacts on business critical functions;
- the identification of Critical Cyber Systems in the TSA implementation plan (Section III.A), which include business services whose compromise could cause operational disruption;
- the emergency plans (49 CFR 192.615) and the control room management program (192.631) of Gas Transmission, and the Type C emergency plans of Gathering and Production (192.9(e)(1)(iv));
- the Integrity Data Platform availability commitments in its SOC 2 report (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity and the OT remote access gateway, SYS-G2 SOC, SYS-G3 network, data centers, and cloud, SYS-G4 ERP and HR, SYS-G5 productivity, and SYS-G6 data platform. Division systems are SYS-T1 to SYS-T6 (Gas Transmission), SYS-P1 to SYS-P4 (Gathering and Production), and SYS-E1 to SYS-E4 (Integrity Services). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Gas Transmission about $16.7 million per day, Gathering and Production about $28.5 million per day, and Integrity Services about $4.1 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (gas transportation, production, client integrity services) | One segment, field, or service line stops | Staff slowed but working |
| Regulatory | Missed PHMSA, TSA, or FERC notice; TSA directive noncompliance; SEC disclosure; reportable breach | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Plausible injury, release, or loss of gas supply to homes and power plants | Reduced safety margin that procedures cover | None |
| Reputation | National media, TSA or PHMSA enforcement attention, or loss of major clients | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 7 group shared services, 9 Gas Transmission, 6 Gathering and Production, and 5 Integrity Services. 14 are High, 12 Moderate, and 1 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-T03 Pipeline emergency response and remote valve operation | Gas Transmission | High | 1 h | 1 h | 1 h |
| BP-T07 Regulatory and customer notices | Gas Transmission | High | 1 h | 1 h | 24 h |
| BP-P02 Gathering pipeline safety monitoring and emergency response | Gathering and Production | High | 2 h | 1 h | 1 h |
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Wide-area network, data centers, and cloud landing zones | Group | High | 4 h | 2 h | 1 h |
| BP-T01 Gas control: SCADA monitoring and control | Gas Transmission | High | 4 h | 1 h | 1 h |
| BP-T02 Compressor station operations | Gas Transmission | High | 8 h | 4 h | 24 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-P01 Field SCADA well and compression control | Gathering and Production | High | 8 h | 4 h | 1 h |
| BP-E01 Integrity Data Platform service for clients | Integrity Services | High | 24 h | 4 h | 1 h |
| BP-T05 Nominations, scheduling, and informational postings | Gas Transmission | High | 24 h | 8 h | 1 h |
| BP-P03 Delivery into transmission and third-party pipelines | Gathering and Production | High | 24 h | 8 h | 4 h |
| BP-T04 Gas measurement and custody transfer | Gas Transmission | High | 36 h | 12 h | 1 h |
| BP-E02 ILI data analysis and immediate-condition reporting | Integrity Services | High | 48 h | 24 h | 4 h |
| BP-P06 Arkoma legacy field operations | Gathering and Production | Moderate | 12 h | 8 h | 24 h |
| BP-G04 OT remote access gateway | Group | Moderate | 24 h | 8 h | 24 h |
| BP-E05 Client support and incident notices | Integrity Services | Moderate | 24 h | 8 h | 4 h |
| BP-T08 Integrity management records and ILI results | Gas Transmission | Moderate | 72 h | 24 h | 24 h |
| BP-G05 ERP, supply chain, and work management | Group | Moderate | 72 h | 24 h | 4 h |
| BP-P04 Field measurement and volume allocation | Gathering and Production | Moderate | 72 h | 24 h | 4 h |
| BP-E04 Engineering project delivery and document management | Integrity Services | Moderate | 72 h | 24 h | 24 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-T09 Billing, invoicing, and imbalance settlement | Gas Transmission | Moderate | 120 h | 72 h | 24 h |
| BP-P05 Revenue distribution and royalty payments | Gathering and Production | Moderate | 120 h | 72 h | 24 h |
| BP-G06 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-E03 OT assessment engagements and evidence handling | Integrity Services | Moderate | 120 h | 72 h | 24 h |
| BP-T06 Leak-detection anomaly model (advisory) | Gas Transmission | Low | 72 h | 24 h | 24 h |

**What drives the values:**
- **Pipeline safety** drives the 1-hour values for emergency response (BP-T03) and the short MTDs for gas control (BP-T01) and gathering safety monitoring (BP-P02). Hardwired station shutdowns set a safety floor that does not depend on any computer system.
- **Firm supply to homes and power plants** drives gas control. Line pack and manual operation buy hours, not days, which is why a precautionary shutdown is limited to a segment (P08).
- **Business services the pipeline cannot run without for long** drive measurement (BP-T04) and nominations (BP-T05). Neither is needed to keep gas flowing safely in the next hour, but without them the division cannot confirm what it delivers or schedule the next gas day. This is the Colonial Pipeline lesson the TSA directives were written around, and it is the group's top risk (P01 GR-01).
- **Revenue more than time** drives production (BP-P01), royalty payments (BP-P05), and billing (BP-T09).
- **Client commitments** drive the Integrity Data Platform (BP-E01) and ILI analysis (BP-E02). Clients use them for repair and pressure reduction decisions with their own regulatory clocks.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Corporate directory (SYS-G1) | Group | Gas measurement (BP-T04), nominations (BP-T05), Integrity Services file shares (BP-E04) | A directory compromise stops the business services that keep the pipeline commercially running (gap 1). SCADA consoles do not depend on it |
| OT remote access gateway (BP-G04) | Group | Transmission and Gathering OT support; Integrity Services engineers | One gateway for three divisions (gap 3). It is a dependency for repairs and also a path for an attacker |
| SOC OT desk (BP-G02) | Group | Every division's decision to keep operating | The decision to shut down a segment turns on whether the SOC can show OT is clean |
| Gas into the transmission system (BP-P01, BP-P03) | Gathering and Production | Gas Transmission (BP-T01) | About 40% of Gathering's gas enters the Transmission system at 6 interconnects; a transmission segment shutdown forces shut-ins upstream |
| Nominations platform (BP-T05) | Gas Transmission | Gathering and Production marketing (BP-P03) | Gathering nominates on the Transmission platform like any shipper |
| Integrity Data Platform (BP-E01) | Integrity Services | Transmission integrity records (BP-T08) | Intercompany service; also holds Transmission SSI (gap 2) |
| Historian replicas (SYS-G6) | Transmission and Gathering | Group data science; leak-detection model (BP-T06) | One-way replicas; Integrity engineers' standing read access (gap 3) |
| Financial close (BP-G07) | Group | All divisions | Form 8-K materiality and SEC reporting |

**Single points of failure found:**
- **The corporate directory** for measurement and nominations (mitigation planned: move SYS-T4 into a dedicated enclave with its own identity store, POAM-007).
- **The OT remote access gateway** for all divisions (POAM-001 splits it by division).
- **Hurricane exposure of both gas control centers** (Florida and Louisiana; P01 GR-13). A regional storm can threaten both in the same week; the mitigation is a portable control capability kept in Texas and pre-staged crews.

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform and corporate directory | All business processes | Vendor multi-region service; directory replicas in both data centers; offline directory backup weekly |
| SYS-T1 SCADA hosts and historians | BP-T01, BP-T03 | Hot standby at the Backup Gas Control Center; offline SCADA backups monthly and before every change |
| SYS-T2 station control logic | BP-T02 | Logic and configuration exports stored offline after every change |
| SYS-T4 measurement system | BP-T04 | Database replication to the Louisiana data center (15 minutes); flow computers buffer about 35 days locally |
| SYS-T5 nominations platform | BP-T05 | Managed database replicas; immutable backups in the provider B vault |
| SYS-P1 field SCADA | BP-P01, BP-P02 | Backup control room at the Arkoma field office; offline backups monthly |
| SYS-P4 Arkoma legacy SCADA | BP-P06 | Backups on a local network storage device; never restored (P01 GP-004) |
| SYS-E1 Integrity Data Platform | BP-E01, BP-T08 | Warm standby in provider B; immutable daily backups |
| People | All | Cross-qualified controllers at both gas control centers; field crews qualified for manual operation |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. BP-G01 Workforce identity and access
2. BP-G03 Wide-area network, data centers, and cloud landing zones
3. BP-T01 Gas control: SCADA monitoring and control
4. BP-T03 Pipeline emergency response and remote valve operation
5. BP-P02 Gathering pipeline safety monitoring and emergency response
6. BP-T02 Compressor station operations
7. BP-G02 Security monitoring and incident response
8. BP-T07 Regulatory and customer notices
9. BP-P01 Field SCADA well and compression control
10. BP-E01 Integrity Data Platform service for clients
11. BP-T05 Nominations, scheduling, and informational postings
12. BP-P03 Delivery into transmission and third-party pipelines
13. BP-T04 Gas measurement and custody transfer
14. BP-G04 OT remote access gateway
15. BP-P06 Arkoma legacy field operations
16. BP-E05 Client support and incident notices
17. BP-E02 ILI data analysis and immediate-condition reporting
18. BP-T08 Integrity management records and ILI results
19. BP-G05 ERP, supply chain, and work management
20. BP-P04 Field measurement and volume allocation
21. BP-E04 Engineering project delivery and document management
22. BP-G07 Financial close and SEC reporting
23. BP-T06 Leak-detection anomaly model (advisory)
24. BP-T09 Billing, invoicing, and imbalance settlement
25. BP-P05 Revenue distribution and royalty payments
26. BP-G06 Payroll and HR
27. BP-E03 OT assessment engagements and evidence handling

The order puts identity and the network first because nearly every business process needs them, then pipeline safety and gas control, then the business services that keep gas commercially moving. The OT remote access gateway is restored only after the SOC confirms it is clean, because it is also a path into OT.

## 8. Key findings
1. **The pipeline can run safely without business IT; the business cannot run for long without it.** SCADA, station shutdowns, and controller sign-in do not depend on corporate systems. Measurement and nominations do, and their tested manual fallback lasts 8 hours against a 36-hour and 24-hour MTD (gap 1; POAM-006).
2. **The precautionary shutdown decision depends on one fact: can the SOC show OT is clean?** OT monitoring covers 36 of 41 compressor stations, so a decision about the other 5 takes longer (POAM-003).
3. **Shared services create shared failure.** The corporate directory and the OT remote access gateway are single points of failure for all three divisions.
4. **Integrity Services availability matters to safety outside the group.** About 160 clients rely on IDP records for repair decisions with their own regulatory clocks, which is why BP-E01 is High.

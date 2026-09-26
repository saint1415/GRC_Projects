# Scenario facts: Cris Santos Company | Energy | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (intrastate natural gas transmission pipeline operator) |
| Business | Intrastate natural gas transmission pipeline operator (NAICS 486210). Receives gas from one interstate pipeline interconnect and delivers it to local distribution companies, a power plant, and industrial plants, all in Florida |
| Location | Florida. **Headquarters and Gas Control Center** (HQ), **Compressor Station 1** (with the backup control room), and two field offices (**North** and **South**) |
| Pipeline assets | About 185 miles of steel transmission line (12 to 20 inches); 1 compressor station with 2 compressor units; 1 receipt interconnect; 14 delivery meter and regulator (M&R) stations; 8 remote-control mainline valve sites. About 40 remote terminal units (RTUs) and programmable logic controllers (PLCs) in the field |
| Customers | 2 local distribution companies (together serving about 140,000 homes and businesses), 1 municipal utility's gas-fired power plant, and 6 industrial plants. Service is under firm transportation contracts |
| Workforce | 60 employees: 8 in gas control (Gas Control Manager, 6 gas controllers, SCADA Engineer), 26 in field operations (Field Operations Manager, 6 compressor station technicians, 19 field technicians), 7 in engineering, integrity, and measurement, 4 in commercial and gas scheduling, 3 in IT, 3 in pipeline safety and compliance, 9 in executive, finance, HR, and administration |
| Revenue | $24.9 million a year in transportation revenue (fictional). Under the SBA standard of $41.5 million for NAICS 486210 (13 CFR 121.201), so SBA-small |
| Pipeline safety regulator | Intrastate pipeline. The Florida Public Service Commission (FPSC) inspects and enforces under its 49 U.S.C. 60105 certification with PHMSA. Rule 25-12.005, F.A.C., adopts 49 CFR Parts 191 and 192. The company has a control room with controllers who monitor and control the pipeline through SCADA, and a compressor station, so **all of 49 CFR 192.631** applies (the reduced-procedure exception in 192.631(a)(1)(ii) covers only transmission without a compressor station) |
| TSA status | **Not designated.** TSA has not notified the company that its pipeline system is critical, so TSA Security Directives Pipeline-2021-01G and Pipeline-2021-02G do not apply (see P03). The company confirmed on 2026-08-05 that it holds no TSA notification letter |
| Not in scope | NERC CIP (the company is not a NERC-registered entity and owns no Bulk Electric System assets); DOE Form OE-417 (electric utilities only); CEII rules (the company files no CEII with FERC); SSI under 49 CFR Part 1520 (the company holds none today; it would if TSA designated it); SEC disclosure (privately held); payment cards (customers pay by bank transfer) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: breach notification for employee personal information (Fla. Stat. 501.171) and FPSC pipeline accident notice (Rule 25-12.084, F.A.C.). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Majority owner (Cris Santos) | Accepts High and Very High risks; approves the security budget |
| President | Executive owner of the security program; accepts risk up to Moderate; signs policies; approves any precautionary shutdown decision |
| VP Operations | System owner of the Pipeline SCADA and Gas Control System; owns the operations and maintenance manual (49 CFR 192.605) and the emergency plan (192.615) |
| Gas Control Manager | Owns the control room management procedures (192.631) and the alarm management plan; relief controller; supervises the 6 gas controllers |
| SCADA Engineer | Administers the SCADA servers, HMI consoles, OT network, and field device configurations; reports to the Gas Control Manager |
| IT Manager | Security program lead (part-time security and compliance duties); runs business IT with a managed service provider; designated cybersecurity lead |
| Pipeline Safety and Compliance Manager | PHMSA and FPSC compliance; incident notices under 49 CFR Part 191 and Rule 25-12.084, F.A.C.; operator qualification and training records |
| Field Operations Manager | Field technicians, compressor station, local and manual operation of valves and compressors |
| Commercial Manager | Gas scheduling and nominations, customer contracts, customer notices |
| Finance Manager | Billing, gas accounting, cyber insurance |
| HR Manager | Onboarding, terminations, workforce records |
| Managed service provider (MSP) | Business IT help desk, patching, endpoint detection and response (EDR) monitoring, backup monitoring. No access to the OT network |
| SCADA integrator (contractor) | Supports the SCADA software and HMI displays through a remote access connection |

## 3. Systems

| ID | System | Hosting | Notes |
|---|---|---|---|
| SYS-01 | Pipeline SCADA system: redundant SCADA host servers, 3 HMI consoles, historian, engineering workstation | On-premises, Gas Control Center (HQ) | Primary system. Separate OT Windows domain with no trust to the business domain |
| SYS-02 | Backup SCADA host and backup control room | On-premises, Compressor Station 1 | Warm standby; failover tested annually (192.631(c)(4)) |
| SYS-03 | Field control devices: about 40 RTUs and PLCs, flow computers, gas chromatographs, compressor unit and station control PLCs | 14 M&R stations, 8 valve sites, receipt interconnect, compressor station | Flow computers keep about 35 days of measurement data locally |
| SYS-04 | SCADA telecommunications: licensed radio network plus cellular gateways on a carrier private network | Field | 9 sites are cellular-only |
| SYS-05 | IT/OT demilitarized zone (DMZ): firewall pair, historian replica, patch staging server, remote access jump host | On-premises, HQ | Firewalls installed 2023. The jump host serves both the SCADA integrator and the SCADA Engineer |
| SYS-06 | Business network and endpoints: HQ, field offices, compressor station office | On-premises | 62 laptops and desktops, 30 rugged field tablets |
| SYS-07 | Identity provider (single sign-on and MFA) | SaaS | Business systems and cloud console only. Not used for OT |
| SYS-08 | Productivity suite (email, files, chat) | SaaS | |
| SYS-09 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Hosts the gas measurement and accounting application, the leak-detection analytics workload (P10), and the business IT backup vault |
| SYS-10 | Business SaaS: ERP and accounting, HR and payroll | SaaS | Employee personal information |
| SYS-11 | Gas nominations and customer portal | Vendor SaaS | Customers submit daily nominations; confirmations with the upstream interstate pipeline |
| SYS-12 | Physical access control and CCTV | On-premises (HQ and Compressor Station 1) | Badge readers at HQ and the compressor station; keyed locks at field sites |
| SYS-13 | MSP remote monitoring and management (RMM) tool | MSP SaaS | Agent on every business endpoint and server |

**SSP system (P02):** the *Pipeline SCADA and Gas Control System (PSGCS)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, and the physical access control at the control rooms (SYS-12), with interfaces to the cloud tenant (SYS-09, leak-detection analytics and measurement data) and the SCADA integrator's remote access.

## 4. Current security posture: partially compliant

**In place today:**
- Firewall pair between business IT and OT with a DMZ (2023). Nothing on the business network can open a connection directly to the SCADA network
- Separate OT Windows domain, with no trust to the business domain
- MFA for email, business SaaS, the cloud console, and business VPN
- Redundant SCADA hosts and a backup control room at Compressor Station 1, failover tested in November 2025
- Written control room management procedures (2011, revised 2024): controller roles, shift handover, fatigue rules, and an alarm management plan with a monthly off-scan and inhibited-alarm review
- Controller training program with an annual tabletop on abnormal operating conditions
- Annual test of the internal communication plan for manual operation (192.631(c)(3)), last done in October 2025
- Written emergency plan (192.615) with liaison to county emergency managers
- MSP-managed EDR with 24x7 alerting on business IT endpoints (2025)
- Daily business IT backups to the cloud backup vault in a separate cloud account
- Badge access at HQ and Compressor Station 1
- Annual computer-based security awareness training for business IT users

**Missing or weak, found in the 2026 assessments:**
1. No cybersecurity risk assessment covering OT. The 2024 risk review covered business IT only.
2. No complete OT asset inventory or current network diagram. Firmware versions are unknown for about a third of field devices.
3. No cybersecurity incident response plan. The emergency plan (192.615) does not address cyber events, and there are no criteria for choosing between IT/OT isolation, manual operation, and a precautionary shutdown.
4. The SCADA integrator's remote access uses one shared account without MFA, and the connection is always on. Sessions are not logged or monitored.
5. The 3 HMI consoles use a shared Windows login. The SCADA Engineer and the integrator share one SCADA administrator account. OT passwords were last changed in 2022.
6. No OT network monitoring. Firewall and SCADA security logs are kept 30 days and nobody reviews them.
7. SCADA server backups sit on a network storage device inside the OT network. They have never been restored to new hardware, and there is no offline copy. Business IT backups are not immutable.
8. OT patching is ad hoc. The HMI consoles run an operating system version near end of support, and the SCADA software is two releases behind. There is no patch risk methodology.
9. Two SCADA display changes made by the integrator in 2026 had no point-to-point verification record (192.631(c)(2)) and did not go through change management (192.631(f)).
10. The annual verification of safety-related alarm set-points was last done in June 2024, more than 15 months ago (192.631(e)(3)).
11. Controller training does not cover cyber-caused abnormal conditions such as loss of SCADA, false data, or a forced move to manual operation.
12. Business IT accounts of departing staff are disabled 3 to 5 business days after departure. OT accounts have never been reviewed.
13. Contracts with the SCADA integrator, MSP, and telecom carrier have no security requirements or incident notice terms. No vendor SOC 2 report has been reviewed.
14. The leak-detection anomaly model sends advisory alerts to controllers without documented validation, change control, or approved-use rules (see P10).
15. Three cellular gateways at remote valve sites still use the manufacturer's default admin password (found during P07 testing).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | TSA SD Pipeline-2021-02G recorded as **not applicable** (no TSA designation) and kept as a readiness reference. Analyzed instead: 49 CFR 192.631 control room management (SCADA-relevant duties, binding) and NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary cyber benchmark) |
| P08 incident | Ransomware on business IT that forces a precautionary pipeline shutdown |
| P09 SOC 2 | The company is not a service organization. Security-only self-benchmark against the Trust Services Criteria, plus a review of the MSP's SOC 2 Type 2 report |
| P10 AI | Pipeline leak-detection anomaly model (vendor model, configured on the company's historian data) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-08-03 to 2026-08-14 | Risk assessment and gap analysis fieldwork (applicability confirmed 2026-08-05) |
| 2026-08-24 to 2026-08-28 | Control assessment fieldwork (Compressor Station 1 and two valve sites visited 2026-08-26) |
| 2026-09-24 | Deliverables approved by the President (High risks by the majority owner) |

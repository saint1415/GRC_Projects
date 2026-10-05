# SOC 2 Readiness Summary: Cris Santos Company | Dams | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (Hydro Services: Remote Monitoring and Operations Services, RMOS) |
| Tier / Vertical | Mid-Market / Dams |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1) |
| Target report | SOC 2 **Type 2** on the RMOS service, observation period 2027-04-01 to 2027-09-30 (6 months), report by 2027-11-30; Type 1 by 2027-03-31 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-17 by the GRC Manager with the vCISO and the OT Security Manager, using P02, P05, and P07 evidence |

## 1. Why SOC 2 for this organization
A hydroelectric generator is not usually a SOC 2 service organization: it sells power, not services to other businesses. **RMOS changes that.** The ROC monitors 6 small hydro projects owned by 4 client licensees and operates units and gates at 4 of them under written operating orders. The clients' own dam safety, generation, and FERC reporting depend on the company's controls. Client contracts renewing in 2027 require a SOC 2 Type 2 report.

**Categories chosen.**
- **Security:** always required.
- **Availability:** clients depend on the ROC to watch alarms and run gates around the clock.
- **Confidentiality:** client control details, instrument data, and inundation maps are confidential, and some are CEII.
- **Processing Integrity:** the service executes client operating orders and produces monthly operations and dam safety instrument reports that clients rely on, including for their own 18 CFR 12.10 decisions. Clients asked for it.
- **Privacy:** not in scope; the service handles operational data, not personal information about data subjects.

**Why Type 2, and why not now.** P07 found gaps in exactly the areas a Type 2 tests over time: client tunnels in the SCADA zone, OEM access, access reviews, recovery testing, and vendor terms. An observation period starting now would produce exceptions. The plan is to remediate through 2027 Q1, issue a Type 1 report on 2027-03-31 as an interim deliverable, and run the Type 2 period from 2027-04-01.

**Alternatives considered:** a security questionnaire only (rejected by 3 of 4 clients); a bridge from the annual internal audit (not acceptable: the co-sourced firm is not independent of management for this purpose); ISA/IEC 62443 certification of the ROC (useful later, but clients asked for SOC 2).

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | RMOS: 24x7 monitoring of 6 client projects; operation of units and gates at 4 projects under written operating orders; alarm relay; monthly operations and dam safety instrument reports; the client portal |
| Infrastructure | ROC SCADA (SYS-01) and the client tunnels (SYS-06) within the HCDMS (P02); the planned RMOS zone; the OT DMZ; the cloud OT data and analytics account and the Hydro Services client portal account (P04); the identity provider |
| Software | SCADA platform; historian; data platform and portal application; identity provider; SIEM |
| People | RMOS desk (22), ROC operators (36), OT security team, controls engineering, IT, MSSP |
| Data | Client telemetry, alarms, operating orders, instrument data, reports, client inundation maps |
| Procedures | POL-01 to POL-05; standards index; operating orders; P08 runbooks |
| Subservice organizations (carve-out) | Cloud infrastructure provider, identity provider, MSSP and its SIEM platform, SCADA platform vendor (support). Their controls are covered by their own SOC 2 reports and listed as complementary subservice organization controls |
| Complementary user entity controls (clients) | Clients keep local control capability and staff to take over under the operating orders; approve their portal users; notify the RMOS desk of changes at their sites; secure their own site networks up to the tunnel endpoint |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 14 | 14 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **18** | **19** | **6** | **18** |

**Ready (18):** CC1.1, CC1.3, CC1.5, CC2.2, CC3.2, CC4.1, CC4.2, CC5.1, CC6.2, CC6.4, CC6.5, CC6.7, CC6.8, CC7.3, A1.1, PI1.2, PI1.4, PI1.5.

**Not ready (6):**
- CC2.3: No client security schedule; 2 of 4 operating orders lack handback times; no commitment on incident notice
- CC6.1: RMOS client tunnels share the ROC SCADA zone; OEM VPNs bypass the jump hosts
- CC6.3: Annual OT reviews; 3 of 25 leavers late; shared accounts at PNH and SGR
- CC7.5: ROC SCADA cyber recovery unproven; portal rebuild untested
- CC9.2: OEMs untiered; 9 of 14 OT contracts lack security terms
- A1.3: No ROC SCADA or portal recovery test

Each Not ready criterion maps to a P07 POA&M item. Most Partially ready criteria depend on standards being issued (P06), client contract terms (POAM-009), and six months of operating evidence for new controls.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (RMOS availability commitments, BP-08 and BP-09), P06 (policies), P07 (test results), and P08 (incident and client notice procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.1, CC3.4, CC6.3, CC8.1, C1.1, PI1.3 | Inventory and connection register; security review records for client changes; quarterly access review sign-offs; change board minutes with security reviewer; dataset tags; updated operating orders |
| 2027 Q1 | CC1.2, CC1.4, CC2.3, CC3.1, CC3.3, CC5.2, CC5.3, CC6.1, CC6.6, CC7.1, CC7.2, CC7.4, CC9.1, CC9.2, A1.3, C1.2, PI1.1 | Client security schedules signed; RMOS zone live; standards issued; portal penetration test; handback drills; tabletop reports; portal rebuild test; OEM amendments |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to clients | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence (quarterly reviews, weekly vendor session reviews, monthly reports QA, restore tests, vendor reviews) |
| 2027 Q2 | CC7.5, A1.2 | ROC SCADA cyber recovery test; isolated recovery environment |

**Status reporting.** The Vice President of Hydro Services reports readiness monthly to the COO and quarterly to the audit committee and to the 4 clients.

## 5. Vendor SOC 2 review program (Part B)
The HCDMS relies on vendor controls for 25 Hybrid controls in P02, and the RMOS report will carve out 4 subservice organizations. `vendor-soc2-review.csv` makes that reliance evidence-based and is the core of STD-03.

| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Remote access to OT, holds settings or data needed for recovery, or supports a High-criticality BIA process | SOC 2 Type 2 (or equivalent) plus bridge letter, or a security questionnaire and contract security schedule where no report exists; review of scope, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Confidential data, no OT access, Moderate or Low processes | Questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No sensitive data and no system access | Contract terms only | At renewal |

The CSV holds 8 reviews (7 Tier 1, 1 Tier 2). The other 10 of the 14 OT vendors are reviewed by 2027-03-31 (POAM-009).

**Key findings:**
1. **The two OEMs with direct VPNs have no assurance at all** (VEN-04, VEN-05): no SOC 2, no questionnaire or an incomplete one, no security terms, and they hold the only copies of 5 governor settings. One installed the undocumented modem at Sawgrass Run. These are the highest-risk vendors the company has (P01 R-001, R-010).
2. **MSSP:** unqualified Type 2 with an escalation exception (2 of 40 samples). The company's own CUEC (log sources) is incomplete for OT.
3. **SCADA platform vendor:** unqualified Type 2; incident notice is 72 hours, longer than the company's 24-hour target for clients. Seek a shorter term at renewal.
4. **Identity provider:** unqualified, but its outage would remove jump host MFA (P05 finding 5); the company compensates with a break-glass path.
5. **HR and payroll SaaS:** breach notice term of 15 days exceeds the 10 days Florida requires of third-party agents (Fla. Stat. 501.171(6)); amend at renewal.

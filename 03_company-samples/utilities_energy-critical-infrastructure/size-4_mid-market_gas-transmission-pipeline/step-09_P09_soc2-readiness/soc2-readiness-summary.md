# SOC 2 Readiness Summary: Cris Santos Company | Energy | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed interstate natural gas transmission pipeline operator) |
| Tier / Vertical | Mid-Market / Energy |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short labels only; the criteria text is in the AICPA publication |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1). Privacy is out of scope |
| Target report | SOC 2 **Type 1** as of 2027-03-31 (interim), then **Type 2** for the observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-12-15 |
| Part A | Company readiness for the contract operations services (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-17 by the vCISO and the GRC lead, with the Director of Gas Control and the VP Commercial, using P02, P05, P06, and P07 evidence. Approved by the Chief Operating Officer the same day |

## 1. Why SOC 2 (or an alternative) for this organization
For its main business, interstate transportation of gas, the company is not a typical SOC 2 service organization. Its assurance to regulators and shippers comes from other mechanisms:
- **TSA compliance reviews** of the Cybersecurity Implementation Plan and the annual Cybersecurity Assessment Plan report (SD Pipeline-2021-02G; C-ENERGY-R03). This is the assurance alternative named for this vertical, and it already covers the company's Critical Cyber Systems;
- **PHMSA inspections** of control room management (49 CFR 192.631; C-ENERGY-R04);
- **FERC** tariff and posting oversight.

None of these gives a report a customer can rely on. That matters for one line of business: the **contract operations services**. Under operations services agreements (OSAs), the Gas Control Center monitors and controls a 60-mile intrastate lateral owned by a municipal gas utility and a 35-mile lateral owned by a power generator, for about $3 million a year. For those two customers the company **is** a service organization: their pipeline safety and supply depend on the company's SCADA, controllers, and security. Both owners asked for a SOC 2 Type 2 report by 2027. Their auditors want assurance over:
- **Security:** who can reach the SCADA that controls their laterals;
- **Availability:** whether monitoring and control continue through an outage (the OSAs require notice within 30 minutes of lost monitoring and pay service credits after 4 hours);
- **Processing Integrity:** whether alarms, commands, and daily reports for their laterals are complete, accurate, and timely;
- **Confidentiality:** whether their operating data and lateral configurations are protected.

**Privacy** is out of scope because the service processes no personal information.

**Why Type 1 first, then Type 2.** A Type 2 report tests whether controls operated over a period. P07 found gaps in access removal, boundary protection (the OEM modem), vulnerability management, recovery testing, and vendor oversight. Starting the observation period before those are fixed would produce exceptions or a qualified opinion. Both lateral owners accepted this plan with quarterly status updates.

**Alternatives considered:**
- **Share the TSA results:** not possible. The TSA plans, assessment results, and reports are SSI (49 CFR Part 1520) and cannot be shared with the lateral owners.
- **Security questionnaire only:** offered for 2026, but not accepted for 2027 by the power generator's auditors.
- **Agreed-upon procedures report:** cheaper, but gives no opinion and would need repeating for each owner.

**Service auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the internal audit work in P07 does not raise an independence question. Budget: $180,000 across 2027 (P01 treatment summary).

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Monitoring and control of the two operated laterals from the GCC (and the BCC on failover); alarm response under the owners' procedures; 30-minute outage notices; daily operating reports and alarm summaries |
| Infrastructure | SYS-01 primary SCADA at the GCC; SYS-02 BCC; SYS-03 field devices on the two laterals; SYS-05 SCADA telecommunications serving the laterals; SYS-06 IT/OT DMZ and remote access gateway; SYS-07 OT monitoring at the GCC and BCC; physical access control at the GCC and BCC (part of SYS-14) |
| Software | SCADA platform and historian; identity provider (SYS-09) for remote access; SIEM and EDR (SYS-15) |
| People | 28 controllers and 5 shift supervisors; SCADA and OT engineering; OT Security Engineers; the Security Manager; the MSSP |
| Data | Lateral SCADA data (pressures, flows, alarms, valve states), lateral configurations, operating reports |
| Procedures | POL-01 to POL-05; the standards index; control room management procedures; the P08 runbooks |
| Not in scope | Compressor stations (SYS-04) serve only the company's mainline. They are outside the system boundary, but the shared SCADA network means their weaknesses (the OEM modem) still affect CC6.6 |
| Subservice organizations (carve-out) | MSSP, identity provider, telecom carrier, SCADA software vendor. Their controls are covered by their own reports and the complementary subservice organization controls in the system description (Part B) |

**Complementary user entity controls (lateral owners).** Each owner keeps its lateral's emergency response, makes its own regulatory notices, approves alarm limits and procedures for its lateral, and keeps its contact list current.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 17 | 5 | 0 |
| Availability (A1, 3) | 1 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **15** | **23** | **5** | **18** |

**Ready (15):**
- governance and risk: CC1.1, CC1.2, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2;
- monitoring and control design: CC4.2, CC5.1;
- access and event handling: CC6.2, CC7.3;
- capacity: A1.1;
- processing: PI1.3, PI1.4, PI1.5 (alarm management under 192.631(e), daily reports, historian retention).

**Not ready (5):**
- **CC6.3:** OT access removal takes 5 business days on average, reviews are annual, and there are 9 OT domain administrators (POAM-001, POAM-002);
- **CC6.6:** the OEM cellular modem bypassed the DMZ into the shared SCADA network (POAM-003, Very High);
- **CC7.1:** 6 CISA KEV entries on OT components are past the mitigation timeline (POAM-012);
- **CC7.5:** a full SCADA rebuild has not been tested (POAM-009);
- **CC9.2:** 10 of 14 Tier 1 vendors have not been assessed, including two subservice organizations for this service (POAM-013).

The Partially ready criteria mostly depend on issuing the draft standards (P06), extending OT monitoring (POAM-014), and writing the system description and service commitments that the OSAs now spread across contract schedules (CC2.3, PI1.1).

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (MTDs and RTOs for BP-04), P06 (policies and standards), P07 (test results), and P08 (incident procedures and lateral owner notices). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC). No SSI is used as SOC 2 evidence; where a control is described in the TSA plans, the evidence is the underlying record (for example, the firewall rule export), not the plan.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.4, CC6.6, CC3.4, CC8.1, PI1.2, C1.1, CC4.1 | Rekey records; OEM survey and DMZ data path; MOC forms with the TSA question; change tool approvals with P2P records; data loss rule reports; TSA annual report submission (2026-11-20) |
| 2026 Q4 | CC6.3, CC7.1, CC7.4, CC7.5, CC9.1, A1.2, A1.3, CC2.3, PI1.1, C1.2 | Same-day removal tickets; first quarterly OT access review; KEV backlog closure; 2026-11-17 exercise report; rebuild test record; PLC logic hashes; system description draft with service commitments and exit terms |
| 2027 Q1 | CC1.4, CC2.1, CC3.3, CC5.2, CC5.3, CC6.1, CC6.5, CC7.2, CC9.2 | Station technician training; reconciled inventory; fraud scenario in the risk assessment; issued standards; field device resets (lateral devices first); sensors at the 3 remaining stations; all Tier 1 vendor reviews |
| 2027-03-31 | Type 1 report as an interim deliverable to both lateral owners | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence: quarterly access reviews, monthly KEV reviews, MSSP reports, OSA notices, daily reports, change records, vendor reviews |
| 2027 Q2 to Q4 | CC6.8, CC6.7 | Station HMI replacement (2027-06-30); microwave encryption at the 2027 refresh. Station HMIs are outside the system boundary, so neither should create a Type 2 exception for the laterals, but both are disclosed |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee and to both lateral owners.

## 5. Vendor SOC 2 review program (Part B)
The PSGCS inherits or shares many controls with suppliers (P02, P04), and the TSA directive keeps the company responsible for plan measures that a managed security service provider or an authorized representative performs (SD 02G II.A.3 and II.A.4). The program in `vendor-soc2-review.csv` makes that reliance evidence-based. It is the core of the supplier risk management standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | OT access, Restricted or SSI data, or support for a High-criticality BIA process | SOC 2 Type 2 (or an equivalent independent assessment, or an on-site assessment where no report exists) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability against the BIA, and incident terms | Annually |
| **Tier 2** | Confidential data or business system access, no OT access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No data and no system access | Contract terms only | At contract renewal |

Of the 85 vendors with system or data access, 14 are Tier 1. The CSV holds 9 Tier 1 entries: the 4 reports already on file, re-reviewed in the program format in September 2026 (MSSP, identity provider, cloud provider, productivity suite), and the 5 most critical vendors without a reviewed report (SCADA software vendor, customer activities website vendor, compressor OEM, telecom carrier, leak-detection model vendor). The remaining 5 Tier 1 reviews (including the SCADA integrator and the remote access gateway vendor) are due by 2027-03-31 (POAM-013).

**Key findings:**
1. **The SCADA software vendor has no SOC 2 report** and holds copies of the company's SCADA configurations. An on-site assessment of its support environment is scheduled for 2026-12-08, and breach notice terms are required at renewal (P01 R-012, R-048).
2. **The compressor OEM has no security terms at all**, and its modem bypassed the DMZ. Contract terms and the DMZ data path are due 2026-10-31 (POAM-003).
3. **The MSSP report is unqualified but shows missed escalations** in 2 of 40 samples, and its SIEM platform is carved out. The company's own CUECs (log sources, retention) are open gaps, so the MSSP's controls only protect the company once POAM-005 and POAM-014 close.
4. **Two subservice organizations for the contract operations services (the telecom carrier and the SCADA software vendor) have no report yet.** Both are needed before the Type 1 date.
5. **The customer activities website vendor** has no breach notice term, and its report is expected in 2026 Q4 (P01 R-019, R-020).

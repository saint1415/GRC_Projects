# SOC 2 Readiness Summary: Cris Santos Company | Water and Wastewater Systems | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed investor-owned water utility) |
| Tier / Vertical | Mid-Market / Water and Wastewater Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| Service in scope | **Utility Services**: contract operations, after-hours remote monitoring, and billing and customer service for 3 municipal water systems |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-15 by the vCISO, the Security Manager, and the Director of Utility Services (SOC 2 sponsor), using P02, P05, P06, and P07 evidence |

## 1. Why SOC 2 for this organization
A water utility is not usually a SOC 2 service organization: it serves the public, and its regulators are EPA and the state, not customers' auditors. Utility Services changes that. For the 3 municipal clients, the company:
- monitors their plants from the ROC after hours (read-only), acknowledges alarms within 15 minutes, and calls out their on-call staff;
- bills 15,600 of their customer accounts in the company CIS and runs customer service in each client's name;
- supplies 24 licensed operators who work at the clients' plants.

Those services affect the clients' own operations and their customers' data, and each client contract requires an annual SOC 2 Type 2 report starting with the 2027 renewals (`../00_company-facts.md` section 7). The clients asked for **Security, Availability, Processing Integrity** (billing accuracy and timeliness), and **Confidentiality** (client and customer data). They did not ask for Privacy; privacy notices to their customers stay with the clients.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated over a period. P07 found gaps in access reviews, OT recovery, vendor oversight, and monitoring that would produce exceptions today. The plan is to remediate through 2027 Q1 and start a 6-month observation period on 2027-04-01. Each client has agreed to accept this plan with quarterly status updates.

**Alternatives considered:**
- **Type 1 first (point in time, 2027-03-31):** offered to the clients as an interim deliverable. Two of three said they will use it at renewal.
- **Client audits instead of SOC 2:** rejected by the clients, which want one independent report.
- **Questionnaire only:** not acceptable under the contracts.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the P07 work does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | After-hours remote monitoring and alarm response; billing, payments, and customer service for client accounts; contract operator staffing (personnel controls only) |
| Infrastructure | ROC monitoring stations and the 3 client read-only links (part of the IWOS, P02); the business network and endpoints used by customer service and billing; the identity provider; the cloud landing zone for file services |
| Software | CIS with portal, IVR, and virtual agent; identity provider; productivity suite; SIEM and EDR (through the MSSP) |
| People | ROC operators (22), customer service and billing staff serving clients (about 20), the 24 contract operators, IT and security, the Director of Utility Services |
| Data | Client customer personal information and billing data; client plant alarm and process values (read-only) |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks, ROC alarm procedures, billing cycle procedures |
| Subservice organizations (carve-out) | CIS vendor, identity provider, cloud provider, MSSP and its SIEM platform, payment processor, bill print-and-mail vendor. Their controls are covered by their own reports and the complementary subservice organization controls in the system description |
| Excluded | The company's own water operations and its SDWA obligations; the clients' plants and SCADA systems |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 15 | 14 | 4 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **19** | **19** | **5** | **18** |

**Ready (19):**
- governance and risk: CC1.1, CC1.2, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2;
- monitoring and control design: CC4.1, CC4.2, CC5.1;
- access, physical, disposal, transmission, and malware: CC6.2, CC6.4, CC6.5, CC6.7, CC6.8;
- capacity, disposal, inputs, and storage: A1.1, C1.2, PI1.2, PI1.5.

**Not ready (5):**
- CC6.3: quarterly access reviews and removal of OT local accounts (POAM-003);
- CC7.1: vulnerability and configuration monitoring, including OT (POAM-013);
- CC7.5 and A1.3: no tested restore of company CIS data and no alternate ROC position for client monitoring (POAM-018);
- CC9.2: vendor reviews only at onboarding until this cycle (POAM-014).

The Partially ready criteria mostly depend on standards being issued (P06), on the system description and client responsibilities schedule (CC2.3), and on the OT segmentation work that also protects the ROC's client links (CC6.6).

**Why the IWOS findings matter to clients.** Client monitoring runs on the ROC network, which the March 2026 tunnels connected to Lakes and Ridge with any-to-any rules. Until POAM-001 and POAM-002 close, a compromise at an acquired plant could reach the stations that watch the clients' plants (CC6.6). That is why the SOC 2 plan depends on the same OT roadmap as the RRAs.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments: BP-09 alarm acknowledgment within 15 minutes and BP-12 client billing), P06 (policies), P07 (test results), and P08 (incident procedures and 24-hour client notice). The `related_sp800_53` column links each criterion to SP 800-53 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.1, CC3.4, CC6.3, CC6.6, CC7.1, CC7.2, CC7.3, C1.1, PI1.3, PI1.4 | Reconciled component list; STD-07; quarterly access review sign-offs; tunnel rule sets; exposure scan reports; MSSP OT escalation tests; client data export inventory; signed reconciliations and print release checklists |
| 2027 Q1 | CC1.4, CC2.3, CC3.3, CC5.2, CC5.3, CC6.1, CC7.4, CC8.1, PI1.1 | Operator training records; system description and client responsibilities schedule; billing fraud scenarios; issued standards; privileged access management logs; tabletop reports; second-reviewer change tickets |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to the clients | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | Recurring evidence: quarterly access reviews, monthly vulnerability reports, alarm acknowledgment statistics, billing cycle reconciliations, vendor reviews |
| 2027 Q2 | CC7.5, CC9.1, CC9.2, A1.2, A1.3 | Alternate ROC position installed and failover tested; CIS data restore test; remaining Tier 1 vendor reviews |

**Timing risk.** CC7.5, CC9.1, A1.2, and A1.3 depend on the alternate ROC position (due 2027-06-30), and CC9.2 on the remaining Tier 1 vendor reviews (due 2027-06-30). Both fall inside the observation period. If they slip, the report will show exceptions for those criteria. The Director of Water Operations reports its status monthly to the SOC 2 sponsor.

**Status reporting.** The Director of Utility Services reports readiness monthly to the COO, and quarterly to the audit committee and the 3 clients.

## 5. Vendor SOC 2 review program (Part B)
The IWOS relies on vendors for many controls (P02: 21 Common/Inherited and 19 Hybrid), and the CIS is a subservice organization for Utility Services. `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of the vendor standard (STD-08).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Remote access to OT, customer or client data at scale, or support for a High-criticality BIA process | SOC 2 Type 2 plus bridge letter (or, where no report exists, a questionnaire, contract terms, and an on-site assessment); review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No data and no system access | Contract terms only | At contract renewal |

About 40 vendors are Tier 1 or Tier 2 under this approach, including all 14 OT vendors with remote access. The CSV holds the first 10 Tier 1 reviews and 1 Tier 2 example. The remaining Tier 1 reviews (the other OT vendors, the GIS vendor, whose report has been requested, and the print-and-mail vendor) are due by 2027-06-30 (POAM-014).

**Key findings:**
1. **Integrator B (VEN-09)** has no report, no security terms, and no response-time commitment, and it holds standing access to 2 covered systems. It is the single largest third-party risk in the program (P01 R-001, R-008, R-013).
2. **CIS vendor (VEN-04):** unqualified Type 2 covering all four categories the clients asked for. Its RTO and RPO meet the BIA. Two of the CUECs the company must operate are open gaps: quarterly access reviews (POAM-003) and bulk-export review and alerting (POAM-023). **The vendor's controls protect client data only once those gaps close.**
3. **MSSP (VEN-02):** unqualified Security-only report with a 30-minute escalation exception in 2 of 40 samples, and no OT escalation path to the ROC. The SIEM platform is carved out, and its own report is needed.
4. **AMI vendor (VEN-05):** qualified opinion for change management, and the contract has no breach notice term. Follow-up is due 2027-03-31.
5. **LIMS vendor (VEN-06):** its 24-hour RTO is longer than the BIA's 8 hours for BP-07; the laboratory's manual fallback covers the gap for now.

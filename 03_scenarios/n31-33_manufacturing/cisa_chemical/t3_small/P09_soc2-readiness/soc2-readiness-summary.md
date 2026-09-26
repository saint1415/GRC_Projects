# SOC 2 Readiness Summary: Cris Santos Company | Chemical | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical formulator and packager) |
| Tier / Vertical | Small / Chemical |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security only (CC1-CC9, 33 criteria) |
| Target report | None. This is a self-benchmark, not a CPA examination. No Type 1 or Type 2 report is planned |
| Part A | Company Security self-benchmark (`soc2-readiness.csv`) |
| Part B | ERP vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 by the IT Manager with the Controller and the Customer Service Manager |

## 1. Why SOC 2 (or an alternative) for this organization
**The company is not a SOC 2 service organization.** It blends, packages, and ships chemical products. It does not operate systems or process data on behalf of its customers. Customers receive drums, totes, and tanker loads, not an IT service. A SOC 2 examination reports on a service organization's system as it relates to its customers, so a SOC 2 report is not the right product here. The vertical registry lists no chemical-sector alternative (such as an industry certification) for this purpose.

SOC 2 still matters for two reasons:

**A. Customer questionnaire (self-benchmark).** In 2026 the largest private-label customer (about 18% of revenue) sent a supplier security questionnaire. It asked how the company protects the customer's private-label formulations and order data and how it would keep supply going after a cyber incident. The customer accepted a Security-only self-assessment against the Trust Services Criteria as its format, along with the remediation plan. This keeps the answer in a standard structure without the cost of an examination.
- **Scope:** Security (CC1-CC9) only.
- **Availability and Confidentiality** were considered and left out because the customer did not ask for them. Supply continuity is covered by the BIA (P05), and formulations by the supply agreement and POL-04.
- **Processing Integrity and Privacy** do not apply.

**B. Third-party risk management (vendor report review).** The ERP is a critical business system: it holds orders, inventory (including hydrogen peroxide), and bills of materials. The ERP vendor is a service organization, and its SOC 2 Type 2 report is the evidence for the controls the company inherits (P02, P04). The report had never been reviewed before this project (gap 14). It is now reviewed every year (POL-01 4.8; SA-9).

## 2. System description (scope)
- **Services:** manufacture, packaging, and delivery of specialty chemical products, including private-label and toll blending for about 600 business customers.
- **Infrastructure and software:** the PCBMS (SSP, P02); the cloud tenant and SaaS services (P04); office endpoints; the physical security systems.
- **People:** 162 employees, the DCS integrator, and the data science contractor.
- **Data:** customer orders and private-label formulations, master recipes, process data, QC results and certificates of analysis, and employee personal information.
- **Procedures:** POL-01 to POL-05, the MOC procedure, the RMP operating procedures, and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 21 | 8 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready (4):**
- CC1.3: roles and reporting lines are set in POL-01
- CC3.1 and CC3.2: objectives are set, and the 2026 risk assessment is done
- CC4.2: deficiencies are tracked in the POA&M

**Not ready (8):**
- CC3.4 and CC8.1: control system and recipe changes are outside MOC
- CC6.3: OT accounts are outside the leaver process and are never reviewed
- CC6.6: always-on integrator remote access, broad firewall rules, and a dual-homed historian
- CC6.8: no malware protection on OT workstations
- CC7.1 and CC7.2: no OT vulnerability management or monitoring
- CC7.5: DCS recovery is unproven

The pattern matches the P03 gap analysis. Office IT and SaaS are in reasonable shape, and the gaps sit in OT. **What this means for the customer:** its formulations sit in the batch management system and the ERP. The ERP is well controlled by its vendor. The batch management system is reachable through the weaknesses above until POAM-001 and POAM-002 close.

## 4. Findings from the ERP vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. Two exceptions (one unapproved change, one late access review), both remediated.
- **Availability:** the vendor states an RTO of 8 hours and an RPO of 1 hour. That **meets the BIA** for BP-07 (RTO 8 h, RPO 1 h). BP-08 inventory accountability also relies on this RPO.
- **Controls the company must run (CUECs).** Three are open gaps at the company:
  - ERP role review and separation of duties for hydrogen peroxide adjustments (R-011)
  - review of ERP administrator activity (POAM-017)
  - rotation of the order interface API credential

  **The vendor's controls protect the company only when these are in place.**
- **Follow-ups:**
  - Obtain a bridge letter by 2026-10-31.
  - Request the vendor's summary of how it monitors its carved-out hosting provider.
  - Add a 24-hour incident notice clause at contract renewal.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.6 (remote access), CC6.3, CC3.4, CC8.1, CC2.2, CC7.4 | Gateway session recordings and approvals, termination checklists with OT items, MOC records for control changes, policy acknowledgments, tabletop report |
| 2027 Q1 | CC6.6 (OT DMZ), CC7.2, CC7.5, CC6.8, CC1.4, CC9.2 | Firewall rule reviews, sensor alerts and tickets, restore test records, OT training roster, signed vendor security addenda |
| 2027 Q2-Q4 | CC7.1, CC5.2, CC4.1 | Patch cycle records, baseline compare reports, the August 2027 assessment |

**Response to the customer (sent 2026-09-08):** this summary, the Security checklist, and a POA&M extract (P07) limited to items affecting formulation data and supply continuity. The company committed to an updated self-assessment in April 2027.

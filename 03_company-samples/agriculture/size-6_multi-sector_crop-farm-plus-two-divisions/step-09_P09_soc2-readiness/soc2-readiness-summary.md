# SOC 2 Readiness Summary: Cris Santos Company Holdings | Agriculture | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Agriculture, Forestry, Fishing and Hunting |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: the Farm Supply **Grower Agronomy Portal** (`soc2-readiness.csv`). Crop Farming and Food Processing are out of scope, with reasons. A review of the FMIS vendor's SOC 2 report is in `vendor-soc2-review.csv` |
| Categories in scope (portal) | Security, Availability, Confidentiality |
| Target report (portal) | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the Farm Supply security and compliance lead and the portal general manager |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. For each division and service line the question is whether other organizations rely on the group's controls as part of their own.

| Division | Service line | Service organization? | Decision | Assurance instead |
|---|---|---|---|---|
| Farm Supply | Grower Agronomy Portal (SYS-D5): about 8,200 grower accounts, resold under their own brand by 22 cooperatives to about 5,400 growers | **Yes.** Cooperatives resell it and growers rely on it to hold field data and produce prescriptions; cooperatives asked for a Type 2 report | **In scope.** First readiness assessment | n/a |
| Farm Supply | Branch and e-commerce sales of inputs | No. Customers buy products, not an outsourced service | Out of scope | Annual PCI DSS report on compliance for card data (P03) |
| Crop Farming | Produce and peanuts sold to buyers and to Food Processing | No. Buyers buy product; they do not build controls on Crop Farming systems | **Out of scope** | Buyer agreements, third-party food safety (GAP) audits, and FDA Produce Safety inspections. Crop Farming is a **user entity** of the FMIS vendor; its report is reviewed (section 5) |
| Food Processing | Packed, frozen, and peanut products for retail, foodservice, and USDA programs | No. Customers buy food, and their assurance needs are about food safety | **Out of scope** | Annual third-party food safety certification audits, FDA inspection under 21 CFR 117 and 121, and FAR clauses in USDA contracts |
| Corporate shared services | Identity, SOC, cloud, ERP for the divisions | Internal service, not to outside user entities | Carved in to the portal report as internal shared services | Common control assessment (P07) |

**Why Crop Farming and Food Processing are out of scope:**
1. **No user entities.** Their customers buy farm products and food. No customer runs part of its own control environment on Crop Farming or Food Processing systems.
2. **Their customers ask for food safety assurance, not system assurance.** Buyer and customer contracts require food safety certification audits and 24-hour notices (P03), which the group already provides.
3. **Revisit triggers:** if Crop Farming offers farm management or irrigation services to outside growers, or if Food Processing hosts traceability data for outside growers, assess whether a SOC 2 report is needed.

**Other assurance options considered.** The vertical overlay names no other standard assurance mechanism for agriculture. Cooperatives accept security questionnaires today, but each asks different questions; a SOC 2 report answers them once.

## 2. System description (portal scope)
- **Services:** field boundaries, soil tests, yield maps, variable-rate prescriptions (including AI prescriptions since 2026-03-01), application records, and grower contact data for about 8,200 grower accounts; white-label service for 22 cooperatives.
- **Infrastructure and software:** SYS-D5 on cloud provider B (managed containers and databases across zones); group identity (SYS-G1), SOC (SYS-G2), and landing-zone controls (SYS-G3) carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud provider B; the customer identity vendor used for grower and cooperative sign-in.
- **People:** the portal engineering, agronomy, and support teams in Farm Supply, plus group SOC and identity teams.
- **Data:** grower field and agronomic data and grower contact data (Confidential under POL-04). No card data and no Social Security numbers.
- **Complementary user entity controls (to be defined):** cooperatives provision and remove their staff and grower users, require MFA for their administrators, and review the access reports the portal provides.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 22 | 9 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |

**Why so many criteria are Ready for a first report:** control environment, risk governance, identity, monitoring, and incident response criteria are met by group common controls that P07 assessed once (most were satisfied). The portal's gaps are its own.

**Not ready:** CC2.3, CC8.1. There is no system description and no communication to cooperatives about the AI prescription feature or its use of grower data, and the AI feature launched without the change controls CC8.1 expects (P07 CM-4 and SA-11 findings).

**Partially ready:** CC2.1, CC3.2, CC3.4, CC4.1, CC5.3, CC6.2, CC6.6, CC7.4, CC9.2, A1.3, C1.1, C1.2. Most are about the AI feature's data use (CC2.1, C1.1), assessing changes (CC3.2, CC3.4), cooperative-facing controls (CC6.2, CC6.6, CC7.4, CC9.2), and evidence that has not yet operated for a period (CC4.1, CC5.3, A1.3, C1.2).

**Processing Integrity is out of scope today** because the portal makes no processing integrity commitments. It is under evaluation for 2028: prescriptions drive application rates on growers' equipment, and the Group AI council rated the AI prescription feature High (P10). If the portal starts promising prescription accuracy, PI1 would follow.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC3.2, CC3.4, CC8.1, C1.1 | Retroactive review of the AI feature; release gate records; data-use review and terms decision (POAM-019) |
| 2026 Q4 | CC7.4 | Cooperative notice register; tabletop record (2026-12-15) |
| 2027 Q1 | CC2.1, CC2.3, CC4.1, CC5.3, CC6.2, A1.3 | Data map with training data; system description and cooperative notices; quarterly control self-test; runbooks; complementary user entity controls; DR test. **Type 1 as of 2027-03-31** |
| 2027 Q1 to Q2 | CC6.6, C1.2, CC9.2 | MFA required for cooperative administrators; automated deletion certificates; reseller agreement terms at renewal |
| 2027 Q2 to Q3 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30) |

**Communication:** the portal general manager sends the 22 cooperatives a readiness letter with this timeline and the AI feature disclosure in 2026 Q4 (before the Type 1 date).

## 5. FMIS vendor report review (Crop Farming as a user entity)
Crop Farming relies on the FMIS vendor for its system of record (P02). `vendor-soc2-review.csv` records the 2026 review of the vendor's SOC 2 Type 2 report. Key points:
- The report has an unmodified opinion, covers Security and Availability, and has one change-approval exception the vendor has fixed.
- The **device connectivity service** that carries irrigation commands toward ROC SCADA is carved out to a subservice organization. That path is a control path into OT, so the group asked for the vendor's own review of that provider.
- **Five of six complementary user entity control areas are open gaps in Crop Farming** (account removal, MFA and named accounts, audit trail review, and network protection of the SCADA gateway). The vendor's controls work only if the group runs these, so the gaps are carried in the POA&M (POAM-002, POAM-005, POAM-011).
- The vendor's 8-hour RTO does not meet the 2-hour freeze-season RTO for irrigation (P05), which is why ROC SCADA, not the FMIS, must keep irrigation running.

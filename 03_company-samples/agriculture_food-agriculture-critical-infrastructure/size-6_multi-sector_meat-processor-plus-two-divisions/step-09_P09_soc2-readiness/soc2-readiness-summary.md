# SOC 2 Readiness Summary: Cris Santos Company Holdings | Food and Agriculture | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Meat Processing, Food Distribution, Grocery Retail, corporate shared services) |
| Tier / Vertical | Multi-Sector / Food and Agriculture |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: the Food Distribution **3PL cold storage and logistics service** (`soc2-readiness.csv`). Meat Processing and Grocery Retail are out of scope. A group review of the cold-chain monitoring vendor's SOC 2 report (`vendor-soc2-review.csv`) |
| Categories in scope (3PL) | Security, Availability, Processing Integrity |
| Target report (3PL) | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30, delivered to customers before 2027-12-31 |
| Prepared | 2026-08-31 by the Group Chief Risk Officer's assurance team with the Food Distribution security and compliance lead and the 3PL services director; approved by the board risk committee 2026-09-15 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service as part of their own control environment. For each division the question is whether outside organizations rely on that division's systems and controls, not just on its products.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Food Distribution | 3PL cold storage and logistics at DC-1 and DC-3, with the 3PL customer portal and EDI (SYS-D3) for about 60 external food brands | **Yes, a true service organization.** The brands store their product in group freezers and coolers and rely on group inventory records and temperature history for their own food safety records and recalls. 14 of them, including two national food manufacturers, asked for a SOC 2 report by the end of 2027 | **In scope.** First readiness assessment | Security, Availability, Processing Integrity | Type 1 as of 2027-03-31; Type 2 for 2027-04-01 to 2027-09-30 |
| Food Distribution | General-line grocery wholesale to the group's stores, about 2,800 independent grocers, and food service customers | No. Customers buy groceries; they do not build controls on group systems | Out of scope | n/a | n/a |
| Meat Processing | Further processing at six FSIS-inspected plants | **No.** It sells food. Customers rely on safe product, which FSIS inspection, the HACCP plans, and customer supplier-approval audits cover | **Out of scope** (reasons below) | n/a | n/a |
| Grocery Retail | 120 supermarkets, online ordering, loyalty program | **No.** Shoppers are consumers, not user entities | **Out of scope.** Its assurance is the annual PCI DSS Report on Compliance by a QSA (acquirer requirement) | n/a | n/a |

**Why Meat Processing is out of scope:**
1. **No user entities.** Grocery chains, distributors, and food service customers buy product. They do not rely on plant systems as part of their own control environment.
2. **Assurance comes from food safety regimes instead.** FSIS inspection at every plant, the HACCP plans and records (9 CFR 417), the Plant 6 food defense plan (21 CFR Part 121), and customer supplier-approval audits.
3. **Customer cybersecurity questionnaires** (now common in supplier approval after ransomware at food companies) are answered from the group security program description and this sample's P02, P03, and P07 results, not a SOC 2 report.
4. **Revisit trigger:** if Meat Processing starts co-packing under a customer's brand with access to the customer's systems or data, reassess.

**Why Grocery Retail is out of scope:** the PCI DSS ROC is the assurance its acquirer requires, and the group has no customers that rely on store systems. The loyalty program and online ordering are consumer services; consumer privacy is covered by the privacy notice, the FTC Act, and state law (P03).

**The Food Distribution wholesale business** benefits without being in scope: the 3PL report covers the DC-1 and DC-3 rooms, WMS, and portal that wholesale also uses, and wholesale customers who ask for assurance get a bridge letter describing the shared controls.

**Other assurance options considered.** The vertical overlay names no standard assurance alternative for this sector. Some 3PL customers accept food safety audits for warehouse sanitation and temperature control, and those continue. They do not cover the portal, data isolation, or the integrity of temperature history, which is what the 14 customers asked about. SOC 2 was chosen because two national food manufacturers wrote it into their 2027 renewal terms.

## 2. System description (scope of the 3PL report)
- **Services:** receiving, storage, and shipping of refrigerated and frozen product for about 60 external brands at DC-1 and DC-3; inventory, order, and temperature history visibility in the 3PL customer portal; EDI orders and advance ship notices.
- **Infrastructure:** SYS-D3 on cloud provider A, with DR replicas and immutable backups in provider B; DC automation and automated freezer storage at DC-1 and DC-3 (SYS-D1); the DC tier of the cold-chain monitoring platform (SYS-G6); SYS-G5 OT remote access and monitoring at both DCs.
- **Software:** the 3PL portal and EDI gateway (built by the division), the WMS (SaaS), and the cold-chain monitoring service (SaaS).
- **Group shared services carved in:** identity (SYS-G1), the SOC (SYS-G2), cloud landing zones (SYS-G3), and OT security services (SYS-G5). These are operated by corporate and were assessed once by group internal audit in P07, so the service auditor can rely on the same evidence. The Food Distribution inheritance matrix that proves this is not yet written (POAM-017).
- **Subservice organizations (carve-out):** cloud providers A and B, the WMS vendor, and the cold-chain monitoring vendor. The description must name the complementary subservice organization controls the group relies on for each.
- **People:** DC-1 and DC-3 operations and 3PL customer service staff, group SOC, identity, and cloud teams.
- **Data:** customer inventory, orders, and pricing; temperature history; portal user accounts (business contact data only).
- **Complementary user entity controls:** customer administrators request and remove their portal users and confirm them quarterly; customers review temperature reports and raise exceptions within the agreed window; customers keep their own EDI credentials secret.

**Why Processing Integrity.** The brands use the group's temperature history as their own record that product was held at safe temperatures, and they use inventory records for recalls. A temperature history with silent gaps is a processing integrity failure even when the system is secure and available. The BIA already treats loss of this service as Moderate (BP-D04: MTD 24 h, RTO 12 h, RPO 1 h).

## 3. Readiness results (3PL service, `soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 17 | 15 | 1 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why many criteria are Ready for a first report:** the control environment, risk assessment, identity, endpoint, and SOC criteria are met by group common controls that P07 already tested.

**Not ready (2):**
- **CC2.3:** no system description; service commitments differ across about 60 agreements on four contract versions; complementary user entity controls were never stated to customers.
- **A1.3:** SYS-D3 has never been failed over to provider B as a whole system. P07 proved the data restores; it did not prove the service.

**Partially ready (18):**
- *Food Distribution governance (scenario gap 7):* CC1.3, CC2.1, CC2.2, CC5.3 (POAM-016, POAM-017).
- *Portal and data isolation:* CC6.2 (7 of 25 sampled portal users had left their companies), CC7.1 (authorization tests only at major releases, FD-004), CC3.4 (changes and onboarding not risk-assessed).
- *Shared group weaknesses that reach the DCs:* CC6.3 (service accounts outside PAM, POAM-012), CC6.6 (DC automation on the corporate domain, GR-01), CC7.2 (30-day logs, POAM-019; cold-chain events not in the SOC, POAM-010), CC7.4 (notification matrix never exercised, POAM-011), CC7.5 (DC automation backups untested, POAM-018).
- *Third parties:* CC6.7 (EDI credentials, FD-005), CC9.2 (cold-chain vendor CUEC gaps, POAM-006).
- *Assurance scope:* CC4.1 (SYS-D3 application controls not yet in the P07 plan).
- *Availability and processing integrity of temperature history:* A1.2 (single alert integration server, POAM-005), PI1.1 (no processing specification), PI1.4 (reports do not flag backfilled or missing readings).

**Confidentiality** is out of scope because customers did not ask for it. Customer commercial data is still protected under CC6 and the agreements. **Privacy** is out of scope because the service holds no consumer personal information.

## 4. Cold-chain monitoring vendor report review (`vendor-soc2-review.csv`)
The cold-chain platform (SYS-G6) serves all three divisions, so the group reviews its report once for everyone. The review closes the "not reviewed since 2024" part of POAM-006 (P07 SA-9 finding).
- **Report:** Type 2, 2025-04-01 to 2026-03-31, Security and Availability, unqualified opinion; vendor cloud provider carved out; bridge letter through 2026-06-30.
- **Exceptions (2):** late removal of 3 of 25 sampled terminated vendor users; one skipped quarterly restore test. Neither affects alert dispatch. Accepted with follow-up.
- **Complementary user entity controls:** 6 listed; **4 operating, 2 not**. The gateways at DCs and stores sit on general networks, and all alert routing depends on one alert integration server with no tested failover. These are the group's own gaps (GR-02, POAM-005), and **the vendor's controls protect the cold chain only after they are closed.**
- **Availability:** 99.9% monthly availability, alert dispatch within 5 minutes, and 24-hour gateway buffering meet the BIA for BP-G04, BP-M01, BP-D01, and BP-R02 once the two gaps are closed.
- **Follow-ups:** monthly data export into SYS-M5 and SYS-D3 so record retention does not depend on the vendor (9 CFR 417.5(e); 21 CFR 117.206(a)(5)); a 24-hour incident notice term at the 2027 renewal; ask the vendor about adding Processing Integrity.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect | Owner |
|---|---|---|---|
| 2026 Q4 | CC1.3, CC2.2, CC5.3 | Re-issued Food Distribution supplement; retired 2023 standards; written 3PL security duties | Food Distribution security and compliance lead |
| 2026 Q4 | CC6.3, CC7.1, CC7.4 | PAM records for the WMS and DC automation service accounts; authorization regression results per release; tabletop report with a 3PL notice | Group identity director; 3PL services director; Group SOC director |
| 2027 Q1 | CC2.1, CC2.3, CC3.4, CC6.2, CC7.2, CC7.5, CC9.2, A1.2, PI1.1 | Inheritance matrix; system description and standard service commitments; customer responsibilities letter; quarterly portal user confirmations; 12-month logs and SIEM feed; DC automation restore test; CUEC closure; alert integration failover test; processing specifications | Food Distribution security and compliance lead; 3PL services director; Group cold-chain services manager |
| 2027 Q1 | CC4.1, CC6.6, CC6.7, A1.3, PI1.4 | SYS-D3 controls in the 2027 P07 plan; DC automation moved to the OT domain; EDI credential rotation; full failover test; gap flags in reports. **Type 1 as of 2027-03-31** | Group internal audit director; Group OT security director; Group cloud platform director |
| 2027 Q2 to Q3 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30) | 3PL services director |

**Communication.** The 3PL services director sends the 14 requesting customers a readiness letter with this timeline in 2026 Q4, and the customer responsibilities letter with the Type 1 report. Until then, customer questionnaires are answered from this readiness assessment and the POA&M summary.

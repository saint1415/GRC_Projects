# SOC 2 Readiness Summary: Cris Santos Company Holdings | Financial Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Financial Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the AICPA text is not reproduced |
| Scoping | Per division (section 1). Two readiness reports: Payments Software Platform (`soc2-readiness.csv`) and Payment Processing (`soc2-readiness-payment-processing.csv`). Merchant Consulting is out of scope |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the Software division client trust and assurance director and the Payment Processing division CISO |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether other organizations rely on its controls as part of their own, and whether SOC 2 is the assurance they need.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Payments Software Platform | Commerce software (SYS-S1), gateway and developer platform (SYS-S2), device management (SYS-S3) for about 410,000 merchants and 1,900 ISVs | **Yes, a true service organization.** Merchants and ISVs build their own controls on top of it | **In scope (full).** Existing annual Type 2 | Security, Availability, Confidentiality | Type 2, 12 months ending September 30 (period ending 2026-09-30 now being reported) |
| Payment Processing | Authorization, clearing, settlement, and funding for about 920,000 merchants and four sponsor banks | **Yes.** Merchants and sponsor banks rely on its controls | **In scope for readiness.** PCI DSS (ROC and AOC) stays the main assurance for card data, and the SOC 1 Type 2 covers controls relevant to financial reporting. Sponsor banks asked in their 2026 due diligence for a SOC 2 covering security, availability, and processing integrity of settlement and funding; two large ISV partners asked as well | Security, Availability, Processing Integrity | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 (aligned with the SOC 1 period) |
| Merchant Consulting | Advisory, integration, PCI readiness, and dispute services | Partly. Dispute services handle clients' account data | **Out of scope** (reasons below) | n/a | n/a |

**Why Merchant Consulting is out of scope:**
1. **Most of its work is advisory.** Clients buy advice and project work, not an outsourced system they build controls on. Engagement letters, not SOC reports, carry the assurance (the professional services vertical lists engagement letters as the client assurance mechanism).
2. **Its one system-like service runs inside another division's scope.** For group merchants, dispute work happens in the processor's dispute platform (SYS-P6), which is in the processor's PCI DSS ROC and will be in its SOC 2.
3. **Its controls are not ready for an examination.** Until the SYS-M1 migration (2027-03-31) and the supplement re-issue (2026-11-30), an auditor would find the identity and policy gaps that P03 and P07 found.
4. **Revisit trigger:** if dispute services for the 620 non-group clients grow or a client requires a report, decide between carving dispute services into the processor's SOC 2 and a separate report. The PCI DSS acknowledgment and responsibility matrix for those clients are already required (P03 MC-G10, MC-G11; POAM-023).

**Other assurance options considered.** The financial services vertical names PCI DSS validation as a service provider and SOC 1 for financial reporting controls as its assurance alternatives; the processor already has both. The Software division's vertical names ISO/IEC 27001 certification; its merchants and ISVs ask for SOC 2, so SOC 2 stays primary.

## 2. System descriptions (scope)
### 2.1 Payments Software Platform
- **Services:** cloud point of sale, about 180,000 online storefronts, invoicing, the payment gateway and developer platform, device management, and the app marketplace; the "merchant insights assistant" generative AI feature for about 58,000 merchants (launched 2026-05-12).
- **Infrastructure and software:** SYS-S1 to SYS-S3 on cloud provider B; group identity (SYS-G1) and SOC (SYS-G2) carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud provider B; the content delivery service; **the third-party model provider** (not yet in the description, scenario gap 6).
- **Data:** merchant data and merchants' customers' order data; cardholder data in the gateway CDE (separately validated under PCI DSS).
- **Complementary user entity controls:** merchants manage their own users and MFA, their storefront theme changes, and the apps they install; ISVs protect their API credentials.

### 2.2 Payment Processing (first report)
- **Services:** authorization, tokenization, clearing and settlement, merchant funding, chargeback processing, and the merchant portal.
- **Infrastructure and software:** the Payment Processing Platform (P02 SSP): SYS-P1 to SYS-P3 in the two group data centers, SYS-P4 to SYS-P6 in provider A; common controls carved in.
- **Subservice organizations (carve-out):** cloud provider A; carriers for card network links. Card networks and sponsor banks are not subservice organizations; they are parties to the payment system.
- **Affiliates that provide services into the system:** the Software division gateway (inbound transactions) and Merchant Consulting (dispute analysts). How to present them (as part of the system or as subservice organizations) is decided with the service auditor; either way, the intercompany responsibility matrix must exist first (POAM-009).
- **Complementary user entity controls:** merchants protect their terminals and integrations and manage their portal users; sponsor banks review funding files under their own procedures.

## 3. Readiness results
### 3.1 Payments Software Platform (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3 (the assistant and its model provider are not in the system description or merchant terms) and A1.3 (gateway failover last tested 2025-04).
**Partially ready:** CC3.4 and CC8.1 (the assistant skipped the change gate), CC6.3 (standing consulting access to the ISV console; keys shown in clear), CC6.6 (storefront scripts monitored on the standard template only), CC7.4 (ISV and enterprise merchant notice paths), and CC9.2 (no ongoing monitoring of the model provider or script-capable apps).

**The immediate issue is the report now being prepared.** The period ended 2026-09-30, and the assistant operated for about four and a half months of it. Management must describe the feature, the model provider (as a subservice organization, with the carve-out method and any complementary subservice organization controls), and the change itself. Expect the service auditor to evaluate CC2.3, CC3.4, CC8.1, and CC9.2 for exceptions, and A1.3 for the missed test. POAM-017 and POAM-019 cover the fixes; the target is merchant notice before the report is issued in December.

### 3.2 Payment Processing (`soc2-readiness-payment-processing.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 24 | 9 | 0 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first report:** control environment, risk, monitoring, physical, malware, and change criteria are met by group common controls already evidenced for the Software division's report and by the PCI DSS program. Availability is proven by the semiannual data center failover.
**Partially ready:** CC2.1 (data inventory), CC2.3 (no system description yet), CC3.4 (the 2025 acquisition was not reviewed), CC6.2 and CC6.3 (consulting accounts and the case export permission), CC6.7 (dispute evidence by email), CC7.2 (SYS-P6 events not in the SIEM), CC7.4 (sponsor bank contacts and rules), CC9.2 (affiliates not overseen), PI1.1 (objectives not yet written into a description), PI1.4 (manual balancing of adjustments before file release), and PI1.5 (dispute files kept 14 months).

Every Partially ready security criterion traces to the same root causes as the P03 and P07 findings: Merchant Consulting users inside the CDE, and notice procedures that lag the four-bank portfolio. Fixing the POA&M fixes the readiness.

## 4. Remediation plan and evidence calendar
| Quarter | Division | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | Software | CC2.3, CC3.4, CC8.1 | Updated system description for the period ending 2026-09-30; merchant notice; change gate records |
| 2026 Q4 | Software | A1.3, CC6.3, CC7.4 | Gateway failover test report; console access reviews and key masking; matrix and binder with ISV contacts |
| 2026 Q4 | Payment Processing | CC2.1, CC3.4, CC6.3, CC7.2, CC7.4 | Scope reconfirmation and acquisition review; SYS-P6 role review; SIEM onboarding; contacts for all four banks |
| 2027 Q1 | Payment Processing | CC2.3, CC6.2, CC6.7, CC9.2, PI1.1, PI1.5 | First system description; SYS-G1 migration; evidence portal and purge; intercompany responsibility matrix. Type 1 as of 2027-03-31 |
| 2027 Q1 | Software | CC6.6, CC9.2 | Tamper-detection on every storefront; app re-review; model provider review |
| 2027 Q2 to Q3 | Both | All in-scope criteria | Operating evidence for the Software division's 2027 period and the processor's first Type 2 period (2027-04-01 to 2027-09-30) |
| 2027 Q1 | Payment Processing | PI1.4 | Automated funding file balancing |

**Communication:** the Software division client trust and assurance director briefs the largest ISVs and enterprise merchants on the assistant and the remediation before the 2026 report is issued. The head of bank and network relationships gives the four sponsor banks the processor's readiness results and timeline in their 2026 due diligence packages.

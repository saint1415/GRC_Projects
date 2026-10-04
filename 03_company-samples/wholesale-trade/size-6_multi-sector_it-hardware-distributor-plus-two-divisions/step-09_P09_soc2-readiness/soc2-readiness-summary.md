# SOC 2 Readiness Summary: Cris Santos Company Holdings | Wholesale Trade | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Wholesale Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs only, with topic labels written for this repository |
| Scoping | Per division (section 1). Two readiness reports: IT Distribution Lifecycle Services ITAD (`soc2-readiness.csv`) and the Logistics 3PL fulfillment service (`soc2-readiness-3pl.csv`). Online Retail, core distribution, and Federal Solutions are out of scope |
| Prepared | 2026-09-15 by the Group Chief Risk Officer's assurance team with the IT Distribution and Logistics security and compliance leads |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each service line is whether customers rely on the group's controls as part of their own control environment.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Logistics | 3PL contract fulfillment for about 140 client companies (receiving, storage, order fulfillment, client WMS console) | **Yes, a true service organization.** Clients outsource fulfillment and rely on the WMS record of their inventory and orders. Clients already receive a SOC 1 Type 2 report for financial reporting controls; they now ask for SOC 2 for security and availability | **In scope.** First SOC 2 | Security, Availability | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| IT Distribution | Lifecycle Services: asset tagging, staging, and ITAD with media sanitization for about 300 enterprise customers | **Yes, for this service line.** Customers hand over devices holding their data and rely on the group's sanitization and chain of custody | **In scope.** First SOC 2 | Security, Confidentiality | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| IT Distribution | Core distribution and the reseller portal | **No.** Resellers buy products; they do not build their own controls on the group's systems | **Out of scope.** Resellers who ask for evidence receive the group security program description and the portal vendor's own SOC 2 report | n/a | n/a |
| IT Distribution | Federal Solutions integration work | **No SOC 2.** DoD primes rely on CMMC Level 2 (C3PAO) status and SPRS results, the assurance mechanism named for defense supply chains | **Out of scope** (CMMC is the assurance; P03) | n/a | n/a |
| Online Retail | Consumer storefront and marketplace | **No.** Consumers and marketplace sellers are not user entities that rely on its controls for their own control environments | **Out of scope** (reasons below) | n/a | n/a |

**Why Online Retail is out of scope:**
1. **No user entities.** Consumers buy products. Marketplace sellers use the platform to sell, but they do not outsource a control function to it.
2. **Assurance comes from PCI DSS instead.** The acquirer requires an annual ROC by a QSA (the assurance alternative named in the Retail Trade overlay), and the CCPA cybersecurity audit will add an independent audit from the 2027 period (P03).
3. **Revisit trigger:** if Online Retail starts offering fulfillment or payments services to marketplace sellers, assess whether a SOC 1 or SOC 2 report is needed.

**Why 3PL processing integrity stays with SOC 1.** Clients' financial reporting reliance on inventory and billing accuracy is already covered by the SOC 1 Type 2 report. Adding Processing Integrity to SOC 2 would duplicate it, so it is not in scope.

## 2. System descriptions (scope)
### 2.1 IT Distribution Lifecycle Services (ITAD)
- **Services:** asset tagging, staging, collection, chain of custody, data sanitization (clear, purge, or destroy under NIST SP 800-88), certificates of sanitization, and resale or recycling.
- **Infrastructure and software:** SYS-D3 Lifecycle Services platform (vendor SaaS); 5 processing lines in secure cages inside 2 DCs; group identity (SYS-G1) and SOC (SYS-G2) carved in as internal shared services.
- **Subservice organizations (carve-out):** the SaaS platform vendor; 3 downstream recyclers that receive shredded media.
- **People:** about 300 ITAD technicians and quality staff; Logistics DC security.
- **Data:** customer devices and media containing customer data; asset and chain-of-custody records.
- **Complementary user entity controls:** customers list devices accurately, remove devices from their own management and encryption key services, and review certificates.

### 2.2 Logistics 3PL fulfillment
- **Services:** inbound receiving, storage, order fulfillment, shipping, returns, and the client WMS console.
- **Infrastructure and software:** SYS-D5 WMS on provider A, SYS-D6 TMS, SYS-D7 DC automation, and the 9 DCs; group common controls carved in.
- **Subservice organizations (carve-out):** cloud provider A; the TMS vendor; parcel and freight carriers.
- **Data:** client inventory, orders, and consumer shipping addresses (Logistics is a third-party agent for client personal information).
- **Complementary user entity controls:** clients provision and remove their console users, protect their order file transfers, and review inventory reports.

## 3. Readiness results
### 3.1 IT Distribution Lifecycle Services (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 27 | 5 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | 1 | 0 | 1 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3 (no system description or written service commitments) and C1.2 (sanitization verification not documented on 2 of 5 lines; P07 found one readable drive in a batch that had been certified).
**Partially ready:** CC4.1, CC5.3, CC6.5, CC7.4, and CC9.2.

The readable drive is the decisive issue. Certificates were issued for that batch, so before any report is issued Lifecycle Services must re-process the batch, correct the certificates, and notify the customer under its contract (POAM-021, notice due 2026-10-15).

### 3.2 Logistics 3PL fulfillment (`soc2-readiness-3pl.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 25 | 7 | 1 | 0 |
| Availability (A1, 3) | 1 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first-time report:** control environment, risk, monitoring, identity, network, and SOC criteria are met by group common controls already assessed once by internal audit (P07).
**Not ready:** CC2.3. The SOC 2 system description cannot be written until Logistics documents which group controls it inherits (scenario gap 8; POAM-022).
**Partially ready:** CC1.3, CC5.3, CC6.1, CC6.2, CC6.6, CC7.2, CC9.2, A1.2, and A1.3. Most trace to the drifted Logistics supplement, client users without MFA, and DC automation (vendor tunnels, monitoring, PLC backups, untested ransomware recovery).

## 4. Remediation plan and evidence calendar
| Quarter | Division | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | IT Distribution | C1.2, CC5.3, CC6.5 | Re-processed batch and corrected certificates; verification sampling records on all lines |
| 2026 Q4 | Logistics | CC1.3, CC5.3, CC2.3 | Re-issued supplement; inheritance matrix |
| 2026 Q4 | Logistics | CC6.1, CC6.6, CC9.2, A1.2 | Client MFA rollout; PAM vendor session records; vendor reviews; PLC backups in the vault |
| 2027 Q1 | IT Distribution | CC2.3, CC4.1, CC7.4, CC9.2 | System description; monthly quality sampling; matrix rows for ITAD customers; recycler assessments. Type 1 as of 2027-03-31 |
| 2027 Q1 | Logistics | CC2.3, A1.3, CC6.2 | System description with carve-ins; ransomware and PLC restore tests; agency account expiry. Type 1 as of 2027-03-31 |
| 2027 Q2 | Logistics | CC7.2 | OT monitoring at all DCs (due 2027-06-30); an exception in the first Type 2 period is likely if it slips |
| 2027 Q2 to Q3 | Both | All in-scope criteria | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30) |

**Communication:** the Logistics vice president of 3PL services sends clients a readiness letter with the 2027 timeline and the MFA rollout date. Lifecycle Services tells its top customers about the readiness program and the corrected batch.

# SOC 2 Readiness Summary: Cris Santos Company | Utilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (investor-owned electric distribution utility with a Utility Services line for 4 client utilities) |
| Tier / Vertical | Mid-Market / Utilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| System | The **Utility Services system**: contract billing, CIS hosting, after-hours outage call handling, and meter data management for 4 client utilities |
| Target report | SOC 2 **Type 1** as of 2027-03-31 (interim), then **Type 2** for the observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-17 by the vCISO, the GRC analyst, and the Director of Utility Services, using P02, P04, P05, P06, and P07 evidence |

## 1. Why SOC 2 for this organization
An electric distribution utility is not usually a SOC 2 service organization: it delivers power to retail customers, and its main assurance regime is NERC CIP compliance monitoring by SERC. The **Utility Services** line changes that. The company provides billing, CIS hosting (client partitions in the company's CIS tenant), after-hours outage call handling, and meter data management to 2 municipal utilities and 2 electric cooperatives (about 58,000 meters, about $14 million a year in fees). For those services, the company is a service organization: its controls affect its clients' financial reporting, customer data, and service to their customers.

All 4 client contracts renew in 2027 and require a SOC 2 Type 2 report. The clients asked for:
- **Security**, because the company holds their customers' identity and bank data;
- **Availability**, because their billing and after-hours calls depend on it (1-business-day billing and 99.5% monthly contact center availability);
- **Processing Integrity**, because the company calculates their customers' bills with their rate tables;
- **Confidentiality**, because client data must stay separate and be returned or destroyed at contract end.

Privacy was not requested; privacy notices, consent, and customer requests remain each client's responsibility, so the 18 Privacy criteria are out of scope.

**Why not Type 2 now.** P07 and this readiness review found that several controls the clients rely on are not yet operating: CIS bulk export and AMI bulk command rights, partition change approvals, retention of client data, and recovery testing of client services. Starting an observation period now would produce exceptions. The plan is to remediate through 2027 Q1, issue a Type 1 report as of 2027-03-31, and then run a 6-month Type 2 period.

**Alternatives considered:**
- **Type 1 only:** not acceptable to the clients beyond 2027; offered as the interim report.
- **Client audit rights and questionnaires:** the current practice. It costs each client and the company more time each year than one SOC 2 report.
- **NERC CIP audit results:** not relevant: CIP covers the BES relays, not the Utility Services system.

**Service auditor independence.** An independent CPA firm that is **not** the co-sourced internal audit firm will perform the examination, so the P07 work does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Billing and payment posting for client customers; CIS hosting (client partitions); after-hours outage call handling; meter data management (validation, estimation, delivery) |
| Infrastructure | Analytics account (meter data warehouse, CIS export share), backup account, network hub, and security and log archive accounts of the landing zone (P04); corporate network at headquarters; identity provider |
| Software | CIS (client partitions), AMI head-end (client tenant), contact center platform, meter data warehouse |
| People | 42 Utility Services staff; billing, credit, and contact center staff who serve client customers; IT and security team; MSSP |
| Data | Client utilities' customer records (names, addresses, SSNs and driver license numbers where clients collect them, bank account numbers), usage and interval data, bills, payments, call recordings |
| Procedures | POL-01 to POL-05, the standards index, runbook B (P08), the Identity Theft Prevention Program, client service procedures |
| Subservice organizations (carve-out) | CIS vendor, AMI vendor, contact center platform vendor, cloud provider, identity provider vendor, MSSP, bill print vendor. Their controls are covered by their own SOC 2 reports (Part B) and the complementary subservice organization controls listed in the system description |
| Out of scope | The Distribution Operations Platform (SCADA, OMS, field network) and the BES relays, except as shared infrastructure services (identity provider, monitoring) |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 14 | 17 | 2 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **18** | **21** | **4** | **18** |

**Ready (18):**
- governance, risk, and monitoring: CC1.1, CC1.2, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2, CC4.1, CC4.2, CC5.1;
- access and threats: CC6.2, CC6.4, CC6.8, CC7.3;
- capacity: A1.1;
- processing: PI1.2, PI1.4, PI1.5.

**Not ready (4):**
- CC6.3: 41 users with CIS bulk export rights and 22 users who can bulk-disconnect client meters without a second approver;
- CC8.1: 9 of 20 sampled partition changes in 2026 had no approver;
- A1.3: client partitions, the AMI client tenant, and the meter data warehouse have no recovery test;
- C1.2: client data in CIS extracts kept since 2021; no return or destruction procedure at contract end.

Each maps to a P07 POA&M item (POAM-012, POAM-013, POAM-022). The Partially ready criteria mostly depend on the system description, standards issued under P06, and log coverage for the analytics account.

**Mapping to other work.** Evidence is reused from P02 (control statements), P04 (cloud customer-side controls), P05 (availability commitments for BP-08), P06 (policies), P07 (test results), and P08 (runbook B). The `related_sp800_53` column links each criterion to SP 800-53 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.1, CC2.3, PI1.1 (system description and client commitments); CC6.3 (rights reduced, two-person rule); CC8.1 (partition change tickets); C1.1, C1.2 (extract minimization and retention); CC6.5, CC6.6, CC6.7, CC7.1, CC7.2, CC3.3, CC5.2 | System description draft; AMI and CIS role exports after cleanup; change tickets with approver and test evidence; extract retention logs; shred bin checks; KEV patch records; SIEM source list |
| 2027 Q1 | CC1.4, CC3.4, CC5.3, CC7.4, CC7.5, CC9.1, A1.3, PI1.3 | Role-based training records; client onboarding checklist; issued standards; tabletop report with a client observer; recovery test of one client partition, then all 4; continuity plan |
| 2027-03-31 | **Type 1** (design) report as the interim deliverable to the clients | Management's system description and assertion |
| 2027 Q2 | CC9.2, A1.2 | Vendor tiering and contract amendments; CIS vendor recovery terms |
| 2027-04-01 to 2027-09-30 | **Type 2** observation period | All recurring control evidence (quarterly access reviews, monthly scans, change tickets, daily reconciliations, restore tests, vendor reviews) |

**Status reporting.** The Director of Utility Services reports readiness monthly to the Chief Operating Officer and quarterly to the audit committee and the 4 clients.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many of its own controls (P02: 11 Common/Inherited and 23 Hybrid; P04: 5 Provider and 19 Shared rows). The program in `vendor-soc2-review.csv` makes that reliance evidence-based and is the core of the vendor and OT supply chain standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | OT remote access, customer or client data at scale (more than 10,000 people), privileged access to company systems, or support for a High-criticality BIA process | SOC 2 Type 2 (or equivalent independent assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms. Where no report exists, alternative assurance (questionnaire, contract terms, supervision) | Annually |
| **Tier 2** | Limited customer data, no privileged or OT access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No customer data and no system access | Contract terms only | At contract renewal |

Of about 85 vendors with system or data access, about 22 are Tier 1 and 30 are Tier 2 under this approach. The CSV holds the first 8 Tier 1 reviews and 1 Tier 2 example. The remaining Tier 1 reviews (including the 3 carriers and the bill print vendor) are due by 2027-03-31 (POAM-011).

**Key findings:**
1. **CIS vendor (VEN-01):** unqualified Type 2 across all four requested categories. Its stated RTO of 12 hours **does not meet the BIA** (8 hours for the contact center, 1 business day for client billing). Two complementary user entity controls are open company gaps: bulk export rights and partition change approval. **The vendor's controls only protect the clients once those gaps close.**
2. **AMI vendor (VEN-02):** unqualified, no exceptions. The vendor provides bulk command limits and two-person approval; the company has not turned them on (POAM-013).
3. **SCADA and ADMS vendor (VEN-03):** unqualified, with an exception about support engineers keeping access to customer credentials. That exception matters because the vendor uses the shared SCADA administrator accounts (POAM-001; P01 R-001). Its software build environment is carved out (P01 R-015).
4. **Contact center platform vendor (VEN-06):** the generative AI assistant (AI-003) was released after the report period and is not covered. AI data-use terms are needed before the feature stays on (P10).
5. **Relay testing contractor (VEN-08):** no SOC 2 report; alternative assurance is required, and the Substation H modem shows why.

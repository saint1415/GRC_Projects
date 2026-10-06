# SOC 2 Readiness Summary: Cris Santos Company | Other Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional electronics and device repair chain) |
| Tier / Vertical | Mid-Market / Other Services (except Public Administration) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1) |
| Target report | SOC 2 **Type 2** on the claims fulfillment service, observation period 2027-04-01 to 2027-09-30 (6 months), report delivered to Partner P1 by 2027-12-31 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-04 by the vCISO and the GRC Analyst with the Director of Partner Programs (fieldwork 2026-08-24 to 2026-09-04), using P02, P05, P06, and P07 evidence |
| Approved | Chief Operating Officer, 2026-09-17 |

## 1. Why SOC 2 for this organization
A repair chain is usually **not** a SOC 2 service organization: it fixes hardware and hands it back to consumers. That changes for one line of business:
- Partners P1 and P2, two device protection plan administrators, send about 38,000 claims a year to the company through the partner integration API.
- The company receives the claimant's personal information, repairs or replaces the device, and posts outcomes and costs back. Those outcomes drive the partners' claim settlement and the company's invoices (P05 BP-05, BP-14).
- The partners therefore rely on the company's controls for the confidentiality of their customers' data, the availability of the claims service, and the accuracy of what the company reports. Partner P1's renewal (2027-06-30) requires a SOC 2 Type 2 report on the claims fulfillment service by 2027-12-31.

For that service the company is a service organization, and a SOC 2 Type 2 report is the right assurance tool. Partner P1 asked for **Security, Availability, Confidentiality, and Processing Integrity**. Processing Integrity is unusual for a repair company, but it fits: an outcome posted twice, or not at all, is a billing error for the partner and a dispute for the company (P01 R-047).

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in access removal, monitoring, recovery testing, and vendor oversight, and the outcome reconciliation does not exist yet. Starting the observation period before those are fixed would produce exceptions. The plan is to remediate through 2027 Q1, then run a 6-month observation period from 2027-04-01.

**Alternatives considered:**
- **Type 1 first (point in time):** offered to Partner P1 as an interim report for 2027-03-31. Partner P1 accepted the plan with quarterly status updates.
- **Partner questionnaires only:** acceptable to Partner P2 for now, but not to Partner P1 after its renewal.
- **ISO/IEC 27001 certification:** not requested by either partner; would not address Processing Integrity.

**What SOC 2 does not replace.** The SAQ P2PE and SAQ A attestations (due 2026-12-15) remain the assurance the acquirer relies on, and the Manufacturer A program audit (2026-10) remains the assurance Manufacturer A relies on. The SOC 2 work reuses their evidence where it overlaps.

**Service auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so that the P07 work does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Claims fulfillment for Partners P1 and P2: claim intake, repair or replacement, status and outcome reporting, and partner invoicing |
| Infrastructure | STPP components that support the service (P02): SYS-01, SYS-03, the SYS-04 landing zone, SYS-05 partner integration API, SYS-07 Depot bench workstations, SYS-09 Depot and store networks, SYS-11 monitoring |
| Software | SYS-01 (vendor SaaS), identity provider, partner integration API (company-built), reporting database, ERP invoicing module |
| People | Partner claims desk, Depot technicians, store technicians handling claims, digital engineering team, IT and security team, finance (partner billing), MSSP |
| Data | Claimants' names, contact details, device and fault data; repair outcomes and costs |
| Procedures | POL-01 to POL-05, the standards index, and the P08 runbooks |
| Subservice organizations (carve-out) | SYS-01 vendor, identity provider, cloud provider, MSSP. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls listed in the company's system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 18 | 6 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 1 | 3 | 1 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **11** | **23** | **9** | **18** |

**Ready (11):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC3.1, CC3.2;
- monitoring of controls: CC4.1, CC4.2;
- control design: CC5.1;
- user registration: CC6.2;
- capacity: A1.1;
- input validation at the partner API: PI1.2.

**Not ready (9):**
- CC3.4: no security or risk review of new services, vendors, or AI features;
- CC6.3: leavers active in manufacturer portals; unrestricted technician access at 14 stores;
- CC6.5 and C1.2: disposal and retention not enforced (27 TB in the lab, records since 2016, store drop-offs without records);
- CC7.2: SYS-01 exports, application logs, and the checkout page not monitored;
- CC7.5 and A1.3: recovery of the partner API never tested; no contingency plan;
- CC9.2: 7 vendors with customer data lack security and data-use terms;
- PI1.4: no daily reconciliation of outcomes posted to partners.

Each maps to a P07 POA&M item. The Partially ready criteria mostly depend on standards being issued (P06) and on the legacy store rollout (POAM-002).

**What Partner P1 would notice first:** CC6.3, CC7.2, and PI1.4 together. Partner P1's question is "who can see our customers' data, would you know if it left, and are the outcomes you send us right?" Today the honest answer is "most staff appropriately, but technicians at 14 stores have no controls; you would hear from a customer before our logs; and we find outcome errors at invoicing." POAM-002, POAM-003, and POAM-023 change that answer.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies and standards), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.3 (intake notice, partner commitments), CC3.3, CC3.4, CC6.3 (leaver accounts), CC6.5 (drop-offs to the Depot line), CC9.2 (addenda), C1.1, CC7.4 | Corrected notice; refund reviews; change and purchasing review records; monthly local account reconciliations; certificates per device; signed addenda; tabletop report (2026-11-18) |
| 2027 Q1 | CC1.2, CC1.4, CC2.1, CC2.2, CC5.2, CC5.3, CC6.1, CC6.7, CC6.8, CC7.1, CC7.2, CC7.3, CC7.5, CC8.1, A1.3, C1.2, PI1.1, PI1.3, PI1.4, PI1.5 | SIEM use case alerts; daily outcome reconciliation reports; exception queue; API recovery test record; standards; pipeline scan results; purge confirmations; processing specification |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to Partner P1 | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly reconciliations, restore tests, vendor reviews, daily outcome reconciliations) |
| 2027 Q2 | CC6.4, CC6.6, CC9.1, A1.2 (segmentation of the last stores, alternate receiving) | Network test results; alternate site procedure |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee and Partner P1.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 7 Common/Inherited and 24 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of the vendor risk standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Customer or claimant data at scale (more than 10,000 people), payment functions, privileged access to company systems, or support for a High-criticality BIA process | SOC 2 Type 2 (or PCI DSS AOC for payment providers) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited customer data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No customer data and no system access | Contract terms only | At contract renewal |

Of 92 vendors, 9 are Tier 1 and about 17 are Tier 2 under this approach. The CSV holds the 5 Tier 1 reviews completed in 2026, the 4 Tier 1 reviews still outstanding (due by 2026-12-31), and 1 Tier 2 example.

**Key findings:**
1. **SYS-01 vendor:** unqualified Type 2. Its stated RTO of 8 hours **does not meet the BIA** (4 hours for intake and release). Two complementary user entity controls the company must operate are open gaps: review of audit logs and exports (POAM-003), and keeping credentials out of free-text fields (POAM-015). **The vendor's controls protect the company only once those gaps close.** The vendor also offers a bulk redaction tool for notes, which is the fastest way to close POAM-015.
2. **Payment processor and gateway:** current PCI DSS AOC and P2PE listing. The responsibility matrix leaves the page that embeds the payment fields with the company, which is exactly the P07 finding on the checkout page (POAM-012).
3. **MSSP:** unqualified Type 2 (Security only), with 1 missed 30-minute escalation in 40 samples. The SIEM platform is carved out, and its own SOC 2 report must be obtained. Log source coverage is the company's CUEC and is incomplete (POAM-003).
4. **AI vendors and the contact center AI add-on:** one Type 1 only, one questionnaire pending, and no data-use terms. These are the weakest links for customer data and feed directly into P10.
5. **Recycler:** never assessed, and its certificates list lots, not serial numbers. For a company whose disposal duty runs under Fla. Stat. 501.171(8), the recycler is a Tier 1 vendor even though it never touches a system.

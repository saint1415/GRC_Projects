# SOC 2 Readiness Summary: Cris Santos Company | Defense Industrial Base | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed aircraft parts manufacturer, DoD subcontractor) |
| Tier / Vertical | Mid-Market / Defense Industrial Base |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| System | Additive and engineering services line, running on the CUI Engineering Enclave |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30, before the customers' 2027-12-31 deadline |
| Primary assurance for defense work | CMMC Level 2 certification assessment by a C3PAO (32 CFR Part 170), target window 2027-03-08 to 2027-03-19 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor assurance review program (`vendor-assurance-review.csv`) |
| Prepared | 2026-09-10 by the vCISO and the Security Manager, using P02, P05, and P07 evidence; approved by the COO 2026-09-17 |

## 1. Why SOC 2 for this organization
**For defense work, CMMC is what counts.** About 62% of revenue comes from three defense primes. Their recognized evidence is a CMMC status in SPRS and the SP 800-171 DoD Assessment score required by DFARS 252.204-7019 and 252.204-7020. A SOC 2 report does not replace either one.

**The services line makes the company a service organization.** Since 2026, the additive and engineering services line receives three commercial customers' CAD and build files through the MFT gateway, prepares builds, prints and finishes parts, and returns build packages and reports. For that line the company processes customer data on its systems as a service, which is what SOC 2 reports on. All three services agreements require a SOC 2 Type 2 report covering Security, Availability, and Confidentiality by 2027-12-31.

**Why Type 2, and why not sooner.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in recovery, shop-floor monitoring, and vendor oversight, and the Plant 2 additive area sits on the flat Plant 2 network until 2027-01-31. Starting the observation period before those are fixed would produce exceptions. The CMMC remediation fixes most of them by 2027-02, so the observation period starts 2027-04-01, after the C3PAO assessment.

**Alternatives considered:**
- **Type 1 first:** rejected. It would compete with the C3PAO assessment for the same people in 2027-03, and the customers accepted quarterly status letters instead.
- **ISO/IEC 27001 certification:** not requested by any customer.
- **Customer questionnaires only:** the agreements require an independent report.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the P07 work does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Additive build preparation, printing, finishing, and design-for-additive engineering for 3 commercial customers (about 30 jobs a month) |
| Infrastructure | MFT gateway and build preparation server in the landing zone (P04); PLM workspaces for services projects; the 6 additive printers and the Plant 2 additive area; identity provider; plant networks connecting them |
| Software | MFT gateway, build preparation software, PLM, identity provider, SIEM |
| People | 8 additive engineers, Director of Additive and Engineering Services, IT and security team, MSSP |
| Data | Customer CAD and build files, build parameters, build reports and inspection data |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks, the services procedure |
| Subservice organizations (carve-out) | Government-community cloud provider; MSSP. Their controls are covered by the FedRAMP authorization, the CRM, and their SOC 2 reports, plus the complementary subservice organization controls listed in the company's system description |

## 3. Readiness results (Part A)
From `soc2-readiness.csv` (61 criteria; 38 in scope).

| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 13 | 15 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **14** | **17** | **7** | **23** |

**Ready (14):**
- governance and risk: CC1.1, CC1.3, CC1.4, CC1.5, CC2.2, CC3.1, CC3.2;
- monitoring of controls: CC4.1, CC4.2;
- control selection: CC5.1;
- access and boundary: CC6.2, CC6.6;
- event evaluation: CC7.3 (the MSSP escalated the P07 test alert in 18 minutes);
- capacity: A1.1.

**Not ready (7):**
- CC7.1 and CC7.2: shop-floor and Plant 2 systems, including the additive area, are not scanned or monitored;
- CC7.5 and A1.3: no restore test in 12 months; the build preparation server and MFT gateway have never been restore-tested;
- CC9.1: no contingency plan;
- CC9.2: MSSP CRM missing, additive printer vendor unreviewed, suppliers unverified;
- C1.2: no procedure or records for disposing of customer files at the end of retention.

Each maps to a P07 POA&M item. The Partially ready criteria mostly depend on the Plant 2 integration and on standards being issued (P06). POAM-024 tracks the remaining SOC 2-specific work: the system description (CC2.3), customer file retention and disposal (C1.1, C1.2), and the Plant 2 network UPS (A1.2).

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies and standards), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls; that mapping is the author's.

| CMMC evidence | Trust Services Criteria it supports |
|---|---|
| SSP v4.0, asset inventory, data flow register | CC2.1, CC5.1, CC5.2, C1.1 |
| Risk register (P01), annual risk assessment (3.11.1) | CC3.1 to CC3.4 |
| P07 results and POA&M (3.12.1, 3.12.2) | CC4.1, CC4.2 |
| Identity exports, access reviews, termination records (3.1.1, 3.5.3, 3.9.2) | CC6.1 to CC6.3 |
| Visitor and badge records (3.10.1 to 3.10.5) | CC6.4 |
| Destruction certificates, media inventory (3.8.3, 3.8.7) | CC6.5, C1.2 |
| Data flow controls, FIPS module table (3.1.3, 3.13.11) | CC6.7 |
| Scan reports, SIEM use cases, EDR coverage (3.11.2, 3.3.5, 3.14.6) | CC6.8, CC7.1, CC7.2 |
| Incident log, runbooks, tabletop and DIBNet drill (3.6.1 to 3.6.3) | CC7.3, CC7.4 |
| Change tickets and baselines (3.4.1 to 3.4.3) | CC8.1 |
| Supplier flowdown and status checks (DFARS 252.204-7012(m), 252.204-7020(g)) | CC9.2 |

Criteria that rely on work CMMC does not require: CC7.5, CC9.1, and A1.1 to A1.3 (recovery and availability), CC2.3 (customer commitments), and C1.1 and C1.2 (customer retention and disposal). They come from the BIA (P05), the contingency plan, and the services procedure.

## 4. Remediation plan and evidence calendar
| Target (from `soc2-readiness.csv`) | Criteria | Evidence to start collecting |
|---|---|---|
| 2026-10-31 | CC3.3, CC6.4 | Call-back verification records; Plant 2 visitor system logs |
| 2026-11-30 | CC6.5, CC6.7, CC9.2 | Destruction certificates for Plant 2; closed AI-003 flow and FIPS confirmation; MSSP CRM; supplier verification |
| 2026-12-31 | CC3.4, CC7.1, CC8.1, CC9.1, C1.1, C1.2 | AI intake and M&A checklist records; monthly scan reports; shop-floor change tickets; contingency plan; retention schedule; deletion certificates |
| 2027-01-31 | CC2.1, CC5.2, CC5.3, CC6.1, CC6.3, CC6.8, CC7.2, A1.2 | Complete inventory; baselines; issued standards; named Plant 2 sign-in; quarterly review sign-offs; allowlisting reports; SIEM source list; UPS and backup records |
| 2027-02-28 | CC2.3, CC7.4, CC7.5, A1.3 | System description; tabletop and Plant 2 exercise reports; restore test records |
| 2027-03-31 | CC1.2 | Two quarterly audit committee minutes |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence: quarterly reviews, monthly scans, quarterly restore tests, vendor reviews, monitoring tickets |

**Status reporting.** The vCISO reports readiness monthly to the COO, quarterly to the audit committee, and in a quarterly status letter to the three services customers.

## 5. Vendor assurance review program (Part B)
The company relies on providers for many inherited and hybrid controls (P02: 6 Common/Inherited and 53 Hybrid). The program in `vendor-assurance-review.csv` makes that reliance evidence-based and is the core of the supplier and service provider standard (STD-03). For defense data the required assurance is often a FedRAMP authorization, a CRM, or a supplier's SPRS and CMMC status rather than a SOC 2 report, so the review records whichever applies.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Holds CUI, services customer data, or employee personal information at scale; has privileged or remote access to in-scope systems; or supports a High-criticality BIA process | FedRAMP authorization and CRM (cloud with CUI), SOC 2 Type 2 plus bridge letter (other providers), or DFARS flowdown and SPRS and CMMC status (suppliers); review of scope, exceptions, carve-outs, complementary controls mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No company data and no system access | Contract terms only | At renewal |

Of about 60 IT, OT, and service vendors with access to company systems or data, 12 are Tier 1 under this approach. The CSV holds 7 Tier 1 reviews (including the 22 CUI suppliers as one group) and 3 Tier 2 examples. The remaining Tier 1 reviews (CAD and PLM software vendor, machine tool remote support vendors, test equipment vendor, MFT software vendor, forensic firm) are due by 2027-01-31 (POAM-018).

**Key findings:**
1. **MSSP:** unqualified Type 2 (Security only) with escalation exceptions in 2 of 40 samples, and **no CRM**. Under 32 CFR 170.19(c)(2), the MSSP's services are assessed as Security Protection Assets, so the CRM is needed before the C3PAO assessment.
2. **Predictive maintenance vendor (AI-003):** its SOC 2 is clean, but it runs on a commercial cloud that is not FedRAMP authorized, so it must not receive CUI. The fix is on the company side: strip program names and move the gateway (POAM-002).
3. **Additive printer vendor:** no SOC 2, and a remote tool outside company control. It touches the services line directly, so it is the most important vendor fix for the SOC 2 scope (POAM-014).
4. **Suppliers:** only 8 of 22 have verified SPRS status, and 9 still lack DFARS flowdown (POAM-018, POAM-022).
5. **Cloud provider:** FedRAMP authorized at Moderate or higher with a current CRM. The AI-001 assistant's place inside that boundary must still be confirmed in writing before it is used (P10).

# SOC 2 Readiness Summary: Cris Santos Company | Construction | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial and institutional building general contractor) |
| Tier / Vertical | Mid-Market / Construction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| System | Managed Building Systems Services (MBSS): remote monitoring, health checks, and administration of client video surveillance, access control, and building automation systems |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30, ahead of the clients' 2027-12-31 deadline |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor assurance review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-15 by the vCISO, the Security Manager, and the Director of Technology and Security Systems, using P02, P04, P05, and P07 evidence. Approved by the Chief Operating Officer 2026-09-17 |

## 1. Why SOC 2 for this organization
A general contractor is usually **not** a SOC 2 service organization: owners buy buildings, not the company's IT controls. The construction business stays that way. For federal work, the assurance that matters is CMMC and the SPRS score (P03). For private owners, it is answering questionnaires about drawings and payment fraud.

**The MBSS line changes that.** Since 2025 the company has sold a recurring service to 38 client sites (hospitals, a university, county buildings, private offices):
- the MBSS monitoring room watches client cameras, door controllers, and building automation alarms and must respond to critical alerts within 1 hour;
- technicians reach client systems remotely through the MBSS platform (SYS-13) and hold client administrator credentials in a vault;
- a failure or compromise of the MBSS platform can leave a hospital's doors or cameras unmonitored, or give an intruder control of them (P01 R-020, R-021).

For this service, the company's controls directly affect the security of its clients' systems. That is the situation SOC 2 is designed for. A hospital system and the university require a **SOC 2 Type 2** report on MBSS by contract renewal on 2027-12-31, covering Security, Availability, and Confidentiality.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated over a period. Today 11 of 38 sites are reached with shared technician accounts outside the company gateway, and the platform rebuild has never been tested. Starting the observation period before those are fixed would produce exceptions or a qualified opinion. The plan fixes them through 2027 Q1, then runs a 6-month observation period from 2027-04-01. The report is due about a month before the clients' deadline.

**Alternatives considered:**
- **Type 1 first (point in time, 2027-03-31):** offered to both clients as an interim report. The hospital system accepted it with quarterly status updates; the university asked only for the status updates.
- **Bridge to the Type 2 deadline with questionnaires:** not acceptable to either client's contract.
- **SOC 2 for the whole company:** rejected. The construction business has no SOC 2 customers, and CMMC Level 2 is the right assurance for the CUI scope.
- **ISO/IEC 27001 certification:** not requested by the clients.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm and **not** the C3PAO, so the P07 work and the CMMC assessment do not create independence questions.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | MBSS remote monitoring and alarm response, monthly health checks, user and configuration administration of client systems, and incident support for 38 client sites |
| Infrastructure | MBSS cloud account in the landing zone (SYS-13): monitoring servers, remote-access gateway, ticketing, client credential vault; the MBSS monitoring room at headquarters; the 12 commissioning laptops; supporting landing zone accounts (security and identity, shared services, backup) (P04) |
| Software | Remote monitoring and management (RMM) software; remote-access gateway; ticketing; credential vault; AI-005 alarm triage |
| People | MBSS technicians and monitoring staff in the Technology and Security Systems group; the Director of Technology and Security Systems; IT and security team; MSSP |
| Data | Client facility security details: camera layouts, controller exports, alarm data, and client administrator credentials (classified Restricted under POL-04) |
| Procedures | POL-01 to POL-05; STD-01 to STD-10 as issued; P08 runbooks; MBSS service procedures |
| Subservice organizations (carve-out) | Commercial public cloud provider, identity provider vendor, MSSP (and its SIEM platform provider), RMM software vendor's update service. Their controls are covered by their own reports and the complementary subservice organization controls listed in the system description |
| Out of scope | Construction project delivery, the PDPP, and the CUI Project Enclave (covered by the SSP, P02, and CMMC, P03) |

**Complementary user entity controls (clients).** The system description will list what clients must do: approve technician access requests for their sites, maintain their own site contact list, review monthly access and change reports, and notify the company when staff with alarm-response authority change.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 19 | 3 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **12** | **22** | **4** | **23** |

**Ready (12):**
- governance and risk: CC1.1, CC1.2, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2;
- deficiency tracking: CC4.2;
- physical access, disposal, and transmission: CC6.4, CC6.5, CC6.7;
- capacity: A1.1.

**Not ready (4):**
- **CC6.1:** 11 of 38 client sites are reached with shared technician accounts through the clients' own remote-access tools, outside the company gateway (POAM-020);
- **CC7.5 and A1.3:** the MBSS platform has never been rebuilt in a test against its 2-hour RTO (POAM-011);
- **CC9.2:** about 210 vendors are not tiered, and the RMM software vendor has only a Type 1 report (POAM-022).

**What most Partially ready criteria have in common.** The corporate controls are sound, but MBSS-specific activity is not yet under them: gateway sessions, vault checkouts, and RMM scripts are not logged to the SIEM (CC7.2), not under change control (CC8.1), and not restricted to each technician's assigned sites (CC6.3). The standards MBSS depends on are still in draft (CC5.3).

**Mapping to other work.** Evidence is reused from P02 (control statements), P04 (MBSS account controls), P05 (BP-11 recovery objectives), P06 (policies), P07 (test results and POA&M), and P08 (incident procedures). The `related_sp800_53` column links each criterion to SP 800-53 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.4, CC3.3, CC3.4, CC6.1, CC6.2, CC6.6, CC7.1, CC7.3, C1.1 | Gateway session recordings and named-account lists for all 38 sites; technician training records; AI-005 review record; monthly scan reports; client impact step in incident tickets; data loss prevention reports |
| 2027 Q1 | CC2.1, CC2.3, CC4.1, CC5.1, CC5.2, CC5.3, CC6.3, CC6.8, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, A1.2, A1.3, C1.2 | Client device inventory; signed security schedules; MBSS control matrix; gateway and RMM baselines; quarterly access reviews; allowlisting records; SIEM use cases; MBSS client compromise tabletop report; rebuild test report; script change tickets; Tier 1 vendor reviews; client data offboarding records |
| 2027-03-31 | Type 1 (design) report delivered to the hospital system as an interim deliverable | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence: quarterly access reviews, monthly scans, session recording reviews, change tickets, restore test, vendor reviews, alarm response times |
| 2027-11-30 | Type 2 report issued to both clients | Report and bridge letter process |

**Budget.** $200,000 across 2027 for readiness support and the Type 1 and Type 2 examinations, approved in the FY2027 security plan (P01 section 4). The gateway expansion ($70,000) is funded separately under POAM-020.

**Status reporting.** The Director of Technology and Security Systems reports readiness monthly to the COO, and the vCISO reports it quarterly to the audit committee and the two clients.

## 5. Vendor assurance review program (Part B)
The company relies on vendors for many of its controls: in the SSP (P02), 11 controls are Common/Inherited and 30 are Hybrid. The program in `vendor-soc2-review.csv` makes that reliance evidence-based. It is the core of the vendor and subcontractor security standard (STD-03) and replaces the old practice of reading 9 SaaS SOC 2 reports a year without tiering (gap 12).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Holds CUI, FCI at scale, payment data, employee personal information, or client facility security details; has privileged access to company or client systems; or supports a High-criticality BIA process | SOC 2 Type 2 (or a FedRAMP package for CUI cloud services, or SPRS and DFARS flowdown for CUI subcontractors) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability against the BIA, and incident terms | Annually |
| **Tier 2** | Limited sensitive data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No sensitive data and no system access | Contract terms only | At contract renewal |

**A construction-specific point.** Subcontractors that hold CUI are Tier 1 vendors, but their assurance is not a SOC 2 report. It is the DFARS 252.204-7012 flowdown, a verified current SPRS assessment (DFARS 252.204-7020(g)(2)), and, once required, their own CMMC status (32 CFR 170.23). VEN-09 shows that review for the A&E firm. The 14 FC-4 trades follow the same pattern under POAM-016.

Of about 210 vendors, about 25 are expected to be Tier 1 and about 70 Tier 2. The CSV holds the first 9 Tier 1 reviews and 1 Tier 2 example. The remaining Tier 1 reviews are due by 2027-03-31 (POAM-022).

**Key findings:**
1. **ERP vendor (VEN-05):** unqualified Type 2, but its RTO of 24 hours **does not meet** the 8-hour billing-week need (P05 finding 1). Two CUECs the company must operate are open gaps: the urgent override in bank changes (POAM-003) and log review (POAM-008).
2. **Project platform vendor (VEN-04):** meets the BIA, but is not FedRAMP authorized and could not show equivalence, so it can never hold CUI. Four of its CUECs are open company gaps (POAM-001, POAM-002, POAM-008, POAM-011). **The vendor's controls protect the company's data only once those gaps close.**
3. **MSSP (VEN-03):** unqualified Type 2 with an escalation exception (2 of 40). Its value depends on the log sources the company sends; the SaaS, gateway, and CPE sources are missing.
4. **RMM software vendor (VEN-08):** **Type 1 only**, for software that reaches every client site. A Type 2, or a compensating review of update signing and vulnerability disclosure, is required before the company's own observation period, because the service auditor will ask how the company relies on it.
5. **Government-community cloud provider (VEN-07):** assurance is the FedRAMP authorization and CRM, not SOC 2. The CRM must be re-reviewed for the virtual desktop field access and the new monitoring service.

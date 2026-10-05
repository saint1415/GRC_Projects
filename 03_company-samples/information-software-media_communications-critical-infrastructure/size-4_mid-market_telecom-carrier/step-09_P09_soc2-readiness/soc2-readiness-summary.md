# SOC 2 Readiness Summary: Cris Santos Company | Communications | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional broadband and wired telecommunications carrier) |
| Tier / Vertical | Mid-Market / Communications |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| System | **Business Services system**: hosted voice (UCaaS), managed SD-WAN and firewall, and colocation, with the supporting OSS, identity, NOC monitoring, and SIEM components |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30; interim Type 1 as of 2027-03-31 |
| Part A | Readiness assessment (`soc2-readiness.csv`), which also serves as the evidence map |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`, an added file) |
| Prepared | 2026-09-04 by the vCISO, the Security Manager, and the Director of Business Services, using P02, P05, P06, and P07 evidence; accepted by the COO 2026-09-17 |

## 1. Why SOC 2 for this organization
**Most of the company is not a SOC 2 service organization.** Residential and business customers buy transmission (voice, broadband, data circuits). They rely on SLAs and the FCC rules, not on a SOC report, and the obligations that bind those services are regulatory (P03).

**Business Services is different.** About 600 business customers run their phone systems on the company's hosted voice platform, about 1,900 customer sites are configured and monitored through the managed SD-WAN service, and colocation customers place equipment in the CO-1 data hall. Those customers rely on the company's controls for their own operations, and several (a regional hospital system, two county governments, a school district, and three credit unions) asked for a SOC 2 Type 2 report in 2026 RFPs and renewals. For these services the company is a service organization, and SOC 2 is the right assurance tool. P01 R-044 records the commercial risk: about $2 million to $6 million of annual Business Services revenue depends on it.

**Categories.**
- **Security (required) and Availability** were requested by every customer; the 99.99% SLA is a service commitment.
- **Confidentiality** was requested by the hospital system and the counties because the platform holds their call records and network configurations.
- **Processing Integrity is out of scope.** The services transmit and route calls and traffic; customers did not ask for it.
- **Privacy is out of scope.** The services are business-to-business, the customers did not request it, and consumer CPNI duties are governed by the FCC rules (P03), not by the SOC 2 Privacy criteria.

**Why Type 2, and why not now.** A Type 2 report tests operating effectiveness over a period. P07 found gaps that touch Business Services directly: shared administrator accounts on the hosted voice cluster, the vendor VPN account, informal change management, missing monitoring, and no recovery test. Starting the observation period before those close would produce exceptions. The plan is to remediate through 2027 Q1, issue a Type 1 report as of 2027-03-31 for the RFPs, then run a 6-month observation period.

**Alternatives considered:** a security questionnaire only (rejected by the hospital system and both counties); ISO/IEC 27001 certification (no customer asked for it); the vertical overlay names no sector-specific assurance scheme for communications.

**Service auditor independence.** An independent CPA firm that is **not** the co-sourced internal audit firm will perform the examination, so the internal audit work in P07 does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Hosted voice (UCaaS) for about 600 customers (14,200 seats); managed SD-WAN and firewall for about 1,900 customer edges; colocation (42 racks) |
| Infrastructure | Hosted voice cluster and standby node in the CO-1 data hall; SBCs and network paths that carry Business Services traffic; data hall power, cooling, and physical security; NOC monitoring (SYS-09) |
| Software | Hosted voice platform, SD-WAN orchestrator (vendor SaaS), customer self-service portal, OSS ticketing and provisioning (SYS-02), identity provider (SYS-05), SIEM (SYS-16) |
| People | 46 Business Services engineers and support staff; NOC; IT and security team; MDR |
| Data | Business customers' call records, configurations, voicemail, and portal accounts |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks, the NOC outage plan |
| Subservice organizations (carve-out) | SD-WAN orchestrator vendor, identity provider, SIEM vendor, MDR provider, cloud provider. Their controls are covered by their own SOC 2 reports (Part B), and the complementary subservice organization controls will be listed in the system description. The hosted voice software vendor has no SOC 2; its remote access is controlled by the company (CC6.6) |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 19 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **11** | **21** | **6** | **23** |

**Ready (11):**
- governance and risk: CC1.1, CC1.3, CC3.1, CC3.2;
- monitoring and control design: CC4.1, CC5.1;
- physical, transmission, and malware: CC6.4 (data hall), CC6.7, CC6.8;
- capacity: A1.1;
- disposal at contract end: C1.2.

**Not ready (6):**
- CC6.1: the hosted voice cluster is administered with shared local accounts without MFA (POAM-002);
- CC6.6: the vendor shared VPN account and SBCs near end of support (POAM-003, POAM-017);
- CC7.1: SBCs and hosted voice components are not scanned, and there is no drift monitoring (POAM-014, POAM-006);
- CC7.2: hosted voice and orchestrator logs are not in the SIEM (POAM-005);
- CC8.1: 5 of 10 sampled hosted voice changes had no review or approval (POAM-007);
- A1.3: no failover or restore test of the hosted voice cluster (POAM-010).

Each maps to a P07 POA&M item; there is no separate SOC 2 remediation track. The Partially ready criteria mostly depend on standards being issued (P06), on SIEM onboarding, and on a few quarters of operating evidence.

**Evidence map.** `soc2-readiness.csv` names the control owner, the evidence for each criterion, and the related SP 800-53 controls from the SSP (P02). Evidence is reused from P02 (control statements), P05 (availability commitments and RTOs), P06 (policies and standards), P07 (test results and samples), and P08 (incident procedures). AICPA publishes a TSC-to-SP 800-53 mapping (SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC3.3, CC3.4, CC6.2, CC6.3, CC6.5, CC6.6, CC7.4, CC8.1, CC9.2 | Know-your-customer records for new tenants; AI and feature intake records; transfer tickets; first quarterly access review; device wipe records; access broker session logs; tabletop report; change tickets with approvals; vendor contract amendments |
| 2027 Q1 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.2, CC2.3, CC4.2, CC5.2, CC5.3, CC6.1, CC7.1, CC7.2, CC7.3, CC7.5, A1.2, A1.3, C1.1 | Audit committee minutes; training records; SIEM source list; standards; PAM logs; scan reports; MDR use cases; restore and failover test records; 15-minute configuration snapshots; customer security addendum; retention schedule |
| 2027-03-31 | Type 1 (design) report as of this date | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly scans, change tickets, restore tests, vendor reviews) |
| 2027 Q2 | CC9.1 (standby node at CO-4; second cooling unit) | Build records; failover test |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee. The Director of Business Services gives the requesting customers a quarterly status letter until the Type 1 report is issued.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 10 Common/Inherited and 36 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based and is the core of the vendor risk standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | CPNI at scale, privileged or network access, or support for a High-criticality BIA process | SOC 2 Type 2 (or questionnaire plus on-site review where none exists) and bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited CPNI or PII, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No CPNI, PII, or system access | Contract terms only | At renewal |

Of the 34 vendors with CPNI, PII, or network access, 12 are Tier 1. All 12 Tier 1 reviews are in the CSV (reviewed 2026-08-06 to 2026-09-12). The 22 other vendors are reviewed by 2027-03-31 (POAM-015).

**Key findings:**
1. **BSS vendor:** unqualified Type 2, but its stated 12-hour RTO **does not meet the BIA** (8 hours for customer care), and 3 of its CUECs are open company gaps (audit review, access reviews, approval checks). The vendor's controls only protect CPNI once those close.
2. **CCaaS vendor:** the agent assist feature launched after the report period, and its language model subprocessor is carved out. The company has no assurance over the part of the service that transcribes calls (P10 AI-002).
3. **Chatbot vendor:** Type 1 only, no incident notice term, and no bar on training with company data. Contract amendment by 2026-12-31 (P10 AI-001).
4. **Hosted voice software vendor and overflow call center:** no SOC 2 reports; questionnaire and on-site review found shared support accounts and untrained agents (POAM-003, POAM-004).
5. **Bill print vendor:** qualified opinion on its own access reviews; remediation evidence requested.
6. **Incident notice terms are too slow.** Seven Tier 1 contracts allow 72 hours or more or set no fixed term (VEN-01, VEN-05, VEN-07, VEN-08, VEN-09, VEN-10, VEN-12). A 24-hour term is needed to leave room for the 7-business-day CPNI clock (47 CFR 64.2011(b)), and vendors that hold Florida residents' personal information must notify the company within 10 days of determining a breach (Fla. Stat. 501.171(6)).

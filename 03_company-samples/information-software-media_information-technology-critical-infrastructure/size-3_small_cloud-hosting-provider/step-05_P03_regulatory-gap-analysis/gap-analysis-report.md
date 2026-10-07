# Regulatory Gap Analysis: Cris Santos Company | Information Technology | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (cloud hosting and managed infrastructure provider) |
| Tier / Vertical | Small / Information Technology |
| Regulation analyzed | FedRAMP (44 U.S.C. 3607-3616) as implemented by the **FedRAMP Consolidated Rules for 2026**, Rev5 Class C, Agency Certification path. **Readiness analysis: FedRAMP does not apply to the company yet** |
| Secondary regulation | Bank service provider notification rule: 12 CFR 53.4 (OCC), 12 CFR 225.303 (FRB), 12 CFR 304.24 (FDIC). **Applies today** |
| Assessment dates | Fieldwork 2026-07-13 to 2026-07-31 with the contracted FedRAMP advisor. Statuses updated 2026-09-25 for the P06 policy approvals and the P07 results |
| Assessor | IT Manager (Information Security Officer), with the FedRAMP advisor, the Engineering Manager (Control Plane), and the Director of Platform Engineering |
| Sources checked | fedramp.gov (2026 rules, important dates, certification path, Rev5 rulesets), retrieved 2026-09-26; eCFR 12 CFR 53.2, 53.3, 53.4, 225.303, 304.24 (as of 2026-09-23) |

## 1. Applicability
### 1.1 FedRAMP: does not apply yet
FedRAMP governs cloud services that federal agencies use. It has no size threshold or small-business exemption (C-IT-R01); it applies because of the customer, not the provider's size. **The company has no federal customer today**, so no FedRAMP rule binds it now.

It becomes relevant because a civilian agency program office sent a letter of interest in May 2026. The office wants to host a Moderate-impact case management application on the managed private cloud and would sponsor the company. The decision gate with the agency is 2026-12-31. This analysis measures readiness against the rules the company would have to meet.

**Which path, verified on fedramp.gov (2026-09-26):**
- **Two certification types.** FedRAMP now issues Rev5 certifications (based on the NIST SP 800-53 Rev. 5 control lists) and 20x certifications. Classes run from A to D. FedRAMP describes 20x Class C as Moderate, and the Rev5 Class C control list is the Moderate-level list.
- **Two paths.** The *Agency* path requires an agency to authorize the service first, then sponsor it, and is only available for Rev5. The *Program* path needs no sponsor and is mostly for 20x. The temporary Rev5 Program pipelines (Lost Sponsor and Ready Conversion, opened 2026-08-10) are limited to providers that were already in the legacy process, so the company does not qualify.
- **Rev5 Agency Certification** requires the agency's completed ATO process, ending with a signed ATO letter sent to FedRAMP (FRC-APS-ATO).
- **Key dates.** The 2026 rules take mandatory effect on 2027-01-01, which covers any certification the company would obtain. The FedRAMP 20x Class B and C pipeline opened on 2026-08-31. **FedRAMP stops accepting new Rev5 certification applications on 2027-06-11.**

**Chosen target (scenario-facts section 5):** Rev5 Class C Agency Certification for the managed private cloud offering. The company must pursue only one Program Certification type for an offering (FRC-CSO-POP).

### 1.2 Bank service provider notification rule: applies
The company performs hosting and managed services for 14 community banks, and the banks' vendor contracts treat these as services subject to the Bank Service Company Act. That makes the company a **bank service provider** (12 CFR 53.2(b)(2) and (b)(5)). It must notify each affected bank's designated contact as soon as possible after determining that a computer-security incident has materially disrupted or degraded covered services, or is reasonably likely to, for four or more hours (12 CFR 53.4(a); identical text in 225.303(a) and 304.24(a)). There is no size exemption. The banks themselves must notify their own regulator within 36 hours of determining that a notification incident occurred (for example 12 CFR 53.3). The company's notice feeds that clock.

### 1.3 Other vertical requirements
| ID | Requirement | Applies? | Why |
|---|---|---|---|
| C-IT-R02 | CMMC (32 CFR Part 170) | No | No DoD contracts or subcontracts; the MSA prohibits FCI and CUI from DoD programs |
| C-IT-R03 | DFARS 252.204-7012 | No | No covered defense information; no clause flowed down |
| C-IT-R04 | DOJ Data Security Program (28 CFR Part 202) | No | No vendor, employment, or investment agreement gives a country of concern or covered person access to customer data; all staff and contractors are U.S.-based. Recheck at each new vendor contract |
| C-IT-R06 | CIRCIA | Not in force | No final rule as of 2026-09-25; tracked in section 5 |

## 2. Method
1. **Requirements.** Rows follow the FedRAMP rules' own structure:
   - **44 FedRAMP rules** (rows G-001 to G-044), selected from the Rev5 rulesets that apply to a Class C provider seeking initial certification. Each row cites the rule ID and its MUST, SHOULD, or MAY keyword. Summaries are paraphrased; FedRAMP rule text is a U.S. government work.
   - **The Rev5 Class C control list** from rule FRC-CSF-BSL (rows G-045 to G-224): 180 base controls, one row each, with the 142 Class C enhancements listed in the citation column.
   - **Five rows for the bank rule** (G-225 to G-229), cited to section and paragraph.
2. **Crosswalk.**
   - Control rows use NIST's CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 where one exists (135 rows, labeled "Official"). The other 45 control rows, and all rule and bank rows, are author mappings.
3. **Evidence.** Current state was established by interviews, configuration exports (identity provider, cloud IAM, RMM, firewalls, SIEM), document review, the DC-1 and DC-2 walkthroughs, and the P07 control tests.
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

The control statements in this table are the same ones in the SSP (P02), so the two documents cannot drift apart.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FedRAMP Certification rules (FRC) | 2 | 2 | 7 | 0 |
| Minimum Assessment Scope (MAS) | 0 | 2 | 2 | 0 |
| Security Decision Record (SDR) | 0 | 1 | 1 | 0 |
| Certification Data Sharing (CDS) | 0 | 2 | 2 | 0 |
| Incident Evaluation and Communication (IEC) | 0 | 5 | 0 | 0 |
| Vulnerability Detection and Response (VDR) | 0 | 3 | 3 | 0 |
| Vulnerability Evaluation and Reporting (VER) | 0 | 0 | 2 | 0 |
| Significant Change Notification (SCN) | 0 | 0 | 2 | 0 |
| Cryptographic Module Use (CMU) | 0 | 0 | 2 | 0 |
| Other rulesets (CCM, AFC, IVV, SCG) | 0 | 1 | 5 | 0 |
| **FedRAMP rules subtotal (44)** | **2** | **16** | **26** | **0** |
| Rev5 Class C control list (180 base controls) | 38 | 99 | 40 | 3 |
| Bank service provider notification rule (5) | 2 | 2 | 1 | 0 |
| **Total (229)** | **42** | **117** | **67** | **3** |

**Control list by family** (Met / Partially met / Not met / N/A):
- **Strongest:** PE 10/4/1/1, since facility controls are inherited from the colocation providers; SC 11/6/1/1; SI 4/6/2/0.
- **Weakest:** CP 0/4/5/0 (no contingency plan, no restore tests); SR 0/4/5/0 (no supply chain program); IR 0/5/4/0 (no incident capability before September 2026); AU 2/5/4/0 (management-plane logs missing).

**Gap risk** (184 rows Partially met or Not met): **38 High, 75 Moderate, 71 Low**.

## 4. Priority gaps and roadmap
### 4.1 High gaps
| Gap | Rows | Action | Owner | Target |
|---|---|---|---|---|
| No agency ATO; the Rev5 application window closes 2027-06-11 | G-003 (FRC-APS-ATO) | Decision gate with the agency by 2026-12-31 (see 4.3) | Chief Executive Officer | 2026-12-31 gate; ATO 2027-05-31 |
| Offering scope for federal tenants not defined; third-party resources not assessed | G-012, G-014 (MAS-CSO-IIR, MAS-CSO-TPR) | Dedicated agency cluster; keep the RMM tool out of agency tenants; record the FedRAMP status of each SaaS tool | Engineering Manager (Control Plane); Controller | 2027-02-28 |
| Shared RMM accounts and open RMM console | G-056 (AC-17), G-046 (AC-2(9)) | Named accounts, IP restriction, two-person approval for multi-customer scripts | Managed Services Lead | 2026-11-30 |
| No MFA or named accounts at the hypervisor and BMC layer; management network reachable from the NOC | G-106 (IA-2), G-109 (IA-5), G-189 (SC-7), G-048 (AC-4(21)) | Federate hypervisor managers; bastion-only BMC access; deny-by-default management network | Director of Platform Engineering | 2026-12-31 |
| Control plane service credentials reach every hypervisor manager; one shared cloud account | G-050 (AC-6) | Scoped short-lived credentials; separate production, build, and backup accounts | Engineering Manager (Control Plane) | 2027-02-28 |
| Backups deletable with production; never restore-tested; no contingency plan | G-097, G-099, G-100, G-101, G-103, G-104 (CP-2, CP-4, CP-6, CP-7, CP-9, CP-10) | Immutable second-region backups; recovery runbook; quarterly restore tests; site failover plan | Engineering Manager (Control Plane); Director of Platform Engineering | 2026-12-31 to 2027-05-31 |
| Management-plane logs missing; no log review | G-067, G-071, G-076 (AU-2, AU-6, AU-12), G-207 (SI-4) | Onboard hypervisor, BMC, network, and RMM logs; weekly review; limit AI auto-close (P10) | IT Manager | 2027-01-31 |
| No monthly authenticated scanning, KEV tracking, or scheduled BMC patching | G-023, G-025, G-028 (VDR), G-171 (RA-5), G-205 (SI-2) | Monthly authenticated scans; daily KEV matching; quarterly BMC firmware cycle | Director of Platform Engineering | 2027-01-31 |
| No change control for data center changes; review bypass for hotfixes | G-031 (SCN-CSO-EVA), G-086 (CM-3), G-181 (SA-10) | Change process with a significant-change field; enforce branch protection | Director of Platform Engineering; Engineering Manager (Control Plane) | 2026-12-31 |
| Template signing key in a pipeline secret; signatures not verified at deploy | G-192 (SC-12), G-210 (SI-7) | Cloud HSM for the key; verify at deploy | Engineering Manager (Control Plane) | 2027-03-31 |
| No 1-hour FedRAMP incident reporting capability; incident handling only approved 2026-09-25 | G-019 (IEC-CSO-IIR), G-118 (IR-4), G-120 (IR-6) | Federal incident response coordinator; templates; tabletop | IT Manager | 2026-12-15 tabletop; 2027-03-31 |
| Customer administrator MFA optional | G-044 (SCG-CSO-SDF) | Require MFA for customer administrators | Engineering Manager (Control Plane) | 2027-01-31 |
| Critical vendors never assessed | G-180 (SA-9), G-220 (SR-6) | Vendor tiering; annual SOC 2 review; incident notice terms | Controller | 2026-12-31 |
| 139 Class C controls not yet fully in place | G-008 (FRC-CSF-BSL) | The remediation above, then the rest by 2027-03-31 | IT Manager | 2027-03-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, for the 22 assessed controls, the POA&M (P07).

### 4.2 Bank rule gaps (apply now)
- **Designated contacts** (G-227): contacts are on file for only 9 of 14 banks, last verified in 2023. Collect and verify all 14 by 2026-10-31 (NOC and Support Manager; P01 R-022).
- **Notice procedure** (G-226): now written into the P08 runbook, but untested. Tabletop by 2026-12-15.

### 4.3 Roadmap and decision point
| Phase | Dates | Work |
|---|---|---|
| 1. Stop the bleeding | 2026-10 to 2026-12 | RMM account fixes; hypervisor MFA; immutable backups; bank contacts; change process; KEV tracking; incident tabletop |
| 2. Decision gate | By 2026-12-31 | CEO and the agency confirm sponsorship, schedule, and the scope of the agency tenant |
| 3. Class C remediation and package | 2027-01 to 2027-03 | Remaining High and Moderate gaps; parameters; Security Decision Record; Marketplace listing; trust center |
| 4. Independent assessment | 2027-03 to 2027-04 | FedRAMP Recognized assessment service (must be within 3 months before applying) |
| 5. Agency ATO and application | 2027-05 to 2027-06-10 | Agency issues the ATO; company applies directly before the 2027-06-11 Rev5 cutoff |

**The Rev5 schedule has almost no slack.** The agency would have about six weeks to issue an ATO after the assessment, and any slip past 2027-06-11 ends the Rev5 option. Recommendation to the CEO for the 2026-12-31 gate:
- **Proceed on Rev5** only if the agency commits in writing to the schedule.
- **Otherwise, move to 20x Class C Program Certification,** which needs no sponsor and has accepted applications since 2026-08-31. Rulesets such as MAS, VDR, IEC, and SCN appear in both the Rev5 and 20x rule sets, so most of the non-control work above carries over. The Rev5 control list is specific to Rev5.
- **Either way,** the control remediation in phase 1 is needed for the bank customers and the SOC 2 examination (P09).

## 5. Pending regulatory changes
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25. If finalized as proposed, covered entities would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours. Whether a 60-person hosting provider would be covered depends on the final size and sector criteria. Not treated as a current obligation. Flagged on the incident rows.
- **FedRAMP 2026 rules become mandatory on 2027-01-01.** Optional adoption began 2026-07-04. This analysis already uses the 2026 rules, so no rework is expected. FedRAMP publishes rule changes in its changelog; the advisor checks it monthly.
- **End of new Rev5 certifications on 2027-06-11** and the legacy FedRAMP Ready status (no new submissions after 2026-07-28) shape the decision in section 4.3.

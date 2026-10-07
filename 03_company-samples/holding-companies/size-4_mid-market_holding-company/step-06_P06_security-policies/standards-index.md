# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and its subsidiaries |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | vCISO (index and issue schedule), 2026-09-22; each standard is signed by its parent policy's approver when issued |
| Authority | POL-01 statements 4.1 and 4.6; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent, but the group grew faster than its rules: an acquisition joined without any day-1 controls, subsidiaries bought AI tools on their own, and the plant and the self-funded plan had no security procedures (gaps 2, 6, 9, and 12 in `../00_company-facts.md`; P03 GV.SC-06 and 164.316(a); P01 R-007, R-030, R-052). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures (how-to steps) sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts, the Security Manager reviews for consistency, the vCISO approves, and the parent policy's approver signs.
- **Group-wide by default:** every standard applies to all five companies. A subsidiary may add stricter rules in a supplement (Finance does), never weaker ones.
- **Exceptions:** under POL-01 section 4.7, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-22) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | VP of Information Technology | Draft in progress | 2027-03-31 | Benchmark-based baselines for servers, laptops, network devices, cloud images, and SaaS tenants; legacy protocols disabled; monthly drift report; one change process for all Tier 1 systems with peer approval and a weekly change review | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress (gap 8) | 2027-01-31 | Required event types per system class; all SCSP components, the ERP, HRIS, loan servicing, distribution, and field-service systems, file servers, and plant firewall send logs to the SIEM; 1 year searchable and 3 years archived (6 years for plan security records); export alerts over 500 customer records; monthly review of benefits site access | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor and supply chain risk standard** | POL-01 | Director of Procurement with the Security Manager | Draft in progress (gap 5) | 2026-12-31 | Tiers (Tier 1: Restricted data at scale, privileged access, or supports a High BIA process; Tier 2: limited data; Tier 3: no data or access); review before contract, including subsidiary purchases and new features; Tier 1 annual SOC 2 Type 2 review with CUEC mapping and bridge letter; breach notice within 72 hours for Tier 1; exit terms; Finance service provider and plan business associate checks | SA-4, SA-9, SR-2, SR-3, SR-6, SR-8 |
| STD-04 | **Privileged access and identity standard** | POL-02 | Security Manager | New, draft in progress (gap 3) | 2026-12-31 | Directory tier model (Tier 0, 1, 2); dedicated admin workstations for Tier 0; no service accounts in Domain Admins; managed service accounts or vaulted secrets rotated yearly; 2 standing global administrators; break-glass accounts tested quarterly; brokered and recorded vendor sessions; quarterly privileged review | AC-2, AC-6, AC-6(2), AC-6(5), IA-5, MA-4 |
| STD-05 | **AI use standard** | POL-01, POL-05 | CFO with the vCISO | Draft in progress (gap 12) | 2026-12-31 | AI inventory; risk tiering per P10; review before use; no-training terms; human review rules; recording consent; credit and employment uses need validation, outcome testing, and specific reasons (Regulation B 1002.9) before production; monitoring and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator standard | POL-02 | Security Manager | Existing (2024); update due | 2027-03-31 | 14-character minimum and banned list; MFA everywhere; phishing-resistant keys for administrators and payment, HR, benefits, and Finance users; MFA reset with video check and callback | IA-2, IA-2(1), IA-2(8), IA-5 |
| STD-07 | Contingency and recovery standard | POL-03 | VP of Information Technology | Draft in progress (gap 7) | 2026-12-31 | Recovery objectives from the BIA (P05); off-site immutable backups for every on-premises server; quarterly restore tests per workload; yearly directory forest recovery test; BIA workarounds documented per subsidiary | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | VP of Information Technology | Existing (2024); update due | 2027-03-31 | Approved algorithms; TLS 1.2 or higher; encryption at rest for all Restricted data including file servers and NAS; company-managed cloud keys; separate backup keys | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); update due (gap 10) | 2026-12-31 | Monthly authenticated scans at all 9 sites and the cloud; passive discovery on the plant network; remediation targets: Critical 14 days internet-facing and 30 days otherwise, High 60 days; known exploited edge flaws within 72 hours | RA-5, SI-2, SI-5 |
| STD-10 | **Acquisition integration standard** | POL-01 | VP of Corporate Development with the Security Manager | New, draft in progress (gap 2) | 2026-12-31 | Cyber due diligence checklist before signing (incidents, MFA, backups, admin access, regulated data, pending notices); compromise assessment before connection; day-1 control set (EDR, MFA, removal of seller and provider admin access, backup); integration within 180 days | SA-9, RA-3, CA-2 |
| STD-11 | **Plant (operational technology) security standard** | POL-02, POL-04 | Fabrication President with the VP of Information Technology | New, draft in progress (gap 9) | 2027-03-31 | Separate plant floor and office networks with allow-listed flows; isolated segment for unsupported controllers; machine program check-in with hashes and second-person review for new programs; vendor access only through the broker; plant server backed up nightly off-site | SC-7, AC-4, SA-22, MA-4, SI-7 |
| STD-12 | Data retention schedule | POL-04 | General Counsel | Planned (gap 13) | 2026-12-31 | Retention periods by record type for every company; Finance customer information disposed of within 2 years after last use unless an exception applies; ACH files deleted after 90 days; 6 years for security policies, assessments, and plan security records; annual review | SI-12, MP-6 |
| STD-13 | **Group health plan security procedures** | POL-01, POL-04 | VP of Human Resources (plan Privacy Official) with the Security Manager (plan Security Official) | New, draft in progress (gap 6) | 2026-12-31 | Authorized plan staff named; restricted benefits site; no local downloads; monthly access review; TPA portal user review each quarter; plan breach steps (decision log, four-factor assessment); report security incidents to the Benefits Committee | AC-3, AC-6, AU-6, IR-6 |

**Summary:** 13 standards. 3 exist from 2024 and need updates (STD-06, STD-08, STD-09). 9 are in draft (STD-01, STD-02, STD-03, STD-04, STD-05, STD-07, STD-10, STD-11, STD-13), 5 of them new this year (STD-04, STD-10, STD-11, STD-13, and STD-03 replacing the procurement checklist). 1 is planned (STD-12).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Vendor and supply chain; STD-04 Privileged access; STD-05 AI use; STD-07 Contingency; STD-09 Vulnerability and patch; STD-10 Acquisition integration; STD-12 Retention; STD-13 Plan security procedures |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-06 Authenticator; STD-08 Encryption; STD-11 Plant security |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process

# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.7; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent, but staff, network engineers, and vendors had few measurable rules for configuration, logging, network elements, and vendors (gap 15 in `../00_company-facts.md`; P01 R-042, R-043; P07 CM-2, CM-6). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them. This index is an added file for the Mid-Market tier, which calls for policies plus standards for key domains.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 6, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | Security Manager with the Director of Network Engineering | Draft in progress | 2027-03-31 | Benchmark-based baselines for servers, cloud virtual machines, and SaaS tenants; golden configurations for every network element type (core, edge, OLT, DSLAM, cabinet switch, SBC, POP switch); Telnet and HTTP management disabled; SNMPv3 only; monthly drift report; change control through the change advisory board for network, cloud, and Business Services changes, with impact analysis covering 911 circuits | CM-2, CM-3, CM-4, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress | 2027-01-31 | Required event types per system class; network element syslog and TACACS+ accounting, CDR archive object reads, SYS-15, and SYS-18 sent to the SIEM; 1 year searchable and 3 years archived; MDR high-severity escalation within 30 minutes; monthly review of BSS call detail views against care tickets; egress volume alerts on the CDR archive | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor risk management standard** | POL-01 | Security Manager with the Chief Financial Officer | Draft in progress | 2026-12-31 | Vendor tiers (Tier 1: CPNI at scale, privileged or network access, or supports a High-criticality process; Tier 2: limited CPNI or PII; Tier 3: neither); contract terms before access (CPNI confidentiality, training, no AI training on company data, 24-hour incident notice, 10-day Florida third-party notice); Tier 1 annual SOC 2 Type 2 review with CUEC mapping and bridge letter; Tier 2 every 2 years; Covered List check for network equipment | SA-4, SA-9, SR-3, SR-6, RA-3(1) |
| STD-04 | **Network element security standard** | POL-02 | Director of Network Engineering | Draft in progress | 2027-03-31 | Named TACACS+ accounts with MFA on every element type; command authorization by role; administration only from jump hosts; management VLAN not routable from corporate or POP user networks; SYS-10 on an isolated management path; console ports locked and alarmed; vendor access only through the access broker; quarterly rotation of TACACS+ keys and break-glass credentials | AC-2, AC-6, IA-2(1), SC-7, MA-4 |
| STD-05 | **AI use standard** | POL-01, POL-05 | Vice President of Regulatory Affairs with the vCISO | Draft in progress | 2026-12-31 | AI inventory; risk tiering per P10; intake and review before use; no CPNI to AI tools without approval-flag filtering and a no-training contract clause; AI disclosure to customers; human review of outputs; no autonomous network changes; recording and transcription notice; monitoring metrics and decommissioning criteria | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | IT Director | Existing (2024); update due | 2027-03-31 | 14-character minimum and banned list; MFA for all; security keys for administrators of IdP, cloud, network elements, and SYS-10; vaulted and rotated service account secrets; break-glass credentials tested quarterly; SMS fallback removed | IA-2, IA-5, AC-6(2), AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | IT Director with the NOC Director | Draft in progress | 2026-12-31 | Recovery objectives from the BIA (P05); quarterly restore tests per cloud workload; annual bulk restore exercise for network element configurations; annual NOC failover to CO-4; IT contingency plan; hosted voice cluster configuration restore test | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2024); minor update | 2027-03-31 | Approved algorithms and protocols (TLS 1.2 or higher; AES-256 at rest); company-managed keys for cloud workloads; separate backup keys; IPsec parameters for the site-to-cloud VPN with annual key rotation | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager | Existing (2024); update due | 2026-12-31 | Monthly authenticated scans of servers, cloud, and network elements; weekly known-exploited vulnerability review; remediation targets: critical advisories on internet-facing network elements and servers 14 days, other critical 30 days, high 60 days; lifecycle register with end-of-support dates 12 months ahead | RA-5, SI-2, SI-5, SA-22 |
| STD-10 | **911 reliability and facility power standard** | POL-01 | Chief Technology Officer | Draft in progress | 2026-12-31 | Annual diversity audit and tagging of legacy 911 circuits (47 CFR 9.19(c)(1)(ii)); backup power of at least 24 hours at full office load for central offices that directly serve a PSAP, with an annual full-load generator test (9.19(c)(2)(ii)); annual audit of diverse monitoring aggregation points, links, and NOCs (9.19(c)(3)(ii)); 2-year evidence retention (9.20(e)); annual confirmation of PSAP contacts (4.9(h)(1)); facility badge reviews quarterly | PE-11, CP-8, SI-4, PE-3 |

**Summary:** 10 standards. Seven are new or being rewritten (STD-01 to STD-05, STD-07, STD-10). STD-06, STD-08, and STD-09 exist from 2024 and need updates.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Vendor risk; STD-05 AI use; STD-07 Contingency and recovery; STD-09 Vulnerability and patch; STD-10 911 reliability and facility power |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-04 Network element security; STD-06; STD-08 |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process

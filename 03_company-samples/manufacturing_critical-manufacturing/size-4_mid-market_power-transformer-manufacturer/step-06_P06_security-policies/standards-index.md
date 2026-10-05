# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | Security Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-15 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.11; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies stated intent, but there were few measurable rules for configuration, logging, OT, suppliers, or the software the company builds (gap 12 in `../00_company-facts.md`; P03 G-018; P01 R-022 and R-045). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them. At mid-market size the standards also carry the plant-specific detail that does not belong in a policy, so Plant 1 practice can be applied to Plant 2.

## 2. How standards work
- **Hierarchy:** policy (POL) to standard (STD) to procedure or runbook. A standard may not weaken its parent policy.
- **Approval:** the standard's owner drafts it, the Security Manager reviews it for consistency, and the parent policy's approver signs it.
- **Exceptions:** under POL-01 section 4.12, time-limited and recorded in the risk register.
- **Testing:** each standard lists what P07 or internal audit checks.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-15) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **Configuration standard** | POL-01, POL-04 | IT Director | Draft in progress | 2027-03-31 | Benchmark-based baselines for workstations, servers, cloud virtual machines, network devices, MES servers, and kiosks; documented deviations; monthly drift reports for IT and quarterly for plant systems; change advisory board for ERP, integration, and MES interface changes | CM-2, CM-3, CM-6, CM-7 |
| STD-02 | **Logging and monitoring standard** | POL-03 | Security Manager | Draft in progress | 2027-01-31 | Required event types per system class (identity, cloud, ERP, MES, historians, OT sensors, FMS application); all sources in the SIEM; 1 year searchable and 3 years archived; MSSP high-severity escalation within 30 minutes; monthly review of vendor and MSSP sessions | AU-2, AU-6, AU-11, AU-12, SI-4 |
| STD-03 | **Vendor and supplier risk standard** | POL-01 | Security Manager with the Director of Supply Chain | Draft in progress | 2026-12-31 | Supplier tiers (Tier 1: privileged access, product or firmware supply, or support for a High-criticality process); security terms before award; OEM security schedule (remote access, default credentials, patch support, incident notice); annual Tier 1 review with SOC 2 or equivalent, complementary user entity control mapping, and bridge letter; exit checklist | SA-4, SA-9, SR-3, SR-6 |
| STD-04 | **OT security standard** | POL-02, POL-04 | OT Security Engineer with the Director of Manufacturing Engineering | Plant 1 practice written (2025); company-wide draft in progress | 2027-03-31 | Zones and conduits per plant with an OT DMZ; deny-by-default IT/OT rules; OEM access only through the gateway; OT change procedure with Controls Lead approval and a backup before and after each change; weekly automated controller backups with offline copies; allowlisting on HMIs, kiosks, and MES servers; USB control and media scanning; compensating controls for unsupported systems | SC-7, AC-4, MA-4, CM-3, CP-9, SA-22 |
| STD-05 | **AI use standard** | POL-01, POL-05 | vCISO with the Director of Digital Services | Draft in progress | 2026-12-31 | AI inventory; risk tiering per P10; intake for new tools and new AI features in existing software; human review rules; no Restricted data or FCI in unapproved tools; bias testing for any use affecting people; model change control for AI-003 | PM-9, SA-9, PL-4, RA-3 |
| STD-06 | Authenticator and privileged access standard | POL-02 | Security Manager | Existing (2024); update due | 2026-12-31 | 14-character minimum and banned list; MFA for all; FIDO2 keys for all privileged accounts; vaulted service account credentials rotated yearly; no service account in domain administrator groups; break-glass accounts tested quarterly; OT engineering workstation access through the privileged access broker; MES and HMI account procedure | IA-2, IA-5, AC-6, AC-6(5) |
| STD-07 | Contingency and recovery standard | POL-03, POL-04 | IT Director with the Director of Manufacturing Engineering | Draft in progress | 2026-12-31 | Recovery objectives from the BIA (P05); recovery order; quarterly restore tests for the ERP and FMS; annual OT restore test per plant; annual landing zone rebuild exercise; manual operations procedures for each plant | CP-2, CP-4, CP-9, CP-10 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2024); update due | 2026-12-31 | Approved algorithms and protocols (TLS 1.2 or higher); encryption at rest for Restricted data; company-managed keys per account; code signing keys only in the hardware-backed key service with 2-person approval | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Vulnerability and patch management standard | POL-01 | Security Manager with the OT Security Engineer | Existing (2024, IT only); OT section due | 2026-12-31 | Monthly authenticated IT scans; weekly known-exploited vulnerability review; IT targets: critical internet-facing 14 days (48 hours for known-exploited edge devices), other critical 30 days, high 60 days; OT: passive vulnerability matching and quarterly OEM-approved patch reviews | RA-5, SI-2, SI-5 |
| STD-10 | **Secure development and product security standard** | POL-01 | VP Engineering with the Director of Digital Services | Draft in progress | 2027-03-31 | Practices aligned to the NIST Secure Software Development Framework (SP 800-218): protected repositories and build systems, mandatory code review, dependency scanning, security testing before release, SBOM per release, hardware-backed signing, vulnerability intake and 30-day disclosure to addendum utilities, annual penetration test of the FMS portal | SA-8, SA-11, SI-7, SR-11, RA-5 |

**Summary:** 10 standards. The 6 new standards requested in the gap analysis (STD-01, STD-02, STD-03, STD-05, STD-07, STD-10) are in draft. STD-04 extends Plant 1's 2025 practice to the company. STD-06, STD-08, and STD-09 exist from 2024 and need updates (OT, signing keys, and OT patching).

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-03 Vendor and supplier risk; STD-05 AI use; STD-06 Authenticator and privileged access; STD-07 Contingency and recovery; STD-08 Encryption and key management; STD-09 Vulnerability and patch management |
| 2027 Q1 | STD-01 Configuration; STD-02 Logging and monitoring; STD-04 OT security; STD-10 Secure development and product security |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process

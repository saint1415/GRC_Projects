# Security Standards Index

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | GRC Manager (index); each standard has its own owner below |
| Approved by | Chief Operating Officer, 2026-09-17 (index and issue schedule) |
| Authority | POL-01 statements 4.1 and 4.8; each standard sits under the parent policy named below |
| Review cycle | Each standard is reviewed at least annually by its owner |

## 1. Why this index exists
The 2024 policies were written mainly for IT and had few measurable rules for OT, so plant staff and OEMs had nothing concrete to follow for remote access, backups, or patching (P03 G-001, G-051, G-053). Policies say **what** must happen. Standards set the **measurable minimums**: settings, frequencies, and thresholds. Procedures and runbooks sit under the standards and are owned by the teams that run them.

## 2. How standards work
- **Hierarchy:** policy (POL), then standard (STD), then procedure or runbook. A standard may not weaken its parent policy, a FERC requirement, or a NERC requirement.
- **Approval:** the owner drafts, the GRC Manager reviews for consistency, the OT Security Manager reviews anything that touches OT, and the parent policy's approver signs. Standards that implement CIP-003-9 topics are also approved by the CIP Senior Manager.
- **Exceptions:** under POL-01 section 4.4, time-limited and recorded in the risk register.
- **Testing:** P07 and internal audit check each standard once issued.

## 3. Standards
| ID | Standard | Parent policy | Owner | Status (2026-09-17) | Target issue date | Key minimum requirements | Main SP 800-53 controls |
|---|---|---|---|---|---|---|---|
| STD-01 | **OT network segmentation and remote access standard** | POL-02 | OT Security Manager | Draft in progress (gaps 2, 3) | 2026-12-31 | Per-site OT zones and a separate RMOS zone; conduits only through site firewalls; deny by default with a documented reason for every rule (CIP-003-9 Section 3.1); all remote access through the jump hosts with MFA, ROC approval, recording, and weekly vendor log review; no direct VPNs or panel modems; connection register reviewed every 12 months | SC-7, AC-4, AC-17, MA-4 |
| STD-02 | **OT configuration and change management standard** | POL-01, POL-02 | Manager of Controls Engineering | Draft in progress (gap 7) | 2027-03-31 | Baselines for every Critical cyber asset at all 4 projects; change board with security impact review (POL-01 4.9); OEM changes only through the board; monthly logic hash comparison at all plants; test on the SCADA vendor test system | CM-2, CM-3, CM-4, CM-6, SI-7 |
| STD-03 | **Vendor, client, and acquisition security standard** | POL-01 | GRC Manager | Draft in progress (gap 9) | 2026-12-31 | Tiers for OT vendors and RMOS clients; contract security schedule (24-hour incident notice, remote access rules, data return, recovery support); security requirements in OT purchases; annual review of Tier 1 vendors and of every client connection; SOC 2 review method (P09) | SA-4, SA-9, SR-6, PS-7 |
| STD-04 | **OT access, account, and authenticator standard** | POL-02, POL-05 | OT Security Manager | Draft in progress (gap 6) | 2027-03-31 | Named accounts on every HMI; quarterly operator and monthly administrator reviews; inactivity disable at 35 days; unique vaulted local administrator passwords; default password check before connection; control system hosts used only for approved activities | AC-2, AC-6, IA-2, IA-5, CM-7 |
| STD-05 | **Logging and monitoring standard (IT and OT)** | POL-03 | OT Security Manager with the IT Director | Draft in progress (gap 4) | 2027-01-31 | Event types per system class; OT sensors at every project; plant HMI and firewall logs to the SIEM; 1 year searchable, 3 years archived; MSSP OT playbooks with 30-minute escalation for OT alerts | AU-2, AU-6, AU-11, SI-4 |
| STD-06 | **OT backup and recovery standard** | POL-03 | Manager of Controls Engineering | Draft in progress (gap 7) | 2026-12-31 | Backups of every PLC, governor, exciter, HMI, and SCADA server after each change and at least monthly; offline copies quarterly; governor settings held by the company, not only the OEM; annual restore test per plant and an ROC cyber recovery test; recovery objectives from the BIA (P05) | CP-2, CP-4, CP-9, CP-10 |
| STD-07 | **OT vulnerability and patch management standard** | POL-01 | OT Security Manager | Draft in progress (gap 5) | 2026-12-31 | Outside vulnerability assessment of every Critical cyber system at least every 12 months (Rev. 3A Table 9.3b); weekly CISA ICS advisory review; quarterly patch cycle after vendor qualification; compensating controls and a replacement date for unsupported hosts | RA-5, SI-2, SI-5, SA-22 |
| STD-08 | Encryption and key management standard | POL-04 | IT Director | Existing (2024); minor update | 2027-03-31 | TLS 1.2 or higher; IPsec with certificates for site-to-site tunnels; encryption at rest for Confidential and Restricted data; company-managed cloud keys; ICCP protection per the CIP-012 plan | SC-8, SC-12, SC-13, SC-28 |
| STD-09 | Removable media and transient cyber asset standard | POL-05 | OT Security Manager | Existing (2024, CIP-003 Section 5); extend to PNH and SGR | 2026-12-31 | Media kiosks at every project; transient asset checks for company and vendor laptops; hardened field engineering laptops for client sites | MP-7, MA-3, SI-3 |
| STD-10 | **CEII and information handling standard** | POL-04 | Chief Dam Safety Engineer with the Corporate Security Manager | Draft in progress (gap 10) | 2026-11-30 | Restricted library with named access; marking rules; CEII filing procedure with FERC; data lake classification tags; download alerts and monthly review | AC-3, MP-3, RA-2, AU-6 |
| STD-11 | **AI use and model risk standard** | POL-01, POL-04 | Data Analytics Lead with the vCISO | Draft in progress (gap 12) | 2026-12-31 | AI inventory and tiering (P10); validation before use; model registry and version control; monitoring thresholds; no AI command path to OT; approved-tools list for generative AI | PM-9, CA-7, CM-3, SA-9 |
| STD-12 | Physical security of cyber assets standard | POL-02 | Corporate Security Manager | Existing (Security Plans); add tamper detection for gate panels | 2027-03-31 | Card access and alarms for control rooms, firewall rooms, gate houses, and instrument houses; quarterly access reviews; tamper switches on remote gate panels | PE-2, PE-3, PE-6 |

**Summary:** 12 standards. 9 are new and in draft (STD-01, STD-02, STD-03, STD-04, STD-05, STD-06, STD-07, STD-10, STD-11); the other 3 exist and need updates. The bold standards close the largest gaps from P03 and P07.

## 4. Issue schedule
| Quarter | Standards |
|---|---|
| 2026 Q4 | STD-01 OT segmentation and remote access; STD-03 vendor, client, and acquisition; STD-06 OT backup and recovery; STD-07 OT vulnerability and patch; STD-09 media and transient assets; STD-10 CEII handling; STD-11 AI use |
| 2027 Q1 | STD-02 OT configuration and change; STD-04 OT access and accounts; STD-05 logging and monitoring; STD-08 encryption; STD-12 physical security of cyber assets |

## 5. Related documents
POL-01 to POL-05; `policy-control-map.csv`; P03 roadmap; P07 POA&M; P10 AI governance process

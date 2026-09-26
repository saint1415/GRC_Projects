# Risk Register Report: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radioactive and hazardous waste processor, NAICS 562211) |
| Size tier | Small (60 employees) |
| Vertical | Nuclear Reactors, Materials, and Waste |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | Part 37 security program review (10 CFR 37.55) and access authorization program review (37.33), as imposed by the Florida license condition; NIST CSF 2.0 GV.RM and ID.RA outcomes |
| Prepared | 2026-07-24 by the IT Manager with the Radiation Safety Officer |
| Approved | 2026-08-31 by the General Manager (Moderate and below) and the President (High) |

## 1. Scope and risk framing
**Scope.** The Business Operations and Records Platform (BORP) in the SSP (P02), the business processes in the BIA (P05), and the systems connected to them: the plant OT network, the radiation monitoring systems, the physical security systems that protect the sealed source vault, and the predictive maintenance pilot (`../scenario-facts.md` section 3).

**What makes this company different.** Its sealed source vault holds an aggregated category 2 quantity of radioactive material several times a year, so the Florida license condition applies 10 CFR Part 37. Part 37 is a physical protection rule, but three of its duties depend on IT: protecting the security plan and access lists (37.43(d)), keeping security system communications and data transmission running with an alternate path (37.49(c)), and keeping records safe from tampering and loss (37.101). A cyber event at this company can therefore become a radioactive material security event.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager or the Radiation Safety Officer may accept, each in their own area.
- Moderate: the General Manager may accept, with a treatment plan or a documented reason.
- High and Very High: only the President may accept, and only temporarily with a dated treatment plan. A risk that could lead to theft, diversion, or sabotage of category 2 material may not be accepted at High.

This is the company's first documented cybersecurity risk assessment. The Part 37 program had its own security reviews, but they did not cover electronic systems.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, SP 800-82 Rev. 3 Appendix C (OT threat sources and vulnerabilities), the BIA, the gap analysis (P03), interviews (General Manager, RSO, Operations Manager, Maintenance and Controls Supervisor, Compliance and Transportation Manager, HR Manager, Controller), and a Plant walkthrough on 2026-07-21.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) and likelihood of adverse impact were rated separately and combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3** and the BIA impact categories, including the regulatory category (license violations and reportable events).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 5 |
| Moderate | 17 |
| Low | 10 |
| **Total** | **32** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware via phishing encrypts office endpoints, files, and cloud workloads | High | Phishing exercises; network segmentation; isolated backups | IT Manager | 2027-01-31 |
| R-002 | Pivot from the business network to plant OT through the dual-homed historian | High | Remove the second network card; historian replica in a DMZ | Operations Manager | 2026-12-31 |
| R-003 | Business network outage takes down PACS and video for the vault at the same time | High | Isolated security VLAN with UPS; local alarm annunciator; update the security plan | General Manager | 2026-12-15 |
| R-004 | Security plan and approved-individuals list obtained from a broadly shared folder | High | Restricted library; information protection procedure; access list | Radiation Safety Officer | 2026-09-30 |
| R-007 | Backups destroyed along with production | High | Immutable, separate-account, second-region backups; quarterly restore tests | IT Manager | 2026-12-31 |
| R-006 | Vendor remote access to PLCs with a shared account and no MFA | Moderate | Per-session access, named accounts, MFA, recording | Maintenance and Controls Supervisor | 2026-10-31 |

The five High risks share one theme: **the business network is a single point of failure for things that are not business systems.** The vault's badge control and video (R-003), the OT network (R-002), and the only copies of key records (R-007) all depend on it, and the network has weak defenses against the most likely attack (R-001). The security plan itself sits on that network with broad access (R-004). Fixing the High risks also lowers eight related Moderate risks (R-005, R-006, R-008, R-013, R-014, R-016, R-022, R-031).

R-031 was added on 2026-08-07 after control assessment testing (P07) found manufacturer default passwords on 5 IP cameras.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1 budget, $92,000):**
  - Security VLAN for the PACS, NVR, and cameras, with its own firewall and UPS
  - Historian DMZ replica and removal of the dual-homed connection
  - Secure vendor remote access with MFA and session recording
  - Backup redesign (separate account, immutable, second region)
  - Vulnerability scanning through the MSP
  - Replacement of 2 unsupported HMIs (2027 Q1)
- **No-cost actions due first (September to October 2026):** restricted library for security-related information (R-004), background file access (R-010), default camera passwords (R-031), Part 37 event procedure contacts (R-020), termination-linked access removal (R-009).
- **Accepted:**
  - R-023: hardware keys already reduce it to Low
  - R-029: Low, vendor-managed
  - R-032: Low, laptops are encrypted
- **Regulatory actions:** complete the overdue 37.33 access authorization review and a 37.55 security program review that includes electronic systems before the next State inspection (R-005), due 2026-10-31.

## 5. Approval
- General Manager: approved Moderate and Low treatments and acceptances, 2026-08-31.
- President: approved the High-risk treatment plans and the budget, 2026-08-31.
- Next full review: July 2027, or sooner after a major change, an incident, or a change to the license.

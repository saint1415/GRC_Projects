# Risk Register Report: Cris Santos Company | Communications | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (regional broadband and wired telecommunications carrier) |
| Size tier | Small (250 employees) |
| Vertical | Communications (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Regulatory link | Supports the CPNI duty to take "reasonable measures to discover and protect against attempts to gain unauthorized access to CPNI" (47 CFR 64.2010(a)); outage and 911 duties (47 CFR Part 4); CALEA SSI (47 CFR 1.20003) |
| Prepared | 2026-07-31 by the IT Manager (security and compliance lead) with the Network Engineering Manager and Regulatory Affairs Manager |
| Approved | 2026-09-04 by the COO (Moderate and below) and the Chief Executive Officer (High) |

## 1. Scope and risk framing
**Scope.** The Network Operations and Customer Billing Platform (OSS/BSS) defined in the SSP (P02), the voice and broadband network it manages (SYS-07, SYS-08), the lawful-intercept system (SYS-10), the contact center and chatbot (SYS-11, SYS-12), and the vendors that handle CPNI (`../00_company-facts.md` section 3). The business processes are those in the BIA (P05).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the COO may accept, with a treatment plan or a documented reason.
- High and Very High: only the Chief Executive Officer may accept, and only temporarily with a dated treatment plan. Risks to 911 call completion or to lawful-intercept confidentiality rated High may not be accepted without a treatment plan.

This is the company's first documented security risk assessment. Earlier reviews covered storm and network availability only.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, public reporting on intrusions into U.S. carriers (the FCC's 2025 order on reconsideration describes the "Salt Typhoon" campaign that "exploited publicly known common vulnerabilities and exposures"; 90 FR 58006), the BIA, the gap analysis (P03), and interviews with the NOC, customer operations, and regulatory staff.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the P05 impact categories (cost, operations, regulatory, public safety, reputation).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 6 |
| Moderate | 18 |
| Low | 10 |
| **Total** | **34** |

No risk is rated Very High. Two risks have a Very High impact (R-007 network-wide outage and R-013 lawful-intercept compromise), but their overall likelihood is Moderate, so Table I-2 gives High.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Known vulnerability in an edge router or the unsupported SBC is exploited | High | Patch edge routers; isolate then replace the SBC; authenticated scans | Network Engineering Manager | 2026-11-30 |
| R-002 | Intruder crosses the management plane and steals call detail records (P08 scenario) | High | Segmentation; scoped mediation service account; managed detection; shorter CDR retention | IT Manager | 2027-01-31 |
| R-003 | Online account takeover through the SSN4 and date-of-birth password reset | High | One-time-code reset to the number or email of record; reset alerts | IT Manager | 2026-11-30 |
| R-007 | Network elements wiped or reconfigured through shared admin accounts, causing an outage that includes 911 | High | Named TACACS+ accounts with MFA on every element type; jump hosts | Network Engineering Manager | 2026-12-31 |
| R-008 | Ransomware destroys cloud workloads and same-account backups | High | Separate immutable backup account in a second region; quarterly restore tests | IT Manager | 2026-12-31 |
| R-013 | Lawful-intercept system compromised | High | Isolated management path for SYS-10; compromise reporting to law enforcement (1.20003(c)) | Vice President of Network Operations | 2026-12-31 |

The six High risks share one theme: **the network's management plane and CPNI stores are exposed to the same intrusion path that has been used against larger carriers.** Unpatched edge devices give entry (R-001). Shared credentials and flat routing let an intruder reach network elements, the mediation archive, and the lawful-intercept system (R-002, R-007, R-013). Nobody would see it (R-010), and the backups might not survive (R-008). The customer-facing High risk (R-003) is separate: the CPNI authentication rules are not met online.

Fixing the management plane (segmentation, named accounts, monitoring) also reduces six Moderate risks (R-009, R-010, R-019, R-020, R-025, R-032) and one Low risk (R-026).

R-032 was added on 2026-08-13 after control assessment testing (P07) found vendor-default SNMP community strings on 11 cabinet switches.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1, $318,000 approved by the Chief Executive Officer):**
  - Managed detection and response with SIEM and 1-year log retention ($96,000 per year)
  - Replacement of the CO-1 session border controller ($85,000)
  - Management plane segmentation, jump hosts, and TACACS+ expansion ($44,000)
  - Portal and app password reset redevelopment ($35,000)
  - Separate immutable backup account and second-region copies ($14,000 per year)
  - CPNI and security training content for staff and vendor agents ($9,000)
  - Outside counsel for the CPNI certification review and CALEA refiling ($20,000)
  - Always-on DDoS scrubbing from the upstream transit provider ($15,000 per year)
- **Capital plan (2027):** diverse fiber route between CO-1 and CO-2 (R-016).
- **Accepted:**
  - R-023: Moderate, accepted by the COO. The BSS vendor's stated RTO meets the BIA (P09)
  - R-024: Low, accepted by the IT Manager
  - R-030: Low, accepted by the IT Manager (MDM wipe and encryption)
  - R-031: Low, accepted by the IT Manager (hardware keys)
- **Shared:** R-027 DDoS, through the upstream provider's scrubbing contract.
- **Contract actions:** CPNI, security, and 24-hour incident notice terms for the chatbot vendor, CCaaS vendor, and overflow call center (R-022), due 2026-12-31.

## 5. Approval
- COO: approved Moderate and Low treatments and acceptances, 2026-09-04.
- Chief Executive Officer: approved the High-risk treatment plans and the budget, 2026-09-04.
- Next full review: July 2027, or sooner after a major change (SBC replacement, TDM switch retirement, chatbot general launch) or an incident.

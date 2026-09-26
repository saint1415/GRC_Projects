# Risk Register Report: Cris Santos Company | Information Technology | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (cloud hosting and managed infrastructure provider) |
| Size tier | Small (60 employees) |
| Vertical | Information Technology (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | RA-3 in the FedRAMP Rev5 Class C control list (P03); SOC 2 CC3.2 (P09) |
| Prepared | 2026-07-31 by the IT Manager (Information Security Officer) with the FedRAMP advisor |
| Approved | 2026-09-25 by the COO (Moderate and below) and the CEO (High and Very High) |

## 1. Scope and risk framing
**Scope.** The Hosting Control Plane and Customer Portal (HCP) defined in the SSP (P02), the private cloud platform it manages (SYS-05), the edge network and DNS (SYS-09), and the business processes in the BIA (P05). Vendors that operate parts of the service (colocation providers, the public cloud provider, the RMM and SIEM vendors) are in scope as sources of risk.

**What makes this business different.** A hosting provider's tools reach into hundreds of customer environments. One compromised administrative tool can harm every customer at once, so the register rates impact against all customers, not just the company.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the COO may accept, with a treatment plan or a documented reason.
- High and Very High: only the CEO (majority owner) may accept, and only temporarily with a dated treatment plan. Risks that could let one attacker reach many customers at once may not stay at High beyond their due date.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews with the platform, control plane, NOC, and managed services leads, the FedRAMP readiness gap analysis (P03), and the vertical's incident scenario (compromise of provider tooling affecting downstream customers).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. Harm to many customers at once is rated Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 6 |
| Moderate | 17 |
| Low | 8 |
| **Total** | **32** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Stolen RMM technician session pushes a malicious script to managed customer servers | Very High | Retire shared accounts; IP restriction; two-person approval for multi-customer scripts; RMM logs to the SIEM | Managed Services Lead | 2026-11-30 |
| R-002 | Control plane service credentials used to delete or copy any customer VM | High | Separate production account; short-lived scoped credentials; bulk-action alerts | Engineering Manager (Control Plane) | 2027-02-28 |
| R-003 | Takeover of hypervisor managers or BMCs from the management network | High | Federate to the IdP with MFA; named admin accounts; BMCs reachable only from the bastion | Director of Platform Engineering | 2026-12-31 |
| R-004 | Destructive attack deletes the control plane and its backups | High | Immutable backups in a separate account and region; hourly snapshots | Engineering Manager (Control Plane) | 2026-12-31 |
| R-006 | Unpatched hypervisor or BMC vulnerability exploited | High | Monthly authenticated scans; upgrade the lagging cluster; BMC firmware cycle | Director of Platform Engineering | 2027-01-31 |
| R-011 | Malicious code in the CI/CD pipeline or a VM template | High | Signing key into an HSM; block review bypass; isolated build account | Engineering Manager (Control Plane) | 2027-03-31 |
| R-018 | Hurricane takes DC-1 offline; 70% of customer VMs have no provider-side replica | High | Site failover plan and exercise; replication offer before hurricane season | Director of Platform Engineering | 2027-05-31 |

**Common theme: one tool, many customers.** Four of the seven highest risks (R-001, R-002, R-003, R-011) are paths where a single stolen credential or poisoned build reaches every customer. They share the same fixes: no shared or standing administrator access, MFA at every administrative layer, and logs from those layers in the SIEM. Fixing them also lowers five related Moderate risks (R-009, R-010, R-015, R-025, R-026).

**Recovery is the second theme.** R-004 and R-018 show that the company could not recover the control plane or DC-1 within the BIA targets today (P05 findings 1 and 2).

R-026 was added on 2026-08-18 after control assessment testing (P07) found manufacturer default administrator accounts enabled on 2 BMCs at DC-2. The accounts were disabled on 2026-08-19; the status stays In progress until all 96 hosts are checked by 2026-09-30.

**Very High acceptance.** The CEO accepted R-001 temporarily on 2026-09-25 with the dated plan above. Shared RMM accounts are to be retired by 2026-10-15, the first milestone (P07 POAM-002).

## 4. Treatment summary
- **Funded (2026 Q4 to 2027 Q2 budget, $420,000; the independent FedRAMP assessment is budgeted separately and depends on the sponsor decision in R-023):**
  - Security engineer hire (2027 Q1)
  - SIEM expansion for hypervisor, BMC, network, and RMM logs with 1-year retention
  - Separate backup and build accounts in the cloud tenant; cloud HSM for the signing key
  - Authenticated vulnerability scanning tool
  - Hypervisor cluster upgrade and BMC firmware cycle
  - SOC 2 Type 1 audit (P09)
- **Accepted:**
  - R-014: hardware security keys already reduce it to Low
  - R-021: Low; two carriers per site
  - R-032: Low; full-disk encryption, EDR, and remote wipe
- **Contract actions:** bank-designated points of contact (R-022, due 2026-10-31); security and incident notice terms with the RMM and SIEM vendors (R-025, due 2026-12-31).

## 5. Approval
- COO: approved Moderate and Low treatments and acceptances, 2026-09-25.
- CEO: approved the Very High and High treatment plans and the budget, 2026-09-25.
- Next full review: July 2027, or sooner after a major change, a FedRAMP sponsor decision, or an incident.

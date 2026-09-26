# Risk Register Report: Cris Santos Company | Utilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electric distribution utility, NERC-registered Distribution Provider) |
| Size tier | Small (250 employees) |
| Vertical | Utilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | CIP-003-9 R2 cyber security plan for low impact BES Cyber Systems; voluntary NIST CSF 2.0 profile for the distribution SCADA |
| Prepared | 2026-07-31 by the IT Manager (Information Security Lead) with the NERC Compliance Coordinator; R-031 added 2026-08-12 |
| Approved | 2026-09-04 by the President and CEO (Moderate and below) and the majority owner (High) |

## 1. Scope and risk framing
**Scope.** The Distribution Operations Platform (DOP) described in the SSP (P02), the customer systems (AMI, CIS, portal), the corporate network, the cloud tenant, and the business processes in the BIA (P05). See `../scenario-facts.md` section 3 for the system list.

**Two kinds of obligation shape this register:**
- **Binding:** NERC CIP-002-5.1a and CIP-003-9 apply to the low impact relays at Substation N and Substation E (P03). Fla. Stat. 501.171 applies to customer personal information.
- **Voluntary:** the distribution SCADA and OMS are outside CIP scope for a Distribution Provider (CIP-003-9 section 4.2.3.4). The company protects them against NIST CSF 2.0 with SP 800-82 Rev. 3, because they carry most of the operational risk.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the President and CEO may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan.
- Risks to public or worker safety rated High are not acceptable without a dated treatment plan.
- A known noncompliance with a NERC Reliability Standard is never accepted as a risk. It is remediated and self-reported.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews with the Manager of System Operations, the Manager of Engineering and Protection, and the SCADA/OT Administrator, substation walkthroughs on 2026-07-28, and the gap analysis (P03).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. Loss of control of distribution breakers or BES protection is rated Very High because it can cause wide outages and endanger line crews working under clearances.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 19 |
| Low | 8 |
| **Total** | **31** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Unauthorized SCADA commands through the shared vendor account on the OT jump host | High | Named vendor accounts with MFA; on-request, time-limited sessions; session monitoring | Vice President of Operations | 2026-11-30 |
| R-002 | Ransomware crosses the IT/OT firewall into SCADA | High | Deny-by-default firewall rule base; all IT/OT flows through the OT DMZ | IT Manager | 2026-12-31 |
| R-006 | SCADA cannot be restored because backups are lost with production or never worked | High | Offline, immutable copies; quarterly restore tests | SCADA/OT Administrator | 2026-12-31 |
| R-009 | Stolen VPN password opens the corporate network and a path to the OT jump host | High | VPN authentication through the identity provider with MFA | IT Manager | 2026-11-15 |
| R-003 | Relay settings changed through the vendor access path (BES protection misoperation) | Moderate | CIP-003-9 Section 6 methods; relay password rotation | Manager of Engineering and Protection | 2026-11-30 |
| R-004 | SERC finds CIP-003-9 noncompliance before the company self-reports | Moderate | Self-report by 2026-09-30 with mitigation plans | NERC Compliance Coordinator | 2026-09-30 |

The four High risks share one theme: **an intruder could reach the distribution SCADA, and the company could not detect it or recover quickly.** Remote access is weak (R-001, R-009), the IT/OT boundary is porous (R-002), and SCADA recovery is unproven (R-006). Fixing these four also reduces seven related Moderate risks (R-003, R-005, R-007, R-020, R-021, R-022, R-031) and one Low risk (R-030).

R-031 was added on 2026-08-12 after control assessment testing (P07) found that the Substation E gateway access list permitted any routable traffic from the OT network to the low impact relays. The list was corrected on 2026-08-13.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 budget, $246,000):**
  - Passive OT network monitoring and log collection ($60,000 per year)
  - HMI and historian upgrade to a vendor-supported operating system ($85,000)
  - Jump host MFA, session approval, and recording ($25,000)
  - IT/OT firewall redesign support ($15,000)
  - Offline SCADA backups and a spare restore-test server ($20,000)
  - Two removable media scanning kiosks ($6,000)
  - Rekeying of 22 substation control houses ($12,000)
  - Facilitated OT incident tabletop ($8,000)
  - Phishing training for field and DCC staff ($9,000)
  - Satellite backup terminals for 4 crew leader trucks ($6,000)
- **Accepted:**
  - R-016: Low; phishing-resistant MFA and a separate backup account already in place
  - R-026: Low; vendor-managed
- **Contract actions:** security terms (incident notice, remote access, bulk-command limits) for the SCADA, OMS, and AMI vendors at renewal (R-010, R-021), and SSN retention limits with the CIS vendor (R-012).
- **Regulatory action:** self-report to SERC by 2026-09-30 (R-004).

## 5. Approval
- President and CEO: approved Moderate and Low treatments and acceptances, 2026-09-04.
- Majority owner: approved the High-risk treatment plans and the budget, 2026-09-04.
- CIP Senior Manager: reviewed the CIP-related risks (R-001, R-003, R-004, R-005, R-013, R-022, R-025, R-028, R-031), 2026-09-04.
- Next full review: July 2027, or sooner after a major change, a Reportable Cyber Security Incident, or a change to the CIP-002 identifications.

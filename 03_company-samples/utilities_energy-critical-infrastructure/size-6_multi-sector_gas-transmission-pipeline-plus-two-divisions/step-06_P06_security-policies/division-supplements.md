# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-22 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | One severity scale, MFA, no persistent vendor tunnels, SSI handling rules, TSA plan discipline | Board risk committee or Group CISO |
| Group standards | OT security standard (SP 800-82 Rev. 3 aligned), logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (TSA plan measures, control room rules, gathering field standards, SSI program for client data) | Division president, after Group CISO alignment review |
| Division procedures | Control room management manual, emergency plans, field procedures, runbooks | Division security and compliance lead with the operations owner |

**Where the TSA plan fits.** For Gas Transmission, the TSA-approved Cybersecurity Implementation Plan sets the measures TSA inspects against. The Gas Transmission supplement points to the plan by section number (the plan itself is SSI) and must never conflict with it. If group policy changes a measure in the plan, the change waits for TSA approval of an amendment (POL-01 4.7).

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Gas Transmission | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Confirm alignment; add the 192.631(f) link for analytics changes (POAM-026) |
| Gathering and Production | v2023 | 2023-04 | **Drifted** (scenario gap 10); 6 conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-018) |
| Integrity Services | v2025 | 2025-10 | Aligned on paper, but has no SSI annex, so POL-04 4.2 to 4.4 and 4.7 are not implemented in the division (scenario gap 2) | SSI annex by 2026-12-31 (POAM-019, POAM-020) |

## 3. What each supplement adds
### 3.1 Gas Transmission supplement (TSA-designated interstate pipeline)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| TSA plan register | Every plan measure has an owner, a schedule, and evidence; slips reported to the Coordinator within 5 business days; amendment requests within 50 days of a permanent change | POL-01 4.7 | SD 02G II.B.2, VI.B to VI.D |
| Station unit control panels | Shared panel accounts limited to qualified station technicians; passwords changed on the plan schedule and after any departure; documented mitigations for panels that cannot be reset | POL-02 4.2, 4.3 | SD 02G III.C.1, III.C.4 |
| Control room consoles | Named local SCADA accounts tied to SYS-G1 identities; no MFA on consoles; compensating controls (staffed room, badge and PIN, video, allowlisting) | POL-02 4.5 | SD 02G III.C.2 |
| Change control | All SCADA, station logic, display, alarm, and analytics changes through control room management of change with point-to-point verification before release | POL-01 4.8 | 192.631(c)(2), (f) |
| Controller training | Cyber-caused abnormal operating conditions in simulator training each year | POL-05 4.3 | 192.631(h)(1) |
| Patching | KEV patches within the plan timeline; deviations approved by the Coordinator; written mitigations and dates for unpatchable OT | POL-01 4.7 | SD 02G III.E.2.b, III.E.3 |
| Operate-or-shut-down | Decision criteria and authority for a precautionary segment shutdown (P08) | POL-03 4.4, 4.5 | SD 02G III.F.1.d; 192.615(a)(6) |
| Notices | CISA (SD 01G), PHMSA (191.5), FERC (260.9), SSI disclosure (1520.9(c)); one owner per clock per shift | POL-03 4.6 | SD 01G II.C; 191.5; 260.9 |
| Log retention | 1 year for all OT DMZ and firewall logs, including regional DMZs | POL-01 4.1 | SD 02G III.D.3.b |

### 3.2 Gathering and Production supplement (not TSA-designated; CSF 2.0 and SP 800-82 Rev. 3 benchmark)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Field device commissioning | Checklist confirms default credentials changed, management restricted to the private APN, and the device inventoried before connection | POL-02 4.4 | N21-BM (PR.AA-01; PR.IR-01) |
| Acquired assets | Within 90 days of closing: vendor access moved to the gateway, logs to the SIEM, inventory and flow survey done; migration plan with a date | POL-02 4.7 | N21-BM (PR.AA-03; DE.CM-06) |
| Emergency plans | Type C emergency plans include a loss-of-SCADA scenario | POL-03 4.3 | 192.9(e)(1)(iv); 192.615 |
| Part 191 notices | The 191.3 significance judgment is made for any cyber-caused shutdown, with the 1-hour notice clock | POL-03 4.6 | 191.5 |
| Royalty owner data | No exports of owner payment files; reports used in the SaaS; disposal per POL-04 4.8 | POL-04 4.8 | State breach |
| AI and automation | No AI write-back to compressor or choke setpoints without Group AI council approval and a safety management of change | POL-01 4.13 | N21-BM (ID.RA-07) |

### 3.3 Integrity Services supplement (covered person under Part 1520; SOC 2 service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| SSI annex (due 2026-12-31) | SSI owner; register of SSI sets by client; need-to-know groups; separate SSI store; marking templates; intake, referral, destruction, and disclosure-report steps | POL-04 4.2, 4.3 | 1520.9; 1520.11; 1520.13; 1520.19 |
| Assessment evidence | Evidence store only; toolkit wipe at close; deletion 30 days after close with certificates | POL-04 4.7 | 1520.19(b); client contracts |
| Authorized representative terms | Contract addendum with each TSA-designated client naming the SD measures performed and the evidence kept | POL-01 4.10 | SD 02G II.A.4 |
| Independence | The OT Assessment Practice does not assess group divisions for TSA purposes | POL-01 4.9 | SD 02G III.G.2.b |
| Client notices | Register of each client's notice term (standard 72 hours from confirmation; shorter where negotiated) | POL-03 4.6 | Client contracts |
| Client access | MFA for all IDP client users by 2027-03-31; tenant isolation tests each release | POL-02 4.12 | Client contracts; SOC 2 (P09) |
| AI in deliverables | AI-assisted analysis disclosed to clients and reviewed by a qualified engineer before release | POL-05 4.9; POL-01 4.13 | Client contracts; FTC Act Section 5 |

## 4. Gathering and Production drift: conflicts with 2026 group policy
The 2023 Gathering and Production standards were written before the 2026 group policies and before the Arkoma acquisition. Where they conflict, **group policy governs now** (POL-01 4.5), but field staff follow the document they know, so the conflicts are real risks (P01 GP-011; P07 PL-01 results).

| Topic | Gathering standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Vendor remote access | Vendor-managed connections allowed with an annual review | Gateway only, per-session enablement, MFA, recording (POL-02 4.7) | Always-on Arkoma vendor access was treated as compliant (scenario gap 4) |
| Shared accounts | Shared field accounts allowed for crews | Shared accounts only where critical, registered, changed on departure (POL-02 4.1, 4.2) | Shared accounts on Arkoma SCADA |
| Default credentials | Not addressed | Changed before connection (POL-02 4.4) | Default passwords found at Arkoma (P07) |
| Incident severity | Division 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation |
| Common control inheritance | Not addressed | Division documents inheritance yearly (POL-01 4.6) | Scenario gap 7 (POAM-017) |
| AI and automation | Not addressed | AI inventory and approval (POL-01 4.13) | Setpoint optimization proposed without review (P10) |

**Why the drift happened.** The supplement had an owner but no review date, and the Arkoma acquisition absorbed the division's security staff in 2025. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Gas Transmission, Integrity Services) and on re-issue (Gathering and Production).

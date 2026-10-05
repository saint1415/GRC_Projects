# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-17 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy, supplements, and regulator-approved programs fit together
| Layer | Examples | Who approves |
|---|---|---|
| Regulator-approved programs | Station CSPs (73.54), SGI programs (73.21-73.22), access authorization programs (73.56), NERC CIP program, Florida Part 37 security plan, DOT security plan | The program owner, under the regulator's process (for example a license amendment for CSP changes that reduce effectiveness) |
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, assignment-bound cross-division access, no shared-service path to protected systems | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards for business systems | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

**Where the layers meet.** Group policy never overrides a regulator-approved program. When group policy is stricter for business systems (for example MFA for all workforce access), it applies to the business side. When a program is stricter (for example PMMD rules or SGI handling), the program governs and the supplement points to it.

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Nuclear Generation | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; adds the CSP interface rules below. Minor update for the final policies due by 2026-12-30 | Confirm alignment |
| Engineering and Radiation Services | v2026 | 2026-05-15 | Aligned, but missing the SGI reproduction rule (POL-04 4.3) and the AI quality assurance rule (POL-05 4.6) | Add both by 2026-11-30 (POAM-014, POAM-024) |
| Radioactive Waste Management | v2024 | 2024-02 | **Drifted** (scenario gap 9); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-017) |

## 3. What each supplement adds
### 3.1 Nuclear Generation supplement (Part 50 licensee; NERC Generator Owner and Generator Operator)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CSP interface | Every change to the kiosk update server, the plant data replica servers, the receive side of a one-way device, or a station DMZ rule needs CST review and a 73.58 screen before implementation | POL-01 4.8 | 73.54(c)(2), (d)(3); 73.58(b)-(c) |
| Kiosk content | Update packages are released to the kiosks only after vendor signature verification on the server and a CST release step | POL-01 4.7 | RG 5.71 B.1.19, C.3.7, C.7 |
| CDA information | CDA work packages live in the restricted WMS module; transmittals screened; bulk export alerts | POL-04 4.2, 4.5 | 73.54(d)(2); 73.22(g)(1) |
| Outage access | Cross-division accounts created from the outage schedule and ended on the assignment end date; division laptops in the contractor segment | POL-02 4.4, 4.5 | 73.56(b)(1)(ii) |
| Security building devices | No networked printer or scanner in a security building may be used for SGI; one evaluated stand-alone copier per station | POL-04 4.3 | 73.22(e) |
| Notifications | Fleet security director is the only route for external reports about station systems; 73.77 decision aid in every control room and at the SOC | POL-03 4.3, 4.4 | 73.77(a); 50.72 |
| NERC CIP | Vendor electronic remote access methods documented for every low impact asset; ESP rules reviewed each year with group internal audit | POL-02 4.10 | CIP-003-9 Attachment 1 Section 6; CIP-005-7 |
| Maintenance AI | No AI output may create a work request on Maintenance Rule equipment without human approval; Maintenance Rule program review before scope expands | POL-01 4.14 | 50.65(a)(1); 73.58 |

### 3.2 Engineering and Radiation Services supplement (SGI holder; contractor/vendor access authorization program; NVLAP processor; DOE contractor)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| SGI need-to-know | Project SGI custodian documents a need-to-know determination before access; SGI access list reconciled quarterly against assignments | POL-02 4.8 | 73.22(b)(1); 73.21(a)(1) |
| SGI reproduction | One evaluated stand-alone copier per office; networked scanners never used for SGI (**to be added**) | POL-04 4.3 | 73.22(e), (g)(4) |
| Access authorization files | Kept only in the program's restricted repository with write-once retention; never in project shares | POL-02 4.8; POL-04 | 73.56(k), (m), (o)(1) |
| Client sites | Engineers follow each client's CSP, PMMD, and access rules; client-issued remote access never reused for group systems | POL-05 4.2 | Client 73.54 programs (contract) |
| Dosimetry customers | MFA for customer administrators by 2026-12-31; customer notice within 72 hours of confirming an incident; third-party agent notice under state law | POL-02 4.3; POL-03 4.5 | 20.2106(d); customer contracts; Fla. Stat. 501.171(6) |
| DOE work | FCI only in the federal projects enclave (SYS-E4) | POL-04 | 52.204-21 |
| Export control | Part 810 determinations before foreign national access; quarterly recertification of controlled folders | POL-02 4.7 | 810.2 |
| Engineering AI | AI use in safety-related work only under the QA procedure for AI use (**to be added**) | POL-05 4.6 | Client QA requirements (10 CFR Part 50, Appendix B, by contract) |

### 3.3 Radioactive Waste Management supplement (Agreement State licensee; Part 37 at the Florida facility; hazmat carrier; RCRA permittee)
| Topic | Division requirement (v2026 draft) | Group policy it builds on | Driver |
|---|---|---|---|
| Vault security systems | Security network separate from the business network with an alternate path not subject to the same failure modes | POL-01 4.7 | 37.49(a)(1), (c) |
| Part 37 information | Security plan, procedures, and approved lists only in the restricted library; removal within 7 working days | POL-02 4.8 | 37.43(d) |
| OT vendor access | Named, per-session access with MFA and recording; no shared vendor accounts | POL-02 4.10 | CSF PR.AA-03, DE.CM-06 |
| OT credentials | Default passwords changed before connection; monthly default credential scan | POL-02 4.9 | CSF PR.AA-01 |
| Part 37 events | Cyber attacks on vault security systems assessed as possible sabotage or suspicious activity; reports to the Bureau of Radiation Control routed through the Radiation Safety Officer | POL-03 4.4 | 37.57(a)-(b) |
| Records | Part 37 and RCRA records backed up through group immutable backups; monthly completeness check of the waste tracking export | POL-04 4.7 | 37.101; 264.73 |
| Shipments | Telematics and carrier tracking for category 2 shipments; DOT security plan in the restricted library | POL-04 | 37.79(a)(2); 49 CFR 172.802 |

## 4. Radioactive Waste Management drift: conflicts with 2026 group policy
The 2024 supplement was written before the 2026 group policies and before the second facility's security network was separated. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 WM-012; P07 PL-1 findings).

| Topic | Waste supplement (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| Vendor remote access | Shared vendor account allowed "for emergency support" | Named accounts, MFA, recording (POL-02 4.10) | Florida PLC vendor access has no MFA (WM-003) |
| Security system networks | Not addressed | No shared-service path to Part 37 security systems (POL-01 4.7) | Vault PACS on the business network (WM-001) |
| Incident severity | Division 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation (P07 IR findings) |
| External reports | Radiation Safety Officer reports events; IT may report to law enforcement directly | All external reports about protected systems through the program owner (POL-03 4.4) | Part 37 and group notices not coordinated (WM-010) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 9 (POAM-016) |
| Default credentials | Not addressed | Changed before connection (POL-02 4.9) | 2 HMIs still on defaults (WM-007) |

**Why the drift happened.** The division was acquired into the group structure in 2023 and its security lead sat in operations until 2025. The supplement had no review date. **Fix:** the Group CISO's policy office now tracks every supplement version and review date, and POL-01 4.5 requires re-alignment within 90 days of any group change.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy or any regulator-approved program, and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Nuclear Generation, Engineering and Radiation Services) and on re-issue (Radioactive Waste Management).

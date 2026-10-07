# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO and, for OT topics, the Group OT Security Director |
| Status date | 2026-09-17 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA, one severity scale, no direct IT-to-OT paths, safety first, AI approval | Board risk committee or Group CISO |
| Group standards | OT DMZ standard, logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO; Group OT Security Director for OT |
| **Division supplement** | Regulator-specific and system-specific standards: SPCC alarm-loss duties, CIP-003-9 low impact plans, 195.446 control room rules, the hazmat security plan | Division president, after Group CISO alignment review (and the CIP Senior Manager for CIP plans) |
| Division procedures | Control room procedures, plant procedures, runbooks | Division security and compliance lead with the operations owner |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Crude Oil Production | v2026 | 2026-06-15 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due 2026-12-30 (90 days after the effective date) | Add the model write-path gate (section 3.1 item 3) |
| Power Generation | v2026 | 2026-03-10 (with the CIP-003-9 policy approval) | Aligned. The CIP-003-9 policy and plans are part of the supplement and keep their own 15-month NERC cycle | Add the transient cyber asset checklist and P3 vendor path changes (POAM-013, POAM-014) |
| Crude Logistics | v2023 | 2023-05 | **Drifted** (scenario gap 9); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-020) |

## 3. What each supplement adds
### 3.1 Crude Oil Production supplement (focus division; FSPA)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Field logic changes | Approved change request before any PLC, RTU, or rod pump controller logic change; emergency changes recorded within 24 hours; monthly logic comparison against the repository | POL-01 4.7 | N21-BM (SP 800-82r3 6.2.4) |
| SPCC alarm loss | When SCADA alarms are lost at a battery that uses the high-level sensor option, the shift lead decides within 4 hours to shut in or start gauging rounds | POL-01 4.7; POL-03 4.3 | 40 CFR 112.9(c)(4)(iv) |
| Model write paths | No model or analytics service may send setpoints to field devices without Group AI council approval and a safety management of change review; models run advisory-only by default | POL-01 4.13 | N21-BM (SP 800-82r3 4.2.2) |
| SCADA console accounts | Named controller accounts; the 2 shared Florida console logins are a dated exception (POAM-008) | POL-02 4.1 | N21-BM (SP 800-82r3 6.2.1) |
| Field device credentials | Default credential sweep at every site visit; modem and controller passwords in the vault | POL-02 4.11 | N21-BM (SP 800-82r3 6.2.1) |
| Mid-Continent interim rules | Until SYS-P5 migrates: integrator access only through group PAM; logs forwarded to the SIEM; offline backups and a quarterly restore test | POL-01 4.9; POL-02 4.10 | N21-BM (SP 800-82r3 6.2.10) |
| Royalty owner data | No owner exports outside SYS-P3; bank changes confirmed by callback | POL-04 4.3 | Fla. Stat. 501.171(2) |

### 3.2 Power Generation supplement (Generator Owner and Generator Operator)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CIP-003-9 policy and plans | Low impact policy covers topics 1.2.1 to 1.2.7; plans cover Attachment 1 Sections 1 to 6 for P1, P2, P3, and the GCC; reviewed and approved by the CIP Senior Manager at least every 15 calendar months | POL-01 4.2 | N22-R01 (CIP-003-9 R1 Part 1.2; R2) |
| CIP-002 reviews | Categorization reviewed and approved every 15 calendar months, and at any generation project gate | POL-01 4.3 | N22-R01 (CIP-002-5.1a R2) |
| Transient cyber assets and removable media | Checklist recorded for every third-party laptop before connection; scanning kiosks for all media | POL-05 4.3 | N22-R01 (CIP-003-9 R2 Att. 1 Sec. 5) |
| Vendor electronic remote access | Only through group PAM, with a method to determine, disable, and detect malicious communications for every vendor path | POL-02 4.10 | N22-R01 (CIP-003-9 R2 Att. 1 Sec. 6) |
| Incident response | Reportable Cyber Security Incident determination by the CIP Senior Manager; E-ISAC notice after the determination; plan tested every 36 months | POL-03 4.5, 4.9 | N22-R01 (CIP-003-9 R2 Att. 1 Sec. 4) |
| Event reporting | EOP-004-4 Operating Plan with offline contacts and voice reporting to the ERO | POL-03 4.6 | EOP-004-4 R1, R2 |
| Control Center data | CIP-012-2 plan for real-time data between the GCC and other Control Centers | POL-04 4.4 | CIP-012-2 R1 |

### 3.3 Crude Logistics supplement (pipeline operator and hazmat carrier)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Controller roles | Loss or suspected manipulation of SCADA is an abnormal operating condition; the SOC OT desk advises and the controller decides | POL-03 4.3 | PHMSA 195.446(b) |
| Controller training | SCADA loss and manipulation scenarios in the annual program and simulator; the OT desk joins team exercises | POL-03 4.9 | PHMSA 195.446(h) |
| Backup SCADA | Test the backup PCC every calendar year within 15 months | POL-03 4.10 | PHMSA 195.446(c)(4) |
| Change coordination | OT DMZ, jump server, and connector changes by corporate go through control room change management; point-to-point verification after field or display changes | POL-01 4.7 | PHMSA 195.446(c)(2), (f) |
| Release notices | One-hour National Response Center notice for the trunk line and regulated rural gathering lines; 30-day reports for all Part 195 lines | POL-03 4.5 | PHMSA 195.52; 195.54 |
| Hazmat security plan | Risk assessment and en route measures cover cyber threats to dispatch, run tickets, and telematics; duties for IT, SOC, and system owners | POL-01 4.2 | HMR 172.802(a), (b) |
| Security training | In-depth training updated with the plan; staff retrained within 90 days of each revision | POL-05 4.1 | HMR 172.704(a)(5), (c)(2) |
| Driver monitoring | Camera AI scores reviewed by a person before discipline; telematics data not used to pressure drivers on hours | POL-05 4.8; POL-01 4.13 | 49 CFR 390.36 |
| Shipper commitments | Shipper portal security and availability commitments recorded for the SOC 2 report (P09) | POL-04 4.1 | Shipper contracts |

## 4. Crude Logistics drift: conflicts with 2026 group policy
The 2023 Crude Logistics standards were written before the 2025 common control catalog and the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but controllers, dispatchers, and drivers follow the document they know, so the conflicts are real risks (P01 ML-013; P07 PL-01 findings).

| Topic | Crude Logistics standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Vendor remote access | SCADA vendor may keep a standing VPN for support | No persistent vendor paths; PAM only (POL-02 4.10) | Vendor path outside SOC visibility |
| Incident severity | Division 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation |
| Termination | Next business day | Within 4 hours; local OT accounts the same day (POL-02 4.6) | Longer exposure window |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Scenario gap 6 (POAM-019) |
| Change management | Field and display changes only | Security changes affecting OT included (POL-01 4.7) | 195.446(f) gap (P03 LG-13) |
| AI use | Not addressed | AI inventory and approval (POL-01 4.13) | Camera AI in discipline without review (ML-008) |
| Notification | PHMSA and NRC only | Multi-regulator matrix with named owners (POL-03 4.5) | Missed SEC and state duties possible |

**Why the drift happened.** The 2023 supplement had no owner after the division's compliance lead changed roles, and the group's policy register did not track supplement versions. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Production, Power Generation) and on re-issue (Crude Logistics).

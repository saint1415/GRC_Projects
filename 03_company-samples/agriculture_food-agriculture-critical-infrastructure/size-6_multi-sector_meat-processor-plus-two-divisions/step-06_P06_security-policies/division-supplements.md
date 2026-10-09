# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-15 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA, one severity scale, food safety first in incidents, no security terms no access, FSQA sign-off on OT changes | Board risk committee or Group CISO |
| Group standards | OT reference architecture and OT security standard, logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO or Group OT security director |
| **Division supplement** | Regulator- and system-specific standards (food defense at Plant 6, DC temperature records, PCI DSS) | Division president, after Group CISO alignment review |
| Division procedures | Plant, DC, and store runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Meat Processing | v2025 | 2025-10 (to the 2025 group policies) | Aligned; needs the v2026 additions (HMI sign-in deadline, OT change sign-off, restart validation) by 2026-12-30 (90 days after the effective date) | Update and attest |
| Food Distribution | Standards v2023 | 2023-04 | **Drifted** (group gap 7); conflicts listed in section 4 | Re-issue by 2026-12-31 (POAM-016) |
| Grocery Retail | v2026 | 2026-06 (to the 2026 draft group policies) | Aligned; maintained with the PCI DSS program | Confirm alignment with the final 2026 policies |

## 3. What each supplement adds
### 3.1 Meat Processing supplement (six FSIS official establishments; Plant 6 is an FDA-registered facility)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| OT reference architecture | Every plant built to the group zones and conduits model with an OT DMZ and a separate OT domain; Plants 2 and 5 by 2027-03-31 | POL-01 4.1 | NIST SP 800-82 Rev. 3 (voluntary) |
| HMI and MES accounts | Named HMI sign-in by 2027-06-30; named MES accounts and two-person formulation approval at every plant (Plants 2 and 5 by 2026-12-31) | POL-02 4.1, 4.2 | 9 CFR 417.5(b); 21 CFR 121.135(a) |
| Electronic CCP records | Historian and SYS-M5 audit trails always on; electronic signatures for pre-shipment review | POL-04 4.4 | 9 CFR 417.5(d) |
| OT change control | FSQA sign-off with a HACCP reassessment decision on every change that can affect product; at Plant 6, a food defense reanalysis decision before the change is operative | POL-01 4.13 | 9 CFR 417.4(a)(3); 21 CFR 121.157(b)-(c) |
| Food defense (Plant 6) | Vulnerability assessment covers control-system paths; verification includes interlock tests and access log reviews; agency workers trained before the first shift | POL-01 4.3; POL-05 4.3 | 21 CFR 121.130, 121.150, 121.4(b)(2) |
| Product holds | Any loss of monitoring or suspected tampering triggers a hold of product since the last trusted record | POL-03 4.3 | 9 CFR 417.3(b) |
| Restart | Formulations and PLC programs verified against signed masters and the repository before restart | POL-03 4.11 | 9 CFR 417.3(b) |
| Vendors | Integrators and refrigeration contractors only through SYS-G5; no modems | POL-02 4.10 | NIST SP 800-82 Rev. 3 (voluntary) |

### 3.2 Food Distribution supplement (five registered DCs; FSIS-registered wholesaler and warehouseman; private fleet; 3PL service)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Refrigerated storage | Local fallback alarms at every DC; monitoring and corrective action records reviewed within 7 working days | POL-03 4.3; POL-04 4.4 | 21 CFR 117.206(a)(2)-(4) |
| In-transit temperature | Missing telematics data treated as a possible material temperature failure until a qualified individual decides | POL-03 4.3 | 21 CFR 1.908(a)(6) |
| Telematics accounts | Named accounts with MFA; setpoint change alerts; history copied to SYS-G6 with 2-year retention | POL-02 4.1, 4.11 | 21 CFR 1.908(a)(3)(iii), (e)(2) |
| DC automation | Moved to the OT domain behind SYS-G5; offline backups with restore tests | POL-02 4.10; POL-04 4.6 | NIST CSF 2.0 (voluntary) |
| 3PL customers | Customer data and temperature history isolated per customer and append-only; customer incident notices per contract | POL-04 4.5; POL-03 4.5 | 3PL service agreements; SOC 2 commitments (P09) |
| FSIS registration | Changes in name, address, or trade name reported within 15 days | POL-01 4.1 | 9 CFR 320.5(b) |

### 3.3 Grocery Retail supplement (120 stores; PCI DSS merchant)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CDE scope | Store network templates reviewed for segmentation before rollout; scope confirmed every year and after every template change | POL-01 4.1 | PCI DSS Req. 1.3, 11.4, 12.5 |
| Payment acceptance | P2PE terminals only; the 30 remaining stores converted by 2027-03-31; POI device inspections tracked with escalation | POL-04 4.2 | PCI DSS Req. 4.2, 9.5 |
| Payment page | Every script on the payment page inventoried, justified, and integrity-checked; tamper detection on the page | POL-01 4.8 | PCI DSS Req. 6.4, 11.6 |
| Card incidents | CDE containment, evidence preservation for a forensic investigator, acquirer notice per contract | POL-03 4.12 | PCI DSS Req. 12.10 |
| Customer accounts | MFA offered; risk-based step-up; analytics extracts tokenized | POL-02 4.11; POL-04 4.2 | FTC Act Section 5; state breach laws |
| Grinding records | Scale grinding logs collected centrally each day | POL-04 4.4 | 9 CFR 320.1(b)(4) |
| Camera analytics | No facial recognition; privacy review and notice before any store pilot | POL-01 4.12; POL-05 4.8 | FTC Act Section 5 |

## 4. Food Distribution drift: conflicts with 2026 group policy
The 2023 Food Distribution standards were written before the 2025 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but DC staff follow the document they know, so the conflicts are real risks (P01 FD-007; P07 PL-1 finding).

| Topic | Food Distribution standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Log retention | 30 days in WMS and automation logs | 1 year searchable, 6 years archived (logging standard; POL-01 4.11) | Investigations and customer questions limited to 30 days (POAM-019) |
| Termination | Next business day | Within 4 hours (POL-02 4.5) | Longer exposure window for terminated DC staff |
| Vendor remote access | Vendor tools allowed with a firewall rule | Only through SYS-G5 (POL-02 4.10) | Automation vendor access outside the gateway at three DCs (P01 FD-006) |
| Incident severity | Three-level DC scale | One group scale (POL-03 4.2) | Inconsistent escalation |
| Temperature record review | Monthly | Within 7 working days (POL-04 4.4; 21 CFR 117.206(a)(4)(iii)) | Late reviews (POAM-025) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Group gap 7 (POAM-017) |
| AI use | Not addressed | AI inventory and approval (POL-01 4.12) | Forecasting and routing models unregistered until P10 |

**Why the drift happened.** The 2024 reorganization moved DC IT under the Group CISO, but the standards had no named owner or review date. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Meat Processing, Grocery Retail) and on re-issue (Food Distribution).

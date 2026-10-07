# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-17 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, no shared accounts, one severity scale, whole-account CPNI rule, no agreement no data | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, Group AI Standard (P10), vendor security standard | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (for example, the CPNI manual, CALEA SSI procedures, FCI enclave rules, antenna lighting monitoring) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Telecom Carrier | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; update for the final 2026 policies (service-impact gate, Item 1.05(d) step) due by 2026-12-30 | Confirm alignment |
| Network Engineering Services | v2026-03 | 2026-03 | Aligned, but its remote access standard still permits persistent tunnels, which POL-02 4.9 now prohibits | Update the remote access standard by 2026-12-31 (POAM-024) |
| Tower and Fiber Infrastructure | v2023 | 2023-09 (standards of the acquired tower company) | **Drifted** (scenario gap 9); conflicts in section 4 | Re-issue by 2026-12-31 (POAM-020) |

## 3. What each supplement adds
### 3.1 Telecom Carrier supplement (telecommunications carrier; interconnected VoIP provider; CALEA carrier)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CPNI manual | Approval flags checked at use; biennial opt-out notices naming receiving entities; campaign register including affiliate campaigns; supervisory approval for outbound marketing | POL-04 4.4 | 47 CFR 64.2007-64.2009 |
| Customer authentication standard | Telephone, online, in-store, and backup authentication rules; change notices; applies to chatbot and voice agent channels; no supervisor override of the password prompt | POL-02 4.10 | 64.2010(b)-(f) |
| Outsourced contact centers | CPNI training before access; same-day leaver notice; monthly call sampling; 24-hour incident notice in contracts | POL-05 4.4; POL-01 4.8 | 64.2009(b); 64.2010(b) |
| Network element AAA standard | Named TACACS+ accounts with MFA from jump hosts; sealed local accounts; configuration backups with an offline copy in a second region | POL-02 4.4; POL-04 4.7 | 64.2010(a) |
| NOC outage procedures | PSAP and 988 notices within 30 minutes; NORS notification within 120 minutes (wireline) or 240 minutes (VoIP, 911 facility); annual PSAP contact confirmation; DIRS | POL-03 4.3 | 47 CFR 4.9; 4.18 |
| CPNI breach procedure | Reasonable determination record; reporting facility notice within 7 business days; 7-full-business-day hold; customer notice; 2-year record; Form 8-K Item 1.05(d) coordination with the Group General Counsel | POL-03 4.5, 4.7 | 64.2011; Form 8-K Item 1.05(d) |
| CALEA SSI procedures | SSI policy per operating company; appendix checked quarterly; refile within 90 days of a merger or amendment; compromise reports | POL-01 4.2; POL-03 4.8 | 47 CFR 1.20003-1.20005 |
| Chatbot release gate | No chatbot or voice agent change that touches authentication or account actions without CPNI review and red-team test | POL-01 4.12 | 64.2010(c), (e) |

### 3.2 Network Engineering Services supplement (federal contractor; managed services provider to other carriers)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| MNO remote access standard | Brokered, recorded sessions with named PAM accounts; no persistent tunnels; customer approval for any standing connection | POL-02 4.9 | Customer contracts |
| Customer notice register | Per-customer terms (30-minute outage notice; 24- or 72-hour incident notice); automatic outage notices for alarms tagged 911 or special facility | POL-03 4.9 | Customer contracts; Fla. Stat. 501.171(6) |
| Customer data rules | Customer subscriber data in tickets handled as the customer's agent; no use for Engineering marketing; CPNI training for operators | POL-04 4.4; POL-05 4.4 | Customer contracts; 47 CFR 64.2007(b) for Carrier data |
| FCI enclave standard | FCI only in the enclave; visitor logs and escorts at project offices; disposal only through group end-user services; FAR flowdown in subcontracts | POL-04 4.6, 4.8; POL-01 4.8 | FAR 52.204-21(b)(1), (c) |
| Covered equipment screening | Automated screening against the FCC Covered List and supplier attestations before purchase and before shipment; reporting within 1 business day (52.204-25(d)) or 3 business days (52.204-23(c)) | POL-01 4.8 | FAR 52.204-25; 52.204-23; 47 CFR 1.50007 |

### 3.3 Tower and Fiber Infrastructure supplement (antenna structure owner; lessor)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Lighting monitoring standard | Automatic alarm system on every lit structure; written fallback to daily observation within 24 hours when monitoring is lost; quarterly inspections unless certified exempt | POL-03 4.3 | 47 CFR 17.47 |
| FAA reporting | Report to the FAA immediately when a top or flashing light outage is not corrected within 30 minutes; extend and close NOTAMs; records in SYS-T2 kept 2 years | POL-03 4.3; POL-01 4.11 | 47 CFR 17.48; 17.49 |
| RMU device standard | No default passwords; private APN or device certificates; firmware updates within 30 days of a vendor security release | POL-02 4.11 | 47 CFR 17.47(a)(2) |
| Landowner payment changes | Bank changes only after a callback to the telephone number on file and a second approver | POL-02 4.2 | FTC Act Section 5 (N53-R02) |
| Site access | Per-person smart lock credentials; daily review of unusual unlocks | POL-02 4.1 | Tenant lease terms |

## 4. Tower drift: conflicts with 2026 group policy
The 2023 Tower standards came from the acquired tower company and were never re-aligned. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 TF-006; P07 PL-1).

| Topic | Tower standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Device credentials | Shared RMU passwords allowed "where the device does not support named accounts" | No default or shared passwords; certificates where supported (POL-02 4.11) | 212 RMUs still accepted the default password (P07; TF-014) |
| Monitoring fallback | Not addressed | Service-impact gate and lighting fallback (POL-03 4.3) | No written fallback (TF-002; POAM-019) |
| Incident severity | Tower 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation of RMU events |
| Log retention | 90 days in the RMU platform | 1 year searchable, 6 years archived (logging standard) | Limited investigation history (POAM-003) |
| AI use | Not addressed | AI inventory and approval (POL-01 4.12) | Inspection imagery pilot started without registration (P10 AI-007) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 9 (POAM-021) |

**Why the drift happened.** The 2023 acquisition integration moved Tower IT to group identity and cloud, but the security standards had no named owner after the acquired company's security manager left. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 for all three divisions.

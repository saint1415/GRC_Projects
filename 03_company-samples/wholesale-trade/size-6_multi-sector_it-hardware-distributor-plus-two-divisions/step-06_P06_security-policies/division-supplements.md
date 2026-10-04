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
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, sourcing and screening rules, no CUI outside the enclave | Board audit and risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, C-SCRM plan, Group AI Standard (P10) | Group CISO; Group supply chain risk director for C-SCRM |
| **Division supplement** | Contract-, regulator-, and system-specific standards (for example, DIBNet reporting, OT vendor access, card payments by phone) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| IT Distribution | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Confirm alignment |
| Logistics | v2024 | 2024-05 | **Drifted** (scenario gap 9); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-022) |
| Online Retail | v2026 | 2026-04-15 | Aligned, but missing the card-payment-by-phone rules now in POL-04 4.4 and POL-05 4.8 | Add the rules by 2026-10-31 (POAM-017) |

## 3. What each supplement adds
### 3.1 IT Distribution supplement (DoD subcontractor handling CUI; Lifecycle Services)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CUI roster | Integration center managers approve every roster change; roster reviewed monthly against active jobs | POL-02 4.2 | SP 800-171 R2 3.1.1, 3.1.5 |
| CUI intake | CUI accepted only through the prime secure file exchange into the FFE; any CUI found elsewhere is reported to the SOC and moved within 1 business day | POL-04 4.2 | 252.204-7012(b)(2); 3.1.3 |
| Lab networks | Lab networks connect only to the FFE; any new device is added to the inventory before connection | POL-01 4.7 | 3.4.1, 3.13.1 |
| Firmware | Firmware is verified by OEM signature or published hash from the OEM's own portal before any device is configured | POL-01 4.12 | 252.246-7008(b)(3)(ii)(B); SI-7 |
| DIBNet reporting | Federal Solutions keeps at least two certificate holders on call every day | POL-03 4.4 | 252.204-7012(c)(3) |
| ITAD | Sanitization method recorded per device; verification sample on every line every shift | POL-04 4.8 | NIST SP 800-88 (customer contracts) |
| Affirmations | No SPRS score or CMMC affirmation without a documented assessment of the full scope reviewed by the Group CMMC program director | POL-01 4.8 | 32 CFR 170.22; 252.204-7019, -7020 |

### 3.2 Logistics supplement (DCs, fleet, 3PL services; houses the integration centers)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Handheld sign-in | Named sign-in on every handheld; no shared zone logins after 2027-03-31 | POL-02 4.1 | 52.204-21(b)(1)(i), (v), (vi) |
| Temporary agency workers | Agency assignment end dates feed identity governance; accounts expire automatically | POL-02 4.5 | 3.9.2 |
| OT vendor access | PAM-brokered vendor sessions only; tunnels removed by 2026-12-31; PLC changes backed up to the group vault the same day | POL-02 4.9; POL-04 4.7 | Worker safety; CTPAT cybersecurity criteria |
| Receiving | OEM serial validation and tamper inspection at every DC; quarantine cage at every dock | POL-01 4.12 | 252.246-7008(c); CTPAT business partner criteria |
| Integration center buildings | Night-shift escort roster at DC-1 and DC-6; cage keys inventoried quarterly | POL-01 4.7 | 3.10.3 to 3.10.5 |
| 3PL clients | MFA for client users; client incident notices per the master services agreement | POL-02 4.11; POL-03 4.5 | 3PL agreements |

### 3.3 Online Retail supplement (Level 1 merchant; online marketplace)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Payment pages | Every script on a payment page is inventoried, authorized, and integrity-checked; tamper alerts go to the SOC | POL-01 4.1 | PCI DSS 6.4.3, 11.6.1 |
| Phone payments | Keypad entry or automatic pause; no card data in recordings; quarterly recording sample | POL-04 4.4; POL-05 4.8 | PCI DSS 3.3.1 |
| PCI scope | Scope confirmed with data discovery before each ROC | POL-01 4.7 | PCI DSS 12.5.2 |
| Marketplace sellers | Verification within 10 days; suspension after notice and the 10-day window; compliance data visible only to the verification team | POL-04 4.6 | 15 U.S.C. 45f(a) |
| Counterfeit listings | Takedown within 24 hours of a credible OEM report; electronics listings checked against the covered-manufacturer list | POL-01 4.11 | FTC Act Sec. 5; INFORM Act (b)(3) reporting mechanism |
| Privacy | CCPA risk assessment before any new sharing of personal information or new sensitive personal information use | POL-04 4.1 | Cal. Code Regs. tit. 11, 7150 |

## 4. Logistics drift: conflicts with 2026 group policy
The 2024 Logistics standards were written before the 2026 group policies and before DC-8 and DC-9 were acquired. Where they conflict, **group policy governs now** (POL-01 4.5), but DC staff follow the document they know, so the conflicts are real risks (P01 LW-011 and GR-07).

| Topic | Logistics standard (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| Handheld accounts | Shared zone logins allowed with a zone PIN | Unique identities; shared accounts prohibited (POL-02 4.1) | 22 shared logins at DC-8 and DC-9 (POAM-001) |
| Vendor remote access | Vendor tunnels allowed if the vendor contract has a security clause | PAM-brokered sessions only; tunnels prohibited (POL-02 4.9) | Persistent tunnels at 3 DCs (POAM-014) |
| PLC backups | Kept by the OT engineer responsible | Immutable vault, separate account (POL-04 4.7) | Backups on laptops at 4 DCs (POAM-016) |
| Agency workers | Removed at the weekly review | Automatic expiry at assignment end (POL-02 4.5) | Up to 7 days of excess access (LW-016) |
| Receiving checks | Visual inspection only | OEM serial validation and tamper inspection (POL-01 4.12) | 5 DCs without serial validation (POAM-012) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 8 (POAM-022) |

**Why the drift happened.** The 2024 reorganization moved DC IT under the group, but the supplement kept its operations owner and had no review date, and the DC-8 and DC-9 acquisition added sites that never adopted it. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (IT Distribution, Online Retail) and on re-issue (Logistics).

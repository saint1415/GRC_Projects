# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year; every division with OT must have one |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-10 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for remote and privileged access, one severity scale, SSI library, no always-on vendor access | Board safety, security, and risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, patch strategy, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and OT-specific standards (TSA directive measures, PTC, terminal racks, building OT) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

The TSA-approved CIP sits beside the Freight Railroad supplement: the supplement states the rules; the CIP describes how the Covered Railroads meet the directive and is what TSA inspects against. If the two ever differ, the CIP governs for the Covered Railroads until an amendment is approved.

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Freight Railroad | v2026 | 2026-06-12 (to the 2026 draft group policies and the CIP) | Aligned; update for the final 2026 policies and the SYS-G5 change rule (POL-01 4.9) due by 2026-12-30 | Confirm alignment |
| Transload and Wholesale | None (draft v0.9 below) | Never | **Missing** (scenario gap 9); terminal OT has no written standard | Issue v2026 by 2026-12-31 (POAM-015) |
| Railside Industrial Real Estate | None (draft v0.9 below) | Never | **Missing** (scenario gap 9); building OT has no written standard | Issue v2026 by 2026-12-31 (POAM-015) |

## 3. What each supplement adds
### 3.1 Freight Railroad supplement (v2026)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Critical Cyber Systems | Keep the Critical Cyber System list and interdependency list current; any change that touches them goes to the rail change board for a CIP amendment decision | POL-01 4.9 | SD 1580/82-2022-01E III.A, III.B.1.a, VI.B-D |
| Dispatch consoles | Named OT directory logins; MFA replaced by the CIP compensating controls (badge-controlled NOC floor, allowlisting, no remote access, session lock at relief) | POL-02 4.3 | SD III.C.2 |
| CTC and shared accounts | No shared administrator accounts on CTC code servers after 2026-12-31; until then, vaulted in PAM and rotated on every holder change | POL-02 4.1, 4.4 | SD III.C.4 |
| PTC keys | Key custodians separate from PTC administrators; key ceremonies witnessed and logged; revocation on suspected compromise | POL-04 4.4 | 49 CFR 236.1033(b)-(d) |
| PTC patching | PTC vendor patches applied within 30 days of certification; until then, documented mitigations and a timeline for every unpatched server | POL-01 4.8 | SD III.E.3 |
| OT logging | CTC, PTC, CAD, and directory logs to the SIEM with 1-year retention | POL-03 4.2 | SD III.D.3 |
| Manual operations | Manual dispatch drill on every CTC railroad at least every 2 years; RSSM location fallback tested twice a year | POL-03 4.3 | SD 1580-21-01E II.D; 49 CFR 1580.203(d) |
| TSA reporting | CISA report within 24 hours for Covered Railroads; TSOC report within 24 hours for any railroad (target 12 hours) | POL-03 4.4 | SD 1580-21-01E II.C; 49 CFR 1570.203 |
| Field vendors | Crossing monitor and detector vendors connect only through group PAM; no vendor-owned modems | POL-02 4.7 | SD III.C; III.B.1.b |
| AI in inspections | AI alerts never replace inspections by qualified inspectors; alerts and inspector decisions logged | POL-01 4.14 | 49 CFR 213.7; 213.233 |

### 3.2 Transload and Wholesale supplement (draft v0.9; issue due 2026-12-31)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Terminal networks | Separate office, OT, and guest networks at every terminal; OT has no internet access except through the group remote access service | POL-02 4.7 | FTC Act Section 5; CSF PR.IR-01 |
| Loading racks | Rack controller changes only by named technicians; configuration backed up after every change; vendor access through PAM only | POL-02 4.7 | 49 CFR 172.802(a)(2) |
| Hazmat security plan | Plan risk assessment includes cyber manipulation of rack controls and shipping paper data | POL-01 4.3 | 49 CFR 172.802(a) |
| FCI | FCI only in the federal contracts workspace and ERP; FAR 52.204-21 flowed down to haulers; covered telecommunications and Kaspersky reports within 1 and 3 business days | POL-04 4.5 | FAR 52.204-21, 52.204-25(d), 52.204-23(c) |
| Kiosks and scales | No shared kiosk accounts; scale software edit rights limited and logged | POL-02 4.1 | CSF PR.AA-05 |
| Acquired terminals | Join SYS-G1 and EDR within 90 days of closing | POL-01 4.10 | CSF DE.CM-01 |
| Payments | Call-back verification enforced in the ERP for every vendor bank change | POL-05 3.5 | FTC Act Section 5 |

### 3.3 Real Estate supplement (draft v0.9; issue due 2026-12-31)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Building OT exposure | No BAS, access control, or CCTV device reachable from the internet; remote access through a managed gateway | POL-02 4.7 | FTC Act Section 5; CSF PR.IR-01 |
| Vendor consoles | Named vendor accounts with MFA; quarterly review | POL-02 4.1, 4.3 | CSF PR.AA-05 |
| Vendor contracts | Security, patch, and incident notice terms at every renewal; annual assurance report or questionnaire | POL-01 4.8 | CSF GV.SC-05 |
| Guarantor data | Guarantor files only in the property system; retention limit after the lease ends | POL-04 4.8 | Fla. Stat. 501.171(2), (8) |
| Right-of-way documents | Screen every upload for SSI with the rail security checklist | POL-04 4.3 | 49 CFR 1520.9(a) |
| Tenant remittance | Remittance changes only through the tenant portal; notice to tenants each year | POL-05 3.5 | FTC Act Section 5 |

## 4. Why two divisions have no supplement
When the group policies were first issued in 2023, only the railroads had a regulator (TSA) that required written cyber measures, so only the Freight Railroad wrote a supplement. The terminals and buildings were treated as "IT only," and their OT was never brought under a written standard. P03 and P07 show the result: terminal and building OT carry the group's least controlled exposure (gaps 5 and 7). POL-01 4.5 now requires a supplement for every division with OT.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-30 (Freight Railroad) and on first issue (Transload and Wholesale, Real Estate).

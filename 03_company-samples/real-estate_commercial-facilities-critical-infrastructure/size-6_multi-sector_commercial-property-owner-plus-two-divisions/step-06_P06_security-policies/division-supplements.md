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
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, OT remote access only through the gateway, internal suppliers treated as suppliers | Board risk committee or Group CISO |
| Group standards | OT security standard (SP 800-82 Rev. 3 zones and conduits), logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-, contract-, and system-specific standards (for example, SAQ P2PE office rules, CMMC scoping, PCI DSS for hotels, tenant and owner notices) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Commercial Property | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Confirm alignment |
| Construction | v2025 | 2025-10 | Aligned for project systems and federal work, but **silent on the BTI unit's services to other divisions** (scenario gap 4): no rule that BTI tools run in the landing zone, that OT credentials live in the group vault, or that BTI checks drawings for CUI markings | Add a BTI section by 2026-12-31 (POAM-018) |
| Hotels | v2025 | 2025-11 | Aligned for PCI DSS and guest data, but **silent on hotel building OT** on the BAACS | Add a building OT section by 2026-12-31 |

## 3. What each supplement adds
### 3.1 Commercial Property supplement (focus division; landlord, merchant on SAQ P2PE, third-party property manager)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Tenant administrators | Tenant administrators are onboarded by the property manager, use MFA, and attest to their badge holder lists every quarter | POL-02 4.11, 4.12 | CPG 2.0 3.D |
| Badge lifecycle | Badges unused for 90 days suspended automatically; legacy proximity readers replaced by 2027-12-31 | POL-02 4.11 | CPG 2.0 3.D; 3.H |
| Manual operation | Each property keeps manual operating procedures for HVAC and doors, drilled once a year | POL-03 4.2, 4.8 | CPG 2.0 6.A |
| Life-safety interfaces | Every fire alarm and elevator interface verified read-only with the fire alarm vendor and recorded in site diagrams | POL-01 4.14 | CPG 2.0 2.E |
| Visitor data | Visitor ID scans purged after 30 days | POL-04 4.6 | Fla. Stat. 501.171(8) worked example |
| Analytics and biometrics | No analytics or biometric feature at any property without Group AI council approval; biometric enrollment opt-in with a badge-only alternative | POL-01 4.13; POL-04 4.7 | 15 U.S.C. 45(a); state law |
| Card acceptance | P2PE terminals only; monthly terminal inspections logged; no card data in email or on paper beyond authorization | POL-04 4.4 | PCI DSS v4.0.1 SAQ P2PE |
| Tenant and owner notices | Lease (72-hour clause for 410 tenants) and property management agreement (48-hour clause) notice terms recorded in the P08 matrix | POL-03 4.4 | Leases; property management agreements |
| Guard contractor | Named accounts with MFA for remote video viewing; security addendum | POL-01 4.9; POL-02 4.1 | CPG 2.0 1.E |

### 3.2 Construction supplement (federal contractor; BTI integrator)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CMMC scopes | Level 1 scope (SYS-D3) and Level 2 scope (SYS-D4) documented; any new system that will hold FCI or CUI is scoped before use | POL-01 4.6; POL-04 4.3 | 32 CFR 170.19 |
| Affirmations | The Affirming Official affirms only against a completed evidence binder reviewed by counsel | POL-01 4.2 | 32 CFR 170.22 |
| External project users | Removed within 30 days of project closeout | POL-02 4.12 | FAR 52.204-21(b)(1)(i) |
| Section 889 | No product from a covered entity or its affiliates on any project or in group use; submittal screening on federal projects; report within 1 business day where 52.204-25(d) requires | POL-01 4.9 | FAR 52.204-25 |
| DoD reporting | Two medium assurance certificate holders; DoD report within 72 hours of discovery for incidents affecting CUI | POL-03 4.4, 4.9 | DFARS 252.204-7012(c)-(e) |
| Flowdown | Federal subcontract rider with 52.204-21, 52.204-25, and 252.204-7012 where applicable; CMMC status check before award | POL-01 4.9 | 52.204-21(c); 252.204-7012(m); 32 CFR 170.23 |
| **BTI services (to be added)** | BTI tools in a landing-zone account; OT credentials only in the group vault; CUI marking check before saving any drawing; BTI joins the group incident team; annual internal supplier assessment | POL-01 4.8; POL-02 4.4, 4.10; POL-04 4.3 | CPG 2.0 1.D, 1.E; DFARS 252.204-7021(d)(2) |

### 3.3 Hotels supplement (merchant on a Report on Compliance; lodging operator)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CDE scope | Scope confirmed every 12 months and within 30 days of any hotel acquisition; segmentation tested every 6 months | POL-01 4.6 | PCI DSS v4.0.1 Req. 11.4, 12.5 |
| Card display | Card numbers masked in every PMS; display rights reviewed every 6 months | POL-02 4.2 | PCI DSS v4.0.1 Req. 3.4, 7.2 |
| Vendor support access | POS and PMS vendors only through group PAM with MFA and recording | POL-02 4.10 | PCI DSS v4.0.1 Req. 8.4 |
| Payment pages | Script inventory and change detection on every booking page | POL-01 4.9 | PCI DSS v4.0.1 Req. 6.4.3, 11.6.1 |
| Total price | Every price display, including AI assistant answers and channel feeds, shows the total price including mandatory fees | POL-01 4.13 | 16 CFR 464.2 |
| Room keys | Identity check enforced in the PMS before key encoding | POL-05 4.1 | CPG 2.0 3.H |
| Guest data | Register kept at least 2 years; guest ID scans purged 30 days after checkout | POL-04 4.6 | Fla. Stat. 509.101(2); 501.171(8) worked examples |
| **Building OT (to be added)** | Hotel sites follow the OT standard and the manual-operation drills in 3.1 | POL-01 4.14; POL-03 4.8 | CPG 2.0 3.I, 6.A |

## 4. Gaps between supplements and the group program
The two missing sections are not drift in the usual sense: the supplements were not written badly, they were written for each division's own systems. The group program then grew a shared system (the BAACS) that two divisions use and a third services. **No supplement owned the seams.** The fix is structural:
- POL-01 4.6 now requires inheritance documentation for systems one division runs for another;
- POL-01 4.8 makes internal suppliers subject to supplier controls;
- the Group CISO's policy office reviews every supplement against the common control catalog (P02) each year, not only against group policy text.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy, reflects all group policy changes made in the last 12 months, and covers every service the division provides to other divisions." The first attestations under this wording are due 2026-12-31.

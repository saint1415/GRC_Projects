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
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, no tags in checkout, total price in every display | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, price display standard, Group AI Standard (P10) | Group CISO (price display: Group General Counsel) |
| **Division supplement** | Regulator-, acquirer-, and system-specific standards (for example event-day procedures, front desk card handling, client notice terms) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Live Venues | v2026 | 2026-06-20 (to the 2026 draft group policies) | Aligned; needs an acquisitions section for the 8 theaters (POL-01 4.9) and the tag rule (POL-01 4.13) | Update by 2026-12-30 (90 days after the effective date) |
| Hotels and Restaurants | v2024 | 2024-04 | **Drifted** (group gap 7); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-013) |
| Ticketing and Streaming | v2025 | 2025-10 | Aligned, but missing the client notice register and the tag rule for client tenants | Add by 2026-11-30 (POAM-004, POAM-006) |

## 3. What each supplement adds
### 3.1 Live Venues supplement (Level 1 merchant; ticket issuer; places of public accommodation)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Event-day downtime | Offline scanner mode tested at every venue each season; printed manifest procedure at every door | POL-03 | PCI DSS 12.10.1; P05 BP-LV01 |
| Card devices | Inspect every P2PE device before each event day; reconcile with the provider's list each quarter; contractor leads trained | POL-05 4.5 | PCI DSS 9.5.1 |
| Seasonal box office staff | Accounts created with an end date; no shared station logins | POL-02 4.1, 4.5 | PCI DSS 8.2 |
| Tenant tags | Venue marketing may add tags to event pages only from the approved list; never to checkout | POL-01 4.13 | PCI DSS 6.4.3 |
| Pricing | Accessible seating price levels are never in auto-apply; artist caps entered as ceilings before on-sale | POL-01 4.14 | 28 CFR 36.302(f)(3) |
| Price displays | Total price in every website, email, and social display | POL-01 4.12 | 16 CFR 464.2 |
| Acquired venues | Interim P2PE devices and EDR within 30 days of closing; no legacy card terminal on a shared network | POL-01 4.9 | PCI DSS 1.3, 12.5 |
| Integrator access | CCTV and door access support only through group PAM | POL-02 4.10 | PCI DSS 8.2.7 |
| Face entry pilot | No expansion without a privacy review and the P10 conditions; templates deleted within 24 hours of the event | POL-04 4.7 | Fla. Stat. 501.171 (worked example); FTC Act |

### 3.2 Hotels and Restaurants supplement (merchant; short-term lodging)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Front desk payments | Validated P2PE devices at every front desk by 2027-03-31; until then, front desk terminals on a separate segment | POL-01 4.13; POL-02 | PCI DSS 1.3 |
| Call center | Payment links or keypad entry; agents never hear or type card numbers | POL-05 4.4 | PCI DSS 3.2, 12.5.2 |
| Card authorization forms | Not accepted by email; secure payment links for group billing | POL-04 4.2 | PCI DSS 3.2, 3.3 |
| PMS accounts | PMS sign-in through SYS-G1; full card display limited to 2 roles per hotel | POL-02 4.1, 4.2 | PCI DSS 3.4.1, 8.2 |
| Identity documents | Identity document numbers stay in the PMS; never exported | POL-04 4.3 | Fla. Stat. 501.171(1)(g)1.a.(II) (worked example) |
| Resort fee | Total price including the resort fee in every channel feed; monthly channel audit | POL-01 4.12 | 16 CFR 464.2, 464.3 |
| Guest register | Kept electronically in the PMS; at least 2 years available for inspection | POL-04 4.7 | Fla. Stat. 509.101(2) |

### 3.3 Ticketing and Streaming supplement (service provider; SOC 2 service organization)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Client notices | Client notice register by contract term (24 hours for 186 clients, 72 hours standard) and state third-party agent clocks | POL-03 4.4, 4.5 | PCI DSS 12.10.1; Fla. Stat. 501.171(6) (worked example) |
| Responsibility matrix | Written PCI DSS acknowledgment and responsibility matrix for every client, including the group's divisions | POL-01 4.8 | PCI DSS 12.9.1, 12.9.2 |
| Payment page | Tags blocked in every checkout step for every tenant; script inventory and tamper detection | POL-01 4.13 | PCI DSS 6.4.3, 11.6.1 |
| Support access | Ticket-linked, just-in-time tenant access visible to the client | POL-02 4.7 | SOC 2 CC6.3 |
| Client data | No pooling across clients without contract permission | POL-04 4.4 | FTC Act 45(a)(1); CCPA service provider terms |
| Product changes | Pricing and bot module releases tested for accessible seating rules and challenge accessibility | POL-01 4.14 | 28 CFR 36.302(f) |
| Scope | Scope confirmed every six months and after organizational change | POL-01 4.6 | PCI DSS 12.5.2.1 |

## 4. Hotels and Restaurants drift: conflicts with 2026 group policy
The 2024 hotels standards were written before the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 HO-010; P07 PL-01 findings).

| Topic | Hotels standard (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| PMS accounts | Local PMS accounts managed by each hotel | SYS-G1 for every in-scope system (POL-02 4.1) | 2,600 local accounts; 340 stale (POAM-015) |
| Front desk logins | Shared login allowed "during peak check-in" | Shared accounts prohibited (POL-02 4.1) | Shared logins at 4 hotels |
| Card authorization forms | Email accepted if deleted monthly | Never by email (POL-04 4.2) | 214 forms with security codes found (P03) |
| Log retention | Vendor default (90 days) | 1 year hot (logging standard) | Breach scoping limited (POAM-003) |
| Incident severity | Hotels 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation |
| Rate displays | Not addressed | Total price everywhere (POL-01 4.12) | Resort fee omitted in some channels (P01 HO-005) |
| Common control inheritance | Not addressed | Division must document (POL-01 4.6) | Gap 6 (POAM-014) |

**Why the drift happened.** The 2024 re-organization moved hotels security under the Group CISO, but the supplement had no owner or review date. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Live Venues, Ticketing and Streaming) and on re-issue (Hotels and Restaurants).

# Regulatory Gap Analysis: Cris Santos Company | Financial Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent insurance agency) |
| Tier / Vertical | Sole Proprietorship / Financial Services |
| Regulation analyzed | **Fla. Stat. 501.171** (data security, breach notice, disposal), the binding security law for this agency. Text read from the 2026 Florida Statutes on 2026-10-05 |
| Also checked | Florida Insurance Code duties that carry a security or records obligation: Fla. Stat. 626.561, 626.748, 626.9651 and Rule 69O-128, F.A.C.; the insurers' data security addenda (contract) |
| Yardstick | **16 CFR 314.3-314.4** (FTC Safeguards Rule elements), used as a **benchmark only** to judge "reasonable measures" under 501.171(2) and the addenda's "consistent with GLBA 501(b)" clause. Text read from eCFR (point in time 2026-09-23) |
| Regulation named in the scenario brief | PCI DSS v4.0.1 (vertical default for a payment processor). **Does not apply**: the agency accepts no payment cards (section 1.5) |
| Assessment dates | 2026-08-03 to 2026-08-07 (self-assessment) |
| Assessor | Owner-agent, with the on-call IT consultant (services agreement since 2026-07-27). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-09-14 |

## 1. Applicability
Applicability was decided first, one rule at a time, before any gap was rated.

### 1.1 Is the agency a "financial institution", and who regulates its safeguards?
- **Yes, it is a financial institution under GLBA.** 12 U.S.C. 1843(k)(4)(B) lists "insuring, guaranteeing, or indemnifying against loss ... and acting as principal, agent, or broker for purposes of the foregoing" as financial in nature.
- **The FTC Safeguards Rule does not apply.** GLBA section 505(a)(6) assigns enforcement "in the case of any person engaged in providing insurance" to "the applicable State insurance authority of the State in which the person is domiciled". The FTC covers only a financial institution "not subject to the jurisdiction of any agency or authority under paragraphs (1) through (6)" (505(a)(7); 15 U.S.C. 6805). 16 CFR 314.1(b) limits Part 314 to institutions "over which the Federal Trade Commission ... has jurisdiction", and none of its 13 examples in 314.2(h)(2) is an insurance business. **Contrast:** the Finance and Insurance sole proprietor sample (a state-registered investment adviser) is under the FTC rule because 314.1(b) names advisers not required to register with the SEC.
- **Florida has privacy rules for insurance licensees, not security program rules.** Fla. Stat. 626.9651 directs rules on the use of nonpublic personal financial and health information, based on the NAIC privacy model and "not more restrictive than" GLBA Title V. Rule 69O-128.001 states its purpose as privacy notices, conditions on disclosure, and opt-out methods. Neither sets security program elements.
- **Florida has not enacted the NAIC Insurance Data Security Model Law (#668).** The 2026 Florida Statutes chapters 624, 626, 627, and 628 contain no "cybersecurity event", information security program, or other cyber provision (searched 2026-10-05). The Florida Administrative Code site could not be reached from this environment, so **the owner's counsel is asked to confirm that no other Department of Financial Services or Office of Insurance Regulation rule sets security duties for agents** (action 10).

### 1.2 Fla. Stat. 501.171 applies (primary)
- **Covered entity.** 501.171(1)(b) defines a covered entity as "a sole proprietorship, partnership, corporation ... or other commercial entity that acquires, maintains, stores, or uses personal information". There is no size threshold.
- **Personal information held.** Names with driver license numbers (auto applications), Social Security numbers (some applications and workers compensation owners), and claim details about injuries ("medical history, mental or physical condition"), all listed in 501.171(1)(g)1.a. Bank account and routing numbers on draft forms count only "in combination with any required security code, access code, or password", so most draft forms alone are not personal information under 501.171; they are still nonpublic personal information under Rule 69O-128 and are protected the same way (POL-01).
- **Encryption matters.** Information that is "encrypted, secured, or modified ... [so it is] unusable" is not personal information (501.171(1)(g)2.). An encrypted lost laptop is not a breach; plain email attachments in a taken-over mailbox are.
- **Third-party agent, both ways.** The agency's vendors are its third-party agents (501.171(1)(h), (6)). Under some agency agreements the agency may also be an insurer's third-party agent; counsel confirms per agreement, and the agency plans to the shorter 72-hour addendum clock (G-013, G-047).
- **No federal deemed-compliance path.** 501.171(4)(g) deems notice under a "primary or functional federal regulator's" rules compliant. The agency has no federal regulator, so Florida's own notice rules apply directly (G-010).

### 1.3 Insurer data security addenda apply by contract
4 of the 9 agency agreements carry an addendum: GLBA 501(b)-consistent safeguards, MFA, 72-hour incident notice, and an annual questionnaire. The 16 CFR 314.4 elements were chosen as the yardstick because the addenda point to GLBA 501(b), and because 501.171(2) gives no structure of its own. Where 16 CFR 314.6 would excuse an institution with customer information on fewer than 5,000 consumers (the agency has about 1,900 individuals), the row says so; the owner kept the written risk assessment and incident plan anyway.

### 1.4 The vertical's requirement list
| ID | Requirement | Decision |
|---|---|---|
| C-FINANCIAL-R01 | 12 CFR Part 53 and parallels | Not a bank and not a bank service provider |
| C-FINANCIAL-R02 | Interagency Guidelines | Apply to banks only |
| C-FINANCIAL-R03 | NCUA 12 CFR 748.1(c) | Not a credit union |
| C-FINANCIAL-R04 | SEC Regulation SCI | Not an SCI entity |
| C-FINANCIAL-R05 | NYDFS 23 NYCRR Part 500 | Applies to agents licensed under New York Insurance Law; the agency holds only Florida licenses and refers seasonal clients' New York property to a New York agent. If it ever took a New York license, the 500.19(a) limited exemption (fewer than 20 employees and contractors) would be its first question |
| C-FINANCIAL-R06 | CIRCIA | Proposed only; no final rule as of 2026-09-25. Tracked in section 5 |

### 1.5 Considered and not applicable
| Requirement | Decision |
|---|---|
| PCI DSS | No payment cards accepted; clients pay insurers directly or pay the agency by check or bank transfer |
| HIPAA | No health or group health lines; injury details in claims are protected under 501.171 and Rule 69O-128 instead |
| FTC Safeguards Rule as law | Section 1.1 |
| Other states' breach laws | Apply after a breach, in each state where affected individuals reside (about 60 seasonal residents). Florida is the worked example in P08 |

## 2. Method
1. **Requirements.** 501.171 was decomposed by subsection, with (6)(a) split into the inbound duty (vendors to the agency) and the outbound duty (agency to an insurer). Florida Insurance Code duties were added where they carry a security or records obligation. Each paragraph of 16 CFR 314.3(a) and 314.4 became one benchmark row, using the rule's own numbering. The addenda's two clauses that add duties beyond the benchmark became 2 rows. 48 rows in total.
2. **Crosswalk.** CSF 2.0 and SP 800-53 columns are an **author mapping**; no official NIST mapping of these sources exists.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT consultant: account security pages and sign-in tests (2026-08-05), the browser password store, bank user settings, the contracts folder, the retired laptop, and a garage walkthrough (2026-08-03).
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| Fla. Stat. 501.171 | 0 | 4 | 8 | 2 | 14 |
| Florida Insurance Code (626.561, 626.748, Rule 69O-128) | 1 | 3 | 0 | 0 | 4 |
| 16 CFR 314.3-314.4 (benchmark) | 3 | 14 | 8 | 3 | 28 |
| Insurer data security addenda | 0 | 1 | 1 | 0 | 2 |
| **Total** | **4** | **22** | **17** | **5** | **48** |

Of the 39 unmet or partially met rows, 15 are binding Florida law (12 in 501.171, 3 in the Insurance Code), 2 are contract clauses, and 22 are benchmark elements. Gap risk: 7 High, 17 Moderate, 15 Low.

**What the pattern says:** the 501.171 rows fail for one reason. The agency had no incident procedure, so 8 notice rows are Not met even though nothing has gone wrong. The High gaps are elsewhere: they are the controls around money and the mailbox (trust account access, MFA, monitoring) and the missing written program that the lead insurer is now asking for.

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Adopt POL-01 as the written program; designate the owner | 501.171(2); 314.3(a), 314.4(a) benchmark | High | 2026-09-14 (done) |
| 2 | Authenticator app or security key on email and banking; rater MFA; password manager | 314.4(c)(5), (c)(1)(i) benchmark; Carrier DSA | High | 2026-09-30 |
| 3 | View-only bank sub-user for the bookkeeper; transfer alerts; fixed bank details on invoices and a client letter | 626.561(1) | High | 2026-09-30 |
| 4 | Block outside forwarding; alert on new mailbox rules; monthly review | 314.4(c)(8) benchmark | High | 2026-10-31 |
| 5 | Answer the lead insurer's questionnaire with this program and the POA&M | Carrier DSA | High | 2026-09-30 |
| 6 | Adopt the P08 runbook: Florida 30-day clocks, insurer 72-hour notice, consumer reporting agencies over 1,000 | 501.171(3)-(6); Carrier DSA | Moderate | 2026-10-15 (walkthrough) |
| 7 | Stop the consumer AI chatbot; counsel reviews the pastes | Rule 69O-128.002(16)(b) | Moderate | 2026-09-30 |
| 8 | AMS upload portal for documents; wipe the retired laptop and printer-scanner storage; retention schedule | 314.4(c)(3), (c)(6) benchmark; 501.171(8) | Moderate | 2026-10-31 |
| 9 | Vendor list; security terms with the bookkeeper; quarterly AMS export | 501.171(6); 626.748 | Moderate | 2026-10-31 (export by 2026-12-31) |
| 10 | Security course; counsel confirms no other Florida insurance security rule applies | 314.4(e)(1) benchmark | Moderate | 2026-11-30 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending changes and triggers to watch
- **Fla. Stat. 501.171** was amended in 2026 (ch. 2026-52) to add biometric data and geolocation to "personal information". The rows use the 2026 text; counsel confirms the effective date.
- **NAIC Model #668.** Not enacted in Florida as of the 2026 statutes. If Florida enacts it, re-run this analysis against the enacted Florida text (its program, notice, and any small-licensee exceptions), not against the model.
- **16 CFR Part 314.** No Federal Register document affecting Part 314 was published from 2024-01-01 to 2026-10-05. Because it is only a benchmark here, a change would matter only through the addenda.
- **CIRCIA** (C-FINANCIAL-R06; proposed 6 CFR Part 226, 89 FR 23644). No final rule as of 2026-09-25. **Not a current obligation**; recheck the final scope criteria when published.
- **License trigger.** A New York agent license would bring NYDFS Part 500 (C-FINANCIAL-R05).

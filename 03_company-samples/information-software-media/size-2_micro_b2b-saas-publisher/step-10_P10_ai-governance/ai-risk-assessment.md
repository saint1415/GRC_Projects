# AI Risk Assessment: Generative AI Document Extraction in the Vendor Compliance Platform

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher) |
| Tier / Vertical | Micro / Information |
| AI use case | AI-001: generative AI document extraction, in production for all 45 customers since 2026-04-20 |
| Company role | **Developer and provider** of the feature. Customers are the **deployers**: they decide whether to review or auto-accept what it extracts and how they use vendor status |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1) |
| Assessor / date | CTO with the Software Engineer, Customer Success Manager, and Operations and Finance Manager, 2026-08-31 to 2026-09-04 |
| Decision | CTO and Chief Executive Officer, 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |
| Related items | P01 R-005, R-015, R-016, R-020; P03 G-003, G-019, G-034, G-036; P07 POAM-010, POAM-012; P09 V-02 |

## 1. GOVERN
- **Accountable owner:** the CTO. **Decision authority:** the Chief Executive Officer, because the feature touches every customer and a public claim.
- **Why this assessment is late.** The CTO built the feature in March 2026 and released it to all customers on 2026-04-20 under the model provider's click-through API terms. There was no risk review, no accuracy testing, no sub-processor notice, and the product page claimed "99% accuracy" (scenario gap 15). POL-02 A.2 and A.5 and POL-04 4.6 and 4.7 now require all of these before any AI feature or provider goes live.
- **Policies that apply:**
  - POL-02 A.4: every AI performance claim verified by the CTO and approved by the Chief Executive Officer
  - POL-02 A.5 and POL-04 4.6: no customer data to a vendor without a written agreement, sub-processor listing, and 30 days' notice
  - POL-04 4.3 and 4.7: Social Security numbers masked before AI; approved AI tools list (AI-001 and AI-002 are approved with conditions; AI-003 is prohibited)
- **Scale for a Micro company:** there is no AI committee. The CTO, the Chief Executive Officer, and the Customer Success Manager review AI use at the monthly security review, and before any new AI feature or model change.
- **Model provider:** bought through an API (SYS-06). The company does not train or fine-tune models. The provider's SOC 2 report was reviewed on 2026-09-03 (P09 V-02); it does not cover the zero-retention option.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Read each uploaded certificate of insurance, W-9, or license; fill in fields (insured name, policy type, policy dates, coverage limits, additional insured wording, TIN type, license number and expiry); compare them with the customer's requirements; and draft a short compliance summary for the customer's reviewer |
| Users | Customer reviewers (compliance coordinators and project managers) at all 45 customers; the Customer Success Manager for onboarding |
| Affected people | About 41,000 vendors, many of them small businesses and sole proprietors. A vendor wrongly marked non-compliant can be held off a job site or lose work; one wrongly marked compliant can leave a customer exposed to an uninsured loss. About 9,800 sole proprietors' Social Security numbers pass through the feature |
| Inputs | Full document images and text sent to the model provider, including full taxpayer identification numbers on W-9s |
| Outputs | Extracted fields marked "AI-filled" on the reviewer screen, a confidence score per field, and a draft summary. With **auto-accept** on (31 of 45 customers), extracted fields are saved and can change a vendor's status with no human review |
| Build or buy | Company-built feature on a bought model |
| Not intended | Deciding which vendors a customer hires; reading documents other than the three types above; any use of vendor data to train or improve models. Adding any of these requires a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5 (N51-R01) | **Yes** | Deception: the "99% accuracy" claim had no test behind it, and the website says tax IDs never leave the platform while every W-9 goes to the model provider (P03 G-032, G-034). Unfairness: sending Social Security numbers to a vendor without need exposes individuals who cannot protect themselves (15 U.S.C. 45(n)). The FTC's proposed AI-accuracy policy statement (Docket FTC-2026-0727) is **not final** and is a watch item only |
| Customer DPA | **Yes** | Customer data may be used only to provide the service, and a new sub-processor needs listing and 30 days' notice. Neither happened (P03 G-036, G-038) |
| Fla. Stat. 501.171(2) | **Yes** | As a third-party agent, the company must take reasonable measures to protect personal information. Sending full Social Security numbers to a vendor on click-through terms is hard to defend as reasonable |
| CPPA ADMT regulations (N51-R03) | **Not today** | The company is not a CCPA business and has no California customers (P03 section 1.3). If a customer that is a CCPA business uses vendor status for decisions covered by the ADMT rules, that customer would carry the duties; recheck when a California customer signs |
| Colorado SB26-189 (effective 2027-01-01) | **Not today; watch** | Developer documentation duties apply to automated decision tools that materially influence consequential decisions. No customer operates in Colorado today, and whether a vendor's eligibility for contracted work is a covered decision has not been confirmed. Counsel to recheck if a Colorado customer signs |
| DOJ Data Security Program (N51-R04) | No | The model provider is U.S.-based; no covered data transactions (P03 section 1.4) |

## 3. Risk tier
**Tier: High as operated today; Medium once the conditions in section 6 are met** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why High today:** with auto-accept on, the extracted expiry dates and coverage limits **are** the decision on whether a vendor is compliant, with no human in between, for 31 customers. The output affects whether small businesses and sole proprietors can work on a site, and the feature handles Social Security numbers.
- **Why Medium after the conditions:** a customer reviewer confirms every date, limit, and status change, low-confidence fields are flagged, and Social Security numbers no longer leave the platform. The AI then drafts; a person decides.

**Re-tier and reassess if:** auto-accept is re-enabled for dates, limits, or status; new document types are added (for example, bank letters or identity documents); the model or model provider changes; or customers start using status to rank or select vendors.

## 4. MEASURE
The Customer Success Manager and the Software Engineer labeled a test set of 400 documents from 12 customers (250 certificates, 100 W-9s, 50 licenses) and ran it through the production prompts on 2026-09-02. Tests used copies inside the production account; no new data went to any vendor.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Field-level accuracy across all fields; critical errors (wrong expiry date, wrong coverage limit, wrong insured name) under 0.5% of documents | 93.5% field-level accuracy; 7 of 250 certificates (2.8%) had a critical error; 2 of 100 W-9s had the TIN type wrong | **No.** Does not support "99%"; critical error rate far above threshold |
| Safe | No vendor status changes without a person confirming dates and limits | 31 of 45 customers use auto-accept; 3 of the 7 critical errors would have marked an expired policy as current | **No** |
| Secure and resilient | Prompt injection: 15 crafted documents with hidden instructions in the text | 2 of 15 changed an extracted field (both set a coverage limit above the printed value); none reached another tenant's data | **Partial** (R-020) |
| Accountable and transparent | AI-filled fields labeled; public claims accurate; customers told about the model provider | Fields labeled "AI-filled"; "99% accuracy" claim unsupported; provider not on the sub-processor list | **No** |
| Explainable and interpretable | Reviewer can see where each value came from | Each field highlights its source region on the document image | Yes |
| Privacy-enhanced | Minimum data to the provider; signed no-training and zero-retention terms | Full W-9 images with Social Security numbers sent; click-through terms allow 30-day retention for abuse monitoring | **No** |
| Fair, with harmful bias managed | Compare critical error rates for documents by quality and source; flag a gap over 2 percentage points | Phone photos and scans of handwritten forms: 5 of 36 certificates with a critical error (13.9%); clean digital PDFs: 2 of 214 (0.9%) | **No (flagged)** |

**Bias finding.** The platform holds no data on vendors' race, sex, or ethnicity, so the test compared document quality, which tracks business size. Phone photos and handwritten forms come mostly from sole proprietors and very small firms. Their certificates were far more likely to be misread, so small vendors bear most of the risk of being wrongly marked non-compliant, or of an expired policy slipping through. The sample is small, but the gap is large enough to treat as real.

## 5. MANAGE
**Data protection:**
- Before any W-9 goes to the model provider, the worker redacts the TIN box on the image (the form layout is fixed) and reads the TIN with the cloud provider's text recognition service inside the company's own account. Only the TIN type and last 4 digits are stored as fields (POL-04 4.3; POAM-012; R-005).
- A signed DPA with the model provider with no-training and zero-retention terms; the provider added to the sub-processor list; customers notified with a 30-day objection window (POAM-010; R-016).
- Extracted text and prompts are never written to error tracking (POL-04 4.11).

**Human in the loop:**
- Auto-accept is turned off for expiry dates, coverage limits, and any status change from 2026-10-15. A customer reviewer must confirm these fields; other fields (address, policy type) may still auto-fill.
- Fields with a confidence score below 0.9, and every document received as a phone photo or handwritten form, go to the reviewer with a "check carefully" flag.
- Rule checks run after extraction: an expiry date in the past, a limit above the policy's printed maximum, or a mismatch between the insured name and the vendor name blocks the update until a reviewer confirms it.
- Customers get a one-page guide on what the feature does, its measured accuracy, and when to override it.

**Security:** document text is passed to the model as data, with instructions kept separate, and the rule checks above catch inflated limits (R-020). The 2027-01 penetration test covers the feature.

**Accurate claims:** the "99% accuracy" claim is withdrawn by 2026-10-15 (P03 G-034). Any future figure must come from this test method, state the test date and document mix, and be approved under POL-02 A.4.

**Monitoring:**
- Monthly: 100 production documents sampled and checked by the Customer Success Manager; critical error rate by document quality.
- Quarterly: rerun the 400-document test set and the prompt injection set; results to the monthly security review.
- After any model or prompt change: rerun both sets before release.
- Customer and vendor complaints about extraction go to the CTO and are logged against R-015.

**Incident handling:** a wrong status that reaches a customer decision is handled under POL-03, with the customer told within 72 hours if its data or decisions were affected. A model provider security incident follows P08 and the DPA terms.

**Decommissioning:** a feature flag switches extraction off for one customer or all customers at once; documents then go to the manual review queue (P05 BP-02 workaround). If the model provider DPA is not signed by 2026-10-31, calls to the provider stop and extraction is switched off until it is.

## 6. Decision
**Approve with conditions.** CTO and Chief Executive Officer, 2026-09-15.

The feature stays in production, with these conditions:
1. By 2026-10-15: auto-accept off for expiry dates, coverage limits, and status changes; the "99% accuracy" claim withdrawn.
2. By 2026-10-31: TIN redaction before any W-9 is sent; model provider DPA with no-training and zero-retention terms signed; provider listed; customers notified with a 30-day objection window. If the DPA is not signed, extraction is switched off.
3. By 2026-11-30: rule checks, low-confidence and document-quality flags, and the customer guide live; first monthly sample recorded.
4. Auto-accept for any date, limit, or status field may return only after two consecutive quarterly tests show a critical error rate under 0.5% overall **and** for phone photos and handwritten forms, with no open bias flag, and after a new assessment.

**Next review:** at the first quarterly test (by 2026-12-31) and no later than 2027-03-31, before the SOC 2 Type 1 date.

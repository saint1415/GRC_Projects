# AI Risk Assessment: Transformer Health Scoring and Rebuild Demand Forecasting

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (transformer repair and remanufacturing shop, Florida) |
| Tier / Vertical | Micro / Critical Manufacturing |
| AI use case | AI-001: the oil laboratory's AI health-scoring portal, used for predictive maintenance of customers' transformers and to forecast storm-season rebuild demand. Pilot since 2026-04 with 3 customers (about 900 units) |
| Why this use case | The registry default is "demand forecasting and predictive maintenance." A 7-person shop builds no models, so the default is met by the one AI service the shop actually uses, which serves both purposes (see `../00_company-facts.md` section 5) |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook. AI 600-1 applies only to AI-003 (public generative AI), handled by policy |
| Assessor / date | Office Manager (Security Coordinator) with the Field Service and Test Technician and the Shop Manager, 2026-08-25 |
| Decision | Owner, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Owner, who sells the fleet health service to customers. **Operator:** the Field Service and Test Technician. **Decision authority:** the Owner.
- **Policies that apply:**
  - POL-04 4.7: Restricted data only in approved AI tools; AI-001 approved only with customer consent, no site coordinates, and no training use by the vendor.
  - POL-02 A.5: no terms, no access. The AI vendor holds customer confidential data, so written terms are required.
  - POL-02 C.2 and POL-04 4.7: no FCI, rewind library, or employee data in any AI tool, and no Restricted data in public chatbots (AI-003).
- **Approved-tools list:** kept by the Office Manager in POL-04 4.7. It has one entry, AI-001, under the conditions in section 6.
- **Scale for a Micro shop:** there is no AI committee. The Owner, Office Manager, and Shop Manager review AI use at the monthly security meeting. A new AI tool, new data source, or new customer needs a short review like this one first (CSF GV.OC-03; SOC 2 CC3.4).

**How the pilot started.** The oil laboratory offered the portal free with its testing service in 2026-04. The Field Service and Test Technician began uploading DGA results and nameplate data, including site coordinates, for 2 cooperatives and 1 municipal utility. Nobody read the vendor's terms, which allow it to use uploaded data to improve its models, and nobody asked the customers. The G&T cooperative's master service agreement treats its substation locations and equipment data as confidential information (P01 R-018).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | (a) **Predictive maintenance:** score each customer transformer's condition (good, watch, poor) from its DGA history so the shop can recommend retest, oil processing, repair, or replacement before failure. (b) **Demand forecasting:** count units rated "poor" or "watch" by size class to plan how many rebuild cores, how much copper, and how many storm-stock units to hold for the hurricane season |
| Users / operators | Field Service and Test Technician (uploads, reviews scores, writes recommendations); Owner (customer reports, stock plan) |
| Affected parties | Utility and solar farm customers and the people they serve. A transformer kept in service when it should be replaced can fail, causing an outage, an oil spill, or a fire. No individual people are scored |
| Data | Inputs: DGA results (dissolved gas concentrations), oil quality tests, nameplate data (size, voltage, age, fluid type), customer asset IDs, and until now site coordinates. Outputs: health score, gas trend charts, and a suggested action. No personal data and no FCI (the federal order's units are not uploaded) |
| Build or buy | Buy: vendor SaaS. The vendor's documentation says its model was built mainly on mineral oil data from larger power transformers |
| Not intended | Automatic recommendations to customers without a technician's review; decisions about the safety of energized equipment in the field; pricing; anything about individual employees |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Customer confidentiality terms (cooperative master service agreement) | **Yes** | The cooperative's substation data is its confidential information. Sharing it with a vendor that may train on it needs the cooperative's consent and terms that prevent other use |
| Cooperative exhibit sec. 1 (CIP-013-2 R1.2.1 flow-down) | **Yes, if there is an incident** | A security incident at the AI vendor that exposes cooperative data would be an incident related to services the shop supplies, starting the 72-hour notice clock (P08) |
| FTC Act Section 5 (15 U.S.C. 45(a)) | **Yes, for the shop's own claims** | If the shop markets the service as "AI-powered fleet health," its claims about accuracy must be truthful and supported. The FTC's July 2026 AI accuracy policy statement is proposed only and is not relied on |
| FAR 52.204-21 | No new issue | No FCI is uploaded. AI-003 public chatbots must not receive FCI ((b)(1)(iii)) |
| State consequential-decision AI laws (for example Colorado SB26-189) | No | AI-001 makes no decision about an individual. The shop operates in Florida and neighboring states only |
| Sector AI rules for critical manufacturing | None found | The vertical profile lists no sector AI rules. The NIST AI RMF Critical Infrastructure Profile is only a concept note (2026-04-07); watch it |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why High:** the rubric puts any AI that "can affect physical safety or critical infrastructure operations" in the High tier. A health score that leads the shop to tell a utility a deteriorating transformer can stay in service can contribute to a distribution outage or a transformer fire. The customer makes the final decision, but the shop's recommendation, built on the score, is a substantial input.
- **Why this is not a reason to stop:** the minimum High-tier controls are achievable at this size: human review before any recommendation, pre-deployment testing, an impact assessment (this document), notice to customers, and ongoing monitoring.
- **Demand forecasting half:** on its own this would be Low (internal planning, a person approves every purchase). It shares the tier because it uses the same scores.

**Re-tier or re-assess if:** the portal sends recommendations to customers directly; the shop uses a score as the only basis for any recommendation; the service expands beyond 3 customers or to substation power transformers; or the vendor changes its model or data terms.

## 4. MEASURE
The Field Service and Test Technician and the Shop Manager back-tested the scores on 2026-08-20 against the shop's own teardown findings: 40 customer units that were scored in the portal between 2026-04 and 2026-06 and later came into the shop and were opened up.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Of units found at teardown with an internal fault (arcing, overheating, insulation failure), share rated "poor" or "watch". Target: at least 90%, and no fault rated "good" | 13 of 15 faulty units flagged (87%). 2 rated "good": one with a winding fault whose oil had been processed 4 months earlier (gases reset), one with low sample history | **No** |
| Valid and reliable (false alarms) | Of units found sound at teardown, share rated "poor". Target: 20% or less | 5 of 25 (20%) | Yes (at the limit) |
| Safe | Every recommendation reviewed by the technician against raw gas values before it reaches a customer | Informal review; no record for 31 of 40 recommendations; one of the two misses was caught by the technician from a rising acetylene trend | **No** |
| Secure and resilient | MFA on the portal account; vendor security evidence | MFA on; one shared login used only by the technician; no SOC 2 report, vendor questionnaire requested | Partial |
| Accountable and transparent | Customers told that scores are AI-assisted and how they are checked | Customer reports show the score with no explanation of how it is produced or reviewed | **No** |
| Explainable and interpretable | Technician can see the gas values and trends behind each score | Gas trend charts available for every unit | Yes |
| Privacy-enhanced (here: customer confidentiality) | Customer consent; no site coordinates; no vendor training on shop data | No consent; coordinates uploaded; standard terms allow training use | **No** |
| Fair, with harmful bias managed (here: data representativeness) | Compare false-alarm rates by fluid type and unit type; flag a gap over 15 percentage points | Natural ester-filled units (mostly at solar farms): 3 of 6 sound units rated "poor" (50%); mineral oil units: 2 of 19 (11%). Pole-mounted units: too few teardowns (4) to judge | **No (flagged)** |

**Representativeness finding.** The vendor says its model was trained mainly on mineral oil data. Ester-filled units gas differently, and the back-test shows far more false "poor" ratings for them. A false alarm is less dangerous than a miss, but it could lead a solar farm customer to replace a sound unit on the shop's advice. Until the vendor provides accuracy data for ester-filled units, their scores are not used: the technician interprets their DGA results directly.

**Missed faults.** The two misses share a cause the model cannot see: recent oil processing or too few samples. The technician's written interpretation steps (section 5) require a manual review whenever the oil was processed in the last 12 months or there are fewer than 3 samples.

## 5. MANAGE
**Data protection:**
- Stop uploading site coordinates now; ask the vendor to delete those already uploaded and confirm in writing.
- Data processing addendum with the vendor: no use of shop or customer data to train or improve models or for any purpose other than providing the service; deletion within 30 days of request or contract end; security incident notice to the shop within 24 hours (so the shop can meet the cooperative's 72-hour clock); MFA; subcontractor flow-down (POL-02 A.5).
- Written consent from each of the 3 customers to their data being processed in the portal under those terms; the cooperative's consent references its confidentiality clause.
- The portal account is added to the monthly account reconciliation (POL-02 B.5).

**Human in the loop:**
- The score is a screening aid. The Field Service and Test Technician reviews the raw gas values and trends for every unit before any recommendation goes to a customer, using written interpretation steps that name the industry DGA interpretation guide the shop follows.
- Manual review is required, regardless of score, when the oil was processed in the last 12 months, when there are fewer than 3 samples, or for ester-filled units.
- Any recommendation to keep a unit in service that the model rates "poor" must be co-signed by the Shop Manager with the reason recorded.
- Customer reports state: "Condition score produced by an AI model and reviewed by a qualified technician. Recommendations are advisory; the owner of the equipment decides."

**Monitoring:**
- Every unit that comes into the shop for teardown is compared with its last score; results are logged monthly against P01 R-017.
- Quarterly: miss rate and false-alarm rate, by fluid type and unit type.
- Demand forecast: compare the forecast count of rebuilds with actual rebuilds each quarter; the Owner sets storm stock, not the forecast.

**Incident handling:** a missed fault that leads to a customer failure is investigated by the Owner and reported to the customer. A vendor security incident is handled under POL-03 and the P08 runbook, including the cooperative notice check.

**Decommissioning:** stop using the portal for recommendations if the addendum is not signed by 2026-09-30, if a fault is missed in two consecutive quarters after the conditions are met, or if the vendor changes its data terms. Export all scores and gas histories first, and ask the vendor to confirm deletion of all shop and customer data.

## 6. Decision
**Approve with conditions.** Owner, 2026-08-31.

Uploads are paused from 2026-08-31 and recommendations based on the portal stop until all of these are met:
1. The data processing addendum is signed with the terms in section 5 (target 2026-09-30; R-018; POAM-012).
2. Site coordinates are deleted by the vendor and no longer uploaded.
3. Written consent is received from the 3 customers.
4. The written interpretation steps, the co-sign rule, and the customer report wording are in use.
5. Ester-filled units are excluded from scoring until the vendor provides accuracy data for them.

Expansion beyond the 3 pilot customers requires two consecutive quarters with no missed fault in the teardown comparison, no open representativeness flag, and a vendor security review.

**AI-002 (ERP stock forecast add-on):** Low tier. It may be enabled after a short review confirming that the ERP vendor's terms bar training use of shop data and that no FCI fields are used; the Office Manager keeps approving every purchase order.

**AI-003 (public chatbots):** prohibited for any Restricted information or FCI (POL-04 4.7; POL-02 C.2). Allowed only for text with no company or customer details. Covered in the October 2026 training (POAM-010).

# What has been accomplished

This page is the short answer to "what did you build?" It covers the whole library for the fictitious **Cris Santos Company**: the 10 projects from the [GRC Project List](https://nicoleenesse.notion.site/GRC-Project-List-3bf8eef497be8080afc3ee1cbd34bf68), applied across industries and company sizes.

## In one paragraph

One universal method for each of the 10 GRC projects was built once, then applied to one company shown in 36 industries and 6 sizes. Each finished sample company has all 10 deliverables, from business impact analysis to AI governance. It also has one facts file that every deliverable shares, so a reader can follow a risk from the risk register to the policy that answers it and the test that checks it. Every regulation is cited to its primary source, and every sample passes automated checks: risk scores recalculate from the NIST tables, and every control test statement matches NIST's official wording. A public [explorer site](https://saint1415.github.io/GRC_Projects/) lets anyone read each company as a plain-English story, in two looks or a plain reading mode.

## Phases

| Phase | What it delivered | Status |
|---|---|---|
| 0. Foundation | Universal framework (NIST CSF 2.0, SP 800-53 Rev. 5, SP 800-53A), 6 company sizes, 36 industries, generator, validator, 216 sample folders | Done |
| 1. Flagship | Health Care, Small: a multi-specialty physician practice, all 10 projects | Done |
| 2. Size ladder | Health Care at all 6 sizes, from a solo physician to a multi-sector health group | Done |
| 3. Named industries | Small samples for Manufacturing, Defense, Wholesale, Retail, Transportation, SaaS, Finance, Education | Done |
| 4. Every industry | Small samples for the remaining 27 industries, so every sector has one finished company | Done |
| 5. Full matrix | The other five sizes for each of the other 35 industries (175 companies) | Done: all 216 companies finished and validated |

Phase records, decisions, and corrections: [PLAN.md](PLAN.md).

## Since Phase 5 (2026-10-07 to 2026-10-08)

| Work | What it delivered | Pull requests |
|---|---|---|
| Sample company explorer | A public website built from the sample folders: [saint1415.github.io/GRC_Projects](https://saint1415.github.io/GRC_Projects/). A landing page offers two looks, **Case Files** (an auditor's file drawer, on light or dark paper) and **Threat Board** (an operations console), plus a plain reading mode. A switch on every page swaps looks and keeps your place. Each company is told as a 9-part plain-English story, with a guided 10-step tour, search by rule, side-by-side size comparison, and an incident simulator that runs the company's legal notice clocks. Rebuilt by `tools/build_explorer.py`. Threat Board sound was later made audible: tones had played at 1 to 5 percent volume. | [#2](https://github.com/saint1415/GRC_Projects/pull/2), [#4](https://github.com/saint1415/GRC_Projects/pull/4), [#5](https://github.com/saint1415/GRC_Projects/pull/5), [#15](https://github.com/saint1415/GRC_Projects/pull/15) |
| External architecture review | An outside review (Gemini) was answered point by point with repository evidence and primary sources: [response](docs/reviews/2026-10-gemini-architecture-review-response.md). Several claims did not hold up, for example that the defense samples use SP 800-171 Rev. 3, that NYC Local Law 144 was missing, and that small companies were given enterprise cloud designs. The valid points were fixed: correct legal forms for the national bank, credit union, and electric cooperative; bank, NRC, and FOCI ownership approvals; fit checks before SOC 2 and AI work; the as-is security plan explained against the NIST RMF; and a compensating controls table for one-person companies. | [#3](https://github.com/saint1415/GRC_Projects/pull/3) |
| Review backlog | All 36 sole proprietor security plans gained explicit compensating controls for AC-5, AU-9, CM-3, and CA-2(1). All 36 Multi-Sector cloud architectures gained a tenancy and identity decision. The nuclear size 5 and 6 samples gained license-transfer rows (10 CFR 50.80). | [#5](https://github.com/saint1415/GRC_Projects/pull/5) |
| Multi-Sector pairings review | All 36 three-division pairings were checked for realism, teaching value, and lawful ownership: [review](docs/reviews/2026-10-multi-sector-pairings-review.md). All were kept. Three gained missing facts: utility holding company and affiliate purchase rules (18 CFR 366, 35.44; Fla. Admin. Code R. 25-6.1351) and Florida lending licenses for a store card (Fla. Stat. 520.32, 516.02). | [#6](https://github.com/saint1415/GRC_Projects/pull/6) |
| CMMC Phase 2 suspension | DoD Class Deviation 2026-O0025, Revision 3 was read in full. It confirms that Phase 2 (planned for 2026-11-10) is suspended and that SP 800-171 Rev. 2 still applies under DFARS 252.204-7012. The industry rules and 29 affected samples were updated, each as of its own assessment date, with no change to any score or count. | [#7](https://github.com/saint1415/GRC_Projects/pull/7) |
| FAR overhaul clause numbers | The FAR Part 40 deviation text in use at DoD, GSA, DHS, DOE, VA, and most other agencies was read and applied dual-track: contracts already awarded keep FAR 52.204-21, -23, -25 and DFARS 252.204-7019/-7020, while new awards carry FAR 52.240-90 to -93 and DFARS 252.240-7997. The real change, one prohibited-product report within 72 hours (FAR 52.240-91(h)), now appears in all 200 notification matrices that cite the old clauses. | [#8](https://github.com/saint1415/GRC_Projects/pull/8) |
| Unverified research rows | 17 of the 19 industry rule rows marked unverified were checked against primary sources: [review](docs/reviews/2026-10-unverified-vertical-rows-review.md). Generic "varies by state" breach rows became a Florida worked example with real clocks (Fla. Stat. 501.171). FedRAMP incident reporting now follows the 2026 Rev5 rules, with first-report clocks by impact rating and certification class. Local government reporting cites Fla. Stat. 282.3185 (12 hours for ransomware). Federal agency reporting cites 44 U.S.C. 3554 and CISA's 1-hour guideline. The lawyer confidentiality row is anchored to the Florida Bar rules. Card compromise rows in the industry rules and 18 samples now carry Visa's verified clocks: report to Visa within 3 calendar days of suspicion, with the incident report 3 days after that (Visa What To Do If Compromised v10.0). American Express's own rules were then verified for the other-brand rows in 16 samples: notify within 72 hours of discovery (Data Security Operating Policy, April 2026, Section 3). Mastercard and Discover rules stay unverified because their sites could not be read. The 46 merchant-agreement card rows were then reviewed: the 32 with fictional contract clocks match their samples' facts and runbooks, and the 14 that gave no clock now carry Visa's verified 3-day reporting duty. Illinois BIPA and the AICPA Code stay unverified because their sources could not be reached. | [#10](https://github.com/saint1415/GRC_Projects/pull/10), [#11](https://github.com/saint1415/GRC_Projects/pull/11), [#13](https://github.com/saint1415/GRC_Projects/pull/13), [#15](https://github.com/saint1415/GRC_Projects/pull/15) |

**Checks after each change:** `tools/validate.py` reports 0 errors across 216 samples and 5,836 markdown files. The one remaining warning is the 2 industry rule rows still marked unverified (Illinois BIPA and the AICPA Code). Open items and the regulatory watch list are in [PLAN.md](PLAN.md).

## What the samples demonstrate

- **Scalability.** The same project at six sizes: a solo practitioner's one-page policy grows into a group-wide policy hierarchy with division supplements. See the [build guide](docs/how-to-build-the-10-projects.md), section 2.
- **A deliberate build order.** Projects are built in dependency order (business impact analysis first, AI governance last), so each one reuses the last. Folder names carry the step number.
- **Applicability before analysis.** Each gap analysis first asks whether the headline rule actually binds this company at this size. Examples: TSA pipeline and rail directives reach only designated operators, the NRC reactor cyber rule does not reach a waste processor, and FedRAMP does not apply without a federal customer. When the rule does not apply, the sample says so with the citation and uses the rule that does.
- **Official mappings where they exist.** The HIPAA gap analyses carry NIST's official HIPAA-to-SP 800-53 mapping (OLIR 110). Where a mapping is the author's own, it is labeled.
- **Keeping current.** When a rule changes, the change is read at its primary source and applied once in the shared layers, then to each affected sample as of that sample's own date. The CMMC Phase 2 suspension and the FAR overhaul renumbering were handled this way.
- **Verification discipline.** Regulatory facts were checked against eCFR, the Federal Register, and agency sites. Errors found along the way were corrected across all affected samples. One example: the scope of Florida's 15-day breach notice extension. Each correction is recorded in PLAN.md.

## Finished sample companies

<!-- BEGIN GENERATED: finished samples (tools/build_scenarios.py) -->
**215 of 216** sample companies are finished (2,150 deliverables). Planned folders are listed in [03_company-samples/INDEX.md](03_company-samples/INDEX.md).

| Industry | Size | Company | Brief |
|---|---|---|---|
| Agriculture, Forestry, Fishing and Hunting | Sole Proprietorship | Crop farm | [README](03_company-samples/agriculture/size-1_sole-proprietor_crop-farm/README.md) |
| Agriculture, Forestry, Fishing and Hunting | Micro | Crop farm | [README](03_company-samples/agriculture/size-2_micro_crop-farm/README.md) |
| Agriculture, Forestry, Fishing and Hunting | Small | Diversified crop farm | [README](03_company-samples/agriculture/size-3_small_diversified-crop-farm/README.md) |
| Agriculture, Forestry, Fishing and Hunting | Mid-Market | Crop farm | [README](03_company-samples/agriculture/size-4_mid-market_crop-farm/README.md) |
| Agriculture, Forestry, Fishing and Hunting | Enterprise | Crop farm | [README](03_company-samples/agriculture/size-5_enterprise_crop-farm/README.md) |
| Agriculture, Forestry, Fishing and Hunting | Multi-Sector | Crop farm plus two divisions | [README](03_company-samples/agriculture/size-6_multi-sector_crop-farm-plus-two-divisions/README.md) |
| Food and Agriculture | Sole Proprietorship | Custom-exempt meat processor | [README](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-1_sole-proprietor_custom-exempt-meat-processor/README.md) |
| Food and Agriculture | Micro | Meat processor | [README](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-2_micro_meat-processor/README.md) |
| Food and Agriculture | Small | Meat processor | [README](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-3_small_meat-processor/README.md) |
| Food and Agriculture | Mid-Market | Meat processor | [README](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-4_mid-market_meat-processor/README.md) |
| Food and Agriculture | Enterprise | Meat processor | [README](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-5_enterprise_meat-processor/README.md) |
| Food and Agriculture | Multi-Sector | Meat processor plus two divisions | [README](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-6_multi-sector_meat-processor-plus-two-divisions/README.md) |
| Mining, Quarrying, and Oil and Gas Extraction | Sole Proprietorship | Oilfield services contractor | [README](03_company-samples/mining-oil-gas/size-1_sole-proprietor_oilfield-services-contractor/README.md) |
| Mining, Quarrying, and Oil and Gas Extraction | Micro | Crude oil producer | [README](03_company-samples/mining-oil-gas/size-2_micro_crude-oil-producer/README.md) |
| Mining, Quarrying, and Oil and Gas Extraction | Small | Crude oil producer | [README](03_company-samples/mining-oil-gas/size-3_small_crude-oil-producer/README.md) |
| Mining, Quarrying, and Oil and Gas Extraction | Mid-Market | Crude oil producer | [README](03_company-samples/mining-oil-gas/size-4_mid-market_crude-oil-producer/README.md) |
| Mining, Quarrying, and Oil and Gas Extraction | Enterprise | Crude oil producer | [README](03_company-samples/mining-oil-gas/size-5_enterprise_crude-oil-producer/README.md) |
| Mining, Quarrying, and Oil and Gas Extraction | Multi-Sector | Crude oil producer plus two divisions | [README](03_company-samples/mining-oil-gas/size-6_multi-sector_crude-oil-producer-plus-two-divisions/README.md) |
| Utilities | Sole Proprietorship | Utility engineering consultant | [README](03_company-samples/utilities/size-1_sole-proprietor_utility-engineering-consultant/README.md) |
| Utilities | Micro | Small electric cooperative | [README](03_company-samples/utilities/size-2_micro_small-electric-cooperative/README.md) |
| Utilities | Small | Electric distribution utility | [README](03_company-samples/utilities/size-3_small_electric-distribution-utility/README.md) |
| Utilities | Mid-Market | Electric distribution utility | [README](03_company-samples/utilities/size-4_mid-market_electric-distribution-utility/README.md) |
| Utilities | Enterprise | Electric distribution utility | [README](03_company-samples/utilities/size-5_enterprise_electric-distribution-utility/README.md) |
| Utilities | Multi-Sector | Electric distribution utility plus two divisions | [README](03_company-samples/utilities/size-6_multi-sector_electric-distribution-utility-plus-two-divisions/README.md) |
| Energy | Sole Proprietorship | Pipeline integrity consultant | [README](03_company-samples/utilities_energy-critical-infrastructure/size-1_sole-proprietor_pipeline-integrity-consultant/README.md) |
| Energy | Micro | Small intrastate pipeline | [README](03_company-samples/utilities_energy-critical-infrastructure/size-2_micro_small-intrastate-pipeline/README.md) |
| Energy | Small | Gas transmission pipeline | [README](03_company-samples/utilities_energy-critical-infrastructure/size-3_small_gas-transmission-pipeline/README.md) |
| Energy | Mid-Market | Gas transmission pipeline | [README](03_company-samples/utilities_energy-critical-infrastructure/size-4_mid-market_gas-transmission-pipeline/README.md) |
| Energy | Enterprise | Gas transmission pipeline | [README](03_company-samples/utilities_energy-critical-infrastructure/size-5_enterprise_gas-transmission-pipeline/README.md) |
| Energy | Multi-Sector | Gas transmission pipeline plus two divisions | [README](03_company-samples/utilities_energy-critical-infrastructure/size-6_multi-sector_gas-transmission-pipeline-plus-two-divisions/README.md) |
| Dams | Sole Proprietorship | Dam safety consultant | [README](03_company-samples/utilities_dams-critical-infrastructure/size-1_sole-proprietor_dam-safety-consultant/README.md) |
| Dams | Micro | Hydroelectric dam operator | [README](03_company-samples/utilities_dams-critical-infrastructure/size-2_micro_hydroelectric-dam-operator/README.md) |
| Dams | Small | Hydroelectric dam operator | [README](03_company-samples/utilities_dams-critical-infrastructure/size-3_small_hydroelectric-dam-operator/README.md) |
| Dams | Mid-Market | Hydroelectric dam operator | [README](03_company-samples/utilities_dams-critical-infrastructure/size-4_mid-market_hydroelectric-dam-operator/README.md) |
| Dams | Enterprise | Hydroelectric dam operator | [README](03_company-samples/utilities_dams-critical-infrastructure/size-5_enterprise_hydroelectric-dam-operator/README.md) |
| Dams | Multi-Sector | Hydroelectric dam operator plus two divisions | [README](03_company-samples/utilities_dams-critical-infrastructure/size-6_multi-sector_hydroelectric-dam-operator-plus-two-divisions/README.md) |
| Nuclear Reactors, Materials, and Waste | Sole Proprietorship | Radiation safety consultant | [README](03_company-samples/utilities_nuclear-critical-infrastructure/size-1_sole-proprietor_radiation-safety-consultant/README.md) |
| Nuclear Reactors, Materials, and Waste | Micro | Radiation safety consulting practice | [README](03_company-samples/utilities_nuclear-critical-infrastructure/size-2_micro_radiation-safety-consulting-practice/README.md) |
| Nuclear Reactors, Materials, and Waste | Small | Radioactive waste processor | [README](03_company-samples/utilities_nuclear-critical-infrastructure/size-3_small_radioactive-waste-processor/README.md) |
| Nuclear Reactors, Materials, and Waste | Mid-Market | Nuclear power plant | [README](03_company-samples/utilities_nuclear-critical-infrastructure/size-4_mid-market_nuclear-power-plant/README.md) |
| Nuclear Reactors, Materials, and Waste | Enterprise | Nuclear power plant | [README](03_company-samples/utilities_nuclear-critical-infrastructure/size-5_enterprise_nuclear-power-plant/README.md) |
| Nuclear Reactors, Materials, and Waste | Multi-Sector | Nuclear power plant plus two divisions | [README](03_company-samples/utilities_nuclear-critical-infrastructure/size-6_multi-sector_nuclear-power-plant-plus-two-divisions/README.md) |
| Water and Wastewater Systems | Sole Proprietorship | Small water system | [README](03_company-samples/utilities_water-critical-infrastructure/size-1_sole-proprietor_small-water-system/README.md) |
| Water and Wastewater Systems | Micro | Community water system | [README](03_company-samples/utilities_water-critical-infrastructure/size-2_micro_community-water-system/README.md) |
| Water and Wastewater Systems | Small | Community water system | [README](03_company-samples/utilities_water-critical-infrastructure/size-3_small_community-water-system/README.md) |
| Water and Wastewater Systems | Mid-Market | Community water system | [README](03_company-samples/utilities_water-critical-infrastructure/size-4_mid-market_community-water-system/README.md) |
| Water and Wastewater Systems | Enterprise | Community water system | [README](03_company-samples/utilities_water-critical-infrastructure/size-5_enterprise_community-water-system/README.md) |
| Water and Wastewater Systems | Multi-Sector | Community water system plus two divisions | [README](03_company-samples/utilities_water-critical-infrastructure/size-6_multi-sector_community-water-system-plus-two-divisions/README.md) |
| Construction | Sole Proprietorship | Commercial general contractor | [README](03_company-samples/construction/size-1_sole-proprietor_commercial-general-contractor/README.md) |
| Construction | Micro | Commercial general contractor | [README](03_company-samples/construction/size-2_micro_commercial-general-contractor/README.md) |
| Construction | Small | Commercial general contractor | [README](03_company-samples/construction/size-3_small_commercial-general-contractor/README.md) |
| Construction | Mid-Market | Commercial general contractor | [README](03_company-samples/construction/size-4_mid-market_commercial-general-contractor/README.md) |
| Construction | Enterprise | Commercial general contractor | [README](03_company-samples/construction/size-5_enterprise_commercial-general-contractor/README.md) |
| Construction | Multi-Sector | Commercial general contractor plus two divisions | [README](03_company-samples/construction/size-6_multi-sector_commercial-general-contractor-plus-two-divisions/README.md) |
| Manufacturing | Sole Proprietorship | CNC machine shop | [README](03_company-samples/manufacturing/size-1_sole-proprietor_cnc-machine-shop/README.md) |
| Manufacturing | Micro | Medical device startup | [README](03_company-samples/manufacturing/size-2_micro_medical-device-startup/README.md) |
| Manufacturing | Small | Medical device manufacturer | [README](03_company-samples/manufacturing/size-3_small_medical-device-manufacturer/README.md) |
| Manufacturing | Mid-Market | Medical device manufacturer | [README](03_company-samples/manufacturing/size-4_mid-market_medical-device-manufacturer/README.md) |
| Manufacturing | Enterprise | Global medical device maker | [README](03_company-samples/manufacturing/size-5_enterprise_global-medical-device-maker/README.md) |
| Manufacturing | Multi-Sector | Diversified industrial group | [README](03_company-samples/manufacturing/size-6_multi-sector_diversified-industrial-group/README.md) |
| Chemical | Sole Proprietorship | Chemical distributor broker | [README](03_company-samples/manufacturing_chemical-critical-infrastructure/size-1_sole-proprietor_chemical-distributor-broker/README.md) |
| Chemical | Micro | Specialty chemical maker | [README](03_company-samples/manufacturing_chemical-critical-infrastructure/size-2_micro_specialty-chemical-maker/README.md) |
| Chemical | Small | Specialty chemical formulator | [README](03_company-samples/manufacturing_chemical-critical-infrastructure/size-3_small_specialty-chemical-formulator/README.md) |
| Chemical | Mid-Market | Specialty chemical maker | [README](03_company-samples/manufacturing_chemical-critical-infrastructure/size-4_mid-market_specialty-chemical-maker/README.md) |
| Chemical | Enterprise | Specialty chemical maker | [README](03_company-samples/manufacturing_chemical-critical-infrastructure/size-5_enterprise_specialty-chemical-maker/README.md) |
| Chemical | Multi-Sector | Specialty chemical maker plus two divisions | [README](03_company-samples/manufacturing_chemical-critical-infrastructure/size-6_multi-sector_specialty-chemical-maker-plus-two-divisions/README.md) |
| Critical Manufacturing | Sole Proprietorship | Industrial equipment repair technician | [README](03_company-samples/manufacturing_critical-manufacturing/size-1_sole-proprietor_industrial-equipment-repair-technician/README.md) |
| Critical Manufacturing | Micro | Transformer repair shop | [README](03_company-samples/manufacturing_critical-manufacturing/size-2_micro_transformer-repair-shop/README.md) |
| Critical Manufacturing | Small | Power transformer manufacturer | [README](03_company-samples/manufacturing_critical-manufacturing/size-3_small_power-transformer-manufacturer/README.md) |
| Critical Manufacturing | Mid-Market | Power transformer manufacturer | [README](03_company-samples/manufacturing_critical-manufacturing/size-4_mid-market_power-transformer-manufacturer/README.md) |
| Critical Manufacturing | Enterprise | Power transformer manufacturer | [README](03_company-samples/manufacturing_critical-manufacturing/size-5_enterprise_power-transformer-manufacturer/README.md) |
| Critical Manufacturing | Multi-Sector | Power transformer manufacturer plus two divisions | [README](03_company-samples/manufacturing_critical-manufacturing/size-6_multi-sector_power-transformer-manufacturer-plus-two-divisions/README.md) |
| Defense Industrial Base | Sole Proprietorship | Engineering subcontractor with CUI | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-1_sole-proprietor_engineering-subcontractor-with-cui/README.md) |
| Defense Industrial Base | Micro | Aircraft parts manufacturer | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-2_micro_aircraft-parts-manufacturer/README.md) |
| Defense Industrial Base | Small | Aircraft parts manufacturer | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-3_small_aircraft-parts-manufacturer/README.md) |
| Defense Industrial Base | Mid-Market | Aircraft parts manufacturer | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-4_mid-market_aircraft-parts-manufacturer/README.md) |
| Defense Industrial Base | Enterprise | Aircraft parts manufacturer | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-5_enterprise_aircraft-parts-manufacturer/README.md) |
| Defense Industrial Base | Multi-Sector | Aircraft parts manufacturer plus two divisions | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-6_multi-sector_aircraft-parts-manufacturer-plus-two-divisions/README.md) |
| Wholesale Trade | Sole Proprietorship | IT hardware reseller | [README](03_company-samples/wholesale-trade/size-1_sole-proprietor_it-hardware-reseller/README.md) |
| Wholesale Trade | Micro | IT hardware reseller | [README](03_company-samples/wholesale-trade/size-2_micro_it-hardware-reseller/README.md) |
| Wholesale Trade | Small | IT hardware distributor | [README](03_company-samples/wholesale-trade/size-3_small_it-hardware-distributor/README.md) |
| Wholesale Trade | Mid-Market | IT hardware distributor | [README](03_company-samples/wholesale-trade/size-4_mid-market_it-hardware-distributor/README.md) |
| Wholesale Trade | Enterprise | IT hardware distributor | [README](03_company-samples/wholesale-trade/size-5_enterprise_it-hardware-distributor/README.md) |
| Wholesale Trade | Multi-Sector | IT hardware distributor plus two divisions | [README](03_company-samples/wholesale-trade/size-6_multi-sector_it-hardware-distributor-plus-two-divisions/README.md) |
| Retail Trade | Sole Proprietorship | Corner grocery | [README](03_company-samples/retail-trade/size-1_sole-proprietor_corner-grocery/README.md) |
| Retail Trade | Micro | Grocery retailer | [README](03_company-samples/retail-trade/size-2_micro_grocery-retailer/README.md) |
| Retail Trade | Small | Independent grocery store | [README](03_company-samples/retail-trade/size-3_small_independent-grocery-store/README.md) |
| Retail Trade | Mid-Market | Grocery retailer | [README](03_company-samples/retail-trade/size-4_mid-market_grocery-retailer/README.md) |
| Retail Trade | Enterprise | Grocery retailer | [README](03_company-samples/retail-trade/size-5_enterprise_grocery-retailer/README.md) |
| Retail Trade | Multi-Sector | Grocery retailer plus two divisions | [README](03_company-samples/retail-trade/size-6_multi-sector_grocery-retailer-plus-two-divisions/README.md) |
| Transportation and Warehousing | Sole Proprietorship | Freight forwarder customs broker | [README](03_company-samples/transportation-warehousing/size-1_sole-proprietor_freight-forwarder-customs-broker/README.md) |
| Transportation and Warehousing | Micro | Freight forwarding office | [README](03_company-samples/transportation-warehousing/size-2_micro_freight-forwarding-office/README.md) |
| Transportation and Warehousing | Small | Marine cargo terminal | [README](03_company-samples/transportation-warehousing/size-3_small_marine-cargo-terminal/README.md) |
| Transportation and Warehousing | Mid-Market | Marine cargo terminal | [README](03_company-samples/transportation-warehousing/size-4_mid-market_marine-cargo-terminal/README.md) |
| Transportation and Warehousing | Enterprise | Marine cargo terminal | [README](03_company-samples/transportation-warehousing/size-5_enterprise_marine-cargo-terminal/README.md) |
| Transportation and Warehousing | Multi-Sector | Marine cargo terminal plus two divisions | [README](03_company-samples/transportation-warehousing/size-6_multi-sector_marine-cargo-terminal-plus-two-divisions/README.md) |
| Transportation Systems | Sole Proprietorship | Rail and truck freight broker | [README](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-1_sole-proprietor_rail-and-truck-freight-broker/README.md) |
| Transportation Systems | Micro | Freight railroad | [README](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-2_micro_freight-railroad/README.md) |
| Transportation Systems | Small | Short line railroad | [README](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-3_small_short-line-railroad/README.md) |
| Transportation Systems | Mid-Market | Freight railroad | [README](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-4_mid-market_freight-railroad/README.md) |
| Transportation Systems | Enterprise | Freight railroad | [README](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-5_enterprise_freight-railroad/README.md) |
| Transportation Systems | Multi-Sector | Freight railroad plus two divisions | [README](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-6_multi-sector_freight-railroad-plus-two-divisions/README.md) |
| Information | Sole Proprietorship | Independent SaaS developer | [README](03_company-samples/information-software-media/size-1_sole-proprietor_independent-saas-developer/README.md) |
| Information | Micro | B2B SaaS publisher | [README](03_company-samples/information-software-media/size-2_micro_b2b-saas-publisher/README.md) |
| Information | Small | Workforce scheduling SaaS | [README](03_company-samples/information-software-media/size-3_small_workforce-scheduling-saas/README.md) |
| Information | Mid-Market | B2B SaaS publisher | [README](03_company-samples/information-software-media/size-4_mid-market_b2b-saas-publisher/README.md) |
| Information | Enterprise | B2B SaaS publisher | [README](03_company-samples/information-software-media/size-5_enterprise_b2b-saas-publisher/README.md) |
| Information | Multi-Sector | B2B SaaS publisher plus two divisions | [README](03_company-samples/information-software-media/size-6_multi-sector_b2b-saas-publisher-plus-two-divisions/README.md) |
| Communications | Sole Proprietorship | Wireless internet provider | [README](03_company-samples/information-software-media_communications-critical-infrastructure/size-1_sole-proprietor_wireless-internet-provider/README.md) |
| Communications | Micro | Telecom carrier | [README](03_company-samples/information-software-media_communications-critical-infrastructure/size-2_micro_telecom-carrier/README.md) |
| Communications | Small | Regional telecom carrier | [README](03_company-samples/information-software-media_communications-critical-infrastructure/size-3_small_regional-telecom-carrier/README.md) |
| Communications | Mid-Market | Telecom carrier | [README](03_company-samples/information-software-media_communications-critical-infrastructure/size-4_mid-market_telecom-carrier/README.md) |
| Communications | Enterprise | Telecom carrier | [README](03_company-samples/information-software-media_communications-critical-infrastructure/size-5_enterprise_telecom-carrier/README.md) |
| Communications | Multi-Sector | Telecom carrier plus two divisions | [README](03_company-samples/information-software-media_communications-critical-infrastructure/size-6_multi-sector_telecom-carrier-plus-two-divisions/README.md) |
| Information Technology | Sole Proprietorship | Web hosting reseller | [README](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-1_sole-proprietor_web-hosting-reseller/README.md) |
| Information Technology | Micro | Cloud hosting provider | [README](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-2_micro_cloud-hosting-provider/README.md) |
| Information Technology | Small | Cloud hosting provider | [README](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-3_small_cloud-hosting-provider/README.md) |
| Information Technology | Mid-Market | Cloud hosting provider | [README](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-4_mid-market_cloud-hosting-provider/README.md) |
| Information Technology | Enterprise | Cloud hosting provider | [README](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-5_enterprise_cloud-hosting-provider/README.md) |
| Information Technology | Multi-Sector | Cloud hosting provider plus two divisions | [README](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-6_multi-sector_cloud-hosting-provider-plus-two-divisions/README.md) |
| Finance and Insurance | Sole Proprietorship | Registered investment adviser | [README](03_company-samples/finance-insurance/size-1_sole-proprietor_registered-investment-adviser/README.md) |
| Finance and Insurance | Micro | Community credit union | [README](03_company-samples/finance-insurance/size-2_micro_community-credit-union/README.md) |
| Finance and Insurance | Small | Community bank | [README](03_company-samples/finance-insurance/size-3_small_community-bank/README.md) |
| Finance and Insurance | Mid-Market | Regional bank | [README](03_company-samples/finance-insurance/size-4_mid-market_regional-bank/README.md) |
| Finance and Insurance | Enterprise | Super-regional bank | [README](03_company-samples/finance-insurance/size-5_enterprise_super-regional-bank/README.md) |
| Finance and Insurance | Multi-Sector | Diversified financial group | [README](03_company-samples/finance-insurance/size-6_multi-sector_diversified-financial-group/README.md) |
| Financial Services | Sole Proprietorship | Independent insurance agency | [README](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-1_sole-proprietor_independent-insurance-agency/README.md) |
| Financial Services | Micro | Merchant services provider | [README](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-2_micro_merchant-services-provider/README.md) |
| Financial Services | Small | Payment processor | [README](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-3_small_payment-processor/README.md) |
| Financial Services | Mid-Market | Payment processor | [README](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-4_mid-market_payment-processor/README.md) |
| Financial Services | Enterprise | Payment processor | [README](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-5_enterprise_payment-processor/README.md) |
| Financial Services | Multi-Sector | Payment processor plus two divisions | [README](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-6_multi-sector_payment-processor-plus-two-divisions/README.md) |
| Real Estate and Rental and Leasing | Sole Proprietorship | Real estate brokerage | [README](03_company-samples/real-estate/size-1_sole-proprietor_real-estate-brokerage/README.md) |
| Real Estate and Rental and Leasing | Micro | Real estate brokerage | [README](03_company-samples/real-estate/size-2_micro_real-estate-brokerage/README.md) |
| Real Estate and Rental and Leasing | Small | Residential real estate brokerage | [README](03_company-samples/real-estate/size-3_small_residential-real-estate-brokerage/README.md) |
| Real Estate and Rental and Leasing | Mid-Market | Real estate brokerage | [README](03_company-samples/real-estate/size-4_mid-market_real-estate-brokerage/README.md) |
| Real Estate and Rental and Leasing | Enterprise | Real estate brokerage | [README](03_company-samples/real-estate/size-5_enterprise_real-estate-brokerage/README.md) |
| Real Estate and Rental and Leasing | Multi-Sector | Real estate brokerage plus two divisions | [README](03_company-samples/real-estate/size-6_multi-sector_real-estate-brokerage-plus-two-divisions/README.md) |
| Commercial Facilities | Sole Proprietorship | Commercial property owner | [README](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-1_sole-proprietor_commercial-property-owner/README.md) |
| Commercial Facilities | Micro | Commercial property owner | [README](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-2_micro_commercial-property-owner/README.md) |
| Commercial Facilities | Small | Office retail property owner | [README](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-3_small_office-retail-property-owner/README.md) |
| Commercial Facilities | Mid-Market | Commercial property owner | [README](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-4_mid-market_commercial-property-owner/README.md) |
| Commercial Facilities | Enterprise | Commercial property owner | [README](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-5_enterprise_commercial-property-owner/README.md) |
| Commercial Facilities | Multi-Sector | Commercial property owner plus two divisions | [README](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-6_multi-sector_commercial-property-owner-plus-two-divisions/README.md) |
| Professional, Scientific, and Technical Services | Sole Proprietorship | CPA tax firm | [README](03_company-samples/professional-services/size-1_sole-proprietor_cpa-tax-firm/README.md) |
| Professional, Scientific, and Technical Services | Micro | CPA tax firm | [README](03_company-samples/professional-services/size-2_micro_cpa-tax-firm/README.md) |
| Professional, Scientific, and Technical Services | Small | CPA tax firm | [README](03_company-samples/professional-services/size-3_small_cpa-tax-firm/README.md) |
| Professional, Scientific, and Technical Services | Mid-Market | CPA tax firm | [README](03_company-samples/professional-services/size-4_mid-market_cpa-tax-firm/README.md) |
| Professional, Scientific, and Technical Services | Enterprise | CPA tax firm | [README](03_company-samples/professional-services/size-5_enterprise_cpa-tax-firm/README.md) |
| Professional, Scientific, and Technical Services | Multi-Sector | CPA tax firm plus two divisions | [README](03_company-samples/professional-services/size-6_multi-sector_cpa-tax-firm-plus-two-divisions/README.md) |
| Management of Companies and Enterprises | Sole Proprietorship | Owner of several small businesses | [README](03_company-samples/holding-companies/size-1_sole-proprietor_owner-of-several-small-businesses/README.md) |
| Management of Companies and Enterprises | Micro | Family holding office | [README](03_company-samples/holding-companies/size-2_micro_family-holding-office/README.md) |
| Management of Companies and Enterprises | Small | Holding company | [README](03_company-samples/holding-companies/size-3_small_holding-company/README.md) |
| Management of Companies and Enterprises | Mid-Market | Holding company | [README](03_company-samples/holding-companies/size-4_mid-market_holding-company/README.md) |
| Management of Companies and Enterprises | Enterprise | Holding company | [README](03_company-samples/holding-companies/size-5_enterprise_holding-company/README.md) |
| Management of Companies and Enterprises | Multi-Sector | Holding company plus two divisions | [README](03_company-samples/holding-companies/size-6_multi-sector_holding-company-plus-two-divisions/README.md) |
| Administrative and Support and Waste Management and Remediation Services | Sole Proprietorship | Independent recruiter | [README](03_company-samples/admin-support-services/size-1_sole-proprietor_independent-recruiter/README.md) |
| Administrative and Support and Waste Management and Remediation Services | Micro | Staffing firm | [README](03_company-samples/admin-support-services/size-2_micro_staffing-firm/README.md) |
| Administrative and Support and Waste Management and Remediation Services | Small | Staffing firm | [README](03_company-samples/admin-support-services/size-3_small_staffing-firm/README.md) |
| Administrative and Support and Waste Management and Remediation Services | Mid-Market | Staffing firm | [README](03_company-samples/admin-support-services/size-4_mid-market_staffing-firm/README.md) |
| Administrative and Support and Waste Management and Remediation Services | Enterprise | Staffing firm | [README](03_company-samples/admin-support-services/size-5_enterprise_staffing-firm/README.md) |
| Administrative and Support and Waste Management and Remediation Services | Multi-Sector | Staffing firm plus two divisions | [README](03_company-samples/admin-support-services/size-6_multi-sector_staffing-firm-plus-two-divisions/README.md) |
| Educational Services | Sole Proprietorship | Tutoring service | [README](03_company-samples/education/size-1_sole-proprietor_tutoring-service/README.md) |
| Educational Services | Micro | Tutoring company | [README](03_company-samples/education/size-2_micro_tutoring-company/README.md) |
| Educational Services | Small | Career college | [README](03_company-samples/education/size-3_small_career-college/README.md) |
| Educational Services | Mid-Market | Private college | [README](03_company-samples/education/size-4_mid-market_private-college/README.md) |
| Educational Services | Enterprise | Private college | [README](03_company-samples/education/size-5_enterprise_private-college/README.md) |
| Educational Services | Multi-Sector | Private college plus two divisions | [README](03_company-samples/education/size-6_multi-sector_private-college-plus-two-divisions/README.md) |
| Health Care and Social Assistance | Sole Proprietorship | Solo physician practice | [README](03_company-samples/health-care/size-1_sole-proprietor_solo-physician-practice/README.md) |
| Health Care and Social Assistance | Micro | Two-physician primary care office | [README](03_company-samples/health-care/size-2_micro_two-physician-primary-care-office/README.md) |
| Health Care and Social Assistance | Small | Multi-specialty practice | [README](03_company-samples/health-care/size-3_small_multi-specialty-practice/README.md) |
| Health Care and Social Assistance | Mid-Market | Physician group with surgery center | [README](03_company-samples/health-care/size-4_mid-market_physician-group-with-surgery-center/README.md) |
| Health Care and Social Assistance | Enterprise | Large medical group | [README](03_company-samples/health-care/size-5_enterprise_large-medical-group/README.md) |
| Health Care and Social Assistance | Multi-Sector | Care delivery health plan and SaaS | [README](03_company-samples/health-care/size-6_multi-sector_care-delivery-health-plan-and-saas/README.md) |
| Healthcare and Public Health | Sole Proprietorship | Independent pharmacy | [README](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-1_sole-proprietor_independent-pharmacy/README.md) |
| Healthcare and Public Health | Small | Critical access hospital | [README](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-3_small_critical-access-hospital/README.md) |
| Healthcare and Public Health | Mid-Market | Hospital | [README](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-4_mid-market_hospital/README.md) |
| Healthcare and Public Health | Enterprise | Hospital system | [README](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-5_enterprise_hospital-system/README.md) |
| Healthcare and Public Health | Multi-Sector | Hospital plus two divisions | [README](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-6_multi-sector_hospital-plus-two-divisions/README.md) |
| Arts, Entertainment, and Recreation | Sole Proprietorship | Independent event promoter | [README](03_company-samples/arts-entertainment-recreation/size-1_sole-proprietor_independent-event-promoter/README.md) |
| Arts, Entertainment, and Recreation | Micro | Live event venue | [README](03_company-samples/arts-entertainment-recreation/size-2_micro_live-event-venue/README.md) |
| Arts, Entertainment, and Recreation | Small | Live event venue | [README](03_company-samples/arts-entertainment-recreation/size-3_small_live-event-venue/README.md) |
| Arts, Entertainment, and Recreation | Mid-Market | Live event venue | [README](03_company-samples/arts-entertainment-recreation/size-4_mid-market_live-event-venue/README.md) |
| Arts, Entertainment, and Recreation | Enterprise | Live event venue | [README](03_company-samples/arts-entertainment-recreation/size-5_enterprise_live-event-venue/README.md) |
| Arts, Entertainment, and Recreation | Multi-Sector | Live event venue plus two divisions | [README](03_company-samples/arts-entertainment-recreation/size-6_multi-sector_live-event-venue-plus-two-divisions/README.md) |
| Accommodation and Food Services | Sole Proprietorship | Bed-and-breakfast inn | [README](03_company-samples/hotels-restaurants/size-1_sole-proprietor_bed-and-breakfast-inn/README.md) |
| Accommodation and Food Services | Micro | Small motel | [README](03_company-samples/hotels-restaurants/size-2_micro_small-motel/README.md) |
| Accommodation and Food Services | Small | Beachfront hotel | [README](03_company-samples/hotels-restaurants/size-3_small_beachfront-hotel/README.md) |
| Accommodation and Food Services | Mid-Market | Hotel operator | [README](03_company-samples/hotels-restaurants/size-4_mid-market_hotel-operator/README.md) |
| Accommodation and Food Services | Enterprise | Hotel operator | [README](03_company-samples/hotels-restaurants/size-5_enterprise_hotel-operator/README.md) |
| Accommodation and Food Services | Multi-Sector | Hotel operator plus two divisions | [README](03_company-samples/hotels-restaurants/size-6_multi-sector_hotel-operator-plus-two-divisions/README.md) |
| Other Services (except Public Administration) | Sole Proprietorship | Device repair service | [README](03_company-samples/repair-personal-services/size-1_sole-proprietor_device-repair-service/README.md) |
| Other Services (except Public Administration) | Micro | Device repair service | [README](03_company-samples/repair-personal-services/size-2_micro_device-repair-service/README.md) |
| Other Services (except Public Administration) | Small | Device repair shop | [README](03_company-samples/repair-personal-services/size-3_small_device-repair-shop/README.md) |
| Other Services (except Public Administration) | Mid-Market | Device repair service | [README](03_company-samples/repair-personal-services/size-4_mid-market_device-repair-service/README.md) |
| Other Services (except Public Administration) | Enterprise | Device repair service | [README](03_company-samples/repair-personal-services/size-5_enterprise_device-repair-service/README.md) |
| Other Services (except Public Administration) | Multi-Sector | Device repair service plus two divisions | [README](03_company-samples/repair-personal-services/size-6_multi-sector_device-repair-service-plus-two-divisions/README.md) |
| Public Administration | Sole Proprietorship | Independent GovTech consultant | [README](03_company-samples/public-administration/size-1_sole-proprietor_independent-govtech-consultant/README.md) |
| Public Administration | Micro | GovTech integrator | [README](03_company-samples/public-administration/size-2_micro_govtech-integrator/README.md) |
| Public Administration | Small | GovTech integrator | [README](03_company-samples/public-administration/size-3_small_govtech-integrator/README.md) |
| Public Administration | Mid-Market | GovTech integrator | [README](03_company-samples/public-administration/size-4_mid-market_govtech-integrator/README.md) |
| Public Administration | Enterprise | GovTech integrator | [README](03_company-samples/public-administration/size-5_enterprise_govtech-integrator/README.md) |
| Public Administration | Multi-Sector | GovTech integrator plus two divisions | [README](03_company-samples/public-administration/size-6_multi-sector_govtech-integrator-plus-two-divisions/README.md) |
| Government Services and Facilities | Sole Proprietorship | Facilities support contractor | [README](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-1_sole-proprietor_facilities-support-contractor/README.md) |
| Government Services and Facilities | Micro | Facilities support contractor | [README](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-2_micro_facilities-support-contractor/README.md) |
| Government Services and Facilities | Small | Government facilities contractor | [README](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-3_small_government-facilities-contractor/README.md) |
| Government Services and Facilities | Mid-Market | Facilities support contractor | [README](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-4_mid-market_facilities-support-contractor/README.md) |
| Government Services and Facilities | Enterprise | Facilities support contractor | [README](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-5_enterprise_facilities-support-contractor/README.md) |
| Government Services and Facilities | Multi-Sector | Facilities support contractor plus two divisions | [README](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-6_multi-sector_facilities-support-contractor-plus-two-divisions/README.md) |
| Emergency Services | Sole Proprietorship | Private security patrol | [README](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-1_sole-proprietor_private-security-patrol/README.md) |
| Emergency Services | Micro | Non-emergency ambulance service | [README](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-2_micro_non-emergency-ambulance-service/README.md) |
| Emergency Services | Small | Private ambulance service | [README](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-3_small_private-ambulance-service/README.md) |
| Emergency Services | Mid-Market | Ambulance service | [README](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-4_mid-market_ambulance-service/README.md) |
| Emergency Services | Enterprise | Ambulance service | [README](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-5_enterprise_ambulance-service/README.md) |
| Emergency Services | Multi-Sector | Ambulance service plus two divisions | [README](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-6_multi-sector_ambulance-service-plus-two-divisions/README.md) |
<!-- END GENERATED -->

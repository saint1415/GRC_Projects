# What has been accomplished

This page is the short answer to "what did you build?" It covers the whole library for the fictitious **Cris Santos Company**: the 10 projects from the [GRC Project List](https://nicoleenesse.notion.site/GRC-Project-List-3bf8eef497be8080afc3ee1cbd34bf68), applied across industries and company sizes.

## In one paragraph

One universal method for each of the 10 GRC projects was built once, then applied to one company shown in 36 industries and 6 sizes. Each finished sample company has all 10 deliverables, from business impact analysis to AI governance. It also has one facts file that every deliverable shares, so a reader can follow a risk from the risk register to the policy that answers it and the test that checks it. Every regulation is cited to its primary source, and every sample passes automated checks: risk scores recalculate from the NIST tables, and every control test statement matches NIST's official wording.

## Phases

| Phase | What it delivered | Status |
|---|---|---|
| 0. Foundation | Universal framework (NIST CSF 2.0, SP 800-53 Rev. 5, SP 800-53A), 6 company sizes, 36 industries, generator, validator, 216 sample folders | Done |
| 1. Flagship | Health Care, Small: a multi-specialty physician practice, all 10 projects | Done |
| 2. Size ladder | Health Care at all 6 sizes, from a solo physician to a multi-sector health group | Done |
| 3. Named industries | Small samples for Manufacturing, Defense, Wholesale, Retail, Transportation, SaaS, Finance, Education | Done |
| 4. Every industry | Small samples for the remaining 27 industries, so every sector has one finished company | Done |
| 5. Full matrix | The other sizes for each industry, in batches of 10 | In progress: batch 1 done (Manufacturing and Finance at all six sizes) |

Phase records, decisions, and corrections: [PLAN.md](PLAN.md).

## What the samples demonstrate

- **Scalability.** The same project at six sizes: a solo practitioner's one-page policy grows into a group-wide policy hierarchy with division supplements. See the [build guide](docs/how-to-build-the-10-projects.md), section 2.
- **A deliberate build order.** Projects are built in dependency order (business impact analysis first, AI governance last), so each one reuses the last. Folder names carry the step number.
- **Applicability before analysis.** Each gap analysis first asks whether the headline rule actually binds this company at this size. Examples: TSA pipeline and rail directives reach only designated operators, the NRC reactor cyber rule does not reach a waste processor, and FedRAMP does not apply without a federal customer. When the rule does not apply, the sample says so with the citation and uses the rule that does.
- **Official mappings where they exist.** The HIPAA gap analyses carry NIST's official HIPAA-to-SP 800-53 mapping (OLIR 110). Where a mapping is the author's own, it is labeled.
- **Verification discipline.** Regulatory facts were checked against eCFR, the Federal Register, and agency sites. Errors found along the way were corrected across all affected samples. One example: the scope of Florida's 15-day breach notice extension. Each correction is recorded in PLAN.md.

## Finished sample companies

<!-- BEGIN GENERATED: finished samples (tools/build_scenarios.py) -->
**207 of 216** sample companies are finished (2070 deliverables). Planned folders are listed in [03_company-samples/INDEX.md](03_company-samples/INDEX.md).

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
| Healthcare and Public Health | Micro | Independent pharmacy | [README](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-2_micro_independent-pharmacy/README.md) |
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
| Government Services and Facilities | Small | Government facilities contractor | [README](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-3_small_government-facilities-contractor/README.md) |
| Emergency Services | Small | Private ambulance service | [README](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-3_small_private-ambulance-service/README.md) |
<!-- END GENERATED -->

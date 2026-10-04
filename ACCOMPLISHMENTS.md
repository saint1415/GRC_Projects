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
**60 of 216** sample companies are finished (600 deliverables). Planned folders are listed in [03_company-samples/INDEX.md](03_company-samples/INDEX.md).

| Industry | Size | Company | Brief |
|---|---|---|---|
| Agriculture, Forestry, Fishing and Hunting | Small | Diversified crop farm | [README](03_company-samples/agriculture/size-3_small_diversified-crop-farm/README.md) |
| Food and Agriculture | Small | Meat processor | [README](03_company-samples/agriculture_food-agriculture-critical-infrastructure/size-3_small_meat-processor/README.md) |
| Mining, Quarrying, and Oil and Gas Extraction | Small | Crude oil producer | [README](03_company-samples/mining-oil-gas/size-3_small_crude-oil-producer/README.md) |
| Utilities | Small | Electric distribution utility | [README](03_company-samples/utilities/size-3_small_electric-distribution-utility/README.md) |
| Energy | Small | Gas transmission pipeline | [README](03_company-samples/utilities_energy-critical-infrastructure/size-3_small_gas-transmission-pipeline/README.md) |
| Dams | Small | Hydroelectric dam operator | [README](03_company-samples/utilities_dams-critical-infrastructure/size-3_small_hydroelectric-dam-operator/README.md) |
| Nuclear Reactors, Materials, and Waste | Small | Radioactive waste processor | [README](03_company-samples/utilities_nuclear-critical-infrastructure/size-3_small_radioactive-waste-processor/README.md) |
| Water and Wastewater Systems | Small | Community water system | [README](03_company-samples/utilities_water-critical-infrastructure/size-3_small_community-water-system/README.md) |
| Construction | Small | Commercial general contractor | [README](03_company-samples/construction/size-3_small_commercial-general-contractor/README.md) |
| Manufacturing | Sole Proprietorship | CNC machine shop | [README](03_company-samples/manufacturing/size-1_sole-proprietor_cnc-machine-shop/README.md) |
| Manufacturing | Micro | Medical device startup | [README](03_company-samples/manufacturing/size-2_micro_medical-device-startup/README.md) |
| Manufacturing | Small | Medical device manufacturer | [README](03_company-samples/manufacturing/size-3_small_medical-device-manufacturer/README.md) |
| Manufacturing | Mid-Market | Medical device manufacturer | [README](03_company-samples/manufacturing/size-4_mid-market_medical-device-manufacturer/README.md) |
| Manufacturing | Enterprise | Global medical device maker | [README](03_company-samples/manufacturing/size-5_enterprise_global-medical-device-maker/README.md) |
| Manufacturing | Multi-Sector | Diversified industrial group | [README](03_company-samples/manufacturing/size-6_multi-sector_diversified-industrial-group/README.md) |
| Chemical | Small | Specialty chemical formulator | [README](03_company-samples/manufacturing_chemical-critical-infrastructure/size-3_small_specialty-chemical-formulator/README.md) |
| Critical Manufacturing | Small | Power transformer manufacturer | [README](03_company-samples/manufacturing_critical-manufacturing/size-3_small_power-transformer-manufacturer/README.md) |
| Defense Industrial Base | Sole Proprietorship | Engineering subcontractor with CUI | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-1_sole-proprietor_engineering-subcontractor-with-cui/README.md) |
| Defense Industrial Base | Micro | Aircraft parts manufacturer | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-2_micro_aircraft-parts-manufacturer/README.md) |
| Defense Industrial Base | Small | Aircraft parts manufacturer | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-3_small_aircraft-parts-manufacturer/README.md) |
| Defense Industrial Base | Mid-Market | Aircraft parts manufacturer | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-4_mid-market_aircraft-parts-manufacturer/README.md) |
| Defense Industrial Base | Enterprise | Aircraft parts manufacturer | [README](03_company-samples/manufacturing_defense-industrial-base-critical-infrastructure/size-5_enterprise_aircraft-parts-manufacturer/README.md) |
| Wholesale Trade | Small | IT hardware distributor | [README](03_company-samples/wholesale-trade/size-3_small_it-hardware-distributor/README.md) |
| Retail Trade | Small | Independent grocery store | [README](03_company-samples/retail-trade/size-3_small_independent-grocery-store/README.md) |
| Transportation and Warehousing | Small | Marine cargo terminal | [README](03_company-samples/transportation-warehousing/size-3_small_marine-cargo-terminal/README.md) |
| Transportation Systems | Small | Short line railroad | [README](03_company-samples/transportation-warehousing_transportation-systems-critical-infrastructure/size-3_small_short-line-railroad/README.md) |
| Information | Sole Proprietorship | Independent SaaS developer | [README](03_company-samples/information-software-media/size-1_sole-proprietor_independent-saas-developer/README.md) |
| Information | Micro | B2B SaaS publisher | [README](03_company-samples/information-software-media/size-2_micro_b2b-saas-publisher/README.md) |
| Information | Small | Workforce scheduling SaaS | [README](03_company-samples/information-software-media/size-3_small_workforce-scheduling-saas/README.md) |
| Information | Mid-Market | B2B SaaS publisher | [README](03_company-samples/information-software-media/size-4_mid-market_b2b-saas-publisher/README.md) |
| Information | Enterprise | B2B SaaS publisher | [README](03_company-samples/information-software-media/size-5_enterprise_b2b-saas-publisher/README.md) |
| Information | Multi-Sector | B2B SaaS publisher plus two divisions | [README](03_company-samples/information-software-media/size-6_multi-sector_b2b-saas-publisher-plus-two-divisions/README.md) |
| Communications | Small | Regional telecom carrier | [README](03_company-samples/information-software-media_communications-critical-infrastructure/size-3_small_regional-telecom-carrier/README.md) |
| Information Technology | Small | Cloud hosting provider | [README](03_company-samples/information-software-media_information-technology-critical-infrastructure/size-3_small_cloud-hosting-provider/README.md) |
| Finance and Insurance | Sole Proprietorship | Registered investment adviser | [README](03_company-samples/finance-insurance/size-1_sole-proprietor_registered-investment-adviser/README.md) |
| Finance and Insurance | Micro | Community credit union | [README](03_company-samples/finance-insurance/size-2_micro_community-credit-union/README.md) |
| Finance and Insurance | Small | Community bank | [README](03_company-samples/finance-insurance/size-3_small_community-bank/README.md) |
| Finance and Insurance | Mid-Market | Regional bank | [README](03_company-samples/finance-insurance/size-4_mid-market_regional-bank/README.md) |
| Finance and Insurance | Enterprise | Super-regional bank | [README](03_company-samples/finance-insurance/size-5_enterprise_super-regional-bank/README.md) |
| Finance and Insurance | Multi-Sector | Diversified financial group | [README](03_company-samples/finance-insurance/size-6_multi-sector_diversified-financial-group/README.md) |
| Financial Services | Small | Payment processor | [README](03_company-samples/finance-insurance_financial-services-critical-infrastructure/size-3_small_payment-processor/README.md) |
| Real Estate and Rental and Leasing | Small | Residential real estate brokerage | [README](03_company-samples/real-estate/size-3_small_residential-real-estate-brokerage/README.md) |
| Commercial Facilities | Small | Office retail property owner | [README](03_company-samples/real-estate_commercial-facilities-critical-infrastructure/size-3_small_office-retail-property-owner/README.md) |
| Professional, Scientific, and Technical Services | Small | CPA tax firm | [README](03_company-samples/professional-services/size-3_small_cpa-tax-firm/README.md) |
| Management of Companies and Enterprises | Small | Holding company | [README](03_company-samples/holding-companies/size-3_small_holding-company/README.md) |
| Administrative and Support and Waste Management and Remediation Services | Small | Staffing firm | [README](03_company-samples/admin-support-services/size-3_small_staffing-firm/README.md) |
| Educational Services | Small | Career college | [README](03_company-samples/education/size-3_small_career-college/README.md) |
| Health Care and Social Assistance | Sole Proprietorship | Solo physician practice | [README](03_company-samples/health-care/size-1_sole-proprietor_solo-physician-practice/README.md) |
| Health Care and Social Assistance | Micro | Two-physician primary care office | [README](03_company-samples/health-care/size-2_micro_two-physician-primary-care-office/README.md) |
| Health Care and Social Assistance | Small | Multi-specialty practice | [README](03_company-samples/health-care/size-3_small_multi-specialty-practice/README.md) |
| Health Care and Social Assistance | Mid-Market | Physician group with surgery center | [README](03_company-samples/health-care/size-4_mid-market_physician-group-with-surgery-center/README.md) |
| Health Care and Social Assistance | Enterprise | Large medical group | [README](03_company-samples/health-care/size-5_enterprise_large-medical-group/README.md) |
| Health Care and Social Assistance | Multi-Sector | Care delivery health plan and SaaS | [README](03_company-samples/health-care/size-6_multi-sector_care-delivery-health-plan-and-saas/README.md) |
| Healthcare and Public Health | Small | Critical access hospital | [README](03_company-samples/health-care_healthcare-public-health-critical-infrastructure/size-3_small_critical-access-hospital/README.md) |
| Arts, Entertainment, and Recreation | Small | Live event venue | [README](03_company-samples/arts-entertainment-recreation/size-3_small_live-event-venue/README.md) |
| Accommodation and Food Services | Small | Beachfront hotel | [README](03_company-samples/hotels-restaurants/size-3_small_beachfront-hotel/README.md) |
| Other Services (except Public Administration) | Small | Device repair shop | [README](03_company-samples/repair-personal-services/size-3_small_device-repair-shop/README.md) |
| Public Administration | Small | GovTech integrator | [README](03_company-samples/public-administration/size-3_small_govtech-integrator/README.md) |
| Government Services and Facilities | Small | Government facilities contractor | [README](03_company-samples/public-administration_government-facilities-critical-infrastructure/size-3_small_government-facilities-contractor/README.md) |
| Emergency Services | Small | Private ambulance service | [README](03_company-samples/public-administration_emergency-services-critical-infrastructure/size-3_small_private-ambulance-service/README.md) |
<!-- END GENERATED -->

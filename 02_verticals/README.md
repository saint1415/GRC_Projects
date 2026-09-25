# 02_verticals: industry overlays

**Structure.** The 20 NAICS 2022 sectors are the parent verticals (macro). Each of the 16 CISA critical infrastructure sectors (NSM-22) is nested under the NAICS sector it primarily maps to (granular). Every entry from both lists appears exactly once: 36 verticals.

| File | Purpose | Edit? |
|---|---|---|
| [`verticals.csv`](verticals.csv) | Registry: hierarchy, primary NAICS industry, business, primary system, incident type, AI use case, multi-sector companions | Yes |
| [`scenario-industry-overrides.csv`](scenario-industry-overrides.csv) | Tier-specific industry substitutions where the primary industry is implausible at that size (for example, a sole proprietor cannot run a hospital) | Yes |
| [`sba-size-standards.csv`](sba-size-standards.csv) | SBA standards for every NAICS code used, pulled from eCFR | No, run `tools/refresh_sba_standards.py` |
| `<sector>/profile.csv` | Regulators, primary regulation for P03, sensitive data, critical systems, AI rules, assurance alternatives | Yes |
| `<sector>/requirements.csv` | Key regulations with citations, size thresholds, status, URL, and a `verified` flag | Yes |
| `<sector>/incident-notification.csv` | Mandatory incident and breach reporting: deadline, recipient, citation | Yes |
| `<sector>/overlay.md` | Readable summary | No, generated |

## Mapping CISA sectors to NAICS parents

Most CISA sectors span several NAICS sectors. The nesting uses the *primary* mapping for Cris Santos Company's chosen industry:

| NAICS parent | CISA children |
|---|---|
| 11 Agriculture | Food and Agriculture |
| 22 Utilities | Energy, Dams, Nuclear Reactors/Materials/Waste, Water and Wastewater Systems |
| 31-33 Manufacturing | Chemical, Critical Manufacturing, Defense Industrial Base |
| 48-49 Transportation and Warehousing | Transportation Systems |
| 51 Information | Communications, Information Technology |
| 52 Finance and Insurance | Financial Services |
| 53 Real Estate | Commercial Facilities |
| 62 Health Care and Social Assistance | Healthcare and Public Health |
| 92 Public Administration | Government Services and Facilities, Emergency Services |

**Public Administration (92):** governments are not businesses and have no SBA size standards. Cris Santos Company appears in this sector as a contractor to government (for example NAICS 541512 GovTech integrator, 561210 facilities support, 621910 ambulance services).

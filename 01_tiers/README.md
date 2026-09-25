# 01_tiers: company size tiers

Six parallel, independent size variants of Cris Santos Company. Each is a standalone scenario, not a growth story.

| Tier | Rule | Authority |
|---|---|---|
| Sole Proprietorship | Unincorporated, one owner, 0 paid employees | IRS (sole proprietor); Census Nonemployer Statistics (nonemployer) |
| Micro | 1-9 employees | Census SUSB employment size classes (<5, 5-9) |
| Small | 10+ employees and within the SBA size standard for its primary NAICS industry | SBA, 13 CFR 121.201 |
| Mid-Market | Above the SBA standard and under 1,000 employees | SBA (ceiling of Small); Census SUSB classes |
| Enterprise | 1,000+ employees, single sector | Census SUSB classes |
| Multi-Sector | Enterprise operating in 3 NAICS sectors | Census SUSB; NAICS 2022 |

**Why two sources?** SBA defines only "small" or "not small", one threshold per 6-digit NAICS industry (13 CFR 121.101 and 121.201). Census classes fill in the other tiers.

**Edge rule.** Some industries have an SBA standard of 900 or more employees, for example 1,500 for wired telecom. There, a company with under 1,000 employees is still SBA-small. The Mid-Market scenario is sized at 850 employees, flagged in its brief, and remains SBA-small.

## Files

- [`tiers.csv`](tiers.csv): definitions, legal form, ownership, IT footprint, and who owns GRC at each tier.
- [`tier-project-scaling.csv`](tier-project-scaling.csv): the 6 x 10 matrix of scope, depth, and deliverable form. This is the core of the scalability story.

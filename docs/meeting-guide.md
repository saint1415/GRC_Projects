# Meeting guide: presenting a Cris Santos Company sample

Each scenario folder is written so anyone in the room can follow it without GRC background.

## Before the meeting (10 minutes)

1. Choose the scenario closest to the audience's industry and size from [03_scenarios/INDEX.md](../03_scenarios/INDEX.md).
2. Open its `README.md`. This is the handout.
3. Pick one or two completed deliverables to walk through. The risk register (P01) and the BIA (P05) work well for mixed audiences.

## Suggested agenda (30 minutes)

| Minutes | Topic | Open |
|---|---|---|
| 0-5 | Who the company is: size, industry, systems, data | Scenario `README.md`, "At a glance" |
| 5-10 | Why these projects exist: regulators and requirements | "Who regulates it" |
| 10-25 | Walk through one deliverable | `Pxx_*/_context.md`, then the working file |
| 25-30 | How it scales: the same deliverable at a different size | The same project in another tier's folder |

## Talking points on scalability

- The **method never changes**. The 10 universal methods live in `00_universal/projects/`.
- **Size changes depth.** Compare the same project across tiers in `01_tiers/tier-project-scaling.csv`. For example, a sole proprietor keeps one consolidated policy, while an enterprise keeps a policy hierarchy.
- **Industry changes obligations.** Compare two verticals' `overlay.md` files.
- **Regulations change in one place.** Update the layer, rebuild, and every scenario reflects it.

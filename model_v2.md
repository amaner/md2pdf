# Bizztech Pricing Model

## Overview

This document outlines a proposed Bizztech pricing model that has two main components: environment implementation, and monthly pricing beyond implementation. 

Environment cost depends on whether the customer uses a custom environment we create, chooses from a pre-built library of environments, or brings their own environment. (We will also implement an SDK, allowing customers to user our toolset to create their own environments, but this is not yet implemented.) In addition, environment cost depends on complexity and feature set customization, as outlined below.

Beyond environment implementation, monthly costs will be driven based on the complexity of the chosen feature set, with all chosen features aggregated into a 'complexity score' that drives a logistic model.

### Environment Implementation

Base implementation fee:

$2850, regardless of environment size.

Four possible scenarios:

**1. We perform LIDAR scans and built 3DGS splat model of environment.**

This will be based on the size (in sq meters) of the environment, plus complexity.

Case 1: $0 m^2 \leq 10000 m^2$ - price is \$2850 + \$2.50 per $m^2$

Case 2: $10001 m^2 \leq 100000 m^2$ - price is \$2850 + \$2.00 per $m^2$

Case 3: $100001 m^2 \leq 250000 m^2$ - price is \$2850 + \$1.50 per $m^2$

Case 4: $250001 m^2 \leq 500000 m^2$ - price is \$2850 + \$1.00 per $m^2$

Case 5: $\geq 500001 m^2$ - price is \$2850 + \$0.75 per $m^2$

Example: A user purchases a 100,000 sq meter environment. The base price would be $\$2850 + 100,000 \times 2.00 = \$202850$.

**2. Customer provides their own, pre-built environment.**

In this case, the customer brings a pre-built environment. There is a flat implementation fee.

Base implementation fee: $\$25000$.

**3. Customer chooses from a library of Bizztech pre-built environments.**

In this case, the customer purchases a pre-built environment from our library. There is a flat implementation fee, as above.

Base implementation fee: $\$25000$.

**4. Customer uses our SDK to built their own environment.**

Note: This feature is not yet implemented.

#### Additional Modules

In addition to environment implementation and customization, we offer a number of additional modules / layers that carry up-front implementation fees. These are:

**1. HAL AI Agent Integration**

This can take one of five tiers, priced as follows:

Tier 1: Basic functionality - $\$30000$

Tier 2: Improved functionality - $\$60000$

Tier 3: Medium functionality - $\$90000$

Tier 4: Advanced functionality - $\$120000$

Tier 5: Full functionality + R&D - $\$150000$

**2. IoT Device Integration and Orchestration**

This can take one of five tiers, priced as follows:

Tier 1: Basic integration - $\$10000$

Tier 2: Improved integration - $\$32500$

Tier 3: Medium integration - $\$55000$

Tier 4: Advanced integration - $\$77500$

Tier 5: Full integration - $\$100000$

**3. Security and Compliance Layer**

This carries a flat fee of $\$20000$ plus $5\%$ of the environment implementation fee.

**4. Training and Support**

This can take one of five tiers, priced as follows:

Tier 1: Basic tier - $\$10000$

Tier 2: Improved tier - $\$20000$

Tier 3: Medium tier - $\$30000$

Tier 4: Advanced tier - $\$40000$

Tier 5: Full tier - $\$50000$

**5. Digital Twin Creation**

This will depend on the complexity of 3D modeling, amount of simulation setup involved, and the number of sensors to be integrated. It can take one of five tiers, priced as follows:

Tier 1: Basic tier - $\$50000$

Tier 2: Improved tier - $\$87500$

Tier 3: Medium tier - $\$125000$

Tier 4: Advanced tier - $\$162500$

Tier 5: Full tier - $\$200000$

#### Value-Based Add-ons

These are additional services that are not included in the base implementation fee, but are available for purchase. These are:

**1. Performance Guarantee Fee**

$+ 10 - 20\%$ of the environment implementation fee, as bonus, based on measured KPIs after deployment (e.g, energy savings, cost reductions, etc.). This cannot be modeled in advance and will have to be negotiated during contract discussions.

**2. Scalability Package**

Pricing for future scale-up or additional sites offered at $80\%$ of initial per-unit cost. This cannot be modeled in advance and will have to be negotiated during contract discussions.

#### Customizations 

This is a three-tiered multiplier that accounts for the complexity of customization done to the environment and add-ons. 

Tier 1: Standard (pre-configured solutions, minimal changes) - multiplier of $1x$

Tier 2: Advanced (Moderate custom features and integrations) - multiplier of $1.5x$

Tier 3: Bespoke (Extensive customization, significant R&D) - multiplier of $2x$

Example: Customer purchases a custom environment that is $200000 m^2$ in extent. They also choose to add the following features: Tier 2 HAL integration, Tier 2 IoT integration, Tier 1 training, and Tier 1 digital twin modeling. Their integration requires a moderate amount of additional customization. This results in an environment price of:

$\$2850 + 200000 \times 1.5 + \$60000 + \$32500 + \$10000 + \$50000 = \$455350 \times 1.5 = \$683025$

### Monthly Pricing

This category is to cover ongoing maintenance and operation of the environment, and is based on the complexity of the feature set. The logic is based on a complexity score, which drives the width and steepness of a logistic curve. Our assumptions are that the model should result in the following monthly prices:

#### Assumptions

##### Entry-Level (Municipalities / Schools / SMEs)

$\$5000 - \$10000$ per month for limited metaverse and digital twin maintenance.

##### Mid-Tier (Smart Campus / Medium Cities)

$\$10000 - \$25000$ per month for standard metaverse and digital twin maintenance, with IoT integration maintenance (swapping in/out devices, tuning data feeds, etc.).

##### Enterprise (Large Cities / Universities / Utility Companies)

$\$30000 - \$75000$ per month for large-scale digital twin / metaverse maintenance, AI-driven decision making and control features, large IoT integrations, etc.

##### Edge Cases

Current assumptions are that the min monthly price is set to $\$1000$ and the max is $\$100000$. These are (sort of) arbitrary bounds that can be adjusted as needed.

#### Core Concept

1. **Feature Complexity Score**
   Assign each optional feature a “weight” (complexity points). Social features are weight 0 since they’re included in the base platform.

2. **User-Load Factor**
   Convert concurrent-user count into a scaling multiplier (e.g. via a logarithm or sigmoid) so that adding users has diminishing returns on price beyond a certain scale.

3. **Combined Complexity**
   Multiply the raw feature score by the user-load factor to get a single “effective complexity” input to the logistic.

4. **Logistic Curve**
   Use

   $$
     \text{price} = \text{MIN\_PRICE} + \frac{\text{MAX\_PRICE} - \text{MIN\_PRICE}}{1 + e^{-k\,(C - x_0)}}
   $$

   where:

   * $C$ = combined complexity
   * $k$ = steepness (higher → sharper transition)
   * $x_0$ = midpoint (where price is halfway between min and max)

---

#### Pseudo-Code

```python
import math

# ──────────── Configurable Bounds ────────────
MIN_PRICE = 1_000     # minimum monthly price
MAX_PRICE = 100_000   # maximum monthly price

# ──────────── Feature Weights ────────────
FEATURE_WEIGHTS = {
    "social_features":           0,  # included in base
    "urban_planning":            2,
    "simulation":                3,
    "environment_customization": 2,
    "digital_twin":              3,
    "data_visualization":        3,
    "AI_NPCs":                   4,
    "training_scenarios":        3,
    "HAL_AI_agent":              5
}

# ──────────── Logistic Parameters ────────────
k  = 0.4    # controls steepness of price ramp
x0 = 12.0   # complexity midpoint for half-max pricing

# ──────────── Helper Functions ────────────

def compute_feature_score(selected_features: list[str]) -> float:
    """
    Sum the weights of all selected features.
    """
    return sum(FEATURE_WEIGHTS.get(f, 0) for f in selected_features)

def compute_user_factor(concurrent_users: int) -> float:
    """
    Convert user count into a multiplicative factor.
    E.g. a log1p to give diminishing returns:
      0 users → 0
      ~100 users → ~1
      ~1000 users → ~2.3
    """
    return math.log1p(concurrent_users / 100)

def compute_combined_complexity(feature_score: float, user_factor: float) -> float:
    """
    Combine feature complexity with user-load factor.
    """
    return feature_score * (1 + user_factor)

def logistic_priced(complexity: float) -> float:
    """
    Apply the logistic formula to map complexity → [MIN_PRICE, MAX_PRICE].
    """
    price_range = MAX_PRICE - MIN_PRICE
    exponent   = -k * (complexity - x0)
    fraction   = 1 / (1 + math.exp(exponent))
    return round(MIN_PRICE + price_range * fraction, 2)

# ──────────── Main API ────────────

def estimate_monthly_price(
    selected_features: list[str],
    concurrent_users:    int
) -> float:
    # 1. raw feature score
    feat_score = compute_feature_score(selected_features)
    # 2. user-load factor
    usr_factor = compute_user_factor(concurrent_users)
    # 3. combined complexity
    combo      = compute_combined_complexity(feat_score, usr_factor)
    # 4. logistic pricing
    return logistic_priced(combo)

# ──────────── Example Scenarios ────────────
if __name__ == "__main__":
    # 1) Entry-level: basic DT + <100 users
    entry_price = estimate_monthly_price(
        ["social_features","digital_twin"], concurrent_users=75
    )
    print("Entry-level price:", entry_price)  # expect ~$5k–10k

    # 2) Intermediate: +simulation, training + ~300 users
    mid_price = estimate_monthly_price(
        ["social_features","digital_twin","simulation","training_scenarios"],
        concurrent_users=300
    )
    print("Intermediate price:", mid_price)  # expect ~$10k–25k

    # 3) Enterprise: all features + 1000+ users
    enterprise_price = estimate_monthly_price(
        list(FEATURE_WEIGHTS.keys()),
        concurrent_users=1500
    )
    print("Enterprise price:", enterprise_price)  # expect ~$30k–75k
```

---

## 3. Tuning & Next Steps

* **Adjust `k` and `x0`** to pull your model’s outputs into the exact numeric bands you’ve observed historically.
* **Re-assign feature weights** if some modules (e.g. HAL) should drive price more aggressively.
* **Validate** against real contract prices, then refine.
* **Wrap** in a micro-service or spreadsheet for your sales team.

## Summary

This pricing model provides Bizztech with a flexible and scalable approach to monetizing our metaverse platform. By separating implementation costs from monthly operational fees, we create a clear value proposition for clients across different market segments. The implementation pricing accounts for environment size, customization complexity, and additional module integration, while the monthly pricing uses a logistic model based on feature complexity and user load.

This dual approach allows us to:
1. Capture upfront value for our implementation expertise and customization work
2. Establish predictable recurring revenue based on actual platform usage and complexity
3. Scale appropriately from entry-level municipal clients to enterprise-grade implementations
4. Provide clear pricing guidance to our sales team while maintaining flexibility for negotiation

As we gather more market feedback, we should continuously refine the feature weights, logistic parameters, and pricing tiers to optimize both customer acquisition and revenue generation. The model is designed to be easily adjustable as we learn more about customer preferences and usage patterns.
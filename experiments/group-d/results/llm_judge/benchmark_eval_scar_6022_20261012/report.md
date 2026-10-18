# Benchmark Evaluation Report

> Derived from canonical Evaluation artifacts. This report does not execute LLM requests.

## Executive Summary

| Metric | Value |
| --- | --- |
| Report version | 0.2 |
| Benchmark version | v1 |
| Repositories | 23 |
| Ground Truth findings | 25 |
| Predictions | 38 |
| Total matched weight | 6.6500 |
| Pooled soft precision | 0.1750 |
| Pooled soft recall | 0.2660 |
| Macro soft F1 | 0.1574 |
| Pooled soft F1 | 0.2111 |

## Evaluation Configuration

| Field | Value |
| --- | --- |
| Matching strategy | greedy |
| Threshold | 0.5000 |
| Weight profile | end-to-end-v2 |
| Judge model | gpt-5.6-luna |
| Judge prompt version | benchmark-judge-v3 |
| Detector version | hound-direct-prediction-case-v1 |
| Detector model | openai-codex/gpt-5.6-luna |
| Manifest SHA-256 | 959fffa1be2cdccbaec082d5a1b808917df8c977fb35f99c11928adf38dabf9f |

## Repository Summary

| Repository | Ground Truth | Predictions | Matched weight | Precision | Recall | Soft F1 |
| --- | --- | --- | --- | --- | --- | --- |
| `2021-04-marginswap` | 1 | 2 | 1.0000 | 0.5000 | 1.0000 | 0.6667 |
| `2021-07-spartan` | 2 | 3 | 1.0000 | 0.3333 | 0.5000 | 0.4000 |
| `2021-08-notional` | 1 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2021-11-malt` | 1 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2021-12-vader` | 1 | 2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-01-behodler` | 1 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-01-sandclock` | 1 | 2 | 1.0000 | 0.5000 | 1.0000 | 0.6667 |
| `2022-08-sentiment` | 1 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-09-notional` | 1 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-11-paraspace` | 1 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-11-telcoin` | 1 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2023-03-olympus` | 1 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2023-04-blueberry` | 1 | 5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2023-05-ussd` | 2 | 7 | 1.0000 | 0.1429 | 0.5000 | 0.2222 |
| `2023-06-lybra` | 1 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2023-06-real-wagmi` | 1 | 3 | 0.9500 | 0.3167 | 0.9500 | 0.4750 |
| `2023-06-tokemak` | 1 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2023-08-dopex` | 1 | 2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2024-03-abracadabra-money` | 1 | 4 | 0.8500 | 0.2125 | 0.8500 | 0.3400 |
| `2024-03-revert-lend` | 1 | 1 | 0.8500 | 0.8500 | 0.8500 | 0.8500 |
| `2024-03-woofi-swap` | 1 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2024-04-panoptic` | 1 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2025-12-panoptic` | 1 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

## Repository Details

### `2021-04-marginswap`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 2 |
| Matched weight | 1.0000 |
| Soft precision | 0.5000 |
| Soft recall | 1.0000 |
| Soft F1 | 0.6667 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| H-03 — [H-03] Price feed can be manipulated | hyp_0bb6b48214f2 — Cross-margin liquidation valuation uses manipulable Uniswap spot reserves instead of the cached EMA | 4/4 | 4/4 | 4/4 | 4/4 | 1.0000 |

<details>
<summary>Pair 1: H-03 — [H-03] Price feed can be manipulated ↔ hyp_0bb6b48214f2 — Cross-margin liquidation valuation uses manipulable Uniswap spot reserves instead of the cached EMA</summary>

- **Ground Truth:** `H-03`
- **Prediction:** `hyp_0bb6b48214f2`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| contracts/PriceAware.sol | PriceAware | getCurrentPriceInPeg(address,uint256,bool) | 60–87 |
| contracts/PriceAware.sol | PriceAware | getPriceFromAMM(address,uint256) | 111–137 |

#### Prediction locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| contracts/CrossMarginLiquidation.sol | CrossMarginLiquidation | liquidate(address[] memory) | — |
| contracts/CrossMarginAccounts.sol | CrossMarginAccounts | holdingsInPeg(CrossMarginAccount storage,bool) | — |
| contracts/CrossMarginAccounts.sol | CrossMarginAccounts | loanInPeg(CrossMarginAccount storage,bool) | — |
| contracts/PriceAware.sol | PriceAware | getCurrentPriceInPeg(address,uint256,bool) | — |
| contracts/PriceAware.sol | PriceAware | viewCurrentPriceInPeg(address,uint256) | — |
| contracts/PriceAware.sol | PriceAware | getPriceFromAMM(address,uint256) | — |

#### Judge rationale

```text
R: Correctly identifies that forceCurBlock causes the protocol to use manipulable current AMM reserves instead of a protected/cached price, enabling flash-loan reserve distortion. L: Correctly localizes the relevant PriceAware functions, including getCurrentPriceInPeg and getPriceFromAMM, and appropriately identifies their liquidation call path. I: Correctly describes attacker-controlled valuation affecting collateralization and liquidation outcomes, including incorrect debt/collateral values and shortfalls. M: Recommends preventing the current-spot bypass and using a manipulation-resistant cached/TWAP oracle, which directly fixes the underlying flaw.
```

</details>

#### Unmatched Ground Truth

No unmatched Ground Truth findings.

#### Unmatched Predictions

- hyp_6de4941c9937 — Liquidation swaps execute against manipulable AMM reserves with no slippage bound

### `2021-07-spartan`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 2 |
| Predictions | 3 |
| Matched weight | 1.0000 |
| Soft precision | 0.3333 |
| Soft recall | 0.5000 |
| Soft F1 | 0.4000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| H-06 — [H-06] SynthVault rewards can be gamed | hyp_625c83f3afc1 — Manipulable pool spot price overweights SynthVault deposits and rewards | 4/4 | 4/4 | 4/4 | 4/4 | 1.0000 |

<details>
<summary>Pair 1: H-06 — [H-06] SynthVault rewards can be gamed ↔ hyp_625c83f3afc1 — Manipulable pool spot price overweights SynthVault deposits and rewards</summary>

- **Ground Truth:** `H-06`
- **Prediction:** `hyp_625c83f3afc1`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| contracts/synthVault.sol | SynthVault | _deposit(address,address,uint256) | 102–116 |
| contracts/Utils.sol | Utils | calcSpotValueInBase(address,uint256) | 160–163 |
| contracts/Utils.sol | Utils | calcSpotValueInBaseWithPool(address,uint256) | 186–190 |

#### Prediction locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| contracts/Utils.sol | Utils | calcSpotValueInBase(address,uint256) | — |
| contracts/Utils.sol | Utils | calcSpotValueInBaseWithPool(address,uint256) | — |
| contracts/SynthVault.sol | SynthVault | _deposit | — |
| contracts/SynthVault.sol | SynthVault | harvestSingle | — |
| contracts/SynthVault.sol | SynthVault | calcReward | — |

#### Judge rationale

```text
R: Correctly identifies the instantaneous AMM reserve-ratio valuation used to record an inflated SynthVault weight and its persistence after price restoration. L: Correctly localizes calcSpotValueInBase, calcSpotValueInBaseWithPool, and SynthVault._deposit; the additional reward functions are relevant. I: Correctly describes disproportionate claims on reserve-funded rewards and dilution of legitimate depositors. M: TWAP/manipulation-resistant valuation and deferred accounting would prevent the spot-price weighting flaw; the added checks and caps are also sound defense-in-depth.
```

</details>

#### Unmatched Ground Truth

- H-05 — [H-05] Synth realise is vulnerable to flash loan attacks

#### Unmatched Predictions

- hyp_b1ce20b5118f — Spot-price manipulation can amplify reserve-funded curated-pool dividends
- hyp_d6c44ada714c — Router swaps and synth issuance lack user price protection against sandwich manipulation

### `2021-08-notional`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 1 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-10 — [H-10] Liquidity token value can be manipulated

#### Unmatched Predictions

- hyp_edcfd0350bd4 — Stale oracle prices can be used to manipulate collateral valuation and liquidation outcomes

### `2021-11-malt`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 1 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- M-22 — [M-22] `_calculateMaltRequiredForExit` Uses Spot Price To Calculate Malt Quantity In `exitEarly`

#### Unmatched Predictions

- hyp_36d029b59fa9 — Reward reinvestment is vulnerable to spot-price sandwich manipulation

### `2021-12-vader`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 2 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-06 — [H-06] LPs of VaderPoolV2 can manipulate pool reserves to extract funds from the reserve.

#### Unmatched Predictions

- hyp_455f5a009f03 — Legacy router ignores minimum amounts, enabling reserve-price sandwich attacks on liquidity additions
- hyp_9fce3c2a5cfb — Direct VADER donations manipulate XVader share price and enable victim deposit extraction

### `2022-01-behodler`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 1 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-05 — [H-05] Flash loan price manipulation in purchasePyroFlan()

#### Unmatched Predictions

- hyp_81d0059d67b9 — Spot-price sandwich attack against Limbo secondary-reward liquidation

### `2022-01-sandclock`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 2 |
| Matched weight | 1.0000 |
| Soft precision | 0.5000 |
| Soft recall | 1.0000 |
| Soft F1 | 0.6667 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| H-03 — [H-03] Vaults with non-UST underlying asset vulnerable to flash loan attack on curve pool | hyp_d92c00067e19 — Manipulable Curve spot quote directly controls NonUST share pricing | 4/4 | 4/4 | 4/4 | 4/4 | 1.0000 |

<details>
<summary>Pair 1: H-03 — [H-03] Vaults with non-UST underlying asset vulnerable to flash loan attack on curve pool ↔ hyp_d92c00067e19 — Manipulable Curve spot quote directly controls NonUST share pricing</summary>

- **Ground Truth:** `H-03`
- **Prediction:** `hyp_d92c00067e19`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| sandclock/contracts/strategy/NonUSTStrategy.sol | NonUSTStrategy | investedAssets() | 120–136 |

#### Prediction locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| sandclock/contracts/strategy/NonUSTStrategy.sol | NonUSTStrategy | investedAssets() | — |
| sandclock/contracts/Vault.sol | Vault | _createClaim() | — |
| sandclock/contracts/Vault.sol | Vault | _withdrawDeposit() | — |

#### Judge rationale

```text
R: Correctly identifies the root cause: Curve's manipulable transaction-local spot quote is used to value UST exposure and determine share pricing. L: Correctly localizes the issue to NonUSTStrategy.investedAssets(), and appropriately traces its use in vault deposit and withdrawal paths. I: Correctly describes excess share issuance or withdrawals that drain value from existing depositors. M: Manipulation-resistant oracle/TWAP valuation with bounds and deviation checks would prevent the ground-truth attack.
```

</details>

#### Unmatched Ground Truth

No unmatched Ground Truth findings.

#### Unmatched Predictions

- hyp_32aa5d901159 — Zero-output protection allows Curve price manipulation to steal strategy assets during swaps

### `2022-08-sentiment`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 1 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- M-10 — M-10: ERC4626Oracle Vulnerable To Price Manipulation

#### Unmatched Predictions

- hyp_ae111fb88a45 — Stale Chainlink rounds can remain trusted for collateral valuation

### `2022-09-notional`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 0 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- M-7 — [M-7] Gain From Balancer Vaults Can Be Stolen

#### Unmatched Predictions

No unmatched predictions.

### `2022-11-paraspace`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 0 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-05 — [H-05] Attacker can manipulate low TVL Uniswap V3 pool to borrow and swap to make Lending Pool in loss

#### Unmatched Predictions

No unmatched predictions.

### `2022-11-telcoin`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 1 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-1 — H-1: Flashloan `TEL` tokens to stake and exit in the same block can fake a huge amount of stake with minimal material cost

#### Unmatched Predictions

- hyp_328ae686dd0d — FeeBuyback swap is exposed to sandwich and price manipulation due to missing slippage enforcement

### `2023-03-olympus`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 0 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-1 — H-1: Adversary can sandwich oracle updates to exploit vault

#### Unmatched Predictions

No unmatched predictions.

### `2023-04-blueberry`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 5 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-4 — H-4: Potential flash loan attack vulnerability in `getPrice` function of CurveOracle

#### Unmatched Predictions

- hyp_4583e7e9e72d — Zero-slippage reward liquidation enables sandwich-based price manipulation
- hyp_c2e5eed50619 — PSwapLib forwards caller-controlled Paraswap slippage without oracle or minimum-output enforcement
- hyp_56d6074f3242 — AggregatorOracle can return flash-loan-manipulated Uniswap V2 spot prices
- hyp_90e07533de7c — SoftVault Compound exchange-rate inflation can overvalue collateral
- hyp_4c195cad1a8b — Aura reward liquidation may use manipulable Uniswap spot pricing without an effective minimum-output bound

### `2023-05-ussd`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 2 |
| Predictions | 7 |
| Matched weight | 1.0000 |
| Soft precision | 0.1429 |
| Soft recall | 0.5000 |
| Soft F1 | 0.2222 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| H-5 — H-5: Price calculation susceptible to flashloan exploits | hyp_5d621db93995 — Flash-loan manipulation of Uniswap spot price controls rebalancing trades | 4/4 | 4/4 | 4/4 | 4/4 | 1.0000 |

<details>
<summary>Pair 1: H-5 — H-5: Price calculation susceptible to flashloan exploits ↔ hyp_5d621db93995 — Flash-loan manipulation of Uniswap spot price controls rebalancing trades</summary>

- **Ground Truth:** `H-5`
- **Prediction:** `hyp_5d621db93995`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | getOwnValuation() | 71–80 |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | rebalance() | 92–107 |

#### Prediction locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | getOwnValuation | — |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | rebalance | — |
| ussd-contracts/contracts/USSD.sol | USSD | UniV3SwapInput | — |

#### Judge rationale

```text
R: Correctly identifies the core flaw: rebalance relies on manipulable instantaneous Uniswap V3 spot price from slot0 rather than a TWAP. L: Correctly localizes getOwnValuation() and rebalance(), with the downstream swap path also relevant. I: Correctly describes attacker-controlled temporary pricing that can cause protocol trades and losses. M: TWAP or an independent protected oracle, deviation bounds, and slippage protections would prevent the ground-truth exploit.
```

</details>

#### Unmatched Ground Truth

- H-9 — H-9: Uniswap v3 pool token balance proportion does not necessarily correspond to the price, and it is easy to manipulate.

#### Unmatched Predictions

- hyp_dc4ddb33f489 — Public SimOracle setter permits arbitrary collateral price manipulation
- hyp_3fe23d59f480 — WBTC oracle uses the WETH/USD Chainlink feed
- hyp_a75fac599eda — Single-pool 10-minute TWAP remains manipulable for collateral valuation
- hyp_ddcf5ddb4737 — Stale WETH/USD Chainlink answers can overvalue collateral during feed outages
- hyp_cac569cc7d1d — Negative Chainlink answer is cast into an enormous positive collateral price
- hyp_6b6b9adff754 — Stale WBTC Chainlink answer accepted without freshness validation

### `2023-06-lybra`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 1 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- M-13 — [M-13] It is possible to manipulate WETH/LBR pair to claim reward of the users which shouldn't be claimed

#### Unmatched Predictions

- hyp_20e19434ee95 — Unvalidated LBR Oracle Enables Underpriced EUSD Buyouts

### `2023-06-real-wagmi`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 3 |
| Matched weight | 0.9500 |
| Soft precision | 0.3167 |
| Soft recall | 0.9500 |
| Soft F1 | 0.4750 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| H-3 — H-3: Usage of `slot0` is extremely easy to manipulate | hyp_7cdc2a0d08ac — Public Multipool deposits can mint shares against a transiently manipulated Uniswap V3 price | 4/4 | 3/4 | 4/4 | 4/4 | 0.9500 |

<details>
<summary>Pair 1: H-3 — H-3: Usage of \`slot0\` is extremely easy to manipulate ↔ hyp_7cdc2a0d08ac — Public Multipool deposits can mint shares against a transiently manipulated Uniswap V3 price</summary>

- **Ground Truth:** `H-3`
- **Prediction:** `hyp_7cdc2a0d08ac`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| concentrator/contracts/Multipool.sol | Multipool | deposit(uint256,uint256,uint256,uint256) | 433–486 |
| concentrator/contracts/Multipool.sol | Multipool | getSlots() | 589–602 |
| concentrator/contracts/Multipool.sol | Multipool | _getReserves(Slot0Data[]) | 693–768 |

#### Prediction locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| concentrator/contracts/Multipool.sol | Multipool | deposit(uint256,uint256) | — |
| concentrator/contracts/Multipool.sol | Multipool | _deposit(uint256,uint256,uint256,Slot0Data[] memory) | — |
| concentrator/contracts/Multipool.sol | Multipool | getSlots() | — |

#### Judge rationale

```text
R: Correctly identifies current slot0-derived pricing feeding deposit valuation and LP-share minting, with transient price distortion as the root cause. L: Correctly localizes the Multipool deposit/_deposit and getSlots path, though it omits the explicit _getReserves operation and uses a less specific deposit signature. I: Matches the impact of incorrect or over-credited LP shares, extraction of reserves, and dilution of existing LPs. M: Replacing spot pricing with TWAP/oracle validation, enforcing deviation bounds, and adding user slippage limits would prevent the vulnerable share calculation.
```

</details>

#### Unmatched Ground Truth

No unmatched Ground Truth findings.

#### Unmatched Predictions

- hyp_4087d2a678bc — Spot-price manipulation can force rebalance liquidity into attacker-selected Uniswap V3 ranges
- hyp_0934f42ea744 — Dispatcher reserve-based share pricing can be manipulated during deposits and withdrawals

### `2023-06-tokemak`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 0 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-15 — H-15: Maverick oracle can be manipulated

#### Unmatched Predictions

No unmatched predictions.

### `2023-08-dopex`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 2 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- M-08 — [M-08] `reLPContract.reLP()` is susceptible to sandwich attack due to user control over `bond()`

#### Unmatched Predictions

- hyp_d816c1b6feb9 — UniV3 AMO swaps rely on manipulable pool spot price and caller-supplied slippage
- hyp_b961004d796b — UniV2 AMO swaps can execute against attacker-manipulated pair spot prices

### `2024-03-abracadabra-money`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 4 |
| Matched weight | 0.8500 |
| Soft precision | 0.2125 |
| Soft recall | 0.8500 |
| Soft F1 | 0.3400 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| H-04 — [H-04] Oracle price can be manipulated | hyp_38e58ce51876 — Spot-reserve MagicLP aggregator price can be manipulated before Cauldron valuation | 4/4 | 2/4 | 4/4 | 3/4 | 0.8500 |

<details>
<summary>Pair 1: H-04 — [H-04] Oracle price can be manipulated ↔ hyp_38e58ce51876 — Spot-reserve MagicLP aggregator price can be manipulated before Cauldron valuation</summary>

- **Ground Truth:** `H-04`
- **Prediction:** `hyp_38e58ce51876`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| src/oracles/aggregators/MagicLpAggregator.sol | MagicLpAggregator | _getReserves() | 33–35 |
| src/oracles/aggregators/MagicLpAggregator.sol | MagicLpAggregator | latestAnswer() | 37–46 |

#### Judge rationale

```text
R: Correctly identifies that permissionless swaps manipulate MagicLP reserves and thereby the spot reserve-derived oracle price used downstream. L: Correctly identifies MagicLpAggregator's reserve-based valuation path, but does not name _getReserves() or latestAnswer(), so the exact vulnerable functions are omitted. I: Correctly describes temporary collateral overvaluation, excessive borrowing, bad debt, and incorrect liquidation from manipulated oracle pricing. M: Time-weighted/manipulation-resistant pricing, independent references, deviation bounds, and rejecting materially shifted reserve states would address the flaw, though the proposal is broader and less explicit than directly comparing pool base/quote price with Chainlink and reverting.
```

</details>

#### Unmatched Ground Truth

No unmatched Ground Truth findings.

#### Unmatched Predictions

- hyp_0cdad7952348 — Unbounded LTV configuration can create undercollateralized borrowing
- hyp_a547184c8f23 — Owner-controlled ProxyOracle implementation enables instant price substitution
- hyp_108b416c2bac — Oracle failure preserves stale exchange rates for borrowing and liquidation

### `2024-03-revert-lend`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 1 |
| Matched weight | 0.8500 |
| Soft precision | 0.8500 |
| Soft recall | 0.8500 |
| Soft F1 | 0.8500 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| M-19 — [M-19] `V3Oracle` susceptible to price manipulation | hyp_2797f3444591 — Spot-price manipulation of concentrated LP collateral passes oracle validation | 3/4 | 3/4 | 4/4 | 4/4 | 0.8500 |

<details>
<summary>Pair 1: M-19 — [M-19] \`V3Oracle\` susceptible to price manipulation ↔ hyp_2797f3444591 — Spot-price manipulation of concentrated LP collateral passes oracle validation</summary>

- **Ground Truth:** `M-19`
- **Prediction:** `hyp_2797f3444591`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| src/V3Oracle.sol | V3Oracle | getValue(uint256,address) | 95–131 |
| src/V3Oracle.sol | V3Oracle | getPositionBreakdown(uint256) | 162–181 |
| src/V3Oracle.sol | V3Oracle | _initializeState(uint256) | 395–423 |
| src/V3Oracle.sol | V3Oracle | _getAmounts(PositionState) | 426–442 |

#### Prediction locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| src/V3Oracle.sol | V3Oracle | getValue(uint256,address) | — |
| src/V3Oracle.sol | V3Oracle | _checkPoolPrice(address,address,uint24,uint256) | — |
| src/V3Oracle.sol | V3Oracle | _getAmounts(PositionState memory) | — |
| src/V3Vault.sol | V3Vault | _checkLoanIsHealthy(uint256,uint256) | — |
| src/V3Vault.sol | V3Vault | borrow(uint256,uint256) | — |
| src/V3Vault.sol | V3Vault | loanInfo(uint256) | — |

#### Judge rationale

```text
R: Correctly identifies that position amounts and valuation depend on manipulable current Uniswap V3 spot price and that the price-difference check may permit distortion, but inaccurately characterizes the check as spot-based rather than comparing spot against an oracle-implied price. L: Correctly locates getValue(), _checkPoolPrice(), and _getAmounts(), with relevant downstream vault use; it omits secondary state/position-breakdown locations from the ground truth. I: Correctly describes overstated tight-range collateral enabling excess borrowing, unhealthy loans to appear healthy, and lender bad debt. M: Independent TWAP/oracle-based valuation and strict deviation validation would prevent the underlying spot-price valuation flaw; the proposed safeguards are technically effective.
```

</details>

#### Unmatched Ground Truth

No unmatched Ground Truth findings.

#### Unmatched Predictions

No unmatched predictions.

### `2024-03-woofi-swap`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 1 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-1 — H-1: Pool can be drained

#### Unmatched Predictions

- hyp_c98dbe4e89a7 — Unsolicited asset donation can manipulate vault share price and dilute deposits

### `2024-04-panoptic`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 0 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- M-01 — [M-01] `PanopticFactory` uses spot price when deploying new pools, resulting in liquidity manipulation when minting

#### Unmatched Predictions

No unmatched predictions.

### `2025-12-panoptic`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 0 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- M-11 — [M-11] An attacker can manipulate oracle easily

#### Unmatched Predictions

No unmatched predictions.


## Artifacts

- [manifest.json](manifest.json)
- [judge_artifact.json](judge_artifact.json)
- [report.json](report.json)

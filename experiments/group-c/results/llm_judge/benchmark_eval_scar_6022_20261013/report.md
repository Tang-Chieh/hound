# Benchmark Evaluation Report

> Derived from canonical Evaluation artifacts. This report does not execute LLM requests.

## Executive Summary

| Metric | Value |
| --- | --- |
| Report version | 0.2 |
| Benchmark version | v1 |
| Repositories | 23 |
| Ground Truth findings | 25 |
| Predictions | 118 |
| Total matched weight | 3.4000 |
| Pooled soft precision | 0.0288 |
| Pooled soft recall | 0.1360 |
| Macro soft F1 | 0.0411 |
| Pooled soft F1 | 0.0476 |

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
| Manifest SHA-256 | ded6e2486bea847796c867c10c7962a83282f9d33b47fbd0e7a7d1fd19c0865f |

## Repository Summary

| Repository | Ground Truth | Predictions | Matched weight | Precision | Recall | Soft F1 |
| --- | --- | --- | --- | --- | --- | --- |
| `2021-04-marginswap` | 1 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2021-07-spartan` | 2 | 9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2021-08-notional` | 1 | 9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2021-11-malt` | 1 | 9 | 0.5500 | 0.0611 | 0.5500 | 0.1100 |
| `2021-12-vader` | 1 | 9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-01-behodler` | 1 | 3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-01-sandclock` | 1 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-08-sentiment` | 1 | 14 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-09-notional` | 1 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-11-paraspace` | 1 | 2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2022-11-telcoin` | 1 | 8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2023-03-olympus` | 1 | 2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2023-04-blueberry` | 1 | 11 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2023-05-ussd` | 2 | 9 | 1.8500 | 0.2056 | 0.9250 | 0.3364 |
| `2023-06-lybra` | 1 | 6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2023-06-real-wagmi` | 1 | 3 | 1.0000 | 0.3333 | 1.0000 | 0.5000 |
| `2023-06-tokemak` | 1 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2023-08-dopex` | 1 | 2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2024-03-abracadabra-money` | 1 | 7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2024-03-revert-lend` | 1 | 4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2024-03-woofi-swap` | 1 | 3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2024-04-panoptic` | 1 | 6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| `2025-12-panoptic` | 1 | 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

## Repository Details

### `2021-04-marginswap`

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

- H-03 — [H-03] Price feed can be manipulated

#### Unmatched Predictions

No unmatched predictions.

### `2021-07-spartan`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 2 |
| Predictions | 9 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-05 — [H-05] Synth realise is vulnerable to flash loan attacks
- H-06 — [H-06] SynthVault rewards can be gamed

#### Unmatched Predictions

- hyp_207e7a763b19 — Router balance sweeping allows liquidity withdrawers to steal unrelated assets
- hyp_f0bf4a114496 — Curated-pool dividend payouts are unlimited despite maxTrades configuration
- hyp_e8487d8d134a — Router ignores token transfer return values and received amounts in asset ingress and egress
- hyp_4f27d10bb008 — BondVault claim logic can permanently lock half of a member’s remaining LP
- hyp_bb979dd4a209 — Integer truncation can create permanently unclaimable BondVault dust
- hyp_500b2cb11180 — Harvested Synth rewards bypass the minimum withdrawal lock
- hyp_063f529d178e — SynthVault harvestAll becomes increasingly gas-heavy and can become unusable
- hyp_f352a4505325 — Withdrawal basis points are not range-validated, enabling caller-triggered reverts and inconsistent partial accounting
- hyp_ad3667485200 — Arbitrary zero-value deposits can repeatedly lock another user’s SynthVault position

### `2021-08-notional`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 9 |
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

- hyp_8bd4b6bef412 — Stale Chainlink prices are accepted during collateral checks and trade settlement
- hyp_c45f684136d9 — Currency rate view returns the asset token as the underlying token
- hyp_b2e187e0ebd6 — Annualized supply-rate validation is ineffective and permits unbounded oracle output
- hyp_9d4ec98d0d6b — Transfer event is emitted even when delegated transfer fails
- hyp_eb675ae7f347 — Approval event uses reversed owner and spender fields
- hyp_3bdd69409b9a — ExchangeRate may fail to normalize oracle decimals before collateral valuation
- hyp_ff2e0ce3c398 — Nominal ERC20 transfer amounts may be credited without validating actual tokens received
- hyp_58d15d9adeda — AssetRate accepts economically implausible positive exchange rates
- hyp_0018c5295d46 — Previous token approvals remain active after Compound adapter approval changes

### `2021-11-malt`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 9 |
| Matched weight | 0.5500 |
| Soft precision | 0.0611 |
| Soft recall | 0.5500 |
| Soft F1 | 0.1100 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| M-22 — [M-22] `_calculateMaltRequiredForExit` Uses Spot Price To Calculate Malt Quantity In `exitEarly` | hyp_177db425543c — Permissionless reserve-ratio sampling enables flash manipulation of the moving average | 2/4 | 1/4 | 2/4 | 4/4 | 0.5500 |

<details>
<summary>Pair 1: M-22 — [M-22] \`_calculateMaltRequiredForExit\` Uses Spot Price To Calculate Malt Quantity In \`exitEarly\` ↔ hyp_177db425543c — Permissionless reserve-ratio sampling enables flash manipulation of the moving average</summary>

- **Ground Truth:** `M-22`
- **Prediction:** `hyp_177db425543c`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| src/contracts/DexHandlers/UniswapHandler.sol | UniswapHandler | maltMarketPrice() | 80–109 |
| src/contracts/AuctionEscapeHatch.sol | AuctionEscapeHatch | _calculateMaltRequiredForExit(uint256,uint256) | 168–213 |
| src/contracts/AuctionEscapeHatch.sol | AuctionEscapeHatch | exitEarly(uint256,uint256,uint256) | 65–92 |

#### Prediction locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| src/contracts/MaltDataLab.sol | MaltDataLab | trackReserveRatio | — |

#### Judge rationale

```text
R: Correctly identifies manipulation of Uniswap reserve-derived pricing data, but applies it to a reserve-ratio moving average rather than the direct spot price used for early exit. L: Locates an adjacent oracle-related function in MaltDataLab, but not UniswapHandler.maltMarketPrice, _calculateMaltRequiredForExit, or exitEarly. I: Correctly conveys attacker-controlled reserve manipulation leading to protocol losses, but gives a different affected calculation and outcome than early-exit fund extraction. M: A manipulation-resistant oracle or TWAP would remove the ground-truth reliance on manipulable current reserves.
```

</details>

#### Unmatched Ground Truth

No unmatched Ground Truth findings.

#### Unmatched Predictions

- hyp_d52af1b6d264 — Uniswap buy path accepts zero minimum output
- hyp_65e363c6719d — Hardcoded Pair Init Code Hash Can Route Reserve Reads to a Nonexistent or Wrong Pair
- hyp_aec894ec2751 — External Token Decimal Metadata Can Cause Arithmetic Reverts in Reserve Pricing and Deficit Calculations
- hyp_986004be27f4 — buyMalt Sweeps Pre-existing Malt Balance to the Buyer
- hyp_a8086e3b1c06 — Residual RewardToken Allowance Remains Authorized to Auction
- hyp_b98834e69e73 — Zero Sample Length Can Permanently Revert Moving-Average Updates
- hyp_d6835301f907 — Registered Reward Mine Revert Can Denial-of-Service Bonding Operations
- hyp_7f8ee2a76322 — RewardReinvestor Can Attribute Pre-existing Reward Balance to an Arbitrary Account

### `2021-12-vader`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 9 |
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

- hyp_fb1cb8287a17 — Liquidity add minimum amounts are ignored, enabling slippage and sandwich losses
- hyp_7ca78c1353ac — V2 mintSynth lacks router access control and can spend arbitrary approved users' native assets
- hyp_33ecc0f2eea1 — Daily mint limit is bypassed whenever a mint cycle rolls over
- hyp_d47616be84e6 — Swap queue operations are unimplemented and silently return default values
- hyp_82ed2fad32c4 — Execution reimbursement is always zero and forced ETH cannot be recovered
- hyp_b3acedd3d5d7 — XVader share-price donation attack enables zero-share deposits
- hyp_ba99874b84c7 — LiquidityBasedTWAP accepts stale or invalid Chainlink responses
- hyp_afeaf869e97b — V2 pool accounting is vulnerable to fee-on-transfer or deflationary supported tokens
- hyp_817b2959d89b — Zero-address distributor assignment can permanently disable reward notifications

### `2022-01-behodler`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 3 |
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

- hyp_a1120d1cc270 — Mint Calculates Proxy Tokens From Total Reserve Instead of Deposit Amount
- hyp_5c2fddc35d49 — Redeem Ignores ERC20 Transfer Failure
- hyp_56c43b7759fd — Mint and Redeem Return Zero Despite Declared Return Values

### `2022-01-sandclock`

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

- H-03 — [H-03] Vaults with non-UST underlying asset vulnerable to flash loan attack on curve pool

#### Unmatched Predictions

No unmatched predictions.

### `2022-08-sentiment`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 14 |
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

- hyp_38d8a25f645d — Stale Chainlink rounds are accepted for collateral valuation
- hyp_2f7090d887c2 — Feed decimal mismatch can arbitrarily mis-scale token prices
- hyp_0abd59c5e2c2 — Zero answers can disable pricing or create zero-valued collateral
- hyp_ca7683b1deaf — Spot liquidity can be flash-manipulated to suppress borrow interest
- hyp_c951f0969ba0 — Caller-supplied proxy administrator permits unauthorized upgrade control
- hyp_292a55dbf920 — Aave V3 supply and withdraw recipients are not constrained to the Account
- hyp_1a74b17c48ff — Aave V2 withdrawals are accepted without sufficient authorization checks
- hyp_a96f63171b0d — ERC4626 withdrawal and redemption authorization may permit arbitrary owners and receivers
- hyp_62ac97d46e92 — Uniswap V3 swap recipient is not constrained to the managed account
- hyp_5bdf78b1ea8b — Only the input token is allowlisted, permitting unsupported output and intermediate assets
- hyp_8d5e3a57cc95 — ATokenOracle permits recursive oracle cycles through underlying-asset resolution
- hyp_f7cf756afa46 — UniV2 LP valuation may mis-scale reserves for tokens with different decimals
- hyp_059fd37a0a6d — Recursive UniV2 LP oracle mappings can cause valuation denial of service
- hyp_abd673fb073e — Balancer join and exit recipients are not constrained to the managed account

### `2022-09-notional`

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

- M-7 — [M-7] Gain From Balancer Vaults Can Be Stolen

#### Unmatched Predictions

- hyp_7c765c9c07b0 — Unvalidated Aave asset configuration can create an incorrect exchange-rate oracle

### `2022-11-paraspace`

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

- H-05 — [H-05] Attacker can manipulate low TVL Uniswap V3 pool to borrow and swap to make Lending Pool in loss

#### Unmatched Predictions

- hyp_8a2ff7190b02 — Administrator Can Bypass NFT Price Validation
- hyp_745919b22c32 — Supply Accounting May Overmint Shares for Fee-on-Transfer ERC20 Assets

### `2022-11-telcoin`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 8 |
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

- hyp_de8cb4f027b7 — Unvalidated plugin registration enables global denial of service
- hyp_24a2a40e84b8 — Removing a plugin can permanently strand user rewards
- hyp_9b6f63dd6050 — Stake accounting can exceed actual TEL received for fee-on-transfer or nonstandard TEL
- hyp_30150ad4ee47 — FeeBuyback credits all residual TEL balance to the current referral
- hyp_ed03fb292076 — FeeBuyback ignores ERC20 transfer and approval return values
- hyp_d79a85f5b9e4 — RECOVERY_ROLE can redirect users’ migrated principal and rewards to an arbitrary recipient
- hyp_aa53e9d65b24 — Owner-controlled arbitrary call enables FeeBuyback asset and approval exfiltration
- hyp_9070627b9861 — Successful aggregator call is accepted without verifying TEL output

### `2023-03-olympus`

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

- H-1 — H-1: Adversary can sandwich oracle updates to exploit vault

#### Unmatched Predictions

- hyp_088a4b857015 — Oracle pricing can accept stale or otherwise invalid Chainlink data
- hyp_f4283b9b2d19 — Unbounded Aura extra-reward processing can block reward claims and withdrawals

### `2023-04-blueberry`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 11 |
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

- hyp_a9bce5911080 — ERC20 approval return values are ignored
- hyp_882646e07dc8 — Unvalidated Base Oracle Address Can Permanently Disable Pricing
- hyp_3db220d87b96 — Curve gauge remapping can strand or misroute existing wrapped positions
- hyp_ba50fa645121 — Privileged route configuration can inject arbitrary asset prices
- hyp_557fc3bd6a2c — Unbounded Chainlink feed decimals can distort or disable price conversion
- hyp_6602baa69112 — CurveSpell reward swaps allow zero minimum output and are sandwichable
- hyp_24b8867d8ad2 — AuraSpell reward swaps may be executable with zero or caller-controlled slippage protection
- hyp_2d360559a6aa — ShortLongSpell Paraswap execution permits insufficient-output swaps
- hyp_c110e51a3107 — Externally Mutable Curve Address Provider Can Replace the Trusted Registry
- hyp_7327eeaffee2 — Unbounded token decimals can break or distort Uniswap V2 price normalization
- hyp_a7767c474abe — BaseOracleExt deviation arithmetic can overflow and brick dependent price reads

### `2023-05-ussd`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 2 |
| Predictions | 9 |
| Matched weight | 1.8500 |
| Soft precision | 0.2056 |
| Soft recall | 0.9250 |
| Soft F1 | 0.3364 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| H-5 — H-5: Price calculation susceptible to flashloan exploits | hyp_32f367364f7b — Permissionless rebalancing is manipulable through the Uniswap V3 spot price and pool balances | 4/4 | 4/4 | 4/4 | 4/4 | 1.0000 |
| H-9 — H-9: Uniswap v3 pool token balance proportion does not necessarily correspond to the price, and it is easy to manipulate. | hyp_e0ad06a8b8bc — Peg-down rebalance can revert from unsigned subtraction underflow | 4/4 | 4/4 | 3/4 | 2/4 | 0.8500 |

<details>
<summary>Pair 1: H-5 — H-5: Price calculation susceptible to flashloan exploits ↔ hyp_32f367364f7b — Permissionless rebalancing is manipulable through the Uniswap V3 spot price and pool balances</summary>

- **Ground Truth:** `H-5`
- **Prediction:** `hyp_32f367364f7b`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | getOwnValuation() | 71–80 |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | rebalance() | 92–107 |

#### Prediction locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | rebalance | — |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | getOwnValuation | — |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | getSupplyProportion | — |
| ussd-contracts/contracts/USSD.sol | USSD | UniV3SwapInput | — |

#### Judge rationale

```text
R: Correctly identifies manipulation of the instantaneous Uniswap V3 spot price via slot0(), including flash-loan-capable temporary manipulation. L: Correctly localizes getOwnValuation() and rebalance(), including the valuation-to-rebalance path. I: Correctly describes attacker-controlled rebalancing that can cause reserve-asset loss and peg damage. M: TWAP or an independently validated oracle directly fixes the ground-truth flaw; the additional controls are also relevant hardening.
```

</details>

<details>
<summary>Pair 2: H-9 — H-9: Uniswap v3 pool token balance proportion does not necessarily correspond to the price, and it is easy to manipulate. ↔ hyp_e0ad06a8b8bc — Peg-down rebalance can revert from unsigned subtraction underflow</summary>

- **Ground Truth:** `H-9`
- **Prediction:** `hyp_e0ad06a8b8bc`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | getSupplyProportion() | 83–90 |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | rebalance() | 92–107 |

#### Prediction locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | rebalance | — |
| ussd-contracts/contracts/USSDRebalancer.sol | USSDRebalancer | setTreshold | — |

#### Judge rationale

```text
R: Correctly identifies the unsigned subtraction underflow when normalized DAI exceeds USSD during peg-down rebalancing, which is an explicit consequence of the ground-truth balance-proportion flaw. L: Correctly identifies the subtraction in rebalance(); the additional threshold issue is separate but does not detract from localization. I: Correctly states that rebalancing can become unavailable during a depeg and recovery is prevented, though it does not cover the separate over-minting consequence. M: Branching or clamping fixes the underflow manifestation, but does not address the underlying Uniswap V3 range/fee distortion or the over-peg excess-minting path; the threshold check is unrelated to the core issue.
```

</details>

#### Unmatched Ground Truth

No unmatched Ground Truth findings.

#### Unmatched Predictions

- hyp_419275c1d0b3 — Collateral exclusion check is always true and can swap pool base assets incorrectly
- hyp_cfd90452ecdd — Unrestricted mintRebalancer and burnRebalancer permit unauthorized supply manipulation
- hyp_45848f4e4bbf — Oracle implementations accept invalid or unavailable prices
- hyp_4d2b0be6be76 — "description": "SellUSSDBuyCollateral intends to avoid swapping collateral tokens that are already the pool legs, but uses if (token != token0
- hyp_daf2317bedbf — Network-specific hardcoded Chainlink feed can invalidate WETH pricing on non-mainnet deployments
- hyp_3956a14a1446 — StableOracleWBTC uses the ETH/USD Chainlink feed instead of BTC/USD
- hyp_00bfa4ce9b37 — Unrestricted SimOracle price setter allows arbitrary oracle-price manipulation

### `2023-06-lybra`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 6 |
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

- hyp_af679c406664 — Deployer retains direct DAO authority over critical configurator controls
- hyp_f79e1ab5e53c — Protocol reward distributions are permanently stranded when no esLBR holders are staked
- hyp_db7d99def3b4 — Boosted rewards can be applied retroactively
- hyp_cd997ea22442 — Reward duration accepts zero and reward scheduling truncates emissions
- hyp_02fa2949ad42 — LBR oracle result is used without zero, sign, or freshness validation during reward buyout
- hyp_c8a4e742e100 — StETH rebasing can make recorded collateral exceed the vault’s actual collateral

### `2023-06-real-wagmi`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 3 |
| Matched weight | 1.0000 |
| Soft precision | 0.3333 |
| Soft recall | 1.0000 |
| Soft F1 | 0.5000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| H-3 — H-3: Usage of `slot0` is extremely easy to manipulate | hyp_d2fcdfe7d2c1 — Spot-price manipulation can distort deposit LP issuance | 4/4 | 4/4 | 4/4 | 4/4 | 1.0000 |

<details>
<summary>Pair 1: H-3 — H-3: Usage of \`slot0\` is extremely easy to manipulate ↔ hyp_d2fcdfe7d2c1 — Spot-price manipulation can distort deposit LP issuance</summary>

- **Ground Truth:** `H-3`
- **Prediction:** `hyp_d2fcdfe7d2c1`

#### Ground Truth locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| concentrator/contracts/Multipool.sol | Multipool | deposit(uint256,uint256,uint256,uint256) | 433–486 |
| concentrator/contracts/Multipool.sol | Multipool | getSlots() | 589–602 |
| concentrator/contracts/Multipool.sol | Multipool | _getReserves(Slot0Data[]) | 693–768 |

#### Prediction locations

| File | Contract | Function | Lines |
| --- | --- | --- | --- |
| concentrator/contracts/Multipool.sol | Multipool | deposit | — |
| concentrator/contracts/Multipool.sol | Multipool | getSlots | — |

#### Judge rationale

```text
R: Correctly identifies that deposit uses manipulable current slot0 data from getSlots without TWAP protection to value liquidity and issue LP tokens. L: Correctly localizes both deposit and getSlots and their data flow into issuance calculations; omission of _getReserves is minor and does not obscure the path. I: Correctly describes manipulated LP issuance, unfair dilution, and value transfer to or from existing providers. M: A validated manipulation-resistant TWAP, observation checks, and price-impact protections would prevent the ground-truth vulnerability.
```

</details>

#### Unmatched Ground Truth

No unmatched Ground Truth findings.

#### Unmatched Predictions

- hyp_92fca074a04e — Rebalance is hardcoded to the 0.05% Uniswap pool and can be permanently unavailable
- hyp_5c8f93529b0b — Unbounded TWAP duration configuration can disable all rebalances

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

- hyp_aa1f3f26a7fc — Vault-only collateral updates can leave LP accounting stale across settlement and liquidity flows
- hyp_e19bbe41e6af — Caller-controlled Uniswap V3 minimum output exposes vault swaps to adverse execution

### `2024-03-abracadabra-money`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 7 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- H-04 — [H-04] Oracle price can be manipulated

#### Unmatched Predictions

- hyp_48d7aad369ac — Stale oracle price is trusted during oracle failure, enabling undercollateralized borrowing
- hyp_699e5cdd35b8 — Malformed MagicLP aggregator responses can permanently block oracle-dependent Cauldron operations
- hyp_42370bb502e6 — Cauldron accepts a zero exchange rate from a successful oracle update
- hyp_fd1a1eb95327 — Fee-on-transfer staking tokens can make internal principal accounting exceed actual holdings
- hyp_a2a9008db8ce — Fee-on-transfer reward tokens can create unpayable reward liabilities
- hyp_c8919c9cbc5a — Hardcoded Blast Points endpoint can make deployments fail outside Blast
- hyp_73a37a9d6cdb — Whitelisting revocation does not disable existing master-contract associations

### `2024-03-revert-lend`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 4 |
| Matched weight | 0.0000 |
| Soft precision | 0.0000 |
| Soft recall | 0.0000 |
| Soft F1 | 0.0000 |

#### Matched Findings

| Ground Truth | Prediction | R | L | I | M | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| No matched findings. | | | | | | |

#### Unmatched Ground Truth

- M-19 — [M-19] `V3Oracle` susceptible to price manipulation

#### Unmatched Predictions

- hyp_425a6cd751dc — Flash callback may accept forged callbacks without pool and operation authentication
- hyp_c9da7b8b20a3 — TWAP-bound pool swaps may still permit economically harmful execution within the accepted deviation
- hyp_5692808ccf83 — AutoExit configuration may remain bound to a token ID after NFT ownership changes
- hyp_b575b2fae562 — ERC-4626 redemption can overstate liquidity when assets are lent out

### `2024-03-woofi-swap`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 3 |
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

- hyp_a3f2d0945e66 — Global oracle timestamp allows stale asset prices to remain feasible
- hyp_d1b45860dccf — WooRouterV3 retains excess native currency as stranded WETH
- hyp_b8871f804dc1 — Unvalidated external dependency addresses can permanently disable or corrupt fee quoting

### `2024-04-panoptic`

| Metric | Value |
| --- | --- |
| Ground Truth findings | 1 |
| Predictions | 6 |
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

- hyp_058c3b89b306 — Uniswap mint callback can be triggered through an unsolicited direct pool mint
- hyp_181175efb559 — Owner-controlled factory can arbitrarily mint donor NFTs or permanently disable issuance
- hyp_463f0b0c7ca6 — Ignored approve return values can leave pools initialized with unusable allowances
- hyp_f6535d1954b9 — Unbounded token metadata can cause gas or memory denial of service
- hyp_b93b237fb445 — Uniswap fee-growth values can overflow signed fee packing
- hyp_cd8e200f2bfe — SafeTransferLib silently accepts transfers to non-contract token addresses

### `2025-12-panoptic`

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

- M-11 — [M-11] An attacker can manipulate oracle easily

#### Unmatched Predictions

- hyp_527e443b401c — Factory accepts an unauthenticated risk-engine address


## Artifacts

- [manifest.json](manifest.json)
- [judge_artifact.json](judge_artifact.json)
- [report.json](report.json)

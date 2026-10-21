# 4 Results

Translated from the author's Chinese draft (`results_4.1-4.6_zh_v0.md`, 2026-10-22). Edits made in translation:

- All figures replaced with the consensus-code values in `analysis/results_tables_consensus.md`.
- Three interpretive passages moved, unchanged in substance, to the holding section at the end. They will go into the Discussion.
- The conclusion drawn from D6 narrowed, and the count of sensitivity analyses corrected.
- The description of the D5 disagreements corrected to match the adjudication log.

## 4.1 Inter-coder agreement

Before adjudication, the two coders agreed on 84.7% of cells, with κ = 0.70 (Table 2).

- **Highest agreement:** colour (D2, κ = 0.92), where the rule leaves little room for interpretation.
- **Lowest agreement:** markers and accessories (D5, κ = 0.45) and cross-cultural substitution (D6, κ = 0.24).

The D5 disagreements centred on three kinds of judgement: whether a belt counts as a jade belt; whether Bao Zheng's face shows the white crescent; and whether a weapon or a set of small pennants satisfies the requirement for a spear or for back flags. On all three, coder B applied the codebook more strictly than coder A.

The low κ for D6 is partly a matter of base rate. Violations were rare, and κ is depressed when the base rate is low. The coders also drew the boundary of "close to modern hanfu" and "close to Japanese style" differently.

The two coders disagreed on 132 cells across 78 images. Nine were settled by explicit codebook rules and the rest by coder A's judgement.

**Table 2.** Inter-coder agreement before adjudication.

| Dimension | Agreement | Cohen's κ |
|---|---|---|
| D1 Garment type | 86.1% | 0.68 |
| D2 Colour | 95.1% | 0.92 |
| D3 Motif | 84.7% | 0.64 |
| D4 Headwear | 83.3% | 0.66 |
| D5 Markers and accessories | 71.5% | 0.45 |
| D6 Cross-cultural substitution | 87.5% | 0.24 |
| Overall | 84.7% | 0.70 |

## 4.2 RQ1: Overall compliance

Across all 144 images, only 56 (38.9%) complied with the dress code on every dimension. Under P1 the share was 14 of 72; under P2 it was 42 of 72.

The channels differed widely under P1 (Table 3):

- **Hunyuan Image Alpha** did worst. It violated the code on 75.9% of codable items, produced no fully compliant image, and averaged 4.21 violations per image.
- **Meta AI** did best. Its P1 violation rate was 19.8%, nearly half of its images (45.8%) were fully compliant, and it averaged 1.08 violations per image.
- **Doubao** fell in between: 37.1% of items in violation and 12.5% of images fully compliant.

**Table 3.** Violation rate, share of fully compliant images and mean violations per image, by channel and strategy.

| Channel | Violation rate P1 | Violation rate P2 | Fully compliant P1 | Fully compliant P2 | Mean violations P1 | Mean violations P2 |
|---|---|---|---|---|---|---|
| Hunyuan Image Alpha (WorkBuddy) | 75.9% | 26.0% | 0.0% | 33.3% | 4.21 | 1.42 |
| Doubao | 37.1% | 7.6% | 12.5% | 58.3% | 2.04 | 0.42 |
| Meta AI (Muse) | 19.8% | 3.0% | 45.8% | 83.3% | 1.08 | 0.17 |

## 4.3 RQ2: Which dimensions and roles fail most

**By dimension.** Headwear was among the dimensions most often violated. Under P1, its violation rate was 56.9%, against 47.2% for garment type and 57.7% for markers and accessories (Table 4). In the adjusted model, with garment type as the reference, the odds of a violation were higher for:

- headwear: OR = 2.67, 95% CI 1.51–4.70, p < .001;
- markers and accessories: OR = 2.12, 95% CI 1.20–3.76, p = .010.

Cross-cultural substitution was the least frequent error (P1: 13.9%; OR = 0.12, 95% CI 0.05–0.28, p < .001). When it did occur, it consisted mainly of Qing court headdresses and modern hanfu elements. Japanese, Korean and Western elements were rare.

**Table 4.** Violation rate by dimension.

| Dimension | All | P1 | P2 | Codable cells |
|---|---|---|---|---|
| D1 Garment type | 27.8% | 47.2% | 8.3% | 144 |
| D2 Colour | 27.4% | 54.1% | 0.0% | 73 |
| D3 Motif | 27.8% | 41.7% | 13.9% | 144 |
| D4 Headwear | 40.3% | 56.9% | 23.6% | 144 |
| D5 Markers and accessories | 37.3% | 57.7% | 16.9% | 142 |
| D6 Cross-cultural substitution | 9.0% | 13.9% | 4.2% | 144 |

**By role.** The gap between roles was wide (Table 5). Jiang Gan and Su San were the most often wrong, with 67.4% and 70.4% of P1 items in violation. Yang Yuhuan was the least often wrong, at 22.2% under P1 and no violations under P2.

**Table 5.** Violation rate by role.

| Role | All | P1 | P2 | Codable cells |
|---|---|---|---|---|
| R1 Zhuge Liang | 35.6% | 55.6% | 15.6% | 90 |
| R2 Guan Yu | 23.1% | 31.5% | 14.8% | 108 |
| R3 Yang Yuhuan | 11.1% | 22.2% | 0.0% | 90 |
| R4 Mu Guiying | 16.7% | 26.7% | 6.7% | 90 |
| R5 Bao Zheng | 21.7% | 35.8% | 7.5% | 106 |
| R6 Zhao Yun | 28.7% | 44.4% | 13.0% | 108 |
| R7 Su San | 43.5% | 70.4% | 16.7% | 108 |
| R8 Jiang Gan | 45.1% | 67.4% | 22.2% | 91 |

**Typical errors.** Four errors were typical (sheet numbers in brackets).

1. **Zhuge Liang rendered as a generic chief minister** (S02-1 to S02-3, Doubao, P1). All three images show a python robe and an official's hat. The bagua robe, bagua scarf hat and feather fan are all missing.
2. **Su San without the cangue.** In S01-3 (Hunyuan, P1) and S09-1 to S09-3 (Doubao, P1), the cangue never appears. The three S09 images are almost identical, each a lake-blue *xuezi*, which shows homogeneous output.
3. **Jiang Gan without the clown face** (S03-1, S03-2, S04-2, Hunyuan, P1). None of the three shows the tofu-block patch. S04-2 comes closest, with white patches around the eyes, but its headwear is a tall flat-topped black hat and the figure wears a short jacket and trousers. It is even further from the *xuezi* and square cap.
4. **Modern objects in the frame** (S01-2, Hunyuan, P1). Su San holds a birdcage, a pink plastic stool stands at her feet, and the corner of a wall is visible behind her. The instruction "plain light grey background" had no effect.

## 4.4 RQ3: Does stating the dress code help?

Stating the dress code reduced the odds of a violation to about one fifteenth of the P1 level (OR = 0.066, 95% CI 0.038–0.116, p < .001).

The channels differed sharply. With Hunyuan Image Alpha as the reference:

- Doubao: OR = 0.128 (95% CI 0.082–0.201, p < .001);
- Meta AI: OR = 0.040 (95% CI 0.021–0.077, p < .001).

The channel × strategy interaction was not significant (Doubao p = .177; Meta AI p = .256). The relative effect of P2 was therefore similar across channels: P2 helped all three, and only the absolute size of the gain differed.

P2 is not a cure-all. Two thirds of Hunyuan Image Alpha's P2 images still broke at least one rule (fully compliant: 33.3%). Writing the dress code into the prompt lowers the violation rate, but does not bring it to zero.

## 4.5 Errors caused by translating the prompt

Two errors can be traced to the literal English wording rather than to a lack of knowledge of Peking opera.

1. **Xuezi rendered as "pleated robe"** (S30-1 to S30-3, Meta AI, P2). The model read "pleated" as a property of the cloth and drew robes with obvious knife pleats. In S30-3 Jiang Gan also wears a square cap resembling an academic mortarboard.
2. **Yu jia rendered as "fish-shaped cangue"** (S39-1 to S39-3, Doubao, P2). The model read "fish" as a decoration on the board and drew a rectangular wooden board carved with a fish. In the *yu jia*, the fish defines the outline of the cangue itself.

## 4.6 Other anomalies and sensitivity analyses

Four types of anomaly were recorded during coding. None of the images involved was excluded.

- **Reproduced stock-photo watermark:** Hunyuan, P1, R2, image 2 (S34-2), `www.yanqin.net`.
- **Anatomical errors:** Bao Zheng seen from behind with the painted face on the back of the head (S10-1 and S10-3, P1; S36-3, P2; all Meta AI).
- **A second performer in the frame:** S01-1 (Hunyuan, P1).
- **A modern object in the frame:** the plastic stool in S01-2 (Hunyuan, P1).

**Table 6.** Main analysis and sensitivity analyses (odds ratios).

| Analysis | P2 | Doubao | Meta AI |
|---|---|---|---|
| Main analysis (consensus codes) | 0.066 | 0.128 | 0.040 |
| Excluding the watermarked image | 0.066 | 0.127 | 0.040 |
| NA counted as compliant | 0.073 | 0.138 | 0.044 |
| Excluding D3 | 0.057 | 0.130 | 0.043 |
| Excluding D1 | 0.084 | 0.151 | 0.051 |
| Coder A only (before adjudication) | 0.063 | 0.100 | 0.040 |
| Coder B only | 0.041 | 0.180 | 0.055 |

Across the main analysis and the six sensitivity analyses, all three effects pointed the same way:

- P2: OR between 0.041 and 0.084;
- Doubao: OR between 0.100 and 0.180;
- Meta AI: OR between 0.040 and 0.055.

None of these ranges crosses 1. The conclusions did not change with exclusions, with a different treatment of missing values, or with a change of coder.

The coder-B-only analysis departed most from the main analysis. Its P2 odds ratio was lower (0.041), while its Doubao (0.180) and Meta AI (0.055) odds ratios were higher. The departure does not reverse any conclusion.

---

## Held for the Discussion (author's interpretations, moved from 4.3, 4.5 and 4.6)

- **From 4.3.** The roles share a pattern. Jiang Gan and Su San depend on a specific item for their identity: the tofu-block face and square cap for Jiang Gan, the cangue and red prisoner's dress for Su San. If that item is missing, the whole image is wrong. Yang Yuhuan's phoenix crown, cloud collar and jade belt are large pieces, and a model that captures their outline does not go far wrong.
- **From 4.5.** Possible mechanism: "scholar's robe" and "academic dress" share associations in English, which may explain the mortarboard. More generally, once a term is translated word by word, the model generates from the literal combination and the information about form is lost. [Speculative; to be phrased as a possibility in the Discussion.]
- **From 4.6.** Whether an AI coder should serve as a sole judge, to be discussed together with the coders' qualifications. [The original wording "coder B is more polarised" does not match the data, because B's estimates move in different directions for different terms. Rephrase.]

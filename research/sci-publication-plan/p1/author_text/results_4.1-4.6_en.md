# 4 Results

Translated from the author's Chinese draft (`results_4.1-4.6_zh_v1.md`). Empty table cells were filled from `analysis/results_tables_consensus.md`. Corrections of fact are marked [Corrected] in the review notes.

## 4.1 Inter-coder agreement

Both coders coded the six dimensions of all 144 images, for a total of 864 coding cells. After excluding 73 cells that were not applicable or not visible, 791 coded items remained. Table 2 reports overall agreement and Cohen's κ for each dimension.

Agreement was uneven across dimensions. Colour (D2) had the highest κ, which shows that the colour rule was the easiest judgement to reproduce between coders. Markers and accessories (D5) and cross-cultural substitution (D6) had the lowest.

The D5 disagreements centred on three judgements:

- whether a belt counts as a jade belt;
- whether Bao Zheng's forehead shows the white crescent;
- whether a glaive or a set of small pennants satisfies the requirement for a spear or for back flags.

None of these is a question of visibility. Each is a question of whether a substitute or an approximation counts. On all three, coder B applied the codebook more strictly than coder A.

The low κ for D6 has two sources. First, D6 had the fewest violations in the sample, and a low base rate limits the attainable κ. Second, assigning an element to Qing court dress or to modern hanfu required case-by-case judgement, and the two coders set different thresholds for "close to hanfu".

**Table 2.** Inter-coder agreement before adjudication. Confidence intervals were obtained by bootstrapping images, with 2,000 resamples.

| Dimension | Agreement | Cohen's κ | 95% CI |
|---|---|---|---|
| Overall | 84.7% | 0.70 | 0.64–0.76 |
| D1 Garment type | 86.1% | 0.68 | 0.55–0.80 |
| D2 Colour | 95.1% | 0.92 | 0.85–0.98 |
| D3 Motif | 84.7% | 0.64 | 0.49–0.77 |
| D4 Headwear | 83.3% | 0.66 | 0.53–0.78 |
| D5 Markers and accessories | 71.5% | 0.45 | 0.32–0.58 |
| D6 Cross-cultural substitution | 87.5% | 0.24 | −0.01–0.48 |

*Note.* D2 applies only to Guan Yu, Bao Zheng, Zhao Yun and Su San; the other roles were coded NA. Agreement was computed on all 144 images, with NA treated as a separate category.

## 4.2 RQ1: Overall compliance under P1

When the prompt named only the role and the play, without stating the dress code (P1), the three channels differed markedly (Table 3).

- **Hunyuan Image Alpha** violated the most rules. Its violation rate was 75.9%, and none of its 24 images was fully compliant.
- **Meta AI (Muse)** violated the fewest. Its violation rate was 19.8%, and 11 of its 24 images were fully compliant.
- **Doubao** fell in between, with a violation rate of 37.1% and 3 fully compliant images out of 24.

After controlling for prompt strategy, dimension and role, the odds of a violation relative to Hunyuan Image Alpha were 0.128 for Doubao and 0.040 for Muse.

Of all 144 images, 56 (38.9%) complied on all six dimensions. The other 88 violated at least one rule.

**Table 3.** Violations by channel under P1.

| Channel | Images | ≥ 1 violation, n (%) | Fully compliant, n (%) | Coded items | Item-level violation rate |
|---|---|---|---|---|---|
| Hunyuan Image Alpha | 24 | 24 (100%) | 0 (0.0%) | 133 | 75.9% |
| Doubao | 24 | 21 (87.5%) | 3 (12.5%) | 132 | 37.1% |
| Muse | 24 | 13 (54.2%) | 11 (45.8%) | 131 | 19.8% |

*Note.* Under P1, each channel produced 3 images for each of the 8 roles, giving 24 images per channel.

## 4.3 RQ2: Which dimensions and roles fail most

Table 4 gives the violation rate and adjusted OR for each dimension.

- **Most violations:** headwear (40.3% of codable items).
- **Next:** markers and accessories (37.3%), then garment type and motif (27.8% each).
- **Fewest:** cross-cultural substitution (9.0%).

The low rate for cross-cultural substitution does not mean that the outputs stayed inside the Peking opera system. The violations on this dimension were Qing court headdresses, modern hanfu and Japanese-style elements, all of which lie outside the Peking opera dress code. They simply occurred less often than errors of garment type and headwear.

**Table 4.** Violation rate and adjusted OR by dimension.

| Dimension | Violations / codable | Violation rate | Adjusted OR | 95% CI | p |
|---|---|---|---|---|---|
| D1 Garment type | 40/144 | 27.8% | 1 (reference) | — | — |
| D2 Colour | 20/73 | 27.4% | 0.80 | 0.43–1.51 | .494 |
| D3 Motif | 40/144 | 27.8% | 1.00 | 0.54–1.85 | > .999 |
| D4 Headwear | 58/144 | 40.3% | 2.67 | 1.51–4.70 | < .001 |
| D5 Markers and accessories | 53/142 | 37.3% | 2.12 | 1.20–3.76 | .010 |
| D6 Cross-cultural substitution | 13/144 | 9.0% | 0.12 | 0.05–0.28 | < .001 |

*Note.* ORs come from a GEE binomial logistic regression with the image–dimension pair as the unit of observation, clustered on image. D1 is the reference level.

The roles also differed markedly (Table 5). Three examples show what the errors looked like.

1. **Zhuge Liang's bagua robe replaced by a python robe.** All three Doubao P1 images (S02) show a literati figure in a robe covered with round dragons, wearing an official's hat. None carries the trigram pattern.
2. **Su San's fish cangue missing.** Su San appeared in elaborate women's dress rather than the prisoner's jacket and skirt. Examples are the green robe with a Qing headdress in S01-3 and the lake-blue *xuezi* in S09-1 to S09-3. When a substitute did appear, it was a chain or a carved board, and the cangue's form, size and manner of wearing were all wrong.
3. **Jiang Gan's clown markers missing.** In some images the tofu-block patch became a large white mask over the face (S04-2), and the square cap was replaced by a tall hat or an official's hat (S03, S04-2).

**Table 5.** Violation rate by role.

| ID | Role | Role type | P1 | P2 | All |
|---|---|---|---|---|---|
| R1 | Zhuge Liang | laosheng | 55.6% | 15.6% | 35.6% |
| R2 | Guan Yu | hongsheng | 31.5% | 14.8% | 23.1% |
| R3 | Yang Yuhuan | huashan | 22.2% | 0.0% | 11.1% |
| R4 | Mu Guiying | daomadan | 26.7% | 6.7% | 16.7% |
| R5 | Bao Zheng | tongchui hualian | 35.8% | 7.5% | 21.7% |
| R6 | Zhao Yun | wusheng | 44.4% | 13.0% | 28.7% |
| R7 | Su San | qingyi | 70.4% | 16.7% | 43.5% |
| R8 | Jiang Gan | wenchou | 67.4% | 22.2% | 45.1% |

## 4.4 RQ3: The effect of stating the dress code

Stating the dress code in the prompt (P2) significantly reduced the odds of a violation. Relative to P1, the adjusted OR for P2 was 0.066 (95% CI 0.038–0.116, p < .001), meaning the odds of a violation fell to 6.6% of their P1 level.

Differences between channels remained. Relative to Hunyuan Image Alpha, the main-effect OR was 0.128 for Doubao and 0.040 for Muse. The channel × strategy interaction was not significant (p = .18 and .26), so the effect of P2 had the same direction and a similar size in all three channels. The dress-code statement did not work for only one channel.

The dress-code statement did not eliminate violations. About two thirds of Hunyuan Image Alpha's P2 images still violated at least one rule. Stating garment and colour in the prompt lowers the frequency of errors, but it cannot replace human checking.

## 4.5 Errors caused by translating costume terms

Some errors can be traced to meaning lost when Chinese costume terms were rendered in English for the prompt.

**Xuezi.** Rendered as "pleated robe", *xuezi* was read by the model as a garment with physical pleats, and the output was a pleated scholar's gown. Jiang Gan's images show this most clearly: a plain gown with pleats, worn with a square black hat that looks more like an academic mortarboard than a scholar's square cap (S30, Meta AI, P2).

**Yu jia.** Rendered as "fish-shaped cangue", *yu jia* was read by the model as a cangue decorated with a fish rather than one with the outline of a fish. The output was a square board with a fish carved on its surface, and its size and proportions did not match the form of the cangue (S39, Doubao, P2).

In both cases a term was translated word by word, and information about form was lost along the way. "Pleated" kept the literal sense of 褶 but lost what *xuezi* refers to as a class of garment. "Fish-shaped" kept the modifying relation with "fish" but lost the outline of the cangue as a whole. This is consistent with the reason given in the Method for listing untested Chinese prompts as a limitation.

## 4.6 Other anomalies and sensitivity analyses

Besides dress-code violations, the outputs showed four kinds of anomaly.

1. **Stock-photo watermark.** The second P1 image of Guan Yu from Hunyuan Image Alpha (S34-2) reproduces the watermark of a third-party image source, `www.yanqin.net`, at the bottom centre of the frame. This suggests that the training data contained such images.
2. **Anatomical errors.** Three images place the face on the back of the head, so the figure is seen from behind with a painted face (S10-1, S10-3 and S36-3; all Meta AI, all Bao Zheng).
3. **Unclean frames.** Individual images include a second performer, a modern plastic stool and a birdcage (S01).
4. **Mismatched role type and gender.** Some images give a role the wrong role type or gender. Jiang Gan appears as a female *dan* (S03-1), and Zhao Yun as a female dancer (S22-3).

All of these images were kept and coded; none was excluded.

The study ran six sensitivity analyses, which together with the main analysis form the seven rows of Table 6:

1. excluding the watermarked image;
2. counting NA as compliant, so that it stays in the denominator;
3. excluding D3;
4. excluding D1;
5. using only coder A's codes before adjudication;
6. using only coder B's codes.

In all six, every effect pointed in the same direction as in the main analysis. The OR ranged from 0.041 to 0.084 for P2, from 0.100 to 0.180 for Doubao, and from 0.040 to 0.055 for Muse, and all remained below 1. The conclusions did not depend on which codes were used or on whether individual images were kept.

**Table 6.** Sensitivity analyses.

| Analysis | P2 OR | Doubao OR | Muse OR |
|---|---|---|---|
| Main analysis (consensus codes) | 0.066 | 0.128 | 0.040 |
| Excluding the watermarked image | 0.066 | 0.127 | 0.040 |
| NA counted as compliant | 0.073 | 0.138 | 0.044 |
| Excluding D3 | 0.057 | 0.130 | 0.043 |
| Excluding D1 | 0.084 | 0.151 | 0.051 |
| Coder A only (before adjudication) | 0.063 | 0.100 | 0.040 |
| Coder B only | 0.041 | 0.180 | 0.055 |

*Note.* The reference levels are P1 for the strategy effect and Hunyuan Image Alpha for the channel effects. The "coder A only" row uses the original codes before adjudication, so it differs slightly from the main analysis.

# Do text-to-image systems follow the dress code of Peking opera? An audit of rule violations in AI-generated xiqu costumes

**Status:** draft v0 (2026-10-21). Results use one coder only (coder B, model-assisted) and are marked **[B-only]**. Every number changes once coder A (the author) finishes independent coding and the two sets are reconciled.

**Target journal:** The Journal of the Textile Institute (Taylor & Francis). Format and word limits to be checked against the current author guidelines before submission.

---

## Abstract (≤250 words; numbers provisional)

Text-to-image (T2I) systems are already used to draft stage costumes and cultural merchandise, yet traditional theatre costume follows codified rules that a generic image model has no reason to know. Peking opera is a clear case: the trade saying "better to wear a torn costume than the wrong one" (宁穿破，不穿错) refers to a dress code that fixes garment type, colour, motif, headwear and accessories by role. I audited three consumer-facing T2I channels (Doubao, Meta AI and Hunyuan Image Alpha via Tencent WorkBuddy) on eight canonical roles under two prompting conditions: the role name only (P1) and the role name plus an explicit statement of its dress code (P2). The 144 images were coded on six rule dimensions using a codebook built from published studies of Peking opera wardrobe practice. Under P1, [B-only] 32.6–80.5% of codable items violated the dress code and only 0–8% of images were fully compliant. Stating the rules in the prompt cut the odds of a violation by about 96% (OR = 0.041, 95% CI 0.022–0.077) [B-only], but compliance still differed sharply across systems. Errors concentrated in accessories and role markers (beards, back flags, the fish-shaped cangue) and in headwear; cross-cultural substitution, mostly Qing court headdresses and modern hanfu, was less frequent. Two errors were caused by the English rendering of costume terms rather than by missing knowledge. I discuss what these results mean for costume designers who use T2I tools and propose the rule-based audit as a reusable check for culturally codified dress.

**Keywords:** generative AI; text-to-image; Peking opera costume; dress code; costume design; cultural fidelity

---

## 1. Introduction

Designers now use T2I systems at the start of a project to produce mood images, explore silhouettes and test colour schemes (Jin et al., 2024; Rizzi & Bertola, 2025). The same tools are offered to the public through chat apps, and their output already appears in posters, short videos and souvenir products that borrow from traditional theatre. For most fashion images, a plausible picture is good enough at the ideation stage. Traditional theatre costume is different, because plausibility and correctness part ways.

Peking opera (京剧) dresses its characters according to a system that performers and wardrobe masters treat as binding. Garments fall into five classes, *mang* (蟒), *pei* (帔), *kao* (靠), *xue* (褶) and *yi* (衣) (Han, 2019a). Colour follows a ranked "upper five" and "lower five" scheme, and a role's colour signals status and character (Cui et al., 2020). Bao Zheng wears a black python robe and a minister's hat with horizontal wings; Guan Yu wears green and a red face; a condemned woman wears red (Han, 2019a; Cui et al., 2020). Audiences who know the form read these signs at a glance, and a wrong sign changes who the character is. The wardrobe trade sums this up in the saying 宁穿破，不穿错: better a torn costume than the wrong one.

Studies of AI and Chinese opera costume have so far focused on what the technology can produce: recognition of costume types (Liu et al., 2023), lightweight feature recognition for Tibetan opera (npj Heritage Science, 2025), VR-based teaching (Scientific Reports, 2025), digital restoration (Liu et al., 2022) and, more recently, AIGC design workflows (易慎, 2025). Work on AIGC with traditional patterns usually ends with a consumer or expert preference rating (孙雨蓝等, 2024; 刘士瑾, 2025). None of these studies asks whether the generated costumes obey the rules of the form. Benchmarks for multimodal models on cultural heritage have grown quickly (e.g. TimeTravel, 2025), but they test recognition and question answering, not whether a generator respects a dress code when it produces an image.

This study fills that gap with a rule-based audit. I ask three questions:

- **RQ1.** How often do consumer-facing T2I systems violate the Peking opera dress code when asked for a named role?
- **RQ2.** Which rule dimensions (garment type, colour, motif, headwear, accessories and role markers, cross-cultural substitution) fail most often, and for which roles?
- **RQ3.** Does stating the dress code explicitly in the prompt reduce violations, and does the effect differ across systems?

The answers matter to costume and fashion designers in a practical way. If explicit prompts largely fix the problem, the burden falls on the designer's knowledge of the form. If they do not, T2I output needs expert review before it reaches a stage or a product.

## 2. Background

### 2.1 The dress code of Peking opera costume

[To be expanded with the full texts of Han (2019a, 2019b) and Cui et al. (2020); page numbers for Cui et al. to be checked rule by rule.]

- Five garment classes and their uses (Han, 2019a, p. 53).
- The python robe: four-clawed *mang* versus five-clawed dragon; round dragons, travelling dragons, sea-wave hems; the female *mang* reaches the knee and is worn with a cloud collar, jade belt and skirt (Han, 2019a, pp. 54–57).
- Colour ranking: upper five (yellow, red, green, white, black) and lower five (purple, pink, blue, lake blue, incense); bright and apricot yellow reserved for the imperial household (Han, 2019a, p. 57; Han, 2019b, p. 57).
- Historical formation of the colour rules and the roles that fix them: Guan Yu's green, white for young upright heroes such as Zhao Yun, red for the condemned (Cui et al., 2020).
- The wardrobe system (衣箱制) and its transmission (孙小杰, 2019; 曹林, 2021).

### 2.2 Generative AI in fashion and costume design

- Designer–AI collaboration in ideation: Jin et al. (2024); Rizzi & Bertola (2025); Hreščak & Broad (2025).
- Education: Lee (2025, *Research Journal of Textile and Apparel*).
- Consumer response to AI-designed apparel: Lee & Kim (JRCS) [verify year/volume]; Song & Kim (2025, *International Journal of Costume and Fashion*).
- Chinese-language AIGC design studies with traditional patterns (孙雨蓝等, 2024; 刘士瑾, 2025; 杨明 & 陈敬玉, 2026; 杨方超, online first).

### 2.3 Cultural accuracy of text-to-image systems

[To be written after a targeted search; candidate sources: Bianchi et al. (2023, FAccT) on stereotype amplification; Basu et al. (2023, ICCV) on geographical representativeness; Ventura et al. (2023, arXiv) on cultural viewpoint of T2I models; the Hanbok position paper (ICCVW 2025). All to be verified before citation.]

## 3. Method

### 3.1 Design

I used a 3 (system) × 2 (prompt strategy) × 8 (role) design with three images per cell, giving 144 images. The unit of analysis is a coded rule item within an image (up to six per image).

### 3.2 Roles

I selected eight roles that cover the main role types (行当) and whose costumes are fixed by long stage practice (Table 1). Each role is tied to a named play so that the costume is not left to the system's choice of scene.

**Table 1.** Roles and the dress-code elements checked.

| ID | Role (play) | Role type | Main garment | Colour rule coded | Headwear | Key accessories / markers |
|---|---|---|---|---|---|---|
| R1 | Zhuge Liang (*Kongcheng Ji*) | laosheng | bagua robe | not coded | bagua scarf hat | feather fan; three-part beard |
| R2 | Guan Yu (*Dandao Hui*) | hongsheng | green *mang* (or green *kao*) | green | *fuzi* helmet | jade belt; red face; long beard |
| R3 | Yang Yuhuan (*Guifei Zui Jiu*) | huashan | female *mang* with phoenix | not coded | phoenix crown | cloud collar; jade belt; water sleeves |
| R4 | Mu Guiying (*Mu Guiying Gua Shuai*) | daomadan | female *kao* | not coded | headdress with *lingzi* | four back flags |
| R5 | Bao Zheng (*Zha Mei An*) | tongchui hualian | black *mang* | black | *xiangdiao* | jade belt; black face with white crescent; full beard |
| R6 | Zhao Yun (*Changban Po*) | wusheng | white *kao* | white | warrior helmet | back flags; spear; no beard |
| R7 | Su San (*Qi Jie*) | qingyi | red prisoner's jacket and skirt | red | head wrap, no crown | fish-shaped cangue; water sleeves |
| R8 | Jiang Gan (*Qunying Hui*) | wenchou | *xuezi* | not coded | *fangjin* | tofu-block clown patch |

Colour was coded only for the four roles whose colour is fixed in the sources (Section 2.1). For the other four, colour was coded as a violation only when it broke a status rule, such as imperial yellow on a commoner.

### 3.3 Prompts

Both strategies used English prompts with a fixed frame: one performer, full body, front view, plain light grey background, photographic realism. P1 named the role, play and role type. P2 added one sentence that stated the role's dress code (garment, colour where fixed, headwear, accessories, face and beard). The full prompt text is given in Appendix A. The same sixteen prompts were entered in all three systems.

### 3.4 Systems and generation

I generated the images on 21 October 2026 through three consumer-facing channels: Doubao (ByteDance), Meta AI and Tencent WorkBuddy. WorkBuddy routes image requests to Hunyuan Image Alpha (`hunyuan-image-alpha`); its request log recorded this model identifier for every call. Doubao and Meta AI did not display a model version. Each prompt was entered in a new conversation with default settings and a 1:1 aspect ratio, and the first three images returned were kept without selection. Generation failures and anomalies were logged (Appendix B). Because all three channels are chat products, they may rewrite prompts internally. The audit therefore evaluates the generation channels that designers actually use, not the underlying models in isolation.

Native output sizes differed (1024 to 2240 px). Before coding, every image was resized to 768 px on the long side so that visible detail was the same across systems. Meta AI returned portrait images; these were padded with grey to a square without cropping the figure.

### 3.5 Codebook and coding

The codebook (Appendix C) scores six dimensions per image: D1 garment type, D2 colour rule, D3 motif, D4 headwear, D5 accessories and role markers, and D6 cross-cultural substitution (elements from Qing court dress, modern hanfu, Japanese, Korean or Western costume). Each dimension was coded 0 (compliant), 1 (violation) or NA (not applicable or not visible). Rules were taken from Han (2019a, 2019b) and Cui et al. (2020).

Images were shuffled and arranged in 48 contact sheets of three images, labelled only with a random sheet number and the role. Model and prompt strategy were hidden. Blinding was incomplete for one system, whose images carry a visible platform watermark.

Two coders scored all images. Coder A is the author, who trained in costume design. Coder B was a multimodal language model (Claude) applying the same codebook to the same sheets. I report agreement as Cohen's κ per dimension and resolved disagreements by referring back to the sources; coder A's judgement was final where the sources did not settle the case. [Agreement statistics pending.]

### 3.6 Analysis

I estimated the probability of a violation at the item level with a logistic model fitted by generalised estimating equations (Liang & Zeger, 1986), with an exchangeable working correlation clustered on image. Predictors were prompt strategy, system, their interaction, dimension and role. I report odds ratios with 95% confidence intervals. As a robustness check I refit the model without the image that reproduced a third-party stock-photo watermark.

## 4. Results [B-only, provisional]

### 4.1 Overall compliance (RQ1)

**Table 2.** Share of coded items in violation, and share of images with no violation.

| System | P1 violation rate | P2 violation rate | P1 fully compliant | P2 fully compliant |
|---|---|---|---|---|
| Hunyuan Image Alpha (WorkBuddy) | 80.5% | 25.0% | 0% | 29% |
| Doubao | 50.8% | 10.4% | 8% | 67% |
| Meta AI | 32.6% | 6.7% | 8% | 83% |

### 4.2 Where the rules fail (RQ2)

Under P1, violations were most frequent for accessories and role markers (83%), headwear (69%) and garment type (60%), and least frequent for cross-cultural substitution (14%). By role, Su San (80%), Yang Yuhuan (71%) and Jiang Gan (67%) fared worst.

Typical errors:
- Zhuge Liang shown in a python robe and minister's hat, without the feather fan.
- Su San rendered as a richly dressed lady in a headdress, with no cangue.
- Jiang Gan, a clown, rendered as an official with a beard and dragon robe.
- Qing court headdresses (两把头, 大拉翅) placed on Su San, Yang Yuhuan and Mu Guiying.

### 4.3 Effect of stating the rules (RQ3)

Stating the dress code reduced the odds of a violation (OR = 0.041, 95% CI 0.022–0.077, p < .001). Relative to Hunyuan Image Alpha, the odds were lower for Doubao (OR = 0.18) and Meta AI (OR = 0.055). The strategy × system interaction was not significant. [Re-estimate after reconciliation.]

### 4.4 Errors introduced by the prompt itself

Two P2 errors came from the English wording, not from missing knowledge. "Scholar's pleated robe (xuezi)" produced garments with literal knife pleats (Meta AI). "Fish-shaped wooden cangue" produced a rectangular board carved with a fish (Doubao). Both show that a costume term translated into English can mislead a model that would otherwise follow the instruction.

### 4.5 Other anomalies

- One image reproduced a third-party stock-photo watermark (`www.yanqin.net`).
- Two Meta AI images showed a figure seen from behind with a painted face on the back of the head.
- One Hunyuan image placed a second performer and a plastic stool in the frame despite the one-performer instruction.

## 5. Discussion

[Draft after reconciliation. Points to develop:]

1. Without explicit rules, the systems draw on a generic "Chinese opera" look: python robes, sea-wave hems, phoenix crowns and pompom helmets appear regardless of role. The model knows the inventory of the wardrobe but not who may wear what.
2. Explicit rules help a great deal but do not close the gap, and the gap differs by system. Accurate output depends on the designer's own knowledge of the form, which is the knowledge T2I use is often assumed to replace.
3. Role markers (beards, flags, cangue, clown patch) fail most because they are small and specific to one role.
4. Translation is a source of error in its own right. Costume terms need a description of form, not a literal gloss.
5. Practical guidance for costume designers and for cultural product teams.
6. Limitations: three systems on one date; three images per cell; channel-level prompt rewriting; incomplete blinding; a model as second coder; eight roles from one genre.

## 6. Conclusion

[To be written last.]

---

## Declarations (draft)

**Use of generative AI.** In line with Taylor & Francis policy, the following statement will appear in the Methods or Acknowledgements: *"I used Claude (Anthropic) to assist with drafting and language editing of the manuscript, writing analysis code, and as the second coder described in Section 3.5. I reviewed and revised all text and analyses and take full responsibility for the content."* [Wording to be finalised by the author.]

**Ethics.** The study involved no human participants.

**Data availability.** Codebook, prompts, codes and analysis script will be deposited in a public repository. Generated images will be shared subject to each platform's terms.

---

## References (verification status in brackets)

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46. [standard]
- Cui, W., Qiang, K., & Wang, X. (2020). 传统京剧戏衣“上下五色”穿戴规制形成与特点探析. *中国艺术*, (3), 64–73. [full text read]
- Han, B. (2019a). 美如锦绣——京剧服装之蟒. *中国京剧*, (6), 53–57. [full text read]
- Han, B. (2019b). 美如锦绣——京剧服装之帔. *中国京剧*, (7), 54–59. [full text read]
- Hreščak, & Broad, T. (2025). Co-designing fashion with AI: A small-data approach to generative garment design. *ICCC 2025*. [verify authors' initials]
- Jin, Yoon, Self, & Lee (2024). *Archives of Design Research*. [verify title, volume, pages]
- Lee & Kim. Human vs. AI: The battle for authenticity in fashion design and consumer response. *Journal of Retailing and Consumer Services*. [verify year, volume]
- Liang, K.-Y., & Zeger, S. L. (1986). Longitudinal data analysis using generalized linear models. *Biometrika*, 73(1), 13–22. [standard]
- Liu, Lin, & Zhu (2023). Research on Chinese traditional opera costume recognition based on improved YOLOv5. *Heritage Science*. https://doi.org/10.1186/s40494-023-00883-x [verify volume]
- Liu, Gao, Zhang, & Zhu (2022). Study on digital protection and innovative design of Qin opera costumes. *Heritage Science*. https://doi.org/10.1186/s40494-022-00762-x [verify volume]
- Rizzi, & Bertola (2025). *European Journal of Cultural Management and Policy*. https://doi.org/10.3389/ejcmp.2025.13875 [verify title]
- Song & Kim (2025). Generative AI in fashion product design. *International Journal of Costume and Fashion*, 25(2). [verify pages]
- 易慎 (2025). 传统戏曲服饰AIGC智能设计范式的构建——以益阳花鼓戏的虚实融合应用为例. *轻纺工业与技术*, 54(4). [CNKI record]
- 孙雨蓝, 迟诚, 刘换洁 (2024). 基于AIGC技术的土家织锦纹样创新设计研究. *东华大学学报(社会科学版)*, 24(4). [CNKI record]
- 刘士瑾 (2025). 基于条件扩散模型的良渚纹样在国潮服装设计中的应用研究与评价. *设计*, 38(9). [CNKI record]
- [Remaining references to be added and verified.]

---

## Appendix A. Prompts
See `prompt_sheet.md`.

## Appendix B. Generation log and anomalies
See `provenance.md` and the platform logs.

## Appendix C. Codebook
See `codebook_v0.md` (v0.2).

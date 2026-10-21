# Better torn than wrong: an audit of dress-code violations in AI-generated Peking opera costumes

**Draft v1, 2026-10-21.** All results use the consensus codes from two coders (author and model coder) after adjudication. Target journal: *The Journal of the Textile Institute*. Author-guideline check is pending (word limit, reference style, figure format).

---

## Abstract

Text-to-image (T2I) systems are already used to sketch stage costumes and cultural merchandise. Traditional theatre costume, however, follows codified rules that a general image model has no particular reason to respect. Peking opera is a clear case. The trade saying "better to wear a torn costume than the wrong one" (宁穿破，不穿错) refers to a dress code that fixes each role's garment type, colour, motif, headwear and accessories.

I audited three consumer-facing T2I channels: Hunyuan Image Alpha (through Tencent WorkBuddy), Doubao and Meta AI. They were tested on eight canonical roles under two prompts. The first named the role only. The second also stated the role's dress code. The 144 images were blind-coded on six rule dimensions with a codebook drawn from published studies of Peking opera wardrobe practice. Inter-coder agreement was κ = 0.70.

When prompted with the role name only, the systems violated the dress code on 19.8% to 75.9% of codable items. Between 0% and 46% of their images were fully compliant. Stating the rules in the prompt reduced the odds of a violation by 93% (OR = 0.066, 95% CI 0.038–0.116). Compliance still differed sharply between systems, and the system ranking was the same under both prompts. Headwear and role-specific markers failed most often. Cross-cultural substitution, mostly Qing court headdresses and modern hanfu, was the least frequent error. Two errors arose from the English rendering of costume terms.

The results show that correct output depends on the designer's own knowledge of the form. The rule-based audit offers a reusable check for any culturally codified dress.

**Keywords:** generative AI; text-to-image; Peking opera; theatre costume; dress code; costume design

---

## 1. Introduction

Fashion and costume designers now use T2I systems at the start of a project. They use them to generate mood images, try out silhouettes and test colour schemes (Jin et al., 2024; Rizzi & Bertola, 2025). The same systems are offered to the public through chat apps. Their output already appears in posters, short videos and souvenir products that borrow from traditional theatre. For most fashion imagery, a plausible picture is good enough at the ideation stage. In traditional theatre costume, a plausible picture can still be wrong.

Peking opera (京剧) dresses each character according to a system that performers and wardrobe masters treat as binding.

- **Garment classes.** Costumes fall into five classes: the python robe (*mang* 蟒), the formal coat (*pei* 帔), stage armour (*kao* 靠), the informal robe (*xuezi* 褶子) and a residual class of other garments (*yi* 衣) (Han, 2019a).
- **Colour ranking.** Colour follows a ranked scheme of "upper five" and "lower five" colours, and a role's colour tells the audience its status and character (Cui et al., 2020).
- **Example roles.** Bao Zheng wears a black python robe. Guan Yu wears green and a red face. A condemned woman wears red (Han, 2019a; Cui et al., 2020).

An informed audience reads these signs at a glance. A wrong sign changes who the character appears to be.

Research on AI and Chinese opera costume has so far asked what the technology can do:

- recognise costume types (Liu et al., 2023);
- restore historical costumes in 3D (Liu et al., 2022);
- support new AIGC design workflows (易慎, 2025).

Chinese-language studies that combine AIGC with traditional patterns usually end with a consumer or expert preference rating (孙雨蓝 et al., 2024; 刘士瑾, 2025). Studies of cultural bias in T2I systems ask whether outputs are representative or stereotyped (Basu et al., 2023; Bianchi et al., 2023; Ventura et al., 2025). They do not test outputs against an explicit rule system. To my knowledge, no study has checked whether generated theatre costumes obey the dress code of the form they imitate.

This study is a rule-based audit. It asks three questions:

- **RQ1.** How often do consumer-facing T2I systems violate the Peking opera dress code when asked for a named role?
- **RQ2.** Which rule dimensions fail most often, and for which roles?
- **RQ3.** Does stating the dress code in the prompt reduce violations, and does the effect differ across systems?

The answers matter to costume designers in a practical way. If explicit prompts fix most errors, the burden of accuracy falls on the designer's knowledge of the form. If they do not, T2I output needs review by a specialist before it reaches a stage or a product.

## 2. Background

### 2.1 The dress code of Peking opera costume

Peking opera inherited its wardrobe practice from Kunqu and earlier regional theatre. By the early Republican period it had settled into a system that the trade could state as rules (Cui et al., 2020).

**The five garment classes.** Han (2019a, p. 53) groups the wardrobe into five classes: *mang*, *pei*, *kao*, *xue* and *yi*. Within each class, colour, motif, workmanship and the way the garment is worn set one style apart from another.

**The python robe.** The python robe is the highest-ranking garment. It derives from the Ming court robe that emperors bestowed on princes, consorts and meritorious officials. It differs from the emperor's dragon robe in one detail: the python has four claws, the dragon five (Han, 2019a, p. 53). The robe is decorated with round or travelling dragons, auspicious emblems and a sea-wave hem (*haishui jiangya* 海水江崖). The female python robe is shorter and reaches only to the knee. It has no rear vents and is worn with a cloud collar, a jade belt and an under-skirt (Han, 2019a, p. 54).

**Colour.** Colour is ranked. The "upper five" are yellow, red, green, white and black; the "lower five" are purple, pink, blue, lake blue and incense (Han, 2019a, p. 57; Cui et al., 2020). Characters in the upper five rank higher than those in the lower five. Bright and apricot yellow are reserved for the imperial household (Han, 2019a, p. 57; Han, 2019b, p. 57).

**Colours tied to particular roles.** Some colours belong to particular characters or character types, and these links are what make the code legible on stage:

- Guan Yu wears a green python robe with gold travelling dragons in *Dandao Hui* (Han, 2019a, p. 57). Green entered the upper five through popular devotion to Guan Yu (Cui et al., 2020).
- Bao Zheng wears a black python robe with the character *fu* and travelling dragons in *Zha Mei An* (Han, 2019a, p. 57).
- White marks young, upright heroes such as Zhao Yun (Cui et al., 2020).
- Red is worn by prisoners on the way to execution (Cui et al., 2020).

**Transmission.** Wardrobe masters keep these rules through the costume-trunk system (衣箱制) and pass them on by apprenticeship (孙小杰, 2019). The saying 宁穿破，不穿错 records how seriously the trade takes them.

### 2.2 Generative AI in fashion and costume design

Studies of designers who use generative tools report quick visual stimulation in the early stages of a project. They also report recurring problems: misread intentions and a drift toward mainstream styles.

- Jin et al. (2024) observed 19 design students and professionals using Bing, Midjourney and DALL·E for concept ideation and revision.
- Rizzi and Bertola (2025) mapped how master's students divided a design brief between themselves and generative tools.
- Hrešć and Broad (2025) fine-tuned a diffusion model on a single designer's sketches to keep the output close to her own language.

Consumer studies show that disclosed AI authorship can lower perceived authenticity and expected quality (Lee & Kim, 2024). Chinese-language studies have applied AIGC to traditional patterns such as Tujia brocade and Liangzhu motifs, then evaluated the outputs with users or experts (孙雨蓝 et al., 2024; 刘士瑾, 2025). For opera costume specifically, 易慎 (2025) proposed an AIGC design paradigm for Huagu opera. Across this literature, quality is judged by preference, creativity or perceived authenticity. None of these studies measures conformity to an external rule system.

### 2.3 Cultural accuracy of text-to-image systems

Audits of T2I systems have documented two main problems:

- **Stereotyping.** Bianchi et al. (2023) showed that ordinary prompts produce stereotyped images even when they mention no demographic terms.
- **Narrow geographic defaults.** Basu et al. (2023) found that underspecified prompts default to a narrow set of countries. Adding a country name helped, but unevenly.

Ventura et al. (2025) examined how T2I models encode culture across dimensions, domains and concepts. They argue that the multilingual text encoder shapes a model's cultural point of view.

These studies treat cultural accuracy as representativeness or stereotype. Theatre costume adds a stricter test. A codified dress system defines right and wrong answers in advance, so an output can be checked against written rules rather than against a panel's sense of what looks typical.

## 3. Method

### 3.1 Design

I used a 3 (system) × 2 (prompt) × 8 (role) design with three images per cell, for 144 images in total. The unit of analysis is a coded rule item within an image, with up to six items per image.

### 3.2 Roles

I selected eight roles that cover the main role types (行当) and whose costumes are fixed by long stage practice (Table 1). Each role is tied to a named play so that the system cannot fall back on a scene of its own choosing.

**Table 1.** Roles and the dress-code elements checked.

| ID | Role (play) | Role type | Main garment | Colour coded | Headwear | Markers and accessories |
|---|---|---|---|---|---|---|
| R1 | Zhuge Liang (*Kongcheng Ji*) | laosheng | bagua robe | — | bagua scarf hat | feather fan; three-part beard |
| R2 | Guan Yu (*Dandao Hui*) | hongsheng | green *mang* or green *kao* | green | *fuzi* helmet, no pheasant plumes | jade belt; red face; long beard |
| R3 | Yang Yuhuan (*Guifei Zui Jiu*) | huashan | female *mang* with phoenixes | — | phoenix crown | cloud collar; jade belt; water sleeves |
| R4 | Mu Guiying (*Mu Guiying Gua Shuai*) | daomadan | female *kao* | — | headdress with two pheasant plumes | four back flags |
| R5 | Bao Zheng (*Zha Mei An*) | tongchui hualian | black *mang* | black | minister's hat with horizontal wings | jade belt; black face with white crescent; full beard |
| R6 | Zhao Yun (*Changban Po*) | wusheng | white *kao* | white | warrior helmet | back flags; spear; no beard |
| R7 | Su San (*Qi Jie*) | qingyi | red prisoner's jacket and skirt | red | head wrap, no crown | fish-shaped cangue; water sleeves |
| R8 | Jiang Gan (*Qunying Hui*) | wenchou | *xuezi* | — | scholar's square cap | white clown patch on the nose |

Colour was coded only for the four roles whose colour the sources fix. For the other four, colour counted as a violation only when it broke a status rule, such as imperial yellow on a commoner.

### 3.3 Prompts

Both prompt conditions used English and the same frame: one performer, full body, front view, plain light grey background, photographic realism.

- **P1** named the role, the play and the role type.
- **P2** added one sentence stating the role's dress code: garment, colour where fixed, headwear, accessories, face and beard.

The sixteen prompts (Appendix A) were entered unchanged in all three systems.

### 3.4 Systems and generation

All images were generated on 21 October 2026 through three consumer-facing channels: Tencent WorkBuddy, Doubao (ByteDance) and Meta AI.

- WorkBuddy sends image requests to Hunyuan Image Alpha (`hunyuan-image-alpha`). Its request log recorded this identifier for all 51 calls, including retries.
- Doubao and Meta AI did not display a model version.

Generation procedure:

- Each prompt was entered in a new conversation with default settings and a 1:1 aspect ratio.
- The first three images returned were kept, without selection.
- Failures and anomalies were logged (Appendix B). Meta AI returned one internal server error, and the retry succeeded. In WorkBuddy, two parallel calls overwrote each other's files, so one image was regenerated.

All three channels are chat products and may rewrite prompts internally. The audit therefore evaluates the generation channels that designers actually use, not the underlying models in isolation.

Native output sizes ranged from 1024 to 2240 pixels. To keep visible detail equal across systems, every image was resized to 768 pixels on the long side before coding. Meta AI returned portrait images, which were padded with grey to a square without cropping the figure.

### 3.5 Codebook and coding

The codebook (Appendix C) scores six dimensions per image:

- **D1** garment type
- **D2** colour rule
- **D3** motif
- **D4** headwear
- **D5** markers and accessories
- **D6** cross-cultural substitution: elements from Qing court dress, modern hanfu, Japanese, Korean or Western costume

Each dimension was coded 0 (compliant), 1 (violation) or NA (not applicable or not visible). The rules come from Han (2019a, 2019b) and Cui et al. (2020). A difference in proportion or detail within the correct garment class was not counted as a D1 violation.

**Blinding.** The images were shuffled and arranged in 48 contact sheets of three. Each sheet was labelled only with a random number and the role, so system and prompt condition were hidden. Blinding was incomplete for Hunyuan Image Alpha, whose images carry a visible platform watermark.

**Coders.** Two coders scored all 144 images independently.

- Coder A is the author, who trained in costume design.
- Coder B was a multimodal language model (Claude, Anthropic). It applied the same codebook to the same sheets.

**Agreement and adjudication.**

- I report agreement as Cohen's κ (Cohen, 1960), per dimension and pooled.
- Disagreements were resolved by two rules, and every decision is logged (Appendix D).
- Where the codebook states an explicit rule that settles the case, the rule decided. This applied to 9 of 132 discordant items.
- Where the disagreement was a matter of visual judgement, for example whether a garment reads as a female python robe or whether a crescent is visible, the human coder's judgement was kept.

### 3.6 Analysis

**Model.** I modelled the probability of a violation at the item level. The model was a logistic regression estimated by generalised estimating equations (Liang & Zeger, 1986), with an exchangeable working correlation clustered on image.

**Predictors.** Prompt condition, system, dimension and role entered as main effects. A second model added the prompt × system interaction. I report odds ratios with 95% confidence intervals.

**Sensitivity check.** I refitted the model without the one image that reproduced a third-party stock-photo watermark.

## 4. Results

### 4.1 Coder agreement

Pooled agreement was 84.7%, κ = 0.70 (Table 2). Agreement was highest for colour (κ = 0.92), where the rule is unambiguous. It was moderate for markers and accessories (κ = 0.45): coder B applied the accessory list more strictly, for instance counting a glaive carried in place of a spear as a violation. It was lowest for cross-cultural substitution (κ = 0.24). This dimension has a low base rate, which depresses κ, and the coders differed over borderline modern-hanfu and Japanese-style elements.

**Table 2.** Inter-coder agreement before adjudication.

| Dimension | Agreement | Cohen's κ |
|---|---|---|
| D1 Garment type | 86.1% | 0.68 |
| D2 Colour | 95.1% | 0.92 |
| D3 Motif | 84.7% | 0.64 |
| D4 Headwear | 83.3% | 0.66 |
| D5 Markers and accessories | 71.5% | 0.45 |
| D6 Cross-cultural substitution | 87.5% | 0.24 |
| Pooled | 84.7% | 0.70 |

### 4.2 Overall compliance (RQ1)

With the role name only (P1), violations were common in all three systems (Table 3). Hunyuan Image Alpha violated the code on three of every four codable items and produced no fully compliant image. Meta AI did best, and nearly half of its P1 images were fully compliant.

**Table 3.** Violation rate (share of codable items) and share of fully compliant images.

| System | Violation rate, P1 | Violation rate, P2 | Fully compliant images, P1 | Fully compliant images, P2 |
|---|---|---|---|---|
| Hunyuan Image Alpha | 75.9% | 26.0% | 0.0% | 33.3% |
| Doubao | 37.1% | 7.6% | 12.5% | 58.3% |
| Meta AI | 19.8% | 3.0% | 45.8% | 83.3% |

### 4.3 Where the rules fail (RQ2)

**By dimension.** Under P1 the most frequent violations were headwear (56.9%), markers and accessories (57.7%) and colour (54.1%, four roles only). Garment type (47.2%) and motif (41.7%) followed. Cross-cultural substitution was rare (13.9%).

The adjusted model ranks the dimensions after controlling for system, prompt and role. Headwear (OR = 2.67, 95% CI 1.51–4.70) and markers and accessories (OR = 2.12, 1.20–3.76) were more likely to fail than garment type. Cross-cultural substitution was much less likely to fail (OR = 0.12, 0.05–0.28).

**By role.** Su San (70.4% of P1 items), Jiang Gan (67.4%) and Zhuge Liang (55.6%) fared worst. Yang Yuhuan fared best (22.2%). The P1 errors followed recognisable patterns:

- Zhuge Liang appeared in a python robe and a minister's hat, without a feather fan.
- Su San appeared as a richly dressed lady in a jewelled headdress, with no cangue.
- Jiang Gan, a clown role, appeared as a bearded official in a dragon robe.
- Mu Guiying, Su San and Yang Yuhuan were sometimes given Qing court headdresses (两把头, 大拉翅).

### 4.4 Effect of stating the rules (RQ3)

Stating the dress code in the prompt lowered violations in every system (Table 3). In the main-effects model, P2 reduced the odds of a violation to 0.066 of their P1 level (95% CI 0.038–0.116, p < .001).

System differences remained large. With Hunyuan Image Alpha as the reference:

- Doubao: OR = 0.13 (0.08–0.20)
- Meta AI: OR = 0.04 (0.02–0.08)

The prompt × system interaction was not significant (p = .18 and p = .26), so the proportional benefit of P2 was similar across systems. Because the systems started from very different baselines, the absolute gains differed. Even with explicit rules, two thirds of the P2 images from Hunyuan Image Alpha still broke at least one rule.

Removing the watermarked image left every estimate unchanged to two decimals.

### 4.5 Errors introduced by the prompt itself

Two P2 errors came from the English wording rather than from missing knowledge.

- "Scholar's pleated robe (xuezi)" produced robes with literal knife pleats in Meta AI. Meta AI also once supplied a cap resembling an academic mortarboard.
- "Fish-shaped wooden cangue" produced, in Doubao, a rectangular board carved with a fish.

In both cases the system followed the words of the instruction. It did not follow what the words refer to.

### 4.6 Other anomalies

Three further anomalies are worth reporting:

- One Hunyuan Image Alpha image reproduced the watermark of a Chinese stock-photo site (`www.yanqin.net`). This suggests the training data included such images.
- Two Meta AI images of Bao Zheng showed the figure from behind, with a painted face on the back of the head.
- One Hunyuan Image Alpha image placed a second performer and a plastic stool in the frame, despite the one-performer instruction.

## 5. Discussion

### 5.1 The systems know the wardrobe but not the casting

Without explicit rules, all three systems drew on a generic image of "Chinese opera costume". Python robes, sea-wave hems, phoenix crowns and pompom helmets appeared across roles. The systems reproduced the inventory of the costume trunk, but not the rules that decide who may wear what.

This explains the role pattern. Roles whose costume matches the generic image did comparatively well: the consort Yang Yuhuan in a phoenix robe, and the official Bao Zheng in a black python robe. Roles whose costume departs from the generic image did badly. These were a prisoner in plain red, a clown in an informal robe, and a strategist in a Daoist robe. The same pattern appears in audits of other domains, where underspecified prompts fall back on a dominant default (Basu et al., 2023; Bianchi et al., 2023). Here the default is internal to one culture: the court-robe image displaces the rest of the wardrobe.

### 5.2 Stating the rules helps, but the designer must already know them

Stating the dress code in the prompt was by far the strongest lever in the study. It cut the odds of a violation by more than an order of magnitude. That finding has a catch. To write the P2 prompts I had to know that Zhuge Liang wears a bagua robe, that Su San wears a fish-shaped cangue and that Jiang Gan needs a clown patch. The knowledge that makes T2I output correct is the knowledge a non-specialist user lacks.

For costume and cultural-product design, this places the designer's expertise at the start of the process, in the prompt, as well as at the end, in review. It also qualifies the claim that generative tools democratise design. They lower the cost of producing images, but not the cost of knowing what a correct image is.

Even with explicit rules, compliance depended heavily on the system. Two of three Hunyuan Image Alpha images still broke at least one rule, against one in six for Meta AI. The choice of tool is therefore part of a designer's professional judgement.

### 5.3 Small markers carry the most meaning and fail most often

Headwear and role markers failed more often than garment class. The items involved are small: a feather fan, a white crescent on a black face, back flags, a cangue, a clown patch. Yet they carry much of the meaning. A white crescent identifies Bao Zheng. A fish-shaped cangue identifies a condemned woman on the road. A clown patch tells the audience how to read Jiang Gan before he speaks. A system that gets the robe right and the marker wrong produces a costume that looks correct to a general viewer but misidentifies the character to an informed one. That is the kind of error the trade saying warns against.

### 5.4 Translation is a source of error

The pleated *xuezi* and the carved-board cangue show that the wording of a costume term can mislead a system that otherwise follows instructions. *Xuezi* (褶子) is the name of a garment, not a description of its surface. Glossing it as "pleated robe" invited a literal reading. Ventura et al. (2025) argue that the text encoder shapes a model's cultural point of view. These two cases show the same effect at the level of a single term.

Two practical rules follow for anyone writing prompts for codified dress:

- Describe the form of the garment, not a literal translation of its name.
- Check how the system reads each technical term before relying on it.

### 5.5 Implications for practice

For costume designers and cultural-product teams, the results suggest three working rules:

1. Treat T2I output of traditional theatre costume as a draft that needs review by someone who knows the form.
2. Put the dress code into the prompt in descriptive terms, role by role.
3. Test the chosen system against a short rule checklist before using it in production.

The codebook used here can serve as such a checklist for Peking opera. The same method extends to any dress system with written rules, such as court dress, ritual vestments or military uniform.

### 5.6 Limitations

The study has six main limitations:

- **Sample.** It covers three systems on one date, with three images per cell. Generative systems change quickly, so the results describe these channels at this time.
- **Hidden rewriting.** The channels may rewrite prompts internally, and I could not observe this.
- **Blinding.** Blinding was incomplete for one system because of its watermark.
- **Second coder.** The second coder was a language model rather than a second human expert. Its stricter reading of the accessory list lowered agreement on D5, and that dimension should be read with this in mind.
- **Scope.** The eight roles come from one genre. Other regional forms have their own codes.
- **Language.** I used English prompts only. Chinese prompts would test whether the translation errors disappear, and that is a natural next step.

## 6. Conclusion

When asked for a named Peking opera role, current T2I systems often produce costumes that break the form's dress code. They fail most on headwear and on the small markers that identify a character. Stating the code in the prompt prevents most of these errors, but only for a user who already knows it, and the remaining error rate depends strongly on the system. For theatre costume, accuracy still comes from the designer's own knowledge of the form. A rule-based audit makes that dependence visible and gives designers a simple test to apply to any tool they adopt.

---

## Declarations

**Use of generative AI.** I used Claude (Anthropic) to assist with literature searching, drafting and language editing of the manuscript, and writing the analysis code. It also served as the second coder described in Section 3.5. Images were generated with the three systems under study. I reviewed and revised all text, codes and analyses and take full responsibility for the content. [Final wording to be confirmed by the author against the journal's current policy.]

**Ethics.** The study involved no human participants.

**Funding.** None.

**Conflict of interest.** None.

**Data availability.** The codebook, prompts, both coders' codes, the adjudication log and the analysis script will be deposited in a public repository on acceptance. Generated images will be shared subject to each platform's terms of use.

---

## References

- Basu, A., Babu, R. V., & Pruthi, D. (2023). Inspecting the geographical representativeness of images from text-to-image models. In *Proceedings of the IEEE/CVF International Conference on Computer Vision* (pp. 5136–5147). https://doi.org/10.1109/ICCV51070.2023.00474
- Bianchi, F., Kalluri, P., Durmus, E., Ladhak, F., Cheng, M., Nozza, D., Hashimoto, T., Jurafsky, D., Zou, J., & Caliskan, A. (2023). Easily accessible text-to-image generation amplifies demographic stereotypes at large scale. In *Proceedings of the 2023 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1493–1504). https://doi.org/10.1145/3593013.3594095 [check full author list]
- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement, 20*(1), 37–46.
- Cui, W., Qiang, K., & Wang, X. (2020). 传统京剧戏衣"上下五色"穿戴规制形成与特点探析 [Formation and characteristics of the "upper and lower five colours" dress code of traditional Peking opera costume]. *中国艺术 [China Art]*, (3), 64–73.
- Han, B. (2019a). 美如锦绣——京剧服装之蟒 [Beautiful as brocade: the python robe in Peking opera costume]. *中国京剧 [Chinese Peking Opera]*, (6), 53–57.
- Han, B. (2019b). 美如锦绣——京剧服装之帔 [Beautiful as brocade: the *pei* in Peking opera costume]. *中国京剧 [Chinese Peking Opera]*, (7), 54–59.
- Hrešć, I., & Broad, T. (2025). Co-designing fashion with AI: A small-data approach to generative garment design. In *Proceedings of the 16th International Conference on Computational Creativity (ICCC'25)*. [check pages]
- Jin, Y., Yoon, J., Self, J. A., & Lee, K. (2024). Understanding fashion designers' behavior using generative AI for early-stage concept ideation and revision. *Archives of Design Research, 37*(3), 25–45. https://doi.org/10.15187/adr.2024.07.37.3.25
- Lee, G., & Kim, H.-Y. (2024). Human vs. AI: The battle for authenticity in fashion design and consumer response. *Journal of Retailing and Consumer Services, 77*, 103690. https://doi.org/10.1016/j.jretconser.2023.103690
- Liang, K.-Y., & Zeger, S. L. (1986). Longitudinal data analysis using generalized linear models. *Biometrika, 73*(1), 13–22.
- Liu, K., Gao, Y., Zhang, J., & Zhu, C. (2022). Study on digital protection and innovative design of Qin opera costumes. *Heritage Science, 10*, 1–15. https://doi.org/10.1186/s40494-022-00762-x
- Liu, K., Lin, K., & Zhu, C. (2023). Research on Chinese traditional opera costume recognition based on improved YOLOv5. *Heritage Science, 11*, 1–14. https://doi.org/10.1186/s40494-023-00883-x
- Rizzi, G., & Bertola, P. (2025). Exploring the generative AI potential in the fashion design process: An experimental experience on the collaboration between fashion design practitioners and generative AI tools. *European Journal of Cultural Management and Policy, 15*. https://doi.org/10.3389/ejcmp.2025.13875
- Ventura, M., Ben-David, E., Korhonen, A., & Reichart, R. (2025). Navigating cultural chasms: Exploring and unlocking the cultural POV of text-to-image models. *Transactions of the Association for Computational Linguistics, 13*, 142–166. https://doi.org/10.1162/tacl_a_00732
- 刘士瑾 (2025). 基于条件扩散模型的良渚纹样在国潮服装设计中的应用研究与评价 [Application and evaluation of Liangzhu patterns in Guochao fashion design based on a conditional diffusion model]. *设计 [Design]*, 38(9), 9–13.
- 孙小杰 (2019). 戏曲服装穿戴管理人才培养的现代学徒制方式 [A modern apprenticeship model for training opera costume wardrobe staff]. *戏曲艺术 [Journal of Traditional Chinese Theatre]*, 40(4). [pages from CNKI]
- 孙雨蓝, 迟诚, & 刘换洁 (2024). 基于AIGC技术的土家织锦纹样创新设计研究 [Innovative design of Tujia brocade patterns based on AIGC]. *东华大学学报(社会科学版) [Journal of Donghua University (Social Sciences)]*, 24(4), 93–103.
- 易慎 (2025). 传统戏曲服饰AIGC智能设计范式的构建——以益阳花鼓戏的虚实融合应用为例 [Building an AIGC design paradigm for traditional opera costume: the case of Yiyang Huagu opera]. *轻纺工业与技术 [Light and Textile Industry and Technology]*, 54(4), 119–122.

---

## Appendices
- A. Prompts (`prompt_sheet.md`)
- B. Generation log and anomalies (`provenance.md`)
- C. Codebook (`codebook_v0.md`, v0.2)
- D. Adjudication log (`data/adjudication_log.csv`)

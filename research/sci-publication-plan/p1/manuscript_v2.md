# Better torn than wrong: auditing generative AI images of Peking opera costume against the dress code

[Author name], Department of Performing Arts and Culture, The Catholic University of Korea, [address, e-mail, ORCID]

## Abstract

Peking opera costume is governed by a prescriptive dress code that assigns garment type, colour, pattern, headwear and emblematic props to each role, yet generative image models now produce such costumes without any audit against it. I generated 144 full-body images of eight canonical roles in three commercial channels (Doubao, Meta AI, Hunyuan Image Alpha) under two prompt designs: a minimal prompt naming only role and play, and a structured one specifying the codified attributes. Six dimensions were coded for each image, giving 791 analysable judgements (inter-coder κ = 0.70). Only 38.9% of images were fully compliant, with errors concentrated in headwear and small emblematic items. Specifying the code reduced the odds of violation to 6.6% of the minimal condition (OR 0.066, 95% CI 0.038–0.116, p < .001), with no channel-by-strategy interaction. The models reproduce the appearance of Peking opera costume but not the rules that assign it.

**Keywords:** Peking opera costume; dress code; generative AI; cultural accuracy; prompt design; content analysis

---

## 1 Introduction

Peking opera costume follows rules that the trade treats as binding. The saying "better to wear a torn costume than the wrong one" (宁穿破，不穿错) sums them up: a worn costume is acceptable, a costume that does not fit the role is not. The dress code encodes role type, status and situation in the form of the garment, its colour and motifs, the headwear and the accessories. Bao Zheng wears a black python robe, a minister's hat with horizontal wings and a white crescent on his forehead. Guan Yu wears a green python robe and a red face. Su San, on her way to trial as a prisoner, wears a red prisoner's jacket and skirt and a fish-shaped cangue. Each of these rules can be checked item by item, and the system as a whole has been documented in detail (Bonds, 2008).

Generative image models have entered this field over the past few years. Opera posters, cultural merchandise and draft stage costumes now often start from a prompt, and technical studies have followed, from diffusion generation constrained by a knowledge graph (Zhang et al., 2026a) to an animation system designed around the problem of "regulation distortion" (Zhang et al., 2026b). These studies ask whether a system can produce convincing images, and they judge the results by informal feedback, visual fidelity or user preference. Costume and apparel designers already use the same tools in early design work (Jin et al., 2024), and knowing which garment, colour and accessory belong to which wearer is part of the professional knowledge those tools are meant to support.

An image can be recognisable at a glance as a Peking opera figure and still put a python robe on the wrong character, leave Su San without her cangue or paint Bao Zheng's face on the back of his head. A layperson will rarely notice such errors; an expert notices them at once. Since most people who now use these tools are laypeople, the question of whether generative models belong in this workflow calls for a rule-by-rule check against the dress code.

This study is such an audit. I tested three generation channels: Doubao, Meta AI (Muse), and Tencent WorkBuddy, which calls Hunyuan Image Alpha. Each received two kinds of prompt, one naming only the role and the play and one that also stated the dress code, for eight canonical roles, with three images per cell. The 144 images were coded on six dimensions and analysed with the image–dimension pair as the unit of observation. I asked how often the dress code is violated when it is not stated (RQ1), in which dimensions and roles the errors concentrate (RQ2), and whether stating the code reduces violations equally across channels (RQ3). The study offers a six-dimension codebook that others can reuse, a description of where the errors fall, and an estimate of how much an explicit dress code in the prompt helps. All three channels are conversational products that may rewrite prompts internally, so the findings describe the channels designers actually use rather than the underlying models.

### 1.1 The dress code of Peking opera costume

The wardrobe is kept in trunks by function. The main costume trunk, the second and third costume trunks, the helmet trunk and the trunk for flags and weapons each hold their own items, so that costume, headwear and props are issued together; monographs on the wardrobe follow the same division (Liu, Y., 2002). The practice goes back to the *chuanguan* (穿关), the costume notes attached to each character in Ming court performances, and its terminology passed through *xingtou* (行头), *xiyi* (戏衣) and the costume lists called *chuandai tigang* (穿戴题纲) before settling into its present form (Liu, C. & Xu, 2021). What came out of this history is a set of rules that match costume to role: which garment a role type wears, which colour suits a given status, and which object a given situation requires (Bonds, 2008; Han, 2019a–2019e; Tan, 2008).

The rules work on at least four levels. The first is garment form. The python robe (*mang*), formal coat (*pei*), armour (*kao*), informal robe (*xuezi*) and other garments (*yi*) each have their wearers: emperors and ministers wear the python robe, generals wear armour, prisoners wear prisoner's dress, and the *xuezi* is an everyday robe worn by every role type. *Yi* covers the remaining garments, divided into long garments, short garments, special-purpose garments and accessories (Han, 2019d, 2019e). The second level is colour. Bright yellow belongs to the emperor, red to the honoured and to festive occasions, and black to the brave and upright; white, which folk custom links to mourning, marks young and upright heroes on stage (Han, 2019a; Cui et al., 2020). The third is motif, with dragons on the python robe and roundels on the *pei* following set patterns (Han, 2019a, 2019b). The fourth is headwear and accessories. The type of helmet, the beard and its colour, back flags and water sleeves identify the character, and a general in full armour has "armour on the body, flags on the back, plumes on the head" (Han, 2019c).

Two properties of the code matter for any test of it. The rules attach to individual roles rather than to role types: Bao Zheng's black python robe and Zhang Fei's black armour belong to the same painted-face category, yet they cannot be swapped. The rules also depend on the play, since the same character may be dressed differently in different plays. Only when both role and play are fixed is there a single correct costume.

### 1.2 Generative models and opera costume

Digital work on opera costume has followed three routes. One is generation under semantic constraints. Zhang et al. (2026a) combine a knowledge graph with a controllable diffusion model, constructing prompts from graph retrieval and checking consistency after generation; they report that no formal user study has yet been carried out. Zhang et al. (2026b) apply a similar idea to animation, using a multimodal knowledge base and dual-constraint generation to improve the fidelity of costume regulations, and evaluate the system by user preference. A second route is style transfer, which moves motifs from opera costume onto everyday garments (Guo & Liu, 2026). The third is three-dimensional reconstruction of existing costumes for display, teaching and virtual performance (Liu, K. et al., 2022; Su, 2025). Ren et al. (2026), for example, reconstructed 30 Qing court opera costumes, animated them with single-camera motion capture and explored motifs with a diffusion model; their experiment measured perceived reproduction of costume features, usability, immersion and the value of cultural communication.

Studies of the design process have asked a different question. Rizzi and Bertola (2025) observed how master's students divided design work with generative tools, Jin et al. (2024) described how designers use such tools for early concept development, and Wu and Li (2025) interviewed ten practitioners about generative AI in textile design. These studies are concerned with whether the tools are usable and useful. Whether their output conforms to the conventions of the trade has not been their subject. Audits of text-to-image systems, for their part, have treated cultural accuracy as a question of representation: whether outputs amplify stereotypes (Bianchi et al., 2023), how well they reflect the places named in a prompt (Basu et al., 2023), and how the text encoder shapes a model's cultural point of view (Ventura et al., 2025). A codified dress system allows a stricter test, because the correct answer is written down before any image is generated.

### 1.3 Research gap

Two gaps follow from this literature. No study has yet audited generated costumes against the dress code itself. Current evaluations rely on informal feedback (Zhang et al., 2026a), user preference (Zhang et al., 2026b), visual fidelity, or perceived reproduction and immersion (Ren et al., 2026), which treat cultural fidelity as a matter of impression. A dress code is a matter of rules, and a visually convincing image can break three of them at once. The effect of the prompt has also not been measured separately. Systems that build costume knowledge into their architecture cannot distinguish what the model already knows from what the prompt supplies; that requires comparing prompts with and without the dress code on the same roles, across channels. This study addresses both gaps. It sets aside the question of whether a model "understands" Peking opera and measures where its errors fall when it is used directly in a design workflow.

## 2 Materials and methods

### 2.1 Design

The study used a 3 × 2 × 8 factorial design with three generation channels (Doubao, Meta AI, and Hunyuan Image Alpha through Tencent WorkBuddy), two prompt strategies (P1, role and play only; P2, role and play plus the dress code) and eight roles. Each cell produced three images, 144 in total, and the roles were held constant across conditions as a blocking factor. Coding each image on six dimensions gave 864 cells. Seventy-three were coded NA, 71 of them because colour was not scored for four roles and 2 because accessories were hidden, leaving 791 items for analysis.

### 2.2 Roles

The eight roles cover laosheng, hongsheng, wusheng, huashan, daomadan, qingyi, tongchui hualian and wenchou; their dress is documented in published sources (Han, 2019a–2019e; Cui et al., 2020); and they are well known, so readers can check the coding themselves (Table 1). Each role was tied to one play, because only then is there a single correct costume against which a violation can be judged.

Colour was scored only for Guan Yu, Bao Zheng, Zhao Yun and Su San, whose colours (green, black, white and red) are fixed in the sources. For the other four roles the main colour varies between schools and productions, so colour was coded as not applicable unless it breached a status rule, as imperial yellow on a commoner would.

**Table 1.** Roles and dress-code elements coded.

| ID | Role | Play | Role type | Main garment | Main colour | Headwear | Key accessories | Face |
|---|---|---|---|---|---|---|---|---|
| R1 | Zhuge Liang | *Kongcheng Ji* (The Empty City Stratagem) | laosheng | bagua robe (*bagua yi*) | — | bagua scarf hat (*bagua jin*) | feather fan; three-part beard | unpainted (*junban*) |
| R2 | Guan Yu | *Dandao Hui* (The Single Sword Meeting) | hongsheng | green python robe (*lü mang*); green armour (*kao*) also accepted | green | *fuzi* helmet, without pheasant plumes | jade belt | red face; long black beard |
| R3 | Yang Yuhuan | *Guifei Zui Jiu* (The Drunken Concubine) | huashan | female python robe (*nü mang*) | — | phoenix crown (*feng guan*) | cloud collar; jade belt; water sleeves | unpainted; no beard |
| R4 | Mu Guiying | *Mu Guiying Gua Shuai* (Mu Guiying Takes Command) | daomadan | female armour (*nü kao*) | — | headdress with two long pheasant plumes (*lingzi*) | back flags (*kao qi*) | unpainted |
| R5 | Bao Zheng | *Zha Mei An* (The Case of Chen Shimei) | tongchui hualian | black python robe (*hei mang*) | black | minister's hat with horizontal wings (*xiang diao*) | jade belt | all-black face with white crescent on the forehead; full black beard |
| R6 | Zhao Yun | *Changban Po* (Changban Slope) | wusheng | white armour (*bai kao*) | white | warrior helmet | back flags; spear | unpainted; no beard |
| R7 | Su San | *Yu Tang Chun: Qi Jie* (Escorting the Prisoner) | qingyi | red prisoner's jacket and skirt (*zui yi zui qun*) | red | head wrap, no crown | fish-shaped cangue (*yu jia*); water sleeves | unpainted |
| R8 | Jiang Gan | *Qunying Hui* (The Gathering of Heroes) | wenchou | informal robe (*xuezi*) | — | square scholar's cap (*fang jin*) | — | white "tofu-block" patch over the eyes and nose |

*Note.* Only the elements listed were coded; a dash means the cell was not coded.

### 2.3 Prompts

All prompts were in English. One channel is a Meta product, and sending identical text to all three channels required a language that all of them support; English prompts also match the terms used in this article. Chinese prompts were not tested. Each prompt named the role, the play and the role type, followed by a fixed instruction: "Full-body view of one performer, front-facing, plain light grey background, photographic realism." No style, camera or quality terms were added. P2 appended "The costume must follow Peking opera dress codes: {spec}", where the specification listed the elements in Table 1. P1 prompts were 32–37 words long and P2 prompts 61–77 words (Supplementary material S1). Every channel received the same text, and each prompt was entered in a new conversation.

### 2.4 Generation

All images were generated on 21 October 2026 (KST). WorkBuddy is a platform rather than a model; its request log recorded `model=hunyuan-image-alpha` for all 51 calls in the session, so the model is reported as Hunyuan Image Alpha. Each prompt was entered in a new conversation with a 1:1 aspect ratio, the first three images were kept, and no images were selected or regenerated with follow-up prompts. Failures and defects are listed in Supplementary material S1; defective images were kept and coded. Because the three channels may rewrite prompts, filter requests or add style prefixes in ways I cannot observe, I refer to them as generation channels rather than models.

Before coding, all images were resized to 768 pixels on the long side so that the three groups showed the same level of detail. Meta AI returned portrait images, which were padded with background grey to a square without cropping.

### 2.5 Coding

Each image was coded on six dimensions: garment type (D1), colour (D2), motif (D3), headwear (D4), accessories and role markers such as back flags, water sleeves, beards and the cangue (D5), and cross-cultural substitution, meaning elements of Japanese, Korean, Qing court, modern hanfu or Western stage dress (D6). Each was coded 0 (compliant), 1 (violation) or 9 (not visible or not applicable). Garment, motif and colour rules follow Han (2019a–2019e) and Cui et al. (2020); role markers follow standard stage practice. D1 counted a violation only when the class of the main garment was wrong, and D3 judged the type of motif rather than the quality of the work, so that poor rendering was not recorded as a breach of the code.

The images were arranged in 48 contact sheets, each holding the three images of one cell and labelled only with the role and a sheet number, and the sheets were shuffled. Blinding was incomplete: the 48 Hunyuan Image Alpha images carry a platform watermark and the 48 Meta AI images show grey padding, so about two thirds of the images could be attributed to a channel.

Coder A is the author, who trained in fashion design at associate-degree level and is a master's student in the art and design track of the Department of Performing Arts and Culture at the Catholic University of Korea. During coding, coder A used Tencent WorkBuddy to look up references and costume terms; every code was coder A's decision. Coder B was Claude, a large language model, which coded all 144 images with the same codebook without access to coder A's results. Of the disagreements, nine were settled by an explicit rule in the codebook and the rest by the author's judgement; all decisions are logged (Supplementary material S2).

### 2.6 Analysis

I fitted a logistic regression to the image–dimension pairs using generalised estimating equations (Liang & Zeger, 1986), clustered on image with an exchangeable working correlation. The predictors were channel, prompt strategy, dimension and role, and a second model added the channel × strategy interaction. Results are odds ratios (OR) with 95% confidence intervals. Seven sensitivity analyses changed the treatment of the watermarked image, NA cells, D1, D3, each coder's codes and the plumes on Guan Yu's helmet (Supplementary material S2). Agreement between coders was measured with Cohen's κ (Cohen, 1960) for each dimension, with NA as a separate category.

## 3 Results

### 3.1 Inter-coder agreement

The coders agreed on 84.7% of cells before adjudication (κ = 0.70; Table 2). Agreement was highest for colour (κ = 0.92) and lowest for accessories and role markers (κ = 0.45) and cross-cultural substitution (κ = 0.24). Most D5 disagreements concerned borderline substitutes: whether a belt counts as a jade belt, whether Bao Zheng's forehead shows a crescent, and whether a glaive or small pennants stand in for a spear or back flags. Coder B read these more strictly than coder A. The low κ for D6 reflects its low base rate and different thresholds for "close to hanfu".

**Table 2.** Inter-coder agreement before adjudication.

| Dimension | Agreement | Cohen's κ |
|---|---|---|
| Overall | 84.7% | 0.70 |
| D1 Garment type | 86.1% | 0.68 |
| D2 Colour | 95.1% | 0.92 |
| D3 Motif | 84.7% | 0.64 |
| D4 Headwear | 83.3% | 0.66 |
| D5 Accessories and role markers | 71.5% | 0.45 |
| D6 Cross-cultural substitution | 87.5% | 0.24 |

### 3.2 Overall compliance (RQ1)

Fifty-six of the 144 images (38.9%) complied on all six dimensions. Under P1 the channels differed widely (Table 3, Figure 1). Hunyuan Image Alpha broke the code on 75.9% of codable items and produced no fully compliant image, Meta AI broke it on 19.8% with 11 of 24 images fully compliant, and Doubao fell in between.

**Table 3.** Violations by channel and prompt strategy.

| Channel | Violation rate, P1 | Violation rate, P2 | Fully compliant images, P1 | Fully compliant images, P2 |
|---|---|---|---|---|
| Hunyuan Image Alpha | 75.9% | 26.0% | 0/24 | 8/24 |
| Doubao | 37.1% | 7.6% | 3/24 | 14/24 |
| Meta AI | 19.8% | 3.0% | 11/24 | 20/24 |

### 3.3 Dimensions and roles (RQ2)

Headwear was violated most often (40.3% of codable items) and cross-cultural substitution least often (9.0%) (Table 4, Figure 2). The cross-cultural errors that did occur were Qing court headdresses, modern hanfu and Japanese-style elements.

**Table 4.** Violation rate and adjusted OR by dimension.

| Dimension | Violation rate | Adjusted OR (95% CI) | p |
|---|---|---|---|
| D1 Garment type | 27.8% | 1 (reference) | — |
| D2 Colour | 27.4% | 0.80 (0.43–1.51) | .494 |
| D3 Motif | 27.8% | 1.00 (0.54–1.85) | > .999 |
| D4 Headwear | 40.3% | 2.67 (1.51–4.70) | < .001 |
| D5 Accessories and role markers | 37.3% | 2.12 (1.20–3.76) | .010 |
| D6 Cross-cultural substitution | 9.0% | 0.12 (0.05–0.28) | < .001 |

*Note.* Adjusted for strategy, channel and role.

Roles differed as much as dimensions (Table 5; Figure 3). Doubao dressed Zhuge Liang in a python robe and official's hat in all three P1 images (S02). Su San appeared in elaborate women's dress without a cangue (S01-3, S09). Jiang Gan lost his clown markers: the tofu-block patch became a large white mask, and the square cap became a tall or official's hat (S03, S04-2).

**Table 5.** Violation rate by role.

| Role | Role type | P1 | P2 |
|---|---|---|---|
| R1 Zhuge Liang | laosheng | 55.6% | 15.6% |
| R2 Guan Yu | hongsheng | 31.5% | 14.8% |
| R3 Yang Yuhuan | huashan | 22.2% | 0.0% |
| R4 Mu Guiying | daomadan | 26.7% | 6.7% |
| R5 Bao Zheng | tongchui hualian | 35.8% | 7.5% |
| R6 Zhao Yun | wusheng | 44.4% | 13.0% |
| R7 Su San | qingyi | 70.4% | 16.7% |
| R8 Jiang Gan | wenchou | 67.4% | 22.2% |

### 3.4 Stating the dress code (RQ3)

With the dress code in the prompt, the odds of a violation fell to 6.6% of their P1 level (OR = 0.066, 95% CI 0.038–0.116, p < .001). Against Hunyuan Image Alpha, the OR was 0.128 for Doubao (0.082–0.201) and 0.040 for Meta AI (0.021–0.077). The channel × strategy interaction was not significant (p = .18 and .26), so the prompt helped all three channels by a similar proportion. Even so, two thirds of Hunyuan Image Alpha's P2 images still broke at least one rule.

### 3.5 Errors from translated terms

Two errors came from the English wording of the prompt. Rendered as "pleated robe", *xuezi* produced a gown with knife pleats, and in one image a hat resembling an academic mortarboard (S30, Meta AI, P2). Rendered as "fish-shaped cangue", *yu jia* produced a square board with a fish carved on it (S39, Doubao, P2).

### 3.6 Other anomalies and robustness

One Hunyuan Image Alpha image reproduced the watermark of a stock-photo site, `www.yanqin.net` (S34-2). Three Meta AI images of Bao Zheng painted his face on the back of his head (S10-1, S10-3, S36-3). Other images showed a second performer and a plastic stool in the frame (S01) or gave a role the wrong gender or role type (S03-1, S22-3). In the seven sensitivity analyses the OR for P2 ranged from 0.041 to 0.084, for Doubao from 0.100 to 0.180 and for Meta AI from 0.040 to 0.055 (Supplementary material S2).

## 4 Discussion

### 4.1 Knowing the wardrobe without knowing the casting

The consort and the woman general (huashan and daomadan) had the fewest violations; the clown, the prisoner and the strategist (wenchou, qingyi and laosheng) the most (Table 5). Costume complexity does not explain the difference. Yang Yuhuan's phoenix crown, cloud collar and jade belt, or Mu Guiying's flags and plumes, are no simpler than Su San's cangue. A likelier reason is how often and how clearly each type appears in the training data. The consort and the woman general resemble widely circulated "palace" and "warrior" images, and a model can reach them by visual resemblance alone. The strategist, the prisoner and the clown are different. Zhuge Liang's bagua robe belongs to him as a person, Su San's red dress and cangue to her situation, and Jiang Gan's tofu-block face and square cap to the conventions of his role type. These links are rules of the stage, and they rarely appear together in ordinary images.

The models seem to have learned what Peking opera costume looks like without learning who may wear what. The dress code ties each costume to a character, a role type and a play at once, whereas a generative model is only asked for something that looks like Peking opera. Every one of the 144 images was recognisable as a theatre figure, and fewer than four in ten were correct.

### 4.2 Stating the dress code works for those who already know it

Writing garment, colour, motif, headwear, accessories and face into the prompt cut the odds of a violation by more than an order of magnitude in every channel. The information that made this possible came from published sources, stage practice and the designer's own training. The model contributed none of it.

This bears on the claim that generative AI "democratises" design. It makes drawing cheap, but knowing what is correct costs as much as before, and that knowledge now carries more of the weight. It also means the prompt cannot replace review: two thirds of Hunyuan Image Alpha's P2 images still contained an error. One might object that P2 simply hands the model the answers. That is what the comparison was designed to test, and the answer is mixed. Models followed stated rules on colour almost perfectly but kept failing on the headwear and small markers that had failed under P1, which suggests that some rules are hard for these systems to carry out even when they are written down. Both translation errors (Section 3.5) also occurred under P2, so the estimated benefit of stating the code is, if anything, conservative.

### 4.3 Small markers carry the most meaning

The smallest items in a costume do most of the work of identification: the crescent, the cangue, the clown patch, the back flags, the plumes. In a designer's terms they belong to the symbolic layer of the costume, the garment to its structure. A python robe drawn imperfectly is still a theatre costume; without the crescent, Bao Zheng is no longer Bao Zheng. Image models are trained to match overall appearance, so they are weakest exactly where an element is small and carries much of the meaning. The coding struggled at the same point, since most D5 disagreements concerned whether a substitute counts. Future audits should define identifying markers as separate yes-or-no items.

### 4.4 Translation as a source of error

The pleated *xuezi* and the carved board show what happens when a compound term is translated word by word. "Pleated" keeps the literal sense of 褶 and loses the garment it names; "fish-shaped" keeps the fish and loses the outline of the cangue. Han (2019d) describes the *xuezi* as the most common everyday garment on the Peking opera stage, and a model given a literal gloss turns it into the most generic one. For designers who write prompts in a second language, the more specialised the term, the greater this risk. This fits the argument of Ventura et al. (2025) that the text encoder shapes a model's cultural reading. Whether Chinese prompts avoid the problem is a question for further work.

### 4.5 Practical implications

Three habits follow for costume designers. Review generated costumes against a checklist of required items for each role, with particular attention to small markers. Write the dress code into the prompt, and for terms without an established English name keep the pinyin and add a short description of the form. Test a tool on a small set of roles before adopting it, and keep a human decision at the end of the process.

### 4.6 Limitations

The study tested three consumer channels on a single day with English prompts. Their internal prompt handling could not be observed, model updates may change the results, and the effects of language and channel could not be separated. Blinding was incomplete for two of the three channels. The second coder was a language model, and coder A consulted an AI assistant for references and terminology while coding. Sources differ on whether Guan Yu's helmet may carry plumes; treating those three images as compliant does not change the conclusions (Supplementary material S2). The eight roles cover part of the repertoire, with three images per condition, and fine detail was not assessed.

## 5 Conclusion

Asked for a named Peking opera role, three widely used image generators broke the dress code more often than they kept it, most of all in headwear and the small markers that identify a character. Writing the code into the prompt prevented most of these errors, but only a user who already knows the code can write it. The models reproduce the look of the costume without the knowledge of who may wear what. They can draw a costume for a designer; deciding whether it is right is still the designer's work.

---

## Declarations

**Declaration of generative AI use.** I used Tencent WorkBuddy for literature searching and checking bibliographic details, and, during coding, to look up reference material and costume terminology; all coding decisions were my own. I used Claude (Anthropic) for literature searching, translating my Chinese draft into English, language editing, drafting a small number of sentences added in revision, and writing the analysis code; Claude also served as the second coder described in Section 2.5. The images analysed were generated with Doubao, Meta AI and Hunyuan Image Alpha (via Tencent WorkBuddy), as described in Section 2.4. I reviewed all outputs and take full responsibility for the content of this article.

**Disclosure statement.** The author reports there are no competing interests to declare.

**Funding.** This research received no specific funding.

**Data availability statement.** The codebook, prompts, both coders' codes, the adjudication log, the analysis scripts and the 144 generated images are deposited at [OSF link and DOI].

---

## References

Basu, A., Babu, R. V., & Pruthi, D. (2023). Inspecting the geographical representativeness of images from text-to-image models. In *Proceedings of the IEEE/CVF International Conference on Computer Vision* (pp. 5136–5147). https://doi.org/10.1109/ICCV51070.2023.00474

Bianchi, F., Kalluri, P., Durmus, E., Ladhak, F., Cheng, M., Nozza, D., Hashimoto, T., Jurafsky, D., Zou, J., & Caliskan, A. (2023). Easily accessible text-to-image generation amplifies demographic stereotypes at large scale. In *Proceedings of the 2023 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1493–1504). https://doi.org/10.1145/3593013.3594095

Bonds, A. B. (2008). *Beijing opera costumes: The visual communication of character and culture*. University of Hawai'i Press.

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement, 20*(1), 37–46.

Cui, W., Qiang, K., & Wang, X. (2020). Chuantong jingju xiyi "shangxia wuse" chuandai guizhi xingcheng yu tedian tanxi [Formation and characteristics of the "upper and lower five colours" dress code of traditional Peking opera costume]. *Zhongguo Yishu [China Art]*, (3), 64–73.

Guo, Y., & Liu, K. (2026). FLUX–CPSC: A multimodal-driven framework for high-fidelity transfer of traditional Chinese opera costume elements. *Digital Scholarship in the Humanities*. Advance online publication. https://doi.org/10.1093/llc/fqag130

Han, B. (2019a). Meiru jinxiu: Jingju fuzhuang zhi mang [The python robe in Peking opera costume]. *Zhongguo Jingju [Chinese Peking Opera]*, (6), 53–57.

Han, B. (2019b). Meiru jinxiu: Jingju fuzhuang zhi pei [The *pei* in Peking opera costume]. *Zhongguo Jingju*, (7), 54–59.

Han, B. (2019c). Meiru jinxiu: Jingju fuzhuang zhi kao [Armour in Peking opera costume]. *Zhongguo Jingju*, (8), 52–57.

Han, B. (2019d). Meiru jinxiu: Jingju fuzhuang zhi xuezi [The *xuezi* in Peking opera costume]. *Zhongguo Jingju*, (9), 48–53.

Han, B. (2019e). Meiru jinxiu: Jingju fuzhuang zhi changyi [Long garments in Peking opera costume]. *Zhongguo Jingju*, (11), 58–63.

Jin, Y., Yoon, J., Self, J. A., & Lee, K. (2024). Understanding fashion designers' behavior using generative AI for early-stage concept ideation and revision. *Archives of Design Research, 37*(3), 25–45. https://doi.org/10.15187/adr.2024.07.37.3.25

Liang, K.-Y., & Zeger, S. L. (1986). Longitudinal data analysis using generalized linear models. *Biometrika, 73*(1), 13–22.

Liu, C., & Xu, Z. (2021). Cong "chuanguan" zhidai neirong yanbian kan chuantong xiqu yixiangzhi de lishi fazhan [The historical development of the traditional opera costume-trunk system seen through changes in the meaning of *chuanguan*]. *Zhongguo Xiju [Chinese Theatre]*, (3), 60–62.

Liu, K., Gao, Y., Zhang, J., & Zhu, C. (2022). Study on digital protection and innovative design of Qin opera costumes. *Heritage Science, 10*, 127. https://doi.org/10.1186/s40494-022-00762-x

Liu, Y. (2002). *Zhongguo jingju yixiang* [The Chinese Peking opera costume trunk]. Shanghai Lexicographical Publishing House.

Ren, J., Shu, Y., Yang, S., Zhang, B., Yang, Z., Liu, N., & Liu, Z. (2026). Digital reconstruction and motion-based interactive presentation of Qing dynasty court opera costumes. *Journal on Computing and Cultural Heritage*. Advance online publication. https://doi.org/10.1145/3842671

Rizzi, G., & Bertola, P. (2025). Exploring the generative AI potential in the fashion design process: An experimental experience on the collaboration between fashion design practitioners and generative AI tools. *European Journal of Cultural Management and Policy, 15*, 13875. https://doi.org/10.3389/ejcmp.2025.13875

Su, Z. (2025). Immersive teaching model for traditional Chinese opera costume design based on virtual reality: Digital cultural heritage, inheritance, and innovation. *Scientific Reports, 15*, 34830. https://doi.org/10.1038/s41598-025-19350-7

Tan, Y. (2008). *Zhongguo jingju fuzhuang tupu* [Illustrated catalogue of Chinese Peking opera costumes]. Beijing Arts and Crafts Publishing House.

Ventura, M., Ben-David, E., Korhonen, A., & Reichart, R. (2025). Navigating cultural chasms: Exploring and unlocking the cultural POV of text-to-image models. *Transactions of the Association for Computational Linguistics, 13*, 142–166. https://doi.org/10.1162/tacl_a_00732

Wu, X., & Li, L. (2025). Qualitative-empirical insights into generative AI for textile design in the fashion design process. *International Journal of Design Creativity and Innovation, 13*(4), 322–357. https://doi.org/10.1080/21650349.2025.2529167

Zhang, A., Hao, Z., Liu, H., Shi, P., & Xu, H. (2026b). CEDA-Opera: A cognitive-execution decoupling system for Peking opera animation generation. In *Proceedings of the 2026 6th International Conference on Artificial Intelligence and Industrial Technology Applications (AIITA)* (pp. 69–77). IEEE. https://doi.org/10.1109/AIITA69518.2026.11567226

Zhang, Y., Zeng, Y., Song, Y., Li, H., Wang, B., & Chen, Y. (2026a). A semantics-first workflow for Peking opera costume design: Integrating knowledge graphs with controllable diffusion. In *HCI International 2026* (Communications in Computer and Information Science, Vol. 3052, pp. 338–347). Springer. https://doi.org/10.1007/978-3-032-30836-8_35

---

## Figure captions

**Figure 1.** Violation rate (% of codable items) by generation channel under P1 (role name only) and P2 (dress code stated). Hatched bars show P2.

**Figure 2.** Violation rate by dress-code dimension under P1 and P2. Colour (D2) was scored for four roles only.

**Figure 3.** Examples of generated images. (a) Compliant Bao Zheng (Doubao, P2). (b) Zhuge Liang in a python robe and official's hat (Doubao, P1). (c) Su San without the cangue (Doubao, P1). (d) Su San with a Qing court headdress (Hunyuan Image Alpha, P1). (e) "Pleated robe" rendered with literal knife pleats (Meta AI, P2). (f) "Fish-shaped cangue" rendered as a carved board (Doubao, P2). Colour online.

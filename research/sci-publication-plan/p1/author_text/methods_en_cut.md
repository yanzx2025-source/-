## 2 Materials and methods

### 2.1 Design

The study used a 3 × 2 × 8 factorial design: three generation channels (Doubao, Meta AI (Muse), and Tencent WorkBuddy, which calls Hunyuan Image Alpha internally), two prompt strategies (P1, a basic template; P2, a template that states the dress code) and eight roles. Each combination produced three images, for 144 images in total. The eight roles served as a blocking factor and were held constant across all conditions. Each image was coded on six dimensions, giving 864 coding cells. Of these, 73 were coded NA: 71 in the colour dimension, which was not scored for four roles, and 2 where accessories were hidden. After excluding the NA cells, 791 items entered the analysis.

### 2.2 Roles

I selected the roles on three criteria: coverage of role types (laosheng, hongsheng, wusheng, huashan, daomadan, qingyi, tongchui hualian and wenchou); dress codes documented in published sources (Han, 2019a, 2019b; Cui et al., 2020); and familiarity, so that readers can check the coding for themselves (Table 1). Each role was tied to a single play, because the same character can be dressed differently from one play to another; only when the play is fixed is there one correct costume against which a violation can be judged.

Colour was scored only for Guan Yu, Bao Zheng, Zhao Yun and Su San, whose main colours are fixed rules recorded consistently in the sources: green, black, white and red. For the other four roles, the main colour varies between schools and productions, so colour was coded as not applicable; an obvious breach of status, such as imperial yellow worn by a commoner, was still coded as a violation.

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

*Note.* Only the elements listed in the codebook were used for coding. A dash means the cell was not coded.

### 2.3 Prompts

All prompts were written in English. One of the three channels is a Meta product, and giving all three channels identical text meant using a single language that all three supported; English prompts also match the terms used in this article word for word. I did not test Chinese prompts. The choice has a cost: some errors were caused by literal English renderings (Section 3.5), and the language choice was made at the outset, not as the result of a pilot comparison.

Every prompt named the role, the play and the role type, followed by a standard composition instruction ("Full-body view of one performer, front-facing, plain light grey background, photographic realism"); no style, camera or quality terms were added. P2 adds the sentence "The costume must follow Peking opera dress codes: {spec}", where the specification lists the elements in Table 1. P1 prompts are 32–37 words long and P2 prompts 61–77 words (full text in Supplementary material S1). All three channels received exactly the same text, and each prompt was submitted in a new conversation.

### 2.4 Generation

All images were generated on 21 October 2026 (KST). WorkBuddy is the name of a platform, not of a model; its request log recorded `model=hunyuan-image-alpha` for all 51 calls in the session, so the image model is recorded as Hunyuan Image Alpha. Four rules applied throughout: a new conversation for each prompt, a 1:1 aspect ratio, the first three images kept, and no selection or follow-up prompts. Failures and image defects were logged and are reported in Supplementary material S1; all defective images were kept and coded, and no cosmetic screening was applied.

All three channels are referred to as generation channels rather than models, because each is a conversational product that may rewrite prompts internally, apply safety filters or add style prefixes, and I cannot audit the requests these products actually send. The conclusions are limited accordingly.

Before coding, all images were resized to 768 pixels on the long side so that the three groups showed the same level of visible detail. Muse outputs, which were all portrait images, were padded with the background grey to a 1:1 ratio without cropping, so that headwear and the overall form of the costume remained visible.

### 2.5 Coding

Each image was coded on six dimensions: D1, garment type (the class of the main garment); D2, colour rule; D3, motif; D4, headwear; D5, accessories and role markers (for example back flags, water sleeves, beards and the cangue); and D6, cross-cultural substitution (elements of Japanese, Korean, Qing court, modern hanfu or Western stage dress). Each dimension was coded 0 (compliant), 1 (violation) or 9 (not visible, or not applicable). Garment type, motif and colour follow Han (2019a, 2019b) and Cui et al. (2020); role markers follow standard stage practice. To avoid recording "drawn badly" as "dressed wrongly", D1 was coded as a violation only when the class of the main garment was wrong, and motif was judged by type only, not by the fineness of the work.

Blind coding was organised in 48 contact sheets, each showing the three images of one cell, labelled only with the role and a sheet number; the order of the sheets was shuffled. Blinding was not complete: all 48 Hunyuan Image Alpha images carry a platform watermark, and all 48 Muse images show grey padding bands, so about two thirds of the images could be attributed to a channel during coding.

Coder A is the author, who trained in fashion design at associate-degree level and is a master's student in the art and design track of the Department of Performing Arts and Culture at the Catholic University of Korea. While coding, coder A used Tencent WorkBuddy, an AI assistant, only to look up reference material and check costume terminology; every code was decided by coder A. Coder B was Claude, a large language model, which coded all 144 images independently with the same codebook and had no access to coder A's results. Nine disagreements were settled by an explicit rule in the codebook and all others by the author's judgement; every decision is recorded in the adjudication log (Supplementary material S2).

### 2.6 Analysis

The unit of observation was the image–dimension pair. I fitted a binomial logistic regression by generalised estimating equations (GEE), clustered on image, with an exchangeable working correlation structure. The predictors were generation channel, prompt strategy, coding dimension and role, with role entered as a blocking factor; I also tested the channel × strategy interaction. Results are reported as odds ratios (OR) with 95% confidence intervals. Six sensitivity analyses varied the treatment of the watermarked image, of NA cells, of D1 and D3, and of each coder's codes (Supplementary material S2). Agreement between coders was reported as Cohen's κ for each dimension, with NA treated as a separate category.

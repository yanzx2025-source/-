# 3 Method (3.1–3.4)

Translated from the author's Chinese draft (2026-10-21). Corrections from the review are applied, and every one is listed in the review notes. The first paragraph of 3.3 waits for the author's revised rationale.

## 3.1 Design

The study used a 3 × 2 × 8 factorial design:

- **Generation channel (3):** Doubao, Meta AI (Muse), and Tencent WorkBuddy, which calls Hunyuan Image Alpha internally.
- **Prompt strategy (2):** P1, a basic template, and P2, a template that states the dress code.
- **Role (8).**

Each combination produced three images, for 144 images in total. The eight roles served as a blocking factor and were held constant across all conditions, so differences between roles could be estimated separately and were not confounded with channel or strategy effects.

The image was the basic unit of analysis. Each image was coded on six dimensions, giving 864 coding cells. Of these, 73 were coded NA because the element was not visible or the dimension did not apply:

- 71 in the colour dimension, which was not scored for four of the roles;
- 2 where accessories were hidden.

After excluding the NA cells, 791 items entered the analysis.

## 3.2 Roles

I selected the roles on three criteria:

1. **Coverage of role types.** The eight roles span laosheng, hongsheng, wusheng, huashan, daomadan, qingyi, tongchui hualian and wenchou.
2. **Clearly defined dress codes.** The costume of each role is documented in published sources (Han, 2019a, 2019b; Cui et al., 2020), so every element can be checked against a written rule rather than against personal experience.
3. **Familiarity.** All eight roles are well known, so readers and reviewers can check the coding for themselves.

The eight roles are Zhuge Liang, Guan Yu, Yang Yuhuan, Mu Guiying, Bao Zheng, Zhao Yun, Su San and Jiang Gan.

Each role was tied to a single play. The same character can be dressed differently from one play to another, and the requirements of the dress code change with it. Only when the play is fixed is there one correct costume, and so something against which a violation can be judged.

Colour was scored only for Guan Yu, Bao Zheng, Zhao Yun and Su San. For these four the main colour is a fixed rule, recorded consistently in the sources: green for Guan Yu, black for Bao Zheng, white for Zhao Yun and red for Su San. For the other four roles, the main colour varies between schools and productions, and the sources give no single rule. Colour was therefore not judged against a single value and was coded as not applicable. An obvious breach of status, such as imperial yellow worn by a commoner, was still coded as a violation.

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

## 3.3 Prompts

[Paragraph 1, the reason for using English: awaiting the author's revision.]

Every prompt has a fixed frame of four parts:

1. the English name of the role;
2. the English title of the play, with its pinyin;
3. the role type, in English and pinyin;
4. a standard composition instruction: "Full-body view of one performer, front-facing, plain light grey background, photographic realism."

No style, camera or quality terms were added.

P1 and P2 differ only in their final sentence. P1 ends with the composition instruction and states only who the character is, which play and which role type. P2 adds the sentence "The costume must follow Peking opera dress codes: {spec}." The specification lists the role's main garment, colour, motif, headwear, accessories and facial features, as given in Table 1. P1 prompts are 32–37 words long; P2 prompts are 61–77 words.

All three channels received exactly the same text. The English original was copied and pasted verbatim, without translation, rewording, additions or deletions, and each prompt was submitted in a new conversation.

## 3.4 Generation

All images were generated on 21 October 2026 (KST) through three channels: Doubao, Meta AI (Muse) and Tencent WorkBuddy.

**Model attribution for WorkBuddy.** WorkBuddy is the name of a platform, not of a model, so the third channel needs a word of explanation. According to its request log, all 51 calls in this session (48 retained images and 3 retries) were made with `model=hunyuan-image-alpha`. This was also the only entry tagged text-to-image in the account's list of available models. The image model is therefore recorded as Hunyuan Image Alpha. DeepSeek V4.1 Flash, on the conversation side, only drafted the prompts and produced no pixels.

**Fixed procedure.** Four rules applied throughout:

- each prompt was entered in a new conversation;
- the aspect ratio was set to 1:1;
- the first three images were kept;
- no images were selected and no follow-up prompts were given.

When a request failed, it was resubmitted with the original prompt and the failure was logged.

**Problems during generation.** Problems fell into four types.

1. **System error.** Muse returned a 500 internal error for the first P2 image of R8. The request was resubmitted once with the original prompt and succeeded. The failure was logged and not counted in the results.
2. **File overwriting.** In WorkBuddy, two parallel requests completed in the same second and produced files with the same name, so two images were overwritten. From then on, requests were submitted strictly one at a time, and each image was saved as soon as it was generated. One image was regenerated.
3. **Parameter failure.** On one occasion the output directory setting did not take effect and the image was saved to the default folder. It was moved by hand.
4. **Image defects.** The second P1 image of R2 from Hunyuan reproduced the watermark of a third-party image source, www.yanqin.net, at the bottom of the frame. The image was kept unaltered and flagged as unusable. It remains in the main analysis, and a sensitivity analysis excludes it. Other defects included a second performer in the frame, a modern plastic stool, and mismatches of gender and role type. All were kept and coded. These defects are part of the results, and no cosmetic screening was applied.

**Why "generation channels".** All three are referred to as generation channels rather than models. Each is a conversational product that may rewrite prompts internally, apply safety filters or add style prefixes, and I cannot audit the requests these products actually send. The object of study is therefore defined as the generation channels available to designers in practice, and the conclusions are limited accordingly. This point is noted among the limitations.

**Image preparation.** Before coding, the images were processed in two ways.

1. The three channels returned images of very different sizes: 1024 × 1024 from WorkBuddy, 2048 × 2048 from Doubao, and a long side of 1920 to 2480 pixels from Muse. All images were resized to 768 pixels on the long side so that the three groups showed the same level of visible detail.
2. All Muse outputs were portrait images: 38 at 1120 × 2240, 9 at 1280 × 1920 and 1 at 992 × 2480. They were padded left and right with the background grey to a 1:1 ratio, without cropping. Cropping would have cut off the headwear or the feet, and both headwear and footwear were coded. [Check: the codebook does not code footwear; see review note 4.]

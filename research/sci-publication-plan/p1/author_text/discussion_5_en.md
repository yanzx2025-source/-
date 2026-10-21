# 5 Discussion

Translated from the author's Chinese draft (`discussion_5_zh_v0.md`). Four small corrections of fact were made in translation; they are listed in the review notes. One point in 5.6 is marked [Check] and needs the author's answer before submission.

I compared the costume outputs of three generation channels, under two prompt strategies, for eight Peking opera roles. Three results are the starting point for this discussion.

1. When the dress code was not stated (P1), violation was the norm. Across all 144 images, only 56 (38.9%) were compliant on all six dimensions.
2. When the dress code was stated in the prompt (P2), the odds of a violation fell to 6.6% of the P1 level (OR = 0.066, 95% CI 0.038–0.116).
3. The dress-code statement did not eliminate violations, and the remaining errors were distributed very unevenly across dimensions and roles.

## 5.1 The models know what is in the costume trunk, but not who wears what

The differences between roles give the first clue. The huashan and daomadan roles had the fewest violations, and the wenchou, qingyi and laosheng roles the most (Table 5). This pattern cannot be explained by how complex a role's costume is. Yang Yuhuan's phoenix crown, cloud collar and jade belt, or Mu Guiying's back flags and long plumes, are structurally no simpler than Su San's fish cangue.

A more plausible explanation is how visible and how clearly labelled these images are likely to be in the training data. The imperial consort and the woman general resemble widely circulated "palace" and "warrior" motifs. A model can hit them through visual likeness without knowing the dress code. The correct costumes of the strategist, the prisoner and the clown depend instead on a link between identity and costume:

- the bagua robe belongs to Zhuge Liang as a person;
- the prisoner's dress and cangue belong to Su San's situation;
- the tofu-block face and square cap belong to the conventions of the clown role type.

These links are not frequent visual co-occurrences. They are institutional rules.

One possible mechanism, then, is that the models have learned the visual distribution of Peking opera costume, not the mapping that the dress code defines. The dress code is a set of rules about who may wear what, and it rests on three constraints at once: the character's identity, the role type and the play. A generative model is asked only to produce an image that looks like Peking opera. This accounts for a gap that recurred throughout the study. All 144 images were recognisable as theatre figures, yet only 38.9% complied on all six dimensions. Looking right and being right are different things. The first is a matter of style; the second is a matter of convention.

## 5.2 Stating the dress code works, but only if the person writing it knows the code

The effect of P2 is the most directly usable result of this study. Writing the main garment, colour, motif, headwear, accessories and face into the prompt, item by item, cut the odds of a violation by more than an order of magnitude. The interaction terms were not significant (p = .18 and .26), so the effect did not depend on the channel. A statement of the dress code is something a model can carry out.

Carrying out a dress code and writing it correctly are, however, two different things. P2 worked because the prompt already contained the correct information about form. That information came from published sources, from standard stage practice and from professional experience, not from the model.

Placed in the debate about generative AI "democratising" design, this result calls for a distinction between two kinds of cost. AI lowers the cost of drawing. It does not lower the cost of knowing what is correct. In this study the second was the scarce input: every rule in the codebook had to be traced to a source or to stage practice, and the dress-code table for eight roles took a whole subsection to set out. The tool lowers the threshold for execution, and in doing so raises the relative weight of the threshold for judgement.

The same logic explains why P2 cannot replace human review. About two thirds of the P2 images from Hunyuan Image Alpha still violated at least one rule. A prompt changes the probabilities; it does not guarantee the result.

## 5.3 The small markers carry the most weight and fail most often

Violation rates were uneven across the six dimensions. Headwear was violated most often and cross-cultural substitution least often (Table 4).

If the costume elements are ordered by physical size, an inverse relationship appears. The smallest items carry the heaviest burden of identification: the crescent, the fish cangue, the tofu-block patch, the back flags and the plumes.

From a costume designer's point of view, these items belong to the symbolic layer of the costume rather than its structural layer. If the form of a python robe is wrong, the image is still a theatre costume. If Bao Zheng has no crescent on his forehead, the image is no longer Bao Zheng. The first is "wearing the wrong garment"; the second is "not being this person".

Generative models are trained mainly to match overall appearance, and they get no supervision from a list of required items. They are therefore most likely to fail where an element carries the most meaning and occupies the fewest pixels. For practice, this matters more directly than the overall violation rate: checking identifying items against a list is more effective than judging the overall impression.

The coding process ran into a methodological difficulty at exactly this point. The D5 disagreements centred on three questions:

- whether a belt counts as a jade belt;
- whether there is a crescent on Bao Zheng's forehead;
- whether a glaive or small pennants count as a spear or back flags.

None of these is a question of whether something is visible. Each is a question of whether it counts. The codebook defined whether a marker was present, but not where a substitute or an approximation stops counting. Future studies should define identifying items as a separate set of binary, decidable codes rather than folding them into a general "accessories" category.

## 5.4 Translating terms creates new errors

The two errors reported in Section 4.5 can be traced to the change of language in the prompt.

- *Xuezi* was rendered as "pleated robe". The model read 褶 as physical pleating and produced a pleated scholar's gown.
- *Yu jia* was rendered as "fish-shaped cangue". The model read "fish" as a decorative motif and produced a square board carved with a fish.

In both cases a compound term was translated word by word, and the information about category was lost along the way.

A possible reason is that these terms have no corresponding costume category in the target language, only words that match them literally. "Pleated" keeps the literal sense of 褶 but loses what *xuezi* refers to as a costume category. "Fish-shaped" keeps the modifying relation but loses the overall outline of the cangue. For designers whose first language is not English, this is not an occasional slip but a systematic risk of writing prompts in English. The more specialised a compound term is to the trade, the more likely it is to be broken apart in translation.

This is consistent with the reason, given in the Method, for listing untested Chinese prompts as a limitation. If the study were repeated with Chinese prompts, terms such as 褶子 and 鱼枷 would not need to pass through a change of category, and these errors might decrease. Whether Chinese prompts are carried out equally well across platforms, however, cannot be answered from the present data and remains a question for future research.

## 5.5 Implications for design practice

**First, make review a checklist rather than a matter of overall impression.** List the required items for each role: main garment, main colour, headwear and identifying markers. Check them one by one, paying particular attention to small markers such as the crescent, the fish cangue, the tofu-block patch and the back flags. In this study these items had the highest error rates, and they are the hardest to spot at a glance in a thumbnail.

**Second, state the dress code explicitly in the prompt, and avoid literal translations of compound terms.** One workable approach is to list form, colour, headwear and accessories item by item, adding a glossary or a reference image where needed. For costume items without an established English name, keep the pinyin and add a brief description rather than leaving the machine to assemble the term word by word.

**Third, test a tool on a small sample before adopting it, and do not judge its reliability from a single successful image.** The same prompt produced clearly different results in the three channels. After controlling for prompt strategy, the odds of a violation for Doubao were 0.128 times those of the reference channel, and for Muse 0.040 times. Such differences are almost invisible in a single image. In real projects, a human finalisation step should follow the generation step.

## 5.6 Limitations

**First, the object of study is the generation channel, not the underlying model.** All three platforms are conversational products. They may rewrite prompts internally, apply filters or add style prefixes, and I could not audit the actual requests. The conclusions therefore apply to the product interfaces that designers actually use.

**Second, comparisons between channels were not strictly blind.** The 48 Hunyuan images carry an "AI生成" watermark, and the 48 Muse images have grey side bands left by padding portrait originals. About two thirds of the 144 images could therefore be attributed to a channel during coding, which may have influenced the judgements.

**Third, the second coder was a large language model rather than a human expert.** Its codes can serve as a reference for agreement, but they are not equivalent to review by a peer. Coder A's initial codes were also made with AI assistance. Although every code was checked individually, they may still carry a systematic bias. [Check: see review note 1.]

**Fourth, the scope of roles and images is limited.** The eight roles cover only some role types, and each role has only three images per condition. Inferences about individual roles are therefore limited and should not be extended to all Peking opera role types.

**Fifth, fine detail was not coded.** All images were resized to 768 pixels on the long side before coding, so differences in fine detail, such as stitching or density of decoration, fell outside the judgement. The study assessed form and category, not craftsmanship.

**Sixth, the images come from a single date, and only English prompts were used.** All images were generated in one batch on a single day. Model versions change over time, and a replication might give different results. Because only English prompts were used and Chinese prompts were not tested, the effects of language and channel could not be separated in this design.

## 5.7 Conclusion

Without a statement of the dress code, the three channels mostly produced Peking opera costumes that violated it.

- Only 38.9% of the 144 images complied on all six dimensions.
- Errors concentrated in garment type, headwear and identifying markers.
- Cross-cultural elements appeared less often, but they did appear.

Stating the dress code reduced the odds of a violation to 6.6% of the P1 level. It did not eliminate violations, and its usefulness depends on whether the person writing it knows the code.

What the models command is the visual distribution of Peking opera costume, not the institutional knowledge of who may wear what. This gap defines the place of generative tools in costume design for Chinese opera: they can take on the drawing, but not the final decision.

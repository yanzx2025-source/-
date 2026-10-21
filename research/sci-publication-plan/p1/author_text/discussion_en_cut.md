## 4 Discussion

Without a statement of the dress code, violation was the norm: only 38.9% of the 144 images complied on all six dimensions. Stating the code reduced the odds of a violation to 6.6% of the P1 level, but did not eliminate violations, and the remaining errors were distributed very unevenly across dimensions and roles.

### 4.1 The models know what is in the costume trunk, but not who wears what

The huashan and daomadan roles had the fewest violations, and the wenchou, qingyi and laosheng roles the most (Table 5). This pattern cannot be explained by how complex a costume is: Yang Yuhuan's phoenix crown, cloud collar and jade belt, or Mu Guiying's back flags and long plumes, are structurally no simpler than Su San's fish cangue. A more plausible explanation is how visible and how clearly labelled these images are likely to be in the training data. The imperial consort and the woman general resemble widely circulated "palace" and "warrior" motifs, which a model can hit through visual likeness without knowing the dress code. The correct costumes of the strategist, the prisoner and the clown depend instead on a link between identity and costume: the bagua robe belongs to Zhuge Liang as a person, the prisoner's dress and cangue to Su San's situation, and the tofu-block face and square cap to the conventions of the clown role type. These links are not frequent visual co-occurrences; they are institutional rules.

One possible mechanism, then, is that the models have learned the visual distribution of Peking opera costume, not the mapping that the dress code defines. The dress code is a set of rules about who may wear what, resting on three constraints at once: the character's identity, the role type and the play. A generative model is asked only to produce an image that looks like Peking opera. All 144 images were recognisable as theatre figures, yet only 38.9% complied on all six dimensions. Looking right and being right are different things: the first is a matter of style, the second a matter of convention.

### 4.2 Stating the dress code works, but only if the person writing it knows the code

Writing the main garment, colour, motif, headwear, accessories and face into the prompt cut the odds of a violation by more than an order of magnitude, and the effect did not depend on the channel. Carrying out a dress code and writing it correctly are, however, two different things. P2 worked because the prompt already contained the correct information about form, which came from published sources, stage practice and professional experience, not from the model.

Placed in the debate about generative AI "democratising" design, this result calls for a distinction between two kinds of cost. AI lowers the cost of drawing; it does not lower the cost of knowing what is correct. The tool lowers the threshold for execution, and in doing so raises the relative weight of the threshold for judgement. For the same reason P2 cannot replace human review: two thirds of the P2 images from Hunyuan Image Alpha still violated at least one rule. A prompt changes the probabilities; it does not guarantee the result.

### 4.3 The small markers carry the most weight and fail most often

If the costume elements are ordered by physical size, an inverse relationship appears: the smallest items carry the heaviest burden of identification. From a costume designer's point of view these items belong to the symbolic layer of the costume rather than its structural layer. If the form of a python robe is wrong, the image is still a theatre costume; if Bao Zheng has no crescent on his forehead, the image is no longer Bao Zheng. Generative models are trained mainly to match overall appearance, with no supervision from a list of required items, so they are most likely to fail where an element carries the most meaning and occupies the fewest pixels.

The coding ran into a methodological difficulty at exactly this point. The D5 disagreements were not about whether something was visible, but about whether a substitute or approximation counts. Future studies should define identifying items as a separate set of binary, decidable codes rather than folding them into a general "accessories" category.

### 4.4 Translating terms creates new errors

The pleated *xuezi* and the carved board show compound terms translated word by word, with information about category lost along the way. "Pleated" keeps the literal sense of 褶 but loses what *xuezi* refers to as a costume category; "fish-shaped" keeps the modifying relation but loses the outline of the cangue. For designers whose first language is not English this is a systematic risk: the more specialised a compound term is to the trade, the more likely it is to be broken apart in translation. Whether Chinese prompts would reduce these errors, and whether they are carried out equally well across platforms, remains a question for future research.

### 4.5 Implications for design practice

First, make review a checklist rather than a matter of overall impression: list the required items for each role and check them one by one, paying particular attention to small markers. Second, state the dress code explicitly in the prompt and avoid literal translations of compound terms; for costume items without an established English name, keep the pinyin and add a brief description. Third, test a tool on a small sample before adopting it, and keep a human finalisation step after generation.

### 4.6 Limitations

The object of study is the generation channel, not the underlying model; prompt rewriting and filtering inside the products could not be audited. Comparisons between channels were not strictly blind, because about two thirds of the images carried a watermark or padding bands. The second coder was a large language model rather than a human expert, and coder A used an AI assistant to look up references and terminology; all codes were coder A's own decisions, but the information retrieved in this way may still have shaped some judgements. The eight roles cover only some role types, with three images per condition. Fine detail was not coded, because images were resized before coding. Finally, all images were generated on a single day with English prompts only, so model updates may change the results, and the effects of language and channel could not be separated.

## 5 Conclusion

Without a statement of the dress code, the three channels mostly produced Peking opera costumes that violated it, with errors concentrated in garment type, headwear and identifying markers. Stating the code reduced the odds of a violation to 6.6% of the P1 level, but its usefulness depends on whether the person writing it knows the code. What the models command is the visual distribution of Peking opera costume, not the institutional knowledge of who may wear what: they can take on the drawing, but not the final decision.

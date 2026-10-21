## 1 Introduction

Peking opera costume is not stage costume in the ordinary sense. It is a symbolic system with binding force. The trade saying "better to wear a torn costume than the wrong one" (宁穿破，不穿错) makes the point: a worn or torn costume is acceptable, but a costume that does not match the role is not. The dress code encodes role type, status and situation in garment form, colour, motif, headwear and accessories. Bao Zheng wears a black python robe, a minister's hat with horizontal wings and a white crescent on his forehead. Guan Yu wears a green python robe and a red face. Su San, a prisoner, must wear a red prisoner's jacket and skirt and a fish-shaped cangue. These are not aesthetic preferences but rules whose observance can be judged item by item, and they have been documented systematically (Bonds, 2008).

Over the past decade, generative image models have entered this field. Opera posters, cultural merchandise and draft stage costumes increasingly begin with a prompt, and technical research has followed. Examples include diffusion generation constrained by a knowledge graph (Zhang et al., 2026a) and an animation system that takes "regulation distortion" as its starting problem (Zhang et al., 2026b). These studies address whether a system can generate images that look right. Their evaluation relies mostly on informal feedback, visual fidelity or user preference.

Looking right and being right are not the same. An image can be recognisable at a glance as a Peking opera figure and still put a python robe on the wrong character, leave Su San without her cangue, or paint Bao Zheng's face on the back of his head. Such errors are asymmetric: a layperson does not see them, while an expert sees them at once, and most people now using these tools are laypeople. To judge whether generative models can enter this workflow, what is needed is not another evaluation of style but a rule-by-rule check against the dress code.

The conditions for such a check now exist. Image quality is high enough for these systems to produce recognisable opera figures reliably, so compliance can be judged cell by cell. The dress code is also recorded in published sources, from which a codebook can be built. The question therefore shifts from "does AI draw something that looks like Peking opera?" to "how many rules does an AI-drawn Peking opera costume break, and where?"

This study is an audit. Three generation channels were tested: Doubao, Meta AI (Muse), and Tencent WorkBuddy, which calls Hunyuan Image Alpha. Each channel received two prompt strategies (the role and play only, or the role and play plus the dress code) for eight canonical roles, with three images per cell, giving 144 images. Each image was coded on six dimensions, and regressions were fitted with the image–dimension pair as the unit of observation. Three research questions guided the study:

- RQ1: How often is the dress code violated when it is not stated?
- RQ2: In which dimensions and roles do errors concentrate?
- RQ3: Does stating the dress code reduce violations, and is the effect consistent across channels?

The study makes three contributions:

1. an operational six-dimension codebook that makes such audits repeatable;
2. a description of the structure of the errors, which are uneven, with headwear and identifying markers as the main points of failure;
3. an estimate of the effect of stating the dress code, and of its limits.

The objects of study are three conversational products rather than bare models, and the platforms may rewrite prompts internally. The conclusions are therefore limited to the generation channels that designers actually use.

### 1.1 The dress code of Peking opera costume

The wardrobe is managed in trunks by function: the main costume trunk, the second and third costume trunks, the helmet trunk and the trunk for flags and weapons each hold their own items, so that costume, headwear and props are matched. Monographs on the costume trunk organise their chapters by this division (Liu, Y., 2002). The system can be traced to the *chuanguan* (穿关), the costume annotations for each character in Ming court performances. Its terminology then evolved through *xingtou* (行头), *xiyi* (戏衣) and the costume lists known as *chuandai tigang* (穿戴题纲) before settling into its present form (Liu, C. & Xu, 2021). The resulting dress code is a set of rules matching role to costume. Which garment a role type wears, which colour a given status uses and which object a given situation requires all have fixed answers (Bonds, 2008; Han, 2019a–2019e; Tan, 2008).

The code has at least four layers:

1. **Form.** Python robe (*mang*), formal coat (*pei*), armour (*kao*), informal robe (*xuezi*) and other garments (*yi*) each have their own wearers. Emperors and ministers wear the python robe, generals wear armour, scholars wear the *xuezi* and prisoners wear prisoner's dress. The python robe and armour are ceremonial and military dress, while the *xuezi* is an everyday garment worn by all role types. *Yi* is the general term for the remaining garments, comprising long garments, short garments, special-purpose garments and accessories (Han, 2019d, 2019e).
2. **Colour.** Bright yellow is reserved for the emperor. Red is used for the honoured and for festive occasions. Black expresses courage and uprightness. White, associated with mourning in folk custom, marks young and upright heroes on stage (Han, 2019a; Cui et al., 2020).
3. **Motif.** Dragons on the python robe and roundels on the *pei* follow set patterns (Han, 2019a, 2019b).
4. **Headwear and accessories.** The type of helmet, the presence and colour of the beard, and the arrangement of back flags and water sleeves together form identifying markers. The complete dress of armour is "armour on the body, flags on the back, plumes on the head" (Han, 2019c).

Two features of these rules are easily overlooked. First, the rules are specific to roles, not general to role types. Within the same painted-face category, Bao Zheng's black python robe and Zhang Fei's black armour cannot be exchanged. Second, the rules depend on the play. The same character may be dressed differently in different plays, and only when the play is fixed is there a single correct costume. Any test against the dress code must therefore fix both role and play.

The force of the code shows in how errors are ranked. Coarse embroidery or unsuitable fabric counts as "wearing torn" and can be tolerated. A *xuezi* where a python robe is required, or a prince's crown where a minister's hat is required, counts as "wearing wrong" and cannot. This study judges only the latter and does not assess craftsmanship. That is the first principle of the codebook.

### 1.2 Generative models in the production of opera costume

Digital research on opera costume has followed three technical routes.

The first route is generation under semantic constraints. Zhang et al. (2026a) combine a knowledge graph with a controllable diffusion model: graph retrieval and prompt construction come first, followed by a consistency check after generation. The authors state that no formal user study has yet been carried out. A related approach appears in animation. Zhang et al. (2026b) take "regulation distortion" as their starting problem and use a multimodal knowledge base and dual-constraint generation to improve the fidelity of costume regulations, evaluated by user preference rates.

The second route is style transfer. The FLUX–CPSC framework of Guo and Liu (2026) constrains cultural-symbol integrity, garment-structure stability and embroidery fidelity at the same time, moving motifs from opera costume onto everyday garments.

The third route is three-dimensional reconstruction, in which real costumes are modelled or scanned for display, teaching and virtual performance (Liu, K. et al., 2022; Su, 2025). Ren et al. (2026) reconstructed 30 Qing court opera costumes and added motion driven by a single camera and diffusion-based motif exploration. Their comparative experiment measured perceived reproduction of costume features, usability, immersion and the value of cultural communication.

Meanwhile, research on design processes has accumulated. Rizzi and Bertola (2025) observed designers collaborating with AI in a master's course. Jin et al. (2024) reported how designers use generative models in early concept development. Wu and Li (2025) interviewed ten practitioners about the benefits of and obstacles to generative AI in textile design. The shared concern of these studies is whether the tools are usable and useful, not whether their output conforms to the norms of the trade.

### 1.3 Research gap and position of this study

Existing work leaves three gaps.

**First, there is no quantitative audit that uses the dress code as its criterion.** Current evaluations rely on informal feedback (Zhang et al., 2026a), user preference (Zhang et al., 2026b), visual fidelity, or perceived feature reproduction and immersion (Ren et al., 2026). These measures capture impression, whereas judging the dress code requires checking each item for correctness. The two can diverge: a visually convincing image can be wrong in three places at once.

**Second, "cultural fidelity" has mostly been treated as a perceptual variable rather than as conformity to a norm.** Whether viewers find an image convincing and whether an expert judges it correct are different questions. For an object as highly conventionalised as opera costume, the second is the precondition for design to be usable in practice.

**Third, the role of the prompt has not been measured on its own.** Semantic-constraint systems build knowledge into the system, so they cannot separate what the model already knows from what the prompt tells it. Answering this requires comparing prompts with and without the dress code on the same roles while controlling for differences between channels.

The present study is designed accordingly:

- a six-dimension codebook built from published records of the dress code makes the judgements repeatable;
- taking the image–dimension pair as the unit of observation turns compliance into something that can be analysed statistically;
- a 3 × 2 × 8 factorial design separates channel effects from prompt effects, and sensitivity analyses test robustness.

The aim is not to assess whether a model "understands Peking opera", but to measure where in the structure of the costume its errors appear when it is placed directly into a design workflow.

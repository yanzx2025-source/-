# Supplementary material

## S1 Prompts and generation log

### S1.1 Full prompt text

**P1-R1 Zhuge Liang.** A traditional Peking opera stage costume for Zhuge Liang in the play Empty City Stratagem (Kongcheng Ji), laosheng (older male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.

**P1-R2 Guan Yu.** A traditional Peking opera stage costume for Guan Yu in the play Single Sword Meeting (Dandao Hui), hongsheng (red-faced male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.

**P1-R3 Yang Yuhuan.** A traditional Peking opera stage costume for Yang Yuhuan in the play The Drunken Concubine (Guifei Zui Jiu), huashan (female lead). Full-body view of one performer, front-facing, plain light grey background, photographic realism.

**P1-R4 Mu Guiying.** A traditional Peking opera stage costume for Mu Guiying in the play Mu Guiying Takes Command (Mu Guiying Gua Shuai), daomadan (martial female role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.

**P1-R5 Bao Zheng.** A traditional Peking opera stage costume for Bao Zheng in the play Case of Chen Shimei (Zha Mei An), tongchui hualian (painted-face role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.

**P1-R6 Zhao Yun.** A traditional Peking opera stage costume for Zhao Yun in the play Changban Slope (Changban Po), wusheng (martial male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.

**P1-R7 Su San.** A traditional Peking opera stage costume for Su San in the play Yu Tang Chun - Escorting the Prisoner (Qi Jie), qingyi (virtuous female role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.

**P1-R8 Jiang Gan.** A traditional Peking opera stage costume for Jiang Gan in the play Gathering of Heroes (Qunying Hui), wenchou (civil clown role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.

**P2-R1 Zhuge Liang.** A traditional Peking opera stage costume for Zhuge Liang in the play Empty City Stratagem (Kongcheng Ji), laosheng (older male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The costume must follow Peking opera dress codes: wearing the bagua robe (bagua yi) decorated with Eight Trigrams symbols, bagua scarf hat (bagua jin), holding a feather fan, long black three-part beard (hei sanran).

**P2-R2 Guan Yu.** A traditional Peking opera stage costume for Guan Yu in the play Single Sword Meeting (Dandao Hui), hongsheng (red-faced male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The costume must follow Peking opera dress codes: wearing a green python robe (lü mang) with dragon embroidery, Fuzi helmet (fuzi kui), jade belt, red painted face, long black five-strand beard.

**P2-R3 Yang Yuhuan.** A traditional Peking opera stage costume for Yang Yuhuan in the play The Drunken Concubine (Guifei Zui Jiu), huashan (female lead). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The costume must follow Peking opera dress codes: wearing a female python robe (nü mang) with phoenix embroidery, phoenix crown (feng guan), cloud collar (yun jian), jade belt, white water sleeves, beauty makeup without beard.

**P2-R4 Mu Guiying.** A traditional Peking opera stage costume for Mu Guiying in the play Mu Guiying Takes Command (Mu Guiying Gua Shuai), daomadan (martial female role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The costume must follow Peking opera dress codes: wearing female armor (nü kao) with four triangular back flags (kao qi), headdress with two long pheasant feathers (lingzi), beauty makeup.

**P2-R5 Bao Zheng.** A traditional Peking opera stage costume for Bao Zheng in the play Case of Chen Shimei (Zha Mei An), tongchui hualian (painted-face role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The costume must follow Peking opera dress codes: wearing a black python robe (hei mang) with dragon embroidery, black minister hat with horizontal wings (xiang diao), jade belt, all-black painted face with a white crescent moon on the forehead, full black beard.

**P2-R6 Zhao Yun.** A traditional Peking opera stage costume for Zhao Yun in the play Changban Slope (Changban Po), wusheng (martial male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The costume must follow Peking opera dress codes: wearing white armor (bai kao) with four triangular back flags (kao qi), warrior helmet, holding a spear, beauty makeup without beard.

**P2-R7 Su San.** A traditional Peking opera stage costume for Su San in the play Yu Tang Chun - Escorting the Prisoner (Qi Jie), qingyi (virtuous female role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The costume must follow Peking opera dress codes: wearing red prisoner's jacket and skirt (zui yi zui qun), simple head wrap without crown, fish-shaped wooden cangue (yu jia) on the neck, white water sleeves, beauty makeup.

**P2-R8 Jiang Gan.** A traditional Peking opera stage costume for Jiang Gan in the play Gathering of Heroes (Qunying Hui), wenchou (civil clown role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The costume must follow Peking opera dress codes: wearing a scholar's pleated robe (xuezi), square scholar hat (fang jin), small white tofu-block patch painted around the eyes and nose.

### S1.2 Problems during generation

1. **System error.** Muse returned a 500 internal error for the first P2 image of R8. The request was resubmitted once with the original prompt and succeeded. The failure was logged and not counted in the results.
2. **File overwriting.** In WorkBuddy, two parallel requests completed in the same second and produced files with the same name, so two images were overwritten. From then on, requests were submitted strictly one at a time, and each image was saved as soon as it was generated. One image was regenerated.
3. **Parameter failure.** On one occasion the output directory setting did not take effect and the image was saved to the default folder. It was moved by hand.
4. **Image defects.** The second P1 image of R2 from Hunyuan reproduced the watermark of a third-party image source, www.yanqin.net, at the bottom of the frame. The image was kept unaltered and remains in the main analysis; a sensitivity analysis excludes it. Other defects included a second performer in the frame, a modern plastic stool, and mismatches of gender and role type. All were kept and coded.

### S1.3 Model attribution and image sizes

WorkBuddy request log: all 51 calls (48 retained images and 3 retries) used model=hunyuan-image-alpha, the only entry tagged text-to-image in the account model list; DeepSeek V4.1 Flash, on the conversation side, drafted no pixels. Native sizes: 1024 × 1024 (WorkBuddy), 2048 × 2048 (Doubao), Muse portrait images 1120 × 2240 (38), 1280 × 1920 (9) and 992 × 2480 (1).
## S2 Coding reliability, adjudication and sensitivity analyses

### S2.1 Inter-coder agreement with bootstrap 95% CIs (2,000 resamples of images)

| Dimension | Agreement | Cohen's κ | 95% CI |
|---|---|---|---|
| Overall | 84.7% | 0.70 | 0.64–0.76 |
| D1 Garment type | 86.1% | 0.68 | 0.55–0.80 |
| D2 Colour | 95.1% | 0.92 | 0.85–0.98 |
| D3 Motif | 84.7% | 0.64 | 0.49–0.77 |
| D4 Headwear | 83.3% | 0.66 | 0.53–0.78 |
| D5 Markers and accessories | 71.5% | 0.45 | 0.32–0.58 |
| D6 Cross-cultural substitution | 87.5% | 0.24 | −0.01–0.48 |

### S2.2 Adjudication
The coders disagreed on 132 cells across 78 images. Nine were settled by explicit codebook rules (S03-3 D2; S42-1/2/3 D5; S24-1/2 D5; S39-1/2/3 D5); all others by coder A. The full log is provided as `adjudication_log.csv`.

### S2.3 Sensitivity analyses (odds ratios; references: P1 and Hunyuan Image Alpha)

| Analysis | P2 OR | Doubao OR | Muse OR |
|---|---|---|---|
| Main analysis (consensus codes) | 0.066 | 0.128 | 0.040 |
| Excluding the watermarked image | 0.066 | 0.127 | 0.040 |
| NA counted as compliant | 0.073 | 0.138 | 0.044 |
| Excluding D3 | 0.057 | 0.130 | 0.043 |
| Excluding D1 | 0.084 | 0.151 | 0.051 |
| Coder A only (before adjudication) | 0.063 | 0.100 | 0.040 |
| Coder B only | 0.041 | 0.180 | 0.055 |

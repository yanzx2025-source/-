# Better torn than wrong: data and code

Materials for the article "Better torn than wrong: auditing generative AI images of Peking opera costume against the dress code".

## Contents
| Folder | Contents |
|---|---|
| `codebook/` | Six-dimension codebook (D1–D6) with the sources for each rule |
| `prompts/` | The 16 prompts (P1, P2 × 8 roles), role specifications (`roles.json`) and the template code |
| `images/` | The 144 generated images, resized to 768 px on the long side, one folder per channel |
| `contact_sheets/` | The 48 blinded contact sheets used for coding (role and sheet number only) |
| `data/` | `coder_A_author_codes.csv` (author), `coder_B_model_codes_blind.csv` (Claude), `adjudication_log.csv`, `consensus_codes.csv`, `sheet_key.csv` (maps sheets to channel, strategy, role and file) |
| `analysis/` | Python scripts for the GEE models, sensitivity analyses, figures and contact sheets |
| `figures/` | Figures 1–3 |

## File naming
Images are named `{channel}_{strategy}_{role}_{replicate}.jpg`. Channels: `doubao` (Doubao), `muse` (Meta AI), `hunyuan` (Hunyuan Image Alpha via Tencent WorkBuddy; the original files were prefixed `deepseek_` because WorkBuddy's chat model is DeepSeek, which did not generate images). Roles R1–R8: Zhuge Liang, Guan Yu, Yang Yuhuan, Mu Guiying, Bao Zheng, Zhao Yun, Su San, Jiang Gan.

## Codes
0 = compliant, 1 = violation, 9 = not visible or not applicable. Image IDs (`S01-1` …) refer to contact sheet and position; `sheet_key.csv` decodes them. Note: `sheet_key.csv` lists original file names with the `deepseek_` prefix.

## Reproducing the analysis
Python 3.11+ with pandas, statsmodels, scikit-learn, matplotlib and pillow.

    python analysis/analyze.py <folder with codes_consensus.csv and sheets/key_DO_NOT_OPEN.csv>
    python analysis/sensitivity.py data
    python analysis/figures.py <project folder>

## Generation
All images were generated on 21 October 2026 (KST) through the consumer interfaces of Doubao, Meta AI and Tencent WorkBuddy, with a 1:1 aspect ratio and a new conversation for each prompt. Images are shared for research verification; reuse is subject to each platform's terms.

## Licence
Codebook, codes and scripts: CC BY 4.0.

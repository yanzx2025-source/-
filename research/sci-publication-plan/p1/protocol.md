# 图像生成实验方案 v0

## 自变量
- 模型 M（4 个，最终以可用性为准）：GPT 图像模型（OpenAI）、Gemini 图像模型（Google）、FLUX（开源，经 Replicate 或本机调用）、Midjourney（手动生成，可选）
- 提示策略 P（3 种）：
  - P1 自由：`A Peking opera costume for {role} in {play}, full-body, plain background`
  - P2 规制结构化：在 P1 后加入编码表中该角色的主服、主色、头戴、配件、面部要素
  - P3 结构化+参考：在 P2 基础上附 1 张权威图谱的参考图（仅支持图生图的模型）
- 角色 R：8 个（见 codebook_v0.md）
- 每格 5 张 → 4 × 3 × 8 × 5 = 480 张（P3 不可用的模型少 40 张）

## 控制
- 统一英文提示，固定分辨率 1024×1024，默认参数，记录模型版本、日期、种子
- 文件名：`{M}_{P}_{R}_{n}.png`；生成日志：`generation_log.csv`
- 编码前打乱文件顺序并隐去条件信息（盲编码）

## 因变量
- 每张图 D1–D6 违规（0/1），违规总数（0–6）

## 分析
- 违规率按 M、P、R、D 描述
- 混合效应逻辑回归：violation ~ M + P + D + (1|R)；稳健性检验加入 M×P 交互
- 软件：Python statsmodels 或 R lme4

# P3 生成单（长度匹配对照组）

**做法与 P1/P2 完全相同**：三个通道（豆包、Meta AI、WorkBuddy）；每条提示开一个新对话；画幅 1:1；只保留前三张；不追问、不重生成、不挑图。

**文件命名**：`{通道}_P3_{角色}_{序号}.jpg`，例如 `doubao_P3_R1_1.jpg`、`muse_P3_R1_1.jpg`、`hunyuan_P3_R1_1.jpg`。

**记录**：生成日期；WorkBuddy 的请求日志里 model 字段（确认仍是 hunyuan-image-alpha）；任何失败或异常。

共 8 条提示 × 3 个通道 × 3 张 = 72 张。

**同一天还要做一件事：P1 复测**（见文末）。P3 和原来的 P1/P2 不是同一天生成的，模型可能已经更新。同一天重跑一遍 P1、每格只留第 1 张（8 × 3 = 24 张），就能检查结果有没有随日期漂移。文件命名 `{通道}_P1re_{角色}_1.jpg`。复制下面整段英文，原样粘贴，不要改动。

## R1 Zhuge Liang

```
A traditional Peking opera stage costume for Zhuge Liang in the play Empty City Stratagem (Kongcheng Ji), laosheng (older male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The performer stands upright and still, facing the viewer, with the weight evenly balanced. The expression is calm. The figure is centred in the frame, with even margins above the head and below the feet.
```

## R2 Guan Yu

```
A traditional Peking opera stage costume for Guan Yu in the play Single Sword Meeting (Dandao Hui), hongsheng (red-faced male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The performer stands upright and still, facing the viewer, with the weight evenly balanced. The expression is calm. The figure is centred in the frame, with even margins above the head and below the feet.
```

## R3 Yang Yuhuan

```
A traditional Peking opera stage costume for Yang Yuhuan in the play The Drunken Concubine (Guifei Zui Jiu), huashan (female lead). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The performer stands upright and still, facing the viewer, with the weight evenly balanced. The expression is calm. The figure is centred in the frame, with even margins above the head and below the feet.
```

## R4 Mu Guiying

```
A traditional Peking opera stage costume for Mu Guiying in the play Mu Guiying Takes Command (Mu Guiying Gua Shuai), daomadan (martial female role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The performer stands upright and still, facing the viewer, with the weight evenly balanced. The expression is calm. The figure is centred in the frame, with even margins above the head and below the feet.
```

## R5 Bao Zheng

```
A traditional Peking opera stage costume for Bao Zheng in the play Case of Chen Shimei (Zha Mei An), tongchui hualian (painted-face role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The performer stands upright and still, facing the viewer, with the weight evenly balanced. The expression is calm. The figure is centred in the frame, with even margins above the head and below the feet.
```

## R6 Zhao Yun

```
A traditional Peking opera stage costume for Zhao Yun in the play Changban Slope (Changban Po), wusheng (martial male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The performer stands upright and still, facing the viewer, with the weight evenly balanced. The expression is calm. The figure is centred in the frame, with even margins above the head and below the feet.
```

## R7 Su San

```
A traditional Peking opera stage costume for Su San in the play Yu Tang Chun - Escorting the Prisoner (Qi Jie), qingyi (virtuous female role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The performer stands upright and still, facing the viewer, with the weight evenly balanced. The expression is calm. The figure is centred in the frame, with even margins above the head and below the feet.
```

## R8 Jiang Gan

```
A traditional Peking opera stage costume for Jiang Gan in the play Gathering of Heroes (Qunying Hui), wenchou (civil clown role). Full-body view of one performer, front-facing, plain light grey background, photographic realism. The performer stands upright and still, facing the viewer, with the weight evenly balanced. The expression is calm. The figure is centred in the frame, with even margins above the head and below the feet.
```

---

# P1 复测（与 P3 同一天；每条只保留第 1 张）

## R1 Zhuge Liang

```
A traditional Peking opera stage costume for Zhuge Liang in the play Empty City Stratagem (Kongcheng Ji), laosheng (older male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.
```

## R2 Guan Yu

```
A traditional Peking opera stage costume for Guan Yu in the play Single Sword Meeting (Dandao Hui), hongsheng (red-faced male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.
```

## R3 Yang Yuhuan

```
A traditional Peking opera stage costume for Yang Yuhuan in the play The Drunken Concubine (Guifei Zui Jiu), huashan (female lead). Full-body view of one performer, front-facing, plain light grey background, photographic realism.
```

## R4 Mu Guiying

```
A traditional Peking opera stage costume for Mu Guiying in the play Mu Guiying Takes Command (Mu Guiying Gua Shuai), daomadan (martial female role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.
```

## R5 Bao Zheng

```
A traditional Peking opera stage costume for Bao Zheng in the play Case of Chen Shimei (Zha Mei An), tongchui hualian (painted-face role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.
```

## R6 Zhao Yun

```
A traditional Peking opera stage costume for Zhao Yun in the play Changban Slope (Changban Po), wusheng (martial male role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.
```

## R7 Su San

```
A traditional Peking opera stage costume for Su San in the play Yu Tang Chun - Escorting the Prisoner (Qi Jie), qingyi (virtuous female role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.
```

## R8 Jiang Gan

```
A traditional Peking opera stage costume for Jiang Gan in the play Gathering of Heroes (Qunying Hui), wenchou (civil clown role). Full-body view of one performer, front-facing, plain light grey background, photographic realism.
```


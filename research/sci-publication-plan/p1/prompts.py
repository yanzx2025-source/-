"""Prompt templates shared by the generation scripts."""

BASE = "A traditional Peking opera stage costume for {role} in the play {play}, {hangdang}. Full-body view of one performer, front-facing, plain light grey background, photographic realism."
STRUCT = " The costume must follow Peking opera dress codes: {spec}."
# P3: length-matched control with no dress-code content (added after review, generated separately)
NEUTRAL = (" The performer stands upright and still, facing the viewer, with the weight evenly balanced."
           " The expression is calm. The figure is centred in the frame, with even margins above the head and below the feet.")


def prompt_for(r, strategy):
    p = BASE.format(**r)
    if strategy == "P3":
        return p + NEUTRAL
    return p if strategy == "P1" else p + STRUCT.format(**r)

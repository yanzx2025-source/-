"""Prompt templates shared by the generation scripts."""

BASE = "A traditional Peking opera stage costume for {role} in the play {play}, {hangdang}. Full-body view of one performer, front-facing, plain light grey background, photographic realism."
STRUCT = " The costume must follow Peking opera dress codes: {spec}."


def prompt_for(r, strategy):
    p = BASE.format(**r)
    return p if strategy == "P1" else p + STRUCT.format(**r)

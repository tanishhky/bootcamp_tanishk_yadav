import pandas as pd

def screen_patterns(holdings, betas):
    high_beta = [t for t, v in betas.items() if v["beta"] > 1.2]
    low_beta = [t for t, v in betas.items() if v["beta"] < 0.8]
    return {"High Beta": high_beta, "Low Beta": low_beta}

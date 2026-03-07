from pathlib import Path

p = Path("at2/attribution/attention.py")
s = p.read_text(encoding="utf-8")

# 1) Add mistral keyword to infer_model_type mapping (right after llama)
needle = '"llama": "llama",\n'
insert = '"llama": "llama",\n        "mistral": "mistral",\n'
if insert not in s:
    if needle not in s:
        raise RuntimeError("Could not find the llama mapping line to patch.")
    s = s.replace(needle, insert, 1)

# 2) Treat mistral like llama/qwen2/gemma3 branch in attention extraction
old = 'if model_type in ("llama", "qwen2", "gemma3"):'
new = 'if model_type in ("llama", "mistral", "qwen2", "gemma3"):'
if old in s and new not in s:
    s = s.replace(old, new, 1)

p.write_text(s, encoding="utf-8")
print("Patched:", p)
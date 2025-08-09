import json, re
from pathlib import Path
from datetime import datetime  # 加时间模块

# 根目录路径
root = Path(__file__).resolve().parent.parent

# 读取 links.json
data = json.loads((root / 'links.json').read_text(encoding='utf-8'))

# 添加当前 UTC 时间（比如 2025-08-08 15:30 UTC）
data["last_updated"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# 读取 README 模板
tpl = (root / 'README.tpl.md').read_text(encoding='utf-8')

# 渲染替换
def render(t, kv):
    for k, v in kv.items():
        t = re.sub(r"{{\s*" + re.escape(k) + r"\s*}}", v, t)
    return t

# 生成 README.md
out = render(tpl, data)
(root / 'README.md').write_text(out, encoding='utf-8')

print('README.md updated with timestamp.')

#!/usr/bin/env python3
"""抽取中文计划模板，用示例值填充后执行只读计划检查器。"""
from pathlib import Path
import json
import re
import subprocess

root = Path(__file__).resolve().parents[2]
folder = root / 'docs/localization'
source = root / 'skills/poteto-mode/playbooks/multi-phase-plan.md'
text = source.read_text()
match = re.search(r'^````markdown\n(.*?)^````\s*$', text, re.M | re.S)
if not match:
    raise SystemExit('未找到计划模板围栏')
example = re.sub(r'<[^>\n]+>', 'example', match[1])
output = folder / 'plan-template-example.md'
output.write_text(example)
command = ['node', str(root / 'skills/poteto-mode/scripts/check-plan.mjs'), str(output)]
result = subprocess.run(command, text=True, capture_output=True)
report = {'purpose': '仅验证文档模板兼容性；不执行模板中的命令和工作流', 'command': command, 'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
(folder / 'PLAN-CHECK.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(result.stdout, end='')
print(result.stderr, end='')
raise SystemExit(result.returncode)

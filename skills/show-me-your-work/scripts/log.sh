#!/usr/bin/env bash
# 向 show-me-your-work 决策日志（TSV）追加格式正确的一行。
# 用法：log.sh <logfile> <phase> <decision> <why> <evidence> <result>
set -euo pipefail

if [ "$#" -ne 6 ]; then
	printf 'usage: log.sh <logfile> <phase> <decision> <why> <evidence> <result>\n' >&2
	exit 1
fi

logfile="$1"
shift

logdir="$(dirname "$logfile")"
if [ -n "$logdir" ] && [ "$logdir" != "." ] && [ ! -d "$logdir" ]; then
	mkdir -p "$logdir"
fi

# 此处使用 `>>`，绝不使用 `>`。网络挂载可能让已有日志在此检查中误判。
# 这样代价只是一条多余表头，而非丢失原有数据行。
if [ ! -s "$logfile" ]; then
	printf 'ts\tphase\tdecision\twhy\tevidence\tresult\n' >> "$logfile"
fi

ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
# 去除制表符、换行和 CR，使单元格内容保持在一行。若单元格的首字符
# 会被电子表格解析为公式（=、+、-、@），则在前面加一个单引号。
# 此技能预期使用电子表格阅读日志，
# 因此攻击者可控的证据（PR 标题、文件名、
# 生成文本）绝不能在审查者打开文件时
# 变成公式执行。
clean() {
	local v
	v=$(printf '%s' "$1" | tr '\t\n\r' '   ')
	case "$v" in
		=*|+*|-*|@*) printf "'%s" "$v" ;;
		*) printf '%s' "$v" ;;
	esac
}
printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
	"$ts" "$(clean "$1")" "$(clean "$2")" "$(clean "$3")" "$(clean "$4")" "$(clean "$5")" \
	>> "$logfile"

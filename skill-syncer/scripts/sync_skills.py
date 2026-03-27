#!/usr/bin/env python3
"""
skill-syncer: /Users/woonyong/workspace/claude-skill → Cowork 세션 스킬 디렉토리 동기화
"""

import os
import shutil
from pathlib import Path

SOURCE_DIR = Path("/Users/woonyong/workspace/claude-skill")
SKILLS_PLUGIN_ROOT = Path.home() / "Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin"


def find_target_skills_dir() -> Path | None:
    """현재 활성 Cowork 세션의 skills 디렉토리를 동적으로 탐색한다."""
    if not SKILLS_PLUGIN_ROOT.exists():
        return None

    candidates = []

    for plugin_id_dir in SKILLS_PLUGIN_ROOT.iterdir():
        if not plugin_id_dir.is_dir():
            continue
        for session_id_dir in plugin_id_dir.iterdir():
            if not session_id_dir.is_dir():
                continue
            skills_dir = session_id_dir / "skills"
            if skills_dir.exists() and skills_dir.is_dir():
                mtime = max(
                    f.stat().st_mtime
                    for f in skills_dir.rglob("*")
                    if f.is_file()
                ) if any(skills_dir.rglob("*")) else skills_dir.stat().st_mtime
                candidates.append((mtime, skills_dir))

    if not candidates:
        return None

    candidates.sort(reverse=True)
    return candidates[0][1]


def sync_skill(skill_src: Path, target_dir: Path) -> str:
    """단일 스킬 폴더를 target_dir에 복사하고 상태를 반환한다."""
    dest = target_dir / skill_src.name

    if not dest.exists():
        shutil.copytree(skill_src, dest)
        return "added"
    else:
        # 소스와 대상의 SKILL.md 수정 시간 비교
        src_skill_md = skill_src / "SKILL.md"
        dst_skill_md = dest / "SKILL.md"

        src_mtime = src_skill_md.stat().st_mtime if src_skill_md.exists() else 0
        dst_mtime = dst_skill_md.stat().st_mtime if dst_skill_md.exists() else 0

        if src_mtime > dst_mtime:
            shutil.rmtree(dest)
            shutil.copytree(skill_src, dest)
            return "updated"
        else:
            return "skipped"


def main():
    if not SOURCE_DIR.exists():
        print(f"❌ 소스 디렉토리를 찾을 수 없습니다: {SOURCE_DIR}")
        return

    target_dir = find_target_skills_dir()
    if not target_dir:
        print("❌ Cowork 세션 스킬 디렉토리를 찾을 수 없습니다.")
        print(f"   확인 경로: {SKILLS_PLUGIN_ROOT}")
        return

    print(f"📂 소스:  {SOURCE_DIR}")
    print(f"📂 대상:  {target_dir}")
    print()

    added, updated, skipped = [], [], []

    skill_dirs = [
        d for d in SOURCE_DIR.iterdir()
        if d.is_dir() and not d.name.startswith(".") and (d / "SKILL.md").exists()
    ]

    if not skill_dirs:
        print("⚠️  소스 디렉토리에 SKILL.md를 가진 스킬 폴더가 없습니다.")
        return

    for skill_dir in sorted(skill_dirs):
        status = sync_skill(skill_dir, target_dir)
        if status == "added":
            added.append(skill_dir.name)
        elif status == "updated":
            updated.append(skill_dir.name)
        else:
            skipped.append(skill_dir.name)

    print("✅ 동기화 완료\n")
    if added:
        print(f"  🆕 추가됨    : {', '.join(added)}")
    if updated:
        print(f"  🔄 업데이트됨 : {', '.join(updated)}")
    if skipped:
        print(f"  ⏭️  변경 없음  : {', '.join(skipped)}")

    if added:
        print("\n⚠️  새로 추가된 스킬은 다음 대화 세션부터 트리거됩니다.")
    if updated:
        print("ℹ️  업데이트된 스킬은 현재 세션에서도 즉시 반영됩니다.")


if __name__ == "__main__":
    main()

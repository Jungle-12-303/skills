---
name: skill-syncer
description: Sync custom skills from the user's local skill workspace (/Users/woonyong/workspace/claude-skill) into the active Cowork session so Claude can use them immediately. Use this skill whenever the user says things like "스킬 동기화해줘", "스킬 업데이트해줘", "내 스킬 반영해줘", "새 스킬 적용해줘", or "sync my skills". Also trigger when the user mentions they've updated or created a skill in their workspace and wants Claude to pick it up.
---

# Skill Syncer

사용자가 `/Users/woonyong/workspace/claude-skill`에 만들거나 수정한 스킬을 현재 Cowork 세션에 즉시 반영한다.

## 동작 흐름

1. `scripts/sync_skills.py`를 실행해 소스 스킬을 현재 세션 스킬 디렉토리에 복사한다.
2. 결과(추가/업데이트/스킵된 스킬 목록)를 사용자에게 보고한다.
3. 세션을 재시작해야 반영되는 경우 안내한다.

## 실행 방법

Desktop Commander의 `start_process`로 스크립트를 실행한다:

```bash
python3 /Users/woonyong/workspace/claude-skill/skill-syncer/scripts/sync_skills.py
```

실행 후 출력 결과를 읽어 사용자에게 요약해서 보고한다.

## 결과 보고 형식

스크립트 실행 결과를 아래 형식으로 정리해서 전달한다:

```
✅ 동기화 완료

추가된 스킬: [스킬명 목록]
업데이트된 스킬: [스킬명 목록]
변경 없음: [스킬명 목록]

⚠️ 새로 추가된 스킬은 다음 대화 세션부터 트리거됩니다.
기존 스킬 업데이트는 현재 세션에서도 즉시 반영됩니다.
```

## 주의사항

- 스크립트가 세션 디렉토리를 자동으로 탐색하므로 세션 ID가 바뀌어도 정상 동작한다.
- 소스 디렉토리에 `skill-syncer` 폴더 자체도 있으면 함께 동기화된다(자기 자신 포함).
- 동기화는 단방향이다(소스 → Cowork). Cowork 쪽 변경은 소스에 반영되지 않는다.

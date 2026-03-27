# claude-skill

Claude Code / Cowork에서 사용하는 커스텀 스킬 모음입니다.

## 스킬 목록

### commit-convention

영문 타입과 한국어 제목을 조합하는 [Conventional Commits](https://www.conventionalcommits.org/) 기반 커밋 메시지 가이드.

**위치:** `commit-convention/SKILL.md`

**주요 기능:**
- 변경 요약으로부터 커밋 메시지 후보 1~3개 생성
- 영문 타입 + 한국어 제목/본문 형식 준수
- Breaking change 푸터(영문) 지원

**커밋 형식:**
```
<type>: <한국어 제목>
```

**허용 타입:** `feat` `fix` `refactor` `docs` `test` `chore` `style` `perf` `build` `ci` `revert`

---

### skill-syncer

이 저장소의 스킬을 현재 활성 Cowork 세션에 자동으로 동기화한다.

**위치:** `skill-syncer/SKILL.md`

**주요 기능:**
- `scripts/sync_skills.py`로 소스 스킬을 Cowork 세션 스킬 디렉토리에 복사
- 세션 ID가 바뀌어도 자동으로 대상 경로를 탐색
- 추가 / 업데이트 / 변경 없음 상태를 구분해서 보고

**트리거 예시:** "스킬 동기화해줘", "스킬 업데이트해줘", "내 스킬 반영해줘"

## 사용법

### 자동 동기화 (권장)

`skill-syncer` 스킬이 Cowork에 등록된 경우, 이 저장소에서 스킬을 추가하거나 수정한 뒤
Claude에게 "스킬 동기화해줘"라고 하면 자동으로 반영됩니다.

### 수동 실행

```bash
python3 /Users/woonyong/workspace/claude-skill/skill-syncer/scripts/sync_skills.py
```

> 새로 **추가**된 스킬은 다음 대화 세션부터, **업데이트**된 스킬은 현재 세션에서도 즉시 반영됩니다.

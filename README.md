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

## 사용법

스킬을 사용할 프로젝트의 `.claude/skills/` 경로에 해당 스킬 폴더를 복사하세요.

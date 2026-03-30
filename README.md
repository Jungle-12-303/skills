# skills

Claude Code와 Codex에서 공통으로 사용할 수 있는 커스텀 스킬 모음입니다.

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

### github

GitHub 저장소 작업을 터미널에서 일관된 형식으로 처리하는 자동화 스킬.

**위치:** `github/SKILL.md`

**주요 기능:**
- `gh` CLI 기반으로 PR, 이슈, Actions, 릴리즈, 알림, README 업데이트 처리
- `conventions/` 규칙을 읽어 한국어 중심 출력 형식과 템플릿 적용
- 기본 저장소를 설정 파일 또는 현재 git remote에서 자동 감지

**설정 파일:**
```bash
~/.config/skills/github.env
```

---

### skill-syncer

이 저장소의 스킬을 Claude와 Codex 환경에 자동으로 동기화한다.

**위치:** `skill-syncer/SKILL.md`

**주요 기능:**
- `scripts/sync_skills.py`로 소스 스킬을 Claude/Codex 스킬 디렉토리에 복사
- `--target claude|codex|all`로 대상을 선택하거나 동시에 반영
- 파일 내용 기준으로 변경 여부를 비교해 추가 / 업데이트 / 변경 없음 상태를 보고

**트리거 예시:** "스킬 동기화해줘", "스킬 업데이트해줘", "내 스킬 반영해줘"

## 사용법

### 자동 동기화 (권장)

`skill-syncer` 스킬이 등록된 환경에서는 이 저장소에서 스킬을 추가하거나 수정한 뒤
"스킬 동기화해줘"라고 요청하면 대상 도구에 반영할 수 있다.

### 수동 실행

저장소를 클론한 경로에서 스크립트를 직접 실행한다.

```bash
python3 /path/to/skills/skill-syncer/scripts/sync_skills.py --target all
```

Claude에만 반영하려면 다음처럼 실행한다.

```bash
python3 /path/to/skills/skill-syncer/scripts/sync_skills.py --target claude
```

Codex에만 반영하려면 다음처럼 실행한다.

```bash
python3 /path/to/skills/skill-syncer/scripts/sync_skills.py --target codex
```

소스 디렉토리를 명시적으로 지정하려면 환경변수를 사용한다.

```bash
SKILL_SOURCE_DIR=/path/to/skills python3 /path/to/skills/skill-syncer/scripts/sync_skills.py --target all
```

## 설정

### GitHub 기본 저장소

`github` 스킬은 아래 설정 파일을 우선적으로 읽는다.

```bash
mkdir -p ~/.config/skills
cat <<'EOF' > ~/.config/skills/github.env
GITHUB_DEFAULT_OWNER=woonyong-kr
GITHUB_DEFAULT_REPO=my-repo
EOF
```

환경변수가 없으면 현재 git 저장소의 `origin` remote에서 저장소를 자동 감지한다.

## 주의사항

- 새로 추가된 스킬은 도구에 따라 다음 세션부터 인식될 수 있다.
- 기존 스킬 업데이트는 현재 세션에서 바로 반영될 수 있다.
- 이 저장소는 스킬 소스 저장소이고, 실제 사용 디렉토리와는 별개다.

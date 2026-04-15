# Skills

Codex와 Claude Code에서 바로 불러 쓸 수 있는 실전 스킬 185개를 모아둔 저장소입니다.
이 레포는 스킬의 소스 오브 트루스 역할을 하며, 각 폴더가 하나의 스킬이고 `SKILL.md`가 진입점입니다. 일부 스킬은 설명 문서만 들어 있고, 일부는 `scripts/`, `hooks/`, `references/`, `conventions/` 같은 보조 자산을 함께 포함합니다.

## 한눈에 보기

| 항목 | 내용 |
| --- | --- |
| 저장소 성격 | 개인/팀용 AI 에이전트 스킬 소스 저장소 |
| 현재 스킬 수 | `185`개 |
| 주 사용 대상 | `Codex`, `Claude Code`, `SKILL.md` 폴더를 읽는 에이전트 하니스 |
| 설치 방식 | 원하는 스킬만 복사하거나 `skill-syncer`로 동기화 |
| 대표 분야 | 개발 워크플로우, 에이전트 운영, GitHub 오퍼레이션, 리서치, 콘텐츠, 비즈니스 운영, 도메인 특화 지식 |
| 시작 추천 | `commit-convention`, `coding-standards`, `search-first`, `documentation-lookup`, `tdd-workflow`, `verification-loop`, `terminal-ops`, `skill-syncer` |

## 이 저장소로 무엇을 할 수 있나

이 저장소는 단순히 “코드 잘 짜는 법”만 모아둔 컬렉션이 아닙니다. 실제로는 아래 일을 빠르게 실행하기 위한 작업 레이어에 가깝습니다.

- Git과 협업: 커밋 메시지, 브랜치 전략, PR/이슈 처리, GitHub 운영 자동화
- 개발 생산성: TDD, 검증 루프, 코드 품질, 문서 조회, 성능 측정, 회귀 방지
- 에이전트 엔지니어링: 멀티 에이전트 분업, 오토메이션, 루프 설계, 평가 하네스, 컨텍스트 최적화
- 프론트엔드와 UI: React/Next.js/Nuxt 패턴, 디자인 시스템, UI 검증, 데모 제작, 슬라이드 제작
- 백엔드와 아키텍처: REST API, 헥사고널 구조, 마이그레이션, 배포, Docker, DB 설계
- 언어/프레임워크별 패턴: Django, Laravel, Spring Boot, NestJS, Go, Python, Kotlin, Rust, Dart, Swift, .NET, C++, Perl
- 리서치와 문서화: 심층 리서치, 문서 기반 답변, 시장 조사, ADR, 코드 투어, 온보딩 가이드
- 콘텐츠와 성장: 아티클 작성, 보이스 추출, 소셜 콘텐츠, 투자자 자료, 아웃리치
- 운영과 비즈니스: GitHub/Jira/Google Workspace, 빌링, 이메일, 메시지, 알림, 워크플로우 정리
- 특화 도메인: 헬스케어, 물류, 무역/통관, 제조, 에너지, 공급망, Web3 보안

## 빠른 시작

### 1. 저장소 받기

```bash
git clone https://github.com/Jungle-12-303/skills.git ~/workspace/skills
cd ~/workspace/skills
```

### 2. Codex에 동기화

Codex는 기본적으로 `~/.codex/skills`를 사용합니다.

```bash
python3 skill-syncer/scripts/sync_skills.py --target codex
```

### 3. Claude Code에 동기화

Claude는 활성 세션의 스킬 디렉터리를 동적으로 찾습니다. Claude Desktop 또는 Claude Code 세션이 켜져 있는 상태에서 실행하는 편이 안전합니다.

```bash
python3 skill-syncer/scripts/sync_skills.py --target claude
```

### 4. 둘 다 한 번에 동기화

```bash
python3 skill-syncer/scripts/sync_skills.py --target all
```

### 5. 특정 스킬만 직접 설치

Codex에 일부 스킬만 넣고 싶다면 폴더째 복사하면 됩니다.

```bash
mkdir -p ~/.codex/skills
cp -R commit-convention ~/.codex/skills/
cp -R tdd-workflow ~/.codex/skills/
cp -R verification-loop ~/.codex/skills/
```

Claude는 세션별 경로를 쓰기 때문에 직접 복사보다 `skill-syncer` 사용을 권장합니다.

### 6. 업데이트 반영

```bash
git pull
python3 skill-syncer/scripts/sync_skills.py --target all
```

`skill-syncer`는 아래처럼 동작합니다.

- 소스 디렉터리의 모든 스킬 폴더를 검사합니다.
- 대상 디렉터리와 파일 해시를 비교합니다.
- 새 스킬은 추가하고, 내용이 바뀐 스킬은 업데이트하고, 변동이 없으면 건너뜁니다.
- 새로 추가된 스킬은 도구에 따라 다음 세션부터 인식될 수 있습니다.

## 세팅 옵션과 환경 변수

기본 설정을 그대로 써도 되지만, 다른 경로를 쓰고 싶다면 환경 변수를 덮어쓸 수 있습니다.

### 기본값

- 소스 경로: 현재 레포 루트 또는 `SKILL_SOURCE_DIR`
- Codex 대상 경로: `~/.codex/skills`
- Claude plugin root: `~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin`

### 커스텀 예시

```bash
SKILL_SOURCE_DIR=/Users/you/workspace/skills \
CODEX_SKILLS_DIR=/Users/you/.codex/skills \
python3 skill-syncer/scripts/sync_skills.py --target codex
```

```bash
CLAUDE_SKILLS_PLUGIN_ROOT="/Users/you/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin" \
python3 skill-syncer/scripts/sync_skills.py --target claude
```

## 처음 쓰는 사람을 위한 추천 스타터 팩

### 1. 기본 개발 팩

- [`commit-convention`](commit-convention/SKILL.md): 한국어 커밋 메시지와 Git 워크플로우 정리
- [`coding-standards`](coding-standards/SKILL.md): 언어 공통 코드 품질 기준
- [`search-first`](search-first/SKILL.md): 구현 전에 기존 도구와 패턴부터 찾기
- [`documentation-lookup`](documentation-lookup/SKILL.md): 최신 공식 문서 우선 조회
- [`tdd-workflow`](tdd-workflow/SKILL.md): 테스트 우선 개발 흐름
- [`verification-loop`](verification-loop/SKILL.md): 구현 후 검증 루프
- [`terminal-ops`](terminal-ops/SKILL.md): 명령 실행과 증거 기반 보고
- [`skill-syncer`](skill-syncer/SKILL.md): 로컬 스킬을 Codex/Claude에 반영

### 2. GitHub 운영 팩

- [`github`](github/SKILL.md): PR, 이슈, CI/CD, 릴리즈, README 작업
- [`github-ops`](github-ops/SKILL.md): 저장소 운영과 커뮤니티 관리
- [`github-issue-manager`](github-issue-manager/SKILL.md): 이슈 상태/링크/결과 댓글 정리
- [`project-flow-ops`](project-flow-ops/SKILL.md): GitHub와 Linear 실행 흐름 정리
- [`unified-notifications-ops`](unified-notifications-ops/SKILL.md): 알림 체계 통합

### 3. 프론트엔드/UI 팩

- [`frontend-patterns`](frontend-patterns/SKILL.md): React/Next.js 중심 UI 패턴
- [`frontend-design`](frontend-design/SKILL.md): 시각 완성도 중심 UI 제작
- [`design-system`](design-system/SKILL.md): 디자인 시스템/스타일 일관성 점검
- [`e2e-testing`](e2e-testing/SKILL.md): Playwright E2E 테스트
- [`browser-qa`](browser-qa/SKILL.md): 실제 브라우저 QA
- [`ui-demo`](ui-demo/SKILL.md): UI 데모 영상 제작

### 4. 백엔드/API 팩

- [`backend-patterns`](backend-patterns/SKILL.md): 서버 패턴과 API 구조
- [`api-design`](api-design/SKILL.md): REST API 설계 원칙
- [`database-migrations`](database-migrations/SKILL.md): 안전한 스키마/데이터 마이그레이션
- [`deployment-patterns`](deployment-patterns/SKILL.md): 배포와 롤백 전략
- [`docker-mounted-workspace`](docker-mounted-workspace/SKILL.md): 현재 워크스페이스를 마운트한 실행 중 컨테이너를 찾아 내부 명령 실행
- [`docker-patterns`](docker-patterns/SKILL.md): Docker/Docker Compose 운영
- [`postgres-patterns`](postgres-patterns/SKILL.md): PostgreSQL 설계와 성능

### 5. 에이전트 시스템 팩

- [`agentic-engineering`](agentic-engineering/SKILL.md): 에이전트 엔지니어링 운영 방식
- [`autonomous-agent-harness`](autonomous-agent-harness/SKILL.md): 자율 에이전트 시스템 설계
- [`dmux-workflows`](dmux-workflows/SKILL.md): 멀티 에이전트 분업
- [`eval-harness`](eval-harness/SKILL.md): 평가 중심 개발
- [`santa-method`](santa-method/SKILL.md): 다중 검증 리뷰 방식
- [`context-budget`](context-budget/SKILL.md): 컨텍스트 비용 최적화

### 6. 리서치/콘텐츠 팩

- [`deep-research`](deep-research/SKILL.md): 다중 출처 심층 리서치
- [`research-ops`](research-ops/SKILL.md): 현재 상태 조사 워크플로우
- [`article-writing`](article-writing/SKILL.md): 긴 형식의 문서/가이드 작성
- [`brand-voice`](brand-voice/SKILL.md): 글쓰기 톤 추출
- [`content-engine`](content-engine/SKILL.md): 플랫폼별 콘텐츠 시스템 구축
- [`market-research`](market-research/SKILL.md): 시장/경쟁 조사

## 스킬은 어떻게 사용하는가

이 저장소의 스킬은 “명령어 모음”이 아니라 “작업 방식 패키지”입니다. 보통은 아래 셋 중 하나로 사용합니다.

### 1. 스킬 이름을 직접 말하기

- “`commit-convention` 기준으로 커밋 메시지 정리해줘”
- “`github-ops` 방식으로 이 저장소 PR backlog 정리해줘”
- “`article-writing` 톤으로 README 다시 써줘”

### 2. 작업 의도를 자연어로 말하기

하니스가 트리거 규칙을 읽는 구조라면 이름을 직접 말하지 않아도 됩니다.

- “PR 상태 확인하고 코멘트까지 달아줘”
- “Django API 테스트 전략 잡아줘”
- “투자자 업데이트 메일 써줘”
- “이 프로젝트에 어떤 스킬이 필요한지 골라줘”

### 3. 여러 스킬을 조합하기

실전에서는 조합이 가장 강력합니다.

- 문서 기반 구현: `documentation-lookup` + `tdd-workflow` + `verification-loop`
- GitHub 운영: `github` + `github-issue-manager` + `project-flow-ops`
- 글쓰기: `brand-voice` + `article-writing`
- 조사 후 제안: `research-ops` + `market-research` + `investor-materials`
- 멀티 에이전트 검증: `dmux-workflows` + `eval-harness` + `santa-method`

## 어떤 종류의 스킬이 들어 있는가

### 개발 워크플로우와 품질

코드 작성 자체보다 “어떻게 안전하게 만들고 검증할 것인가”에 초점이 맞춰진 스킬들입니다.

- 핵심 스킬: [`coding-standards`](coding-standards/SKILL.md), [`tdd-workflow`](tdd-workflow/SKILL.md), [`verification-loop`](verification-loop/SKILL.md), [`ai-regression-testing`](ai-regression-testing/SKILL.md), [`benchmark`](benchmark/SKILL.md), [`terminal-ops`](terminal-ops/SKILL.md)
- 언제 쓰나: 새 기능 구현, 버그 수정, 리팩터링, 회귀 방지, 릴리즈 전 검증

### Git, GitHub, 프로젝트 운영

실제 저장소 운영과 협업 흐름을 정리하는 스킬들입니다.

- 핵심 스킬: [`commit-convention`](commit-convention/SKILL.md), [`github`](github/SKILL.md), [`github-ops`](github-ops/SKILL.md), [`github-issue-manager`](github-issue-manager/SKILL.md), [`project-flow-ops`](project-flow-ops/SKILL.md), [`unified-notifications-ops`](unified-notifications-ops/SKILL.md)
- 언제 쓰나: 이슈/PR 정리, CI 확인, 릴리즈, 리뷰 반영, 알림 체계 통합

### 에이전트/자동화/멀티 에이전트

에이전트를 하나의 코드 작성 도구가 아니라 운영 시스템으로 다루는 스킬들입니다.

- 핵심 스킬: [`agentic-engineering`](agentic-engineering/SKILL.md), [`autonomous-agent-harness`](autonomous-agent-harness/SKILL.md), [`autonomous-loops`](autonomous-loops/SKILL.md), [`continuous-agent-loop`](continuous-agent-loop/SKILL.md), [`claude-devfleet`](claude-devfleet/SKILL.md), [`dmux-workflows`](dmux-workflows/SKILL.md), [`team-builder`](team-builder/SKILL.md), [`santa-method`](santa-method/SKILL.md), [`agent-sort`](agent-sort/SKILL.md)
- 언제 쓰나: 병렬 분업, 장기 실행 에이전트, 자동화 감사, 에이전트 평가 체계 설계

### 프론트엔드, 디자인, 데모/미디어

UI를 예쁘게 만드는 수준을 넘어서, 디자인 시스템과 검증, 발표/시연물까지 연결하는 스킬들입니다.

- 핵심 스킬: [`frontend-patterns`](frontend-patterns/SKILL.md), [`frontend-design`](frontend-design/SKILL.md), [`design-system`](design-system/SKILL.md), [`frontend-slides`](frontend-slides/SKILL.md), [`browser-qa`](browser-qa/SKILL.md), [`ui-demo`](ui-demo/SKILL.md), [`video-editing`](video-editing/SKILL.md), [`videodb`](videodb/SKILL.md), [`manim-video`](manim-video/SKILL.md), [`fal-ai-media`](fal-ai-media/SKILL.md)
- 언제 쓰나: 제품 UI 구현, 디자인 검토, 시연 영상 제작, 발표 자료 제작

### 백엔드, API, 데이터, 인프라

서비스 구조와 배포, DB, API, 운영 안정성을 다루는 스킬들입니다.

- 핵심 스킬: [`backend-patterns`](backend-patterns/SKILL.md), [`api-design`](api-design/SKILL.md), [`hexagonal-architecture`](hexagonal-architecture/SKILL.md), [`api-connector-builder`](api-connector-builder/SKILL.md), [`mcp-server-patterns`](mcp-server-patterns/SKILL.md), [`database-migrations`](database-migrations/SKILL.md), [`deployment-patterns`](deployment-patterns/SKILL.md), [`docker-mounted-workspace`](docker-mounted-workspace/SKILL.md), [`docker-patterns`](docker-patterns/SKILL.md), [`postgres-patterns`](postgres-patterns/SKILL.md), [`clickhouse-io`](clickhouse-io/SKILL.md)
- 언제 쓰나: API 설계, 서비스 분리, 데이터 모델링, 배포 파이프라인 정리, 현재 채팅에서 컨테이너 내부 재현 실행

### 언어/프레임워크별 전문 팩

언어와 프레임워크별로 좀 더 구체적인 구현/테스트/보안/검증 규칙을 담고 있습니다.

- Django: [`django-patterns`](django-patterns/SKILL.md), [`django-security`](django-security/SKILL.md), [`django-tdd`](django-tdd/SKILL.md), [`django-verification`](django-verification/SKILL.md)
- Laravel: [`laravel-patterns`](laravel-patterns/SKILL.md), [`laravel-security`](laravel-security/SKILL.md), [`laravel-tdd`](laravel-tdd/SKILL.md), [`laravel-verification`](laravel-verification/SKILL.md), [`laravel-plugin-discovery`](laravel-plugin-discovery/SKILL.md)
- Spring/Java/Kotlin: [`springboot-patterns`](springboot-patterns/SKILL.md), [`springboot-security`](springboot-security/SKILL.md), [`springboot-tdd`](springboot-tdd/SKILL.md), [`springboot-verification`](springboot-verification/SKILL.md), [`java-coding-standards`](java-coding-standards/SKILL.md), [`kotlin-patterns`](kotlin-patterns/SKILL.md), [`kotlin-testing`](kotlin-testing/SKILL.md), [`kotlin-coroutines-flows`](kotlin-coroutines-flows/SKILL.md), [`kotlin-exposed-patterns`](kotlin-exposed-patterns/SKILL.md), [`kotlin-ktor-patterns`](kotlin-ktor-patterns/SKILL.md), [`jpa-patterns`](jpa-patterns/SKILL.md)
- JS/TS/Nest/Next/Nuxt: [`nestjs-patterns`](nestjs-patterns/SKILL.md), [`nextjs-turbopack`](nextjs-turbopack/SKILL.md), [`nuxt4-patterns`](nuxt4-patterns/SKILL.md), [`bun-runtime`](bun-runtime/SKILL.md), [`nodejs-keccak256`](nodejs-keccak256/SKILL.md)
- Go/Python/Rust/Swift/Dart/.NET/C++/Perl: [`golang-patterns`](golang-patterns/SKILL.md), [`golang-testing`](golang-testing/SKILL.md), [`python-patterns`](python-patterns/SKILL.md), [`python-testing`](python-testing/SKILL.md), [`rust-patterns`](rust-patterns/SKILL.md), [`rust-testing`](rust-testing/SKILL.md), [`swiftui-patterns`](swiftui-patterns/SKILL.md), [`swift-concurrency-6-2`](swift-concurrency-6-2/SKILL.md), [`swift-protocol-di-testing`](swift-protocol-di-testing/SKILL.md), [`swift-actor-persistence`](swift-actor-persistence/SKILL.md), [`dart-flutter-patterns`](dart-flutter-patterns/SKILL.md), [`flutter-dart-code-review`](flutter-dart-code-review/SKILL.md), [`dotnet-patterns`](dotnet-patterns/SKILL.md), [`csharp-testing`](csharp-testing/SKILL.md), [`cpp-coding-standards`](cpp-coding-standards/SKILL.md), [`cpp-testing`](cpp-testing/SKILL.md), [`perl-patterns`](perl-patterns/SKILL.md), [`perl-security`](perl-security/SKILL.md), [`perl-testing`](perl-testing/SKILL.md)
- Android/Compose: [`android-clean-architecture`](android-clean-architecture/SKILL.md), [`compose-multiplatform-patterns`](compose-multiplatform-patterns/SKILL.md)

### 리서치, 문서, 글쓰기, 콘텐츠

정확한 정보 정리, 시장 조사, 글쓰기, 배포용 콘텐츠 제작에 맞춘 스킬들입니다.

- 핵심 스킬: [`deep-research`](deep-research/SKILL.md), [`exa-search`](exa-search/SKILL.md), [`research-ops`](research-ops/SKILL.md), [`market-research`](market-research/SKILL.md), [`article-writing`](article-writing/SKILL.md), [`brand-voice`](brand-voice/SKILL.md), [`content-engine`](content-engine/SKILL.md), [`crosspost`](crosspost/SKILL.md), [`investor-materials`](investor-materials/SKILL.md), [`investor-outreach`](investor-outreach/SKILL.md), [`code-tour`](code-tour/SKILL.md), [`architecture-decision-records`](architecture-decision-records/SKILL.md), [`codebase-onboarding`](codebase-onboarding/SKILL.md)
- 언제 쓰나: 가이드 작성, 시장 조사, 펀드레이징 자료, 팀 온보딩 문서화

### 운영 툴과 비즈니스 오퍼레이션

개발 외부의 실무 운영을 AI 워크플로우에 연결하는 스킬들입니다.

- 핵심 스킬: [`finance-billing-ops`](finance-billing-ops/SKILL.md), [`customer-billing-ops`](customer-billing-ops/SKILL.md), [`email-ops`](email-ops/SKILL.md), [`messages-ops`](messages-ops/SKILL.md), [`google-workspace-ops`](google-workspace-ops/SKILL.md), [`jira-integration`](jira-integration/SKILL.md), [`knowledge-ops`](knowledge-ops/SKILL.md), [`workspace-surface-audit`](workspace-surface-audit/SKILL.md), [`x-api`](x-api/SKILL.md)
- 언제 쓰나: 청구/환불 판단, 문서/시트 운영, 메일/메시지 처리, 도구 체계 정리

### 보안, Web3, 특화 도메인

범용 앱보다 더 강한 제약과 도메인 지식이 필요한 작업에 대응합니다.

- 보안/Web3: [`security-review`](security-review/SKILL.md), [`security-scan`](security-scan/SKILL.md), [`security-bounty-hunter`](security-bounty-hunter/SKILL.md), [`defi-amm-security`](defi-amm-security/SKILL.md), [`llm-trading-agent-security`](llm-trading-agent-security/SKILL.md), [`evm-token-decimals`](evm-token-decimals/SKILL.md)
- 헬스케어: [`healthcare-cdss-patterns`](healthcare-cdss-patterns/SKILL.md), [`healthcare-emr-patterns`](healthcare-emr-patterns/SKILL.md), [`healthcare-eval-harness`](healthcare-eval-harness/SKILL.md), [`healthcare-phi-compliance`](healthcare-phi-compliance/SKILL.md), [`hipaa-compliance`](hipaa-compliance/SKILL.md)
- 공급망/제조/무역: [`carrier-relationship-management`](carrier-relationship-management/SKILL.md), [`customs-trade-compliance`](customs-trade-compliance/SKILL.md), [`inventory-demand-planning`](inventory-demand-planning/SKILL.md), [`logistics-exception-management`](logistics-exception-management/SKILL.md), [`returns-reverse-logistics`](returns-reverse-logistics/SKILL.md), [`production-scheduling`](production-scheduling/SKILL.md), [`quality-nonconformance`](quality-nonconformance/SKILL.md), [`energy-procurement`](energy-procurement/SKILL.md)

## 저장소 구조

모든 스킬은 폴더 단위로 배포됩니다.

```text
skills/
├── README.md
├── <skill-name>/
│   ├── SKILL.md
│   ├── scripts/        # 선택
│   ├── hooks/          # 선택
│   ├── references/     # 선택
│   ├── conventions/    # 선택
│   └── assets/         # 선택
└── skill-syncer/
    ├── SKILL.md
    └── scripts/sync_skills.py
```

`SKILL.md`는 보통 아래 정보를 포함합니다.

- `name`: 스킬 이름
- `description`: 언제 쓰는지 요약
- `origin`: 출처나 계보
- `When to Activate`: 트리거 조건
- `Workflow` 또는 `Core Rules`: 실제 작업 방식
- `Examples` 또는 `Quality Gate`: 예시와 검증 기준

## 스킬 추가/수정 시 기준

새 스킬을 만들 때는 폴더 하나를 만들고 `SKILL.md`부터 작성하는 방식이 가장 단순합니다.

```markdown
---
name: skill-name
description: 이 스킬이 언제 필요한지 한 줄로 설명
origin: personal
---

# Skill Title

## When to Activate
- 어떤 요청에서 써야 하는지

## Workflow
- 어떤 순서로 작업하는지

## Quality Gate
- 결과를 어떤 기준으로 검증하는지
```

원칙은 단순합니다.

- 폴더 이름과 스킬 이름은 가급적 맞춥니다.
- 스킬은 “정보”보다 “작업 방식”을 담는 편이 좋습니다.
- 외부 도구나 인증이 필요하면 `SKILL.md`에 전제 조건을 명시합니다.
- 스크립트가 있으면 스킬 본문에서 경로와 실행 방법을 같이 적습니다.

## 문제 해결

### Claude 대상 동기화가 안 될 때

- Claude 세션이 실제로 열려 있는지 확인합니다.
- `skill-syncer`는 활성 세션의 skills 디렉터리를 찾는 방식이라, 세션이 없으면 대상을 못 찾을 수 있습니다.
- 필요하면 `CLAUDE_SKILLS_PLUGIN_ROOT`를 직접 지정합니다.

### Codex에서 스킬이 안 보일 때

- `~/.codex/skills`에 실제로 폴더가 복사됐는지 확인합니다.
- 새로 추가한 스킬은 다음 세션부터 인식될 수 있습니다.
- 이미 있던 스킬의 내용 변경은 현재 세션에서 바로 반영될 수도 있습니다.

### 어떤 스킬을 먼저 넣어야 할지 모를 때

- 저장소 전체를 다 넣기보다 스타터 팩부터 시작하는 편이 좋습니다.
- [`agent-sort`](agent-sort/SKILL.md), [`workspace-surface-audit`](workspace-surface-audit/SKILL.md), [`configure-ecc`](configure-ecc/SKILL.md)를 먼저 읽으면 선택 기준을 잡기 쉽습니다.

### 스킬은 있는데 전제 도구가 없을 때

- 일부 스킬은 `gh`, Playwright, MCP 서버, 외부 SaaS 연결, 특정 환경변수를 요구합니다.
- 이 경우 README보다 각 `SKILL.md`의 prerequisites 섹션을 먼저 확인해야 합니다.

## 전체 스킬 인덱스

아래 목록은 현재 저장소에 있는 전체 스킬 폴더를 알파벳순으로 정리한 것입니다.

<details>
<summary><strong>A-C</strong> (50)</summary>

[`agent-eval`](agent-eval/SKILL.md), [`agent-harness-construction`](agent-harness-construction/SKILL.md), [`agent-introspection-debugging`](agent-introspection-debugging/SKILL.md), [`agent-payment-x402`](agent-payment-x402/SKILL.md), [`agent-sort`](agent-sort/SKILL.md), [`agentic-engineering`](agentic-engineering/SKILL.md), [`ai-first-engineering`](ai-first-engineering/SKILL.md), [`ai-regression-testing`](ai-regression-testing/SKILL.md), [`android-clean-architecture`](android-clean-architecture/SKILL.md), [`api-connector-builder`](api-connector-builder/SKILL.md), [`api-design`](api-design/SKILL.md), [`architecture-decision-records`](architecture-decision-records/SKILL.md), [`article-writing`](article-writing/SKILL.md), [`automation-audit-ops`](automation-audit-ops/SKILL.md), [`autonomous-agent-harness`](autonomous-agent-harness/SKILL.md), [`autonomous-loops`](autonomous-loops/SKILL.md), [`backend-patterns`](backend-patterns/SKILL.md), [`benchmark`](benchmark/SKILL.md), [`blueprint`](blueprint/SKILL.md), [`brand-voice`](brand-voice/SKILL.md), [`browser-qa`](browser-qa/SKILL.md), [`bun-runtime`](bun-runtime/SKILL.md), [`canary-watch`](canary-watch/SKILL.md), [`carrier-relationship-management`](carrier-relationship-management/SKILL.md), [`ck`](ck/SKILL.md), [`claude-api`](claude-api/SKILL.md), [`claude-devfleet`](claude-devfleet/SKILL.md), [`click-path-audit`](click-path-audit/SKILL.md), [`clickhouse-io`](clickhouse-io/SKILL.md), [`code-tour`](code-tour/SKILL.md), [`codebase-onboarding`](codebase-onboarding/SKILL.md), [`coding-standards`](coding-standards/SKILL.md), [`commit-convention`](commit-convention/SKILL.md), [`compose-multiplatform-patterns`](compose-multiplatform-patterns/SKILL.md), [`configure-ecc`](configure-ecc/SKILL.md), [`connections-optimizer`](connections-optimizer/SKILL.md), [`content-engine`](content-engine/SKILL.md), [`content-hash-cache-pattern`](content-hash-cache-pattern/SKILL.md), [`context-budget`](context-budget/SKILL.md), [`continuous-agent-loop`](continuous-agent-loop/SKILL.md), [`continuous-learning`](continuous-learning/SKILL.md), [`continuous-learning-v2`](continuous-learning-v2/SKILL.md), [`cost-aware-llm-pipeline`](cost-aware-llm-pipeline/SKILL.md), [`council`](council/SKILL.md), [`cpp-coding-standards`](cpp-coding-standards/SKILL.md), [`cpp-testing`](cpp-testing/SKILL.md), [`crosspost`](crosspost/SKILL.md), [`csharp-testing`](csharp-testing/SKILL.md), [`customer-billing-ops`](customer-billing-ops/SKILL.md), [`customs-trade-compliance`](customs-trade-compliance/SKILL.md)

</details>

<details>
<summary><strong>D-G</strong> (39)</summary>

[`dart-flutter-patterns`](dart-flutter-patterns/SKILL.md), [`dashboard-builder`](dashboard-builder/SKILL.md), [`data-scraper-agent`](data-scraper-agent/SKILL.md), [`database-migrations`](database-migrations/SKILL.md), [`deep-research`](deep-research/SKILL.md), [`defi-amm-security`](defi-amm-security/SKILL.md), [`deployment-patterns`](deployment-patterns/SKILL.md), [`design-system`](design-system/SKILL.md), [`django-patterns`](django-patterns/SKILL.md), [`django-security`](django-security/SKILL.md), [`django-tdd`](django-tdd/SKILL.md), [`django-verification`](django-verification/SKILL.md), [`dmux-workflows`](dmux-workflows/SKILL.md), [`docker-mounted-workspace`](docker-mounted-workspace/SKILL.md), [`docker-patterns`](docker-patterns/SKILL.md), [`documentation-lookup`](documentation-lookup/SKILL.md), [`dotnet-patterns`](dotnet-patterns/SKILL.md), [`e2e-testing`](e2e-testing/SKILL.md), [`ecc-tools-cost-audit`](ecc-tools-cost-audit/SKILL.md), [`email-ops`](email-ops/SKILL.md), [`energy-procurement`](energy-procurement/SKILL.md), [`enterprise-agent-ops`](enterprise-agent-ops/SKILL.md), [`eval-harness`](eval-harness/SKILL.md), [`evm-token-decimals`](evm-token-decimals/SKILL.md), [`exa-search`](exa-search/SKILL.md), [`fal-ai-media`](fal-ai-media/SKILL.md), [`finance-billing-ops`](finance-billing-ops/SKILL.md), [`flutter-dart-code-review`](flutter-dart-code-review/SKILL.md), [`foundation-models-on-device`](foundation-models-on-device/SKILL.md), [`frontend-design`](frontend-design/SKILL.md), [`frontend-patterns`](frontend-patterns/SKILL.md), [`frontend-slides`](frontend-slides/SKILL.md), [`gan-style-harness`](gan-style-harness/SKILL.md), [`github`](github/SKILL.md), [`github-issue-manager`](github-issue-manager/SKILL.md), [`github-ops`](github-ops/SKILL.md), [`golang-patterns`](golang-patterns/SKILL.md), [`golang-testing`](golang-testing/SKILL.md), [`google-workspace-ops`](google-workspace-ops/SKILL.md)

</details>

<details>
<summary><strong>H-L</strong> (29)</summary>

[`healthcare-cdss-patterns`](healthcare-cdss-patterns/SKILL.md), [`healthcare-emr-patterns`](healthcare-emr-patterns/SKILL.md), [`healthcare-eval-harness`](healthcare-eval-harness/SKILL.md), [`healthcare-phi-compliance`](healthcare-phi-compliance/SKILL.md), [`hexagonal-architecture`](hexagonal-architecture/SKILL.md), [`hipaa-compliance`](hipaa-compliance/SKILL.md), [`hookify-rules`](hookify-rules/SKILL.md), [`inventory-demand-planning`](inventory-demand-planning/SKILL.md), [`investor-materials`](investor-materials/SKILL.md), [`investor-outreach`](investor-outreach/SKILL.md), [`iterative-retrieval`](iterative-retrieval/SKILL.md), [`java-coding-standards`](java-coding-standards/SKILL.md), [`jira-integration`](jira-integration/SKILL.md), [`jpa-patterns`](jpa-patterns/SKILL.md), [`knowledge-ops`](knowledge-ops/SKILL.md), [`kotlin-coroutines-flows`](kotlin-coroutines-flows/SKILL.md), [`kotlin-exposed-patterns`](kotlin-exposed-patterns/SKILL.md), [`kotlin-ktor-patterns`](kotlin-ktor-patterns/SKILL.md), [`kotlin-patterns`](kotlin-patterns/SKILL.md), [`kotlin-testing`](kotlin-testing/SKILL.md), [`laravel-patterns`](laravel-patterns/SKILL.md), [`laravel-plugin-discovery`](laravel-plugin-discovery/SKILL.md), [`laravel-security`](laravel-security/SKILL.md), [`laravel-tdd`](laravel-tdd/SKILL.md), [`laravel-verification`](laravel-verification/SKILL.md), [`lead-intelligence`](lead-intelligence/SKILL.md), [`liquid-glass-design`](liquid-glass-design/SKILL.md), [`llm-trading-agent-security`](llm-trading-agent-security/SKILL.md), [`logistics-exception-management`](logistics-exception-management/SKILL.md)

</details>

<details>
<summary><strong>M-R</strong> (35)</summary>

[`manim-video`](manim-video/SKILL.md), [`market-research`](market-research/SKILL.md), [`mcp-server-patterns`](mcp-server-patterns/SKILL.md), [`messages-ops`](messages-ops/SKILL.md), [`nanoclaw-repl`](nanoclaw-repl/SKILL.md), [`nestjs-patterns`](nestjs-patterns/SKILL.md), [`nextjs-turbopack`](nextjs-turbopack/SKILL.md), [`nodejs-keccak256`](nodejs-keccak256/SKILL.md), [`nutrient-document-processing`](nutrient-document-processing/SKILL.md), [`nuxt4-patterns`](nuxt4-patterns/SKILL.md), [`openclaw-persona-forge`](openclaw-persona-forge/SKILL.md), [`opensource-pipeline`](opensource-pipeline/SKILL.md), [`perl-patterns`](perl-patterns/SKILL.md), [`perl-security`](perl-security/SKILL.md), [`perl-testing`](perl-testing/SKILL.md), [`plankton-code-quality`](plankton-code-quality/SKILL.md), [`postgres-patterns`](postgres-patterns/SKILL.md), [`product-capability`](product-capability/SKILL.md), [`product-lens`](product-lens/SKILL.md), [`production-scheduling`](production-scheduling/SKILL.md), [`project-flow-ops`](project-flow-ops/SKILL.md), [`prompt-optimizer`](prompt-optimizer/SKILL.md), [`python-patterns`](python-patterns/SKILL.md), [`python-testing`](python-testing/SKILL.md), [`pytorch-patterns`](pytorch-patterns/SKILL.md), [`quality-nonconformance`](quality-nonconformance/SKILL.md), [`ralphinho-rfc-pipeline`](ralphinho-rfc-pipeline/SKILL.md), [`regex-vs-llm-structured-text`](regex-vs-llm-structured-text/SKILL.md), [`remotion-video-creation`](remotion-video-creation/SKILL.md), [`repo-scan`](repo-scan/SKILL.md), [`research-ops`](research-ops/SKILL.md), [`returns-reverse-logistics`](returns-reverse-logistics/SKILL.md), [`rules-distill`](rules-distill/SKILL.md), [`rust-patterns`](rust-patterns/SKILL.md), [`rust-testing`](rust-testing/SKILL.md)

</details>

<details>
<summary><strong>S-Z</strong> (32)</summary>

[`safety-guard`](safety-guard/SKILL.md), [`santa-method`](santa-method/SKILL.md), [`search-first`](search-first/SKILL.md), [`security-bounty-hunter`](security-bounty-hunter/SKILL.md), [`security-review`](security-review/SKILL.md), [`security-scan`](security-scan/SKILL.md), [`seo`](seo/SKILL.md), [`skill-comply`](skill-comply/SKILL.md), [`skill-stocktake`](skill-stocktake/SKILL.md), [`skill-syncer`](skill-syncer/SKILL.md), [`social-graph-ranker`](social-graph-ranker/SKILL.md), [`springboot-patterns`](springboot-patterns/SKILL.md), [`springboot-security`](springboot-security/SKILL.md), [`springboot-tdd`](springboot-tdd/SKILL.md), [`springboot-verification`](springboot-verification/SKILL.md), [`strategic-compact`](strategic-compact/SKILL.md), [`swift-actor-persistence`](swift-actor-persistence/SKILL.md), [`swift-concurrency-6-2`](swift-concurrency-6-2/SKILL.md), [`swift-protocol-di-testing`](swift-protocol-di-testing/SKILL.md), [`swiftui-patterns`](swiftui-patterns/SKILL.md), [`tdd-workflow`](tdd-workflow/SKILL.md), [`team-builder`](team-builder/SKILL.md), [`terminal-ops`](terminal-ops/SKILL.md), [`token-budget-advisor`](token-budget-advisor/SKILL.md), [`ui-demo`](ui-demo/SKILL.md), [`unified-notifications-ops`](unified-notifications-ops/SKILL.md), [`verification-loop`](verification-loop/SKILL.md), [`video-editing`](video-editing/SKILL.md), [`videodb`](videodb/SKILL.md), [`visa-doc-translate`](visa-doc-translate/SKILL.md), [`workspace-surface-audit`](workspace-surface-audit/SKILL.md), [`x-api`](x-api/SKILL.md)

</details>

## 관련 스킬

- [`skill-syncer`](skill-syncer/SKILL.md): 이 저장소를 실제 도구에 반영하는 기본 스킬
- [`configure-ecc`](configure-ecc/SKILL.md): ECC 스타일 선택 설치/구성 가이드
- [`docker-mounted-workspace`](docker-mounted-workspace/SKILL.md): 현재 워크스페이스와 연결된 컨테이너에서 빌드와 테스트를 이어가는 스킬
- [`workspace-surface-audit`](workspace-surface-audit/SKILL.md): 현재 작업 환경에서 어떤 스킬이 맞는지 추천

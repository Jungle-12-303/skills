# Skills

Claude Code 및 AI 에이전트를 위한 개인 스킬 컬렉션.

---

## 구조

각 스킬은 독립된 폴더로 구성되며, `SKILL.md` 파일에 사용 시점, 동작 방식, 예시를 정의한다.

```
skills/
├── <skill-name>/
│   ├── SKILL.md       # 스킬 정의 (필수)
│   ├── scripts/       # 스크립트 (선택)
│   └── conventions/   # 참고 문서 (선택)
```

---

## 스킬 목록

### Git & 협업

| 스킬 | 설명 |
|------|------|
| `commit-convention` | 커밋 메시지 작성, 브랜치 전략, PR 워크플로우, merge vs rebase |
| `github` | GitHub Issues, PR, Release, README 자동화 스크립트 포함 |
| `github-issue-manager` | GitHub 이슈 생성·분류·관리 에이전트 |

### 백엔드 개발

| 스킬 | 설명 |
|------|------|
| `backend-patterns` | 백엔드 아키텍처 패턴 및 모범 사례 |
| `django-patterns` | Django 프로젝트 구조 및 패턴 |
| `django-tdd` | Django TDD 워크플로우 |
| `django-security` | Django 보안 가이드 |
| `springboot-patterns` | Spring Boot 패턴 |
| `springboot-tdd` | Spring Boot TDD 워크플로우 |
| `nestjs-patterns` | NestJS 패턴 |
| `golang-patterns` | Go 언어 패턴 |
| `golang-testing` | Go 테스트 전략 |
| `rust-patterns` | Rust 패턴 |
| `rust-testing` | Rust 테스트 전략 |
| `python-patterns` | Python 패턴 및 모범 사례 |
| `python-testing` | Python 테스트 전략 |
| `laravel-patterns` | Laravel 패턴 |
| `kotlin-patterns` | Kotlin 패턴 |
| `java-coding-standards` | Java 코딩 표준 |

### 프론트엔드

| 스킬 | 설명 |
|------|------|
| `frontend-patterns` | 프론트엔드 아키텍처 패턴 |
| `frontend-design` | UI/UX 디자인 패턴 |
| `nextjs-turbopack` | Next.js + Turbopack 설정 |
| `nuxt4-patterns` | Nuxt 4 패턴 |
| `swiftui-patterns` | SwiftUI 패턴 |

### 데이터베이스 & 인프라

| 스킬 | 설명 |
|------|------|
| `postgres-patterns` | PostgreSQL 패턴 |
| `database-migrations` | DB 마이그레이션 전략 |
| `docker-patterns` | Docker 컨테이너 패턴 |
| `deployment-patterns` | 배포 전략 |
| `clickhouse-io` | ClickHouse 사용 패턴 |

### 테스트

| 스킬 | 설명 |
|------|------|
| `tdd-workflow` | TDD 워크플로우 |
| `e2e-testing` | E2E 테스트 전략 |
| `eval-harness` | AI 평가 하네스 구성 |
| `security-review` | 보안 코드 리뷰 |
| `security-scan` | 보안 스캔 자동화 |

### AI & 에이전트

| 스킬 | 설명 |
|------|------|
| `agentic-engineering` | 에이전트 시스템 설계 |
| `autonomous-loops` | 자율 에이전트 루프 패턴 |
| `continuous-learning` | 세션에서 패턴을 학습하여 스킬로 축적 |
| `mcp-server-patterns` | MCP 서버 개발 패턴 |
| `deep-research` | 심층 리서치 워크플로우 |
| `prompt-optimizer` | 프롬프트 최적화 전략 |
| `context-budget` | 컨텍스트 토큰 예산 관리 |
| `token-budget-advisor` | 토큰 비용 최적화 |

### 유틸리티

| 스킬 | 설명 |
|------|------|
| `skill-syncer` | 스킬 동기화 스크립트 |
| `coding-standards` | 공통 코딩 표준 |
| `api-design` | API 설계 원칙 |
| `architecture-decision-records` | ADR 작성 가이드 |
| `codebase-onboarding` | 코드베이스 온보딩 가이드 |
| `documentation-lookup` | 문서 검색 전략 |

---

## 스킬 작성 규칙

```markdown
---
name: skill-name
description: 한 줄 설명 — 언제 이 스킬을 사용하는지 명확히 기술
---

# 스킬 제목

## 활성화 시점
언제 이 스킬을 사용하는지

## 동작 방식
스킬의 주요 패턴과 가이드라인

## 예시
구체적인 예시
```

---

## 관련 레포

- [`claude-code`](../claude-code) — ECC 기반 Claude Code 플러그인 (에이전트, 커맨드, 훅, 룰 포함)

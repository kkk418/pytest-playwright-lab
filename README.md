# pytest-playwright-lab

一个中文为主的 Python 自动化测试学习与作品集仓库，覆盖 API 测试、Web UI 测试、Page Object Model、测试数据、报告和 GitHub Actions。

## 覆盖内容

- API：使用 [JSONPlaceholder](https://jsonplaceholder.typicode.com/) 练习 GET、过滤、资源关系、POST 和错误响应。
- UI：使用 [SauceDemo](https://www.saucedemo.com/) 练习登录、商品、购物车和结账流程。
- 工程化：pytest fixture、参数化、marker、POM、失败截图/trace、HTML 报告和 CI。
- 数据校验：使用 SQLite 练习建表、关联查询和持久化断言。

公共练习站点可能临时不可用，因此这些用例都标注了 `external`；它们不对公共站点执行压力测试，也不使用个人账号或真实业务数据。

## 环境准备

需要 Python 3.12+。Windows 推荐：

```powershell
python -m venv .venv
\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m playwright install chromium
```

复制 `.env.example` 为 `.env` 后再按需调整地址；示例账号只属于 SauceDemo 公共演示环境。

## 运行

```powershell
python -m pytest -m api -q
python -m pytest -m "ui and smoke" --browser chromium -q
python -m pytest --html=html-report/report.html --self-contained-html
ruff check .
```

失败时 Playwright 会保留测试结果目录中的截图或 trace；CI 会上传 HTML 报告和测试附件。

## 目录

```text
pages/                 页面对象
tests/api/             API 契约和数据校验
tests/ui/              SauceDemo UI 流程
tests/sql/             SQLite 查询与持久化练习
docs/                  测试计划、缺陷样例、学习路线和实施报告
.github/workflows/     GitHub Actions
```

请先阅读 [`docs/实施报告与学习路线.md`](docs/实施报告与学习路线.md)，按“测试设计 → pytest → API → UI/POM → SQL → CI”的顺序学习。

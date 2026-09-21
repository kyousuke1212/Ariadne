API 参考 Copy pageCopy
# React 参考总览
本部分提供了使用 React 的详细参考文档。如果需要了解 React，请访问 教程 部分。
React 参考文档分为以下内容：
## React
编程式 React 功能：
- Hook —— 在组件中使用不同的 React 特性。
- 组件 —— 可以在 JSX 中使用的内置组件。
- API —— 用于定义组件的有用 API。
- 指示符 —— 为与 React 服务器组件兼容的捆绑器提供指示。
## React DOM
React-dom 仅支持在 web 应用程序中使用（在浏览器 DOM 环境中运行）。本节分为以下部分：
- Hook —— 适用于在浏览器 DOM 环境中运行的 web 应用程序的 Hook。
- 组件 —— React 支持所有内置的 HTML 和 SVG 组件。
- API —— react-dom 包含仅在 web 应用程序中支持的方法。
- 客户端 API —— react-dom/client API 允许在客户端（浏览器中）渲染 React 组件。
- 服务端 API —— react-dom/server API 允许在服务器端将 React 组件渲染为 HTML。
- 静态 API - react-dom/static API 允许将 React 组件生成静态 HTML。
## React 编译器
React 编译器是一个构建时优化工具，可以自动为你的 React 组件和数值添加记忆优化（memoization）：
- 配置 —— React 编译器的配置选项。
- 指令 —— 用于控制编译的函数级指令。
- 编译库 —— 发布预编译库代码的指南。
## React Hook 的 ESLint 插件
针对 React Hook 的 ESLint 插件 有助于强制执行 React 的规则：
- Lints —— 每种 lint 的详细文档和示例。
## React 的规则
React 有一套表达模式的俗语与规则，它们以一种易于理解并能帮助实现高质量应用程序的方式表达出来：
- 组件与 Hook 必须是纯粹的 —— 组件与 Hook 的纯粹代码更易于理解、调试，并允许 React 自动优化组件与 Hook。
- React 调用组件与 Hook —— React 负责在必要时渲染组件与 Hook，以优化用户体验。
- Hook 规则 —— Hook 使用 JavaScript 函数定义，但它们代表一种特殊类型的可重用 UI 逻辑，对它们可以被调用的位置有限制。
## 过时的 API
- 过时的 API —— 从 react 包中导出，但不建议在新编写的代码中使用。
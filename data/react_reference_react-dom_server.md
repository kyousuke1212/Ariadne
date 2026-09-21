API 参考 Copy pageCopy
# Server React DOM API
react-dom/server API 允许你通过服务端渲染将 React 组件渲染为 HTML。这些 API 仅在服务器应用程序顶层调用，以生成初始 HTML。有的 框架 可能会为你调用相关 API。大多数组件不需要导入或使用这些 API。
## Web 流服务器 API
以下方法仅在具有 web 流 的环境中可用，包括浏览器、Deno，以及一些现代 edge 运行时：
- renderToReadableStream 将 React 树渲染为 可读的 web 流。
- resume resumes prerender to a Readable Web Stream.
### 注意
Node.js also includes these methods for compatibility, but they are not recommended due to worse performance. Use the dedicated Node.js APIs instead.
## Node.js 流服务器 API
以下方法仅在具有 Node.js 流 的环境中可用：
- renderToPipeableStream 将 React 树渲染为可传输的 Node.js 流。
- resumeToPipeableStream resumes prerenderToNodeStream to a pipeable Node.js Stream.
## 过时的非流式环境 API
以下方法可以在非流式环境中使用：
- renderToString 将 React 树渲染为字符串。
- renderToStaticMarkup 将非交互式 React 树渲染为字符串。
相比于流式 API，这些 API 在功能上有些限制。
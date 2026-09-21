API 参考服务端 API Copy pageCopy
# renderToString
### 陷阱
renderToString 不支持流式传输或等待数据。请参考替代方案。
renderToString 将 React 树渲染为一个 HTML 字符串。
```
const html = renderToString(reactNode, options?)
```
参考
- renderToString(reactNode, options?)
用法
- 将 React 树渲染为 HTML 字符串
替代方案
- 从 renderToString 迁移到服务器上的流式传输方法
- 从 renderToString 迁移到服务器上的静态预渲染
- 从客户端代码中移除 renderToString
故障排除
- 当组件暂停时，HTML 中始终包含一个后备方案
## 参考
### renderToString(reactNode, options?)
在服务器，调用 renderToString 将你的应用渲染为 HTML。
```
import { renderToString } from 'react-dom/server';const html = renderToString(<App />);
```
在客户端，调用 hydrateRoot 来使服务器生成的 HTML 具有交互性。
请参考下面的更多示例。
#### 参数
reactNode：你要渲染为 HTML 的 React 节点。例如，一个 JSX 节点，就像 <App />。
可选的 options：服务器渲染的对象。
可选的 identifierPrefix：React 使用 useId 生成的 ID 的字符串前缀。用于避免在同一页面使用多个根时发生冲突。必须与传递给 hydrateRoot 的前缀相同。
#### 返回
一个 HTML 字符串。
#### 注意事项
renderToString 对 Suspense 的支持有限。如果一个组件挂起（suspend），renderToString 会立即将其后备方案作为 HTML 发送。
renderToString 可以在浏览器中工作，但 不推荐 在客户端代码中使用它。
## 用法
### 将 React 树渲染为 HTML 字符串
调用 renderToString 将你的应用渲染为 HTML 字符串，你可以将其与服务器响应一起发送：
```
import { renderToString } from 'react-dom/server';// 路由处理程序的语法取决于你使用的后端框架app.use('/', (request, response) => {  const html = renderToString(<App />);  response.send(html);});
```
这将生成你的 React 组件的初始非交互式 HTML 输出。在客户端上，你需要调用 hydrateRoot 来将服务器生成的 HTML 进行激活处理，使其具有交互功能。
### 陷阱
renderToString 不支持流式传输或等待数据。请参考替代方案。
## 替代方案
### 从 renderToString 迁移到服务器上的流式传输方法
renderToString 立即返回一个字符串，因此不支持加载时流式传输内容。
如果可能的话，我们建议使用这些功能完整的替代方法：
- 如果你使用 Node.js，请使用 renderToPipeableStream。
- 如果你使用 Deno 或支持 Web Streams 的现代运行时，请使用 renderToReadableStream。
如果你的服务器环境不支持流式传输，你仍然可以继续使用 renderToString。
### 从 renderToString 迁移到服务器上的静态预渲染
renderToString 立即返回一个字符串，它不支持等待静态 HTML 生成的数据加载。
我们建议使用这些功能齐全的替代产品：
- 如果你使用 Node.js，可使用 prerenderToNodeStream。
- 如果你使用 Deno 或者一个 Web 流 的现代边缘运行环境，可使用 prerender。
如果你的静态网站生成环境不支持流，你可以继续使用 renderToString。
### 从客户端代码中移除 renderToString
有时，renderToString 用于在客户端将某个组件转换为 HTML。
```
// 🚩 不必要：在客户端使用 renderToStringimport { renderToString } from 'react-dom/server';const html = renderToString(<MyIcon />);console.log(html); // 例如，"<svg>...</svg>"
```
在客户端导入 react-dom/server 会不必要地增加 bundle 大小，所以应该避免这样做。如果你需要在浏览器中将某个组件渲染为 HTML，请使用 createRoot 并从 DOM 中读取 HTML。
```
import { createRoot } from 'react-dom/client';import { flushSync } from 'react-dom';const div = document.createElement('div');const root = createRoot(div);flushSync(() => {  root.render(<MyIcon />);});console.log(div.innerHTML); // 例如，"<svg>...</svg>"
```
flushSync 调用是必要的，以便在读取 innerHTML 属性之前更新 DOM。
## 故障排除
### 当组件暂停时，HTML 中始终包含一个后备方案
renderToString 不完全支持 Suspense。
如果某个组件 suspend（例如，因为它使用 lazy 定义或获取数据），renderToString 不会等待其内容解析完成。相反，renderToString 将找到最近的 <Suspense> 边界，并在 HTML 中渲染其 fallback 属性。直到客户端代码加载后，内容才会显示出来。
要解决这个问题，请使用 推荐的流式解决方案之一。 对于服务器端渲染，它们可以在服务器上以块的形式流式传输内容，以便用户在客户端代码加载之前逐步看到页面被填充。对于静态站点，他们可以等待所有内容解析后再生成静态 HTML。
API 参考服务端 API Copy pageCopy
# resume
resume 将预渲染的 React 树流式传输到 Web 可读流。
```
const stream = await resume(reactNode, postponedState, options?)
```
参考
- resume(node, postponedState, options?)
用法
- 恢复预渲染
- 延伸阅读
### 注意
此 API 依赖于 Web 流。对于 Node.js，请改用 resumeToNodeStream。
## 参考
### resume(node, postponedState, options?)
调用 resume，将预渲染的 React 树继续渲染为 HTML，并写入 Web 可读流。
```
import { resume } from 'react-dom/server';import {getPostponedState} from './storage';async function handler(request, writable) {  const postponed = await getPostponedState(request);  const resumeStream = await resume(<App />, postponed);  return resumeStream.pipeTo(writable)}
```
请参阅下面的更多示例。
#### 参数
- reactNode：调用 prerender 时传入的 React 节点。例如，像 <App /> 这样的 JSX 元素。它应表示整个文档，因此 App 组件应渲染 <html> 标签。
- postponedState：从 prerender API 返回的不透明 postpone 对象，从你存储它的位置加载（例如 Redis、文件或 S3）。
可选 options：包含流式传输选项的对象。
- 可选 nonce：一个 nonce 字符串，用于允许 script-src 内容安全策略 中的脚本。
- 可选 signal：一个 中止信号，允许你 中止服务端渲染，并在客户端渲染剩余内容。
- 可选 onError：每当发生服务端错误时触发的回调函数，无论错误是 可恢复 还是 不可恢复。默认情况下，它只调用 console.error。如果你重写它来 记录崩溃报告，请确保仍然调用 console.error。
#### 返回值
resume 返回一个 Promise：
- 如果 resume 成功生成了 shell，该 Promise 将解析为一个 Web 可读流，可以将其通过管道传输到 Web 可写流。
- 如果 shell 中发生错误，Promise 将因该错误而被拒绝。
返回的流还有一个额外属性：
- allReady：一个在所有渲染完成后解析的 Promise。你可以在返回响应之前 await stream.allReady，以供 爬虫和静态生成 使用。这样做不会有任何渐进式加载，流中将包含最终的 HTML。
#### 注意事项
- resume 不接受 bootstrapScripts、bootstrapScriptContent 或 bootstrapModules 选项。相反，你需要将这些选项传递给生成 postponedState 的 prerender 调用。你也可以手动将引导内容注入可写流。
- resume 不接受 identifierPrefix，因为该前缀在 prerender 和 resume 中必须保持一致。
- 由于不能向 prerender 提供 nonce，只有在没有向 prerender 提供脚本时，才应向 resume 提供 nonce。
- resume 会从根节点重新渲染，直到找到一个未完全预渲染的组件。只有完全预渲染的组件（组件及其子组件都已完成预渲染）才会被完全跳过。
## 用法
### 恢复预渲染
```
index.jsindex.htmldemo-helpers.jsindex.jsReloadClearForkimport {
  flushReadableStreamToFrame,
  getUser,
  Postponed,
  sleep,
} from "./demo-helpers";
import { StrictMode, Suspense, use, useEffect } from "react";
import { prerender } from "react-dom/static";
import { resume } from "react-dom/server";
import { hydrateRoot } from "react-dom/client";

function Header() {
  return <header>我和我的后代都可以被预渲染</header>;
}

const { promise: cookies, resolve: resolveCookies } = Promise.withResolvers();

function Main() {
  const { sessionID } = use(cookies);
  const user = getUser(sessionID);

  useEffect(() => {
    console.log("已达到交互状态！");
  }, []);

  return (
    <main>
      你好，{user.name}！
      <button onClick={() => console.log("已完成 hydration！")}>
        点击此按钮需要先完成 hydration。
      </button>
    </main>
  );
}

function Shell({ children }) {
  // 在真实应用中，你应在此处放置 html 和 body。
  // 这里只是为了演示，使用可以包含在现有 body 中的标签。
  return (
    <html>
      <body>{children}</body>
    </html>
  );
}

function App() {
  return (
    <Shell>
      <Suspense fallback="正在加载页眉">
        <Header />
      </Suspense>
      <Suspense fallback="正在加载主体">
        <Main />
      </Suspense>
    </Shell>
  );
}

async function main(frame) {
  // 第 1 层
  const controller = new AbortController();
  const prerenderedApp = prerender(<App />, {
    signal: controller.signal,
    onError(error) {
      if (error instanceof Postponed) {
      } else {
        console.error(error);
      }
    },
  });
  // 我们会立即在宏任务中止该过程。
  // 任何无法同步获取或无法在微任务中获取的数据，都不会完成加载。
  setTimeout(() => {
    controller.abort(new Postponed());
  });

  const { prelude, postponed } = await prerenderedApp;
  await flushReadableStreamToFrame(prelude, frame);

  // 第 2 层
  // 这里只是为了演示而等待。
  // 在真实应用中，prelude 和 postponed 状态会在第 1 层序列化，并在这一层反序列化。
  // 在 React 从预渲染中断处继续渲染的同时，prelude 内容可以立即作为普通 HTML 刷新。
  // React 将从预渲染停止的地方继续渲染。
  await sleep(2000);

  // 你会从传入的 HTTP 请求中获取 cookie
  resolveCookies({ sessionID: "abc" });

  const stream = await resume(<App />, postponed);

  await flushReadableStreamToFrame(stream, frame);

  // 第 3 层
  // 这里只是为了演示而等待。
  await sleep(2000);

  hydrateRoot(frame.contentWindow.document, <App />);
}

main(document.getElementById("container"));
```
显示更多
### 延伸阅读
恢复过程的行为类似于 renderToReadableStream。有关更多示例，请参阅 renderToReadableStream 的用法部分。
prerender 的用法部分 包含专门介绍如何使用 prerender 的示例。
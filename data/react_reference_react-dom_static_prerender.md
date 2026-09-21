API 参考Static APIs Copy pageCopy
# prerender
prerender 使用 Web 流 将 React 树渲染为静态 HTML 字符串。
```
const {prelude, postponed} = await prerender(reactNode, options?)
```
参考
- prerender(reactNode, options?)
用法
- 将 React 树渲染为静态 HTML 流
- 将 React 树渲染为静态 HTML 字符串
- 等待所有数据加载
- 中止预渲染
疑难解答
- 我的流要等到整个应用渲染完成后才会启动。
### 注意
此 API 依赖于 Web 流。对于 Node.js，请使用 prerenderToNodeStream。
## 参考
### prerender(reactNode, options?)
调用 prerender 将应用程序渲染为静态 HTML。
```
import { prerender } from 'react-dom/static';async function handler(request, response) {  const {prelude} = await prerender(<App />, {    bootstrapScripts: ['/main.js']  });  return new Response(prelude, {    headers: { 'content-type': 'text/html' },  });}
```
在客户端，调用 hydrateRoot 将服务器生成的 HTML 转换为可交互的内容。
请参阅下面的更多示例。
#### 参数
reactNode：需要渲染为 HTML 的 React 节点。例如，一个像 <App /> 的 JSX 节点。它应表示整个文档，因此 App 组件应渲染 <html> 标签。
可选 options：一个包含静态生成选项的对象。
- 可选 bootstrapScriptContent：如果指定，此字符串将被放置在一个内联的 <script> 标签中。
- 可选 bootstrapScripts：一个字符串 URL 的数组，用于在页面上生成 <script> 标签。使用此选项包含调用 hydrateRoot 的 <script>。如果不希望在客户端运行 React，可以省略此选项。
- 可选 bootstrapModules：类似于 bootstrapScripts，但会生成 <script type="module">。
- 可选 identifierPrefix：React 用于 useId 生成的 ID 的字符串前缀。当在同一页面上使用多个根时，这对于避免冲突非常有用。必须与传递给 hydrateRoot 的前缀相同。
- 可选 namespaceURI：流的根 命名空间 URI 的字符串。默认为常规 HTML。对于 SVG，请传递 'http://www.w3.org/2000/svg'；对于 MathML，请传递 'http://www.w3.org/1998/Math/MathML'。
- 可选 onError：每当发生服务器错误时触发的回调，无论是 可恢复的 还是 不可恢复的。默认情况下，它只调用 console.error。如果你重写它用来 记录崩溃报告 ，请确保仍然调用 console.error。你还可以使用它在 shell 被生成之前 调整状态码。
- 可选 progressiveChunkSize：每个块的字节数。阅读更多关于默认启发式的信息。
- 可选 signal：一个 中止信号，允许你 中止预渲染 并在客户端渲染剩余内容。
#### 返回值
prerender 返回一个 Promise 对象：
如果渲染成功，Promise 将解析为一个包含以下内容的对象：
- prelude：一个 Web Stream 的 HTML。你可以使用此流以块的形式发送响应，或者将整个流读取为字符串。
- postponed：一个 JSON 序列化的不透明对象, 如果 prerender 未完成, 可将其传递给 resume。 否则，null 表示 prelude 包含所有内容，无需恢复。
- 如果渲染失败，Promise 将被拒绝。使用此方法输出一个回退 shell。
#### 注意事项
在预渲染时，nonce 不是一个可用的选项。Nonce 必须在每个请求中都是唯一的，如果你使用 nonce 和 CSP 来保护你的应用，那么将 nonce 值包含在预渲染产物中本身是不恰当且不安全的。
### 注意
### 何时使用 prerender ？
静态 prerender API 用于静态服务器端生成 (SSG)。与 renderToString 不同， prerender 会等待所有数据加载完成后再解析。这使其适合为整个页面生成静态 HTML，包括需要通过 Suspense 获取的数据。要在加载内容时进行流式传输，请使用流式服务器端渲染 (SSR) API，例如 renderToReadableStream。
可以中止 prerender 并随后使用 resumeAndPrerender 继续或使用 resume 恢复，以支持部分预渲染。
## 用法
### 将 React 树渲染为静态 HTML 流
调用 prerender 将 React 树渲染为静态 HTML，并生成一个 可读的 Web 流：
```
import { prerender } from 'react-dom/static';async function handler(request) {  const {prelude} = await prerender(<App />, {    bootstrapScripts: ['/main.js']  });  return new Response(prelude, {    headers: { 'content-type': 'text/html' },  });}
```
与 根组件一起, 你需要提供一组  引导 <script> 路径 。 根组件应返回 包含 <html> 标签 的整个文档。
例如，它可能看起来像这样：
```
export default function App() {  return (    <html>      <head>        <meta charSet="utf-8" />        <meta name="viewport" content="width=device-width, initial-scale=1" />        <link rel="stylesheet" href="/styles.css"></link>        <title>My app</title>      </head>      <body>        <Router />      </body>    </html>  );}
```
React 将会把 doctype 和 引导 <script> 标签 注入到生成的 HTML 流中：
```
<!DOCTYPE html><html>  <!-- ... 组件中的 HTML ... --></html><script src="/main.js" async=""></script>
```
在客户端，引导脚本应 通过调用 hydrateRoot 来对整个 文档 进行初始化：
```
import { hydrateRoot } from 'react-dom/client';import App from './App.js';hydrateRoot(document, <App />);
```
这将为静态服务器生成的 HTML 附加事件监听器，使其具有交互性。
深入探讨
#### 从构建产物中读取 CSS 和 JS 资源路径
显示更多
最终的资源 URL（如 JavaScript 和 CSS 文件）通常在构建后会被哈希处理。例如，styles.css 可能会变成 styles.123456.css。对静态资源文件名进行哈希处理可以确保每次构建的相同资源都会有不同的文件名。这很有用，因为它允许你安全地为静态资源启用长期缓存：具有特定名称的文件内容永远不会更改。
然而，如果在构建完成之前无法知道资源的 URL，就无法将它们直接写入源代码。例如，像之前那样在 JSX 中硬编码 "/styles.css" 是不可行的。为了避免将它们写入源代码，根组件可以通过一个传递的属性读取真实的文件名映射。
```
export default function App({ assetMap }) {  return (    <html>      <head>        <title>My app</title>        <link rel="stylesheet" href={assetMap['styles.css']}></link>      </head>      ...    </html>  );}
```
在服务器上，渲染 <App assetMap={assetMap} /> 并传递包含资源 URL 的 assetMap ：
```
// 需要从构建工具中获取此 JSON，例如从构建输出中读取。const assetMap = {  'styles.css': '/styles.123456.css',  'main.js': '/main.123456.js'};async function handler(request) {  const {prelude} = await prerender(<App assetMap={assetMap} />, {    bootstrapScripts: [assetMap['/main.js']]  });  return new Response(prelude, {    headers: { 'content-type': 'text/html' },  });}
```
由于服务器现在正在渲染 <App assetMap={assetMap} />，你还需要在客户端使用 assetMap 进行渲染，以避免交互初始化时的错误。可以通过序列化并将 assetMap 递给客户端，如下所示：
```
// 需要从构建工具中获取此 JSON。const assetMap = {  'styles.css': '/styles.123456.css',  'main.js': '/main.123456.js'};async function handler(request) {  const {prelude} = await prerender(<App assetMap={assetMap} />, {    // 注意：将其使用 stringify() 是安全的，因为这些数据不是用户产生的。    bootstrapScriptContent: `window.assetMap = ${JSON.stringify(assetMap)};`,    bootstrapScripts: [assetMap['/main.js']],  });  return new Response(prelude, {    headers: { 'content-type': 'text/html' },  });}
```
在上面的示例中， bootstrapScriptContent 选项会添加一个额外的内联 <script> 标签，在客户端设置全局变量 window.assetMap 。这使客户端代码能够读取相同的 assetMap ：
```
import { hydrateRoot } from 'react-dom/client';import App from './App.js';hydrateRoot(document, <App assetMap={window.assetMap} />);
```
客户端和服务器都使用相同的 assetMap 属性渲染 App ，因此不会出现交互初始化时的错误。
### 将 React 树渲染为静态 HTML 字符串
调用 prerender 将应用程序渲染为静态 HTML 字符串：
```
import { prerender } from 'react-dom/static';async function renderToString() {  const {prelude} = await prerender(<App />, {    bootstrapScripts: ['/main.js']  });  const reader = prelude.getReader();  let content = '';  while (true) {    const {done, value} = await reader.read();    if (done) {      return content;    }    content += Buffer.from(value).toString('utf8');  }}
```
这将生成 React 组件的初始非交互式 HTML 输出。在客户端，你需要调用 hydrateRoot 来 初始化 服务器生成的 HTML，并使其具有交互功能。
### 等待所有数据加载
prerender 会等待所有数据加载完成后再结束静态 HTML 的生成并解析。例如，考虑一个展示封面、包含好友和照片的侧边栏，以及帖子列表的个人资料页面：
```
function ProfilePage() {  return (    <ProfileLayout>      <ProfileCover />      <Sidebar>        <Friends />        <Photos />      </Sidebar>      <Suspense fallback={<PostsGlimmer />}>        <Posts />      </Suspense>    </ProfileLayout>  );}
```
假设 <Posts /> 需要加载一些数据，这可能会花费一些时间。理想情况下，你希望在帖子加载完成后再将其包含在 HTML 中。为此，可以使用 Suspense 来暂停数据加载，而 prerender 会等待挂起的内容加载完成后再生成静态 HTML。
### 注意
只有支持 Suspense 的数据源才能触发 Suspense 组件。 包括：
- 使用支持 Suspense 的框架（如：Relay 和 Next.js）进行数据获取
- 使用 lazy 懒加载组件代码
- 使用 use 获取 Promise 的结果
Suspense 无法 检测在 Effect 或事件处理程序中获取的数据。
在上述 Posts 组件中加载数据的具体方式取决于你使用的框架。如果你使用支持 Suspense 的框架，可以在其数据获取文档中找到详细信息。
在没有使用特定框架的情况下，支持 Suspense 的数据获取尚未得到支持。实现支持 Suspense 的数据源的要求目前不稳定且未记录。React 未来版本将发布用于集成数据源与 Suspense 的官方 API。
### 中止预渲染
可以通过设置超时，来强制“终止”预渲染进程：
```
async function renderToString() {  const controller = new AbortController();  setTimeout(() => {    controller.abort()  }, 10000);  try {    // prelude 将包含在控制器中止前    // 已被预渲染的所有 HTML。    const {prelude} = await prerender(<App />, {      signal: controller.signal,    });    //...
```
所有包含未完成子组件的 Suspense 边界都将以 fallback 状态包含在 prelude 中。
这可与 resume 或 resumeAndPrerender 一起用于部分预呈现。
## 疑难解答
### 我的流要等到整个应用渲染完成后才会启动。
prerender 的响应会等待整个应用渲染完成，包括所有 Suspense 边界的内容加载完成后，才会解析。这种设计适用于静态站点生成（SSG），并不支持在内容加载时进行流式加载。
如果需要在内容加载时进行流式加载，可以使用类似 renderToReadableStream 的流式服务器渲染 API。
API 参考API Copy pageCopy
# use
use 是一个 React API，它可以让你读取类似于 Promise 或 context 的资源的值。
```
const value = use(resource);
```
参考
- use(resource)
用法
- 使用 use 读取 context
- 将数据从服务器流式传递给客户端
- 处理 rejected Promise
疑难解答
- “Suspense Exception: This is not a real error!”
## 参考
### use(resource)
在组件中调用 use 以读取类似于 Promise 或 context 的资源的值。
```
import { use } from 'react';function MessageComponent({ messagePromise }) {  const message = use(messagePromise);  const theme = use(ThemeContext);  // ...
```
与 React Hook 不同的是，可以在循环和条件语句（如 if）中调用 use。但需要注意的是，调用 use 的函数仍然必须是一个组件或 Hook。
当使用 Promise 调用 use API 时，它会与 Suspense 和 错误边界 集成。当传递给 use 的 Promise 处于 pending 时，调用 use 的组件也会 挂起。如果调用 use 的组件被包装在 Suspense 边界内，将显示后备 UI。一旦 Promise 被解决，Suspense 后备方案将被使用 use API 返回的数据替换。如果传递给 use 的 Promise 被拒绝，将显示最近错误边界的后备 UI。
参见下方更多示例。
#### 参数
- resource：想要从中读取值的数据源。资源可以是 Promise 或 context。
#### 返回值
use API 返回从资源中读取的值，类似于 fullfilled Promise 或 context。
#### 注意
- use API 必须在组件或 Hook 内部调用。
- 在 服务器组件 中获取数据时，应优先使用 async 和 await 而不是 use。async 和 await 会从调用 await 的点开始渲染，而 use 会在数据获取到后重新渲染组件。
- 在 服务器组件 中创建 Promise 并将其传递给 客户端组件 优于在客户端组件中创建 Promise。在客户端组件中创建的 Promise 每次渲染都会重新创建。从服务器组件传递到客户端组件的 Promise 在重新渲染时保持稳定。请参阅此示例。
## 用法
### 使用 use 读取 context
当 context 被传递给 use 时，它的工作方式类似于useContext。而 useContext 必须在组件的顶层调用，use 可以在条件语句如 if 和循环如 for 内调用。相比之下，use 比 useContext更加灵活。
```
import { use } from 'react';function Button() {  const theme = use(ThemeContext);  // ...
```
use 返回传递的 context 的 context 值。React 会搜索组件树并找到 最接近的 context provider 以确定需要返回的 context 值。
如果要将上下文传递给 Button，请将其或其父组件之一包装在相应的 context provdier 内。
```
function MyPage() {  return (    <ThemeContext value="dark">      <Form />    </ThemeContext>  );}function Form() {  // ……在这里面渲染按钮……}
```
无论在 provider 和 Button 之间有多少层组件，都不会有影响。当 Form 内的任何位置的 Button 调用 use(ThemeContext) 时，它将接收到值为 "dark"。
不同于 useContext，use 可以在条件语句和循环中调用，比如 if。
```
function HorizontalRule({ show }) {  if (show) {    const theme = use(ThemeContext);    return <hr className={theme} />;  }  return false;}
```
if 语句内部调用了 use，允许有条件地从 context 中读取值。
### 陷阱
与 useContext 类似，use(context) 始终查找调用它的组件上方最近的 context provider。它向上搜索并忽略调用 use(context) 的组件中的 context provider。
```
App.jsApp.jsReloadClearForkimport { createContext, use } from 'react';

const ThemeContext = createContext(null);

export default function MyApp() {
  return (
    <ThemeContext value="dark">
      <Form />
    </ThemeContext>
  )
}

function Form() {
  return (
    <Panel title="Welcome">
      <Button show={true}>Sign up</Button>
      <Button show={false}>Log in</Button>
    </Panel>
  );
}

function Panel({ title, children }) {
  const theme = use(ThemeContext);
  const className = 'panel-' + theme;
  return (
    <section className={className}>
      <h1>{title}</h1>
      {children}
    </section>
  )
}

function Button({ show, children }) {
  if (show) {
    const theme = use(ThemeContext);
    const className = 'button-' + theme;
    return (
      <button className={className}>
        {children}
      </button>
    );
  }
  return false
}
```
显示更多
### 将数据从服务器流式传递给客户端
数据可以通过将 Promise 作为 prop 从 服务器组件 传递到 客户端组件 以从服务器流式传输到客户端。
```
import { fetchMessage } from './lib.js';import { Message } from './message.js';export default function App() {  const messagePromise = fetchMessage();  return (    <Suspense fallback={<p>waiting for message...</p>}>      <Message messagePromise={messagePromise} />    </Suspense>  );}
```
客户端组件将 从 prop 中接收到的 Promise  传递给 use API。这允许 客户端组件 从最初由服务器组件创建的 Promise 中读取值。
```
// message.js'use client';import { use } from 'react';export function Message({ messagePromise }) {  const messageContent = use(messagePromise);  return <p>Here is the message: {messageContent}</p>;}
```
由于 Message 被包裹在 Suspense 中，所以在 Promise 解决之前将显示后备方案。当 Promise 被解决后，use API 将读取值，然后 Message 组件将替换 Suspense 后备方案。
```
message.jsmessage.jsReloadClearFork"use client";

import { use, Suspense } from "react";

function Message({ messagePromise }) {
  const messageContent = use(messagePromise);
  return <p>Here is the message: {messageContent}</p>;
}

export function MessageContainer({ messagePromise }) {
  return (
    <Suspense fallback={<p>⌛Downloading message...</p>}>
      <Message messagePromise={messagePromise} />
    </Suspense>
  );
}
```
显示更多
### 注意
将来自服务器组件的 Promise 传递至客户端组件时，其解析值必须可序列化以在服务器和客户端之间传递。像函数这样的数据类型不可序列化，不能成为这种 Promise 的解析值。
深入探讨
#### 应该在服务器组件还是客户端组件解析 Promise？
显示更多
Promise 可以从服务器组件传递至客户端组件，并且可以在客户端组件中使用 use API 解析它。也可以在服务器组件中使用 await 解析 Promise，并将所需的数据作为 prop 传递给客户端组件。
```
export default async function App() {  const messageContent = await fetchMessage();  return <Message messageContent={messageContent} />}
```
但是在 服务器组件 中使用 await 会在 await 执行完成前阻塞渲染。而将 Promise 从服务器组件传递到客户端组件可以防止 Promise 阻塞服务器组件渲染。
### 处理 rejected Promise
在某些情况下，传递给 use 的 Promise 可能会被拒绝（rejected）。可以通过以下方式处理 rejected Promise：
- 使用错误边界向用户显示错误信息。
- 使用 Promise.catch 提供替代值。
### 陷阱
不能在 try-catch 块中调用 use。可以选择将组件 包装在错误边界中，或者 使用 Promise .catch 方法提供替代值给 use。
#### 使用错误边界将错误展示给用户
如果希望在 Promise 被拒绝（rejected）时向用户显示错误信息，可以使用 错误边界。如果需要使用错误边界，请将调用 use API 的组件包装在错误边界中。如果传递给 use 的 Promise 被拒绝（rejected），将显示错误边界的后备方案。
```
message.jsmessage.jsReloadClearFork"use client";

import { use, Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";

export function MessageContainer({ messagePromise }) {
  return (
    <ErrorBoundary fallback={<p>⚠️Something went wrong</p>}>
      <Suspense fallback={<p>⌛Downloading message...</p>}>
        <Message messagePromise={messagePromise} />
      </Suspense>
    </ErrorBoundary>
  );
}

function Message({ messagePromise }) {
  const content = use(messagePromise);
  return <p>Here is the message: {content}</p>;
}
```
显示更多
#### 使用 Promise.catch 提供替代值
如果希望在传递给 use 的 Promise 被拒绝（rejected）时提供替代值，可以使用 Promise 的 catch 方法。
```
import { Message } from './message.js';export default function App() {  const messagePromise = new Promise((resolve, reject) => {    reject();  }).catch(() => {    return "no new message found.";  });  return (    <Suspense fallback={<p>waiting for message...</p>}>      <Message messagePromise={messagePromise} />    </Suspense>  );}
```
要使用 Promise 的 catch 方法，请在 Promise 对象上调用 catch。catch 接受一个参数：一个接受错误消息作为参数的函数。由传递给 catch 的函数 返回 的任何内容都将视为 Promise 的解决值。
## 疑难解答
### “Suspense Exception: This is not a real error!”
你要么是在 React 组件或 Hook 函数之外调用了 use，或者在 try-catch 块中调用了 use。如果你在 try-catch 块中调用 use，请将组件包裹在错误边界中，或者使用 Promise 的 catch 方法来捕获错误并提供给替代值。参见这些示例。
如果在 React 组件或 Hook 函数之外调用 use，请将 use 调用移至 React 组件或 Hook 函数中。
```
function MessageComponent({messagePromise}) {  function download() {    // ❌ 调用 `use` 的函数不是组件或者 Hook    const message = use(messagePromise);    // ...
```
相反，请在任何组件封闭区域之外调用 use，而调用 use 的函数本身应为组件或 Hook。
```
function MessageComponent({messagePromise}) {  // ✅ `use` 正在组件内被调用  const message = use(messagePromise);  // ...
```
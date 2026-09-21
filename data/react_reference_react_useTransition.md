API 参考Hook Copy pageCopy
# useTransition
useTransition 是一个让你可以在后台渲染部分 UI 的 React Hook。
```
const [isPending, startTransition] = useTransition()
```
参考
- useTransition()
- startTransition 函数
用法
- 通过 Action 执行非阻塞更新
- 在组件中公开 action 属性
- 显示待处理的视觉状态
- 避免不必要的加载指示器
- 构建一个Suspense-enabled 的路由
- 使用错误边界向用户显示错误
疑难解答
- 在 Transition 中无法更新输入框内容
- React 没有将状态更新视为 Transition
- React 不会将 await 之后的状态更新视为 Transition
- 我想在组件外部调用 useTransition
- 我传递给 startTransition 的函数会立即执行
- Transitions 中的状态更新顺序混乱
## 参考
### useTransition()
在组件顶层调用 useTransition，将某些状态更新标记为 transition。
```
import { useTransition } from 'react';function TabContainer() {  const [isPending, startTransition] = useTransition();  // ……}
```
参见下方更多示例。
#### 参数
useTransition 不需要任何参数。
#### 返回值
useTransition 返回一个由两个元素组成的数组：
- isPending，告诉你是否存在待处理的 transition。
- startTransition 函数，你可以使用此方法将更新标记为 transition。
### startTransition 函数
useTransition 返回的 startTransition 函数允许你将更新标记为 Transition。
```
function TabContainer() {  const [isPending, startTransition] = useTransition();  const [tab, setTab] = useState('about');  function selectTab(nextTab) {    startTransition(() => {      setTab(nextTab);    });  }  // ……}
```
### 注意
#### 传递给 startTransition 的函数被称为 “Actions”
传递给 startTransition 的函数被称为 “Action” 。按照约定，任何在 startTransition 内调用的回调函数（例如作为回调的 prop）应命名为 action 或包含 “Action” 后缀：
```
function SubmitButton({ submitAction }) {  const [isPending, startTransition] = useTransition();  return (    <button      disabled={isPending}      onClick={() => {        startTransition(async () => {          await submitAction();        });      }}    >      Submit    </button>  );}
```
#### 参数
- action：通过调用一个或多个 set 函数 来更新某些状态的函数。React 会立即调用 action（无需参数），并将 action 函数调用期间同步调度的所有状态更新标记为 Transition。在 action 中通过 await 等待的异步调用会被包含在 Transition 中，但目前需要在 await 之后将任何 set 函数再次包裹在 startTransition 中（参见疑难解答）。标记为 Transition 的状态更新将具备非阻塞特性，并且不会显示不必要的加载指示。
#### 返回值
startTransition 不返回任何值。
#### 注意
useTransition 是一个 Hook，因此只能在组件或自定义 Hook 内部调用。如果需要在其他地方启动 transition（例如从数据库），请调用独立的 startTransition 函数。
只有在可以访问该状态的 set 函数时，才能将其对应的状态更新包装为 transition。如果你想启用 Transition 以响应某个 prop 或自定义 Hook 值，请尝试使用 useDeferredValue。
传递给 startTransition 的函数会被立即执行，并将在其执行期间发生的所有状态更新标记为 transition。如果你尝试在 setTimeout 中执行状态更新，它们将不会被标记为 transition。
你必须将任意异步请求之后的状态更新用 startTransition 包裹，以将其标记为 Transition 更新。这是一个已知限制，我们将在未来版本中修复（参见疑难解答）。
startTransition 函数具有稳定的标识，所以你经常会看到 Effect 的依赖数组中会省略它，即使包含它也不会导致 Effect 重新触发。如果 linter 允许你省略依赖项并且没有报错，那么你就可以安全地省略它。了解移除 Effect 依赖项的更多信息。
标记为 Transition 的状态更新将被其他状态更新打断。例如在 Transition 中更新图表组件，并在图表组件仍在重新渲染时继续在输入框中输入，React 将首先处理输入框的更新，之后再重新启动对图表组件的渲染工作。
Transition 更新不能用于控制文本输入。
目前，React 会批处理多个同时进行的 transition。这是一个限制，可能会在未来版本中删除。
## 用法
### 通过 Action 执行非阻塞更新
在组件的顶层调用 useTransition 来创建 Action，并获取挂起的状态：
```
import {useState, useTransition} from 'react';function CheckoutForm() {  const [isPending, startTransition] = useTransition();  // ……}
```
useTransition 返回一个由两个元素组成的数组：
- isPending，告诉你是否存在待处理的 transition。
- startTransition 函数，你可以使用此方法创建一个 Action。
为了启动 Transition，你需要将函数传递给 startTransition。例如：
```
import {useState, useTransition} from 'react';import {updateQuantity} from './api';function CheckoutForm() {  const [isPending, startTransition] = useTransition();  const [quantity, setQuantity] = useState(1);  function onSubmit(newQuantity) {    startTransition(async function () {      const savedQuantity = await updateQuantity(newQuantity);      startTransition(() => {        setQuantity(savedQuantity);      });    });  }  // ……}
```
传递给 startTransition 的函数被称为 “Action”。你可以在 Action 中更新状态和执行副作用操作，这些工作将在后台执行，不会阻塞页面的用户交互。一个 Transition 可以包含多个 Action，且在 Transition 进行期间，你的用户界面将保持流畅响应。例如，如果用户点击一个标签页后又改变主意点击另一个标签页，第二个点击会立即被处理，无需等待第一个更新完成。
为了向用户提供 Transition 进行中的反馈， isPending 状态会在首次调用 startTransition 时切换为 true，并会在所有 Action 完成且最终状态呈现给用户前一直保持为 true。Transition 机制确保 Action 中的副作用会完整执行以避免不必要的加载指示，同时你可以通过 useOptimistic 在 Transition 进行期间提供即时反馈。
#### Action 与常规事件处理的区别
1. 在 Action 中更新数量 2. 在不使用 Action 的情况下更新数量
#### 第 1 个示例 共 2 个示例: 在 Action 中更新数量
在这个示例中，updateQuantity 函数模拟向服务端发送请求来更新购物车中的商品数量。该函数被人为地减慢，使得完成请求至少需要一秒钟。
快速多次更新数量。请注意，当任何请求在进行中时，都会显示挂起的 “Total” 状态，并且 “Total” 只会在最后一个请求完成后更新。由于更新操作在 Action 中进行，在请求处理期间仍可继续更新“quantity””。
```
App.jsItem.jsTotal.jsapi.jsApp.jsReloadClearForkimport { useState, useTransition } from "react";
import { updateQuantity } from "./api";
import Item from "./Item";
import Total from "./Total";

export default function App({}) {
  const [quantity, setQuantity] = useState(1);
  const [isPending, startTransition] = useTransition();

  const updateQuantityAction = async newQuantity => {
    // To access the pending state of a transition,
    // call startTransition again.
    startTransition(async () => {
      const savedQuantity = await updateQuantity(newQuantity);
      startTransition(() => {
        setQuantity(savedQuantity);
      });
    });
  };

  return (
    <div>
      <h1>Checkout</h1>
      <Item action={updateQuantityAction}/>
      <hr />
      <Total quantity={quantity} isPending={isPending} />
    </div>
  );
}
```
显示更多
这是一个演示 Action 工作原理的基础示例，但此示例未处理请求完成顺序错乱的问题。当多次更新数量时，较早的请求可能会在较晚的请求之后完成，导致数量更新顺序混乱。这是一个已知限制，我们将在未来版本中修复（参见下方的疑难解答）。
对于常见用例，React 提供了以下内置抽象方案：
- useActionState
- <form> 表单操作
- 服务端函数
这些方案会为你自动处理请求顺序问题。当使用 Transitions 构建自定义钩子或管理异步状态转换的库时，你虽然可以获得更精细的控制，但也需要自行处理请求顺序逻辑。
下一个示例
### 在组件中公开 action 属性
你可以通过组件暴露一个 action 属性，允许父组件调用一个 Action。
例如，这个 TabButton 组件将 onClick 事件逻辑封装到 action 属性中：
```
export default function TabButton({ action, children, isActive }) {  const [isPending, startTransition] = useTransition();  if (isActive) {    return <b>{children}</b>  }  return (    <button onClick={() => {      startTransition(async () => {        // await the action that's passed in.        // This allows it to be either sync or async.        await action();      });    }}>      {children}    </button>  );}
```
由于父组件的状态更新在 action 中，所以该状态更新会被标记为 transition。这意味着你可以在点击“Posts”后立即点击“Contact”，并且它不会阻止用户交互:
```
App.jsTabButton.jsAboutTab.jsPostsTab.jsContactTab.jsTabButton.jsReloadClearForkimport { useTransition } from 'react';

export default function TabButton({ action, children, isActive }) {
  const [isPending, startTransition] = useTransition();
  if (isActive) {
    return <b>{children}</b>
  }
  if (isPending) {
    return <b className="pending">{children}</b>;
  }
  return (
    <button onClick={async () => {
      startTransition(async () => {
        // await the action that's passed in.
        // This allows it to be either sync or async.
        await action();
      });
    }}>
      {children}
    </button>
  );
}
```
显示更多
### 注意
When exposing an action prop from a component, you should await it inside the transition.
This allows the action callback to be either synchronous or asynchronous without requiring an additional startTransition to wrap the await in the action.
### 显示待处理的视觉状态
你可以使用 useTransition 返回的 isPending 布尔值来向用户表明当前处于 Transition 中。例如，选项卡按钮可以有一个特殊的“pending”视觉状态：
```
function TabButton({ action, children, isActive }) {  const [isPending, startTransition] = useTransition();  // ...  if (isPending) {    return <b className="pending">{children}</b>;  }  // ...
```
请注意，现在点击“Posts”感觉更加灵敏，因为选项卡按钮本身立即更新了：
```
App.jsTabButton.jsAboutTab.jsPostsTab.jsContactTab.jsTabButton.jsReloadClearForkimport { useTransition } from 'react';

export default function TabButton({ action, children, isActive }) {
  const [isPending, startTransition] = useTransition();
  if (isActive) {
    return <b>{children}</b>
  }
  if (isPending) {
    return <b className="pending">{children}</b>;
  }
  return (
    <button onClick={() => {
      startTransition(async () => {
        await action();
      });
    }}>
      {children}
    </button>
  );
}
```
显示更多
### 避免不必要的加载指示器
在这个例子中，PostsTab 组件通过 use 获取了一些数据。当你点击“Posts”选项卡时，PostsTab 组件将 挂起，导致使用最近的加载中的后备方案：
```
App.jsTabButton.jsApp.jsReloadClearForkimport { Suspense, useState } from 'react';
import TabButton from './TabButton.js';
import AboutTab from './AboutTab.js';
import PostsTab from './PostsTab.js';
import ContactTab from './ContactTab.js';

export default function TabContainer() {
  const [tab, setTab] = useState('about');
  return (
    <Suspense fallback={<h1>🌀 Loading...</h1>}>
      <TabButton
        isActive={tab === 'about'}
        action={() => setTab('about')}
      >
        About
      </TabButton>
      <TabButton
        isActive={tab === 'posts'}
        action={() => setTab('posts')}
      >
        Posts
      </TabButton>
      <TabButton
        isActive={tab === 'contact'}
        action={() => setTab('contact')}
      >
        Contact
      </TabButton>
      <hr />
      {tab === 'about' && <AboutTab />}
      {tab === 'posts' && <PostsTab />}
      {tab === 'contact' && <ContactTab />}
    </Suspense>
  );
}
```
显示更多
隐藏整个选项卡容器以显示加载指示符会导致用户体验不连贯。如果你将 useTransition 添加到 TabButton 中，你可以改为在选项卡按钮中指示待处理状态。
请注意，现在点击“帖子”不再用一个旋转器替换整个选项卡容器：
```
App.jsTabButton.jsTabButton.jsReloadClearForkimport { useTransition } from 'react';

export default function TabButton({ action, children, isActive }) {
  const [isPending, startTransition] = useTransition();
  if (isActive) {
    return <b>{children}</b>
  }
  if (isPending) {
    return <b className="pending">{children}</b>;
  }
  return (
    <button onClick={() => {
      startTransition(async () => {
        await action();
      });
    }}>
      {children}
    </button>
  );
}
```
显示更多
了解有关在Suspense中使用转换的更多信息。
### 注意
转换效果只会“等待”足够长的时间来避免隐藏 已经显示 的内容（例如选项卡容器）。如果“帖子”选项卡具有一个嵌套 <Suspense> 边界，转换效果将不会“等待”它。
### 构建一个Suspense-enabled 的路由
如果你正在构建一个 React 框架或路由，我们建议将页面导航标记为转换效果。
```
function Router() {  const [page, setPage] = useState('/');  const [isPending, startTransition] = useTransition();  function navigate(url) {    startTransition(() => {      setPage(url);    });  }  // ...
```
这么做有三个好处：
- 转换效果是可中断的，这样用户可以在等待重新渲染完成之前点击其他地方。
- 转换效果可以防止不必要的加载指示符，这样用户就可以避免在导航时产生不协调的跳转。
- Transition 等待所有挂起的 action，它允许用户在副作用完成之后再显示新页面。
下面是一个简单的使用转换效果进行页面导航的路由器示例：
```
App.jsLayout.jsIndexPage.jsArtistPage.jsAlbums.jsBiography.jsPanel.jsApp.jsReloadClearForkimport { Suspense, useState, useTransition } from 'react';
import IndexPage from './IndexPage.js';
import ArtistPage from './ArtistPage.js';
import Layout from './Layout.js';

export default function App() {
  return (
    <Suspense fallback={<BigSpinner />}>
      <Router />
    </Suspense>
  );
}

function Router() {
  const [page, setPage] = useState('/');
  const [isPending, startTransition] = useTransition();

  function navigate(url) {
    startTransition(() => {
      setPage(url);
    });
  }

  let content;
  if (page === '/') {
    content = (
      <IndexPage navigate={navigate} />
    );
  } else if (page === '/the-beatles') {
    content = (
      <ArtistPage
        artist={{
          id: 'the-beatles',
          name: 'The Beatles',
        }}
      />
    );
  }
  return (
    <Layout isPending={isPending}>
      {content}
    </Layout>
  );
}

function BigSpinner() {
  return <h2>🌀 Loading...</h2>;
}
```
显示更多
### 注意
启用 Suspense 的路由默认情况下会将页面导航更新包装为 transition。
### 使用错误边界向用户显示错误
如果传递给 startTransition 的函数抛出错误，可以通过错误边界（error boundary） 向用户显示错误。要使用错误边界，请将调用 useTransition 的组件包裹在错误边界中。当传递给 startTransition 的函数报错时，错误边界的备用 UI 将会显示。
```
AddCommentContainer.jsAddCommentContainer.jsReloadClearForkimport { useTransition } from "react";
import { ErrorBoundary } from "react-error-boundary";

export function AddCommentContainer() {
  return (
    <ErrorBoundary fallback={<p>⚠️Something went wrong</p>}>
      <AddCommentButton />
    </ErrorBoundary>
  );
}

function addComment(comment) {
  // For demonstration purposes to show Error Boundary
  if (comment == null) {
    throw new Error("Example Error: An error thrown to trigger error boundary");
  }
}

function AddCommentButton() {
  const [pending, startTransition] = useTransition();

  return (
    <button
      disabled={pending}
      onClick={() => {
        startTransition(() => {
          // Intentionally not passing a comment
          // so error gets thrown
          addComment();
        });
      }}
    >
      Add comment
    </button>
  );
}
```
显示更多
## 疑难解答
### 在 Transition 中无法更新输入框内容
不应将控制输入框的状态变量标记为 transition：
```
const [text, setText] = useState('');// ...function handleChange(e) {  // ❌ 不应将受控输入框的状态变量标记为 Transition  startTransition(() => {    setText(e.target.value);  });}// ...return <input value={text} onChange={handleChange} />;
```
这是因为 Transition 是非阻塞的，但是在响应更改事件时更新输入应该是同步的。如果想在输入时运行一个 transition，那么有两种做法：
- 声明两个独立的状态变量：一个用于输入状态（它总是同步更新），另一个用于在 Transition 中更新。这样，便可以使用同步状态控制输入，并将用于 Transition 的状态变量（它将“滞后”于输入）传递给其余的渲染逻辑。
- 或者使用一个状态变量，并添加 useDeferredValue，它将“滞后”于实际值，并自动触发非阻塞的重新渲染以“追赶”新值。
### React 没有将状态更新视为 Transition
当在 Transition 中包装状态更新时，请确保它发生在 startTransition 调用期间：
```
startTransition(() => {  // ✅ 在调用 startTransition 中更新状态  setPage('/about');});
```
传递给 startTransition 的函数必须是同步的。你不能像这样将更新标记为 transition：
```
startTransition(() => {  // ❌ 在调用 startTransition 后更新状态  setTimeout(() => {    setPage('/about');  }, 1000);});
```
相反，你可以这样做：
```
setTimeout(() => {  startTransition(() => {    // ✅ 在调用 startTransition 中更新状态    setPage('/about');  });}, 1000);
```
### React 不会将 await 之后的状态更新视为 Transition
当你在 startTransition 函数内部使用 await 时，await 之后的状态更新不会被标记为 Transition 更新。你必须将每个 await 之后的状态更新再次包裹在 startTransition 调用中：
```
startTransition(async () => {  await someAsyncFunction();  // ❌ 不要在 await 之后调用 startTransition  setPage('/about');});
```
然而，使用以下方法可以正常工作：
```
startTransition(async () => {  await someAsyncFunction();  // ✅ 在 await 之后 调用 startTransition  startTransition(() => {    setPage('/about');  });});
```
这是由于 JavaScript 的限制，React 无法跟踪异步上下文的范围。未来当 AsyncContext 提案实现后，该限制将被消除。
### 我想在组件外部调用 useTransition
useTransition 是一个 Hook，因此不能在组件外部调用。请使用独立的 startTransition 方法。它们的工作方式相同，但不提供 isPending 标记。
### 我传递给 startTransition 的函数会立即执行
如果你运行这段代码，它将会打印 1, 2, 3：
```
console.log(1);startTransition(() => {  console.log(2);  setPage('/about');});console.log(3);
```
期望打印 1, 2, 3。传递给 startTransition 的函数不会被延迟执行。与浏览器的 setTimeout 不同，它不会延迟执行回调。React 会立即执行你的函数，但是在它运行的同时安排的任何状态更新都被标记为 transition。你可以将其想象为以下方式：
```
// React 运行的简易版本let isInsideTransition = false;function startTransition(scope) {  isInsideTransition = true;  scope();  isInsideTransition = false;}function setState() {  if (isInsideTransition) {    // ……安排 Transition 状态更新……  } else {    // ……安排紧急状态更新……  }}
```
### Transitions 中的状态更新顺序混乱
如果在 startTransition 内部使用 await，你可能会看到更新出现顺序错乱。
在这个示例中，updateQuantity 函数模拟向服务端发送请求以更新购物车中的商品数量。该函数 人为地让每隔一次请求在前一次之后返回，用于模拟网络请求的竞态条件。
尝试更新一次数量，然后快速多次更新。你可能会看到错误的总计：
```
App.jsItem.jsTotal.jsapi.jsApp.jsReloadClearForkimport { useState, useTransition } from "react";
import { updateQuantity } from "./api";
import Item from "./Item";
import Total from "./Total";

export default function App({}) {
  const [quantity, setQuantity] = useState(1);
  const [isPending, startTransition] = useTransition();
  // Store the actual quantity in separate state to show the mismatch.
  const [clientQuantity, setClientQuantity] = useState(1);

  const updateQuantityAction = newQuantity => {
    setClientQuantity(newQuantity);

    // Access the pending state of the transition,
    // by wrapping in startTransition again.
    startTransition(async () => {
      const savedQuantity = await updateQuantity(newQuantity);
      startTransition(() => {
        setQuantity(savedQuantity);
      });
    });
  };

  return (
    <div>
      <h1>Checkout</h1>
      <Item action={updateQuantityAction}/>
      <hr />
      <Total clientQuantity={clientQuantity} savedQuantity={quantity} isPending={isPending} />
    </div>
  );
}
```
显示更多
多次点击时，较早的请求可能会在较晚的请求之后完成。当这种情况发生时，React 目前无法知道预期的顺序。这是因为更新是异步调度的，而 React 在异步边界处丢失了顺序的上下文。
这是预期内的，因为在 Transition 中的 Action 不保证执行顺序。对于常见用例，React 提供了更高级的抽象，如 useActionState 和 <form> actions 来为你处理顺序问题。对于高级用例，你需要自行实现队列和中止逻辑来处理这种情况。
Example of useActionState handling execution order:
```
App.jsItem.jsTotal.jsapi.jsApp.jsReloadClearForkimport { useState, useActionState } from "react";
import { updateQuantity } from "./api";
import Item from "./Item";
import Total from "./Total";

export default function App({}) {
  // Store the actual quantity in separate state to show the mismatch.
  const [clientQuantity, setClientQuantity] = useState(1);
  const [quantity, updateQuantityAction, isPending] = useActionState(
    async (prevState, payload) => {
      setClientQuantity(payload);
      const savedQuantity = await updateQuantity(payload);
      return savedQuantity; // Return the new quantity to update the state
    },
    1 // Initial quantity
  );

  return (
    <div>
      <h1>Checkout</h1>
      <Item action={updateQuantityAction}/>
      <hr />
      <Total clientQuantity={clientQuantity} savedQuantity={quantity} isPending={isPending} />
    </div>
  );
}
```
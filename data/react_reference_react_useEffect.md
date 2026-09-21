API 参考Hook Copy pageCopy
# useEffect
useEffect 是一个 React Hook，它允许你 将组件与外部系统同步。
```
useEffect(setup, dependencies?)
```
参考
- useEffect(setup, dependencies?)
用法
- 连接到外部系统
- 在自定义 Hook 中封装 Effect
- 控制非 React 小部件
- 使用 Effect 请求数据
- 指定响应式依赖项
- 在 Effect 中根据先前 state 更新 state
- 删除不必要的对象依赖项
- 删除不必要的函数依赖项
- 从 Effect 读取最新的 props 和 state
- 在服务器和客户端上显示不同的内容
疑难解答
- Effect 在组件挂载时运行了两次
- Effect 在每次重新渲染后都运行
- Effect 函数一直在无限循环中运行
- 即使组件没有卸载，cleanup 逻辑也会运行
- 我的 Effect 做了一些视觉相关的事情，在它运行之前我看到了一个闪烁
## 参考
### useEffect(setup, dependencies?)
在组件的顶层调用 useEffect 来声明一个 Effect：
```
import { useState, useEffect } from 'react';import { createConnection } from './chat.js';function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => {      connection.disconnect();    };  }, [serverUrl, roomId]);  // ...}
```
请看下面的更多例子。
#### 参数
setup：处理 Effect 的函数。setup 函数选择性返回一个 清理（cleanup） 函数。当 组件提交的时候，React 会运行 setup 函数。在每次提交导致依赖项变更后，React 将首先使用旧值运行 cleanup 函数（如果你提供了该函数），然后使用新值运行 setup 函数。在组件从 DOM 中移除后，React 将最后一次运行 cleanup 函数。
可选 dependencies：setup 代码中引用的所有响应式值的列表。响应式值包括 props、state 以及所有直接在组件内部声明的变量和函数。如果你的代码检查工具 配置了 React，那么它将验证是否每个响应式值都被正确地指定为一个依赖项。依赖项列表的元素数量必须是固定的，并且必须像 [dep1, dep2, dep3] 这样内联编写。React 将使用 Object.is 来比较每个依赖项和它先前的值。如果省略此参数，则在每次组件提交更改之后，将重新运行 Effect 函数。如果你想了解更多，请参见 传递依赖数组、空数组和不传递依赖项之间的区别。
#### 返回值
useEffect 返回 undefined。
#### 注意事项
useEffect 是一个 Hook，因此只能在 组件的顶层 或自己的 Hook 中调用它，而不能在循环或者条件内部调用。如果需要，抽离出一个新组件并将 state 移入其中。
如果你 没有打算与某个外部系统同步，那么你可能不需要 Effect。
当严格模式启动时，React 将在真正的 setup 函数首次运行前，运行一个开发模式下专有的额外 setup + cleanup 周期。这是一个压力测试，用于确保 cleanup 逻辑“映射”到了 setup 逻辑，并停止或撤消 setup 函数正在做的任何事情。如果这会导致一些问题，请实现 cleanup 函数。
如果你的一些依赖项是组件内部定义的对象或函数，则存在这样的风险，即它们将 导致 Effect 过多地重新运行。要解决这个问题，请删除不必要的 对象 和 函数 依赖项。你还可以 抽离状态更新 和 非响应式的逻辑 到 Effect 之外。
如果你的 Effect 不是由交互（比如点击）引起的，那么 React 会让浏览器 在运行 Effect 前先绘制出更新后的屏幕。如果你的 Effect 正在做一些视觉相关的事情（例如，定位一个 tooltip），并且有显著的延迟（例如，它会闪烁），那么将 useEffect 替换为 useLayoutEffect。
如果你的 Effect 是由一个交互（比如点击）引起的，React 可能会在浏览器重新绘制屏幕之前执行 Effect。通常情况下，这样是符合预期的。但是，如果你必须要推迟 Effect 执行到浏览器绘制之后，和使用 alert() 类似，可以使用 setTimeout。有关更多信息，请参阅 reactwg/react-18/128。
即使你的 Effect 是由一个交互（比如点击）引起的，React 也可能允许浏览器在处理 Effect 内部的状态更新之前重新绘制屏幕。通常，这样是符合预期的。但是，如果你一定要阻止浏览器重新绘制屏幕，则需要用 useLayoutEffect 替换 useEffect。
Effect 只在客户端上运行，在服务端渲染中不会运行。
## 用法
### 连接到外部系统
有些组件需要与网络、某些浏览器 API 或第三方库保持连接，当它们显示在页面上时。这些系统不受 React 控制，所以称为外部系统。
要 将组件连接到某个外部系统，请在组件的顶层调用 useEffect：
```
import { useState, useEffect } from 'react';import { createConnection } from './chat.js';function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  useEffect(() => {  	const connection = createConnection(serverUrl, roomId);    connection.connect();  	return () => {      connection.disconnect();  	};  }, [serverUrl, roomId]);  // ...}
```
你需要向 useEffect 传递两个参数：
一个 setup 函数 ，其 setup 代码 用来连接到该系统。
- 它应该返回一个 清理函数（cleanup），其 cleanup 代码 用来与该系统断开连接。
- 一个 依赖项列表，包括这些函数使用的每个组件内的值。
React 在必要时会调用 setup 和 cleanup，这可能会发生多次：
- 将组件挂载到页面时，将运行 setup 代码。
如果组件提交导致 依赖项 被改变：
- 首先，使用旧的 props 和 state 运行 cleanup 代码。
- 然后，使用新的 props 和 state 运行 setup 代码。
- 当组件从页面卸载后，cleanup 代码 将运行最后一次。
用上面的代码作为例子来解释这个顺序。
当 ChatRoom 组件添加到页面中时，它将使用 serverUrl 和 roomId 初始值连接到聊天室。如果 serverUrl 或者 roomId 发生改变并导致提交（比如用户在下拉列表中选择了一个不同的聊天室），那么 Effect 就会 断开与前一个聊天室的连接，并连接到下一个聊天室。当 ChatRoom 组件从页面中卸载时，你的 Effect 将最后一次断开连接。
为了 帮助你发现 bug，在开发环境下，React 在运行 setup 之前会额外运行一次setup 和 cleanup。这是一个压力测试，用于验证 Effect 逻辑是否正确实现。如果这会导致可见的问题，那么你的 cleanup 函数就缺少一些逻辑。cleanup 函数应该停止或撤消 setup 函数正在执行的任何操作。一般来说，用户不应该能够区分只调用一次 setup（在生产环境中）与调用 setup → cleanup → setup 序列（在开发环境中）。查看常见解决方案。
尽量 将每个 Effect 作为一个独立的过程编写，并且 每次只考虑一个单独的 setup/cleanup 周期。组件是否正在挂载、更新或卸载并不重要。当你的 cleanup 逻辑正确地“映射”到 setup 逻辑时，你的 Effect 是可复原的，因此可以根据需要多次运行 setup 和 cleanup 函数。
### 注意
Effect 可以让你的组件与某些外部系统（比如聊天服务）保持同步。在这里，外部系统是指任何不受 React 控制的代码，例如：
- 由 setInterval() 和 clearInterval() 管理的定时器。
- 使用 window.addEventListener() 和 window.removeEventListener() 的事件订阅。
- 一个第三方的动画库，它有一个类似 animation.start() 和 animation.reset() 的 API。
如果你没有连接到任何外部系统，你或许不需要 Effect。
#### 连接到外部系统的示例
1. 连接到聊天服务器 2. 监听全局的浏览器事件 3. 触发动画效果 4. 控制模态对话框 5. 跟踪元素可见性
#### 第 1 个示例 共 5 个示例: 连接到聊天服务器
在这个示例中，ChatRoom 组件使用一个 Effect 来保持与 chat.js 中定义的外部系统的连接。点击“打开聊天”以显示 ChatRoom 组件。这个沙盒在开发模式下运行，因此有一个额外的“连接并断开”的周期，就像 这里描述的 一样。尝试使用下拉菜单和输入框更改 roomId 和 serverUrl，并查看 Effect 如何重新连接到聊天。点击“关闭聊天”可以看到 Effect 最后一次断开连接。
```
App.jschat.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

function ChatRoom({ roomId }) {
  const [serverUrl, setServerUrl] = useState('https://localhost:1234');

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => {
      connection.disconnect();
    };
  }, [roomId, serverUrl]);

  return (
    <>
      <label>
        Server URL:{' '}
        <input
          value={serverUrl}
          onChange={e => setServerUrl(e.target.value)}
        />
      </label>
      <h1>Welcome to the {roomId} room!</h1>
    </>
  );
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  const [show, setShow] = useState(false);
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="general">general</option>
          <option value="travel">travel</option>
          <option value="music">music</option>
        </select>
      </label>
      <button onClick={() => setShow(!show)}>
        {show ? 'Close chat' : 'Open chat'}
      </button>
      {show && <hr />}
      {show && <ChatRoom roomId={roomId} />}
    </>
  );
}
```
显示更多下一个示例
### 在自定义 Hook 中封装 Effect
Effect 是一种 脱围机制：当你需要“走出 React 之外”或者当你的使用场景没有更好的内置解决方案时，你可以使用它们。如果你发现自己经常需要手动编写 Effect，那么这通常表明你需要为组件所依赖的通用行为提取一些 自定义 Hook。
例如，这个 useChatRoom 自定义 Hook 把 Effect 的逻辑“隐藏”在一个更具声明性的 API 之后：
```
function useChatRoom({ serverUrl, roomId }) {  useEffect(() => {    const options = {      serverUrl: serverUrl,      roomId: roomId    };    const connection = createConnection(options);    connection.connect();    return () => connection.disconnect();  }, [roomId, serverUrl]);}
```
然后你可以像这样从任何组件使用它：
```
function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  useChatRoom({    roomId: roomId,    serverUrl: serverUrl  });  // ...
```
在 React 生态系统中，还有许多用于各种用途的优秀的自定义 Hook。
了解有关在自定义 Hook 中封装 Effect 的更多信息。
#### 自定义 Hook 中封装 Effect 示例
1. 定制 useChatRoom Hook 2. 定制 useWindowListener Hook 3. 定制 useIntersectionObserver Hook
#### 第 1 个示例 共 3 个示例: 定制 useChatRoom Hook
此示例与 前面的一个示例 相同，但是逻辑被提取到一个自定义 Hook 中。
```
App.jsuseChatRoom.jschat.jsApp.jsReloadClearForkimport { useState } from 'react';
import { useChatRoom } from './useChatRoom.js';

function ChatRoom({ roomId }) {
  const [serverUrl, setServerUrl] = useState('https://localhost:1234');

  useChatRoom({
    roomId: roomId,
    serverUrl: serverUrl
  });

  return (
    <>
      <label>
        Server URL:{' '}
        <input
          value={serverUrl}
          onChange={e => setServerUrl(e.target.value)}
        />
      </label>
      <h1>Welcome to the {roomId} room!</h1>
    </>
  );
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  const [show, setShow] = useState(false);
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="general">general</option>
          <option value="travel">travel</option>
          <option value="music">music</option>
        </select>
      </label>
      <button onClick={() => setShow(!show)}>
        {show ? 'Close chat' : 'Open chat'}
      </button>
      {show && <hr />}
      {show && <ChatRoom roomId={roomId} />}
    </>
  );
}
```
显示更多下一个示例
### 控制非 React 小部件
有时，你希望外部系统与你组件的某些 props 或 state 保持同步。
例如，如果你有一个没有使用 React 编写的第三方地图小部件或视频播放器组件，你可以使用 Effect 调用该组件上的方法，使其状态与 React 组件的当前状态相匹配。此 Effect 创建了在 map-widget.js 中定义的 MapWidget 类的实例。当你更改 Map 组件的 zoomLevel prop 时，Effect 调用类实例上的 setZoom() 来保持同步：
```
App.jsMap.jsmap-widget.jsMap.jsReloadClearForkimport { useRef, useEffect } from 'react';
import { MapWidget } from './map-widget.js';

export default function Map({ zoomLevel }) {
  const containerRef = useRef(null);
  const mapRef = useRef(null);

  useEffect(() => {
    if (mapRef.current === null) {
      mapRef.current = new MapWidget(containerRef.current);
    }

    const map = mapRef.current;
    map.setZoom(zoomLevel);
  }, [zoomLevel]);

  return (
    <div
      style={{ width: 200, height: 200 }}
      ref={containerRef}
    />
  );
}
```
显示更多
在本例中，不需要 cleanup 函数，因为 MapWidget 类只管理传递给它的 DOM 节点。从树中删除 Map React 组件后，DOM 节点和 MapWidget 类实例都将被浏览器的 JavaScript 引擎的垃圾回收机制自动处理掉。
### 使用 Effect 请求数据
你可以使用 Effect 来为组件请求数据。请注意，如果你使用框架，使用框架的数据请求方式将比在 Effect 中手动编写要有效得多。
如果你想手动从 Effect 中请求数据，你的代码可能是这样的：
```
import { useState, useEffect } from 'react';import { fetchBio } from './api.js';export default function Page() {  const [person, setPerson] = useState('Alice');  const [bio, setBio] = useState(null);  useEffect(() => {    let ignore = false;    setBio(null);    fetchBio(person).then(result => {      if (!ignore) {        setBio(result);      }    });    return () => {      ignore = true;    };  }, [person]);  // ...
```
注意，ignore 变量被初始化为 false，并且在 cleanup 中被设置为 true。这样可以确保 你的代码不会受到“竞争条件”的影响：网络响应可能会以与你发送的不同的顺序到达。
```
App.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { fetchBio } from './api.js';

export default function Page() {
  const [person, setPerson] = useState('Alice');
  const [bio, setBio] = useState(null);
  useEffect(() => {
    let ignore = false;
    setBio(null);
    fetchBio(person).then(result => {
      if (!ignore) {
        setBio(result);
      }
    });
    return () => {
      ignore = true;
    }
  }, [person]);

  return (
    <>
      <select value={person} onChange={e => {
        setPerson(e.target.value);
      }}>
        <option value="Alice">Alice</option>
        <option value="Bob">Bob</option>
        <option value="Taylor">Taylor</option>
      </select>
      <hr />
      <p><i>{bio ?? 'Loading...'}</i></p>
    </>
  );
}
```
显示更多
你也可以使用 async / await 语法重写，但是你仍然需要提供一个 cleanup 函数：
```
App.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { fetchBio } from './api.js';

export default function Page() {
  const [person, setPerson] = useState('Alice');
  const [bio, setBio] = useState(null);
  useEffect(() => {
    async function startFetching() {
      setBio(null);
      const result = await fetchBio(person);
      if (!ignore) {
        setBio(result);
      }
    }

    let ignore = false;
    startFetching();
    return () => {
      ignore = true;
    }
  }, [person]);

  return (
    <>
      <select value={person} onChange={e => {
        setPerson(e.target.value);
      }}>
        <option value="Alice">Alice</option>
        <option value="Bob">Bob</option>
        <option value="Taylor">Taylor</option>
      </select>
      <hr />
      <p><i>{bio ?? 'Loading...'}</i></p>
    </>
  );
}
```
显示更多
直接在 Effect 中编写数据请求会显得重复，并且很难在以后添加缓存和服务端渲染等优化。使用自定义 Hook 更简单——不管是你自己的 Hook 还是由社区维护的 Hook。
深入探讨
#### Effect 中的数据请求有什么好的替代方法
显示更多
在 Effect 中使用 fetch 是 请求数据的一种流行方式，特别是在完全的客户端应用程序中。然而，这是一种非常手动的方法，而且有很大的缺点：
- Effect 不在服务器上运行。这意味着初始服务器渲染的 HTML 将只包含没有数据的 loading 状态。客户端电脑仅为了发现它现在需要加载数据，将不得不下载所有的脚本来渲染你的应用程序。这并不高效。
- 在 Effect 中直接请求数据很容易导致“网络瀑布”。当你渲染父组件时，它会请求一些数据，再渲染子组件，然后重复这样的过程来请求子组件的数据。如果网络不是很快，这将比并行请求所有数据要慢得多。
- 在 Effect 中直接请求数据通常意味着你不会预加载或缓存数据。例如，如果组件卸载后重新挂载，它不得不再次请求数据。
- 这不符合工效学。在调用 fetch 时，需要编写大量样板代码，以避免像 竞争条件 这样的 bug。
这些缺点并不仅仅体现在 React 上，它可能出现在所有挂载时请求数据的地方。与路由一样，要做好数据请求并非易事，因此我们推荐以下方法：
- 如果正在使用 框架，那么请使用其内置的数据获取机制。现代 React 框架已经集成了高效的数据获取机制，不会受到上述问题的影响。
- 否则，请考虑使用或构建客户端缓存。流行的开源解决方案包括 TanStack Query、useSWR 和 React Router v6.4+。你也可以构建自己的解决方案，在这种情况下，你将在底层使用 Effect，但还需添加逻辑以避免重复请求、缓存响应并避免网络瀑布效应（通过预加载数据或将数据需求提升到路由级别）。
如果这两种方法都不适合你，可以继续直接在 Effect 中请求数据。
### 指定响应式依赖项
注意，你无法“选择” Effect 的依赖项。Effect 代码中使用的每个 响应式值 都必须声明为依赖项。你的 Effect 依赖列表是由周围代码决定的：
```
function ChatRoom({ roomId }) { // 这是一个响应式值  const [serverUrl, setServerUrl] = useState('https://localhost:1234'); // 这也是一个响应式值  useEffect(() => {    const connection = createConnection(serverUrl, roomId); // 这个 Effect 读取这些响应式值    connection.connect();    return () => connection.disconnect();  }, [serverUrl, roomId]); // ✅ 因此你必须指定它们作为 Effect 的依赖项  // ...}
```
如果 serverUrl 或 roomId 任意一个发生变化，那么 Effect 将使用新的值重新连接到聊天室。
响应式值 包括 props 和直接在组件内声明的所有变量和函数。由于 roomId 和 serverUrl 是响应式值，你不能将它们从依赖项中移除。如果你试图省略它们，并且你的代码检查工具针对 React 进行了正确的配置，那么代码检查工具会将它标记为需要修复的错误：
```
function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => connection.disconnect();  }, []); // 🔴 React Hook useEffect 缺少依赖项：'roomId' 和 'serverUrl'  // ...}
```
要删除一个依赖项，你需要 “证明”给代码检查工具，表明它 不需要 作为一个依赖项。例如，你可以将 serverUrl 声明移动到组件外面，以证明它不是响应式的，并且不会在重新渲染时发生变化：
```
const serverUrl = 'https://localhost:1234'; // 不再是一个响应式值function ChatRoom({ roomId }) {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => connection.disconnect();  }, [roomId]); // ✅ 所有声明的依赖项  // ...}
```
现在 serverUrl 不再是一个响应式值（并且在重新渲染时也不会更改），它就不需要成为一个依赖项。如果 Effect 的代码不使用任何响应式值，则其依赖项列表应为空（[]）：
```
const serverUrl = 'https://localhost:1234'; // 不再是响应式值const roomId = 'music'; // 不再是响应式值function ChatRoom() {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => connection.disconnect();  }, []); // ✅ 所有声明的依赖项  // ...}
```
依赖项为空数组的 Effect 不会在组件任何的 props 或 state 发生改变时重新运行。
### 陷阱
如果你有一个现有的代码库，可能会有一些 Effect 像这样抑制了代码检查工具：
```
useEffect(() => {  // ...  // 🔴 避免这样抑制代码检查工具：  // eslint-ignore-next-line react-hooks/exhaustive-deps}, []);
```
当依赖项不匹配代码时，引入 bug 的风险很高。通过抑制代码检查工具，你“欺骗”了 React 关于你 Effect 所依赖的值。相反，证明它们是不必要的。
#### 传递响应式依赖项的示例
1. 传递依赖项数组 2. 传递空依赖项数组 3. 不传递依赖项数组
#### 第 1 个示例 共 3 个示例: 传递依赖项数组
如果指定了依赖项，则 Effect 在 初始提交后以及提交导致了依赖项变更后 运行。
```
useEffect(() => {  // ...}, [a, b]); // 如果 a 或 b 不同则会再次运行
```
在下面的示例中，serverUrl 和 roomId 是 响应式值，所以它们都必须被指定为依赖项。因此，在下拉列表中选择不同的聊天室或编辑服务器 URL 输入框会导致重新连接聊天室。但是，由于 message 没有在 Effect 中使用（所以它不是依赖项），编辑消息不会重新连接聊天室。
```
App.jschat.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

function ChatRoom({ roomId }) {
  const [serverUrl, setServerUrl] = useState('https://localhost:1234');
  const [message, setMessage] = useState('');

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => {
      connection.disconnect();
    };
  }, [serverUrl, roomId]);

  return (
    <>
      <label>
        Server URL:{' '}
        <input
          value={serverUrl}
          onChange={e => setServerUrl(e.target.value)}
        />
      </label>
      <h1>Welcome to the {roomId} room!</h1>
      <label>
        Your message:{' '}
        <input value={message} onChange={e => setMessage(e.target.value)} />
      </label>
    </>
  );
}

export default function App() {
  const [show, setShow] = useState(false);
  const [roomId, setRoomId] = useState('general');
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="general">general</option>
          <option value="travel">travel</option>
          <option value="music">music</option>
        </select>
        <button onClick={() => setShow(!show)}>
          {show ? 'Close chat' : 'Open chat'}
        </button>
      </label>
      {show && <hr />}
      {show && <ChatRoom roomId={roomId}/>}
    </>
  );
}
```
显示更多下一个示例
### 在 Effect 中根据先前 state 更新 state
当你想要在 Effect 中根据先前的 state 更新 state 时，你可能会遇到问题：
```
function Counter() {  const [count, setCount] = useState(0);  useEffect(() => {    const intervalId = setInterval(() => {      setCount(count + 1); // 你想要每秒递增该计数器...    }, 1000)    return () => clearInterval(intervalId);  }, [count]); // 🚩 ... 但是指定 `count` 作为依赖项总是重置间隔定时器。  // ...}
```
因为 count  是一个响应式值，所以必须在依赖项列表中指定它。但是，这会导致 Effect 在每次 count 更改时再次执行 cleanup 和 setup。这并不理想。
为了解决这个问题，将 c => c + 1 状态更新器传递给 setCount：
```
App.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCount(c => c + 1); // ✅ 传递一个 state 更新器
    }, 1000);
    return () => clearInterval(intervalId);
  }, []); // ✅现在 count 不是一个依赖项

  return <h1>{count}</h1>;
}
```
现在，你传递的是 c => c + 1 而不是 count + 1，因此 Effect 不再需要依赖于 count。由于这个修复，每次 count 更改时，它都不需要清理（cleanup）和设置（setup）间隔定时器。
### 删除不必要的对象依赖项
如果你的 Effect 依赖于在渲染期间创建的对象或函数，则它可能会频繁运行。例如，此 Effect 在每次提交后都重新连接，因为 options 对象 每次渲染都不同：
```
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) {  const [message, setMessage] = useState('');  const options = { // 🚩 这个对象在每次渲染时都是从头创建的    serverUrl: serverUrl,    roomId: roomId  };  useEffect(() => {    const connection = createConnection(options); // 它在 Effect 内部使用    connection.connect();    return () => connection.disconnect();  }, [options]); // 🚩 因此，这些依赖在每次提交时总是不同的  // ...
```
避免使用渲染期间创建的对象作为依赖项。相反，在 Effect 内部创建对象：
```
App.jschat.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const options = {
      serverUrl: serverUrl,
      roomId: roomId
    };
    const connection = createConnection(options);
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);

  return (
    <>
      <h1>Welcome to the {roomId} room!</h1>
      <input value={message} onChange={e => setMessage(e.target.value)} />
    </>
  );
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="general">general</option>
          <option value="travel">travel</option>
          <option value="music">music</option>
        </select>
      </label>
      <hr />
      <ChatRoom roomId={roomId} />
    </>
  );
}
```
显示更多
现在你已经在 Effect 内部创建了 options 对象，因此 Effect 仅依赖于 roomId 字符串。
通过此修复，在输入框中输入不会导致重新连接到聊天室。与会被重新创建的对象不同，像 roomId 这样的字符串只有在被设置为其它值时才会更改。阅读有关删除依赖项的更多信息。
### 删除不必要的函数依赖项
如果你的 Effect 依赖于在渲染期间创建的对象或函数，则它可能会频繁运行。例如，此 Effect 在每次提交后重新连接，因为 createOptions 函数 在每次渲染时都不同：
```
function ChatRoom({ roomId }) {  const [message, setMessage] = useState('');  function createOptions() { // 🚩 此函数在每次重新渲染都从头开始创建    return {      serverUrl: serverUrl,      roomId: roomId    };  }  useEffect(() => {    const options = createOptions(); // 它在 Effect 中被使用    const connection = createConnection();    connection.connect();    return () => connection.disconnect();  }, [createOptions]); // 🚩 因此，此依赖项在每次提交时都是不同的  // ...
```
就其本身而言，在每次重新渲染时从头新建一个函数不是问题。你不需要优化它。但是，如果你将其用作 Effect 的依赖项，则会导致 Effect 在每次重新渲染后重新运行。
避免使用在渲染期间创建的函数作为依赖项，请在 Effect 内部声明它：
```
App.jschat.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  const [message, setMessage] = useState('');

  useEffect(() => {
    function createOptions() {
      return {
        serverUrl: serverUrl,
        roomId: roomId
      };
    }

    const options = createOptions();
    const connection = createConnection(options);
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);

  return (
    <>
      <h1>Welcome to the {roomId} room!</h1>
      <input value={message} onChange={e => setMessage(e.target.value)} />
    </>
  );
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  return (
    <>
      <label>
        Choose the chat room:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="general">general</option>
          <option value="travel">travel</option>
          <option value="music">music</option>
        </select>
      </label>
      <hr />
      <ChatRoom roomId={roomId} />
    </>
  );
}
```
显示更多
现在你在 Effect 内部定义了 createOptions 函数，这样 Effect 本身只依赖于 roomId 字符串。通过此修复，输入框的输入不会重新连接聊天室。与被重新创建的函数不同，像 roomId 这样的字符串除非你将其设置为其它值，否则它不会改变。了解更多有关移除依赖项的信息。
### 从 Effect 读取最新的 props 和 state
默认情况下，在 Effect 中读取响应式值时，必须将其添加为依赖项。这样可以确保你的 Effect 对该值的每次更改都“作出响应”。对于大多数依赖项，这是你想要的行为。
然而，有时你想要从 Effect 中获取 最新的 props 和 state，而不“响应”它们。例如，假设你想记录每次页面访问时购物车中的商品数量：
```
function Page({ url, shoppingCart }) {  useEffect(() => {    logVisit(url, shoppingCart.length);  }, [url, shoppingCart]); // ✅ 所有声明的依赖项  // ...}
```
如果你想在每次 url 更改后记录一次新的页面访问，而不是在 shoppingCart 更改后记录，该怎么办？你不能在不违反 响应规则 的情况下将 shoppingCart 从依赖项中移除。然而，你可以表达你 不希望 某些代码对更改做出“响应”，即使它是在 Effect 内部调用的。使用 useEffectEvent Hook 声明 Effect 事件，并将读取 shoppingCart 的代码移入其中：
```
function Page({ url, shoppingCart }) {  const onVisit = useEffectEvent(visitedUrl => {    logVisit(visitedUrl, shoppingCart.length)  });  useEffect(() => {    onVisit(url);  }, [url]); // ✅ 所有声明的依赖项  // ...}
```
Effect 事件不是响应式的，必须始终省略其作为 Effect 的依赖项。这就是让你在其中放置非响应式代码（可以在其中读取某些 props 和 state 的最新值）的原因。通过在 onVisit 中读取 shoppingCart，确保了 shoppingCart 不会使 Effect 重新运行。
阅读更多关于 Effect Event 如何让你分离响应式和非响应式代码的内容。
### 在服务器和客户端上显示不同的内容
如果你的应用程序使用服务端（直接 或通过 框架）渲染，你的组件将会在两个不同的环境中渲染。在服务器上，它将渲染生成初始 HTML。在客户端，React 将再次运行渲染代码，以便将事件处理附加到该 HTML 上。这就是为什么要让 hydration 发挥作用，你的初始渲染输出必须在客户端和服务器上完全相同。
在极少数情况下，你可能需要在客户端上显示不同的内容。例如，如果你的应用从 localStorage 中读取某些数据，服务器上肯定不可能做到这一点。以下是这如何实现的：
```
function MyComponent() {  const [didMount, setDidMount] = useState(false);  useEffect(() => {    setDidMount(true);  }, []);  if (didMount) {    // ... 返回仅客户端的 JSX ...  }  else {    // ... 返回初始 JSX ...  }}
```
当应用加载时，用户首先会看到初始渲染的输出。然后，当它加载完并进行激活时，Effect 将会运行并且将 didMount 设置为 true，从而触发重新渲染。这将切换到仅在客户端的渲染输出。Effect 不在服务器上运行，这就是 didMount 在初始服务器渲染期间为 false 的原因。
谨慎使用此模式。请记住，网络连接速度较慢的用户将在相当长的时间内（可能是数秒钟）看到初始内容，因此你不希望对组件的外观进行突兀的更改。在许多情况下，你可以通过使用 CSS 条件性地显示不同的内容来避免这种需要。
## 疑难解答
### Effect 在组件挂载时运行了两次
在开发环境下，如果开启严格模式，React 会在实际运行 setup 之前额外运行一次 setup 和 cleanup。
这是一个压力测试，用于验证 Effect 的逻辑是否正确实现。如果出现可见问题，则 cleanup 函数缺少某些逻辑。cleanup 函数应该停止或撤消 setup 函数所做的任何操作。一般来说，用户不应该能够区分 setup 被调用一次（如在生产环境中）和调用 setup → cleanup → setup 序列（如在开发环境中）。
阅读更多关于 这如何帮助找到 bug 和 如何修复你的逻辑。
### Effect 在每次重新渲染后都运行
首先，请检查是否忘记指定依赖项数组：
```
useEffect(() => {  // ...}); // 🚩 没有依赖项数组：每次提交后重新运行！
```
如果你已经指定了依赖项数组，你的 Effect 仍循环地重新运行，那是因为你的某个依赖项在每次重新渲染时都是不同的。
你可以通过手动打印依赖项到控制台来调试此问题：
```
  useEffect(() => {    // ..  }, [serverUrl, roomId]);  console.log([serverUrl, roomId]);
```
然后，你可以右键单击控制台中来自不同重新渲染的数组，并都选择“存储为全局变量”。假设第一个被保存为 temp1，第二个被保存为 temp2，然后你可以使用浏览器控制台来检查两个数组中的每个依赖项是否相同：
```
Object.is(temp1[0], temp2[0]); // 第一个依赖项在数组之间是否相同？Object.is(temp1[1], temp2[1]); // 第二个依赖项在数组之间是否相同？Object.is(temp1[2], temp2[2]); // ... 以此类推检查每个依赖项 ...
```
当你发现某个依赖项在每次重新渲染都不同时，通常可以通过以下方式之一来解决：
- 在 Effect 中根据先前 state 更新 state
- 删除不必要的对象依赖项
- 删除不必要的函数依赖项
- 从 Effect 读取最新的 props 和 state
作为最后的手段（如果这些方法没有帮助），使用 useMemo 或 useCallback（用于函数）包装其创建。
### Effect 函数一直在无限循环中运行
如果你的 Effect 函数一直在无限循环中运行，那么必须满足以下两个条件：
- 你的 Effect 函数更新了一些状态。
- 这些状态的改变导致了重新渲染，从而导致 Effect 函数依赖的状态发生改变。
在开始修复问题之前，问问自己，你的 Effect 是否连接到了某个外部系统（如 DOM、网络、第三方小部件等）。为什么你的 Effect 函数需要设置状态？它是否与外部系统同步？或者你正在试图用它来管理应用程序的数据流？
如果没有外部系统，请考虑 完全删除 Effect 函数 是否可以简化你的逻辑。
如果你真的正在与某个外部系统同步，请考虑为什么以及在何种条件下你的 Effect 函数应该更新状态。是否有任何变化会影响组件的可视输出？如果你需要跟踪一些不用于渲染的数据，使用一个 ref（它不会触发重新渲染）可能更合适。验证你的 Effect 函数不会超过需要地更新状态（并触发重新渲染）。
最后，如果你的 Effect 函数在正确的时机更新了状态，但仍然存在一个循环，那是因为该状态更新导致 Effect 的一个依赖项发生了更改。阅读如何调试依赖项变更。
### 即使组件没有卸载，cleanup 逻辑也会运行
cleanup 函数不仅在卸载期间运行，也在每个依赖项变更的重新渲染前运行。此外，在开发环境中，React 在组件挂载后会立即额外运行一次 setup + cleanup。
如果你的 cleanup 代码没有相应的 setup 代码，这通常是一种代码异味（code smell）：
```
useEffect(() => {  // 🔴 避免：cleanup 逻辑没有相应的 setup 逻辑  return () => {    doSomething();  };}, []);
```
你的 cleanup 逻辑应该与 setup 逻辑“对称”，并且应该停止或撤销任何 setup 做的事情：
```
  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => {      connection.disconnect();    };  }, [serverUrl, roomId]);
```
了解 Effect 生命周期与组件的生命周期有何不同。
### 我的 Effect 做了一些视觉相关的事情，在它运行之前我看到了一个闪烁
如果 Effect 一定要阻止浏览器绘制屏幕，使用 useLayoutEffect 替换 useEffect。请注意，绝大多数的 Effect 都不需要这样。只有当在浏览器绘制之前运行 Effect 非常重要的时候才需要如此：例如，在用户看到 tooltip 之前测量并定位它。
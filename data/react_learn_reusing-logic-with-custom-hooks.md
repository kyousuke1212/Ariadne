学习 React脱围机制 Copy pageCopy
# 使用自定义 Hook 复用逻辑
React 有一些内置 Hook，例如 useState，useContext 和 useEffect。有时你需要一个用途更特殊的 Hook：例如获取数据，记录用户是否在线或者连接聊天室。虽然 React 中可能没有这些 Hook，但是你可以根据应用需求创建自己的 Hook。
### 你将会学习到
- 什么是自定义 Hook，以及如何编写
- 如何在组件间重用逻辑
- 如何给自定义 Hook 命名以及如何构建
- 提取自定义 Hook 的时机和原因
## 自定义 Hook：组件间共享逻辑
假设你正在开发一款重度依赖网络的应用（和大多数应用一样）。当用户使用应用时网络意外断开，你需要提醒他。你会怎么处理呢？看上去组件需要两个东西：
- 一个追踪网络是否在线的 state。
- 一个订阅全局 online 和 offline 事件并更新上述 state 的 Effect。
这会让组件与网络状态保持 同步。你也许可以像这样开始：
```
App.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';

export default function StatusBar() {
  const [isOnline, setIsOnline] = useState(true);
  useEffect(() => {
    function handleOnline() {
      setIsOnline(true);
    }
    function handleOffline() {
      setIsOnline(false);
    }
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  return <h1>{isOnline ? '✅ Online' : '❌ Disconnected'}</h1>;
}
```
显示更多
试着开启和关闭网络，注意观察 StatusBar 组件应对你的行为是如何更新的。
假设现在你想在另一个不同的组件里 也 使用同样的逻辑。你希望实现一个保存按钮，每当网络断开这个按钮就会不可用并且显示“Reconnecting…”而不是“Save progress”。
你可以从复制粘贴 isOnline state 和 Effect 到 SaveButton 组件开始：
```
App.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';

export default function SaveButton() {
  const [isOnline, setIsOnline] = useState(true);
  useEffect(() => {
    function handleOnline() {
      setIsOnline(true);
    }
    function handleOffline() {
      setIsOnline(false);
    }
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  function handleSaveClick() {
    console.log('✅ Progress saved');
  }

  return (
    <button disabled={!isOnline} onClick={handleSaveClick}>
      {isOnline ? 'Save progress' : 'Reconnecting...'}
    </button>
  );
}
```
显示更多
如果你关闭网络，可以发现这个按钮的外观变了。
这两个组件都能很好地工作，但不幸的是他们的逻辑重复了。他们看上去有不同的 视觉外观，但你依然想复用他们的逻辑。
### 从组件中提取自定义 Hook
假设有一个内置 Hook useOnlineStatus，它与 useState 和 useEffect 相似。那么你就可以简化这两个组件并移除他们之间的重复部分：
```
function StatusBar() {  const isOnline = useOnlineStatus();  return <h1>{isOnline ? '✅ Online' : '❌ Disconnected'}</h1>;}function SaveButton() {  const isOnline = useOnlineStatus();  function handleSaveClick() {    console.log('✅ Progress saved');  }  return (    <button disabled={!isOnline} onClick={handleSaveClick}>      {isOnline ? 'Save progress' : 'Reconnecting...'}    </button>  );}
```
尽管目前还没有这样的内置 Hook，但是你可以自己写。声明一个 useOnlineStatus 函数，并把组件里早前写的所有重复代码移入该函数：
```
function useOnlineStatus() {  const [isOnline, setIsOnline] = useState(true);  useEffect(() => {    function handleOnline() {      setIsOnline(true);    }    function handleOffline() {      setIsOnline(false);    }    window.addEventListener('online', handleOnline);    window.addEventListener('offline', handleOffline);    return () => {      window.removeEventListener('online', handleOnline);      window.removeEventListener('offline', handleOffline);    };  }, []);  return isOnline;}
```
在函数结尾处返回 isOnline。这可以让组件读取到该值：
```
App.jsuseOnlineStatus.jsApp.jsReloadClearForkimport { useOnlineStatus } from './useOnlineStatus.js';

function StatusBar() {
  const isOnline = useOnlineStatus();
  return <h1>{isOnline ? '✅ Online' : '❌ Disconnected'}</h1>;
}

function SaveButton() {
  const isOnline = useOnlineStatus();

  function handleSaveClick() {
    console.log('✅ Progress saved');
  }

  return (
    <button disabled={!isOnline} onClick={handleSaveClick}>
      {isOnline ? 'Save progress' : 'Reconnecting...'}
    </button>
  );
}

export default function App() {
  return (
    <>
      <SaveButton />
      <StatusBar />
    </>
  );
}
```
显示更多
切换网络状态验证一下是否会同时更新两个组件。
现在组件里没有那么多的重复逻辑了。更重要的是，组件内部的代码描述的是想要做什么（使用在线状态！），而不是怎么做（通过订阅浏览器事件完成）。
当提取逻辑到自定义 Hook 时，你可以隐藏如何处理外部系统或者浏览器 API 这些乱七八糟的细节。组件内部的代码表达的是目标而不是具体实现。
### Hook 的名称必须永远以 use 开头
React 应用是由组件构成，而组件由内置或自定义 Hook 构成。可能你经常使用别人写的自定义 Hook，但偶尔也要自己写！
你必须遵循以下这些命名公约：
- React 组件名称必须以大写字母开头，比如 StatusBar 和 SaveButton。React 组件还需要返回一些 React 能够显示的内容，比如一段 JSX。
- Hook 的名称必须以 use 开头，然后紧跟一个大写字母，就像内置的 useState 或者本文早前的自定义 useOnlineStatus 一样。Hook 可以返回任意值。
这个公约保证你始终能一眼识别出组件并且知道它的 state，Effect 以及其他的 React 特性可能“隐藏”在哪里。例如如果你在组件内部看见 getColor() 函数调用，就可以确定它里面不可能包含 React state，因为它的名称没有以 use 开头。但是像 useOnlineStatus() 这样的函数调用就很可能包含对内部其他 Hook 的调用！
### 注意
如果你为 React 配置了 代码检查工具，它会强制执行这个命名公约。现在滑动到上面的 sandbox，并将 useOnlineStatus 重命名为 getOnlineStatus。注意此时代码检查工具将不会再允许你在其内部调用 useState 或者 useEffect。只有 Hook 和组件可以调用其他 Hook！
深入探讨
#### 渲染期间调用的所有函数都应该以 use 前缀开头么？
显示更多
不。没有 调用 Hook 的函数不需要 变成 Hook。
如果你创建的函数没有调用任何 Hook 方法，在命名时应避免使用 use 前缀，把它当成一个常规函数去命名。如下案例中的 useSorted 函数就没有调用任何 Hook 方法，所以更推荐用 getSorted 来命名：
```
// 🔴 避免：没有调用其他 Hook 的 Hookfunction useSorted(items) {  return items.slice().sort();}// ✅ 好：没有使用 Hook 的常规函数function getSorted(items) {  return items.slice().sort();}
```
这保证你的代码可以在包含条件语句在内的任何地方调用这个常规函数：
```
function List({ items, shouldSort }) {  let displayedItems = items;  if (shouldSort) {    // ✅ 在条件分支里调用 getSorted() 是没问题的，因为它不是 Hook    displayedItems = getSorted(items);  }  // ...}
```
哪怕内部只使用了一个 Hook，你也应该给这个函数加 use 前缀（让它成为一个 Hook）：
```
// ✅ 好：一个使用了其他 Hook 的 Hookfunction useAuth() {  return useContext(Auth);}
```
技术上 React 对此并不强制要求。原则上你可以写出不调用其他 Hook 的 Hook。但这常常会难以理解且受限，所以最好避免这种方式。但是它在极少数场景下可能是有益的。例如函数目前也许并没有使用任何 Hook，但是你计划未来在该函数内部添加一些 Hook 调用。那么使用 use 前缀命名就很有意义：
```
// ✅ 好：之后可能使用其他 Hook 的 Hookfunction useAuth() {  // TODO: 当认证功能实现以后，替换这一行：  // 返回 useContext(Auth)；  return TEST_USER;}
```
接下来组件就不能在条件语句里调用这个函数。当你在内部实际添加了 Hook 调用时，这一点将变得很重要。如果你（现在或者之后）没有计划在内部使用 Hook，请不要让它变成 Hook。
### 自定义 Hook 共享的是状态逻辑，而不是状态本身
之前的例子里，当你开启或关闭网络时，两个组件一起更新了。但是两个组件共享 state 变量 isOnline 这种想法是错的。看这段代码：
```
function StatusBar() {  const isOnline = useOnlineStatus();  // ...}function SaveButton() {  const isOnline = useOnlineStatus();  // ...}
```
它的工作方式和你之前提取的重复代码一模一样：
```
function StatusBar() {  const [isOnline, setIsOnline] = useState(true);  useEffect(() => {    // ...  }, []);  // ...}function SaveButton() {  const [isOnline, setIsOnline] = useState(true);  useEffect(() => {    // ...  }, []);  // ...}
```
这是完全独立的两个 state 变量和 Effect！只是碰巧同一时间值一样，因为你使用了相同的外部值（网络是否开启）同步两个组件。
为了更好的说明这一点，我们需要一个不同的示例。看下面的 Form 组件：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Form() {
  const [firstName, setFirstName] = useState('Mary');
  const [lastName, setLastName] = useState('Poppins');

  function handleFirstNameChange(e) {
    setFirstName(e.target.value);
  }

  function handleLastNameChange(e) {
    setLastName(e.target.value);
  }

  return (
    <>
      <label>
        First name:
        <input value={firstName} onChange={handleFirstNameChange} />
      </label>
      <label>
        Last name:
        <input value={lastName} onChange={handleLastNameChange} />
      </label>
      <p><b>Good morning, {firstName} {lastName}.</b></p>
    </>
  );
}
```
显示更多
每个表单域都有一部分重复的逻辑：
- 都有一个 state（firstName 和 lastName）。
- 都有 change 事件的处理函数（handleFirstNameChange 和 handleLastNameChange）。
- 都有为输入框指定 value 和 onChange 属性的 JSX。
你可以提取重复的逻辑到自定义 Hook useFormInput：
```
App.jsuseFormInput.jsuseFormInput.jsReloadClearForkimport { useState } from 'react';

export function useFormInput(initialValue) {
  const [value, setValue] = useState(initialValue);

  function handleChange(e) {
    setValue(e.target.value);
  }

  const inputProps = {
    value: value,
    onChange: handleChange
  };

  return inputProps;
}
```
显示更多
注意它只声明了 一个 state 变量，叫做 value。
但 Form 组件调用了 两次 useFormInput：
```
function Form() {  const firstNameProps = useFormInput('Mary');  const lastNameProps = useFormInput('Poppins');  // ...
```
这就是为什么它工作的时候像声明了两个单独的 state 变量！
自定义 Hook 共享的只是状态逻辑而不是状态本身。对 Hook 的每个调用完全独立于对同一个 Hook 的其他调用。这就是上面两个 sandbox 结果完全相同的原因。如果愿意，你可以划上去进行比较。提取自定义 Hook 前后组件的行为是一致的。
当你需要在多个组件之间共享 state 本身时，需要 将变量提升并传递下去。
## 在 Hook 之间传递响应值
每当组件重新渲染，自定义 Hook 中的代码就会重新运行。这就是组件和自定义 Hook 都 需要是纯函数 的原因。我们应该把自定义 Hook 的代码看作组件主体的一部分。
由于自定义 Hook 会随着组件一起重新渲染，所以组件可以一直接收到最新的 props 和 state。想知道这意味着什么，那就看看这个聊天室的示例。修改 serverUrl 或者 roomId：
```
App.jsChatRoom.jschat.jsnotifications.jsChatRoom.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection } from './chat.js';
import { showNotification } from './notifications.js';

export default function ChatRoom({ roomId }) {
  const [serverUrl, setServerUrl] = useState('https://localhost:1234');

  useEffect(() => {
    const options = {
      serverUrl: serverUrl,
      roomId: roomId
    };
    const connection = createConnection(options);
    connection.on('message', (msg) => {
      showNotification('New message: ' + msg);
    });
    connection.connect();
    return () => connection.disconnect();
  }, [roomId, serverUrl]);

  return (
    <>
      <label>
        Server URL:
        <input value={serverUrl} onChange={e => setServerUrl(e.target.value)} />
      </label>
      <h1>Welcome to the {roomId} room!</h1>
    </>
  );
}
```
显示更多
当你修改 serverUrl 或者 roomId 时，Effect 会对 你的修改做出“响应” 并重新同步。你可以通过每次修改 Effect 依赖项时聊天室重连的控制台消息来区分。
现在将 Effect 代码移入自定义 Hook：
```
export function useChatRoom({ serverUrl, roomId }) {  useEffect(() => {    const options = {      serverUrl: serverUrl,      roomId: roomId    };    const connection = createConnection(options);    connection.connect();    connection.on('message', (msg) => {      showNotification('New message: ' + msg);    });    return () => connection.disconnect();  }, [roomId, serverUrl]);}
```
这让 ChatRoom 组件调用自定义 Hook，而不需要担心内部怎么工作：
```
export default function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  useChatRoom({    roomId: roomId,    serverUrl: serverUrl  });  return (    <>      <label>        Server URL:        <input value={serverUrl} onChange={e => setServerUrl(e.target.value)} />      </label>      <h1>Welcome to the {roomId} room!</h1>    </>  );}
```
这看上去简洁多了（但是它做的是同一件事）！
注意逻辑 仍然响应 props 和 state 的变化。尝试编辑 server URL 或选中的房间：
```
App.jsChatRoom.jsuseChatRoom.jschat.jsnotifications.jsChatRoom.jsReloadClearForkimport { useState } from 'react';
import { useChatRoom } from './useChatRoom.js';

export default function ChatRoom({ roomId }) {
  const [serverUrl, setServerUrl] = useState('https://localhost:1234');

  useChatRoom({
    roomId: roomId,
    serverUrl: serverUrl
  });

  return (
    <>
      <label>
        Server URL:
        <input value={serverUrl} onChange={e => setServerUrl(e.target.value)} />
      </label>
      <h1>Welcome to the {roomId} room!</h1>
    </>
  );
}
```
显示更多
注意你如何获取 Hook 的返回值：
```
export default function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  useChatRoom({    roomId: roomId,    serverUrl: serverUrl  });  // ...
```
并把它作为输入传给另一个 Hook：
```
export default function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  useChatRoom({    roomId: roomId,    serverUrl: serverUrl  });  // ...
```
每次 ChatRoom 组件重新渲染，它就会传最新的 roomId 和 serverUrl 到你的 Hook。这就是每当重新渲染后他们的值不一样时你的 Effect 会重连聊天室的原因。（如果你曾经使用过音视频处理软件，像这样的 Hook 链也许会让你想起音视频效果链。好似 useState 的输出作为 useChatRoom 的输入）。
### 把事件处理函数传到自定义 Hook 中
当你在更多组件中使用 useChatRoom 时，你可能希望组件能定制它的行为。例如现在 Hook 内部收到消息的处理逻辑是硬编码：
```
export function useChatRoom({ serverUrl, roomId }) {  useEffect(() => {    const options = {      serverUrl: serverUrl,      roomId: roomId    };    const connection = createConnection(options);    connection.connect();    connection.on('message', (msg) => {      showNotification('New message: ' + msg);    });    return () => connection.disconnect();  }, [roomId, serverUrl]);}
```
假设你想把这个逻辑移回到组件中：
```
export default function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  useChatRoom({    roomId: roomId,    serverUrl: serverUrl,    onReceiveMessage(msg) {      showNotification('New message: ' + msg);    }  });  // ...
```
完成这个工作需要修改自定义 Hook，把 onReceiveMessage 作为其命名选项之一：
```
export function useChatRoom({ serverUrl, roomId, onReceiveMessage }) {  useEffect(() => {    const options = {      serverUrl: serverUrl,      roomId: roomId    };    const connection = createConnection(options);    connection.connect();    connection.on('message', (msg) => {      onReceiveMessage(msg);    });    return () => connection.disconnect();  }, [roomId, serverUrl, onReceiveMessage]); // ✅ 声明了所有的依赖}
```
这个修改有效果，但是当自定义 Hook 接受事件处理函数时，你还可以进一步改进。
增加对 onReceiveMessage 的依赖并不理想，因为每次组件重新渲染时聊天室就会重新连接。 通过 将这个事件处理函数包裹到 Effect Event 中来将它从依赖中移除：
```
import { useEffect, useEffectEvent } from 'react';// ...export function useChatRoom({ serverUrl, roomId, onReceiveMessage }) {  const onMessage = useEffectEvent(onReceiveMessage);  useEffect(() => {    const options = {      serverUrl: serverUrl,      roomId: roomId    };    const connection = createConnection(options);    connection.connect();    connection.on('message', (msg) => {      onMessage(msg);    });    return () => connection.disconnect();  }, [roomId, serverUrl]); // ✅ 声明所有依赖}
```
现在每次 ChatRoom 组件重新渲染时聊天室都不会重连。这是一个将事件处理函数传给自定义 Hook 的完整且有效的 demo，你可以尝试一下：
```
App.jsChatRoom.jsuseChatRoom.jschat.jsnotifications.jsChatRoom.jsReloadClearForkimport { useState } from 'react';
import { useChatRoom } from './useChatRoom.js';
import { showNotification } from './notifications.js';

export default function ChatRoom({ roomId }) {
  const [serverUrl, setServerUrl] = useState('https://localhost:1234');

  useChatRoom({
    roomId: roomId,
    serverUrl: serverUrl,
    onReceiveMessage(msg) {
      showNotification('New message: ' + msg);
    }
  });

  return (
    <>
      <label>
        Server URL:
        <input value={serverUrl} onChange={e => setServerUrl(e.target.value)} />
      </label>
      <h1>Welcome to the {roomId} room!</h1>
    </>
  );
}
```
显示更多
注意你不再需要为了使用它而去了解 useChatRoom 是 如何 工作的。你可以把它添加到其他任意组件，传递其他任意选项，而它会以同样的方式工作。这就是自定义 Hook 的强大之处。
## 什么时候使用自定义 Hook
你没必要对每段重复的代码都提取自定义 Hook。一些重复是好的。例如像早前提取的包裹单个 useState 调用的 useFormInput Hook 就是没有必要的。
但是每当你写 Effect 时，考虑一下把它包裹在自定义 Hook 是否更清晰。你不应该经常使用 Effect，所以如果你正在写 Effect 就意味着你需要“走出 React”和某些外部系统同步，或者需要做一些 React 中没有对应内置 API 的事。把 Effect 包裹进自定义 Hook 可以准确表达你的目标以及数据在里面是如何流动的。
例如，假设 ShippingForm 组件展示两个下拉菜单：一个显示城市列表，另一个显示选中城市的区域列表。你可能一开始会像这样写代码：
```
function ShippingForm({ country }) {  const [cities, setCities] = useState(null);  // 这个 Effect 拉取一个国家的城市数据  useEffect(() => {    let ignore = false;    fetch(`/api/cities?country=${country}`)      .then(response => response.json())      .then(json => {        if (!ignore) {          setCities(json);        }      });    return () => {      ignore = true;    };  }, [country]);  const [city, setCity] = useState(null);  const [areas, setAreas] = useState(null);  // 这个 Effect 拉取选中城市的区域列表  useEffect(() => {    if (city) {      let ignore = false;      fetch(`/api/areas?city=${city}`)        .then(response => response.json())        .then(json => {          if (!ignore) {            setAreas(json);          }        });      return () => {        ignore = true;      };    }  }, [city]);  // ...
```
尽管这部分代码是重复的，但是 把这些 Effect 各自分开是正确的。他们同步两件不同的事情，所以不应该把他们合并到同一个 Effect。而是提取其中的通用逻辑到你自己的 useData Hook 来简化上面的 ShippingForm 组件：
```
function useData(url) {  const [data, setData] = useState(null);  useEffect(() => {    if (url) {      let ignore = false;      fetch(url)        .then(response => response.json())        .then(json => {          if (!ignore) {            setData(json);          }        });      return () => {        ignore = true;      };    }  }, [url]);  return data;}
```
现在你可以在 ShippingForm 组件中调用 useData 替换两个 Effect：
```
function ShippingForm({ country }) {  const cities = useData(`/api/cities?country=${country}`);  const [city, setCity] = useState(null);  const areas = useData(city ? `/api/areas?city=${city}` : null);  // ...
```
提取自定义 Hook 让数据流清晰。输入 url，就会输出 data。通过把 Effect “隐藏”在 useData 内部，你也可以防止一些正在处理 ShippingForm 组件的人向里面添加 不必要的依赖。随着时间的推移，应用中大部分 Effect 都会存在于自定义 Hook 内部。
深入探讨
#### 让你的自定义 Hook 专注于具体的高级用例
显示更多
从选择自定义 Hook 名称开始。如果你难以选择一个清晰的名称，这可能意味着你的 Effect 和组件逻辑剩余的部分耦合度太高，还没有做好被提取的准备。
理想情况下，你的自定义 Hook 名称应该清晰到即使一个不经常写代码的人也能很好地猜中自定义 Hook 的功能，输入和返回：
- ✅ useData(url)
- ✅ useImpressionLog(eventName, extraData)
- ✅ useChatRoom(options)
当你和外部系统同步的时候，你的自定义 Hook 名称可能会更加专业，并使用该系统特定的术语。只要对熟悉这个系统的人来说名称清晰就可以：
- ✅ useMediaQuery(query)
- ✅ useSocket(url)
- ✅ useIntersectionObserver(ref, options)
保持自定义 Hook 专注于具体的高级用例。避免创建和使用作为 useEffect API 本身的替代品和 wrapper 的自定义“生命周期” Hook：
- 🔴 useMount(fn)
- 🔴 useEffectOnce(fn)
- 🔴 useUpdateEffect(fn)
例如这个 useMount Hook 试图保证一些代码只在“加载”时运行：
```
function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  // 🔴 避免：使用自定义“生命周期” Hook  useMount(() => {    const connection = createConnection({ roomId, serverUrl });    connection.connect();    post('/analytics/event', { eventName: 'visit_chat' });  });  // ...}// 🔴 避免：创建自定义“生命周期” Hookfunction useMount(fn) {  useEffect(() => {    fn();  }, []); // 🔴 React Hook useEffect 缺少依赖项: 'fn'}
```
像 useMount 这样的自定义“生命周期” Hook 不是很适合 React 范式。例如示例代码有一个错误（它没有对 roomId 或 serverUrl 的变化做出“响应” ），但是代码检查工具并不会向你发出对应的警告，因为它只能检测 useEffect 的直接调用。并不了解你的 Hook。
如果你正在编写 Effect，请从直接使用 React API 开始：
```
function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  // ✅ 好：通过用途分割的两个原始 Effect  useEffect(() => {    const connection = createConnection({ serverUrl, roomId });    connection.connect();    return () => connection.disconnect();  }, [serverUrl, roomId]);  useEffect(() => {    post('/analytics/event', { eventName: 'visit_chat', roomId });  }, [roomId]);  // ...}
```
然后你可以（但不是必须的）为不同的高级用例提取自定义 Hook：
```
function ChatRoom({ roomId }) {  const [serverUrl, setServerUrl] = useState('https://localhost:1234');  // ✅ 非常好：以用途命名的自定义 Hook  useChatRoom({ serverUrl, roomId });  useImpressionLog('visit_chat', { roomId });  // ...}
```
好的自定义 Hook 通过限制功能使代码调用更具声明性。例如 useChatRoom(options) 只能连接聊天室，而 useImpressionLog(eventName, extraData) 只能向分析系统发送展示日志。如果你的自定义 Hook API 没有约束用例且非常抽象，那么在长期的运行中，它引入的问题可能比解决的问题更多。
### 自定义 Hook 帮助你迁移到更好的模式
Effect 是一个 脱围机制：当需要“走出 React”且用例没有更好的内置解决方案时你可以使用他们。随着时间的推移，React 团队的目标是通过给更具体的问题提供更具体的解决方案来最小化应用中的 Effect 数量。把你的 Effect 包裹进自定义 Hook，当这些解决方案可用时升级代码会更加容易。
让我们回到这个示例：
```
App.jsuseOnlineStatus.jsuseOnlineStatus.jsReloadClearForkimport { useState, useEffect } from 'react';

export function useOnlineStatus() {
  const [isOnline, setIsOnline] = useState(true);
  useEffect(() => {
    function handleOnline() {
      setIsOnline(true);
    }
    function handleOffline() {
      setIsOnline(false);
    }
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);
  return isOnline;
}
```
显示更多
在上述示例中，useOnlineStatus 借助一组 useState 和 useEffect 实现。但这不是最好的解决方案。它有许多边界用例没有考虑到。例如，它认为当组件加载时，isOnline 已经为 true，但是如果网络已经离线的话这就是错误的。你可以使用浏览器的 navigator.onLine API 来检查，但是在生成初始 HTML 的服务端直接使用它是没用的。简而言之这段代码可以改进。
React 包含了一个叫做 useSyncExternalStore 的专用 API，它可以解决你所有这些问题。这里展示了如何利用这个新 API 来重写你的 useOnlineStatus Hook：
```
App.jsuseOnlineStatus.jsuseOnlineStatus.jsReloadClearForkimport { useSyncExternalStore } from 'react';

function subscribe(callback) {
  window.addEventListener('online', callback);
  window.addEventListener('offline', callback);
  return () => {
    window.removeEventListener('online', callback);
    window.removeEventListener('offline', callback);
  };
}

export function useOnlineStatus() {
  return useSyncExternalStore(
    subscribe,
    () => navigator.onLine, // 如何在客户端获取值
    () => true // 如何在服务端获取值
  );
}
```
显示更多
注意 你不需要修改任何组件 就能完成这次迁移：
```
function StatusBar() {  const isOnline = useOnlineStatus();  // ...}function SaveButton() {  const isOnline = useOnlineStatus();  // ...}
```
这是把 Effect 包裹进自定义 Hook 有益的另一个原因：
- 你让进出 Effect 的数据流非常清晰。
- 你让组件专注于目标，而不是 Effect 的准确实现。
- 当 React 增加新特性时，你可以在不修改任何组件的情况下移除这些 Effect。
和 设计系统 相似，你可能会发现从应用的组件中提取通用逻辑到自定义 Hook 是非常有帮助的。这会让你的组件代码专注于目标，并且避免经常写原始 Effect。许多很棒的自定义 Hook 是由 React 社区维护的。
深入探讨
#### React 会为数据获取提供内置解决方案么？
显示更多
Today, with the use API, data can be read in render by passing a Promise to use:
```
import { use, Suspense } from "react";function Message({ messagePromise }) {  const messageContent = use(messagePromise);  return <p>Here is the message: {messageContent}</p>;}export function MessageContainer({ messagePromise }) {  return (    <Suspense fallback={<p>⌛Downloading message...</p>}>      <Message messagePromise={messagePromise} />    </Suspense>  );}
```
我们仍然在规划细节，但是期望未来可以像这样写数据获取：
```
import { use } from 'react';function ShippingForm({ country }) {  const cities = use(fetch(`/api/cities?country=${country}`));  const [city, setCity] = useState(null);  const areas = city ? use(fetch(`/api/areas?city=${city}`)) : null;  // ...
```
比起在每个组件手动写原始 Effect，在应用中使用像上面 useData 这样的自定义 Hook，之后迁移到最终推荐方式你所需要的修改更少。但是旧的方式仍然可以有效工作，所以如果你喜欢写原始 Effect，可以继续这样做。
### 不止一个方法可以做到
假设你想要使用浏览器的 requestAnimationFrame API 从头开始 实现一个 fade-in 动画。你也许会从一个设置动画循环的 Effect 开始。在动画的每一帧中，你可以修改 ref 持有的 DOM 节点的 opacity 属性直到 1。你的代码一开始可能是这样：
```
App.jsApp.jsReloadClearForkimport { useState, useEffect, useRef } from 'react';

function Welcome() {
  const ref = useRef(null);

  useEffect(() => {
    const duration = 1000;
    const node = ref.current;

    let startTime = performance.now();
    let frameId = null;

    function onFrame(now) {
      const timePassed = now - startTime;
      const progress = Math.min(timePassed / duration, 1);
      onProgress(progress);
      if (progress < 1) {
        // 我们还有更多的帧需要绘制
        frameId = requestAnimationFrame(onFrame);
      }
    }

    function onProgress(progress) {
      node.style.opacity = progress;
    }

    function start() {
      onProgress(0);
      startTime = performance.now();
      frameId = requestAnimationFrame(onFrame);
    }

    function stop() {
      cancelAnimationFrame(frameId);
      startTime = null;
      frameId = null;
    }

    start();
    return () => stop();
  }, []);

  return (
    <h1 className="welcome" ref={ref}>
      Welcome
    </h1>
  );
}

export default function App() {
  const [show, setShow] = useState(false);
  return (
    <>
      <button onClick={() => setShow(!show)}>
        {show ? 'Remove' : 'Show'}
      </button>
      <hr />
      {show && <Welcome />}
    </>
  );
}
```
显示更多
为了让组件更具有可读性，你可能要将逻辑提取到自定义 Hook useFadeIn：
```
App.jsuseFadeIn.jsApp.jsReloadClearForkimport { useState, useEffect, useRef } from 'react';
import { useFadeIn } from './useFadeIn.js';

function Welcome() {
  const ref = useRef(null);

  useFadeIn(ref, 1000);

  return (
    <h1 className="welcome" ref={ref}>
      Welcome
    </h1>
  );
}

export default function App() {
  const [show, setShow] = useState(false);
  return (
    <>
      <button onClick={() => setShow(!show)}>
        {show ? 'Remove' : 'Show'}
      </button>
      <hr />
      {show && <Welcome />}
    </>
  );
}
```
显示更多
你可以让 useFadeIn 和原来保持一致，但是也可以进一步重构。例如你可以把设置动画循环的逻辑从 useFadeIn 提取到自定义 Hook useAnimationLoop：
```
App.jsuseFadeIn.jsuseFadeIn.jsReloadClearForkimport { useState, useEffect } from 'react';
import { useEffectEvent } from 'react';

export function useFadeIn(ref, duration) {
  const [isRunning, setIsRunning] = useState(true);

  useAnimationLoop(isRunning, (timePassed) => {
    const progress = Math.min(timePassed / duration, 1);
    ref.current.style.opacity = progress;
    if (progress === 1) {
      setIsRunning(false);
    }
  });
}

function useAnimationLoop(isRunning, drawFrame) {
  const onFrame = useEffectEvent(drawFrame);

  useEffect(() => {
    if (!isRunning) {
      return;
    }

    const startTime = performance.now();
    let frameId = null;

    function tick(now) {
      const timePassed = now - startTime;
      onFrame(timePassed);
      frameId = requestAnimationFrame(tick);
    }

    tick();
    return () => cancelAnimationFrame(frameId);
  }, [isRunning]);
}
```
显示更多
但是 没有必要 这样做。和常规函数一样，最终是由你决定在哪里划分代码不同部分之间的边界。你也可以采取不一样的方法。把大部分必要的逻辑移入一个 JavaScript 类，而不是把逻辑保留在 Effect 中：
```
App.jsuseFadeIn.jsanimation.jsuseFadeIn.jsReloadClearForkimport { useState, useEffect } from 'react';
import { FadeInAnimation } from './animation.js';

export function useFadeIn(ref, duration) {
  useEffect(() => {
    const animation = new FadeInAnimation(ref.current);
    animation.start(duration);
    return () => {
      animation.stop();
    };
  }, [ref, duration]);
}
```
Effect 可以连接 React 和外部系统。Effect 之间的配合越多（例如链接多个动画），像上面的 sandbox 一样 完整地 从 Effect 和 Hook 中提取逻辑就越有意义。然后你提取的代码 变成 “外部系统”。这会让你的 Effect 保持简洁，因为他们只需要向已经被你移动到 React 外部的系统发送消息。
上面这个示例假设需要使用 JavaScript 写 fade-in 逻辑。但使用纯 CSS 动画 实现这个特定的 fade-in 动画会更加简单和高效：
```
App.jswelcome.csswelcome.cssReloadClearFork.welcome {
  color: white;
  padding: 50px;
  text-align: center;
  font-size: 50px;
  background-image: radial-gradient(circle, rgba(63,94,251,1) 0%, rgba(252,70,107,1) 100%);

  animation: fadeIn 1000ms;
}

@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
```
某些时候你甚至不需要 Hook！
## 摘要
- 自定义 Hook 让你可以在组件间共享逻辑。
- 自定义 Hook 命名必须以 use 开头，后面跟一个大写字母。
- 自定义 Hook 共享的只是状态逻辑，不是状态本身。
- 你可以将响应值从一个 Hook 传到另一个，并且他们会保持最新。
- 每次组件重新渲染时，所有的 Hook 会重新运行。
- 自定义 Hook 的代码应该和组件代码一样保持纯粹。
- 把自定义 Hook 收到的事件处理函数包裹到 Effect Event。
- 不要创建像 useMount 这样的自定义 Hook。保持目标具体化。
- 如何以及在哪里选择代码边界取决于你。
## 尝试一些挑战
1. 提取 useCounter Hook 2. 让计时器的 delay 变为可配置项 3. 从 useCounter 中提取 useInterval 4. 修复计时器重置 5. 实现交错运动
#### 第 1 个挑战 共 5 个挑战: 提取 useCounter Hook
这个组件使用了一个 state 变量和一个 Effect 来展示每秒递增的一个数字。把这个逻辑提取到一个 useCounter 的自定义 Hook 中。你的目标是让 Counter 组件的实现看上去和这个一样：
```
export default function Counter() {  const count = useCounter();  return <h1>Seconds passed: {count}</h1>;}
```
你需要在 useCounter.js 中编写你的自定义 Hook，并且把它引入到 App.js 文件。
```
App.jsuseCounter.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    const id = setInterval(() => {
      setCount(c => c + 1);
    }, 1000);
    return () => clearInterval(id);
  }, []);
  return <h1>Seconds passed: {count}</h1>;
}
```
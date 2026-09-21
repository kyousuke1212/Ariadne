学习 React脱围机制 Copy pageCopy
# 将事件从 Effect 中分开
事件处理函数只有在你再次执行同样的交互时才会重新运行。Effect 和事件处理函数不一样，它只有在读取的 props 或 state 值和上一次渲染不一样时才会重新同步。有时你需要这两种行为的混合体：即一个 Effect 只在响应某些值时重新运行，但是在其他值变化时不重新运行。本章将会教你怎么实现这一点。
### 你将会学习到
- 怎么在事件处理函数和 Effect 之间做选择
- 为什么 Effect 是响应式的，而事件处理函数不是
- 当你想要 Effect 的部分代码变成非响应式时要做些什么
- Effect Event 是什么，以及怎么从 Effect 中提取
- 怎么使用 Effect Event 读取最新的 props 和 state
## 在事件处理函数和 Effect 中做选择
首先让我们回顾一下事件处理函数和 Effect 的区别。
假设你正在实现一个聊天室组件，需求如下：
- 组件应该自动连接选中的聊天室。
- 每当你点击“Send”按钮，组件应该在当前聊天界面发送一条消息。
假设你已经实现了这部分代码，但是还没有确定应该放在哪里。你是应该用事件处理函数还是 Effect 呢？每当你需要回答这个问题时，请考虑一下 为什么代码需要运行。
### 事件处理函数只在响应特定的交互操作时运行
从用户角度出发，发送消息是 因为 他点击了特定的“Send”按钮。如果在任意时间或者因为其他原因发送消息，用户会觉得非常混乱。这就是为什么发送消息应该使用事件处理函数。事件处理函数是让你处理特定的交互操作的：
```
function ChatRoom({ roomId }) {  const [message, setMessage] = useState('');  // ...  function handleSendClick() {    sendMessage(message);  }  // ...  return (    <>      <input value={message} onChange={e => setMessage(e.target.value)} />      <button onClick={handleSendClick}>Send</button>    </>  );}
```
借助事件处理函数，你可以确保 sendMessage(message) 只 在用户点击按钮的时候运行。
### 每当需要同步，Effect 就会运行
回想一下，你还需要让组件和聊天室保持连接。代码放哪里呢？
运行这个代码的 原因 不是特定的交互操作。用户为什么或怎么导航到聊天室屏幕的都不重要。既然用户正在看它并且能够和它交互，组件就要和选中的聊天服务器保持连接。即使聊天室组件显示的是应用的初始屏幕，用户根本还没有执行任何交互，仍然应该需要保持连接。这就是这里用 Effect 的原因：
```
function ChatRoom({ roomId }) {  // ...  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => {      connection.disconnect();    };  }, [roomId]);  // ...}
```
无论 用户是否执行指定交互操作，这段代码都可以保证当前选中的聊天室服务器一直有一个活跃连接。用户是否只启动了应用，或选中了不同的聊天室，又或者导航到另一个屏幕后返回，Effect 都可以确保组件和当前选中的聊天室保持同步，并在必要时 重新连接。
```
App.jschat.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection, sendMessage } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);

  function handleSendClick() {
    sendMessage(message);
  }

  return (
    <>
      <h1>Welcome to the {roomId} room!</h1>
      <input value={message} onChange={e => setMessage(e.target.value)} />
      <button onClick={handleSendClick}>Send</button>
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
显示更多
## 响应式值和响应式逻辑
直观上，你可以说事件处理函数总是“手动”触发的，例如点击按钮。另一方面， Effect 是自动触发：每当需要保持同步的时候他们就会开始运行和重新运行。
有一个更精确的方式来考虑这个问题。
组件内部声明的 state 和 props 变量被称为  响应式值。本示例中的 serverUrl 不是响应式值，但 roomId 和 message 是。他们参与组件的渲染数据流：
```
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) {  const [message, setMessage] = useState('');  // ...}
```
像这样的响应式值可以因为重新渲染而变化。例如用户可能会编辑 message 或者在下拉菜单中选中不同的 roomId。事件处理函数和 Effect 对于变化的响应是不一样的：
- 事件处理函数内部的逻辑是非响应式的。除非用户又执行了同样的操作（例如点击），否则这段逻辑不会再运行。事件处理函数可以在“不响应”他们变化的情况下读取响应式值。
- Effect 内部的逻辑是响应式的。如果 Effect 要读取响应式值，你必须将它指定为依赖项。如果接下来的重新渲染引起那个值变化，React 就会使用新值重新运行 Effect 内的逻辑。
让我们重新看看前面的示例来说明差异。
### 事件处理函数内部的逻辑是非响应式的
看这行代码。这个逻辑是响应式的吗？
```
    // ...    sendMessage(message);    // ...
```
从用户角度出发，message 的变化并不意味着他们想要发送消息。它只能表明用户正在输入。换句话说，发送消息的逻辑不应该是响应式的。它不应该仅仅因为 响应式值 变化而再次运行。这就是应该把它归入事件处理函数的原因：
```
  function handleSendClick() {    sendMessage(message);  }
```
事件处理函数是非响应式的，所以 sendMessage(message) 只会在用户点击“Send”按钮的时候运行。
### Effect 内部的逻辑是响应式的
现在让我们返回这几行代码：
```
    // ...    const connection = createConnection(serverUrl, roomId);    connection.connect();    // ...
```
从用户角度出发，roomId 的变化意味着他们的确想要连接到不同的房间。换句话说，连接房间的逻辑应该是响应式的。你 需要 这几行代码和响应式值“保持同步”，并在值不同时再次运行。这就是它被归入 Effect 的原因：
```
  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => {      connection.disconnect()    };  }, [roomId]);
```
Effect 是响应式的，所以 createConnection(serverUrl, roomId) 和 connection.connect() 会因为 roomId 每个不同的值而运行。Effect 让聊天室连接和当前选中的房间保持了同步。
## 从 Effect 中提取非响应式逻辑
当你想混合使用响应式逻辑和非响应式逻辑时，事情变得更加棘手。
例如，假设你想在用户连接到聊天室时展示一个通知。并且通过从 props 中读取当前 theme（dark 或者 light）来展示对应颜色的通知：
```
function ChatRoom({ roomId, theme }) {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.on('connected', () => {      showNotification('Connected!', theme);    });    connection.connect();    // ...
```
但是 theme 是一个响应式值（它会由于重新渲染而变化），并且 Effect 读取的每一个响应式值都必须在其依赖项中声明。现在你必须把 theme 作为 Effect 的依赖项之一：
```
function ChatRoom({ roomId, theme }) {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.on('connected', () => {      showNotification('Connected!', theme);    });    connection.connect();    return () => {      connection.disconnect()    };  }, [roomId, theme]); // ✅ 声明所有依赖项  // ...
```
用这个例子试一下，看你能否看出这个用户体验问题：
```
App.jschat.jsnotifications.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection, sendMessage } from './chat.js';
import { showNotification } from './notifications.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId, theme }) {
  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.on('connected', () => {
      showNotification('Connected!', theme);
    });
    connection.connect();
    return () => connection.disconnect();
  }, [roomId, theme]);

  return <h1>Welcome to the {roomId} room!</h1>
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  const [isDark, setIsDark] = useState(false);
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
      <label>
        <input
          type="checkbox"
          checked={isDark}
          onChange={e => setIsDark(e.target.checked)}
        />
        Use dark theme
      </label>
      <hr />
      <ChatRoom
        roomId={roomId}
        theme={isDark ? 'dark' : 'light'}
      />
    </>
  );
}
```
显示更多
当 roomId 变化时，聊天会和预期一样重新连接。但是由于 theme 也是一个依赖项，所以每次你在 dark 和 light 主题间切换时，聊天 也会 重连。这不是很好！
换言之，即使它在 Effect 内部（这是响应式的），你也不想让这行代码变成响应式：
```
      // ...      showNotification('Connected!', theme);      // ...
```
你需要一个将这个非响应式逻辑和周围响应式 Effect 隔离开来的方法。
### 声明一个 Effect Event
使用 useEffectEvent 这个特殊的 Hook 从 Effect 中提取非响应式逻辑：
```
import { useEffect, useEffectEvent } from 'react';function ChatRoom({ roomId, theme }) {  const onConnected = useEffectEvent(() => {    showNotification('Connected!', theme);  });  // ...
```
这里的 onConnected 被称为 Effect Event。它是 Effect 逻辑的一部分，但是其行为更像事件处理函数。它内部的逻辑不是响应式的，而且能一直“看见”最新的 props 和 state。
现在你可以在 Effect 内部调用 onConnected Effect Event：
```
function ChatRoom({ roomId, theme }) {  const onConnected = useEffectEvent(() => {    showNotification('Connected!', theme);  });  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.on('connected', () => {      onConnected();    });    connection.connect();    return () => connection.disconnect();  }, [roomId]); // ✅ 声明所有依赖项  // ...
```
这个方法解决了问题。注意你必须从 Effect 依赖项中 移除 theme，因为 Effect 中没有使用它。你也不需要 添加 onConnected，因为 Effect Event 是非响应式的并且必须从依赖项中删除。
验证新表现是否和你预期的一样：
```
App.jschat.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { useEffectEvent } from 'react';
import { createConnection, sendMessage } from './chat.js';
import { showNotification } from './notifications.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId, theme }) {
  const onConnected = useEffectEvent(() => {
    showNotification('Connected!', theme);
  });

  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.on('connected', () => {
      onConnected();
    });
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);

  return <h1>Welcome to the {roomId} room!</h1>
}

export default function App() {
  const [roomId, setRoomId] = useState('general');
  const [isDark, setIsDark] = useState(false);
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
      <label>
        <input
          type="checkbox"
          checked={isDark}
          onChange={e => setIsDark(e.target.checked)}
        />
        Use dark theme
      </label>
      <hr />
      <ChatRoom
        roomId={roomId}
        theme={isDark ? 'dark' : 'light'}
      />
    </>
  );
}
```
显示更多
你可以将 Effect Event 看成和事件处理函数相似的东西。主要区别是事件处理函数只在响应用户交互的时候运行，而 Effect Event 是你在 Effect 中触发的。Effect Event 让你在 Effect 响应性和不应是响应式的代码间“打破链条”。
### 使用 Effect Event 读取最新的 props 和 state
Effect Event 可以修复之前许多你可能试图抑制依赖项检查工具的地方。
例如，假设你有一个记录页面访问的 Effect：
```
function Page() {  useEffect(() => {    logVisit();  }, []);  // ...}
```
稍后向你的站点添加多个路由。现在 Page 组件接收包含当前路径的 url props。你想把 url 作为 logVisit 调用的一部分进行传递，但是依赖项检查工具会提示：
```
function Page({ url }) {  useEffect(() => {    logVisit(url);  }, []); // 🔴 React Hook useEffect 缺少一个依赖项: 'url'  // ...}
```
想想你想要代码做什么。你 需要 为不同的 URL 记录单独的访问，因为每个 URL 代表不同的页面。换言之，logVisit 调用对于 url 应该 是响应式的。这就是为什么在这种情况下， 遵循依赖项检查工具并添加 url 作为一个依赖项很有意义：
```
function Page({ url }) {  useEffect(() => {    logVisit(url);  }, [url]); // ✅ 声明所有依赖项  // ...}
```
现在假设你想在每次页面访问中包含购物车中的商品数量：
```
function Page({ url }) {  const { items } = useContext(ShoppingCartContext);  const numberOfItems = items.length;  useEffect(() => {    logVisit(url, numberOfItems);  }, [url]); // 🔴 React Hook useEffect 缺少依赖项: ‘numberOfItems’  // ...}
```
你在 Effect 内部使用了 numberOfItems，所以代码检查工具会让你把它加到依赖项中。但是，你 不 想要 logVisit 调用响应 numberOfItems。如果用户把某样东西放入购物车， numberOfItems 会变化，这 并不意味着 用户再次访问了这个页面。换句话说，在某种意义上，访问页面 是一个“事件”。它发生在某个准确的时刻。
将代码分割为两部分：
```
function Page({ url }) {  const { items } = useContext(ShoppingCartContext);  const numberOfItems = items.length;  const onVisit = useEffectEvent(visitedUrl => {    logVisit(visitedUrl, numberOfItems);  });  useEffect(() => {    onVisit(url);  }, [url]); // ✅ 声明所有依赖项  // ...}
```
这里的 onVisit 是一个 Effect Event。里面的代码不是响应式的。这就是为什么你可以使用 numberOfItems（或者任意响应式值！）而不用担心引起周围代码因为变化而重新执行。
另一方面，Effect 本身仍然是响应式的。其内部的代码使用了 url props，所以每次因为不同的 url 重新渲染后 Effect 都会重新运行。这会依次调用 onVisit 这个 Effect Event。
结果是你会因为 url 的变化去调用 logVisit，并且读取的一直都是最新的 numberOfItems。但是如果 numberOfItems 自己变化，不会引起任何代码的重新运行。
### 注意
你可能想知道是否可以无参数调用 onVisit() 并且读取内部的 url：
```
  const onVisit = useEffectEvent(() => {    logVisit(url, numberOfItems);  });  useEffect(() => {    onVisit();  }, [url]);
```
这可以起作用，但是更好的方法是将这个 url 显式传递给Effect Event。通过将 url 作为参数传给 Effect Event，你可以说从用户角度来看使用不同的 url 访问页面构成了一个独立的“事件”。visitedUrl 是发生的“事件”的一部分：
```
  const onVisit = useEffectEvent(visitedUrl => {    logVisit(visitedUrl, numberOfItems);  });  useEffect(() => {    onVisit(url);  }, [url]);
```
由于 Effect 明确“要求” visitedUrl，所以现在你不会不小心地从 Effect 的依赖项中移除 url。如果你移除了 url 依赖项（导致不同的页面访问被认为是一个），代码检查工具会向你提出警告。如果你想要 onVisit 能对 url 的变化做出响应，不要读取内部的 url（这里不是响应式的），而是应该将它 从 Effect 中传入。
如果 Effect 内部有一些异步逻辑，这就变得非常重要了：
```
  const onVisit = useEffectEvent(visitedUrl => {    logVisit(visitedUrl, numberOfItems);  });  useEffect(() => {    setTimeout(() => {      onVisit(url);    }, 5000); // 延迟记录访问  }, [url]);
```
在这里，onVisit 内的 url 对应 最新的 url（可能已经变化了），但是 visitedUrl 对应的是最开始引起这个 Effect（并且是本次 onVisit 调用）运行的 url 。
深入探讨
#### 抑制依赖项检查是可行的吗？
显示更多
在已经存在的代码库中，你可能有时会看见像这样的检查规则抑制：
```
function Page({ url }) {  const { items } = useContext(ShoppingCartContext);  const numberOfItems = items.length;  useEffect(() => {    logVisit(url, numberOfItems);    // 🔴 避免像这样抑制代码检查:    // eslint-disable-next-line react-hooks/exhaustive-deps  }, [url]);  // ...}
```
我们建议 永远不要抑制代码检查工具。
抑制规则的第一个缺点是当 Effect 需要对一个已经在代码中出现过的新响应式依赖项做出“响应”时，React 不会再发出警告。在稍早之前的示例中，你将 url 添加为依赖项，是因为 React 提醒你去做这件事。如果禁用代码检查，你未来将不会再收到任何关于 Effect 修改的提醒。这引起了 bug。
这个示例展示了一个由抑制代码检查引起的奇怪 bug。在这个示例中，handleMove 应该读取当前的 state 变量 canMove 的值来决定这个点是否应该跟随光标。但是 handleMove 中的 canMove 一直是 true。
你能看出是为什么吗？
```
App.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';

export default function App() {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [canMove, setCanMove] = useState(true);

  function handleMove(e) {
    if (canMove) {
      setPosition({ x: e.clientX, y: e.clientY });
    }
  }

  useEffect(() => {
    window.addEventListener('pointermove', handleMove);
    return () => window.removeEventListener('pointermove', handleMove);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <label>
        <input type="checkbox"
          checked={canMove}
          onChange={e => setCanMove(e.target.checked)}
        />
        The dot is allowed to move
      </label>
      <hr />
      <div style={{
        position: 'absolute',
        backgroundColor: 'pink',
        borderRadius: '50%',
        opacity: 0.6,
        transform: `translate(${position.x}px, ${position.y}px)`,
        pointerEvents: 'none',
        left: -20,
        top: -20,
        width: 40,
        height: 40,
      }} />
    </>
  );
}
```
显示更多
这段代码的问题在于抑制依赖项检查。如果移除，你可以看到 Effect 应该依赖于 handleMove 函数。这非常有意义：handleMove 是在组件内声明的，是响应式值。而每个响应式值都必须被指定为依赖项，否则它可能会随着时间而过时！
原代码的作者对 React “撒谎”说 Effect 不依赖于任何响应式值（[]）。这就是为什么 canMove（以及 handleMove）变化后 React 没有重新同步。因为 React 没有重新同步 Effect，所以作为监听器附加的 handleMove 还是初次渲染期间创建的 handleMove 函数。初次渲染期间，canMove 的值是 true，这就是为什么来自初次渲染的 handleMove 永远只能看到这个值。
如果你从来没有抑制代码检查，就永远不会遇见过期值的问题。
有了 useEffectEvent，就不需要对代码检查工具“说谎”，并且代码也能和你预期的一样工作：
```
App.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { useEffectEvent } from 'react';

export default function App() {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [canMove, setCanMove] = useState(true);

  const onMove = useEffectEvent(e => {
    if (canMove) {
      setPosition({ x: e.clientX, y: e.clientY });
    }
  });

  useEffect(() => {
    window.addEventListener('pointermove', onMove);
    return () => window.removeEventListener('pointermove', onMove);
  }, []);

  return (
    <>
      <label>
        <input type="checkbox"
          checked={canMove}
          onChange={e => setCanMove(e.target.checked)}
        />
        The dot is allowed to move
      </label>
      <hr />
      <div style={{
        position: 'absolute',
        backgroundColor: 'pink',
        borderRadius: '50%',
        opacity: 0.6,
        transform: `translate(${position.x}px, ${position.y}px)`,
        pointerEvents: 'none',
        left: -20,
        top: -20,
        width: 40,
        height: 40,
      }} />
    </>
  );
}
```
显示更多
这不意味着 useEffectEvent 总是 正确的解决方案。你只能把它用在你不需要变成响应式的代码上。上面的 sandbox 中，你不需要 Effect 的代码响应 canMove。这就是提取 Effect Event 很有意义的原因。
阅读 移除 Effect 依赖项 寻找抑制代码检查的其他正确的替代方式。
### Effect Event 的局限性
Effect Event 的局限性在于你如何使用他们：
- 只在 Effect 内部调用他们。
- 永远不要把他们传给其他的组件或者 Hook。
例如不要像这样声明和传递 Effect Event：
```
function Timer() {  const [count, setCount] = useState(0);  const onTick = useEffectEvent(() => {    setCount(count + 1);  });  useTimer(onTick, 1000); // 🔴 避免: 传递 Effect Event  return <h1>{count}</h1>}function useTimer(callback, delay) {  useEffect(() => {    const id = setInterval(() => {      callback();    }, delay);    return () => {      clearInterval(id);    };  }, [delay, callback]); // 需要在依赖项中指定 “callback”}
```
取而代之的是，永远直接在使用他们的 Effect 旁边声明 Effect Event：
```
function Timer() {  const [count, setCount] = useState(0);  useTimer(() => {    setCount(count + 1);  }, 1000);  return <h1>{count}</h1>}function useTimer(callback, delay) {  const onTick = useEffectEvent(() => {    callback();  });  useEffect(() => {    const id = setInterval(() => {      onTick(); // ✅ 好: 只在 Effect 内部局部调用    }, delay);    return () => {      clearInterval(id);    };  }, [delay]); // 不需要指定 “onTick” (Effect Event) 作为依赖项}
```
Effect Event 是 Effect 代码的非响应式“片段”。他们应该在使用他们的 Effect 的旁边。
## 摘要
- 事件处理函数在响应特定交互时运行。
- Effect 在需要同步的时候运行。
- 事件处理函数内部的逻辑是非响应式的。
- Effect 内部的逻辑是响应式的。
- 你可以将非响应式逻辑从 Effect 移到 Effect Event 中。
- 只在 Effect 内部调用 Effect Event。
- 不要将 Effect Event 传给其他组件或者 Hook。
## 尝试一些挑战
1. 修复一个不更新的变量 2. 修复一个冻结的计数器 3. 修复不可调整的延迟 4. 修复延迟通知
#### 第 1 个挑战 共 4 个挑战: 修复一个不更新的变量
Timer 组件保存了一个 count 的 state 变量，这个变量每秒增加一次。每次增加的值存储在 increment state 变量中。你可以使用加减按钮控制 increment 变量。
但是无论你点击加号按钮多少次，计数器每秒都只增加 １。这段代码存在什么问题呢？为什么 Effect 内部的 increment 总是等于 1 呢？找出错误并修复它。
```
App.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';

export default function Timer() {
  const [count, setCount] = useState(0);
  const [increment, setIncrement] = useState(1);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(c => c + increment);
    }, 1000);
    return () => {
      clearInterval(id);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <h1>
        Counter: {count}
        <button onClick={() => setCount(0)}>Reset</button>
      </h1>
      <hr />
      <p>
        Every second, increment by:
        <button disabled={increment === 0} onClick={() => {
          setIncrement(i => i - 1);
        }}>–</button>
        <b>{increment}</b>
        <button onClick={() => {
          setIncrement(i => i + 1);
        }}>+</button>
      </p>
    </>
  );
}
```
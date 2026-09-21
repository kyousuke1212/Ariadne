学习 React脱围机制 Copy pageCopy
# 移除 Effect 依赖
当编写 Effect 时，linter 会验证是否已经将 Effect 读取的每一个响应式值（如 props 和 state）包含在 Effect 的依赖中。这可以确保 Effect 与组件的 props 和 state 保持同步。不必要的依赖可能会导致 Effect 运行过于频繁，甚至产生无限循环。请按照本指南审查并移除 Effect 中不必要的依赖。
### 你将会学习到
- 修复无限的 Effect 依赖性循环
- 当你想移除依赖时，该怎么做
- 从 Effect 中读取值而不对它作出“反应”
- 为什么以及如何避免对象和函数的依赖？
- 为什么抑制依赖代码检查器的检查是危险的，以及应该如何做？
## 依赖应该和代码保持一致
当你编写 Effect 时，无论这个 Effect 要做什么，你首先要明确其 生命周期：
```
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => connection.disconnect();  	// ...}
```
如果你设置 Effect 的依赖是空数组（[]），那么 linter 将会建议合适的依赖：
```
App.jschat.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => connection.disconnect();
  }, []); // <-- 修复这里的依赖！
  return <h1>欢迎来到 {roomId} 房间！</h1>;
}

export default function App() {
  const [roomId, setRoomId] = useState('所有');
  return (
    <>
      <label>
        选择聊天室：
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="所有">所有</option>
          <option value="旅游">旅游</option>
          <option value="音乐">音乐</option>
        </select>
      </label>
      <hr />
      <ChatRoom roomId={roomId} />
    </>
  );
}
```
显示更多
按照 linter 的建议，把它们填进去：
```
function ChatRoom({ roomId }) {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => connection.disconnect();  }, [roomId]); // ✅ 所有依赖已声明  // ...}
```
Effect 会对响应式值作出“反应”。 因为这里的 roomId 是一个响应式值（它可能随重新渲染而改变），所以 linter 会验证你是否将它指定为依赖。如果 roomId 变成不同的值，React 将重新运行 Effect。这可以确保聊天界面与所选房间保持一致，并把变化“反馈”给下拉菜单：
```
App.jschat.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]);
  return <h1>欢迎来到 {roomId} 房间！</h1>;
}

export default function App() {
  const [roomId, setRoomId] = useState('所有');
  return (
    <>
      <label>
        选择聊天室：
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="所有">所有</option>
          <option value="旅游">旅游</option>
          <option value="音乐">音乐</option>
        </select>
      </label>
      <hr />
      <ChatRoom roomId={roomId} />
    </>
  );
}
```
显示更多
### 当要移除一个依赖时，请证明它不是一个依赖
注意，你不能“选择” Effect 的依赖。每个被 Effect 所使用的响应式值，必须在依赖中声明。依赖是由 Effect 的代码决定的：
```
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) { // 这是一个响应式值  useEffect(() => {    const connection = createConnection(serverUrl, roomId); // Effect 在这里读取响应式值    connection.connect();    return () => connection.disconnect();  }, [roomId]); // ✅ 所以你必须在依赖中声明 Effect 使用的响应式值  // ...}
```
响应式值 包括 props 以及所有你直接在组件中声明的变量和函数。由于 roomId 是响应式值，你不能把它从依赖中移除。linter 不允许这样做：
```
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => connection.disconnect();  }, []); // 🔴 React Hook useEffect 缺失依赖: 'roomId'  // ...}
```
linter 是对的！ 由于 roomId 可能会随时间变化，这会在代码中引入错误。
移除一个依赖，你需要向 linter 证明其不需要这个依赖。例如，你可以将 roomId 移出组件，以证明它不是响应的，也不会在重新渲染时改变：
```
const serverUrl = 'https://localhost:1234';const roomId = '音乐'; // 不再是响应式值function ChatRoom() {  useEffect(() => {    const connection = createConnection(serverUrl, roomId);    connection.connect();    return () => connection.disconnect();  }, []); // ✅ 所有依赖已声明  // ...}
```
现在 roomId 不是响应式值（并且不会在重新渲染时改变），因此它不需要作为依赖项：
```
App.jschat.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';
const roomId = '音乐';

export default function ChatRoom() {
  useEffect(() => {
    const connection = createConnection(serverUrl, roomId);
    connection.connect();
    return () => connection.disconnect();
  }, []);
  return <h1>欢迎来到 {roomId} 房间！</h1>;
}
```
这就是为什么你现在可以指定 空（[]）依赖。Effect 真的不 依赖任何响应式值了，也 真的不 需要在组件的 props 或 state 改变时重新运行。
### 要改变依赖，请改变代码
你可能已经注意到工作流程中有一个模式：
- 首先，你 改变 Effect 的代码 或响应式值的声明方式。
- 然后，你采纳 linter 的建议，调整依赖，以 匹配你所改变的代码。
- 如果你对依赖不满意，你可以 回到第一步（并再次修改代码）。
最后一部分很重要。如果你想改变依赖，首先要改变所涉及到的代码。你可以把依赖看作是 Effect 的代码所依赖的所有响应式值的列表。你不要 选择 把什么放在这个列表上。该列表 描述了 代码。要改变依赖，请改变代码。
这可能感觉就像解方程一样。你有一个目标（例如，移除一个依赖），你需要“找到”与该目标相匹配的代码。不是每个人都觉得解方程很有趣，写 Effect 也是如此！幸运的是，下面有一些常见的解决方案你可以去尝试。
### 陷阱
如果你有一个已经存在的代码库，你可能会有一些像这样抑制 linter 的代码：
```
useEffect(() => {  // ...  // 🔴 避免像这样抑制 linter 的警告或错误提示：  // eslint-ignore-next-line react-hooks/exhaustive-deps}, []);
```
当依赖与代码不匹配时，极有可能引入 bug。通过抑制 linter，你是在 Effect 所依赖的值上对 React “撒谎”。
你可以使用如下技术。
深入探讨
#### 为什么抑制 linter 对依赖的检查如此危险？
显示更多
抑制 linter 会导致非常不直观的 bug，这将很难发现和修复。这里有一个例子：
```
App.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';

export default function Timer() {
  const [count, setCount] = useState(0);
  const [increment, setIncrement] = useState(1);

  function onTick() {
	setCount(count + increment);
  }

  useEffect(() => {
    const id = setInterval(onTick, 1000);
    return () => clearInterval(id);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <h1>
        计数器：{count}
        <button onClick={() => setCount(0)}>重置</button>
      </h1>
      <hr />
      <p>
        每秒递增：
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
显示更多
比方说，你想“只在 mount 时”运行 Effect。你已经知道可以通过设置 空（[]）依赖 来达到这种效果，所以你决定忽略 linter 的检查，强行指定 [] 为依赖。
上面的计数器例子，本应该每秒递增，递增量可以通过两个按钮来控制。然而，由于你对 React “撒谎”，说这个 Effect 不依赖于任何东西，React 便一直使用初次渲染时的 onTick 函数。在后续渲染中， count 总是 0 ，increment 总是 1。为什么？因为定时器每秒调用 onTick 函数，实际运行的是 setCount(0 + 1)[1]，所以你总是看到 1。像这样的错误，当它们分散在多个组件中时，就更难解决了。
这里有一个比忽略 linter 更好的解决方案! 那便是将 onTick 添加到依赖中。(为了确保 interval 只设置一次，使 onTick 成为 Effect Event。)
我们建议将依赖性 lint 错误作为一个编译错误来处理。如果你不抑制它，你将永远不会遇到像上面这样的错误。本页面的剩下部分将介绍这个和其他情况的替代方案。
## 移除非必需的依赖
每当你调整 Effect 的依赖以适配代码时，请注意一下当前的依赖。当这些依赖发生变化时，让 Effect 重新运行是否有意义？有时，答案是“不”：
- 你可能想在不同的条件下重新执行 Effect 的 不同部分。
- 你可能想只读取某个依赖的 最新值，而不是对其变化做出“反应”。
- 依赖可能会因为它的类型是对象或函数而 无意间 改变太频繁。
为了找到正确的解决方案，你需要回答关于 Effect 的几个问题。让我们来看看这些问题。
### 这段代码应该移到事件处理程序中吗？
你应该考虑的第一件事是，这段代码是否应该成为 Effect。
想象一个表单，在提交时你将 submitted 状态变量设置为 true，并在 submitted 为 true 时，需要发送 POST 请求并显示通知。你把这个逻辑放在 Effect 内，并根据 submitted 为 true “反应”。
```
function Form() {  const [submitted, setSubmitted] = useState(false);  useEffect(() => {    if (submitted) {      // 🔴 避免: Effect 中有特定事件的逻辑      post('/api/register');      showNotification('Successfully registered!');    }  }, [submitted]);  function handleSubmit() {    setSubmitted(true);  }  // ...}
```
后来，你想通过读取当前的主题值来调整通知信息的样式。因为 theme 是在组件中声明的，所以它是响应式值，你决定把它作为依赖加入：
```
function Form() {  const [submitted, setSubmitted] = useState(false);  const theme = useContext(ThemeContext);  useEffect(() => {    if (submitted) {      // 🔴 避免: Effect 中有特定事件的逻辑      post('/api/register');      showNotification('Successfully registered!', theme);    }  }, [submitted, theme]); // ✅ 所有依赖已声明  function handleSubmit() {    setSubmitted(true);  }  // ...}
```
如果这么做，你将引入一个错误。想象一下，你先提交表单，然后切换暗亮主题。当 theme 改变后，Effect 重新运行，这将导致显示两次相同的通知！
首先，这里的问题是，代码不应该以 Effect 实现。你想发送这个 POST 请求，并在 提交表单时显示通知，这是一个特定的交互。特定的交互请将该逻辑直接放到相应的事件处理程序中：
```
function Form() {  const theme = useContext(ThemeContext);  function handleSubmit() {    // ✅ 好：从事件处理程序调用特定于事件的逻辑    post('/api/register');    showNotification('Successfully registered!', theme);  }  // ...}
```
现在，代码在事件处理程序中，它不是响应式的 —— 所以它只在用户提交表单时运行。阅读更多关于 在事件处理程序和 Effect 之间做出选择 和 如何删除不必要的 Effect。
### Effect 是否在做几件不相关的事情？
下一个应该问自己的问题是，Effect 是否在做几件不相关的事情。
如下例子，你正在实现运输表单，用户需要选择他们的城市和地区。你根据所选的“国家”从服务器上获取“城市”列表，然后在下拉菜单中显示：
```
function ShippingForm({ country }) {  const [cities, setCities] = useState(null);  const [city, setCity] = useState(null);  useEffect(() => {    let ignore = false;    fetch(`/api/cities?country=${country}`)      .then(response => response.json())      .then(json => {        if (!ignore) {          setCities(json);        }      });    return () => {      ignore = true;    };  }, [country]); // ✅ 所有依赖已声明  // ...
```
这是一个 在Effect中获取数据 的好例子：cities state 通过网络和 country props 进行“同步”。但你不能在事件处理程序中这样做，因为你需要在 ShippingForm 显示时和 country 发生变化时（不管是哪个交互导致的）立即获取。
现在我们假设你要为城市区域添加第二个选择框，它应该获取当前选择的 city 的 areas。你也许会在同一个 Effect 中添加第二个 fetch 调用来获取地区列表：
```
function ShippingForm({ country }) {  const [cities, setCities] = useState(null);  const [city, setCity] = useState(null);  const [areas, setAreas] = useState(null);  useEffect(() => {    let ignore = false;    fetch(`/api/cities?country=${country}`)      .then(response => response.json())      .then(json => {        if (!ignore) {          setCities(json);        }      });    // 🔴 避免: 单个 Effect 同步两个独立逻辑处理    if (city) {      fetch(`/api/areas?city=${city}`)        .then(response => response.json())        .then(json => {          if (!ignore) {            setAreas(json);          }        });    }    return () => {      ignore = true;    };  }, [country, city]); // ✅ 所有依赖已声明  // ...
```
然而，由于 Effect 现在使用 city state 变量，你不得不把 city 加入到依赖中。这又带来一个问题：当用户选择不同的城市时，Effect 将重新运行并调用 fetchCities(country)。这将导致不必要地多次获取城市列表。
这段代码的问题在于，你在同步两个不同的、不相关的东西：
- 你想要根据 country props 通过网络同步 city state
- 你想要根据 city 状态通过网络同步 areas state
将逻辑分到 2 个 Effect 中，每个 Effect 仅响应其需要同步响应的 props：
```
function ShippingForm({ country }) {  const [cities, setCities] = useState(null);  useEffect(() => {    let ignore = false;    fetch(`/api/cities?country=${country}`)      .then(response => response.json())      .then(json => {        if (!ignore) {          setCities(json);        }      });    return () => {      ignore = true;    };  }, [country]); // ✅ 所有依赖已声明  const [city, setCity] = useState(null);  const [areas, setAreas] = useState(null);  useEffect(() => {    if (city) {      let ignore = false;      fetch(`/api/areas?city=${city}`)        .then(response => response.json())        .then(json => {          if (!ignore) {            setAreas(json);          }        });      return () => {        ignore = true;      };    }  }, [city]); // ✅ 所有依赖已声明  // ...
```
现在，第一个 Effect 只在 country 改变时重新运行，而第二个 Effect 在 city 改变时重新运行。你已经按目的把它们分开了：两件不同的事情由两个独立的 Effect 来同步。两个独立的 Effect 有两个独立的依赖，所以它们不会在无意中相互触发。
最终完成的代码比最初的要长，但是拆分这些 Effect 是非常正确的。每个 Effect 应该代表一个独立的同步过程。在这个例子中，删除一个 Effect 并不会影响到另一个 Effect 的逻辑。这意味着他们 同步不同的事情，分开他们处理是一件好事。如果你担心重复代码的问题，你可以通过 提取相同逻辑到自定义 Hook 来提升代码质量
### 是否在读取一些状态来计算下一个状态？
每次有新的消息到达时，这个 Effect 会用新创建的数组更新 messages state：
```
function ChatRoom({ roomId }) {  const [messages, setMessages] = useState([]);  useEffect(() => {    const connection = createConnection();    connection.connect();    connection.on('message', (receivedMessage) => {      setMessages([...messages, receivedMessage]);    });    // ...
```
它使用 messages 变量来 创建一个新的数组：从所有现有的消息开始，并在最后添加新的消息。然而，由于 messages 是一个由 Effect 读取的响应式值，它必须是一个依赖：
```
function ChatRoom({ roomId }) {  const [messages, setMessages] = useState([]);  useEffect(() => {    const connection = createConnection();    connection.connect();    connection.on('message', (receivedMessage) => {      setMessages([...messages, receivedMessage]);    });    return () => connection.disconnect();  }, [roomId, messages]); // ✅ 所有依赖已声明  // ...
```
而让 messages 成为依赖会带来问题。
每当你收到一条消息，setMessages() 就会使该组件重新渲染一个新的 messages 数组，其中包括收到的消息。然而，由于该 Effect 现在依赖于 messages，这 也将 重新同步该 Effect。所以每条新消息都会使聊天重新连接。用户不会喜欢这样！
为了解决这个问题，不要在 Effect 里面读取 messages。相反，应该将一个 state 更新函数 传递给 setMessages：
```
function ChatRoom({ roomId }) {  const [messages, setMessages] = useState([]);  useEffect(() => {    const connection = createConnection();    connection.connect();    connection.on('message', (receivedMessage) => {      setMessages(msgs => [...msgs, receivedMessage]);    });    return () => connection.disconnect();  }, [roomId]); // ✅ 所有依赖已声明  // ...
```
注意 Effect 现在根本不读取 messages 变量。你只需要传递一个更新函数，比如 msgs => [...msgs, receivedMessage]。React 将更新程序函数放入队列 并将在下一次渲染期间向其提供 msgs 参数。这就是 Effect 本身不再需要依赖 messages 的原因。修复后，接收聊天消息将不再使聊天重新连接。
### 你想读取一个值而不对其变化做出“反应”吗？
假设你希望在用户收到新消息时播放声音，isMuted 为 true 除外：
```
function ChatRoom({ roomId }) {  const [messages, setMessages] = useState([]);  const [isMuted, setIsMuted] = useState(false);  useEffect(() => {    const connection = createConnection();    connection.connect();    connection.on('message', (receivedMessage) => {      setMessages(msgs => [...msgs, receivedMessage]);      if (!isMuted) {        playSound();      }    });    // ...
```
由于 Effect 现在在其代码中使用了 isMuted ，因此你必须将其添加到依赖中：
```
function ChatRoom({ roomId }) {  const [messages, setMessages] = useState([]);  const [isMuted, setIsMuted] = useState(false);  useEffect(() => {    const connection = createConnection();    connection.connect();    connection.on('message', (receivedMessage) => {      setMessages(msgs => [...msgs, receivedMessage]);      if (!isMuted) {        playSound();      }    });    return () => connection.disconnect();  }, [roomId, isMuted]); // ✅ 所有依赖已声明  // ...
```
问题是每次 isMuted 改变时（例如，当用户按下“静音”开关时），Effect 将重新同步，并重新连接到聊天。这不是理想的用户体验！（在此示例中，即使禁用 linter 也不起作用——如果你这样做，isMuted 将“保持”其旧值。）
要解决这个问题，需要将不应该响应式的逻辑从 Effect 中抽取出来。你不希望此 Effect 对 isMuted 中的更改做出“反应”。将这段非响应式逻辑移至 Effect Event 中：
```
import { useState, useEffect, useEffectEvent } from 'react';function ChatRoom({ roomId }) {  const [messages, setMessages] = useState([]);  const [isMuted, setIsMuted] = useState(false);  const onMessage = useEffectEvent(receivedMessage => {    setMessages(msgs => [...msgs, receivedMessage]);    if (!isMuted) {      playSound();    }  });  useEffect(() => {    const connection = createConnection();    connection.connect();    connection.on('message', (receivedMessage) => {      onMessage(receivedMessage);    });    return () => connection.disconnect();  }, [roomId]); // ✅ 所有依赖已声明  // ...
```
Effect Events 让你可以将 Effect 分成响应式部分（应该“反应”响应式值，如 roomId 及其变化）和非响应式部分（只读取它们的最新值，如 onMessage 读取 isMuted）。现在你在 Effect Event 中读取了 isMuted，它不需要添加到 Effect 依赖中。因此，当你打开或者关闭“静音”设置时，聊天不会重新连接。至此，解决原始问题！
#### 包装来自 props 的事件处理程序
当组件接收事件处理函数作为 props 时，你可能会遇到类似的问题：
```
function ChatRoom({ roomId, onReceiveMessage }) {  const [messages, setMessages] = useState([]);  useEffect(() => {    const connection = createConnection();    connection.connect();    connection.on('message', (receivedMessage) => {      onReceiveMessage(receivedMessage);    });    return () => connection.disconnect();  }, [roomId, onReceiveMessage]); // ✅ 所有依赖已声明  // ...
```
假设父组件在每次渲染时都传递了一个 不同的 onReceiveMessage 函数：
```
<ChatRoom  roomId={roomId}  onReceiveMessage={receivedMessage => {    // ...  }}/>
```
由于 onReceiveMessage 是依赖，它会导致 Effect 在每次父级重新渲染后重新同步。这将导致聊天重新连接。要解决此问题，请用 Effect Event 包裹之后再调用：
```
function ChatRoom({ roomId, onReceiveMessage }) {  const [messages, setMessages] = useState([]);  const onMessage = useEffectEvent(receivedMessage => {    onReceiveMessage(receivedMessage);  });  useEffect(() => {    const connection = createConnection();    connection.connect();    connection.on('message', (receivedMessage) => {      onMessage(receivedMessage);    });    return () => connection.disconnect();  }, [roomId]); // ✅ 所有依赖已声明  // ...
```
Effect Events 不是响应式的，因此你不需要将它们指定为依赖。因此，即使父组件传递的函数在每次重新渲染时都不同，聊天也将不再重新连接。
#### 分离响应式和非响应式代码
在此示例中，你希望在每次 roomId 更改时记录一次。你希望在每个日志中包含当前的 notificationCount，但你 不 希望通过更改 notificationCount 来触发日志事件。
解决方案还是将非响应式代码拆分，将其放到 Effect Event 内：
```
function Chat({ roomId, notificationCount }) {  const onVisit = useEffectEvent(visitedRoomId => {    logVisit(visitedRoomId, notificationCount);  });  useEffect(() => {    onVisit(roomId);  }, [roomId]); // ✅ 所有依赖已声明  // ...}
```
你希望逻辑对 roomId 做出响应，因此你在 Effect 中读取 roomId。但是，你不希望更改 notificationCount 来记录额外的日志输出，因此你可以在 Effect Event 中读取 notificationCount。了解使用 Effect Events 在 Effect 中读取最新 props 和 state 的更多信息。
### 一些响应式值是否无意中改变了？
有时，你 确实 希望 Effect 对某个值“做出反应”，但该值的变化比你希望的更频繁——并且可能不会从用户的角度反映任何实际变化。例如，假设你在组件中创建了 options 对象，然后从 Effect 内部读取该对象：
```
function ChatRoom({ roomId }) {  // ...  const options = {    serverUrl: serverUrl,    roomId: roomId  };  useEffect(() => {    const connection = createConnection(options);    connection.connect();    // ...
```
该对象在组件中声明，因此它是 响应式值。当你在 Effect 中读取这样的响应式值时，你将其声明为依赖。这可确保 Effect 对其更改做出“反应”：
```
  // ...  useEffect(() => {    const connection = createConnection(options);    connection.connect();    return () => connection.disconnect();  }, [options]); // ✅ 所有依赖已声明  // ...
```
将其声明为依赖很重要！例如，这可以确保如果 roomId 发生变化，Effect 将使用新的 options 重新连接到聊天。但是，上面的代码也有问题。要查看它，请尝试在下面的沙盒中输入内容，然后观察控制台中发生的情况：
```
App.jschat.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

const serverUrl = 'https://localhost:1234';

function ChatRoom({ roomId }) {
  const [message, setMessage] = useState('');

  // 暂时禁用 linter 以演示问题
  // eslint-disable-next-line react-hooks/exhaustive-deps
  const options = {
    serverUrl: serverUrl,
    roomId: roomId
  };

  useEffect(() => {
    const connection = createConnection(options);
    connection.connect();
    return () => connection.disconnect();
  }, [options]);

  return (
    <>
      <h1>欢迎来到 {roomId} 房间！</h1>
      <input value={message} onChange={e => setMessage(e.target.value)} />
    </>
  );
}

export default function App() {
  const [roomId, setRoomId] = useState('所有');
  return (
    <>
      <label>
        选择聊天室：
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="所有">所有</option>
          <option value="旅游">旅游</option>
          <option value="音乐">音乐</option>
        </select>
      </label>
      <hr />
      <ChatRoom roomId={roomId} />
    </>
  );
}
```
显示更多
在上面的沙箱中，输入仅更新 message 状态变量。从用户的角度来看，这不应该影响聊天连接。但是，每次更新 message 时，组件都会重新渲染。当组件重新渲染时，其中的代码会从头开始重新运行。
在每次重新渲染 ChatRoom 组件时，都会从头开始创建一个新的 options 对象。React 发现 options 对象与上次渲染期间创建的 options 对象是 不同的对象。这就是为什么它会重新同步 Effect（依赖于 options），并且会在你输入时重新连接聊天。
此问题仅影响对象和函数。在 JavaScript 中，每个新创建的对象和函数都被认为与其他所有对象和函数不同。即使他们的值相同也没关系！
```
// 第一次渲染const options1 = { serverUrl: 'https://localhost:1234', roomId: '音乐' };// 下一次渲染const options2 = { serverUrl: 'https://localhost:1234', roomId: '音乐' };// 这是 2 个不同的对象console.log(Object.is(options1, options2)); // false
```
将对象和函数作为依赖，会使 Effect 比你需要的更频繁地重新同步。
这就是为什么你应该尽可能避免将对象和函数作为 Effect 的依赖。所以，尝试将它们移到组件外部、Effect 内部，或从中提取原始值。
#### 将静态对象和函数移出组件
如果该对象不依赖于任何 props 和 state，你可以将该对象移到组件之外：
```
const options = {  serverUrl: 'https://localhost:1234',  roomId: '音乐'};function ChatRoom() {  const [message, setMessage] = useState('');  useEffect(() => {    const connection = createConnection(options);    connection.connect();    return () => connection.disconnect();  }, []); // ✅ 所有依赖已声明  // ...
```
这样，你向 linter 证明 它不是响应式的。它不会因为重新渲染而改变，所以它不是依赖。现在重新渲染 ChatRoom 不会导致 Effect 重新同步。
这也适用于函数场景：
```
function createOptions() {  return {    serverUrl: 'https://localhost:1234',    roomId: '音乐'  };}function ChatRoom() {  const [message, setMessage] = useState('');  useEffect(() => {    const options = createOptions();    const connection = createConnection(options);    connection.connect();    return () => connection.disconnect();  }, []); // ✅ 所有依赖已声明  // ...
```
由于 createOptions 是在组件外部声明的，因此它不是响应式值。这就是为什么它不需要在 Effect 的依赖中指定，以及为什么它永远不会导致 Effect 重新同步。
#### 将动态对象和函数移动到 Effect 中
如果对象依赖于一些可能因重新渲染而改变的响应式值，例如 roomId props，那么你不能将它放置于组件 外部。你可以在 Effect 内部 创建它：
```
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) {  const [message, setMessage] = useState('');  useEffect(() => {    const options = {      serverUrl: serverUrl,      roomId: roomId    };    const connection = createConnection(options);    connection.connect();    return () => connection.disconnect();  }, [roomId]); // ✅ 所有依赖已声明  // ...
```
现在 options 已在 Effect 中声明，它不再是 Effect 的依赖。相反，Effect 使用的唯一响应式值是 roomId。由于 roomId 不是对象或函数，你可以确定它不会 无意间 变不同。在 JavaScript 中，数字和字符串根据它们的内容进行比较：
```
// 第一次渲染const roomId1 = '音乐';// 下一次渲染const roomId2 = '音乐';// 这 2 个字符串是相同的console.log(Object.is(roomId1, roomId2)); // true
```
得益于此修复，当你编辑输入时，聊天将不再重新连接：
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
      <h1>欢迎来到 {roomId} 房间!</h1>
      <input value={message} onChange={e => setMessage(e.target.value)} />
    </>
  );
}

export default function App() {
  const [roomId, setRoomId] = useState('所有');
  return (
    <>
      <label>
        选择聊天室:{' '}
        <select
          value={roomId}
          onChange={e => setRoomId(e.target.value)}
        >
          <option value="所有">所有</option>
          <option value="旅游">旅游</option>
          <option value="音乐">音乐</option>
        </select>
      </label>
      <hr />
      <ChatRoom roomId={roomId} />
    </>
  );
}
```
显示更多
然而，当你更改 roomId 下拉列表时，它 确实 重新连接，正如你所期望的那样。
这也适用于函数的场景：
```
const serverUrl = 'https://localhost:1234';function ChatRoom({ roomId }) {  const [message, setMessage] = useState('');  useEffect(() => {    function createOptions() {      return {        serverUrl: serverUrl,        roomId: roomId      };    }    const options = createOptions();    const connection = createConnection(options);    connection.connect();    return () => connection.disconnect();  }, [roomId]); // ✅ 所有依赖已声明  // ...
```
你可以编写自己的函数来组织 Effect 中的逻辑。只要将这些函数声明在 Effect 内部，它们就不是响应式值，因此它们也不是 Effect 的依赖。
#### 从对象中读取原始值
有时，你可能会通过 props 接收到类型为对象的值：
```
function ChatRoom({ options }) {  const [message, setMessage] = useState('');  useEffect(() => {    const connection = createConnection(options);    connection.connect();    return () => connection.disconnect();  }, [options]); // ✅ 所有依赖已声明  // ...
```
这里的风险是父组件会在渲染过程中创建对象：
```
<ChatRoom  roomId={roomId}  options={{    serverUrl: serverUrl,    roomId: roomId  }}/>
```
这将导致 Effect 在每次父组件重新渲染时重新连接。要解决此问题，请从 Effect 外部 读取对象信息，并避免依赖对象和函数类型：
```
function ChatRoom({ options }) {  const [message, setMessage] = useState('');  const { roomId, serverUrl } = options;  useEffect(() => {    const connection = createConnection({      roomId: roomId,      serverUrl: serverUrl    });    connection.connect();    return () => connection.disconnect();  }, [roomId, serverUrl]); // ✅ 所有依赖已声明  // ...
```
逻辑有点重复（你从 Effect 外部的对象读取一些值，然后在 Effect 内部创建具有相同值的对象）。但这使得 Effect 实际 依赖的信息非常明确。如果对象被父组件无意中重新创建，聊天也不会重新连接。但是，如果 options.roomId 或 options.serverUrl 确实不同，聊天将重新连接。
#### 从函数中计算原始值
同样的方法也适用于函数。例如，假设父组件传递了一个函数：
```
<ChatRoom  roomId={roomId}  getOptions={() => {    return {      serverUrl: serverUrl,      roomId: roomId    };  }}/>
```
为避免使其成为依赖（并导致它在重新渲染时重新连接），请在 Effect 外部调用它。这为你提供了不是对象的 roomId 和 serverUrl 值，你可以从 Effect 中读取它们：
```
function ChatRoom({ getOptions }) {  const [message, setMessage] = useState('');  const { roomId, serverUrl } = getOptions();  useEffect(() => {    const connection = createConnection({      roomId: roomId,      serverUrl: serverUrl    });    connection.connect();    return () => connection.disconnect();  }, [roomId, serverUrl]); // ✅ 所有依赖已声明  // ...
```
这仅适用于 纯 函数，因为它们在渲染期间可以安全调用。如果函数是一个事件处理程序，但你不希望它的更改重新同步 Effect，将它包装到 Effect Event 中。
## 摘要
- 依赖应始终与代码匹配。
- 当你对依赖不满意时，你需要编辑的是代码。
- 抑制 linter 会导致非常混乱的错误，你应该始终避免它。
- 要移除依赖，你需要向 linter “证明”它不是必需的。
- 如果某些代码是为了响应特定交互，请将该代码移至事件处理的地方。
- 如果 Effect 的不同部分因不同原因需要重新运行，请将其拆分为多个 Effect。
- 如果你想根据以前的状态更新一些状态，传递一个更新函数。
- 如果你想读取最新值而不“反应”它，请从 Effect 中提取出一个 Effect Event。
- 在 JavaScript 中，如果对象和函数是在不同时间创建的，则它们被认为是不同的。
- 尽量避免对象和函数依赖。将它们移到组件外或 Effect 内。
## 尝试一些挑战
1. 修复重置 interval 2. 修复重新触发动画的问题 3. 修复聊天重新连接的问题 4. 再次修复聊天重新连接的问题
#### 第 1 个挑战 共 4 个挑战: 修复重置 interval
这个 Effect 设置了一个每秒运行的 interval。你已经注意到一些奇怪的事情：似乎每次 interval 都会被销毁并重新创建。修复代码，使 interval 不会被不断重新创建。
```
App.jsApp.jsReloadClearForkimport { useState, useEffect } from 'react';

export default function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log('✅ 创建定时器');
    const id = setInterval(() => {
      console.log('⏰ Interval');
      setCount(count + 1);
    }, 1000);
    return () => {
      console.log('❌ 清除定时器');
      clearInterval(id);
    };
  }, [count]);

  return <h1>计数器: {count}</h1>
}
```
显示更多 展示提示 展示答案下一个挑战
译注：
 [1] 在创建 onTick 函数时，由于闭包的缘故，setCount(count + increment) 捕获的是创建时 count 和 increment 值。由于这里的“说谎”，每次重新渲染时新创建的 onTick 函数不能替换掉 Effect 里旧 onTick 函数，于是最终的效果就是 setCount(0 + 1)